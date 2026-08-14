# Production Trace

**Generated:** 2026-08-14T06:28:22+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-E884A1`
**Session ID:** `SES-20260814-7D7795`
**Started:** 2026-08-14T06:15:19+00:00
**Finished:** 2026-08-14T06:28:22+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6190.8 | 77 | 0 | — |
| document_discovery | completed | 6190.9 | 77 | 0 | — |
| document_download | completed | 39384.1 | 42 | 0 | — |
| extraction | completed | 24.2 | 0 | 5 | — |
| candidate_validation | completed | 7.0 | 0 | 5 | — |
| publish_queue | completed | 7.0 | 0 | 5 | — |
| append_dataset | completed | 21.8 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
