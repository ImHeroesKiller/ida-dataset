"""Lightweight normalization of industry / country / aliases before extraction."""

from __future__ import annotations

import re
from typing import Any

# Canonical industry aliases → preferred name
INDUSTRY_ALIASES: dict[str, str] = {
    "manufaktur": "Manufacturing",
    "manufacturing": "Manufacturing",
    "manufacturing industry": "Manufacturing",
    "industri pengolahan": "Manufacturing",
    "perbankan": "Banking",
    "banking": "Banking",
    "bank": "Banking",
    "telekomunikasi": "Telecommunications",
    "telecommunications": "Telecommunications",
    "telecom": "Telecommunications",
    "pertanian": "Agriculture",
    "agriculture": "Agriculture",
    "pertambangan": "Mining & Quarrying",
    "mining": "Mining & Quarrying",
    "minyak dan gas": "Oil & Gas",
    "oil and gas": "Oil & Gas",
    "oil & gas": "Oil & Gas",
    "kelistrikan": "Electricity & Utilities",
    "electricity": "Electricity & Utilities",
    "energi terbarukan": "Renewable Energy",
    "renewable energy": "Renewable Energy",
    "konstruksi": "Construction",
    "construction": "Construction",
    "logistik": "Transportation & Logistics",
    "logistics": "Transportation & Logistics",
    "transportation": "Transportation & Logistics",
    "perdagangan eceran": "Retail Trade",
    "retail": "Retail Trade",
    "e-commerce": "E-commerce",
    "ecommerce": "E-commerce",
    "asuransi": "Insurance",
    "insurance": "Insurance",
    "fintech": "Fintech & Digital Finance",
    "farmasi": "Pharmaceuticals",
    "pharmaceuticals": "Pharmaceuticals",
    "pariwisata": "Tourism & Travel Services",
    "tourism": "Tourism & Travel Services",
    "pendidikan": "Education Services",
    "education": "Education Services",
    "kesehatan": "Healthcare Services",
    "healthcare": "Healthcare Services",
    "health care": "Healthcare Services",
    "real estate": "Real Estate",
    "properti": "Real Estate",
    "it services": "Information Technology Services",
    "information technology": "Information Technology Services",
    "software": "Software & SaaS",
    "saas": "Software & SaaS",
    "outsourcing": "Business Process Outsourcing",
    "bpo": "Business Process Outsourcing",
    "business process outsourcing": "Business Process Outsourcing",
    "public procurement": "Public Procurement Ecosystem",
    "pengadaan": "Public Procurement Ecosystem",
    "palm oil": "Palm Oil & Plantations",
    "kelapa sawit": "Palm Oil & Plantations",
    "textile": "Textiles & Apparel",
    "textiles": "Textiles & Apparel",
    "apparel": "Textiles & Apparel",
    "automotive": "Automotive",
    "otomotif": "Automotive",
    "chemicals": "Chemicals",
    "kimia": "Chemicals",
    "steel": "Steel & Metals",
    "baja": "Steel & Metals",
    "cement": "Cement & Building Materials",
    "semen": "Cement & Building Materials",
    "fisheries": "Fisheries & Aquaculture",
    "perikanan": "Fisheries & Aquaculture",
    "hospitality": "Hospitality & Hotels",
    "hotels": "Hospitality & Hotels",
    "aviation": "Aviation",
    "penerbangan": "Aviation",
    "maritime": "Maritime & Shipping",
    "shipping": "Maritime & Shipping",
    "ports": "Ports & Terminals",
    "pelabuhan": "Ports & Terminals",
    "data center": "Data Centers & Cloud Infrastructure",
    "data centres": "Data Centers & Cloud Infrastructure",
    "cloud": "Data Centers & Cloud Infrastructure",
    "payments": "Payments & Payment Systems",
    "payment systems": "Payments & Payment Systems",
    "microfinance": "Microfinance",
    "keuangan mikro": "Microfinance",
    "capital markets": "Capital Markets & Securities",
    "securities": "Capital Markets & Securities",
    "waste management": "Waste Management & Environmental Services",
    "pengelolaan limbah": "Waste Management & Environmental Services",
    "water": "Water & Sanitation Utilities",
    "sanitation": "Water & Sanitation Utilities",
    "security services": "Security Services",
    "keamanan": "Security Services",
    "facilities management": "Facilities Management",
    "professional services": "Professional Services",
    "media": "Media & Entertainment",
    "entertainment": "Media & Entertainment",
    "food and beverage": "Food & Beverage Processing",
    "food & beverage": "Food & Beverage Processing",
    "fnb": "Food & Beverage Processing",
    "electronics": "Electronics Manufacturing",
    "elektronik": "Electronics Manufacturing",
    "warehousing": "Warehousing & Distribution",
    "wholesale": "Wholesale Trade",
    "leasing": "Multifinance & Leasing",
    "multifinance": "Multifinance & Leasing",
    "agri-services": "Agriculture Input & Agri-Services",
    "agri services": "Agriculture Input & Agri-Services",
}

# Candidate industries not yet in catalog may still be proposed if evidence is strong
EXPANDABLE_INDUSTRIES: list[dict[str, str]] = [
    {
        "name": "Business Process Outsourcing",
        "category": "Professional Services",
        "aliases": "outsourcing, BPO, shared services, business process outsourcing, offshoring",
    },
    {
        "name": "Shared Services Centers",
        "category": "Professional Services",
        "aliases": "shared services, SSC, GBS, global business services",
    },
    {
        "name": "Industrial Estates & SEZ",
        "category": "Infrastructure",
        "aliases": "industrial estate, special economic zone, SEZ, kawasan industri, KEK",
    },
    {
        "name": "Halal Industry",
        "category": "Industrial",
        "aliases": "halal industry, industri halal, halal certification, BPJPH",
    },
    {
        "name": "Creative Economy",
        "category": "Services",
        "aliases": "creative economy, ekonomi kreatif, creative industry",
    },
    {
        "name": "Digital Economy",
        "category": "Digital",
        "aliases": "digital economy, ekonomi digital, digitalization, digital transformation",
    },
    {
        "name": "Startup Ecosystem",
        "category": "Digital",
        "aliases": "startup, start-up, unicorn, venture capital ecosystem",
    },
    {
        "name": "MSMEs / UMKM",
        "category": "Trade / Services",
        "aliases": "MSME, UMKM, micro small medium enterprises, usaha mikro",
    },
    {
        "name": "Labor & Employment Services",
        "category": "Services",
        "aliases": "labor market, employment services, ketenagakerjaan, manpower",
    },
    {
        "name": "Export Processing",
        "category": "Trade",
        "aliases": "export processing, EPZ, export-oriented manufacturing, bonded zone",
    },
    {
        "name": "Nickel Downstream Industry",
        "category": "Industrial / Extractive",
        "aliases": "nickel downstream, smelter, hilirisasi nikel, EV battery materials",
    },
    {
        "name": "Electric Vehicle Ecosystem",
        "category": "Automotive / Energy",
        "aliases": "electric vehicle, EV, kendaraan listrik, battery electric",
    },
    {
        "name": "Green Industry",
        "category": "Industrial",
        "aliases": "green industry, industri hijau, decarbonization industry",
    },
    {
        "name": "Cybersecurity Industry",
        "category": "Technology",
        "aliases": "cybersecurity, cyber security, keamanan siber",
    },
    {
        "name": "Artificial Intelligence Services",
        "category": "Technology",
        "aliases": "artificial intelligence, AI services, machine learning industry",
    },
]


def normalize_text(text: str) -> str:
    t = text or ""
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def normalize_country(text: str) -> str:
    low = (text or "").lower()
    if any(x in low for x in ("indonesia", "indonesian", "jakarta", "nusantara")):
        return "Indonesia"
    return ""


def match_industry_mentions(text: str) -> list[dict[str, Any]]:
    """Return industry mentions grounded in text (alias match only)."""
    body = normalize_text(text)
    low = body.lower()
    found: dict[str, dict[str, Any]] = {}

    # Expandable industries (preferred for new rows)
    for ind in EXPANDABLE_INDUSTRIES:
        aliases = [a.strip() for a in ind["aliases"].split(",") if a.strip()]
        aliases.append(ind["name"])
        for alias in aliases:
            a = alias.lower()
            if len(a) < 3:
                continue
            if a in low:
                found[ind["name"]] = {
                    "name": ind["name"],
                    "category": ind["category"],
                    "matched_alias": alias,
                    "expandable": True,
                }
                break

    # Known alias map (may already exist in dataset)
    for alias, canonical in INDUSTRY_ALIASES.items():
        if alias in low and canonical not in found:
            found[canonical] = {
                "name": canonical,
                "category": "",
                "matched_alias": alias,
                "expandable": False,
            }

    return list(found.values())


def evidence_snippets(text: str, term: str, *, window: int = 180, max_snips: int = 3) -> list[str]:
    """Extract literal evidence windows around term occurrences."""
    body = normalize_text(text)
    low = body.lower()
    term_l = term.lower()
    snips: list[str] = []
    start = 0
    while len(snips) < max_snips:
        idx = low.find(term_l, start)
        if idx < 0:
            break
        a = max(0, idx - window)
        b = min(len(body), idx + len(term) + window)
        snip = body[a:b].strip()
        if snip and snip not in snips:
            snips.append(snip)
        start = idx + len(term)
    return snips
