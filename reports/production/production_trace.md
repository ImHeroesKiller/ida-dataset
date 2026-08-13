# Production Trace

**Generated:** 2026-08-13T22:56:50+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-9891A3`
**Session ID:** `SES-20260813-4BC823`
**Started:** 2026-08-13T22:43:44+00:00
**Finished:** 2026-08-13T22:56:50+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.2 | 0 | 0 | — |
| connector | completed | 6153.3 | 47 | 0 | — |
| document_discovery | completed | 6153.4 | 47 | 0 | — |
| document_download | completed | 35523.8 | 31 | 0 | — |
| extraction | completed | 24.2 | 0 | 5 | — |
| candidate_validation | completed | 7.7 | 0 | 5 | — |
| publish_queue | completed | 7.8 | 0 | 5 | — |
| append_dataset | completed | 19.4 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
