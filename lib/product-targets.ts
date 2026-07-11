/**
 * Product KPI target registry — dynamic manufacturing profiles.
 * Source: automation/config/product_targets.yaml
 *
 * Coverage uses stretch_target as a progress reference only.
 * hard_limit null / never_stop means no artificial finish line.
 */

import fs from "fs";
import { repoPath } from "./paths";
import { loadSimpleYaml } from "./simple-yaml";

export type DatasetTargetProfile = {
  minimum_target: number;
  stretch_target: number;
  estimated_universe: string | number;
  hard_limit: number | null;
};

export type ProductTargetsConfig = {
  version: string;
  continuous_manufacturing: boolean;
  never_stop_at_numeric_target: boolean;
  freshness_window_days: number;
  /** Legacy flat map: minimum targets (and stretch when datasets block present) */
  targets: Record<string, number>;
  datasets: Record<string, DatasetTargetProfile>;
  sprint_milestones: Record<string, number>;
  capacity: {
    lookback_days: number;
    sessions_lookback: number;
  };
};

const DEFAULT_PROFILE: DatasetTargetProfile = {
  minimum_target: 100,
  stretch_target: 1000,
  estimated_universe: "dynamic",
  hard_limit: null,
};

const DEFAULTS: ProductTargetsConfig = {
  version: "2.0",
  continuous_manufacturing: true,
  never_stop_at_numeric_target: true,
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
    risk_library: 500,
    trend_library: 500,
    competitor_library: 1000,
    opportunity_analysis: 2000,
    business_signal_library: 1000,
    _default: 100,
  },
  datasets: {
    industry_library: {
      minimum_target: 250,
      stretch_target: 5000,
      estimated_universe: "dynamic",
      hard_limit: null,
    },
    company_profile: {
      minimum_target: 10000,
      stretch_target: 100000,
      estimated_universe: "dynamic",
      hard_limit: null,
    },
    service_library: {
      minimum_target: 2000,
      stretch_target: 50000,
      estimated_universe: "dynamic",
      hard_limit: null,
    },
    _default: DEFAULT_PROFILE,
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

function asProfile(
  raw: unknown,
  fallbackMin: number
): DatasetTargetProfile {
  if (!raw || typeof raw !== "object") {
    return {
      minimum_target: fallbackMin,
      stretch_target: Math.max(fallbackMin * 10, fallbackMin + 100),
      estimated_universe: "dynamic",
      hard_limit: null,
    };
  }
  const o = raw as Record<string, unknown>;
  const min = Number(o.minimum_target ?? fallbackMin);
  const stretch = Number(o.stretch_target ?? Math.max(min * 10, min + 100));
  let hard: number | null = null;
  if (o.hard_limit != null && o.hard_limit !== "null" && o.hard_limit !== "") {
    const n = Number(o.hard_limit);
    hard = Number.isFinite(n) && n > 0 ? n : null;
  }
  return {
    minimum_target: min > 0 ? min : fallbackMin,
    stretch_target: stretch > 0 ? stretch : Math.max(min * 10, 1000),
    estimated_universe: (o.estimated_universe as string | number) ?? "dynamic",
    hard_limit: hard,
  };
}

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
    const flatTargets = {
      ...DEFAULTS.targets,
      ...((raw.targets as Record<string, number>) || {}),
    };
    const rawDatasets = (raw.datasets as Record<string, unknown>) || {};
    const datasets: Record<string, DatasetTargetProfile> = {
      ...DEFAULTS.datasets,
    };
    for (const [k, v] of Object.entries(rawDatasets)) {
      datasets[k] = asProfile(v, Number(flatTargets[k] ?? flatTargets._default ?? 100));
    }
    // Ensure every flat target has a profile
    for (const [k, min] of Object.entries(flatTargets)) {
      if (!datasets[k]) {
        datasets[k] = asProfile(null, Number(min));
      }
    }
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
      continuous_manufacturing: raw.continuous_manufacturing !== false,
      never_stop_at_numeric_target: raw.never_stop_at_numeric_target !== false,
      freshness_window_days: Number(
        raw.freshness_window_days ?? DEFAULTS.freshness_window_days
      ),
      targets: flatTargets,
      datasets,
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

export function datasetProfile(datasetName: string): DatasetTargetProfile {
  const cfg = loadProductTargets();
  const key = datasetName.replace(/\.csv$/i, "");
  return (
    cfg.datasets[key] ||
    cfg.datasets._default || {
      minimum_target: Number(cfg.targets._default ?? 100),
      stretch_target: 1000,
      estimated_universe: "dynamic",
      hard_limit: null,
    }
  );
}

/**
 * Progress-reference target (stretch). Not a finish line.
 * Used for coverage % display and ETA — factory continues past this.
 */
export function productTargetFor(datasetName: string): number {
  const prof = datasetProfile(datasetName);
  const n = Number(prof.stretch_target || prof.minimum_target || 100);
  return n > 0 ? n : 100;
}

/** Bootstrap floor only — does not stop manufacturing. */
export function productMinimumFor(datasetName: string): number {
  return Math.max(1, Number(datasetProfile(datasetName).minimum_target || 100));
}

/** Coverage against stretch target: current / stretch → 0–100% (progress only). */
export function productCoveragePct(current: number, target: number): number {
  if (target <= 0) return 0;
  return Math.min(100, Math.round((current / target) * 1000) / 10);
}
