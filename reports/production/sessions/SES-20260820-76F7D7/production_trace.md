# Production Trace

**Generated:** 2026-08-20T19:51:52+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-55B43A`
**Session ID:** `SES-20260820-76F7D7`
**Started:** 2026-08-20T19:33:27+00:00
**Finished:** 2026-08-20T19:51:52+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6185.2 | 77 | 0 | — |
| document_discovery | completed | 6185.3 | 77 | 0 | — |
| document_download | completed | 361043.6 | 42 | 0 | — |
| extraction | completed | 34.5 | 0 | 5 | — |
| candidate_validation | completed | 16.0 | 0 | 5 | — |
| publish_queue | completed | 16.1 | 0 | 5 | — |
| append_dataset | completed | 22.0 | 0 | 5 | — |
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
