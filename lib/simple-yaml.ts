/**
 * Minimal YAML subset loader for ECC policy/source configs.
 * Same philosophy as automation/lib/simple_yaml.py — no hard dependency.
 */

type YamlValue = string | number | boolean | null | YamlValue[] | { [k: string]: YamlValue };

function parseScalar(raw: string): YamlValue {
  const value = raw.trim();
  if (!value || value === "null" || value === "~") return null;
  if (value === "true" || value === "yes" || value === "on") return true;
  if (value === "false" || value === "no" || value === "off") return false;
  if (
    (value.startsWith('"') && value.endsWith('"')) ||
    (value.startsWith("'") && value.endsWith("'"))
  ) {
    return value.slice(1, -1);
  }
  if (value === "[]") return [];
  if (value === "{}") return {};
  if (/^-?\d+$/.test(value)) return Number(value);
  if (/^-?\d+\.\d+$/.test(value)) return Number(value);
  if (value.startsWith("[") && value.endsWith("]")) {
    const inner = value.slice(1, -1).trim();
    if (!inner) return [];
    return inner.split(",").map((p) => parseScalar(p));
  }
  return value;
}

function stripComment(line: string): string {
  let inSingle = false;
  let inDouble = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (ch === "'" && !inDouble) inSingle = !inSingle;
    else if (ch === '"' && !inSingle) inDouble = !inDouble;
    else if (ch === "#" && !inSingle && !inDouble) return line.slice(0, i).trimEnd();
  }
  return line;
}

function indentOf(line: string): number {
  return line.length - line.trimStart().length;
}

export function loadSimpleYaml(text: string): YamlValue {
  const lines = text.split(/\n/).map(stripComment);
  const { value } = parseBlock(lines, 0, 0);
  return value;
}

function parseBlock(
  lines: string[],
  index: number,
  minIndent: number
): { value: YamlValue; next: number } {
  let i = index;
  while (i < lines.length && !lines[i].trim()) i++;
  if (i >= lines.length) return { value: null, next: i };
  const first = lines[i];
  const indent = indentOf(first);
  if (indent < minIndent) return { value: null, next: i };
  if (first.trim().startsWith("- ")) return parseList(lines, i, indent);
  return parseMap(lines, i, indent);
}

function parseMap(
  lines: string[],
  index: number,
  indent: number
): { value: Record<string, YamlValue>; next: number } {
  const result: Record<string, YamlValue> = {};
  let i = index;
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) {
      i++;
      continue;
    }
    const cur = indentOf(line);
    if (cur < indent) break;
    if (cur > indent) {
      i++;
      continue;
    }
    const stripped = line.trim();
    if (stripped.startsWith("- ")) break;
    if (!stripped.includes(":")) {
      i++;
      continue;
    }
    const colon = stripped.indexOf(":");
    const key = stripped.slice(0, colon).trim();
    const rest = stripped.slice(colon + 1).trim();
    if (rest) {
      result[key] = parseScalar(rest);
      i++;
    } else {
      const child = parseBlock(lines, i + 1, indent + 1);
      result[key] = child.value ?? {};
      i = child.next;
    }
  }
  return { value: result, next: i };
}

function parseList(
  lines: string[],
  index: number,
  indent: number
): { value: YamlValue[]; next: number } {
  const result: YamlValue[] = [];
  let i = index;
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) {
      i++;
      continue;
    }
    const cur = indentOf(line);
    if (cur < indent) break;
    if (cur > indent) {
      i++;
      continue;
    }
    const stripped = line.trim();
    if (!stripped.startsWith("- ")) break;
    const body = stripped.slice(2).trim();
    if (!body) {
      const child = parseBlock(lines, i + 1, indent + 2);
      result.push(child.value ?? {});
      i = child.next;
    } else if (body.includes(":") && !body.startsWith("[") && !body.startsWith('"')) {
      const colon = body.indexOf(":");
      const key = body.slice(0, colon).trim();
      const rest = body.slice(colon + 1).trim();
      const item: Record<string, YamlValue> = {};
      if (rest) {
        item[key] = parseScalar(rest);
        i++;
      } else {
        const child = parseBlock(lines, i + 1, indent + 2);
        item[key] = child.value ?? {};
        i = child.next;
      }
      while (i < lines.length) {
        const nxt = lines[i];
        if (!nxt.trim()) {
          i++;
          continue;
        }
        const ni = indentOf(nxt);
        if (ni <= indent) break;
        const ns = nxt.trim();
        if (ns.startsWith("- ")) break;
        if (!ns.includes(":")) break;
        const c = ns.indexOf(":");
        const k = ns.slice(0, c).trim();
        const r = ns.slice(c + 1).trim();
        if (r) {
          item[k] = parseScalar(r);
          i++;
        } else {
          const child = parseBlock(lines, i + 1, ni + 1);
          item[k] = child.value ?? {};
          i = child.next;
        }
      }
      result.push(item);
    } else {
      result.push(parseScalar(body));
      i++;
    }
  }
  return { value: result, next: i };
}
