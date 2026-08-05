# Session Trace

**Generated:** 2026-08-05T09:01:42+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260805-64B07B |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 865.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=34 entity=Exploring the influence of regional ec |
| start_time | 2026-08-05T08:45:53+00:00 |
| end_time | 2026-08-05T09:00:18+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 3.0 | — | — | connectors=[{'connector_id': 'CONN-BPS-001', 'name': 'BPS Indonesia', 'source_id |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 93983.2 | 53 | — |  |
| documents_skipped | completed | — | 19 | — | duplicates_or_skips=19 |
| document_download | completed | 110998.3 | 34 | — | downloaded=34 |
| extraction | completed | 110.3 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=34 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 34 |
| documents_duplicates | 19 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
