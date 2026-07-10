/**
 * Executive factory view — derived only from existing production state.
 * No simulated counters. Observe sessions, KPIs, journal, mission selector.
 */

import fs from "fs";
import { getFactoryKpis, type FactoryKpis } from "./factory-kpis";
import { getSessionsDashboard, nextScheduledRunIso, type SessionSummary } from "./sessions";
import { productTargetFor } from "./product-targets";
import { repoPath } from "./paths";
import { selectNextMission } from "./mission-select-bridge";

export type FactoryUiStatus =
  | "ONLINE"
  | "IDLE"
  | "RUNNING"
  | "WAITING"
  | "ERROR";

export type PipelineStageId =
  | "mission"
  | "discovery"
  | "collection"
  | "extraction"
  | "normalization"
  | "validation"
  | "append"
  | "quality"
  | "export"
  | "completed";

export const PIPELINE_STAGES: Array<{ id: PipelineStageId; label: string }> = [
  { id: "mission", label: "Mission" },
  { id: "discovery", label: "Discovery" },
  { id: "collection", label: "Collection" },
  { id: "extraction", label: "Extraction" },
  { id: "normalization", label: "Normalization" },
  { id: "validation", label: "Validation" },
  { id: "append", label: "Append" },
  { id: "quality", label: "Quality" },
  { id: "export", label: "Export" },
  { id: "completed", label: "Completed" },
];

const PRODUCT_DATASETS: Array<{ key: string; label: string; fileStem?: string }> = [
  { key: "industry_library", label: "Industry" },
  { key: "service_library", label: "Service", fileStem: "product_catalog" },
  { key: "product_catalog", label: "Product" },
  { key: "company_profile", label: "Company" },
  { key: "pain_point_library", label: "Pain Point" },
  { key: "solution_library", label: "Solution" },
  { key: "framework_library", label: "Framework" },
  { key: "case_study_library", label: "Case Study" },
  { key: "buyer_persona_library", label: "Buyer Persona" },
  { key: "decision_maker_library", label: "Decision Maker" },
  { key: "regulation_library", label: "Regulation" },
  { key: "opportunity_analysis", label: "Opportunity" },
  { key: "risk_library", label: "Risk" },
  { key: "trend_library", label: "Trend" },
  { key: "competitor_library", label: "Competitor" },
];

function readJson(p: string): Record<string, unknown> | null {
  try {
    if (!fs.existsSync(p)) return null;
    return JSON.parse(fs.readFileSync(p, "utf8"));
  } catch {
    return null;
  }
}

function mapStage(verb?: string, stage?: string, task?: string): PipelineStageId {
  const blob = `${verb || ""} ${stage || ""} ${task || ""}`.toLowerCase();
  if (/complete|finished|done/.test(blob)) return "completed";
  if (/export|packag/.test(blob)) return "export";
  if (/quality|qa\b/.test(blob)) return "quality";
  if (/publish|append|knowledge added|knowledge updated/.test(blob)) return "append";
  if (/validat|review|policy|confidence/.test(blob)) return "validation";
  if (/normaliz/.test(blob)) return "normalization";
  if (/extract|pipeline|entity|understanding/.test(blob)) return "extraction";
  if (/download|document|reading|queue/.test(blob)) return "collection";
  if (/search|connector|planner|gap|discovery|scheduler/.test(blob)) return "discovery";
  if (/mission|session/.test(blob)) return "mission";
  return "mission";
}

function countServiceRows(): number {
  const p = repoPath("domains/business_development/product_catalog.csv");
  if (!fs.existsSync(p)) return 0;
  try {
    const text = fs.readFileSync(p, "utf8");
    const lines = text.split("\n").filter(Boolean);
    if (lines.length < 2) return 0;
    const headers = lines[0].replace(/^\uFEFF/, "").split(",");
    const typeIdx = headers.findIndex((h) => h.trim() === "Product Type");
    if (typeIdx < 0) return 0;
    let n = 0;
    for (const line of lines.slice(1)) {
      // crude CSV split sufficient for type column presence check
      const cols = line.split(",");
      const t = (cols[typeIdx] || "").toLowerCase();
      if (t.includes("service")) n += 1;
    }
    return n;
  } catch {
    return 0;
  }
}

function datasetRowCount(stem: string): number {
  if (stem === "service_library") return countServiceRows();
  if (stem === "risk_library" || stem === "trend_library" || stem === "buyer_persona_library" || stem === "decision_maker_library" || stem === "regulation_library") {
    // dedicated files may not exist yet
    const candidates = [
      repoPath(`domains/business_development/${stem}.csv`),
    ];
    for (const p of candidates) {
      if (!fs.existsSync(p)) continue;
      try {
        const n = fs.readFileSync(p, "utf8").split("\n").filter(Boolean).length - 1;
        return Math.max(0, n);
      } catch {
        /* */
      }
    }
    return 0;
  }
  const p = repoPath(`domains/business_development/${stem}.csv`);
  if (!fs.existsSync(p)) return 0;
  try {
    return Math.max(0, fs.readFileSync(p, "utf8").split("\n").filter(Boolean).length - 1);
  } catch {
    return 0;
  }
}

function lastCommitHint(): string {
  // Prefer latest learning journal / session commit message from session index
  const idx = readJson(repoPath("automation/sessions/index.json"));
  const sessions = (idx?.sessions as SessionSummary[]) || [];
  const s = sessions[0];
  if (s?.session_id) return `session ${s.session_id}`;
  const act = readJson(repoPath("automation/learning/state/live_activity.json"));
  if (act?.session_id) return String(act.session_id);
  return "—";
}

function readinessScore(): number | null {
  const p = repoPath("reports/quality/readiness_v2_summary.json");
  const j = readJson(p);
  if (j?.production_readiness_score != null) {
    return Number(j.production_readiness_score);
  }
  return null;
}

function factoryHealthFromKpis(kpis: FactoryKpis): number {
  // Use dataset readiness as live health signal (0–100)
  return kpis.dataset_readiness ?? 0;
}

export type ExecutiveFactoryView = {
  generated_at: string;
  status: FactoryUiStatus;
  current_mission: string;
  current_dataset: string;
  current_stage: PipelineStageId;
  current_stage_label: string;
  current_source: string;
  current_workflow: string;
  current_batch: string;
  elapsed_seconds: number | null;
  estimated_completion: string;
  next_scheduled_mission: string;
  next_scheduled_run: string;
  counters: {
    rows_today: number;
    rows_rejected_today: number;
    documents_processed_today: number;
    sessions_today: number;
    rows_week: number;
    rows_month: number;
    average_confidence: number | null;
    freshness: number;
    duplicate_rate: number;
  };
  coverage: Array<{
    key: string;
    label: string;
    current: number;
    target: number;
    coverage_pct: number;
    readiness: number;
    href: string;
  }>;
  knowledge_feed: Array<{
    id: string;
    label: string;
    delta: number;
    dataset: string;
    href: string;
    ts: string;
    session_id?: string;
  }>;
  heartbeat: {
    online: boolean;
    last_event: string;
    last_event_ts: string;
    last_commit: string;
    last_session: string;
    last_workflow: string;
    rows_today: number;
    factory_health: number;
    production_readiness: number | null;
    idle_message: string | null;
  };
  timeline: Array<{
    session_id: string;
    mission: string;
    status: string;
    start_time: string;
    end_time: string;
    knowledge_added: number;
    knowledge_rejected: number;
    trigger: string;
    events: number;
  }>;
  pipeline_stages: typeof PIPELINE_STAGES;
  kpis: FactoryKpis;
};

export function getExecutiveFactoryView(): ExecutiveFactoryView {
  const kpis = getFactoryKpis();
  const dash = getSessionsDashboard();
  const activity =
    readJson(repoPath("automation/learning/state/live_activity.json")) || {};

  const gaRunning = false; // GA status only on client via /api/sessions
  const statusRaw = String(activity.status || kpis.factory_status || "idle").toLowerCase();
  let status: FactoryUiStatus = "IDLE";
  if (statusRaw === "running" || kpis.factory_status === "running") status = "RUNNING";
  else if (statusRaw === "waiting_review" || statusRaw === "waiting") status = "WAITING";
  else if (statusRaw === "error" || statusRaw === "failed" || kpis.factory_status === "error")
    status = "ERROR";
  else if (statusRaw === "idle" || statusRaw === "completed") status = "IDLE";
  else status = "ONLINE";

  // If we have recent activity within 2 minutes, treat as ONLINE when idle
  const updatedAt = String(activity.updated_at || "");
  if (status === "IDLE" && updatedAt) {
    const age = Date.now() - new Date(updatedAt).getTime();
    if (Number.isFinite(age) && age < 120_000) status = "ONLINE";
  }

  const currentTask = String(
    activity.current_task || kpis.current_activity || ""
  );
  const stageId = mapStage(
    undefined,
    String(activity.stage || ""),
    currentTask
  );

  // Mission selector snapshot (real ranking from coverage + deps)
  let batch = "—";
  let nextMission = kpis.current_mission;
  try {
    const m = selectNextMission();
    if (m?.selected) {
      batch = String(m.selected.batch_id || "—");
      if (status === "IDLE" || status === "ONLINE") {
        nextMission = String(m.selected.instruction || nextMission);
      }
    }
  } catch {
    const r = readJson(repoPath("reports/quality/readiness_v2_summary.json"));
    const sm = (r?.selected_mission || {}) as Record<string, unknown>;
    if (sm.batch_id) batch = String(sm.batch_id);
    if (sm.instruction && (status === "IDLE" || status === "ONLINE")) {
      nextMission = String(sm.instruction);
    }
  }

  const currentDataset = String(
    activity.current_dataset ||
      activity.dataset ||
      (kpis.datasets?.find((d) => d.current_rows > 0)?.name) ||
      "industry_library"
  );

  const currentSource = String(
    activity.current_source || "—"
  );

  const workflow =
    status === "RUNNING"
      ? "Learn"
      : String(activity.execution_model || "github_actions");

  // Elapsed from current/last session
  let elapsed: number | null = null;
  const cur = dash.current_session;
  if (cur?.start_time) {
    const start = new Date(cur.start_time).getTime();
    const end = cur.end_time
      ? new Date(cur.end_time).getTime()
      : Date.now();
    if (Number.isFinite(start)) {
      elapsed = Math.max(0, Math.round((end - start) / 1000));
    }
  } else if (typeof dash.session_duration === "number") {
    elapsed = dash.session_duration;
  }

  // Coverage cards
  const readinessByName = new Map(
    (kpis.datasets || []).map((d) => [d.name, d])
  );
  const coverage = PRODUCT_DATASETS.map((d) => {
    const stem = d.fileStem || d.key;
    const current =
      d.key === "service_library"
        ? countServiceRows()
        : d.key === "product_catalog"
          ? datasetRowCount("product_catalog")
          : datasetRowCount(d.key);
    const target = productTargetFor(
      d.key === "service_library" ? "service_library" : d.key
    );
    const pct =
      target > 0 ? Math.min(100, Math.round((current / target) * 1000) / 10) : 0;
    const ready =
      readinessByName.get(stem)?.readiness ??
      readinessByName.get(d.key)?.readiness ??
      (current > 0 ? 50 : 0);
    return {
      key: d.key,
      label: d.label,
      current,
      target,
      coverage_pct: pct,
      readiness: ready,
      href: `/datasets`,
    };
  });

  // Knowledge feed from recent sessions (real deltas)
  const sessions = (dash.sessions || []).slice(0, 20);
  const knowledge_feed: ExecutiveFactoryView["knowledge_feed"] = [];
  for (const s of sessions) {
    const added = Number(s.knowledge_added || 0);
    const updated = Number(s.knowledge_updated || 0);
    const total = added + updated;
    if (total <= 0) continue;
    // Infer dataset from mission text
    const mission = String(s.mission || "").toLowerCase();
    let ds = "industry_library";
    let label = "Knowledge rows";
    if (mission.includes("service")) {
      ds = "service_library";
      label = "Services";
    } else if (mission.includes("product")) {
      ds = "product_catalog";
      label = "Products";
    } else if (mission.includes("company")) {
      ds = "company_profile";
      label = "Companies";
    } else if (mission.includes("pain")) {
      ds = "pain_point_library";
      label = "Pain Points";
    } else if (mission.includes("solution")) {
      ds = "solution_library";
      label = "Solutions";
    } else if (mission.includes("framework")) {
      ds = "framework_library";
      label = "Frameworks";
    } else if (mission.includes("case")) {
      ds = "case_study_library";
      label = "Case Studies";
    } else if (mission.includes("regulat")) {
      ds = "regulation_library";
      label = "Regulations";
    } else if (mission.includes("persona")) {
      ds = "buyer_persona_library";
      label = "Personas";
    } else if (mission.includes("industry")) {
      ds = "industry_library";
      label = "Industries";
    }
    knowledge_feed.push({
      id: s.session_id,
      label: `+${total} ${label}`,
      delta: total,
      dataset: ds,
      href: "/datasets",
      ts: String(s.end_time || s.start_time || ""),
      session_id: s.session_id,
    });
  }

  // Daily rejected from daily counters
  const day = new Date().toISOString().slice(0, 10);
  const daily = readJson(repoPath(`automation/learning/state/daily_${day}.json`));
  const rejectedToday = Number(daily?.knowledge_rejected || 0);
  const hist = dash.history;
  const sessionsToday = hist?.today?.sessions ?? 0;
  // documents: approximate from events count on today's sessions when available
  const docsToday = sessions.filter((s) =>
    String(s.start_time || "").startsWith(day)
  ).length;

  const lastEvent =
    kpis.recent_activity?.[0]?.detail ||
    String(activity.current_thought || activity.current_task || "—");
  const lastEventTs =
    kpis.recent_activity?.[0]?.ts || String(activity.updated_at || "");

  const timeline = sessions.slice(0, 16).map((s) => ({
    session_id: s.session_id,
    mission: String(s.mission || "—"),
    status: String(s.status || "unknown"),
    start_time: String(s.start_time || ""),
    end_time: String(s.end_time || ""),
    knowledge_added: Number(s.knowledge_added || 0),
    knowledge_rejected: Number(s.knowledge_rejected || 0),
    trigger: String(s.trigger || ""),
    events: Number(s.events || 0),
  }));

  const nextRun = dash.next_scheduled_run || nextScheduledRunIso();
  const idleMessage =
    status === "IDLE" || status === "ONLINE"
      ? `Factory Idle · Waiting for scheduled mission · Next run ${nextRun}`
      : null;

  return {
    generated_at: new Date().toISOString(),
    status,
    current_mission: String(
      activity.mission_id || kpis.current_mission || nextMission || "—"
    ),
    current_dataset: currentDataset,
    current_stage: stageId,
    current_stage_label:
      PIPELINE_STAGES.find((s) => s.id === stageId)?.label || stageId,
    current_source: currentSource,
    current_workflow: workflow,
    current_batch: batch,
    elapsed_seconds: elapsed,
    estimated_completion: kpis.capacity?.estimated_completion || "—",
    next_scheduled_mission: nextMission,
    next_scheduled_run: nextRun,
    counters: {
      rows_today: kpis.rows_added_today,
      rows_rejected_today: rejectedToday,
      documents_processed_today: docsToday,
      sessions_today: sessionsToday,
      rows_week: kpis.rows_added_week,
      rows_month: kpis.rows_added_month,
      average_confidence: kpis.average_confidence,
      freshness: kpis.freshness,
      duplicate_rate: kpis.duplicate_rate,
    },
    coverage,
    knowledge_feed: knowledge_feed.slice(0, 24),
    heartbeat: {
      online: status !== "ERROR",
      last_event: lastEvent,
      last_event_ts: lastEventTs,
      last_commit: lastCommitHint(),
      last_session: String(
        dash.current_session?.session_id ||
          dash.last_successful_run?.session_id ||
          activity.session_id ||
          "—"
      ),
      last_workflow: workflow,
      rows_today: kpis.rows_added_today,
      factory_health: factoryHealthFromKpis(kpis),
      production_readiness: readinessScore(),
      idle_message: idleMessage,
    },
    timeline,
    pipeline_stages: PIPELINE_STAGES,
    kpis,
  };
}
