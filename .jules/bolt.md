## 2026-08-15 - Segment Slicing for CSV Parsing
**Learning:** Naive index tracking (`fieldStart`) breaks on unquoted quotes and carriage returns (`\r`). Using segment slicing (`segmentStart`) preserves exact state-machine behavior while capturing bulk string slices between delimiter transitions.
**Action:** Use segment slicing instead of character concatenation or naive index offsets when optimizing string state machines.
