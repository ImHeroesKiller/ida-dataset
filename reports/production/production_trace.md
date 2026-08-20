# Production Trace

**Generated:** 2026-08-20T09:54:11+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-1574F9`
**Session ID:** `SES-20260820-44217A`
**Started:** 2026-08-20T09:36:31+00:00
**Finished:** 2026-08-20T09:54:11+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.7 | 0 | 0 | — |
| source_discovery | completed | 2.2 | 0 | 0 | — |
| connector | completed | 6149.3 | 77 | 0 | — |
| document_discovery | completed | 6149.4 | 77 | 0 | — |
| document_download | completed | 315383.6 | 42 | 0 | — |
| extraction | completed | 25.9 | 0 | 5 | — |
| candidate_validation | completed | 170.5 | 0 | 5 | — |
| publish_queue | completed | 170.5 | 0 | 5 | — |
| append_dataset | completed | 17.0 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
