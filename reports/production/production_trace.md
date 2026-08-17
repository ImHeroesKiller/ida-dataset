# Production Trace

**Generated:** 2026-08-17T01:35:26+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-3439A1`
**Session ID:** `SES-20260817-21BC9B`
**Started:** 2026-08-17T01:20:31+00:00
**Finished:** 2026-08-17T01:35:26+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6199.0 | 47 | 0 | — |
| document_discovery | completed | 6199.1 | 47 | 0 | — |
| document_download | completed | 150672.5 | 31 | 0 | — |
| extraction | completed | 27.5 | 0 | 5 | — |
| candidate_validation | completed | 11.1 | 0 | 5 | — |
| publish_queue | completed | 11.1 | 0 | 5 | — |
| append_dataset | completed | 18.1 | 0 | 5 | — |
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
