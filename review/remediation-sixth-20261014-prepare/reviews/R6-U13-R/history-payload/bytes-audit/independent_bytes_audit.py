"""Reviewer-owned, read-only Git/byte audit; never imports or executes author tools.

Only this review directory receives new files. Source text is neither executed nor
copied into outputs; object and JSON-pointer fingerprints are sufficient here.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
import datetime, difflib, hashlib, json, re, stat, subprocess

REPO = Path('/workspace/pokemon-essentials-clean-room')
OUT = Path(__file__).resolve().parent
C = '00b45de642f07cee9953e42f04cce9c35d77346f'
TREE = '6708f580d5a02f874a1a24a95d7c0649b10c393b'
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BASE = 'review/remediation-sixth-20261014-prepare'
PREFIX = BASE + '/candidates/R6-U13/'
EV = PREFIX + 'evidence/'
UTC = datetime.datetime.now(datetime.timezone.utc).isoformat()
commands = []
errors = []

def git(*args):
    r = subprocess.run(['git', *args], cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    commands.append({'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                     'cwd': str(REPO), 'argv': ['git', *args], 'exit': r.returncode,
                     'stdout_bytes': len(r.stdout), 'stdout_sha256': hashlib.sha256(r.stdout).hexdigest(),
                     'stderr': r.stderr.decode('utf-8', errors='replace')})
    if r.returncode:
        raise RuntimeError(f'git {args!r}: exit {r.returncode}; {r.stderr.decode().strip()}')
    return r.stdout

def ident(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}

@lru_cache(None)
def fixed(commit, path):
    entries = git('ls-tree', '-z', commit, '--', path).split(b'\0')
    entries = [e for e in entries if e]
    if len(entries) != 1:
        raise RuntimeError(f'exact Git path unavailable: {commit}:{path} ({len(entries)} entries)')
    header, actual_path = entries[0].split(b'\t', 1)
    mode, typ, oid = header.decode().split()
    if actual_path.decode() != path or typ != 'blob':
        raise RuntimeError(f'exact regular blob path mismatch: {commit}:{path}')
    data = git('cat-file', 'blob', oid)
    value = {'commit': commit, 'path': path, 'mode': mode, 'type': typ, **ident(data),
             'lines': len(data.splitlines()), 'git_entry': header.decode() + '\t' + path}
    if value['git_blob'] != oid:
        raise RuntimeError('computed Git object ID mismatch')
    return data, value

@lru_cache(None)
def fixed_json(commit, path):
    return json.loads(fixed(commit, path)[0])

def check_declared(label, commit, path, decl):
    try:
        _, actual = fixed(commit, path)
        fields = [k for k in ['bytes', 'sha256', 'git_blob', 'lines'] if k in decl]
        differences = {k: {'declared': decl[k], 'actual': actual[k]} for k in fields if decl[k] != actual[k]}
        row = {'label': label, 'observed': actual, 'declared_fields': {k: decl[k] for k in fields},
               'matches': not differences, 'differences': differences}
        if differences: errors.append({'label': label, 'differences': differences})
        return row
    except RuntimeError as e:
        row = {'label': label, 'commit': commit, 'path': path, 'matches': None, 'unavailable': str(e)}
        errors.append(row)
        return row

def ptr(doc, path):
    cur = doc
    for key in path.split('/')[1:]:
        key = key.replace('~1', '/').replace('~0', '~')
        cur = cur[int(key)] if isinstance(cur, list) else cur[key]
    return cur

def canonical(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

snapshot = {'utc': UTC, 'cwd': str(REPO), 'candidate_commit': C, 'candidate_tree_expected': TREE,
            'candidate_tree_actual': git('rev-parse', C + '^{tree}').decode().strip(),
            'HEAD': git('rev-parse', 'HEAD').decode().strip(),
            'prepare_commit': PREP, 'formal_commit': MAIN, 'reference_commit': REF,
            'actual_configuration': {k: 'UNVERIFIED' for k in ['model', 'effort', 'tier', 'speed', 'uuid']},
            'author_scripts_executed': False, 'reference_or_host_execution': False,
            'semantic_8ID_review': False}
payloads = []
for entry in git('ls-tree', '-rz', C, '--', PREFIX).split(b'\0'):
    if not entry: continue
    _, p = entry.split(b'\t', 1); p = p.decode()
    data, value = fixed(C, p)
    path = REPO / p
    st = path.lstat()
    regular = stat.S_ISREG(st.st_mode)
    observed = ident(path.read_bytes()) if regular else None
    payloads.append({**value, 'workspace_regular_file': regular,
                     'workspace_permissions': oct(stat.S_IMODE(st.st_mode)),
                     'workspace_identity': observed, 'workspace_byte_equal': regular and path.read_bytes() == data})
dump('candidate-payload-identities.json', payloads)

manifest = fixed_json(C, EV + 'candidate-manifest.json')
contract = fixed_json(PREP, BASE + '/contracts/R6-U13.json')
baselines = []
rebuilt_spans = []
for row in manifest:
    p, cp = row['formal_path'], row['candidate_path']
    old, main = fixed(MAIN, p)
    base, prep_mirror = fixed(PREP, PREFIX + 'mirror/' + p)
    prepare_formal, prep_formal = fixed(PREP, p)
    new, candidate = fixed(C, cp)
    current_formal, cand_formal = fixed(C, p)
    baselines.append({'formal_path': p, 'fixed_main': main, 'prepare_mirror': prep_mirror,
                      'prepare_formal': prep_formal, 'candidate_mirror': candidate,
                      'candidate_formal': cand_formal,
                      'prepare_mirror_equals_fixed_main': old == base,
                      'prepare_formal_equals_fixed_main': old == prepare_formal,
                      'candidate_formal_equals_fixed_main': old == current_formal,
                      'candidate_differs_from_baseline': new != old,
                      'manifest_baseline_matches': ident(old) == row['baseline'],
                      'manifest_candidate_matches': ident(new) == row['candidate']})
    sm = difflib.SequenceMatcher(None, old.decode().splitlines(), new.decode().splitlines(), autojunk=False)
    for tag, a, b, c, d in sm.get_opcodes():
        if tag != 'equal':
            rebuilt_spans.append({'path': p, 'operation': tag, 'old_lines': [a+1, b], 'new_lines': [c+1, d],
                                  'old_text': old.decode().splitlines()[a:b], 'new_text': new.decode().splitlines()[c:d]})
dump('baseline-bindings.json', baselines)

inputs = fixed_json(C, EV + 'input-identities.json')
declarations = []
for label in ['prompt', 'contract', 'AGENTS']:
    z = inputs[label]
    declarations.append(check_declared(label, PREP, z['path'], z))
for i, z in enumerate(inputs['required_source_and_formal']):
    declarations.append(check_declared(f'input/{i}/{z["kind"]}', z['commit'], z['path'], z))
prompt = fixed(PREP, inputs['prompt']['path'])[0]
embedded = prompt.decode().split('```json\n', 1)[1].split('\n```', 1)[0].encode()
contract_embedded_equal = embedded == fixed(PREP, inputs['contract']['path'])[0].rstrip(b'\n')
payload_checks = fixed_json(C, EV + 'contract-payload-checks.json')
contract_rebuilt_checks = []
for scope in contract['scope_contracts']:
    for kind in ['source', 'formal']:
        for z in scope['bidirectional_evidence'][kind]:
            decl = z['payload_identity']
            b, _ = fixed(decl['commit'], decl['path'])
            contract_rebuilt_checks.append({'id': scope['id'], 'kind': kind, 'locator': z['locator'],
                                           'commit': decl['commit'], 'path': decl['path'], **ident(b), 'identity_matches': True})
for i, z in enumerate(payload_checks):
    declarations.append(check_declared(f'contract-payload/{i}/{z["id"]}', z['commit'], z['path'], z))
counterchecks = fixed_json(C, EV + 'counter-packet-identities.json')
for i, z in enumerate(counterchecks):
    declarations.append(check_declared(f'counter/{i}', z['commit'], z['path'], z))
dump('input-and-contract-identities.json', {'declarations': declarations,
    'prompt_embedded_contract_exact_bytes': contract_embedded_equal,
    'contract_payload_checks_exact_reconstruction': payload_checks == contract_rebuilt_checks,
    'contract_payload_count': len(payload_checks),
    'required_paths_exact': [(r['kind'], r['path']) for r in inputs['required_source_and_formal']] ==
                           [('source', p) for p in contract['read_only_reference_paths']] + [('formal', p) for p in contract['candidate_formal_paths']],
    'prepare_formal_reference_constants_match': (inputs['prepare'], inputs['formal'], inputs['reference']) == (PREP, MAIN, REF)})

ledger_checks = []
coverage = {}
for i, line in enumerate(fixed(C, EV + 'reading-ledger.jsonl')[0].splitlines(), 1):
    r = json.loads(line)
    try:
        data, f = fixed(r['commit'], r['path'])
        lines = data.decode().splitlines(keepends=True)
        start, end = r['start_line'], r['end_line']
        payload = ''.join(lines[start-1:end]).encode()
        fields = {'bytes': len(data), 'sha256': ident(data)['sha256'], 'lines': len(lines),
                  'git_entry': f['git_entry'], 'returned_bytes': len(payload),
                  'stdout_content_sha256': hashlib.sha256(payload).hexdigest()}
        diffs = {k: {'declared': r[k], 'actual': v} for k,v in fields.items() if r[k] != v}
        valid_interval = 1 <= start <= end <= len(lines)
        coverage.setdefault((r['commit'], r['path']), set()).update(range(start, end+1))
        ledger_checks.append({'ledger_line': i, 'commit': r['commit'], 'path': r['path'],
                              'start_line': start, 'end_line': end, 'valid_interval': valid_interval,
                              'matches': not diffs and valid_interval, 'differences': diffs})
    except (RuntimeError, KeyError, ValueError) as e:
        ledger_checks.append({'ledger_line': i, 'commit': r['commit'], 'path': r['path'],
                              'matches': None, 'unavailable': str(e)})
coverage_checks = []
for z in inputs['required_source_and_formal'] + counterchecks:
    n = len(fixed(z['commit'], z['path'])[0].splitlines())
    count = len(set(range(1,n+1)) - coverage.get((z['commit'],z['path']), set()))
    coverage_checks.append({'commit': z['commit'], 'path': z['path'], 'lines': n, 'uncovered_lines': count})
dump('author-reading-ledger-mechanical-audit.json', {'entries': ledger_checks, 'required_coverage': coverage_checks,
    'boundary': 'Valid fixed identities and segment hashes prove ledger consistency, not downstream untruncated display or actual human/model semantic reading.'})

history = fixed_json(C, EV + 'historical-regression.json')
histrows = [check_declared('history-input', PREP, history['input']['path'], history['input'])]
hist_base = 'review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/'
hist_commit = history['fixed_historical_files']['commit']
for name, decl in history['fixed_historical_files']['files'].items():
    histrows.append(check_declared('history-fixed/' + name, hist_commit, hist_base + name, decl))
hi = fixed_json(PREP, history['input']['path'])
formal_paths = {r['formal_path'] for r in manifest}
rebuilt_nav = []
for r in hi['records']:
    matched = [z for z in r.get('current_formal_paths', []) if z['path'] in formal_paths]
    if matched:
        rebuilt_nav.append({'id': r['id'], 'owner': r['batch_owner'], 'record_key': r.get('record_key'),
                            'frozen_record': r['frozen_record'], 'qualified_scope_binding': r['qualified_scope_binding'],
                            'matched_paths': matched, 'role': 'FINITE_NAVIGATION_NO_VERDICT_TRANSFER'})
nav_checks = []
for i, r in enumerate(history['affected_path_navigation']):
    z = r['frozen_record']; q = r['qualified_scope_binding']
    row = {'index': i, 'id': r['id'], 'owner': r['owner'], 'frozen_record': z, 'qualified_scope_binding': q,
           'identity': check_declared(f'nav/{i}', z['commit'], z['path'], z)}
    try:
        orig = fixed_json(z['commit'], z['path'])
        record = ptr(orig, z['pointer'])
        scope = ptr(fixed_json(q['commit'], q['path']), q['pointer'])
        owner_field = 'batch_owner' if 'batch_owner' in record else 'primary_owner'
        normalized_tuple = {k: record.get(owner_field) if k == 'batch_owner' else record.get(k)
                            for k in q['required_identity_tuple']}
        row.update({'record_sha256_observed': canonical(record), 'record_sha256_matches': canonical(record) == z['record_sha256'],
                    'scope_sha256_observed': canonical(scope), 'scope_sha256_matches': canonical(scope) == q['record_sha256'],
                    'owner_field_observed': owner_field,
                    'owner_normalization_boundary': 'Legacy /controls use primary_owner; /contributions and R3/R4 records use batch_owner. Required navigation tuple names the normalized owner batch_owner.',
                    'record_id_owner_match': (record.get('id'), record.get(owner_field)) == (r['id'], r['owner']),
                    'scope_keys_match': list(scope) == q['scope_keys'],
                    'required_identity_tuple_observed': normalized_tuple,
                    'required_identity_tuple_match': normalized_tuple == q['required_identity_tuple']})
    except (RuntimeError, KeyError, ValueError) as e: row['pointer_unavailable'] = str(e)
    nav_checks.append(row)
scope_checks = []
for r in history['R3_R4_exact_scopes_read']:
    try:
        orig = ptr(fixed_json(r['commit'],r['path']),r['pointer'])
        scope_checks.append({'id': r['id'], 'commit': r['commit'], 'path': r['path'], 'pointer': r['pointer'],
                             'scope_sha256': canonical(orig), 'qualified_scope_matches': orig == r['qualified_scope']})
    except (RuntimeError, KeyError, ValueError) as e: scope_checks.append({'id': r['id'], 'unavailable': str(e)})
legacy_checks = []
try:
    legacy = fixed_json(hist_commit, hist_base + 'regression-legacy-scope.json')
    for r in history['R2_exact_owner_contribution_bindings_read']:
        orig = legacy['contributions'][r['index']]['historical_identity_scope_reuse']
        legacy_checks.append({'index': r['index'], 'pointer': f'/contributions/{r["index"]}/historical_identity_scope_reuse',
                              'scope_sha256': canonical(orig), 'scope_matches': orig == r['scope']})
    b12_matches = legacy['controls'][84]['historical_identity_scope_reuse'] == history['R2_B12_qualified_scope_read']
except (RuntimeError, KeyError, ValueError) as e:
    legacy_checks.append({'unavailable': str(e)}); b12_matches = None
b13 = history['R2_B13_controls']
histrows.append(check_declared('R2-B13', b13['commit'], b13['path'], b13))
b13_checks = []
try:
    original = fixed_json(b13['commit'], b13['path'])
    for i,r in enumerate(b13['assigned_scopes']):
        raw = ptr(original, r['pointer'])
        expected = dict(raw)
        if i == 0:
            expected = {k:v for k,v in raw.items() if k not in ['extensions','extension_decisions','minimum_revision','determinate_recheck']}
            expected['extensions'] = [e for e in raw.get('extensions',[]) if any(p in json.dumps(e,ensure_ascii=False) for p in formal_paths)]
            expected['projection_boundary'] = 'Common root qualification plus complete extensions naming affected paths only; unrelated source-organization extensions not adopted.'
        b13_checks.append({'id': r['id'], 'pointer': r['pointer'], 'whole_original_sha256': canonical(raw),
                           'projected_scope_sha256': canonical(expected), 'assigned_scope_matches': r['qualified_scope'] == expected,
                           'scope_rule_matches': r['scope_rule'] == original['controls'][i]['scope_rule']})
except (RuntimeError, KeyError, ValueError) as e: b13_checks.append({'unavailable':str(e)})
r5_checks = []
r5_contract_path = 'review/remediation-fifth-20261013-prepare/contracts/R5-U04/contract.json'
r5_contract = fixed_json(PREP, r5_contract_path)
def find_identity_rows(value, target, pointer=''):
    rows=[]
    if isinstance(value,dict):
        if value.get('git_blob') == target:
            rows.append({'contract_commit':PREP,'contract_path':r5_contract_path,'contract_pointer':pointer,'declared_identity':value})
        for k,v in value.items():rows.extend(find_identity_rows(v,target,pointer+'/'+k.replace('~','~0').replace('/','~1')))
    elif isinstance(value,list):
        for i,v in enumerate(value):rows.extend(find_identity_rows(v,target,pointer+'/'+str(i)))
    return rows
for r in history['R5_exact_scopes_read']:
    row = {'id': r['id'], 'binding_blob': r['binding_blob'], 'pointer': r['pointer']}
    try:
        try:
            raw = git('cat-file','blob',r['binding_blob'])
            row['recovery_type']='local Git blob';row['git_blob_available']=True
        except RuntimeError as object_error:
            name='recovered-bbdee081.json' if r['binding_blob'].startswith('bbdee081') else 'recovered-7b21312.json'
            cache=OUT.parent/name
            raw=cache.read_bytes()
            row.update({'recovery_type':'parent recovered cache, byte identity independently checked',
                        'cache_path':str(cache),'git_blob_available':False,'local_object_unavailable':str(object_error)})
        original = ptr(json.loads(raw),r['pointer'])
        projected = {k: original[k] for k in ['preconditions','expected_reference_behavior','minimal_counterexample','normal_case','failure_or_boundary_case','proposed_spec_change','acceptance_criteria','review_resolution']}
        row.update({'observed_identity': ident(raw), 'declared_identity_matches': all(ident(raw)[k] == r[k] for k in ident(raw)),
                    'record_id_match': original['id'] == r['id'], 'record_sha256': canonical(original),
                    'projected_scope_sha256': canonical(projected), 'qualified_scope_matches': projected == r['qualified_scope']})
    except (RuntimeError, KeyError, ValueError, OSError) as e: row['unavailable'] = str(e)
    row['declared_original_bindings'] = []
    for z in find_identity_rows(r5_contract,r['binding_blob']):
        f = z['declared_identity']
        observed = check_declared('R5-original/' + r['id'], f['commit'], f['path'], f)
        row['declared_original_bindings'].append({**z,'identity': observed,
            'contract_declared_blob_equals_recovered_blob': f['git_blob'] == r['binding_blob']})
    r5_checks.append(row)
dump('historical-payload-identity-audit.json', {'file_identities':histrows,'navigation_exact_reconstruction':rebuilt_nav == history['affected_path_navigation'],
    'navigation':nav_checks,'R3_R4_scope_pointer_checks':scope_checks,'R2_contribution_pointer_checks':legacy_checks,
    'R2_B12_scope_matches':b12_matches,'R2_B13_projection_checks':b13_checks,'R5_blob_and_original_binding_checks':r5_checks,
    'record_hash_encoding':'UTF-8 JSON ensure_ascii=False sort_keys=True separators=(comma,colon); no trailing newline',
    'boundary':'All pointer/content comparisons are structural identity checks. They do not transfer historical verdicts or validate new behavioral claims.'})

mechanical = {}
ct = 'deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md'
pt = 'deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
old = fixed(MAIN,ct)[0].decode(); new = fixed(C,PREFIX+'mirror/'+ct)[0].decode()
def groups(s):
    return {part.split('：',1)[0]:part for part in re.split(r'^## ',s,flags=re.M)[1:]}
catalog = []
for group, changed in [('QC',set()),('WS',{'W13'}),('PA',{'P14','P15','P16'}),('RC',{'W18'})]:
    a,b = groups(old)[group],groups(new)[group]
    before = [l for l in a.splitlines() if re.match(r'^\| [QWP]\d',l)]
    after = [l for l in b.splitlines() if re.match(r'^\| [QWP]\d',l)]
    ids = [l.split('|')[1].strip() for l in after]
    index = {l.split('|')[1].strip():l for l in after}
    catalog.append({'series':group,'raw_row_count':len(after),'distinct_id_count':len(set(ids)),
                    'duplicate_ids':{k:v for k,v in Counter(ids).items() if v>1},
                    'original_count':len(before),'changed_original_rows_observed':[l.split('|')[1].strip() for l in before if index.get(l.split('|')[1].strip()) != l],
                    'all_other_original_rows_equal':all(index.get(l.split('|')[1].strip()) == l for l in before if l.split('|')[1].strip() not in changed)})
old = fixed(MAIN,pt)[0].decode(); new = fixed(C,PREFIX+'mirror/'+pt)[0].decode()
before = [l for l in old.splitlines() if re.match(r'^\| SF\d',l)]
after = [l for l in new.splitlines() if re.match(r'^\| SF\d',l)]
ids = [l.split('|')[1].strip() for l in after];index={l.split('|')[1].strip():l for l in after}
catalog.append({'series':'SF','raw_row_count':len(after),'distinct_id_count':len(set(ids)),
                'duplicate_ids':{k:v for k,v in Counter(ids).items() if v>1},'original_count':len(before),
                'changed_original_rows_observed':[l.split('|')[1].strip() for l in before if index.get(l.split('|')[1].strip()) != l],
                'all_other_original_rows_equal':all(index.get(l.split('|')[1].strip())==l for l in before if l.split('|')[1].strip() not in {'SF01','SF30'})})
mechanical['catalogue_rows'] = catalog
mechanical['BP_FP_PD_VF_LT_suffix_exact'] = old.split('## BP：',1)[1].encode() == new.split('## BP：',1)[1].encode()
wp40 = 'deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md'
old = fixed(MAIN,wp40)[0]
new = fixed(C,PREFIX+'mirror/'+wp40)[0]
addon = 'Arena 裁判调用同一完整取消：只清列明持续招，回复期为正时保留当前招身份；裁判后的存活未替代者仍受下一轮回复门约束（WP56 §3.2），败者倒下/补位清效另算。'.encode()
mechanical['WP40_addition_occurrences'] = new.count(addon)
mechanical['WP40_previous_whole_bytes_exact_after_removing_addition'] = new.replace(addon,b'') == old
mechanical['changed_spans_exact_reconstruction'] = rebuilt_spans == fixed_json(C,EV+'changed-spans.json')
mechanical['changed_span_count'] = len(rebuilt_spans)
mechanical['candidate_diff_check'] = git('diff','--check',PREP,C).decode()
changed = git('diff','--name-only',PREP,C).decode().splitlines()
allowed = {PREFIX+'mirror/'+p for p in contract['candidate_formal_paths']}
mechanical['frozen_changed_paths'] = changed
mechanical['all_8_mirror_paths_changed'] = set(changed) & allowed == allowed
mechanical['frozen_changes_within_candidate_scope'] = all(p in allowed or p.startswith(EV) for p in changed)
mechanical['integer_arithmetic_observed'] = {'1x100_div205':100//205,'3x100_div205':300//205,'r0_less30':0<30}
mechanical['h24_factor_fields_boundary'] = 'Author verify_candidate.py writes two literal30 fields; it does not derive the factor from reference or a behavior model.'
env = fixed_json(C,EV+'environment-snapshot.json')
mechanical['environment_ref_checks'] = [{'expression':expr,'declared':value,
    'observed':git('rev-parse',PREP if expr=='HEAD' else PREP+'^{tree}' if expr=='HEAD^{tree}' else expr).decode().strip()}
    for expr,value in env['refs'].items()]
dump('independent-mechanical-validation.json',mechanical)

ranges = {'candidate-manifest.json':[(1,122)],'input-identities.json':[(1,300),(301,600),(601,763)],
          'contract-payload-checks.json':[(1,280),(281,560),(561,840),(841,1136)],
          'counter-packet-identities.json':[(1,126)],'environment-snapshot.json':[(1,31)],
          'tool-validation.json':[(1,88)],'verify_candidate.py':[(1,149)],'bind_history.py':[(1,91)],
          'read_unit.py':[(1,38)],'edit_candidate.py':[(1,44),(45,88),(89,129)]}
readings=[]
for name, intervals in ranges.items():
    data,value=fixed(C,EV+name);lines=data.splitlines(keepends=True)
    for start,end in intervals:
        body=b''.join(lines[start-1:end])
        readings.append({'commit':C,'tree':TREE,'path':EV+name,**ident(data),'file_lines':len(lines),
                         'start_line':start,'end_line':end,'segment_bytes':len(body),
                         'segment_sha256':hashlib.sha256(body).hexdigest(),
                         'presentation':'Full nontruncated tool transcript; edit_candidate.py displayed with nl -ba, scripts with line-numbered Python display, JSON with plain sed/full display',
                         'initial_presentation_utc':'NOT_RECONSTRUCTED',
                         'identity_receipt_utc':UTC,'cwd':str(REPO),'fully_read_attestation':True,
                         'content_boundary':'Reviewer byte identity/script capability reading; no8ID semantic adjudication'})
ag,value=fixed(PREP,'AGENTS.md')
readings.insert(0,{'commit':PREP,'path':'AGENTS.md',**ident(ag),'file_lines':len(ag.splitlines()),
                   'start_line':1,'end_line':len(ag.splitlines()),'segment_bytes':len(ag),
                   'segment_sha256':hashlib.sha256(ag).hexdigest(),'initial_presentation_utc':'NOT_RECONSTRUCTED',
                   'identity_receipt_utc':UTC,'cwd':str(REPO),'fully_read_attestation':True,'presentation':'cat AGENTS.md, full nontruncated tool transcript'})
dump('reviewer-segment-reading-ledger.json',readings)
dump('audit-command-receipts.json',commands)
summary={'snapshot':snapshot,'payload_count':len(payloads),'mirror_count':sum('/mirror/' in r['path'] for r in payloads),
         'evidence_count':sum('/evidence/' in r['path'] for r in payloads),'all23_payloads_regular100644_blob':all(r['mode']=='100644' and r['type']=='blob' and r['workspace_regular_file'] for r in payloads),
         'all23_workspace_byte_equal':all(r['workspace_byte_equal'] for r in payloads),
         'baseline_bindings_all_match':all(all(r[k] for k in r if k.endswith('_matches') or k.startswith('prepare_') and k.endswith('_main') or k=='candidate_formal_equals_fixed_main') for r in baselines),
         'input_declaration_count':len(declarations),'input_declarations_all_match':all(r['matches'] is True for r in declarations),
         'contract_payload_count':len(payload_checks),'reading_ledger_entries':len(ledger_checks),
         'reading_ledger_mechanical_all_match':all(r['matches'] is True for r in ledger_checks),
         'required_reading_coverage_no_gap':all(r['uncovered_lines']==0 for r in coverage_checks),
         'history_navigation_count':len(nav_checks),'historical_unavailable_or_mismatch_errors':errors,
         'reviewer_full_read_segments':len(readings),'semantic_8ID_review':False,
         'actual_configuration':snapshot['actual_configuration']}
dump('audit-summary.json',summary)
print(json.dumps({k:v for k,v in summary.items() if k not in ['snapshot','historical_unavailable_or_mismatch_errors']},ensure_ascii=False))
print(json.dumps({'historical_errors':len(errors),'out':str(OUT)},ensure_ascii=False))
