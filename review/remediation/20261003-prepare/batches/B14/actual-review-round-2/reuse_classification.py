"""Exact own consumed partial-view reuse; not completion by hash."""
import json,pathlib,sys
import complete_reader as c
P=pathlib.Path(__file__).parent;done=json.loads((P/'semantic-consumption.json').read_text());targets={};maps={}
for ph in ['qualified','qualified-bounded','audit-initial-view','contracts','contracts-bounded','preceding-final','preceding-complete','preceding-semantic']:
    record=done.get(ph,{});ranges=record.get('consumed_ranges',[])
    if not ranges:continue
    m=json.loads((P/(ph+'-complete-context-map.json')).read_text());maps[ph]=m
    for z in m['semantic_pool']:
        if any(lo<=z['id']<hi for lo,hi in ranges):targets.setdefault((z['type'],z['sha256']),{'phase':ph,'semantic_id':z['id'],'context':z['first_context']})
m=json.loads((P/'classification-supplement-complete-context-map.json').read_text());reuses=[]
for z in m['semantic_pool']:
    tok=(z['type'],z['sha256'])
    if tok not in targets:continue
    t=targets[tok];q=t['context'];i=maps[t['phase']]['inputs'][q['input']]
    if q['key']=='literal_line':v=c.show(i['sha'],i['path'],i['sha']==c.REF).decode().splitlines()[q['ordinal'][0]-1]
    else:
        v=c.parsed_json(i['sha'],i['path'])
        for n in q['ordinal']:v=list(v.values())[n] if isinstance(v,dict) else v[n]
    assert c.digest(v)==z['sha256'] and type(v).__name__==z['type']
    reuses.append({'semantic_id':z['id'],'type':z['type'],'sha256':z['sha256'],'original_context':z['first_context'],'own_consumed_target':t,'exact_native_target_verified':True})
(P/'classification-supplement-display-exact-reuse.json').write_text(json.dumps({'policy':'Exact typed/value reuse from explicitly consumed ranges of earlier wider views; incomplete whole views are not credited as whole. All target/native ordinal/hash and original structures retained. No writer proof substitutes for source.','reuses':reuses},separators=(',',':'))+'\n')
print('EXACT_OWN_PARTIAL_VIEW_REUSES',len(reuses),flush=True)
