/**
 * Scheduler heartbeat reader — production observability only.
 * Source: automation/learning/state/scheduler_heartbeat.json
 * Written by automation/learning/heartbeat.py each production cycle.
 */

import fs from "fs";
import { repoPath } from "./paths";

export type SchedulerHeartbeat = {
  status: "Running" | "Idle" | "Publishing" | "Failed" | string;
  last_heartbeat: string | null;
  last_success: string | null;
  last_failure: string | null;
  current_job: string | null;
  job_id: string | null;
  dataset: string | null;
  mission_id: string | null;
  session_id: string | null;
  job_started_at: string | null;
  job_duration_seconds: number | null;
  last_error: string | null;
  cycle_count: number;
  success_count: number;
  failure_count: number;
  updated_at: string | null;
};

function emptyHeartbeat(): SchedulerHeartbeat {
  return {
    status: "Idle",
    last_heartbeat: null,
    last_success: null,
    last_failure: null,
    current_job: null,
    job_id: null,
    dataset: null,
    mission_id: null,
    session_id: null,
    job_started_at: null,
    job_duration_seconds: null,
    last_error: null,
    cycle_count: 0,
    success_count: 0,
    failure_count: 0,
    updated_at: null,
  };
}

/**
 * Load latest scheduler/production heartbeat from existing state storage.
 * Observe-only — never mutates production files.
 */
export function getSchedulerHeartbeat(): SchedulerHeartbeat {
  const p = repoPath("automation/learning/state/scheduler_heartbeat.json");
  try {
    if (!fs.existsSync(p)) return emptyHeartbeat();
    const raw = JSON.parse(fs.readFileSync(p, "utf8")) as Record<string, unknown>;
    const base = emptyHeartbeat();
    return {
      ...base,
      status: String(raw.status || "Idle"),
      last_heartbeat: (raw.last_heartbeat as string) || null,
      last_success: (raw.last_success as string) || null,
      last_failure: (raw.last_failure as string) || null,
      current_job: (raw.current_job as string) || null,
      job_id: (raw.job_id as string) || null,
      dataset: (raw.dataset as string) || null,
      mission_id: (raw.mission_id as string) || null,
      session_id: (raw.session_id as string) || null,
      job_started_at: (raw.job_started_at as string) || null,
      job_duration_seconds:
        raw.job_duration_seconds != null
          ? Number(raw.job_duration_seconds)
          : null,
      last_error: (raw.last_error as string) || null,
      cycle_count: Number(raw.cycle_count || 0),
      success_count: Number(raw.success_count || 0),
      failure_count: Number(raw.failure_count || 0),
      updated_at: (raw.updated_at as string) || null,
    };
  } catch {
    return emptyHeartbeat();
  }
}
