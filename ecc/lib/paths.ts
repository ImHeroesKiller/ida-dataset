import fs from "fs";
import path from "path";

/**
 * Resolve the IDA dataset repository root.
 *
 * Local:  <repo>/ecc  → parent is repo root
 * Vercel: process.cwd() is usually the ecc project dir (Root Directory = ecc)
 *         and the monorepo checkout still contains sibling folders.
 */
export function getRepoRoot(): string {
  const fromEnv = process.env.IDA_REPO_ROOT;
  if (fromEnv && fs.existsSync(path.join(fromEnv, "VERSION"))) {
    return path.resolve(fromEnv);
  }

  const candidates = [
    process.env.VERCEL ? path.resolve(process.cwd(), "..") : null,
    path.resolve(process.cwd(), ".."),
    path.resolve(process.cwd()),
    path.resolve(__dirname, "../.."),
    path.resolve(__dirname, "../../.."),
    // Vercel serverless bundle layouts
    path.resolve("/var/task", ".."),
    path.resolve("/var/task"),
  ].filter(Boolean) as string[];

  for (const candidate of candidates) {
    try {
      if (
        fs.existsSync(path.join(candidate, "VERSION")) &&
        fs.existsSync(path.join(candidate, "domains"))
      ) {
        return candidate;
      }
    } catch {
      // ignore unreadable paths
    }
  }

  // Last resort: parent of cwd (local `npm run dev` from ecc/)
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
