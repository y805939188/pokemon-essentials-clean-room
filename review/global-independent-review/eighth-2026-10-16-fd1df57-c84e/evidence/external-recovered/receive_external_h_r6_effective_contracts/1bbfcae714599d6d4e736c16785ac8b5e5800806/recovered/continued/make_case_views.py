import sys,json,hashlib,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
batch,owner,*indices=sys.argv[1:]
source=f'recovered-r6-cases-current/tasks/{owner}/assigned-14-current-reception.json'
x=json.loads((root/source).read_text());seen={};index=[];lines=[]
def enc(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def visit(v,pointer):
 s=enc(v);alias=None
 if len(s)>100:
  if s in seen:return {'$same':seen[s]}
  alias='C'+str(len(seen));seen[s]=alias;index.append({'id':alias,'pointer':pointer,'sha256':hashlib.sha256(s.encode()).hexdigest()})
 if isinstance(v,dict):out={k:visit(a,pointer+'/'+k) for k,a in v.items()}
 elif isinstance(v,list):out=[visit(a,pointer+'/'+str(i)) for i,a in enumerate(v)]
 else:out=v
 return {'$id':alias,'value':out} if alias else out
for i in map(int,indices):
 lines.append('RECORD '+str(i))
 for k,v in x['records'][i].items():lines.append(k+'='+enc(visit(v,'/records/'+str(i)+'/'+k)))
pages=[];buf='';n=1
for line in lines:
 if len(buf)+len(line)>12000 and buf:
  p=root/'continued'/f'{batch}-cases-compact-{n:02d}.txt';p.write_text(buf);pages.append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(buf.encode()).hexdigest()});buf='';n+=1
 buf+=line+'\n'
if buf:
 p=root/'continued'/f'{batch}-cases-compact-{n:02d}.txt';p.write_text(buf);pages.append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(buf.encode()).hexdigest()})
(root/'continued'/f'{batch}-case-view-index.json').write_text(json.dumps({'source':source,'records':list(map(int,indices)),'lossless_exact_aliases':index,'pages':pages},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'batch':batch,'pages':len(pages),'chars':sum(len((root/a['path']).read_text()) for a in pages),'definitions':len(index)}))
