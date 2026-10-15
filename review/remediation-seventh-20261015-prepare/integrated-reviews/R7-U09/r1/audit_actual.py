"""Bounded byte/document audit only; never execute restored evidence or reference code."""
from pathlib import Path
import datetime, hashlib, json, os, subprocess, urllib.request, urllib.parse

ROOT = Path('/workspace/r7-ir-R7-U09')
OUT = Path(__file__).resolve().parent
CHECKOUT = ROOT / 'checkout'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
MI = '45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI = '13d76ba61838b13925ba9d41f58a6b047564d926'
PREFIX = 'deliverables/final-specification-set/'
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p): return json.loads(p.read_text())
def ident(b): return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest())
def match(b, e):
    a=ident(b)
    for k,v in a.items():
        key='git_blob_content_id' if k=='git_blob' and 'git_blob_content_id' in e else k
        if key in e: assert e[key]==v, (key,e[key],v)
    return a
def git(*args): return subprocess.check_output(['git',*args],cwd=CHECKOUT)
def fetch(path, commit, target, expected=None):
    if target.exists():
        b=target.read_bytes()
        if expected: match(b,expected)
        return b
    target.parent.mkdir(parents=True,exist_ok=True)
    u=f'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/{commit}/'+urllib.parse.quote(path)
    start=utc()
    with urllib.request.urlopen(u,timeout=40) as r: b=r.read((expected or {}).get('bytes',2000000)+1); status=r.status
    if expected: match(b,expected)
    with target.open('xb') as f:f.write(b)
    downloads.append(dict(url=u,path=str(target),start_utc=start,end_utc=utc(),http_status=status,**ident(b)))
    (OUT/'audit-downloads.json').write_text(json.dumps(downloads,ensure_ascii=False,indent=2)+'\n')
    return b

start=utc(); downloads=read(OUT/'audit-downloads.json') if (OUT/'audit-downloads.json').exists() else []; receipt=dict(start_utc=start,pid=os.getpid(),scope='TOOL_VALIDATION_ONLY_NO_SEMANTIC_OR_RUNTIME_CREDIT')
fi=read(ROOT/'supplemental/integrated-input.json')
assert fi['actual_MI']==MI and fi['actual_MI_tree']=='6480ffe3df49bd9776c719f3c9be1c13618fdb0a'
assert read(ROOT/'supplemental/MI-git-metadata.json')['tree']['sha']==fi['actual_MI_tree']
assert read(ROOT/'supplemental/FI-git-metadata.json')['tree']['sha']=='6747a584b91c86acd4771c1a6dee93260602106f'
assert read(ROOT/'supplemental/FI-git-metadata.json')['parents'][0]['sha']==MI
assert read(ROOT/'supplemental/MI-deliverables-tree.json')['tree'][0]['sha']==fi['actual_formal_subtree']
assert any(x['path']=='deliverables' and x['sha']==read(ROOT/'supplemental/MI-deliverables-tree.json')['sha'] for x in read(ROOT/'supplemental/MI-root-tree.json')['tree'])
assert read(ROOT/'supplemental/R-git-metadata.json')['tree']['sha']=='7589c800b61ba13a13040ed0d686979b80a84fd0'
tree=read(ROOT/'supplemental/MI-formal-tree.json'); assert not tree['truncated']
blobs={PREFIX+x['path']:x for x in tree['tree'] if x['type']=='blob'}
assert len(blobs)==131 and set(blobs)=={r['path'] for r in fi['all_formal_file_identities']}
rows=[]; formal={}
for row in fi['all_formal_file_identities']:
    p=row['path']; t=blobs[p]; assert t['sha']==row['git_blob'] and t['mode']==row['git_mode']=='100644' and t['size']==row['bytes']
    base=git('show',B+':'+p);match(base,row['base_B_identity'])
    changed=ident(base)['git_blob']!=t['sha'];assert changed==row['changed_against_B']
    if not changed: b=base; source='B_GIT_OBJECT_SAME_MI_TREE_BLOB'
    else:
        candidates=[ROOT/'actual-input/actual'/p,ROOT/'supplemental/actual'/p]
        target=next((x for x in candidates if x.exists()),ROOT/'supplemental/formal'/p)
        b=fetch(p,MI,target,row);source=str(target)
    match(b,row);formal[p]=b
    rows.append(dict(path=p,**ident(b),git_mode=t['mode'],changed_against_B=changed,actual_bytes_source=source))
assert sum(x['changed_against_B'] for x in rows)==26
receipt['formal_131']=rows;receipt['formal_counts']=dict(all=131,changed=26,unchanged=105)
# Recompute the complete formal subtree from the independently verified bytes.
def tree_id(node):
    entries=[]
    for name,v in node.items():
        mode='40000' if isinstance(v,dict) else '100644'; sha=tree_id(v) if isinstance(v,dict) else ident(v)['git_blob']
        entries.append((name+('/' if isinstance(v,dict) else ''),mode.encode()+b' '+name.encode()+b'\0'+bytes.fromhex(sha)))
    body=b''.join(v for _,v in sorted(entries))
    return hashlib.sha1(f'tree {len(body)}\0'.encode()+body).hexdigest()
node={}
for p,b in formal.items():
    parts=p[len(PREFIX):].split('/'); d=node
    for a in parts[:-1]:d=d.setdefault(a,{})
    d[parts[-1]]=b
assert tree_id(node)==fi['actual_formal_subtree']
receipt['recomputed_formal_tree']=tree_id(node)
# Verify both restoration plans and all 86 selected restored members again.
restored=[]
for kind,dest in [('original','original'),('actual','actual-input')]:
    plan=read(ROOT/(kind+'-plans/R7-U09.json')); members=[]
    for row in plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']:
        members.append(dict(local_path=row['local_path'],**match((ROOT/dest/row['local_path']).read_bytes(),row)))
    restored.append(dict(kind=kind,files=len(members),bytes=sum(x['bytes'] for x in members),members=members))
receipt['restorations']=restored
j=read(ROOT/'actual-input/integration/applied-clauses.json');own=[];assembly=[]
for f in j['files']:
    p=f['path'];exists=bool(git('ls-tree',B,'--',p));base=git('show',B+':'+p) if exists else b'';match(base,f['baseline_identity']);lines=base.splitlines(keepends=True);cursor=0;chunks=[]
    for h in f['hunks']:
        a,b=h['base_line_indices_half_open'];assert a>=cursor
        removed=b''.join(lines[a:b]);added=h['added_text'].encode();assert removed==h['removed_text'].encode()
        match(removed,h['removed_identity']);match(added,h['added_identity']);chunks += [b''.join(lines[cursor:a]),added];cursor=b
        if h['batch_id']=='R7-U09':own.append(dict(path=p,**h))
    assembled=b''.join(chunks+[b''.join(lines[cursor:])]);match(assembled,f['assembled_candidate_clauses_identity'])
    current=formal.get(p)
    if current is None: current=fetch(p,MI,ROOT/'supplemental/administrative'/p)
    adjustment=next((a for a in j['root_administrative_reception_adjustments'] if a['path']==p),None)
    if adjustment:
        match(assembled,adjustment['before_identity']);match(current,adjustment['after_identity'])
        if 'added_text' in adjustment: assert current==assembled+adjustment['added_text'].encode()
        else:
            before=json.loads(assembled);after=json.loads(current)
            receipt['administrative_errata_changed_fields']=[dict(field=k,before=before.get(k),after=after.get(k)) for k in set(before)|set(after) if before.get(k)!=after.get(k)]
    else:assert current==assembled,p
    assembly.append(dict(path=p,contributors=f['contributors'],hunks=len(f['hunks']),actual_bytes_match=True,semantic_credit_for_other_batches=False))
    if 'R7-U09' in f['contributors']:
        assert f['contributors']==['R7-U09']
        c=(ROOT/'actual-input/candidate/candidates/R7-U09'/p).read_bytes();assert current==c
        for h in f['hunks']:
            a,b=h['actual_final_line_indices_half_open'];assert b''.join(current.splitlines(keepends=True)[a:b])==h['added_text'].encode()
assert len(own)==6 and sum(x['hunks'] for x in assembly)==56 and len(assembly)==24
receipt['assembly']=assembly;receipt['own_six_hunks']=own
old=ROOT/'actual-input/prior-accepted/actual-at-accepted-MI'
receipt['prior_five_preservation']=[]
for p in old.rglob('*.md'):
    rel=p.relative_to(old).as_posix();assert formal[rel]==p.read_bytes();receipt['prior_five_preservation'].append(dict(path=rel,**ident(p.read_bytes()),mechanical_only=True))
assert len(receipt['prior_five_preservation'])==5
contract=read(ROOT/'original/dispatch/delegation/contracts/R7-U09.json');refs={}
def walk(x):
    if isinstance(x,dict):
        if 'raw_member_byte_offsets' in x: refs[(x['input_sha256'],tuple(x['raw_member_byte_offsets']))]=x
        for v in x.values():walk(v)
    elif isinstance(x,list):
        for v in x:walk(v)
walk(contract);receipt['raw_members']=[]
for (sha,(a,b)),ref in refs.items():
    p=ROOT/f'original/evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs/{sha}.raw';data=p.read_bytes();part=data[a:b]
    assert len(part)==ref['raw_member_bytes'] and hashlib.sha256(part).hexdigest()==ref['raw_member_sha256']
    value=json.loads(data)
    for key in ref['json_pointer'].strip('/').split('/'):
        key=key.replace('~1','/').replace('~0','~');value=value[int(key)] if isinstance(value,list) else value[key]
    assert value==json.loads(part)
    receipt['raw_members'].append(dict(pointer=ref['json_pointer'],bytes=len(part),sha256=hashlib.sha256(part).hexdigest(),slice_matches_pointer=True))
catalog=formal[PREFIX+'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'].decode().splitlines()
receipt['vectors']=[]
author=read(ROOT/'actual-input/candidate/candidates/R7-U09/evidence/author/per-id.json')
reviewer=read(ROOT/'actual-input/candidate-review/candidates/R7-U09/evidence/reviewer/r1/per-id.json')
for rec in author['records']:
    for v in rec['vectors']:
        row=catalog[v['candidate_line']-1];assert row==v['candidate_row'] and 'NOT_EXECUTED' in row
        assert sum('| '+v['id']+' |' in x for x in catalog)==1
        rv=next(z for r in reviewer['records'] for z in r['vector_review'] if z['id']==v['id'])
        match(row.encode(),rv['candidate_row_identity_without_LF'])
        receipt['vectors'].append(dict(id=v['id'],line=v['candidate_line'],**ident(row.encode()),execution='NOT_EXECUTED',document_identity_check_only=True))
assert len(receipt['vectors'])==14
# Count base species headers as data, without evaluating reference expressions.
species=(ROOT/'supplemental/reference/PBS/pokemon.txt').read_text(encoding='utf-8-sig').splitlines()
headers=[x.strip()[1:-1] for x in species if x.strip().startswith('[') and x.strip().endswith(']')]
assert headers.index('CHIKORITA')+1==152
receipt['static_data_count']=dict(CHIKORITA_base_header_ordinal=152,reference_expressions_executed=0)
receipt['skills_checked']={str(p):dict(exists=p.exists(),files=[str(f) for f in p.rglob('SKILL.md')] if p.exists() else []) for p in [Path('/workspace/.agents/skills'),CHECKOUT/'.agents/skills',Path.home()/'.agents/skills']}
assert all(not x['files'] for x in receipt['skills_checked'].values())
receipt['identity']=dict(actual_thread_id=os.environ.get('CODEX_THREAD_ID'),source='CODEX_THREAD_ID',actual_context_id='NOT_EXPOSED',children_created=0,effective_configuration='UNVERIFIED')
assert receipt['identity']['actual_thread_id']=='01a1401c-5207-71b6-b9fe-3916211c003d'
receipt.update(end_utc=utc(),status='BOUNDED_ACTUAL_BYTE_DOCUMENT_AUDIT_PASS',behavior_execution='NOT_EXECUTED',reference_host_Demo_native_full_model_real_save_replay=0)
(OUT/'audit-result.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],formal_files=131,changed=26,unchanged=105,actual_formal_tree=receipt['recomputed_formal_tree'],own_hunks=6,all_assembled_hunks=56,restored_files=sum(x['files'] for x in restored),raw_members=len(refs),vectors=14,pid=os.getpid(),semantic_PASS_from_audit=False)))
