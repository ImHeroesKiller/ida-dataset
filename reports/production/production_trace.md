# Production Trace

**Generated:** 2026-08-14T23:36:43+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-805120`
**Session ID:** `SES-20260814-196CE0`
**Started:** 2026-08-14T23:23:39+00:00
**Finished:** 2026-08-14T23:36:43+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6157.1 | 47 | 0 | — |
| document_discovery | completed | 6157.2 | 47 | 0 | — |
| document_download | completed | 41585.5 | 31 | 0 | — |
| extraction | completed | 24.6 | 0 | 5 | — |
| candidate_validation | completed | 8.1 | 0 | 5 | — |
| publish_queue | completed | 8.1 | 0 | 5 | — |
| append_dataset | completed | 17.7 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
