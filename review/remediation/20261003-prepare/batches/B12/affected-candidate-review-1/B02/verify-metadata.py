"""Independent finite Git/JSON/hash/text checks; never executes reviewed programs."""
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path

BASE = '1d06c45cc0a744fca181ac80ee573cc9ebb9b862'
CANDIDATE = '8ddba850af71f24e7bd77a80b7605c456c31dc7a'
PACKET = '9ad5539f38544fef6037356018015fe418021514'
ROOT = 'review/remediation/20261003-prepare/batches/B12/'
OUT = Path(ROOT + 'affected-candidate-review-1/B02')
cache = {}
checks = []

def git(*args):
    return subprocess.check_output(['git', *args])

def blob(commit, path):
    key = (commit, path)
    if key not in cache:
        raw = git('show', commit + ':' + path)
        cache[key] = (raw, {'commit': commit, 'path': path,
            'git_blob': git('rev-parse', commit + ':' + path).decode().strip(),
            'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
    return cache[key]

def check(label, result, **details):
    checks.append({'check': label, 'pass': bool(result), **details})

def binding(x):
    raw, identity = blob(x['commit'], x['path'])
    check('exact binding', all(identity.get(k) == x[k] for k in
        ['git_blob', 'sha256', 'bytes'] if k in x), identity=identity)
    return raw

def load(path, commit=CANDIDATE):
    return json.loads(blob(commit, path)[0])

def pointer(obj, path):
    for token in path.strip('/').split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        obj = obj[int(token)] if isinstance(obj, list) else obj[token]
    return obj

def logical_hash(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def patch_text(before, patch):
    """Read a unified text patch as metadata; validate context and reconstruct bytes in memory."""
    lines = before.decode().splitlines(keepends=True)
    result, cursor = [], 0
    active = False
    for line in patch.decode().splitlines(keepends=True):
        if line.startswith('@@ '):
            m = re.match(r'@@ -(\d+)(?:,\d+)? \+\d+(?:,\d+)? @@', line)
            start = int(m[1]) - 1
            assert start >= cursor
            result.extend(lines[cursor:start])
            cursor, active = start, True
        elif active and line[0:1] in [' ', '-']:
            assert lines[cursor] == line[1:], (cursor, line)
            if line.startswith(' '): result.append(line[1:])
            cursor += 1
        elif active and line.startswith('+'):
            result.append(line[1:])
    result.extend(lines[cursor:])
    return ''.join(result).encode()

diff = git('diff', '--binary', '--no-ext-diff', '--no-textconv', BASE, CANDIDATE)
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'full-fix-base-to-candidate.diff').write_bytes(diff)
changed = git('diff', '--name-only', '--no-ext-diff', '--no-textconv', BASE, CANDIDATE).decode().splitlines()
check('frozen tree', git('rev-parse', CANDIDATE + '^{tree}').decode().strip()
      == 'c8af1998818447f0e8969bada0b23fc83dfd24fd')
check('FIX_BASE tree', git('rev-parse', BASE + '^{tree}').decode().strip()
      == '5c99f51ec4cc084bc1c2b081306f1b55370744df')
formal = load(ROOT + 'candidate-1/formal-output-identities.json')['outputs']
original = load(ROOT + 'candidate-1/original-output-identities.json')['outputs']
check('complete 11 formal + 5 original scope',
      len(formal) == 11 and len(original) == 5 and
      set(p for p in changed if p.startswith(('deliverables/', 'specs/')))
      == {x['path'] for x in formal + original})
check('other changed paths only B12 author/candidate evidence', all(
      p.startswith(('deliverables/', 'specs/', ROOT + 'author-draft-1/', ROOT + 'candidate-1/'))
      for p in changed))
for x in formal:
    binding(x['input'])
    _, identity = blob(CANDIDATE, x['path'])
    check('formal output', identity['sha256'] == x['output_sha256'] and
          identity['bytes'] == x['output_bytes'], identity=identity)
amendment = load(ROOT + 'author-draft-1/scope-amendment-1.json')
binding(amendment['approved_proposal'])
for x in original:
    before, ident = blob(BASE, x['path'])
    check('original before', ident['git_blob'] == x['input_blob'] and
          ident['sha256'] == x['input_sha256'] and ident['bytes'] == x['input_bytes'], identity=ident)
    _, ident = blob(CANDIDATE, x['path'])
    proposal = next(y for y in amendment['proposals'] if y['path'] == x['path'])
    check('original after exact approved hash', ident['git_blob'] == x['output_blob'] and
          ident['sha256'] == x['output_sha256'] == proposal['approved_after_sha256'] and
          ident['bytes'] == x['output_bytes'], identity=ident)
    patch, ident = blob(proposal['approved_patch_commit'], proposal['approved_patch_path'])
    check('approved patch identity retained', ident['git_blob'] == x['approved_patch_blob'] and
          ident['sha256'] == x['approved_patch_sha256'] and
          patch == blob(CANDIDATE, proposal['approved_patch_path'])[0], identity=ident)
    actual = git('diff', '--no-ext-diff', '--no-textconv', BASE, CANDIDATE, '--', x['path'])
    check('entire approved text patch reconstructs exact candidate original',
          patch_text(before, patch) == blob(CANDIDATE, x['path'])[0], path=x['path'],
          git_diff_serialization_equal_to_patch=actual == patch,
          actual_diff_sha256=hashlib.sha256(actual).hexdigest())
for x in load(ROOT + 'author-draft-1/reading-log.json')['records']:
    binding(x['input'])
controls = load(ROOT + 'author-draft-1/qualified-control-bindings.json')['contributions']
control_objects = []
for x in controls:
    objects = {}
    for key, hashkey in [('whole_original_object_binding', 'whole_original_object_sha256'),
                         ('whole_approved_acceptance_binding', 'whole_acceptance_object_sha256')]:
        obj = pointer(json.loads(binding(x[key])), x[key]['pointer'])
        check('whole qualified logical object', logical_hash(obj) == x[hashkey],
              id=x['id'], kind=key, actual_sha256=logical_hash(obj))
        objects[key] = obj
    control_objects.append({'id': x['id'], **objects,
                            'current_fields': x['complete_current_control_fields']})
# Finite named objects only; no recursive historical traversal or old program invocation.
# The exact objects are inspected in memory; their original paths/pointers remain authoritative.
nav = load(ROOT + 'candidate-1/affected-interface-proposals.json')['interfaces']
map_path = ROOT + 'refreeze-after-B15-C-1/affected-interface-map.json'
amap = load(map_path, PACKET)['potential_interfaces']
check('all potential owners accounted', {x['owner'] for x in nav} ==
      {x['accepted_batch'] for x in amap}, owners=[x['owner'] for x in nav])
for x in nav:
    for b in x['potential_navigation_inputs']:
        binding(b)
for x in amap:
    binding(x['accepted_receipts_binding'])
    for b in x['reverse_declared_reader_inputs']:
        binding(b)
catalogs = []
for path in [ROOT_PATH['path'] for ROOT_PATH in formal if '/test-catalog/' in ROOT_PATH['path']] + [
        'deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md']:
    rows = []
    for commit in [BASE, CANDIDATE]:
        text = blob(commit, path)[0].decode()
        section = ''
        seq = []
        for lineno, line in enumerate(text.splitlines(), 1):
            if line.startswith('## '):
                section = re.split(r'[:：]', line[3:], 1)[0].strip()
            m = re.match(r'^\|\s*([A-Z]+\d+[a-z]?)\s*\|', line)
            if m: seq.append((section, m[1], line, lineno))
        rows.append(seq)
    old, new = rows
    positions = { (s, i): [] for s, i, _, _ in new }
    for s, i, line, n in new: positions[s, i].append((line, n))
    retained = [(s, i, line) for s, i, line, _ in new if (s, i) in
                {(s0, i0) for s0, i0, _, _ in old}]
    equal = retained == [(s, i, line) for s, i, line, _ in old]
    additions = [{'section':s,'id':i,'line':n,'text':line} for s,i,line,n in new
                 if (s,i) not in {(s0,i0) for s0,i0,_,_ in old}]
    check('all catalog old row full text/order/multiplicity', equal, path=path,
          before_rows=len(old), after_rows=len(new))
    catalogs.append({'path':path,'old_rows':len(old),'new_rows':len(new),
                     'old_rows_preserved':equal,'additions':additions,
                     'before':blob(BASE,path)[1],'after':blob(CANDIDATE,path)[1]})
inventory=[]
for path in changed:
    after, ident = blob(CANDIDATE, path)
    before = blob(BASE, path)[1] if git('ls-tree', BASE, '--', path) else None
    if path.endswith('.json'): json.loads(after)
    inventory.append({'path':path,'before':before,'after':ident})
report={'role':'INDEPENDENT_AFFECTED_METADATA_ONLY','FIX_BASE':BASE,
        'reviewed_sha':CANDIDATE,'packet_sha':PACKET,
        'unfiltered_diff':{'command':['git','diff','--binary','--no-ext-diff','--no-textconv',BASE,CANDIDATE],
           'sha256':hashlib.sha256(diff).hexdigest(),'bytes':len(diff),'files':len(changed)},
        'checks':checks,'catalogs':catalogs,'changed_inventory':inventory,
        'unique_exact_file_bindings':list(x[1] for x in cache.values()),
        'failures':[x for x in checks if not x['pass']],
        'quality_pass_inferred_from_metadata':False,'behavior_executions':0}
owner_wp={'B02':list(range(6,11)), 'B03':list(range(11,15)), 'B04':list(range(15,18)),
          'B07':list(range(28,33)), 'B08':list(range(33,38)), 'B09':list(range(38,43)),
          'B10':list(range(43,47)), 'B11':list(range(47,51)), 'B14':list(range(59,62)),
          'B15':list(range(62,65))}
all_paths=git('ls-tree','-r','--name-only',BASE,'--','specs/','deliverables/final-specification-set/').decode().splitlines()
owner_inputs={}
for owner, wp in owner_wp.items():
    paths=[p for p in all_paths if (m:=re.search(r'/wp(\d+)(?:[-.]|[abc])',p)) and int(m[1]) in wp]
    owner_inputs[owner]=[]
    for path in paths:
        before, before_id=blob(BASE,path)
        after, after_id=blob(CANDIDATE,path)
        check('accepted owner body preserved',before == after, owner=owner,path=path)
        owner_inputs[owner].append({'before':before_id,'after':after_id,'bytes_equal':before == after})
report['owner_body_identities']=owner_inputs
report['failures']=[x for x in checks if not x['pass']]
(OUT / 'shared-metadata.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'diff':report['unfiltered_diff'],'checks':len(checks),
       'failures':report['failures'],'catalogs':[{k:v for k,v in x.items() if k!='additions'} for x in catalogs]},ensure_ascii=False,indent=2))
