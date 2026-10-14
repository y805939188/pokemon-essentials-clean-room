"""Join manually reviewed overlays; never grade semantics from interval overlap.
Input: task-local matrices/explicit manual overlays and current R6-B owner rows.
Output: task-local source-edge resolution; fixed source/formal identities preserved.
"""
import json, hashlib, datetime
from pathlib import Path
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-DX'
def read(name): return json.loads((OUT/name).read_text())
base=read('reverse-matrix.json')
editor=read('editor-vector-source-overlay.json')['rows']
animation=read('animation/coverage-counter.json')['animation_exact_source_test_overlay']
debug_document=read('debug/vector-source-overlay.json')
debug=debug_document if isinstance(debug_document,list) else debug_document.get('rows',debug_document.get('vectors',[]))
assert len(debug)==85, len(debug)
B=json.loads((OUT.parent/'R6-B/reverse-matrix.json').read_text())['rows']
overlays=[]
for owner,raw_rows in [('editor-vector',editor),('animation-vector',animation),('debug-vector',debug),('current-R6-B',B)]:
 for i,row in enumerate(raw_rows):
  formal=row.get('formal',row.get('formal_clause',{}))
  if not formal and 'path' in row and 'lines' in row: formal={'path':row['path'],'lines':row['lines']}
  if not formal: continue
  lines=formal.get('lines',[formal.get('start_line'),formal.get('end_line')])
  if not lines or lines[0] is None: continue
  overlays.append({'owner':owner,'ordinal':i,'formal_path':formal['path'],'formal_lines':lines,'source':row.get('source',row.get('sources',[])),'consumer':row.get('consumer',row.get('necessary_consumer',row.get('necessary_consumers'))),'inventory_evidence':row.get('inventory_evidence'),'scope':row.get('scope_portion',row.get('scope',row.get('assessment'))),'raw':row})
for block in base['rows']:
 links=[o for o in overlays if o['formal_path']==block['path'] and o['formal_lines'][0]<=block['end_line'] and o['formal_lines'][1]>=block['start_line']]
 block['explicit_source_overlays']=[{k:v for k,v in o.items() if k!='raw'} for o in links]
 block['semantic_PASS']=False
 block['final_classification']='PENDING_GLOBAL_ROOT'
 # Existing owner facts remain authoritative; overlays do not turn routing or reading into approval.
 block['evidence_policy']='Manual owner facts + exact source/consumer/premise; interval join only locates records. Mixed and outside-owner portions retain their own scope.'
base['manual_vector_source_overlays']=overlays
base['explicit_overlay_counts']={'editor':len(editor),'animation':len(animation),'debug':len(debug),'R6_B_owner_rows':len(B)}
base['source_edge_completion_policy']='Complete overlays for the assigned already-reviewed local vectors; scope/evidence-limit/other-owner rows are classified separately. No whole R6 semantic PASS.'
(OUT/'reverse-matrix.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
forward=read('forward-matrix.json')
forward['parts']['editor']=read('editor-forward-matrix.json')
forward['vector_source_overlays']={'editor':'editor-vector-source-overlay.json','animation':'animation/coverage-counter.json#animation_exact_source_test_overlay','debug':'debug/vector-source-overlay.json'}
forward['current_external_tool_owner']='../R6-B/report.md and reverse-matrix.json; identities recorded in interface-consumption.json'
(OUT/'forward-matrix.json').write_text(json.dumps(forward,ensure_ascii=False,indent=2)+'\n')
resolution={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'independent_counter':'animation/coverage-counter.json','counter_findings':read('coverage-counter-summary.json')['findings_about_coverage_claims'],'resolution':{'DX-COV-01':'24/19904 and11/3408 bound identities verified, never converted to semantic PASS','DX-COV-02':'65 root exact editor/supplement vector edges persisted; WP73-A/B297 block facts kept','DX-COV-03':'43 exact animation vector links consumed; WP74 metadata separately classified','DX-COV-04':'Official2422 IDs joined to per-line/aggregate rows;159 omitted structure/metadata read and explicitly classified','DX-COV-05':'85 Debug manual vector/boundary/structure rows now persist exact source edges or explicit nonbehavior classification; no reader-only approval','DX-COV-06':'Current B tools report/owner rows consumed. Kernel/domain responsibility routes remain explicitly global-owner scoped','DX-COV-07':'Parent class/module headers now list all intersecting manual facts; a header alone is not whole-body proof'},'metadata_and_scope_not_semantic_pass':True,'runtime_execution':0,'root_adjudication':'PENDING_GLOBAL_ROOT','input_hashes':{n:hashlib.sha256((OUT/n).read_bytes()).hexdigest() for n in ['editor-vector-source-overlay.json','debug/vector-source-overlay.json','animation/coverage-counter.json']}}
(OUT/'coverage-resolution.json').write_text(json.dumps(resolution,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'formal_blocks':len(base['rows']),'overlay_counts':base['explicit_overlay_counts'],'semantic_PASS':False,'decision':'PENDING_GLOBAL_ROOT'}))
