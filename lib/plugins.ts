/**
 * ECC Plugin architecture — future modules register without redesign.
 *
 * Flow remains fixed:
 * Dashboard → Planner → Policy → Pipeline → Review → Publisher
 */

export type PluginSlot =
  | "sidebar"
  | "dashboard-card"
  | "inspector"
  | "console"
  | "settings"
  | "future";

export type PluginStatus = "available" | "planned" | "disabled";

export type EccPlugin = {
  id: string;
  name: string;
  description: string;
  status: PluginStatus;
  slots: PluginSlot[];
  href?: string;
  /** Architecture note — plugins must not bypass Planner/Policy/Review */
  respectsControlFlow: true;
};

export const CORE_PLUGINS: EccPlugin[] = [
  {
    id: "scheduler",
    name: "Continuous Learning Scheduler",
    description: "Single orchestration entry for continuous + directed learning",
    status: "available",
    slots: ["sidebar", "dashboard-card"],
    href: "/learning",
    respectsControlFlow: true,
  },
  {
    id: "missions",
    name: "Learning Missions",
    description: "Directed learning missions and contracts",
    status: "available",
    slots: ["sidebar", "dashboard-card"],
    href: "/missions",
    respectsControlFlow: true,
  },
  {
    id: "planner",
    name: "Knowledge Planner",
    description: "Proposes acquisition plans and gap priorities (via Scheduler only)",
    status: "available",
    slots: ["sidebar", "dashboard-card"],
    href: "/planner",
    respectsControlFlow: true,
  },
  {
    id: "policies",
    name: "Policy Engine",
    description: "Human controller gates for crawl/extract/publish",
    status: "available",
    slots: ["sidebar", "dashboard-card"],
    href: "/policies",
    respectsControlFlow: true,
  },
  {
    id: "ontology",
    name: "Ontology Viewer",
    description: "CSV-backed entity and relationship browser",
    status: "available",
    slots: ["sidebar"],
    href: "/ontology",
    respectsControlFlow: true,
  },
  {
    id: "datasets",
    name: "Datasets",
    description: "Read-only CSV browser for domain knowledge",
    status: "available",
    slots: ["sidebar"],
    href: "/datasets",
    respectsControlFlow: true,
  },
  {
    id: "review",
    name: "Review Queue",
    description: "Human approval surface before publish",
    status: "available",
    slots: ["sidebar", "dashboard-card"],
    href: "/review",
    respectsControlFlow: true,
  },
  {
    id: "publisher",
    name: "Publisher",
    description: "Append-only publish after review (never bypasses queue)",
    status: "available",
    slots: ["sidebar"],
    href: "/publisher",
    respectsControlFlow: true,
  },
  {
    id: "reports",
    name: "Reports",
    description: "Validation, planner, review, publish artifacts",
    status: "available",
    slots: ["sidebar"],
    href: "/reports",
    respectsControlFlow: true,
  },
];

/** Future modules — registered as planned plugins only. */
export const FUTURE_PLUGINS: EccPlugin[] = [
  {
    id: "connectors",
    name: "Knowledge Connectors",
    description: "External trusted source connectors",
    status: "planned",
    slots: ["future", "sidebar"],
    respectsControlFlow: true,
  },
  {
    id: "crawler",
    name: "Crawler",
    description: "Controlled collection backend (disabled by default)",
    status: "planned",
    slots: ["future"],
    respectsControlFlow: true,
  },
  {
    id: "browser",
    name: "Browser Automation",
    description: "Human-gated browser collection",
    status: "planned",
    slots: ["future"],
    respectsControlFlow: true,
  },
  {
    id: "llm-extract",
    name: "LLM Extraction",
    description: "Extraction backend with provenance + confidence",
    status: "planned",
    slots: ["future"],
    respectsControlFlow: true,
  },
  {
    id: "knowledge-graph",
    name: "Knowledge Graph",
    description: "Graph projection of ontology + instances",
    status: "planned",
    slots: ["future"],
    respectsControlFlow: true,
  },
  {
    id: "rag",
    name: "RAG",
    description: "Retrieval-augmented generation over approved knowledge",
    status: "planned",
    slots: ["future"],
    respectsControlFlow: true,
  },
  {
    id: "fine-tuning",
    name: "Fine Tuning",
    description: "Dataset export for model fine-tuning",
    status: "planned",
    slots: ["future"],
    respectsControlFlow: true,
  },
  {
    id: "executive-agent",
    name: "Executive Agent",
    description: "Human-supervised executive reasoning agent",
    status: "planned",
    slots: ["future"],
    respectsControlFlow: true,
  },
];

export function listPlugins(): EccPlugin[] {
  return [...CORE_PLUGINS, ...FUTURE_PLUGINS];
}

export function listSidebarPlugins(): EccPlugin[] {
  return listPlugins().filter((p) => p.slots.includes("sidebar"));
}
