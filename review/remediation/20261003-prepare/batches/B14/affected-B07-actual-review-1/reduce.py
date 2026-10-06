# Lossless bookkeeping decomposition of audit text. No behavioral execution.
import json,pathlib,hashlib,re,csv,io
D=pathlib.Path(__file__).parent
vs=json.loads((D/'audit-values.json').read_text());vals=[];lookup={};maps=[]
def add(x,loc,seed):
 key=type(x).__name__+':'+json.dumps(x,ensure_ascii=False,separators=(',',':'))
 if key not in lookup:lookup[key]=len(vals);vals.append({'type':type(x).__name__,'value':x,'first':loc,'seed_read':seed,'occurrences':0})
 i=lookup[key];vals[i]['occurrences']+=1;vals[i]['seed_read']|=seed;return i
def walk(x,loc,seed):
 if isinstance(x,dict):return {'dict':[[k,walk(z,loc+'/'+k,seed)] for k,z in x.items()]}
 if isinstance(x,list):return {'list':[walk(z,loc+'/'+str(i),seed) for i,z in enumerate(x)]}
 if isinstance(x,str):
  if x.startswith(('{','[')):
   try:return {'serialized_json':walk(json.loads(x),loc+'/decoded',seed),'original_sha256':hashlib.sha256(x.encode()).hexdigest()}
   except json.JSONDecodeError:pass
  if '\t' in x:
   sign=x[0] if x[0] in '+-' else '';body=x[1:] if sign else x
   cells=next(csv.reader(io.StringIO(body),delimiter='\t',quotechar='"'))
   return {'tsv_sign':sign,'cells':[walk(c,loc+'/cell/'+str(i),seed) for i,c in enumerate(cells)],'original_sha256':hashlib.sha256(x.encode()).hexdigest()}
  if x.startswith(('+','-',' ')) and ('.diff' in loc or '.patch' in loc):return {'diff_sign':x[0],'body':walk(x[1:],loc+'/body',seed)}
  m=re.fullmatch(r'(\s*)(.*?)(\s*)',x,re.S)
  if m[1] or m[3]:return {'prefix':m[1],'body':walk(m[2],loc+'/framed',seed),'suffix':m[3]}
 return {'value':add(x,loc,seed)}
for i,x in enumerate(vs):maps.append({'original_value':i,'type':x['type'],'sha256':hashlib.sha256(json.dumps(x['value'],ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),'tree':walk(x['value'],x['first'],x['seed_read'])})
(D/'reduced-values.json').write_text(json.dumps(vals,ensure_ascii=False,separators=(',',':'))+'\n');(D/'reduction-map.json').write_text(json.dumps(maps,ensure_ascii=False,separators=(',',':'))+'\n')
print('reduced',len(vals),'seed',sum(x['seed_read'] for x in vals))
