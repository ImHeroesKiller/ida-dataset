# Production Trace

**Generated:** 2026-08-14T08:30:16+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-3C9B2F`
**Session ID:** `SES-20260814-88228F`
**Started:** 2026-08-14T08:17:11+00:00
**Finished:** 2026-08-14T08:30:15+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.5 | 0 | 0 | — |
| connector | completed | 6111.2 | 45 | 0 | — |
| document_discovery | completed | 6228.3 | 45 | 0 | — |
| document_download | completed | 35493.0 | 31 | 0 | — |
| extraction | completed | 18.6 | 0 | 5 | — |
| candidate_validation | completed | 121.9 | 0 | 5 | — |
| publish_queue | completed | 122.0 | 0 | 5 | — |
| append_dataset | completed | 13.7 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
