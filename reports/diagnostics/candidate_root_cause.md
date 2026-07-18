# Candidate Root Cause

**Generated:** 2026-07-18T15:14:29+00:00
**Session:** `SESSION-20260718-11BBA6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000441`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-11BBA6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000441': 1, 'duplicate_id:SIG-000444': 1, 'duplicate_id:SIG-000442': 1, 'duplicate_id:SIG-000443': 1, 'duplicate_id:SIG-000440': 1}`
- `candidate CAND-93BC59927FA3 entity_id=SIG-000441 reason=duplicate_id:SIG-000441 conf=0.92`
- `candidate CAND-34E84BC14BC6 entity_id=SIG-000444 reason=duplicate_id:SIG-000444 conf=0.92`
- `candidate CAND-F00A006EF5E3 entity_id=SIG-000442 reason=duplicate_id:SIG-000442 conf=0.88`
- `candidate CAND-CA2A684453D9 entity_id=SIG-000443 reason=duplicate_id:SIG-000443 conf=0.9`
- `candidate CAND-B33FC5765C81 entity_id=SIG-000440 reason=duplicate_id:SIG-000440 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-93BC59927FA3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000441 | Rejected |
| CAND-34E84BC14BC6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000444 | Rejected |
| CAND-F00A006EF5E3 | business_signal_library | 0.88 | False | duplicate_id:SIG-000442 | Rejected |
| CAND-CA2A684453D9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000443 | Rejected |
| CAND-B33FC5765C81 | business_signal_library | 0.9 | False | duplicate_id:SIG-000440 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000441` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
