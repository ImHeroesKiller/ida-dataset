import type { LucideIcon } from "lucide-react";
import {
  Activity,
  BookOpen,
  Boxes,
  ClipboardCheck,
  FileBarChart2,
  GitBranch,
  LayoutDashboard,
  ListChecks,
  Network,
  Settings,
  Shield,
  UploadCloud,
} from "lucide-react";

export type NavItem = {
  href: string;
  label: string;
  icon: LucideIcon;
  section?: string;
};

export const NAV_ITEMS: NavItem[] = [
  { href: "/", label: "Dashboard", icon: LayoutDashboard },
  { href: "/planner", label: "Knowledge Planner", icon: ListChecks },
  { href: "/policies", label: "Knowledge Policies", icon: Shield },
  { href: "/ontology", label: "Ontology", icon: Network },
  { href: "/datasets", label: "Datasets", icon: Boxes },
  { href: "/review", label: "Review Queue", icon: ClipboardCheck },
  { href: "/publisher", label: "Publisher", icon: UploadCloud },
  { href: "/reports", label: "Reports", icon: FileBarChart2 },
  { href: "/settings", label: "Settings", icon: Settings },
  { href: "/system", label: "System", icon: Activity },
];

export const FLOW_HINT = [
  "Planner",
  "Policy",
  "Pipeline",
  "Review",
  "Publisher",
] as const;

export { BookOpen, GitBranch };
