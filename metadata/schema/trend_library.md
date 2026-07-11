# Trend Library Schema

## Purpose

Grounded production schema for `trend_library` in IDA Dataset Factory.

## Status: Production

## Columns

`Trend ID,Trend Title,Direction,Industry ID,Industry,Time Horizon,Signal,Description,Data Sources,Last Updated,Notes`

## Rules

- Append-only
- Provenance required in Notes / Data Sources
- Confidence ≥ 0.80 for publish; auto-publish prefers ≥ 0.92
- No fabricated fields — leave empty when evidence absent
