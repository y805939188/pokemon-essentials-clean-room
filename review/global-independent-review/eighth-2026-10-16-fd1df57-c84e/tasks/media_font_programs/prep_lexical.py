"""Pair the prep's preloaded literal stack to data consumers; conditional prologue is read manually."""
from pathlib import Path
import json,ast
R=Path(__file__).resolve().parent
node=ast.parse((R/'lexical.py').read_text());ARITY=next(ast.literal_eval(n.value) for n in node.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='ARITY' for t in n.targets))
p=json.loads((R/'decoded-programs.json').read_text())[1];stack=[];roles=[];actions=[]
def pop(role):
 assert stack,(ins['pc'],role)
 v,origin=stack.pop();roles.append([origin,ins['pc'],role,v]);return v
for ins in p['code']:
 pc=ins['pc'];name=ins['name']
 if pc<610:
  if ins['values']:stack.extend((v,f'{pc}.{j}') for j,v in enumerate(ins['values']))
  else:
   assert name=='CALL';target=pop('function_id');assert target in (83,84);actions.append(f'{pc}:F{target}()')
 elif 610<=pc<647:continue
 elif pc in (647,648,649):actions.append(f'{pc}:{name}={pop(name)}')
 elif pc==650:actions.append('650:SVTCA0')
 elif pc==651:
  val=pop('storage_value');loc=pop('storage_index');actions.append(f'651:WS[{loc}]={val}')
 elif pc==652:actions.append(f'652:SCVTCI={pop("cvt_cutin")}')
 elif 653<=pc<684:continue
 elif name.startswith('DELTAC'):
  n=pop('delta_pair_count');pairs=[]
  for j in range(n):loc=pop('cvt_index');delta=pop('packed_ppem_shift');pairs.append([loc,delta])
  actions.append(f'{pc}:{name}'+json.dumps(pairs,separators=(',',':')))
 elif name=='CALL':
  target=pop('function_id');n,m=ARITY[target];assert m==0
  args=[pop(f'F{target}.arg{n-j}') for j in range(n)][::-1];actions.append(f'{pc}:F{target}'+str(args))
 elif name=='SDB':actions.append(f'{pc}:SDB={pop("delta_base")}')
 else:assert name in ('SVTCA','RTG');actions.append(f'{pc}:{name}{ins["flags"] if ins["flags"] is not None else ""}')
assert not stack,stack
(R/'prep-roles.json').write_text(json.dumps(roles,indent=2)+'\n')
(R/'prep-actions.txt').write_text('\n'.join(actions)+'\n')
print('\n'.join(actions))
