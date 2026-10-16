import pathlib,sys,re,json,hashlib,datetime
out=pathlib.Path(__file__).parent; root=pathlib.Path('/workspace/pokemon-essentials'); rel=sys.argv[1]; lo=int(sys.argv[2]); hi=int(sys.argv[3]); raw=(root/rel).read_bytes(); lines=raw.decode('utf-8-sig').splitlines(); rec=[]; cur=None; comments=[]
for n,line in enumerate(lines,1):
 if line.startswith('#') or not line.strip():comments.append([n,line]);continue
 m=re.fullmatch(r'\[(.*)\]',line)
 if m:
  if cur:cur['end']=n-1
  cur={'id':m[1],'start':n,'end':len(lines),'fields':[]};rec.append(cur)
 else:
  k,v=line.split('=',1);cur['fields'].append([n,k.strip(),v.strip()])
keys=list(dict.fromkeys(k for r in rec for _,k,_ in r['fields']))
selected=rec[lo-1:hi]
text='FIELDS '+ '|'.join(['record@lines','ID']+keys)+'\n'
for i,r in enumerate(selected,lo):
 values=[]
 for k in keys:
  vs=[v for _,kk,v in r['fields'] if kk==k]
  values.append('∅' if not vs else ' ↵ '.join(vs))
 text+=f"{i}@{r['start']}-{r['end']}|{r['id']}|"+'|'.join(values)+'\n'
name=rel.replace('/','_').replace(' ','_')
(out/'read-io'/f'{name}.raw').write_bytes(raw)
view=f'{name}.{lo}-{min(hi,len(rec))}.view.txt';(out/'read-io'/view).write_text(text)
meta={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reader':'/root/pbs_battle','path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),'lines':len(lines),'records':len(rec),'record_range':[lo,min(hi,len(rec))],'field_keys':keys,'io':'read-io/'+view,'raw':'read-io/'+name+'.raw','status':'FULL_FIELD_VIEW_FOR_ACTUAL_READING_NOT_AUTOMATIC_CREDIT','comments':'documentation wiki line and separators only' if all(not l or l.startswith('#') for _,l in comments) else comments}
with (out/'read-io/pbs-index.jsonl').open('a') as f:f.write(json.dumps(meta,ensure_ascii=False)+'\n')
print(json.dumps(meta,ensure_ascii=False));print(text,end='')
