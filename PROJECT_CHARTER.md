# Project Charter — IDA Dataset Factory v2.0

## Product

| Field | Value |
|-------|--------|
| Repository | `ida-dataset` |
| Product name | **IDA Dataset Factory** |
| Version | 2.0.0 |

## Purpose

Automatically build high-quality structured datasets for:

1. LLM fine-tuning (OpenAI-compatible JSONL)  
2. Hugging Face dataset packages  
3. Internal IDA knowledge corpus (CSV/JSON/Parquet)  

## Inputs

- Missions  
- Trusted sources (registry)  
- Documents / reports / public data  

## Outputs

- CSV (domains)  
- JSON / JSONL  
- Parquet  
- Hugging Face package  
- OpenAI fine-tuning JSONL  

## Non-goals

Decision Engine · Reasoning · Chatbot · Knowledge Graph UI · BI · Executive AI · Agents · Workflow platforms  

## Quality law

Every published row retains:

Source · Retrieved Date · Confidence · Version · Freshness · Schema completeness · Duplicate check · Validation result  

## Policy

**Append-only** domain datasets. Never destroy verified knowledge.
