# Production Trace

**Generated:** 2026-08-22T04:01:25+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-6B7851`
**Session ID:** `SES-20260822-E0F79C`
**Started:** 2026-08-22T03:43:50+00:00
**Finished:** 2026-08-22T04:01:25+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6199.2 | 77 | 0 | — |
| document_discovery | completed | 6199.3 | 77 | 0 | — |
| document_download | completed | 307890.6 | 42 | 0 | — |
| extraction | completed | 37.3 | 0 | 5 | — |
| candidate_validation | completed | 18.1 | 0 | 5 | — |
| publish_queue | completed | 18.2 | 0 | 5 | — |
| append_dataset | completed | 24.2 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
