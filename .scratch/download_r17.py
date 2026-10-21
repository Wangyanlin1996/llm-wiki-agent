"""Download 15 PDFs for Round 17."""
import subprocess, os, time, sys

PAPERS = [
    ("scx-router-task-ontology", "2609.02292"),
    ("domain-grounded-tool-orchestration", "2608.30696"),
    ("skillnet-ai-skills", "2603.04448"),
    ("generative-ontology", "2602.05636"),
    ("workflow-to-skill", "2606.06893"),
    ("satir-constraint-ir-clinical", "2604.08849"),
    ("deeprag-hierarchical-reasoning", "2506.00671"),
    ("ragged-events-reasoning", "2506.07042"),
    ("rag-ontology-relational-db", "2506.01232"),
    ("raredxr1-rare-disease", "2607.00147"),
    ("trove-trace-route-validation", "2609.05019"),
    ("gubernaut-homeostatic-controller", "2607.24339"),
    ("argus-agentic-reasoning-runtime", "2608.05144"),
    ("masc-metacognitive-self-correction", "2510.14319"),
    ("failed-trajectories-harness-flaws", "2606.06324"),
]

OUT_DIR = "raw/papers"
os.makedirs(OUT_DIR, exist_ok=True)

success = 0
failed = []
for slug, arxiv_id in PAPERS:
    out_path = os.path.join(OUT_DIR, f"{slug}.pdf")
    if os.path.exists(out_path) and os.path.getsize(out_path) > 102400:
        print(f"SKIP {slug} ({os.path.getsize(out_path)} bytes)")
        success += 1
        continue
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    print(f"DL {slug}...", file=sys.stderr)
    try:
        subprocess.run(
            ["curl.exe", "-s", "-L", "-o", out_path,
             "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=90
        )
        sz = os.path.getsize(out_path) if os.path.exists(out_path) else 0
        if sz > 102400:
            print(f"  OK {slug} ({sz} bytes)")
            success += 1
        else:
            print(f"  FAIL {slug} (sz={sz})")
            failed.append((slug, arxiv_id))
    except Exception as e:
        print(f"  ERR {slug}: {e}")
        failed.append((slug, arxiv_id))
    time.sleep(2)

print(f"\n{success}/{len(PAPERS)} success")
if failed:
    print(f"Failed: {failed}")
