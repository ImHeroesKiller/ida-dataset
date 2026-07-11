/**
 * IDA Dataset Factory — centralized design tokens.
 * Single source of truth for colors, type, spacing, radii.
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

export const typography = {
  pageTitle: { size: "36px", weight: 700, lineHeight: 1.2 },
  sectionTitle: { size: "24px", weight: 700, lineHeight: 1.25 },
  cardTitle: { size: "18px", weight: 600, lineHeight: 1.35 },
  body: { size: "16px", weight: 400, lineHeight: 1.5 },
  small: { size: "14px", weight: 400, lineHeight: 1.5 },
  caption: { size: "12px", weight: 500, lineHeight: 1.4 },
} as const;

/** 8px grid */
export const spacing = {
  1: 8,
  2: 16,
  3: 24,
  4: 32,
  5: 40,
  6: 48,
} as const;

export const radii = {
  md: "8px",
  lg: "12px",
  xl: "16px",
  full: "9999px",
} as const;

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
