# Session Trace

**Generated:** 2026-08-18T16:43:35+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260818-227F02 |
| status | completed |
| mission | Produce Industry Dataset — expand industry_library toward product target |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 566.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=34 entity=World Bank document |
| start_time | 2026-08-18T16:34:01+00:00 |
| end_time | 2026-08-18T16:43:27+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=industry_library score=908.1 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.4% · priority=100 · deps_met · so |
| source_discovery | completed | 2.9 | — | — | connectors=[{'connector_id': 'CONN-CROSSREF-001', 'name': 'Crossref', 'source_id |
| connector_calls | completed | — | 11 | — | discovered=11 |
| document_discovery | completed | 6223.6 | 53 | — |  |
| documents_skipped | completed | — | 19 | — | duplicates_or_skips=19 |
| document_download | completed | 35493.8 | 34 | — | downloaded=34 |
| extraction | completed | 30.4 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=34 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 11 |
| documents_downloaded | 34 |
| documents_duplicates | 19 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `—`
