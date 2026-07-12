"""Persistent edge store + adjacency indexes.

Layout:
  automation/knowledge/store/relationships.json
  automation/knowledge/store/indexes/
    edge_key.json      # source|type|target → relationship_id
    outgoing.json      # entity_id → [relationship_id, ...]
    incoming.json      # entity_id → [relationship_id, ...]
    rel_type.json      # relationship_type → [relationship_id, ...]

No external graph DB. No dataset rows.
"""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any, Iterable, Optional

from automation.knowledge.models import GraphRelationship, RelationshipStatus
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

_LOCK = threading.Lock()


def store_root(repo_root: Optional[Path] = None) -> Path:
    root = repo_root or find_repo_root()
    return root / "automation" / "knowledge" / "store"


def relationships_path(repo_root: Optional[Path] = None) -> Path:
    return store_root(repo_root) / "relationships.json"


def indexes_dir(repo_root: Optional[Path] = None) -> Path:
    d = store_root(repo_root) / "indexes"
    d.mkdir(parents=True, exist_ok=True)
    return d


def edge_key(source_entity: str, relationship_type: str, target_entity: str) -> str:
    return f"{source_entity}|{relationship_type}|{target_entity}"


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


def load_all_relationships(
    *, repo_root: Optional[Path] = None
) -> dict[str, GraphRelationship]:
    data = _read_json(relationships_path(repo_root))
    if not isinstance(data, dict):
        return {}
    raw = data.get("relationships") or {}
    out: dict[str, GraphRelationship] = {}
    if isinstance(raw, dict):
        for rid, row in raw.items():
            if isinstance(row, dict):
                rel = GraphRelationship.from_dict(row)
                out[rel.relationship_id or str(rid)] = rel
    return out


def load_edge_indexes(
    *, repo_root: Optional[Path] = None
) -> dict[str, dict[str, Any]]:
    d = indexes_dir(repo_root)
    names = ("edge_key", "outgoing", "incoming", "rel_type")
    idx: dict[str, dict[str, Any]] = {n: {} for n in names}
    for name in names:
        raw = _read_json(d / f"{name}.json")
        if isinstance(raw, dict):
            idx[name] = raw
    return idx


def rebuild_edge_indexes(
    relationships: dict[str, GraphRelationship],
) -> dict[str, dict[str, Any]]:
    idx: dict[str, dict[str, Any]] = {
        "edge_key": {},
        "outgoing": {},
        "incoming": {},
        "rel_type": {},
    }
    for rid, rel in relationships.items():
        if rel.status not in (RelationshipStatus.ACTIVE.value, "ACTIVE"):
            # Keep superseded keys only for redirect via merged_into if needed
            if rel.status in (
                RelationshipStatus.MERGED.value,
                RelationshipStatus.SUPERSEDED.value,
            ):
                pass
            else:
                continue
        key = edge_key(rel.source_entity, rel.relationship_type, rel.target_entity)
        idx["edge_key"][key] = rid
        idx["outgoing"].setdefault(rel.source_entity, [])
        if rid not in idx["outgoing"][rel.source_entity]:
            idx["outgoing"][rel.source_entity].append(rid)
        idx["incoming"].setdefault(rel.target_entity, [])
        if rid not in idx["incoming"][rel.target_entity]:
            idx["incoming"][rel.target_entity].append(rid)
        idx["rel_type"].setdefault(rel.relationship_type, [])
        if rid not in idx["rel_type"][rel.relationship_type]:
            idx["rel_type"][rel.relationship_type].append(rid)
    return idx


def save_relationships(
    relationships: dict[str, GraphRelationship],
    *,
    repo_root: Optional[Path] = None,
) -> None:
    payload = {
        "version": "1.0",
        "updated_at": utc_now_iso(),
        "relationship_count": len(relationships),
        "relationships": {rid: r.to_dict() for rid, r in relationships.items()},
    }
    _write_json(relationships_path(repo_root), payload)


def save_edge_indexes(
    indexes: dict[str, dict[str, Any]],
    *,
    repo_root: Optional[Path] = None,
) -> None:
    d = indexes_dir(repo_root)
    for name, data in indexes.items():
        _write_json(d / f"{name}.json", data)


def upsert_relationships_batch(
    batch: Iterable[GraphRelationship],
    *,
    repo_root: Optional[Path] = None,
) -> dict[str, Any]:
    """Merge batch into store; rebuild edge indexes once."""
    with _LOCK:
        rels = load_all_relationships(repo_root=repo_root)
        created = 0
        updated = 0
        for rel in batch:
            if rel.relationship_id in rels:
                updated += 1
            else:
                created += 1
            rels[rel.relationship_id] = rel
        indexes = rebuild_edge_indexes(rels)
        save_relationships(rels, repo_root=repo_root)
        save_edge_indexes(indexes, repo_root=repo_root)
        return {
            "relationship_count": len(rels),
            "created": created,
            "updated": updated,
            "edge_keys": len(indexes.get("edge_key") or {}),
        }


def get_relationship(
    relationship_id: str,
    *,
    relationships: Optional[dict[str, GraphRelationship]] = None,
    repo_root: Optional[Path] = None,
) -> Optional[GraphRelationship]:
    rels = (
        relationships
        if relationships is not None
        else load_all_relationships(repo_root=repo_root)
    )
    rel = rels.get(relationship_id)
    if rel and rel.merged_into and rel.merged_into in rels:
        return rels[rel.merged_into]
    return rel
