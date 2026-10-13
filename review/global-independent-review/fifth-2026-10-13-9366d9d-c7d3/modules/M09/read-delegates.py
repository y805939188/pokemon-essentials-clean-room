"""Static lexical display only; never imports or executes reference source."""
from pathlib import Path
import re,sys
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
D=R/'Data/Scripts/011_Battle'
mode=sys.argv[1]; lo=int(sys.argv[2]);hi=int(sys.argv[3])
blocks=[]
for p in sorted((D/'003_Move').glob('*.rb')):
 lines=p.read_text().splitlines();starts=[i for i,s in enumerate(lines) if s.startswith('class Battle::Move::')]
 for ix,a in enumerate(starts):
  b=starts[ix+1] if ix+1<len(starts) else len(lines)
  body=lines[a:b]
  if mode=='params':
   ids=[j for j,s in enumerate(body) if re.search(r'@statUp\s*=|@statDown\s*=|@moveBlacklist\s*=|@number_effects\s*=|@boolean_effects\s*=',s)]
   if ids:
    keep={0}
    for j in ids:
     k=j
     while k<len(body):
      keep.add(k)
      if ']' in body[k]:break
      k+=1
    blocks.append((p,a,body,sorted(keep)))
  elif mode in ('power','failure'):
   pattern = r'  def (pbBaseDamage|pbFixedDamage|pbModifyDamage|pbBaseDamageMultiplier|pbNumHits)\b' if mode=='power' else r'  def (pbFailsAgainstTarget|pbMoveFailedAromaVeil)\??'
   ids=[j for j,s in enumerate(body) if re.match(pattern,s)]
   if ids:
    keep={0}
    for j in ids:
     k=j
     while k<len(body):
      keep.add(k)
      if body[k]=='  end':break
      k+=1
    blocks.append((p,a,body,sorted(keep)))
print('BLOCKS',len(blocks),'DISPLAY',lo,hi)
for idx,(p,a,body,keep) in enumerate(blocks[lo:hi],lo):
 print('BLOCK',idx,str(p.relative_to(R)))
 for j in keep:print(f'{a+j+1:5} {body[j]}')
