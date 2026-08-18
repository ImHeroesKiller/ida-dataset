# Production Trace

**Generated:** 2026-08-18T06:58:33+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-791E38`
**Session ID:** `SES-20260818-E6EAAC`
**Started:** 2026-08-18T06:45:25+00:00
**Finished:** 2026-08-18T06:58:33+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6162.5 | 47 | 0 | — |
| document_discovery | completed | 6162.6 | 47 | 0 | — |
| document_download | completed | 35513.1 | 31 | 0 | — |
| extraction | completed | 29.2 | 0 | 5 | — |
| candidate_validation | completed | 13.5 | 0 | 5 | — |
| publish_queue | completed | 13.4 | 0 | 5 | — |
| append_dataset | completed | 18.7 | 0 | 5 | — |
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
