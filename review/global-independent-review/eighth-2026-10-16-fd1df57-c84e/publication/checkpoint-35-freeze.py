"""Root explicitly authorized C35 freeze; metadata/transport only, no recovered code."""
from pathlib import Path
import datetime, hashlib, json, stat, subprocess, sys

W=Path('/workspace/pokemon-essentials-clean-room')
RR=W/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
PUB=RR/'publication';IO=PUB/'checkpoint-35-io'
PREFIX=str(RR.relative_to(W))+'/'
HEAD='81cc98eec7cc81706e51c8b274e9ff7042c0868b'
BRANCH='codex/review-eighth-20261016-fd1df57-c84e'
old_live={'tasks/pbs_creature_current_cloud/'+n for n in ['dependency-identities.json',
    'formal-dependency-identities.json','record-field-ledger.json','sync_current_state.py']}
events=[];hash_events=[]
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def oid(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def put(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def run(args,label,stdin=None):
    start=utc();p=subprocess.run(args,cwd=W,input=stdin,capture_output=True)
    e=dict(args=args,start_utc=start,end_utc=utc(),exit=p.returncode)
    for k,b in [('stdout',p.stdout),('stderr',p.stderr)]:
        path=IO/(label+'.'+k);assert not path.exists();path.write_bytes(b)
        e.update({k:str(path.relative_to(RR)),k+'_bytes':len(b),k+'_sha256':sha(b)})
    if stdin is not None:e.update(stdin_bytes=len(stdin),stdin_sha256=sha(stdin))
    path=IO/(label+'.operation.json');assert not path.exists();put(path,e);events.append(e)
    assert p.returncode==0,e
    return p.stdout
def git(*args,label):return run(['git','-C',str(W),*args],label)
def guard(label):
    assert git('rev-parse','HEAD',label=label+'-head').decode().strip()==HEAD
    assert git('branch','--show-current',label=label+'-branch').decode().strip()==BRANCH
    assert not git('diff','--cached','--name-only','-z',label=label+'-index')
def exact_relative(path):
    rel=Path(path)
    assert not rel.is_absolute() and '..' not in rel.parts
    assert not any(x.endswith('.git') for x in rel.parts)
    assert 'tmp_pack_' not in str(rel) and '__pycache__' not in rel.parts
    assert not str(rel).endswith(('.pyc','.tmp'))
    return str(rel)
def verify_identity(rel,entry):
    rel=exact_relative(rel);p=RR/rel
    st=p.lstat();assert stat.S_ISREG(st.st_mode) and not p.is_symlink()
    b=p.read_bytes();assert len(b)==entry['bytes'] and sha(b)==entry['sha256'],rel
    if 'blob' in entry:assert oid(b)==entry['blob'],rel
    return rel
def metadata(rel):
    p=RR/rel;st=p.lstat();assert stat.S_ISREG(st.st_mode) and not p.is_symlink()
    b=p.read_bytes();assert len(b)<100000000,rel
    fmt='RAW_BYTES_NOT_JSON'
    if p.suffix in ['.json','.jsonl','.ndjson']:
        if p.suffix in ['.jsonl','.ndjson']:
            lines=[x for x in b.splitlines() if x.strip()]
            for line in lines:json.loads(line)
            fmt='EXPLICIT_NDJSON_ALL_NONEMPTY_LINES_PARSED'
        else:
            json.loads(b);fmt='WHOLE_JSON_PARSED_MECHANICALLY'
    blob=oid(b);start=utc();q=subprocess.run(['git','-C',str(W),'hash-object','-w','--stdin'],input=b,capture_output=True)
    hash_events.append(dict(path=rel,args=['git','-C',str(W),'hash-object','-w','--stdin'],
        start_utc=start,end_utc=utc(),exit=q.returncode,stdin_bytes=len(b),stdin_sha256=sha(b),
        stdout=q.stdout.decode(errors='replace'),stderr=q.stderr.decode(errors='replace')))
    assert q.returncode==0 and q.stdout.decode().strip()==blob
    assert p.read_bytes()==b,('changed_during_freeze',rel)
    return dict(path=PREFIX+rel,mode='100644',type='blob',blob=blob,bytes=len(b),sha256=sha(b),
                actual_filesystem_mode=oct(stat.S_IMODE(st.st_mode)),format=fmt)

def main():
    assert sys.argv[1:]==['freeze-root-authorized']
    assert not (PUB/'checkpoint-35-candidates.json').exists()
    guard('freeze-initial')
    # New fresh guard instance, without replacing earlier preparation evidence.
    pre=(PUB/'checkpoint-35-prepare.py').read_text()
    pre=pre.replace("'preflight-%02d.%s'","'freeze-preflight-%02d.%s'").replace("checkpoint-35-preflight.json","checkpoint-35-freeze-preflight.json").replace('gr8-checkpoint35-preflight/v1','gr8-checkpoint35-freeze-preflight/v1')
    pp=PUB/'checkpoint-35-freeze-preflight.py';assert not pp.exists();pp.write_text(pre)
    run([sys.executable,'-B',str(pp)],'freeze-fresh-protected-preflight')
    corepath=RR/'core-manifest.json';core_raw=corepath.read_bytes()
    assert len(core_raw)==563500 and sha(core_raw)=='d2650e97c5e8e3d2ed8f6c71de810fd7077036ebb1ef7cd5e5c31fa4dd09f7b8'
    fr=(RR/'final-report.md').read_bytes()
    assert len(fr)==18978 and sha(fr)=='97acfb99c89ddc9cc235f4529fdd69942037504fd75a4cea45e514430e8abe6e'
    core=json.loads(core_raw);assert len(core['core_authority_payloads'])==51
    allow={verify_identity(x['path'],x) for x in core['core_authority_payloads']}
    allow.add('core-manifest.json')
    # Root's exact five-packet byte reception fixes membership and identities.
    packet_receipt=json.loads((RR/'adjudication/root-final-history-and-membership-byte-reception.v1.json').read_bytes())
    packet_sets=[]
    for packet in packet_receipt['packets']:
        mp=packet['manifest'];mb=(RR/mp).read_bytes()
        assert len(mb)==packet['manifest_bytes'] and sha(mb)==packet['manifest_sha256']
        allow.add(exact_relative(mp))
        for x in packet['files']:allow.add(verify_identity(x['path'],x))
        packet_sets.append({k:packet[k] for k in ['manifest','manifest_bytes','manifest_sha256','checked_files','checked_bytes']})
    assert sum(x['checked_files'] for x in packet_sets)==218
    # Last qualified finite execution-classification contribution.
    em='tasks/creature_b/final-execution-classification/manifest.json'
    eraw=(RR/em).read_bytes();ex=json.loads(eraw)
    assert ex['file_count']==17 and ex['total_bytes']==119833
    assert sha(eraw).startswith('32eae71')
    allow.add(em)
    for x in ex['files']:
        allow.add(verify_identity(str(Path(em).parent/x['path']),x))
    # Root completed and explicitly authorized both exact handoff preparation trees.
    handoff_roots=['tasks/handoff_final_five_root_deltas/effective39',
                   'tasks/handoff_final_five_root_deltas/final-binding-preparation']
    for root in handoff_roots:
        for p in (RR/root).rglob('*'):
            if p.is_file():allow.add(exact_relative(str(p.relative_to(RR))))
    changed=set(x.decode() for x in git('diff','--name-only','-z',HEAD,label='freeze-tracked-snapshot').split(b'\0') if x)
    changed.update(x.decode() for x in git('ls-files','--others','--exclude-standard','-z',label='freeze-untracked-snapshot').split(b'\0') if x)
    assert all(x.startswith(PREFIX) for x in changed)
    # Completed root receipts are within the explicit root-owned freeze scope.
    for path in changed:
        rel=path[len(PREFIX):]
        if rel.startswith('adjudication/'):allow.add(exact_relative(rel))
        if rel.startswith('publication/checkpoint-34-') or rel.startswith('publication/checkpoint-35-'):
            allow.add(exact_relative(rel))
    allow.update(['publication/r8-four-receivers-and-metadata-readback-34.json',
                  'publication/semantic-core-precommit-check.v1.json'])
    # Compressed original duplicates are excluded only after exact full-byte SHA.
    comp=json.loads((PUB/'compressed-artifacts.json').read_bytes())['artifacts'];assert len(comp)==116
    cmap={x['original_path']:x for x in comp};materialized=[]
    for x in comp:
        p=RR/x['original_path']
        if p.exists():
            st=p.lstat();assert stat.S_ISREG(st.st_mode) and not p.is_symlink()
            h=hashlib.sha256();size=0
            with p.open('rb') as f:
                while b:=f.read(4*1024*1024):h.update(b);size+=len(b)
            materialized.append(dict(path=x['original_path'],bytes=size,sha256=h.hexdigest(),
                matches_published_compressed_original=size==x['original_bytes'] and h.hexdigest()==x['original_sha256']))
        assert (RR/x['container_path']).is_file()
    mat={x['path']:x for x in materialized}
    selected=[];excluded=[]
    for path in sorted(changed):
        rel=path[len(PREFIX):]
        if rel in old_live:
            excluded.append(dict(path=path,reason='EXPLICIT_OLD_LIVE_PBS_CURRENT_UNQUALIFIED_VERSION_PRESERVE_LOCAL'));continue
        if rel not in allow:
            excluded.append(dict(path=path,reason='OUTSIDE_EXACT_COMPLETED_ROOT_PACKET_OR_PUBLICATION_SCOPE_PRESERVE_LOCAL'));continue
        if rel in mat and mat[rel]['matches_published_compressed_original']:
            excluded.append(dict(path=path,reason='EXACT_PUBLISHED_GZIP_ORIGINAL_BYTES_AND_SHA_MATCH',bytes=mat[rel]['bytes'],sha256=mat[rel]['sha256']));continue
        selected.append(metadata(exact_relative(rel)))
    guard('freeze-final')
    # Include all already completed own freeze IO, not the future/self manifest.
    existing={x['path'] for x in selected}
    for p in sorted(IO.rglob('*')):
        if p.is_file() and str(p.relative_to(W)) not in existing:
            selected.append(metadata(str(p.relative_to(RR))));existing.add(str(p.relative_to(W)))
    # The complete object-write log remains local evidence, added by exact bytes.
    log=IO/'freeze-hash-object-events.json';assert not log.exists()
    put(log,dict(events=hash_events,semantic_credit='NONE'))
    selected.append(metadata(str(log.relative_to(RR))))
    freeze=dict(schema='gr8-checkpoint35-exact-frozen-candidates/v1',utc=utc(),baseline_HEAD=HEAD,branch=BRANCH,
        root_authorized_freeze=True,root_authorization='Explicit FREEZE C35 CORE received in original /root/com_move context',
        files=selected,count=len(selected),bytes=sum(x['bytes'] for x in selected),
        frozen_root_core=dict(path='core-manifest.json',bytes=len(core_raw),sha256=sha(core_raw),status=core['status'],counts=core['counts']),
        frozen_root_summary_status=json.loads((RR/'summary.json').read_bytes())['status'],
        root_registry_count=29,known_actual_contexts=125,new_contexts=0,new_votes=0,new_source_FULL_credit=0,
        packet_sets=packet_sets,explicit_old_live_exclude_paths=sorted(old_live),excluded=excluded,
        materialized_original_identity_checks=materialized,compressed_original_map_entries=116,
        candidate_envelope='publication/checkpoint-35-candidates.json added separately by exact preannounced SHA; no self-hash recursion',
        all_rows_regular_nonexecuting_git_mode=True,all_rows_under_100MB=True,
        post_freeze_rule='Stage only exact frozen Git objects; do not stage root later writes',
        business='NOT_EXECUTED',UPDATE_NOT_STARTED=True,semantic_credit='NONE added by publication; root-owned semantic core preserved')
    assert not (set(x['path'] for x in selected)&{PREFIX+x for x in old_live})
    manifest=PUB/'checkpoint-35-candidates.json';put(manifest,freeze)
    raw=manifest.read_bytes()
    print(json.dumps(dict(status='C35_EXACT_CANDIDATES_FROZEN',count=len(selected),bytes=freeze['bytes'],
        candidate_path=str(manifest.relative_to(RR)),candidate_bytes=len(raw),candidate_sha256=sha(raw),
        root_summary_status=freeze['frozen_root_summary_status'],root_registry=29,known_contexts=125,
        excluded=len(excluded),old_live_excluded=4,materialized_originals=len(materialized),
        materialized_exact_matches=sum(x['matches_published_compressed_original'] for x in materialized),fresh_protected_preflight='PASS'),ensure_ascii=False),flush=True)

if __name__=='__main__':main()
