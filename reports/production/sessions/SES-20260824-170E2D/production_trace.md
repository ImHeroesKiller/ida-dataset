# Production Trace

**Generated:** 2026-08-24T10:08:15+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260824-6E05A2`
**Session ID:** `SES-20260824-170E2D`
**Started:** 2026-08-24T09:50:32+00:00
**Finished:** 2026-08-24T10:08:15+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6205.1 | 47 | 0 | — |
| document_discovery | completed | 6205.1 | 47 | 0 | — |
| document_download | completed | 317886.7 | 31 | 0 | — |
| extraction | completed | 39.3 | 0 | 5 | — |
| candidate_validation | completed | 21.3 | 0 | 5 | — |
| publish_queue | completed | 21.3 | 0 | 5 | — |
| append_dataset | completed | 17.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
