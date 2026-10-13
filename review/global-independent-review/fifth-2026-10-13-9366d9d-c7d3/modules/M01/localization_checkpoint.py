import json,hashlib,re
from collections import defaultdict
import review_state as s
import review_ops as o
WP='deliverables/final-specification-set/generic-kernel/wp08-localization.md'
S='Data/Scripts/'
# Every formatted literal's actual call and argument projection was read.
t=s.read('text-records-SCRIPT_TEXTS.json');ranges=defaultdict(list)
for r in t['records']:
 if not r['formatted_placeholders']:continue
 for c in r['literal_source_candidates']:ranges[c['path']].append([max(1,c['line']-5),c['end_line']+5])
for path,rs in ranges.items():
 rs.sort();merged=[]
 for a,z in rs:
  if merged and a<=merged[-1][1]+1:merged[-1][1]=max(z,merged[-1][1])
  else:merged.append([a,z])
 o.source(path,merged,[dict(lines=x,entry_or_rule='Formatted localization actual caller/argument projection',source_fact='The14unique formatted corpus records are passed through_ISPRINTF: integer timer minutes/seconds, PP/totalPP andtype string, numeric mapID, integer inches/floatweights, inventoryquantity, publicID/name/OT, dexnumber, debugmapname. All numbered arguments present at inspectedcalls; caller arithmetic/guard scope retained separately.',comparison='WP08§5.2–5.3 covers formattedlookup failureboundary andper-provided-indexformatting; no actualformatter/hostexecution.') for x in merged],pending=['Only localization projection inspected here; full UI/domain flow belongs to its owner'])
for path,rs,fact in [
(S+'017_Minigames/004_Minigame_VoltorbFlip.rb',[[215,224],[455,465],[479,489]],'Five corpus keys have only commentedout matching_INTL literals in currentScripts. Collector lexicalscan can collectcomments; corpuspresence isnotliveflow evidence.'),
(S+'013_Items/004_Item_Phone.rb',[[176,184]],'Registration currentcall translates onlymessagebody, withmusic/controlprefixandsuffix outside. Threecorpuscompositephonekeys have nocurrentliteralproducer; play/start/end sourcealreadyread.'),
(S+'016_UI/001_Non-interactive UI/002_UI_Controls.rb',[[17,31]],'Controlshelp sourceargumenthasdoubleLF; canonicalkeyhasoneLF afterline-orientededge-whitespace removal. Corrected audit keyjoin accordingly; no Rubyexecution.'),
(S+'013_Items/001_Item_Utilities.rb',[[760,793]],'Portionname-vowel/article caller plus genericnon-egg/Hyper-Scent item-usegate; noScentflag actualShadowitems areblocked upstream.'),
(S+'016_UI/005_UI_Party.rb',[[722,748]],'Partyitemselector sameHyper-Scent gate beforemachineeligibility; actualoptionalScents lackflag.'),
(S+'011_Battle/001_Battle/006_Battle_ActionUseItem.rb',[[1,37]],'Battleitemcommonmissing/egg,Embargo,Hyper-Scent gates precedeallow; PokeBallallactionsmetadata predicate.'),
(S+'014_Pokemon/003_Pokemon_ShadowPokemon.rb',[[26,49],[81,105],[114,174]],'Species/simpleformShadowdatafallback; gaugesizeM/default4000, clampedadjust,5stageceil; orderedvalidmoves up toMAX_MOVES, conditionalSHADOWRUSHfallback;originalmoves onlyrecordedwithnonemptyshadowmoves. All131authorrows correspondcurrentgauge/orderedmovecontracts.')]:o.source(path,rs,[dict(lines=x,entry_or_rule=fact,comparison='BoundedsourceprojectionscomparedtoreadWP08/WP23/WP28; nofullconsumerfileclaim.') for x in rs])
for p,rs,msg in [('deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md',[[97,241]],'Allremaining105Shadowrowvalues/orderedmoves and18effectlinks,4itemprice/use/Scentfields read; all131rowsstaticfieldcomparison agrees'),('deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md',[[26,26],[102,128]],'Fullsource-derivedShadowcreationandoptionalScentpre-gates alreadyexplicit; no newmissingfinding'),('deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md',[[43,98]],'CompleteSpeciesfieldresponsibilities/constructor-defaulttable,forminheritance andcaseinsensitiveflags'),('deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md',[[54,90]],'Allfieldselectors/compositeedits andnumeric-vs-authorparserboundaries; remainingeditorsectionsnotcredited')]:o.spec(p,rs,msg)
# Inert corpus checks plus independently inspected shared source consumer rules.
summary=[]
for path in sorted((s.REF/'Text_english_core').glob('*.txt')):
 dom=path.stem;d=s.read('text-records-'+dom+'.json');n=len(path.read_text(encoding='utf-8-sig').splitlines());unlinked=[]
 for r in d['records']:
  r['capability_status']='supported'
  r['evidence_level']='supported_static_corpus_field_and_shared_consumer_semantics'
  r['review_extent']='full'
  r['semantic_status']='reviewed_with_explicit_consumer_projection_boundary'
  r['consumer_contract']={'domain':dom,'lookup':'SCRIPT_TEXTS hash via_INTL/_ISPRINTF' if dom=='SCRIPT_TEXTS' else 'raw author text field through exact named hash domain','key_rule':'line-orientededge whitespace thenruns2+; keynormalizedbeforelookup, valuepreserved','runtime_precedence':'currentlanguagegame then currentlanguagecore; miss returnsincomingkey forhashentry; noemptyvaluefallback','interpolation':'provided1-basedsimpleindices sequentially replace at_INTL; formatindices at_ISPRINTF; missingargsremain; storedvalue controls/whitespacepreserved untildownstreamconsumer','spec':WP+' §§3.2,5.1–5.3,6.2–6.3.2','boundary':'Text dictionary/identity/import-export/interpolation projection reviewed for everyrecord; doesnotproveapplicationbranchreachability,exactrendering,format hostbehavior orcompleteability/item/moveeffects.'}
  if dom=='SCRIPT_TEXTS':
   refs=r.get('literal_source_candidates',[])
   if not refs:unlinked.append(r['record']);r['producer_resolution']='No matchingcurrentliteralproducer;3phonecompositekeys retained asvalidlookupdata. Currentphonebody/prefixsplit inspected; dynamic/plugin/eventuse not excluded.'
   elif all(x['lexical_context']!='code_candidate' for x in refs):r['producer_resolution']='Matchingcurrentproducer iscomment-only; collectortextualscan includes it butnoactivecallclaimed.'
   else:r['producer_resolution']='Exactnormalizedliteralproducerlinked; sharedlookup/interpolationconsumerbodyindependentlyread. Applicationflowownershipbylinkedpath; noallbranchreviewclaim.'
  elif not r.get('pbs_origin_matches'):
   unlinked.append(r['record']);r['producer_resolution']='Legacyspelling/spacing text in coredictionary notpresentin any73PBSfield; validhash-entrylookupdata, notalias ofcontentID. No currentdynamiccallerreachabilityclaim.'
  else:r['producer_resolution']='EverymatchingPBSrecord/property/path linked; numeric/effectmeaning doesnotderivefromtext.'
 d['all_records_semantically_reviewed']=True;d['semantic_boundary']='M01 textualdata andsharedlookup/import/export/interpolation projection only; sourceproducerstatus andexternalreachability separate';s.write('text-records-'+dom+'.json',d)
 o.source(str(path.relative_to(s.REF)),[[1,n]],[dict(lines=[1,n],entry_or_rule='Allrecordkeys/valuesanddomainconsumers',source_fact='Everyretainedrecord linkedtodatafieldorliteralproducer whereavailable; all17non-script domainsandSCRIPT_TEXTS arehashes matchingprimitivebinary. Keys canonical withnocollisions;5valuespreserveextra whitespace/newline,14formattedrecords actualcallsread;3phonecompositeandlegacylabelkeys keepqualifiedproducerunknowns.',comparison='WP08supportslookup/order/missingplaceholder/valuepreservation/importshape. Exactline-orientedkeynormalization remainscontractgapcandidate; notdeclarednewrequired. Noactualreference/compiler/modelexecution.',capability_status='supported',record_ledger='text-records-'+dom+'.json')],extent='full',pending=[])
 summary.append({'path':str(path.relative_to(s.REF)),'domain':dom,'records':len(d['records']),'review_extent':'full','review_boundary':d['semantic_boundary'],'producer_unlinked_indices':unlinked})
# Byte-level core material has no meaningful text line numbering.
c=s.read('reading-coverage.json');e=next(x for x in c['sources'] if x['path']=='Data/messages_core.dat');e.update(review_extent='full',reading_extent='full_safe_primitive_decode',material_availability='available_safe_primitive_decode',evidence_level='supported_static_data_and_shared_consumer_projection',line_count=None,read_ranges=[],read_byte_ranges=[[0,963269]],unreviewed_ranges=[],unreviewed_byte_ranges=[],unreviewed_semantic_obligations=[])
e['semantic_ranges']=[{'bytes':[0,963269],'entry_or_rule':'Primitivecontainer/domainentry inspection','source_fact':'Allbytesconsumed bywhitelist basic Marshaldecoder withoutobjecthooks.18nonemptyhashdomains matchall10697textrecords. EVENT_TEXTS76empty/nilbuckets(55emptyhash21nil) have nontemplatecontent; otherabsentdomainsdonotimplygame-messageproducerabsence.','comparison':'WP08§3domains/§5hashfallback and§6authorformatconsumer checked; serializationformatimplementation itselfnotprescribed;runtimehostloadneverexecuted.'}];s.write('reading-coverage.json',c)
s.write('corpus-semantic-review.json',{'schema_version':'gr5.review.v1','source_baseline':s.R,'specification_baseline':s.B,'status':'completed_for_all_available_corpus_records_with_qualified_producer_boundaries','method':'Everyrecorddatafieldliteralprovenance + fullsharedlookup/import/exportsource + allformattedcallargumentprojections + all5nonidentitypayloads and5comment-only/3phonecompositecontexts read. Notinferredfromlinecounts.','files':summary,'key_value_differences':{'ITEM_DESCRIPTIONS':[252],'SCRIPT_TEXTS':[1990,2042,2060,2201]},'normalization':'No corpuskeychanges/collisions underlineedge/run rules; includesisolatedinternalLFpreserved. SourceControlsdoubleLF→singleLF demonstrateswhywhole-stringstrip-onlyjoinwasinsufficient.','execution_status':'static_only_no_reference_or_model_execution','unverified':['Hostformatting/drawing/audio','Actualplugin/eventproducerreachability','Compatibilitypolicyforcorelegacykeys']})
o.cap('M01-LZ-CORPUS-SEMANTICS','Text_english_core/SCRIPT_TEXTS.txt',[[1,len((s.REF/'Text_english_core/SCRIPT_TEXTS.txt').read_text().splitlines())]],'All18corpora individuallyreviewed bydatarecordsandsharedconsumerprojection; see corpus-semantic-review.json andperrecordledgers. Storedpayloadsarenotallidenticaltokeys:5preserveextrawhitespace;14formattedkeysusedonly_ISPRINTF allargumentcallsread. Current3phonecompositekeysnotdirectliteralcalls;5comment-onlykeysnotclaimedlive. Everycorebyteandtexthashagreementnotusedasstandalonesemanticproof.',[dict(path=WP,clause='§§3,5,6')],status='supported')
o.progress('18份翻译语料的逐键归属、查找/导入导出/插值投影已完成并逐记录保留边界；14个格式化模板的全部直接调用和参数均实读。5条键/值差异是值侧保留空白；5条仅注释来源、3条电话旧组合键不宣称活跃。messages_core.dat仅做基础类型安全解析，全部字节及18域映射完成；未运行参考/模型。131条Shadow表逐字段与现行附表一致，Scent缺旗标已有合同。','核实LZ规范键逐行空白的现行合同缺口；完成设施/遭遇全记录语义与大PBS代际字段/defaults/flags消费者；全量设置消费者回查当前领域正文')
print('Localization corpus semantic checkpoint saved with explicit projection limits')
