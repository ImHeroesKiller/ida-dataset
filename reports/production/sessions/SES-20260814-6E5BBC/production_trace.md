# Production Trace

**Generated:** 2026-08-14T07:53:55+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-DFE3F1`
**Session ID:** `SES-20260814-6E5BBC`
**Started:** 2026-08-14T07:40:42+00:00
**Finished:** 2026-08-14T07:53:55+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.4 | 0 | 0 | — |
| connector | completed | 6239.9 | 47 | 0 | — |
| document_discovery | completed | 6240.1 | 47 | 0 | — |
| document_download | completed | 35567.9 | 31 | 0 | — |
| extraction | completed | 21.3 | 0 | 5 | — |
| candidate_validation | completed | 5.5 | 0 | 5 | — |
| publish_queue | completed | 5.5 | 0 | 5 | — |
| append_dataset | completed | 13.9 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
