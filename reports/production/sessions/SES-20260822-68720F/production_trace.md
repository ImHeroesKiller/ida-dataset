# Production Trace

**Generated:** 2026-08-22T19:41:34+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-94AF3E`
**Session ID:** `SES-20260822-68720F`
**Started:** 2026-08-22T19:24:12+00:00
**Finished:** 2026-08-22T19:41:34+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6191.9 | 77 | 0 | — |
| document_discovery | completed | 6192.1 | 77 | 0 | — |
| document_download | completed | 307780.4 | 42 | 0 | — |
| extraction | completed | 38.0 | 0 | 5 | — |
| candidate_validation | completed | 18.5 | 0 | 5 | — |
| publish_queue | completed | 18.6 | 0 | 5 | — |
| append_dataset | completed | 23.4 | 0 | 5 | — |
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
