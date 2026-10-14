"""Independent payload/scope checks; never imports or executes reference code."""
import datetime as dt
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parents[3]
BASE = 'review/remediation-sixth-20261014-prepare'
CAND = 'c3044166390b3d8c36f4cd121bb8619060b58bfe'
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
calls = []

def git(*args, source=False):
    argv = ['git', '-C', str(ROOT / 'reference-objects.git' if source else REPO), *args]
    start = dt.datetime.now(dt.timezone.utc).isoformat()
    p = subprocess.run(argv, capture_output=True, check=True)
    calls.append({'argv': argv, 'cwd': str(REPO), 'utc_start': start,
                  'utc_end': dt.datetime.now(dt.timezone.utc).isoformat(), 'exit': p.returncode,
                  'stdout_bytes': len(p.stdout), 'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(),
                  'stderr': p.stderr.decode(), 'reference_execution': False})
    return p.stdout

def ident(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}

def payload(commit, path, source=False):
    b = git('show', commit + ':' + path, source=source)
    entry = git('ls-tree', commit, '--', path, source=source).decode().strip().split()
    root_tree = git('rev-parse', commit + '^{tree}', source=source).decode().strip()
    binding_tree = git('rev-parse', commit + ':deliverables/final-specification-set').decode().strip() if path.startswith('deliverables/final-specification-set/') else root_tree
    return b, {'commit': commit, 'path': path, 'root_tree': root_tree, 'tree': binding_tree,
               'tree_scope': 'formal_subtree' if path.startswith('deliverables/final-specification-set/') else 'repository_root',
               'mode': entry[0], 'type': entry[1], **ident(b)}

def write(name, obj):
    (ROOT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def check(name, ok, detail):
    checks.append({'name': name, 'passed': bool(ok), 'detail': detail})

checks = []
author = json.loads(git('show', CAND + ':' + BASE + '/candidates/R6-U09/evidence/candidate-files.json'))
inputs = json.loads(git('show', CAND + ':' + BASE + '/candidates/R6-U09/evidence/input-manifest.json'))
manifest = {'candidate_commit': CAND, 'prepare': PREP, 'formal_main': MAIN, 'reference_commit': REF, 'candidate_files': [], 'inputs': []}
for f in author['files']:
    cand, cid = payload(CAND, f['candidate_path'])
    main, mid = payload(MAIN, f['formal_path'])
    prep, pid = payload(PREP, f['candidate_path'])
    check(f['formal_path'] + ':candidate_identity', all(cid[k] == v for k, v in f['candidate'].items()), cid)
    check(f['formal_path'] + ':baseline_identity', all(mid[k] == v for k, v in f['baseline'].items()), mid)
    check(f['formal_path'] + ':prepare_equals_main', prep == main, pid)
    manifest['candidate_files'].append({'candidate': cid, 'formal': mid, 'prepared_mirror': pid})
for f in inputs['inputs']:
    expected = f['identity']
    _, actual = payload(expected['commit'], expected['path'], source=expected['commit'] == REF)
    check(expected['path'] + ':fixed_input_identity', all(actual[k] == expected[k] for k in ['bytes','sha256','git_blob','mode','tree']), actual)
    manifest['inputs'].append(actual)
prompt, prompt_id = payload(PREP, BASE + '/prompts/R6-U09-R.md')
contract, contract_id = payload(PREP, BASE + '/contracts/R6-U09.json')
embedded = re.search(rb'```json\n(.*?)\n```', prompt, re.S).group(1) + b'\n'
check('prompt_exact_user_identity', ident(prompt) == {'bytes':226189,'sha256':'5e041f81d5b34505e8d4b8656a8f93f92b5478c52b794a8f75aa9a1cb12d12cd','git_blob':'1481887f8a75707a0591fbcadb05d6e39f0e7162'}, prompt_id)
check('embedded_contract_exact_bytes', embedded == contract, contract_id)
manifest['prompt'] = prompt_id
manifest['contract'] = contract_id
paths = [f['candidate_path'] for f in author['files']]
diff = git('diff', PREP, CAND, '--', *paths)
published = git('show', CAND + ':' + BASE + '/candidates/R6-U09/evidence/candidate.patch')
check('candidate_patch_exact_recomputed', diff == published, ident(diff))
changes = git('diff', '--name-status', PREP, CAND).decode().splitlines()
check('author_diff_isolated', all(line.split('\t',1)[1].startswith(BASE + '/candidates/R6-U09/') for line in changes), changes)
check('formal_subtree_unchanged', git('rev-parse', CAND + ':deliverables/final-specification-set') == git('rev-parse', MAIN + ':deliverables/final-specification-set'), None)
def pair(rel):
    path = 'deliverables/final-specification-set/' + rel
    return git('show', MAIN + ':' + path).decode(), git('show', CAND + ':' + BASE + '/candidates/R6-U09/mirror/' + path).decode()
def span(text, start, end=None):
    a = text.index(start)
    return text[a:text.index(end,a) if end else len(text)]
for rel,start,end in [
    ('demo-dx/wp75-project-conversion-and-authoring-tools.md','### 3.2','## 4.'),
    ('demo-dx/wp75-project-conversion-and-authoring-tools.md','## 5.','## 16.'),
    ('demo-dx/wp74-battle-animation-authoring-and-exchange.md','# 战斗动画','## 15.'),
    ('demo-dx/wp74-battle-animation-authoring-and-exchange.md','## 17.',None),
    ('pokemon-rules/wp62-pokedex-records-regions-and-content.md','### 5.2',None),
    ('generic-kernel/wp04-pbs-lifecycle.md','**分词**','## 5.')]:
    before,after=pair(rel)
    check('preserved:'+rel+':'+start, span(before,start,end)==span(after,start,end), {'start':start,'end':end})
before,after=pair('test-catalog/demo-dx-wp72-73-74-75-76-77.md')
check('preserved:whole_prior_DX_catalog', after.startswith(before), ident(before.encode()))
before,after=pair('test-catalog/generic-kernel-wp02-03-04.md')
for n in range(1,37):
    key=f'KL{n:02d}'
    old=next(l for l in before.splitlines() if l.startswith('| '+key+' |'))
    new=next(l for l in after.splitlines() if l.startswith('| '+key+' |'))
    check('preserved:'+key, old.split(' | ')[-1]==new.split(' | ')[-1] if n in [2,3] else old==new, {'scope':'expected result only' if n in [2,3] else 'whole row'})
write('identity-manifest.json', manifest)

# Preserve the exact selected historical acceptance contracts. This is a
# projection, with full-object and record identities; not a whole-R5 re-review.
hp = 'review/remediation-fifth-20261013-prepare/contracts/R5-U07/task-packet.json'
hb, hi = payload('22fba7786b0090a1955ce6211315b0036cddfbcd', hp)
h = json.loads(hb)
keys = ['id','severity','disposition','source_anchors','expected_reference_behavior','preconditions','minimal_counterexample','normal_case','failure_or_boundary_case','proposed_spec_change','acceptance_criteria','history_links','excluded_claims','review_resolution']
write('history-contract-projection.json', {'payload': hi, 'selected': [{**{k:f[k] for k in keys if k in f},'pointer':'/findings/'+str(i),'record_sha256':hashlib.sha256(json.dumps(f,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()} for i,f in enumerate(h['findings']) if i < 4]})
selected = json.loads(git('show', CAND + ':' + BASE + '/candidates/R6-U09/evidence/history-selected-bindings.json'))
closure_b, closure_id = payload(selected['fixed_commit'], selected['path'])
closure = json.loads(closure_b)
def walk(x):
    if isinstance(x,dict):
        yield x
        for v in x.values(): yield from walk(v)
    elif isinstance(x,list):
        for v in x: yield from walk(v)
records = {x.get('id'):x for x in walk(closure) if x.get('id') in {r['id'] for r in selected['records']} and 'frozen_required_scope' in x}
check('seven_history_binding_records_exact', all(records.get(r['id']) == r for r in selected['records']), closure_id)
ep='review/remediation-fifth-20261013-prepare/registration/successors/20261013-candidate-progress-u05-u07/SC-U07-001-erratum.json'
eb, ei = payload(MAIN, ep)
write('history-erratum-binding.json', {'payload': ei, 'record': json.loads(eb)})
write('verification-result.json', {'evidence_level':'TOOL_VALIDATION','semantic_verdict_source':'review-report.md; these checks do not adjudicate behavior',
     'reference_execution':False,'checks':checks,'count':len(checks),'failed':sum(not c['passed'] for c in checks),'commands':calls})
print(json.dumps({'checks':len(checks),'failed':sum(not c['passed'] for c in checks),'reference_execution':0,'manifest':'identity-manifest.json','history_projection':'history-contract-projection.json'},ensure_ascii=False))
raise SystemExit(1 if any(not c['passed'] for c in checks) else 0)
