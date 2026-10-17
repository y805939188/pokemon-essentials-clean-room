#!/usr/bin/env python3
"""Independent, read-only candidate/input audit; writes only adjacent JSON evidence.

Does not import or execute the candidate author's validation program.
"""
import collections
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess

REPO = Path('/workspace/r8-u06-review')
SOURCE = Path('/workspace/pokemon-essentials')
REPORT = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
HANDOFF = REPO / REPORT / 'handoff'
CAND = REPO / 'review/remediation-eighth-20261016-prepare/candidates/R8-U06'
OUT = Path(__file__).resolve().parent
HEAD = '16f986afc1c85e64131f1dc8c6f2477a79c04029'
BASE = '4575e80d041ab0c74a42e2e36399d05791dbaa5b'
PAYLOAD = '0384629ccf1c2c492ebab611bbbb858f825e9a31'
commands = []

def sha(b):
    return hashlib.sha256(b).hexdigest()

def git(repo, *args):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = subprocess.run(['git', *args], cwd=repo, capture_output=True)
    commands.append(dict(start_utc=start, end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), cwd=str(repo), argv=['git', *args], exit_code=p.returncode, stdout_bytes=len(p.stdout), stdout_sha256=sha(p.stdout), stderr=p.stderr.decode(errors='replace')))
    if p.returncode:
        raise RuntimeError(p.stderr.decode(errors='replace'))
    return p.stdout

def local_repo(identity):
    return SOURCE if identity.get('repo') == str(SOURCE) or identity['path'].startswith('Data/') else REPO

def resolve_path(identity, repo):
    path = identity['path']
    if repo == REPO and not path.startswith(('review/', 'deliverables/', 'planning/', 'audit/', 'AGENTS')):
        path = REPORT + '/' + path
    return path

def verify(identity, label):
    repo = local_repo(identity)
    path = resolve_path(identity, repo)
    commit = identity['commit']
    expected = {k: identity[k] for k in ('bytes','sha256','blob','mode') if k in identity}
    result = dict(label=label, original_identity=identity, resolved_repo=str(repo), resolved_path=path)
    try:
        b = git(repo, 'show', commit + ':' + path)
        entry = git(repo, 'ls-tree', commit, '--', path).decode().strip().split(None, 3)
        actual = dict(bytes=len(b), sha256=sha(b), mode=entry[0], blob=entry[2])
        checks = {k:actual[k] == v for k,v in expected.items()}
        for key in ('tree','workspace_tree'):
            if key in identity:
                checks[key] = git(repo, 'rev-parse', commit + '^{tree}').decode().strip() == identity[key]
        if 'report_tree' in identity:
            checks['report_tree'] = git(repo, 'rev-parse', commit + ':' + REPORT).decode().strip() == identity['report_tree']
        result.update(observed=actual, checks=checks, passed=all(checks.values()))
    except Exception as e:
        result.update(passed=False, error=str(e))
    return result

r = json.loads((HANDOFF / 'batches/R8-U06/readset.json').read_text())
checks = []
for group in ('source_spec_files','mandatory_root_input','additional_mandatory_companions'):
    for i, identity in enumerate(r['inherited_contents'][group]):
        # Current exact recovery is a second identity, never a replacement for provenance.
        checks.append(verify(identity, f'inherited_contents/{group}/{i}'))
recovered = []
for i, identity in enumerate(r['inherited_contents']['mandatory_root_input']):
    if 'current_recovered_at' in identity:
        recovered.append(verify(identity['current_recovered_at'], f'mandatory_root_input/{i}/current_recovered_at'))
delta = [verify(x, f'delta_contents/units/{i}') for i,x in enumerate(r['delta_contents']['units'])]
conditional = []
for group in ('source_units','formal_units'):
    for i,x in enumerate(r['conditional_F05_readset'][group]):
        ident=x.get('identity',x)
        check=verify(ident,f'conditional_F05_readset/{group}/{i}')
        if 'range' in x and check['passed']:
            b=git(local_repo(ident),'show',ident['commit']+':'+resolve_path(ident,local_repo(ident)))
            sliced=b'\n'.join(b.splitlines()[x['range'][0]-1:x['range'][1]])
            check['slice_observed']={'bytes':len(sliced),'sha256':sha(sliced)}
            check['slice_passed']=len(sliced)==x['slice_bytes'] and sha(sliced)==x['slice_sha256']
        conditional.append(check)
conditional.append(verify(r['conditional_F05_readset']['original_candidate'],'conditional_F05_readset/original_candidate'))

manifest=json.loads((CAND/'evidence/candidate-files.json').read_text())
mirrors=[]
link_checks=[]
catalogs=[]
for item in manifest['files']:
    rel=item['candidate']; destination=item['formal_destination']
    path=CAND/rel; candidate_path=str(path.relative_to(REPO))
    b=path.read_bytes(); base=git(REPO,'show',BASE+':'+destination)
    committed=git(REPO,'show',HEAD+':'+candidate_path)
    payload=git(REPO,'show',PAYLOAD+':'+candidate_path)
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    entry=git(REPO,'ls-tree',HEAD,'--',candidate_path).decode().strip().split(None,3)
    actual=dict(bytes=len(b),sha256=sha(b),blob=blob,mode=entry[0])
    matches=dict(manifest_bytes=len(b)==item['candidate_bytes'],manifest_sha=sha(b)==item['candidate_sha256'],manifest_blob=blob==item['candidate_blob'],base_sha=sha(base)==item['base_sha256'],base_blob=hashlib.sha1(b'blob '+str(len(base)).encode()+b'\0'+base).hexdigest()==item['base_blob'],worktree_equal_head=b==committed,payload_equal_head=payload==committed,changed=b!=base)
    diff=list(difflib.unified_diff(base.decode().splitlines(True),b.decode().splitlines(True),fromfile=destination,tofile=rel))
    mirrors.append(dict(candidate=candidate_path,formal_destination=destination,observed=actual,checks=matches,passed=all(matches.values()),base_lines=len(base.splitlines()),candidate_lines=len(b.splitlines()),diff=''.join(diff)))
    text=b.decode()
    # Links resolve inside candidate mirror for changed destinations, baseline tree for read-only companions.
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)\)',text):
        target=target.strip('<>')
        if '://' in target or target.startswith(('mailto:','app:')):continue
        filename,sep,fragment=target.partition('#')
        dest=(path.parent/filename).resolve() if filename else path
        if dest.is_file():exists=True;destination_kind='candidate_or_local'
        else:
            try:
                formal_relative=str(dest.relative_to(CAND/'mirror'))
                git(REPO,'cat-file','-e',BASE+':'+formal_relative); exists=True;destination_kind='baseline_formal'
            except Exception:
                exists=False;destination_kind='missing'
        link_checks.append(dict(file=candidate_path,target=target,exists=exists,destination_kind=destination_kind))
    if '/test-catalog/' in destination:
        def rows(s):
            return [line for line in s.splitlines() if line.startswith('|') and not re.match(r'^\|\s*[-: ]+\|',line)]
        old=rows(base.decode());new=rows(text)
        changed=list((collections.Counter(old)-collections.Counter(new)).elements())
        added=list((collections.Counter(new)-collections.Counter(old)).elements())
        catalogs.append(dict(path=destination,baseline_rows=len(old),candidate_rows=len(new),removed_or_modified_original_rows=changed,new_or_modified_rows=added,baseline_row_prefixes_missing=[x.split('|')[1].strip() for x in changed if not any(y.split('|')[1].strip()==x.split('|')[1].strip() for y in new)]))

branch=git(REPO,'symbolic-ref','--short','HEAD').decode().strip()
formal_trees={c:git(REPO,'rev-parse',c+':deliverables/final-specification-set').decode().strip() for c in (BASE,HEAD,PAYLOAD,'fd1df570cad987dc3852a3b958f03916e317f7fe')}
remote=git(REPO,'ls-remote','--heads','origin','main','codex/r8-u06-revision-20261017','codex/r8-u06-independent-review-20261017').decode()
changed_paths=git(REPO,'diff','--name-only',BASE,HEAD).decode().splitlines()
scope=dict(branch=branch,head=git(REPO,'rev-parse','HEAD').decode().strip(),ancestor=git(REPO,'merge-base','--is-ancestor',BASE,HEAD).decode(),formal_trees=formal_trees,changed_paths=changed_paths,only_batch_candidate=all(x.startswith(str(CAND.relative_to(REPO))+'/') for x in changed_paths),remote_readback=remote,source_head=git(SOURCE,'rev-parse','HEAD').decode().strip(),source_status=git(SOURCE,'status','--porcelain').decode(),review_worktree_status=git(REPO,'status','--short').decode())
nonmirror=[]
for p in sorted(CAND.rglob('*')):
    if p.is_file() and 'mirror' not in p.parts:
        b=p.read_bytes();nonmirror.append(dict(path=str(p.relative_to(REPO)),bytes=len(b),sha256=sha(b),lines=len(b.splitlines())))

# Independently bind publication claims to the exact historical payload, not HEAD.
receipts=[]
for name in ('publication-readback.initial.json','publication-readback.json'):
    receipt=json.loads((CAND/'evidence'/name).read_text())
    rows=[]
    for item in receipt['all_files']:
        b=git(REPO,'show',receipt['payload_commit']+':'+item['path'])
        blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        rows.append(dict(path=item['path'],passed=len(b)==item['bytes'] and sha(b)==item['sha256'] and blob==item['git_blob'],observed_bytes=len(b),observed_sha256=sha(b),observed_blob=blob))
    receipts.append(dict(file=name,payload_commit=receipt['payload_commit'],files=rows,all_passed=all(x['passed'] for x in rows),qualification='Historical author transport record only; independently checked against Git payload, not a nonauthor semantic review or a fresh remote byte fetch by this auditor.'))

log_integrity=[]
for name in ('commands.jsonl','publication-commands.jsonl'):
    rows=[]
    for i,line in enumerate((CAND/'evidence'/name).read_text().splitlines(),1):
        item=json.loads(line)
        start=datetime.datetime.fromisoformat(item['start_utc']);end=datetime.datetime.fromisoformat(item['end_utc'])
        row=dict(line=i,argv=item['argv'],exit_code=item['exit_code'],utc_ordered=start<=end,stdout_retained=item.get('stdout') is not None,stderr_retained='stderr' in item)
        if item.get('stdout') is not None and 'stdout_sha256' in item:
            b=item['stdout'].encode();row['stdout_hash_and_size_match']=len(b)==item['stdout_bytes'] and sha(b)==item['stdout_sha256']
        elif item['argv'][1]=='show' and item.get('stdout') is None:
            b=git(REPO,'show',item['argv'][2]);row['stdout_hash_and_size_match']=len(b)==item['stdout_bytes'] and sha(b)==item['stdout_sha256']
        rows.append(row)
    log_integrity.append(dict(file=name,rows=rows,failures=[x for x in rows if x['exit_code']!=0],credit='TOOL_VALIDATION; recorded timing and stream self-consistency, not independent proof of unlogged reading operations.'))

author_units=[]
ledger=json.loads((CAND/'evidence/author-reading-ledger.json').read_text())
for i,item in enumerate(ledger['actual_additional_source_and_formal_units']):
    repo=SOURCE if item['repo']==str(SOURCE) else REPO
    b=git(repo,'show',item['commit']+':'+item['path'])
    sliced=b''.join(b.splitlines(keepends=True)[item['range'][0]-1:item['range'][1]])
    matches=dict(whole_sha256=sha(b)==item['whole_sha256'])
    if 'whole_bytes' in item:matches['whole_bytes']=len(b)==item['whole_bytes']
    if 'unit_sha256' in item:matches['unit_sha256']=sha(sliced)==item['unit_sha256']
    if 'git_blob' in item:matches['git_blob']=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob']
    author_units.append(dict(index=i,path=item['path'],range=item['range'],checks=matches,passed=all(matches.values()),credit='Author ledger locator integrity only; no transfer of author reading credit.'))

anchor_inventory=[]
for item in manifest['files']:
    text=(CAND/item['candidate']).read_text()
    base=git(REPO,'show',BASE+':'+item['formal_destination']).decode()
    old=re.findall(r'<a\s+id=[\"\']([^\"\']+)',base)
    new=re.findall(r'<a\s+id=[\"\']([^\"\']+)',text)
    oldh=[x for x in base.splitlines() if x.startswith('#')]
    newh=[x for x in text.splitlines() if x.startswith('#')]
    anchor_inventory.append(dict(path=item['formal_destination'],explicit_ids=new,unique=len(new)==len(set(new)),old_explicit_ids_preserved=not(set(old)-set(new)),old_heading_lines_preserved=not(collections.Counter(oldh)-collections.Counter(newh))))
package_navigation=[]
for p in CAND.rglob('*.md'):
    if 'mirror' in p.parts:continue
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)\)',p.read_text()):
        if '://' not in target and not target.startswith('#'):
            package_navigation.append(dict(file=str(p.relative_to(CAND)),target=target,exists=(p.parent/target.partition('#')[0]).is_file()))

actual_diff=''
for item in manifest['files']:
    old=git(REPO,'show',BASE+':'+item['formal_destination']).decode()
    new=(CAND/item['candidate']).read_text()
    actual_diff+=''.join(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),fromfile='a/'+item['formal_destination'],tofile='b/'+item['formal_destination'],n=0))
diff_check=dict(expected_bytes=len(actual_diff.encode()),expected_sha256=sha(actual_diff.encode()),artifact_bytes=(CAND/'evidence/candidate.diff').stat().st_size,exact_match=actual_diff.encode()==(CAND/'evidence/candidate.diff').read_bytes())

assignment=json.loads((HANDOFF/'batch-assignment.json').read_text())
batch=next(x for x in assignment['batches'] if x['id']=='R8-U06')
contracts=json.loads((HANDOFF/'contracts.zh.json').read_text())
dispositions=json.loads((CAND/'evidence/dispositions.json').read_text())
disposition_checks=[]
for item in dispositions['records']:
    pointer=item['original_evidence']['current_contract']['pointer']
    contract=contracts['records'][int(pointer.split('/')[-1])]
    disposition_checks.append(dict(id=item['id'],current_contract_pointer=pointer,same_id=contract['id']==item['id'],same_classification=contract['classification']==item['classification'],same_severity=contract['severity']==item['severity'],same_original_provenance=contract['full_contract_original_provenance']==item['original_evidence']['original_and_recovered_provenance'],same_root_adjudication=contract['root_adjudication']==item['original_evidence']['root_adjudication'],all_four_gates_pending=all(item[k] is False for k in ('candidate_independent_PASS','actual_integration_PASS','ACCEPTED','CLOSED'))))
lookup={(x['resolved_path'],x['original_identity']['commit']):x['observed'] for x in checks+recovered+delta+conditional}
author_checks=[]
for index,item in enumerate(json.loads((CAND/'evidence/input-identity-checks.json').read_text())['checks']):
    actual=lookup.get((item['path'],item['commit']))
    author_checks.append(dict(index=index,match=bool(actual and actual['blob']==item['blob'] and actual['bytes']==item['bytes']==item['expected'] and item['verified'])))
contract_scope=dict(dispositions_14=disposition_checks,required_ids_exact={x['id'] for x in dispositions['records'] if x['classification']=='required'}==set(batch['required_ids']),selected_optional_ids_exact={x['id'] for x in dispositions['records'] if x['optional_adopted']}==set(batch['optional_ids_if_later_selected']),candidate_targets_match_authorized={x['formal_destination'] for x in mirrors}==set(batch['actual_target_write_set'])|set(batch['conditional_target_write_set_by_id']['GR8-COM-RECORD-DEBUG-RNG-001']),author_132_records=author_checks,author_static_check_count=len(json.loads((CAND/'evidence/static-validation.json').read_text())['checks']),unselected_visual_policy=dispositions['independent_visual_policy'],other_optional=dispositions['other_optional_ids'])

result=dict(schema='independent-r8-u06-identity-scope-audit/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer='/root/identity_scope_audit',actual_configuration={k:'UNVERIFIED' for k in ('model','effort','tier','speed','Fast')},credit='OBJECT_IDENTITY_AND_STRUCTURE_ONLY; not semantic reading or reference execution',input_denominators=dict(inherited_132={'source_spec_files':60,'mandatory_root_input':64,'additional_mandatory_companions':8},current_recovery_aliases=len(recovered),delta_all_batches=len(delta),F05={'source':6,'formal':3,'original_candidate':1},note='Counts are identity entries with overlap, not additive unique semantic atoms.'),inherited_132=checks,current_recoveries=recovered,delta_all_batches=delta,F05=conditional,mirrors=mirrors,scope=scope,catalog_preservation=catalogs,relative_file_links=link_checks,nonmirror_manifest=nonmirror,receipt_integrity=receipts,log_integrity=log_integrity,author_ledger_unit_integrity=author_units,anchor_inventory=anchor_inventory,package_navigation=package_navigation,candidate_diff_check=diff_check,contract_scope_structure=contract_scope,commands=commands)
(OUT/'identity-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(inherited=f'{sum(x["passed"] for x in checks)}/{len(checks)}',current_recovery=f'{sum(x["passed"] for x in recovered)}/{len(recovered)}',delta=f'{sum(x["passed"] for x in delta)}/{len(delta)}',F05=f'{sum(x["passed"] for x in conditional)}/{len(conditional)}',mirrors=f'{sum(x["passed"] for x in mirrors)}/{len(mirrors)}',receipt_files=[len(x['files']) for x in receipts],receipt_all_pass=all(x['all_passed'] for x in receipts),author_units_pass=sum(x['passed'] for x in author_units),author_units_total=len(author_units),diff_check=diff_check,missing_links=[x for x in link_checks+package_navigation if not x['exists']],failed=[x for x in checks+recovered+delta+conditional if not x['passed']]),ensure_ascii=False,indent=2))
