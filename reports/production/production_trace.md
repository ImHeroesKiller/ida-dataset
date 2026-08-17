# Production Trace

**Generated:** 2026-08-17T22:40:02+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-6E3548`
**Session ID:** `SES-20260817-F5D0E0`
**Started:** 2026-08-17T22:27:03+00:00
**Finished:** 2026-08-17T22:40:02+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.3 | 0 | 0 | — |
| connector | completed | 6223.7 | 75 | 0 | — |
| document_discovery | completed | 6223.8 | 75 | 0 | — |
| document_download | completed | 37412.5 | 42 | 0 | — |
| extraction | completed | 29.8 | 0 | 5 | — |
| candidate_validation | completed | 12.5 | 0 | 5 | — |
| publish_queue | completed | 12.4 | 0 | 5 | — |
| append_dataset | completed | 24.1 | 0 | 5 | — |
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
