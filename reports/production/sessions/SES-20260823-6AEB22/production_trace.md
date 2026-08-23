# Production Trace

**Generated:** 2026-08-23T16:45:43+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-3E3396`
**Session ID:** `SES-20260823-6AEB22`
**Started:** 2026-08-23T16:28:10+00:00
**Finished:** 2026-08-23T16:45:43+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6177.9 | 77 | 0 | — |
| document_discovery | completed | 6178.0 | 77 | 0 | — |
| document_download | completed | 308874.9 | 42 | 0 | — |
| extraction | completed | 38.6 | 0 | 5 | — |
| candidate_validation | completed | 20.2 | 0 | 5 | — |
| publish_queue | completed | 20.2 | 0 | 5 | — |
| append_dataset | completed | 22.2 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
