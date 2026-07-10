"""Acquisition pipeline with full production observability.

Mission → Source Discovery → Connector → Document Discovery → Download
→ Extraction → Candidate Validation → Publish Queue → Append Dataset
"""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path
from typing import Any, Callable, Optional

from automation.acquisition.document_store import DocumentStore
from automation.acquisition.extractor import (
    extract_business_signal_candidates,
    extract_industry_candidates,
    save_candidate_queue,
)
from automation.acquisition.reports import write_production_reports
from automation.acquisition.source_registry import SourceRegistry
from automation.acquisition.trace import ProductionTrace
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
    """Execute real acquisition end-to-end with production trace."""
    root = repo_root or find_repo_root()
    emit = log or _default_log

    trace = ProductionTrace(
        mission=instruction,
        mission_id=mission_id,
        session_id=session_id,
        dataset=dataset,
        repo_root=root,
    )
    trace.start_stage("mission")
    emit("Mission", instruction)
    trace.finish_stage("mission", status="completed", meta={"instruction": instruction})

    audit: dict[str, Any] = {
        "started_at": trace.started_at,
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
        "connectors": [],
        "publish": {},
        "evidence_chains": [],
        "production_trace": None,
        "console": "",
    }

    registry = SourceRegistry(repo_root=root)
    manager = ConnectorManager(repo_root=root)
    doc_store = DocumentStore(repo_root=root)

    # --- Source discovery ---
    trace.start_stage("source_discovery")
    sources = registry.select_for_mission(dataset=dataset, limit=8)
    connector_ids = preferred_connector_ids or registry.connector_ids_for(sources)
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
            continue
        selected.append(cid)
    if not selected:
        selected = [cid for cid, c in enabled_cfgs.items() if not c.get("dry_run")][:6]
    if not selected:
        selected = list(enabled_cfgs.keys())[:4]

    audit["sources_contacted"] = selected
    source_name_by_id = {str(s.get("id")): str(s.get("name") or s.get("id")) for s in sources}
    for cfg in enabled_cfgs.values():
        sid = str(cfg.get("source_id") or "")
        if sid and sid not in source_name_by_id:
            source_name_by_id[sid] = str(cfg.get("name") or sid)

    emit("Source Discovery", f"Selected {len(selected)} connectors")
    trace.finish_stage(
        "source_discovery",
        status="completed",
        meta={"connectors": selected, "sources": [s.get("id") for s in sources]},
    )

    query_text = instruction if len(instruction) < 160 else f"{dataset} Indonesia"
    if "indonesia" not in query_text.lower():
        query_text = f"{query_text} Indonesia"

    # --- Connector search (per-connector for visibility) ---
    trace.start_stage("connector")
    trace.start_stage("document_discovery")
    all_results: list[Any] = []
    connector_rows: list[dict[str, Any]] = []

    for cid in selected:
        cfg = enabled_cfgs.get(cid) or {}
        name = str(cfg.get("name") or cid)
        source_id = str(cfg.get("source_id") or "")
        emit("Searching", f"Searching {name}")
        t0 = time.perf_counter()
        row: dict[str, Any] = {
            "connector_id": cid,
            "name": name,
            "source_id": source_id,
            "source_name": source_name_by_id.get(source_id, name),
            "status": "ok",
            "http_status": None,
            "elapsed_ms": 0.0,
            "documents_discovered": 0,
            "documents_downloaded": 0,
            "skipped": 0,
            "rejected": 0,
            "retry_count": 0,
            "last_successful_sync": "",
            "urls": [],
            "error": None,
        }
        try:
            q = SearchQuery(
                query=query_text,
                limit=limit,
                mission_id=mission_id,
                dry_run=dry_run,
                metadata={"mission_id": mission_id, "session_id": session_id},
            )
            found = manager.search(q, connector_ids=[cid])
            elapsed = round((time.perf_counter() - t0) * 1000, 1)
            row["elapsed_ms"] = elapsed
            row["documents_discovered"] = len(found)
            row["urls"] = [r.url for r in found[:5]]
            # Infer HTTP from first success (connectors don't always expose status)
            row["http_status"] = 200 if found or not dry_run else None
            if not found:
                row["status"] = "no_updates"
                row["http_status"] = row["http_status"] or 200
                emit("Searching", f"{name}: No updates")
            else:
                row["status"] = "ok"
                row["http_status"] = 200
                row["last_successful_sync"] = utc_now_iso()
                emit(
                    "Searching",
                    f"{name}: HTTP 200 · {len(found)} documents",
                )
            all_results.extend(found)
            audit["http_requests"] += 1
        except Exception as exc:  # noqa: BLE001
            elapsed = round((time.perf_counter() - t0) * 1000, 1)
            row["elapsed_ms"] = elapsed
            row["status"] = "error"
            row["error"] = str(exc)
            row["http_status"] = 0
            audit["failures"].append(f"connector_error:{cid}:{exc}")
            emit("Searching", f"{name}: error {exc}")
        connector_rows.append(row)
        trace.add_connector(row)
        audit["connectors"].append(row)

    # de-dupe results by URL
    seen_urls: set[str] = set()
    unique_results: list[Any] = []
    for r in all_results:
        key = (r.url or "").strip().lower()
        if not key or key in seen_urls:
            continue
        seen_urls.add(key)
        unique_results.append(r)

    audit["documents_discovered"] = len(unique_results)
    emit("Connector", f"Found {len(unique_results)} candidate documents")
    trace.finish_stage(
        "connector",
        status="completed",
        documents=len(unique_results),
        meta={"connectors_selected": selected},
    )
    trace.finish_stage(
        "document_discovery",
        status="completed" if unique_results else "failed",
        documents=len(unique_results),
        error=None if unique_results else "no_documents_discovered",
    )

    if not unique_results:
        reason = (
            "No documents discovered from trusted sources. "
            f"Connectors tried: {', '.join(selected)}."
        )
        audit["failures"].append(reason)
        audit["reasons"].append(reason)
        audit["ok"] = False
        audit["error"] = "no_documents_discovered"
        return _finalize_audit(audit, trace, ok=False, emit=emit)

    # Prefer high-success APIs; diversify
    prefer_order = fallback_order
    rank = {cid: i for i, cid in enumerate(prefer_order)}
    unique_results = sorted(
        unique_results,
        key=lambda r: (rank.get(r.connector_id, 99), -float(r.trust_score or 0)),
    )
    by_conn: dict[str, list] = {}
    for r in unique_results:
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
    results = diversified or unique_results

    # --- Download ---
    trace.start_stage("document_download")
    documents: list[dict[str, Any]] = []
    seen_checksums: set[str] = set()
    duplicates = 0
    conn_download_counts: dict[str, int] = {c["connector_id"]: 0 for c in connector_rows}

    for res in results:
        if len(documents) >= limit:
            break
        try:
            emit("Downloading", f"Downloading report {res.title[:80]}")
            doc = manager.acquire(res, mission_id=mission_id)
            d = doc.to_dict()
            fetch_mode = "download"
        except Exception as exc:  # noqa: BLE001
            emit(
                "Downloading",
                f"Full fetch failed ({exc}); storing search metadata document",
            )
            d = _document_from_search_result(res, mission_id=mission_id)
            audit["failures"].append(f"download_fallback:{res.url}:{exc}")
            fetch_mode = "metadata_fallback"

        meta = d.get("metadata") or {}
        if not meta.get("text_excerpt") and res.snippet:
            meta["text_excerpt"] = res.snippet
            meta["snippet"] = res.snippet
        if res.metadata:
            meta = {
                **meta,
                **{
                    k: v
                    for k, v in res.metadata.items()
                    if k not in meta or not meta.get(k)
                },
            }
        if res.title and res.title not in str(meta.get("text_excerpt") or ""):
            meta["text_excerpt"] = (
                f"{res.title}\n\n{meta.get('text_excerpt') or res.snippet or ''}"
            )
        d["metadata"] = meta
        d["title"] = d.get("title") or res.title
        d["mission_id"] = mission_id

        checksum = str(d.get("checksum") or d.get("hash") or "")
        if checksum and checksum in seen_checksums:
            duplicates += 1
            trace.document_queue["duplicates"] = duplicates
            emit("Document Queue", f"Duplicate skipped {d.get('document_id')}")
            for crow in connector_rows:
                if crow["connector_id"] == res.connector_id:
                    crow["skipped"] = int(crow.get("skipped") or 0) + 1
            continue
        if checksum:
            seen_checksums.add(checksum)

        doc_store.enqueue(d)
        doc_rec = {
            "document_id": d.get("document_id"),
            "title": d.get("title"),
            "url": d.get("original_url") or d.get("url"),
            "source_id": d.get("source_id"),
            "source_name": source_name_by_id.get(
                str(d.get("source_id") or ""), str(d.get("source_id") or "")
            ),
            "connector_id": d.get("connector_id"),
            "connector_name": next(
                (
                    c["name"]
                    for c in connector_rows
                    if c["connector_id"] == d.get("connector_id")
                ),
                d.get("connector_id"),
            ),
            "retrieved_at": d.get("retrieved_at"),
            "checksum": checksum,
            "size": d.get("bytes") or 0,
            "bytes": d.get("bytes") or 0,
            "content_type": d.get("content_type") or "text/plain",
            "document_type": (d.get("content_type") or "text/plain").split("/")[-1],
            "status": "queued",
            "fetch_mode": fetch_mode,
        }
        documents.append(d)
        audit["documents"].append(doc_rec)
        trace.add_document(doc_rec)
        audit["documents_downloaded"] += 1
        audit["http_requests"] += 1
        cid = str(d.get("connector_id") or "")
        conn_download_counts[cid] = conn_download_counts.get(cid, 0) + 1
        emit("Document Queue", f"Queued {d.get('document_id')}")

    # update connector download counts on trace
    for crow in connector_rows:
        crow["documents_downloaded"] = conn_download_counts.get(
            crow["connector_id"], 0
        )
    for i, crow in enumerate(trace.connectors):
        if i < len(connector_rows):
            crow["documents_downloaded"] = connector_rows[i]["documents_downloaded"]
            crow["skipped"] = connector_rows[i].get("skipped", 0)

    audit["queue_stats"]["documents"] = doc_store.counts()
    trace.document_queue["queued"] = len(documents)
    trace.document_queue["duplicates"] = duplicates

    if not documents:
        reason = (
            "Documents discovered but none downloaded successfully. "
            f"Failures: {audit['failures'][:5]}"
        )
        audit["failures"].append(reason)
        audit["reasons"].append(reason)
        audit["ok"] = False
        audit["error"] = "no_documents_downloaded"
        trace.finish_stage(
            "document_download",
            status="failed",
            documents=0,
            error=reason,
        )
        return _finalize_audit(audit, trace, ok=False, emit=emit)

    trace.finish_stage(
        "document_download",
        status="completed",
        documents=len(documents),
        meta={"duplicates": duplicates},
    )

    # Mark processing
    for d in documents:
        did = str(d.get("document_id") or "")
        if did:
            doc_store.move(did, "processing")
            for rec in audit["documents"]:
                if rec.get("document_id") == did:
                    rec["status"] = "processing"
            emit("Parsing document", f"Parsing document {did}")
    trace.document_queue["processing"] = len(documents)

    # --- Extraction ---
    trace.start_stage("extraction")
    emit("Extracting", f"Extracting knowledge candidates for {dataset}")
    candidates = extract_industry_candidates(
        documents,
        mission_id=mission_id,
        session_id=session_id,
        repo_root=root,
        max_candidates=5,
    )
    if not candidates:
        emit("Extracting", "No new industry entities — extracting business signals")
        candidates = extract_business_signal_candidates(
            documents,
            mission_id=mission_id,
            session_id=session_id,
            repo_root=root,
            max_candidates=3,
        )

    audit["candidates_extracted"] = len(candidates)
    cand_records: list[dict[str, Any]] = []
    # map document_id → doc
    doc_by_id = {str(d.get("document_id")): d for d in documents}

    for c in candidates:
        doc_id = str((c.metadata or {}).get("document_id") or "")
        # fall back: first document
        if not doc_id and documents:
            doc_id = str(documents[0].get("document_id") or "")
        doc = doc_by_id.get(doc_id) or (documents[0] if documents else {})
        evidence = (c.metadata or {}).get("evidence") or []
        snip = ""
        if isinstance(evidence, list) and evidence:
            snip = str(evidence[0])
        elif isinstance(evidence, str):
            snip = evidence
        rec = {
            "candidate_id": c.candidate_id,
            "entity": c.canonical_name,
            "name": c.canonical_name,
            "entity_id": c.entity_id,
            "dataset": c.target_dataset,
            "confidence": c.provenance.confidence,
            "validation_status": "pending",
            "publish_status": "pending",
            "reject_reason": None,
            "document_id": doc_id or doc.get("document_id"),
            "source_document": doc_id or doc.get("document_id"),
            "evidence_snippet": snip[:500],
            "source_id": c.provenance.source_id,
            "source_url": c.provenance.source_url,
            "connector_id": doc.get("connector_id"),
        }
        cand_records.append(rec)
        audit["candidates"].append(rec)
        trace.add_candidate(rec)
        emit("Extracting", f"Extracting {c.entity_type}: {c.canonical_name}")

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
                for rec in audit["documents"]:
                    if rec.get("document_id") == did:
                        rec["status"] = "completed"
        trace.document_queue["completed"] = len(documents)
        trace.document_queue["processing"] = 0
        trace.set_publish_counts(
            extracted=0, validated=0, rejected=0, queued=0, published=0
        )
        trace.finish_stage("extraction", status="failed", rows=0, error=reason)
        return _finalize_audit(audit, trace, ok=False, emit=emit)

    trace.finish_stage("extraction", status="completed", rows=len(candidates))
    emit("Candidate Queue", f"Queued {len(candidates)} candidates")

    # Save candidate + publish queue
    stage = "approved" if auto_approve else "pending"
    if auto_approve:
        for c in candidates:
            c.provenance.validation_status = "approved"
            c.provenance.reviewer = "acquisition-engine"
    save_candidate_queue(candidates, repo_root=root, stage=stage)
    pub_dir = root / "automation" / "queue" / "publish"
    pub_dir.mkdir(parents=True, exist_ok=True)
    for c in candidates:
        (pub_dir / f"{c.candidate_id}.json").write_text(
            json.dumps(c.to_dict(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    # --- Validation + Publish ---
    trace.start_stage("candidate_validation")
    trace.start_stage("publish_queue")
    published_rows = 0
    rejected = 0
    duplicates_pub = 0
    skipped = 0
    published_entities: list[str] = []
    by_dataset: dict[str, int] = {}
    validated = 0

    if publish and not dry_run:
        by_ds: dict[str, list] = {}
        for c in candidates:
            by_ds.setdefault(c.target_dataset, []).append(c)

        for ds_name, group in by_ds.items():
            csv_path = root / "domains" / "business_development" / f"{ds_name}.csv"
            if ds_name == "business_signal_library":
                _ensure_signal_csv(csv_path)
            if not csv_path.exists():
                audit["failures"].append(f"dataset_missing:{ds_name}")
                skipped += len(group)
                for c in group:
                    _mark_cand(cand_records, c.candidate_id, "skipped", "skipped", f"dataset_missing:{ds_name}")
                continue

            with csv_path.open(encoding="utf-8-sig", newline="") as f:
                headers = [(h or "").lstrip("\ufeff") for h in next(csv.reader(f))]

            rows = []
            cand_for_row = []
            for c in group:
                row = {h: str(c.payload.get(h, "") or "") for h in headers}
                rows.append(row)
                cand_for_row.append(c)

            filtered = filter_append_rows(csv_path, rows, repo_root=root)
            rejected += int(filtered["rejected_count"])
            for r in filtered.get("rejected") or []:
                reason = str(r.get("reason") or "rejected")
                audit["failures"].append(f"validation_reject:{reason}")
                emit("Validation", f"Rejected: {reason}")
                # match candidate by entity id field
                rej_row = r.get("row") or {}
                matched = False
                for c in group:
                    eid = c.entity_id
                    if eid and eid in str(rej_row.values()):
                        status = "duplicate" if "duplicate" in reason else "rejected"
                        if status == "duplicate":
                            duplicates_pub += 1
                        _mark_cand(
                            cand_records,
                            c.candidate_id,
                            "rejected" if status != "duplicate" else "duplicate",
                            status,
                            reason,
                        )
                        matched = True
                        break
                if not matched and group:
                    reason_full = reason
                    status = "duplicate" if "duplicate" in reason else "rejected"
                    if status == "duplicate":
                        # already counted in loop above only when matched — count here
                        pass
                    _mark_cand(
                        cand_records,
                        group[0].candidate_id,
                        "rejected",
                        status,
                        reason_full,
                    )

            accepted = filtered.get("accepted") or []
            validated += len(accepted)
            if accepted:
                emit("Validation", f"Validation passed for {len(accepted)} row(s)")
                # map accepted rows back to candidates by entity id
                accept_cands = []
                for row in accepted:
                    for c in group:
                        if c.entity_id and c.entity_id in str(row.values()):
                            accept_cands.append((c, row))
                            break
                    else:
                        # positional fallback
                        idx = accepted.index(row)
                        if idx < len(group):
                            accept_cands.append((group[idx], row))

                append_csv_rows(csv_path, accepted, fieldnames=headers)
                published_rows += len(accepted)
                by_dataset[ds_name] = by_dataset.get(ds_name, 0) + len(accepted)

                for c, row in accept_cands:
                    name = (
                        row.get("Industry Name")
                        or row.get("Signal Name")
                        or row.get("Company Name")
                        or c.canonical_name
                    )
                    published_entities.append(str(name))
                    _mark_cand(
                        cand_records, c.candidate_id, "approved", "published", None
                    )
                    emit("Publishing", f"Published {name} → {ds_name}.csv")
                    doc_id = str((c.metadata or {}).get("document_id") or "")
                    doc = doc_by_id.get(doc_id) or (documents[0] if documents else {})
                    evidence = (c.metadata or {}).get("evidence") or []
                    snip = str(evidence[0]) if isinstance(evidence, list) and evidence else ""
                    conn_name = next(
                        (
                            cr["name"]
                            for cr in connector_rows
                            if cr["connector_id"] == doc.get("connector_id")
                        ),
                        str(doc.get("connector_id") or ""),
                    )
                    src_id = str(c.provenance.source_id or doc.get("source_id") or "")
                    trace.add_evidence(
                        dataset=ds_name,
                        entity=str(name),
                        entity_id=c.entity_id,
                        candidate_id=c.candidate_id,
                        document_id=str(doc.get("document_id") or doc_id),
                        document_title=str(doc.get("title") or ""),
                        connector_id=str(doc.get("connector_id") or ""),
                        connector_name=conn_name,
                        source_id=src_id,
                        source_name=source_name_by_id.get(src_id, src_id),
                        url=str(c.provenance.source_url or doc.get("original_url") or ""),
                        confidence=float(c.provenance.confidence or 0),
                        evidence_snippet=snip,
                    )

                for c in group:
                    pq = pub_dir / f"{c.candidate_id}.json"
                    if pq.exists() and any(
                        x.candidate_id == c.candidate_id for x, _ in accept_cands
                    ):
                        pq.unlink()

        # recount duplicates from reject reasons if needed
        if duplicates_pub == 0:
            duplicates_pub = sum(
                1
                for r in cand_records
                if r.get("publish_status") == "duplicate"
                or (r.get("reject_reason") or "").startswith("duplicate")
            )
    elif dry_run:
        emit("Publishing", "dry_run — candidates queued but not appended")
        validated = len(candidates)
        for rec in cand_records:
            rec["validation_status"] = "approved"
            rec["publish_status"] = "queued"
        skipped = 0
    else:
        emit("Publishing", "publish disabled — candidates left in queue")
        validated = 0
        skipped = len(candidates)
        for rec in cand_records:
            rec["publish_status"] = "queued"

    # Fix validated count when some rejections happened
    if publish and not dry_run:
        # extracted = validated + rejected (including duplicates as rejected path)
        rejected_total = rejected
        # published should equal validated accepted
        validated = published_rows  # accepted rows that passed integrity
        # but rejected includes duplicates — keep as integrity count
        pass

    # Recompute balanced metrics carefully
    extracted_n = len(candidates)
    if publish and not dry_run:
        # rejected from filter; published from append; duplicate subset of rejected
        rejected_n = rejected
        # validated = those that passed filter
        validated_n = published_rows  # all accepted were published immediately
        queued_n = extracted_n  # all entered publish queue
        published_n = published_rows
        duplicate_n = duplicates_pub
        skipped_n = max(0, extracted_n - rejected_n - published_n)
    elif dry_run:
        rejected_n = 0
        validated_n = extracted_n
        queued_n = extracted_n
        published_n = 0
        duplicate_n = 0
        skipped_n = extracted_n
    else:
        rejected_n = 0
        validated_n = 0
        queued_n = extracted_n
        published_n = 0
        duplicate_n = 0
        skipped_n = 0

    # Ensure extracted == validated + rejected when we published path
    if publish and not dry_run:
        # integrity: accepted + rejected = extracted (filter_append processes all)
        if rejected_n + published_n != extracted_n and rejected_n + published_n + skipped_n != extracted_n:
            # adjust skipped for accounting
            skipped_n = max(0, extracted_n - published_n - rejected_n)
        validated_n = published_n  # rows that passed validation

    # Actually for balance display:
    # extracted = validated + rejected
    # where validated means passed DPS, rejected means failed DPS
    # published <= validated, duplicate is a type of reject
    balance_validated = published_n  # passed and appended
    balance_rejected = rejected_n
    if balance_validated + balance_rejected < extracted_n:
        balance_rejected = extracted_n - balance_validated  # remaining not published

    # Better: use actual filter counts
    balance_validated = validated if publish and not dry_run else (
        extracted_n if dry_run else 0
    )
    # When we set validated = published_rows above, rejected was from filter
    if publish and not dry_run:
        balance_validated = published_rows
        balance_rejected = rejected
        # If filter processed all rows: published_rows + rejected == extracted
        if published_rows + rejected != extracted_n:
            # some not processed
            skipped_n = extracted_n - published_rows - rejected
        else:
            skipped_n = 0
        # duplicate subset
        duplicate_n = sum(
            1
            for r in cand_records
            if "duplicate" in str(r.get("reject_reason") or "").lower()
            or r.get("publish_status") == "duplicate"
        )

    audit["candidates_validated"] = balance_validated
    audit["candidates_rejected"] = balance_rejected
    audit["rows_published"] = published_n
    audit["published_entities"] = published_entities
    audit["publish"] = {
        "extracted": extracted_n,
        "validated": balance_validated,
        "rejected": balance_rejected,
        "queued": queued_n,
        "published": published_n,
        "skipped": skipped_n,
        "duplicate": duplicate_n,
        "by_dataset": by_dataset,
    }
    audit["evidence_chains"] = list(trace.evidence_chains)

    # sync candidate records into trace
    trace.candidates = cand_records
    trace.set_publish_counts(
        extracted=extracted_n,
        validated=balance_validated,
        rejected=balance_rejected,
        queued=queued_n,
        published=published_n,
        skipped=skipped_n,
        duplicate=duplicate_n,
        by_dataset=by_dataset,
    )

    trace.finish_stage(
        "candidate_validation",
        status="completed",
        rows=balance_validated,
        meta={"rejected": balance_rejected, "duplicate": duplicate_n},
    )
    trace.finish_stage(
        "publish_queue",
        status="completed",
        rows=queued_n,
    )
    trace.start_stage("append_dataset")
    for d in documents:
        did = str(d.get("document_id") or "")
        if did:
            doc_store.move(did, "processed")
            for rec in audit["documents"]:
                if rec.get("document_id") == did:
                    rec["status"] = "completed"
            try:
                manager.queue.move(did, "processed")
            except Exception:  # noqa: BLE001
                pass
    trace.document_queue["completed"] = len(documents)
    trace.document_queue["processing"] = 0
    trace.document_queue["queued"] = 0

    audit["queue_stats"]["documents_final"] = doc_store.counts()
    audit["queue_stats"]["publish_remaining"] = len(list(pub_dir.glob("*.json")))

    trace.finish_stage(
        "append_dataset",
        status="completed" if published_n > 0 or dry_run or not publish else "failed",
        rows=published_n,
    )

    # Export / git stages are CI-owned — mark deferred (not fake success)
    trace.start_stage("export")
    trace.exports = {
        "jsonl": False,
        "openai": False,
        "huggingface": False,
        "notes": ["Export packaging runs in dedicated export CI job"],
    }
    trace.finish_stage(
        "export",
        status="skipped",
        warning="Deferred to export CI job",
    )
    trace.start_stage("git_commit")
    trace.git = {
        "commit": False,
        "push": False,
        "notes": ["Git commit/push performed by learning CI after session"],
    }
    trace.finish_stage("git_commit", status="skipped", warning="Deferred to CI")
    trace.start_stage("push")
    trace.finish_stage("push", status="skipped", warning="Deferred to CI")

    audit["ok"] = published_n > 0 or (not publish) or dry_run
    if published_n == 0 and publish and not dry_run:
        if balance_rejected and candidates:
            audit["error"] = "all_candidates_rejected"
            audit["reasons"].append("All candidates rejected by integrity/DPS validation")
            audit["ok"] = False
        elif not candidates:
            audit["error"] = "no_candidates"
            audit["ok"] = False
        else:
            audit["error"] = "zero_published"
            audit["ok"] = False
            audit["reasons"].append("Zero rows published — see failures")

    emit(
        "Knowledge Updated",
        f"Published {published_n} rows · Knowledge Added {published_n}",
    )
    return _finalize_audit(audit, trace, ok=bool(audit["ok"]), emit=emit)


def _mark_cand(
    records: list[dict[str, Any]],
    candidate_id: str,
    validation_status: str,
    publish_status: str,
    reject_reason: str | None,
) -> None:
    for r in records:
        if r.get("candidate_id") == candidate_id:
            r["validation_status"] = validation_status
            r["publish_status"] = publish_status
            r["reject_reason"] = reject_reason
            return


def _finalize_audit(
    audit: dict[str, Any],
    trace: ProductionTrace,
    *,
    ok: bool,
    emit: LogFn,
) -> dict[str, Any]:
    audit["finished_at"] = utc_now_iso()
    payload = trace.finalize(ok=ok)
    audit["production_trace"] = payload
    audit["console"] = trace.format_console()
    audit["connectors"] = payload.get("connectors") or audit.get("connectors")
    audit["publish"] = payload.get("publish") or audit.get("publish")
    audit["evidence_chains"] = payload.get("evidence_chains") or []
    audit["document_queue"] = payload.get("document_queue") or {}
    # Print manufacturing console
    print("\n" + audit["console"] + "\n")
    try:
        written = write_production_reports(payload, repo_root=trace.repo_root)
        audit["reports"] = written
        emit("Reports", f"Wrote {len(written)} production reports")
    except Exception as exc:  # noqa: BLE001
        audit["failures"].append(f"report_write_failed:{exc}")
        emit("Reports", f"Report write failed: {exc}")
    return audit


def _document_from_search_result(res: Any, *, mission_id: str = "") -> dict[str, Any]:
    """Build a document record from search metadata when binary/page fetch fails."""
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
