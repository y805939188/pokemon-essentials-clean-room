"""New JSON bookkeeping, not execution of any historical review helper."""
import pathlib,json,hashlib,importlib.util,sys
sys.dont_write_bytecode = True
D=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('reader',D/'read_documents.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
docs=json.loads((D/'reading-documents.json').read_text());values=json.loads((D/'reading-values.json').read_text());lookup={}
for x in values:
 v=m.document_value(x['first'][0])
 for k in x['first'][1]:v=v[k]
 lookup[(type(v).__name__,json.dumps(v,ensure_ascii=False,separators=(',',':')))]=x['id']
original_count=len(values)
O=m.O;R='review/global-independent-review/2026-10-03-fd82a639/'
sha = sys.argv[1] if len(sys.argv)>1 else O
paths = sys.argv[2:] if len(sys.argv)>2 else [R+'root/extension-adjudications.json',R+'agents/A/X-A-C05-RECHECK/recheck.json',R+'root/fullwidth-syntax-review.json']
for path in paths:
 if any(x['commit']==sha and x['path']==path and x['selection'] is None for x in docs):continue
 raw=m.show(sha,path);di=len(docs);dm={'commit':sha,'path':path,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'selection':None,'format':path.rsplit('.',1)[-1],'supplement_reason':'Complete standalone original qualified evidence; prior selected extension document had zero records.','nodes_file':'typed-map-%03d.json'%di};docs.append(dm);nodes=[]
 def walk(v,loc):
  if isinstance(v,dict):
   nodes.append([loc,'object',list(v)])
   for k,x in v.items():walk(x,loc+[k])
  elif isinstance(v,list):
   nodes.append([loc,'array',len(v)])
   for i,x in enumerate(v):walk(x,loc+[i])
  else:
   typ=type(v).__name__;key=(typ,json.dumps(v,ensure_ascii=False,separators=(',',':')))
   if key not in lookup:
    vi=len(values);lookup[key]=vi;values.append({'id':vi,'type':typ,'sha256':hashlib.sha256(key[1].encode()).hexdigest(),'first':[di,loc],'characters':len(v) if isinstance(v,str) else None,'class':'semantic' if isinstance(v,str) and not m.pure(v) else 'identity_or_numeric'})
   nodes.append([loc,typ,lookup[key]])
 walk(m.transform(raw,dm),[]);(D/dm['nodes_file']).write_text(json.dumps(nodes,ensure_ascii=False,separators=(',',':'))+'\n')
(D/'reading-documents.json').write_text(json.dumps(docs,indent=2)+'\n');(D/'reading-values.json').write_text(json.dumps(values,indent=2)+'\n');print('Total documents',len(docs),'value range',original_count,len(values),'new semantic',sum(x['class']=='semantic' for x in values[original_count:]),'new characters',sum(x['characters'] or 0 for x in values[original_count:] if x['class']=='semantic'))
