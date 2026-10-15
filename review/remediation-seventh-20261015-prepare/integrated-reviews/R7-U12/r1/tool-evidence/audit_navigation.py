"""New independent navigation/raw-binding checks, not execution of behavior vectors."""
from pathlib import Path
import datetime
import gzip
import hashlib
import json
import posixpath
import re
import subprocess
import urllib.request

ROOT=Path('/workspace/r7-ir-R7-U12')
OUT=Path(__file__).resolve().parent
A=ROOT/'actual-input'
O=ROOT/'original'
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
H='e58486178e746273fb6fab55df00722807f1dc44'
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(d): return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest())
def verify(d,row):
    got=ident(d)
    for k,v in row.items():
        k='git_blob' if k in ['blob','git_blob_content_id'] else k
        if k in got: assert got[k]==v,(k,got[k],v)
    return got
def git(*args): return subprocess.check_output(['git','-C',str(ROOT/'checkout'),*args])
def save(name,data): (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def pointer(obj,p):
    for key in p.split('/')[1:]:
        key=key.replace('~1','/').replace('~0','~')
        obj=obj[int(key)] if isinstance(obj,list) else obj[key]
    return obj

contract=json.loads((O/'dispatch/delegation/contracts/R7-U12.json').read_bytes())
inputs={hashlib.sha256(p.read_bytes()).hexdigest():p for p in (O/'evidence').rglob('*') if p.is_file()}
refs={}
def walk(v):
    if isinstance(v,dict):
        if 'raw_member_byte_offsets' in v: refs[(v['input_sha256'],v['json_pointer'])]=v
        for value in v.values(): walk(value)
    elif isinstance(v,list):
        for value in v: walk(value)
walk(contract)
bindings=[]
for (sha,ptr),ref in refs.items():
    raw=inputs[sha].read_bytes();a,b=ref['raw_member_byte_offsets'];part=raw[a:b]
    assert len(part)==ref['raw_member_bytes']
    assert hashlib.sha256(part).hexdigest()==ref['raw_member_sha256']
    value=pointer(json.loads(raw),ptr); assert json.loads(part)==value
    canonical=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(canonical).hexdigest()==ref['canonical_sha256']
    bindings.append(dict(pointer=ptr,raw_sha=sha,offsets=[a,b],member_sha=ref['raw_member_sha256'],pointer_match=True,canonical_match=True))
save('original-raw-bindings.json',dict(count=len(bindings),bindings=bindings,qualification='Structure and exact bytes only, no inherited semantic PASS.'))

files=['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md']
universes={c:set(git('ls-tree','-r','--name-only',c).decode().splitlines()) for c in [B,MI]}
def links(c,path):
    rows=[]
    for number,line in enumerate(git('show',c+':'+path).decode().splitlines(),1):
        for label,href in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',line):
            if '://' in href or href.startswith('#'):continue
            resolved=posixpath.normpath(posixpath.join(posixpath.dirname(path),href.split('#')[0]))
            directory=any(n.startswith(resolved.rstrip('/')+'/') for n in universes[c])
            rows.append(dict(path=path,line=number,label=label,href=href,resolved=resolved,directory=directory,exists=resolved in universes[c] or directory))
    return rows
baseline=sum([links(B,p) for p in files],[])
current=sum([links(MI,p) for p in files],[])
missing=[r for r in baseline if not r['exists']]
assert (len(baseline),len(missing),len(set(r['resolved'] for r in missing)))==(136,10,4)
assert len(current)==126 and all(r['exists'] for r in current)
assert [(r['label'],r['href']) for r in baseline if r['exists']]==[(r['label'],r['href']) for r in current]
urls=[];scope=[]
for path in files:
    data=git('show',MI+':'+path); b=git('show',B+':'+path)
    candidate=(A/'candidate/candidates/R7-U12'/path).read_bytes(); assert candidate==data
    s=data.decode(); notes=[line for line in s.splitlines(keepends=True) if line.startswith('GR7-M19-001 历史导航勘误：')]
    assert len(notes)==1
    old=s.replace(notes[0]+'\n','')
    for target in sorted(set(r['resolved'] for r in missing)):
        url=f'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/{H}/{target}'
        count=old.count(url)
        if count:
            urls.extend([url]*count)
            old=old.replace(url,posixpath.relpath(target,posixpath.dirname(path)))
    assert old.encode()==b,path
    scope.append(dict(path=path,actual_identity=ident(data),reverse_to_B=True,note_prerequisites_explicit=True))
assert len(urls)==10 and len(set(urls))==4
recovered=[]
plan=json.loads((ROOT/'original-plans/R7-U12.json').read_bytes())
for row in plan['fixed_read_inputs']:
    if row['commit']!=H:continue
    data=(O/row['local_path']).read_bytes();verify(data,row)
    recovered.append(dict(path=row['path'],commit=H,**ident(data)))
controls=[]
for path,line in [('README.md',7),('CURRENT-DELIVERY.md',5),('delivery/2026-10-14-sixth/README.md',7)]:
    assert git('show',MI+':'+path)==git('show',B+':'+path)
    controls.append(dict(path=path,line=line,links=links(MI,path)))
save('m19-navigation-audit.json',dict(baseline_local=136,baseline_resolved=126,baseline_missing=missing,
    actual_local=126,actual_local_resolved=126,actual_historical_occurrences=10,actual_unique_historical_targets=4,
    current_links=current,scopes=scope,historical_files=recovered,normal_controls=controls,
    behavior_execution='NOT_EXECUTED',scope='Three entry files and exact controls only; no browser/fragment/all131 semantic link certificate.'))

errata_path='review/remediation-seventh-20261015-prepare/current-navigation-errata.json'
errata=json.loads(git('show',MI+':'+errata_path))
assert errata['status']=='INTEGRATED_PENDING_INDEPENDENT_ACTUAL_REVIEW'
assert errata['current_label']=='WP72 §5.3／WP27' and errata['old_label']=='WP72 §5.2／WP27'
source=errata['frozen_original'];frozen=git('show',B+':'+source['path']);verify(frozen,source)
assert git('show',MI+':'+source['path'])==frozen
assert pointer(json.loads(frozen),source['pointer'])==errata['old_label']
current_clause=errata['current_clause'];body=git('show',MI+':'+current_clause['path']);verify(body,current_clause)
rule=body.splitlines(keepends=True)[current_clause['rule_line']-1];verify(rule,current_clause['rule_line_identity_including_LF'])
assert b'5.3' in body.splitlines()[current_clause['heading_line']-1]
projections=[]
for p in errata['current_projections']:
    rows=[(i+1,l) for i,l in enumerate(git('show',MI+':'+p['path']).decode().splitlines()) if l.startswith('| R6-DX-DEBUG-001 |')]
    assert len(rows)==1 and errata['current_label'] in rows[0][1]
    b_rows=[l for l in git('show',B+':'+p['path']).decode().splitlines() if l.startswith('| R6-DX-DEBUG-001 |')]
    assert rows[0][1].split('|')[-2]==b_rows[0].split('|')[-2]
    projections.append(dict(path=p['path'],actual_line=rows[0][0],actual_text=rows[0][1],old_state_preserved=True))
source_ids=[]
for row in errata['fixed_source']['locators']:
    d=(O/'inputs/reference'/row['path']).read_bytes();source_ids.append(dict(path=row['path'],**verify(d,row),ranges=row['lines']))
save('h08-navigation-audit.json',dict(errata_identity=ident(git('show',MI+':'+errata_path)),frozen_original=ident(frozen),rule_identity=ident(rule),projections=projections,source_identities=source_ids,
    precedence=errata['precedence'],ACCEPTED=False,CLOSED=False,behavior_execution='NOT_EXECUTED'))

history=json.loads((A/'candidate-review/candidates/R7-U12/evidence/reviewer/r1/tool-evidence/provenance-receipt.json').read_bytes())
receipts=[]
for row in history['original_C01_pinned_remote_objects']:
    start=utc()
    with urllib.request.urlopen(row['url'],timeout=40) as response:
        encoded=response.read(row['encoded_identity']['bytes']+1);status=response.status
    verify(encoded,row['encoded_identity'])
    with gzip.GzipFile(fileobj=__import__('io').BytesIO(encoded)) as stream: decoded=stream.read(row['decoded_identity']['bytes']+1)
    verify(decoded,row['decoded_identity'])
    retained=A/'candidate-review/candidates/R7-U12/evidence/reviewer/r1/tool-evidence/original-C01'/row['logical_path']
    assert retained.read_bytes()==decoded
    receipts.append(dict(logical_path=row['logical_path'],url=row['url'],start_utc=start,end_utc=utc(),http_status=status,encoded_identity=ident(encoded),decoded_identity=ident(decoded),matches_retained_copy=True,reexecuted=False))
save('original-c01-remote-recheck.json',dict(files=receipts,count=len(receipts),semantic_credit=False))
print(json.dumps(dict(raw_bindings=len(bindings),baseline_links=136,missing=10,actual_local=126,historical_urls=10,historical_targets=4,original_C01=len(receipts),behavior_execution='NOT_EXECUTED',semantic_PASS=False)))
