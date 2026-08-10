# Session Trace

**Generated:** 2026-08-10T22:56:54+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260810-983065 |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 968.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=51 entity=Exploring the influence of regional ec |
| start_time | 2026-08-10T22:39:22+00:00 |
| end_time | 2026-08-10T22:55:30+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.8 | — | — | connectors=[{'connector_id': 'CONN-OECD-001', 'name': 'OECD', 'source_id': 'SRC- |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 94150.3 | 67 | — |  |
| documents_skipped | completed | — | 16 | — | duplicates_or_skips=16 |
| document_download | completed | 114173.9 | 51 | — | downloaded=51 |
| extraction | completed | 115.9 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=51 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 51 |
| documents_duplicates | 16 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
