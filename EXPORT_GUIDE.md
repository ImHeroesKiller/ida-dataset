# Export Guide

## Formats

| Format | Location | Command |
|--------|----------|---------|
| Domain CSV | `domains/**` | Produced by publisher |
| JSONL | `exports/jsonl/` | `python3 -m automation.export.packager` |
| OpenAI fine-tune JSONL | `exports/openai/` | same (`formats` includes `openai`) |
| Hugging Face JSON | `exports/huggingface/` | same |
| Parquet | `exports/parquet/` | Planned (v2.1) |

## Local export

```bash
python3 - <<'PY'
from automation.export.packager import export_dataset
print(export_dataset(formats=["jsonl", "openai", "huggingface"]))
PY
```

## CI

`.github/workflows/export.yml` — workflow_dispatch / callable.

## Dashboard

`/exports` shows artifact folders and status.
