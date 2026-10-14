#!/usr/bin/env python3
"""Read fixed Git objects and literal call inventory; never execute reference."""
import hashlib
import json
from pathlib import Path
import subprocess
from datetime import datetime, timezone

e = Path(__file__).resolve().parent
p = e.parents[2]
r = '/tmp/r6-u09-reference-objects.git'
c = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
expected_tree = '7589c800b61ba13a13040ed0d686979b80a84fd0'
start = datetime.now(timezone.utc).isoformat()
def git(*args):
    return subprocess.check_output(['git', '-C', r, *args])
tree = git('rev-parse', c + '^{tree}').decode().strip()
assert tree == expected_tree
inputs = json.loads((e / 'input-retrieval.json').read_text())
rows = [(v['argv'][-1], json.loads(v['stdout'])['path']) for v in inputs if v['argv'][-2] == 'source']
rows += [(v['identity']['path'], v['local']) for v in json.loads((e / 'additional-readset.json').read_text()) if v['identity']['commit'] == c]
entries = []
for path, local in rows:
    mode, kind, blob, _ = git('ls-tree', c, '--', path).decode().strip().split(None, 3)
    data = git('show', c + ':' + path)
    assert data == Path(local).read_bytes()
    entries.append({'path': path, 'mode': mode, 'type': kind, 'sha': blob,
                    'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                    'full_git_object_equals_raw_payload': True})
(e / 'source-tree-readback.json').write_text(json.dumps({
    'binding_method': 'fixed remote shallow fetch followed by full selected Git blob reads',
    'remote': 'https://github.com/Maruno17/pokemon-essentials.git', 'object_database': r,
    'commit': c, 'tree': tree, 'utc_start': start,
    'utc_end': datetime.now(timezone.utc).isoformat(), 'selected_entries': entries,
    'reference_execution': False, 'tree_identity_not_semantic_full_read': True,
    'previous_attempts': ['source-tree-query.json', 'source-tree-query-retry-1.json']}, ensure_ascii=False, indent=2) + '\n')
searches = []
for literal in ('compile_all', 'pbClearData'):
    argv = ['git', '-C', r, 'grep', '-n', '-F', literal, c, '--', 'Data/Scripts']
    begin = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(argv, capture_output=True, text=True)
    assert result.returncode in (0, 1)
    searches.append({'argv': argv, 'utc_start': begin, 'utc_end': datetime.now(timezone.utc).isoformat(),
                     'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr,
                     'scope': 'literal tracked text matches in fixed R Data/Scripts only; no dynamic/native/plugin absence claim'})
(e / 'source-current-call-search.json').write_text(json.dumps({
    'commit': c, 'searches': searches, 'evidence_level': 'TOOL_VALIDATION',
    'reference_execution': False, 'semantic_full_read_all_tracked_files': False}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'tree': tree, 'full_selected_blobs_verified': len(entries), 'literal_searches': searches}, ensure_ascii=False))
