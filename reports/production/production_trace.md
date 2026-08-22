# Production Trace

**Generated:** 2026-08-22T07:50:58+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-E41657`
**Session ID:** `SES-20260822-906250`
**Started:** 2026-08-22T07:33:14+00:00
**Finished:** 2026-08-22T07:50:58+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6177.3 | 47 | 0 | — |
| document_discovery | completed | 6177.4 | 47 | 0 | — |
| document_download | completed | 314293.7 | 31 | 0 | — |
| extraction | completed | 36.7 | 0 | 5 | — |
| candidate_validation | completed | 18.3 | 0 | 5 | — |
| publish_queue | completed | 18.3 | 0 | 5 | — |
| append_dataset | completed | 19.3 | 0 | 5 | — |
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
