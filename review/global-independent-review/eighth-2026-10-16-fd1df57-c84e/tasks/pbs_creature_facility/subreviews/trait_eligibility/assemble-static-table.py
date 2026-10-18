"""Mechanical static evidence assembly. Reads projected PBS fields already reviewed.
No reference code import, game execution, sampling, or future framework output.
All predicates are deductions under the explicit cold-cache premises in review.md.
"""
from pathlib import Path
import json
from decimal import Decimal, ROUND_HALF_UP
P=Path(__file__).parent
classes=json.loads((P/'species-field-classes.json').read_text())
selected=json.loads((P/'template-species.json').read_text())
def nunit(v):return max(1,int((Decimal(v)*10).quantize(Decimal(1),rounding=ROUND_HALF_UP)))
def arr(f,k):return [x.strip() for x in ','.join(f.get(k,[])).split(',') if x.strip()]
def evos(f):
 out=[]
 for k in ['Evolutions','Evolution']:
  for v in f.get(k,[]):
   t=v.split(',')
   for j in range(0,len(t),3):out.append([x.strip() for x in t[j:j+3]])
 return out
result=[]
for dataset in ['default',*[f'Gen {i} backup' for i in range(5,9)]]:
 # All included records retain source order via first matching occurrence.
 rows=[]
 for c in classes:
  for o in c['occurrences']:
   if o['dataset']==dataset:rows.append((o,c))
 rows.sort(key=lambda z:('pokemon_forms' in z[0]['file'],z[0]['start']))
 base={};forms={}
 for o,c in rows:
  ident=c['species'];f=c['fields'];bits=ident.split(',');s=bits[0];form=int(bits[1]) if len(bits)>1 else 0
  default=int(next((a[12:] for a in arr(f,'Flags') if a.lower().startswith('defaultform_')),'-1'))
  q={'species':s,'form':form,'source_class':c['id'],'source':o,'default_form':default,
     'base_stats':[int(x) for x in arr(f,'BaseStats')], 'abilities':arr(f,'Abilities'),
     'hidden_abilities':arr(f,'HiddenAbilities'),'height_dm':nunit(f['Height'][0]) if 'Height' in f else None,
     'weight_hg':nunit(f['Weight'][0]) if 'Weight' in f else None,'evolutions':evos(f)}
  if form==0:base[s]=q
  else:forms[(s,form)]=q
 # Relevant incoming edges, including None, already included in ancestor closure.
 incoming={}
 for q in base.values():
  for e in q['evolutions']:incoming.setdefault(e[0],q['species'])
 for q in forms.values():
  b=base[q['species']]
  for k in ['base_stats','abilities','hidden_abilities']:
   if k not in {'base_stats':'BaseStats','abilities':'Abilities','hidden_abilities':'HiddenAbilities'}:continue
   # Missing property inherits; explicit empty properties are absent after PBS conversion.
   if not q[k]:q[k]=b[k].copy()
  for k in ['height_dm','weight_hg']:
   if q[k] is None:q[k]=b[k]
  if q['default_form']<0:q['default_form']=b['default_form']
  if not q['evolutions']:q['evolutions']=[e.copy() for e in b['evolutions']]
 form_incoming={}
 for q in list(base.values())+list(forms.values()):
  for e in q['evolutions']:
   incoming.setdefault(e[0],q['species'])
   if q['form']>0:form_incoming.setdefault((e[0],q['form']),q['species'])
 # Baby resolution recurses through the default record after the first step.
 def prev(q):return form_incoming.get((q['species'],q['default_form'] if q['default_form']>=0 else q['form']),incoming.get(q['species']))
 def baby(q):
  s=q['species'];p=prev(q);visited=set()
  while p and p!=s:
   if p in visited:raise ValueError('cycle')
   visited.add(p);s=p;p=prev(base[s])
  return s
 for q in list(base.values())+list(forms.values()):
  s=q['species']
  if s not in selected:continue
  q=dict(q);bst=sum(q['base_stats']);a=q['abilities'];bb=baby(q)
  valid_e=[e for e in q['evolutions'] if len(e)>1 and e[1]!='None']
  st=True if set(a)&{'TRUANT','SLOWSTART'} or s in {'DRAGONITE','SALAMENCE','TYRANITAR'} else s not in {'WYNAUT','WOBBUFFET'} and bst<600
  reason='ordinary_ability_early_allow' if set(a)&{'TRUANT','SLOWSTART'} else 'named_species_early_allow' if s in {'DRAGONITE','SALAMENCE','TYRANITAR'} else 'named_species_deny' if s in {'WYNAUT','WOBBUFFET'} else 'bst_below_600' if bst<600 else 'bst_at_least_600'
  created=[0]
  if s=='UNOWN':created=list(range(28))
  elif s in {'BURMY','WORMADAM'}:created=[0,1,2]
  q.update(dataset=dataset,bst=bst,baby_species_cold=bb,baby_restriction_cold=(s==bb),valid_evolutions=valid_e,
    can_evolve_cold=bool(valid_e),unevolved_restriction_cold=s==bb and bool(valid_e),standard_non_egg=st,standard_reason=reason,
    height_le_2m=q['height_dm']<=20,weight_le_20kg=q['weight_hg']<=200,weight_le_99kg=q['weight_hg']<=990,
    fancy_species_cold=st and s==bb and q['height_dm']<=20 and q['weight_hg']<=200,
    little_factory_species_cold=st and s==bb and bool(valid_e),little_direct_species_cold=st and s==bb,
    light_direct_species_cold=st and s==bb and q['weight_hg']<=990,
    strict_species_cold=st and s==bb and bool(valid_e) and s not in {'SCYTHER','SNEASEL','MEDITITE','YANMA','TANGELA','MURKROW'},
    template_creation_forms=created,template_created_this_form=q['form'] in created,
    factory_species=(s!='UNOWN'),execution='NOT_EXECUTED',evidence='SOURCE_STATIC_DEDUCTION')
  result.append(q)
(P/'finite-traits.json').write_text(json.dumps({'schema':'gr8-facility-finite-traits/v1','semantics':'Cold caches, compiled finite PBS profile, normal non-egg instance, current form; all source deductions, no execution. Fields with _species exclude level/item/move/team gates.','template_species_count':len(selected),'records':result},ensure_ascii=False,indent=2)+'\n')
base_rows={q['species']:q for q in result if q['dataset']=='default' and q['form']==0}
(P/'default-base-traits.json').write_text(json.dumps(base_rows,ensure_ascii=False,indent=2)+'\n')
counts={d:sum(q['dataset']==d for q in result) for d in ['default',*[f'Gen {i} backup' for i in range(5,9)]]}
print(json.dumps({'records':len(result),'datasets':counts,'base_default':len(base_rows),'default_standard_denied':[(s,q['bst'],q['standard_reason']) for s,q in base_rows.items() if not q['standard_non_egg']],'default_fancy_species_count':sum(q['fancy_species_cold'] for q in base_rows.values()),'default_little_species_count':sum(q['little_factory_species_cold'] for q in base_rows.values())},ensure_ascii=False))
