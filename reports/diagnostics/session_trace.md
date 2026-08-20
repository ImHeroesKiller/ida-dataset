# Session Trace

**Generated:** 2026-08-20T10:46:54+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260820-08A8BD |
| status | completed |
| mission | Produce Industry Dataset — expand industry_library toward product target |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 844.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=42 entity=World Bank document |
| start_time | 2026-08-20T10:32:43+00:00 |
| end_time | 2026-08-20T10:46:47+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=industry_library score=908.1 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.4% · priority=100 · deps_met · so |
| source_discovery | completed | 2.9 | — | — | connectors=[{'connector_id': 'CONN-WB-001', 'name': 'World Bank', 'source_id': ' |
| connector_calls | completed | — | 11 | — | discovered=11 |
| document_discovery | completed | 6221.8 | 73 | — |  |
| documents_skipped | completed | — | 31 | — | duplicates_or_skips=31 |
| document_download | completed | 331935.8 | 42 | — | downloaded=42 |
| extraction | completed | 33.5 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=42 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 11 |
| documents_downloaded | 42 |
| documents_duplicates | 31 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `—`
