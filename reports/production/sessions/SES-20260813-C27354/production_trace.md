# Production Trace

**Generated:** 2026-08-13T01:08:27+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-E95C7C`
**Session ID:** `SES-20260813-C27354`
**Started:** 2026-08-13T00:54:24+00:00
**Finished:** 2026-08-13T01:08:27+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6193.4 | 46 | 0 | — |
| document_discovery | completed | 6193.6 | 46 | 0 | — |
| document_download | completed | 79270.9 | 31 | 0 | — |
| extraction | completed | 24.1 | 0 | 7 | — |
| candidate_validation | completed | 8.0 | 0 | 4 | — |
| publish_queue | completed | 8.0 | 0 | 7 | — |
| append_dataset | completed | 19.6 | 0 | 4 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **7**
- Candidates validated: **4**
- Candidates rejected: **3**
- Rows published: **4**
- Duplicates: **0**
