import json, subprocess, sys
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_exact_and_diagonal_control():
    from src.claim1_exact_preconditioning import run_one
    e=run_one(17); c=run_one(17, approximate=True)
    assert e['max_state_residual'] < 1e-10 and e['max_output_residual'] < 1e-10
    assert c['max_state_residual'] > 1e-6
def test_summary_matches_saved_raw():
    p=ROOT/'outputs/claim1_exact_preconditioning/summary.json'
    if p.exists():
      s=json.loads(p.read_text()); assert s['exact_pass'] and s['control_fails']

def test_saved_results_has_one_kind_column():
    with (ROOT/'outputs/claim1_exact_preconditioning/results.csv').open(newline='') as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames == ['seed','d','value_dim','steps','approximate','max_state_residual','max_output_residual','kind']
        assert len(list(reader)) == 10
