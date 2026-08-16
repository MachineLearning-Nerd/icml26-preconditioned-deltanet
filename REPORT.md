# Audit report

## Decision

`TOY_FINITE_AUDIT_WITH_UNSTARTED_CLAIMS`

The repository is a trustworthy, scoped record of one finite clean-room
recurrence audit. It is not a complete reproduction of the paper's practical
models or empirical results.

## Evidence decision

- **C1:** The exact PDN recurrence and independently reconstructed `C_t P_t`
  agree within the recorded float64 residuals across five seeds. The diagonal
  control fails the equality test, as expected when the exact theorem premise
  is removed. Status: `TOY_FINITE_AUDIT`.
- **C2:** No throughput or chunkwise-kernel result is recorded. Status:
  `UNSTARTED`.
- **C3:** No 340M SlimPajama training or evaluation result is recorded. Status:
  `UNSTARTED`.
- **C4:** No 1B training or evaluation result is recorded. Status:
  `UNSTARTED`.
- **C5:** No MQAR or S-NIAH result is recorded. Status: `UNSTARTED`.

## Reproduction boundary

The paper source and official implementation revision are pinned for inspection,
but the official GPU kernels, training framework, datasets, checkpoints,
throughput measurements, and benchmark runs are not vendored. The finite
Claim 1 fixture therefore supports only the declared local recurrence audit.

## Publication decision

The target repository is `MachineLearning-Nerd/icml26-preconditioned-deltanet`.
It has one public `main` branch, canonical MachineLearning-Nerd attribution,
paper citation metadata, an author thank-you note, content-addressed evidence,
and a dependency-free verifier intended to pass in a fresh clone.
