# Risk Library Schema

## Purpose

Grounded production schema for `risk_library` in IDA Dataset Factory.

## Status: Production

## Columns

`Risk ID,Risk Name,Risk Type,Probability,Impact,Mitigation,Industry ID,Industry,Description,Data Sources,Last Updated,Notes`

## Rules

- Append-only
- Provenance required in Notes / Data Sources
- Confidence ≥ 0.80 for publish; auto-publish prefers ≥ 0.92
- No fabricated fields — leave empty when evidence absent
