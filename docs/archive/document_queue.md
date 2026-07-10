# Document Queue

## Purpose

All acquired documents land in a queue before any pipeline processing.

## Status: Active (Sprint 5)

```text
automation/documents/
  incoming/
  processing/
  processed/
  failed/
```

Each document JSON carries Source ID, Connector ID, Trust Score, Retrieved Time, Original URL, Checksum, Version.

Nothing goes directly into `domains/` datasets.
