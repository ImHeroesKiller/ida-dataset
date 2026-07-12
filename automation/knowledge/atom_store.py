"""Persistent Knowledge Atom store — local JSON files, no external DB.

Layout (additive):
  automation/knowledge/store/atoms/{document_id}.json
  automation/knowledge/store/atoms/_index.json

Does not modify domain CSVs, queues, or frozen pipeline stages.
"""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any, Iterable, Optional

from automation.knowledge.models import KnowledgeAtom
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

_LOCK = threading.Lock()


def store_root(repo_root: Optional[Path] = None) -> Path:
    root = repo_root or find_repo_root()
    return root / "automation" / "knowledge" / "store"


def atoms_dir(repo_root: Optional[Path] = None) -> Path:
    d = store_root(repo_root) / "atoms"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _index_path(repo_root: Optional[Path] = None) -> Path:
    return atoms_dir(repo_root) / "_index.json"


def _doc_path(document_id: str, repo_root: Optional[Path] = None) -> Path:
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in document_id)
    return atoms_dir(repo_root) / f"{safe}.json"


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


def save_atoms_for_document(
    document_id: str,
    atoms: Iterable[KnowledgeAtom],
    *,
    repo_root: Optional[Path] = None,
    replace: bool = True,
) -> dict[str, Any]:
    """Persist atoms for one document. Returns summary stats."""
    atom_list = [a if isinstance(a, KnowledgeAtom) else KnowledgeAtom.from_dict(a) for a in atoms]  # type: ignore[arg-type]
    # Deduplicate by atom_id within document
    by_id: dict[str, KnowledgeAtom] = {}
    for a in atom_list:
        if a.atom_id:
            by_id[a.atom_id] = a
    atom_list = sorted(by_id.values(), key=lambda x: x.order)

    path = _doc_path(document_id, repo_root)
    with _LOCK:
        if not replace and path.exists():
            existing = load_atoms_for_document(document_id, repo_root=repo_root)
            merged = {a.atom_id: a for a in existing}
            for a in atom_list:
                merged[a.atom_id] = a
            atom_list = sorted(merged.values(), key=lambda x: x.order)

        payload = {
            "document_id": document_id,
            "atom_count": len(atom_list),
            "updated_at": utc_now_iso(),
            "atoms": [a.to_dict() for a in atom_list],
        }
        _write_json(path, payload)
        _update_index(document_id, len(atom_list), repo_root=repo_root)

    type_counts: dict[str, int] = {}
    for a in atom_list:
        type_counts[a.atom_type] = type_counts.get(a.atom_type, 0) + 1
    return {
        "document_id": document_id,
        "atom_count": len(atom_list),
        "path": str(path),
        "type_counts": type_counts,
    }


def load_atoms_for_document(
    document_id: str,
    *,
    repo_root: Optional[Path] = None,
) -> list[KnowledgeAtom]:
    data = _read_json(_doc_path(document_id, repo_root))
    if not isinstance(data, dict):
        return []
    raw = data.get("atoms") or []
    out: list[KnowledgeAtom] = []
    for row in raw:
        if isinstance(row, dict):
            out.append(KnowledgeAtom.from_dict(row))
    return out


def list_atomized_documents(*, repo_root: Optional[Path] = None) -> list[dict[str, Any]]:
    idx = _read_json(_index_path(repo_root))
    if isinstance(idx, dict) and isinstance(idx.get("documents"), list):
        return list(idx["documents"])
    # Rebuild from files
    docs: list[dict[str, Any]] = []
    for p in sorted(atoms_dir(repo_root).glob("DOC-*.json")):
        data = _read_json(p)
        if isinstance(data, dict) and data.get("document_id"):
            docs.append(
                {
                    "document_id": data["document_id"],
                    "atom_count": int(data.get("atom_count") or 0),
                    "updated_at": data.get("updated_at"),
                }
            )
    return docs


def count_atoms(*, repo_root: Optional[Path] = None) -> int:
    return sum(int(d.get("atom_count") or 0) for d in list_atomized_documents(repo_root=repo_root))


def iter_all_atoms(*, repo_root: Optional[Path] = None):
    for d in list_atomized_documents(repo_root=repo_root):
        did = str(d.get("document_id") or "")
        if not did:
            continue
        for atom in load_atoms_for_document(did, repo_root=repo_root):
            yield atom


def _update_index(
    document_id: str,
    atom_count: int,
    *,
    repo_root: Optional[Path] = None,
) -> None:
    path = _index_path(repo_root)
    idx = _read_json(path)
    if not isinstance(idx, dict):
        idx = {"documents": [], "updated_at": utc_now_iso()}
    docs = list(idx.get("documents") or [])
    found = False
    now = utc_now_iso()
    for d in docs:
        if isinstance(d, dict) and d.get("document_id") == document_id:
            d["atom_count"] = atom_count
            d["updated_at"] = now
            found = True
            break
    if not found:
        docs.append(
            {
                "document_id": document_id,
                "atom_count": atom_count,
                "updated_at": now,
            }
        )
    idx["documents"] = docs
    idx["updated_at"] = now
    idx["document_count"] = len(docs)
    idx["total_atoms"] = sum(int(x.get("atom_count") or 0) for x in docs if isinstance(x, dict))
    _write_json(path, idx)


def atomize_and_persist_document(
    doc: dict[str, Any],
    *,
    repo_root: Optional[Path] = None,
    text: Optional[str] = None,
) -> dict[str, Any]:
    """Convenience: atomize production document dict and save."""
    from automation.knowledge.atoms import atomize_document

    atoms = atomize_document(doc, text=text)
    document_id = str(doc.get("document_id") or "DOC-UNKNOWN")
    summary = save_atoms_for_document(
        document_id, atoms, repo_root=repo_root, replace=True
    )
    summary["atoms_sample"] = [a.to_dict() for a in atoms[:3]]
    return summary
