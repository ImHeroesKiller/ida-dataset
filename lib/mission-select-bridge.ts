/**
 * TS bridge to dynamic mission selector for dashboard/executive views.
 * Pure observe — no side effects.
 */

import { select_next_mission as selectNextMissionPy } from "./mission-selector-shim";

// Re-export using the Python-named export from shim
export function selectNextMission() {
  return selectNextMissionPy();
}
