# Production Trace

**Generated:** 2026-08-20T13:10:07+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-334F06`
**Session ID:** `SES-20260820-4397BC`
**Started:** 2026-08-20T12:52:23+00:00
**Finished:** 2026-08-20T13:10:07+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 6.2 | 0 | 0 | — |
| source_discovery | completed | 152.9 | 0 | 0 | — |
| connector | completed | 6145.3 | 47 | 0 | — |
| document_discovery | completed | 6145.4 | 47 | 0 | — |
| document_download | completed | 312108.3 | 31 | 0 | — |
| extraction | completed | 25.1 | 0 | 5 | — |
| candidate_validation | completed | 12.1 | 0 | 5 | — |
| publish_queue | completed | 12.1 | 0 | 5 | — |
| append_dataset | completed | 14.0 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
