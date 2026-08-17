# Candidate Root Cause

**Generated:** 2026-08-17T09:05:16+00:00
**Session:** `SESSION-20260817-D39018`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000422`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-D39018`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000422': 1, 'duplicate_id:SIG-000423': 1, 'duplicate_id:SIG-000424': 1, 'duplicate_id:SIG-000421': 1, 'duplicate_id:SIG-000425': 1}`
- `candidate CAND-110F0B521613 entity_id=SIG-000422 reason=duplicate_id:SIG-000422 conf=0.9`
- `candidate CAND-2645C0E6E148 entity_id=SIG-000423 reason=duplicate_id:SIG-000423 conf=0.9`
- `candidate CAND-81368DB4C0C3 entity_id=SIG-000424 reason=duplicate_id:SIG-000424 conf=0.9`
- `candidate CAND-2766B459EB1D entity_id=SIG-000421 reason=duplicate_id:SIG-000421 conf=0.92`
- `candidate CAND-20D8636713CA entity_id=SIG-000425 reason=duplicate_id:SIG-000425 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-110F0B521613 | business_signal_library | 0.9 | False | duplicate_id:SIG-000422 | Rejected |
| CAND-2645C0E6E148 | business_signal_library | 0.9 | False | duplicate_id:SIG-000423 | Rejected |
| CAND-81368DB4C0C3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000424 | Rejected |
| CAND-2766B459EB1D | business_signal_library | 0.92 | False | duplicate_id:SIG-000421 | Rejected |
| CAND-20D8636713CA | business_signal_library | 0.9 | False | duplicate_id:SIG-000425 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000422` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
