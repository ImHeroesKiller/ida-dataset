# Buyer Persona Library Schema

## Purpose

Grounded production schema for `buyer_persona_library` in IDA Dataset Factory.

## Status: Production

## Columns

`Persona ID,Persona Name,Industry ID,Industry,Company Size,Job Role,Department,Seniority,Pain Points,Goals,Budget Characteristics,Buying Behavior,Decision Criteria,Information Sources,Description,Data Sources,Last Updated,Notes`

## Rules

- Append-only
- Provenance required in Notes / Data Sources
- Confidence ≥ 0.80 for publish; auto-publish prefers ≥ 0.92
- No fabricated fields — leave empty when evidence absent
