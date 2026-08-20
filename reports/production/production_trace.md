# Production Trace

**Generated:** 2026-08-20T08:58:23+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-28F8BF`
**Session ID:** `SES-20260820-DEF8E3`
**Started:** 2026-08-20T08:40:33+00:00
**Finished:** 2026-08-20T08:58:23+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 16.3 | 0 | 0 | — |
| connector | completed | 6488.9 | 75 | 0 | — |
| document_discovery | completed | 6489.3 | 75 | 0 | — |
| document_download | completed | 314939.7 | 42 | 0 | — |
| extraction | completed | 26.0 | 0 | 5 | — |
| candidate_validation | completed | 10.9 | 0 | 5 | — |
| publish_queue | completed | 11.0 | 0 | 5 | — |
| append_dataset | completed | 20.8 | 0 | 5 | — |
| export | skipped | 1.2 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
