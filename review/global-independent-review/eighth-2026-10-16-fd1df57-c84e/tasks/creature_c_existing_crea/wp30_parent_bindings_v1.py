import json,hashlib,datetime,re
from pathlib import Path
C=Path(__file__).parent;B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception'
def rd(p):return json.loads(p.read_text())
def wr(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
names={'G':'wp30-compound-meaning.v1.json','V':'growth-catalog63-meaning.v1.json','W':'wp30-learning-consumers-and-binding.v1.json','ST':'stat-catalog67-meaning.v1.json'};packs={};bind={}
for k,n in names.items():
 raw=(C/n).read_bytes();d=json.loads(raw);packs[k]={x['id']:x for x in d['records']};bind[k]=dict(path=n,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader)
groups=[]
def refs(s):
 ret=[]
 for z in s.split('|'):
  k,id=z.split('@',1);assert id in packs[k],z;x=packs[k][id];ret.append(dict(package=names[k],complete_record_id=id,complete_existing_atom_ids=[a['id'] for a in x['child_assertions']]))
 return ret
def group(id,lo,hi,status,rr,meaning):groups.append(dict(id='WP30-PG-'+id,range=[lo,hi],disposition=status,complete_existing_manual_records=refs(rr) if rr else [],manual_semantic_scope=meaning))
group('01',1,31,'TYPED_PURPOSE_SCOPE',None,'标题、净化/来源资格、目的/范围/非目标。作为当前行为解释范围实际全文接收，不把source职责/未来API非目标当新增运行保证。')
group('02',36,42,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R001|G@CGR-R003|G@CGR-R005|G@CGR-R013|G@CGR-R014|G@CGR-R016|G@CGR-R017','术语逐项区分曲线表/表外、战斗分队索引与Owner、共享/全队、1.7或1.5外来、Move新对象与改ID、原h/受控域、派生affection、first_moves与level候选重叠位置。')
group('03',52,56,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R001|V@GCV-GR-02|V@GCV-GR-03|V@GCV-GR-04|V@GCV-GR-06','最大等级配置及容错；minimum先max夹再表/公式、nil/<=0返回error对象；最大经验；加法夹限；反向nil/负诊断名称异常、>=max、首阈值减一。五函数各自边界不互换。')
group('04',60,75,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R002|V@GCV-GR-01|V@GCV-GR-02|V@GCV-GR-06|V@GCV-GR-07','六条各自表内数学/1,50,100锚点、表长101/600值、L1特例、分段双层整除和表外两不同登记公式完整分层；默认max钳制与max101人工反向、非单调未知及反查分列，非独立模型运行通过。')
group('05',83,87,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R003|V@GCV-GR-08|V@GCV-GR-15|V@GCV-GR-16','internalBattle&&expGain→对方倒下或捕获且非空参与记录→有效参与按仍在队/未濒死/分队OwnerIdx；全队与共享收集互斥，当前或initial EXP_SHARE；先EV后EXP、余队补一次/一次其它消息、每对方最后清participants。')
group('06',91,97,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R004|V@GCV-GR-13|V@GCV-GR-14|V@GCV-GR-15|V@GCV-GR-16|V@GCV-GR-46|V@GCV-GR-47','满经验只calc早返；a=Lv*baseexp；参与/共享有无/兼任及split开关所有分支，各份额先整数；全队半份；基础<=0早于修正/+1且EV前缀保。有效参与0与从未参与不同。')
group('07',98,105,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R005|V@GCV-GR-09|V@GCV-GR-10|V@GCV-GR-11|V@GCV-GR-17|V@GCV-GR-18|V@GCV-GR-45|V@GCV-GR-48','严格顺序Trainer1.5→scaled先/5整数后因子floor/+1或非scaled/7→Owner语言非零1.7或ID1.5→BagCharm3/2→当前held负值才initial fallback→affection>=4/internal/未Mega6/5与消息标志→max夹/实际增量<=0静默→消息，倍率不合并。')
group('08',106,106,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R006|V@GCV-GR-20|V@GCV-GR-21|V@GCV-GR-22','Shadow实际max夹后增量经覆盖exp=只加saved与统计；stage<=3才提交，当前exp不变且return；stage>3不加exp/统计，不冒完整净化原子回滚。')
group('09',110,114,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R007|V@GCV-GR-19','先反算newlevel并拒反降，再统计exp，逐边界写EXP/经验条/逐level；仅当前场上成员levelup幸福，calc/升等消息与两窗/学习恰该级新招/形态复检；终点calc刷新。')
group('10',118,122,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R008|V@GCV-GR-23|V@GCV-GR-24|ST@STV-ST48','evYield当前持物handler否才initial；Pokerus>=1含cured倍2；Shadowstage<=3+saved含现值和暂存夹252/510；普通分支各次更新total，函数无calc，后调用者再算。')
group('11',130,134,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R009|V@GCV-GR-44','ChangeLevel夹目标/同值消息早返→记六stat/totalHP→level写/calc→升级baseHP1特例；降只消息两窗，升一次vitamin/消息两窗/跨区间招/进化资格。静态入口不补无源egg门。')
group('12',138,142,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R010|V@GCV-U03-EX01|V@GCV-U03-EX02|V@GCV-U03-EX03|V@GCV-U03-EX04|V@GCV-U03-EX05','ChangeExp先夹目标和同值早返；先差量消息仍oldE再提交；降不幸福、升先vitamin；calc/refresh后比较等级，同级分别早返，升才窗学招进化，降只窗。队伍/普通消息receiver和故障前缀保，五EX完整对照不代运行。')
group('13',146,148,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R011|V@GCV-GR-43','ExpCandy拒max/Shadow，qty>1先qty-1次vitamin，再一次ChangeExp；正常helper升再一次vitamin，共qty，实际消费由caller。')
group('14',154,157,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R012|V@GCV-GR-19|V@GCV-GR-51','Battle学习已会早返、空槽追加和同步/形态复检；满槽询问→Summary旧槽选择→新Move替换、在场同步、消息与复检；放弃不学。Battle本身无通用egg/Shadow前门，真实battle无蛋。')
group('15',161,164,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R013|V@GCV-GR-25|V@GCV-GR-26|V@GCV-GR-27|V@GCV-GR-28','通用nil/蛋非Debug/Shadow/已会分门，空槽追加；满槽选择后先新Move数组写，machine&&keep旧PP才min，后3消息/machine幸福/true。外层取消false与早期UI动态副作用范围另记242不扩保证。')
group('16',168,176,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R014|G@CGR-R015|W@WLC-BAG_TR_ACTUAL_WRITER|W@WLC-TM57_DEFAULT_RECEIVERS|W@WLC-EMPTY_RELEARN_DEFAULTS|V@GCV-GR-49|V@GCV-GR-50|V@GCV-GR-51|V@GCV-GR-52','两遗忘包装单对象4+1，HM/Debug/BACK/第五槽返回各自；候选nil/egg/Shadow空，level<=current未会首去重，额外只first未会且不重叠才前置；Bulba四组/BagTR真正writer/Party不追加、TM57与Magnemite实际raw；空UI首次strict失败先于输入；非空成功绘制才三层取消/成功提醒统计。')
group('17',180,180,'MANUALLY_JOINED_BOUNDED_STATIC','W@WLC-EVENT_SELECTOR_PREDICATES|V@GCV-GR-53','Able要求!egg且HP>0，NonEgg另允许fainted；唯一蛋不合格，选蛋留循环/BACK变量-1名字空，具体pbSet nil/negative guard及真实事件调用未知分别保。')
group('18',186,187,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R016|V@GCV-R6-U14-GR01|V@GCV-R6-U14-GR02|V@GCV-R6-U14-GR03|V@GCV-R6-U14-GR04','创建rawhappiness与editor域/parse unsigned无255上限/Species缺省70零保/constructor拷贝分层；作者256/255/省略/0观察在后继change之前；裸创建无取消/前门失败不保证成功对象，未来兼容政策不擅定。必须同读Happiness12unit producer伴件。')
group('19',191,206,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R016|G@CGR-R017|V@GCV-GR-35|V@GCV-GR-37|V@GCV-GR-38|V@GCV-GR-39|V@GCV-GR-40|V@GCV-R6-U14-GR05','档h/100仅0..255表内每方法独立三元；walking/levelup/groom/berry/vitamin/wing/machine/battleitem/faint/faintbad/powder/root/herb数值与已定位caller各限原领域入口。groom定义审完但defaultcaller未定位；wing成功EV才幸福；任意超界不无限外推gain。')
group('20',208,210,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R016|G@CGR-R017|V@GCV-GR-35|V@GCV-GR-36|V@GCV-GR-37','未知方法raise；仅正gain按同map+1/豪华+1/铃floor1.5顺序，再非evberrysoftcap179；负值跳全部正修正，正常末端clamp0..255，前故障不假夹限。')
group('21',214,218,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R017|V@GCV-GR-41|V@GCV-GR-42','h六区间映射0..5纯派生；EXP效果需开；战斗效果主责只接口登记；FRIENDBALL OnCatch直接h150/200与LUXURYBALL正变化+1区分，非所有球统一幸福规则。')
group('22',224,233,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R001|G@CGR-R004|G@CGR-R005|G@CGR-R006|G@CGR-R007|G@CGR-R008|G@CGR-R009|G@CGR-R010|G@CGR-R012|G@CGR-R013|G@CGR-R014|G@CGR-R016|G@CGR-R017','十条不变量逐个连接以上完整处理：raw/辅助夹限、经验路径、EV先行/Shadow、modifier序、Move新对象窄keepPP、通用门、记录重学排序、h修正/affection、场上levelup与vitamin差异、升降新招进化资格。不扩大成其它caller万能保证。')
group('23',237,241,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R001|G@CGR-R004|G@CGR-R007|G@CGR-R009|G@CGR-R010|G@CGR-R011','两非法接口各不同异常、Battle静默增量<=0与辅助差量消息区分，多级逐级/降无新招幸福进化、满经验Battle仅calc与Candy拒/满级RareCandy独立配置接口。')
group('24',242,242,'OPEN_ROOT_SCOPE_ONLY','G@CGR-R013|V@GCV-GR-27|V@GCV-GR-51','学习本身未到slot替换与Move新对象窄提交已核；“个体不变”是否整对象保证另有完整取消动态读scope观察，优先NO_REQUIRED解释，未由本表自裁/自验。')
group('25',243,244,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R006|G@CGR-R017|V@GCV-GR-20|V@GCV-GR-21|V@GCV-GR-22','Shadow实际暂存与stage>3不加保留；步数happiness计数persistent/128步caller有限接口，完整global步数分发不由本段重审/假穷尽。')
group('26',250,261,'MANUALLY_JOINED_BOUNDED_STATIC','G@CGR-R018','十二配置行逐项沿原15完整选定constants源与默认世代8值接合，EXPscaled/split/Trainer、Power8/capture、affection/softcap、afterbattle/fainted、relearn/rareCandy/keepPP/multiuse彼此不替代；未执行配置切换组合。')
group('27',263,263,'TYPED_EXPLICIT_UNVERIFIED_BOUNDARY','G@CGR-R002|G@CGR-R003|G@CGR-R017','软限加法序已有静态定义；ExpAll与Share由路径互斥，不把列为组合未知变成缺已知守卫；表外数值与完整运行后果分列。')
group('28',267,271,'TYPED_STATIC_VECTOR_REFERENCE','V@GCV-GR-01|V@GCV-GR-53|V@GCV-R6-U14-GR01|V@GCV-R6-U14-GR05|V@GCV-U03-EX01|V@GCV-U03-EX05','GR53/作者初值5/EX5共63完整有限向量实际人工包另列；本交叉引用不是新执行证明，不改原旧控制或增加强制测试。')
group('29',275,276,'TYPED_DEPENDENCY_RESPONSIBILITY',None,'上游数据/身份/步数/设置与下游进化/Shadow/道具/战斗/寄养/捕获持有责任链完整接收，不从依赖名转移其它主责批准。')
group('30',280,286,'TYPED_EXPLICIT_UNRESOLVED',None,'groom caller、Shadow完整恢复、表外完整运行、战斗affection、界面/事件、寄养静默对照、全部无运行确认按原具名边界保留。已在本上下文其它有限包真正读取的部分可接合，不能把该历史未决列表当未读借口或全域PASS。')
formal='deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md';raw=(B/formal).read_bytes();lines=raw.decode().splitlines();assert len(lines)==286
parents=[];unknown=[]
for i,l in enumerate(lines,1):
 if not l.strip():continue
 gs=[g for g in groups if g['range'][0]<=i<=g['range'][1]]
 structural=l.startswith('#') or l.strip()=='---' or bool(re.match(r'^\|\s*(?:---|术语 \||函数 \||曲线 \||方法 \||配置 \||友好度 \|)',l))
 if structural:parents.append(dict(id=f'WP30-L{i:03}',line=i,complete_raw=l,disposition='TYPED_STRUCTURE_OR_TABLE_HEADER',semantic_group_ids=[g['id'] for g in gs],new_atoms=0));continue
 if not gs:unknown.append((i,l));continue
 assert len(gs)==1
 parents.append(dict(id=f'WP30-L{i:03}',line=i,complete_raw=l,disposition=gs[0]['disposition'],semantic_group_ids=[gs[0]['id']],qualification='Actual fulltext and complete manually authored meaning records read; no clause inferred complete solely from range/table/semicolon or hash. This ledger links the exact paragraph to finite recorded meanings, not a new atom denominator.',new_atoms=0))
assert not unknown,unknown
out=dict(schema='gr8-crec-wp30-physical-parent-dispositions/v1',recorded_utc=utc,actual_reader=reader,formal=dict(path=formal,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),lines=286,prior_actual_whole_read=['476217','24a59d','97f99b'],current_actual_complete_reread=['12f6a0','d0fc48','5594ac']),complete_manual_semantic_groups=groups,complete_nonempty_parent_records=parents,nonempty_parent_count=len(parents),manual_groups=30,unassigned_parents=0,root_scope_open_parent_lines=[242],mandatory_complete_source_packet_bindings=bind,mandatory_selected_assertion_companions={'CGR-R014-A04':'wp30-learning-consumers-and-binding.v1.json','CGR-R016-A01':'wp30-happiness-initial-producer-binding.v1.json','current reread metadata':'mandatory-wp30-reread-extent-clarification.v1.json'},qualification='This is a parent-to-existing-complete-manual-meaning ledger, not additional assertions/newcontext/vote or globaldenominator. Each original body/wholeunit was actuallyread. Source/host/caller boundaries and pending line242scope preserved; no automatic wholeWP30/globalPASS.',business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');p=C/'wp30-formal-parent-dispositions.v1.json';assert not p.exists();wr(p,out);print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),parents=len(parents),manual_groups=30,unassigned=0,scope_open=[242],utc=utc)))
