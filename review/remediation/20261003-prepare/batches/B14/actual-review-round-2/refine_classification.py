"""Conservative navigation-only refinement; no behavioral claims are exempted."""
import json,pathlib,sys,re,hashlib
import complete_reader as c
P=pathlib.Path(__file__).parent;m=json.loads((P/'classification-supplement-complete-context-map.json').read_text());cache={};ex=[];reasons={}
known=c.known_paths()|{x['path'] for x in m['inputs']}
known_directories={x.rsplit('/',1)[0] for x in known}
def pure(v,q):
    if not isinstance(v,str):return False
    if v in known:return 'Exact frozen native logical path identity'
    if q['key']=='value_id' and re.fullmatch(r'(?:previous|owner):(?:[0-9a-f]{64}|\d+)',v):return 'Typed exact-value reference identifier; native structure retained'
    if q['key']=='mapped_value_id' and re.fullmatch(r'read_formal_line:[0-9a-f]{64}',v):return 'Exact formal-line value hash reference; native mapping retained'
    if v.rstrip('/') in known_directories:return 'Exact frozen native logical directory identity'
    if q.get('dictionary_key') and re.fullmatch(r'\d+|[0-9A-Za-z_.:$@#/-]+',v):return 'Typed structural ASCII key or occurrence identifier'
    # Complete ASCII selector grammar with explicit path separators and native metadata context.
    # Whitespace, Unicode prose, mixed strings and writer rationale remain in the semantic queue.
    if '/' in v and re.fullmatch(r'[0-9A-Za-z_./~:#@$\[\](),+%-]+',v):return 'Complete ASCII JSON selector/path/occurrence grammar; ordered source structure verified'
    if re.fullmatch(r'[0-9a-f]{8,64}|[A-Z][A-Za-z0-9_.-]*[0-9][A-Za-z0-9_.-]*|\d{4}-\d{2}-\d{2}(?:T| )[0-9:.+Z -]+',v,re.I):return 'Hash, canonical catalog ID or historical coordinate identity'
    # A known path may contain spaces. Only an ASCII selector suffix is exempted.
    parts=re.split(r'(?<=\.(?:json))(?=[#/])',v) if False else []
    match=re.match(r'^(?:[0-9a-f]{8,40}[:/])?(.+?\.(?:jsonl|json|md|tsv|py|rb|txt))([#/].*)?$',v)
    if match and match[1] in known and (not match[2] or re.fullmatch(r'[#/0-9A-Za-z_~:.,$@\[\]()+%-]*',match[2])):return 'Exact known path plus complete ASCII selector suffix'
    return False
for z in m['semantic_pool']:
    q=z['first_context'];i=m['inputs'][q['input']];k=(i['sha'],i['path'])
    if k not in cache:
        raw=c.show(*k,k[0]==c.REF)
        if q['key']=='literal_line':cache[k]=raw.decode().splitlines()
        elif i['path'].endswith('.tsv') and i.get('format'):cache[k]=c.document_tsv(raw)
        elif i['path'].endswith('.jsonl'):cache[k]=[json.loads(x) for x in raw.splitlines() if x.strip()]
        else:cache[k]=json.loads(raw)
    v=cache[k]
    if q['key']=='literal_line':v=v[q['ordinal'][0]-1]
    else:
        for j,n in enumerate(q['ordinal']):
            if z.get('dictionary_key') and j==len(q['ordinal'])-1:v=list(v)[n]
            else:v=list(v.values())[n] if isinstance(v,dict) else v[n]
    assert c.digest(v)==z['sha256']
    why=pure(v,{**q,'dictionary_key':z.get('dictionary_key')})
    if why:ex.append({'semantic_id':z['id'],'type':z['type'],'sha256':z['sha256'],'first_context':q,'reason':why});reasons[why]=reasons.get(why,0)+1
name='classification-supplement-display-mechanical-exemptions'+('-optimized' if len(sys.argv)>2 and sys.argv[1]=='optimized' else '')+'.json'
(P/name).write_text(json.dumps({'policy':'Only complete identities/ASCII selectors/structural keys. Every mixed/substantive value remains for actual semantic consumption. Original contexts and verified native structure remain intact.','exemptions':ex},separators=(',',':'))+'\n')
print('POOL',len(m['semantic_pool']),'PURE_METADATA',len(ex),'SUBSTANTIVE_QUEUE',len(m['semantic_pool'])-len(ex),'REASONS',reasons,flush=True)
