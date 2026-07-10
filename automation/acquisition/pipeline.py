"""Acquisition pipeline:

Mission → Source Discovery → Download → Normalize → Document Queue
→ Extraction → Candidate Queue → Validation → Publish Queue → Dataset
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Callable, Optional

from automation.acquisition.document_store import DocumentStore
from automation.acquisition.extractor import (
    extract_business_signal_candidates,
    extract_industry_candidates,
    save_candidate_queue,
)
from automation.acquisition.source_registry import SourceRegistry
from automation.connectors.manager import ConnectorManager
from automation.connectors.types import SearchQuery
from automation.lib.io_utils import append_csv_rows
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root
from automation.quality.integrity_guard import filter_append_rows


LogFn = Callable[[str, str], None]


def _default_log(verb: str, detail: str) -> None:
    print(f"[{verb}] {detail}")


def run_acquisition(
    *,
    instruction: str,
    mission_id: str = "",
    session_id: str = "",
    dataset: str = "industry_library",
    limit: int = 5,
    dry_run: bool = False,
    publish: bool = True,
    auto_approve: bool = True,
    repo_root: Path | None = None,
    log: Optional[LogFn] = None,
    preferred_connector_ids: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Execute real acquisition end-to-end. Never silently succeeds with empty results."""
    root = repo_root or find_repo_root()
    emit = log or _default_log
    audit: dict[str, Any] = {
        "started_at": utc_now_iso(),
        "instruction": instruction,
        "mission_id": mission_id,
        "session_id": session_id,
        "dataset": dataset,
        "dry_run": dry_run,
        "sources_contacted": [],
        "http_requests": 0,
        "documents_discovered": 0,
        "documents_downloaded": 0,
        "candidates_extracted": 0,
        "candidates_validated": 0,
        "candidates_rejected": 0,
        "rows_published": 0,
        "failures": [],
        "queue_stats": {},
        "documents": [],
        "candidates": [],
        "published_entities": [],
        "reasons": [],
    }

    registry = SourceRegistry(repo_root=root)
    sources = registry.select_for_mission(dataset=dataset, limit=8)
    manager = ConnectorManager(repo_root=root)
    doc_store = DocumentStore(repo_root=root)

    # Map sources → connectors
    connector_ids = preferred_connector_ids or registry.connector_ids_for(sources)
    # Always prefer production APIs known healthy
    fallback_order = [
        "CONN-WB-001",
        "CONN-OPENALEX-001",
        "CONN-CROSSREF-001",
        "CONN-ADB-001",
        "CONN-OECD-001",
        "CONN-BPS-001",
    ]
    for fid in fallback_order:
        if fid not in connector_ids:
            connector_ids.append(fid)

    # Filter to enabled non-dry-run connectors when not dry_run
    enabled_cfgs = {
        str(c["connector_id"]): c
        for c in manager.list_connectors()
        if c.get("enabled")
    }
    selected: list[str] = []
    for cid in connector_ids:
        cfg = enabled_cfgs.get(cid)
        if not cfg:
            continue
        if not dry_run and cfg.get("dry_run"):
            # skip pure dry-run connectors in production acquisition
            continue
        selected.append(cid)
    if not selected:
        # last resort: any enabled
        selected = [cid for cid, c in enabled_cfgs.items() if not c.get("dry_run")][:6]
    if not selected:
        selected = list(enabled_cfgs.keys())[:4]

    audit["sources_contacted"] = selected
    for cid in selected:
        cfg = enabled_cfgs.get(cid) or {}
        emit("Searching", f"Searching {cfg.get('name') or cid}")

    query_text = instruction if len(instruction) < 160 else f"{dataset} Indonesia"
    # Bias toward Indonesia industry knowledge
    if "indonesia" not in query_text.lower():
        query_text = f"{query_text} Indonesia"

    q = SearchQuery(
        query=query_text,
        limit=limit,
        mission_id=mission_id,
        dry_run=dry_run,
        metadata={"mission_id": mission_id, "session_id": session_id},
    )

    results = manager.search(q, connector_ids=selected)
    audit["documents_discovered"] = len(results)
    audit["http_requests"] += len(selected)  # at least one search per connector
    emit("Connector", f"Found {len(results)} candidate documents")

    if not results:
        reason = (
            "No documents discovered from trusted sources. "
            f"Connectors tried: {', '.join(selected)}. "
            "Check network, rate limits, or source health."
        )
        audit["failures"].append(reason)
        audit["reasons"].append(reason)
        audit["ok"] = False
        audit["error"] = "no_documents_discovered"
        audit["finished_at"] = utc_now_iso()
        emit("Connector", reason)
        return audit

    # Prefer high-success API connectors; diversify across sources
    prefer_order = [
        "CONN-WB-001",
        "CONN-OPENALEX-001",
        "CONN-CROSSREF-001",
        "CONN-ADB-001",
        "CONN-OECD-001",
        "CONN-BPS-001",
    ]
    rank = {cid: i for i, cid in enumerate(prefer_order)}
    results = sorted(
        results,
        key=lambda r: (rank.get(r.connector_id, 99), -float(r.trust_score or 0)),
    )
    # Round-robin across connectors so one failing source cannot monopolize the batch
    by_conn: dict[str, list] = {}
    for r in results:
        by_conn.setdefault(r.connector_id, []).append(r)
    diversified: list = []
    while len(diversified) < max(limit * 2, limit) and any(by_conn.values()):
        for cid in list(by_conn.keys()):
            bucket = by_conn.get(cid) or []
            if not bucket:
                continue
            diversified.append(bucket.pop(0))
            if len(diversified) >= max(limit * 2, limit):
                break
    results = diversified or results

    # Download / acquire (with metadata fallback — never invent content)
    documents: list[dict[str, Any]] = []
    for res in results:
        if len(documents) >= limit:
            break
        try:
            emit("Downloading", f"Downloading report {res.title[:80]}")
            doc = manager.acquire(res, mission_id=mission_id)
            d = doc.to_dict()
        except Exception as exc:  # noqa: BLE001
            # Fallback: materialize document from trusted search metadata only
            emit(
                "Downloading",
                f"Full fetch failed ({exc}); storing search metadata document",
            )
            d = _document_from_search_result(res, mission_id=mission_id)
            audit["failures"].append(f"download_fallback:{res.url}:{exc}")

        meta = d.get("metadata") or {}
        if not meta.get("text_excerpt") and res.snippet:
            meta["text_excerpt"] = res.snippet
            meta["snippet"] = res.snippet
        if res.metadata:
            meta = {**meta, **{k: v for k, v in res.metadata.items() if k not in meta or not meta.get(k)}}
        # Always keep title in text for extraction
        if res.title and res.title not in str(meta.get("text_excerpt") or ""):
            meta["text_excerpt"] = f"{res.title}\n\n{meta.get('text_excerpt') or res.snippet or ''}"
        d["metadata"] = meta
        d["title"] = d.get("title") or res.title
        d["mission_id"] = mission_id
        doc_store.enqueue(d)
        documents.append(d)
        audit["documents"].append(
            {
                "document_id": d.get("document_id"),
                "title": d.get("title"),
                "url": d.get("original_url") or d.get("url"),
                "source_id": d.get("source_id"),
                "connector_id": d.get("connector_id"),
            }
        )
        audit["documents_downloaded"] += 1
        audit["http_requests"] += 1
        emit("Document Queue", f"Queued {d.get('document_id')}")

    audit["queue_stats"]["documents"] = doc_store.counts()

    if not documents:
        reason = (
            "Documents discovered but none downloaded successfully. "
            f"Failures: {audit['failures'][:5]}"
        )
        audit["failures"].append(reason)
        audit["reasons"].append(reason)
        audit["ok"] = False
        audit["error"] = "no_documents_downloaded"
        audit["finished_at"] = utc_now_iso()
        emit("Connector", reason)
        return audit

    # Mark processing
    for d in documents:
        did = str(d.get("document_id") or "")
        if did:
            doc_store.move(did, "processing")
            emit("Parsing document", f"Parsing document {did}")

    # Extract
    emit("Extracting", f"Extracting knowledge candidates for {dataset}")
    candidates = extract_industry_candidates(
        documents,
        mission_id=mission_id,
        session_id=session_id,
        repo_root=root,
        max_candidates=5,
    )
    if not candidates:
        # fallback: business signals so queue is never empty after real docs
        emit("Extracting", "No new industry entities — extracting business signals")
        candidates = extract_business_signal_candidates(
            documents,
            mission_id=mission_id,
            session_id=session_id,
            repo_root=root,
            max_candidates=3,
        )

    audit["candidates_extracted"] = len(candidates)
    for c in candidates:
        emit(
            "Extracting",
            f"Extracting {c.entity_type}: {c.canonical_name}",
        )
        audit["candidates"].append(
            {
                "candidate_id": c.candidate_id,
                "entity_id": c.entity_id,
                "name": c.canonical_name,
                "dataset": c.target_dataset,
                "confidence": c.provenance.confidence,
            }
        )

    if not candidates:
        reason = (
            "Documents downloaded but no grounded candidates could be extracted "
            "(no matched industry aliases / insufficient evidence). "
            "No fabricated rows will be published."
        )
        audit["failures"].append(reason)
        audit["reasons"].append(reason)
        audit["ok"] = False
        audit["error"] = "no_candidates_extracted"
        for d in documents:
            did = str(d.get("document_id") or "")
            if did:
                doc_store.move(did, "processed")
        audit["finished_at"] = utc_now_iso()
        emit("Pipeline", reason)
        return audit

    # Save candidate queue
    stage = "approved" if auto_approve else "pending"
    if auto_approve:
        for c in candidates:
            c.provenance.validation_status = "approved"
            c.provenance.reviewer = "acquisition-engine"
    save_candidate_queue(candidates, repo_root=root, stage=stage)
    # also publish queue folder
    pub_dir = root / "automation" / "queue" / "publish"
    pub_dir.mkdir(parents=True, exist_ok=True)
    for c in candidates:
        (pub_dir / f"{c.candidate_id}.json").write_text(
            json.dumps(c.to_dict(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    emit("Candidate Queue", f"Queued {len(candidates)} candidates")

    # Validate + Publish
    published_rows = 0
    rejected = 0
    published_entities: list[str] = []

    if publish and not dry_run:
        # group by dataset
        by_ds: dict[str, list] = {}
        for c in candidates:
            by_ds.setdefault(c.target_dataset, []).append(c)

        for ds_name, group in by_ds.items():
            csv_path = root / "domains" / "business_development" / f"{ds_name}.csv"
            # Ensure CSV exists with headers for business_signal if empty
            if ds_name == "business_signal_library":
                _ensure_signal_csv(csv_path)
            if not csv_path.exists():
                audit["failures"].append(f"dataset_missing:{ds_name}")
                continue

            with csv_path.open(encoding="utf-8-sig", newline="") as f:
                headers = [(h or "").lstrip("\ufeff") for h in next(csv.reader(f))]

            rows = []
            for c in group:
                row = {h: str(c.payload.get(h, "") or "") for h in headers}
                rows.append(row)

            filtered = filter_append_rows(csv_path, rows, repo_root=root)
            rejected += int(filtered["rejected_count"])
            for r in filtered.get("rejected") or []:
                audit["failures"].append(f"validation_reject:{r.get('reason')}")
                emit("Validation", f"Rejected: {r.get('reason')}")

            accepted = filtered.get("accepted") or []
            audit["candidates_validated"] += len(accepted)
            if accepted:
                emit("Validation", f"Validation passed for {len(accepted)} row(s)")
                append_csv_rows(csv_path, accepted, fieldnames=headers)
                published_rows += len(accepted)
                for r in accepted:
                    name = (
                        r.get("Industry Name")
                        or r.get("Signal Name")
                        or r.get("Company Name")
                        or list(r.values())[0]
                    )
                    published_entities.append(str(name))
                    emit("Publishing", f"Published {name} → {ds_name}.csv")
                # remove from publish queue after success
                for c in group:
                    pq = pub_dir / f"{c.candidate_id}.json"
                    if pq.exists():
                        pq.unlink()
    elif dry_run:
        emit("Publishing", "dry_run — candidates queued but not appended")
        audit["candidates_validated"] = len(candidates)
    else:
        emit("Publishing", "publish disabled — candidates left in queue")

    for d in documents:
        did = str(d.get("document_id") or "")
        if did:
            doc_store.move(did, "processed")
            try:
                manager.queue.move(did, "processed")
            except Exception:  # noqa: BLE001
                pass

    audit["candidates_rejected"] = rejected
    audit["rows_published"] = published_rows
    audit["published_entities"] = published_entities
    audit["queue_stats"]["documents_final"] = doc_store.counts()
    audit["queue_stats"]["publish_remaining"] = len(list(pub_dir.glob("*.json")))
    audit["ok"] = published_rows > 0 or (not publish) or dry_run
    if published_rows == 0 and publish and not dry_run:
        if rejected and candidates:
            audit["error"] = "all_candidates_rejected"
            audit["reasons"].append("All candidates rejected by integrity/DPS validation")
            audit["ok"] = False
        elif not candidates:
            audit["error"] = "no_candidates"
            audit["ok"] = False
        else:
            # candidates validated path without publish shouldn't happen
            audit["error"] = "zero_published"
            audit["ok"] = False
            audit["reasons"].append("Zero rows published — see failures")
    audit["finished_at"] = utc_now_iso()
    emit(
        "Knowledge Updated",
        f"Published {published_rows} rows · Knowledge Added {published_rows}",
    )
    return audit


def _document_from_search_result(res: Any, *, mission_id: str = "") -> dict[str, Any]:
    """Build a document record from search metadata when binary/page fetch fails.

    Uses only title/snippet/url from the trusted connector — never fabricates body text.
    """
    import hashlib

    title = str(getattr(res, "title", "") or "")
    snippet = str(getattr(res, "snippet", "") or "")
    url = str(getattr(res, "url", "") or "")
    meta = dict(getattr(res, "metadata", None) or {})
    text = f"{title}\n\n{snippet}".strip()
    checksum = hashlib.sha256(text.encode("utf-8")).hexdigest()
    doc_id = f"DOC-{checksum[:12].upper()}"
    return {
        "document_id": doc_id,
        "connector_id": str(getattr(res, "connector_id", "") or ""),
        "source_id": str(getattr(res, "source_id", "") or ""),
        "trust_score": float(getattr(res, "trust_score", 0.85) or 0.85),
        "original_url": url,
        "url": url,
        "checksum": checksum,
        "hash": checksum,
        "version": "2.0",
        "title": title,
        "content_type": "text/plain",
        "local_path": None,
        "status": "incoming",
        "dry_run": False,
        "mission_id": mission_id,
        "bytes": len(text.encode("utf-8")),
        "notes": "Metadata document from connector search (page fetch unavailable)",
        "metadata": {
            **meta,
            "text_excerpt": text[:8000],
            "snippet": snippet,
            "acquired": True,
            "metadata_only": True,
        },
        "retrieved_at": utc_now_iso(),
        "published_at": str(meta.get("published_at") or ""),
    }


def _ensure_signal_csv(path: Path) -> None:
    if path.exists() and path.stat().st_size > 0:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = [
        "Signal ID",
        "Signal Name",
        "Signal Type",
        "Description",
        "Industry",
        "Source",
        "Source URL",
        "Published Date",
        "Retrieved Date",
        "Confidence",
        "Mission ID",
        "Version",
        "Data Sources",
        "Notes",
    ]
    path.write_text(",".join(headers) + "\n", encoding="utf-8", newline="\n")
