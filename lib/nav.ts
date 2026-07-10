import type { LucideIcon } from "lucide-react";
import {
  BookOpen,
  ClipboardCheck,
  FileBarChart2,
  LayoutDashboard,
  Settings,
  Target,
} from "lucide-react";

export type NavItem = {
  href: string;
  label: string;
  icon: LucideIcon;
  emoji?: string;
};

/** Executive navigation only — implementation modules stay internal. */
export const NAV_ITEMS: NavItem[] = [
  { href: "/", label: "Dashboard", icon: LayoutDashboard, emoji: "🏠" },
  { href: "/knowledge", label: "Knowledge", icon: BookOpen, emoji: "📚" },
  { href: "/missions", label: "Missions", icon: Target, emoji: "🎯" },
  { href: "/review", label: "Review", icon: ClipboardCheck, emoji: "✅" },
  { href: "/reports", label: "Reports", icon: FileBarChart2, emoji: "📈" },
  { href: "/settings", label: "Settings", icon: Settings, emoji: "⚙" },
];

/** Internal architecture flow (not shown in executive nav). */
export const FLOW_HINT = [
  "Scheduler",
  "Planner",
  "Policy",
  "Connectors",
  "Document Queue",
  "Pipeline",
  "Review",
  "Publisher",
] as const;
