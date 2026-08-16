# Production Trace

**Generated:** 2026-08-16T14:38:39+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-674743`
**Session ID:** `SES-20260816-45DD70`
**Started:** 2026-08-16T14:24:45+00:00
**Finished:** 2026-08-16T14:38:39+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6213.5 | 77 | 0 | — |
| document_discovery | completed | 6213.7 | 77 | 0 | — |
| document_download | completed | 99781.4 | 42 | 0 | — |
| extraction | completed | 28.4 | 0 | 5 | — |
| candidate_validation | completed | 10.9 | 0 | 5 | — |
| publish_queue | completed | 10.8 | 0 | 5 | — |
| append_dataset | completed | 23.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
