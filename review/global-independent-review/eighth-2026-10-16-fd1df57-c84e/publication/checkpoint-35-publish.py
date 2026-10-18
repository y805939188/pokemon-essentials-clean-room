"""Publish only root-authorized frozen C35 blobs, then independently read remote bytes.

Preparation may compile this file. Running publish requires the later real freeze
manifest's preannounced SHA256; this program does not discover/freeze candidates.
"""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, re, subprocess, sys

W=Path('/workspace/pokemon-essentials-clean-room')
R=Path('/workspace/pokemon-essentials')
RR=W/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
PUB=RR/'publication'; IO=PUB/'checkpoint-35-io'
PREFIX=str(RR.relative_to(W))+'/'
HEAD='81cc98eec7cc81706e51c8b274e9ff7042c0868b'
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
BRANCH='codex/review-eighth-20261016-fd1df57-c84e'
FORMAL='f292698cdd4a8e725525a9be6dc34b75faaf151e'
OLD_LIVE={PREFIX+'tasks/pbs_creature_current_cloud/'+n for n in [
    'dependency-identities.json','formal-dependency-identities.json',
    'record-field-ledger.json','sync_current_state.py']}
events=[]

def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(raw): return hashlib.sha256(raw).hexdigest()
def oid(raw): return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def put(path,value): path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def run(args,label,stdin=None):
    start=utc(); p=subprocess.run(args,cwd=W,input=stdin,capture_output=True)
    row=dict(args=args,start_utc=start,end_utc=utc(),exit=p.returncode)
    for key,value in [('stdout',p.stdout),('stderr',p.stderr)]:
        path=IO/(label+'.'+key); assert not path.exists(),str(path)
        path.write_bytes(value)
        row.update({key:str(path.relative_to(RR)),key+'_bytes':len(value),key+'_sha256':sha(value)})
    if stdin is not None: row.update(stdin_bytes=len(stdin),stdin_sha256=sha(stdin))
    path=IO/(label+'.operation.json'); assert not path.exists()
    put(path,row);events.append(row)
    assert p.returncode==0,row
    return p.stdout

def git(*args,label,stdin=None): return run(['git','-C',str(W),*args],label,stdin)

def porcelain_paths(raw):
    rows=raw.split(b'\0');result=[];i=0
    while i<len(rows):
        row=rows[i];i+=1
        if not row: continue
        assert len(row)>=4 and row[2:3]==b' '
        result.append(row[3:].decode())
        if b'R' in row[:2] or b'C' in row[:2]:
            assert i<len(rows) and rows[i]
            result.append(rows[i].decode());i+=1
    return result

def preflight():
    commands=[
        (W,['branch','--show-current']),
        (W,['rev-parse',B8+'^{tree}']),
        (W,['rev-parse',B8+':deliverables/final-specification-set']),
        (W,['diff','--name-only','-z',B8]),
        (W,['status','--porcelain','-z','--untracked-files=all']),
        (R,['rev-parse','HEAD']),
        (R,['rev-parse','HEAD^{tree}']),
        (R,['status','--porcelain','-z','--untracked-files=all']),
        (W,['ls-remote','origin','refs/heads/main','refs/tags/delivery/seventh-round-closed-final-20261016','refs/heads/'+BRANCH]),
    ]
    def one(item):
        i,(where,args)=item
        return run(['git','-C',str(where),*args],'publish-preflight-%02d'%(i+1))
    with concurrent.futures.ThreadPoolExecutor(max_workers=9) as pool:
        rows=list(pool.map(one,enumerate(commands)))
    assert rows[0].decode().strip()==BRANCH
    assert rows[1].decode().strip()=='751dfde81048c81390f89a65ca1d1a565ba8e1ca'
    assert rows[2].decode().strip()==FORMAL
    assert all(not x or x.decode().startswith(PREFIX) for x in rows[3].split(b'\0'))
    assert all(p.startswith(PREFIX) for p in porcelain_paths(rows[4]))
    assert rows[5].decode().strip()=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
    assert rows[6].decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0'
    assert not rows[7]
    refs={line.split()[1]:line.split()[0] for line in rows[8].decode().splitlines()}
    assert refs=={'refs/heads/main':B8,'refs/tags/delivery/seventh-round-closed-final-20261016':B8,'refs/heads/'+BRANCH:HEAD}

def main():
    assert len(sys.argv)==4 and sys.argv[1]=='publish', 'Usage: script publish FROZEN_CANDIDATE_SHA256 ROOT_APPROVED_READBACK_NAME'
    candidate_sha,name=sys.argv[2:]
    assert re.fullmatch('[0-9a-f]{64}',candidate_sha)
    assert re.fullmatch('r8-[a-z0-9-]+-readback-35',name)
    assert not (Path('/workspace/scratch')/name).exists()
    assert not (PUB/(name+'.json')).exists()
    IO.mkdir(exist_ok=True)
    assert git('rev-parse','HEAD',label='publish-guard-head').decode().strip()==HEAD
    assert git('branch','--show-current',label='publish-guard-branch').decode().strip()==BRANCH
    assert not git('diff','--cached','--name-only','-z',label='publish-guard-index')
    preflight()
    manifest=PUB/'checkpoint-35-candidates.json'
    raw=manifest.read_bytes();assert sha(raw)==candidate_sha
    frozen=json.loads(raw)
    assert frozen['schema']=='gr8-checkpoint35-exact-frozen-candidates/v1'
    assert frozen['baseline_HEAD']==HEAD and frozen['branch']==BRANCH
    assert frozen['root_authorized_freeze'] is True
    rows=list(frozen['files'])
    envelope_oid=git('hash-object','-w','--stdin',label='publish-frozen-envelope',stdin=raw).decode().strip()
    assert envelope_oid==oid(raw)
    rows.append(dict(path=str(manifest.relative_to(W)),mode='100644',type='blob',blob=envelope_oid,bytes=len(raw),sha256=sha(raw)))
    assert len({x['path'] for x in rows})==len(rows)
    assert not ({x['path'] for x in rows}&OLD_LIVE)
    for x in rows:
        path=Path(x['path'])
        assert x['path'].startswith(PREFIX) and '..' not in path.parts and not path.is_absolute()
        assert x['mode']=='100644' and x['type']=='blob' and 0<=x['bytes']<100000000
        assert re.fullmatch('[0-9a-f]{40}',x['blob']) and re.fullmatch('[0-9a-f]{64}',x['sha256'])
        assert not any(c.endswith('.git') for c in path.parts)
        assert 'tmp_pack_' not in x['path'] and '__pycache__' not in path.parts
        assert not x['path'].endswith(('.pyc','.tmp'))
    bypath={x['path']:x for x in rows}
    semantic_names=['summary.json','core-manifest.json','adjudication/root-primary-task-final-registry.final.json',
                    'coverage/final-typed-denominators.json','coverage/wp-final-coverage.json']
    assert all(PREFIX+n in bypath for n in semantic_names)
    # Consume only exact previously frozen Git objects, even if live files changed.
    args=['git','-C',str(W),'cat-file','--batch']
    start=utc();proc=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    checked=[];semantic={}
    try:
        for x in rows:
            proc.stdin.write((x['blob']+'\n').encode());proc.stdin.flush()
            header=proc.stdout.readline().decode().split()
            assert header==[x['blob'],'blob',str(x['bytes'])]
            b=proc.stdout.read(x['bytes'])
            assert len(b)==x['bytes'] and proc.stdout.read(1)==b'\n' and sha(b)==x['sha256'] and oid(b)==x['blob']
            checked.append(dict(path=x['path'],blob=x['blob'],bytes=len(b),sha256=sha(b)))
            if x['path'] in [PREFIX+n for n in semantic_names]: semantic[x['path'][len(PREFIX):]]=json.loads(b)
    finally:
        proc.stdin.close();err=proc.stderr.read();code=proc.wait()
        put(IO/'publish-frozen-objects.operation.json',dict(args=args,start_utc=start,end_utc=utc(),exit=code,
            checked=len(checked),expected=len(rows),all_frozen_object_bytes_exact=(code==0 and len(checked)==len(rows)),
            stderr=err.decode(errors='replace'),objects=checked,
            qualification='Frozen local object bytes only; never live worktree substitution or source semantic credit.'))
    assert code==0 and len(checked)==len(rows)
    summary=semantic['summary.json'];core=semantic['core-manifest.json']
    registry=semantic['adjudication/root-primary-task-final-registry.final.json']
    assert summary['final_marker']==core['final_marker']=='UPDATE_NOT_STARTED'
    assert registry['count']==len(registry['accepted'])==29
    root_semantics=dict(authority='Root-owned exact frozen files; publication grants no semantic credit',
        summary_status=summary['status'],core_status=core['status'],
        root_registry_count=registry['count'],root_core_counts=core['counts'],
        exact_authority_files=[bypath[PREFIX+n] for n in semantic_names],
        handoff_publication='SUCCESSOR_REQUIRED_AFTER_THIS_REAL_CORE_COMMIT_AND_READBACK')
    data=b''.join((x['mode']+' '+x['blob']+'\t'+x['path']).encode()+b'\0' for x in rows)
    git('update-index','-z','--index-info',label='publish-exact-update-index',stdin=data)
    cached={x.decode() for x in git('diff','--cached','--name-only','-z',label='publish-staged-paths').split(b'\0') if x}
    assert cached==set(bypath)
    tree=git('write-tree',label='publish-index-tree').decode().strip()
    assert git('rev-parse',tree+':deliverables/final-specification-set',label='publish-formal-guard').decode().strip()==FORMAL
    delta=git('diff','--name-only','-z',HEAD,tree,label='publish-tree-delta')
    assert {x.decode() for x in delta.split(b'\0') if x}==set(bypath)
    treebytes=git('ls-tree','-r','-z',tree,'--',PREFIX.rstrip('/'),label='publish-exact-index-members')
    actual={}
    for line in treebytes.split(b'\0'):
        if not line:continue
        meta,path=line.split(b'\t',1);actual[path.decode()]=tuple(meta.decode().split())
    assert all(actual[x['path']]==(x['mode'],x['type'],x['blob']) for x in rows)
    assert git('rev-parse','HEAD',label='publish-final-parent-guard').decode().strip()==HEAD
    assert git('ls-remote','origin','refs/heads/'+BRANCH,label='publish-remote-before').decode().split()==[HEAD,'refs/heads/'+BRANCH]
    git('commit','-m','review: checkpoint 35 completed eighth-review semantic core',label='publish-commit')
    commit=git('rev-parse','HEAD',label='publish-commit-id').decode().strip();assert commit!=HEAD
    assert git('rev-parse','HEAD^{tree}',label='publish-commit-tree').decode().strip()==tree
    assert git('rev-parse','HEAD^',label='publish-commit-parent').decode().strip()==HEAD
    assert not git('diff','--cached','--name-only','-z',label='publish-postcommit-index')
    reporttree=git('rev-parse',commit+':'+PREFIX.rstrip('/'),label='publish-report-tree').decode().strip()
    git('push','origin','HEAD:refs/heads/'+BRANCH,label='publish-push')
    assert git('ls-remote','origin','refs/heads/'+BRANCH,label='publish-remote-after').decode().split()==[commit,'refs/heads/'+BRANCH]
    push=dict(schema='gr8-checkpoint35-ordinary-commit-push-receipt/v1',utc=utc(),status='PUSH_SUCCEEDED_REMOTE_REF_EXACT',
        parent=HEAD,commit=commit,workspace_tree=tree,report_tree=reporttree,branch=BRANCH,remote_ref='refs/heads/'+BRANCH,
        candidate_sha256=candidate_sha,committed_paths=len(rows),committed_bytes=sum(x['bytes'] for x in rows),
        frozen_root_semantics=root_semantics,new_contexts=0,new_votes=0,new_source_FULL_credit=0,
        semantic_credit='NONE added by transport; retain actual root-owned frozen semantic scope',
        business='NOT_EXECUTED',UPDATE_NOT_STARTED=True,post_freeze_root_writes_not_staged=True,events=list(events))
    put(PUB/'checkpoint-35-push-receipt.json',push)
    print(json.dumps({k:push[k] for k in ['status','commit','workspace_tree','report_tree','committed_paths','committed_bytes']},ensure_ascii=False),flush=True)
    wrapper=PUB/'checkpoint-35-readback-wrapper.py'
    assert PREFIX+'publication/checkpoint-35-readback-wrapper.py' in bypath
    assert sha(wrapper.read_bytes())==bypath[PREFIX+'publication/checkpoint-35-readback-wrapper.py']['sha256']
    run([sys.executable,'-B',str(wrapper),commit,name],'publish-independent-remote-readback')
    proof=PUB/(name+'.json');receipt=json.loads(proof.read_bytes())
    assert receipt['status']=='VERIFIED' and receipt['commit']==commit and receipt['report_tree']==reporttree
    assert receipt['baseline_commit']==HEAD and receipt['compressed_original_count']==116
    adapter=bypath[PREFIX+'publication/checkpoint-35-adapted-incremental-readback.py']
    assert receipt['verifier_source_sha256']==adapter['sha256']
    done=dict(schema='gr8-checkpoint35-completed-publication/v1',utc=utc(),
        status='ORDINARY_COMMIT_PUSH_AND_FRESH_REMOTE_READBACK_VERIFIED',commit=commit,workspace_tree=tree,report_tree=reporttree,
        remote_ref='refs/heads/'+BRANCH,candidate_sha256=candidate_sha,push_receipt='publication/checkpoint-35-push-receipt.json',
        remote_readback=dict(path=str(proof.relative_to(RR)),bytes=proof.stat().st_size,sha256=sha(proof.read_bytes())),
        remote_files=receipt['count'],remote_bytes=receipt['bytes'],full_new_remote_blob_count=receipt['full_new_remote_blob_count'],
        reused_verified_blob_count=receipt['reused_verified_blob_count'],compressed_original_count=receipt['compressed_original_count'],
        compressed_original_bytes=receipt['compressed_original_bytes'],frozen_root_semantics=root_semantics,
        successor_handoff_publication='REQUIRED; actual identities now available to root; no future/self binding fabricated',
        proof_file_timing='Own C35 push/readback/IO/completion evidence is postcommit successor material, not included in the same C35 commit.',
        old_live_four_excluded=True,new_contexts=0,new_votes=0,new_source_FULL_credit=0,
        semantic_credit='NONE added by publication',business='NOT_EXECUTED',UPDATE_NOT_STARTED=True)
    put(PUB/'checkpoint-35-completed.json',done)
    print(json.dumps(done,ensure_ascii=False),flush=True)

if __name__=='__main__': main()
