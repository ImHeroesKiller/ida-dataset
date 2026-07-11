import type { LucideIcon } from "lucide-react";
import {
  Download,
  Factory,
  LayoutDashboard,
  Radio,
  Settings,
  Target,
} from "lucide-react";

export type NavItem = {
  href: string;
  label: string;
  icon: LucideIcon;
};

/**
 * Operator dashboard navigation (simplification sprint).
 * Only surfaces that directly support production operations.
 * Datasets → Export; Quality/Logs → Dashboard console.
 */
export const NAV_ITEMS: NavItem[] = [
  { href: "/", label: "Dashboard", icon: LayoutDashboard },
  { href: "/missions", label: "Mission", icon: Target },
  { href: "/sources", label: "Sources", icon: Radio },
  { href: "/exports", label: "Export", icon: Download },
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
