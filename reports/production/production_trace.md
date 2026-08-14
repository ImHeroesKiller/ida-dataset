# Production Trace

**Generated:** 2026-08-14T17:09:33+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-DCE569`
**Session ID:** `SES-20260814-DCF69D`
**Started:** 2026-08-14T16:55:20+00:00
**Finished:** 2026-08-14T17:09:33+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.2 | 0 | 0 | — |
| connector | completed | 6153.4 | 47 | 0 | — |
| document_discovery | completed | 6153.6 | 47 | 0 | — |
| document_download | completed | 104196.2 | 31 | 0 | — |
| extraction | completed | 24.5 | 0 | 5 | — |
| candidate_validation | completed | 8.2 | 0 | 5 | — |
| publish_queue | completed | 8.2 | 0 | 5 | — |
| append_dataset | completed | 18.7 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.4 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
