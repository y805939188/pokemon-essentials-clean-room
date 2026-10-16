import json,hashlib,datetime,re
from pathlib import Path
C=Path(__file__).parent;B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception'
names={'R':'wp31-registry-meaning-atoms.v1.json','C':'wp31-wrappers-commit-meaning.v1.json','V':'evolution-catalog79-meaning.v1.json','A':'wp31-author-reverse-relation-bindings.v1.json','B':'battle-consumer-delta.v1.json','G':'wp30-compound-meaning.v1.json','X':'wp32-context-meaning.v1.json','BR':'breeding-catalog44-meaning.v1.json','N':'wp31-family-moonball-consumer-bindings.v1.json'};packs={};bind={};allpacks={}
for k,n in names.items():
 raw=(C/n).read_bytes();d=json.loads(raw);allpacks[k]=d;packs[k]={x['id']:x for x in d['records']};bind[k]=dict(path=n,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader)
groups=[]
def refs(s):
 ret=[]
 for z in s.split('|'):
  k,id=z.split('@',1);assert id in packs[k],z;x=packs[k][id];ret.append(dict(package=names[k],complete_record_id=id,complete_existing_atom_ids=[a['id'] for a in x['child_assertions']]))
 return ret
def rr(*ns):return '|'.join(f'R@C31-R{n:03}' for n in ns)
def group(id,lo,hi,status,r,meaning):groups.append(dict(id='WP31-PG-'+id,range=[lo,hi],disposition=status,complete_existing_manual_records=refs(r) if r else [],manual_semantic_scope=meaning))
S='MANUALLY_JOINED_BOUNDED_STATIC'
group('01',1,11,'TYPED_PURPOSE_SCOPE_AND_RESPONSIBILITY',None,'基础进化注册/五入口/目标顺序/准备取消提交/复制/道具消耗为本片，环境全触发、形态组合、HP/PP/Dex/UI/media/孵化/事件路线分属明示依赖；全部静态非运行通过。')
group('02',15,25,S,'C@CEC-R001|C@CEC-R002|C@CEC-R003|C@CEC-R006|R@C31-R050','十一术语：evolution三tuple多行、prevo反向不扫、methods参数类型、五家族+after、首success目标、oldspecies先afteraction、animationcommit/cancel、Shedinjaappend、readyset及HP/heal/evo clear、any_level_upmetadata非判定level比较。')
group('03',29,29,'TYPED_REGISTRY_DIRECTORY_LEGEND',None,'家族列及无参数说明是本表读法；后置不作为检查目标；不当调用可达性或新API。')
group('04',35,51,S,rr(*range(1,20)),'全部Level族逐完整注册：>=参数+各sex/time/weather类别/骑surfdiving/darkmap/darkparty非egg/atkdef关系/高PID16bits%10互斥/Ninjask与Level同谓词。weather/时段source在WP32具名，注册能力即使无defaultcaller仍审。')
group('05',52,58,S,rr(*range(20,27)),'Happiness阈值softcap160/220/sex/daynight/knownmove/type/held条件、MaxH==255、Beauty>=param；any_level_up不是函数内部升级检查，happiness持物after必须targetmatch且stillheld。合法defaultFeebas170源在完整author-edge有限接收，不把字面样本当任意资格。')
group('06',59,66,S,rr(*range(27,39)),'Hold/sex/daynight/happiness、HasMove/type/party(nonEgg)、LocationID/Flag(case rules原getter)/region各参数类型与完整proc；持物后置target&&held门另审，partytypes不补HPalive门，Envglobals未观察。')
group('07',72,75,S,rr(39,40,41,42),'Item族用inputitem==param加sex/daynight/happiness，非held身份替代；barecheck仍统一fourguard，不自消费使用物品。')
group('08',81,85,S,rr(43,44,45,46,47)+'|X@CCX-R006','Trade恒真/sex/time/held；TradeSpecies比较self.species==param且counterparty无Everstone（不是counterparty species）；selfEverstone还有外层统一门；TradeItemaftertarget/held实际移除。')
group('09',91,101,S,rr(48,49,50)+'|B@CBC-R002|B@CBC-R003|B@CBC-R004|B@CBC-R007','BattleCriticalcount>=param真实hit/targetrecord；Damage>=49设ready但本次false，event另一回inputID==param&&ready；Event无一次性使用集合，default0及异ID不命中/编号可复用不是个体state可重复任意成功。')
group('10',107,110,S,rr(24,27,28,29,30,31,32,46,51)+'|C@CEC-R006','Shedinja仅after动作无五判定，先partycapacity后POKEBALL才Duplicate条目target并扣balltrue停止，失败false继续；所有hold耗仅newSpecies==tupletarget且currentlyheldparam，首true后停止，真实Nincada双row保持Ninjasktarget/Shedinja附加。')
group('11',114,118,S,'R@C31-R052|C@CEC-R002|A@WAR-R004|N@WFC-R001','None registered无proc/runtimeexclude，不是未知ID；minimum前身incense1/nolevelproc非Shedinja继承/any+1或literalparam，sourcegetter完整。MoonBall真实从baby/family查use_item_proc+param，不等当前个体用石资格；DayCarefamily/baby consumer是依赖引用，family排序与firstsuccess不同，不推事件可达。')
group('12',122,126,S,'A@WAR-R001|A@WAR-R002|A@WAR-R003|A@WAR-R004','作者Evolutions后读物理位置不改schema先plural/singularappend；AB/BC顺序三个例firstreverse，form-specific[target,base_form]优先generic，firstwithin各key。合法acyclic/premises、forward保留、None补边与反向选择不作minmax/lastwrite，20PBS未whole不被schema代读。')
group('13',134,138,S,'C@CEC-R001','五wrapperlevel/item/trade/battle/event各额外参数（eventdefault0、battlerpartyindexvsOwner）；都调用同internalguard+各族handler；检查不负责renderer或外层资源提交。')
group('14',142,146,S,'C@CEC-R001|V@CEV-BE07|V@CEV-BE08|V@CEV-BE09|V@CEV-BE10','internal先egg/Shadow→Everstone→BattleBond，任一earlynil后row不评估；四guard影响所有family/stoneinput，abilitycache读取可有既有cache求值，不伪装完整bytes不变。')
group('15',150,154,S,'C@CEC-R001|R@C31-R050|A@WAR-R001','当前species_data/form_simple进化rows排prevo/None、sourceorder首truthyreturn目标/其后不试，allfalse nil；唯一领域判定写ready但缓存仍可fill。Tyrogue/Wurmple互斥与Eevee同目标多条件仍按原序，Level>=条件与any_level_up由caller给event区分。')
group('16',160,163,S,'C@CEC-R003|V@CEV-BE36|V@CEV-BE37','preparation当前cry/textwait/animation；target先hidden、firstupdatevisible/white255/zoom0，再约2放大2.6首大白轮廓/约9finish；successflash oldhide/targetzoom1/white0，cancelflash旧恢复/目标隐藏但先前白影不能擦历史。有效非透明bitmap/hosttimer/nointerrupt前提；BACK仅canCancel动画循环，cancelstat/msg而无wholeSuccess，早callerwrites保。')
group('17',169,171,S,'C@CEC-R004|C@CEC-R006','成功先count++→newSpeciescry→successME/message旧显示名→oldspecies afteractions首true停；normalreturn顺序非独立原子事务，中途message/cry失败可只留count。')
group('18',172,175,S,'C@CEC-R004|C@CEC-R005','genuine targetspecies change物种setterdefault_form>=0/targetform>0/否则oldstored，forcedclear/conditionalgendercacheclear/level/ability值cache失效而index保；samebase裸setter早退限定沿WP18。faintbefore保存/after保持HP0，再显式calc第二次，readyfalse，通常保留字段不倒补handler。')
group('19',176,178,S,'C@CEC-R004|C@CEC-R006|G@CGR-R013','newDexregister+owned，首次/hasDex/unlocked/configmore提示才msg/lastseen/Entry；0或currentlevelnewmoves按表order通用learn已会silent/满槽newMove或giveup，只拒这次learn不undoevo；noMovesDexEntry早EndScreen否则caller后关。')
group('20',182,185,S,'C@CEC-R006|R@C31-R051|V@CEV-BE22|V@CEV-BE23|V@CEV-BE24','Shedinja先容量后球；clone oldspecies/PID不重随机→tupletargetspecies/name空/marks[]/itemnil/ribbonsclear/POKEBALL/calc/heal→append/Dexseenowned→callerballremove，能力来源/EV/标记共享规则分别保。门失败仅跳copy正常原evo继续；晚exception不是保证原evo仍完成。')
group('21',189,191,S,'C@CEC-R005|C@CEC-R006','完整保留/变化表昵称来源owner/shinyIVnaturemarksribbons/repro通常gender，单/无性别新派例外，未命名新Speciesname；真实form优先级/HP/ready/Dex/evoLearn/hold消耗/额外copy变化。只提交本身，afteractions/caller各额外状态另核。')
group('22',197,200,S,'C@CEC-R009|C@CEC-R007|G@CGR-R009|G@CGR-R010','ChangeLevel/ChangeExp先跨intervallearn再levelcheck、canCanceltrue、先前Lv/EXP/h/moves保；RareCandy非max走Levelhelper返回true后外consume；Max路径Shadow拒/targetnil无effectfalse，targetfound可cancel仍handlertrue故consume，any-level family无需真升级。')
group('23',201,204,S,'B@CBC-R007|C@CEC-R008|X@CCX-R006|X@CCX-R009','worldafter currentparty oldlevel→levelcheck优先再battlefamily，配置false仅2/5截/eggs跳/conditionalfaint；stoneannotations beforechoice/readinputcheck后Evolution(false)无cancel/外按consumable处理；tradeincomingfalse与TradeItem提交内耗；eventableparty逐独立canCancel/编号可复用，地图callerU01未证。')
group('24',206,207,S,'C@CEC-R003|C@CEC-R007|C@CEC-R008|C@CEC-R009','三类renderer接口的cancel属caller非methodfamily；取消不扣内部held/ball但calleritem另据handlertruthy。进化石注释在UI打开前算，成功refresh/重新annotations，取消/失败前prefix保持。')
group('25',211,220,S,'C@CEC-R001|C@CEC-R003|C@CEC-R004|C@CEC-R005|C@CEC-R006|C@CEC-R007|C@CEC-R008|C@CEC-R009','十不变量每义分别接五wrapper/caches/guards/order/wholecancel、internalvsouterconsume、copy门独立、字段retention例外、success/cancelstats而非tradecount、HP/heal/commitclearready、取消权归caller。不是新增全caller事务或badinput保证。')
group('26',224,227,S,'C@CEC-R001|C@CEC-R008|C@CEC-R006','allnohitnil无领域evo含ready/cache例外；levelsilent/itemNoEffect；egg/Shadow及itemfrontmessage；Everstone/BattleBond含用石恒空；复制先party再ball，合法门失败原Evolution继续。')
group('27',228,232,S,'C@CEC-R006|C@CEC-R007|G@CGR-R013|X@CCX-R010','storehealing暂存/恢复ready例外源完整Storage单位在evo-catalog包且CCX-R010保精确writer；learnknownsilent/giveup不undo，animationcancel无内部consume但maxCandy仍consume；configuredfaint进化保0；maxCandy可命中any_level族无真Lvchange。')
group('28',233,235,S,'R@C31-R052|R@C31-R049|R@C31-R050|C@CEC-R004|X@CCX-R009','None不target；eventID错nil/no consumedset，另一member可同ID，cancel仍eligible可retry/成功species/ready变化非编号消耗；DexnoMoves早点EndScreen仅展示后缀不更已写状态。')
group('29',241,245,S,'C@CEC-R007|C@CEC-R004|R@C31-R020|B@CBC-R007','五Settings literal/default+expr逐项：SoftCapoff→220/on160；AfterAllGen>=6true但false2/5拒其它0/1/3/4仍可；Faintedtrue；DexmoreGen>=7true受其它门；RareCandyMaxGen>=8true。未观察runtimeoverrides/完整交互组合。')
group('30',247,247,'ROOT_OPTIONAL_P3_BOUNDED_SCOPE_ACTUALLY_RECEIVED','A@WAR-R001|C@CEC-R001','行格式/None/registeredmethod实际已核；未知静态“未定位”及§10错指经root不同context实际全文反证，GR8-CRE-WP31-UNKNOWN-001仅optionalP3窄资格/导航澄清。作者enum拒与directbadrowreachedgeterror已知、guard/先成功可避晚坏条；不新增required行为/API/向量，globalhistorydedupOPEN。')
group('31',249,249,'TYPED_EXPLICIT_UNVERIFIED_COMBINATIONS','C@CEC-R007|C@CEC-R006','maxCandycancel消费为静态明确但真实UI未运行；copy后续party/box运行组合、Env真实时机/事件U01分列，不把已知静态能力错记未知。')
group('32',253,253,'TYPED_COMPLETE_STATIC_VECTOR_REFERENCE','|'.join(f'V@CEV-BE{i:02}' for i in range(1,38)),'BE37全部原完整行/共同前提/人工children/必要sourceunits实际接合，exact-sourceunit-joins强制伴件94wholeunits保。只交叉目录，不新增执行/测试要求或独立票。')
group('33',257,257,'TYPED_DEPENDENCY_RESPONSIBILITY',None,'个体/HP/PP/growth/context/item/storage/Dex/MoonBall/trade/stats全部真实责任链解释，没收的whole域保持原reader/精确OPEN，未知host不作PASS。')
group('34',261,265,'TYPED_EXPLICIT_UNVERIFIED',None,'eventactualcall/完整Envinput主责已WP32静态闭合不代运行、copyPID已知与运行组合未知、Dex画面/动画host资源时长分别保；定义层已实读不借未知省略。')
group('35',266,266,'ROOT_OPTIONAL_P3_BOUNDED_SCOPE_ACTUALLY_RECEIVED','C@CEC-R001|A@WAR-R001','未知method静态未定位同一optionalrootcause第二片：作者pipeline拒与绕编译actualreached runtimegetraise不整体未知；完整root9102已实读7e475e及ack，52手工组/64独立registry身份限定保留，未改formal/原查询字节或自动启动optional采用。')
group('36',267,268,'TYPED_EXPLICIT_UNVERIFIED','C@CEC-R007','maxCandy取消后消费实际UI与进化后form/战斗form组合未运行；前向不自动缺required规范。')
formal='deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md';raw=(B/formal).read_bytes();lines=raw.decode().splitlines();assert len(lines)==268;parents=[];unknown=[]
lookup={s:x['id'] for x in allpacks['R']['records'] for s in x['registered_identities']}
for i,l in enumerate(lines,1):
 if not l.strip():continue
 gs=[g for g in groups if g['range'][0]<=i<=g['range'][1]];structural=l.startswith('#') or (l.startswith('|') and l.lstrip('| ').startswith(('---','方法 |','入口 |','步 |','保留 |','配置 |')))
 if not gs and not structural:unknown.append((i,l));continue
 assert len(gs)<=1
 p=dict(id=f'WP31-L{i:03}',line=i,complete_raw=l,disposition='TYPED_STRUCTURE_OR_TABLE_HEADER' if structural else gs[0]['disposition'],semantic_group_ids=[g['id'] for g in gs],new_atoms=0,qualification='Physical/compound parent actuallyread and manually interpreted, linked whole priorrecords means all children/commonpremise/receivers/source bodies. No range/hash/oldPASS substitution or new denominator; lines247/266 have finite rootoptional classification actuallyreceived, not wholeWP31 PASS.')
 if l.startswith('| `') and 35<=i<=107:
  methodcell=l.split('|')[1];ids=re.findall(r'`([^`]+)`',methodcell);assert ids and all(x in lookup for x in ids);p['complete_registered_method_row_bindings']=[dict(method=x,complete_record_id=lookup[x],package=names['R'],all_manual_child_assertions=[a['id'] for a in packs['R'][lookup[x]]['child_assertions']]) for x in ids]
 parents.append(p)
assert not unknown,unknown
companions={}
for n in ['evolution-catalog79-exact-sourceunit-joins.v1.json','wp31-unknown-method-note-review-request.v1.json','wp31-root-optional-reception-ack.v1.json']:
 b=(C/n).read_bytes();companions[n]=dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),qualification='Exact complete existing source mapping or originalquery/receivedrootack; all old bytes retained. Catalogjoin mandatory with any referenced vector. Rootoptional9102 actualfullreceived; rootexact40394 only identity metadata here.')
out=dict(schema='gr8-crec-wp31-physical-parent-dispositions/v1',recorded_utc=utc,actual_reader=reader,formal=dict(path=formal,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),lines=268,current_actual_whole_reread='1–140 toolfull +141–268 recoveredcomplete7e8795'),complete_manual_semantic_groups=groups,complete_nonempty_parent_records=parents,nonempty_parent_count=len(parents),manual_groups=len(groups),unassigned_parents=0,root_scope_open_parent_lines=[],root_optional_parent_lines=[247,266],root_optional_id='GR8-CRE-WP31-UNKNOWN-001',mandatory_complete_source_packet_bindings=bind,mandatory_companions=companions,qualification='All primary clauses actually audited. Oldunknownlocator has actualreceived boundedroot optionalP3 classification; artifact is not full task closure or automatic parent acceptance. Definitions without defaultcaller still statically audited; 52manualgroups versus64registeredidentities/host/independent credit boundaries retained.',new_atoms=0,new_votes=0,whole_domain_acceptance=False,denominator_frozen=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');p=C/'wp31-formal-parent-dispositions.v1.json';assert not p.exists();p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),parents=len(parents),manual_groups=len(groups),unassigned=0,root_optional=[247,266],utc=utc)))
