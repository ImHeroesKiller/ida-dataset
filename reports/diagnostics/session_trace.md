# Session Trace

**Generated:** 2026-07-17T12:15:10+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260717-907A03 |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 2265.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=73 entity=The Influence of Service Quality on Li |
| start_time | 2026-07-17T11:36:02+00:00 |
| end_time | 2026-07-17T12:13:47+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.8 | — | — | connectors=[{'connector_id': 'CONN-OECD-001', 'name': 'OECD', 'source_id': 'SRC- |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 94094.3 | 97 | — |  |
| documents_skipped | completed | — | 24 | — | duplicates_or_skips=24 |
| document_download | completed | 1440196.2 | 73 | — | downloaded=73 |
| extraction | completed | 95.7 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=73 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 73 |
| documents_duplicates | 24 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
