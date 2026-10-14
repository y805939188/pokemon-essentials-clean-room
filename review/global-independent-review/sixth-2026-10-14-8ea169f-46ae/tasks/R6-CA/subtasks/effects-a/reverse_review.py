"""Clause join for this subtask. Explicitly marks shared clauses owned by parent."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parent
base=R.parents[3]
denom=json.loads((base/'inventory/formal-block-denominator.json').read_text())
fwd=list(csv.DictReader((R/'forward-matrix.csv').open()))
names=['wp52-a-generic-numerical-and-status-evaluation.md','wp52-a-evaluation-coverage-and-data.md','wp52-b-field-damage-healing-and-target-evaluation.md','wp52-b-effect-coverage.md','wp52-c-items-calling-and-control-evaluation.md','wp52-c-item-control-coverage-and-data.md','combat-requirements-wp49-51-52.md']
rows=[]
for b in denom:
 p=Path(b['path'])
 if p.name not in names:continue
 a,z=b['start_line'],b['end_line'];txt='\n'.join(p.read_text().splitlines()[a-1:z])
 matched=[]
 for f in fwd:
  for loc in f['formal_clause'].split(' | '):
   path,sp=loc.rsplit(':',1)
   if path!=str(p):continue
   for part in sp.split(','):
    ab=part.split('-');lo=int(ab[0]);hi=int(ab[-1])
    if max(a,lo)<=min(z,hi):matched.append(f);break
 parent=''
 extra=''
 if p.name=='wp52-a-generic-numerical-and-status-evaluation.md':
  if 23<=a<=66: parent='005_AI/005_AI_ChooseMove.rb:177-323;005_AI/007_AI_ChooseMove_OtherScores.rb (full core review owned by parent)'
  if 70<=a<=108: parent='005_AI/011_AIMove.rb:30-561;005_AI/010_AIBattler.rb:rough_stat/type (full numerical source review owned by parent)'
  if 112<=a<=140: extra='005_AI/006_AI_ChooseMove_GenericEffects.rb:11-569;005_AI/011_AIMove.rb:549-561;005_AI/010_AIBattler.rb:292-317'
  if 219<=a<=231: extra='005_AI/008_AI_Utilities.rb:101-159,235-381;005_AI/010_AIBattler.rb:407-420'
  if a==15:extra='005_AI/008_AI_Utilities.rb:9-35;GR6-C-001 independent rebuttal: raw-array exception must be named'
 if p.name=='wp52-a-evaluation-coverage-and-data.md' and 215<=a<=235:extra='005_AI/008_AI_Utilities.rb:101-159;static-checks.json complete267 data equality'
 # Catalog is read in full. Only rows whose owned source is available are adjudicated here.
 if p.name=='combat-requirements-wp49-51-52.md':
  sec='AB' if a<43 else 'AI' if a<78 else 'AE' if a<142 else 'BE' if a<230 else 'CE'
  ident=re.match(r'\| ([A-Z0-9]+(?:b|c|d)?) \|',txt)
  tid=sec+'-'+ident[1] if ident else ''
  owned=(sec=='AE' and ident and ident[1].startswith(('G','S','T','F'))) or (sec=='BE' and ident and ident[1] in ['B28','B31','B34','B35','B36','B37','B38','B39','B40','B41','B42','B49']) or (sec=='CE' and ident and ident[1] in ['C35','C47','C48','C49','C50','C51'])
  if owned:extra='vector-review.md:'+tid
  elif ident:parent='Catalog source-numerical/other effect owner is parent or sibling; full text newly read here, no local semantic PASS inferred'
 nonnorm=txt.startswith('#') or txt.startswith('---') or bool(re.match(r'^\|\s*[-:]+',txt))
 if matched:state='OWNED_SOURCE_BRANCH_REVIEWED'
 elif extra:state='OWNED_CROSS_CLAUSE_REVIEWED'
 elif parent:state='READ_PARENT_SEMANTIC_OWNER'
 elif nonnorm:state='READ_STRUCTURAL_HEADING'
 else:state='READ_SCOPE_OR_OTHER_OWNER_CLAUSE'
 if p.name=='wp52-b-effect-coverage.md' and a==21:state='PROPOSED_LOCATOR_CORRECTION_R6-CA-EA-P001'
 rows.append({'clause_id':b['id'],'formal_path':str(p),'start_line':a,'end_line':z,'state':state,'facts':';'.join(dict.fromkeys(f['fact_id'] for f in matched)),'source_units':';'.join(dict.fromkeys(f["path"]+':'+f['line']+'['+f['family']+'/'+f['key']+']' for f in matched)),'additional_source_or_vector':extra,'parent_dependency':parent,'premises':'Registration phase and normal target consumer, ScoreMoves/PredictMoveFailure/medium gates remain separate; no runtime claim'})
with (R/'reverse-matrix.csv').open('w') as h:
 w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(json.dumps({'reverse_blocks':len(rows),'by_state':{s:sum(r['state']==s for r in rows) for s in sorted(set(r['state'] for r in rows))}},ensure_ascii=False))
