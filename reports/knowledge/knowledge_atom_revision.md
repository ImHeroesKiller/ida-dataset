# Knowledge Atom Revision (Commit 2)

**Date:** 2026-07-12  
**Version:** `knowledge-atom-1.1.0`  
**API compatibility:** Prior `atomize_text` / `atomize_document` signatures preserved

## Stable atom IDs

**Before:** `Hash(document_id | order | atom_type | text[:200])`  
**After:** `Hash(document_id | section | paragraph_index | normalized_text)`

`normalized_text` = NFKC + lower + collapsed whitespace.  
Small casing/spacing edits no longer churn IDs.

## New fields (additive defaults)

| Field | Description |
|-------|-------------|
| knowledge_score | Atom-level richness score |
| normalized_text | Hash/compare form |
| original_text | Pre-normalization body |
| language | Heuristic `en` / `id` |
| document_type | text / pdf / html |
| mime_type | From document record |
| publisher | Metadata when present |
| published_date | Metadata when present |
| crawl_date | retrieved_at |
| parser_version | semantic-chunker-1.1.0 |
| extractor_version | knowledge-atom-1.1.0 |
| status | ACTIVE · SUPERSEDED · MERGED · ARCHIVED |
| paragraph_index | Sequence index |

## Lifecycle

Atoms default to **ACTIVE**.  
Entity extraction only processes ACTIVE atoms.  
Supersede/merge/archive reserved for re-parse workflows (no forced recreation).

## Validation notes

Re-atomizing the same document content with whitespace-only changes yields the same `atom_id` when section + paragraph_index + normalized_text match.
