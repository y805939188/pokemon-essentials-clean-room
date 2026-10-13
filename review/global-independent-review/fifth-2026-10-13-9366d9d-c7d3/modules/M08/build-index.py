"""Audit navigation only: consumes the reviewer's completed range comparisons.
It never executes, imports, translates or simulates reference behavior.
"""
import sys,re,json,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
from ledger import read,write,ROOT
cov=read('reading-coverage.json');out=read('source-to-spec.json');rev=read('spec-to-source.json')
R=Path(cov['source_baseline']['root']);S=Path(cov['specification_baseline']['root']);version=cov['source_baseline']['commit'];bversion=cov['specification_baseline']['commit']
specfiles={f['path']:(Path(f['path']).read_text().splitlines(),f) for f in rev['specifications']}
missing={'UserSwapBaseAtkDef','UserTargetSwapBaseSpeed','UserTargetAverageBaseAtkSpAtk','UserTargetAverageBaseDefSpDef'}
move_caps={};navigation_gaps=[]
for f in cov['sources']:
 if '/003_Move/' not in f['path']:continue
 lines=(R/f['path']).read_text().splitlines();entries=[]
 for i,line in enumerate(lines):
  m=re.match(r'class Battle::Move::(\w+)',line)
  if not m:continue
  end=i+1
  while end<len(lines) and lines[end]!='end':end+=1
  name=m[1];cover=[v for v in f['semantic_ranges'] if v['lines'][0]<=i+1<=v['lines'][1]];segment=cover[-1] if cover else None
  if not segment:raise ValueError('Body without semantic disposition: '+name)
  anchors=[]
  for path,(doc,_) in specfiles.items():
   if '/test-catalog/' in path:continue
   hits=[n for n,l in enumerate(doc,1) if re.search(r'(?<![\w])'+re.escape(name)+r'(?![\w])',l)]
   if hits:anchors.append({'path':path,'version':bversion,'lines':[[n,n] for n in hits],'anchor_role':'behavior_or_coverage_identity; read together with manually compared contract segment'})
  cid='M08-MOVE-'+name
  extent='missing' if name in missing else 'unresolved' if name in ['BurnAttackerBeforeUserActs','Unimplemented'] else 'supported'
  if not anchors:navigation_gaps.append(name)
  cap={'id':cid,'name':name,'classification':['Pokémon Rules','Combat Requirements'],'source_anchors':[{'path':f['path'],'version':version,'lines':[[i+1,end+1]],'entry':name}],'specification_anchors':anchors,'manually_compared_contracts':segment['specification_anchors'],'rules_checked':segment['semantic_comparison'],'capability_status':extent,'supported_boundary':'supported_static: full local effect body and shared rules read at fixed R/B5; execution, independent counterevidence and broader M07/M09 sign-off excluded' if extent=='supported' else None,'evidence_level':'static_source_and_contract_comparison','review_extent':'full','shared_contract_identity':cid,'consumer_projections':[],'execution_status':'NOT_EXECUTED','related_findings':['GR5-M08-001'] if name in missing else ['GR5-M08-002'] if name=='BurnAttackerBeforeUserActs' else [],'indexing_note':'Literal lookup only indexes clauses after the documented full human/model semantic reading; not proof by string match.'}
  if name=='Unimplemented':cap['unknowns']=['Default 740 move records all bind existing effects. Core unknown-function fallback body reviewed; full configurable-content contract counterevidence outside primary specs is not closed. Do not assert missing yet.']
  move_caps[name]=cap;entries.append({'line':i+1,'lines':[i+1,end+1],'entry':name,'shared_rule_id':cid,'review_extent':'full','material_availability':'available','evidence_level':'static_source_and_contract_comparison','semantic_comparison':segment['semantic_comparison'],'specification_anchors':anchors,'manually_compared_contracts':segment['specification_anchors'],'capability_status':extent,'unreviewed_ranges':[]})
 f['effect_entry_inventory']=entries
# Every reopening is a source projection of the same effect, not another feature.
clauses=next(f for f in cov['sources'] if f['path'].endswith('006_Battle_Clauses.rb'))
clines=(R/clauses['path']).read_text().splitlines()
for i,l in enumerate(clines):
 m=re.match(r'class Battle::Move::(\w+)',l)
 if not m or m[1] not in move_caps:continue
 end=i+1
 while end<len(clines) and clines[end]!='end':end+=1
 move_caps[m[1]]['source_anchors'].append({'path':clauses['path'],'version':version,'lines':[[i+1,end+1]],'entry':'loaded clause override','role':'effective-entry override, not independent effect'})
for c in move_caps.values():out['capabilities'].append(c)
# Exact source constant/data input projections, not additional capabilities.
data=read('data-audit.json')
for v in data['move_records']:
 effect=v['data']['FunctionCode'] or 'None';cap=move_caps.get(effect)
 v['review_extent']='partial';v['semantic_status']='battle_parameter_projection_read_and_compared';v['reviewed_fields']=list(v['data']);v['unreviewed_fields']=['display Name/Description prose','compiler/runtime artifact generation'];v['capability_status']='partial';v['evidence_level']='static_data_projection_and_effect_semantics';v['semantic_boundary']='Reviewer inspected all 740 printed battle-parameter records in four complete batches. Data-to-effect binding and relevant default sample/vector inputs checked; most roster rows are configurable input, not individually specified normative constants. No full PBS prose/content or runtime claim.'
 v['shared_rule_id']=cap['id'] if cap else None
 if cap:cap['consumer_projections'].append({'kind':'default_move_data','path':'PBS/moves.txt','version':version,'data_id':v['id'],'lines':v['source_lines'],'key_lines':v['key_lines'],'evidence_level':'static_data_projection','independent_feature_count':False})
write('data-audit.json',data)
# Repair ranges for prebuilt ability/item anchors against inspected declaration navigation.
for f in cov['sources']:
 if not any(k in f['path'] for k in ['AbilityEffects.rb','ItemEffects.rb']):continue
 for e in f['effect_entry_inventory']:
  cid=e.get('shared_rule_id')
  if not cid:continue
  cap=next(c for c in out['capabilities'] if c['id']==cid)
  for a in cap['source_anchors']:
   if isinstance(a,dict) and a.get('path')==f['path']:
    ls=a.get('lines',[])
    if ls and isinstance(ls[0],int) and ls[0]==e['line']:a['lines']=e['lines']
# Add source paragraphs as shared contract anchors for anonymous/Chinese clauses.
by_spec={p:[] for p in specfiles}
for f in cov['sources']:
 for seg in f['semantic_ranges']:
  for ref in seg['specification_anchors']:
   if not isinstance(ref,str):continue
   for path in by_spec:
    if Path(path).name in ref:
     by_spec[path].append({'path':f['path'],'version':version,'lines':[seg['lines']],'entries_and_rules':seg['entries_and_rules'],'semantic_comparison':seg['semantic_comparison'],'capability_status':seg['capability_status']})
for path,(doc,spec) in specfiles.items():
 heading='';clauses_out=[]
 for n,l in enumerate(doc,1):
  if l.startswith('#'):heading=l.lstrip('#').strip();continue
  if not l.strip() or l.strip()=='---' or re.match(r'^\|[\s:|\-]+$',l):continue
  if '/test-catalog/' in path:
   if path.endswith('wp39-40-41-42-45.md') and not 163<=n<=231:continue
   if path.endswith('wp49-51-52.md') and n>42:continue
  ids=[];anchors=[]
  for c in out['capabilities']:
   for a in c.get('specification_anchors',[]):
    if not isinstance(a,dict) or a.get('path')!=path:continue
    if any(isinstance(x,list) and x[0]<=n<=x[-1] for x in a.get('lines',[])):
     ids.append(c['id']);anchors.extend(z for z in c['source_anchors'] if isinstance(z,dict))
  # Exact named default data instances in tests and prose are consumer projections.
  data_refs=[]
  for v in data['move_records']:
   if re.search(r'(?<![A-Z0-9])'+re.escape(v['id'])+r'(?![A-Z0-9])',l):
    data_refs.append({'path':'PBS/moves.txt','version':version,'data_keys':[v['id']],'lines':[v['source_lines']],'shared_rule_id':v.get('shared_rule_id')})
  explicit=bool(anchors or data_refs)
  if not anchors:anchors=by_spec.get(path,[])
  ids=list(dict.fromkeys(ids));v_id=l.split('|')[1].strip() if l.startswith('|') else None
  clauses_out.append({'lines':[n,n],'section':heading,'kind':'table_row_or_vector' if l.startswith('|') else 'paragraph_or_scope','vector_or_row_id':v_id,'source_anchors':anchors,'data_anchors':data_refs,'shared_rule_ids':ids,'review_extent':'full' if explicit else 'partial','capability_status':'unresolved' if any(k in l for k in missing) else 'partial','evidence_level':'static_clause_comparison' if explicit else 'static_segment_comparison_navigation','supported_boundary':'No runtime claim. Exact named identity/table mappings accompany manually documented segment comparisons; fallback segment lists are not represented as independently closed clause proofs.','comparison_note':'Read in full during this review; exact line-level counterevidence closure is pending where only a segment mapping is available.'})
 spec['clause_mappings']=clauses_out
 spec['current_effective_supplements']=[{'path':'review/remediation-third-20261012-prepare/U04/actual-integration/source-successor.json','version':bversion,'semantic_scope':'GR3-M08-001 substantive record only: NaturalGift self-consumption second-hit failure and high-HP/single-hit controls','use':'Current linked supplemental facts compared to already-read primary sources; historical PASS not evidence'}] if any(k in path for k in ['wp46','wp47-a','wp50','pokemon-rules-wp43','combat-requirements-wp47-ab']) else []
 spec['clause_mapping_status']='partial_explicit: exact named mappings present; anonymous paragraphs retain segment navigation and are NOT counted as complete independent clause closure'
# Preserve every source including unreviewed dependencies honestly.
out['source_files']=[{'path':f['path'],'version':f['version'],'actual_semantic_ranges':f['semantic_ranges'],'review_extent':f['review_extent'],'material_availability':f['material_availability'],'evidence_level':f['evidence_level'],'unreviewed_ranges':f['unreviewed_ranges']} for f in cov['sources']]
out['coverage_interpretation']='Capabilities count unique shared rules; aliases/reopenings/default-move data are projections. Full body reading is distinguished from full contract/consumer closure.'
out['move_index_navigation_gaps']=navigation_gaps
write('source-to-spec.json',out);write('spec-to-source.json',rev);write('reading-coverage.json',cov)
print('Indexed move definitions:',len(move_caps),'; no direct literal-name anchor:',navigation_gaps)
print('Reverse clause rows:',sum(len(f.get('clause_mappings',[])) for f in rev['specifications']))
print('Anonymous clause fallbacks remain explicitly partial; complete review must not be claimed from this index.')
