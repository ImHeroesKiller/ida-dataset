# Session Trace

**Generated:** 2026-08-13T00:38:59+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260813-EFF8A4 |
| status | failed |
| mission | Produce Industry Dataset — expand industry_library toward product target |
| trigger | manual |
| dry_run | False |
| duration_seconds | 518.0 |
| knowledge_added | 0 |
| knowledge_rejected | 0 |
| summary | prioritize_search_results() got an unexpected keyword argument 'dataset' |
| start_time | 2026-08-13T00:30:15+00:00 |
| end_time | 2026-08-13T00:38:53+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=industry_library score=908.6 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.3% · priority=100 · deps_met · so |
| source_discovery | completed | — | — | — | connectors=[{'connector_id': 'CONN-CROSSREF-001', 'name': 'Crossref', 'source_id |
| connector_calls | completed | — | 0 | — | discovered=0 |
| document_discovery | completed | — | 0 | — |  |
| documents_skipped | completed | — | 0 | — | duplicates_or_skips=0 |
| document_download | completed | — | 0 | — | downloaded=0 |
| extraction | completed | — | — | — |  |
| validation | completed | — | — | 0 |  |
| publish | completed | — | — | 0 |  |
| commit | skipped | — | — | — | deferred_to_CI |
| end_session | failed | — | — | — | prioritize_search_results() got an unexpected keyword argument 'dataset' |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | — |
| documents_downloaded | 0 |
| documents_duplicates | — |
| candidates_extracted | 0 |
| candidates_validated | — |
| candidates_rejected | — |
| rows_published | 0 |

**Next mission (rank #2):** `—`
