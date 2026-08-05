# Session Trace

**Generated:** 2026-08-05T13:14:15+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260805-AB3DD6 |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 1091.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=52 entity=Exploring the influence of regional ec |
| start_time | 2026-08-05T12:54:39+00:00 |
| end_time | 2026-08-05T13:12:50+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.9 | — | — | connectors=[{'connector_id': 'CONN-ADB-001', 'name': 'Asian Development Bank', ' |
| connector_calls | completed | — | 21 | — | discovered=21 |
| document_discovery | completed | 94078.9 | 87 | — |  |
| documents_skipped | completed | — | 35 | — | duplicates_or_skips=35 |
| document_download | completed | 237297.2 | 52 | — | downloaded=52 |
| extraction | completed | 99.7 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=52 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 21 |
| documents_downloaded | 52 |
| documents_duplicates | 35 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
