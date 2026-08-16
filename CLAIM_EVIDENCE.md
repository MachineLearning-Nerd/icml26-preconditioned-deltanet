# Claim-to-evidence map

This file explains how each live paper claim would be produced and what the
current repository actually supports. A status is scoped to the recorded
producer and its declared inputs; a finite numerical check is not a proof of a
universal theorem.

## Common production graph

```text
paper anchor → pinned source/code → local producer → raw evidence
             → independent checks and negative controls → scoped status
```

## C1 — Exact PDN/PLA equivalence

- **Paper anchor:** Section 3.1, Theorem 3.1 and Eq. `atk_update`.
- **Claim:** under exact inverse-Gram preconditioning, the PDN state satisfies
  `S_t = C_t P_t`, so PDN and PLA query outputs agree.
- **Source:** `evidence/source/claim1_method_excerpt.tex`, extracted from the
  hash-pinned arXiv source archive and listed in
  `evidence/source/SHA256SUMS`.
- **Producer:** `src/claim1_exact_preconditioning.py::run_one` generates
  independent keys, values, and queries; it applies the online PDN recurrence
  and independently reconstructs `C_t P_t` from accumulated statistics and a
  direct Gram inverse.
- **Protocol:** `CLAIM_1_PROTOCOL.md` fixes five seeds (`17, 29, 43, 71,
  101`), `d=6`, value dimension `4`, `30` tokens, float64 arithmetic,
  `G_0=I`, a `1e-10` exact residual threshold, and a diagonal-preconditioner
  negative control.
- **Evidence:** `outputs/claim1_exact_preconditioning/results.csv`,
  `raw_fixtures.npz`, `summary.json`, `config.json`, `run.log`, and
  `SHA256SUMS`.
- **Recorded result:** maximum exact state residual
  `7.216449660063518e-16`; maximum exact query-output residual
  `2.6645352591003757e-15`; minimum diagonal-control state residual
  `0.5055056483628361`.
- **Status:** `TOY_FINITE_AUDIT`.
- **Limitation:** the fixture supports the recurrence on five finite random
  sequences. It does not prove the theorem for arbitrary sequences, lengths,
  conditioning regimes, or implementations.

## C2 — Practical diagonal preconditioning and throughput

- **Paper anchor:** Section 3.3, Eq. 7, Figure 3.
- **Claim:** a diagonal key-Gram approximation enables practical PGDN/PKDA
  variants and chunkwise-parallel algorithms with about 10% throughput
  overhead relative to the corresponding base models.
- **Planned production path:** inspect the pinned official repository;
  identify the exact preconditioner, kernel, chunk size, sequence length,
  device, model, and baseline; run matched baseline/preconditioned kernels;
  retain raw timing data and controls; then compare medians or the paper's
  stated aggregation.
- **Current evidence:** the local Claim 1 control only shows that replacing
  the exact preconditioner changes the finite recurrence. It contains no
  kernel timings or chunkwise benchmark.
- **Status:** `UNSTARTED`.

## C3 — 340M language-model and recall results

- **Paper anchor:** the 340M rows of Table 1.
- **Claim:** on SlimPajama, PGDN reaches 49.96% versus 48.86% average
  zero-shot commonsense accuracy and 26.17% versus 24.77% average in-context
  recall accuracy for GDN.
- **Planned production path:** pin the official 340M config, dataset revision,
  tokenizer, training steps, batch/sequence settings, evaluator and task
  aggregation; run matched PGDN/GDN jobs; preserve checkpoints, logs, raw
  per-task scores, seeds, hardware and budget.
- **Current evidence:** no 340M training or evaluation artifact is present.
- **Status:** `UNSTARTED`.

## C4 — 1B language-model and recall results

- **Paper anchor:** the 1B rows of Table 1.
- **Claim:** at 1B parameters, PGDN reaches 56.38% versus 55.44% average
  zero-shot commonsense accuracy and 34.99% versus 33.87% average in-context
  recall accuracy for GDN.
- **Planned production path:** pin the official 1B config and all training and
  evaluation inputs; record the hardware and token budget; reproduce at the
  stated scale or label any reduced-scale substitution separately.
- **Current evidence:** no 1B training or evaluation artifact is present.
- **Status:** `UNSTARTED`.

## C5 — MQAR and S-NIAH behavior

- **Paper anchor:** Figures 5 and 6 and the associated synthetic-benchmark
  discussion.
- **Claim:** PGDN maintains or improves performance on MQAR across sequence
  lengths and improves S-NIAH results.
- **Planned production path:** pin the synthetic-data generator, task
  definitions, sequence-length sweep, model variants, seeds, metrics and
  plotting code; run PGDN and the named baselines; preserve per-setting raw
  scores and plots.
- **Current evidence:** no MQAR or S-NIAH result is present.
- **Status:** `UNSTARTED`.

## Overall interpretation

Only C1 has a local producer and saved evidence, and it is deliberately
labeled a finite toy audit. C2–C5 remain open. No throughput, training-scale,
benchmark, theorem-wide, or challenge-score conclusion should be inferred
from the C1 residuals.
