# Production Trace

**Generated:** 2026-08-19T11:45:53+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-99C52B`
**Session ID:** `SES-20260819-049499`
**Started:** 2026-08-19T11:27:39+00:00
**Finished:** 2026-08-19T11:45:53+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6188.6 | 77 | 0 | — |
| document_discovery | completed | 6188.8 | 77 | 0 | — |
| document_download | completed | 345321.6 | 42 | 0 | — |
| extraction | completed | 31.9 | 0 | 5 | — |
| candidate_validation | completed | 14.0 | 0 | 5 | — |
| publish_queue | completed | 14.0 | 0 | 5 | — |
| append_dataset | completed | 23.3 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.4 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
