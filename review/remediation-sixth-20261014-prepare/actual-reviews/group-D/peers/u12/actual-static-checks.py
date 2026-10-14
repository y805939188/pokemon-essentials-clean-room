"""Independent immutable object/composition checks; no author or reference code execution."""
from pathlib import Path
import json,hashlib,subprocess,difflib,datetime,sys

ROOT=Path('/workspace/pokemon-essentials-clean-room')
OUT=ROOT/'review/remediation-sixth-20261014-prepare/actual-reviews/group-D/peers/u12'
ACT='9d5b4e99b617828690e6529b77a1e555d7c9eb1b'
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
U12='caa090d8e396c08b09fb2d4d5067aa00f4d6c3cb'
REVIEW='d7460b2a689245671e1b4f9c00da8d930113218d'
INPUT='review/remediation-sixth-20261014-prepare/integration/U01-U12-U14-composite-20261014/actual-review-input.json'
READSET=[]

def git(*a):return subprocess.check_output(['git','-C',str(ROOT),*a])
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def read(c,p,purpose):
    b=git('show',c+':'+p)
    e=git('ls-tree','-z',c,'--',p).rstrip(b'\0').decode();mode,typ,blob=e.split('\t',1)[0].split()
    r={'repository':str(ROOT),'commit':c,'tree':git('rev-parse',c+'^{tree}').decode().strip(),'path':p,'mode':mode,'type':typ,**ident(b),'physical_lines':len(b.splitlines()),'purpose':purpose,'complete_bytes_read':True,'automatic_semantic_credit':False}
    assert r['git_blob']==blob;READSET.append(r);return b,r
def matches(x,y):return all(x[k]==y[k] for k in ['bytes','sha256','git_blob'])

start=datetime.datetime.now(datetime.timezone.utc).isoformat()
binding={'commit':ACT,'workspace_tree':git('rev-parse',ACT+'^{tree}').decode().strip(),'formal_tree':git('rev-parse',ACT+':deliverables/final-specification-set').decode().strip(),'fixed_main':MAIN,'reference':REF,'reference_tree':git('rev-parse',REF+'^{tree}').decode().strip()}
assert binding['workspace_tree']=='faae3b9a22c37a2e2e994553f59e7099c6394db0'
assert binding['formal_tree']=='74dccc64506d008d50cf1cdfd906f701931020cc'
b,inputid=read(ACT,INPUT,'complete2661-line semantic input read; independent identity')
assert ident(b)=={'bytes':124082,'sha256':'7b63483a915792c077b2f8cf84208e9f5a7ac94e55ce93cfc8bbde718bf6d9aa','git_blob':'f7f220a4ee7c4b2ff6dc94b799fe54b13879b6c8'}
j=json.loads(b)
assert len(j['batches'])==13 and len(j['required_ids'])==j['required_count']==48
group=[x for x in j['batches'] if x['batch'] in ['R6-U10','R6-U11','R6-U12']]
ids=[i for x in group for i in x['required_ids']];assert len(ids)==9 and len(set(ids))==9
group_checks=[]
for x in group:
    c=x['candidate_published_commit'];review=x['independent_review']
    assert git('rev-parse',c+'^{tree}').decode().strip()==x['candidate_workspace_tree']
    assert git('rev-parse',c+':review/remediation-sixth-20261014-prepare/candidates/'+x['batch']+'/mirror').decode().strip()==x['candidate_mirror_tree']
    cb,cid=read(ACT,x['contract_path'],'group binding identity; U12 contract semantic full, other two identity only')
    rb,rid=read(review['review_commit'],review['report_path'],'fixed candidate review identity; U12report complete semantic read, others identity only')
    assert matches(x['contract_identity'],cid) and matches(review['report_identity'],rid)
    assert git('rev-parse',review['review_commit']+'^{tree}').decode().strip()==review['review_workspace_tree']
    assert review['scope_ids']==x['required_ids']
    group_checks.append({'batch':x['batch'],'required_ids':x['required_ids'],'candidate_commit':c,'candidate_tree':x['candidate_workspace_tree'],'candidate_mirror_tree':x['candidate_mirror_tree'],'contract':cid,'review_commit':review['review_commit'],'review_tree':review['review_workspace_tree'],'review_report':rid,'original_review_scope':'candidate-only; does not sign actual composition','bindings_match':True})
file_checks=[]
for x in j['files']:
    actual,aid=read(ACT,x['path'],'all47 declared actual inputs immutable identity; not full semantic review outside U12')
    assert matches(x['actual'],aid) and x['mode']==aid['mode'] and x['type']==aid['type']
    file_checks.append({'path':x['path'],'actual':aid,'declared_actual_match':True,'contributor_batches':[y['batch'] for y in x['contributions']],'pending_primary_writers':x['pending_primary_writers']})
contract=json.loads(git('show',ACT+':review/remediation-sixth-20261014-prepare/contracts/R6-U12.json'))
own_paths=contract['candidate_formal_paths'];own_checks=[]
for p in own_paths:
    actual,aid=read(ACT,p,'U12 actual full semantic text read (UI personally partial+current team full separate)')
    candidate,cid=read(U12,'review/remediation-sixth-20261014-prepare/candidates/R6-U12/mirror/'+p,'candidate composition identity and complete byte diff')
    a=candidate.decode().splitlines(keepends=True);z=actual.decode().splitlines(keepends=True)
    diff=[{'kind':t,'candidate_range':[i+1,j],'actual_range':[k+1,l],'candidate_text':''.join(a[i:j]),'actual_text':''.join(z[k:l])} for t,i,j,k,l in difflib.SequenceMatcher(None,a,z,autojunk=False).get_opcodes() if t!='equal']
    assert (ROOT/p).read_bytes()==actual
    own_checks.append({'path':p,'actual':aid,'candidate':cid,'actual_equals_candidate':actual==candidate,'delta':diff,'current_worktree_matches_frozen':True})
ui=own_paths[2];base=git('show',MAIN+':'+ui).decode().splitlines(keepends=True);actual=git('show',ACT+':'+ui).decode()
blocks=[]
for x in group:
    batch=x['batch'];c=x['candidate_published_commit'];path='review/remediation-sixth-20261014-prepare/candidates/'+batch+'/mirror/'+ui
    candidate=git('show',c+':'+path).decode().splitlines(keepends=True)
    for t,i,j,k,l in difflib.SequenceMatcher(None,base,candidate,autojunk=False).get_opcodes():
        if t=='equal':continue
        block=''.join(candidate[k:l]);at=actual.find(block);assert at>=0
        lo=actual[:at].count('\n')+1;hi=lo+block.count('\n')-1
        blocks.append({'batch':batch,'kind':t,'baseline_range':[i+1,j],'candidate_range':[k+1,l],'actual_range':[lo,hi],'bytes':len(block.encode()),'sha256':hashlib.sha256(block.encode()).hexdigest(),'complete_block_byte_equal':True,'read_scope':'Independent entire block byte check. U12 semantics personally read; U10/U11 semantics assigned current peer owners.'})
assert len(blocks)==5
assert [x['actual_range'] for x in blocks if x['baseline_range']==[915,914]]==[[946,1009],[1010,1026]]
assert actual.splitlines(keepends=True)[:243]==base[:243]
selected=[]
for line in actual.splitlines():
    if line.startswith('| R6-U12-'):selected.append(line.split('|')[1].strip())
assert selected==['R6-U12-BP01','R6-U12-BP02','R6-U12-BP03','R6-U12-BP04','R6-U12-TS01','R6-U12-TS02','R6-U12-TS03','R6-U12-TS04','R6-U12-TS05']
# Prior current peer read9 evidence stays same bytes; no credit moved to current author.
prior='2b6832d1049650e08a071dccabce23326cc2c9ef'
peerpath='review/remediation-sixth-20261014-prepare/reviews/R6-U11-R/peers/evidence/counter-payload-audit.json'
pb,pid=read(prior,peerpath,'prior current non-author peer complete9 evidence read receipt; identity reuse only')
peer=json.loads(pb);counter=[]
for x in peer['payload_records']:
    cb,cid=read(ACT,x['input_path'],'current9 cached counter payload identity matched prior complete non-author read')
    old=git('show','e93d0e56750a6a16cc50cc68b2c97f11ea255153:'+x['input_path'])
    assert cb==old and matches(x['expected'],cid)
    counter.append({'id':x['id'],'current_identity':cid,'prior_receipt':pid,'current_equals_prior_full_read_payload':True,'prior_full_read_task':'/root/evidence_audit/counter_payloads','personal_new_relevant_read':'root/counterreview-bag complete1–73; imported /205 /210 /251 /257 complete nodes','source_read_credit_to_K_remains_zero':True})
# Preserve old catalogue dependency rows exactly in both accepted candidate and actual.
old_ui=git('show',MAIN+':'+ui).decode().splitlines()
protected=[]
prefixes=['| C20 |','| C29 |','| C30 |','| C31 |','| C32 |','| B16-B035 |','| B16-D023 |','| U06-M10-001-','| U05-QN','| R4-CM','| R4-NM']
for line in old_ui:
    if not any(line.startswith(p) for p in prefixes):continue
    assert line in actual.splitlines();protected.append({'prefix':line.split('|')[1].strip(),'row_sha256':hashlib.sha256((line+'\n').encode()).hexdigest(),'original_row_retained_exact':True,'actual_line':actual.splitlines().index(line)+1})
result={'schema':'r6-group-d-u12-actual-object-checks.v1','start_utc':start,'finish_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime':sys.version,'binding':binding,'input_identity':inputid,'input_semantic_ranges':[[1,440],[441,920],[921,1410],[1411,1910],[1911,2390],[2391,2661]],'cumulative_context':{'batches':13,'IDs':48,'actual_declared_paths':len(file_checks)},'group_D':{'batches':['R6-U10','R6-U11','R6-U12'],'IDs':ids,'count':9,'old_filename_not_group_scope':True},'personal_U12':['GR6-UI-BAG-001','GR6-UI-BAG-002'],'group_identity_checks':group_checks,'all47_actual_identity_checks':file_checks,'own_actual_paths':own_checks,'shared_UI_all_changed_blocks':blocks,'two_EOF_append_blocks_complete_retained':True,'actual_prefix1_243_equals_frozen_but_newly_read':True,'U12_unique_new_vectors':selected,'prior_counter_receipt':pid,'counter_current_identity_reuse':counter,'protected_legacy_rows':protected,'new_reference_source_behavior_model_host_execution':0,'no_author_script_execution':True,'formal_acceptance':None,'CLOSED':False,'read_set':READSET,'limitations':['Effective runtime metadata UNVERIFIED; no CLI probe.','All47 identity read is not semantic review of all47 formal files.','Candidate PASS reused only as provenance, not actual PASS.','U10/U11 behavior/remaining UI text belong current assigned peer/root receipts.','U13FAIL/repaired9971fe...unaccepted and WP66-A/WP54 interfaces remain excluded.','Public administrative synchronization belongs R6-I after review; not performed here.']}
(OUT/'static-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':'STATIC_IDENTITIES_AND_COMPOSITION_PASS','cumulative13batches48IDs':True,'groupD3batches9IDs':True,'actual_paths':len(file_checks),'U12_paths':4,'shared_UI_changed_blocks':5,'EOF_appends':2,'U12_vectors':9,'protected_legacy_rows':len(protected),'counter9same_as_prior_full_read':True,'new_source_execution':0}))
