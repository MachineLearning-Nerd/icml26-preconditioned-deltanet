#!/usr/bin/env python3
"""Fail-closed checks for the published Preconditioned DeltaNet audit."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_REPOSITORY = "MachineLearning-Nerd/icml26-preconditioned-deltanet"
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = "MachineLearning-Nerd@users.noreply.github.com"
EXPECTED_BRANCHES = {"main"}
EXPECTED_COMMIT_COUNT = 8
EXPECTED_CLAIMS = {
    "C1": "TOY_FINITE_AUDIT",
    "C2": "UNSTARTED",
    "C3": "UNSTARTED",
    "C4": "UNSTARTED",
    "C5": "UNSTARTED",
}
EXPECTED_HASHES = {
    "outputs/claim1_exact_preconditioning/config.json": "f9abec1314c50f27a3b6932b66af8b4e7b450fd984de005a235771013c99ebd0",
    "outputs/claim1_exact_preconditioning/raw_fixtures.npz": "53017d3ca63d5ebfab1cc69ec12c3fbc87720a84cb7e6c7818127733244049d2",
    "outputs/claim1_exact_preconditioning/results.csv": "0968b3317ab31f4db32070712663a42b18d39291a27fb6f7a2b8787d04377142",
    "outputs/claim1_exact_preconditioning/run.log": "3fa06e0ad3872d7e286de977624455a5f9fb8c39c61b33a32d607d1e179e7916",
    "outputs/claim1_exact_preconditioning/summary.json": "2f2eb939bca00d9e9823dcceabc4820ade5a05df6abbe24273fd1d192e7e8640",
    "evidence/source/arxiv_source.tar.gz": "a2d0711e7eb1f7377a39c139fa49cfebd076e9ad68c7e0044ef56de1526299b7",
    "evidence/source/paper.pdf": "8544f821f293706df82f29af315036b659f499ee7b9b39fb167c9f0639425739",
    "evidence/source/claim1_method_excerpt.tex": "323f5bb4b6b26d3d33d1d61554bd3e8e405934f39b2de227321e3122c7cb5fc1",
}
REQUIRED_FILES = {
    "README.md",
    "STATUS.md",
    "REPORT.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "BRANCH_AUDIT.md",
    "ENVIRONMENT.md",
    "AUTHOR_THANK_YOU.md",
    "CITATION.cff",
    "claims.json",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
}
REQUIRED_EVIDENCE_PATHS = {
    "CLAIM_1_PROTOCOL.md",
    "src/claim1_exact_preconditioning.py",
    "tests/test_claim1_exact_preconditioning.py",
    "contract/metadata.json",
    "contract/live_claims.json",
    "contract/contract_manifest.json",
    "evidence/source/SHA256SUMS",
    "outputs/claim1_exact_preconditioning/SHA256SUMS",
    *EXPECTED_HASHES,
}


def fail(message: str) -> None:
    raise AssertionError(message)


def run(*args: str) -> str:
    result = subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True)
    return result.stdout


def read_json(relative_path: str) -> object:
    with (ROOT / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def sha256(relative_path: str) -> str:
    digest = hashlib.sha256()
    with (ROOT / relative_path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def local_branches() -> set[str]:
    refs = run("git", "for-each-ref", "refs/heads", "--format=%(refname:strip=2)")
    return {ref.strip() for ref in refs.splitlines() if ref.strip()}


def remote_branches() -> set[str]:
    prefix = "refs/remotes/origin/"
    refs = run("git", "for-each-ref", "refs/remotes/origin", "--format=%(refname)")
    return {
        ref.strip()[len(prefix) :]
        for ref in refs.splitlines()
        if ref.strip().startswith(prefix) and ref.strip() != prefix + "HEAD"
    }


def verify_history() -> None:
    records = run("git", "log", "--all", "--format=%an%x00%ae%x00%cn%x00%ce").splitlines()
    if not records:
        fail("no reachable commits")
    expected = f"{CANONICAL_NAME}\x00{CANONICAL_EMAIL}\x00{CANONICAL_NAME}\x00{CANONICAL_EMAIL}"
    unexpected = sorted({record for record in records if record != expected})
    if unexpected:
        fail(f"non-canonical reachable identities: {unexpected}")
    if "Co-authored-by:" in run("git", "log", "--all", "--format=%B"):
        fail("co-author trailer found")
    count = int(run("git", "rev-list", "--count", "--all").strip())
    if count != EXPECTED_COMMIT_COUNT:
        fail(f"expected {EXPECTED_COMMIT_COUNT} reachable commits, found {count}")
    if run("git", "for-each-ref", "refs/original", "--format=%(refname)").strip():
        fail("temporary refs/original remain")


def verify_remote() -> None:
    remote = run("git", "config", "--get", "remote.origin.url").strip()
    normalized = remote.removesuffix(".git").rstrip("/")
    if not normalized.endswith(EXPECTED_REPOSITORY):
        fail(f"origin is {remote!r}, expected {EXPECTED_REPOSITORY!r}")


def verify_outputs() -> None:
    for relative_path, expected_hash in EXPECTED_HASHES.items():
        if sha256(relative_path) != expected_hash:
            fail(f"hash mismatch for {relative_path}")

    summary = read_json("outputs/claim1_exact_preconditioning/summary.json")
    if not isinstance(summary, dict):
        fail("summary must be an object")
    expected_summary = {
        "exact_max_state_residual": 7.216449660063518e-16,
        "exact_max_output_residual": 2.6645352591003757e-15,
        "control_min_state_residual": 0.5055056483628361,
    }
    for key, expected in expected_summary.items():
        if summary.get(key) != expected:
            fail(f"summary value changed: {key}")
    if summary.get("exact_pass") is not True or summary.get("control_fails") is not True:
        fail("Claim 1 acceptance flags are not both true")

    results_path = ROOT / "outputs/claim1_exact_preconditioning/results.csv"
    with results_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_fields = [
            "seed",
            "d",
            "value_dim",
            "steps",
            "approximate",
            "max_state_residual",
            "max_output_residual",
            "kind",
        ]
        if reader.fieldnames != expected_fields:
            fail(f"unexpected results.csv fields: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 10 or sum(row["kind"] == "exact" for row in rows) != 5:
        fail("results.csv does not contain five exact and five control rows")
    if sum(row["kind"] == "diagonal_approx_control" for row in rows) != 5:
        fail("results.csv control rows are incomplete")

    for checksum_path in ("evidence/source/SHA256SUMS", "outputs/claim1_exact_preconditioning/SHA256SUMS"):
        for line in (ROOT / checksum_path).read_text(encoding="utf-8").splitlines():
            expected_hash, relative_name = line.split(maxsplit=1)
            base = Path(checksum_path).parent
            target = (base / relative_name.strip()).as_posix()
            if sha256(target) != expected_hash:
                fail(f"checksum file mismatch for {target}")


def verify_ledgers() -> None:
    claims = read_json("claims.json")
    manifest = read_json("EVIDENCE_MANIFEST.json")
    if not isinstance(claims, dict) or not isinstance(manifest, dict):
        fail("claims and manifest must be JSON objects")
    for record in (claims, manifest):
        if record.get("repository") != EXPECTED_REPOSITORY:
            fail("repository marker is wrong")
        if record.get("overall_status") != "TOY_FINITE_AUDIT_WITH_UNSTARTED_CLAIMS":
            fail("overall status is wrong")
    observed = {row.get("id"): row.get("status") for row in claims.get("claims", [])}
    if observed != EXPECTED_CLAIMS:
        fail(f"claim ledger statuses are wrong: {observed}")
    if manifest.get("claim_statuses") != EXPECTED_CLAIMS:
        fail("manifest claim statuses are wrong")
    manifest_hashes = {
        item.get("path"): item.get("sha256")
        for item in manifest.get("content_addressed_artifacts", [])
        if isinstance(item, dict)
    }
    if any(manifest_hashes.get(path) != digest for path, digest in EXPECTED_HASHES.items()):
        fail("manifest artifact hashes do not match")
    if set(manifest.get("required_audit_files", [])) != REQUIRED_FILES:
        fail("manifest audit-file list is wrong")


def main() -> int:
    missing = sorted(path for path in REQUIRED_FILES | REQUIRED_EVIDENCE_PATHS if not (ROOT / path).exists())
    if missing:
        fail(f"missing required paths: {missing}")
    verify_ledgers()
    verify_outputs()
    verify_remote()
    if local_branches() != EXPECTED_BRANCHES:
        fail(f"local branches differ: {sorted(local_branches())}")
    if remote_branches() != EXPECTED_BRANCHES:
        fail(f"remote branches differ: {sorted(remote_branches())}")
    verify_history()

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in (
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "CITATION.cff",
        "AUTHOR_THANK_YOU.md",
        "TOY_FINITE_AUDIT",
        "UNSTARTED",
    ):
        if marker not in readme:
            fail(f"README is missing marker {marker!r}")
    print("PASS: paper dossier, claim ledger, evidence hashes, main-only branches, and canonical history verified")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, subprocess.CalledProcessError, OSError, json.JSONDecodeError, ValueError) as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
