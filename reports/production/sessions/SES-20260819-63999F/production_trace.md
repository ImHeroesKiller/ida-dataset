# Production Trace

**Generated:** 2026-08-19T10:49:32+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-7B8A61`
**Session ID:** `SES-20260819-63999F`
**Started:** 2026-08-19T10:31:37+00:00
**Finished:** 2026-08-19T10:49:32+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.2 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6224.5 | 77 | 0 | — |
| document_discovery | completed | 6224.6 | 77 | 0 | — |
| document_download | completed | 331363.6 | 42 | 0 | — |
| extraction | completed | 32.1 | 0 | 5 | — |
| candidate_validation | completed | 14.0 | 0 | 5 | — |
| publish_queue | completed | 14.1 | 0 | 5 | — |
| append_dataset | completed | 24.7 | 0 | 5 | — |
| export | skipped | 0.9 | 0 | 0 | — |
| git_commit | skipped | 0.5 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
