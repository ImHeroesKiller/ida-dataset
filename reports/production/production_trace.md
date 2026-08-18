# Production Trace

**Generated:** 2026-08-18T22:37:03+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-7FDE64`
**Session ID:** `SES-20260818-6B23FF`
**Started:** 2026-08-18T22:25:57+00:00
**Finished:** 2026-08-18T22:37:03+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.7 | 0 | 0 | — |
| source_discovery | completed | 2.0 | 0 | 0 | — |
| connector | completed | 6136.7 | 53 | 0 | — |
| document_discovery | completed | 6136.8 | 53 | 0 | — |
| document_download | completed | 35510.5 | 34 | 0 | — |
| extraction | completed | 21.6 | 0 | 5 | — |
| candidate_validation | completed | 7.0 | 0 | 5 | — |
| publish_queue | completed | 7.1 | 0 | 5 | — |
| append_dataset | completed | 10.4 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.1 | 0 | 0 | — |
| push | skipped | 0.1 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **34**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
