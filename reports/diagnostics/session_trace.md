# Session Trace

**Generated:** 2026-08-08T15:50:07+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260808-B626D9 |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 990.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=32 entity=Exploring the influence of regional ec |
| start_time | 2026-08-08T15:32:13+00:00 |
| end_time | 2026-08-08T15:48:43+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 3.1 | — | — | connectors=[{'connector_id': 'CONN-ADB-001', 'name': 'Asian Development Bank', ' |
| connector_calls | completed | — | 21 | — | discovered=21 |
| document_discovery | completed | 94132.4 | 65 | — |  |
| documents_skipped | completed | — | 33 | — | duplicates_or_skips=33 |
| document_download | completed | 113480.2 | 32 | — | downloaded=32 |
| extraction | completed | 101.9 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=32 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 21 |
| documents_downloaded | 32 |
| documents_duplicates | 33 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
