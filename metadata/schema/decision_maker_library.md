# Decision Maker Library Schema

## Purpose

Grounded production schema for `decision_maker_library` in IDA Dataset Factory.

## Status: Production

## Columns

`Decision Maker ID,Title,Authority Level,Department,Responsibility,Approval Chain,Industry ID,Industry,Typical Persona Link,Description,Data Sources,Last Updated,Notes`

## Rules

- Append-only
- Provenance required in Notes / Data Sources
- Confidence ≥ 0.80 for publish; auto-publish prefers ≥ 0.92
- No fabricated fields — leave empty when evidence absent
