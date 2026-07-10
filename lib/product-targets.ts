/**
 * Product KPI target registry (configurable, not hardcoded).
 * Source: automation/config/product_targets.yaml
 */

import fs from "fs";
import { repoPath } from "./paths";
import { loadSimpleYaml } from "./simple-yaml";

export type ProductTargetsConfig = {
  version: string;
  freshness_window_days: number;
  targets: Record<string, number>;
  sprint_milestones: Record<string, number>;
  capacity: {
    lookback_days: number;
    sessions_lookback: number;
  };
};

const DEFAULTS: ProductTargetsConfig = {
  version: "1.0",
  freshness_window_days: 90,
  targets: {
    industry_library: 250,
    company_profile: 10000,
    product_catalog: 5000,
    service_library: 2000,
    pain_point_library: 3000,
    solution_library: 3000,
    framework_library: 500,
    case_study_library: 1000,
    discovery_question_library: 500,
    buyer_persona_library: 500,
    decision_maker_library: 500,
    regulation_library: 1000,
    competitor_library: 1000,
    opportunity_analysis: 2000,
    business_signal_library: 1000,
    _default: 100,
  },
  sprint_milestones: {
    industry_phase1: 50,
    industry_stretch: 100,
  },
  capacity: {
    lookback_days: 30,
    sessions_lookback: 30,
  },
};

let cached: ProductTargetsConfig | null = null;

export function loadProductTargets(): ProductTargetsConfig {
  if (cached) return cached;
  const p = repoPath("automation/config/product_targets.yaml");
  try {
    if (!fs.existsSync(p)) {
      cached = DEFAULTS;
      return cached;
    }
    const raw = loadSimpleYaml(fs.readFileSync(p, "utf8")) as Record<
      string,
      unknown
    >;
    const targets = {
      ...DEFAULTS.targets,
      ...((raw.targets as Record<string, number>) || {}),
    };
    const sprint = {
      ...DEFAULTS.sprint_milestones,
      ...((raw.sprint_milestones as Record<string, number>) || {}),
    };
    const cap = {
      ...DEFAULTS.capacity,
      ...((raw.capacity as Record<string, number>) || {}),
    };
    cached = {
      version: String(raw.version || DEFAULTS.version),
      freshness_window_days: Number(
        raw.freshness_window_days ?? DEFAULTS.freshness_window_days
      ),
      targets,
      sprint_milestones: sprint,
      capacity: {
        lookback_days: Number(cap.lookback_days ?? 30),
        sessions_lookback: Number(cap.sessions_lookback ?? 30),
      },
    };
    return cached;
  } catch {
    cached = DEFAULTS;
    return cached;
  }
}

/** Product target for a dataset file stem (e.g. industry_library). */
export function productTargetFor(datasetName: string): number {
  const cfg = loadProductTargets();
  const key = datasetName.replace(/\.csv$/i, "");
  const n = Number(cfg.targets[key] ?? cfg.targets._default ?? 100);
  return n > 0 ? n : 100;
}

/** Coverage against product target: current / target → 0–100%. */
export function productCoveragePct(current: number, target: number): number {
  if (target <= 0) return 0;
  return Math.min(100, Math.round((current / target) * 1000) / 10);
}
