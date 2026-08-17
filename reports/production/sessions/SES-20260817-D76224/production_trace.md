# Production Trace

**Generated:** 2026-08-17T21:41:20+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-6E3E87`
**Session ID:** `SES-20260817-D76224`
**Started:** 2026-08-17T21:28:13+00:00
**Finished:** 2026-08-17T21:41:20+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.6 | 0 | 0 | — |
| connector | completed | 6239.1 | 25 | 0 | — |
| document_discovery | completed | 6239.2 | 25 | 0 | — |
| document_download | completed | 35530.8 | 11 | 0 | — |
| extraction | completed | 24.5 | 0 | 5 | — |
| candidate_validation | completed | 9.3 | 0 | 5 | — |
| publish_queue | completed | 9.3 | 0 | 5 | — |
| append_dataset | completed | 8.2 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
