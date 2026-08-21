# Production Trace

**Generated:** 2026-08-21T19:45:08+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-F759CB`
**Session ID:** `SES-20260821-2DBD4B`
**Started:** 2026-08-21T19:27:22+00:00
**Finished:** 2026-08-21T19:45:08+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.7 | 0 | 0 | — |
| connector | completed | 6204.0 | 77 | 0 | — |
| document_discovery | completed | 6204.1 | 77 | 0 | — |
| document_download | completed | 321328.0 | 42 | 0 | — |
| extraction | completed | 34.9 | 0 | 5 | — |
| candidate_validation | completed | 16.9 | 0 | 5 | — |
| publish_queue | completed | 16.9 | 0 | 5 | — |
| append_dataset | completed | 22.2 | 0 | 5 | — |
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
