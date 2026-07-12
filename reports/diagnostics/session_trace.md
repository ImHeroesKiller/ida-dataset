# Session Trace

**Generated:** 2026-07-12T07:33:56+00:00

## Session summary

| Field | Value |
| --- | --- |
| session_id | SESSION-20260712-37CE0D |
| status | completed |
| mission | Expand Industry Library — factory learn cycle |
| trigger | manual |
| dry_run | True |
| duration_seconds | 630.0 |
| knowledge_added | 0 |
| knowledge_rejected | 4 |
| summary | Session completed · published=0 extracted=4 validated=4 rejected=4 docs=83 entity=— · dry_run |
| start_time | 2026-07-12T07:22:22+00:00 |
| end_time | 2026-07-12T07:32:52+00:00 |

## Pipeline stages

| Stage | Status | Duration ms | Documents | Rows | Evidence |
| --- | --- | --- | --- | --- | --- |
| mission_selection | completed | — | — | — | selected=service_library score=2137.87 |
| knowledge_gap_evaluation | completed | — | — | — | mode={'mode': 'BOOTSTRAP', 'reason': 'empty_or_below_minimum_datasets', 'empty_d |
| dependency_evaluation | completed | — | — | — | see mission_trace eligible flags |
| mission_eligible | completed | — | — | — | mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · |
| source_discovery | completed | 2.4 | — | — | connectors=[{'connector_id': 'CONN-CROSSREF-001', 'name': 'Crossref', 'source_id |
| connector_calls | completed | — | 21 | — | discovered=21 |
| document_discovery | completed | 6154.7 | 157 | — |  |
| documents_skipped | completed | — | 67 | — | duplicates_or_skips=67 |
| document_download | completed | 129777.6 | 83 | — | downloaded=83 |
| extraction | completed | 54.7 | — | 4 |  |
| validation | completed | — | — | 4 |  |
| publish | completed | — | — | 0 |  |
| commit | skipped | — | — | — | ['Deferred to CI'] |
| end_session | completed | — | — | — | Session completed · published=0 extracted=4 validated=4 rejected=4 docs=83 entit |

## Funnel

| Metric | Value |
| --- | --- |
| documents_discovered | 21 |
| documents_downloaded | 83 |
| documents_duplicates | 67 |
| candidates_extracted | 4 |
| candidates_validated | 4 |
| candidates_rejected | 4 |
| rows_published | 0 |

**Next mission (rank #2):** `competitor_library`
