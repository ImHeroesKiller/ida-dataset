# Session Trace

**Generated:** 2026-08-13T15:12:45+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260813-966463 |
| status | completed |
| mission | Produce Industry Dataset — expand industry_library toward product target |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 784.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=31 entity=World Bank document |
| start_time | 2026-08-13T14:59:33+00:00 |
| end_time | 2026-08-13T15:12:37+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=industry_library score=908.1 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.4% · priority=100 · deps_met · so |
| source_discovery | completed | 3.1 | — | — | connectors=[{'connector_id': 'CONN-OPENALEX-001', 'name': 'OpenAlex', 'source_id |
| connector_calls | completed | — | 11 | — | discovered=11 |
| document_discovery | completed | 6213.4 | 47 | — |  |
| documents_skipped | completed | — | 16 | — | duplicates_or_skips=16 |
| document_download | completed | 35501.8 | 31 | — | downloaded=31 |
| extraction | completed | 23.1 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=31 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 11 |
| documents_downloaded | 31 |
| documents_duplicates | 16 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `—`
