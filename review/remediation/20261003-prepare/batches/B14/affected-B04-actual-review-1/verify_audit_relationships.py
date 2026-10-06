"""New static identity/selector/reuse relationship checks; never execute reviewed helpers."""
import hashlib,json,collections
import review_bookkeeping as k
P='review/remediation/20261003-prepare/batches/B14/'
cache={}; parsed={}; results=[]
def raw(c,p):
    key=(c,p)
    if key not in cache:cache[key]=k.get(c,p)
    return cache[key]
def pointer(c,p,s):
    key=(c,p)
    if key not in parsed:parsed[key]=k.document(raw(c,p),p)
    x=parsed[key]
    for a in s.split('/')[1:]:
        a=a.replace('~1','/').replace('~0','~');x=x[int(a)] if isinstance(x,list) else x[a]
    return x
def typed(x):return (type(x).__name__,json.dumps(x,ensure_ascii=False,separators=(',',':')))
def identity(r):
    b=raw(r['commit'],r['path'])
    if 'sha256' in r:assert hashlib.sha256(b).hexdigest()==r['sha256']
    if 'bytes' in r:assert len(b)==r['bytes']
    if 'git_blob' in r:assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['git_blob']

p=P+'integration-stage-1/control-reading-map.json';x=json.loads(raw(k.ACT,p));first=[]
for r in x['scalar_source_selectors']:
    o=r['source'];v=pointer(o['commit'],o['path'],r['selector']);assert not isinstance(v,(list,dict));first.append(typed(v))
for r in x['aliases']:
    o=r['source'];assert typed(pointer(o['commit'],o['path'],r['selector']))==first[r['value_index']]
for r in x['structures']:
    o=r['source'];v=pointer(o['commit'],o['path'],r['selector']);assert type(v).__name__==r['kind'];assert r['children']==(list(v) if isinstance(v,dict) else list(range(len(v))))
results.append({'path':p,'scalar_aliases':len(x['aliases']),'native_ordered_containers':len(x['structures']),'all_exact_typed_relationships_match':True})

p=P+'integration-stage-1/evidence-reading-map.json';x=json.loads(raw(k.ACT,p))
for r in x['files']:identity(r)
for r in x['narrative_selectors']:pointer(r['commit'],r['path'],r['selector'])
results.append({'path':p,'files':len(x['files']),'narrative_selectors_resolved':len(x['narrative_selectors']),'all_match':True})

p=P+'integration-stage-1/literal-reading-map.json';x=json.loads(raw(k.ACT,p))
for r in x['all_lines']:
    line=raw(r['commit'],r['path']).decode().splitlines(keepends=True)[r['line']-1]
    assert hashlib.sha256(line.encode()).hexdigest()==r['sha256']
for r in x['selectors']:assert 1<=r['line']<=len(raw(r['commit'],r['path']).decode().splitlines())
results.append({'path':p,'all_exact_lines':len(x['all_lines']),'unique_selectors':len(x['selectors']),'all_match':True})

for basename in ['reading-dedup-map.json','semantic-dedup-map.json']:
    p=P+'review-round-3/'+basename;x=json.loads(raw(k.ACT,p))
    for r in x.get('input_identities',[]):identity(r)
    values={r[0]:r for r in x['mapping'] if r[1]=='value'}
    for r in values.values():assert r[2] in values and r[3]==values[r[2]][3]
    # Native object member lists / array lengths are retained in complete audited input.
    assert all(isinstance(r[2],list) for r in x['mapping'] if r[1]=='object')
    assert all(isinstance(r[2],int) and r[2]>=0 for r in x['mapping'] if r[1]=='array')
    results.append({'path':p,'mapping_rows':len(x['mapping']),'value_references':len(values),'every_reuse_target_exists_with_equal_digest':True,'native_structure_retained':True,'limit':'Internal reuse linkage/identity verification; author semantic read chronology is not certified.'})

p=P+'review-round-3/formal-reading-map.json';x=json.loads(raw(k.ACT,p))
for r in x['identities']:identity(r)
for loc,first,digest in x['mapping']:
    p1,n=loc.rsplit(':',1);line=raw('c06db6cd964188b3c693a9b7820e3a8aaffe0b04',p1).decode().splitlines()[int(n)-1]
    assert hashlib.sha256(line.encode()).hexdigest()==digest
results.append({'path':p,'current_line_mappings':len(x['mapping']),'all_source_line_digests_match':True})
k.write('audit-relationship-verification.json',{'reviewed_ACT':k.ACT,'kind':'Static document identities and reconstruction/reuse relationships only; every substantive claim was separately read and judged','checks':results,'no_historical_program_execution':True})
print(json.dumps(results,ensure_ascii=False))
