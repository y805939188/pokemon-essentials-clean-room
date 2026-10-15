"""Finite command receipt census; imports the fully inspected C10 classifier.

It reads task log metadata and public command events. It does not run recovered
commands, change original receipts, or infer process/semantic success from exit.
"""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'tasks/R7-C10/receipt_audit.py'
spec = importlib.util.spec_from_file_location('r7_receipts', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
# Reuse the actual collector with a distinct report-only destination. C10's
# prior snapshots remain immutable. The output is final evidence, not a PASS.
module.HERE = ROOT / 'execution'
module.ROOT = ROOT
sys.argv = [str(Path(__file__)), '--out', 'final-command-census', '--events']
module.main()
