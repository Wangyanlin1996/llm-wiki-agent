$remaining = @(
    @{id="2605.29168"; slug="neuro-symbolic-kg-ontology"},
    @{id="2503.14957"; slug="kml-procedural-video-qa"},
    @{id="2510.14670"; slug="titan-graph-reasoning-cti"},
    @{id="2604.27713"; slug="kg-policy-compliance"},
    @{id="2602.00029"; slug="lom-large-ontology-model"},
    @{id="2603.01690"; slug="qime-ontology-embeddings"},
    @{id="2604.23345"; slug="vlk-rl-cross-domain-tod"},
    @{id="2507.23358"; slug="teqodo-tod-ontology"}
)
$success = 0
foreach ($d in $remaining) {
    $out = "raw/papers/$($d.slug).pdf"
    & curl.exe -s -L -o $out "https://arxiv.org/pdf/$($d.id)"
    if ((Test-Path -LiteralPath $out) -and (Get-Item -LiteralPath $out).Length -gt 100KB) {
        Write-Output "OK $($d.slug)"; $success++
    } else { Write-Output "FAIL $($d.slug)" }
}
Write-Output "Batch 2: $success/$($remaining.Count)"
