# Production Trace

**Generated:** 2026-08-23T14:42:51+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-A2BECF`
**Session ID:** `SES-20260823-56FEA9`
**Started:** 2026-08-23T14:25:16+00:00
**Finished:** 2026-08-23T14:42:51+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6197.9 | 77 | 0 | — |
| document_discovery | completed | 6197.9 | 77 | 0 | — |
| document_download | completed | 307418.3 | 42 | 0 | — |
| extraction | completed | 38.2 | 0 | 5 | — |
| candidate_validation | completed | 20.2 | 0 | 5 | — |
| publish_queue | completed | 20.2 | 0 | 5 | — |
| append_dataset | completed | 23.8 | 0 | 5 | — |
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
