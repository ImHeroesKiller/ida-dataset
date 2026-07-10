/**
 * Learning mode config — development vs production.
 * Source of truth: automation/config/learning.yaml → learning_mode
 */

import fs from "fs";
import { repoPath } from "@/lib/paths";
import { loadSimpleYaml } from "@/lib/simple-yaml";

export type LearningModeName = "development" | "production";

export type LearningModeConfig = {
  mode: LearningModeName;
  auto_publish: boolean;
  progressive_publish: boolean;
  review_bypassed: boolean;
  publish_mode: "auto" | "manual";
  publish_rate: number;
  publish_rate_unit: string;
  /** Milliseconds between progressive publishes (backend only). */
  interval_ms: number;
  label: string;
};

function readYaml(): Record<string, unknown> {
  const p = repoPath("automation/config/learning.yaml");
  try {
    if (!fs.existsSync(p)) return {};
    const data = loadSimpleYaml(fs.readFileSync(p, "utf8"));
    return (data && typeof data === "object" ? data : {}) as Record<
      string,
      unknown
    >;
  } catch {
    return {};
  }
}

/** Env override: IDA_LEARNING_MODE=production|development */
export function getLearningMode(): LearningModeConfig {
  const raw = readYaml();
  const block = (raw.learning_mode || {}) as Record<string, unknown>;
  const envMode = (process.env.IDA_LEARNING_MODE || "").toLowerCase();
  let mode = String(block.mode || "development").toLowerCase();
  // Vercel is always a read-only production host unless explicitly overridden.
  // Prevents auto_publish GET side-effects (EROFS on publish_state.json).
  if (process.env.VERCEL && envMode !== "development") {
    mode = "production";
  }
  if (envMode === "production" || envMode === "development") mode = envMode;
  if (mode !== "production") mode = "development";

  const profile = (
    mode === "production" ? block.production : block.development
  ) as Record<string, unknown> | undefined;

  const rate = Math.max(0, Number(profile?.publish_rate ?? 1));
  const interval_ms =
    rate <= 0 ? 0 : Math.round(1000 / Math.max(rate, 0.001));

  return {
    mode: mode as LearningModeName,
    auto_publish: Boolean(profile?.auto_publish ?? mode === "development"),
    progressive_publish: Boolean(
      profile?.progressive_publish ?? mode === "development"
    ),
    review_bypassed: Boolean(profile?.review_bypassed ?? mode === "development"),
    publish_mode: (profile?.publish_mode as "auto" | "manual") ||
      (mode === "development" ? "auto" : "manual"),
    publish_rate: rate,
    publish_rate_unit: String(
      profile?.publish_rate_unit || "rows_per_second"
    ),
    interval_ms,
    label: mode === "development" ? "Development" : "Production",
  };
}

export function isDevelopmentMode(): boolean {
  return getLearningMode().mode === "development";
}
