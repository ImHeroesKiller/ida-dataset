# Duplicate Forensics

**Generated:** 2026-07-11T13:39:39+00:00

## Counts by type

| Type | Count |
|------|------:|
| Trace document duplicates skipped | 156 |
| Duplicate URL (same original_url, >1 doc) | 0 |
| Duplicate content hash (checksum) | 1 |
| Duplicate entity_id (candidates) | 23 |
| Candidates with `duplicate_of` set | 0 |
| Trace rows_duplicate | 0 |

## Percentages (of class sum = 180)

| Class | Count | % |
|-------|------:|--:|
| Trace pre-download doc dups | 156 | 86.67% |
| Duplicate URL docs | 0 | 0.0% |
| Duplicate Hash | 1 | 0.56% |
| Duplicate Entity ID | 23 | 12.78% |

## Fingerprint skips (last acquisition)

| Field | Value |
|-------|------:|
| skips | 7 |
| unique_hashes | 32 |
| unique_urls | 32 |

## Finding

1. **Early:** 156 document-level dups skipped vs 206 downloads.  
2. **Late:** integrity `duplicate_id` blocks re-publish of existing entities.  
3. Early doc-dup + low extract multiplicity dominate “thousands → handful” more than late rejects.
