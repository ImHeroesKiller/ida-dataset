# Production Trace

**Generated:** 2026-08-17T17:37:22+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-FDB669`
**Session ID:** `SES-20260817-AD1FB5`
**Started:** 2026-08-17T17:27:56+00:00
**Finished:** 2026-08-17T17:37:22+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.1 | 0 | 0 | — |
| connector | completed | 6248.0 | 73 | 0 | — |
| document_discovery | completed | 6248.1 | 73 | 0 | — |
| document_download | completed | 37416.4 | 42 | 0 | — |
| extraction | completed | 41.8 | 0 | 5 | — |
| candidate_validation | completed | 5.9 | 0 | 5 | — |
| publish_queue | completed | 5.8 | 0 | 5 | — |
| append_dataset | completed | 16.7 | 0 | 5 | — |
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
