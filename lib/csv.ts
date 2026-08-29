import fs from "fs";

export type CsvTable = {
  path: string;
  headers: string[];
  rows: Record<string, string>[];
  rowCount: number;
  exists: boolean;
  error?: string;
};

/** Minimal RFC4180-ish CSV parser (handles quotes). Optimized using segment slicing to eliminate character-by-character string concatenation. */
export function parseCsv(text: string): { headers: string[]; rows: Record<string, string>[] } {
  const raw = text.startsWith("\uFEFF") ? text.slice(1) : text;
  const len = raw.length;
  if (len === 0) {
    return { headers: [], rows: [] };
  }

  const records: string[][] = [];
  let current: string[] = [];
  let field = "";
  let inQuotes = false;
  let segmentStart = 0;

  const pushField = () => {
    current.push(field);
    field = "";
  };
  const pushRecord = () => {
    // skip fully empty trailing lines
    if (current.length === 1 && current[0] === "" && records.length > 0) {
      current = [];
      return;
    }
    records.push(current);
    current = [];
  };

  for (let i = 0; i < len; i++) {
    const ch = raw[i];
    if (inQuotes) {
      if (ch === '"') {
        if (i + 1 < len && raw[i + 1] === '"') {
          field += raw.slice(segmentStart, i) + '"';
          i++;
          segmentStart = i + 1;
        } else {
          field += raw.slice(segmentStart, i);
          inQuotes = false;
          segmentStart = i + 1;
        }
      }
    } else {
      if (ch === '"') {
        field += raw.slice(segmentStart, i);
        inQuotes = true;
        segmentStart = i + 1;
      } else if (ch === ",") {
        field += raw.slice(segmentStart, i);
        pushField();
        segmentStart = i + 1;
      } else if (ch === "\n") {
        field += raw.slice(segmentStart, i);
        pushField();
        pushRecord();
        segmentStart = i + 1;
      } else if (ch === "\r") {
        field += raw.slice(segmentStart, i);
        segmentStart = i + 1;
      }
    }
  }

  // last field
  field += raw.slice(segmentStart, len);
  pushField();
  if (current.length > 1 || (current.length === 1 && current[0] !== "")) {
    pushRecord();
  }

  if (records.length === 0) {
    return { headers: [], rows: [] };
  }

  const headerRow = records[0];
  const headerCount = headerRow.length;
  const headers = new Array<string>(headerCount);
  for (let i = 0; i < headerCount; i++) {
    headers[i] = headerRow[i].trim();
  }

  const recordCount = records.length;
  const rows: Record<string, string>[] = [];
  for (let r = 1; r < recordCount; r++) {
    const cols = records[r];
    const row: Record<string, string> = {};
    for (let h = 0; h < headerCount; h++) {
      row[headers[h]] = (cols[h] ?? "").trim();
    }
    rows.push(row);
  }

  return { headers, rows };
}

export function readCsvFile(filePath: string): CsvTable {
  if (!fs.existsSync(filePath)) {
    return {
      path: filePath,
      headers: [],
      rows: [],
      rowCount: 0,
      exists: false,
      error: "File not found",
    };
  }
  try {
    const text = fs.readFileSync(filePath, "utf8");
    const { headers, rows } = parseCsv(text);
    return {
      path: filePath,
      headers,
      rows,
      rowCount: rows.length,
      exists: true,
    };
  } catch (err) {
    return {
      path: filePath,
      headers: [],
      rows: [],
      rowCount: 0,
      exists: true,
      error: err instanceof Error ? err.message : "Failed to read CSV",
    };
  }
}

export function listCsvFiles(dir: string, recursive = true): string[] {
  if (!fs.existsSync(dir)) return [];
  const out: string[] = [];
  const walk = (d: string) => {
    for (const entry of fs.readdirSync(d, { withFileTypes: true })) {
      if (entry.name.startsWith(".")) continue;
      const full = `${d}/${entry.name}`;
      if (entry.isDirectory() && recursive) walk(full);
      else if (entry.isFile() && entry.name.endsWith(".csv")) out.push(full);
    }
  };
  walk(dir);
  return out.sort();
}
