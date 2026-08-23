# Production Trace

**Generated:** 2026-08-23T13:51:44+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-7836B8`
**Session ID:** `SES-20260823-D61F66`
**Started:** 2026-08-23T13:34:04+00:00
**Finished:** 2026-08-23T13:51:43+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6204.7 | 43 | 0 | — |
| document_discovery | completed | 6204.9 | 43 | 0 | — |
| document_download | completed | 308763.2 | 31 | 0 | — |
| extraction | completed | 36.7 | 0 | 5 | — |
| candidate_validation | completed | 19.2 | 0 | 5 | — |
| publish_queue | completed | 19.1 | 0 | 5 | — |
| append_dataset | completed | 18.8 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
