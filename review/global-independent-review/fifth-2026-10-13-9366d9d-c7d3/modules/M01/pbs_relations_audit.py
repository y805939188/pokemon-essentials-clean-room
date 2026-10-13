"""Primitive relation audit, not compilation, gameplay, formulas or model tests."""
import re,hashlib
from pathlib import Path
from collections import defaultdict,Counter
import review_state as s
D=s.read('pbs-data-inspection.json')
def readpbs(path):return s.read('pbs-records-'+path[4:].replace('/','--').replace(' ','_')+'.json')
# Read only declarations of parameter kinds; no callback bodies executed.
evo_path='Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb';lines=(s.REF/evo_path).read_text().splitlines();methods={};cur=None
for n,l in enumerate(lines,1):
 m=re.search(r':id\s*=>\s*:(\w+)',l)
 if m:cur=m[1];methods[cur]={'parameter_kind':'none','id_line':n}
 m=re.search(r':parameter\s*=>\s*(:?\w+)',l)
 if m and cur:methods[cur].update(parameter_kind=m[1].lstrip(':'),parameter_line=n)
profile_results=[];unknown=[];summaries=[]
for profile in ['current','Gen 5 backup','Gen 6 backup','Gen 7 backup','Gen 8 backup']:
 prefix='PBS/' if profile=='current' else 'PBS/'+profile+'/'
 reg={}
 for dom,f in [('Species','pokemon'),('Item','items'),('Move','moves'),('Type','types'),('Ability','abilities')]:reg[dom]={r['record_key'] for r in readpbs(prefix+f+'.txt')['records']}
 forms=readpbs(prefix+'pokemon_forms.txt')
 for r in forms['records']:
  sp,fo=[x.strip() for x in r['record_key'].split(',')];reg['Species'].add(sp+'_'+str(int(fo)))
 evos=[];dupes=[];nonmonotonic=[];forms_fields=[]
 for fam in ['pokemon','pokemon_forms']:
  path=prefix+fam+'.txt';d=readpbs(path)
  for r in d['records']:
   for prop in r['properties']:
    k=prop['key'];v=prop.get('data_value');loc={'path':path,'record_key':r['record_key'],'field':k,'line':prop['line']}
    if k=='Evolution':
     a=[t.strip() for t in v.split(',')];target,method=a[:2];param=a[2] if len(a)>2 else '';meta=methods.get(method);kind=meta['parameter_kind'] if meta else None
     check={'target_defined':target in reg['Species'],'method_defined':meta is not None,'parameter_kind':kind,'parameter':param,'target':target,'method':method,'declaration_line':meta['id_line'] if meta else None}
     if kind=='Integer':check['parameter_valid']=bool(re.fullmatch(r'\d+',param))
     elif kind=='String':check['parameter_valid']=bool(param)
     elif kind in reg:check['parameter_valid']=param in reg[kind]
     else:check['parameter_valid']=kind=='none'
     row={**loc,**check};evos.append(row)
     if not all(check[z] for z in ['target_defined','method_defined','parameter_valid']):unknown.append(row)
    if k in ['Types','Abilities','HiddenAbilities','TutorMoves','EggMoves','EggGroups','Offspring','Flags','WildItemCommon','WildItemUncommon','WildItemRare']:
     a=[t.strip() for t in v.split(',')];c=Counter(a)
     if any(x>1 for x in c.values()):dupes.append({**loc,'duplicates':{k:x for k,x in c.items() if x>1},'semantic_note':'Field-specific dedup required; not an automatic invalidity.'})
    if k=='Moves':
     a=v.split(',');pairs=[(int(a[i]),a[i+1]) for i in range(0,len(a),2)]
     if any(pairs[i][0]>pairs[i+1][0] for i in range(len(pairs)-1)):nonmonotonic.append({**loc,'ordered_level_move_pairs':pairs,'semantic_note':'Consumption is by authored order after <=level filtering; source compiler not assumed sorting.'})
   if fam=='pokemon_forms':forms_fields.append({'record_key':r['record_key'],'lines':r['lines'],'defined_fields':[x['key'] for x in r['properties']],'base_record_exists':r['record_key'].split(',')[0] in reg['Species']})
 row={'profile':profile,'evolution_records':evos,'duplicate_list_atoms':dupes,'out_of_order_level_lists':nonmonotonic,'form_field_presence':forms_fields,'used_evolution_methods':dict(Counter(x['method'] for x in evos))}
 s.write('pbs-relations-'+profile.replace(' ','_')+'.json',{'schema_version':'gr5.review.v1','source_baseline':s.R,'boundary':'Full literal reference/type/order relation checks. Callback/evolution/learning/compile/model execution not performed.',**row});profile_results.append({'profile':profile,'evolution_records':len(evos),'duplicate_lists':len(dupes),'out_of_order_level_lists':len(nonmonotonic),'forms':len(forms_fields),'used_methods':row['used_evolution_methods']})
# Every current move effect string gets an audit-only implementation location.
definitions=defaultdict(list)
for f in sorted((s.REF/'Data/Scripts').rglob('*.rb')):
 for n,l in enumerate(f.read_text().splitlines(),1):
  m=re.match(r'\s*class\s+Battle::Move::([A-Za-z0-9_]+)',l)
  if m:definitions[m[1]].append({'path':str(f.relative_to(s.REF)),'line':n})
move_links=[]
for f in D['files']:
 if f['family']!='moves':continue
 for r in readpbs(f['path'])['records']:
  fn=next(x for x in r['properties'] if x['key']=='FunctionCode');code=fn['data_value'];loc=definitions.get(code,[])
  move_links.append({'path':f['path'],'record_key':r['record_key'],'line':fn['line'],'effect_identity':code,'source_definitions':loc,'status':'effect_handler_location_only_not_behavior_approval'})
s.write('move-effect-data-links.json',{'schema_version':'gr5.review.v1','source_baseline':s.R,'boundary':'Identity linkage only; selected handler defaults and concrete effect semantics are reviewed independently. Not future class architecture.','records':move_links})
s.write('pbs-relations-audit.json',{'schema_version':'gr5.review.v1','source_baseline':s.R,'profiles':profile_results,'invalid_or_unhandled_evolution_parameters':unknown,'move_effect_unresolved':[x for x in move_links if not x['source_definitions']]})
for x in profile_results:print(x)
print('EVOLUTION PARAMETER EXCEPTIONS',len(unknown))
for x in unknown[:30]:print(x)
no=[x for x in move_links if not x['source_definitions']];print('MOVE EFFECT UNRESOLVED',len(no));print(sorted({x['effect_identity'] for x in no}))
