"use client";

/**
 * Single source of truth for learning session monitoring.
 * RootLayout mounts one provider; Shell chrome + all pages share the same poll.
 */

import { createContext, useContext, type ReactNode } from "react";
import {
  useLearningMonitor,
  type UseLearningMonitorResult,
} from "@/hooks/use-learning-monitor";

export type {
  SessionEvent,
  SessionSummary,
  LearningDashboardState,
  StartLearningResult,
  PeriodStats,
} from "@/hooks/use-learning-monitor";

const LearningCtx = createContext<UseLearningMonitorResult | null>(null);

export function LearningProvider({
  children,
  pollMs = 5000,
}: {
  children: ReactNode;
  pollMs?: number;
}) {
  const value = useLearningMonitor(pollMs);
  return (
    <LearningCtx.Provider value={value}>{children}</LearningCtx.Provider>
  );
}

/** Shared instance from RootLayout LearningProvider. */
export function useLearning(): UseLearningMonitorResult {
  const ctx = useContext(LearningCtx);
  if (!ctx) {
    throw new Error(
      "useLearning must be used within LearningProvider (RootLayout)"
    );
  }
  return ctx;
}

/** @deprecated use useLearning */
export const useLearningSessions = useLearning;
