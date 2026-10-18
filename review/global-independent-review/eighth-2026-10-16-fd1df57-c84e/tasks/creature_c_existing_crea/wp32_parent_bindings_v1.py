import json,hashlib,datetime,re
from pathlib import Path
C=Path(__file__).parent;B=Path('/workspace/pokemon-essentials-clean-room');BASE=C.parents[1];utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception'
names={'X':'wp32-context-meaning.v1.json','B':'battle-consumer-delta.v1.json','V':'evolution-catalog79-meaning.v1.json','R':'wp31-registry-meaning-atoms.v1.json','C':'wp31-wrappers-commit-meaning.v1.json','G':'wp30-compound-meaning.v1.json','F':'wp21-handler-meaning-atoms.v1.json','S':'wp23-shadow-lifecycle-meaning-atoms.v1.json','M':'mega-menu-entry-consumers.v1.json'};packs={};bind={};allpacks={}
for k,n in names.items():
 raw=(C/n).read_bytes();d=json.loads(raw);allpacks[k]=d;packs[k]={x['id']:x for x in d['records']};bind[k]=dict(path=n,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader)
def refs(s):
 out=[]
 for z in s.split('|'):
  k,i=z.split('@',1);assert i in packs[k],z;x=packs[k][i];out.append(dict(package=names[k],complete_record_id=i,all_existing_manual_children=[a['id'] for a in x['child_assertions']]))
 return out
def vs(*ns):return '|'.join(f'V@CEV-CX{i:02}' for i in ns)
def rs(*ns):return '|'.join(f'R@C31-R{i:03}' for i in ns)
groups=[]
def group(p,i,lo,hi,status,r,meaning):groups.append(dict(id=f'WP32-{p}-PG-{i:02}',paper=p,range=[lo,hi],disposition=status,complete_existing_manual_records=refs(r) if r else [],manual_semantic_scope=meaning))
S='MANUALLY_JOINED_BOUNDED_STATIC';T='TYPED_SCOPE_OR_RESPONSIBILITY';U='TYPED_EXPLICIT_UNVERIFIED_BOUNDARY'
group('M',1,1,7,T,None,'情境输入/三临时成就/ready持久标记/触发调用为本正文；基础五家族/首目标/统一守卫/成功提交与资源消费引用WP31，成长/交换获得/捕获/Dex各真实主责保持；静态与固定算术未运行。')
group('M',2,9,9,S,'X@CCX-R010|R@C31-R050|C@CEC-R004','D>=49置ready/目标返回或triggertrue/演出未取消后真正species提交三层分离；准备无物种变化，找到目标不保提交，只有提交清ready并继续既有successsequence。HP0/heal其它清ready门另有明确规则。')
group('M',3,13,13,S,'X@CCX-R001|X@CCX-R002|X@CCX-R003|X@CCX-R004','逐条件真正调用才读取来源；无统一开战快照。具体短路先级/reader对象在各完整registration和callingunit，不是所有predicate每次全部运行。')
group('M',4,17,17,S,'X@CCX-R001|'+vs(1,2),'宿主livepbGetTimeNow、日5<=h<20/夜余下、早5–10/午后14–17/傍晚17–20；10–13仅day，各谓词非互补partition。不读背景time/TIME_SHADING/室外条件；host值/时区/异常未运行。')
group('M',5,18,18,S,'X@CCX-R002|'+vs(3,4),'worldscreen.weather_type已写intention再Weather.get.category；缺screen不命中、NoWeather直接==:None无需registry，其他未知categorylookup可失败。不是Battleweather/计时，淡变未结束也读新type。')
group('M',6,19,23,S,'X@CCX-R003|'+vs(5,6,7),'Location当前map.map_id不读坐标/获得图，mapnil可失败；flag当前MapMetadata.has_flag?大小写不敏感/缺metadatafalse；RegionTownMapPosition[0]非Dex区域；DarkMapmetadata非亮度/Flash/night；global骑surfdiving若metadata缺则false，none不补统一nilguard。')
group('M',7,24,24,S,'X@CCX-R004|'+vs(8,37),'player.pokemon_party排egg不排faint，可包括self；不读盒/partnermerged/场上临时types。依序逐成员时前member提交/append可改变后member读到队伍。')
group('M',8,25,28,S,'X@CCX-R006|X@CCX-R007|X@CCX-R009|B@CBC-R006|B@CBC-R007','持续model等级form/knownmoves/happiness/ability/gender/item在检查时读取，非Battler临时副本；交换counterparty为画面保存送出oldobject；battle记录当前partyindex不是PID；event参数caller显式/default0无usedset。正常EXP/item还原已在前，伙伴错配后真实值不能假称owninitial。')
group('M',9,30,30,S,'C@CEC-R001|C@CEC-R006|X@CCX-R001|'+vs(2),'等级先短路不读后clock/weather；forwardlist按原order首truthytarget停；选好target再动画等待不重跑全部condition，跨时不撤target。success oldspeciesafteractions仍targetmatch&&currentlyheld检查，可能与先前selection时item不同。')
group('M',10,32,32,S,'X@CCX-R005|C@CEC-R007|C@CEC-R009','环境变化本身不自动发起；worldafterLevel/helperExp/Level/maxRareCandy具体caller消费。满级且配置许用可不增长直接level-family检查，不将any_level_up元数据或timecondition改成必须刚升级。')
group('M',11,38,38,S,'B@CBC-R001|'+vs(9),'worldWild/Trainer先skip/able/debug门后startnotification记录当时playerparty L0、K0、D0，包括egg；后foe/partner/setup。准入skip在通知前返无新表，后callback失败可已留新表；不是partnermerged全体表。')
group('M',12,40,40,S,'B@CBC-R001|B@CBC-R007|X@CCX-R010','三表temporary每start重建/end正常进化后nil；ready属于Pokemon持久field，start或predicate失败不清，只有特定afterbattleDamage达49且统一guard通过才设true。')
group('M',13,44,44,S,'B@CBC-R002|'+vs(10,11),'pbProcessMoveHit每hit逐nonunaffectedtarget按effectivenessmessage入口：critical+Kcontainer+slot+userOwnedByPlayer则+1；无internalBattle/foe/nonSub/useralive附门。Disguise/IceFace消息入口先返；sub仅message继续，partner不playerowner故不计；numeric0slot有效、nil不补建。')
group('M',14,46,46,'TYPED_EXISTING_CONFIRMED_HISTORY','B@CBC-R002|'+vs(11),'N01旧已确认同步正确，当前WP31“对对方”旧摘要已经单点改好；只核当前真实记录domain，不新增finding/重开旧ID/重投。critical产生概率另归Combat，来源边界不省略实际计量receiver。')
group('M',15,50,54,S,'B@CBC-R003|'+vs(12,13,14),'actualhpLost在lethal/survival/substituteHPclamp后形成，先inflict/selfKO/faint再nonunaffected消息/损失record；D只要playerOwnedtarget容器及slot，不加foe/nonSub/individualHPchanged门。sub30+19个体不扣仍D49；confusion单独selfrecord有D无K；Disguise/IceFace这hit0，额外DisguiseHP减不经record。')
group('M',16,55,58,S,'B@CBC-R003|B@CBC-R004|'+vs(13,15,16,17),'ordinarypoison/burn/weather/hazards/recoil只减HP不自动record，以actualhelper调用为界而非allHPdelta；heal/withdraw不减D；真Faint经先前scene/callback后D0不清K，HP0先清R。presence0truthy/nilnoslot不写；裸battle未start不补表，specialmode独立通知。晚faint异常可停在Dreset前。')
group('M',17,64,64,S,'G@CGR-R003|G@CGR-R007|G@CGR-R008|G@CGR-R012|B@CBC-R007','T1击倒/捕获EXP/EV/level/moves已写model，L0旧值；普通battle成长不会即时跑worldend扫描，不把level学习提交等同本afterworld进化。')
group('M',18,65,66,S,'B@CBC-R006|B@CBC-R005|X@CCX-R011','T2先Dex/caughtstore后activeabilityleave再player-sidePeer generalform/item；T3currentplayerpoisonCount/UnmegaPrimal、partner存在heal双队、canLose2/5heal，进入endnotification前可清ready/复活，不此处清L0/K/D。normalend失败可只留先到达前缀，不保证全T2。')
group('M',19,67,70,S,'B@CBC-R007|R@C31-R048|R@C31-R050|'+vs(18,19,20,21),'T4allresults开或!=2&&!=5；关仍0/1/3/4。T5currentparty跳nil/egg/configfainted，L0存在且old<current则levelfirst，noTarget才battlefamily；cancel已选level不回头。T6Kthresholdtarget/D49只readyfalse-return；T7normalreturn清三表后pickupHoney或不可输2/5blackout；cancel不保存K/D。')
group('M',20,72,74,S,'B@CBC-R005|B@CBC-R007|'+vs(18,19,20,38),'两个Settings defaults依gen>=6true及faintedtrue；检查当时currentfaint，canLose预heal使falseconfig也可检查。不可输2/5默认先scan再blackout。BattleAbortedException明确rescue0可worldT3–7但不保T2；skip无notifications，replay/facilitybare/异常不自动取worldchain，无ensure清表。')
group('M',21,76,76,S,'B@CBC-R007|X@CCX-R004|X@CCX-R009|C@CEC-R006|'+vs(28,37),'eachcurrentparty单member最多oneTarget/oneScene，不chain重查同self；后member可读已变化队伍。Ruby普通Array迭代可遇appendShedinja，append无L0/K/D不继承creator；event入口先able_party新选集，不随之后append扩展。')
group('M',22,82,83,S,'X@CCX-R011|'+vs(16),'ordinaryswitch/BattlerShift不改Pokemon自身partyindex，K/D按原槽；displayposition或frontback变不清记录。特殊外部reorder另无通用同步。')
group('M',23,84,88,S,'X@CCX-R011|X@CCX-R010|B@CBC-R006|'+vs(22,23,24,36,39),'满队选择旧member：Peerleave/解除形态/存同reference/删player/消息后initialItems,L0,K,D左移末nil；新增只initialitem不补三表。直接box/取消后box无player移动，选择前cancel无指定member离场/删除但Dexprefix可已写。正常end后表nil，R个体持久；指定storageheal save/restoreR，一般heal清R。')
group('M',24,90,90,S,'X@CCX-R011|'+vs(22,23,39),'显式capacity3full+档0或2+boxspace+选A/noPartner/noextraCallback，array[B,C,X]且L0[20,30,nil]/K[3,0,nil]/D[49,5,nil]；nil≠0。A未转R的D49先box不在scan；已有R另保。反向default6only3不菜单/leftshift，appendindex3missing。')
group('M',25,92,92,S,'X@CCX-R011|S@C23-R023','Shadowbeforebattleheart数组不在四shifted表，不因L0/K/D正确而宣所有snapshot同步。任意插件/eventreorder无generalautoresync，具体旧ShadowindexMismatch保持本身约定，不扩所有储存路径。')
group('M',26,94,96,S,'B@CBC-R006|X@CCX-R011|'+vs(40,41,42),'伙伴actual参加/满6/档0/boxspace/两wild先击倒一后捕获余下且X/Y/Z/W合法无passive/callback不改：newmerged仍oldrefs而playerarray和6initialItemsshift；box同A/C仍被normalend旧merged索引访问，A=Y/B=nil或C=W/D=nil，A/B未移场景保持。无partneraliasarray则A退出遍历保持X/B=Y。不是enemyKnockOff必要条件，也不改L0/K/D的currentplayer扫描正确义。')
group('M',27,100,100,S,'X@CCX-R006|'+vs(30,34),'Trade统计先++→oldpartyref→incomingnew或reuse/Ownername/source/firstmoves→scene演出前Dexregisterowned→trade/endcheck/incomingEvolution(false)→wrapperreturn后才slotreplace。Incomingevo当时尚未最终入playerparty，earlyfailure可留statistics/Ownermodification/Dex。')
group('M',28,102,102,S,'X@CCX-R007|'+vs(31,32,33),'Trade/sex/time/item读incoming；TradeSpecies先incoming.species==param再outgoing.hasItemEverstone，非outgoingspecies。incomingEverstone外guard拒所有；default互换self≠param无target但trade收照常；customparam=self时outgoingspecies任意仍受stone门，outgoingnil且selfbranchtrue后查询可raise。')
group('M',29,104,104,S,'X@CCX-R007|C@CEC-R006|C@CEC-R008|'+vs(30,34),'TradeItemafter成功targetmatch&&incomingstillheld实际remove，不动outgoing/Bag/eventID；nohit不耗。Trade/evofalse无canceltrade，selector可以-1/emptyname并由event决定是否call；selector排eggShadow/不可trade门不嫁接裸pbStartTrade。')
group('M',30,106,108,S,'X@CCX-R008|'+vs(35),'conditionalnewDexpage内EndScreen(false)后wrapper仍EndScreen，无endedbusinessguard；spriteHash先clear使二message跳但sameviewport重复dispose宿主未知。两检查位置静态存在≠二次必抵达/必进化；若host继续则已变species再查，default末端通常none/customchain风险。任异常不回滚旧stat/Owner/Dex/evo，finalpartyreplace可未到。保N02旧问题无新finding。')
group('M',31,112,117,S,'X@CCX-R009|'+vs(26,27,28,29),'pbEvolutionEvent无playerreturn，先able_party(非egg非faint)快照array逐对象不扫box/后append；singletrigger无额外aliveguard，checknilfalse/targetscene默认cancel→关screen后true即使cancel。EventID/Kubfu1/Yamask1form2+R来自exactraw，具体剧情地点不在registry，只有definition的actualeventcaller仍U01，不造塔/拱门。')
group('M',32,119,121,S,'X@CCX-R010|'+vs(25,26,27,28,36),'Damage>=49实际battlecondition执行且outerguard过才Rtrue，不达不清既有true；成功evo/HP0/一般heal清，metadata地点变化不直接R。Event编号不消费，取消R/species保可同IDretry/多个memberreuse；成功改变个体资格不产生globalusedset。Criticalcancel后normalend仍清K不能跨场重试，后续需新记录/合适directcaller。')
group('M',33,125,127,U,'C@CEC-R001|X@CCX-R001|X@CCX-R002|X@CCX-R008|X@CCX-R009','守卫/判定ready/target/commit分层无坏weather/map/indexautofix。实际event地点caller/交换接待奖励/hostclock时区/doubleDispose/plugins/并发/media真实保留，不把已知静态definition/normalprefix当未知略读；U01–10跨域未自动关闭。')
group('M',34,131,131,'TYPED_COMPLETE_STATIC_VECTOR_REFERENCE',vs(*range(1,43)),'全部CX01–42完整原行/共同前提/人工children和mandatory94whole-sourceunitjoins已有逐完整有限接合；当前此行仅目录导航，不新增执行/要求新test/票。')
group('M',35,135,135,T,None,'基础进化/获得/战斗结果/maptime/HPparty/growth/catch/command/switch/MoveEffects/Dex/Mega/Shadow按真实跨片责任接合；全域批准不互转。')
group('M',36,139,142,U,'X@CCX-R008|X@CCX-R009','四具名未验证：实际eventcalls/交换接待奖励；双dispose第二检查可达未知；hostclockzone/plugins/concurrentparty；媒体/取消手感。静态双caller与真实来源已实审，运行保持NOT_EXECUTED。')
group('D',1,1,3,T,'X@CCX-R012','附表35contexts/57作者rows/mapweather/固定statevector，基础规则仍主稿/WP31。零作者样本不是能力不存在；sourceTrace定位是导航不是此处模拟执行。')
group('D',2,9,43,S,'X@CCX-R012','35每行独立ID/count/context，完整registrations全部存在；day/weather/transport/map/playerparty/itemtrade/battleevent族实际receiver各按主稿refs与下列每row精确绑定。零样本不移除函数定义；EventAfterDamageAcrossTwoFamilies仍oneidentity。')
group('D',3,45,45,S,'X@CCX-R012','35uniqueIDs，57authoredrows，17positive18zero，计数口径顶层currentbase+form作者字段，非运行compile后继承出来全部rows/wholePBS阅读；零不代表nocaller。')
group('D',4,49,49,S,'X@CCX-R007|'+vs(31,32),'57authoredrows不证明predicatepass，defaultKarrablast/Shelmet自身种≠param只是TradeSpecies不match，普通交换接收不被阻断。')
group('D',5,53,109,S,'X@CCX-R012','57每行parentheader/target/method/rawparam全部逐完整vector已actual收，typedparam与原sourcepointer/作者顺序保留；下面每physicalrow绑定完整19列edge，不用计数或sameblob代具体原值。未接898baseparentabsence向量不凭此授。')
group('D',6,115,117,S,'X@CCX-R003|'+vs(5,6,7),'Map028MossRock/034IceRock/049050051Magnetic逐完整rawmetadata，050DarkMap；当前图级flag可满足但不证明rock事件/真实可达/坐标约束。')
group('D',7,118,120,S,'X@CCX-R002','Map021Rain100/047Rain0/072Storm50完整raw，maptransfer天气概率consumer已真读；100normal设Rain可成为input/0只声明不当前rain/50Storm随机classRain。未执行rand或媒体，实际predicate仍检查时读屏幕意图。')
group('D',8,122,122,S,'X@CCX-R002','9defaultWeather全部完整注册：None/ Sun/ Rain Storm HeavyRain Fog/ Snow Blizzard/ Sandstorm类别各精确，NoWeather仅None，world!=BattleWeather。未知type部分categorylookup失败前缀主稿保。')
group('D',9,128,129,S,'B@CBC-R003|R@C31-R050|'+vs(12,13),'subHP30+19=49个体可0loss；confusion10+friend39=49无foe门，未faint前提；battleevent只Rtrue无target。实际加的hpLost而非预计伤害，status伤害不自动record。')
group('D',10,130,132,S,'B@CBC-R001|B@CBC-R002|B@CBC-R003|B@CBC-R004|'+vs(10,14,17),'48下一场1各start重建非49；20撑至1实际19不是100；perhit/perTarget三可计criticalwritesK+3可含friend/sub而Disguiseearly不同。固定算术与actualreceiver相接无概率运行。')
group('D',11,133,134,S,'X@CCX-R011|'+vs(22,39),'fullcapacity3chooseA/noPartner三数组左移精确 [20,30,nil]/[3,0,nil]/[49,5,nil]；defaultcapacity6only3直接append原records留/slot3nil。装空slot!=0，所有资源/选择/正常callback前提完整保留。')
group('D',12,135,135,S,'B@CBC-R007|'+vs(18,19),'worldendnotification确入前提，alltrue0..5、false0/1/3/4，不把准入skip当decision0scan。')
group('D',13,136,136,S,'X@CCX-R009|X@CCX-R010|'+vs(26,27),'Rtrueevent2match后cancel，trigger工具true但species/R不提交、编号不消费；只有真正successclearready，worldK/Dcleanup另一层。')
group('D',14,140,140,T,'X@CCX-R012','35literalregistry/57作者字段/具名map/weather源和consumer分别记录；没有参考表达式/游戏/编译器/事件执行，机械count/数学/人工控制流互不代替。')
formalpaths={'M':'deliverables/final-specification-set/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md','D':'deliverables/final-specification-set/pokemon-rules/wp32-context-inputs-and-scenarios.md'};formal={};parents=[];unknown=[]
receipt=json.loads((C/'pbs-evolution-reception.v1.json').read_text());selected=receipt['selected_snapshot'];snap=json.loads((BASE/selected['path']).read_text());edgeby={r[0]:r for r in snap['edges']};lookup={s:r['id'] for r in allpacks['R']['records'] for s in r['registered_identities']};data35=dict(allpacks['X']['data_context_method35']);rows57=iter(allpacks['X']['formal57_to_received_edges']);seenmethods=[];seen57=[]
for p,f in formalpaths.items():
 raw=(B/f).read_bytes();ls=raw.decode().splitlines();assert len(ls)=={'M':142,'D':140}[p];formal[p]=dict(path=f,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),lines=len(ls),current_actual_whole_reread={'M':'0c95e5 entire1–142','D':'6fb176 entire1–140'}[p])
 for i,l in enumerate(ls,1):
  if not l.strip():continue
  gs=[g for g in groups if g['paper']==p and g['range'][0]<=i<=g['range'][1]];struct=l.startswith('#') or (l.startswith('|') and l.lstrip('| ').startswith(('---','情境 |','阶段 |','变化 |','身份（审计） |','来源个体数据节 |','地图元数据编号 |','前提 |')))
  if not gs and not struct:unknown.append([p,i,l]);continue
  assert len(gs)<=1
  d=dict(id=f'WP32-{p}-L{i:03}',line=i,paper=p,complete_raw=l,disposition='TYPED_STRUCTURE_OR_TABLE_HEADER' if struct else gs[0]['disposition'],semantic_group_ids=[g['id'] for g in gs],new_atoms=0,qualification='Actual whole parent manually interpreted with whole selected childrecords/premises/fullunits and concrete receivers. No whole-domainPASS, sourcehash/count/oldPASS not used as meaning substitute.')
  if p=='D' and 9<=i<=43:
   cols=[x.strip() for x in l.split('|')[1:-1]];method=cols[0];assert method in data35 and int(cols[1])==data35[method];seenmethods.append(method);rid=lookup[method];d['complete_context_identity_binding']=dict(method=method,authored_row_count=int(cols[1]),actual_context=cols[2],registry_package=names['R'],complete_registry_record_id=rid,all_manual_registry_children=[x['id'] for x in packs['R'][rid]['child_assertions']],explicit_context_record='CCX-R012',complete_registration_source_unit='evolution:REG:'+method)
  if p=='D' and 53<=i<=109:
   cols=[x.strip() for x in l.split('|')[1:-1]];r=next(rows57);assert cols==r['formal'];edge=edgeby[r['received_edge_ordinal']];assert [edge[2],edge[10],edge[11]]==cols[:3];d['complete_authored_edge_binding']=dict(formal_four_fields=cols,full_received_edge_columns=snap['edge_columns'],full_received_edge_vector=edge,mandatory_received_snapshot=selected,actual_source_reader=receipt['original_reader'],finite_receipt='pbs-evolution-reception.v1.json',whole_PBS_credit=False);seen57.append(edge[0])
  parents.append(d)
assert not unknown,unknown
assert len(seenmethods)==35 and len(set(seenmethods))==35 and sum(data35.values())==57 and sum(v>0 for v in data35.values())==17 and len(seen57)==57
try:next(rows57);raise AssertionError('extra57row')
except StopIteration:pass
companions={}
for n in ['evolution-catalog79-exact-sourceunit-joins.v1.json','pbs-evolution-reception.v1.json','received/evolution460-forms339-selected-51ef7b0c.json']:
 raw=(C/n).read_bytes();companions[n]=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),qualification='Whole original finite object/common envelope previously actually received or ownread; all referenced completevectors require exact-unit-joins companion. Originalreader not transferred to own FULL.')
qualification=dict(same_actual_context=True,new_contexts=0,new_votes=0,own_full_file_metadata_qualification='Trade source actual EOF243. Original CCX complete pbStartTrade requested217–244 literal slice contains actual217–243 only, no extra line244reading credit. Sourcebytes/hash and complete method remain unchanged.',already_closed_historical_items=['WP32-N01 currentcorrectfielddomain','WP32-N02 staticdoublecaller/secondreachhostOPEN'],not_closed_by_parent_ledger=['20declaredPBSnotwhole','Aoldsourcefact/1430 obligations','fullhistorydedup','actualeventcalls/hostmedia/native/callbackruntime','WP23negativepositiondownstreamallvariants'])
out=dict(schema='gr8-crec-wp32-physical-parent-dispositions/v1',recorded_utc=utc,actual_reader=reader,formal_identities=formal,complete_manual_semantic_groups=groups,complete_nonempty_parent_records=parents,nonempty_parent_count=len(parents),manual_groups=len(groups),unassigned_parents=0,exact_context_identity_rows=35,exact_authored_edge_rows=57,mandatory_complete_source_packet_bindings=bind,mandatory_companions=companions,qualification=qualification,new_atoms=0,new_votes=0,whole_domain_acceptance=False,denominator_frozen=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');p=C/'wp32-formal-parent-dispositions.v1.json';assert not p.exists();p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),parents=len(parents),manual_groups=len(groups),unassigned=0,formal_papers=2,utc=utc)))
