# Session Trace

**Generated:** 2026-07-13T16:55:52+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260713-AA142C |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 1078.0 |
| knowledge_added | 1 |
| knowledge_rejected | 0 |
| summary | Session completed · published=1 extracted=1 validated=1 rejected=0 docs=95 entity=Industrial Estates & SEZ |
| start_time | 2026-07-13T16:36:31+00:00 |
| end_time | 2026-07-13T16:54:29+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.8 | — | — | connectors=[{'connector_id': 'CONN-ADB-001', 'name': 'Asian Development Bank', ' |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 94016.8 | 177 | — |  |
| documents_skipped | completed | — | 82 | — | duplicates_or_skips=82 |
| document_download | completed | 214326.9 | 95 | — | downloaded=95 |
| extraction | completed | 90.2 | — | 1 |  |
| validation | completed | — | — | 1 |  |
| publish | completed | — | — | 1 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=1 extracted=1 validated=1 rejected=0 docs=95 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 95 |
| documents_duplicates | 82 |
| candidates_extracted | 1 |
| candidates_validated | 1 |
| candidates_rejected | 0 |
| rows_published | 1 |

**Next mission (rank #2):** `competitor_library`
