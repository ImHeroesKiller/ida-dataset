"""Root-cause analysis from diagnostic evidence only — no fix suggestions."""

from __future__ import annotations

from typing import Any


def analyze_root_cause(bundle: dict[str, Any]) -> dict[str, Any]:
    """Determine where production stopped and what evidence proves it."""
    session = bundle.get("session") or {}
    pt = bundle.get("production_trace") or {}
    pub = (bundle.get("publish_trace") or {}).get("balance") or pt.get("publish") or {}
    summary = pt.get("summary") or {}
    stages = bundle.get("execution_stages") or []
    fingerprints = bundle.get("fingerprints") or {}
    mission = (bundle.get("mission") or {}).get("selected") or {}
    docs_disc = int(
        summary.get("documents_discovered")
        or (bundle.get("acquisition") or {}).get("documents_discovered")
        or 0
    )
    docs_dl = int(
        summary.get("documents_downloaded")
        or (bundle.get("acquisition") or {}).get("documents_downloaded")
        or 0
    )
    dups = int(summary.get("documents_duplicates") or 0)
    extracted = int(pub.get("extracted") or summary.get("candidates_extracted") or 0)
    published = int(
        pub.get("published")
        or session.get("knowledge_added")
        or summary.get("rows_published")
        or 0
    )
    rejected = int(
        pub.get("rejected")
        or session.get("knowledge_rejected")
        or summary.get("candidates_rejected")
        or 0
    )
    dry_run = bool(session.get("dry_run"))

    findings: list[dict[str, Any]] = []
    stop_stage = "unknown"
    condition = "insufficient_evidence"
    module = "unknown"
    evidence: list[str] = []

    # Ordered decision tree — first decisive stop wins
    if dry_run and published == 0:
        stop_stage = "publish"
        condition = "session_dry_run_true"
        module = "automation/ci/learning_session.py (dry_run / publish flags)"
        evidence = [
            f"session.dry_run={dry_run}",
            f"knowledge_added={session.get('knowledge_added')}",
            f"extracted={extracted} rejected={rejected}",
            f"summary={session.get('summary')}",
        ]
        findings.append(
            {
                "claim": "No rows published because session ran with dry_run.",
                "evidence": evidence,
            }
        )
    elif docs_disc == 0:
        stop_stage = "connector_calls / document_discovery"
        condition = "no_documents_discovered"
        module = "automation/acquisition/pipeline.py connector search + discovery layer"
        evidence = [
            f"documents_discovered={docs_disc}",
            f"connectors={[(c.get('name'), c.get('status'), c.get('documents_discovered')) for c in (pt.get('connectors') or [])[:8]]}",
        ]
        findings.append({"claim": "Discovery found zero documents.", "evidence": evidence})
    elif docs_disc > 0 and docs_dl == 0:
        stop_stage = "document_download / documents_skipped"
        condition = "all_documents_skipped_or_failed_download"
        module = "automation/acquisition/pipeline.py + fingerprint store + download_manager"
        evidence = [
            f"discovered={docs_disc} downloaded={docs_dl} duplicates={dups}",
            f"fingerprints.urls_known={fingerprints.get('urls_known')}",
            f"fingerprints.stats={fingerprints.get('stats')}",
            f"document_queue={pt.get('document_queue')}",
        ]
        findings.append(
            {
                "claim": "Documents were discovered but none downloaded (skips/duplicates/failures).",
                "evidence": evidence,
            }
        )
    elif docs_dl > 0 and extracted == 0:
        stop_stage = "extraction"
        condition = "no_candidates_extracted"
        module = "automation/acquisition/multi_stage_extract.py / library_extract.py / extractor.py"
        evidence = [
            f"downloaded={docs_dl} extracted={extracted}",
            f"extraction_stats={(bundle.get('extraction_trace') or {}).get('stage_stats')}",
            f"dataset={pt.get('dataset') or mission.get('dataset')}",
        ]
        findings.append(
            {
                "claim": "Documents downloaded but grounded extraction produced zero candidates.",
                "evidence": evidence,
            }
        )
    elif extracted > 0 and published == 0 and rejected >= extracted:
        stop_stage = "validation"
        condition = "all_candidates_rejected_by_integrity"
        module = "automation/quality/integrity_guard.py (filter_append_rows)"
        evidence = [
            f"extracted={extracted} published={published} rejected={rejected}",
            f"publish_balance={pub}",
            f"candidate_rejects={[c.get('reject_reason') for c in ((bundle.get('publish_trace') or {}).get('candidates') or []) if c.get('reject_reason')]}",
            f"session.summary={session.get('summary')}",
        ]
        findings.append(
            {
                "claim": "Candidates extracted but all rejected by validation/integrity.",
                "evidence": evidence,
            }
        )
    elif extracted > 0 and published == 0:
        stop_stage = "publish"
        condition = "candidates_not_appended"
        module = "automation/acquisition/pipeline.py publish path / auto_publish gate"
        evidence = [
            f"extracted={extracted} published={published} rejected={rejected}",
            f"publish_balance={pub}",
            f"dry_run={dry_run}",
            f"candidates={[ (c.get('publish_status'), c.get('reject_reason')) for c in ((bundle.get('publish_trace') or {}).get('candidates') or [])[:12] ]}",
        ]
        findings.append(
            {
                "claim": "Candidates existed but none were published.",
                "evidence": evidence,
            }
        )
    elif published > 0:
        stop_stage = "none (production produced rows)"
        condition = "rows_published"
        module = "append path succeeded"
        evidence = [
            f"published={published}",
            f"extracted={extracted}",
            f"discovered={docs_disc} downloaded={docs_dl} duplicates={dups}",
        ]
        findings.append(
            {
                "claim": "Session published rows; if overnight gap exists, examine later sessions.",
                "evidence": evidence,
            }
        )
    else:
        # High duplicate ratio relative to discovered
        if docs_disc > 0 and dups >= docs_disc * 0.5 and docs_dl < max(1, docs_disc * 0.5):
            stop_stage = "documents_skipped"
            condition = "high_duplicate_fingerprint_skip_rate"
            module = "automation/acquisition/fingerprint.py FingerprintStore.should_skip"
            evidence = [
                f"discovered={docs_disc} downloaded={docs_dl} duplicates={dups}",
                f"fingerprint_urls_known={fingerprints.get('urls_known')}",
                f"fingerprint_stats={fingerprints.get('stats')}",
            ]
            findings.append(
                {
                    "claim": "Majority of discovered documents skipped as duplicates/unchanged.",
                    "evidence": evidence,
                }
            )
        else:
            stop_stage = "end_session"
            condition = "zero_published_unclassified"
            module = "session summary / production_trace"
            evidence = [
                f"session={session.get('session_id')} status={session.get('status')}",
                f"summary={session.get('summary')}",
                f"discovered={docs_disc} downloaded={docs_dl} extracted={extracted} published={published}",
            ]
            findings.append(
                {
                    "claim": "No rows published; stage not fully classified from available fields.",
                    "evidence": evidence,
                }
            )

    # Stage failure annotations from production_trace
    failed_stages = [
        s
        for s in stages
        if str(s.get("status") or "").lower() in {"failed", "error"}
    ]

    # Mission selection context (always include)
    findings.append(
        {
            "claim": "Mission selection outcome (context).",
            "evidence": [
                f"selected_dataset={mission.get('dataset')}",
                f"score={mission.get('score')}",
                f"reason={mission.get('reason')}",
                f"instruction={mission.get('instruction')}",
            ],
        }
    )

    return {
        "why_no_new_rows": (
            f"Production stopped or yielded zero published rows at stage `{stop_stage}` "
            f"due to condition `{condition}`."
            if published == 0
            else f"Latest evidence shows published={published}; zero-row claim may refer to a later window."
        ),
        "stop_stage": stop_stage,
        "condition": condition,
        "module": module,
        "evidence": evidence,
        "findings": findings,
        "metrics": {
            "documents_discovered": docs_disc,
            "documents_downloaded": docs_dl,
            "documents_duplicates": dups,
            "candidates_extracted": extracted,
            "candidates_rejected": rejected,
            "rows_published": published,
            "dry_run": dry_run,
            "fingerprint_urls_known": fingerprints.get("urls_known"),
            "selected_dataset": mission.get("dataset"),
        },
        "failed_stages": failed_stages,
        "session_id": session.get("session_id"),
        "mission_id": session.get("mission_id") or mission.get("batch_id"),
    }
