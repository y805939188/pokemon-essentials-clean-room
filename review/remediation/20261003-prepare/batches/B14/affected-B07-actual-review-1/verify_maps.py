# Independent new structure/reconstruction bookkeeping, never behavior evidence.
import json,pathlib,subprocess,hashlib,csv,io,re
D=pathlib.Path(__file__).parent;A='d48197f365c39925f795c1d325988c0d74e59979';B='1e6b11a47370f1c7c4659a32443fc1afda597bac'
def equal(a,b):return json.dumps(a,ensure_ascii=False,separators=(',',':'))==json.dumps(b,ensure_ascii=False,separators=(',',':'))
av=json.loads((D/'audit-values.json').read_text());rv=json.loads((D/'reduced-values.json').read_text())
def recover(t):
 if 'dict' in t:return {k:recover(v) for k,v in t['dict']}
 if 'list' in t:return [recover(v) for v in t['list']]
 if 'scalar' in t:return av[t['scalar']]['value']
 if 'string_parts' in t:
  s=''.join(p+av[n]['value']+z for p,n,z in t['string_parts']);assert hashlib.sha256(s.encode()).hexdigest()==t['original_sha256'];assert len(s.encode())==t['original_bytes'];return s
 raise ValueError(t)
counts=[]
for ent in json.loads((D/'corpus-index.json').read_text()):
 r=json.loads((D/ent['map']).read_text());p=r['path']
 args=['git','show',A+':'+p] if r['kind']=='whole' else ['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',B,A,'--',p]
 b=subprocess.check_output(args);assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'];s=b.decode()
 original=json.loads(s) if p.endswith('.json') and r['kind']=='whole' else [json.loads(l) for l in s.splitlines()] if p.endswith('.jsonl') else s
 assert equal(recover(r['structure']),original),p
 counts.append({'path':p,'kind':r['kind'],'exact_native_structure_and_text_reconstruction':True})
def reduction(t,x):
 if 'value' in t:assert equal(rv[t['value']]['value'],x);assert rv[t['value']]['type']==type(x).__name__;return
 if 'dict' in t:
  assert isinstance(x,dict) and [k for k,v in t['dict']]==list(x)
  for k,v in t['dict']:reduction(v,x[k])
 elif 'list' in t:
  assert isinstance(x,list) and len(t['list'])==len(x)
  for v,z in zip(t['list'],x):reduction(v,z)
 elif 'serialized_json' in t:
  assert isinstance(x,str) and hashlib.sha256(x.encode()).hexdigest()==t['original_sha256'];reduction(t['serialized_json'],json.loads(x))
 elif 'tsv_sign' in t:
  assert isinstance(x,str) and hashlib.sha256(x.encode()).hexdigest()==t['original_sha256'];sign=x[0] if x[0] in '+-' else '';assert sign==t['tsv_sign'];body=x[1:] if sign else x;cells=next(csv.reader(io.StringIO(body),delimiter='\t',quotechar='"'));assert len(cells)==len(t['cells'])
  for v,z in zip(t['cells'],cells):reduction(v,z)
 elif 'diff_sign' in t:
  assert isinstance(x,str) and x[0]==t['diff_sign'];reduction(t['body'],x[1:])
 elif 'prefix' in t:
  assert isinstance(x,str) and x.startswith(t['prefix']) and x.endswith(t['suffix']);end=len(x)-len(t['suffix']) if t['suffix'] else len(x);reduction(t['body'],x[len(t['prefix']):end])
 else:raise ValueError(t)
rm=json.loads((D/'reduction-map.json').read_text())
for z in rm:
 x=av[z['original_value']]['value'];assert z['type']==type(x).__name__;assert hashlib.sha256(json.dumps(x,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()==z['sha256'];reduction(z['tree'],x)
queue=json.loads((D/'semantic-queue.json').read_text());assert len(queue)==5207
progress=json.loads((D/'progress.json').read_text());progress['audit_queue_consumed']=[0,5207];progress['audit_next']=5207;progress['audit_total']=5207;(D/'progress.json').write_text(json.dumps(progress,indent=2)+'\n')
result={'native_inputs_verified':len(counts),'input_checks':counts,'complete_audit_value_count':len(av),'reduced_value_count':len(rv),'complete_reduction_relationships_verified':len(rm),'semantic_queue_total':5207,'reading_assertion':'Separate model semantic consumption through complete delivered chunks and exact reuse; this reconstruction check alone does not prove reading or behavior.'}
(D/'structure-reconstruction-checks.json').write_text(json.dumps(result,indent=2)+'\n');print('RECONSTRUCTION VERIFIED',len(counts),'inputs',len(rm),'typed values')
