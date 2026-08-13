# Production Trace

**Generated:** 2026-08-13T15:12:37+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-D9D241`
**Session ID:** `SES-20260813-E1C16E`
**Started:** 2026-08-13T14:59:34+00:00
**Finished:** 2026-08-13T15:12:37+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6213.2 | 47 | 0 | — |
| document_discovery | completed | 6213.4 | 47 | 0 | — |
| document_download | completed | 35501.8 | 31 | 0 | — |
| extraction | completed | 23.1 | 0 | 5 | — |
| candidate_validation | completed | 7.1 | 0 | 5 | — |
| publish_queue | completed | 7.2 | 0 | 5 | — |
| append_dataset | completed | 18.9 | 0 | 5 | — |
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
