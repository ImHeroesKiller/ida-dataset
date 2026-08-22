# Production Trace

**Generated:** 2026-08-22T21:41:08+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-238002`
**Session ID:** `SES-20260822-5ED0D8`
**Started:** 2026-08-22T21:23:26+00:00
**Finished:** 2026-08-22T21:41:08+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6215.1 | 77 | 0 | — |
| document_discovery | completed | 6215.2 | 77 | 0 | — |
| document_download | completed | 316164.7 | 42 | 0 | — |
| extraction | completed | 37.1 | 0 | 5 | — |
| candidate_validation | completed | 19.2 | 0 | 5 | — |
| publish_queue | completed | 19.3 | 0 | 5 | — |
| append_dataset | completed | 23.2 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.4 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
