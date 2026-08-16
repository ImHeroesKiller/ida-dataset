# Production Trace

**Generated:** 2026-08-16T07:46:32+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-0DAA30`
**Session ID:** `SES-20260816-35B316`
**Started:** 2026-08-16T07:32:17+00:00
**Finished:** 2026-08-16T07:46:32+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6199.6 | 27 | 0 | — |
| document_discovery | completed | 6199.8 | 27 | 0 | — |
| document_download | completed | 108700.1 | 11 | 0 | — |
| extraction | completed | 25.1 | 0 | 5 | — |
| candidate_validation | completed | 10.1 | 0 | 5 | — |
| publish_queue | completed | 10.1 | 0 | 5 | — |
| append_dataset | completed | 10.3 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
