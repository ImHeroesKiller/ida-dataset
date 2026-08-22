# Production Trace

**Generated:** 2026-08-22T23:40:14+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-90D25B`
**Session ID:** `SES-20260822-D588B9`
**Started:** 2026-08-22T23:22:33+00:00
**Finished:** 2026-08-22T23:40:14+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6151.7 | 47 | 0 | — |
| document_discovery | completed | 6151.8 | 47 | 0 | — |
| document_download | completed | 315796.2 | 31 | 0 | — |
| extraction | completed | 37.4 | 0 | 5 | — |
| candidate_validation | completed | 19.5 | 0 | 5 | — |
| publish_queue | completed | 19.5 | 0 | 5 | — |
| append_dataset | completed | 19.4 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
