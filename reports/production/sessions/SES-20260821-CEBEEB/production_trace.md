# Production Trace

**Generated:** 2026-08-21T13:09:15+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-B825A0`
**Session ID:** `SES-20260821-CEBEEB`
**Started:** 2026-08-21T12:51:17+00:00
**Finished:** 2026-08-21T13:09:15+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.7 | 0 | 0 | — |
| source_discovery | completed | 2.4 | 0 | 0 | — |
| connector | completed | 6351.2 | 43 | 0 | — |
| document_discovery | completed | 6351.4 | 43 | 0 | — |
| document_download | completed | 323976.2 | 31 | 0 | — |
| extraction | completed | 165.3 | 0 | 5 | — |
| candidate_validation | completed | 13.9 | 0 | 5 | — |
| publish_queue | completed | 14.0 | 0 | 5 | — |
| append_dataset | completed | 12.0 | 0 | 5 | — |
| export | skipped | 0.7 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
