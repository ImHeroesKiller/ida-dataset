# Production Trace

**Generated:** 2026-08-23T21:41:17+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-24F9F0`
**Session ID:** `SES-20260823-211666`
**Started:** 2026-08-23T21:23:41+00:00
**Finished:** 2026-08-23T21:41:17+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6199.5 | 77 | 0 | — |
| document_discovery | completed | 6199.7 | 77 | 0 | — |
| document_download | completed | 307083.7 | 42 | 0 | — |
| extraction | completed | 39.5 | 0 | 5 | — |
| candidate_validation | completed | 20.9 | 0 | 5 | — |
| publish_queue | completed | 20.9 | 0 | 5 | — |
| append_dataset | completed | 22.0 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
