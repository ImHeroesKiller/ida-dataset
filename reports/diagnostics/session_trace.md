# Session Trace

**Generated:** 2026-07-11T13:10:45+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260711-CF5FA7 |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 2163.0 |
| knowledge_added | 2 |
| knowledge_rejected | 0 |
| summary | Session completed · published=2 extracted=2 validated=2 rejected=0 docs=277 entity=Startup Ecosystem |
| start_time | 2026-07-11T12:33:21+00:00 |
| end_time | 2026-07-11T13:09:24+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.9 | — | — | connectors=[{'connector_id': 'CONN-OECD-001', 'name': 'OECD', 'source_id': 'SRC- |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 94176.2 | 627 | — |  |
| documents_skipped | completed | — | 223 | — | duplicates_or_skips=223 |
| document_download | completed | 1263152.2 | 277 | — | downloaded=277 |
| extraction | completed | 61.2 | — | 2 |  |
| validation | completed | — | — | 2 |  |
| publish | completed | — | — | 2 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=2 extracted=2 validated=2 rejected=0 docs=277 enti |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 277 |
| documents_duplicates | 223 |
| candidates_extracted | 2 |
| candidates_validated | 2 |
| candidates_rejected | 0 |
| rows_published | 2 |

**Next mission (rank #2):** `competitor_library`
