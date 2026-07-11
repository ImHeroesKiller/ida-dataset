# Session Trace

**Generated:** 2026-07-11T17:10:54+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260711-29CE5A |
| status | completed |
| mission | Expand company profile, product and solution for outsourcing company in indonesia |
| trigger | mission |
| dry_run | False |
| duration_seconds | 2353.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=95 entity=World Bank document |
| start_time | 2026-07-11T16:30:20+00:00 |
| end_time | 2026-07-11T17:09:33+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 3.0 | — | — | connectors=[{'connector_id': 'CONN-ADB-001', 'name': 'Asian Development Bank', ' |
| connector_calls | completed | — | 21 | — | discovered=21 |
| document_discovery | completed | 97806.2 | 151 | — |  |
| documents_skipped | completed | — | 56 | — | duplicates_or_skips=56 |
| document_download | completed | 1509355.9 | 95 | — | downloaded=95 |
| extraction | completed | 93.4 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=95 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 21 |
| documents_downloaded | 95 |
| documents_duplicates | 56 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
