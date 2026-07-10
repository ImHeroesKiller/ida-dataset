import type { LucideIcon } from "lucide-react";
import {
  Database,
  Download,
  Factory,
  LayoutDashboard,
  ListChecks,
  Radio,
  ScrollText,
  Settings,
  Target,
} from "lucide-react";

export type NavItem = {
  href: string;
  label: string;
  icon: LucideIcon;
};

/** IDA Dataset Factory navigation — product surfaces only. */
export const NAV_ITEMS: NavItem[] = [
  { href: "/", label: "Dashboard", icon: LayoutDashboard },
  { href: "/datasets", label: "Datasets", icon: Database },
  { href: "/missions", label: "Missions", icon: Target },
  { href: "/sources", label: "Sources", icon: Radio },
  { href: "/quality", label: "Quality", icon: ListChecks },
  { href: "/exports", label: "Exports", icon: Download },
  { href: "/logs", label: "Logs", icon: ScrollText },
  { href: "/settings", label: "Settings", icon: Settings },
];

/** Official factory pipeline stages (documentation / status only). */
export const FACTORY_PIPELINE = [
  "Mission",
  "Source Discovery",
  "Document Collection",
  "Extraction",
  "Normalization",
  "Validation",
  "Schema Mapping",
  "Append Dataset",
  "Quality Validation",
  "Export",
  "Dashboard Update",
] as const;

export const PRODUCT = {
  name: "IDA Dataset Factory",
  short: "Dataset Factory",
  tagline: "Automatic Knowledge Factory",
  icon: Factory,
} as const;
