# Branch audit

## Final branch policy

| Final branch | Former public ref | Purpose |
| --- | --- | --- |
| `main` | `main` | Paper-first audit dossier, Claim 1 evidence, claim ledger, and publication surface. |

The repository has no experiment, release, or `orx/*` branches. The final
publication is intentionally main-only; future claim work should use a
focused branch and merge its evidence into `main` only after updating the
claim ledger and verifier.

## Pre-normalization history

Before attribution cleanup, the public repository had one branch with tip
`6b2a6463931e13f4f050494d0f25dce044841d30` and five reachable commits:

| Commit | Purpose |
| --- | --- |
| `03d7ca3` | Initialize the UC6YiTOeKb reproduction contract and Claim 1 protocol. |
| `4e336cd` | Record the public repository and initialization checkpoint. |
| `06850ea` | Add the Claim 1 exact PDN/PLA recurrence toy audit. |
| `b9ea8dc` | Document the initial preconditioned DeltaNet audit. |
| `6b2a646` | Record the initial verified publication checkpoint. |

The result-schema cleanup is retained as a separate history entry. The
documentation dossier is the final additional entry. No scientific result is
changed by either metadata normalization or the duplicate-header cleanup.

## Attribution policy

- **Repository:** `MachineLearning-Nerd/icml26-preconditioned-deltanet`.
- **Default and final branch:** `main`.
- **Author and committer:** `MachineLearning-Nerd
  <MachineLearning-Nerd@users.noreply.github.com>`.
- **Co-author trailers:** none permitted.
- **Legacy refs:** no legacy branch ref is part of the final publication.

[`verify_final.py`](verify_final.py) checks the final branch inventory and all
reachable author/committer identities in a fresh clone.
