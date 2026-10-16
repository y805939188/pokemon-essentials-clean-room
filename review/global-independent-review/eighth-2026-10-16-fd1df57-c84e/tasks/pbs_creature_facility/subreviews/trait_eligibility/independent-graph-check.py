"""Finite graph tool validation, not a reference/game/behavior-model execution.
Only the already-read parent's mathematical certificate function is evaluated.
The independent upper certificate is a vertex cover derived from max-flow cut.
All output is confined to this child directory.
"""
from pathlib import Path
from collections import defaultdict,deque
import ast,collections,json,hashlib,datetime,itertools
P=Path(__file__).parent;H=P.parent.parent;R=Path('/workspace/pokemon-essentials')
started=datetime.datetime.now(datetime.timezone.utc).isoformat()

def fileid(path):
 b=path.read_bytes();return {'path':str(path.resolve()),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
parent_inputs=[fileid(H/'finite-pool-audit.py'),fileid(H/'finite-pool-summary.json')]
assert parent_inputs[0]['sha256']=='43c8f5ccc038a5fd4f143d84d5247eb3db392ef67cbe85406a20e94b275069b2'
assert parent_inputs[1]['sha256']=='fef3f71acff4666555e56d2df7d285dacc6f50982682818135c9885f1425ac91'
# Complete script was read before evaluating this one pure function. No main call,
# no parent writes, and no import of source/reference code.
module=ast.parse((H/'finite-pool-audit.py').read_text())
node=next(n for n in module.body if isinstance(n,ast.FunctionDef) and n.name=='certificate')
context={'collections':collections}
exec(compile(ast.Module(body=[node],type_ignores=[]),'<parent graph certificate only>','exec'),context)
parent_certificate=context['certificate']

def maxflow_certificate(rows,item_clause):
 # Tagged endpoints deliberately avoid collisions between held IDs/private nil.
 edges={};left=set();right=set()
 for row in rows:
  s=('species',row['species']);i=('item',row['item']) if item_clause and row['item'] else ('free',row['species'])
  edges.setdefault((s,i),row['index']);left.add(s);right.add(i)
 src=('source',);sink=('sink',);cap=defaultdict(dict)
 def edge(a,b):cap[a][b]=1;cap[b].setdefault(a,0)
 for s in left:edge(src,s)
 for i in right:edge(i,sink)
 for s,i in edges:edge(s,i)
 flow=0
 while True:
  previous={src:None};todo=deque([src])
  while todo and sink not in previous:
   a=todo.popleft()
   for b,c in cap[a].items():
    if c and b not in previous:previous[b]=a;todo.append(b)
  if sink not in previous:break
  b=sink
  while previous[b] is not None:
   a=previous[b];cap[a][b]-=1;cap[b][a]+=1;b=a
  flow+=1
 reach={src};todo=deque([src])
 while todo:
  a=todo.popleft()
  for b,c in cap[a].items():
   if c and b not in reach:reach.add(b);todo.append(b)
 cover=(left-reach)|(right&reach)
 matched=[(s,i,row_index) for (s,i),row_index in edges.items() if cap[i].get(s,0)==1]
 assert len({s for s,i,r in matched})==len(matched)==len({i for s,i,r in matched})==flow
 assert all(s in cover or i in cover for s,i in edges)
 assert len(cover)==flow
 return {'maximum_matching':flow,'witness_rows':[r for s,i,r in matched],
         'upper_vertex_cover':[list(x) for x in sorted(cover)],'edge_count':len(edges)}

def check_rows(rows,item_clause):
 own=maxflow_certificate(rows,item_clause);parent=parent_certificate(rows,item_clause)
 assert own['maximum_matching']==parent['maximum_matching']
 selected={r['index']:r for r in rows}
 witness=[selected[i] for i in parent['witness_rows']]
 assert len(witness)==parent['maximum_matching'] and len({r['species'] for r in witness})==len(witness)
 if item_clause:assert len([r['item'] for r in witness if r['item']])==len({r['item'] for r in witness if r['item']})
 return own

# Complete finite class: all simple bipartite graphs with <=4 labelled species
# and <=4 labelled nonempty item vertices (zero-degree labels permitted).
small=0
for mask in range(1<<16):
 rows=[{'species':f'S{a}','item':f'I{b}','index':a*4+b} for a in range(4) for b in range(4) if mask&(1<<(a*4+b))]
 check_rows(rows,True);small+=1
# Explicit nil, duplicate occurrences, augmenting-path and strict no-item gates.
edge_cases=[
 ('several_nil',[('A',None),('B',None),('C',None)],True,3),
 ('same_species_nil_twice',[('A',None),('A',None),('B','X')],True,2),
 ('same_item_different_species',[('A','X'),('B','X'),('C','Y')],True,2),
 ('alternating_reassignment',[('A','X'),('A','Y'),('B','X')],True,2),
 ('strict_ignores_repeated_items',[('A','X'),('B','X'),('C','X')],False,3),
 ('strict_still_rejects_repeated_species',[('A','X'),('A','Y'),('B','X')],False,2),
]
edge_out=[]
for name,pairs,clause,wanted in edge_cases:
 rows=[{'species':s,'item':i,'index':j} for j,(s,i) in enumerate(pairs)]
 c=check_rows(rows,clause);assert c['maximum_matching']==wanted
 edge_out.append({'name':name,'input':rows,'item_clause':clause,'expected_maximum':wanted,'certificate':c})
print(json.dumps({'phase':'finite_math_graphs_complete','all_4_by_4_graphs':small,'targeted_cases':len(edge_out)}),flush=True)

# Reconstruct already-frozen raw pool projections without executing a species
# registry, ruleset, random generator or any game function.
pairs={'PBS/battle_tower_trainers.txt':'PBS/battle_tower_pokemon.txt','PBS/cup_fancy_trainers.txt':'PBS/cup_fancy_pkmn.txt','PBS/cup_fancy_trainers_single.txt':'PBS/cup_fancy_pkmn_single.txt','PBS/cup_little_trainers.txt':'PBS/cup_little_pkmn.txt','PBS/cup_pika_trainers.txt':'PBS/cup_pika_pkmn.txt','PBS/cup_poke_trainers.txt':'PBS/cup_poke_pkmn.txt'}
traits=defaultdict(list)
for q in json.loads((P/'finite-traits.json').read_text())['records']:
 if q['dataset']=='default' and q['template_created_this_form']:traits[q['species']].append(q)
keys={'all_normal':None,'standard':'standard_non_egg','fancy':'fancy_species_cold','little_factory':'little_factory_species_cold','little_direct':'little_direct_species_cold','light_direct':'light_direct_species_cold','strict_little':'strict_species_cold','factory':'factory_species'}
assert set(traits)==set(json.loads((P/'template-species.json').read_text()))
# Cold cache proof checks each actual created form for every dependency used by
# the8 projections, rather than inferring graph equality from a summary alone.
form_differences=[]
for species,forms in traits.items():
 for name,key in keys.items():
  values=[True if key is None else q[key] for q in forms]
  if len(set(values))>1:form_differences.append({'species':species,'predicate':name,'values':values})
assert not form_differences

def read_templates(rel):
 rows=[]
 for lineno,line in enumerate((R/rel).read_text(encoding='utf-8-sig').splitlines(),1):
  if not line.strip() or line.lstrip().startswith('#'):continue
  s,i,n,e,m=line.strip().split(';')
  rows.append({'species':s,'item':i or None,'moves':m.split(','),'index':len(rows),'line':lineno})
 return rows

def read_pools(rel):
 # Only finite PokemonNos fields, retaining multiplicity/order.
 return [[int(x) for x in line.split('=',1)[1].split(',')] for line in (R/rel).read_text(encoding='utf-8-sig').splitlines() if line.startswith('PokemonNos =')]

summary={};certs=[];pool_count=0;math_count=0
for trainerfile,templatefile in pairs.items():
 templates=read_templates(templatefile);pools=read_pools(trainerfile);pool_count+=len(pools)
 part={name:[] for name in keys}
 for trainer_index,pool in enumerate(pools):
  assert all(0<=i<len(templates) for i in pool)
  for name,key in keys.items():
   eligible=[]
   for i in pool:
    row=templates[i];formvalues=[True if key is None else q[key] for q in traits[row['species']]]
    if name=='strict_little' and (row['item'] in {'BERRYJUICE','DEEPSEATOOTH'} or set(row['moves'])&{'SONICBOOM','DRAGONRAGE'}):formvalues=[False]*len(formvalues)
    assert all(formvalues)==any(formvalues)
    if all(formvalues):eligible.append(row)
   cert=check_rows(eligible,name!='strict_little');math_count+=1
   certs.append({'file':trainerfile,'trainer_index':trainer_index,'profile':name,'eligible_occurrences':len(eligible),'certificate':cert})
   part[name].append(cert['maximum_matching'])
 profiles={name:{'minimum_matching':min(values),'no_team3_trainer_indices':[i for i,n in enumerate(values) if n<3],'no_robust_team4_trainer_indices':[i for i,n in enumerate(values) if n<4],'form_condition_changes_graph':[]} for name,values in part.items()}
 summary[trainerfile]={'trainers':len(pools),'templates':len(templates),'profiles':profiles}
assert summary==json.loads((H/'finite-pool-summary.json').read_text())
finished=datetime.datetime.now(datetime.timezone.utc).isoformat()
report={'schema':'gr8-independent-finite-graph-check/v1','reviewer':'/root/pbs_creature_facility/trait_eligibility','parent_inputs':parent_inputs,'child_traits':fileid(P/'finite-traits.json'),'start_utc':started,'end_utc':finished,'qualification':'TOOL_VALIDATION_OF_EXISTENCE_GRAPH_AND_STATIC_DATA_PROJECTION_ONLY','reference_game_behavior_model_execution':'NOT_EXECUTED','finite_4_by_4_graphs':small,'explicit_cases':edge_out,'finite_actual_pools':pool_count,'profiles_per_pool':8,'independent_actual_matching_checks':math_count,'independent_algorithm':'unit-capacity max-flow; feasible matching lower witness + equally sized vertex-cover upper certificate; compared to parent DFSaugment cardinalities','summary_exact_structural_equal':True,'all_some_shape_predicate_differences':form_differences,'cold_cache_premise':'normal successful fixed default creation; actual preexisting caches handled by generic predicates in graph-review.md','raw_projection_inputs':[fileid(R/f) for f in list(pairs)+list(pairs.values())],'remaining':'parent actual reception; full team gates/counts/total level and short-pool bypass remain separate source conditions','result':'PASS_FINITE_GRAPH_SCOPE'}
(P/'graph-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(P/'graph-certificates.json').write_text(json.dumps({'schema':'gr8-independent-lower-upper-graph-certificates/v1','records':certs,'all_behavior':'NOT_EXECUTED'},ensure_ascii=False,indent=2)+'\n')
(P/'independent-pool-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':'PASS_FINITE_GRAPH_SCOPE','synthetic_graphs':small,'pools':pool_count,'actual_profile_graphs':math_count,'summary_equal':True,'form_predicate_differences':len(form_differences),'utc':finished}),flush=True)
