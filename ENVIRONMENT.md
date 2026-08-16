# Environment and artifact record

## Recorded Claim 1 run

- **Command:** `python src/claim1_exact_preconditioning.py --out outputs/claim1_exact_preconditioning`
- **Interpreter:** Python 3.14.5.
- **Platform:** `Linux-7.0.9-arch2-1-x86_64-with-glibc2.43`.
- **Compute:** local CPU; no GPU, remote, paid, or hosted compute.
- **Protocol:** five seeds, `d=6`, value dimension `4`, `30` steps, float64.
- **Recorded duration:** 0.038698673248291016 seconds.
- **Recorded test command:** `python -m pytest -q`.

The saved run metadata is in `outputs/claim1_exact_preconditioning/config.json`
and `summary.json`. A new run can legitimately change timestamp, platform,
runtime, and floating-point last bits; it must be treated as a new evidence
record rather than silently replacing this one.

## Dependencies

`requirements.txt` pins NumPy `2.4.6` and pytest `9.1.1`. The repository does
not claim a fully locked operating-system image. The publication verifier is
dependency-free and checks the saved evidence bytes without rerunning the
scientific producer.

## Content-addressed artifacts

| Artifact | SHA-256 |
| --- | --- |
| `outputs/claim1_exact_preconditioning/config.json` | `f9abec1314c50f27a3b6932b66af8b4e7b450fd984de005a235771013c99ebd0` |
| `outputs/claim1_exact_preconditioning/raw_fixtures.npz` | `53017d3ca63d5ebfab1cc69ec12c3fbc87720a84cb7e6c7818127733244049d2` |
| `outputs/claim1_exact_preconditioning/results.csv` | `0968b3317ab31f4db32070712663a42b18d39291a27fb6f7a2b8787d04377142` |
| `outputs/claim1_exact_preconditioning/run.log` | `3fa06e0ad3872d7e286de977624455a5f9fb8c39c61b33a32d607d1e179e7916` |
| `outputs/claim1_exact_preconditioning/summary.json` | `2f2eb939bca00d9e9823dcceabc4820ade5a05df6abbe24273fd1d192e7e8640` |
| `evidence/source/arxiv_source.tar.gz` | `a2d0711e7eb1f7377a39c139fa49cfebd076e9ad68c7e0044ef56de1526299b7` |
| `evidence/source/paper.pdf` | `8544f821f293706df82f29af315036b659f499ee7b9b39fb167c9f0639425739` |
| `evidence/source/claim1_method_excerpt.tex` | `323f5bb4b6b26d3d33d1d61554bd3e8e405934f39b2de227321e3122c7cb5fc1` |

The CSV header was normalized to one `kind` column. The numeric rows and
summary values were preserved; the updated row hash is recorded above and in
the output checksum file.
