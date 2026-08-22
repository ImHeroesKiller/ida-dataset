# Production Trace

**Generated:** 2026-08-22T09:46:14+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-CD765A`
**Session ID:** `SES-20260822-C40AAB`
**Started:** 2026-08-22T09:28:32+00:00
**Finished:** 2026-08-22T09:46:14+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6200.9 | 47 | 0 | — |
| document_discovery | completed | 6201.0 | 47 | 0 | — |
| document_download | completed | 310204.5 | 31 | 0 | — |
| extraction | completed | 36.8 | 0 | 5 | — |
| candidate_validation | completed | 18.3 | 0 | 5 | — |
| publish_queue | completed | 18.4 | 0 | 5 | — |
| append_dataset | completed | 19.1 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
