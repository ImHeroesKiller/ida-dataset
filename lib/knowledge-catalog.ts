/**
 * Executive Knowledge catalog — curated domain libraries.
 */

import { listDatasets, readDataset, type DatasetInfo } from "@/lib/repo-data";

export type KnowledgeCategory = {
  id: string;
  label: string;
  description: string;
  datasetNames: string[];
};

export const KNOWLEDGE_CATEGORIES: KnowledgeCategory[] = [
  {
    id: "industry",
    label: "Industry",
    description: "Industry profiles and market context",
    datasetNames: ["industry_library"],
  },
  {
    id: "pain_points",
    label: "Pain Points",
    description: "Customer and operational pain points",
    datasetNames: ["pain_point_library"],
  },
  {
    id: "solutions",
    label: "Solutions",
    description: "Solution offerings and approaches",
    datasetNames: ["solution_library"],
  },
  {
    id: "case_studies",
    label: "Case Studies",
    description: "Reference implementations and wins",
    datasetNames: ["case_study_library"],
  },
  {
    id: "frameworks",
    label: "Frameworks",
    description: "Methodologies and thinking frameworks",
    datasetNames: ["framework_library"],
  },
  {
    id: "competitors",
    label: "Competitors",
    description: "Competitive landscape",
    datasetNames: ["competitor_library"],
  },
  {
    id: "regulations",
    label: "Regulations",
    description: "Regulatory and compliance signals",
    datasetNames: ["guidance", "business_signal_library"],
  },
];

export function getKnowledgeOverview() {
  const datasets = listDatasets();
  const byName = new Map(datasets.map((d) => [d.name, d]));

  return KNOWLEDGE_CATEGORIES.map((cat) => {
    const matched: DatasetInfo[] = cat.datasetNames
      .map((n) => byName.get(n))
      .filter(Boolean) as DatasetInfo[];
    const rows = matched.reduce((s, d) => s + d.rowCount, 0);
    const populated = matched.some((d) => !d.isPlaceholder);
    return {
      ...cat,
      rows,
      populated,
      datasets: matched.map((d) => ({
        name: d.name,
        path: d.relativePath,
        rows: d.rowCount,
        domain: d.domain,
      })),
    };
  });
}

export function getCategoryDetail(categoryId: string, limit = 40) {
  const cat = KNOWLEDGE_CATEGORIES.find((c) => c.id === categoryId);
  if (!cat) return null;
  const datasets = listDatasets();
  const tables = cat.datasetNames
    .map((name) => {
      const info = datasets.find((d) => d.name === name);
      if (!info) return null;
      const table = readDataset(info.relativePath, limit);
      return {
        name: info.name,
        path: info.relativePath,
        headers: table.headers,
        rows: table.previewRows,
        rowCount: table.rowCount,
      };
    })
    .filter(Boolean);
  return { category: cat, tables };
}
