"""Validate the bounded reviewer deliverable and refresh its non-self manifest."""
from pathlib import Path
import hashlib
import json
import subprocess

root = Path('candidates/R7-U01/evidence/reviewer/r2')
prefix = root.as_posix() + '/'
base = 'e646432c644dec04d306842cc5a559a29c718fbc'
paths = subprocess.check_output(['git','diff','--name-only',base]).decode().splitlines()
paths += subprocess.check_output(['git','ls-files','--others','--exclude-standard']).decode().splitlines()
assert all(p.startswith(prefix) for p in paths), paths
per_id = json.loads((root/'per-id.json').read_bytes())
assert per_id['candidate_commit'] == 'a3938bbb8f8c2294465b75363a39fd4598b82a15'
assert per_id['candidate_tree'] == '9a53dcb2abdedbf4246e3e9d93c42080f92939ec'
assert [r['id'] for r in per_id['records']] == ['GR7-M01-001','GR7-J01-001']
vectors = [v for r in per_id['records'] for v in r['vectors']]
assert len(vectors) == len({v['id'] for v in vectors}) == 20
assert all(v['behavior_execution'] == 'NOT_EXECUTED' for v in vectors)
assert all(r['conclusion'] == 'PASS_SCOPED_CANDIDATE' for r in per_id['records'])
assert not any(per_id[k] for k in ['integrated_PASS','ACCEPTED','CLOSED'])
assert all(v == 'UNVERIFIED' for v in per_id['configuration']['effective'].values())
entries = []
for path in sorted(root.rglob('*')):
    if not path.is_file() or path.name == 'artifact-manifest.json':
        continue
    data = path.read_bytes()
    if path.suffix == '.json':
        json.loads(data)
    entries.append({'path': path.as_posix(), 'bytes': len(data),
                    'sha256': hashlib.sha256(data).hexdigest(),
                    'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest(),
                    'mode': '100644'})
manifest = {'schema':'r7.u01-reviewer-artifact-manifest.r2.v1', 'base':base,
            'branch':'codex/r7-u01-reviewer-20261015-r2',
            'reviewer_context':per_id['reviewer_identity']['reviewer_thread_id'],
            'candidate_commit':per_id['candidate_commit'], 'candidate_tree':per_id['candidate_tree'],
            'write_prefix':prefix, 'files':entries,
            'self_identity':'Manifest itself bound by final externally returned commit/tree and exhaustive remote readback. No circular self hash.',
            'qualification':'Reviewer evidence only, no author mirror or formal changes. Tool exits do not grant semantic or runtime credit.'}
(root/'artifact-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'scope':'PASS', 'nonself_files':len(entries), 'vectors':len(vectors),
                  'required_conclusions':[r['conclusion'] for r in per_id['records']]}))
