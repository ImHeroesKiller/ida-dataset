#!/usr/bin/env node
/**
 * Repository health validation — factory v2.0 frozen surface.
 *
 * Checks:
 * - No forbidden legacy runtime modules
 * - Single design token entry
 * - Factory feature modules present
 * - Learning provider single poll source
 * - Public nav matches factory routes
 * - Deprecated API registry present
 * - Required reliability scripts present
 * - No dual useLearningMonitor callers outside provider
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
      if (name === "node_modules" || name === ".git" || name === ".next") continue;
      walk(rel, pred, out);
    } else if (pred(rel)) out.push(rel);
  }
  return out;
}

// 1. Forbidden legacy modules
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

// 3. Factory feature modules
const features = [
  "features/dashboard/factory-dashboard.tsx",
  "features/missions/missions-client.tsx",
  "components/shared/datasets-client.tsx",
  "components/console/bottom-console.tsx",
];
for (const f of features) {
  if (!exists(f)) errors.push(`Missing factory module: ${f}`);
}

// 4. Reliability surface
const reliability = [
  "scripts/git_safe_sync_push.sh",
  "automation/lib/git_safe.py",
  "automation/quality/integrity_guard.py",
  "automation/scheduler/mission_selector.py",
  "lib/time-wib.ts",
  "lib/executive-factory.ts",
];
for (const f of reliability) {
  if (!exists(f)) errors.push(`Missing reliability module: ${f}`);
}

// 5. Learning provider single source
if (!exists("hooks/learning-provider.tsx") || !exists("hooks/use-learning-monitor.ts")) {
  errors.push("Missing hooks/learning-provider or use-learning-monitor");
}

// 6. Nav factory surface
const nav = read("lib/nav.ts");
const hrefs = [...nav.matchAll(/href:\s*"([^"]+)"/g)].map((m) => m[1]);
const required = ["/", "/datasets", "/missions", "/sources", "/quality", "/exports", "/logs", "/settings"];
for (const h of required) {
  if (!hrefs.includes(h)) {
    // soft: settings may exist
    if (h === "/settings" && !hrefs.includes(h)) {
      warnings.push(`Nav missing optional route: ${h}`);
    } else if (!hrefs.includes(h)) {
      errors.push(`Nav missing factory route: ${h}`);
    }
  }
}

// 7. Deprecated API registry
if (!exists("lib/api/deprecated.ts")) {
  errors.push("Missing lib/api/deprecated.ts");
}

// 8. Live API routes
const apiRoutes = [
  "app/api/sessions/route.ts",
  "app/api/factory/status/route.ts",
  "app/api/run/route.ts",
  "app/api/missions/route.ts",
  "app/api/search/route.ts",
  "app/api/datasets/route.ts",
  "app/api/sources/route.ts",
  "app/api/publish-queue/route.ts",
];
for (const f of apiRoutes) {
  if (!exists(f)) errors.push(`Missing API route: ${f}`);
}

// 9. Dual poll heuristic
const srcFiles = walk(".", (r) =>
  (r.endsWith(".ts") || r.endsWith(".tsx")) &&
  !r.includes("node_modules") &&
  !r.includes(".next")
);
const srcText = srcFiles.map((r) => {
  try {
    return { r, t: read(r) };
  } catch {
    return { r, t: "" };
  }
});

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

// 10. No live /api/learning fetches (registry entry in deprecated.ts is OK)
const deadLearning = srcText.filter(
  (x) =>
    !x.r.includes("lib/api/deprecated.ts") &&
    (x.t.includes('"/api/learning"') ||
      x.t.includes("'/api/learning'") ||
      x.t.includes("`/api/learning"))
);
if (deadLearning.length > 0) {
  errors.push(
    `Dead /api/learning reference: ${deadLearning.map((x) => x.r).join(", ")}`
  );
}

// Report
console.log("Repository health check (factory v2.0)\n");
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
console.log("OK — factory repository health rules passed");
process.exit(0);
