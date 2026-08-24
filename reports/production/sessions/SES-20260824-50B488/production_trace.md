# Production Trace

**Generated:** 2026-08-24T23:38:42+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260824-C58635`
**Session ID:** `SES-20260824-50B488`
**Started:** 2026-08-24T23:23:59+00:00
**Finished:** 2026-08-24T23:38:42+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.2 | 0 | 0 | — |
| source_discovery | completed | 3.3 | 0 | 0 | — |
| connector | completed | 6196.4 | 23 | 0 | — |
| document_discovery | completed | 6196.6 | 23 | 0 | — |
| document_download | completed | 317654.5 | 11 | 0 | — |
| extraction | completed | 38.0 | 0 | 5 | — |
| candidate_validation | completed | 20.8 | 0 | 5 | — |
| publish_queue | completed | 20.8 | 0 | 5 | — |
| append_dataset | completed | 10.3 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
