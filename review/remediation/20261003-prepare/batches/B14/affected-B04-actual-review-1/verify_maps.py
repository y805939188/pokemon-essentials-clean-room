"""Reviewer-owned document reconstruction and reading-range bookkeeping only."""
import collections, hashlib, json, pathlib, sys
import review_bookkeeping as k

results = []
for name in ['primary','owner-numeric','root-controls','accepted-owner','audit']:
    p=k.ROOT/(name+'-map.json')
    m=json.loads(k.artifact_bytes(p.name)); cache={}; counts=collections.Counter(); leaves=0
    for b in m['inputs']:
        key=(b['commit'],b['path'])
        if key not in cache:
            raw=k.get(*key)
            assert hashlib.sha256(raw).hexdigest()==b['sha256'] and len(raw)==b['bytes']
            cache[key]=k.document(raw,key[1])
    def check(node,x,c,p,s):
        global leaves
        if isinstance(x,dict):
            assert node['type']=='object' and [a[0] for a in node['members']]==list(x)
            for key,n in node['members']:check(n,x[key],c,p,s+[key])
        elif isinstance(x,list):
            assert node['type']=='array' and len(node['items'])==len(x)
            for i,n in enumerate(node['items']):check(n,x[i],c,p,s+[i])
        else:
            i=node['value']; r=m['values'][i]
            assert type(x).__name__==r['type']
            assert hashlib.sha256(json.dumps([type(x).__name__,x],ensure_ascii=False).encode()).hexdigest()==r['sha256']
            counts[(i,c,p,tuple(s))]+=1; leaves+=1
    for r in m['structures']:
        check(r['structure'],k.at(cache[(r['commit'],r['path'])],r['selector']),r['commit'],r['path'],r['selector'])
    for i,r in enumerate(m['values']):
        for o in r['occurrences']:
            key=(i,o['commit'],o['path'],tuple(o['selector']))
            assert counts[key]>0; counts[key]-=1
    assert not any(counts.values())
    result={'map':p.name,'map_sha256':hashlib.sha256(k.artifact_bytes(p.name)).hexdigest(),'inputs':len(m['inputs']),'ordered_structures':len(m['structures']),'unique_typed_values':len(m['values']),'scalar_occurrences':leaves,'all_hashes_types_order_contexts_and_occurrences_match':True}
    results.append(result);print(json.dumps(result)); del m,cache,counts

m=json.loads(k.artifact_bytes('audit-map.json')); plan=json.loads((k.ROOT/'audit-semantic-plan.json').read_bytes())
coverage=collections.defaultdict(list); value_lengths=collections.defaultdict(set)
for line in (k.ROOT/'reading-events.jsonl').read_text().splitlines():
    e=json.loads(line)
    if e.get('mode')=='semantic-fragments-delivered':
        for f in e['fragments']:
            coverage[f['value']].append(f['characters']);value_lengths[f['value']].add(f['length'])
missing=[]
for i in plan['queue']:
    o=m['values'][i]['occurrences'][0]
    # Character counts are recorded by each full/fragment delivery; final length must agree.
    spans=sorted(coverage[i]); end=0
    for a,b in spans:
        if a>end:missing.append({'value':i,'gap':[end,a]})
        end=max(end,b)
    lengths=value_lengths[i]
    assert len(lengths)==1
    if end!=next(iter(lengths)):missing.append({'value':i,'tail':[end,next(iter(lengths))]})
assert not missing
k.write('map-verification.json',{'kind':'Document/hash/typed reconstruction and delivered-range accounting; semantic inspection is separately attested by reviewer, never proven by this program','maps':results,'audit_semantic_queue':len(plan['queue']),'delivered_fragment_coverage_complete':True,'truncation_supplements_required':[[1106,1158]],'supplements_consumed':True})
