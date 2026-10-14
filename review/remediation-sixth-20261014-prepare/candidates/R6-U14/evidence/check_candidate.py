"""Document replay, old-row preservation and identity checks, not gameplay tests."""
from pathlib import Path
import ast,datetime,hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[5];OUT=Path(__file__).resolve().parent;BATCH=OUT.parent
PREP='469a268b92daed7b4d28d7fd0da75520cbb7228f'
FORMAL='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
R5='13fddb0a217b36974c75657aa68da0caf104ee48'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
c=json.loads((ROOT/'review/remediation-sixth-20261014-prepare/contracts/R6-U14.json').read_text())
allowed={str((BATCH/'mirror'/p).relative_to(ROOT)) for p in c['candidate_formal_paths']}
replay={p:git('show',PREP+':'+p).decode() for p in allowed}
for script,func in [('revise_candidate.py','replace'),('refine_candidate.py','edit')]:
    for node in ast.parse((OUT/script).read_text()).body:
        if not isinstance(node,ast.Expr) or not isinstance(node.value,ast.Call):continue
        call=node.value
        if not isinstance(call.func,ast.Name) or call.func.id not in [func,'append']:continue
        args=[ast.literal_eval(a) for a in call.args]
        p=str((BATCH/'mirror/deliverables/final-specification-set'/args[0]).relative_to(ROOT))
        assert p in replay
        if call.func.id=='append':
            assert args[1] not in replay[p];replay[p]=replay[p].rstrip()+'\n\n'+args[1]+'\n'
        else:
            assert replay[p].count(args[1])==1;replay[p]=replay[p].replace(args[1],args[2],1)
assert all((ROOT/p).read_text()==t for p,t in replay.items())
changed=set(git('diff','--name-only',PREP,'--',str(BATCH.relative_to(ROOT)/'mirror')).decode().splitlines())
assert changed==allowed,(changed-allowed,allowed-changed)
assert not git('diff','--name-only',PREP,'--','deliverables','audit','planning','specs','reference')
assert git('branch','--show-current').decode().strip()=='codex/remediation-sixth-r6-u14-author-20261014'
git('diff','--check')
manifest=[];oldrows=[];newvectors=[];newlinks=[]
for formal in c['candidate_formal_paths']:
    local=BATCH/'mirror'/formal;b=local.read_bytes();old=git('show',FORMAL+':'+formal)
    assert git('show',PREP+':'+str(local.relative_to(ROOT)))==old
    assert git('show',R5+':'+formal)==old
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    manifest.append(dict(formal_path=formal,candidate_path=str(local.relative_to(ROOT)),mode='100644',bytes=len(b),sha256=sha(b),git_blob=blob,baseline_sha256=sha(old),baseline_equals_exact_R5_accepted_bytes=True))
    if '/test-catalog/' in formal:
        before=[x for x in old.decode().splitlines() if x.startswith('|')]
        after=b.decode().splitlines()
        assert all(after.count(x)>=before.count(x) for x in set(before))
        assert b.startswith(old.rstrip())
        oldrows.append(dict(path=formal,preserved_table_lines=len(before),status='BYTE_IDENTICAL_OLD_ROWS; no runtime verdict'))
        delta=b.decode()[len(old.decode().rstrip()):]
        newvectors.extend(re.findall(r'^\| (LZ(?:3[6-9]|4[01])|R6-U14-[^ |]+) \|',delta,re.M))
        assert 'NOT_EXECUTED_THIS_UPDATE' in delta
    for label,target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',b.decode()):
        if target in old.decode() or target.startswith('http'):continue
        filepath,_,fragment=target.partition('#')
        dest=(local.parent/filepath).resolve()
        if not dest.exists():
            rel=dest.relative_to(BATCH/'mirror');text=git('show',FORMAL+':'+str(rel)).decode()
        else:text=dest.read_text()
        if fragment:
            headings=re.findall(r'^#+\s+(.+)$',text,re.M)
            slugs=[re.sub(r'\s','-',re.sub(r'[^\w\- ]','',h.lower())) for h in headings]
            assert fragment in slugs,(formal,target,slugs)
        newlinks.append(dict(path=formal,target=target,status='TARGET_AND_ANCHOR_RESOLVED'))
assert len(newvectors)==len(set(newvectors))==27
reads=[json.loads(x) for x in (OUT/'reading-receipts.jsonl').read_text().splitlines()]
coverage=[]
for path in c['read_only_reference_paths']:
    if not path.endswith(('.rb','.txt')):continue
    rows=[x for x in reads if x['kind']=='git' and x['ref']==R and x['path']==path and x['exit_code']==0]
    assert rows,path
    n=rows[0]['input_lines'];seen=set()
    for row in rows:seen.update(range(row['range'][0],row['range'][1]+1))
    assert seen==set(range(1,n+1)),(path,len(seen),n)
    coverage.append(dict(path=path,complete_text_lines=n,ranges=[x['range'] for x in rows],identity=rows[0]['input_sha256'],semantic_inspection='Displayed original ranges inspected by author; not execution'))
for path in c['candidate_formal_paths']:
    rows=[x for x in reads if x['path']==path and x['exit_code']==0]
    n=rows[0]['input_lines'];seen=set()
    for row in rows:seen.update(range(row['range'][0],row['range'][1]+1))
    assert seen==set(range(1,n+1)),(path,len(seen),n)
history=json.loads(git('show',R5+':review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-closure-candidate/closure-candidate.json'))
activation=json.loads(git('show','12df95a8e81061a606d50d3f0a0528793b2e6b2c:review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-activation/activation-receipt.json'))
for x in activation['state_resolution']['selection']:
    row=history['records'][x['record_index']]
    assert row['id']==x['id']
    assert sha(canonical(row))==x['scope_record_sha256']
    assert sha(canonical(row['proposed_only_after_valid_activation']))==x['selected_state_record_sha256']
assert len(activation['state_resolution']['selection'])==92
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),runtime=sys.version,evidence_level='TOOL_VALIDATION_ONLY',document_patch_replay='EXACT_ALL_14',old_catalog_table_lines=oldrows,new_vector_ids=newvectors,new_vector_count=27,new_local_links=newlinks,designated_text_read_coverage=coverage,formal_baseline_full_reads=14,activation_identity_check=dict(selected_states=92,all_record_hashes_match=True,semantic_boundary='Identity only; author read selected13 R5 criteria/case premises, R2 selected9 controls and2 contribution fields, R3 selected3 and R4 selected2; no full historical semantic re-review'),protected_tracked_diff='NONE_AT_THIS_CHECK',nonauthor_review='PENDING_PARENT_ASSIGNED_REVIEWER',execution=dict(reference_functions=0,independent_gameplay_model=0,host=0,Demo=0,real_save=0,media=0),status='AUTHOR_TOOL_CHECKS_COMPLETE; not CANDIDATE_PASS or formal acceptance')
(OUT/'author-tool-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(OUT/'candidate-manifest.json').write_text(json.dumps(dict(prepare=PREP,formal=FORMAL,reference=R,files=manifest),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changed_mirrors=len(changed),new_vectors=27,old_table_lines_preserved=sum(x['preserved_table_lines'] for x in oldrows),full_designated_texts=len(coverage),formal_baseline_full_reads=14,new_links=len(newlinks),historical_activation_hashes=92,status=out['status']),ensure_ascii=False))
