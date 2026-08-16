# Production Trace

**Generated:** 2026-08-16T01:38:16+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-53996B`
**Session ID:** `SES-20260816-279E7B`
**Started:** 2026-08-16T01:23:32+00:00
**Finished:** 2026-08-16T01:38:16+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6173.3 | 27 | 0 | — |
| document_discovery | completed | 6173.4 | 27 | 0 | — |
| document_download | completed | 137779.3 | 11 | 0 | — |
| extraction | completed | 24.7 | 0 | 5 | — |
| candidate_validation | completed | 9.8 | 0 | 5 | — |
| publish_queue | completed | 9.8 | 0 | 5 | — |
| append_dataset | completed | 10.4 | 0 | 5 | — |
| export | skipped | 0.5 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
