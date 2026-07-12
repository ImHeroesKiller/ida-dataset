# Session Trace

**Generated:** 2026-07-12T18:23:54+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260712-B8F796 |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 1353.0 |
| knowledge_added | 1 |
| knowledge_rejected | 0 |
| summary | Session completed · published=1 extracted=1 validated=1 rejected=0 docs=133 entity=Green Industry |
| start_time | 2026-07-12T18:00:28+00:00 |
| end_time | 2026-07-12T18:23:01+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 1.8 | — | — | connectors=[{'connector_id': 'CONN-ADB-001', 'name': 'Asian Development Bank', ' |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 94241.0 | 234 | — |  |
| documents_skipped | completed | — | 101 | — | duplicates_or_skips=101 |
| document_download | completed | 483987.6 | 133 | — | downloaded=133 |
| extraction | completed | 54.3 | — | 1 |  |
| validation | completed | — | — | 1 |  |
| publish | completed | — | — | 1 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=1 extracted=1 validated=1 rejected=0 docs=133 enti |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 133 |
| documents_duplicates | 101 |
| candidates_extracted | 1 |
| candidates_validated | 1 |
| candidates_rejected | 0 |
| rows_published | 1 |

**Next mission (rank #2):** `competitor_library`
