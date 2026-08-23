# Production Trace

**Generated:** 2026-08-23T11:40:02+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-7EA4C7`
**Session ID:** `SES-20260823-55B89D`
**Started:** 2026-08-23T11:22:27+00:00
**Finished:** 2026-08-23T11:40:02+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6199.0 | 77 | 0 | — |
| document_discovery | completed | 6199.1 | 77 | 0 | — |
| document_download | completed | 311317.9 | 42 | 0 | — |
| extraction | completed | 38.4 | 0 | 5 | — |
| candidate_validation | completed | 19.3 | 0 | 5 | — |
| publish_queue | completed | 19.4 | 0 | 5 | — |
| append_dataset | completed | 23.5 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
