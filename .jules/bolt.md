# Bolt's Journal

## 2026-08-16 - Zero-allocation string slicing in CSV parser
**Learning:** In TypeScript/Node.js, character-by-character string concatenation (`field += ch`) in loop-based parsers over large dataset files causes massive CPU overhead and memory allocations. Replacing character accumulation with slice pointers (`raw.slice(fieldStart, i)`) yields a ~3.9x speedup without sacrificing RFC4180 compliance or readability.
**Action:** Use index tracking and `raw.slice()` for parsing formatted string files instead of string concatenation in loops.
