# Production Trace

**Generated:** 2026-08-18T01:30:19+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-8DD447`
**Session ID:** `SES-20260818-DF37AD`
**Started:** 2026-08-18T01:18:31+00:00
**Finished:** 2026-08-18T01:30:19+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6194.8 | 73 | 0 | — |
| document_discovery | completed | 6194.9 | 73 | 0 | — |
| document_download | completed | 81754.6 | 42 | 0 | — |
| extraction | completed | 29.6 | 0 | 5 | — |
| candidate_validation | completed | 12.0 | 0 | 5 | — |
| publish_queue | completed | 12.0 | 0 | 5 | — |
| append_dataset | completed | 23.4 | 0 | 5 | — |
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
