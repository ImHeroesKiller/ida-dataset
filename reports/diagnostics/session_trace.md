# Session Trace

**Generated:** 2026-07-11T18:00:48+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260711-41DBF5 |
| status | completed |
| mission | Expand Industry Library |
| trigger | mission |
| dry_run | False |
| duration_seconds | 1239.0 |
| knowledge_added | 2 |
| knowledge_rejected | 1 |
| summary | Session completed · published=2 extracted=3 validated=2 rejected=1 docs=90 entity=Halal Industry |
| start_time | 2026-07-11T17:38:48+00:00 |
| end_time | 2026-07-11T17:59:27+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.6 | — | — | connectors=[{'connector_id': 'CONN-ADB-001', 'name': 'Asian Development Bank', ' |
| connector_calls | completed | — | 28 | — | discovered=28 |
| document_discovery | completed | 94110.4 | 204 | — |  |
| documents_skipped | completed | — | 60 | — | duplicates_or_skips=60 |
| document_download | completed | 370722.2 | 90 | — | downloaded=90 |
| extraction | completed | 89.8 | — | 3 |  |
| validation | completed | — | — | 2 |  |
| publish | completed | — | — | 2 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=2 extracted=3 validated=2 rejected=1 docs=90 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 28 |
| documents_downloaded | 90 |
| documents_duplicates | 60 |
| candidates_extracted | 3 |
| candidates_validated | 2 |
| candidates_rejected | 1 |
| rows_published | 2 |

**Next mission (rank #2):** `competitor_library`
