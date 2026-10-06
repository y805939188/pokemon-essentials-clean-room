"""New document display bookkeeping using already reconstructed exact contexts. No behavior execution."""
import sys,json,pathlib,subprocess
import complete_reader as c
p=pathlib.Path(__file__).parent
phase=sys.argv[1];start=int(sys.argv[2]);budget=int(sys.argv[3]);m=json.loads((p/(phase+'-complete-context-map.json')).read_text());pool=m['semantic_pool'];out=[];size=0;idx=start
exfile=p/(phase+'-display-mechanical-exemptions.json');exempt={x['semantic_id'] for x in json.loads(exfile.read_text())['exemptions']} if exfile.exists() else set()
optimized=p/(phase+'-display-mechanical-exemptions-optimized.json')
if optimized.exists():exempt={x['semantic_id'] for x in json.loads(optimized.read_text())['exemptions']}
reusefile=p/(phase+'-display-exact-reuse.json');exempt.update(x['semantic_id'] for x in json.loads(reusefile.read_text())['reuses']) if reusefile.exists() else None
cache={}
def value(item):
 q=item['first_context'];i=m['inputs'][q['input']];key=(i['sha'],i['path']);ord=q['ordinal']
 if key not in cache:
  raw=c.show(*key,key[0]==c.REF)
  if q['key']=='literal_line':cache[key]=raw.decode().splitlines()
  elif i['path'].endswith('.tsv'):cache[key]=c.document_tsv(raw)
  elif i['path'].endswith('.jsonl'):cache[key]=[json.loads(l) for l in raw.splitlines() if l.strip()]
  else:cache[key]=json.loads(raw)
 x=cache[key]
 if q['key']=='literal_line':x=x[ord[0]-1]
 else:
  for j,n in enumerate(ord):
   if item.get('dictionary_key') and j==len(ord)-1:x=list(x)[n]
   else:x=list(x.values())[n] if isinstance(x,dict) else x[n]
 assert c.digest(x)==item['sha256']
 return x
while idx<len(pool):
 item=pool[idx];q=item['first_context'];v=value(item)
 if idx in exempt:idx+=1;continue
 s='S'+str(idx)+' I'+str(q['input'])+' '+q['pointer']+' '+q['key']+' '+json.dumps(q['record_context'],ensure_ascii=False,separators=(',',':'))+' = '+json.dumps(v,ensure_ascii=False,separators=(',',':'))
 if out and size+len(s)>budget:break
 if not out and len(s)>budget:
  offset=int(sys.argv[4]) if len(sys.argv)>5 else 0;out.append(c.display_private_identity(s[offset:offset+budget]));size=budget
  print('LONG_VALUE',idx,'CHAR_RANGE',offset,min(offset+budget,len(s)),'TOTAL',len(s));idx+=int(offset+budget>=len(s));break
 out.append(c.display_private_identity(s));size+=len(s);idx+=1
print('PHASE',phase,'SEMANTIC_VALUES',len(pool),'RANGE',start,idx,'CHARS',size,'INPUTS',len(m['inputs']),'STRUCTURES',len(m['structures']))
print('\n'.join(out))
with (p/'continuation-delivery.jsonl').open('a') as f:f.write(json.dumps({'phase':phase,'semantic_pool_range':[start,idx],'characters':size,'reader':'exact_context_reconstruction','semantic_read':'Offered only; assess actual truncation before credit'})+'\n')
