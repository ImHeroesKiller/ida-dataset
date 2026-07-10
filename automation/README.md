# Knowledge Acquisition System (KAS)

Human-controlled knowledge acquisition pipeline for the IDA Dataset repository.

## Principles

1. Human-in-the-loop
2. Trust-first
3. No hallucination
4. Every row must have provenance
5. Every change must be reviewable
6. Nothing is written directly into production datasets
7. Every action must be reproducible

This is **not** a web scraper and **not** an autonomous AI agent.

## Pipeline stages (fixed order)

1. `discover` — trusted source discovery  
2. `collect` — document collection (placeholder; gated by controller)  
3. `extract` — content extraction (placeholder; gated by controller)  
4. `normalize` — field normalization  
5. `validate` — validation rules → `queue/rejected` on failure  
6. `deduplicate` — duplicate detection  
7. `entity_link` — entity linking  
8. `reviewer` — human review queue  
9. `publisher` — append-only publish to `domains/`  

No stage may be skipped in full profiles.

## Directory layout

```text
automation/
  config/           # sources.yaml, policies.yaml, scheduler.yaml
  pipeline/         # stage modules
  lib/              # controller, models, config, io
  queue/
    pending/
    approved/
    rejected/
  logs/
  reports/
  cache/
  raw_documents/
  review/
  orchestrator.py   # CLI entrypoint
```

## Human controller

Configured primarily in `config/policies.yaml` and `config/sources.yaml`.

| Control | Config location |
| --- | --- |
| Enable crawling / extraction / publishing | `policies.features.*` |
| Trusted sources | `metadata/source_registry.csv` + `sources.yaml` |
| Domain whitelist / blacklist | `sources.domains` |
| Max documents / rows/day / updates/day | `policies.limits` |
| Confidence threshold | `policies.confidence_threshold` |
| Approval mode | `policies.approval_mode` (`automatic` \| `semi_automatic` \| `manual`) |
| Review required | `policies.review_required` |
| Publishing schedule | `policies.publishing.schedule` (`immediate` \| `daily` \| `weekly` \| `manual`) |

Runtime CLI overrides are also available (see below).

## Provenance (mandatory on every row)

- Source ID  
- Source URL  
- Retrieved At  
- Confidence  
- Extraction Version  
- Validation Status  
- Reviewer  
- Published At  

## CLI

From the repository root:

```bash
# List stages
python -m automation.orchestrator stages

# Show controller snapshot
python -m automation.orchestrator controller

# Dry-run full pipeline (default; safe)
python -m automation.orchestrator run --profile dry_run

# Full pipeline with collection/extraction enabled (still no publish)
python -m automation.orchestrator run --profile full_pipeline \
  --no-dry-run \
  --enable-crawling \
  --enable-extraction

# Apply a human review decision
python -m automation.orchestrator review \
  --candidate-id CAND-XXXXXXXXXXXX \
  --action approve \
  --reviewer "arya"

# Publish approved queue (requires publishing enabled)
python -m automation.orchestrator run --profile publish_only \
  --no-dry-run \
  --publish \
  --enable-publishing
```

## Publishing rules

- Append only into `domains/**`
- Never overwrite existing data
- Always preserve IDs
- Always emit a publish report under `automation/reports/`
- Always capture git status / diff stats in the report
- No automatic publish unless `approval_mode=automatic` **and** `review_required=false` **and** publishing is enabled

## Phase 1 status

Architecture and pipeline wiring only.

- Collection and extraction are **placeholders** ready for search APIs, browser automation, or LLM extraction.
- Default config keeps crawling, extraction, and publishing **disabled**.
- Production datasets under `domains/` are not modified by a default dry-run.

## Reports

- `automation/reports/run_RUN-*.json` — per-run machine report  
- `automation/reports/daily_YYYY-MM-DD.md` — human daily summary  
- `automation/reports/publish_RUN-*.json` — publish audit trail  

## Related

- Source registry: `metadata/source_registry.csv`
- Domain datasets: `domains/`
