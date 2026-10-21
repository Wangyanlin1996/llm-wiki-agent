"""Download 18 PDFs for Round 16."""
import subprocess
import os
import time
import sys

PAPERS = [
    ("ontology-driven-graph-rag-legal", "2505.00039"),
    ("kg2qa-communication-standards", "2506.07037"),
    ("ontology-evidence-path-kgqa", "2606.28076"),
    ("ontologx-cybersecurity-kg", "2510.01409"),
    ("ragulating-compliance-kg", "2508.09893"),
    ("dense-ontology-kge", "2504.02889"),
    ("dynamic-ontology-llm-agents", "2608.22974"),
    ("ontology-project-memory-coding", "2608.13662"),
    ("owlpath-bug-repair", "2607.27249"),
    ("deeproot-kg-multi-agent", "2606.15931"),
    ("competency-questions-executable-rag", "2604.02545"),
    ("agentmap-ontology-matching", "2607.27130"),
    ("ontoextend-ontology-extension", "2607.17963"),
    ("beyond-probabilistic-rag-limitations", "2606.09724"),
    ("retrieval-state-lock-in", "2606.22728"),
    ("omni-retrieval-heterogeneous", "2605.29250"),
    ("manufacturing-knowledge-llm", "2507.22619"),
    ("ontology-hybrid-prompt-kgqa", "2502.03992"),
]

OUT_DIR = "raw/papers"
os.makedirs(OUT_DIR, exist_ok=True)

success = 0
failed = []
for slug, arxiv_id in PAPERS:
    out_path = os.path.join(OUT_DIR, f"{slug}.pdf")
    if os.path.exists(out_path) and os.path.getsize(out_path) > 102400:
        print(f"SKIP {slug} (already exists, {os.path.getsize(out_path)} bytes)")
        success += 1
        continue
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    print(f"Downloading {slug} from {url}...", file=sys.stderr)
    try:
        result = subprocess.run(
            ["curl.exe", "-s", "-L", "-o", out_path,
             "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=60
        )
        size = os.path.getsize(out_path) if os.path.exists(out_path) else 0
        if size > 102400:
            print(f"  OK {slug} ({size} bytes)")
            success += 1
        else:
            print(f"  FAIL {slug} (size={size})")
            failed.append((slug, arxiv_id))
    except Exception as e:
        print(f"  ERROR {slug}: {e}")
        failed.append((slug, arxiv_id))
    time.sleep(2)

print(f"\nDone: {success}/{len(PAPERS)} success")
if failed:
    print(f"Failed: {failed}")
