"""Relationship Intelligence Layer — extract, resolve, query.

No related_to unless unavoidable.
No dataset manufacturing. No scheduler hooks.

Taxonomy families:
  Business · Organization · Market · Technology · Governance · Geography · Supply Chain
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

from automation.knowledge.entity_store import (
    load_all_entities,
    load_indexes as load_entity_indexes,
    normalize_name,
)
from automation.knowledge.models import (
    GraphEntity,
    GraphRelationship,
    KnowledgeAtom,
    RelationshipStatus,
)
from automation.knowledge.relationship_store import (
    edge_key,
    get_relationship,
    load_all_relationships,
    load_edge_indexes,
    upsert_relationships_batch,
)
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

REL_EXTRACTOR_VERSION = "relationship-extract-1.0.0"

# ---------------------------------------------------------------------------
# Taxonomy (no related_to)
# ---------------------------------------------------------------------------

RELATIONSHIP_TAXONOMY: dict[str, list[str]] = {
    "Business": ["provides", "offers", "manufactures", "distributes"],
    "Organization": ["owns", "managed_by", "subsidiary_of", "founded_by"],
    "Market": ["targets", "serves", "competes_with"],
    "Technology": ["uses", "depends_on", "integrates_with", "replaces", "implements"],
    "Governance": ["regulated_by", "certified_by", "audited_by"],
    "Geography": ["located_in", "operates_in", "headquartered_in"],
    "Supply Chain": ["supplied_by", "partner_of", "purchased_from"],
}

ALL_RELATIONSHIP_TYPES: set[str] = {
    t for types in RELATIONSHIP_TAXONOMY.values() for t in types
}

# Verb cues → predicate
_VERB_CUES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\b(provides?|providing|provide)\b", re.I), "provides"),
    (re.compile(r"\b(offers?|offering)\b", re.I), "offers"),
    (re.compile(r"\b(manufactures?|produces?|builds?)\b", re.I), "manufactures"),
    (re.compile(r"\b(distributes?|distribution)\b", re.I), "distributes"),
    (re.compile(r"\b(owns?|ownership|owned by)\b", re.I), "owns"),
    (re.compile(r"\b(managed by|manages|management of)\b", re.I), "managed_by"),
    (re.compile(r"\b(subsidiary|parent company)\b", re.I), "subsidiary_of"),
    (re.compile(r"\b(founded by|founder)\b", re.I), "founded_by"),
    (re.compile(r"\b(targets?|targeting|aimed at)\b", re.I), "targets"),
    (re.compile(r"\b(serves?|serving|customers? in)\b", re.I), "serves"),
    (re.compile(r"\b(competes?|competition|versus| vs\.? )\b", re.I), "competes_with"),
    (re.compile(r"\b(uses?|using|utiliz|adopts?|adopted)\b", re.I), "uses"),
    (re.compile(r"\b(depends? on|dependent on|dependency)\b", re.I), "depends_on"),
    (re.compile(r"\b(integrat|interop|compatible with)\b", re.I), "integrates_with"),
    (re.compile(r"\b(replaces?|supersedes?|migration from)\b", re.I), "replaces"),
    (re.compile(r"\b(implements?|implementation of)\b", re.I), "implements"),
    (re.compile(r"\b(regulat|compliance with|subject to)\b", re.I), "regulated_by"),
    (re.compile(r"\b(certified|certification|accredited)\b", re.I), "certified_by"),
    (re.compile(r"\b(audit(ed)? by|auditor)\b", re.I), "audited_by"),
    (re.compile(r"\b(located in|based in|headquartered)\b", re.I), "located_in"),
    (re.compile(r"\b(operates? in|operating in)\b", re.I), "operates_in"),
    (re.compile(r"\b(headquarters|hq in)\b", re.I), "headquartered_in"),
    (re.compile(r"\b(supplied by|supplier)\b", re.I), "supplied_by"),
    (re.compile(r"\b(partner(ed)? with|partnership)\b", re.I), "partner_of"),
    (re.compile(r"\b(purchased from|bought from|procurement from)\b", re.I), "purchased_from"),
]

# Default predicate when type pair co-occurs without verb (conservative)
_TYPE_PAIR_DEFAULT: dict[tuple[str, str], str] = {
    ("Company", "Industry"): "targets",
    ("Company", "Country"): "located_in",
    ("Company", "Technology"): "uses",
    ("Company", "Regulation"): "regulated_by",
    ("Company", "Standard"): "certified_by",
    ("Company", "Framework"): "implements",
    # Company–Company only via compete/partner verbs (no default)
    ("Technology", "Technology"): "integrates_with",
    ("Framework", "Technology"): "depends_on",
    ("Company", "Job Title"): "managed_by",
    ("Industry", "Country"): "located_in",
}

# Map "requires" (user example) onto taxonomy member
_PREDICATE_ALIASES = {
    "requires": "depends_on",
    "headquartered": "headquartered_in",
}


def taxonomy_catalog() -> dict[str, list[str]]:
    return {k: list(v) for k, v in RELATIONSHIP_TAXONOMY.items()}


def _relationship_id(source: str, rel_type: str, target: str) -> str:
    key = edge_key(source, rel_type, target)
    h = hashlib.sha1(key.encode("utf-8")).hexdigest()[:12].upper()
    return f"REL-{h}"


def _normalize_predicate(pred: str) -> str:
    p = (pred or "").strip().lower().replace(" ", "_")
    p = _PREDICATE_ALIASES.get(p, p)
    if p not in ALL_RELATIONSHIP_TYPES:
        return ""
    return p


def _detect_verbs(text: str) -> list[str]:
    found: list[str] = []
    for pattern, pred in _VERB_CUES:
        if pattern.search(text or ""):
            np = _normalize_predicate(pred)
            if np and np not in found:
                found.append(np)
    return found


def _entity_surface_forms(ent: GraphEntity) -> list[str]:
    forms = [ent.canonical_name] + list(ent.aliases or [])
    return [f for f in forms if f and len(f) >= 2]


def _entity_in_text(ent: GraphEntity, text_lower: str) -> bool:
    for form in _entity_surface_forms(ent):
        key = form.lower()
        if len(key) < 3:
            # short forms: word boundary
            if re.search(rf"\b{re.escape(key)}\b", text_lower):
                return True
        elif key in text_lower:
            return True
    return False


# Verb → allowed (source_type, target_type) pairs (empty set = any when type-pair default exists)
_VERB_TYPE_ALLOW: dict[str, set[tuple[str, str]]] = {
    "targets": {("Company", "Industry"), ("Product", "Industry")},
    "serves": {("Company", "Industry")},
    "uses": {("Company", "Technology"), ("Company", "Framework"), ("Industry", "Technology")},
    "implements": {("Company", "Framework"), ("Company", "Standard"), ("Company", "Technology")},
    "provides": {("Company", "Technology"), ("Company", "Industry")},
    "offers": {("Company", "Technology"), ("Company", "Industry")},
    "manufactures": {("Company", "Technology"), ("Company", "Industry")},
    "distributes": {("Company", "Technology"), ("Company", "Industry")},
    "regulated_by": {("Company", "Regulation"), ("Industry", "Regulation")},
    "certified_by": {("Company", "Standard"), ("Company", "Framework")},
    "audited_by": {("Company", "Company"), ("Company", "Regulation")},
    "managed_by": {("Company", "Job Title")},
    "located_in": {("Company", "Country"), ("Industry", "Country"), ("Technology", "Country")},
    "operates_in": {("Company", "Country"), ("Industry", "Country")},
    "headquartered_in": {("Company", "Country")},
    "competes_with": {("Company", "Company")},
    "integrates_with": {("Technology", "Technology"), ("Framework", "Technology")},
    "depends_on": {("Technology", "Technology"), ("Framework", "Technology"), ("Company", "Technology")},
    "replaces": {("Technology", "Technology")},
    "partner_of": {("Company", "Company")},
    "purchased_from": {("Company", "Company")},
    "supplied_by": {("Company", "Company")},
    "owns": {("Company", "Company"), ("Company", "Technology")},
    "subsidiary_of": {("Company", "Company")},
    "founded_by": {("Company", "Job Title")},
}


def _pair_predicate(
    src_type: str,
    tgt_type: str,
    verbs: list[str],
    text_lower: str,
) -> Optional[str]:
    """Choose taxonomy predicate for a directed type pair."""
    pair = (src_type, tgt_type)

    # Verb-driven with type constraints (most specific first)
    for v in verbs:
        allowed = _VERB_TYPE_ALLOW.get(v)
        if allowed is not None and pair in allowed:
            return v
        # Geography verbs also accept headquartered language on Company→Country
        if v in {"located_in", "operates_in", "headquartered_in"} and pair == (
            "Company",
            "Country",
        ):
            return v

    # Type-pair default (conservative)
    default = _TYPE_PAIR_DEFAULT.get(pair)
    if not default:
        return None
    default = _normalize_predicate(default) or default
    if default == "competes_with":
        if not any(x in text_lower for x in ("compet", "versus", " vs ", "rival")):
            return None
    if default not in ALL_RELATIONSHIP_TYPES:
        return None
    # If a more specific verb exists for another reading, still allow default
    return default


def edge_knowledge_score(
    *,
    confidence: float,
    evidence_count: int,
    source_count: int = 1,
) -> float:
    conf = max(0.0, min(1.0, float(confidence)))
    evidence = min(1.0, 0.4 + 0.15 * min(int(evidence_count), 4))
    sources = min(1.0, 0.5 + 0.1 * min(int(source_count), 5))
    return round(0.5 * conf + 0.3 * evidence + 0.2 * sources, 4)


def extract_relationship_candidates(
    atom: KnowledgeAtom,
    entities: Sequence[GraphEntity],
) -> list[dict[str, Any]]:
    """Extract directed relationship candidates from one atom + known entities."""
    text = atom.original_text or atom.text or ""
    if not text or len(entities) < 2:
        return []
    text_lower = text.lower()
    present = [e for e in entities if e.status in ("ACTIVE", "") and _entity_in_text(e, text_lower)]
    if len(present) < 2:
        return []

    verbs = _detect_verbs(text)
    candidates: list[dict[str, Any]] = []
    # Pair entities that co-occur (limit fan-out; prefer non-Company diversity)
    def _rank(e: GraphEntity) -> int:
        return 0 if e.entity_type == "Company" else 1

    present = sorted(present, key=_rank, reverse=True)[:16]
    for i, a in enumerate(present):
        for b in present[i + 1 :]:
            if a.entity_id == b.entity_id:
                continue
            if a.entity_type == "Company" and b.entity_type == "Company":
                if not any(
                    v in verbs
                    for v in (
                        "competes_with",
                        "partner_of",
                        "subsidiary_of",
                        "owns",
                    )
                ):
                    continue
            for src, tgt in ((a, b), (b, a)):
                pred = _pair_predicate(
                    src.entity_type, tgt.entity_type, verbs, text_lower
                )
                if not pred:
                    continue
                conf = float(atom.confidence or 0.7)
                if pred in verbs:
                    conf = min(0.95, conf + 0.12)
                else:
                    conf = conf * 0.85
                candidates.append(
                    {
                        "source_entity": src.entity_id,
                        "target_entity": tgt.entity_id,
                        "relationship_type": pred,
                        "confidence": conf,
                        "atom_id": atom.atom_id,
                        "document_id": atom.document_id,
                        "source": atom.source,
                    }
                )
    # Dedupe candidates by edge key within atom (keep max conf)
    best: dict[str, dict[str, Any]] = {}
    for c in candidates:
        k = edge_key(c["source_entity"], c["relationship_type"], c["target_entity"])
        if k not in best or c["confidence"] > best[k]["confidence"]:
            best[k] = c
    return list(best.values())


def resolve_relationship(
    candidate: Mapping[str, Any],
    *,
    relationships: dict[str, GraphRelationship],
    edge_index: dict[str, str],
    session_id: str = "",
) -> tuple[GraphRelationship, bool]:
    """Merge into existing edge or create new. Returns (rel, created)."""
    src = str(candidate.get("source_entity") or "")
    tgt = str(candidate.get("target_entity") or "")
    rtype = _normalize_predicate(str(candidate.get("relationship_type") or ""))
    if not src or not tgt or not rtype or src == tgt:
        raise ValueError("invalid_relationship_candidate")

    conf = float(candidate.get("confidence") or 0.7)
    atom_id = str(candidate.get("atom_id") or "")
    document_id = str(candidate.get("document_id") or "")
    source = str(candidate.get("source") or "")
    now = utc_now_iso()
    key = edge_key(src, rtype, tgt)
    existing_id = edge_index.get(key)

    if existing_id and existing_id in relationships:
        rel = relationships[existing_id]
        if rel.merged_into and rel.merged_into in relationships:
            rel = relationships[rel.merged_into]
        # Merge evidence
        rel.evidence_count = int(rel.evidence_count or 1) + 1
        # Confidence grows with diminishing returns
        rel.confidence = round(
            min(0.99, max(rel.confidence, conf) + 0.03 * min(rel.evidence_count, 5)),
            4,
        )
        if atom_id and atom_id not in rel.atom_ids:
            rel.atom_ids.append(atom_id)
        if atom_id:
            rel.atom_id = rel.atom_id or atom_id
        if source and source not in rel.sources:
            rel.sources.append(source)
        if document_id and document_id not in rel.document_ids:
            rel.document_ids.append(document_id)
        # Append provenance trail
        prov = dict(rel.provenance or {})
        trail = list(prov.get("evidence") or [])
        trail.append(
            {
                "atom_id": atom_id,
                "session_id": session_id,
                "confidence": conf,
                "at": now,
            }
        )
        prov["evidence"] = trail[-20:]
        prov["extractor_version"] = REL_EXTRACTOR_VERSION
        rel.provenance = prov
        rel.last_seen = now
        rel.timestamp = now
        rel.session_id = session_id or rel.session_id
        rel.knowledge_score = edge_knowledge_score(
            confidence=rel.confidence,
            evidence_count=rel.evidence_count,
            source_count=len(rel.sources) or 1,
        )
        relationships[rel.relationship_id] = rel
        return rel, False

    rid = _relationship_id(src, rtype, tgt)
    if rid in relationships:
        # Race: treat as update
        edge_index[key] = rid
        return resolve_relationship(
            candidate,
            relationships=relationships,
            edge_index=edge_index,
            session_id=session_id,
        )

    rel = GraphRelationship(
        relationship_id=rid,
        source_entity=src,
        target_entity=tgt,
        relationship_type=rtype,
        confidence=conf,
        knowledge_score=edge_knowledge_score(
            confidence=conf, evidence_count=1, source_count=1 if source else 0
        ),
        provenance={
            "extractor_version": REL_EXTRACTOR_VERSION,
            "evidence": [
                {
                    "atom_id": atom_id,
                    "session_id": session_id,
                    "confidence": conf,
                    "at": now,
                }
            ],
        },
        atom_id=atom_id,
        atom_ids=[atom_id] if atom_id else [],
        session_id=session_id,
        first_seen=now,
        last_seen=now,
        status=RelationshipStatus.ACTIVE.value,
        evidence_count=1,
        sources=[source] if source else [],
        document_ids=[document_id] if document_id else [],
        timestamp=now,
    )
    relationships[rid] = rel
    edge_index[key] = rid
    return rel, True


def extract_and_resolve_relationships(
    atoms: Sequence[KnowledgeAtom],
    *,
    session_id: str = "",
    repo_root: Optional[Path] = None,
    persist: bool = True,
    entity_ids: Optional[Sequence[str]] = None,
) -> dict[str, Any]:
    """Extract relationships from atoms using canonical entities; merge duplicates."""
    root = repo_root or find_repo_root()
    entities_map = load_all_entities(repo_root=root)
    if entity_ids:
        entity_list = [entities_map[i] for i in entity_ids if i in entities_map]
    else:
        # Prefer entities linked to these atoms
        ent_idx = load_entity_indexes(repo_root=root)
        linked: set[str] = set()
        for atom in atoms:
            for eid in ent_idx.get("atom", {}).get(atom.atom_id) or []:
                linked.add(eid)
        if linked:
            entity_list = [entities_map[i] for i in linked if i in entities_map]
        else:
            entity_list = list(entities_map.values())

    relationships = load_all_relationships(repo_root=root)
    edge_idx = dict(load_edge_indexes(repo_root=root).get("edge_key") or {})

    created = 0
    merged = 0
    candidates_n = 0
    touched: set[str] = set()

    for atom in atoms:
        st = str(getattr(atom, "status", "ACTIVE") or "ACTIVE")
        if st not in ("ACTIVE",):
            continue
        for cand in extract_relationship_candidates(atom, entity_list):
            candidates_n += 1
            try:
                rel, was_created = resolve_relationship(
                    cand,
                    relationships=relationships,
                    edge_index=edge_idx,
                    session_id=session_id,
                )
            except ValueError:
                continue
            touched.add(rel.relationship_id)
            if was_created:
                created += 1
            else:
                merged += 1

    if persist and touched:
        batch = [relationships[i] for i in touched if i in relationships]
        upsert_relationships_batch(batch, repo_root=root)

    return {
        "candidates": candidates_n,
        "created": created,
        "merged": merged,
        "relationships_touched": len(touched),
        "relationship_ids": sorted(touched),
        "store_relationship_count": len(relationships),
    }


def process_document_relationships(
    doc: Mapping[str, Any],
    *,
    session_id: str = "",
    repo_root: Optional[Path] = None,
) -> dict[str, Any]:
    """Ensure entities exist, then extract relationships for one document."""
    from automation.knowledge.atom_store import load_atoms_for_document
    from automation.knowledge.entities import process_document_entities

    root = repo_root or find_repo_root()
    ent_summary = process_document_entities(
        doc, session_id=session_id, repo_root=root, persist_atoms=True
    )
    document_id = str(doc.get("document_id") or "")
    atoms = load_atoms_for_document(document_id, repo_root=root)
    rel_summary = extract_and_resolve_relationships(
        atoms,
        session_id=session_id,
        repo_root=root,
        persist=True,
        entity_ids=ent_summary.get("entities", {}).get("entity_ids"),
    )
    return {
        "document_id": document_id,
        "entities": ent_summary.get("entities"),
        "relationships": rel_summary,
    }


# ---------------------------------------------------------------------------
# Query API (no reasoning)
# ---------------------------------------------------------------------------


def find_relationship(
    source_entity: str,
    relationship_type: str,
    target_entity: str,
    *,
    repo_root: Optional[Path] = None,
) -> Optional[GraphRelationship]:
    """Lookup edge by (source, type, target)."""
    root = repo_root or find_repo_root()
    idx = load_edge_indexes(repo_root=root)
    rtype = _normalize_predicate(relationship_type) or relationship_type
    rid = (idx.get("edge_key") or {}).get(edge_key(source_entity, rtype, target_entity))
    if not rid:
        return None
    return get_relationship(rid, repo_root=root)


def outgoing(
    entity_id: str,
    *,
    repo_root: Optional[Path] = None,
) -> list[GraphRelationship]:
    root = repo_root or find_repo_root()
    idx = load_edge_indexes(repo_root=root)
    rels = load_all_relationships(repo_root=root)
    ids = idx.get("outgoing", {}).get(entity_id) or []
    return [rels[i] for i in ids if i in rels and rels[i].status == "ACTIVE"]


def incoming(
    entity_id: str,
    *,
    repo_root: Optional[Path] = None,
) -> list[GraphRelationship]:
    root = repo_root or find_repo_root()
    idx = load_edge_indexes(repo_root=root)
    rels = load_all_relationships(repo_root=root)
    ids = idx.get("incoming", {}).get(entity_id) or []
    return [rels[i] for i in ids if i in rels and rels[i].status == "ACTIVE"]


def neighbors(
    entity_id: str,
    *,
    repo_root: Optional[Path] = None,
) -> dict[str, Any]:
    """Adjacent entity ids via incoming + outgoing ACTIVE edges."""
    out_edges = outgoing(entity_id, repo_root=repo_root)
    in_edges = incoming(entity_id, repo_root=repo_root)
    out_ids = sorted({e.target_entity for e in out_edges})
    in_ids = sorted({e.source_entity for e in in_edges})
    return {
        "entity_id": entity_id,
        "outgoing_entity_ids": out_ids,
        "incoming_entity_ids": in_ids,
        "neighbor_entity_ids": sorted(set(out_ids) | set(in_ids)),
        "degree": len(set(out_ids) | set(in_ids)),
        "out_degree": len(out_edges),
        "in_degree": len(in_edges),
    }


def relationship_stats(*, repo_root: Optional[Path] = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    rels = load_all_relationships(repo_root=root)
    idx = load_edge_indexes(repo_root=root)
    by_type: dict[str, int] = {}
    by_status: dict[str, int] = {}
    degrees: dict[str, int] = {}
    for r in rels.values():
        by_type[r.relationship_type] = by_type.get(r.relationship_type, 0) + 1
        by_status[r.status] = by_status.get(r.status, 0) + 1
        if r.status != "ACTIVE":
            continue
        degrees[r.source_entity] = degrees.get(r.source_entity, 0) + 1
        degrees[r.target_entity] = degrees.get(r.target_entity, 0) + 1
    avg_degree = (sum(degrees.values()) / len(degrees)) if degrees else 0.0
    top = sorted(degrees.items(), key=lambda x: -x[1])[:10]
    entities = load_all_entities(repo_root=root)
    top_named = [
        {
            "entity_id": eid,
            "canonical_name": entities[eid].canonical_name if eid in entities else eid,
            "degree": deg,
        }
        for eid, deg in top
    ]
    return {
        "relationship_count": len(rels),
        "active_count": by_status.get("ACTIVE", 0),
        "by_type": by_type,
        "by_status": by_status,
        "edge_key_index": len(idx.get("edge_key") or {}),
        "outgoing_index_nodes": len(idx.get("outgoing") or {}),
        "incoming_index_nodes": len(idx.get("incoming") or {}),
        "average_degree": round(avg_degree, 3),
        "top_connected_entities": top_named,
    }
