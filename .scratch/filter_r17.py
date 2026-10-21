"""Filter Round 17 candidates — exclude already-ingested papers, show abstracts for relevance screening."""
import json

with open(".scratch/arxiv_search_r17.json", encoding="utf-8") as f:
    data = json.load(f)

# Already in wiki (arXiv IDs from all rounds)
ALREADY_IN_WIKI = {
    # Round 16
    "2505.00039", "2506.07037", "2606.28076", "2510.01409", "2508.09893",
    "2504.02889", "2608.22974", "2608.13662", "2607.27249", "2606.15931",
    "2604.02545", "2607.27130", "2607.17963", "2606.09724", "2606.22728",
    "2605.29250", "2507.22619", "2502.03992",
    # Round 15
    "2412.15235", "2604.00500", "2604.09550", "2606.11910", "2607.11464",
    "2502.18992", "2504.00389", "2604.18478", "2607.04391", "2608.08618",
    "2607.18029", "2608.07700", "2508.11784", "2507.14032", "2607.28662",
    "2607.01773", "2604.23090",
    # Round 14
    "2603.25152", "2511.13201",
    # Round 13
    "2604.20795", "2604.23563", "2506.05887", "2106.05568", "2512.21699",
    "2403.09567", "2510.03442", "2205.15462", "2506.04133", "2302.10809",
    "2604.20043", "2505.17801", "2204.12568",
    # Round 12
    "2406.02818", "2509.21848", "2601.11913", "2510.04568", "2603.09835",
    "2603.08329", "2511.22850", "2604.03664", "2507.02259", "2601.20352",
    "2601.21545", "2606.24535", "2607.07666", "2607.10987", "2602.03695",
    "2607.19595", "2602.22603", "2606.14790", "2607.02807", "2607.08662",
    "2510.24428", "2410.08143", "2603.21190", "2605.14563", "2605.00444",
    "2604.12890", "2606.00655", "2601.21064", "2606.10507", "2605.24775",
    "2607.21503",
    # Round 10
    "2606.28076",  # already above
    "2605.29168", "2604.27713", "2604.10853", "2604.14362",
    # Round 9
    "2603.25152",  # already above
    # Others
    "2608.18613",  # CTIFoundry - was candidate but not ingested in R16
    "2608.04011",  # legal grammar - was candidate but not ingested
    "2606.28011",  # fault-tolerant control - was candidate but not ingested
    "2406.06469",  # husky - already in wiki from Round 10
    "2602.15898",  # multicube-rag - already in wiki from Round 10
}

filtered = [r for r in data if r["arxiv_id_nover"] not in ALREADY_IN_WIKI]
print(f"After excluding already-in-wiki: {len(filtered)}")
print()

for i, r in enumerate(filtered, 1):
    aid = r["arxiv_id_nover"]
    pub = r["published"]
    title = r["title"][:110]
    ab = r["summary"][:300]
    auth = r["authors"][0] if r["authors"] else "?"
    if len(r["authors"]) > 1:
        auth += " et al."
    venue = r["journal_ref"] or r["comment"] or ""
    if venue:
        venue = venue[:50]
    print(f"{i:2}. [{pub}] {aid} | {auth} | {venue}")
    print(f"    T: {title}")
    print(f"    A: {ab}")
    print()
