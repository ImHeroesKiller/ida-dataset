# Session Trace

**Generated:** 2026-07-12T19:37:50+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260712-9C1F13 |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 1028.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=96 entity=The Influence of Service Quality on Li |
| start_time | 2026-07-12T19:19:20+00:00 |
| end_time | 2026-07-12T19:36:28+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.7 | — | — | connectors=[{'connector_id': 'CONN-ADB-001', 'name': 'Asian Development Bank', ' |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 94006.4 | 178 | — |  |
| documents_skipped | completed | — | 82 | — | duplicates_or_skips=82 |
| document_download | completed | 176842.6 | 96 | — | downloaded=96 |
| extraction | completed | 96.6 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=96 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 96 |
| documents_duplicates | 82 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
