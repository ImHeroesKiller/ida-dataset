# Knowledge Acquisition System (KAS)

## Purpose

Define the human-controlled knowledge acquisition pipeline that populates IDA datasets without autonomous scraping or unreviewed writes.

## Status: Draft

## Overview

KAS lives under `automation/` and implements a fixed nine-stage pipeline. Humans control enablement, source trust, limits, approval mode, and publishing schedule. Production domain CSVs are never written directly by discovery or extraction stages.

See `automation/README.md` for CLI usage and operational details.

## Provenance contract

Every candidate and every published row must carry:

| Field | Description |
| --- | --- |
| Source ID | Key into `metadata/source_registry.csv` |
| Source URL | Exact retrieval URL |
| Retrieved At | ISO-8601 timestamp |
| Confidence | 0.0–1.0 extraction confidence |
| Extraction Version | Extractor software version |
| Validation Status | pending / valid / invalid / duplicate / rejected / approved / published |
| Reviewer | Human reviewer identity (or `auto` only when explicitly allowed) |
| Published At | Set only at publish time |

## Trust boundary

1. Source must be present in the source registry and `Allowed=true`
2. Trust score must meet configured minimum
3. Domain must pass whitelist/blacklist checks
4. Confidence must meet threshold
5. Human review is required unless automatic approval is explicitly configured
6. Publishing is disabled by default
