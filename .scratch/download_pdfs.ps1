$downloads = @(
    @{id="2606.28076"; slug="opi-ontology-kgqa"},
    @{id="2502.11491"; slug="ort-ontology-reverse-kgqa"},
    @{id="2508.01424"; slug="oracle-ontology-multihop"},
    @{id="2602.15898"; slug="multicube-rag-multihop-qa"},
    @{id="2605.29168"; slug="neuro-symbolic-kg-ontology"},
    @{id="2503.14957"; slug="kml-procedural-video-qa"},
    @{id="2510.14670"; slug="titan-graph-reasoning-cti"},
    @{id="2604.27713"; slug="kg-policy-compliance"},
    @{id="2602.00029"; slug="lom-large-ontology-model"},
    @{id="2603.01690"; slug="qime-ontology-embeddings"},
    @{id="2604.23345"; slug="vlk-rl-cross-domain-tod"},
    @{id="2507.23358"; slug="teqodo-tod-ontology"},
    @{id="2501.17348"; slug="positive-friction-dialogue"},
    @{id="2408.02361"; slug="dialogue-ontology-relation-extraction"},
    @{id="2209.04595"; slug="opal-ontology-aware-tod"},
    @{id="2201.08904"; slug="d3st-description-driven-tod"},
    @{id="2108.11275"; slug="ontology-enhanced-slot-filling"},
    @{id="2409.15861"; slug="zero-shot-open-vocab-dst"},
    @{id="2410.22767"; slug="beyond-ontology-dst"},
    @{id="2204.13021"; slug="nlu-plus-plus"},
    @{id="2605.14259"; slug="hear-hypergraph-enterprise"},
    @{id="2509.22434"; slug="ontobot-robotics-ontology"},
    @{id="2406.06469"; slug="husky-language-agent"},
    @{id="2604.10853"; slug="kg-gap-overlap-benchmark"},
    @{id="2108.02174"; slug="knowledge-grounded-dialogue-flow"},
    @{id="2304.12026"; slug="socialdial-socially-aware"},
    @{id="2502.19023"; slug="inconsistency-kg-reasoning-survey"},
    @{id="2406.08223"; slug="llm-kg-research-trends"}
)

$success = 0
$failed = @()
foreach ($d in $downloads) {
    $url = "https://arxiv.org/pdf/$($d.id)"
    $out = "raw/papers/$($d.slug).pdf"
    if (Test-Path -LiteralPath $out) {
        $size = (Get-Item -LiteralPath $out).Length
        if ($size -gt 100KB) {
            Write-Output "SKIP $($d.slug) (already exists, $size bytes)"
            $success++
            continue
        }
    }
    & curl.exe -s -L -o $out $url
    Start-Sleep -Milliseconds 500
    if (Test-Path -LiteralPath $out) {
        $size = (Get-Item -LiteralPath $out).Length
        if ($size -gt 100KB) {
            Write-Output "OK $($d.slug) ($size bytes)"
            $success++
        } else {
            Write-Output "FAIL $($d.slug) (too small: $size bytes)"
            $failed += $d.slug
        }
    } else {
        Write-Output "FAIL $($d.slug) (not downloaded)"
        $failed += $d.slug
    }
}
Write-Output "`n=== Download Summary: $success/$($downloads.Count) succeeded ==="
if ($failed.Count -gt 0) { Write-Output "Failed: $($failed -join ', ')" }
