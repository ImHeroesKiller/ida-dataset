# Session Trace

**Generated:** 2026-07-24T07:50:40+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260724-A6E0FB |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 958.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=62 entity=The Influence of Service Quality on Li |
| start_time | 2026-07-24T07:33:18+00:00 |
| end_time | 2026-07-24T07:49:16+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 3.0 | — | — | connectors=[{'connector_id': 'CONN-ADB-001', 'name': 'Asian Development Bank', ' |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 94072.5 | 97 | — |  |
| documents_skipped | completed | — | 35 | — | duplicates_or_skips=35 |
| document_download | completed | 126430.3 | 62 | — | downloaded=62 |
| extraction | completed | 100.5 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=62 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 62 |
| documents_duplicates | 35 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
