"""Minimal YAML subset loader for KAS configs (no external dependency).

Supports: mappings, sequences, scalars (str/int/float/bool/null), comments,
nested indentation. Not a full YAML 1.2 implementation — sufficient for
automation/config/*.yaml in Phase 1. Prefer PyYAML when available.
"""

from __future__ import annotations

import re
from typing import Any


_BOOL = {"true": True, "false": False, "yes": True, "no": False, "on": True, "off": False}
_NULL = {"null", "~", ""}


def load_simple_yaml(text: str) -> Any:
    lines = text.splitlines()
    # Strip full-line comments and trailing spaces; keep structure
    cleaned: list[str] = []
    for line in lines:
        if not line.strip():
            cleaned.append("")
            continue
        # remove inline comments not inside quotes
        cleaned.append(_strip_inline_comment(line.rstrip()))
    return _parse_block(cleaned, 0, 0)[0]


def _strip_inline_comment(line: str) -> str:
    in_single = False
    in_double = False
    for i, ch in enumerate(line):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double:
            return line[:i].rstrip()
    return line


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if not value:
        return None
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    lower = value.lower()
    if lower in _NULL:
        return None
    if lower in _BOOL:
        return _BOOL[lower]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?\d+\.\d+", value):
        return float(value)
    # flow-style empty structures
    if value == "[]":
        return []
    if value == "{}":
        return {}
    # simple flow list: [a, b]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        parts = _split_flow(inner)
        return [_parse_scalar(p) for p in parts]
    return value


def _split_flow(inner: str) -> list[str]:
    parts: list[str] = []
    buf: list[str] = []
    in_single = in_double = False
    for ch in inner:
        if ch == "'" and not in_double:
            in_single = not in_single
            buf.append(ch)
        elif ch == '"' and not in_single:
            in_double = not in_double
            buf.append(ch)
        elif ch == "," and not in_single and not in_double:
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if buf:
        parts.append("".join(buf).strip())
    return parts


def _parse_block(lines: list[str], index: int, min_indent: int) -> tuple[Any, int]:
    # Determine container type from first non-empty line
    i = index
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines):
        return None, i

    first = lines[i]
    indent = _indent(first)
    if indent < min_indent:
        return None, i

    stripped = first.strip()
    if stripped.startswith("- "):
        return _parse_list(lines, i, indent)
    return _parse_map(lines, i, indent)


def _parse_map(lines: list[str], index: int, indent: int) -> tuple[dict[str, Any], int]:
    result: dict[str, Any] = {}
    i = index
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        cur_indent = _indent(line)
        if cur_indent < indent:
            break
        if cur_indent > indent:
            # orphan nested content — skip safety
            i += 1
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            break
        if ":" not in stripped:
            i += 1
            continue
        key, _, rest = stripped.partition(":")
        key = key.strip()
        rest = rest.strip()
        if rest:
            result[key] = _parse_scalar(rest)
            i += 1
        else:
            # nested block
            child, next_i = _parse_block(lines, i + 1, indent + 1)
            # empty nested -> {} or [] depending on next content; default {}
            if child is None:
                # peek if next is list at deeper indent
                result[key] = {}
                i += 1
            else:
                result[key] = child
                i = next_i
    return result, i


def _parse_list(lines: list[str], index: int, indent: int) -> tuple[list[Any], int]:
    result: list[Any] = []
    i = index
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        cur_indent = _indent(line)
        if cur_indent < indent:
            break
        if cur_indent > indent:
            i += 1
            continue
        stripped = line.strip()
        if not stripped.startswith("- "):
            break
        item_body = stripped[2:].strip()
        if not item_body:
            child, next_i = _parse_block(lines, i + 1, indent + 2)
            result.append({} if child is None else child)
            i = next_i
        elif item_body.endswith(":") and ":" == item_body[-1] and item_body.count(":") == 1:
            # "- key:" with nested map under list item — uncommon; treat as map start
            key = item_body[:-1].strip()
            child, next_i = _parse_block(lines, i + 1, indent + 2)
            result.append({key: {} if child is None else child})
            i = next_i
        elif ":" in item_body and not item_body.startswith("[") and not (
            item_body.startswith('"') or item_body.startswith("'")
        ):
            # inline map start on list item: "- key: value" possibly with nested keys
            key, _, rest = item_body.partition(":")
            key = key.strip()
            rest = rest.strip()
            item: dict[str, Any] = {}
            if rest:
                item[key] = _parse_scalar(rest)
                i += 1
            else:
                child, next_i = _parse_block(lines, i + 1, indent + 2)
                item[key] = {} if child is None else child
                i = next_i
            # continue reading sibling keys of this list map item
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    i += 1
                    continue
                ni = _indent(nxt)
                if ni <= indent:
                    break
                if ni > indent + 2:
                    # nested already consumed by parse_block in other paths
                    break
                ns = nxt.strip()
                if ns.startswith("- "):
                    break
                if ":" not in ns:
                    break
                k, _, r = ns.partition(":")
                k = k.strip()
                r = r.strip()
                if r:
                    item[k] = _parse_scalar(r)
                    i += 1
                else:
                    child, next_i = _parse_block(lines, i + 1, ni + 1)
                    item[k] = {} if child is None else child
                    i = next_i
            result.append(item)
        else:
            result.append(_parse_scalar(item_body))
            i += 1
    return result, i
