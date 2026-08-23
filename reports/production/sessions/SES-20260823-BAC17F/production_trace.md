# Production Trace

**Generated:** 2026-08-23T17:40:33+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-6183E4`
**Session ID:** `SES-20260823-BAC17F`
**Started:** 2026-08-23T17:22:03+00:00
**Finished:** 2026-08-23T17:40:33+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.7 | 0 | 0 | — |
| connector | completed | 6225.5 | 45 | 0 | — |
| document_discovery | completed | 6225.6 | 45 | 0 | — |
| document_download | completed | 356428.7 | 31 | 0 | — |
| extraction | completed | 38.6 | 0 | 5 | — |
| candidate_validation | completed | 20.1 | 0 | 5 | — |
| publish_queue | completed | 20.1 | 0 | 5 | — |
| append_dataset | completed | 19.3 | 0 | 5 | — |
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
