import type { NextConfig } from "next";
import path from "path";
import { fileURLToPath } from "url";

const configDir = path.dirname(fileURLToPath(import.meta.url));

const nextConfig: NextConfig = {
  // Allow file tracing to include the knowledge repository root
  outputFileTracingRoot: path.join(configDir, ".."),
};

export default nextConfig;
