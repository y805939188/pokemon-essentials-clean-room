import json,hashlib,datetime,subprocess
from pathlib import Path
T=Path('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/ui_full');R=Path('/workspace/pokemon-essentials');C=Path('/workspace/pokemon-essentials-clean-room');now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(name,data):(T/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def bind(path):
 p=Path(path);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
deps=json.loads((T/'dependency-identities.json').read_text());dep_full=sum(x['whole_file_read'] for x in deps['records'])
# source identity normalization does not grant new reading.
for x in deps['records']:
 ranges=[]
 for lo,hi in sorted(x['ranges']):
  if ranges and lo<=ranges[-1][1]+1:ranges[-1][1]=max(hi,ranges[-1][1])
  else:ranges.append([lo,hi])
 x['ranges']=ranges
 x['unread_ranges']=[];cur=1
 for lo,hi in ranges:
  if cur<lo:x['unread_ranges'].append([cur,lo-1])
  cur=max(cur,hi+1)
 if cur<=x['lines']:x['unread_ranges'].append([cur,x['lines']])
 x['unread_is_available_text']=bool(x['unread_ranges'])
 x['qualified_scope']='Exactcomplete namedunit semanticcredit only; outside listedreadranges availableUNREAD, not host/materiallimit.' if not x['whole_file_read'] else 'Ownfulltextactorcredit; no business execution.'
deps['utc']=now;deps['count_summary']=dict(record_paths=len(deps['records']),full_read_files=dep_full,partial_read_files=len(deps['records'])-dep_full,primary_overlap_paths=['Data/Scripts/016_UI/005_UI_Party.rb','Data/Scripts/016_UI/006_UI_Summary.rb','Data/Scripts/016_UI/017_UI_PokemonStorage.rb'],additional_nonprimary_files=len(deps['records'])-3,additional_nonprimary_full_read=dep_full-3,available_unread_partial_paths=sum(bool(x['unread_ranges']) for x in deps['records']),available_unread_line_extents=sum(sum(hi-lo+1 for lo,hi in x['unread_ranges']) for x in deps['records']),extent_count_is_not_semantic_denominator=True);dump('dependency-identities.json',deps)
# canonical v3 current state; immutable v2 remains unchanged and separatelybound.
led=json.loads((T/'reading-ledger.v2.json').read_text());led['schema']='gr8-ui-full-reading-ledger/v3';led['utc']=led['as_of_utc']=now
for rec in led['records']:
 rec['as_of_utc']=now
 if 'VoltorbFlip' in rec['identity_path']:
  rec.update(reader='/root/ui_full',actual_reader='/root/ui_full',status='OWN_PARTIAL_READ_AND_PEER_COMPLETE_MEANING_RECEIVED',ranges=[[257,317]],unread_ranges=[[1,256],[318,705]],credit='OWN_COMPLETE_PBCREATESPRITES_PARTIAL_PLUS_PEER_FULL_FACT_RECEPTION',own_full_read=False)
  rec['own_partial_unit']='completepbCreateSprites257–317; fullprovidercredit /root/ui_minigames remains unchanged'
 rec['atomic_mapping']='Complete recorded currentformal/catalog handmeaning mappings own or actualpeerreception; perinterface remaining scope/history preserved, not alltransitive semanticclosure.'
led.update(own_reference_not_full=7,own_reference_wholly_unread=6,own_reference_partial=1,own_reference_unread=7,own_formal_unread=6,source_structure_denominator='MANUAL_EXPLICIT_FACT_CENSUS_PRIMARY_146_UNITS_1933_FACTS_PLUS_FINITE_PACKETS; NOT_METHOD_LINE_OR_SEMICOLON_COUNT; FINAL_ALLTRANSITIVE_HISTORY_DENOMINATOR_NOT_CLOSED',formal_atomic_denominator='RECORDED_CURRENT_FORMAL3788=OWN2762+WP66RECEIVED342+MINIGAMESRECEIVED684; EXCLUDING_CATALOG2082; NO_HISTORY_OR_WHOLEFOREIGN_DOMAIN_APPROVAL',dependency_full_files=dep_full,dependency_partial_files=len(deps['records'])-dep_full,current_dependencies=bind(T/'dependency-identities.json'),current_v3_change='No newprimaryFULL:44R12F unchanged. NewownVoltorbcomplete61line method partial; finiteproducerdependencies andcurrentmappingmetadataupdated. Oldv2/rootsnapshot preserve exactpriorstate.',previous_v2_binding=bind(T/'reading-ledger.v2.json'),full_read_is_not_atomic_closure=True,all_current_clauses_closed=False)
dump('reading-ledger.json',led);dump('reading-ledger.v3.json',led)
# whole/partial extraformal credit only; primary18 neverexpanded.
extra=[]
for filename,extent,full in [('engine-resources/wp15-assets-windowskins-fonts-audio.md',None,True)]:pass
# identify exact existing WP15 file from already read primary supplemental identity, not by guessed filename.
wp15=list((C/'deliverables/final-specification-set').rglob('wp15*.md'))
for p in wp15:
 raw=p.read_bytes();extra.append(dict(path=str(p.relative_to(C)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),ranges=[[1,len(raw.splitlines())]],reader='/root/ui_full',status='FULL_READ_PREVIOUSLY_ATTESTED',whole_file_read=True))
for packet in ['bottle-fusion-interface.json','facility-lifecycle-interface.json']:
 for s in json.loads((T/packet).read_text())['sources']:
  if s['repo']==str(C):extra.append(s)
dump('additional-formal-reading.json',dict(schema='gr8-ui-extraformal-reading/v1',utc=now,primary_denominator_unchanged=18,records=extra,extraformal_full=sum(x['whole_file_read'] for x in extra),extraformal_partial=sum(not x['whole_file_read'] for x in extra),note='B8fixed sourcebytes. Partial outside listedranges availableUNREAD, not arbitrarywholeformalapproval; no originalI/O logs reconstructed.'))
# Four finite previouslyopen interfaces now actuallyclosed for exact currentprimaryassertions only.
ints=json.loads((T/'interfaces.json').read_text());ints['schema']='gr8-ui-full-interfaces/v3';ints['utc']=now
patch={
'UIFULL-I01':('OWN_MESSAGES_COMPLETE_AND_WI11_FULL_OBJECTS59_FACTS_RECEIVED','Messages859 ownFULL; interpreter-bounded-reception.json actual11wholeunits59facts/3interfaces/5identities+ledger received; maps menu/message/button/query waiting/index semantics to ownWP17/WP65.','WholeInterpreter/Event contracts/history outside finite scopes not adopted.'),
'UIFULL-I12':('CURRENT_FINITE_CRE_B_AND_BOTTLE_FUSION_COMPOSITION_CLOSED','CRE-B42/20 finiteinterfaces received withtwoMAILcorrections; bottle-fusion-interface55facts+11source/formal scopes ownread covers exactWP28§5.6.1/2 defaultrecords/callback/ordinary/cancel/failure controls.','Allotherfusioncombinations,fullspecies/PBScompiledpopulation/aliasreload remain outside finiteproof.'),
'UIFULL-I15':('CURRENT_WP66_A14_FINITE_PRODUCER_CONSUMER_JOIN_CLOSED','entry36 frozenfacts plusfacility-lifecycle63actualfacts cover nil/[]/start/saveprefix,normalindexedrestore,ordinaryArena continuance,ownerquerypostmove. Recorded287/ChallengeBattles144 newownFULL; exactnecessaryothermethods/3formalparts ownread.','FullWP54/55/56/58allclauses/PBS/history not received here; no runtime.'),
'UIFULL-I16':('CURRENT_WP66_FINITE_RECEIVER_AND_PREVIOUS3_LOCAL_GAPS_CLOSED','113units446facts/342formalassertions/232vectors508 received. A10 twofiniteforms composition55facts; A14currenttail36+63; Area actualMapMetadata138/PBS398full69records/necessarycompiler24facts; WP63cumulative334 own complete.','ProvideroriginalOPEN preservedinfrozenpayload; parentcurrentclosure separate. Allhistorysharedapproval and nonfinite compiled/wholeforeign domains remain OPEN; compiledMapMetadata actualfileABSENT, notfakeavailableUNREAD.')}
for u in ints['records']:
 if u['id'] in patch:u['status'],u['received_scope'],u['remaining']=patch[u['id']]
ints['denominator']='17 namedfinitechains; currentprimarytext/catalogsemantics all ownorcompleteactualpeerreceived; broader externalhistory/transitive atomicdenominator NOT_FINAL. Chaincount notsemanticatomdenominator.'
ints['current_finite_closure_artifacts']=[bind(T/n) for n in ['interpreter-bounded-reception.json','bottle-fusion-interface.json','area-producer-interface.json','facility-entry-interface.json','facility-lifecycle-interface.json']];dump('interfaces.json',ints)
p=json.loads((T/'progress.json').read_text());p['state']='COMPLETED_FINITE_PRIMARY_REVIEW_WITH_EXPLICIT_EXTERNAL_HISTORY_AND_IO_OPEN';p['updated_utc']=now;p['own_extra_dependencies']=deps['count_summary'];p['hand_authored_source']['additional_finite_interface_facts']={'entry':36,'bottle_fusion':55,'area_producer':24,'facility_lifecycle':63,'sum':178,'warning':'Namedsemanticfactcount; overlappingprimary/peerfactsareboundnotdoublecountedinto1933maincensus.'};p['current']='本人44R/12F全文、另小游戏7R/6F完整贡献意义已收，Voltorb ownpbCreateSprites61linePARTIAL不升whole。WP66113units446facts/342formal/232vectors均实际收到；其A10/A14/Area有限本域接口已用新实源闭合。主catalog746全部逐意义接合2082selectedatoms；外域/13历史/原I/O资格仍具名OPEN。';p['remaining_open']=['13minigame历史批准子断言及全部相关历史资格/closure roots仍root新实际context分组接收，未冒本人完整历史阅读','整域PBS全species/forms/moves/compiledpopulation和未知外部reward/NPC/plugincallers，超出各冻结有限接口不授批准','完整WP72钱包域仅minigames实际必要842–880片段已接，非全WP72；其它具名outsideformal wholecontracts不自动由有限接口批准','最终native控制器注册/CC04查询桥及实际媒体/字体/消息全部物质/宿主执行仍依对应owner；本context未读的可得文本保未读','真实资源/host/native/UI/game/save-roundtrip所有业务执行0 NOT_EXECUTED；这是未执行，不伪造成功','原始source/formal平台stdout未本地捕获；operation/UTC/早期chunk和EOF/截断独立资格UNVERIFIED，见io-provenance','28具名partialdependency文件确切可得未读区间见dependency-identities；不把它们当材料limit，不以已读有限单元批准整文件或域'];p['execution']='NOT_EXECUTED';p['update']='UPDATE_NOT_STARTED';p['global_approval']=False;dump('progress.json',p)
# Current primary identity fields are identities only; retain frozen set and bind current ledger/extras.
ids=json.loads((T/'identities.json').read_text());ids['current_delivery_utc']=now;ids['current_reading_ledger_binding']=bind(T/'reading-ledger.json');ids['current_dependency_identity_binding']=bind(T/'dependency-identities.json');ids['extra_formal_reading_binding']=bind(T/'additional-formal-reading.json');ids['identity_is_not_semantic_proof']=True;dump('identities.json',ids)
print(json.dumps(dict(primary_full='44R12F',primary_peer='7R6F',deps=deps['count_summary'],extraformal_count=len(extra),status=p['state']),ensure_ascii=False))
