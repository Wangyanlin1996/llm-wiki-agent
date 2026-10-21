"""Supplementary search for D3: agent loop detection/resolution."""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import json
import sys

BASE = "https://export.arxiv.org/api/query"

QUERIES = [
    ("D3-S1", "abs:agent AND abs:repetition AND abs:detection AND abs:LLM"),
    ("D3-S2", "abs:agent AND abs:trajectory AND abs:verification AND abs:runtime"),
    ("D3-S3", "abs:LLM AND abs:agent AND abs:self-correction AND abs:planning"),
    ("D3-S4", "abs:agent AND abs:termination AND abs:condition AND abs:LLM"),
    ("D3-S5", "abs:agent AND abs:monitoring AND abs:anomaly AND abs:execution"),
    ("D3-S6", "abs:ontology AND abs:agent AND abs:verification AND abs:execution"),
    ("D3-S7", "abs:agent AND abs:stuck AND abs:recovery AND abs:LLM"),
    ("D3-S8", "abs:multi-agent AND abs:deadlock AND abs:resolution"),
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
            "journal_ref": journal_ref,
            "comment": comment,
        })
    return results


def search(query, max_results=15):
    params = urllib.parse.urlencode({
        "search_query": query,
        "start": 0,
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
            results = search(q, max_results=15)
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            time.sleep(3)
            continue
        print(f"  {len(results)} results", file=sys.stderr)
        for r in results:
            aid = r["arxiv_id_nover"]
            if aid in seen_ids:
                continue
            if r["published"] < "2024-06-01":
                continue
            seen_ids.add(aid)
            all_results.append(r)
        time.sleep(3)

    all_results.sort(key=lambda x: x["published"], reverse=True)
    print(f"\nTotal unique D3 candidates: {len(all_results)}", file=sys.stderr)

    with open(".scratch/arxiv_search_r17_d3.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    for i, r in enumerate(all_results, 1):
        auth = r["authors"][0] if r["authors"] else "?"
        if len(r["authors"]) > 1:
            auth += " et al."
        venue = r["journal_ref"] or r["comment"] or ""
        if venue:
            venue = venue[:40]
        print(f"{i:2}. [{r['published']}] {r['arxiv_id_nover']} | {auth} | {venue}")
        print(f"    {r['title'][:130]}")
        print(f"    A: {r['summary'][:250]}")
        print()


if __name__ == "__main__":
    main()
