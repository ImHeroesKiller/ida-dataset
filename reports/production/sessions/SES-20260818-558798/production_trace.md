# Production Trace

**Generated:** 2026-08-18T18:51:48+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-F3EB99`
**Session ID:** `SES-20260818-558798`
**Started:** 2026-08-18T18:40:39+00:00
**Finished:** 2026-08-18T18:51:48+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6196.2 | 73 | 0 | — |
| document_discovery | completed | 6196.3 | 73 | 0 | — |
| document_download | completed | 39215.0 | 42 | 0 | — |
| extraction | completed | 31.3 | 0 | 5 | — |
| candidate_validation | completed | 14.0 | 0 | 5 | — |
| publish_queue | completed | 14.1 | 0 | 5 | — |
| append_dataset | completed | 23.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.4 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
