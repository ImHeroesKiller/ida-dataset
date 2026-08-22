# Production Trace

**Generated:** 2026-08-22T03:11:19+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-10DBB5`
**Session ID:** `SES-20260822-1A5612`
**Started:** 2026-08-22T02:55:44+00:00
**Finished:** 2026-08-22T03:11:19+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 2.0 | 0 | 0 | — |
| connector | completed | 6132.8 | 43 | 0 | — |
| document_discovery | completed | 6132.9 | 43 | 0 | — |
| document_download | completed | 318579.4 | 31 | 0 | — |
| extraction | completed | 20.5 | 0 | 5 | — |
| candidate_validation | completed | 71.9 | 0 | 5 | — |
| publish_queue | completed | 72.4 | 0 | 5 | — |
| append_dataset | completed | 31.5 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.4 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
