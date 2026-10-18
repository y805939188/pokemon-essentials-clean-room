"""Independent current-default PBS normalization and finite graph tool check.
No reference/game/ruleset/behavior model functions are evaluated. Mathematical
helpers are read from the previous local verifier; all new output stays here.
"""
from pathlib import Path
from collections import defaultdict,deque
import collections,ast,hashlib,json,datetime
P=Path(__file__).parent;H=P.parent.parent;R=Path('/workspace/pokemon-essentials')
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
def fid(p):
 b=p.read_bytes();return {'path':str(p.resolve()),'bytes':len(b),'lines':len(b.splitlines()),'sha256':hashlib.sha256(b).hexdigest()}
auditid=fid(H/'finite-pool-audit.py');summaryid=fid(H/'finite-pool-summary.json')
assert auditid['sha256']=='43c8f5ccc038a5fd4f143d84d5247eb3db392ef67cbe85406a20e94b275069b2'
assert summaryid['sha256']=='fef3f71acff4666555e56d2df7d285dacc6f50982682818135c9885f1425ac91'
ns={'collections':collections,'defaultdict':defaultdict,'deque':deque,'R':R}
parent=ast.parse((H/'finite-pool-audit.py').read_text());node=next(q for q in parent.body if isinstance(q,ast.FunctionDef) and q.name=='certificate')
exec(compile(ast.Module(body=[node],type_ignores=[]),'<current parent math certificate only>','exec'),ns);ns['parent_certificate']=ns['certificate']
old=ast.parse((P/'independent-graph-check.py').read_text());wanted={'maxflow_certificate','check_rows','read_templates','read_pools'}
exec(compile(ast.Module(body=[q for q in old.body if isinstance(q,ast.FunctionDef) and q.name in wanted],type_ignores=[]),'<local math verification helpers only>','exec'),ns)

def headers(file):return {s[1:-1] for s in (R/file).read_text(encoding='utf-8-sig').splitlines() if s.startswith('[')}
ids={'items':headers('PBS/items.txt'),'moves':headers('PBS/moves.txt')}
pairs={'PBS/battle_tower_trainers.txt':'PBS/battle_tower_pokemon.txt','PBS/cup_fancy_trainers.txt':'PBS/cup_fancy_pkmn.txt','PBS/cup_fancy_trainers_single.txt':'PBS/cup_fancy_pkmn_single.txt','PBS/cup_little_trainers.txt':'PBS/cup_little_pkmn.txt','PBS/cup_pika_trainers.txt':'PBS/cup_pika_pkmn.txt','PBS/cup_poke_trainers.txt':'PBS/cup_poke_pkmn.txt'}
tables={file:ns['read_templates'](file) for file in pairs.values()}
unknownitems=[];unknownmoves=[];blankmoves=0;nil_farfetchd_raw=0;stick_edges=[]
for file,rows in tables.items():
 for row in rows:
  if row['species']=='FARFETCHD' and row['item'] is None:nil_farfetchd_raw+=1
  if row['item']=='STICK':stick_edges.append({'file':file,'index':row['index'],'line':row['line'],'species':row['species']})
  row['raw_item']=row['item'];row['raw_moves']=row['moves'].copy()
  if row['item'] and row['item'] not in ids['items']:
   unknownitems.append({'file':file,'index':row['index'],'line':row['line'],'species':row['species'],'raw_item':row['item'],'normalized_item':None});row['item']=None
  for m in row['moves'][:4]:
   if m and m not in ids['moves']:unknownmoves.append({'file':file,'index':row['index'],'line':row['line'],'species':row['species'],'unknown_move':m})
   if not m:blankmoves+=1
  row['moves']=[m for m in row['moves'][:4] if m in ids['moves']]
  assert row['moves'] # No first-registry-move fallback in current finite inputs.
assert len(unknownitems)==1 and unknownitems[0]['raw_item']=='STICK' and unknownitems[0]['index']==137 and unknownitems[0]['line']==140
assert len(unknownmoves)==1 and unknownmoves[0]['unknown_move']=='VICEGRIP' and unknownmoves[0]['index']==249 and unknownmoves[0]['line']==252
assert len(stick_edges)==1 and stick_edges[0]['species']=='FARFETCHD' and nil_farfetchd_raw==0
assert all(not q['item'] or not q['item'].startswith('@free:') for rows in tables.values() for q in rows)
traits=defaultdict(list)
for row in json.loads((P/'finite-traits.json').read_text())['records']:
 if row['dataset']=='default' and row['template_created_this_form']:traits[row['species']].append(row)
keys={'all_normal':None,'standard':'standard_non_egg','fancy':'fancy_species_cold','little_factory':'little_factory_species_cold','little_direct':'little_direct_species_cold','light_direct':'light_direct_species_cold','strict_little':'strict_species_cold','factory':'factory_species'}
summary={};certificates=[];poolcount=0;graphcount=0
for trainerfile,templatefile in pairs.items():
 table=tables[templatefile];pools=ns['read_pools'](trainerfile);poolcount+=len(pools);part={name:[] for name in keys}
 for trainer,pool in enumerate(pools):
  for name,key in keys.items():
   eligible=[]
   for index in pool:
    row=table[index];values=[True if key is None else q[key] for q in traits[row['species']]]
    if name=='strict_little' and (row['item'] in {'BERRYJUICE','DEEPSEATOOTH'} or set(row['moves'])&{'SONICBOOM','DRAGONRAGE'}):values=[False]*len(values)
    assert all(values)==any(values)
    if all(values):eligible.append(row)
   cert=ns['check_rows'](eligible,name!='strict_little');graphcount+=1;part[name].append(cert['maximum_matching'])
   certificates.append({'file':trainerfile,'trainer_index':trainer,'profile':name,'eligible_occurrences':len(eligible),'normalized_current_default':True,'certificate':cert})
 summary[trainerfile]={'trainers':len(pools),'templates':len(table),'profiles':{name:{'minimum_matching':min(values),'no_team3_trainer_indices':[i for i,n in enumerate(values) if n<3],'no_robust_team4_trainer_indices':[i for i,n in enumerate(values) if n<4],'form_condition_changes_graph':[]} for name,values in part.items()}}
assert summary==json.loads((H/'finite-pool-summary.json').read_text())
assert summary==json.loads((P/'independent-pool-summary.json').read_text())
end=datetime.datetime.now(datetime.timezone.utc).isoformat()
report={'schema':'gr8-normalized-graph-independent-check/v1','start_utc':start,'end_utc':end,'parent_script':auditid,'parent_summary':summaryid,'traits':fid(P/'finite-traits.json'),'previous_verification':fid(P/'graph-check.json'),'previous_raw_check_preserved':True,'new_actual_normalized_recompute':True,'pools':poolcount,'profile_graphs':graphcount,'summary_exact_equal_to_current_parent':True,'summary_exact_equal_to_prior_raw_projection':True,'normalization':{'unknown_items':unknownitems,'unknown_moves':unknownmoves,'blank_move_slots_removed':blankmoves,'all_rows_have_surviving_move':True,'STICK_occurrences':stick_edges,'raw_FARFETCHD_nil_item_occurrences':nil_farfetchd_raw},'endpoint_proof':'STICK occurs at one FARFETCHD row only, and FARFETCHD has no raw nil item row in these2770 templates. In every retained graph containing that row, right STICK is a private leaf of left FARFETCHD and can be renamed to the previously absent FARFETCHD-private nil endpoint; all other edges unchanged. StrictLittle already uses species-private endpoints regardless of item, and STICK/nil are both outside its held ban.','move_proof':'Only unknown nonempty move VICEGRIP occurs in Tower index249; surviving moves BUBBLEBEAM,KNOCKOFF,PROTECT remain. Neither VICEGRIP nor any survivor is SONICBOOM/DRAGONRAGE, and no other projected member predicate consumes these move slots. RETURN conversion also cannot introduce either forbidden ID.','algorithm':'independent unit-capacity max-flow with equally sized vertex-cover upper bound, compared to current parent certificate; no rerun of unaffected65536 mathematical graph suite','behavior_execution':'NOT_EXECUTED','reference_game_behavior_model_processes':0,'math_tool_processes_this_followup':1,'result':'PASS_CURRENT_DEFAULT_NORMALIZED_GRAPH_SCOPE','underlying_exit':'recorded in normalized-graph-tool-execution.json after actual process exit'}
(P/'normalized-graph-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(P/'normalized-graph-certificates.json').write_text(json.dumps({'schema':'gr8-normalized-independent-graph-certificates/v1','records':certificates,'behavior':'NOT_EXECUTED'},ensure_ascii=False,indent=2)+'\n')
(P/'normalized-pool-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':report['result'],'normalized_actual_profile_graphs':graphcount,'pools':poolcount,'summary_current_parent_equal':True,'unknown_item_occurrences':len(unknownitems),'unknown_move_occurrences':len(unknownmoves),'parent_script_sha256':auditid['sha256'],'parent_summary_sha256':summaryid['sha256'],'end_utc':end}),flush=True)
