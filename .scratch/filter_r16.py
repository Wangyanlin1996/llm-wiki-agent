"""Filter and display candidates for Round 16."""
import json

with open(".scratch/arxiv_search_r16.json", encoding="utf-8") as f:
    data = json.load(f)

# Cross-round duplicates to exclude (arXiv IDs already in wiki from other rounds)
cross_dup = {
    "2605.29168",  # Better Later Than Sooner = neuro-symbolic-kg-ontology (R10)
    "2605.01189",  # NEURON = neuron-clinical-explainability (R13)
    "2604.27713",  # KG Policy Compliance = kg-policy-compliance (R10)
    "2604.20795",  # Auto Ontology Construction = auto-ontology-construction-llm (R13)
    "2604.14362",  # APEX-MEM = apex-mem (R4)
    "2604.10853",  # KG Gap Overlap = kg-gap-overlap-benchmark (R10)
}

filtered = [r for r in data if r["arxiv_id_nover"] not in cross_dup]
print(f"After cross-round dedup: {len(filtered)}")
print()

for i, r in enumerate(filtered, 1):
    aid = r["arxiv_id_nover"]
    pub = r["published"]
    title = r["title"][:100]
    ab = r["summary"][:280]
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
