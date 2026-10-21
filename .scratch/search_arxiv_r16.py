"""arXiv API search for ontology graph retrieval papers (Round 16)."""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import json
import sys

BASE = "https://export.arxiv.org/api/query"

# Round 15 already-ingested arXiv IDs (exclude these)
ALREADY = {
    "2412.15235", "2604.00500", "2604.09550", "2606.11910", "2607.11464",
    "2502.18992", "2504.00389", "2604.18478", "2607.04391", "2608.08618",
    "2607.18029", "2608.07700", "2508.11784", "2507.14032", "2607.28662",
    "2607.01773", "2604.23090",
}

QUERIES = [
    ("Q1", "abs:ontology AND abs:retrieval AND abs:\"knowledge graph\""),
    ("Q2", "abs:ontology AND abs:RAG AND abs:grounded"),
    ("Q3", "abs:ontology AND abs:SPARQL AND abs:query AND abs:LLM"),
    ("Q4", "abs:ontology AND abs:graph AND abs:retrieval AND abs:embedding"),
    ("Q5", "abs:ontology AND abs:reasoning AND abs:retrieval AND abs:agent"),
]


def parse_arxiv_xml(xml_text):
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(xml_text)
    results = []
    for entry in root.findall("a:entry", ns):
        arxiv_id_url = entry.find("a:id", ns).text.strip()
        arxiv_id = arxiv_id_url.split("/abs/")[-1]
        # strip version
        arxiv_id_nover = arxiv_id.split("v")[0]
        title = " ".join(entry.find("a:title", ns).text.split())
        summary = " ".join(entry.find("a:summary", ns).text.split())
        published = entry.find("a:published", ns).text[:10]
        authors = [a.find("a:name", ns).text for a in entry.findall("a:author", ns)]
        # category
        categories = [c.get("term") for c in entry.findall("a:category", ns)]
        # journal/doi
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
            if aid in ALREADY:
                continue
            if aid in seen_ids:
                continue
            # Filter: year 2025-2026
            if r["published"] < "2025-01-01":
                continue
            seen_ids.add(aid)
            all_results.append(r)
        time.sleep(3)  # rate limit

    # Sort by published date descending
    all_results.sort(key=lambda x: x["published"], reverse=True)

    print(f"\nTotal unique new candidates: {len(all_results)}", file=sys.stderr)
    out_path = ".scratch/arxiv_search_r16.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}", file=sys.stderr)

    # Print compact table
    for i, r in enumerate(all_results, 1):
        auth = r["authors"][0] if r["authors"] else "?"
        if len(r["authors"]) > 1:
            auth += " et al."
        venue = ""
        if r["journal_ref"]:
            venue = r["journal_ref"][:40]
        elif r["comment"]:
            venue = r["comment"][:40]
        print(f"{i:2}. [{r['published']}] {r['arxiv_id']} | {auth} | {venue}")
        print(f"    {r['title'][:120]}")


if __name__ == "__main__":
    main()
