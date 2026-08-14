# Production Trace

**Generated:** 2026-08-14T20:46:06+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-32F73A`
**Session ID:** `SES-20260814-D99890`
**Started:** 2026-08-14T20:33:02+00:00
**Finished:** 2026-08-14T20:46:06+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 301.0 | 0 | 0 | — |
| source_discovery | completed | 2.1 | 0 | 0 | — |
| connector | completed | 6200.2 | 47 | 0 | — |
| document_discovery | completed | 6200.3 | 47 | 0 | — |
| document_download | completed | 35479.1 | 31 | 0 | — |
| extraction | completed | 600.1 | 0 | 5 | — |
| candidate_validation | completed | 124.9 | 0 | 5 | — |
| publish_queue | completed | 125.3 | 0 | 5 | — |
| append_dataset | completed | 33.1 | 0 | 5 | — |
| export | skipped | 0.7 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
