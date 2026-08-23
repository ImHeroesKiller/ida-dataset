# Production Trace

**Generated:** 2026-08-23T01:43:39+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-8C0FE1`
**Session ID:** `SES-20260823-E6D596`
**Started:** 2026-08-23T01:25:28+00:00
**Finished:** 2026-08-23T01:43:39+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6209.6 | 77 | 0 | — |
| document_discovery | completed | 6209.7 | 77 | 0 | — |
| document_download | completed | 344537.1 | 42 | 0 | — |
| extraction | completed | 38.4 | 0 | 5 | — |
| candidate_validation | completed | 18.8 | 0 | 5 | — |
| publish_queue | completed | 18.8 | 0 | 5 | — |
| append_dataset | completed | 23.9 | 0 | 5 | — |
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
