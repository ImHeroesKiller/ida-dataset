"""Entity extraction + canonical resolution + knowledge_score.

Flow:
  Knowledge Atom → mention → Canonical match → reuse OR create

Never duplicates canonical entities. Preserves aliases.
No relationship extraction (Commit 3).
No dataset row writes.
"""

from __future__ import annotations

import hashlib
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

from automation.knowledge.entity_store import (
    find_by_canonical,
    load_all_entities,
    load_indexes,
    normalize_name,
    upsert_entities_batch,
)
from automation.knowledge.models import EntityStatus, GraphEntity, KnowledgeAtom
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

ENTITY_EXTRACTOR_VERSION = "entity-extract-1.0.0"

# --- mention patterns (grounded surface forms only) ---

_COMPANY = re.compile(
    r"\b((?:PT\.?\s+|CV\.?\s+)?[A-Z][A-Za-z0-9&.\'\-]+(?:\s+[A-Z][A-Za-z0-9&.\'\-]+){0,5}"
    r"(?:\s+(?:Tbk\.?|Inc\.?|Corp\.?|Corporation|Ltd\.?|LLC|GmbH|Persero))?)\b"
)
_ISO = re.compile(r"\bISO\s?\d{3,5}(?::\d{4})?\b", re.I)
_NIST = re.compile(r"\bNIST(?:\s+[A-Za-z0-9\-]+)?\b")
_FRAMEWORK = re.compile(
    r"\b((?:COBIT|ITIL|TOGAF|PMBOK|SCRUM|Kanban|Six Sigma|Lean Six Sigma|"
    r"Balanced Scorecard|OKR|KPI Framework)\b)",
    re.I,
)
_COUNTRY = re.compile(
    r"\b(Indonesia|Singapore|Malaysia|Thailand|Vietnam|Philippines|"
    r"United States|United Kingdom|Japan|China|India|Australia|"
    r"Germany|France|Netherlands)\b",
    re.I,
)
_REGULATOR = re.compile(
    r"\b(OJK|Bank Indonesia|BI|LKPP|Kemenkeu|Bappenas|BSN|Kominfo|"
    r"SEC|FDA|EMA|GDPR|PDPA)\b"
)
_ROLE = re.compile(
    r"\b(Chief Executive Officer|CEO|Chief Financial Officer|CFO|"
    r"Chief Technology Officer|CTO|Chief Information Officer|CIO|"
    r"Managing Director|General Manager|Plant Manager|HR Director|"
    r"IT Director|Procurement Manager|Direktur|Komisaris)\b"
)
_TECH = re.compile(
    r"\b(ERP|CRM|SAP|Oracle|Salesforce|Kubernetes|Docker|Python|"
    r"Machine Learning|Artificial Intelligence|AI|Cloud Computing|"
    r"Cybersecurity|Blockchain|IoT|RPA)\b",
    re.I,
)


@lru_cache(maxsize=2)
def _load_kg_config(config_path: str) -> dict[str, Any]:
    path = Path(config_path)
    if not path.exists():
        return {}
    try:
        from automation.lib.simple_yaml import load_simple_yaml

        data = load_simple_yaml(path.read_text(encoding="utf-8")) or {}
        return data if isinstance(data, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


def knowledge_score_weights(repo_root: Optional[Path] = None) -> dict[str, float]:
    root = repo_root or find_repo_root()
    cfg = _load_kg_config(str((root / "automation/config/knowledge_graph.yaml").resolve()))
    w = (cfg.get("knowledge_score") or {}) if isinstance(cfg, dict) else {}
    if not isinstance(w, dict):
        w = {}
    weights = {
        "confidence": float(w.get("confidence", 0.35)),
        "richness": float(w.get("richness", 0.25)),
        "completeness": float(w.get("completeness", 0.20)),
        "source_quality": float(w.get("source_quality", 0.15)),
        "relationship_potential": float(w.get("relationship_potential", 0.05)),
    }
    total = sum(weights.values()) or 1.0
    return {k: v / total for k, v in weights.items()}


def compute_knowledge_score(
    *,
    confidence: float,
    alias_count: int = 0,
    source_count: int = 1,
    atom_count: int = 1,
    has_type: bool = True,
    trust_hint: float = 0.7,
    relationship_potential: float = 0.0,
    repo_root: Optional[Path] = None,
) -> float:
    """Weighted knowledge_score — weights from knowledge_graph.yaml."""
    w = knowledge_score_weights(repo_root)
    conf = max(0.0, min(1.0, float(confidence)))
    richness = min(1.0, 0.3 + 0.15 * min(alias_count, 4) + 0.1 * min(atom_count, 5))
    completeness = min(1.0, (0.5 if has_type else 0.2) + 0.1 * min(source_count, 5))
    source_quality = max(0.0, min(1.0, float(trust_hint)))
    rel_pot = max(0.0, min(1.0, float(relationship_potential)))
    score = (
        w["confidence"] * conf
        + w["richness"] * richness
        + w["completeness"] * completeness
        + w["source_quality"] * source_quality
        + w["relationship_potential"] * rel_pot
    )
    return round(max(0.0, min(1.0, score)), 4)


def _entity_id(entity_type: str, canonical_name: str) -> str:
    key = f"{entity_type}|{normalize_name(canonical_name)}"
    h = hashlib.sha1(key.encode("utf-8")).hexdigest()[:12].upper()
    return f"ENT-{h}"


def _dedupe_aliases(canonical: str, aliases: Iterable[str]) -> list[str]:
    seen = {normalize_name(canonical)}
    out: list[str] = []
    for a in aliases:
        a = (a or "").strip()
        if not a:
            continue
        k = normalize_name(a)
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(a)
    return out


def extract_mentions_from_atom(atom: KnowledgeAtom) -> list[dict[str, Any]]:
    """Surface entity mentions from one atom (no store access)."""
    text = atom.original_text or atom.text or ""
    mentions: list[dict[str, Any]] = []
    conf = float(atom.confidence or 0.7)

    def add(
        name: str,
        entity_type: str,
        confidence: float,
        alias_extra: Optional[list[str]] = None,
    ) -> None:
        name = (name or "").strip(" ,.;:()[]")
        if len(name) < 2 or len(name) > 120:
            return
        if name.lower() in {
            "the",
            "and",
            "for",
            "with",
            "from",
            "this",
            "that",
            "title",
        }:
            return
        mentions.append(
            {
                "name": name,
                "entity_type": entity_type,
                "confidence": confidence,
                "aliases": list(alias_extra or []),
                "atom_id": atom.atom_id,
                "document_id": atom.document_id,
                "source": atom.source,
            }
        )

    try:
        from automation.acquisition.normalize import INDUSTRY_ALIASES as _IA

        lower = text.lower()
        for alias, canonical in _IA.items():
            if alias in lower:
                add(canonical, "Industry", min(0.9, conf + 0.05), [alias])
    except Exception:  # noqa: BLE001
        pass

    for m in _COUNTRY.finditer(text):
        add(m.group(1).title() if m.group(1).islower() else m.group(1), "Country", conf)

    for m in _REGULATOR.finditer(text):
        add(m.group(1), "Regulation", conf)

    for m in _ISO.finditer(text):
        add(m.group(0).upper().replace("  ", " "), "Standard", min(0.92, conf + 0.1))

    for m in _NIST.finditer(text):
        add(m.group(0).strip(), "Framework", min(0.9, conf + 0.08))

    for m in _FRAMEWORK.finditer(text):
        add(m.group(1).strip(), "Framework", min(0.88, conf + 0.05))

    for m in _TECH.finditer(text):
        add(m.group(1).strip(), "Technology", conf)

    for m in _ROLE.finditer(text):
        add(m.group(1).strip(), "Job Title", conf)

    # Companies — only Title-Case multi-token or PT/CV forms
    for m in _COMPANY.finditer(text):
        name = m.group(1).strip()
        if len(name.split()) < 2 and not re.match(r"^(PT|CV)\b", name, re.I):
            continue
        if name.lower() in {"united states", "united kingdom"}:
            continue
        add(name, "Company", conf * 0.95)

    return mentions


def resolve_mention(
    mention: Mapping[str, Any],
    *,
    entities: dict[str, GraphEntity],
    indexes: dict[str, dict[str, Any]],
    session_id: str = "",
    repo_root: Optional[Path] = None,
) -> tuple[GraphEntity, bool]:
    """Resolve mention → existing canonical entity or create new.

    Returns (entity, created).
    """
    name = str(mention.get("name") or "").strip()
    etype = str(mention.get("entity_type") or "Entity")
    conf = float(mention.get("confidence") or 0.7)
    aliases_in = list(mention.get("aliases") or [])
    atom_id = str(mention.get("atom_id") or "")
    document_id = str(mention.get("document_id") or "")
    source = str(mention.get("source") or "")
    now = utc_now_iso()

    existing_id = find_by_canonical(name, indexes=indexes, repo_root=repo_root)
    # Also try each alias
    if not existing_id:
        for a in aliases_in:
            existing_id = find_by_canonical(a, indexes=indexes, repo_root=repo_root)
            if existing_id:
                break

    if existing_id and existing_id in entities:
        ent = entities[existing_id]
        # Prefer ACTIVE; follow merge pointer
        if ent.merged_into and ent.merged_into in entities:
            ent = entities[ent.merged_into]
        # Reuse — append alias, sources, atoms
        if name and normalize_name(name) != normalize_name(ent.canonical_name):
            ent.aliases = _dedupe_aliases(ent.canonical_name, list(ent.aliases) + [name] + aliases_in)
        else:
            ent.aliases = _dedupe_aliases(ent.canonical_name, list(ent.aliases) + aliases_in)
        if source and source not in ent.sources:
            ent.sources.append(source)
        if atom_id and atom_id not in ent.atom_ids:
            ent.atom_ids.append(atom_id)
        if document_id and document_id not in ent.document_ids:
            ent.document_ids.append(document_id)
        ent.confidence = max(ent.confidence, conf)
        ent.last_seen = now
        ent.updated_at = now
        ent.updated_session = session_id or ent.updated_session
        ent.knowledge_score = compute_knowledge_score(
            confidence=ent.confidence,
            alias_count=len(ent.aliases),
            source_count=len(ent.sources),
            atom_count=len(ent.atom_ids),
            has_type=bool(ent.entity_type),
            trust_hint=ent.confidence,
            repo_root=repo_root,
        )
        entities[ent.entity_id] = ent
        # Refresh index keys for new aliases
        ckey = normalize_name(ent.canonical_name)
        if ckey:
            indexes.setdefault("canonical", {})[ckey] = ent.entity_id
        for a in ent.aliases:
            akey = normalize_name(a)
            if akey:
                indexes.setdefault("alias", {})[akey] = ent.entity_id
        if document_id:
            indexes.setdefault("document", {}).setdefault(document_id, [])
            if ent.entity_id not in indexes["document"][document_id]:
                indexes["document"][document_id].append(ent.entity_id)
        if atom_id:
            indexes.setdefault("atom", {}).setdefault(atom_id, [])
            if ent.entity_id not in indexes["atom"][atom_id]:
                indexes["atom"][atom_id].append(ent.entity_id)
        if source:
            indexes.setdefault("source", {}).setdefault(source, [])
            if ent.entity_id not in indexes["source"][source]:
                indexes["source"][source].append(ent.entity_id)
        return ent, False

    # Create new canonical entity
    eid = _entity_id(etype, name)
    # Collision: same id already exists (same type+name)
    if eid in entities:
        return resolve_mention(
            {**dict(mention), "name": entities[eid].canonical_name},
            entities=entities,
            indexes=indexes,
            session_id=session_id,
            repo_root=repo_root,
        )

    aliases = _dedupe_aliases(name, aliases_in)
    kscore = compute_knowledge_score(
        confidence=conf,
        alias_count=len(aliases),
        source_count=1 if source else 0,
        atom_count=1 if atom_id else 0,
        has_type=True,
        trust_hint=conf,
        repo_root=repo_root,
    )
    ent = GraphEntity(
        entity_id=eid,
        entity_type=etype,
        canonical_name=name,
        aliases=aliases,
        knowledge_score=kscore,
        confidence=conf,
        first_seen=now,
        last_seen=now,
        sources=[source] if source else [],
        atom_ids=[atom_id] if atom_id else [],
        document_ids=[document_id] if document_id else [],
        status=EntityStatus.ACTIVE.value,
        provenance={
            "extractor_version": ENTITY_EXTRACTOR_VERSION,
            "created_from_atom": atom_id,
        },
        created_session=session_id,
        updated_session=session_id,
        created_at=now,
        updated_at=now,
    )
    entities[eid] = ent
    ckey = normalize_name(name)
    if ckey:
        indexes.setdefault("canonical", {})[ckey] = eid
    for a in aliases:
        akey = normalize_name(a)
        if akey:
            indexes.setdefault("alias", {})[akey] = eid
    if document_id:
        indexes.setdefault("document", {}).setdefault(document_id, [])
        indexes["document"][document_id].append(eid)
    if atom_id:
        indexes.setdefault("atom", {}).setdefault(atom_id, [])
        indexes["atom"][atom_id].append(eid)
    if source:
        indexes.setdefault("source", {}).setdefault(source, [])
        indexes["source"][source].append(eid)
    return ent, True


def extract_and_resolve_atoms(
    atoms: Sequence[KnowledgeAtom],
    *,
    session_id: str = "",
    repo_root: Optional[Path] = None,
    persist: bool = True,
) -> dict[str, Any]:
    """Extract entities from atoms, resolve to canonical store."""
    root = repo_root or find_repo_root()
    entities = load_all_entities(repo_root=root)
    indexes = load_indexes(repo_root=root)
    created = 0
    reused = 0
    mentions_total = 0
    touched_ids: set[str] = set()

    for atom in atoms:
        st = str(getattr(atom, "status", "ACTIVE") or "ACTIVE")
        if st not in ("ACTIVE", EntityStatus.ACTIVE.value):
            continue
        for mention in extract_mentions_from_atom(atom):
            mentions_total += 1
            ent, was_created = resolve_mention(
                mention,
                entities=entities,
                indexes=indexes,
                session_id=session_id,
                repo_root=root,
            )
            touched_ids.add(ent.entity_id)
            if was_created:
                created += 1
            else:
                reused += 1

    if persist and touched_ids:
        batch = [entities[i] for i in touched_ids if i in entities]
        upsert_entities_batch(batch, repo_root=root)

    return {
        "mentions": mentions_total,
        "created": created,
        "reused": reused,
        "entities_touched": len(touched_ids),
        "entity_ids": sorted(touched_ids),
        "store_entity_count": len(entities),
    }


def process_document_entities(
    doc: Mapping[str, Any],
    *,
    session_id: str = "",
    repo_root: Optional[Path] = None,
    persist_atoms: bool = True,
) -> dict[str, Any]:
    """Atomize document (if needed) + extract/resolve entities. No relationships."""
    from automation.knowledge.atom_store import (
        atomize_and_persist_document,
        load_atoms_for_document,
    )
    from automation.knowledge.atoms import atomize_document

    root = repo_root or find_repo_root()
    document_id = str(doc.get("document_id") or "")
    if persist_atoms:
        atom_summary = atomize_and_persist_document(dict(doc), repo_root=root)
        atoms = load_atoms_for_document(document_id, repo_root=root)
    else:
        atoms = atomize_document(doc)
        atom_summary = {"atom_count": len(atoms)}

    entity_summary = extract_and_resolve_atoms(
        atoms, session_id=session_id, repo_root=root, persist=True
    )
    return {
        "document_id": document_id,
        "atoms": atom_summary,
        "entities": entity_summary,
    }
