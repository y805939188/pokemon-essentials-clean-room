from pathlib import Path
import json,re,datetime
O=Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/ui_navigation_audit');j=json.loads((O/'forward.json').read_text());facts=j['facts'];M='deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md';C='deliverables/final-specification-set/user-interface/wp65-controls-help-appendix.md';T='deliverables/final-specification-set/user-interface/wp65-trainer-card-appendix.md';CAT='deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
# These are manually audited clause bindings, replacing broad range routing.
bind={
'LANGUAGE':[135]*4,
'BOOT':[27,27,27,28,27,27,27,27,31,31],
'TITLE':[29,29,29,29,29,29,29,30,30,30,30,30],
'LOADGATE':[35,35,35,67,67,63,64,65,36,36,38,39,[40,41,44],42,43],
'LOADPANEL':[45,45,45,45,[45,57],57,59,45,45,[45,76],72,46,46],
'LOADCOMMAND':[48,49,50,51,[52,136,144],[52,136,144],[52,136,144],[52,136,144],52,53,54,46],
'SAVE':[87,87,88,89,89,[89,90],90,90,90,100,98,99,99,88],
'EVENTSAVE':[152,100,31],
'EMERGENCY':[94,94,94,94,94,94],
'OPTIONFRAME':[107,108,109,110,110,110,111,111,112,112,113,112,113],
'OPTIONCONSUMER':[120,120,120,121,134,136,[142,143,145],146,[146,232]],
'RESIZE':[130]*7,
'MAPINPUT':[152]*13,
'PAUSELOOP':[153,153,154,154,154,154,250],
'SESSIONS':[174,174,174,174,174,174,171,171,172,172,174,238],
'PC':[181,181,[181,190],186,192,196,181,186,186,186,196,[198,200],199,201,203,204,204,204,204,204,[181,196,259]],
'PCEXTRA':[188,189,189,[188,189],261],
'READYBUILD':[212,212,213,214,214,228],
'READYUI':[218,218,218,218,[219,220],219,219,220,220,220,220],
'READYUSE':[225,225,226,227,227,227,227,227,227,250],
'PREVIEW':[[77,78],79,[76,77,78],79,81],
'HELP':[23,28,47,30,31,31,16,39,44,38,38,37,44,48,53],
'CARD':[15,31,32,33,33,33,37,37,37,[37,46],38,38,39,43,43,59],
'CREDITS':[461,461,461,459,460,460],
'CLOCK':[29,29,[29,31],30],
'CURSORINPUT':[220,220,219]}
# Additional assertions beyond a literal current clause are retained as source facets, not implied support.
source_facets={'UIF-READYUI-06','UIF-READYUI-09','UIF-READYUI-11','UIF-CURSORINPUT-01','UIF-CURSORINPUT-02','UIF-CURSORINPUT-03','UIF-EMERGENCY-02','UIF-EMERGENCY-04','UIF-EMERGENCY-06','UIF-CREDITS-02','UIF-CREDITS-03','UIF-CREDITS-06','UIF-SESSIONS-12','UIF-EVENTSAVE-01','UIF-EVENTSAVE-03'}
for f in facts:
 m=re.fullmatch(r'UIF-(.+)-(\d+)',f['id']);g,idx=m.group(1),int(m.group(2))-1
 if re.fullmatch(r'OPT\d+',g):lines=[119+int(g[3:])-1]
 elif g.startswith('PAUSE') and g!='PAUSELOOP':lines=[161+int(g[5:])-1]
 else:
  assert idx<len(bind[g]),(g,idx,len(bind[g]))
  v=bind[g][idx];lines=v if isinstance(v,list) else [v]
 path=C if g=='HELP' else T if g=='CARD' else CAT if g=='CREDITS' else M
 f['spec_locations']=[{'path':path,'line':n} for n in lines]
 f['relation']='ADDITIONAL_SOURCE_FACET_NEEDS_PRECISE_SCOPE' if f['id'] in source_facets else ('DISPUTED_LITERAL_SCOPE_GR8_UI_001' if f['id']=='UIF-SAVE-14' else 'BOUNDED_CLAUSE_SUPPORT')
 # Keep original range only as historical discovery route, never final support.
 f['discovery_section_route']=f.pop('spec')
# Repeated summaries receive the same bounded atom IDs, without creating duplicated source facts.
repeat={
17:['OPTIONFRAME-04','OPTIONFRAME-05','PAUSELOOP-01','PC-01'],
18:['OPTIONFRAME-12','OPTIONFRAME-13','LOADCOMMAND-05','EMERGENCY-03'],
19:['PAUSELOOP-05','PAUSELOOP-06','LOADCOMMAND-11'],
20:['PAUSELOOP-02','PAUSELOOP-04','PC-02','PC-06','PC-07','READYUI-05','OPTIONCONSUMER-08','OPTIONCONSUMER-09'],
21:['READYBUILD-06','PC-08','PC-09','SAVE-03'],
35:['LOADGATE-01','LOADGATE-02','LOADGATE-03','LOADGATE-04','LOADGATE-05'],
36:['LOADGATE-09','LOADGATE-10'],
38:['LOADPANEL-01'],42:['BOOT-07'],45:['PREVIEW-01','PREVIEW-02','PREVIEW-03','PREVIEW-04'],
55:['LOADCOMMAND-11'],57:['LOADPANEL-05','LOADPANEL-06'],59:['LOADPANEL-07'],63:['LOADGATE-06'],64:['LOADGATE-07'],65:['LOADGATE-08'],66:['LOADGATE-06','LOADGATE-07'],67:['LOADGATE-04','LOADGATE-05'],72:['LOADPANEL-10','LOADPANEL-11'],
98:['SAVE-03','SAVE-07','SAVE-08','SAVE-11'],99:['SAVE-12','SAVE-13'],100:['SAVE-10','EVENTSAVE-02'],
119:['OPTIONFRAME-03'],120:['OPTIONCONSUMER-01','OPTIONCONSUMER-02'],121:['OPTIONCONSUMER-04'],124:['OPT06-04'],125:['OPT07-04'],129:['OPT11-04'],
130:['RESIZE-01','RESIZE-02','RESIZE-03','RESIZE-04','RESIZE-05','RESIZE-06','RESIZE-07'],
134:['BOOT-07','BOOT-08'],136:['LOADCOMMAND-05','LOADCOMMAND-06','LOADCOMMAND-07','LOADCOMMAND-08'],
142:['OPTIONFRAME-12','OPTIONFRAME-13','LOADCOMMAND-05','LOADCOMMAND-06'],143:['OPTIONFRAME-12','OPTIONFRAME-13','LOADCOMMAND-05','LOADCOMMAND-06'],144:['LOADCOMMAND-05','LOADCOMMAND-06','LOADCOMMAND-07','LOADCOMMAND-08'],145:['BOOT-08','OPTIONCONSUMER-07'],146:['OPTIONCONSUMER-08','OPTIONCONSUMER-09','READYUI-05'],
152:['MAPINPUT-'+f'{n:02}' for n in range(1,14)],153:['PAUSELOOP-01','PAUSELOOP-02'],154:['PAUSELOOP-'+f'{n:02}' for n in range(3,7)],155:['PAUSE02-02','PAUSE03-02','PAUSE04-02','PAUSE05-02','PAUSE06-02','PAUSE08-02'],
174:['SESSIONS-'+f'{n:02}' for n in range(1,12)],175:['PAUSELOOP-04','OPTIONCONSUMER-08','SESSIONS-07','SESSIONS-09'],
181:['PC-01','PC-02','PC-03','PC-06','PC-07','PC-21'],186:['PC-04','PC-07','PC-08','PC-09','PC-10'],187:['PC-05','PC-06'],188:['PCEXTRA-01','PCEXTRA-04'],189:['PCEXTRA-02','PCEXTRA-03','PCEXTRA-04'],190:['PC-03'],192:['PC-05','PC-08','PC-09','PCEXTRA-04'],196:['PC-06','PC-11','PC-21'],198:['PC-12'],199:['PC-13'],200:['PC-12'],201:['PC-14'],203:['PC-15'],204:['PC-'+f'{n:02}' for n in range(16,21)],
210:['MAPINPUT-02','MAPINPUT-08','MAPINPUT-09','MAPINPUT-12'],212:['READYBUILD-01','READYBUILD-02'],213:['READYBUILD-03'],214:['READYBUILD-04','READYBUILD-05'],218:['READYUI-'+f'{n:02}' for n in range(1,5)],219:['READYUI-05','READYUI-06','READYUI-07','OPTIONCONSUMER-09'],220:['READYUI-05','READYUI-08','READYUI-10','OPTIONCONSUMER-09'],225:['READYUSE-01','READYUSE-02'],226:['READYUSE-03'],227:['READYUSE-'+f'{n:02}' for n in range(4,10)],228:['READYBUILD-05','READYBUILD-06','READYUSE-05','READYUSE-06'],232:['OPTIONCONSUMER-09','READYUI-05'],
236:['BOOT-04','TITLE-01','LOADGATE-09','LOADGATE-14'],237:['BOOT-08','LOADGATE-09','OPT07-03','OPT06-03'],238:['OPT09-01','OPT10-01','OPT12-02','PC-04'],
244:['LOADGATE-02','LOADGATE-03','LOADGATE-04','LOADGATE-05'],245:['LOADGATE-08'],246:['SAVE-08','SAVE-11','SAVE-13'],247:['LOADPANEL-08'],248:['PC-08','PC-09','PC-12','PC-15'],249:['READYBUILD-04','READYUI-07'],250:['PAUSELOOP-07','READYUSE-10'],259:['PC-21','PCEXTRA-01','PCEXTRA-03','HELP-15'],261:['PCEXTRA-05']}
for line,keys in repeat.items():
 for k in keys:
  f=next(f for f in facts if f['id']=='UIF-'+k)
  if {'path':M,'line':line} not in f['spec_locations']:f['spec_locations'].append({'path':M,'line':line})
# Add exact CH/TC repeated clause links by explicit ID lists.
for path,mp in [(C,{9:[1,10,12],15:[4,5],16:[7,8,9],17:[12],23:[1,3],24:[1],25:[1,3],26:[1,3],28:[2],30:[4,5,6],31:[5,6,11],32:[5],36:[1,12],37:[12],38:[10,11],39:[7,8],40:[7],44:[8,9,10,11,13],45:[8,12],46:[2],47:[3],48:[4,10,12,14],53:[15],57:[1,12,3,2,13]}),(T,{9:[1,14,15],15:[1],16:[2,3],17:[11,12],18:[14,15],24:[1,2,3,4,5,6,7],25:[14],26:[14],27:[1,14],31:[2],32:[3],33:[4,5,6],37:[7,8,9,10],38:[11,12],39:[13],43:[14,15],45:[2,3],46:[10],47:[12],48:[10,14],53:[2,3,4,12],57:[2,3,4,5,6,8,9,10,11,12,14,15]})]:
 prefix='HELP' if path==C else 'CARD'
 for line,nums in mp.items():
  for n in nums:
   f=next(f for f in facts if f['id']==f'UIF-{prefix}-{n:02}')
   if {'path':path,'line':line} not in f['spec_locations']:f['spec_locations'].append({'path':path,'line':line})
# Bind NV/CH/TC exact test IDs to the corresponding normal/boundary assertions; no full catalog generalization.
nv={
'T01':['TITLE','LOADGATE'],'T02':['LOADPANEL'],'T03':['LOADGATE'],'T04':['BOOT'],'T05':['BOOT','LOADGATE'],'T06':['LOADCOMMAND'],'T06b':['LOADCOMMAND','OPTIONFRAME'],'T07':['LOADGATE'],'T08':['LOADGATE'],'T09':['LOADGATE'],'T10':['LOADGATE'],
'T11':['SAVE'],'T12':['SAVE'],'T13':['SAVE'],'T14':['SAVE'],'T15':['EMERGENCY'],'T16':['OPT03','OPTIONFRAME'],'T17':['OPTIONFRAME'],'T18':['OPTIONFRAME','OPT09'],'T19':['OPTIONFRAME','OPT01'],'T20':['OPT01','OPT02'],'T21':['OPT06'],'T22':['OPT07'],'T23':['OPTIONCONSUMER'],'T24':['PAUSE01','PAUSE02','PAUSE04','PAUSE05','PAUSE06','PAUSE07','PAUSE08','PAUSE10'],'T25':['SESSIONS'],'T25b':['SESSIONS'],'T26':['PAUSE02'],'T27':['PC'],'T28':['PC'],'T29':['PC'],'T30':['READYBUILD'],'T31':['READYUI'],'T32':['READYBUILD'],'T33':['READYUSE'],'T34':['READYUSE'],'T34b':['READYUSE'],'T35':['LOADPANEL'],'T36':['READYUI','OPTIONCONSUMER']}
cat=(O.parents[3]/'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md')
# O.parents[3] is not repository root; resolve known root.
cat=Path('/workspace/pokemon-essentials-clean-room')/CAT
for i,line in enumerate(cat.read_text().splitlines(),1):
 if not (135<=i<=196):continue
 cells=line.split('|');k=cells[1].strip() if len(cells)>2 else ''
 prefixes=nv.get(k,[]) if 135<=i<=173 else ['HELP'] if k.startswith('CH') else ['CARD'] if k.startswith('TC') else []
 for f in facts:
  if any(f['id'].startswith('UIF-'+g+'-') for g in prefixes):f['test_routing_locations']=f.get('test_routing_locations',[])+[{'path':CAT,'line':i,'test_id':k,'status':'REQUIRES_EXACT_ROW_SUBASSERTION_RECONCILIATION'}]
j['mapping_refined_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();j['facts']=facts;j['clause_binding_quality']='Hand-audited exact locations; per-test broad routing still explicitly pending';(O/'forward.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
# Reverse retains all text units but exact source-fact links replace old broad section matches.
rev=json.loads((O/'reverse.json').read_text())
admin_main={3,5,9,11,13,37,47,74,75,106,117,118,140,141,159,160,182,184,185,197,202,211,224,240,254,258,263};admin_other={3,5,11,21,22,44,52,59,61}
for c in rev['records']:
 exact=[f for f in facts if any(q['path']==c['path'] and q['line']==c['line'] for q in f['spec_locations'])]
 c['linked_source_fact_ids']=[f['id'] for f in exact]
 c['bounded_assertions']=[{'fact_id':f['id'],'assertion':f['assertion'],'premise':f['premise'],'relation':f['relation']} for f in exact]
 if c['path']==M and c['line']==88:c['disposition']='DISPUTED_SCOPE_GR8_UI_001_NONAUTHOR_REFUTATION_PENDING_ROOT'
 elif exact:c['disposition']='FULL_READ_EXPLICIT_BOUNDED_ASSERTIONS_LINKED; NOT_ALL_CHILD_CLAIMS_ACCEPTED'
 elif c['path']==CAT:c['disposition']='FULL_TEXT_READ; OTHER_UI_OR_TEST_ATOMIC_RECEPTION_PENDING'
 elif c['path']==M and c['line'] in admin_main:c['disposition']='READ_SCOPE_OR_TABLE_STRUCTURE_OR_HISTORY_NAVIGATION; CURRENT_QUALIFICATION_RECEPTION_PENDING_IF_CLAIMED'
 elif c['line'] in admin_other:c['disposition']='READ_SCOPE_OR_TABLE_STRUCTURE_OR_DEPENDENCY; SOURCE_DOMAIN_RECEPTION_PENDING_IF_BEHAVIOUR_CLAIMED'
 else:c['disposition']='FULL_READ; NO_EXPLICIT_ASSERTION_LINK_YET'
 c['remaining']='Exact linked assertions are bounded reviewed facts; any child assertion absent from this explicit list remains unaccepted. Source facets do not silently turn into current formal requirements.'
rev['records']=rev['records'];rev['explicit_source_assertion_count']=len(facts);rev['section_only_links_removed']=True
(O/'reverse.json').write_text(json.dumps(rev,ensure_ascii=False,indent=2)+'\n')
print('refined',len(facts),'facts; exact formal factlink lines',sum(bool(x['linked_source_fact_ids']) for x in rev['records']))
