"""New exact document context/reuse checks, not behavior evidence."""
import json,pathlib,sys,re,hashlib,subprocess,collections
import complete_reader as c
P=pathlib.Path(__file__).parent
def native(m,q,key_mode=False):
    i=m['inputs'][q['input']]
    if i.get('role')=='FORMAL_UNFILTERED_HUNK':
        x=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',c.BASE,c.ACT,'--',i['path']]).decode().splitlines()[q['ordinal'][0]-1][1:]
    elif q['key']=='literal_line':x=c.show(i['sha'],i['path'],i['sha']==c.REF).decode().splitlines()[q['ordinal'][0]-1]
    else:
        x=c.parsed_json(i['sha'],i['path'])
        for n in q['ordinal']:x=list(x.values())[n] if isinstance(x,dict) else x[n]
    return x
a=json.loads((P/'audit-complete-context-map.json').read_text());ex=json.loads((P/'audit-display-mechanical-exemptions.json').read_text())['exemptions'];checked=[]
for z in ex:
    s=a['semantic_pool'][z['semantic_id']];assert s['sha256']==z['sha256'] and s['first_context']==z['first_context'];v=native(a,s['first_context']);assert c.digest(v)==z['sha256']
    key=s['first_context']['key'];ptr=s['first_context']['pointer'];reason=z['reason']
    if 'key' in reason:assert isinstance(v,str) and re.fullmatch(r'[0-9A-Za-z_.:$@#/-]+',v) and ('/children/' in ptr or '/structure' in ptr)
    else:assert isinstance(v,(int,float)) and not isinstance(v,bool) and (re.search(r'(?:range|ordinal|line|start|end|total|bytes|length|event|delivery|index|coordinate|unit|char|hunk|count|unique_values)',ptr,re.I) or key.isdigit())
    checked.append({'semantic_id':z['semantic_id'],'type':type(v).__name__,'sha256':z['sha256'],'reason':reason,'native_context_verified':True})
ms={};reuse=[]
for z in json.loads((P/'audit-display-exact-reuse.json').read_text())['reuses']:
    s=a['semantic_pool'][z['semantic_id']];v=native(a,s['first_context']);assert c.digest(v)==z['original_sha256'];tr=z['transform'];value=v
    if tr.get('line_ending'):assert value.endswith(tr['line_ending']);value=value[:-len(tr['line_ending'])]
    if tr.get('diff_prefix'):assert value.startswith(tr['diff_prefix']);value=value[len(tr['diff_prefix']):]
    t=z['own_consumed_target'];phase=t['phase']
    if phase not in ms:ms[phase]=json.loads((P/(phase+'-complete-context-map.json')).read_text())
    if 'semantic_id' in t:q=ms[phase]['semantic_pool'][t['semantic_id']]['first_context']
    else:
        q={'input':t['input'],'ordinal':t['ordinal'],'key':'literal_line'}
        # Native occurrence fixes whether this is a JSON scalar, literal or diff body.
        occurrence=next(o for o in ms[phase]['occurrences'] if o['input']==t['input'] and o['ordinal']==t['ordinal']);q['key']=occurrence['key']
    target=native(ms[phase],q)
    assert type(value)==type(target) and value==target and c.digest(value)==z['exact_value_sha256']==t['sha256'];reuse.append({'semantic_id':z['semantic_id'],'original_sha256':z['original_sha256'],'target':t,'transform':tr,'exact_type_value_verified':True})
primary=json.loads((P/'primary-exact-value-map.json').read_text());roots=set();value_ids={};cache={}
for z in primary['mappings']:
    key=(z['sha'],z['path'])
    if key not in cache:cache[key]=json.loads(c.show(*key))
    x=cache[key]
    for k in z['pointer'].lstrip('/').split('/'):
        k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
    assert c.digest(x)==z['sha256'];token=(type(x).__name__,z['sha256']);assert z['value_id'] not in value_ids or value_ids[z['value_id']]==token;value_ids[z['value_id']]=token;roots.add((z['sha'],z['pointer'].split('/')[1]))
snap=json.loads((P/'preliminary-turn-1/snapshot-manifest.json').read_text())
for z in snap['files']:
    path=P/'preliminary-turn-1'/pathlib.Path(z['snapshot']).name;raw=path.read_bytes();assert len(raw)==z['bytes'] and hashlib.sha256(raw).hexdigest()==z['sha256']
f=(P/'independent-first-judgment.md').read_bytes();assert len(f)==4543 and hashlib.sha256(f).hexdigest()=='7ecd63db605500c5a2bf218b5777fe9a32db8614d0cdec197642c7f741098f1d';assert (P/'first-judgment-receipt.json').read_bytes()==(P/'preliminary-turn-1/first-judgment-receipt.json').read_bytes()
(P/'exact-map-and-immutability-checks.json').write_text(json.dumps({'reviewed_ACT':c.ACT,'exemptions':checked,'display_exact_reuses':reuse,'primary_control_occurrences_verified':len(primary['mappings']),'primary_complete_root_objects':len(roots),'primary_exact_typed_reuse_identity_checked':True,'first_judgment_bytes':len(f),'first_judgment_sha256':hashlib.sha256(f).hexdigest(),'first_receipt_unchanged':True,'initial_snapshots_verified':len(snap['files']),'basis':'Own mechanical exact-value/type/context reconstruction only; explicit semantic consumption is recorded separately.'},separators=(',',':'))+'\n')
print('COMPLETE',len(ex),len(reuse),len(primary['mappings']),len(roots),len(snap['files']),flush=True)
