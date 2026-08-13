# Production Trace

**Generated:** 2026-08-13T05:06:19+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-636CA5`
**Session ID:** `SES-20260813-82AD2B`
**Started:** 2026-08-13T04:52:21+00:00
**Finished:** 2026-08-13T05:06:19+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 15719.2 | 77 | 0 | — |
| document_discovery | completed | 15719.4 | 77 | 0 | — |
| document_download | completed | 78539.4 | 42 | 0 | — |
| extraction | completed | 23.3 | 0 | 5 | — |
| candidate_validation | completed | 6.1 | 0 | 5 | — |
| publish_queue | completed | 6.2 | 0 | 5 | — |
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
