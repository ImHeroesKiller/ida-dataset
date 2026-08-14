# Production Trace

**Generated:** 2026-08-14T11:58:04+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-80604E`
**Session ID:** `SES-20260814-B6076F`
**Started:** 2026-08-14T11:44:56+00:00
**Finished:** 2026-08-14T11:58:04+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.6 | 0 | 0 | — |
| connector | completed | 6251.5 | 77 | 0 | — |
| document_discovery | completed | 6251.7 | 77 | 0 | — |
| document_download | completed | 39195.3 | 42 | 0 | — |
| extraction | completed | 22.5 | 0 | 5 | — |
| candidate_validation | completed | 5.6 | 0 | 5 | — |
| publish_queue | completed | 5.6 | 0 | 5 | — |
| append_dataset | completed | 17.3 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.8 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
