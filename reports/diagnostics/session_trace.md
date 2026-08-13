# Session Trace

**Generated:** 2026-08-13T00:05:10+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260812-299AA2 |
| status | completed |
| mission | corporate finance — industry knowledge for Finance — continuous knowledge manufacturing for industry_library across ente |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 1226.0 |
| knowledge_added | 14 |
| knowledge_rejected | 26 |
| summary | Session completed · published=14 extracted=40 validated=14 rejected=26 docs=51 entity=Tourism & Travel Services |
| start_time | 2026-08-12T23:43:31+00:00 |
| end_time | 2026-08-13T00:03:57+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=industry_library score=1904.83 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=87.823 · stretch_cov=0.3% · priority=100 · deps_met · |
| source_discovery | completed | 2.7 | — | — | connectors=[{'connector_id': 'CONN-OECD-001', 'name': 'OECD', 'source_id': 'SRC- |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 93833.4 | 67 | — |  |
| documents_skipped | completed | — | 16 | — | duplicates_or_skips=16 |
| document_download | completed | 350339.4 | 51 | — | downloaded=51 |
| extraction | completed | 86.0 | — | 40 |  |
| validation | completed | — | — | 14 |  |
| publish | completed | — | — | 14 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=14 extracted=40 validated=14 rejected=26 docs=51 e |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 51 |
| documents_duplicates | 16 |
| candidates_extracted | 40 |
| candidates_validated | 14 |
| candidates_rejected | 26 |
| rows_published | 14 |

**Next mission (rank #2):** `solution_library`
