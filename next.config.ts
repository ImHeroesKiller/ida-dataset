import type { NextConfig } from "next";
import path from "path";
import { fileURLToPath } from "url";

const configDir = path.dirname(fileURLToPath(import.meta.url));

/**
 * ECC lives at the repository root so Vercel auto-detects Next.js.
 * Knowledge assets (domains/, metadata/, automation/, …) are siblings.
 *
 * distDir is `ecc/.next` to match the Vercel project Output Directory
 * leftover from the earlier monorepo layout. Preferred long-term:
 * clear Output Directory in Vercel project settings and set distDir to `.next`.
 */
const knowledgeGlobs = [
  "./VERSION",
  "./domains/**/*",
  "./relationships/**/*",
  "./metadata/**/*",
  "./automation/config/**/*",
  "./automation/queue/**/*",
  "./automation/review/**/*",
  "./automation/ci/**/*",
  "./automation/README.md",
  "./reports/**/*",
  "./config/**/*",
  "./docs/**/*",
];

const nextConfig: NextConfig = {
  // Keep in sync with Vercel → Project Settings → Output Directory
  distDir: "ecc/.next",
  outputFileTracingRoot: configDir,
  outputFileTracingIncludes: {
    "/*": knowledgeGlobs,
    "/**": knowledgeGlobs,
    "/api/*": knowledgeGlobs,
    "/api/**/*": knowledgeGlobs,
  },
  serverExternalPackages: [],
};

export default nextConfig;
