"""Structural projection of explicit manual notes, not an automatic semantic grader.
Inputs fixed notes and frozen source/formal denominator. Outputs task-local matrices.
"""
import json, re, subprocess, hashlib
from pathlib import Path
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-DX'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
notes=json.loads((OUT/'editor-review-notes.json').read_text())
formal={'A':'deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md','B':'deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md'}
facts=[]; units=[]
for filename, groups in notes['files'].items():
 rel='Data/Scripts/020_Debug/'+filename
 data=subprocess.check_output(['git','-C',str(ROOT/'reference/pokemon-essentials'),'show',REF+':'+rel])
 assert (ROOT/'reference/pokemon-essentials'/rel).read_bytes()==data
 lines=data.decode('utf-8-sig').splitlines()
 local=[]
 for k,g in enumerate(groups):
  start,end,fact,s,fs,fe,consumer=g
  row={'fact_id':'ED-'+filename.replace('/','_')+'-'+str(k+1),'source_path':'reference/pokemon-essentials/'+rel,'source_lines':[start,end],'fact':fact,'consumer':consumer,'formal_path':formal[s],'formal_lines':[fs,fe],'review_status':'MANUALLY_INTERPRETED_STATIC_ONLY','notes_provenance':'editor-review-notes.json'}
  facts.append(row);local.append(row)
 for n,line in enumerate(lines,1):
  m=re.match(r'^(\s*)(def|module|class)\s+([^\s(]+)',line)
  if not m: continue
  indent=len(m[1]);end=n
  if '; end' not in line:
   for j in range(n+1,len(lines)+1):
    if re.match(r'^'+r' '*indent+r'end\s*(?:#.*)?$',lines[j-1]):end=j;break
  parent=next((f for f in local if f['source_lines'][0]<=n<=f['source_lines'][1]),None)
  units.append({'source_path':'reference/pokemon-essentials/'+rel,'start_line':n,'end_line':end,'kind':m[2],'unit_name':m[3],'inventory_status':'STRUCTURALLY_ENUMERATED','semantic_evidence_fact':parent['fact_id'] if parent else None,'semantic_status':'ENCLOSING_UNIT_MANUALLY_REVIEWED' if parent else 'UNMAPPED_NEEDS_REVIEW','sha256':hashlib.sha256(data).hexdigest()})
(OUT/'editor-forward-matrix.json').write_text(json.dumps({'facts':facts,'units':units,'note':'Facts were explicitly manually supplied after full reading. Header extraction only establishes structure; it does not award PASS.'},ensure_ascii=False,indent=2)+'\n')
den=json.loads((OUT.parent.parent/'inventory/formal-block-denominator.json').read_text())
reverse=[]
for c in den:
 if c['path'] not in formal.values():continue
 matching=[f['fact_id'] for f in facts if f['formal_path']==c['path'] and f['formal_lines'][0]<=c['end_line'] and f['formal_lines'][1]>=c['start_line']]
 reverse.append({**c,'status':'MAPPED_TO_MANUAL_BEHAVIOR_FACTS' if matching else 'CONTEXT_OR_DEPENDENCY_REQUIRES_CLAUSE_CLASSIFICATION','fact_ids':matching,'verification':'STATIC_ONLY','no_automatic_pass':True})
(OUT/'editor-reverse-matrix.json').write_text(json.dumps(reverse,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'facts':len(facts),'structural_units':len(units),'unmapped_units':[u for u in units if not u['semantic_evidence_fact']],'reverse_blocks':len(reverse),'unmapped_blocks':sum(not r['fact_ids'] for r in reverse)},ensure_ascii=False))
