# ICML 2026 — Preconditioned DeltaNet

This repository is an independent reproduction and audit record for [Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences](https://arxiv.org/abs/2604.21100).

Current scope is intentionally explicit:

- Claim 1 has a finite clean-room recurrence audit labeled TOY_FINITE_AUDIT.
- Claims 2–5 have not been reproduced in this repository and are labeled UNSTARTED.
- No theorem, throughput, language-model, or synthetic-benchmark claim is marked verified by the current evidence.
- No judge score is recorded here. The challenge contract contains five claims worth ten points; that is not a result.

The repository has been normalized from its former challenge-generated name to:

    MachineLearning-Nerd/icml26-preconditioned-deltanet

The published audit surface is intentionally paper-first. The detailed
claim, source, branch, environment, and attribution records are linked below;
[`verify_final.py`](verify_final.py) checks the same invariants in a fresh
clone.

## Audit dossier

| File | Purpose |
| --- | --- |
| [`STATUS.md`](STATUS.md) | Current publication and per-claim status. |
| [`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md) | Claim-to-producer-to-evidence map and limitations. |
| [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md) | Paper, official-code pin, and source-boundary record. |
| [`BRANCH_AUDIT.md`](BRANCH_AUDIT.md) | Branch inventory and attribution-normalization record. |
| [`ENVIRONMENT.md`](ENVIRONMENT.md) | Recorded environment, commands, and artifact hashes. |
| [`REPORT.md`](REPORT.md) | Scoped audit decision and reproduction boundary. |
| [`CITATION.cff`](CITATION.cff) | Citation metadata for this audit repository. |
| [`AUTHOR_THANK_YOU.md`](AUTHOR_THANK_YOU.md) | Thank-you note and independence statement. |
| [`claims.json`](claims.json) | Machine-readable claim ledger. |
| [`EVIDENCE_MANIFEST.json`](EVIDENCE_MANIFEST.json) | Machine-readable evidence and publication manifest. |

## Paper and implementation record

| Field | Record |
| --- | --- |
| Paper | Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences |
| Authors | Neehal Tumma, Noel Loo, and Daniela Rus |
| Venue | ICML 2026 |
| arXiv | [2604.21100v1](https://arxiv.org/abs/2604.21100) |
| OpenReview | [UC6YiTOeKb](https://openreview.net/forum?id=UC6YiTOeKb) |
| Former repository | icml26-repro-UC6YiTOeKb-preconditioned-deltanet |
| Target repository | icml26-preconditioned-deltanet |
| Canonical branch | main |
| Official implementation | [ntumm120/preconditioned-deltanet](https://github.com/ntumm120/preconditioned-deltanet/tree/7bd753279af87b39114149a104c5bde9bf67145f) |
| Official implementation pin | 7bd753279af87b39114149a104c5bde9bf67145f |
| Local source archive SHA-256 | a2d0711e7eb1f7377a39c139fa49cfebd076e9ad68c7e0044ef56de1526299b7 |
| Local paper PDF SHA-256 | 8544f821f293706df82f29af315036b659f499ee7b9b39fb167c9f0639425739 |
| Compute used here | Local CPU; no remote or paid compute |
| Challenge contract | Five live claims, maximum ten points |

## What the paper is doing

The paper views linear sequence models through test-time regression: a recurrent state learns a key-to-value map by online least squares. Standard DeltaNet performs a first-order delta-rule update, while this work introduces preconditioning to account for the curvature of the key Gram matrix.

The exact inverse-Gram construction gives an equivalence between preconditioned linear attention (PLA) and preconditioned DeltaNet (PDN). The practical method uses a diagonal key-Gram approximation to build preconditioned DeltaNet, Gated DeltaNet (PGDN), and Kimi Delta Attention (PKDA) variants with chunkwise-parallel forms. The empirical section evaluates synthetic recall and language modeling at 340M and 1B parameters.

The distinction that matters for this audit is:

- exact algebraic equivalence under the full inverse-Gram preconditioner;
- approximate diagonal preconditioning used by the practical models;
- benchmark and throughput results at training scale.

Only the first item has a finite local check in the current repository. The other two require separate reproduction routes.

## Claim ledger

| Claim | Paper statement | Production path | Current evidence | Status |
| --- | --- | --- | --- | --- |
| 1 | Theorem 3.1: with exact inverse-Gram preconditioning, the PDN state satisfies S_t = C_t P_t for every t and PDN/PLA query outputs match. | evidence/source/claim1_method_excerpt.tex pins the source equation; src/claim1_exact_preconditioning.py independently computes the online PDN state and C_t P_t from accumulated statistics; outputs/claim1_exact_preconditioning/ stores raw rows, fixtures, summary, run log, and hashes. | Five seeds, d=6, value dimension 4, 30 tokens, float64. Maximum exact state residual 7.22e-16; maximum output residual 2.66e-15; diagonal-preconditioner control minimum state residual 0.5055. | TOY_FINITE_AUDIT — the finite fixture supports the recurrence within tolerance but is not a proof for arbitrary sequences. |
| 2 | The diagonal key-Gram approximation enables practical preconditioned DeltaNet, GDN, and KDA variants with chunkwise-parallel algorithms and about 10% throughput overhead relative to the base models. | Planned route: audit the pinned official implementation, compare exact and diagonal preconditioners, reproduce the kernel/throughput setup, and preserve device, sequence-length, chunk-size, and baseline details. | No throughput or chunkwise benchmark result is present in this repository. | UNSTARTED |
| 3 | At 340M parameters on SlimPajama, PGDN reaches 49.96% average zero-shot commonsense accuracy versus 48.86% for GDN, and 26.17% average in-context recall versus 24.77%. | Planned route: pin the official 340M configuration and data/evaluation commands, run the smallest faithful training/evaluation path available, and compare PGDN with GDN using the paper's task aggregation. | No 340M training or evaluation artifact is present. | UNSTARTED |
| 4 | At 1B parameters, PGDN reaches 56.38% average zero-shot commonsense accuracy versus 55.44% for GDN, and 34.99% average in-context recall versus 33.87%. | Planned route: pin the official 1B configuration, record hardware and training budget, and reproduce or transparently scope any reduced-scale substitution. | No 1B training or evaluation artifact is present. | UNSTARTED |
| 5 | PGDN maintains or improves performance on MQAR across sequence lengths and improves S-NIAH results. | Planned route: audit the official synthetic-benchmark configs, reproduce the sequence-length sweeps, and preserve metric tables and plots with baseline and seed details. | No MQAR or S-NIAH result is present. | UNSTARTED |

## How the current Claim 1 result is produced

The finite Claim 1 path is:

1. The local arXiv source archive, PDF, and method excerpt are hash-pinned in evidence/source/SHA256SUMS.
2. CLAIM_1_PROTOCOL.md fixes five seeds, float64, the exact residual threshold, and the diagonal negative control.
3. src/claim1_exact_preconditioning.py generates independent keys, values, and queries, runs the exact PDN update, and reconstructs the PLA target from C_t and a direct Gram inverse.
4. The exact and diagonal-control rows are written to outputs/claim1_exact_preconditioning/results.csv and raw_fixtures.npz.
5. summary.json applies the predeclared acceptance rule; SHA256SUMS records the output bytes.
6. logbook/claim-1.md records the command, result, and limitation.

The two tests check the exact recurrence/control behavior and the completeness of the local contract/source manifest. They do not validate the unstarted empirical claims.

The saved CSV has one `kind` column and its checksum is recorded in
`outputs/claim1_exact_preconditioning/SHA256SUMS`. The producer and its small
schema test are kept together so future reruns cannot silently recreate the
earlier duplicated-header artifact.

## Repository map

| Path | Purpose |
| --- | --- |
| contract/metadata.json | Paper identity and five live challenge claims. |
| contract/live_claims.json | Current claim text and unverified initial statuses. |
| contract/contract_manifest.json | Challenge source URLs and contract hashes. |
| evidence/source/ | Hash-pinned arXiv source, PDF, and Claim 1 excerpt. |
| CLAIM_1_PROTOCOL.md | Pre-registered finite recurrence protocol and verdict rule. |
| src/claim1_exact_preconditioning.py | Claim 1 clean-room implementation. |
| outputs/claim1_exact_preconditioning/ | Claim 1 results, configuration, fixtures, log, and manifest. |
| logbook/claim-1.md | Claim 1 method, commands, result, control, and limitation. |
| tests/ | Small contract and Claim 1 checks. |
| STATUS.md | Current paper, claim, and publication status. |
| AUTONOMOUS_STATE.json | Continuation checkpoint for the next claim audit. |
| BRANCH_AUDIT.md | Final branch inventory and identity policy. |
| SOURCE_AUDIT.md | Paper and upstream implementation provenance. |
| verify_final.py | Dependency-free fail-closed publication verifier. |

## Reproduce the current finite audit

Install the pinned local requirements:

    python -m pip install -r requirements.txt

Run Claim 1:

    python src/claim1_exact_preconditioning.py --out outputs/claim1_exact_preconditioning

Run the repository's small checks:

    python -m pytest -q

Verify the saved output bytes:

    (cd outputs/claim1_exact_preconditioning && sha256sum -c SHA256SUMS)

The current output was generated on local CPU. Re-running it may update timestamps, Python/platform metadata, and output hashes; a new run should be committed only with its provenance.

## Branch policy

The former repository has only `main`. There are no experiment branches to
merge or delete, and no `orx/*` refs. The final public surface keeps one
canonical `main` branch. All reachable commits are attributed to
`MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>` with no
co-author trailers; see [`BRANCH_AUDIT.md`](BRANCH_AUDIT.md).

Future claim work should use one focused branch at a time, merge the final evidence into main, and record the paper/code revision, command, environment, hardware, raw output, negative controls, and limitations in the claim log.

## Limitations and open work

- The Claim 1 fixture is finite and synthetic. It does not prove Theorem 3.1 for arbitrary sequence length or numerical regimes.
- The diagonal negative control demonstrates that the exact theorem premise matters; it does not establish the practical model's quality.
- Claims 2–5 need source-faithful implementation and experiment audits.
- The official code repository is pinned for inspection, but no official training run or benchmark result has been reproduced here.
- No throughput, 340M, 1B, MQAR, or S-NIAH result should be inferred from the Claim 1 residuals.
- No remote compute or GPU result is claimed by this repository.

## Citation

Please cite the paper when using this audit:

    @inproceedings{tumma2026preconditioned,
      title={Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences},
      author={Neehal Tumma and Noel Loo and Daniela Rus},
      booktitle={International Conference on Machine Learning},
      year={2026},
      url={https://openreview.net/forum?id=UC6YiTOeKb}
    }

The arXiv record is [2604.21100](https://arxiv.org/abs/2604.21100).

## Thank you

Thank you to Neehal Tumma, Noel Loo, and Daniela Rus for developing the preconditioned recurrence perspective and for releasing an implementation that makes the method inspectable. This repository is an independent reproduction and documentation effort; the authors are not responsible for its code, experiments, or status labels.
