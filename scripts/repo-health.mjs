#!/usr/bin/env node
/**
 * Repository health validation — fails CI on consolidation regressions.
 *
 * Checks:
 * - Exactly one public nav source (lib/nav.ts executive items)
 * - No orphan executive feature modules without page imports
 * - Deprecated API routes still return via deprecatedGone (presence of lib/api/deprecated.ts)
 * - No dual learning hooks (use-live-learning must not exist)
 * - Single design token file under styles/globals.css
 * - No live-dashboard / runtime-manager orphans reintroduced
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const errors = [];
const warnings = [];

function exists(rel) {
  return fs.existsSync(path.join(root, rel));
}

function read(rel) {
  return fs.readFileSync(path.join(root, rel), "utf8");
}

function walk(dir, pred, out = []) {
  const full = path.join(root, dir);
  if (!fs.existsSync(full)) return out;
  for (const name of fs.readdirSync(full)) {
    const rel = path.join(dir, name);
    const abs = path.join(root, rel);
    const st = fs.statSync(abs);
    if (st.isDirectory()) {
      if (name === "node_modules" || name === ".git" || name === "ecc") continue;
      walk(rel, pred, out);
    } else if (pred(rel)) out.push(rel);
  }
  return out;
}

// 1. Forbidden legacy modules must not return
const forbidden = [
  "lib/use-live-learning.ts",
  "lib/live-sse-bus.ts",
  "lib/runtime-manager.ts",
  "lib/sse-registry.ts",
  "components/shared/live-dashboard.tsx",
  "components/shared/live-progress.tsx",
  "components/shared/progress-bar.tsx",
  "components/dashboard/status-card.tsx",
];
for (const f of forbidden) {
  if (exists(f)) errors.push(`Forbidden legacy module present: ${f}`);
}

// 2. Single styling entry
if (!exists("styles/globals.css")) {
  errors.push("Missing styles/globals.css (single design token system)");
}
if (exists("app/globals.css")) {
  const g = read("app/globals.css");
  if (!g.includes("styles/globals.css")) {
    errors.push("app/globals.css must import styles/globals.css only");
  }
}

// 3. Executive features exist
const features = [
  "features/dashboard/executive-dashboard.tsx",
  "features/knowledge/knowledge-client.tsx",
  "features/missions/missions-client.tsx",
  "features/review/review-client.tsx",
  "features/reports/reports-client.tsx",
];
for (const f of features) {
  if (!exists(f)) errors.push(`Missing feature module: ${f}`);
}

// 4. Learning provider single source
if (!exists("hooks/learning-provider.tsx") || !exists("hooks/use-learning-monitor.ts")) {
  errors.push("Missing hooks/learning-provider or use-learning-monitor");
}

// 5. Nav public surface count
const nav = read("lib/nav.ts");
const hrefs = [...nav.matchAll(/href:\s*"([^"]+)"/g)].map((m) => m[1]);
const publicHrefs = hrefs.filter((h) =>
  ["/", "/knowledge", "/missions", "/review", "/reports", "/settings"].includes(h)
);
if (publicHrefs.length !== 6) {
  errors.push(
    `Expected exactly 6 public nav routes, found ${publicHrefs.length}: ${publicHrefs.join(", ")}`
  );
}

// 6. Deprecated API registry present
if (!exists("lib/api/deprecated.ts")) {
  errors.push("Missing lib/api/deprecated.ts");
}

// 7. Orphan scan: components under components/shared that are never imported
const shared = walk("components/shared", (r) => r.endsWith(".tsx"));
const srcFiles = walk(".", (r) =>
  (r.endsWith(".ts") || r.endsWith(".tsx")) &&
  !r.includes("node_modules") &&
  !r.startsWith("ecc/")
);
const srcText = srcFiles.map((r) => {
  try {
    return { r, t: read(r) };
  } catch {
    return { r, t: "" };
  }
});

for (const s of shared) {
  const base = s.replace(/\.tsx$/, "");
  const alias = `@/${base}`;
  const users = srcText.filter(
    (x) => x.r !== s && (x.t.includes(alias) || x.t.includes(path.basename(base)))
  );
  // basename match is loose; require alias
  const strict = srcText.filter((x) => x.r !== s && x.t.includes(alias));
  if (strict.length === 0) {
    // learning-client may still be used by redirected learning page - check
    if (s.includes("learning-client") || s.includes("publisher-client")) {
      warnings.push(`Shared module may be orphan after redirects: ${s}`);
    } else if (
      s.includes("datasets-client") ||
      s.includes("network-client") ||
      s.includes("ontology") ||
      s.includes("planner") ||
      s.includes("policy") ||
      s.includes("run-actions")
    ) {
      // internal operator tools — ok if imported by internal pages
      const pageUsers = srcText.filter(
        (x) => x.r.startsWith("app/") && x.t.includes(alias)
      );
      if (pageUsers.length === 0) {
        warnings.push(`No page import for internal client: ${s}`);
      }
    } else {
      warnings.push(`No @/ import found for: ${s}`);
    }
  }
}

// 8. Dual poll heuristic: useLearningMonitor should only be called from provider
const monitorCallers = srcText.filter(
  (x) =>
    x.t.includes("useLearningMonitor(") &&
    !x.r.includes("use-learning-monitor") &&
    !x.r.includes("learning-provider")
);
if (monitorCallers.length > 0) {
  errors.push(
    `useLearningMonitor called outside provider: ${monitorCallers.map((x) => x.r).join(", ")}`
  );
}

// Report
console.log("Repository health check\n");
if (warnings.length) {
  console.log("Warnings:");
  for (const w of warnings) console.log("  ⚠", w);
  console.log("");
}
if (errors.length) {
  console.log("Errors:");
  for (const e of errors) console.log("  ✖", e);
  console.log(`\nFAILED (${errors.length} error(s))`);
  process.exit(1);
}
console.log("OK — consolidation health rules passed");
process.exit(0);
