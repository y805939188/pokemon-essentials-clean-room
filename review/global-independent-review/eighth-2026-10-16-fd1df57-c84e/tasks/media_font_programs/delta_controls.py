"""Expose every DELTAP selector literal, with the lexically selected graphics-state base/shift."""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parent
ps=json.loads((R/'static-push-roles.json').read_text())['glyphs'];programs={p['unit']:p for p in json.loads((R/'decoded-programs.json').read_text())};out=[];typed=[]
for p in ps:
 base=9;shift=3;fields=[];rows=collections.defaultdict(list)
 for origin,pc,role,value in p['roles']:rows[pc].append((role,value,origin))
 for ins in programs[p['unit']]['code']:
  pc=ins['pc'];name=ins['name']
  if name in ('SDB','SDS'):
   v=rows[pc][0][1]
   if name=='SDB':base=v
   else:shift=v
  if name.startswith('DELTAP'):
   vals=[v for role,v,origin in rows[pc] if role=='packed_ppem_shift']
   fields.append(f'{pc}/D{name[-1]}@{base},{shift}:'+','.join(map(str,vals)))
   for arg in vals:
    n=arg&15;step=n-8 if n<8 else n-7
    typed.append({'glyph':p['unit'],'pc':pc,'raw':arg,'ppem':base+(int(name[-1])-1)*16+(arg>>4),'stepNumerator':step,'stepDenominator':2**shift})
 if fields:out.append(p['unit']+' '+' | '.join(fields))
(R/'delta-controls.read.txt').write_text('\n'.join(out)+'\n');(R/'delta-controls-decoded.json').write_text(json.dumps(typed,indent=2)+'\n')
print('programs',len(out),'selectors',len(typed),'bytes',(R/'delta-controls.read.txt').stat().st_size)
