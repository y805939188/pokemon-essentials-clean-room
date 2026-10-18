"""Lexical static argument pairing only. No point/CVT/storage/rounding or branch is evaluated."""
from pathlib import Path
import json,collections,itertools
R=Path(__file__).resolve().parent
P=json.loads((R/'decoded-programs.json').read_text())
# Manually read all 71 function definitions first; these are stack-interface summaries.
ARITY={0:(2,0),1:(1,0),2:(4,0),3:(4,0),4:(4,0),5:(4,0),6:(2,0),7:(2,0),8:(1,0),9:(0,0),10:(0,0),11:(2,2),13:(2,0),14:(2,0),15:(1,0),16:(0,0),17:(1,1),20:(4,0),24:(2,0),31:(3,0),33:(3,0),34:(5,0),35:(5,0),36:(6,0),37:(5,0),38:(2,0),39:(2,0),40:(0,0),44:(2,1),45:(2,1),46:(2,1),47:(2,1),48:(5,0),53:(5,2),54:(4,0),55:(2,0),56:(2,0),57:(3,0),58:(3,0),59:(2,0),60:(1,0),61:(2,0),62:(3,0),63:(1,0),64:(5,0),65:(5,0),66:(8,0),67:(4,0),68:(3,0),69:(2,0),70:(4,0),71:(3,0),72:(4,0),73:(3,0),74:(5,0),75:(4,0),76:(5,0),77:(4,0),78:(5,0),79:(2,0),80:(5,0),81:(3,0),82:(1,0),83:(0,0),84:(0,0),85:(3,0),88:(2,0),89:(3,0),90:(3,0),91:(3,0)}
SCHEMA={'MIAP':['point','cvt_index'],'MDAP':['point'],'MDRP':['point'],'SRP0':['point'],'SRP1':['point'],'SRP2':['point'],'SMD':['minimum_distance_F26Dot6'],'SDS':['delta_shift'],'SDB':['delta_base'],'SHC':['contour'],'SLOOP':['loop_count'],'SDPVTL':['point','point']}
ALL=[];TEXT=[];ERRORS=[];CALLS=collections.Counter()
for prog in P[2:]:
 stack=[];roles=[];actions=[];loop=1;origins={}
 def pop(role):
  assert stack,('underflow',prog['unit'],ins['pc'],role)
  v,origin=stack.pop();roles.append([origin,ins['pc'],role,v]);return v,origin
 try:
  for ins in prog['code']:
   name=ins['name'];pc=ins['pc'];act=name+(str(ins['flags']) if ins['flags'] is not None else '')
   if name in ('PUSHB','PUSHW','NPUSHB','NPUSHW'):
    for j,v in enumerate(ins['values']):
     origin=f'{pc}.{j}';stack.append((v,origin));origins[origin]=v
    continue
   if name=='CALL':
    target,origin=pop('function_id');assert target in ARITY
    n,m=ARITY[target];args=[pop(f'F{target}.arg{n-j}') for j in range(n)][::-1];CALLS[target]+=1
    act='F'+str(target)+'('+','.join(str(v) for v,o in args)+')'
    for k in range(m):stack.append((None,f'F{target}@{pc}.out{k}'))
   elif name in ('DELTAP1','DELTAP2','DELTAP3'):
    n,_=pop('delta_pair_count');assert isinstance(n,int) and n>=0
    for j in range(n):pop('point');pop('packed_ppem_shift')
    act=name+'{'+str(n)+'}'
   elif name in ('IP','SHP'):
    for j in range(loop):pop('point')
    act += '{'+str(loop)+'}';loop=1
   elif name in SCHEMA:
    got=[pop(role) for role in reversed(SCHEMA[name])][::-1]
    if name=='SLOOP':loop=got[0][0];assert isinstance(loop,int) and loop>0
    if name in ('SDS','SDB','SMD','SLOOP'):act+='='+str(got[0][0])
   else:assert name in ('SVTCA','IUP','RTG','RTHG'),('unexpected',name)
   actions.append(act)
  assert not stack,('leftover',prog['unit'],stack)
  assert set(origins)<=set(r[0] for r in roles),('unpaired',prog['unit'])
  counts=collections.Counter(r[2] for r in roles)
  ALL.append({'unit':prog['unit'],'offset':prog['offset'],'bytes':prog['bytes'],'roles':roles,'roleCounts':dict(counts),'actions':actions})
  rle=[]
  for action,it in itertools.groupby(actions):
   n=sum(1 for _ in it);rle.append(action+('*'+str(n) if n>1 else ''))
  TEXT.append(prog['unit']+': '+' '.join(rle))
 except Exception as e:ERRORS.append({'unit':prog['unit'],'error':repr(e)})
(R/'static-push-roles.json').write_text(json.dumps({'functionArity':ARITY,'glyphs':ALL,'errors':ERRORS,'calls':dict(CALLS)},indent=2)+'\n')
(R/'glyph-actions.txt').write_text('\n'.join(TEXT)+'\n')
print(json.dumps({'glyphPrograms':len(P)-2,'paired':len(ALL),'errors':ERRORS,'calls':dict(CALLS),'readBytes':(R/'glyph-actions.txt').stat().st_size}))
