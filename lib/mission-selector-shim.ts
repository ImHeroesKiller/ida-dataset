/**
 * TypeScript port entry for mission selection used by executive UI.
 * Mirrors automation/scheduler/mission_selector.py logic at a high level
 * by importing the same scoring via a lightweight reimplementation.
 */

import fs from "fs";
import path from "path";
import { repoPath } from "./paths";
import { productTargetFor } from "./product-targets";

type Selected = {
  batch_id: string;
  dataset: string;
  title: string;
  instruction: string;
  coverage_pct: number;
  current_rows: number;
  product_target: number;
  product_priority: number;
  score: number;
  reason: string;
};

function rowCount(rel: string): number {
  const p = repoPath(rel);
  if (!fs.existsSync(p)) return 0;
  try {
    return Math.max(0, fs.readFileSync(p, "utf8").split("\n").filter(Boolean).length - 1);
  } catch {
    return 0;
  }
}

function serviceCount(): number {
  const p = repoPath("domains/business_development/product_catalog.csv");
  if (!fs.existsSync(p)) return 0;
  const lines = fs.readFileSync(p, "utf8").split("\n").filter(Boolean);
  if (lines.length < 2) return 0;
  const headers = lines[0].replace(/^\uFEFF/, "").split(",");
  const idx = headers.findIndex((h) => h.trim() === "Product Type");
  if (idx < 0) return 0;
  let n = 0;
  for (const line of lines.slice(1)) {
    if ((line.split(",")[idx] || "").toLowerCase().includes("service")) n += 1;
  }
  return n;
}

const CATALOG: Array<{
  batch_id: string;
  dataset: string;
  target_key: string;
  title: string;
  instruction: string;
  product_priority: number;
  current: () => number;
  deps: () => boolean;
}> = [
  {
    batch_id: "Batch-001",
    dataset: "industry_library",
    target_key: "industry_library",
    title: "Produce Industry Dataset",
    instruction: "Produce Industry Dataset — expand industry_library toward product target",
    product_priority: 100,
    current: () => rowCount("domains/business_development/industry_library.csv"),
    deps: () => true,
  },
  {
    batch_id: "Batch-009",
    dataset: "buyer_persona_library",
    target_key: "buyer_persona_library",
    title: "Produce Buyer Persona Dataset",
    instruction: "Produce Buyer Persona Dataset — structured buyer personas (Batch-009)",
    product_priority: 96,
    current: () => 0,
    deps: () =>
      rowCount("domains/business_development/industry_library.csv") >= 50 &&
      rowCount("domains/business_development/company_profile.csv") >= 25,
  },
  {
    batch_id: "Batch-002",
    dataset: "service_library",
    target_key: "service_library",
    title: "Produce Service Dataset",
    instruction: "Produce Service Dataset — expand service-type rows in product_catalog",
    product_priority: 95,
    current: () => serviceCount(),
    deps: () => rowCount("domains/business_development/industry_library.csv") >= 50,
  },
  {
    batch_id: "Batch-003",
    dataset: "product_catalog",
    target_key: "product_catalog",
    title: "Produce Product Dataset",
    instruction: "Produce Product Dataset — expand product_catalog",
    product_priority: 94,
    current: () => rowCount("domains/business_development/product_catalog.csv"),
    deps: () => rowCount("domains/business_development/industry_library.csv") >= 50,
  },
  {
    batch_id: "Batch-004",
    dataset: "company_profile",
    target_key: "company_profile",
    title: "Produce Company Dataset",
    instruction: "Produce Company Dataset — expand company_profile",
    product_priority: 93,
    current: () => rowCount("domains/business_development/company_profile.csv"),
    deps: () => rowCount("domains/business_development/industry_library.csv") >= 50,
  },
  {
    batch_id: "Batch-005",
    dataset: "pain_point_library",
    target_key: "pain_point_library",
    title: "Produce Pain Point Dataset",
    instruction: "Produce Pain Point Dataset — expand pain_point_library",
    product_priority: 92,
    current: () => rowCount("domains/business_development/pain_point_library.csv"),
    deps: () => rowCount("domains/business_development/company_profile.csv") >= 25,
  },
  {
    batch_id: "Batch-011",
    dataset: "regulation_library",
    target_key: "regulation_library",
    title: "Produce Regulation Dataset",
    instruction: "Produce Regulation Dataset — regulation knowledge (Batch-011)",
    product_priority: 88,
    current: () => 0,
    deps: () => rowCount("domains/business_development/industry_library.csv") >= 50,
  },
];

export function select_next_mission(): {
  ok: boolean;
  selected: Selected;
  ranking: Array<{ batch_id: string; dataset: string; coverage_pct: number; score: number }>;
} {
  const ranked = CATALOG.filter((c) => c.deps())
    .map((c) => {
      const cur = c.current();
      const tgt = productTargetFor(c.target_key);
      const cov = tgt > 0 ? Math.min(100, (cur / tgt) * 100) : 0;
      if (cov >= 100) return null;
      const gap = (100 - cov) / 100;
      let score = gap * 1000 + c.product_priority * 2 + (cur === 0 ? 50 : 0);
      if (c.batch_id === "Batch-009" && cur === 0) score += 200;
      return {
        batch_id: c.batch_id,
        dataset: c.dataset,
        title: c.title,
        instruction: c.instruction,
        coverage_pct: Math.round(cov * 10) / 10,
        current_rows: cur,
        product_target: tgt,
        product_priority: c.product_priority,
        score: Math.round(score * 100) / 100,
        reason: `lowest_coverage=${Math.round(cov * 10) / 10}% · priority=${c.product_priority}`,
      } as Selected & { score: number };
    })
    .filter(Boolean) as Array<Selected & { score: number }>;

  ranked.sort((a, b) => b.score - a.score || a.coverage_pct - b.coverage_pct);
  const top =
    ranked[0] ||
    ({
      batch_id: "Batch-001",
      dataset: "industry_library",
      title: "Produce Industry Dataset",
      instruction: "Produce Industry Dataset — expand industry_library toward product target",
      coverage_pct: 0,
      current_rows: 0,
      product_target: 250,
      product_priority: 100,
      score: 0,
      reason: "fallback",
    } as Selected);

  return {
    ok: true,
    selected: top,
    ranking: ranked.slice(0, 8).map((r) => ({
      batch_id: r.batch_id,
      dataset: r.dataset,
      coverage_pct: r.coverage_pct,
      score: r.score,
    })),
  };
}
