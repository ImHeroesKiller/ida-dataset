# Regulation Library Schema

## Purpose

Grounded production schema for `regulation_library` in IDA Dataset Factory.

## Status: Production

## Columns

`Regulation ID,Regulation Name,Issuer,Effective Date,Scope,Industry ID,Industry,Jurisdiction,Summary,Source URL,Data Sources,Last Updated,Notes`

## Rules

- Append-only
- Provenance required in Notes / Data Sources
- Confidence ≥ 0.80 for publish; auto-publish prefers ≥ 0.92
- No fabricated fields — leave empty when evidence absent
