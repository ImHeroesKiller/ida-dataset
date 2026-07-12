"""Canonical Entity Store + indexes — local JSON, no external DB.

Layout:
  automation/knowledge/store/entities.json
  automation/knowledge/store/indexes/
    canonical.json   # normalized_key → entity_id
    alias.json       # normalized_alias → entity_id
    document.json    # document_id → [entity_id, ...]
    atom.json        # atom_id → [entity_id, ...]
    source.json      # source_id → [entity_id, ...]

No linear full-scan lookups for resolve/find.
No relationships (Commit 3).
"""

from __future__ import annotations

import json
import re
import threading
import unicodedata
from pathlib import Path
from typing import Any, Iterable, Optional

from automation.knowledge.models import EntityStatus, GraphEntity
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

_LOCK = threading.Lock()
_WS = re.compile(r"\s+")


def store_root(repo_root: Optional[Path] = None) -> Path:
    root = repo_root or find_repo_root()
    return root / "automation" / "knowledge" / "store"


def entities_path(repo_root: Optional[Path] = None) -> Path:
    return store_root(repo_root) / "entities.json"


def indexes_dir(repo_root: Optional[Path] = None) -> Path:
    d = store_root(repo_root) / "indexes"
    d.mkdir(parents=True, exist_ok=True)
    return d


def normalize_name(name: str) -> str:
    """Canonical lookup key for names and aliases."""
    s = unicodedata.normalize("NFKC", name or "")
    s = s.lower().strip()
    # Strip common corporate suffixes for matching
    s = re.sub(
        r"\b(pt\.?|tbk\.?|inc\.?|corp\.?|corporation|ltd\.?|llc\.?|co\.?|company|"
        r"gmbh|ag|plc|limited|persero)\b",
        " ",
        s,
    )
    s = re.sub(r"[^\w\s&/+-]", " ", s)
    s = _WS.sub(" ", s).strip()
    return s


def _read_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    tmp.replace(path)


def _empty_indexes() -> dict[str, dict[str, Any]]:
    return {
        "canonical": {},
        "alias": {},
        "document": {},
        "atom": {},
        "source": {},
    }


def load_all_entities(*, repo_root: Optional[Path] = None) -> dict[str, GraphEntity]:
    data = _read_json(entities_path(repo_root))
    if not isinstance(data, dict):
        return {}
    entities_raw = data.get("entities") or {}
    out: dict[str, GraphEntity] = {}
    if isinstance(entities_raw, dict):
        for eid, row in entities_raw.items():
            if isinstance(row, dict):
                ent = GraphEntity.from_dict(row)
                out[ent.entity_id or str(eid)] = ent
    return out


def load_indexes(*, repo_root: Optional[Path] = None) -> dict[str, dict[str, Any]]:
    d = indexes_dir(repo_root)
    idx = _empty_indexes()
    for name in idx:
        raw = _read_json(d / f"{name}.json")
        if isinstance(raw, dict):
            # document/atom/source map to lists
            idx[name] = raw
    return idx


def save_entities(
    entities: dict[str, GraphEntity],
    *,
    repo_root: Optional[Path] = None,
) -> None:
    payload = {
        "version": "1.0",
        "updated_at": utc_now_iso(),
        "entity_count": len(entities),
        "entities": {eid: e.to_dict() for eid, e in entities.items()},
    }
    _write_json(entities_path(repo_root), payload)


def save_indexes(
    indexes: dict[str, dict[str, Any]],
    *,
    repo_root: Optional[Path] = None,
) -> None:
    d = indexes_dir(repo_root)
    for name, data in indexes.items():
        _write_json(d / f"{name}.json", data)


def rebuild_indexes(
    entities: dict[str, GraphEntity],
) -> dict[str, dict[str, Any]]:
    idx = _empty_indexes()
    for eid, ent in entities.items():
        if ent.status not in {
            EntityStatus.ACTIVE.value,
            "ACTIVE",
        } and ent.status in {
            EntityStatus.ARCHIVED.value,
            EntityStatus.SUPERSEDED.value,
            EntityStatus.MERGED.value,
        }:
            # Still index MERGED/SUPERSEDED for alias redirect via merged_into
            pass
        ckey = normalize_name(ent.canonical_name)
        if ckey:
            idx["canonical"][ckey] = eid
        for alias in ent.aliases:
            akey = normalize_name(alias)
            if akey:
                idx["alias"][akey] = eid
        for did in ent.document_ids:
            idx["document"].setdefault(did, [])
            if eid not in idx["document"][did]:
                idx["document"][did].append(eid)
        for aid in ent.atom_ids:
            idx["atom"].setdefault(aid, [])
            if eid not in idx["atom"][aid]:
                idx["atom"][aid].append(eid)
        for src in ent.sources:
            idx["source"].setdefault(src, [])
            if eid not in idx["source"][src]:
                idx["source"][src].append(eid)
    return idx


def find_by_canonical(
    name: str,
    *,
    indexes: Optional[dict[str, dict[str, Any]]] = None,
    repo_root: Optional[Path] = None,
) -> Optional[str]:
    idx = indexes or load_indexes(repo_root=repo_root)
    key = normalize_name(name)
    if not key:
        return None
    return idx.get("canonical", {}).get(key) or idx.get("alias", {}).get(key)


def find_by_alias(
    alias: str,
    *,
    indexes: Optional[dict[str, dict[str, Any]]] = None,
    repo_root: Optional[Path] = None,
) -> Optional[str]:
    return find_by_canonical(alias, indexes=indexes, repo_root=repo_root)


def get_entity(
    entity_id: str,
    *,
    entities: Optional[dict[str, GraphEntity]] = None,
    repo_root: Optional[Path] = None,
) -> Optional[GraphEntity]:
    ents = entities if entities is not None else load_all_entities(repo_root=repo_root)
    ent = ents.get(entity_id)
    if ent and ent.merged_into and ent.status in {
        EntityStatus.MERGED.value,
        EntityStatus.SUPERSEDED.value,
    }:
        return ents.get(ent.merged_into) or ent
    return ent


def entities_for_document(
    document_id: str,
    *,
    indexes: Optional[dict[str, dict[str, Any]]] = None,
    entities: Optional[dict[str, GraphEntity]] = None,
    repo_root: Optional[Path] = None,
) -> list[GraphEntity]:
    idx = indexes or load_indexes(repo_root=repo_root)
    ents = entities if entities is not None else load_all_entities(repo_root=repo_root)
    ids = idx.get("document", {}).get(document_id) or []
    out: list[GraphEntity] = []
    for eid in ids:
        e = ents.get(eid)
        if e:
            out.append(e)
    return out


def upsert_entity(
    entity: GraphEntity,
    *,
    repo_root: Optional[Path] = None,
) -> GraphEntity:
    """Thread-safe upsert of one entity + index rebuild for that entity's keys."""
    with _LOCK:
        entities = load_all_entities(repo_root=repo_root)
        entities[entity.entity_id] = entity
        indexes = rebuild_indexes(entities)
        save_entities(entities, repo_root=repo_root)
        save_indexes(indexes, repo_root=repo_root)
        return entity


def upsert_entities_batch(
    batch: Iterable[GraphEntity],
    *,
    repo_root: Optional[Path] = None,
) -> dict[str, Any]:
    """Batch upsert — single write of entities + indexes."""
    with _LOCK:
        entities = load_all_entities(repo_root=repo_root)
        created = 0
        updated = 0
        for ent in batch:
            if ent.entity_id in entities:
                updated += 1
            else:
                created += 1
            entities[ent.entity_id] = ent
        indexes = rebuild_indexes(entities)
        save_entities(entities, repo_root=repo_root)
        save_indexes(indexes, repo_root=repo_root)
        return {
            "entity_count": len(entities),
            "created": created,
            "updated": updated,
            "canonical_keys": len(indexes.get("canonical") or {}),
            "alias_keys": len(indexes.get("alias") or {}),
        }


def entity_stats(*, repo_root: Optional[Path] = None) -> dict[str, Any]:
    entities = load_all_entities(repo_root=repo_root)
    indexes = load_indexes(repo_root=repo_root)
    by_type: dict[str, int] = {}
    by_status: dict[str, int] = {}
    alias_count = 0
    for e in entities.values():
        by_type[e.entity_type] = by_type.get(e.entity_type, 0) + 1
        by_status[e.status] = by_status.get(e.status, 0) + 1
        alias_count += len(e.aliases)
    return {
        "entity_count": len(entities),
        "by_type": by_type,
        "by_status": by_status,
        "alias_count": alias_count,
        "index_canonical": len(indexes.get("canonical") or {}),
        "index_alias": len(indexes.get("alias") or {}),
        "index_document": len(indexes.get("document") or {}),
        "index_atom": len(indexes.get("atom") or {}),
        "index_source": len(indexes.get("source") or {}),
    }
