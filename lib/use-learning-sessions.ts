/**
 * Compatibility re-export — single source of truth lives in hooks/.
 * @deprecated Import from @/hooks/learning-provider
 */
export {
  useLearning,
  useLearningSessions,
  LearningProvider,
} from "@/hooks/learning-provider";
export type {
  SessionEvent,
  SessionSummary,
  LearningDashboardState,
  StartLearningResult,
  PeriodStats,
} from "@/hooks/use-learning-monitor";
