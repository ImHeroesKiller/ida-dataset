# Session Trace

**Generated:** 2026-07-12T03:54:29+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260712-A029B2 |
| status | completed |
| mission | corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_libra |
| trigger | schedule |
| dry_run | False |
| duration_seconds | 1086.0 |
| knowledge_added | 5 |
| knowledge_rejected | 0 |
| summary | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=147 entity=The Influence of Service Quality on L |
| start_time | 2026-07-12T03:35:00+00:00 |
| end_time | 2026-07-12T03:53:06+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.9 | — | — | connectors=[{'connector_id': 'CONN-OECD-001', 'name': 'OECD', 'source_id': 'SRC- |
| connector_calls | completed | — | 31 | — | discovered=31 |
| document_discovery | completed | 94147.8 | 235 | — |  |
| documents_skipped | completed | — | 88 | — | duplicates_or_skips=88 |
| document_download | completed | 213300.7 | 147 | — | downloaded=147 |
| extraction | completed | 97.5 | — | 5 |  |
| validation | completed | — | — | 5 |  |
| publish | completed | — | — | 5 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=5 extracted=5 validated=5 rejected=0 docs=147 enti |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 31 |
| documents_downloaded | 147 |
| documents_duplicates | 88 |
| candidates_extracted | 5 |
| candidates_validated | 5 |
| candidates_rejected | 0 |
| rows_published | 5 |

**Next mission (rank #2):** `competitor_library`
