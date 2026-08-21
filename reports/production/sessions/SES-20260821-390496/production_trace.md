# Production Trace

**Generated:** 2026-08-21T22:44:32+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-5585FC`
**Session ID:** `SES-20260821-390496`
**Started:** 2026-08-21T22:26:54+00:00
**Finished:** 2026-08-21T22:44:32+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.2 | 0 | 0 | — |
| connector | completed | 6141.0 | 77 | 0 | — |
| document_discovery | completed | 6169.6 | 77 | 0 | — |
| document_download | completed | 312019.7 | 42 | 0 | — |
| extraction | completed | 21.9 | 0 | 5 | — |
| candidate_validation | completed | 9.5 | 0 | 5 | — |
| publish_queue | completed | 9.5 | 0 | 5 | — |
| append_dataset | completed | 13.2 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.1 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
