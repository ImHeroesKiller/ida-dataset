import fs from "fs";
import path from "path";

/**
 * Resolve the IDA dataset repository root.
 * ECC lives in <repo>/ecc, so parent is the knowledge repository.
 */
export function getRepoRoot(): string {
  const fromEnv = process.env.IDA_REPO_ROOT;
  if (fromEnv && fs.existsSync(fromEnv)) {
    return path.resolve(fromEnv);
  }

  // Prefer parent of ecc/ when VERSION + domains exist
  const candidates = [
    path.resolve(process.cwd(), ".."),
    path.resolve(process.cwd()),
    path.resolve(__dirname, "../.."),
    path.resolve(__dirname, "../../.."),
  ];

  for (const candidate of candidates) {
    if (
      fs.existsSync(path.join(candidate, "VERSION")) &&
      fs.existsSync(path.join(candidate, "domains"))
    ) {
      return candidate;
    }
  }

  // Fallback: parent of cwd (dev from ecc/)
  return path.resolve(process.cwd(), "..");
}

export function repoPath(...parts: string[]): string {
  return path.join(getRepoRoot(), ...parts);
}

export const PATHS = {
  version: () => repoPath("VERSION"),
  domains: () => repoPath("domains"),
  relationships: () => repoPath("relationships"),
  metadata: () => repoPath("metadata"),
  ontology: () => repoPath("metadata/ontology"),
  policies: () => repoPath("automation/config/policies.yaml"),
  sources: () => repoPath("automation/config/sources.yaml"),
  environments: () => repoPath("config/environments"),
  reports: () => repoPath("reports"),
  queuePending: () => repoPath("automation/queue/pending"),
  queueApproved: () => repoPath("automation/queue/approved"),
  queueRejected: () => repoPath("automation/queue/rejected"),
  review: () => repoPath("automation/review"),
  automationLogs: () => repoPath("automation/logs"),
  kasReadme: () => repoPath("automation/README.md"),
} as const;
