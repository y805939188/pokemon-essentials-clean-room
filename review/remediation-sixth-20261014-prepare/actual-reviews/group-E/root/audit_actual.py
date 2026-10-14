"""Reviewer-owned byte/contribution audit; never execute reference or candidate code."""
from pathlib import Path
from collections import Counter
import difflib
import hashlib
import json
import re
import subprocess

OUT = Path(__file__).resolve().parent
ACTUAL = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
BASE = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
INPUT = 'review/remediation-sixth-20261014-prepare/integration/U01-U14-final-composite-20261014/actual-review-input.json'
CONTRACT = 'review/remediation-sixth-20261014-prepare/contracts/R6-U13.json'

def git(*args):
    return subprocess.run(['git', *args], check=True, capture_output=True).stdout

def blob(commit, path):
    return git('show', f'{commit}:{path}')

def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())

def save(name, value):
    (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

data = blob(ACTUAL, INPUT)
x = json.loads(data)
selected = [f for f in x['files'] if any(c['batch']=='R6-U13' for c in f['contributions'])
            or f['path'].endswith('wp66-a-party-and-summary-ui.md')]
files = []
diffs = []
for f in selected:
    path = f['path']
    current = blob(ACTUAL, path)
    base = blob(BASE, path)
    ident = identity(current)
    assert ident == f['actual'], (path, ident, f['actual'])
    entry = git('ls-tree', ACTUAL, '--', path).decode().strip().split('\t')[0].split()
    assert entry == [f['mode'], f['type'], ident['git_blob']], entry
    changes = []
    for c in f['contributions']:
        candidate = blob(c['candidate_commit'], c['candidate_path'])
        assert identity(candidate) == c['identity'], c
        oldlines, newlines = base.decode().splitlines(keepends=True), candidate.decode().splitlines(keepends=True)
        blocks = []
        for tag, a, b, start, stop in difflib.SequenceMatcher(None, oldlines, newlines, autojunk=False).get_opcodes():
            if tag == 'equal':
                continue
            postimage = ''.join(newlines[start:stop]).encode()
            blocks.append(dict(tag=tag, baseline_lines=[a+1,b], candidate_lines=[start+1,stop],
                               postimage_identity=identity(postimage),
                               exact_postimage_contained_in_actual=postimage in current,
                               actual_occurrences=current.count(postimage) if postimage else None,
                               qualification='Exact postimage containment is a mechanical preservation check, not semantic acceptance.'))
        changes.append(dict(batch=c['batch'], candidate_commit=c['candidate_commit'],
                            candidate_path=c['candidate_path'], identity=identity(candidate),
                            actual_equals_candidate=current==candidate, changed_blocks=blocks))
    ids, scoped_ids = [], []
    section = 'document'
    for line in current.decode().splitlines():
        heading = re.match(r'^##\s+([^：: ]+)',line)
        if heading:
            section = heading.group(1)
        match = re.match(r'^\|\s*([A-Z][A-Za-z0-9_-]*)\s*\|',line)
        if match and any(c.isdigit() for c in match.group(1)):
            ids.append(match.group(1))
            scoped_ids.append(section+'/'+match.group(1))
    counts, unscoped = Counter(scoped_ids), Counter(ids)
    files.append(dict(path=path, mode=f['mode'], type=f['type'], actual=ident,
                      baseline=identity(base), contributions=changes,
                      table_ids_raw_count=len(ids), duplicate_scoped_table_ids={k:v for k,v in counts.items() if v>1},
                      unscoped_label_collisions={k:v for k,v in unscoped.items() if v>1},
                      table_namespace_qualification='WS/Wxx and RC/Wxx are different existing table namespaces; count raw rows before mapping.'))
    diffs.extend(difflib.unified_diff(base.decode().splitlines(keepends=True), current.decode().splitlines(keepends=True),
                                    fromfile=f'{BASE}:{path}', tofile=f'{ACTUAL}:{path}'))

receiver = json.loads(blob('3ef4854ef43eac92fd1dc57350e4cf6aa160082b',
 'review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/facility/wp66-a-receiver-payload.json'))
u10 = next(c for f in selected if f['path']==receiver['receiver_path'] for c in f['contributions'])
candidate = blob(u10['candidate_commit'], u10['candidate_path'])
actual_receiver = blob(ACTUAL, receiver['receiver_path'])
old, new = receiver['old_full_line'].encode(), receiver['proposed_full_line'].encode()
assert candidate.count(old)==1 and candidate.count(new)==0
assert actual_receiver == candidate.replace(old,new,1)

contracts = [dict(commit=c, identity=identity(blob(c,CONTRACT)))
             for c in [PREP,'00b45de642f07cee9953e42f04cce9c35d77346f',
                       '9971fe84896786645cdcda3ab45e5caf7785cabc',ACTUAL]]
assert all(c['identity']==contracts[0]['identity'] for c in contracts)
save('actual-byte-contribution-audit.json',dict(
    schema='r6.group-E.actual-byte-contribution-audit.v1', actual_commit=ACTUAL,
    workspace_tree=git('rev-parse',f'{ACTUAL}^{{tree}}').decode().strip(),
    formal_tree=git('rev-parse',f'{ACTUAL}:deliverables/final-specification-set').decode().strip(),
    input_path=INPUT,input_identity=identity(data),selected_path_count=len(files),files=files,
    receiver=dict(path=receiver['receiver_path'], payload_commit='3ef4854ef43eac92fd1dc57350e4cf6aa160082b',
                  exact_single_clause_over_U10_candidate=True,
                  all_other_U10_candidate_bytes_preserved=True,
                  semantic_joint_review='Separate human/agent full-text review; not inferred from exact replacement.'),
    contract_bindings=contracts,
    reviewer_metadata_correction='Earlier root len(str)=354597 was Unicode characters, not UTF-8 bytes. Correct UTF-8 length is 370944; all four contract blobs are identical. No contract drift exists.',
    execution=dict(reference_source=0,candidate_checker=0,independent_behavior_model=0,host_Demo_real_save=0),
    qualification='Byte/hash/tree/table-ID/diff analysis only. No all-group semantic signature, no formal acceptance, no CLOSED.'))
(OUT/'baseline-to-actual.diff').write_text(''.join(diffs))
print(json.dumps(dict(paths=len(files), all_actual_identities_match=True,
    total_actual_bytes=sum(f['actual']['bytes'] for f in files),
    noncontained_postimages=[dict(path=f['path'],batch=c['batch'],block=b)
      for f in files for c in f['contributions'] for b in c['changed_blocks']
      if not b['exact_postimage_contained_in_actual']],
    duplicate_scoped_table_ids={f['path']:f['duplicate_scoped_table_ids'] for f in files if f['duplicate_scoped_table_ids']},
    receiver_exact_single_clause=True,contract_exact_identity=True),ensure_ascii=False))
