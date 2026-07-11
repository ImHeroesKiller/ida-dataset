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
  // buyer_persona / decision_maker / regulation / risk / trend use dedicated CSVs
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
    /** Real acquisition pipeline counters (from sessions + queues) */
    documents_discovered: number;
    documents_downloaded: number;
    candidates_extracted: number;
    candidates_validated: number;
    publish_queue_size: number;
    rows_appended: number;
    documents_queued: number;
    candidates_queued: number;
  };
  /** Latest real production trace snapshot (no simulation) */
  production: {
    current_stage: string;
    current_connector: string;
    current_document: string;
    last_connector: string;
    last_document: string;
    last_published_entity: string;
    documents_queued: number;
    documents_processed: number;
    candidates_queued: number;
    publish_queue: number;
    rows_appended_today: number;
    publish_balance: Record<string, unknown> | null;
    connectors: Array<Record<string, unknown>>;
  };
  /** Discovery layer analytics (search engines = discovery only) */
  discovery: {
    queries_today: number;
    urls_found: number;
    urls_accepted: number;
    urls_rejected: number;
    urls_remaining: number;
    top_provider: string;
    top_trusted_source: string;
    providers_ready: number;
    providers_offline: number;
    providers_misconfigured: number;
    providers_exhausted: number;
    stop_reason: string;
    urls_per_hour: number;
    knowledge_yield: number;
    provider_utilization_top: string;
  };
  /** Continuous manufacturing intelligence (real state only) */
  manufacturing: {
    mode: string;
    knowledge_gap_dataset: string;
    knowledge_gap_score: number;
    estimated_universe: number;
    growth_velocity: number;
    coverage_velocity: number;
    rows_today: number;
    rows_week: number;
    rows_month: number;
    knowledge_produced: number;
    top_dataset: string;
    top_source: string;
    top_connector: string;
    top_mission: string;
    factory_capacity_rph: number;
    production_cost: number;
    knowledge_roi: number;
    /** Throughput metrics (real production only — metrics-only dashboard evolution) */
    rows_per_hour: number;
    docs_per_hour: number;
    rows_per_session: number;
    avg_connector_latency_ms: number;
    worker_utilization: number;
    queue_depth: number;
    pipeline_throughput: number;
    knowledge_growth_velocity: number;
    production_efficiency: number;
    process_ratio_pct: number;
    auto_publish_ratio: number;
    manual_review_ratio: number;
    /** Enterprise function generalization metrics (metrics-only; no redesign) */
    enterprise_function_count: number;
    knowledge_by_top_function: string;
    coverage_top_function: string;
    top_growing_function: string;
    weakest_function: string;
    production_distribution_top: string;
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

  const productionTrace =
    readJson(repoPath("automation/learning/state/production_trace.json")) || {};
  const discoveryAnalytics =
    readJson(repoPath("automation/learning/state/discovery_analytics.json")) || {};
  const manufacturingState =
    readJson(repoPath("automation/learning/state/manufacturing_state.json")) || {};
  const throughputStats =
    readJson(repoPath("automation/learning/state/throughput_stats.json")) || {};
  const acquisitionPerf =
    readJson(repoPath("automation/learning/state/acquisition_performance.json")) || {};
  const currentSource = String(
    activity.current_source ||
      productionTrace.current_connector ||
      productionTrace.last_connector ||
      "—"
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

  // Real acquisition counters from session knowledge_delta + document queues
  let documentsDiscovered = 0;
  let documentsDownloaded = 0;
  let candidatesExtracted = 0;
  let candidatesValidated = 0;
  let rowsAppended = 0;
  for (const s of sessions) {
    if (!String(s.start_time || "").startsWith(day)) continue;
    const delta = (s as { knowledge_delta?: Record<string, unknown> }).knowledge_delta || {};
    documentsDiscovered += Number(delta.documents_discovered || 0);
    documentsDownloaded += Number(delta.documents_downloaded || 0);
    candidatesExtracted += Number(delta.candidates_extracted || 0);
    candidatesValidated += Number(delta.candidates_validated || 0);
    rowsAppended += Number(s.knowledge_added || 0);
  }
  // Fallback: count document queue files when sessions lack acquisition fields
  const countJson = (rel: string) => {
    try {
      const dir = repoPath(rel);
      if (!fs.existsSync(dir)) return 0;
      return fs.readdirSync(dir).filter((f) => f.endsWith(".json")).length;
    } catch {
      return 0;
    }
  };
  const docsIncoming = countJson("automation/queue/documents/incoming");
  const docsProcessed = countJson("automation/queue/documents/processed");
  const docsProcessing = countJson("automation/queue/documents/processing");
  if (documentsDownloaded === 0) {
    documentsDownloaded = docsIncoming + docsProcessed + docsProcessing;
  }
  if (documentsDiscovered === 0) {
    documentsDiscovered = documentsDownloaded;
  }
  const publishQueueSize =
    countJson("automation/queue/publish") +
    countJson("automation/queue/candidates/pending");
  const docsQueued =
    countJson("automation/queue/documents/incoming") +
    countJson("automation/queue/documents/processing");
  const candidatesQueued =
    countJson("automation/queue/candidates/pending") +
    countJson("automation/queue/publish");
  const docsToday = documentsDownloaded || sessions.filter((s) =>
    String(s.start_time || "").startsWith(day)
  ).length;

  // Prefer live production trace counters when present
  const ptSummary = (productionTrace.summary || {}) as Record<string, unknown>;
  const ptPublish = (productionTrace.publish || {}) as Record<string, unknown>;
  const ptDq = (productionTrace.document_queue || {}) as Record<string, unknown>;
  if (Number(ptSummary.documents_discovered || 0) > 0) {
    documentsDiscovered = Math.max(
      documentsDiscovered,
      Number(ptSummary.documents_discovered || 0)
    );
  }
  if (Number(ptSummary.documents_downloaded || 0) > 0) {
    documentsDownloaded = Math.max(
      documentsDownloaded,
      Number(ptSummary.documents_downloaded || 0)
    );
  }
  if (Number(ptPublish.extracted || ptSummary.candidates_extracted || 0) > 0) {
    candidatesExtracted = Math.max(
      candidatesExtracted,
      Number(ptPublish.extracted || ptSummary.candidates_extracted || 0)
    );
  }
  if (Number(ptPublish.validated || ptSummary.candidates_validated || 0) > 0) {
    candidatesValidated = Math.max(
      candidatesValidated,
      Number(ptPublish.validated || ptSummary.candidates_validated || 0)
    );
  }

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
      String(productionTrace.current_stage || "").replace(/_/g, " ") ||
      PIPELINE_STAGES.find((s) => s.id === stageId)?.label ||
      stageId,
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
      documents_discovered: documentsDiscovered,
      documents_downloaded: documentsDownloaded,
      candidates_extracted: candidatesExtracted,
      candidates_validated: candidatesValidated,
      publish_queue_size: publishQueueSize,
      rows_appended: rowsAppended || kpis.rows_added_today,
      documents_queued: docsQueued || Number(ptDq.queued || 0),
      candidates_queued: candidatesQueued || Number(ptPublish.queued || 0),
    },
    production: {
      current_stage: String(
        productionTrace.current_stage ||
          activity.current_stage ||
          stageId ||
          "idle"
      ),
      current_connector: String(
        productionTrace.current_connector ||
          activity.current_connector ||
          "—"
      ),
      current_document: String(
        productionTrace.current_document ||
          activity.current_document ||
          "—"
      ),
      last_connector: String(
        productionTrace.last_connector || activity.last_connector || "—"
      ),
      last_document: String(
        productionTrace.last_document || activity.last_document || "—"
      ),
      last_published_entity: String(
        productionTrace.last_published_entity ||
          activity.last_published_entity ||
          activity.last_learned ||
          "—"
      ),
      documents_queued: docsQueued || Number(ptDq.queued || 0),
      documents_processed:
        documentsDownloaded ||
        Number(ptDq.completed || 0) ||
        Number(ptSummary.documents_downloaded || 0),
      candidates_queued: candidatesQueued || Number(ptPublish.queued || 0),
      publish_queue: publishQueueSize,
      rows_appended_today: rowsAppended || kpis.rows_added_today,
      publish_balance: Object.keys(ptPublish).length ? ptPublish : null,
      connectors: Array.isArray(productionTrace.connectors)
        ? (productionTrace.connectors as Array<Record<string, unknown>>).slice(0, 12)
        : [],
    },
    discovery: (() => {
      const providers = Array.isArray(discoveryAnalytics.providers)
        ? (discoveryAnalytics.providers as Array<Record<string, unknown>>)
        : [];
      const ready = providers.filter(
        (p) =>
          p.credentials_available === true ||
          p.status === "ready" ||
          ["rss", "atom", "sitemap", "trusted_site"].includes(String(p.api_type || ""))
      ).length;
      const offline = providers.filter(
        (p) =>
          p.credentials_available === false ||
          String((p.health as { status?: string } | undefined)?.status || "") ===
            "offline"
      ).length;
      // top provider by urls
      let topProvider = "—";
      let topUrls = -1;
      for (const p of providers) {
        const u = Number(p.urls || 0);
        if (u > topUrls) {
          topUrls = u;
          topProvider = String(p.name || p.provider_id || "—");
        }
      }
      // top trusted source by accepted url attribution
      const usage: Record<string, number> = {};
      for (const a of (discoveryAnalytics.accepted_urls || []) as Array<
        Record<string, unknown>
      >) {
        const sid = String(a.source_id || "");
        if (!sid) continue;
        usage[sid] = (usage[sid] || 0) + 1;
      }
      let topSource = "—";
      let topN = -1;
      for (const [sid, n] of Object.entries(usage)) {
        if (n > topN) {
          topN = n;
          topSource = sid;
        }
      }
      const misconfigured = providers.filter(
        (p) =>
          String(p.operational_status || "") === "MISCONFIGURED" ||
          String(p.status || "") === "misconfigured"
      ).length;
      const exhausted = providers.filter((p) => p.exhausted === true).length;
      // top utilization provider
      let topUtilName = "—";
      let topUtil = -1;
      for (const p of providers) {
        const u = Number(p.utilization || 0);
        if (u > topUtil) {
          topUtil = u;
          topUtilName = String(p.name || p.provider_id || "—");
        }
      }
      const acceptedN = Number(discoveryAnalytics.urls_accepted || 0);
      const foundN = Number(discoveryAnalytics.urls_discovered || 0);
      return {
        queries_today: Number(discoveryAnalytics.queries_executed || 0),
        urls_found: foundN,
        urls_accepted: acceptedN,
        urls_rejected: Number(discoveryAnalytics.urls_rejected || 0),
        urls_remaining: Number(discoveryAnalytics.urls_remaining || 0),
        top_provider: topProvider,
        top_trusted_source: topSource,
        providers_ready: ready,
        providers_offline: offline,
        providers_misconfigured:
          misconfigured || Number(discoveryAnalytics.providers_misconfigured || 0),
        providers_exhausted:
          exhausted || Number(discoveryAnalytics.providers_exhausted || 0),
        stop_reason: String(discoveryAnalytics.stop_reason || "—"),
        urls_per_hour: Number(discoveryAnalytics.urls_per_hour || 0),
        knowledge_yield: foundN > 0 ? Math.round((acceptedN / foundN) * 1000) / 1000 : 0,
        provider_utilization_top: topUtilName,
      };
    })(),
    manufacturing: (() => {
      const modeObj = (manufacturingState.mode || {}) as Record<string, unknown>;
      const gap = (manufacturingState.knowledge_gap_summary ||
        {}) as Record<string, unknown>;
      const cap = (manufacturingState.capacity || {}) as Record<string, unknown>;
      const eco = (manufacturingState.economics || {}) as Record<string, unknown>;
      const growth = (manufacturingState.growth || {}) as Record<string, unknown>;
      const sel = (manufacturingState.selected_mission ||
        {}) as Record<string, unknown>;
      const evals = Array.isArray(manufacturingState.evaluations)
        ? (manufacturingState.evaluations as Array<Record<string, unknown>>)
        : [];
      const topEval = evals[0] || {};
      const univ = (topEval.universe || {}) as Record<string, unknown>;
      const topSrc =
        Array.isArray(eco.rows_per_source) && eco.rows_per_source[0]
          ? String(
              (eco.rows_per_source[0] as Record<string, unknown>).source_id || "—"
            )
          : "—";
      const topConn =
        Array.isArray(eco.rows_per_connector) && eco.rows_per_connector[0]
          ? String(
              (eco.rows_per_connector[0] as Record<string, unknown>).name ||
                (eco.rows_per_connector[0] as Record<string, unknown>)
                  .connector_id ||
                "—"
            )
          : String(
              throughputStats.top_connector ||
                productionTrace.last_connector ||
                "—"
            );
      const thr = (throughputStats.throughput ||
        acquisitionPerf.throughput ||
        {}) as Record<string, unknown>;
      const wrk = (throughputStats.workers || {}) as Record<string, unknown>;
      const tr = (throughputStats.traces || {}) as Record<string, unknown>;
      const sess = (throughputStats.sessions || {}) as Record<string, unknown>;
      const q = (throughputStats.queues || {}) as Record<string, unknown>;
      const dq = (q.document_queue || {}) as Record<string, unknown>;
      const cq = (q.candidate_queue || {}) as Record<string, unknown>;
      const pq = (q.publish_queue || {}) as Record<string, unknown>;
      const pubPol = (throughputStats.publish_policy || {}) as Record<
        string,
        unknown
      >;
      const rowsH = Number(thr.rows_per_hour || cap.rows_per_hour || 0);
      const docsH = Number(thr.documents_per_hour || cap.documents_per_hour || 0);
      const rowsSess = Number(sess.rows_per_session || kpis.capacity?.average_rows_per_session || 0);
      const docs = Number(thr.documents || tr.documents_processed || 0);
      const rows = Number(thr.rows || tr.rows_published || 0);
      const autoN = Number(pubPol.last_published || 0);
      const manN = Number(pubPol.last_manual_or_skipped || 0);
      const autoDenom = Math.max(1, autoN + manN);
      const efState =
        (manufacturingState.enterprise_functions as Record<string, unknown>) ||
        readJson(repoPath("automation/learning/state/enterprise_function_state.json")) ||
        readJson(repoPath("reports/enterprise/enterprise_state.json")) ||
        {};
      const efTopGrow = (efState.top_growing_function || {}) as Record<string, unknown>;
      const efWeak = (efState.weakest_function || {}) as Record<string, unknown>;
      const efKb = Array.isArray(efState.knowledge_by_function)
        ? (efState.knowledge_by_function as Array<Record<string, unknown>>)
        : [];
      const efCov = Array.isArray(efState.coverage_by_function)
        ? (efState.coverage_by_function as Array<Record<string, unknown>>)
        : [];
      const efDist = Array.isArray(efState.production_distribution)
        ? (efState.production_distribution as Array<Record<string, unknown>>)
        : [];
      const topKb = efKb[0] || {};
      const topCov =
        [...efCov].sort(
          (a, b) => Number(b.coverage_pct || 0) - Number(a.coverage_pct || 0)
        )[0] || {};
      const topDist = efDist[0] || {};
      return {
        mode: String(modeObj.mode || "CONTINUOUS"),
        knowledge_gap_dataset: String(
          gap.highest_gap_dataset || topEval.dataset || "—"
        ),
        knowledge_gap_score: Number(
          gap.highest_gap_score || topEval.knowledge_gap_score || 0
        ),
        estimated_universe: Number(univ.estimated_universe || 0),
        growth_velocity: Number(
          growth.growth_velocity || cap.growth_velocity_rows_per_day || 0
        ),
        coverage_velocity: Number(
          growth.coverage_velocity || cap.rows_per_day || 0
        ),
        rows_today: Number(cap.rows_today_approx || kpis.rows_added_today || 0),
        rows_week: Number(cap.rows_this_week || kpis.rows_added_week || 0),
        rows_month: Number(cap.rows_this_month || kpis.rows_added_month || 0),
        knowledge_produced: Number(growth.knowledge_produced_total || 0),
        top_dataset: String(
          manufacturingState.top_dataset || topEval.dataset || "—"
        ),
        top_source: String(throughputStats.top_source || topSrc || "—"),
        top_connector: topConn,
        top_mission: String(
          throughputStats.top_mission || sel.title || sel.instruction || "—"
        ).slice(0, 80),
        factory_capacity_rph: Number(cap.rows_per_hour || rowsH || 0),
        production_cost: Number(eco.estimated_production_cost_usd || 0),
        knowledge_roi: Number(eco.knowledge_roi || 0),
        rows_per_hour: rowsH,
        docs_per_hour: docsH,
        rows_per_session: rowsSess,
        avg_connector_latency_ms: Number(wrk.avg_connector_latency_ms || 0),
        worker_utilization: Number(wrk.utilization_est || 0),
        queue_depth:
          Number(dq.depth || 0) + Number(cq.depth || 0) + Number(pq.depth || 0),
        pipeline_throughput: rowsH > 0 ? rowsH : docsH,
        knowledge_growth_velocity: Number(
          growth.growth_velocity || sess.rows_per_session || 0
        ),
        production_efficiency:
          docs > 0 ? Math.round((rows / docs) * 1000) / 1000 : 0,
        process_ratio_pct: Number(tr.process_ratio_pct || 0),
        auto_publish_ratio:
          Math.round((autoN / autoDenom) * 1000) / 1000,
        manual_review_ratio:
          Math.round((manN / autoDenom) * 1000) / 1000,
        enterprise_function_count: Number(efState.function_count || 0),
        knowledge_by_top_function: String(
          topKb.name
            ? `${topKb.name} (${topKb.rows || 0})`
            : "—"
        ),
        coverage_top_function: String(
          topCov.name
            ? `${topCov.name} (${topCov.coverage_pct ?? 0}%)`
            : "—"
        ),
        top_growing_function: String(
          efTopGrow.name
            ? `${efTopGrow.name} (${efTopGrow.rows || 0})`
            : topKb.name || "—"
        ),
        weakest_function: String(
          efWeak.name
            ? `${efWeak.name} (${efWeak.coverage_pct ?? efWeak.rows ?? 0})`
            : "—"
        ),
        production_distribution_top: String(
          topDist.name
            ? `${topDist.name} ${topDist.share_pct ?? 0}%`
            : "—"
        ),
      };
    })(),
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
