# Production Trace

**Generated:** 2026-08-21T21:43:58+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-69DF6F`
**Session ID:** `SES-20260821-1249BA`
**Started:** 2026-08-21T21:26:16+00:00
**Finished:** 2026-08-21T21:43:58+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.5 | 0 | 0 | — |
| source_discovery | completed | 71.9 | 0 | 0 | — |
| connector | completed | 6152.8 | 77 | 0 | — |
| document_discovery | completed | 6152.9 | 77 | 0 | — |
| document_download | completed | 317095.5 | 42 | 0 | — |
| extraction | completed | 21.6 | 0 | 5 | — |
| candidate_validation | completed | 12.8 | 0 | 5 | — |
| publish_queue | completed | 12.8 | 0 | 5 | — |
| append_dataset | completed | 12.9 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
