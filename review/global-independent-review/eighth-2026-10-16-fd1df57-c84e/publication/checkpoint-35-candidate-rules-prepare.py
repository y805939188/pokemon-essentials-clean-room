"""Read-only worktree metadata snapshot and proposed rules; no candidate freeze."""
from pathlib import Path
import collections, datetime, hashlib, json, os, stat, subprocess

W = Path('/workspace/pokemon-essentials-clean-room')
RR = W/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
PUB = RR/'publication'
IO = PUB/'checkpoint-35-io'
PREFIX = str(RR.relative_to(W))+'/'
HEAD = '81cc98eec7cc81706e51c8b274e9ff7042c0868b'
old_live = ['tasks/pbs_creature_current_cloud/'+x for x in [
    'dependency-identities.json', 'formal-dependency-identities.json',
    'record-field-ledger.json', 'sync_current_state.py']]
events = []

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def run(args, label, stdin=None):
    start = utc()
    p = subprocess.run(args, input=stdin, capture_output=True)
    out = dict(args=args, start_utc=start, end_utc=utc(), exit=p.returncode)
    for k,v in [('stdout',p.stdout),('stderr',p.stderr)]:
        f = IO/('rules-'+label+'.'+k)
        assert not f.exists()
        f.write_bytes(v)
        out.update({k:str(f.relative_to(RR)), k+'_bytes':len(v),k+'_sha256':sha(v)})
    events.append(out)
    assert p.returncode==0, out
    return p.stdout

def git(*args,label):
    return run(['git','-C',str(W),*args],label)

def ident(path):
    p = W/path
    before = p.lstat()
    assert stat.S_ISREG(before.st_mode) and not p.is_symlink()
    h = hashlib.sha256()
    b = hashlib.sha1(b'blob '+str(before.st_size).encode()+b'\0')
    size = 0
    with p.open('rb') as source:
        while data := source.read(4*1024*1024):
            size += len(data)
            h.update(data)
            b.update(data)
    after = p.lstat()
    return dict(bytes=size,sha256=h.hexdigest(),blob=b.hexdigest(),type='blob',
                prospective_git_mode='100644',posix_mode=oct(stat.S_IMODE(after.st_mode)),
                regular=True,stable_during_metadata_read=(before.st_ino,before.st_size,before.st_mtime_ns)==(after.st_ino,after.st_size,after.st_mtime_ns),
                frozen=False)

assert git('rev-parse','HEAD',label='head').decode().strip()==HEAD
assert not git('diff','--cached','--name-only','-z',label='index')
tracked = sorted(x.decode() for x in git('diff','--name-only','-z',HEAD,label='tracked').split(b'\0') if x)
untracked = sorted(x.decode() for x in git('ls-files','--others','--exclude-standard','-z',label='untracked').split(b'\0') if x)
assert all(x.startswith(PREFIX) for x in tracked+untracked)
old = {}
raw = git('ls-tree','-r','-z',HEAD,'--',*tracked,label='tracked-base-tree')
for entry in raw.split(b'\0'):
    if not entry: continue
    meta,path=entry.split(b'\t',1)
    mode,typ,blob=meta.decode().split()
    old[path.decode()]=dict(mode=mode,type=typ,blob=blob)
check = run(['git','-C',str(W),'cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)'],
            'tracked-base-sizes', ''.join(x['blob']+'\n' for x in old.values()).encode())
sizes = {x.split()[0]:int(x.split()[2]) for x in check.decode().splitlines()}
rows=[]
for path in tracked:
    rel=path[len(PREFIX):]
    base=old[path];base['bytes']=sizes[base['blob']]
    disposition='EXPLICITLY_EXCLUDED_OLD_LIVE_QUALIFICATION_NOT_GRANTED' if rel in old_live else 'PENDING_ROOT_COMPLETION_AND_EXACT_FREEZE'
    rows.append(dict(path=rel,baseline=base,observed_worktree=ident(path),candidate_disposition=disposition))

prior33=json.loads((PUB/'checkpoint-33-exact-selection.json').read_bytes())
prior34=json.loads((PUB/'checkpoint-34-candidates.json').read_bytes())
def paths_any(value):
    out=[]
    if isinstance(value,dict):
        for key,v in value.items():
            if key=='path' and isinstance(v,str):out.append(v)
            elif isinstance(v,(dict,list)):out.extend(paths_any(v))
    elif isinstance(value,list):
        for v in value:out.extend(paths_any(v))
    return out
# Compare actual commit deltas as the decisive publication-membership check.
delta33=git('diff-tree','--no-commit-id','--name-only','-r','-z','c7fec918d511a0ead8ab325c934e9346d7c43cac',label='c33-members')
delta34=git('diff-tree','--no-commit-id','--name-only','-r','-z',HEAD,label='c34-members')
s33={x.decode() for x in delta33.split(b'\0') if x}
s34={x.decode() for x in delta34.split(b'\0') if x}
old_exclusions=[]
for rel in old_live:
    path=PREFIX+rel
    assert path not in s33 and path not in s34
    matches=[x for x in prior34['excluded'] if x['path']==path]
    old_exclusions.append(dict(path=rel,C33_commit_changed_path_member=False,C34_commit_changed_path_member=False,
                               C34_original_exclusion=matches,rule='PRESERVE_LOCAL_DO_NOT_STAGE_DO_NOT_PROMOTE_QUALIFICATION'))

byte_receipt='adjudication/root-final-history-and-membership-byte-reception.v1.json'
raw=(RR/byte_receipt).read_bytes()
receipt=json.loads(raw)
packets=[]
for packet in receipt['packets']:
    manifest=packet['manifest']
    mb=(RR/manifest).read_bytes()
    assert len(mb)==packet['manifest_bytes'] and sha(mb)==packet['manifest_sha256']
    packets.append({k:packet[k] for k in ['manifest','manifest_bytes','manifest_sha256','checked_files','checked_bytes','all_exact']})
groups=collections.Counter('/'.join(x[len(PREFIX):].split('/')[:2]) for x in untracked)
snapshot=dict(schema='gr8-checkpoint35-tracked-metadata-snapshot/v1',utc=utc(),status='READ_ONLY_LIVE_SNAPSHOT_NOT_FREEZE',
              baseline_HEAD=HEAD,tracked_count=len(rows),rows=rows,untracked_count=len(untracked),
              untracked_group_counts=dict(sorted(groups.items())),old_live_explicit_exclusions=old_exclusions,
              events=events,candidate_freeze='NOT_STARTED',staging='NOT_STARTED',commit='NOT_STARTED',push='NOT_STARTED',
              semantic_credit='NONE',source_FULL_added=0,new_contexts=0,new_votes=0,business='NOT_EXECUTED',UPDATE_NOT_STARTED=True)
f=PUB/'checkpoint-35-tracked-metadata.json';assert not f.exists();f.write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
rules=dict(schema='gr8-checkpoint35-candidate-rules-proposal/v1',utc=utc(),status='PROPOSED_AWAITING_ROOT_FREEZE_WINDOW',
    baseline_HEAD=HEAD,index_empty_at_snapshot=True,
    explicit_exclude_paths=old_live,
    exclude_path_components=['any component ending .git','__pycache__'],
    exclude_path_substrings=['tmp_pack_'],exclude_suffixes=['.pyc','.tmp'],
    exclude_unqualified_scopes=['all non-explicit evidence/external-recovered caches','old c699d364 ELR duplicate cache and matching recovery JSON','all non-explicit old unqualified target/counter directories'],
    preserve_unselected_local=True,
    materialized_compressed_original_rule='Exclude only after exact bytes and SHA256 match the published 116-entry map. Keep all published gzip containers; never delete local originals.',
    prospective_include_authority='Root completed final files and exact named receipts/manifests only, frozen after root supplies window; no whole-RR or whole-task default.',
    prospective_root_completed_scopes=['adjudication/ exact completed files, including current29 ABI and formal_shared receipts','root final-report/summary/current final coverage exact paths supplied at freeze'],
    accepted_five_packet_receipt=dict(path=byte_receipt,bytes=len(raw),sha256=sha(raw)),
    accepted_five_packets=packets,
    accepted_packet_selection_rule='Use exact manifest plus root-receipted payload members, preserve original versions and all qualification fields; no inferred directory-wide qualification.',
    handoff_preparation_manifest_paths=['tasks/handoff_final_five_root_deltas/effective39/delivery-manifest.json','tasks/handoff_final_five_root_deltas/final-binding-preparation/manifest.json'],
    handoff_rule='Include exact completed effective39 payloads, both prior-freeze archives and final-binding-preparation after root authorizes exact freeze; do not bind future core/self commit.',
    publication_rule='Include completed C34 success receipts/proof and retained actual C34 failure/recovery IO; C35 prep evidence may be included only at exact freeze. No blind old wrapper execution.',
    freeze_validation=['HEAD fixed and index empty','fresh nine protected checks','regular files only, no symlink/submodule or .git components','single file under 100MB','exact path/mode/blob/bytes/SHA256 for every selected file','JSON or explicit NDJSON parse/anomaly qualification','freeze stable bytes and stage only their exact Git blobs','never stage later root writes'],
    snapshot='publication/checkpoint-35-tracked-metadata.json',
    staging='NOT_STARTED',candidate_freeze='NOT_STARTED',commit='NOT_STARTED',push='NOT_STARTED',
    semantic_credit='NONE',source_FULL_added=0,new_contexts=0,new_votes=0,business='NOT_EXECUTED',UPDATE_NOT_STARTED=True)
f=PUB/'checkpoint-35-candidate-rules.json';assert not f.exists();f.write_text(json.dumps(rules,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=rules['status'],tracked_count=len(rows),old_live_excluded=len(old_exclusions),C33_C34_old_live_not_members=True,
                     root_received_packet_count=len(packets),root_received_payloads=sum(x['checked_files'] for x in packets),
                     root_received_bytes=sum(x['checked_bytes'] for x in packets),index_empty=True),ensure_ascii=False))
