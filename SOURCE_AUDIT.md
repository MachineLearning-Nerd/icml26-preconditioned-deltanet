# Source audit

## Paper identity

| Source | Pin or identifier | Local record |
| --- | --- | --- |
| arXiv abstract and paper | `2604.21100v1` | `evidence/source/paper.pdf` |
| arXiv source | `2604.21100v1` | `evidence/source/arxiv_source.tar.gz` |
| OpenReview submission | `UC6YiTOeKb` | `contract/metadata.json` |
| Claim 1 excerpt | extracted from `main_material/3_method.tex` | `evidence/source/claim1_method_excerpt.tex` |
| Official implementation | `ntumm120/preconditioned-deltanet@7bd753279af87b39114149a104c5bde9bf67145f` | referenced, not vendored |

The paper record identifies Neehal Tumma, Noel Loo, and Daniela Rus as the
authors and describes exact inverse-Gram equivalence, a diagonal practical
approximation, chunkwise-parallel variants, and 340M/1B empirical results.
The primary paper record is [arXiv:2604.21100](https://arxiv.org/abs/2604.21100);
the official code is [ntumm120/preconditioned-deltanet](https://github.com/ntumm120/preconditioned-deltanet/tree/7bd753279af87b39114149a104c5bde9bf67145f).

## Local source integrity

The vendored paper/source artifacts are checked by
`evidence/source/SHA256SUMS`:

| Path | SHA-256 |
| --- | --- |
| `evidence/source/arxiv_source.tar.gz` | `a2d0711e7eb1f7377a39c139fa49cfebd076e9ad68c7e0044ef56de1526299b7` |
| `evidence/source/paper.pdf` | `8544f821f293706df82f29af315036b659f499ee7b9b39fb167c9f0639425739` |
| `evidence/source/claim1_method_excerpt.tex` | `323f5bb4b6b26d3d33d1d61554bd3e8e405934f39b2de227321e3122c7cb5fc1` |

The official implementation pin resolves to a public upstream commit. Its
configs, training scripts, bundled FLA fork, and kernel paths were inspected
for claim planning; they are not silently treated as local reproduction
evidence.

## Evidence boundaries

- Claim 1 is a clean-room implementation. It does not copy the official
  training code or claim to reproduce its GPU kernels.
- The exact theorem premise and the practical diagonal approximation are kept
  separate. The diagonal negative control is not a quality benchmark.
- No SlimPajama data, checkpoints, GPU timing, 340M/1B run, MQAR result, or
  S-NIAH result is vendored or claimed here.
- The local source archive and PDF establish the paper revision used for the
  audit; they do not make the local Claim 1 fixture a general proof.
- The official source commit and its authorship remain upstream provenance;
this repository's code and audit labels are independent.
