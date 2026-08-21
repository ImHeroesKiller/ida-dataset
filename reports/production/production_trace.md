# Production Trace

**Generated:** 2026-08-21T14:55:33+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-0031E8`
**Session ID:** `SES-20260821-4CF719`
**Started:** 2026-08-21T14:37:04+00:00
**Finished:** 2026-08-21T14:55:33+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.6 | 0 | 0 | — |
| connector | completed | 6149.1 | 47 | 0 | — |
| document_discovery | completed | 6149.2 | 47 | 0 | — |
| document_download | completed | 356062.2 | 31 | 0 | — |
| extraction | completed | 28.1 | 0 | 5 | — |
| candidate_validation | completed | 17.6 | 0 | 5 | — |
| publish_queue | completed | 17.6 | 0 | 5 | — |
| append_dataset | completed | 14.3 | 0 | 5 | — |
| export | skipped | 79.5 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
