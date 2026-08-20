# Production Trace

**Generated:** 2026-08-20T15:53:50+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-C52618`
**Session ID:** `SES-20260820-DC5E08`
**Started:** 2026-08-20T15:35:02+00:00
**Finished:** 2026-08-20T15:53:50+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.4 | 0 | 0 | — |
| source_discovery | completed | 1.8 | 0 | 0 | — |
| connector | completed | 13147.2 | 77 | 0 | — |
| document_discovery | completed | 13147.3 | 77 | 0 | — |
| document_download | completed | 376417.1 | 42 | 0 | — |
| extraction | completed | 21.0 | 0 | 5 | — |
| candidate_validation | completed | 9.0 | 0 | 5 | — |
| publish_queue | completed | 9.0 | 0 | 5 | — |
| append_dataset | completed | 13.4 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
