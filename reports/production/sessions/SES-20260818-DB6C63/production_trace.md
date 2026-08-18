# Production Trace

**Generated:** 2026-08-18T13:03:12+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-1DE3C2`
**Session ID:** `SES-20260818-DB6C63`
**Started:** 2026-08-18T12:50:01+00:00
**Finished:** 2026-08-18T13:03:12+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.2 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6165.2 | 77 | 0 | — |
| document_discovery | completed | 6165.4 | 77 | 0 | — |
| document_download | completed | 45154.3 | 42 | 0 | — |
| extraction | completed | 30.8 | 0 | 5 | — |
| candidate_validation | completed | 13.2 | 0 | 5 | — |
| publish_queue | completed | 13.2 | 0 | 5 | — |
| append_dataset | completed | 23.6 | 0 | 5 | — |
| export | skipped | 0.5 | 0 | 0 | — |
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
