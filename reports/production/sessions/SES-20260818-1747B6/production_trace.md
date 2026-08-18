# Production Trace

**Generated:** 2026-08-18T04:46:52+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-93B68C`
**Session ID:** `SES-20260818-1747B6`
**Started:** 2026-08-18T04:37:25+00:00
**Finished:** 2026-08-18T04:46:52+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.7 | 0 | 0 | — |
| connector | completed | 6239.9 | 73 | 0 | — |
| document_discovery | completed | 6240.1 | 73 | 0 | — |
| document_download | completed | 39985.3 | 42 | 0 | — |
| extraction | completed | 27.3 | 0 | 5 | — |
| candidate_validation | completed | 9.6 | 0 | 5 | — |
| publish_queue | completed | 9.6 | 0 | 5 | — |
| append_dataset | completed | 17.5 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
