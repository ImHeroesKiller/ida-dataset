# Production Trace

**Generated:** 2026-08-18T05:41:28+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-88C7D1`
**Session ID:** `SES-20260818-942272`
**Started:** 2026-08-18T05:31:53+00:00
**Finished:** 2026-08-18T05:41:28+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 2.1 | 0 | 0 | — |
| connector | completed | 6164.6 | 53 | 0 | — |
| document_discovery | completed | 6164.8 | 53 | 0 | — |
| document_download | completed | 35460.9 | 34 | 0 | — |
| extraction | completed | 22.5 | 0 | 5 | — |
| candidate_validation | completed | 8.4 | 0 | 5 | — |
| publish_queue | completed | 8.4 | 0 | 5 | — |
| append_dataset | completed | 10.9 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **34**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
