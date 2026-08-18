# Production Trace

**Generated:** 2026-08-18T04:02:48+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-D693DF`
**Session ID:** `SES-20260818-E7E992`
**Started:** 2026-08-18T03:49:41+00:00
**Finished:** 2026-08-18T04:02:48+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.7 | 0 | 0 | — |
| source_discovery | completed | 43.6 | 0 | 0 | — |
| connector | completed | 6136.1 | 75 | 0 | — |
| document_discovery | completed | 6136.0 | 75 | 0 | — |
| document_download | completed | 38385.1 | 42 | 0 | — |
| extraction | completed | 50.2 | 0 | 5 | — |
| candidate_validation | completed | 6.9 | 0 | 5 | — |
| publish_queue | completed | 6.9 | 0 | 5 | — |
| append_dataset | completed | 12.8 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
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
