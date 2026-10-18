"""Static stack-shape checker. Both IF arms are inspected; no font arithmetic or predicate is evaluated."""
from pathlib import Path
import json,ast,copy
R=Path(__file__).resolve().parent
node=ast.parse((R/'lexical.py').read_text());sig=next(ast.literal_eval(n.value) for n in node.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='ARITY' for t in n.targets))
p=json.load(open(R/'decoded-programs.json'))[0];pending=[];funcs={};cur=None
for i in p['code']:
 if cur is None and i['values']:pending+=i['values']
 elif i['name']=='FDEF':cur=pending.pop();funcs[cur]=[]
 elif i['name']=='ENDF':cur=None
 elif cur is not None:funcs[cur].append(i)
meta_path=Path('/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/fontTools/ttLib/tables/ttProgram.py');meta={}
for n in ast.parse(meta_path.read_text()).body:
 if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='instructions' for t in n.targets):
  for op,name,bits,desc,pop,push in ast.literal_eval(n.value):meta[name]=(pop,push)
results=[]
for fid,code in funcs.items():
 touched=set();errors=[]
 def touch(v):
  if isinstance(v,tuple):touched.add(v[1])
 def flow(code,stack):
  z=0
  def pop():v=stack.pop();touch(v);return v
  while z<len(code):
   ins=code[z];name=ins['name'];z+=1
   if ins['values']:stack.extend(ins['values']);continue
   if name=='IF':
    pop();level=1;els=None;end=None
    for j in range(z,len(code)):
     t=code[j]['name']
     if t=='IF':level+=1
     if t=='EIF':
      level-=1
      if level==0:end=j;break
     if t=='ELSE' and level==1:els=j
    assert end is not None
    a=flow(code[z:els if els is not None else end],stack.copy())
    b=flow(code[els+1:end] if els is not None else [],stack.copy())
    assert len(a)==len(b),('unequal branch',fid,ins['pc'],len(a),len(b))
    stack=[x if x==y else None for x,y in zip(a,b)];z=end+1;continue
   if name=='CALL':
    target=pop()
    if target is None and fid==17:target=44
    assert target in sig,(fid,ins['pc'],target)
    n,m=sig[target]
    for _ in range(n):pop()
    stack.extend([None]*m);continue
   if name=='DUP':v=pop();stack.extend([v,v]);continue
   if name=='SWAP':a=pop();b=pop();stack.extend([a,b]);continue
   if name=='ROLL':a=pop();b=pop();c=pop();stack.extend([b,a,c]);continue
   if name in ('CINDEX','MINDEX'):
    k=pop();assert isinstance(k,int) and k>0,(fid,ins['pc'],k)
    v=stack[-k];touch(v)
    if name=='MINDEX':del stack[-k]
    stack.append(v);continue
   n,m=meta[name]
   if n==-1:
    assert name in ('ALIGNRP','SHPIX','IP','SHP');n=2 if name=='SHPIX' else 1
   assert m>=0
   for _ in range(n):pop()
   stack.extend([None]*m)
  return stack
 try:
  if fid==49:
   k=next(j for j,x in enumerate(code) if x['name']=='ELSE');e=len(code)-1
   for label,arm in [('ppem_le_threshold',code[3:k]),('ppem_gt_threshold',code[k+1:e])]:
    touched.clear();out=flow(code[:2]+[{'name':'POP','values':[],'pc':764}]+arm,[('arg',v) for v in range(100)]);need=100-min(touched);net=len(out)-100
    results.append({'id':fid,'branch':label,'required':need,'net':net,'suggested':[need,need+net]})
   continue
  out=flow(code,[('arg',k) for k in range(100)])
  need=100-min(touched) if touched else 0;net=len(out)-100
  results.append({'id':fid,'required':need,'net':net,'old':sig.get(fid),'suggested':[need,need+net]})
 except Exception as e:results.append({'id':fid,'error':repr(e)})
(R/'function-signatures-check.json').write_text(json.dumps(results,indent=2)+'\n')
for row in results:print(row)
