# Publish Trace

**Generated:** 2026-07-11T15:03:27+00:00

## Execution path

```
learn.yml
  → Publish Hugging Face dataset
    → automation/ci/huggingface_publish.py
      → automation/export/hf_publisher.publish_to_huggingface
        → huggingface_hub HfApi
          → https://huggingface.co/datasets/ariew/ida-dataset
```

## Gate conditions

| Condition | Value |
|-----------|------:|
| commit_session | n/a |
| dry_run (learning) | n/a |
| learn exit_code | n/a |
| HF publish mode | dry_run |
| HF_TOKEN | Missing |
| HF_DATASET_REPO | ariew/ida-dataset |
| Branch | main |
| Git commit | 4bca139 |

## Outcome

| Field | Value |
|-------|------:|
| Executed | True |
| OK | True |
| Skipped | False |
| Message | Dry-run: would upload 51 files as 2.0.1 |
| Version | 2.0.1 |
| Uploaded files | 0 |
| Datasets | 16 |
| Rows | 567 |
| Commit SHA (HF) | None |
| Elapsed ms | 91.1 |
| Attempts | 0 |

## Errors (explicit)

- none
