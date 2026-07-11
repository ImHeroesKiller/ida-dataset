# Session Trace

**Generated:** 2026-07-11T14:49:15+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260711-CA5D36 |
| status | completed |
| mission | Expand Industry Library — factory learn cycle |
| trigger | manual |
| dry_run | True |
| duration_seconds | 623.0 |
| knowledge_added | 0 |
| knowledge_rejected | 3 |
| summary | Session completed · published=0 extracted=3 validated=3 rejected=3 docs=82 entity=— · dry_run |
| start_time | 2026-07-11T14:37:31+00:00 |
| end_time | 2026-07-11T14:47:54+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.9 | — | — | connectors=[{'connector_id': 'CONN-CROSSREF-001', 'name': 'Crossref', 'source_id |
| connector_calls | completed | — | 21 | — | discovered=21 |
| document_discovery | completed | 6180.2 | 283 | — |  |
| documents_skipped | completed | — | 68 | — | duplicates_or_skips=68 |
| document_download | completed | 112546.0 | 82 | — | downloaded=82 |
| extraction | completed | 67.7 | — | 3 |  |
| validation | completed | — | — | 3 |  |
| publish | completed | — | — | 0 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=0 extracted=3 validated=3 rejected=3 docs=82 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 21 |
| documents_downloaded | 82 |
| documents_duplicates | 68 |
| candidates_extracted | 3 |
| candidates_validated | 3 |
| candidates_rejected | 3 |
| rows_published | 0 |

**Next mission (rank #2):** `competitor_library`
