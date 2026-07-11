/**
 * IDA Dataset Factory — Operator UI v1.0 (FROZEN)
 * Compact console typography. Single source of truth.
 * CSS variables in styles/globals.css mirror these values.
 */

export const colors = {
  light: {
    bg: "#F8FAFC",
    surface: "#FFFFFF",
    surfaceSecondary: "#F1F5F9",
    border: "#E2E8F0",
    text: "#0F172A",
    textSecondary: "#334155",
    textMuted: "#64748B",
    textDisabled: "#94A3B8",
    blue: "#2563EB",
    green: "#16A34A",
    orange: "#F59E0B",
    red: "#DC2626",
    purple: "#7C3AED",
  },
  dark: {
    bg: "#020617",
    surface: "#0F172A",
    surfaceSecondary: "#111827",
    border: "#1E293B",
    text: "#F8FAFC",
    textSecondary: "#CBD5E1",
    textMuted: "#94A3B8",
    textDisabled: "#64748B",
    blue: "#3B82F6",
    green: "#22C55E",
    orange: "#F59E0B",
    red: "#EF4444",
    purple: "#A78BFA",
  },
} as const;

/** Operator console scale — compact by default; KPIs may use medium. */
export const typography = {
  pageTitle: { size: "18px", weight: 600, lineHeight: 1.3 },
  sectionTitle: { size: "13px", weight: 600, lineHeight: 1.35 },
  cardTitle: { size: "12px", weight: 600, lineHeight: 1.35 },
  body: { size: "13px", weight: 400, lineHeight: 1.45 },
  small: { size: "12px", weight: 400, lineHeight: 1.4 },
  caption: { size: "11px", weight: 500, lineHeight: 1.35 },
  kpi: { size: "18px", weight: 600, lineHeight: 1.2 },
} as const;

/** 4px denser grid for operator console */
export const spacing = {
  1: 4,
  2: 8,
  3: 12,
  4: 16,
  5: 20,
  6: 24,
} as const;

export const radii = {
  md: "6px",
  lg: "8px",
  xl: "10px",
  full: "9999px",
} as const;

/** Operator status language (never expose internal engine terms). */
export const operatorStatus = [
  "Learning",
  "Running",
  "Paused",
  "Waiting",
  "Exporting",
  "Publishing",
  "Healthy",
  "Warning",
  "Error",
  "Completed",
  "Idle",
  "Synced",
] as const;

/** Badge semantic roles for production UI */
export const badgeRoles = [
  "healthy",
  "warning",
  "error",
  "idle",
  "running",
  "publishing",
  "completed",
] as const;

export type BadgeRole = (typeof badgeRoles)[number];
