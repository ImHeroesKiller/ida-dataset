# Production Trace

**Generated:** 2026-08-13T19:27:19+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-FB9941`
**Session ID:** `SES-20260813-4F2280`
**Started:** 2026-08-13T19:14:09+00:00
**Finished:** 2026-08-13T19:27:19+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6192.9 | 75 | 0 | — |
| document_discovery | completed | 6193.1 | 75 | 0 | — |
| document_download | completed | 38818.2 | 42 | 0 | — |
| extraction | completed | 23.8 | 0 | 5 | — |
| candidate_validation | completed | 7.1 | 0 | 5 | — |
| publish_queue | completed | 7.1 | 0 | 5 | — |
| append_dataset | completed | 23.2 | 0 | 5 | — |
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
