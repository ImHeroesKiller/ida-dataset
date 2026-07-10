import type { NextConfig } from "next";
import path from "path";
import { fileURLToPath } from "url";

const configDir = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.join(configDir, "..");

/**
 * Knowledge data lives one level above the Next.js app (ida-dataset monorepo).
 * Vercel Root Directory should be `ecc`, with file tracing including parent assets.
 */
const knowledgeGlobs = [
  "../VERSION",
  "../domains/**/*",
  "../relationships/**/*",
  "../metadata/**/*",
  "../automation/config/**/*",
  "../automation/queue/**/*",
  "../automation/review/**/*",
  "../automation/ci/**/*",
  "../automation/README.md",
  "../reports/**/*",
  "../config/**/*",
  "../docs/**/*",
];

const nextConfig: NextConfig = {
  outputFileTracingRoot: repoRoot,
  outputFileTracingIncludes: {
    "/*": knowledgeGlobs,
    "/**": knowledgeGlobs,
    "/api/*": knowledgeGlobs,
    "/api/**/*": knowledgeGlobs,
  },
  // Avoid failing the build when optional server binaries are missing on Vercel
  serverExternalPackages: [],
};

export default nextConfig;
