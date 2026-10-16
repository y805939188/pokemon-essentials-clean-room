"""Assemble audit ledgers from already read complete evidence. Grants no generated reading credit."""
from pathlib import Path
import json,hashlib,datetime,collections,re
R=Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text())
def save(n,x):(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def bind(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
BASE=10217888
T=read('decoded-tables.json');G=read('decoded-glyphs.json');P=read('decoded-programs.json');L=read('decoded-layout.json');S=read('static-push-roles.json')
BY={g['gid']:g for g in G};PS={p['unit']:p for p in P};ROLES={g['unit']:g for g in S['glyphs']}
contract=json.loads((R.parent.parent/'delegation/readsets/media_font_programs.complete.json').read_text())
font=(R.parent/'binary_remaining_texts/embedded-font.ttf').read_bytes()
for t in contract['full_primary_units']:
 own=T['tables'][t['table']];assert BASE+own['offset']==t['start'] and own['length']==t['bytes'] and own['sha256']==t['sha256']
 assert hashlib.sha256(font[own['offset']:own['offset']+own['length']]).hexdigest()==t['sha256']
# Numeric data graph checks, not interpretation/rendering.
def depth(gid,seen=()):
 assert gid not in seen
 return 0 if BY[gid]['kind']!='composite' else 1+max(depth(c['child'],seen+(gid,)) for c in BY[gid]['components'])
numeric={'all_component_depths':[depth(g) for g in BY],'padding_counts':dict(collections.Counter(g.get('padding','') for g in G))}
assert max(numeric['all_component_depths'])==1
assert all(not any(bytes.fromhex(g.get('padding',''))) for g in G)
for p in P[2:]:
 loop=1
 for i in p['code']:
  if i['name']=='CALL':assert loop==1
  elif i['name']=='SLOOP':loop=next(v for origin,pc,role,v in ROLES[p['unit']]['roles'] if pc==i['pc'] and role=='loop_count')
  elif i['name'] in ('IP','SHP'):loop=1
numeric['glyph_call_loop_invariant']=1
save('numeric-integrity.json',numeric)
# Every original complete FDEF body. IDs are preloaded, not discovered by a name regexp.
stack=[];functions=[];cur=None
for ins in P[0]['code']:
 if cur is None and ins['values']:stack+=ins['values']
 elif ins['name']=='FDEF':cur={'id':stack.pop(),'definition_pc':ins['pc'],'code':[]}
 elif ins['name']=='ENDF':
  cur['end_pc']=ins['end'];cur['code'].append(ins);functions.append(cur);cur=None
 else:assert cur is not None;cur['code'].append(ins)
assert cur is None and not stack and len(functions)==71
signs=read('function-signatures-check.json');meaning=(R/'facts.md').read_text().split('\n\n')
edges=[]
for f in functions:
 a=f['definition_pc'];b=f['end_pc'];f['font_relative_span']=[P[0]['offset']+a,P[0]['offset']+b];f['Game_span']=[BASE+P[0]['offset']+a,BASE+P[0]['offset']+b]
 f['sha256']=hashlib.sha256(font[f['font_relative_span'][0]:f['font_relative_span'][1]]).hexdigest()
 f['stack_interfaces']=[x for x in signs if x['id']==f['id']]
 f['meaning_paragraphs']=[x for x in meaning if re.search(r'F'+str(f['id'])+r'(?![0-9])',x)]
 f['read_credit']={'reader':'/root/media_font_programs','kind':'ACTUAL_FULL_DEFINITION','evidence':'functions-01.stdout','execution':'NOT_EXECUTED'}
 for k,i in enumerate(f['code']):
  if i['name']=='CALL':
   targets=[44,45,46,47] if f['id']==17 else [f['code'][k-1]['values'][-1]]
   edges.append({'from':f['id'],'pc':i['pc'],'targets':targets,'resolution':'finite arithmetic derivation in facts.md' if f['id']==17 else 'actual literal function ID'})
save('function-semantics.json',{'schema':'gr8-font-function-semantics/v1','registration_prefix_pc':[0,73],'registration_meaning':'Push all71 literal IDs; each FDEF consumes corresponding top ID; bodies end ENDF; no top-level state execution implied.','functions':functions,'call_edges':edges,'actual_source_full_reader':'/root/media_font_programs','execution':'NOT_EXECUTED'})
programs=[];glyphrows=(R/'glyphs.read.txt').read_text().splitlines()
glyph_ranges=[(1,300),(301,600),(601,900),(901,1200),(1201,1500),(1501,1800),(1801,2100),(2101,2347)]
for k,p in enumerate(P):
 row={'unit':p['unit'],'font_relative_span':[p['offset'],p['offset']+p['bytes']],'Game_span':[BASE+p['offset'],BASE+p['offset']+p['bytes']],'bytes':p['bytes'],'sha256':p['sha256'],'complete_code_pointer':'decoded-programs.json#/'+str(k)+'/code','read_status':'ACTUAL_FULL_PROGRAM','reader':'/root/media_font_programs','numeric_geometry':'full-range exact type/use; source values retained; no pixel assertion','control_data':'all actual values/consumers/control meaning read; no control operand exemption','execution':'NOT_EXECUTED'}
 if k<2:row['read_evidence']=['globals-final-full-read.stdout','functions-01.stdout'] if k==0 else ['globals-final-full-read.stdout','prep-01.stdout','verification-read-01.stdout']
 else:
  nr=k-1;a,b=next((a,b) for a,b in glyph_ranges if a<=nr<=b);row.update(read_evidence=[f'glyph-read-{a:04d}-{b:04d}.stdout'],read_row=nr,complete_read_spelling=glyphrows[nr-1],roles_pointer='static-push-roles.json#/glyphs/'+str(k-2),role_counts=ROLES[p['unit']]['roleCounts'])
 programs.append(row)
save('program-ledger.json',{'schema':'gr8-complete-font-program-ledger/v1','program_count':len(P),'program_bytes':sum(p['bytes'] for p in P),'opcode_count':sum(len(p['code']) for p in P),'unread_programs':0,'functions':71,'all_programs':programs,'actual_not_received_by_parent':len(P),'parent_reception':'PENDING_ACTUAL_CONTENT_RECEPTION','numeric_scope':'geometry numeric values typed over entire exact ranges; executable/control values actually read','glyph_control_additional_evidence':['delta-controls-short-read-001-100.stdout','delta-controls-short-read-101-300.stdout','delta-controls-short-read-301-568.stdout'],'full_roles':bind(R/'static-push-roles.json')})
table_records=[]
for t in contract['full_primary_units']:
 table_records.append(dict(t,read_status='ACTUAL_FULL_STRUCTURAL_SEMANTIC_READ_WITH_EXACT_NUMERIC_TYPE_USE',reader='/root/media_font_programs',meaning='facts.md',source='R/Game.exe',parent_reception='PENDING_ACTUAL_CONTENT_RECEPTION'))
glyphs=[]
for g in G:
 a,b=g['range'];row={'gid':g['gid'],'kind':g['kind'],'glyf_relative_span':[a,b],'Game_span':[BASE+T['tables']['glyf']['offset']+a,BASE+T['tables']['glyf']['offset']+b],'sha256':g['sha256'],'metric':g['hmetric'],'loca_entries':[g['gid'],g['gid']+1],'program':'g'+str(g['gid']) if g.get('instructionLength',0) else None,'structure_status':'complete typed boundary/point/component/flag/metric interpretation','numeric_disposition':'all coordinates/bbox/endPoints/deltas/metrics/point addresses retained and assigned geometry type/use over whole range','exact_structure_pointer':'decoded-glyphs.json#/'+str(g['gid'])}
 if g['kind']=='composite':row['all_components']=g['components'];row['component_depth']=depth(g['gid'])
 glyphs.append(row)
save('structure-ledger.json',{'schema':'gr8-font-complete-structure-ledger/v1','tables':table_records,'glyph_count':2587,'glyphs':glyphs,'numeric_table_bodies':{'source':'decoded-tables.json','fields':['head','hhea','maxp','cvt','loca']},'raw_layout_structures':read('raw-layout-structures.json'),'all_layout_rules':bind(R/'decoded-layout.json'),'unread_owned_tables':0,'unread_owned_glyph_structures':0,'execution':'NOT_EXECUTED'})
# Seven interface facets are local audit facets, not seven whole formal documents.
facets=[
 ('FONT-REQUESTS','wp17-messages-windows-input.md','§3.4/§8','MessageConfig default/getter/setter/pbSet*','PowerGreen27/Small21/Narrow27 offset8 are requests; host availability not asserted.'),
 ('FONT-CANDIDATES','wp17-messages-windows-input.md','§3.4','MessageConfig recursive getFontName','first available nonempty candidate; actual Font.exist remains unknown.'),
 ('FONT-NAME-STACK','wp17-draw-text-tags.md','§2/§6/§7','DrawText getFormattedText/getLastParam','fn stack and missing-name Arial fallback; normal-call context.'),
 ('FONT-SIZE-STACK','wp17-draw-text-tags.md','§2','DrawText getFormattedText','fs to_i/stack/application; no target acceptance asserted.'),
 ('FONT-CONSUMPTION','wp17-draw-text-tags.md','§2/§6/§7','drawSingleFormattedChar/drawFormattedChars','stored item font name/size consumed; normal final oldfont restoration, no exception rollback claim.'),
 ('FONT-MEASUREMENT','wp17-draw-text-tags.md','§3.1/§6/§7','getFormattedTextFast/getFormattedText','per-character Bitmap.text_size boundary; actual widths not measured.'),
 ('FONT-FIXTURE-LIMIT','wp17-draw-text-tags.md','§3.1','fixed B8 explicit fixture premise','8/8/4 fixture explicitly not PowerGreen measurement; no layout table guarantees actual application.')]
forward=[{'reference_unit':'font-table:'+t['table'],'source_span':[t['start'],t['end']],'disposition':'complete compatibility evidence; no obligatory reuse of VM/outlines/native classes','formal_destination':['FONT-REQUESTS','FONT-MEASUREMENT','FONT-FIXTURE-LIMIT'],'limits':['L04 concrete native selection/decoder','L08 actual host execution/visual']} for t in contract['full_primary_units']]
reverse=[{'facet':i,'fixed_formal':'deliverables/final-specification-set/user-interface/'+file,'clauses':clauses,'reference_units':src,'conclusion':con,'status':'SUPPORTED_IN_FINITE_STATIC_SCOPE','full_formal_text_read':True,'whole_formal_semantic_approval':False} for i,file,clauses,src,con in facets]
save('forward-mapping.json',{'schema':'gr8-font-forward/v1','denominator':{'owned_complete_tables':13,'owned_glyph_structures':2587,'owned_programs':2349,'fpgm_definitions':71,'local_interface_facets':7},'complete_units':forward,'all_glyph_and_program_mapping':'Each entire exact unit in structure/program ledgers maps through its owning glyf/fpgm/prep table; none is omitted for lack of default caller.','unmapped_owned_units':0,'current_formal_defects_proposed':0})
save('reverse-mapping.json',{'schema':'gr8-font-reverse/v1','local_facets':reverse,'denominator':7,'unreviewed_local_facets':0,'not_denominator_for_entire_WP17':True})
save('interfaces.json',{'schema':'gr8-font-interfaces/v1','interfaces':[
 {'id':'RAW-FONT-NATIVE','producer':'R/Game.exe fixed span','consumer':'209072 wrapper→indirect RW wrapper→681300→680fa0; parent native contributions','state':'bounded native facts received; full lower decoder/active selection OPEN','limit':'L04'},
 {'id':'FONT-CVT-VM','producer':'fpgm/prep/cvt','consumer':'all materialized glyph programs','state':'all readable declarations/calls/branches/control data actually read; actual state values/interpretation NOT_EXECUTED','limit':'L08'},
 {'id':'FONT-LAYOUT','producer':'GDEF/GSUB/GPOS/kern','consumer':'selected host shaping/measurement/drawing','state':'all rules complete; host feature/charmap/raster selection unknown','limits':['L04','L08']},
 {'id':'FONT-CONFIG-UI','producer':'MessageConfig/DrawText item formatting','consumer':'Font.exist?/Bitmap.font/text_size/draw_text','state':'complete named source units plus two full fixed formal texts read; calls/requests distinguished from host results','limit':'L08'}],'receiving_parent':'/root/resource_media_serialized_cloud','shared_full_read_credit':'original source readers retained; contribution reception does not mint second FULL vote'})
parent=R.parent/'resource_media_serialized_cloud'
names=['native-font-followup-contribution.json','native-font-deeper-contribution.json','native-font-driver-contribution.json','font-three-metadata-contribution.json','font-envelope-contribution.json']
receipts=[]
for n in names:
 obj=json.loads((parent/n).read_text());receipts.append(dict(bind(parent/n),source_full_reader='/root/resource_media_serialized_cloud',receiver='/root/media_font_programs',receipt='ACTUAL_COMPLETE_CONTRIBUTION_CONTENT_RECEIVED_WITH_PREMISES_AND_OPEN_BOUNDARIES',new_source_full_vote=False,body_credit='Parent retains original FULL; mine is contribution receipt only.'))
save('receptions.json',{'schema':'gr8-font-receptions/v1','utc':UTC,'records':receipts,'receiving_evidence':['native-contribution-read-01.stdout','native-contribution-read-02.stdout','native-contribution-read-03.stdout','metadata-parent-read.stdout','parent-envelope-compact-read.stdout'],'native_functions_instructions_parent_original':3208,'own_native_source_instructions_full_credit':0})
reads=[{'scope':'full instruction contracts/AGENTS/skill/readset','status':'ACTUAL_FULL_TEXT_READ','earliest_local_separate_capture':'initial platform outputs retained; initial per-command UTC not retroactively invented'},
 {'scope':'13 full owned font tables / 2587 glyph structures','status':'ACTUAL_COMPLETE_STATIC_SEMANTICS_PLUS_FULL_RANGE_NUMERIC_TYPE_USE','structure_ledger':'structure-ledger.json'},
 {'scope':'71 complete fpgm definitions and registration prefix','status':'ACTUAL_FULL','evidence':['globals-final-full-read.stdout','functions-01.stdout'],'ledger':'function-semantics.json'},
 {'scope':'complete prep including actual preloaded stack/control prologue/calls','status':'ACTUAL_FULL','evidence':['globals-final-full-read.stdout','prep-01.stdout','verification-read-01.stdout']},
 {'scope':'2347 entire glyph programs','status':'ACTUAL_FULL','evidence':[f'glyph-read-{a:04d}-{b:04d}.stdout' for a,b in glyph_ranges],'numeric_values':'All controls actually read; geometry/CVT address numeric values assigned exact type/use across complete source spans.'},
 {'scope':'5927 DELTAP packed controls in568 glyphs','status':'ACTUAL_FULL_VALUES_AND_MEANING_READ','evidence':['delta-controls-short-read-001-100.stdout','delta-controls-short-read-101-300.stdout','delta-controls-short-read-301-568.stdout']},
 {'scope':'all GDEF/GPOS/GSUB/kern rules and raw original Coverage/ClassDef ranges','status':'ACTUAL_FULL','evidence':['layout-read-01.stdout','layout-read-02.stdout','layout-read-03.stdout','layout-read-04.stdout','gpos-pairs-01.stdout','gpos-pairs-02.stdout','gpos-pairs-03.stdout','gpos17-read.stdout','kern-read.stdout','raw-layout-ranges-read.stdout']},
 {'scope':'two full fixed formal documents','status':'ACTUAL_FULL_TEXT_READ_LOCAL_FONT_INTERFACE_SEMANTICS','evidence':['formal-messages-complete-01.stdout','formal-messages-complete-02.stdout','formal-drawtags-final-read.stdout']},
 {'scope':'MessageConfig.rb whole text; mkxp.json whole text; named DrawText complete units only','status':'ACTUAL_READ_WITH_NAMED_SEMANTIC_SCOPE','DrawText_complete_units':['getFormattedTextForDims119..126','getFormattedTextFast128..242','getLastParam248..255','getLastColors257..269','getFormattedText345..784','drawSingleFormattedChar940..1001','drawFormattedChars1003..1011'],'DrawText_whole_file_full_credit':False},
 {'scope':'5 complete parent native/metadata/envelope contributions','status':'ACTUAL_CONTENT_RECEIVED','ledger':'receptions.json','new_source_full_vote':False},
 {'scope':'parent original name/post/cmap bodies','status':'PARENT_ORIGINAL_FULL_CREDIT_ONLY_NO_NEW_SOURCE_FULL','input_auxiliary_cmap_structure_index':'identity verified; own source13 tables independently decoded; no new textual cmap/post/name credit from helper JSON'},
 {'scope':'native whole CFG/SFNT service/selected callbacks/VM implementation','status':'NAMED_OPEN_L04','disposition':'outside complete finite native contribution; no arbitrary full-Game reversal demanded'},
 {'scope':'actual target Font.exist/text_size/hinting/UI visual','status':'NOT_EXECUTED_L08'}]
save('reading-ledger.json',{'schema':'gr8-font-reading-ledger/v1','reader':'/root/media_font_programs','utc':UTC,'actual_source_full_distinct_reader_count':1,'records':reads,'unread_within_owned13_tables':0,'unread_within_owned2587_glyph_structures':0,'unread_within_owned2349_programs':0,'pending_parent_reception_owned_tables':13,'pending_parent_reception_status':'NO_RECEIPT_ASSUMED','tool_success_semantic_credit':0,'all_target_execution':0})
save('proposals.json',{'schema':'gr8-font-proposals/v1','required':[],'optional':[],'policy':[],'new_formal_defect_proposals':0,'no_required_scope':'Complete finite font programs/layout/consumer font interfaces at fixed B8; full negative rationale in facts.md and reverse mapping. Not global NO_REQUIRED_UPDATE.','no_defect_counterproof':'No defect was proposed; actual different receiver still required for complete facts.','source_peculiarities':[{'unit':'F49','fact':'8→0 vs5→0 conditional stack interface','disposition':'no actual materialized caller; not elevated to fixed formal defect'},{'unit':'parent native callbacks','fact':'selected callee errors/callback bodies bounded separately','disposition':'no unsupported host-success/rollback claim'}],'limits':[{'id':'L04','open':'active class registration/selection; sfnt service +08/+10; installed callback bodies69ace0/69ad40/6997a0/69b0c0/69e1e0; glyph loader/VM lower CFG'},{'id':'L08','open':'Font.exist/text_size/hinting/visual; actual host feature/charmap/raster behavior'}],'UPDATE_NOT_STARTED':True})
save('progress.json',{'schema':'gr8-font-progress/v1','owner':'/root/media_font_programs','receiver':'/root/resource_media_serialized_cloud','utc':UTC,'status':'READ_COMPLETE_AWAITING_ACTUAL_PARENT_RECEPTION','source_contract_history':'PROPOSED_NOT_APPLIED_0START retained unchanged; this actual task ran after real spawn','requested':contract['requested'],'actual':contract['actual'],'write_set':str(R),'owned_totals':{'tables':13,'glyphs':2587,'programs':2349,'definitions':71},'read_complete':{'tables':13,'glyphs':2587,'programs':2349,'definitions':71},'owned_unread':0,'owned_pending_parent_reception_tables':13,'open':['named L04 lower native graph','L08 actual host execution'],'platform_task':'/root/media_font_programs; real platform tool/collaboration logs','files':['facts.md','identities.json','reading-ledger.json','program-ledger.json','function-semantics.json','structure-ledger.json','forward-mapping.json','reverse-mapping.json','interfaces.json','receptions.json','proposals.json','review.md'],'first_local_captured_run':read('decode-01.json'),'target_executions':0,'update':'UPDATE_NOT_STARTED','commit_push':'not performed; root exclusive'})
print(json.dumps({'utc':UTC,'tables':len(table_records),'glyphs':len(glyphs),'programs':len(programs),'functions':len(functions),'GPOS_subtables':sum(len(x['subtables']) for x in L['GPOS']['lookups']),'GSUB_subtables':sum(len(x['subtables']) for x in L['GSUB']['lookups']),'raw_layout_structures':len(read('raw-layout-structures.json')),'parent_receipts':len(receipts),'padding':numeric['padding_counts'],'native_FULL_credit_here':0}))
