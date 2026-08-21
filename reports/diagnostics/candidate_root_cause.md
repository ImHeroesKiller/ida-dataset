# Candidate Root Cause

**Generated:** 2026-08-21T07:09:13+00:00
**Session:** `SESSION-20260821-7968D5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000867`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-7968D5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000867': 1, 'duplicate_id:SIG-000868': 1, 'duplicate_id:SIG-000869': 1, 'duplicate_id:SIG-000866': 1, 'duplicate_id:SIG-000870': 1}`
- `candidate CAND-8351A8FBEAAF entity_id=SIG-000867 reason=duplicate_id:SIG-000867 conf=0.9`
- `candidate CAND-A746C3024615 entity_id=SIG-000868 reason=duplicate_id:SIG-000868 conf=0.9`
- `candidate CAND-C6664F044228 entity_id=SIG-000869 reason=duplicate_id:SIG-000869 conf=0.9`
- `candidate CAND-8CB1062E3673 entity_id=SIG-000866 reason=duplicate_id:SIG-000866 conf=0.92`
- `candidate CAND-23A258CD81E3 entity_id=SIG-000870 reason=duplicate_id:SIG-000870 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8351A8FBEAAF | business_signal_library | 0.9 | False | duplicate_id:SIG-000867 | Rejected |
| CAND-A746C3024615 | business_signal_library | 0.9 | False | duplicate_id:SIG-000868 | Rejected |
| CAND-C6664F044228 | business_signal_library | 0.9 | False | duplicate_id:SIG-000869 | Rejected |
| CAND-8CB1062E3673 | business_signal_library | 0.92 | False | duplicate_id:SIG-000866 | Rejected |
| CAND-23A258CD81E3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000870 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000867` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
