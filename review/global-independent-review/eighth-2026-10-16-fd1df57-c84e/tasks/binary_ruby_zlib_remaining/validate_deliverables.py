"""Independent conservation and source-slice consistency checks for the handoff."""
from pathlib import Path
import json,gzip,hashlib,collections
P=Path(__file__).resolve().parent
IN=P.parent/'binary_remaining_texts'/'ruby-zlib-subtask'
def sha(b):return hashlib.sha256(b).hexdigest()
def read(n):return json.loads((P/n).read_text())
def rows(p):return [json.loads(l) for l in gzip.open(p,'rt')]
o=rows(IN/'unread.jsonl.gz');d=rows(P/'full-disposition-ledger.jsonl.gz');u=rows(IN/'readset.jsonl.gz')
assert len(o)==len(d)==20907
oi={r['candidate_id']:r for r in o};di={r['candidate_id']:r for r in d}
assert len(oi)==len(di)==20907 and oi.keys()==di.keys()
texts={x['read_id']:x['text'] for x in u}
src={path:Path('/workspace/pokemon-essentials',path).read_bytes() for path in ('x64-msvcrt-ruby310.dll','zlib1.dll')}
for cid,r in di.items():
 for k in ('candidate_id','path','inventory_line','encoding','start','end_exclusive','bytes','sha256','section'):assert r[k]==oi[cid][k],(cid,k)
 b=src[r['path']][r['start']:r['end_exclusive']];assert sha(b)==r['sha256']
 s=b.decode('ascii' if r['encoding']=='ascii' else 'utf-16le');assert s==texts[r['read_id']]
 assert r['text_sha256']==sha(s.encode())
 assert r['semantic_status'] in ('FULL_LITERAL_READ','FULL_STATIC_PROGRAM_AND_LITERAL_READ')
mapping=read('bidirectional-mapping.json');f=mapping['candidate_forward'];rev=mapping['literal_reverse']
assert len(f)==20907 and {r['candidate_id'] for r in f}==oi.keys()
assert len(rev)==13574 and len({r['read_id'] for r in rev})==13574
assert collections.Counter(cid for r in rev for cid in r['candidate_ids'])==collections.Counter(oi.keys())
actualsha=sha(('\n'.join(sorted(oi))+'\n').encode());assert actualsha==read('remaining.json')['scope_set_sha256']
yl=read('yarb-decoded.json');pi=read('new-program-inventory.json')['units']
assert len(yl)==len(pi)==16 and sum(x['bytes'] for x in yl)==34524
assert sum(len(x['iseqs']) for x in yl)==171 and sum(len(x['objects']) for x in yl)==654
assert sum(len(q['code']) for x in yl for q in x['iseqs'])==1002
assert sum(len(x['builtin_wiring']['entries']) for x in pi)==115
assert sum(len(x['builtin_wiring']['bytecode_native_refs']) for x in pi)==120
ids=[cid for x in pi for cid in x['candidate_ids']];assert len(ids)==len(set(ids))==542
for x in pi:
 assert sha(src['x64-msvcrt-ruby310.dll'][x['start']:x['end_exclusive']])==x['sha256']
 for cid in x['candidate_ids']:assert di[cid]['program_unit']==x['name']
cstrings=read('complete-cstrings.json');assert len(cstrings)==536 and sum(x['bytes'] for x in cstrings)==16235
for x in cstrings:
 b=src[x['path']][x['start']:x['end_exclusive']];assert sha(b)==x['sha256']
 assert b.decode('ascii')==x['text'] and src[x['path']][x['end_exclusive']]==0
remaining=read('remaining.json');assert not remaining['unread_candidate_ids'] and remaining['unread_candidate_count']==0
assert not remaining['unread_read_ids'] and remaining['unread_distinct_text_count']==0
for x in read('consumer-source-identities.json').values():
 for e in x:assert e['frozen_bytes_equal']
print(json.dumps(dict(status='PASS_TOOL_VALIDATION_ONLY',candidate_count=len(d),distinct_texts=len(rev),candidate_set_sha256=actualsha,source_slices_verified=20907,decoded_programs=16,whole_cstrings=536,target_programs_executed=0,global_semantic_approval=False)))
