from pathlib import Path
import json,re,datetime
o=Path(__file__).resolve().parent;d=json.loads((o/'reverse-mapping.json').read_text());ids=json.loads((o/'identities.json').read_text());f=next(x for x in ids['files'] if x['kind']=='formal' and x['index']==8);lines=(Path(f['repo'])/f['path']).read_text().splitlines()
# Each support assignment is authored after actual full reading, not inferred by
# a text search. The parser below preserves exact clause cells/locations only.
m={
'AI':{
'A01':[3,4],'A02':[3,14],'A03':[1],'A04':[4],
'S01':[4,25],'S02':[4],'S03':[4],'S04':[4],'S05':[6],'S06':[7,19],'S07':[24],'S08':[5,24],'S09':[24],
'S10':[1,6],'S11':[1,6],'S12':[6],'S13':[6],'S14':[6],'S15':[6],'S16':[5,6],
'I01':[9,10],'I02':[9,10],'I03':[10],'I04':[10,26],'I05':[10],'I06':[1,10],'I07':[1,10],'I08':[9,10],
'M01':[14],'M02':[14],'M03':[12,14],'M04':[12,14],'M05':[12,14],'M06':[14],'M07':[11,14],'M08':[12],'M09':[12,14]},
'AE':{
'A01':[13],'A02':[13],'A03':[13],'A04':[13],'A05':[18],'A06':[18],'A07':[18],'A08':[18],'A09':[18],'A10':[18,24],
'N01':[25],'N02':[29,31],'N02b':[31,48],'N02c':[31,48],'N02d':[29,31],'N03':[29],'N04':[29],'N05':[29],'N06':[30],'N07':[30],'N08':[31],'N09':[29],'N10':[29],'N11':[29],
'G01':[15,35],'G02':[15,16],'G03':[15,16,24],'G04':[15,16],'G05':[15],'G06':[15,16],'G07':[15],'G08':[38],'G09':[39],'G10':[38],'G11':[35],'G12':[37],'G13':[15,16,24],
'S01':[41],'S02':[41],'S03':[41],'S04':[41],'S05':[41],'S06':[41],'S07':[42],'S08':[42],'S09':[42],'S10':[42],'S11':[42],
'T01':[43],'T02':[43],'T03':[44],'T04':[44],'T05':[44],'T06':[21,26],'T07':[19,21],'F01':[32],'F02':[32]},
'BE':{
'B01':[46],'B02':[46],'B02b':[46],'B03':[47],'B04':[47],'B04b':[47],'B04c':[47],'B05':[47],'B06':[47],'B07':[47],'B08':[47],'B09':[47],
'B10':[60],'B11':[60],'B12':[48],'B12b':[31,48],'B13':[52],'B14':[52],'B15':[52],'B16':[52],'B17':[53],'B18':[53],'B19':[53],'B20':[53],'B21':[54],
'B22':[55],'B23':[55],'B24':[55],'B25':[55],'B26':[55],'B27':[55],'B28':[40],'B29':[60],'B30':[57],'B31':[34],'B32':[57],'B33':[57],
'B34':[33],'B35':[17],'B36':[17,33],'B37':[17],'B38':[17],'B39':[33],'B40':[37],'B41':[40],'B42':[40],'B43':[49],'B44':[41,49],'B45':[49],'B46':[49],'B47':[2,49],'B48':[50],'B49':[32],'B50':[51],
'B51':[56],'B52':[56],'B53':[56],'B54':[56],'B55':[59],'B56':[59],'B57':[60],'B58':[48],'B59':[48],'B60':[50],'B61':[47],'B62':[12,13,35,53],'B63':[40],
'B64':[13,55],'B65':[55],'B66':[55],'B67':[12,55],'B68':[13,55],'B69':[13,55],'B70':[55],'B71':[12,55],
'B72':[12,13,29,52],'B73':[13,52],'B74':[29,52],'B75':[29,52],'B76':[13,52],'B77':[13,29,51],'B78':[13,51],'B79':[29,51],'B80':[29,51],'B81':[13,51],'B82':[28,51]},
'CE':{
'C01':[22,26],'C02':[22],'C03':[22],'C04':[22,26],'C05':[23],'C06':[23,25],'C07':[22],'C08':[27],'C09':[27],'C10':[27],'C11':[27],'C12':[27],
'C13':[58],'C14':[58],'C15':[58],'C16':[58],'C17':[58],'C18':[58],'C19':[27,58],'C20':[41,58],'C21':[61],'C22':[2,61],'C23':[61],'C24':[61],'C25':[59],'C26':[59],'C27':[59],'C28':[59],
'C29':[62],'C30':[2,62],'C31':[62],'C32':[62],'C33':[63],'C34':[63],'C35':[32],'C36':[64],'C37':[64],'C38':[64],'C39':[64],'C40':[64],'C41':[65],'C42':[65],'C43':[65],'C44':[65],'C45':[65],'C46':[12,65],'C47':[45],'C48':[45],'C49':[34],'C50':[19,34],'C51':[45],'C52':[25,64],'C53':[58],'C54':[58],'C55':[2,23],'C56':[2,59],'C57':[12,65],'C58':[23],'C59':[2,47,49,61,62]}}
notes={
('AI','I06'):'AI local ordered scan/phase exception accepted; exact item qualification/registration resource prefix requires IF-COMAI-CORE-ITEM-REGISTER, not closed from local code.',
('AI','I07'):'POTION-only and MAXETHER/activeLEPPA alternatives preserve separate qualification/register consumer; open real receiver.',
('AI','I08'):'AI estimate1/misspelling accepted; exact actual active25/26 and heldtrigger are outside local table and need item/PBS receiver.',
('AE','N02b'):'Old table stage5 cap4 denominator2, not1: local115; configuration is initialized before query.',
('AE','N02c'):'New table cap3 denominator1: local60. Same algorithm, distinct table.',
('AE','N02d'):'Both negative indices satisfy denominator≤2 in rough damage; no real forbiddencrit inference.',
('AE','T02'):'Ordinary User0 bypass is accepted. Missing finite existing callable once+14 definition proposed GR8-AI-001; do not mark unknown-extension text as complete direct-query coverage.',
('BE','B02b'):'AI targetICE refusal independent ofOHKO ordinary copy; actual loaded alias losesICE check withfalseclause. No unified trueeffect claim.',
('BE','B62'):'DefaultGeomancyUser0 never entersGchargescore/statbenefit; only wholeF cappedall20. HP/herb/stage unchanged; condition excludes other general modifiers.',
('BE','B63'):'AI unclipped100.5/51 distinct from real capped60/100; real HealBlock/substitute receiver remains finite Move fact transfer, not scoring mutation.',
('BE','B72'):'n0: predictionoff, specificG firstroughdamage normalmin1, then substitute division0; wrapper initial100 retained onlyafterdiagnosticsnormal, not normal computed100.',
('BE','B73'):'Predictionon blocks emptylist with20, GbodyNOT_ENTERED.',
('BE','B74'):'n1 sum15, divisionnormal andstrictthreshold0 so no break10; no finaldamage/score inference.',
('BE','B75'):'NoSubst skipslocaldivision only; genericdamage consumers continue.',
('BE','B76'):'ScoreMovesoff preventsGbody, no caughtdivision.',
('BE','B77'):'Nilcurrentitem identityaccess raises beforedefault1; typeprepnormal; wrapper retained100 notnormalP100.',
('BE','B78'):'Predictionon noBerry20 androughbaseNOT_ENTERED.',
('BE','B79'):'RealcurrentORANcompleteflag80, no scoringconsumption orafterhit simulation.',
('BE','B80'):'Presentitem malformedprefix→realbase1→AI0; roughdamage min1 still separate.',
('BE','B81'):'ScoreMovesoff avoidsgenericroughdamage consumer, no localbaseexception.',
('BE','B82'):'Skill31 P1 first60 andnomediumcallback, flagindependence; doesnotcertifyskill32safe.',
('CE','C39'):'AI firstmatchingPP slot vs real lastmatching slot; lastmoveconsumption distinct, no common normalizer.',
('CE','C46'):'DefaultUser0nogscore, directquerybreakfirstfoe+8not16.',
('CE','C55'):'Future directkey is conditional precedence statement only, no pluginloaded.',
('CE','C56'):'PowerUpAllyS missingretains100, G+5; no extraS5.',
('CE','C57'):'DefaultImprisonUser0candidate100understatedcommonexclusions, directG108not116.',
('CE','C58'):'Gemgen≤5add2thenmatchingdamagetype; no type→0bothgens, notbase-ratingcomparison.',
('CE','C59'):'Conceptualrepresentationequivalenceonly, family/key/effectivebinding/defaultsretained; no codearchitecture requirement.'}
vectors=[];context='AB'
for n,l in enumerate(lines,1):
 if l.startswith('## '):context=next((s for s in ('AB','AI','AE','BE','CE') if l.startswith('## '+s+'：')),context)
 if l.startswith('### R7-U06'):context='R7-U06'
 if not l.startswith('| '):continue
 cells=[c.strip() for c in l.strip().strip('|').split('|')]
 if len(cells)!=3 or cells[0]=='ID' or re.fullmatch(r'[-: ]+',cells[0]):continue
 key=cells[0];supports=m.get(context,{}).get(key)
 if supports is None and context not in ('AB','R7-U06'):raise ValueError((context,key,n))
 status='SUPPORTED_AI_LOCAL_STATIC'
 interfaces=[]
 if context=='AB':status='FORMAL_READ_SOURCE_RECEPTION_OPEN';interfaces=['IF-COMAI-ABILITY-ITEM-CALLBACKS','IF-COMAI-BATTLER-QUERIES']
 elif context=='R7-U06':status='DIRECT_TAIL_GUARDS_RECEIVED_CENTRAL_AND_FULL_VECTOR_OPEN';interfaces=['IF-COMAI-BATTLER-QUERIES','IF-COMAI-ABILITY-ITEM-CALLBACKS']
 if context=='AI' and key in ('I06','I07','I08'):status='AI_LOCAL_SUPPORTED_REAL_ITEM_RECEIVER_OPEN';interfaces=['IF-COMAI-CORE-ITEM-REGISTER','IF-COMAI-ABILITY-ITEM-CALLBACKS']
 if context=='AE' and key=='T02':status='ORDINARY_BYPASS_SUPPORTED_CALLABLE_DEFINITION_GAP_GR8-AI-001'
 vectors.append({'id':context+'-'+key,'formal_index':8,'line':n,'reviewer':'/root/com_ai','actual_full_table_and_context_read':True,'source_fact_units':[f'AIU{x:03d}' for x in (supports or [])], 'premise_cell':cells[1],'asserted_result_cell':cells[2],'assessment':status,'manual_semantic_judgment':notes.get((context,key),'Compared complete stated finite input, each contrasted boundary and stage-qualified result against the named manually read source facts. Retain all exclusions and no final action/HP/host guarantee.' if supports else 'Full formal vector read, but no full source/callback reception credited from this prose; individual real source receiver is explicitly open.'),'interfaces_required':interfaces,'evidence_level':'SOURCE_STATIC; DERIVED_VECTOR' if supports else 'FORMAL_TEXT_READ_ONLY_FOR_FULL_VECTOR','execution':'NOT_EXECUTED'})
expected={'AI':37,'AE':57,'BE':86,'CE':59,'AB':31,'R7-U06':15};actual={s:sum(x['id'].startswith(s+'-') for x in vectors) for s in expected}
assert expected==actual,(expected,actual)
fixture_ranges=[{'range':[1,9],'role':'title, provenance, static evidence and shared31AB fixture'}, {'range':[43,49],'role':'R7-U06 complete commonS fixture'}, {'range':[65,69],'role':'historical-qualifiedcrossreference andAI series'}, {'range':[102,108],'role':'S10–16 common legal1v2 sparse-array fixture'}, {'range':[116,120],'role':'AE stage-local score and no-execution scope'}, {'range':[180,184],'role':'BE localbase/score and manual-source scope'}, {'range':[254,257],'role':'LifeDew guard fixture'}, {'range':[266,271],'role':'BeatUp/NaturalGift finite predictionoff fixtures'}, {'range':[285,290],'role':'CE value/local stage scope'}]
d['vectors']=vectors;d['vector_denominators']=actual;d['test_fixtures_read']=fixture_ranges;d['formal_files_with_main_groups']=9;d['status']='PRIMARY_AI_LOCAL_MANUAL_MAPPING_COMPLETE_WITH_NAMED_CROSS_DOMAIN_RECEPTION_OPEN';d['shared_catalog_source_open_vectors']=46;d['all_primary_formal_text_read']=True;d['updated_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(o/'reverse-mapping.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'vectors':len(vectors),'denominators':actual,'main_manual_assertions':d['manual_subassertions']}))
