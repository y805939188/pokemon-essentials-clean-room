import collections
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

parser=argparse.ArgumentParser(description='New read-only B16 exact Git/JSON/bytes metadata check; never runs game/source/old programs.')
parser.add_argument('--repo', default='/workspace/pokemon-essentials-clean-room')
parser.add_argument('--reference-git', default='/tmp/b16-reference.git')
parser.add_argument('--scratch-dir', default='/tmp/b16-affected-review')
args=parser.parse_args()
REPO = args.repo
REF = args.reference_git
OUT = Path(args.scratch_dir)
OUT.mkdir(parents=True,exist_ok=True)
BASE = '27185563f307e16d2612fa86e83b2c9bd772c79e'
CANDIDATE = 'ae223d7bfb9ff6ed8a1ac153debb986115345957'
PUBLICATION = '5c70c6945ede498f1d7d59592da1d37a96c07a98'
PACKET = '8e2753430ccb4bad8098048c814576aa386a09ef'
PREFIX = 'review/remediation/20261003-prepare/batches/B16/'

def git(*args, repo=REPO):
    return subprocess.check_output(['git', *args], cwd=repo)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def canon(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()

cache = {}
identities = {}
def read(commit, path, repo=REPO):
    key = (repo, commit, path)
    if key not in cache:
        cache[key] = git('show', commit + ':' + path, repo=repo)
    return cache[key]

def identity(commit, path, repo=REPO):
    data = read(commit, path, repo)
    return dict(commit=commit, path=path,
                git_blob=git('rev-parse', commit + ':' + path, repo=repo).decode().strip(),
                sha256=sha(data), bytes=len(data))

def verify(a, default_commit=None, repo=REPO):
    actual = identity(a.get('commit', default_commit), a['path'], repo)
    for k in ('git_blob', 'sha256', 'bytes'):
        if k in a:
            assert actual[k] == a[k], (a['path'], k, actual[k], a[k])
    identities[(repo, actual['commit'], actual['path'])] = actual
    return actual

def pointer(obj, p):
    for part in p.split('/')[1:]:
        part = part.replace('~1', '/').replace('~0', '~')
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj

def load(name):
    packet=PREFIX+'refreeze-after-B13-C-1/'
    candidate=PREFIX+'candidate-1/complete-after-original-scope-3/'
    author=PREFIX+'author-draft-1/'
    locations={
        'dispatch':(PUBLICATION,author+'original-sync-3/affected-review-dispatch.json'),
        'manifest':(CANDIDATE,candidate+'manifest.json'),
        'navigation':(CANDIDATE,candidate+'affected-interface-navigation.json'),
        'contract':(PACKET,packet+'B16-downstream-contract.json'),
        'controls':(PACKET,packet+'original-and-acceptance-controls.json'),
        'effective':(PACKET,packet+'effective-case-constraints.json'),
        'scope':('bd14b2170085fdb491c01f633c9e9d794c723c3c',PREFIX+'original-scope-approval-3/scope-receipt.json'),
        'trace':('2c2b11e03e24155b5eda8508ec8172c5912156cf',author+'traceability.json'),
        'trace-completion':(CANDIDATE,candidate+'traceability-completion.json'),
        'catalog-preservation':(CANDIDATE,author+'catalog-preservation.json'),
        'source-reading-supplement':(CANDIDATE,author+'source-reading-supplement.json'),
    }
    commit,path=locations[name]
    return json.loads(read(commit,path))

d, m, nav, c, controls, effective, scope = [load(x) for x in
    ('dispatch','manifest','navigation','contract','controls','effective','scope')]
assert git('rev-parse', CANDIDATE + '^{tree}').decode().strip() == '7b3a16f86aea8438eceb007436687b72aced8e74'
assert git('rev-parse', BASE + '^{tree}').decode().strip() == 'e44ed01586846bb42b03105dcc575d463df4ef49'
assert git('rev-parse', '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b^{tree}', repo=REF).decode().strip() == '7589c800b61ba13a13040ed0d686979b80a84fd0'
assert d['candidate_commit'] == CANDIDATE and d['candidate_tree'] == '7b3a16f86aea8438eceb007436687b72aced8e74'

# Read all exact contract inputs as bytes. No referenced program is executed.
for r in c['planned_reads']:
    verify(r['input'])
for k in ('approved_PLAN','original_batch_contract','fixed_original_findings','fixed_approved_acceptance'):
    verify(c[k])
for obj in (d, m):
    for a in obj.values():
        if isinstance(a, dict) and {'commit','path','git_blob','sha256','bytes'} <= a.keys():
            verify(a)

ctrls = controls['controls']
assert c['contribution_controls'] == ctrls
assert [r['exact_current_navigation'] for r in nav['owners']] == c['accepted_interface_impact_map']['potential_interfaces']
assert len(ctrls) == 24 and sum(r['primary'] for r in ctrls) == 20
assert [r['id'] for r in ctrls] == m['contribution_ids'] == c['contribution_finding_ids']
assert [r['id'] for r in ctrls if r['primary']] == m['primary_ids'] == c['primary_finding_ids']
control_checks = []
for r in ctrls:
    for binding, field, hashfield in (
        ('whole_original_object_binding','whole_original_object','whole_original_object_sha256'),
        ('whole_approved_acceptance_binding','whole_approved_acceptance_object','whole_acceptance_object_sha256')):
        a = r[binding]
        verify(a)
        exact = pointer(json.loads(read(a['commit'], a['path'])), a['pointer'])
        assert exact == r[field] and sha(canon(exact)) == r[hashfield], (r['id'],field)
    current = r['complete_current_control_fields']
    tr = next(x for x in load('trace')['trace'] if x['id'] == r['id'])
    assert tr['current_qualified_controls_full'] == current
    assert tr['whole_original_object'] == r['whole_original_object_binding']
    assert tr['whole_approved_acceptance_object'] == r['whole_approved_acceptance_binding']
    completed = next(x for x in load('trace-completion')['rows'] if x['id'] == r['id'])
    a = completed['complete_local_body_appendix_catalog_source_reverse_regression_evidence']
    verify(a)
    assert pointer(json.loads(read(a['commit'],a['path'])), a['pointer']) == tr
    control_checks.append(dict(id=r['id'], primary=r['primary'], primary_owner=r['primary_owner'],
        whole_original_object_sha256=r['whole_original_object_sha256'],
        whole_acceptance_object_sha256=r['whole_acceptance_object_sha256'],
        current_control_sha256=sha(canon(current)),
        current_field_names=list(current),
        root_adjudications=len(current.get('root_adjudications',[])),
        extensions=len(current.get('extensions',[])),
        extension_decisions=len(current.get('extension_decisions',[])),
        accepted_contributors=r['accepted_contributors'], pending_contributors=r['pending_contributors']))

effective_checks = []
assert len(effective['full_exact_values']) == 12
for r in effective['full_exact_values']:
    assert sha(canon(r['aggregate'])) == r['canonical_json_sha256'], r['id']
    control = next(x for x in ctrls if x['id'] == r['id'])
    assert control['complete_current_control_fields']['effective_case_constraints'] == r['aggregate'], r['id']
    # Verify exact fixed-version prior objects, not only the author equality flag.
    for k in ('prior_complete_packet','prior_preparation'):
        a = r[k]
        verify(a)
        assert pointer(json.loads(read(a['commit'],a['path'])),a['pointer']) == r['aggregate'], (r['id'],k)
    effective_checks.append(dict(id=r['id'], sha256=r['canonical_json_sha256'], exact_equal=True))

# Exact 11 payload identities and the five original grants; no patch is executed.
payloads = []
assert len(m['outputs']) == 11
for o in m['outputs']:
    before = verify(o['before'])
    after = verify(dict(o['after'], commit=CANDIDATE, path=o['path']))
    payloads.append(dict(path=o['path'], kind=o['kind'], before=before, after=after))
assert len([r for r in payloads if r['path'].startswith('specs/')]) == 5
scope_checks=[]
for r in scope['granted_files']:
    for k in ('current_before','before_snapshot_reuse','complete_combined_patch','complete_proposed_after','scope_request_file'):
        verify(r[k])
    before=r['current_before']; after=r['complete_proposed_after']
    assert read(BASE,r['path']) == read(before['commit'],before['path'])
    assert read(CANDIDATE,r['path']) == read(after['commit'],after['path'])
    scope_checks.append(dict(path=r['path'], exact_before_and_after_equal=True,
        qualified_ids=r['qualified_ids'], scope_only=True))

# Whole, unfiltered stream first; subsequent path/row checks are derived from it.
stream = git('diff','--binary',BASE,CANDIDATE)
assert len(stream) == 2248505 and sha(stream) == 'f8012172e5751ba620d9ddd37793382f9128973ba2331fef187575adbbf7fd7b'
(OUT/'unfiltered.diff').write_bytes(stream)
changes = []
for line in git('diff','--name-status','--no-renames',BASE,CANDIDATE).decode().splitlines():
    status, path = line.split('\t',1)
    changes.append(dict(status=status,path=path))
permitted = {r['path'] for r in payloads}
assert {r['path'] for r in changes if r['status'] != 'A'} == permitted
assert all(r['status'] == 'A' and r['path'].startswith(PREFIX) or r['path'] in permitted for r in changes)

def tree(commit):
    result={}
    for record in git('ls-tree','-rz','--full-tree',commit).split(b'\0'):
        if not record: continue
        head,path=record.split(b'\t',1)
        mode,kind,blob=head.decode().split(' ')
        result[path.decode()]=(mode,kind,blob)
    return result
bt,ct=tree(BASE),tree(CANDIDATE)
assert not (bt.keys()-ct.keys())
protected={p:b for p,b in bt.items() if p not in permitted}
assert all(ct[p] == b for p,b in protected.items())

receipt_path='review/remediation/20261003-prepare/batches/B13/acceptance-stage-1/completion-statistics-successor.json'
assert read(BASE,receipt_path) == read(CANDIDATE,receipt_path)
receipts=json.loads(read(BASE,receipt_path))
rs=receipts['accepted_contribution_receipts']
assert len(rs) == 240 and len({(r['batch'],r['id']) for r in rs}) == 240
assert receipts['primary_denominator'] == 154 and receipts['canonical_OPEN'] == 229 and receipts['canonical_CLOSED'] == 0

owners=[]
assert [x['accepted_batch'] for x in nav['owners']] == ['B01','B02','B03','B04','B05','B06','B07','B08','B09','B10','B12','B13','B14','B15']
for r in nav['owners']:
    n=r['exact_current_navigation']; inputs=[]
    for role in ('reverse_declared_reader_inputs','current_accepted_inputs_consumed_by_author'):
        for a in n[role]:
            verify(a)
            inputs.append(dict(role=role,before=identity(BASE,a['path']),
                candidate=identity(CANDIDATE,a['path']),
                byte_equal=read(BASE,a['path'])==read(CANDIDATE,a['path'])))
    verify(n['accepted_receipts_binding'])
    owners.append(dict(owner=r['accepted_batch'],inputs=inputs,shared_control_IDs=n['shared_control_IDs']))

catalog=payloads[0]['path']
def rows(data):
    section=''; occ=collections.Counter(); result=[]
    for raw in data.splitlines(keepends=True):
        line=raw.decode()
        if line.startswith('## '): section=line.rstrip('\n\r')
        match=re.match(r'^\|\s*([A-Za-z][A-Za-z0-9_-]*\d[a-z]?)\s*\|',line)
        if not match: continue
        code=match[1]; occ[(section,code)]+=1
        result.append(((section,code,occ[(section,code)]),raw))
    return result
br,cr=rows(read(BASE,catalog)),rows(read(CANDIDATE,catalog))
assert len(br)==460 and len(cr)==484
oldkeys=[r[0] for r in br]; newkeys=[r[0] for r in cr]
assert [k for k in newkeys if k in set(oldkeys)] == oldkeys
newmap=dict(cr)
edits=[dict(section=k[0],id=k[1],occurrence=k[2],before_sha256=sha(b),after_sha256=sha(newmap[k]))
       for k,b in br if b!=newmap[k]]
newrows=[dict(section=k[0],id=k[1],sha256=sha(b)) for k,b in cr if k not in set(oldkeys)]
assert len(edits)==9 and len(newrows)==24
author_catalog=load('catalog-preservation')
assert [r['id'] for r in edits] == [r['before']['id'] for r in author_catalog['changed_assigned_rows']]
assert all(r['id'].startswith('B16-') for r in newrows)

# Reuse accurate prior source evidence; identity validation does not imply new reading.
source=load('source-reading-supplement')
source_checks=[]
for a in source['entries']:
    source_checks.append(dict(verify(a,repo=REF), ranges=a['lines'],
                             disposition='EXACT_VERSION_PRIOR_STATIC_EVIDENCE_REUSED'))
log=source['prior_exact_reading_log']
prior_log=json.loads(read(log['commit'],log['path']))
prior_log_identity=identity(log['commit'],log['path'])
prior_reference_checks=[]
for a in prior_log['reading']:
    if a['commit'] != '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b':
        continue # historical project snapshots are not substituted for current inputs
    actual=verify(a,repo=REF)
    lines=read(a['commit'],a['path'],REF).decode().splitlines()
    for span in a['ranges']:
        start,end=map(int,span['lines'].split('-'))
        assert sha(('\n'.join(lines[start-1:end])+'\n').encode()) == span['sha256'], (a['path'],span)
    prior_reference_checks.append(dict(actual,ranges=a['ranges'],exact_range_hashes_equal=True))

result=dict(
    role='B16_AFFECTED_CANDIDATE_ONLY',
    reviewed_commit=CANDIDATE,reviewed_tree=git('rev-parse',CANDIDATE+'^{tree}').decode().strip(),
    publication=PUBLICATION,FIX_BASE=BASE,
    identity_validation='PASS_METADATA_ONLY_NOT_SEMANTIC_OR_RUNTIME_PASS',
    planned_exact_inputs=len(c['planned_reads']), verified_identities=list(identities.values()),
    controls=control_checks,effective_case_constraints=effective_checks,
    payloads=payloads,original_scope_exact_after_checks=scope_checks,
    unfiltered_diff=dict(bytes=len(stream),sha256=sha(stream),path_count=len(changes),inventory=changes),
    base_tree_protection=dict(base_path_count=len(bt),payload_modified_count=len(permitted),
        protected_path_count=len(protected),removed_paths=0,all_protected_modes_types_blobs_equal=True,
        protected_tree_projection_sha256=sha(canon(protected))),
    accepted_receipts=dict(binding=identity(BASE,receipt_path),byte_equal=True,
        records=len(rs),distinct_batch_ID_pairs=len({(r['batch'],r['id']) for r in rs}),
        records_sha256=sha(canon(rs)),per_batch=dict(sorted(collections.Counter(r['batch'] for r in rs).items())),
        primary_denominator=154,canonical_OPEN=229,canonical_CLOSED=0),
    catalog=dict(existing_rows=len(br),candidate_rows=len(cr),old_order_and_multiplicity_equal=True,
        old_deletes_or_renames=0,protected_rows_byte_equal=len(br)-len(edits),edits=edits,new_rows=newrows,
        executed_rows=0,method='Independent section+ID+occurrence parser over exact Git bytes; author result only cross-checked afterwards'),
    owner_input_identities=owners,
    reused_source_evidence=dict(prior_log=prior_log_identity,source_supplement=source_checks,
        prior_reference_static_ranges=prior_reference_checks,
        historical_project_inputs='Not substituted for current FIX_BASE/candidate inputs; exact current identities and full eleven payload deltas independently checked'),
    prohibited_execution_count=0,
    note='Git/JSON/hash/row metadata checks only. Existing source logs and vectors were read as evidence, never run. Quality findings are separate owner judgments.')
(OUT/'independent-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(result='PASS',payloads=len(payloads),controls=len(ctrls),primary=sum(r['primary'] for r in ctrls),
    effective=len(effective_checks),owners=len(owners),receipts=len(rs),catalog_old=len(br),catalog_protected=len(br)-len(edits),
    catalog_edits=len(edits),catalog_new=len(newrows),protected_paths=len(protected),diff_bytes=len(stream),diff_sha256=sha(stream)),ensure_ascii=False))
