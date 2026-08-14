# Production Trace

**Generated:** 2026-08-14T21:40:22+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-EDFB28`
**Session ID:** `SES-20260814-9191E8`
**Started:** 2026-08-14T21:26:53+00:00
**Finished:** 2026-08-14T21:40:22+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6228.8 | 77 | 0 | — |
| document_discovery | completed | 6228.9 | 77 | 0 | — |
| document_download | completed | 72374.8 | 42 | 0 | — |
| extraction | completed | 25.5 | 0 | 5 | — |
| candidate_validation | completed | 8.5 | 0 | 5 | — |
| publish_queue | completed | 9.2 | 0 | 5 | — |
| append_dataset | completed | 25.4 | 0 | 5 | — |
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
