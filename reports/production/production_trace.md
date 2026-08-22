# Production Trace

**Generated:** 2026-08-22T18:50:39+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-BE5C74`
**Session ID:** `SES-20260822-BDFCDB`
**Started:** 2026-08-22T18:32:59+00:00
**Finished:** 2026-08-22T18:50:39+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6194.3 | 75 | 0 | — |
| document_discovery | completed | 6194.4 | 75 | 0 | — |
| document_download | completed | 305446.7 | 42 | 0 | — |
| extraction | completed | 37.3 | 0 | 5 | — |
| candidate_validation | completed | 19.1 | 0 | 5 | — |
| publish_queue | completed | 19.2 | 0 | 5 | — |
| append_dataset | completed | 22.3 | 0 | 5 | — |
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
