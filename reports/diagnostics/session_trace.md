# Session Trace

**Generated:** 2026-07-11T12:22:38+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260711-B8F6DE |
| status | completed |
| mission | Expand Industry Library — factory learn cycle |
| trigger | manual |
| dry_run | True |
| duration_seconds | 561.0 |
| knowledge_added | 0 |
| knowledge_rejected | 2 |
| summary | Session completed · published=0 extracted=2 validated=2 rejected=2 docs=61 entity=— · dry_run |
| start_time | 2026-07-11T12:11:55+00:00 |
| end_time | 2026-07-11T12:21:16+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.8 | — | — | connectors=[{'connector_id': 'CONN-CROSSREF-001', 'name': 'Crossref', 'source_id |
| connector_calls | completed | — | 21 | — | discovered=21 |
| document_discovery | completed | 6206.8 | 294 | — |  |
| documents_skipped | completed | — | 56 | — | duplicates_or_skips=56 |
| document_download | completed | 39365.8 | 61 | — | downloaded=61 |
| extraction | completed | 35.0 | — | 2 |  |
| validation | completed | — | — | 2 |  |
| publish | completed | — | — | 0 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=0 extracted=2 validated=2 rejected=2 docs=61 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 21 |
| documents_downloaded | 61 |
| documents_duplicates | 56 |
| candidates_extracted | 2 |
| candidates_validated | 2 |
| candidates_rejected | 2 |
| rows_published | 0 |

**Next mission (rank #2):** `competitor_library`
