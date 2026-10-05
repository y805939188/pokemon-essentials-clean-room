#!/usr/bin/env python3
"""Read-only Git/document/hash checks for this bounded review.

No reference program, old verifier, behavioral vector, or simulator is executed.
Semantic dispositions are human findings in report.md, not script assertions.
"""
import collections
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
REFROOT = Path('/tmp/R-B14-affected-B06-reference')
B09 = '1e6b11a47370f1c7c4659a32443fc1afda597bac'
C1 = '47f7514765f8569ae9172bb06a2cd615e2b83b8a'
C2 = 'af39efbf32549be964cb083bd49bed6d1d5c0d2a'
OLD = 'c67f400c000df4fd73ab1440e1487a3d534336aa'
OLDREPORT = '98e418ef1d9f99db999e5c0ec25118eacfe0601c'
ORIGINAL = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BATCHES = 'review/remediation/20261003-prepare/batches/'
AUTHOR = BATCHES + 'B14/candidate-2/'
OLDPATH = BATCHES + 'B06/integration-review-1/'
ENGINE = 'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'
POKEMON = 'deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
OPTIONS = ['--no-ext-diff', '--no-textconv', '--no-color', '--no-renames',
           '--binary', '--full-index', '--unified=3']
checks = []


def git(*args, ref=False):
    return subprocess.check_output(['git', '-C', str(REFROOT if ref else ROOT), *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


def data(commit, path, ref=False):
    return git('show', commit + ':' + path, ref=ref)


def obj(commit, path):
    return json.loads(data(commit, path))


def identity(commit, path, ref=False):
    raw = data(commit, path, ref)
    return {'commit': commit, 'path': path,
            'git_blob': git('rev-parse', commit + ':' + path, ref=ref).decode().strip(),
            'sha256': sha(raw), 'bytes': len(raw)}


def check(label, value):
    if not value:
        raise AssertionError(label)
    checks.append({'check': label, 'result': 'PASS'})


def matches(record, commit, path=None, ref=False):
    p = path or record['path']
    actual = identity(commit, p, ref)
    for key in ('git_blob', 'sha256', 'bytes'):
        check(f'identity:{commit}:{p}:{key}', actual[key] == record[key])
    return actual


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def canonical_sha(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(',', ':')).encode())


def statuses(base, target):
    fields = git('diff', '--no-ext-diff', '--no-textconv', '--no-renames',
                 '--name-status', '-z', base, target).decode().split('\0')[:-1]
    return [{'change': fields[i], 'path': fields[i+1]} for i in range(0, len(fields), 2)]


expected_trees = {B09: '18433d8e75ec0cddbd3227ae7e63c9d49590e375',
                  C1: 'd1203c2c6a0177fb66b89acf5c7ba1cfbc511aeb',
                  C2: '932ffac11a2701ddb432516e7bd07aa990fd326f'}
git_objects = []
for c, tree in expected_trees.items():
    actual_tree = git('rev-parse', c + '^{tree}').decode().strip()
    parents = git('show', '-s', '--format=%P', c).decode().strip().split()
    check('tree:' + c, actual_tree == tree)
    git_objects.append({'commit': c, 'tree': actual_tree, 'parents': parents})
check('candidate2 parent is candidate1', git_objects[2]['parents'] == [C1])
subprocess.run(['git', '-C', str(ROOT), 'merge-base', '--is-ancestor', B09, C1], check=True)
check('accepted predecessor is ancestor of candidate1', True)

contract_path = BATCHES + 'B09/acceptance-stage-1/B14-downstream-contract.json'
contract = obj(B09, contract_path)
gate = next(x for x in contract['accepted_reverse_review_gates'] if x['accepted_batch'] == 'B06')
package_path = BATCHES + 'B14/candidate-1/reverse-impact-packages.json'
package = next(x for x in obj(C2, package_path)['accepted_owner_packages'] if x['accepted_owner'] == 'B06')
check('B06 package exact accepted gate', package['contract_gate'] == gate)
check('B06 package requests independent candidate and later actual',
      package['author_NOT_AFFECTED_assertion'] is False and
      gate['independent_exact_impact_disposition_required'] is True and
      package['candidate_gate']['status'] == 'PENDING' and
      package['actual_gate']['status'] == 'PENDING_FUTURE_PUBLIC_INTEGRATION')
planned = []
check('72 accepted planned-read identities', len(contract['planned_reads']) == 72)
for row in contract['planned_reads']:
    r = row['accepted_current_input']
    c = r.get('commit', B09)
    planned.append(matches(r, c, row['path']))
for row in contract['allowed_write_input_identities']:
    matches(row, B09)
for row in contract['whole_catalog_locks']:
    matches(row['baseline'], B09, row['path'])
for row in gate['changed_planned_reverse_readers']:
    matches(row['current_baseline'], B09, row['path'])
for dep in contract['dependency_baselines']:
    check('only accepted dependency receipt:' + dep['batch'], bool(dep['actual']) and bool(dep['independent_actual_report']))
matches(contract['fixed_original_findings'], ORIGINAL)
matches(contract['fixed_approved_acceptance'], PLAN)
check('AGENTS unchanged', data(B09, 'AGENTS.md') == data(C2, 'AGENTS.md'))

findings = obj(ORIGINAL, 'review/global-independent-review/2026-10-03-fd82a639/findings.json')
acceptance = obj(PLAN, 'review/remediation-20261003-prepare/finding-acceptance.json')
original_c103 = next(x for x in findings if x['id'] == 'GIR-FD82-C103')
control = next(x for x in contract['contribution_controls'] if x['id'] == 'GIR-FD82-C103')
stored = json.loads((OUT / 'C103-complete-controls.json').read_text())
check('complete C103 original fixed object', stored['original_complete_object'] == original_c103)
check('complete C103 acceptance fixed object', stored['approved_complete_object'] == acceptance['GIR-FD82-C103'])
check('C103 original canonical object hash', canonical_sha(original_c103) == control['whole_original_object_sha256'])
check('C103 acceptance canonical object hash', canonical_sha(acceptance['GIR-FD82-C103']) == control['whole_acceptance_object_sha256'])
for key, value in control['complete_current_control_fields'].items():
    check('C103 complete current control:' + key, original_c103.get(key) == value)
protected_c003 = json.loads((OUT / 'C003-complete-protection-controls.json').read_text())
check('C003 fixed original protection object', protected_c003['original'] == next(x for x in findings if x['id'] == 'GIR-FD82-C003'))
check('C003 fixed acceptance protection object', protected_c003['acceptance'] == acceptance['GIR-FD82-C003'])
ancillary = json.loads((OUT / 'ancillary-current-controls.json').read_text())
for row in ancillary['controls']:
    id = row['id']
    source = next(x for x in findings if x['id'] == id)
    ac = next(x for x in contract['contribution_controls'] if x['id'] == id)
    check('ancillary complete fixed original:' + id, row['original_complete_object'] == source)
    check('ancillary complete fixed acceptance:' + id, row['acceptance_complete_object'] == acceptance[id])
    check('ancillary contract original object hash:' + id, canonical_sha(source) == ac['whole_original_object_sha256'])
    check('ancillary contract acceptance object hash:' + id, canonical_sha(acceptance[id]) == ac['whole_acceptance_object_sha256'])
required = [x for x in findings if x.get('required_revision')]
check('229 fixed required IDs retain unresolved dispositions', len(required) == 229 and
      all(x['status'] in ('CONFIRMED_REQUIRED_REVISION', 'PARTIALLY_ADDRESSED_RESIDUAL_OPEN') for x in required))
check('no fixed canonical ID closed', all('CLOSED' not in x['status'] for x in required))

revised = obj(C2, AUTHOR + 'revised-identities.json')
check('candidate2 revised baselines exact', revised['candidate1'] == C1 and revised['accepted_predecessor'] == B09)
formal = {x['path'] for x in revised['documents']}
check('12 cumulative formal paths', len(formal) == 12)
check('five originals seven final paths', sum(x.startswith('specs/') for x in formal) == 5 and sum(x.startswith('deliverables/') for x in formal) == 7)
revised_checks = []
for row in revised['documents']:
    p = row['path']
    matches(row['accepted_B09_before'], B09, p)
    matches(row['candidate1_before'], C1, p)
    actual = matches(row['after'], C2, p)
    changed = data(C1, p) != data(C2, p)
    check('changed_in_candidate2:' + p, row['changed_in_candidate2'] == changed)
    revised_checks.append({**actual, 'changed_from_candidate1': changed})
changed_formal = {x['path'] for x in revised_checks if x['changed_from_candidate1']}
check('eight amended formal paths', len(changed_formal) == 8)
full_diff_metadata = json.loads((OUT / 'full-diff-identities.json').read_text())
inventories = []
for row in full_diff_metadata['diffs']:
    base, target = row['base'], row['target']
    raw = git('diff', *OPTIONS, base, target)
    check('unfiltered diff exact archived:' + base, raw == (ROOT / row['path']).read_bytes())
    check('unfiltered diff hash bytes:' + base, sha(raw) == row['sha256'] and len(raw) == row['bytes'])
    items = statuses(base, target)
    check('full unfiltered path inventory:' + base, items == row['complete_path_statuses'])
    modified = {x['path'] for x in items if x['change'] == 'M'}
    added = [x['path'] for x in items if x['change'] == 'A']
    check('only declared formal modifications:' + base, modified == (formal if base == B09 else changed_formal))
    check('only new B14 author evidence additions:' + base,
          len(items) == len(modified) + len(added) and
          all(any(p.startswith(BATCHES + 'B14/' + d + '/') for d in
                  (('scope-proposal-1','author-stage-1','candidate-1','candidate-2') if base == B09 else ('candidate-2',))) for p in added))
    check('exact path counts:' + base, (len(items), len(modified), len(added)) == ((46, 12, 34) if base == B09 else (22, 8, 14)))
    inventories.append({'base': base, 'target': target, 'paths': items, 'modified_count': len(modified), 'added_count': len(added)})
historical = git('ls-tree', '-r', '--name-only', C1, BATCHES + 'B14/').decode().splitlines()
check('20 prior B14 author materials', len(historical) == 20)
for p in historical:
    check('historical B14 bytes preserved:' + p, data(C1, p) == data(C2, p))

amend = obj(C2, AUTHOR + 'bounded-amendment-1.json')
applied = obj(C2, AUTHOR + 'amendment-application.json')
check('bounded amendments five paths', len(amend['documents']) == len(applied['documents']) == 5)
amend_checks = []
for row in amend['documents']:
    p = row['path']
    matches(row['before'], C1, p)
    actual = matches(row['intended_after'], C2, p)
    patch = data(C2, AUTHOR + row['patch'])
    computed_patch = ''.join(difflib.unified_diff(data(C1, p).decode().splitlines(True),
                      data(C2, p).decode().splitlines(True), fromfile='a/' + p, tofile='b/' + p, n=3)).encode()
    check('bounded exact amendment patch:' + p, patch == computed_patch and sha(patch) == row['patch_sha256'])
    app = next(x for x in applied['documents'] if x['path'] == p)
    matches(app['actual_after'], C2, p)
    check('application hash and intended-after agreement:' + p, app['patch_sha256'] == sha(patch))
    before, after = data(C1, p), data(C2, p)
    if 'wp16-' in p:
        a, b = before.splitlines(True), after.splitlines(True)
        differences = [i for i in range(len(a)) if a[i] != b[i]] if len(a) == len(b) else []
        check('WP16 only one line amended:' + p, len(differences) == 1)
        check('WP16 surrounding Snow sentence preserved:' + p,
              a[differences[0]].split('Snow'.encode())[1] == b[differences[0]].split('Snow'.encode())[1])
    elif 'wp60-berry-plants' in p:
        def outside_section(raw):
            start = raw.index(b'### 5.2')
            end = raw.index(b'### 5.3', start)
            return raw[:start], raw[end:]
        check('berry amendment only section5.2:' + p, outside_section(before) == outside_section(after))
    amend_checks.append({**actual, 'finding_id': row['finding_id'], 'patch_sha256': sha(patch), 'scope_record': row['bounded_scope']})
fly_original = 'specs/overworld/wp59-world-time-weather-field-moves.md'
fly_patch = data(C2, AUTHOR + 'original-FLY-amendment.patch')
default_diff = git('diff', '--no-ext-diff', '--no-textconv', '--no-color', '--no-renames', C1, C2, '--', fly_original)
check('FLY original exact patch', fly_patch == default_diff and sha(fly_patch) == revised['original_FLY_patch_sha256'])

row_cache = {}


def rows(commit, path):
    key = commit, path
    if key not in row_cache:
        found = []
        for n, line in enumerate(data(commit, path).splitlines(True), 1):
            m = re.match(rb'^\|\s+([A-Z][A-Z0-9-]*[0-9])\s+\|', line)
            if m:
                found.append((m[1].decode(), n, line))
        check('unique static row IDs:' + commit + ':' + path, len(found) == len({x[0] for x in found}))
        row_cache[key] = found
    return row_cache[key]


catalogs = []
expected_changed = {
    ENGINE: ['WT03','WT07','WT09','WT14','WT15','WT17','WT18','WT20','WT23','WT25','FS02','FS03','FS06'],
    POKEMON: ['FP01','FP02','FP06','FP12','FP14','FP15']}
for p in (ENGINE, POKEMON):
    sets = {c: rows(c, p) for c in (B09, C1, C2)}
    inventory = {}
    for c, rr in sets.items():
        inventory[c] = {'row_count': len(rr), 'ID_order': [x[0] for x in rr],
                        'families': dict(collections.Counter(re.sub(r'\d.*$', '', x[0]) for x in rr))}
    transitions = []
    for base in (B09, C1):
        old_ids = [x[0] for x in sets[base]]
        oldmap = {x[0]: x[2] for x in sets[base]}
        newmap = {x[0]: x[2] for x in sets[C2]}
        check('all old catalog IDs ordered with multiplicity:' + base + ':' + p,
              [x[0] for x in sets[C2] if x[0] in oldmap] == old_ids)
        changed = [i for i in old_ids if oldmap[i] != newmap[i]]
        expected = expected_changed[p] if base == B09 else (['WT28'] if p == ENGINE else ['BP18'])
        check('exact changed old catalog rows:' + base + ':' + p, set(changed) == set(expected))
        added = [x[0] for x in sets[C2] if x[0] not in oldmap]
        expected_added = ([f'WT{i:02d}' for i in range(26,41)] + ['FS16','FS17','FS18'] if p == ENGINE else ['BP18','BP19','BP20','FP32','FP33','FP34','FP35']) if base == B09 else (['WT39','WT40'] if p == ENGINE else [])
        check('exact added catalog IDs:' + base + ':' + p, added == expected_added)
        unchanged = [{'id':i, 'sha256':sha(oldmap[i])} for i in old_ids if i not in changed]
        transitions.append({'base':base, 'target':C2, 'changed_old_IDs':changed,
                            'added_IDs':added, 'preserved_old_rows':unchanged})
    protected = [(i,n,v) for i,n,v in sets[B09] if not i.startswith(('WT','FS') if p == ENGINE else ('BP','FP'))]
    newmap = {x[0]:x[2] for x in sets[C2]}
    check('all unrelated shared catalog row bytes:' + p, all(newmap[i] == v for i,n,v in protected))
    check('unrelated shared catalog row count:' + p, len(protected) == (299 if p == ENGINE else 93))
    if p == ENGINE:
        b03 = [x for x in protected if x[0].startswith(('MP','MV','EV','FW','IM','MR','DG'))]
        b04 = [x for x in protected if x[0].startswith(('RS','B04-R'))]
        check('B03 protected 251 rows', len(b03) == 251)
        check('B04 protected RS20 plus B04-R28', len(b04) == 48)
    catalogs.append({'path':p,'inventory':inventory,'transitions':transitions,
                     'unrelated_owner_rows_preserved':len(protected)})
check('shared catalog counts480/503/505', [sum(x['inventory'][c]['row_count'] for x in catalogs) for c in (B09,C1,C2)] == [480,503,505])

old_acceptance = obj(B09, BATCHES + 'B06/acceptance-stage-1/acceptance-manifest.json')
check('B06 accepted actual/report bindings', old_acceptance['reviewed_integration_commit'] == OLD and old_acceptance['integration_report_commit'] == OLDREPORT)
check('B06 prior independent actual report parent', git('show','-s','--format=%P',OLDREPORT).decode().strip() == OLD)
formal_preserved = []
for row in old_acceptance['accepted_formal_identities']:
    matches(row, OLD)
    p = row['path']
    check('B06 formal path unchanged B09 to candidate2:' + p, data(B09,p) == data(C2,p))
    formal_preserved.append({'path':p,'B09':identity(B09,p),'candidate2':identity(C2,p),
                             'entire_old_actual_blob_preserved':data(OLD,p)==data(C2,p)})
old_dispositions = obj(OLDREPORT, OLDPATH + 'finding-contribution-dispositions.json')
clause_checks = []
for f in old_dispositions['findings']:
    for clause in f['formal_clause_bindings']:
        lo, hi = clause['lines']
        p = clause['path']
        bound = b''.join(data(C2,p).splitlines(True)[lo-1:hi])
        check('B06 old accepted clause freshly bound:' + f['id'] + ':' + p + ':' + str(lo), sha(bound) == clause['range_sha256'])
        clause_checks.append({'finding_id':f['id'], 'path':p,'lines':[lo,hi],'candidate2_range_sha256':sha(bound)})
old_rows = obj(OLDREPORT, OLDPATH + 'all60-actual-static-rows.json')['rows']
check('60 old B06 allocated rows',len(old_rows)==60)
preserved_rows = []
for row in old_rows:
    p, tid = row['path'], row['test_id']
    matching = [x for x in rows(C2,p) if x[0]==tid]
    check('B06 allocated row hash:' + tid,len(matching)==1 and sha(matching[0][2])==row['sha256'])
    preserved_rows.append({**row,'candidate2':C2,'current_line':matching[0][1],'current_sha256':sha(matching[0][2])})

fix = obj(C2, AUTHOR + 'fix-response.json')
review_input_checks = [matches(r,r['commit']) for r in fix['review_inputs']]
matches(applied['before_application_record'], C2)
matches(revised['earlier_original_application'], C1)
matches(fix['source_limits_inherited'], C1)
for trace in fix['successor_local_traceability']:
    if 'old_entry' in trace:
        old_entry = trace['old_entry']
        if isinstance(old_entry,dict) and 'sha256' in old_entry and 'path' in old_entry:
            matches(old_entry, old_entry.get('commit',C1))
limits = obj(C2,BATCHES+'B14/candidate-1/source-limits.json')
limits_identity = limits['contract_source_limits']['complete_limits_file']
matches(limits_identity,limits_identity['commit'])
matches(limits['contract_source_limits']['scope_statement'],B09)
source_log = obj(C2,AUTHOR+'source-reading-log.json')
author_source_checks = []
for record in source_log['own_source_reads']:
    actual = matches(record,REF,ref=True)
    count = len(data(REF,record['path'],True).splitlines(True))
    check('author source navigation range in bounds:' + record['path'], all(1 <= lo <= hi <= count for lo,hi in record['own_text_ranges']))
    author_source_checks.append({**actual,'author_ranges_in_bounds':record['own_text_ranges'],
                                 'meaning':'Metadata verification only; no claim of independently reading these entire author spans.'})

own_read_spans = {
 'Data/Scripts/012_Overworld/001_Overworld.rb':[(125,187)],
 'Data/Scripts/015_Trainers and player/004_Player.rb':[(98,103)],
 'Data/Scripts/013_Items/008_PokemonBag.rb':[(45,72),(237,253)],
 'Data/Scripts/001_Settings.rb':[(55,55)],
 'PBS/items.txt':[(6326,6333)],
 'Data/Scripts/004_Game classes/004_Game_Map.rb':[(421,427)],
 'Data/Scripts/004_Game classes/006_Game_Character.rb':[(417,455),(893,992)],
 'Data/Scripts/004_Game classes/008_Game_Player.rb':[(416,439),(460,503),(543,576)],
 'Data/Scripts/012_Overworld/002_Overworld_Metadata.rb':[(116,127)],
 'Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb':[(42,67)],
 'Data/Scripts/003_Game processing/005_Event_Handlers.rb':[(1,99)],
 'Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb':[(471,515)],
 'Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb':[(1,175),(231,305)],
 'Data/Scripts/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb':[(210,226),(239,313)],
 'Data/Scripts/007_Objects and windows/002_MessageConfig.rb':[(552,606)],
 'Data/Scripts/012_Overworld/001_Overworld visuals/002_Overworld_Overlays.rb':[(1,45)],
 'Data/Scripts/004_Game classes/012_Game_Stats.rb':[(45,51),(129,134)],
 'Data/Scripts/019_Utilities/003_Utilities_BattleAudio.rb':[(104,149)],
 'Data/Scripts/010_Data/002_PBS data/007_BerryPlant.rb':[(1,30)],
 'Data/Scripts/012_Overworld/003_Overworld_Time.rb':[(1,14)],
 'Data/Scripts/013_Items/002_Item_Effects.rb':[(345,362)],
 'Data/Scripts/016_UI/001_UI_PauseMenu.rb':[(207,239)]}
own_reads = []
for p, ranges in own_read_spans.items():
    raw = data(REF,p,True)
    lines = raw.splitlines(True)
    check('own source read bounds:' + p, all(1 <= lo <= hi <= len(lines) for lo,hi in ranges))
    own_reads.append({**identity(REF,p,True),'line_count':len(lines),
                     'fresh_human_read_ranges':[{'start':lo,'end':hi,'range_sha256':sha(b''.join(lines[lo-1:hi]))} for lo,hi in ranges]})
check('independent reference fixed SHA',git('rev-parse','HEAD',ref=True).decode().strip()==REF)
check('independent reference fixed tree',git('rev-parse','HEAD^{tree}',ref=True).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0')
check('independent reference clean',git('status','--porcelain=v1','--untracked-files=all',ref=True)==b'')

# These are human-read document excerpts. Hashing does not evaluate their behavior.
document_spans = {
 'specs/creature-rpg/wp24-player-trainers-partners.md':[(95,101)],
 'deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md':[(91,104),(167,190)],
 'specs/creature-rpg/wp27-bag-and-item-storage.md':[(45,52)],
 'deliverables/final-specification-set/creature-rpg/wp27-bag-and-item-storage.md':[(47,54)],
 'specs/pokemon-rules/wp61-field-passive-effects-and-blackout.md':[(45,53),(55,65)],
 'deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md':[(24,44)],
 'specs/overworld/wp59-world-time-weather-field-moves.md':[(275,287)],
 'deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md':[(251,262)],
 'specs/pokemon-rules/wp60-berry-plants.md':[(98,109)],
 'deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md':[(72,83)],
 'specs/overworld/wp16-world-rendering-and-visual-transitions.md':[(185,185)],
 'deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md':[(162,162)]}
document_bindings = []
for p, ranges in document_spans.items():
    raw = data(C2,p)
    ll = raw.splitlines(True)
    check('current document range in bounds:' + p, all(1 <= lo <= hi <= len(ll) for lo,hi in ranges))
    document_bindings.append({**identity(C2,p),'human_read_ranges':[
        {'start':lo,'end':hi,'range_sha256':sha(b''.join(ll[lo-1:hi]))} for lo,hi in ranges]})
def marked_line(path, marker):
    found = [line for line in data(C2,path).decode().splitlines(True) if line.startswith(marker)]
    check('paired marker unique:' + path + ':' + marker,len(found)==1)
    return found[0]
paired = [
 ('specs/pokemon-rules/wp61-field-passive-effects-and-blackout.md',
  'deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md',
  ['**完成移动的组合调用','**煤烟状态与收集门分开']),
 ('specs/pokemon-rules/wp60-berry-plants.md',
  'deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md',
  ['- **公共写入顺序的静态对照']),
 ('specs/overworld/wp59-world-time-weather-field-moves.md',
  'deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md',
  ['**FLY 可选回调的成对静态对照','反向同一输入仅改为无可选回调']),
 ('specs/overworld/wp16-world-rendering-and-visual-transitions.md',
  'deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md',
  ['Rain类别从0起'])]
for original, final, markers in paired:
    for marker in markers:
        check('selected original/final paired semantics text:' + marker,
              marked_line(original,marker)==marked_line(final,marker))
affected_static_rows = []
for p, ids in [(ENGINE,['MP27','WT28','WT31','WT32','WT36','WT39','WT40']),
               (POKEMON,['BP18','FP01','FP02','FP32','FP33'])]:
    for tid,n,line in rows(C2,p):
        if tid in ids:
            affected_static_rows.append({'path':p,'test_id':tid,'line':n,'sha256':sha(line),
                                        'text':line.decode().rstrip('\n'),'executed':False})
lock = json.loads((OUT/'first-evidence-lock.json').read_text())
first = (OUT/'independent-first-evidence.md').read_bytes()
check('first-evidence lock bytes unchanged',sha(first)==lock['sha256'] and len(first)==lock['bytes'])
write('current-affected-document-bindings.json',{'candidate2':C2,'human_document_ranges':document_bindings,
    'affected_static_rows':affected_static_rows,'meaning':'Human static comparison; no executed behavior.'})

write('independent-source-reading.json', {
    'candidate2':C2, 'reference_commit':REF, 'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0',
    'reference_path':str(REFROOT),'clean_checked':True,'fresh_readings':own_reads,
    'meaning':'Human static text reading spans in this review; range hashing is document bookkeeping, not behavioral coverage.',
    'author_source_metadata_crosscheck':author_source_checks,'reference_execution':0,
    'behavior_vectors_executed':0,'runtime_observations':0,'proven_Demo_chains':0})
write('catalog-and-B06-protection.json',{'candidate2':C2,'shared_catalogs':catalogs,
    'B06_formal_paths_unchanged_from_B09':formal_preserved,'B06_current_clause_bindings':clause_checks,
    'B06_all60_preserved_rows':preserved_rows,'static_rows_executed':0})
write('independent-identity-checks.json',{'candidate2':C2,'Git_objects':git_objects,
    'contract':identity(B09,contract_path),'B06_accepted_gate':gate,'B06_candidate_package':package,
    'accepted_dependency_receipts':contract['dependency_baselines'],
    '72_planned_read_metadata':planned,'revised12_formal_identities':revised_checks,
    'complete_unfiltered_inventories':inventories,'exact_five_amendments':amend_checks,
    'six_prior_review_input_metadata':review_input_checks,
    'amendment_authorization':'Narrow parent authorization supplied in delegation; content scope verified. Same-commit records do not independently certify before-application chronology or cross-container lease.',
    'limits_identity':limits_identity,'own_checks':checks,'failed_checks':0,
    'meaning':'Own read-only Git/text/hash bookkeeping; semantic PASS_SCOPED is the human report, not these assertions.',
    'old_verifier_execution':0,'reference_program_execution':0,'behavior_simulation':0})
print(json.dumps({'document_identity_checks_passed':len(checks),'failed':0,
                  'formal_paths':12,'candidate2_formal_changes':8,
                  'B06_preserved_rows':60,'shared_catalog_row_counts':[480,503,505],
                  'reference_files_fresh_human_read':len(own_reads),
                  'behavior_vectors_executed':0,'runtime_observations':0},ensure_ascii=False))
