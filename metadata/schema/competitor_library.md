# Competitor Library Schema

## Purpose

Grounded production schema for `competitor_library` in IDA Dataset Factory.

## Status: Production

## Columns

`Competitor ID,Competitor Name,Industry Category,Company Description,Headquarters,Operating Region,Target Customer,Main Products/Services,Strengths,Weaknesses,Unique Selling Proposition (USP),Pricing Level,Pricing Model,Typical Sales Strategy,Typical Decision Makers,Industries Served,Competitive Advantages,Competitive Disadvantages,Our Competitive Advantage,Win Strategy,Common Customer Objections,Recommended Response,Market Position,Threat Level,Reference Projects,Information Source,Last Updated,Notes`

## Rules

- Append-only
- Provenance required in Notes / Data Sources
- Confidence ≥ 0.80 for publish; auto-publish prefers ≥ 0.92
- No fabricated fields — leave empty when evidence absent
