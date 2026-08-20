# Production Trace

**Generated:** 2026-08-20T14:54:19+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-C7A69A`
**Session ID:** `SES-20260820-1035B8`
**Started:** 2026-08-20T14:38:07+00:00
**Finished:** 2026-08-20T14:54:19+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6196.7 | 43 | 0 | — |
| document_discovery | completed | 6196.8 | 43 | 0 | — |
| document_download | completed | 348311.0 | 31 | 0 | — |
| extraction | completed | 33.3 | 0 | 5 | — |
| candidate_validation | completed | 15.3 | 0 | 5 | — |
| publish_queue | completed | 15.4 | 0 | 5 | — |
| append_dataset | completed | 18.7 | 0 | 5 | — |
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
