# Session Trace

**Generated:** 2026-07-12T11:31:27+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260712-A064BA |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 1055.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=144 entity=The Influence of Service Quality on L |
| start_time | 2026-07-12T11:12:28+00:00 |
| end_time | 2026-07-12T11:30:03+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.9 | — | — | connectors=[{'connector_id': 'CONN-ADB-001', 'name': 'Asian Development Bank', ' |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 93872.3 | 235 | — |  |
| documents_skipped | completed | — | 91 | — | duplicates_or_skips=91 |
| document_download | completed | 195407.8 | 144 | — | downloaded=144 |
| extraction | completed | 102.4 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=144 enti |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 144 |
| documents_duplicates | 91 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
