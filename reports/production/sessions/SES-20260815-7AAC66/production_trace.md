# Production Trace

**Generated:** 2026-08-15T10:36:56+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-4B05B0`
**Session ID:** `SES-20260815-7AAC66`
**Started:** 2026-08-15T10:23:54+00:00
**Finished:** 2026-08-15T10:36:56+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.4 | 0 | 0 | — |
| source_discovery | completed | 1.8 | 0 | 0 | — |
| connector | completed | 6242.6 | 47 | 0 | — |
| document_discovery | completed | 6242.7 | 47 | 0 | — |
| document_download | completed | 35366.6 | 31 | 0 | — |
| extraction | completed | 15.8 | 0 | 5 | — |
| candidate_validation | completed | 4.6 | 0 | 5 | — |
| publish_queue | completed | 4.6 | 0 | 5 | — |
| append_dataset | completed | 8.8 | 0 | 5 | — |
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
