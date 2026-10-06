# New document/JSON/diff bookkeeping only. No historical helper execution.
import pathlib,subprocess,json,hashlib,re
D=pathlib.Path(__file__).parent; A='d48197f365c39925f795c1d325988c0d74e59979'; B='1e6b11a47370f1c7c4659a32443fc1afda597bac'
def sha(x):return hashlib.sha256(x).hexdigest()
def git(*a):return subprocess.check_output(['git',*a])
def build():
 vals=[];lookup={};counts=[]
 def val(x,ctx,seed=False):
  t=type(x).__name__;key=t+':'+json.dumps(x,ensure_ascii=False,separators=(',',':'))
  if key not in lookup:lookup[key]=len(vals);vals.append({'type':t,'value':x,'first':ctx,'seed_read':seed,'occurrences':0})
  n=lookup[key];vals[n]['occurrences']+=1
  if seed:vals[n]['seed_read']=True
  return n
 def walk(x,ctx,seed=False):
  if isinstance(x,dict):return {'dict':[[k,walk(z,ctx+'/'+k,seed)] for k,z in x.items()]}
  if isinstance(x,list):return {'list':[walk(z,ctx+'/'+str(i),seed) for i,z in enumerate(x)]}
  if isinstance(x,str):
   # Lossless textual framing, allowing exact body values to be read once.
   parts=[]
   for i,line in enumerate(x.splitlines(keepends=True) or ['']):
    m=re.fullmatch(r'(\s*)(.*?)(\s*)',line,re.S)
    parts.append([m[1],val(m[2],ctx+'/text/'+str(i),seed),m[3]])
   return {'string_parts':parts,'original_sha256':sha(x.encode()),'original_bytes':len(x.encode())}
  return {'scalar':val(x,ctx,seed)}
 for name in ['primary-controls','gate','bounded-formal']:
  for n,x in enumerate(json.loads((D/(name+'-values.json')).read_text())):walk(x['value'],name+'/'+str(n),True)
 paths=[z['paths'].split(' b/')[1] for z in json.loads((D/'diff-inventory.json').read_text())[0]['paths']]
 index=[]
 for i,p in enumerate(paths):
  b=git('show',A+':'+p)
  if p.startswith(('specs/','deliverables/final-specification-set/engine-overworld/','deliverables/final-specification-set/pokemon-rules/')) or ('test-catalog/' in p and p.endswith(('wp11-15-59-60.md','wp53-60-61-62-69-70.md'))):continue
  if '/batches/B14/' not in p:
   b=git('diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',B,A,'--',p);kind='diff'
  else:kind='whole'
  text=b.decode()
  try:
   x=json.loads(text) if p.endswith('.json') and kind=='whole' else [json.loads(l) for l in text.splitlines()] if p.endswith('.jsonl') else text
  except json.JSONDecodeError:x=text
  record={'path':p,'kind':kind,'commit':A,'base':B if kind=='diff' else None,'sha256':sha(b),'bytes':len(b),'structure':walk(x,p)}
  (D/f'corpus-structure-{i:03}.json').write_text(json.dumps(record,ensure_ascii=False,separators=(',',':'))+'\n');index.append({'path':p,'kind':kind,'map':f'corpus-structure-{i:03}.json','sha256':sha(b),'bytes':len(b)})
 (D/'audit-values.json').write_text(json.dumps(vals,ensure_ascii=False,separators=(',',':'))+'\n');(D/'corpus-index.json').write_text(json.dumps(index,indent=2)+'\n')
 print('AUDIT',len(index),'VALUES',len(vals),'seed',sum(x['seed_read'] for x in vals))
def view(start,budget=10000):
 vs=json.loads((D/'audit-values.json').read_text());i=start;used=0;out=[]
 for i in range(start,len(vs)):
  x=vs[i];z=x['value']
  pure=not isinstance(z,str) or bool(re.fullmatch(r'[0-9a-f]{40,64}|[A-Z0-9_./:+ -]{1,90}|[0-9;:,.+()\- ]+|(?:review|deliverables|specs|planning|audit|root|agents|Data|PBS)/[A-Za-z0-9_ ./()@:+\-]+\.(?:md|json|tsv|csv|rb|txt|dat|pdf|png|rxdata|jsonl)|(?:\$|#|/)?(?:[A-Za-z_0-9.\[\]~:#-]+/)*[A-Za-z_0-9.\[\]~:#-]+',z))
  if x['seed_read'] or pure:continue
  line=f"{i} {x['first']} {json.dumps(z,ensure_ascii=False)}\n"
  if used and used+len(line)>budget:break
  print(line,end='');used+=len(line);out.append(i)
 else:i=len(vs)
 print('NEXT',i,'TOTAL',len(vs));return out
if __name__=='__main__':
 import sys
 if sys.argv[1]=='build':build()
 else:view(int(sys.argv[1]),int(sys.argv[2]) if len(sys.argv)>2 else 10000)
