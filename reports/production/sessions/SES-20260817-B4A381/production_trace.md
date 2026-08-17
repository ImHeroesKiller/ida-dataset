# Production Trace

**Generated:** 2026-08-17T07:11:53+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-CEC830`
**Session ID:** `SES-20260817-B4A381`
**Started:** 2026-08-17T06:58:23+00:00
**Finished:** 2026-08-17T07:11:53+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6150.3 | 75 | 0 | — |
| document_discovery | completed | 6150.4 | 75 | 0 | — |
| document_download | completed | 62809.7 | 42 | 0 | — |
| extraction | completed | 28.2 | 0 | 5 | — |
| candidate_validation | completed | 10.9 | 0 | 5 | — |
| publish_queue | completed | 10.9 | 0 | 5 | — |
| append_dataset | completed | 23.0 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
