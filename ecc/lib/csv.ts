import fs from "fs";

export type CsvTable = {
  path: string;
  headers: string[];
  rows: Record<string, string>[];
  rowCount: number;
  exists: boolean;
  error?: string;
};

/** Minimal RFC4180-ish CSV parser (handles quotes). */
export function parseCsv(text: string): { headers: string[]; rows: Record<string, string>[] } {
  const lines = text.replace(/^\uFEFF/, "").split(/\n/);
  const records: string[][] = [];
  let current: string[] = [];
  let field = "";
  let inQuotes = false;

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

  const raw = lines.join("\n");
  for (let i = 0; i < raw.length; i++) {
    const ch = raw[i];
    const next = raw[i + 1];
    if (inQuotes) {
      if (ch === '"' && next === '"') {
        field += '"';
        i++;
      } else if (ch === '"') {
        inQuotes = false;
      } else {
        field += ch;
      }
    } else {
      if (ch === '"') {
        inQuotes = true;
      } else if (ch === ",") {
        pushField();
      } else if (ch === "\n") {
        pushField();
        pushRecord();
      } else if (ch === "\r") {
        // ignore
      } else {
        field += ch;
      }
    }
  }
  // last field
  pushField();
  if (current.length > 1 || (current.length === 1 && current[0] !== "")) {
    pushRecord();
  }

  if (records.length === 0) {
    return { headers: [], rows: [] };
  }
  const headers = records[0].map((h) => h.trim());
  const rows = records.slice(1).map((cols) => {
    const row: Record<string, string> = {};
    headers.forEach((h, idx) => {
      row[h] = (cols[idx] ?? "").trim();
    });
    return row;
  });
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
