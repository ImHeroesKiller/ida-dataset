#!/usr/bin/env node
/**
 * Factory health — fails if IDA Dataset Factory v2.0 surface regresses.
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const errors = [];

function exists(rel) {
  return fs.existsSync(path.join(root, rel));
}

function read(rel) {
  return fs.readFileSync(path.join(root, rel), "utf8");
}

// Forbidden legacy surfaces
const forbidden = [
  "app/ontology",
  "app/planner",
  "app/network",
  "app/knowledge",
  "app/api/runtime",
  "app/api/live",
  "features/dashboard/executive-dashboard.tsx",
  "features/knowledge",
  "reasoning",
  "plugins",
];
for (const f of forbidden) {
  if (exists(f)) errors.push(`Forbidden legacy path present: ${f}`);
}

// Required factory routes
const requiredPages = [
  "app/page.tsx",
  "app/datasets/page.tsx",
  "app/missions/page.tsx",
  "app/sources/page.tsx",
  "app/quality/page.tsx",
  "app/exports/page.tsx",
  "app/logs/page.tsx",
  "app/settings/page.tsx",
];
for (const f of requiredPages) {
  if (!exists(f)) errors.push(`Missing factory page: ${f}`);
}

// Nav must list exactly factory items
const nav = read("lib/nav.ts");
for (const label of [
  "Dashboard",
  "Datasets",
  "Missions",
  "Sources",
  "Quality",
  "Exports",
  "Logs",
  "Settings",
]) {
  if (!nav.includes(`label: "${label}"`)) {
    errors.push(`Nav missing: ${label}`);
  }
}
if (nav.includes("/knowledge") || nav.includes("/review") || nav.includes("Executive")) {
  errors.push("Nav still contains legacy items");
}

// Domains must survive
if (!exists("domains/business_development/industry_library.csv")) {
  errors.push("Industry dataset missing");
}

// Factory packages
for (const d of [
  "automation/collector",
  "automation/extractor",
  "automation/validator",
  "automation/publisher",
  "automation/quality",
  "automation/export",
]) {
  if (!exists(d)) errors.push(`Missing factory package: ${d}`);
}

if (errors.length) {
  console.log("Factory health FAILED\n");
  for (const e of errors) console.log("  ✖", e);
  process.exit(1);
}
console.log("OK — IDA Dataset Factory v2.0 health rules passed");
process.exit(0);
