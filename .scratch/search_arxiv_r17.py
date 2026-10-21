"""arXiv API search for Round 17: ontology skill routing / precise retrieval reasoning / agent loop detection."""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import json
import sys
import os

BASE = "https://export.arxiv.org/api/query"

# Load all existing arXiv IDs from wiki to exclude
ALREADY = set()
# Read index.md and extract arXiv IDs is complex; instead use a broad set from recent rounds
# We'll check against a file if it exists, otherwise just filter later

QUERIES = [
    # Direction 1: Ontology-assisted multi-level skill routing
    ("D1-Q1", "abs:ontology AND abs:skill AND abs:routing AND abs:agent"),
    ("D1-Q2", "abs:ontology AND abs:tool AND abs:selection AND abs:LLM"),
    ("D1-Q3", "abs:ontology AND abs:\"multi-level\" AND abs:routing AND abs:task"),
    # Direction 2: Ontology precise reasoning (retrieval-oriented, not judgment)
    ("D2-Q1", "abs:ontology AND abs:precise AND abs:retrieval AND abs:reasoning"),
    ("D2-Q2", "abs:ontology AND abs:knowledge AND abs:grounding AND abs:retrieval AND abs:LLM"),
    ("D2-Q3", "abs:ontology AND abs:semantic AND abs:retrieval AND abs:\"knowledge graph\" AND abs:reasoning"),
    # Direction 3: Ontology-assisted agent loop detection and resolution
    ("D3-Q1", "abs:ontology AND abs:loop AND abs:detection AND abs:agent"),
    ("D3-Q2", "abs:agent AND abs:cycle AND abs:resolution AND abs:LLM"),
    ("D3-Q3", "abs:agent AND abs:termination AND abs:ontology AND abs:reasoning"),
    ("D3-Q4", "abs:LLM AND abs:agent AND abs:deadlock AND abs:repetition"),
    # Additional complementary queries
    ("D1-Q4", "abs:ontology AND abs:action AND abs:planning AND abs:hierarchy AND abs:agent"),
    ("D2-Q4", "abs:ontology AND abs:retrieval AND abs:augmented AND abs:generation AND abs:precise"),
]


def parse_arxiv_xml(xml_text):
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(xml_text)
    results = []
    for entry in root.findall("a:entry", ns):
        arxiv_id_url = entry.find("a:id", ns).text.strip()
        arxiv_id = arxiv_id_url.split("/abs/")[-1]
        arxiv_id_nover = arxiv_id.split("v")[0]
        title = " ".join(entry.find("a:title", ns).text.split())
        summary = " ".join(entry.find("a:summary", ns).text.split())
        published = entry.find("a:published", ns).text[:10]
        authors = [a.find("a:name", ns).text for a in entry.findall("a:author", ns)]
        categories = [c.get("term") for c in entry.findall("a:category", ns)]
        journal_ref_el = entry.find("arxiv:journal_ref", ns)
        journal_ref = journal_ref_el.text if journal_ref_el is not None else ""
        comment_el = entry.find("arxiv:comment", ns)
        comment = comment_el.text if comment_el is not None else ""
        results.append({
            "arxiv_id": arxiv_id,
            "arxiv_id_nover": arxiv_id_nover,
            "title": title,
            "summary": summary,
            "published": published,
            "authors": authors,
            "categories": categories,
            "journal_ref": journal_ref,
            "comment": comment,
        })
    return results


def search(query, start=0, max_results=20):
    params = urllib.parse.urlencode({
        "search_query": query,
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"{BASE}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        xml_text = resp.read().decode("utf-8")
    return parse_arxiv_xml(xml_text)


def main():
    seen_ids = set()
    all_results = []
    for label, q in QUERIES:
        print(f"\n=== {label}: {q} ===", file=sys.stderr)
        try:
            results = search(q, max_results=20)
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            time.sleep(3)
            continue
        print(f"  {len(results)} results", file=sys.stderr)
        for r in results:
            aid = r["arxiv_id_nover"]
            if aid in seen_ids:
                continue
            if r["published"] < "2024-01-01":
                continue
            seen_ids.add(aid)
            all_results.append(r)
        time.sleep(3)

    all_results.sort(key=lambda x: x["published"], reverse=True)
    print(f"\nTotal unique candidates: {len(all_results)}", file=sys.stderr)

    os.makedirs(".scratch", exist_ok=True)
    out_path = ".scratch/arxiv_search_r17.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}", file=sys.stderr)

    for i, r in enumerate(all_results, 1):
        auth = r["authors"][0] if r["authors"] else "?"
        if len(r["authors"]) > 1:
            auth += " et al."
        venue = ""
        if r["journal_ref"]:
            venue = r["journal_ref"][:40]
        elif r["comment"]:
            venue = r["comment"][:40]
        print(f"{i:2}. [{r['published']}] {r['arxiv_id_nover']} | {auth} | {venue}")
        print(f"    {r['title'][:130]}")


if __name__ == "__main__":
    main()
