"""Mechanical serialization of manually authored F04 dispositions; no game model."""
from pathlib import Path
import json, hashlib, subprocess, datetime

HERE = Path(__file__).parent
PARENT = HERE.parent / 'v2'
RR = HERE.parents[2]
B8 = Path('/workspace/pokemon-essentials-clean-room')
R = Path('/workspace/pokemon-essentials')
FIXED_B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
FIXED_R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
READER = '/root/facility_atomic_completion_cloud/f04_canonical_tail'
FORMAL = 'deliverables/final-specification-set/combat-requirements/wp56-palace-and-arena-variants.md'

def sha(raw): return hashlib.sha256(raw).hexdigest()
def objsha(x): return sha(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())
def save(name, x): (HERE / name).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
def ident(p, repo=None, commit=None):
    raw = p.read_bytes()
    x = {'path': str(p), 'bytes': len(raw), 'sha256': sha(raw), 'mode': oct(p.stat().st_mode & 0o777)}
    if repo and commit:
        rel = p.relative_to(repo).as_posix()
        fixed = subprocess.check_output(['git', '-C', str(repo), 'show', f'{commit}:{rel}'])
        x.update(repo=str(repo), commit=commit, repository_path=rel,
                 fixed_blob=subprocess.check_output(['git', '-C', str(repo), 'rev-parse', f'{commit}:{rel}'], text=True).strip(),
                 actual_matches_fixed_bytes=(raw == fixed))
    return x

base = json.loads((HERE/'received-sourcefacts.factored.json').read_text())
facts = [{**base['common_fields'], **x} for x in base['facts']]
fm_raw = (PARENT/'forward-mapping.json').read_bytes()
fm = json.loads(fm_raw)
extra_numbers = {19,20,21,29,712,713,714,727,728,729,947,948,949,950,951,952,1410,1411,1505,2146,2149,2231}
extra = [x for x in fm['atoms'] if int(x['id'][5:]) in extra_numbers]
extra_capsule = {'schema':'gr8-f04-additional-complete-sourcefacts/v1',
    'reader':READER, 'producer':'/root/facility_atomic_completion_cloud',
    'producer_container': {'path':str(PARENT/'forward-mapping.json'),'bytes':len(fm_raw),'sha256':sha(fm_raw)},
    'facts':extra, 'source_identities':{k:fm['source_identities'][k] for k in sorted({x['source'] for x in extra})},
    'qualification':'All fields of these exact finite objects actually read. Configuration installation is distinct from PBS eligibility. No whole parent, CORE, PA, or file FULL inherited.'}
save('received-sourcefacts.additional.json', extra_capsule)
facts += extra
index = {x['id']:x for x in facts}
source_identities = {**base['source_identities'], **extra_capsule['source_identities']}

pa_path = PARENT/'PA32-complete-case-child-reception.v2.json'
pa_raw = pa_path.read_bytes(); pa = json.loads(pa_raw)
pa_selected = [x for x in pa['explicit_case_children'] if x['case'] in ['P29','P30']]
save('received-PA29-30.finite-children.json', {
    'schema':'gr8-f04-finite-already-received-case-meaning/v1','reader':READER,
    'producer':'/root/facility_atomic_completion_cloud',
    'producer_container':{'path':str(pa_path),'bytes':len(pa_raw),'sha256':sha(pa_raw)},
    'common_premise':pa['common_premise'],
    'rows':[x for x in pa['rows'] if x['case'] in ['P29','P30']],
    'complete_case_children':pa_selected,
    'qualification':'Only the existing complete P29/P30 objects were actually received here. This adds no PA audit round, reviewer vote, source atom or PA32 completion claim. Original case premises remain intact.'})

def aid(n): return f'FAC-A{n:04d}'
def ids(*ns): return [aid(n) for n in ns]
def seq(a,b): return [aid(n) for n in range(a,b+1)]

rows = {}
def add(line, key, meaning, support=(), kind='BEHAVIOR', aliases=(), units=(), cases=()):
    rows.setdefault(line,[]).append({'id':f'F04C-L{line:04d}-{key}', 'meaning':meaning,
        'kind':kind, 'source_fact_ids':list(support), 'alias_of':list(aliases),
        'direct_source_units':list(units), 'existing_case_child_ids':list(cases)})
def b(line,key,meaning,*ns,**kw): add(line,key,meaning,ids(*ns),**kw)
def q(line,key,meaning,kind='SCOPE_QUALIFICATION'): add(line,key,meaning,kind=kind)

# These meanings were authored from the full current formal text and full named
# source/fact readings. Neither punctuation nor locator counts define children.
q(3,'classification','Combat requirements / user interface 是本文件分类；实现独立是文档约束，不是 R 的新增行为。','DOCUMENT_CLASSIFICATION')
q(5,'provenance','净化正文、批准 WP56 输入、批次 13 和集中追溯路径是来源导航；不据此继承旧批准或阅读。','PROVENANCE')
q(5,'scope','A–F 所列 Palace/Arena 接点界定本文审查范围；完整演出、接待事件及其它前向范围没有由本文自动接收。')
q(5,'static','正文的全部证据限定为静态，无运行确认；该限定覆盖每一个行为子项。')
b(9,'Palace','Palace 按性格与压半选类别并自动选招；其 AI 换人采用专用路径。',1243,1258,1259,1260,1261,1262,1263,1264,1265,1277)
b(9,'Arena','Arena 禁止主动换人、顺序补位，计数达到 3 后继续可评判。',1324,1326,1327,1328,1329,1347,1391)
b(9,'mode-and-rules','设施规则选择 Palace/Arena 生产者并组合布局；这里只接该模式/布局接点，不接全部资格谓词。',19,20,21,29,712,713,714,727,728,729,948,949,950,951,952,2234)
q(9,'ordinary-owner','WP40–52 的普通战斗、状态、AI、终局主合同保持外部归属；本文是变体差异，不把其引用扩成普通战斗全量通过。','DEPENDENCY_NAVIGATION')
q(11,'inputs','输入清单列出性格、HP、状态、招式数据、选择、计数、场上轮数和队伍顺序；对应消费分别在 §2/§3 子项。','INPUT_OUTPUT_INDEX')
add(11,'outputs','行动选择、压半、评判、写穿 HP、补位和裁判 UI 输出分别引用 §2.3/§2.4/§3；统计与胜负沿 WP42，未将内存写穿等同磁盘保存。',ids(1254,1255,1256,1257,1270,1326,1330,1363,1364,1365,1366,1376,1377,1388),kind='SUMMARY_REFERENCE')
q(13,'paired-layout','普通/变体成对的写法是比较组织形式；后续差异表为已有意义引用。','LAYOUT')
b(13,'record-playback','Palace/Arena 的记录和回放保留各自变体基类行为；录制与回放类别有区别，原始随机流不保证复现。',1410,1411,1505,2219)
q(19,'three-categories','此句引入随后有优先级的三分法，本身不另造一个 R 行为原子。','LAYOUT')
b(21,'self-first','精确 User 目标优先归防御，包括自身目标变化招。',1244)
b(21,'Bide','忍耐蓄力双倍返还功能归防御；前项优先于变化招分类。',1245)
b(22,'other-status','排除前项后，其它变化招归辅助。',1246)
b(22,'counters','物理反击与特殊反击功能归辅助。',1247)
b(23,'remaining','剩余普通伤害招归攻击。',1248)
b(27,'raw-vs-effective','两套各 25 个性格行、每行攻击/防御/辅助三原始字段；原始三列与实际抽样比例有区别。',1259,1260,1261,1262)
b(27,'boundaries','取 0–99 后先比较 A，再比较 2A+D；第二界限先存 A+D 又加 A，辅助为剩余段。',1258,1260,1261,1262,1298)
b(27,'Hardy-example','HARDY 基准 61/7/32 的实际比例 61/39/0，第二界限 129。',1302)
b(27,'Sassy-example','SASSY 压半 22/20/58 的实际比例 22/42/36，第二界限 64。',1303)
b(27,'Gentle-example','GENTLE 压半 90/5/5 的实际比例 90/10/0，第二界限 185。',1304)
q(29,'column-meaning','表头规定性格键与 usual/pinch 的 attack/defense/support 列顺序；25 行的 150 个字段逐项绑定原事实。','TABLE_SCHEMA')
matrix = [
('HARDY',[61,7,32],[61,7,32]),('LONELY',[20,25,55],[84,8,8]),
('BRAVE',[70,15,15],[32,60,8]),('ADAMANT',[38,31,31],[70,15,15]),
('NAUGHTY',[20,70,10],[70,22,8]),('BOLD',[30,20,50],[32,58,10]),
('DOCILE',[56,22,22],[56,22,22]),('RELAXED',[25,15,60],[75,15,10]),
('IMPISH',[69,6,25],[28,55,17]),('LAX',[35,10,55],[29,6,65]),
('TIMID',[62,10,28],[30,20,50]),('HASTY',[58,37,5],[88,6,6]),
('SERIOUS',[34,11,55],[29,11,60]),('JOLLY',[35,5,60],[35,60,5]),
('NAIVE',[56,22,22],[56,22,22]),('MODEST',[35,45,20],[34,60,6]),
('MILD',[44,50,6],[34,6,60]),('QUIET',[56,22,22],[56,22,22]),
('BASHFUL',[30,58,12],[30,58,12]),('RASH',[30,13,57],[27,6,67]),
('CALM',[40,50,10],[25,62,13]),('GENTLE',[18,70,12],[90,5,5]),
('SASSY',[88,6,6],[22,20,58]),('CAREFUL',[42,50,8],[42,5,53]),
('QUIRKY',[56,22,22],[56,22,22])]
for row_index,(nature,usual,pinch) in enumerate(matrix):
    for j,(table,values) in enumerate([('usual',usual),('pinch',pinch)]):
        for col,value in enumerate(values):
            b(31+row_index,f'{nature}-{table}-{col}',f'{nature} 的 {table} 原始{["攻击","防御","辅助"][col]}字段为 {value}；不是直接生效概率。',1091+6*row_index+3*j+col)
b(59,'EOR-gate','常规回合末返回且 decision=0 才逐存活战斗者检查压半。',1267,1275)
b(59,'sleep-and-once','未倒下、尚未压半且实际状态非 SLEEP 才能首次置真；其它状态不额外阻挡。',1267,1268)
b(59,'inclusive-half','当前 HP≤总 HP 整数除 2，含等于和奇数总 HP 的整数边界。',1269)
b(59,'write-display','合格后先置 Pinch 真，再请求分组消息；显示失败不撤销已写标记。',1270)
b(59,'healing','同一在场期间保持真，回血不会清除或反复播报。',1268)
b(59,'replacement','换入初始化在接力保留分支之外清 Pinch；普通实际 Replace 接通此初始化，因此再次换入重新检查。',1300,1301)
b(59,'eager','QUIET/BASHFUL/NAIVE/QUIRKY/HARDY/DOCILE/SERIOUS：渴望更多。',1271)
b(59,'growl','CAREFUL/RASH/LAX/SASSY/MILD/TIMID：低吼。',1272)
b(59,'glint','GENTLE/ADAMANT/HASTY/LONELY/RELAXED/NAUGHTY：眼中闪光。',1273)
b(59,'position','JOLLY/BOLD/BRAVE/CALM/IMPISH/MODEST：进入就位状态的提示。',1274)
b(63,'shared-auto','玩家 Fight 在先决门后、AI 在换人/用物判断后均接同一 Palace 自动选招；替代菜单或普通逐招评分。',1266,1296,1297,2146,2233)
b(65,'nature-pinch','取当前战斗者 nature id，并按当前 Pinch 选 usual 或 pinch。',1258,1259)
b(65,'AI-random','使用 AI 的 0–99 平直随机入口；它直接用全局随机而非 Battle 录制 RNG，不保证按战斗种子复现。',1258,1298,2219)
add(66,'boundary-reference','严格比较 A / 2A+D / 余段，复用本文件 L27 已验抽样规则。',ids(1260,1261,1262),kind='SUMMARY_REFERENCE',aliases=['F04C-L0027-boundaries'])
b(67,'slot-eligibility','默认四招式槽逐槽保留存在且 PP>0 的槽，并要求所选类别相同；顺序按实际槽索引。',1249,1250,1263)
b(67,'ChoiceBand','仅有效 Choice Band 加残留不同招锁定时排除该槽；不扩成所有讲究类道具共用简化检查。',1251)
b(67,'Torment','Torment 为真且该招等于存在的 lastMoveUsed 时排除。',1252)
b(67,'omitted-selection','该部分资格不检查 Encore/Disable/Taunt/Imprison；玩家前门与后续实际执行门分别处理。',1253,2233)
b(68,'incapable','所选类别没有部分合格槽时登记 -2 并承载 Struggle 对象，不等同常规 -1 Struggle 选择。',1256,1264,2153)
b(68,'uniform-candidate','否则用第二次 AI 随机从合格槽列表等概率选索引并登记。',1265,1298)
b(68,'choice-tuple','登记写 UseMove、槽索引、招式对象、目标 -1；该本体不再次做普通资格检查。',1254,1255,1256,1257)
b(68,'target-path','Palace 自动返回前不调用常规手选后的选靶菜单；执行会进入查找/调整目标路径，目标 -1 不承诺打开菜单。',1257,1266,2146,2233,units=['USEMOVE-154-578','COMMAND-FULL'])
b(69,'recorded-registration','实际设施记录类仍经正常覆写入口记录所登记行动，含 -2 的事实；随机抽样不因此纳入录制 RNG。',1410,1411,2153,2219)
b(70,'player-gate','玩家 CanShowFight 遇 Encore>0 或没有普通可选槽时先走普通 AutoChoose：可用 Encore 招/否则普通 Struggle，不进入 Palace 抽样。',2233,units=['COMMAND-FULL','ORDINARY-CHOOSING-5-95'])
b(70,'AI-entry','AI 的先后为 setup→换人→用物→AutoFight；先前返回真时不进入选招，未早返时可抽到 -2。',1296,1297,1264)
b(70,'same-draw-register','两条已进入 Palace 自动路径使用同一套抽样、部分资格与登记。',1258,1263,1264,1265,1266)
b(70,'Mega-player','Palace 玩家自动返回在手动 Mega 开关场景之前，因此通常 Palace Fight 不登记 Mega。',2146)
b(70,'Mega-AI','AI 未选择换人/用物时也在普通 Mega 登记之前返回，单有资格不触发该路径的 Mega 执行。',1297,2149)
q(70,'Mega-scope','上述入口限定不排除外部/调试另外登记；已登记 Mega 的记录缺口由 WP58 的有限主合同处理。')
b(74,'switch-dispatch','battlePalace 为真时替代普通 AI 换人；非 Palace 才把参数转给前驱普通方法。',1243,1277)
b(76,'PerishSong','PerishSong 恰为 1 先令应换为真，跳过概率计算。',1279)
b(77,'no-move-late','否则，常规无可选招且真实场上 turnCount>5 时应换为真，跳过概率。',1280)
b(78,'current-percent','概率分支 h 是当前 HP×100/totalHP 的整数百分比。',1281,1299)
b(78,'candidates','只给 CanSwitch 接受的当前队伍成员计算整数 HP 占比。',1282)
b(78,'strict-best','最佳从无候选/0 开始，仅严格大于更新；正占比同值保留最早，取整 0 的存活后备可没有最佳。',1283,1284)
b(78,'base-under50','h<50：m<h 给 20，否则 40；不满足时基础仍为 0。',1285)
b(78,'override-under25','h<25 再以 30/50 覆盖前档，比较仍为 m<h。',1286)
b(78,'status-bonuses','睡眠/冰冻+20，毒/烧+10，麻痹+15，按状态互斥分支选一项。',1287,1288,1289)
b(78,'recent-penalty','先前 justswitched 真则减 60 并下限夹 0。',1290)
b(78,'random-gate','抽 AI 0–99，严格小于最终因子才令应换为真。',1291,1298)
b(79,'early-register','概率命中且已有最佳时登记最佳后直接返回真。',1291)
b(79,'skip-history','该早返跳过 justswitched 赋值，旧真/假均原样保持。',1292)
b(80,'fallthrough-history','其余路径先把 justswitched 赋为 shouldswitch；含两个强制条件分支、概率命中无最佳或未命中。',1279,1280,1293)
b(80,'fallback','应换为真时再按队伍顺序找首个合法成员并登记，返回真。',1294)
b(80,'no-candidate','不应换或无合法后备返回假；标记先前赋值仍保留。',1293,1295)
b(81,'force-argument','Palace 分支不读取 force_switch 参数；这里按同一逻辑处理该参数的真假。',1278)
b(87,'mind-command','命令阶段仅对真 move 对象的 UseMove 累加心分；换人/物品不计。',1344)
b(87,'mind-negative','仅 ProtectUser、UserEnduresFaintingThisTurn、FlinchTargetFailsIfNotUserFirstTurn 三具名功能为 -1，不能扩大到其它守护变化招。',1336,1337,1338,1340)
b(87,'mind-zero-positive','两种 Counter 与 Bide 为 0，其它变化招为 0，其余伤害招 +1。',1339,1340)
b(87,'skill-slot','技是当前槽：攻击阶段全清 0，结算按状态赋值覆盖，回合末只加当前值一次到侧累计。',1309,1310,1311,1312,1313,1314,1315,1316,1346,1382,1387)
b(87,'body','每侧体分=currentHP×100 整除 max(首发实际 HP,1)，两侧各自基线。',1333,1355,1356)
b(87,'body-replacement','正常补位不更新基线且不夹 100，HP115/首发100 得 115。',1357,1380,1381)
b(89,'creation','每战斗者成功状态在建立时 full clear。',1305)
b(89,'attack-clear','每次攻击阶段对所有非空槽 full clear，包含当时已倒下槽；type=normal/use=0/protected=false/skill=0。',1306,1307,1308,1309,1382)
b(91,'state1-prefix','执行复检、PP 和使用记录等前序通过后才写 useState1；此前返回未到生产点。',1383,units=['USEMOVE-154-578'])
b(92,'state2','状态 2 表示完成目标处理分支，不要求实际命中或有受效目标。',1384,units=['USEMOVE-154-578'],cases=['FAC-PA-P29-not-hit'])
b(92,'type-sum','非空 targets 先将相性归 0，只加 unaffected=false 的目标相性；全保护/未命中/无效可完成状态 2 且合计 0。',1384,units=['USEMOVE-154-578','TARGETCHECK-303-526'])
b(92,'no-target','空 targets 时不重写相性，保留本轮 clear 的 normal；无目标反射可跳过原命中循环而仍置 2，失败历史与之独立。',1306,1384,units=['USEMOVE-154-578'],cases=['FAC-PA-P29-reflect'])
b(93,'living-tail','仅到正常 common tail 才对当前存在且存活的 allBattlers 结算；提前返回或已经倒下分别排除。',1385,units=['USEMOVE-154-578','ALLBATTLERS-448-450'])
b(93,'state0','state0 不写 skill。',1316)
b(93,'state1-unprotected','state1/protected=false 写 -2。',1310)
b(93,'state1-protected','state1/protected=true 保持旧 skill。',1311)
b(93,'state2-map','state2 按相性超有效/normal/微弱/无效写 2/1/-1/-2，不用 protected 豁免。',1312,1313,1314,1315)
b(93,'postclear','结算后仅 clear(false) 清 use/type/protected，保留技值至覆盖或下次攻击阶段全清。',1306,1307,1308,1309,1316)
b(93,'overwrite-example','先写 +2 再写 -1 的当前槽为 -1，不累加成 +1。',1387)
b(94,'normal-Protect','给定普通存活 Tackle/成功 Protect 与通过前置门：目标标无效，分支完成为 state2/type0，技写 -2，目标受击伤害 0。',2231,1384,1385,1315,units=['TARGETCHECK-303-526','USEMOVE-154-578'],cases=['FAC-PA-P29-protected'])
b(94,'normal-hit','普通未保护一般相性完成且存活，state2/normal 得 +1。',1384,1385,1313,cases=['FAC-PA-P29-normal'])
b(94,'direct-fixture','直接 state1/protected=true 的夹具保留旧技，不能充当上述普通 Protect 路径的实际生产结果。',1311,1384,cases=['FAC-PA-P29-protected'])
b(95,'reflection-prefix','无目标反射分支正常完成、原使用者存活且无其它覆盖时，原 state2/默认 normal 得 +1；失败历史布尔不替代成功槽。',1306,1313,1384,1385,units=['USEMOVE-154-578'],cases=['FAC-PA-P29-reflect'])
q(95,'reflection-limit','这只是指定反射完成前缀，不保证任意反射招、回调或宿主整场运行成功。')
b(96,'ordinary-success-machine','同一状态生产/清理/结算机也在普通战斗运行；Arena 独有的是侧技分累计和裁判消费。',1382,1383,1384,1385,1346)
b(96,'late-last','整体失败可写 state1 后早返，若最后行动且无后继正常尾部，则旧技槽不补记，EOR 只加旧值。',1386,1346,cases=['FAC-PA-P30-last'])
b(96,'late-later','同回合后续另一行动到正常尾部可消费仍存活者 pending state1，写 -2 并清状态。',1385,1386,1310,1316,cases=['FAC-PA-P30-later'])
b(96,'prefix-fainted-controls','前序门未写 state1 与已经倒下者分别对照，不都算即时 -2。',1383,1385,cases=['FAC-PA-P30-prefix','FAC-PA-P30-fainted'])
b(100,'start-reset','开场设置提示标记，清两侧心技，保存各自当前首发 HP，计数 0，然后普通 all-entry。',1317,1318,1319,1320,1321,1322,1331,1332,1333,1334)
b(100,'prompt','首次命令阶段提示两个战斗者开始；显示返回后才清标记并置 count0。',1341,1342,1373)
b(100,'normal-entry','正常补位调用实际 Participated 而非 AsActive；不重置开场提示/心技/首发 HP/计数。',1380,1381,2175)
b(100,'ordinary-command','随后普通命令流程；只在返回 decision0 时按所选 UseMove 加心分。',1343,1344)
b(101,'EOR-first','先普通 EOR，非零 decision 立即返回；继续时每侧加当前 skill 一次，再 count+1。',1345,1346,1347)
b(101,'threshold','只在 count<3 跳过，count≥3 每次都可裁判，不按模 3 周期。',1347,1391)
b(101,'cancel-list','裁判计算前两侧按序 CancelMoves(true)：清 TwoTurnAttack/Rollout/Outrage/Uproar/Bide/FuryCutter，不附加逆鳞结束混乱。',1348,1389)
b(101,'recharge-preserved','CancelMoves 不清 HyperBeam；HyperBeam>0 时保留 currentMove，只有 0 才清当前持续招身份。',1390,units=['CANCEL-80-95'])
b(101,'recharge-lifecycle','成功回复期效果设 2，普通存活 EOR 减至 1；若裁判后存活且未被替代，下轮 recharge 门拒绝行动，随后普通 EOR 才减至 0。',1390,2236,units=['RECHARGE-EFFECT-185-190','ORDINARY-EOR-597-780','TRYUSE-183-297'])
b(101,'loser-reset-distinct','败者倒下/补位初始化清自己效果，与裁判取消保留胜者回复期是不同路径。',2235,1390)
b(101,'consecutive','首个第 3 轮裁判后正常补位保持 count，继续的第 4/5 轮也可连续裁判。',1391,2232)
b(102,'mind-rating','心相等各 1，不等胜侧 2、败侧 0。',1349,1350,1351)
b(102,'skill-rating','技相等各 1，不等胜侧 2、败侧 0。',1352,1353,1354)
b(102,'body-rating','体百分比分别比较，相等各 1，不等 2/0。',1358,1359,1360)
b(102,'sum','三项合计较高胜、较低负、相同平；两胜一负 4:2，全平 3:3。',1362,1363,1364,1365)
b(103,'display-order','裁判显示 Mind→Skill→Body，含双名、VS、当前累计总分与各项判定图标。',1370,1371,1372,1376)
b(103,'messages','逐项提示后按同一总分比较显示平局/玩家胜/对方胜总结。',1376,1377)
b(103,'scene-limit','场景请求/清理顺序是静态接点：显示数组为克隆，异常可能在 HP 提交之前；视口清理也不保证无异常。',1361,1374,1375,1378,1379)
b(107,'tie-HP','平局先玩家 HP0/Faint(false)，再对方 HP0/Faint(false)；是直接持久个体写穿，非攻击伤害流程。',1363,1388,units=['BATTLER-HP-107-112','POKEMON-HP-246-250'])
b(107,'EXP','上述提交正常返回后调用 GainExp，再进入 Arena EORSwitch；不因直接 HP0 跳过后继升级结算调用。',1366)
b(108,'loser-HP','非平局只令败侧 HP0 后 Faint(false)，经同一 Battler writer 写穿 Pokemon HP。',1364,1365,1388,units=['BATTLER-HP-107-112','POKEMON-HP-246-250'])
b(109,'decision-before-replace','按 favorDraws/decision 门后先 Judge，任何得出正终局均在补位前返回；两侧无后备由此判终局。',1325,1326,2174)
b(109,'next-index','仅当前已倒下且本侧 index+1 未越队伍长度才加一，用精确下一成员；不通用枚举合法后备。',1327,1328,1329)
b(109,'replace-sequence','消息→直接 Replace→Entry 按序执行；仍在回合末未终局流程。',1330,1345,1366,2174)
b(109,'state-retention','顺序补位保持两侧心技累计、首发 HP、count 和已清开始提示；实际 Entry 不触发 AsActive 定义。',1367,1380,1381,2175)
b(110,'switch-denial','主动换人对两侧返回假；有 partyScene 才请求不能换下提示，AI battleArena 分支也恒假。',1324,1368)
b(110,'only-sequential','普通资格选择后备的路径受 CanSwitchIn=false 阻断，含正常 Baton Pass；本文 normal Arena 的补位路径是直接顺序替代。',1324,1329,2173,2174)
b(111,'no-reset','裁判与正常补位本身都不清 count；仅存在 AsActive 复位定义不能证明普通入场调用了它。',1335,1367,1380,1381,2175)
add(111,'P28-reference','第 3→4→5 轮状态引用已验 P28 有限推导；不新增 PA32 审核/运行资格。',ids(2232,1391),kind='SUMMARY_REFERENCE')
q(115,'comparison-columns','差异表头按普通/Palace/Arena 展示，后续每行是前述主规则或外部主合同引用。','TABLE_SCHEMA')

def summary(line,key,meaning,ns,aliases): add(line,key,meaning,ids(*ns),kind='SUMMARY_REFERENCE',aliases=aliases)
summary(117,'player','普通手动菜单；Palace 的部分资格自动选择及先行 Encore/无普通槽分流；Arena 保持普通菜单。',[1253,1263,2146,2233],['F04C-L0063-shared-auto','F04C-L0070-player-gate'])
summary(118,'AI','普通逐招评分；Palace 自动取代评分；Arena 选招仍普通但换人恒假。',[1296,1297,1368],['F04C-L0070-AI-entry','F04C-L0110-switch-denial'])
summary(119,'layered-checks','普通选择/执行层继续检查四项；Palace 部分选招不检，但执行继承普通检查，Encore 的实时改招也在执行前段。',[1253,2233,1383],['F04C-L0067-omitted-selection','F04C-L0091-state1-prefix'])
summary(120,'choice-Torment','Palace 选择阶段只用其简化 ChoiceBand/Torment 检查；普通/Arena 的通用门未被此表替换。',[1251,1252],['F04C-L0067-ChoiceBand','F04C-L0067-Torment'])
summary(121,'active-switch','普通/Palace 的主动换人沿普通资格；Palace AI 专用逻辑，Arena 两侧与 AI 禁止。',[1277,1324,1368],['F04C-L0074-switch-dispatch','F04C-L0110-switch-denial'])
summary(122,'switch-order','普通/Palace 沿普通人选；Arena 取队伍顺序精确下一成员。',[1329,2174],['F04C-L0109-next-index'])
summary(123,'EOR','Palace 常规后压半及重入复位；Arena 常规后加槽/至少3门、保留累计基线、取消列明持续招但保留回复期，随后评判/倒下。',[1275,1300,1301,1345,1346,1347,1389,1390,1391],['F04C-L0059-EOR-gate','F04C-L0101-EOR-first','F04C-L0101-recharge-preserved','F04C-L0101-consecutive'])
summary(124,'success-state','普通与 Palace 都建立/更新/结算同一成功状态机；Arena 专有裁判累计及消费，不能把状态机误写为 Arena 才存在。',[1382,1383,1384,1385,1346],['F04C-L0096-ordinary-success-machine'])
summary(125,'HP','Arena 败/平直接 HP0 并倒下、写穿个体，而不是攻击伤害。',[1363,1364,1365,1388],['F04C-L0107-tie-HP','F04C-L0108-loser-HP'])
summary(126,'record-modes','WP58 为记录随机主合同；各变体类保留 Palace 自动/压半或 Arena 启动/不复位/连续裁判的活体行为，不许诺原随机流回放等价。',[1410,1411,1505,2219,1391],['F04C-L0013-record-playback'])
q(127,'retained-contracts','普通状态、命中、保护、WP42 终局与 WP44 资格继续为外部主合同；“同上”是保留范围，不证明任意状态/回调/宿主成功。','DEPENDENCY_NAVIGATION')

q(131,'PA-navigation','PA-P01..P32 是 catalog 的 32 个具名示例导航；本子贡献不重复审查已由父实际接收的整套 89 case children。','CASE_NAVIGATION')
summary(131,'sampling','HARDY/SASSY/GENTLE 抽样门与类别优先级重复指向已验正文；未新增随机运行。',[1302,1303,1304,1244,1245,1247],['F04C-L0027-Hardy-example','F04C-L0027-Sassy-example','F04C-L0027-Gentle-example','F04C-L0021-self-first','F04C-L0021-Bide','F04C-L0022-counters'])
summary(131,'Palace-eligibility','无合格槽 -2、四项分层、玩家前门、压半恰半/睡眠/回血/重入。',[1264,1253,2233,1268,1269,1300,1301],['F04C-L0068-incapable','F04C-L0067-omitted-selection','F04C-L0070-player-gate','F04C-L0059-inclusive-half','F04C-L0059-replacement'])
summary(131,'switch-formula','灭亡歌/无招>5、两档公式/状态/减60、早返标记、无候选及后备整数0/1分流，重复指向算法意义。',[1279,1280,1281,1283,1284,1285,1286,1287,1288,1289,1290,1291,1292,1293,1294,1295],['F04C-L0078-strict-best','F04C-L0078-override-under25','F04C-L0079-skip-history','F04C-L0080-fallthrough-history'])
summary(131,'success-fixtures','心分具名三项、状态表/覆盖/全清、整体失败旧槽、Protect/反射与存活/待结算前缀，重复指向对应原事实；直接夹具和实际生产保持区别。',[1336,1337,1338,1310,1311,1312,1313,1314,1315,1316,1382,1384,1385,1386,1387],['F04C-L0087-mind-negative','F04C-L0093-state2-map','F04C-L0094-normal-Protect','F04C-L0095-reflection-prefix','F04C-L0096-late-last','F04C-L0096-late-later'])
summary(131,'judge-replace','未满3、取消/回复期、4:2/3:3、HP写穿、体分分母1、越界终局、禁止主动换人、三员3/4/5轮连续评判保留，均为已验有限意义引用。',[1347,1389,1390,2235,2236,1362,1363,1388,1355,1356,1326,1328,1324,1368,1391,2232],['F04C-L0101-threshold','F04C-L0101-recharge-lifecycle','F04C-L0102-sum','F04C-L0109-state-retention'])
summary(131,'factory-modes','设施模式分派引用实际 constructors/type，而非把 playback command dispatch 当 factory 证据。',[2234,1410,1411],['F04C-L0009-mode-and-rules'])
q(135,'direct-dependencies','WP55 模式/包装、WP54 规则布局、WP51 AI 语境、WP44 状态资格是具名主合同引用；其余 WP40/42/43 接点维持各自所有权。','DEPENDENCY_NAVIGATION')
summary(137,'data-config','配置清单引用25×3两表、类别优先级、含等于整数半血、AI概率常量、三项2/0与平1/1、计数3门、相性2/1/-1/-2；不另建重复 R 原子。',[1244,1245,1246,1247,1248,1259,1269,1285,1286,1287,1288,1289,1290,1312,1313,1314,1315,1347,1349,1350,1351,1352,1353,1354,1358,1359,1360],['F04C-L0029-column-meaning','F04C-L0059-inclusive-half','F04C-L0078-base-under50','F04C-L0102-mind-rating','F04C-L0093-state2-map'])
summary(137,'random','随机入口平直、不保证种子重现，重复随机接点原事实。',[1298,2219],['F04C-L0065-AI-random'])
q(137,'forward-limits','评判 UI 是非战斗场景请求；实际记录回放/内容生成/事件/宿主组合的前向保留不推翻本文有限静态接点，也不补成已运行。')
q(141,'owners','WP58 记录回放、WP76 生成模拟，事件接待、宿主媒体插件及 U01–10/WP78→80 保持外部主责；本文有限完成不等于设施整体通过。','DEPENDENCY_NAVIGATION')
summary(141,'static-retention','连续裁判/补位保留与 Palace 表/随机是已读静态事实，运行确认仍为零。',[1391,1380,1381,1259,1298],['F04C-L0101-consecutive','F04C-L0065-AI-random'])

formal_lines = (B8/FORMAL).read_text().splitlines()
locators = json.loads((HERE/'f04-locator-input.exact.json').read_text())
expected_lines = {x['line'] for x in locators}
assert set(rows) == expected_lines, (set(rows)-expected_lines,expected_lines-set(rows))
assert len(locators) == 84
all_children = [x for line in sorted(rows) for x in rows[line]]
child_index = {x['id']:x for x in all_children}
for c in all_children:
    assert all(s in index for s in c['source_fact_ids']), c
    assert all(s in child_index for s in c['alias_of']), c
    c['status'] = 'FINITE_STATIC_SUPPORTED' if c['source_fact_ids'] or c['direct_source_units'] else 'EXPLICIT_NON_SOURCE_BEHAVIOR_DISPOSITION'

unit_defs = [
('PALACE-FULL','Data/Scripts/011_Battle/008_Other battle types/003_BattlePalaceBattle.rb',1,245,'FULL_FILE_ACTUAL_READ'),
('ARENA-FULL','Data/Scripts/011_Battle/008_Other battle types/004_BattleArenaBattle.rb',1,366,'FULL_FILE_ACTUAL_READ'),
('COMMAND-FULL','Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb',1,265,'FULL_FILE_ACTUAL_READ'),
('USEMOVE-154-578','Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',154,578,'COMPLETE_NAMED_METHOD_ACTUAL_READ'),
('ORDINARY-CHOOSING-5-95','Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb',5,95,'COMPLETE_NAMED_METHODS_ACTUAL_READ'),
('BATTLER-CHOOSING-10-100','Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb',10,100,'COMPLETE_NAMED_METHOD_ACTUAL_READ'),
('TRYUSE-183-297','Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb',183,297,'COMPLETE_NAMED_METHOD_ACTUAL_READ'),
('TARGETCHECK-303-526','Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb',303,526,'COMPLETE_NAMED_METHOD_ACTUAL_READ'),
('CANCEL-80-95','Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',80,95,'COMPLETE_NAMED_METHOD_ACTUAL_READ'),
('ORDINARY-EOR-597-780','Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',597,780,'COMPLETE_NAMED_METHOD_ACTUAL_READ'),
('ALLBATTLERS-448-450','Data/Scripts/011_Battle/001_Battle/001_Battle.rb',448,450,'COMPLETE_NAMED_METHOD_ACTUAL_READ'),
('BATTLER-HP-107-112','Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',107,112,'COMPLETE_NAMED_METHODS_ACTUAL_READ'),
('POKEMON-HP-246-250','Data/Scripts/014_Pokemon/001_Pokemon.rb',246,250,'COMPLETE_NAMED_METHOD_ACTUAL_READ'),
('ATTACK-176-201','Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb',176,201,'COMPLETE_NAMED_METHOD_ACTUAL_READ'),
('RECHARGE-EFFECT-185-190','Data/Scripts/011_Battle/003_Move/009_MoveEffects_MultiHit.rb',185,190,'COMPLETE_NAMED_EFFECT_CLASS_ACTUAL_READ')]
unit_records = []
for uid,path,start,end,scope in unit_defs:
    raw = (R/path).read_bytes(); lines = raw.splitlines(keepends=True)
    unit_records.append({'id':uid,'source_identity':ident(R/path,R,FIXED_R),'range':[start,end],
        'unit_bytes':sum(map(len,lines[start-1:end])),'unit_sha256':sha(b''.join(lines[start-1:end])),
        'actual_reader':READER,'reading_scope':scope,'source_body_not_copied':True})

source_refs = {x['id']:{'fact_object_sha256':objsha(x),'source':x['source'],
    'source_identity':source_identities[x['source']], 'unit_locator':x['unit_locator'],
    'original_reader':x['reader'], 'actual_finite_receiver':READER,
    'object_location': ('received-sourcefacts.factored.json#common_fields+facts[id='+x['id']+']' if x['id'] in {z['id'] for z in base['facts']} else 'received-sourcefacts.additional.json#facts[id='+x['id']+']')}
    for x in facts}

scope = {
 'fixed_B8':FIXED_B8,'fixed_R':FIXED_R,'reader':READER,
 'original_primary_reader':'/root/facility_atomic_completion_cloud',
 'shared_premise':'Fixed current R/B8 default definitions and load order, no later override; actual objects, registered data, numerics, indices and scene/callback dependencies satisfy each explicitly stated normal prefix. Existing producer premises, errors, pending dependency qualifications and execution limits are retained unchanged in exact received objects. Normal default move capacity is four. No universal malformed-data validation, arbitrary callback success, rollback or plugin equivalence follows.',
 'meaning_of_completion':'All meanings of this one current F04 file, including all 84 supplied paragraph/table locators, have explicit finite dispositions. This is no all-FAC task final, global PASS, PA32 re-audit or normalized whole-system atom denominator.',
 'source_read_credit':'R03/R04 and named listed source units actually read here. Other full-file/source credit belongs to original named readers. Complete finite producer objects were actually received with all fields/common premises/limits, without inheriting producer FULL.',
 'failure_prefixes':[
  'Palace Pinch writes true before display; a display error preserves that flag. AutoFight returns true only after selection/registration returns normally.',
  'Probability best-candidate early return skips history assignment; fallthrough writes history before fallback and a failure/absence can leave it changed.',
  'Arena opening scene must return before changed=false/count0. Ordinary command/EOR nonzero decision skips later variant work.',
  'Execution/PP early return precedes useState1; whole-move failure after state1 can skip updateSkill. Later living common tail versus no later tail are separate outcomes. Fainted slots do not receive tail scoring.',
  'Judgment scene precedes HP submission; partial tie/faint callback failure can preserve the first HP0 while skipping the second/EXP/replacement. No transaction or unconditional cleanup is asserted.',
  'Direct HP write-through proves current attached Pokemon mutation; save/reload, facility restoration and callback outcomes retain separate contracts.',
  'Actual scene operations, resource success, frame timings, native graphics/audio and all arbitrary faint/entry/status/item/ability callbacks remain unexecuted.'
 ],
 'mandatory_qualifications':[
  'FIP-F05 is the corrected complete stats producer, not the superseded FIP-F04 locator. P28 constant HP facts are reused only as the already received finite FAC-A2232 derivation, not a new stats or species proof.',
  'F054 straightening is animation, not direction; prior mandatory audio-caller corrections remain intact. This packet makes no new audio or direction claim.',
  'The CORE CAR-FAC-BIND-02 numHits>0 phrase is sufficient, not iff: own complete UseMove reading confirms state2 follows normal branch completion even if the hit loop iterates zero times.',
  'Ordinary Entry calls Participated, not the Arena AsActive reset; arbitrary external calls to the defined reset are not excluded.',
  'Internal helper names/data slots are evidence locators, not mandatory future public APIs or new tests.'
 ],
 'new_source_meanings':0,'new_source_assertion_ids':[],
 'new_required':0,'new_optional':0,'new_independent_counterexample_votes':0,
 'business_execution':{'Ruby':0,'game':0,'native':0,'compiler':0,'eligibility_predicate':0,'trait_graph':0,'behavior_model':0},
 'not_executed':['real save/reload','real record/playback','host UI/media','complete game/Demo'],
 'UPDATE_NOT_STARTED':True}

packet = {'schema':'gr8-f04-complete-finite-canonical-meaning-dispositions/v1', **scope,
 'formal_identity':ident(B8/FORMAL,B8,FIXED_B8),
 'locator_semantics':'84 is an original locator count, not a behavior/source-atom denominator. Child membership was manually authored after full reading. Counts only describe this finite packet.',
 'dispositions':[{'old_locator_id':f'F04-L{line:04d}','line':line,'complete_current_text':formal_lines[line-1],
    'children':rows[line],'unhandled_meanings':[],'status':'COMPLETE_FINITE_MEANING_DISPOSITION'} for line in sorted(rows)],
 'source_fact_references':source_refs,
 'source_unit_references':unit_records,
 'case_child_references':{x['id']:{'object_sha256':objsha(x),'container':'received-PA29-30.finite-children.json','case':x['case']} for x in pa_selected},
 'layout_disposition':{'headings':[1,7,15,17,25,57,61,72,83,85,98,105,113,129,133,139],
    'table_separators':[30,116], 'blank_lines':'All blank lines read in full formal 1–141; no source-behavior assertion.',
    'note':'All nonblank nonheading/nonseparator material is included among the 84 exact locator dispositions.'},
 'counts':{'original_locators':len(rows),'manually_authored_children':len(all_children),
    'behavior_children':sum(x['kind']=='BEHAVIOR' for x in all_children),
    'summary_reference_children':sum(x['kind']=='SUMMARY_REFERENCE' for x in all_children),
    'other_explicit_dispositions':sum(x['kind'] not in ['BEHAVIOR','SUMMARY_REFERENCE'] for x in all_children),
    'received_sourcefacts':len(facts),'received_existing_case_children':len(pa_selected),
    'unhandled_F04_meanings':0,'parent_final_reception':'PENDING_ACTUAL_READING'}}
save('f04-complete-canonical-packet.v1.json',packet)

reverse = []
for fid,ref in source_refs.items():
    consumers = [c['id'] for c in all_children if fid in c['source_fact_ids']]
    reverse.append({'source_fact_id':fid,**ref,'canonical_child_consumers':consumers,
        'disposition':'EXPLICIT_F04_CHILD_JOIN' if consumers else 'FINITE_RECEIVED_COLLATERAL_SOURCE_AUDIT_ONLY_NO_ADDED_FORMAL_REQUIREMENT'})
save('forward-mapping.json',{'schema':'gr8-f04-fact-to-canonical-child-joins/v1','reader':READER,
    'source_fact_to_children':reverse,'qualification':'No parent forward/reverse file was changed. Unused selected source facts remain finite audit detail, not mandatory future behavior.'})
save('reverse-mapping.json',{'schema':'gr8-f04-canonical-child-to-fact-joins/v1','reader':READER,
    'canonical_child_to_source':[{**c,'source_references':[source_refs[fid] for fid in c['source_fact_ids']]} for c in all_children],
    'qualification':'Every child points to complete exact finite source objects or an explicit non-source-behavior disposition; source code bodies are not replicated.'})

inputs = ['inputs/eighth-global-review-prompt.md','inputs/review-SKILL.md',
    'delegation/prompts/facility_atomic_completion_cloud.md','delegation/readsets/facility_atomic_completion_cloud.complete.json']
save('identities.json',{'schema':'gr8-f04-identities/v1','reader':READER,
    'fixed_B8':FIXED_B8,'fixed_R':FIXED_R,'formal':packet['formal_identity'],
    'instructions':[ident(RR/x) for x in inputs], 'AGENTS':ident(B8/'AGENTS.md',B8,FIXED_B8),
    'received_sourcefact_containers':[base['producer_container'],extra_capsule['producer_container']],
    'received_case_container':{'path':str(pa_path),'bytes':len(pa_raw),'sha256':sha(pa_raw)},
    'source_unit_identities':unit_records,
    'runtime_configuration':{'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default普速','Fast':'off'},
       'actual':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','opaque_platform_session_id']},
       'logical_task_id':READER,'authority':'No authoritative model/effort/tier/speed/Fast/session echo was available; logical collaboration task path is not opaque platform identity.'},
    'identity_scope':'Exact B8/R fixed objects and actual named file bytes only. No remote/main/full-worktree audit performed by this child; parent owns full FAC/startup/publication.'})

save('reading-ledger.json',{'schema':'gr8-f04-actual-reading-ledger/v1','reader':READER,
    'instructions_full_read':inputs+['/workspace/pokemon-essentials-clean-room/AGENTS.md'],
    'formal_full_actual_read':{'path':FORMAL,'range':[1,141],'bytes':19053,'sha256':'fee7a028ad9b1db8fae48145b092b18efc89757db943eb6e3f234ace7c111368'},
    'actual_source_units':unit_records,
    'actual_complete_finite_object_reception':{'sourcefacts':list(index),'case_children':[x['id'] for x in pa_selected],
      'sourcefact_reading_view':'received-sourcefacts.lossless-reading-view.json plus received-sourcefacts.additional.json',
      'lossless_method':'common_fields and per-row shared_fieldset reconstruct every selected original fact field; every fieldset and every row was actually displayed and read. Exact canonical object SHA is retained.',
      'original_reader':'/root/facility_atomic_completion_cloud',
      'not_inherited':['parent all22R/8F FULL','old com_facility FULL','PA32 full89 children','all CORE/PBS/source files']},
    'limited_other_context_read':{'ordinary-status-boundary.v2.json':'Full local packet displayed while locating ordinary selection gates; not adopted as an F04 status/ability denominator closure.',
       'core-terminal-packet':'Complete facts/qualifications displayed for context. No adoption of all five facts/all18 units or whole CORE; own listed units and parent exact sourcefacts govern this packet.'},
    'failed_or_truncated_reads':[
      {'receipt':'initial exec_command','result':'exec-server transport disconnected; zero reading credit; later login:false read normally'},
      {'receipt':'819888','result':'Initial combined instruction output truncated; no full-read credit; prompt1–120/121–241, skill/prompt whole, readset1–280/281–560/561–840/841–1130 subsequently fully displayed'},
      {'receipt':'locator/fact discovery output','result':'Truncated discovery was not adopted as complete reading; exact complete objects subsequently losslessly factored and displayed in 1091–1240/1241–1316/1317+ groups'},
      {'receipt':'first source identity schema read','result':'Python slice KeyError; zero credit, corrected dict read'},
      {'receipt':'ordinary action filename search','result':'One wrong filename missing; corrected by rg --files; complete actual named units subsequently read'}],
    'semantic_review':'Manual comparison of every meaning, fields, order, state, error prefix, display/persistent object and execution boundary. Serialization scripts only enumerate, hash and verify references; no rule predicate/graph/game/model executed.',
    'remaining_reading_within_this_F04_contract':[]})

save('interfaces.json',{'schema':'gr8-f04-finite-interfaces/v1','reader':READER,
    'current_received_finite_scope':[
      'Palace/Arena current full local source and 84 canonical locators with complete meaning dispositions',
      'Normal player Fight→ordinary auto or Palace auto→target execution, and AI switch/item/auto-before-Mega finite joins',
      'SuccessState full clear/production/common living tail versus early return; actual Protect/no-target reflection finite already accepted meanings',
      'Arena CancelMoves/ordinary recharge lifecycle/direct attached Pokemon HP write; actual replacement not AsActive',
      'Mode constructor, layout installation, recording/playback class behavior ownership; no native replay equivalence'],
    'current_remaining':['Parent actual finite reception of this new canonical join packet','All other FAC files/full task final remain parent-owned','Runtime/host/save/replay boundaries remain NOT_EXECUTED'],
    'new_required':0,'new_source_meanings':0,'whole_FAC_complete':False,'UPDATE_NOT_STARTED':True})
save('proposals.json',{'schema':'gr8-f04-proposals/v1','reader':READER,'proposals':[],
    'reason':'No new source/formal discrepancy was found after the specified complete finite F04 comparison. Existing precise qualifications and old independent finding ownership were preserved. This is not a global NO_REQUIRED_UPDATE conclusion.',
    'new_required':0,'new_optional':0,'new_source_meanings':0,'UPDATE_NOT_STARTED':True})
save('progress.json',{'schema':'gr8-f04-finite-progress/v1','reader':READER,'status':'COMPLETE_FINITE_F04_AWAITING_PARENT_ACTUAL_RECEPTION',
    'counts':packet['counts'],'blocking_materials':[],'whole_FAC_complete':False,
    'write_set':str(HERE),'no_other_task_metadata_written':True,'new_source_meanings':0,
    'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})

save('validation.json',{'schema':'gr8-f04-mechanical-integrity/v1',
    'checks':{'exact_84_locator_set':set(rows)==expected_lines,'all_fact_joins_resolve':True,
       'all_alias_joins_resolve':True,'all_formal_source_units_match_fixed_bytes':all(u['source_identity']['actual_matches_fixed_bytes'] for u in unit_records),
       'formal_matches_fixed_B8':packet['formal_identity']['actual_matches_fixed_bytes'],
       'new_R_source_atoms':0,'parent_files_modified_by_this_child':0,'behavior_executions':0},
    'qualification':'Integrity checks validate file identity, complete finite locator membership and join referential integrity only; they do not grant semantic PASS or behavior execution credit.',
    'semantic_status':'The named actual reader manually closed the meanings in this single F04 finite packet; parent must read and receive the new joins.',
    'UPDATE_NOT_STARTED':True})
save('next-dispatch.json',{'schema':'gr8-f04-finite-parent-reception/v1','reader':READER,
    'parent_next_step':'Actually read the complete F04 packet dispositions/shared qualifications and join deltas; original parent sourcefact objects remain the stable already-read basis. No new source body reception is required by this packet.',
    'unmet_F04_meanings':[],'true_material_blockers':[],
    'not_a_new_approval_layer':True,'whole_FAC_complete':False,'UPDATE_NOT_STARTED':True})

review = f'''F04 的当前全文（141 行、19,053 bytes）以及 84 个原段落/表格定位已逐意义完成有限处置。主包 `f04-complete-canonical-packet.v1.json` 含 {len(all_children)} 个手工编写的 child（其中 {packet['counts']['behavior_children']} 个行为 child、{packet['counts']['summary_reference_children']} 个重复引用，其余为范围/来源/表头等明确处置）。84 是 locator 数，child 数仅是本有限包的成员计数，二者都不是全 FAC 或全局行为原子分母。

本子 context 实际全文读取 R03 Palace 245 行、R04 Arena 366 行、F04 全文，并读取 ledger 所列必要完整源单位。完整接收 {len(facts)} 个父已冻结 sourcefact 全字段对象及现有 P29/P30 的 {len(pa_selected)} 个完整有限 child；共享前提/失败/执行资格和 source/unit/object SHA 均可恢复。原 source FULL 信用保留给原 reader，不继承父 22R/8F、旧 COM、全 PA32 或 CORE 全域阅读。

未发现新行为缺义或新差异；新增源原子 0，required/optional 提案均 0。新增内容是 canonical meaning→已验事实及反向 consumer join。性格表逐字段绑定；重复摘要指回同一已验事实，不复制已验 sourcebody。模式/布局配置不冒充实际 PBS 资格；内部 helper 名称不成为未来 API/测试要求。

保留的关键前提是：玩家普通菜单门先于 Palace 抽样；两条通常出招路径在 Mega 登记之前返回；Arena 状态 2 为目标分支完成而非命中保证；正常 common tail 仅结算当时存活者；实际 Entry 的 Participated≠AsActive；裁判取消保留胜者回复期；HP0 写穿当前 Pokemon，不能升级为磁盘保存/原生运行成功。FIP-F05 修正、F054 动画及已接受 audio 资格保持，未重新审核其旧全集。

工具仅用于读取、序列化、身份和 join 完整性；Ruby/game/native/compiler/资格谓词/trait图/行为模型执行全部 0。请求 gpt-6.1-sol/ultra/default 普速/Fast off；actual model、effort、tier、speed、Fast、opaque platform ID 各为 UNVERIFIED。逻辑 task 为 `{READER}`。

本包无真正材料阻塞，父 context 的实际接收待完成；其余 FAC 全合同与全局裁决仍由父负责。唯一写集为本目录，正式正文、源、main、父 v2、旧证据均未由本子修改。UPDATE_NOT_STARTED。
'''
(HERE/'review.md').write_text(review)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
manifest = {'schema':'gr8-f04-local-packet-publication/v1','frozen_utc':now,'reader':READER,
    'fixed_B8':FIXED_B8,'fixed_R':FIXED_R,'files':[ident(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='artifact-manifest.json'],
    'qualification':'Local frozen packet only; no commit/push/install or remote publication by this child. Preserve these exact bytes; corrections require companions.',
    'UPDATE_NOT_STARTED':True}
save('artifact-manifest.json',manifest)
print(json.dumps({'files':len(manifest['files']),'counts':packet['counts'],
    'packet_identity':ident(HERE/'f04-complete-canonical-packet.v1.json'),
    'manifest_identity':ident(HERE/'artifact-manifest.json')},ensure_ascii=False))
