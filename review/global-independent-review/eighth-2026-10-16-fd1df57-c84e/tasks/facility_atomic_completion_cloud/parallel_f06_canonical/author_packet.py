import json,hashlib,datetime,subprocess
from pathlib import Path
rr=Path.cwd(); p=rr/'tasks/facility_atomic_completion_cloud/parallel_f06_canonical'; v=rr/'tasks/facility_atomic_completion_cloud/v2'; R=Path('/workspace/pokemon-essentials'); B=Path('/workspace/pokemon-essentials-clean-room')
fixedR='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';fixedB='fd1df570cad987dc3852a3b958f03916e317f7fe';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(f,root=rr,commit=None):
 b=f.read_bytes();d={'path':str(f.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 if commit:d|={'commit':commit,'blob':subprocess.check_output(['git','-C',str(root),'rev-parse',commit+':'+d['path']],text=True).strip()}
 return d
def dump(name,x): (p/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
premise='Fixed R/B8; normal default loader and named registrations have run successfully, no later plugins/override or unrelated callback mutation; valid typed objects and normally returning dependencies to each stated observation except named failure prefixes. Random uniformity is conditional on legal ordinary positive integer offsets. Source instructions and live object association are distinct from native outputs, rendering, actual serialization/reload and Demo composition. No game, model, Ruby, compiler, graph or native execution.'
new=[
('F06-S001','Data/Scripts/018_Alternate battle modes/002_BugContest.rb','pbStart171–196','Start first copies budget/activity/spares reset/stock reset/lastContest reset/uptime/places, then reads selected member and records spares. It clears contestants and completes duplicate-rejection opponent sampling BEFORE replacing player party with the selected singleton, resetting decision/ended and incrementing count. A failure during sampling preserves original current party while leaving earlier live fields/spares/partial contestants.','Necessary exact sequence; existing FAC-A0316–26 received, no novel primary business value.'),
('F06-S002','Data/Scripts/012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb','complete four on_wild_pokemon_created callbacks9–60','Default registration order is shiny-switch, Safari/Contest IV reroll, flagged-species perfect-IV guarantee, map-flag level scaling. Reroll declines only when both mode queries are false. Up to four iterations first check whether any current IV equals IV_STAT_LIMIT; absent a perfect IV, each main stat rerandomizes in that iteration. calc_stats runs afterward only if at least one reroll occurred. Existing perfect IV skips rerolls. Later guarantee requires configured enable flag and Legendary/Mythical/UltraBeast effective data flag, samples three main stats and writes their IV maximum then recalculates. Scaling requires ScaleWildEncounterLevels and changes clamped level, recalculates stats and resets moves. These are conditional notification consumers, bypassed by direct NPC constructor.','No whole species registry, native sample distribution or animation proof.'),
('F06-S003','PBS/map_metadata.txt','complete records028–030 lines128–145 and067–068 lines341–352','Map028 Natural Park is outdoor and has MossRock,BugContest flags. Maps029 and030 have BugContestReception flags. Map067 Safari gate has no SafariMap field; map068 is outdoor, SafariMap=true, backdrop forest, Environment Forest. Gate membership still depends on saved origin, not its label.','Literal records only; no actual map/event resource or Demo reachability.'),
('F06-S004','PBS/items.txt','complete SAFARIBALL3839–3846 and SPORTBALL3848–3855 records','Safari Ball: pocket3, price0, BattleUse OnFoe, PokeBall flag; Sport Ball: pocket3, price300, BattleUse OnFoe, PokeBall flag. Names/plurals/descriptions are literal labels. Mode budgets come from Start arguments, not these prices or bag counts.','Identity/record body only; rate behavior separately FAC-A1655–60.'),
('F06-S005','Data/Scripts/001_Settings.rb','complete declarations17,88,90,140','Default mechanics generation8; Safari step budget600; Contest time20×60=1200 seconds; flagged-species three-perfect-IV setting evaluates true for generation8. Safari Start reads its current setting; Contest captures TIME_ALLOWED at class definition (FAC-A2308).','Configuration values at consumption time; dynamic mutation does not retroactively alter captured constant.'),
('F06-S006','Data/Scripts/002_BattleSettings.rb','complete declaration92 and preceding configuration comment','Critical captures enabled when mechanics generation>=5, therefore enabled by fixed generation8. Actual critical entry additionally depends on computed modifier/positive threshold; zero threshold skips entry draw.','Source default declaration, not capture rate observation.'),
('F06-S007','Data/Scripts/012_Overworld/001_Overworld visuals/003_Overworld_MapTransitionAnims.rb','complete pbStartOver80–139','Blackout entry checks active BugContest first, calls ContestStartOver and returns before ordinary blackout statistic/heal/center-or-home route. The mode helper heal/unmega/unprimal/judging facts remain FAC-A2302/2310.','Only finite diversion accepted; ordinary blackout domain is not re-audited or adopted.'),
('F06-S008','Data/Scripts/013_Items/005_Item_PokeRadar.rb','complete pbCanUsePokeRadar18–44 and Game_Temp11–13','Radar permission checks grass-capable terrain, normal-land encounter table, bicycle, then debug-Control bypass, then positive battery. It contains no Safari/Contest query. Radar data is an ordinary Game_Temp accessor, distinct from saved global battery.','Static gate request only; user-facing resources and actual input are unexecuted.'),
('F06-S009','Data/Scripts/012_Overworld/001_Overworld.rb','complete relevant registrations5–16,47–65,83–113,279–316','Fixed default file registers virus, low-battery and delayed BGM callbacks on frame update; poison-party on transfer-capable step; darkness then location-window on map/spriteset changes. Given received sorted loader and normal standard dispatcher, these registrations precede later 018 Safari/Contest registrations. This states relative order of named callbacks, not an exclusive complete event chain. Poison checks handled before work and can set it true before failure-return handling; callbacks can interrupt later dispatch on exception.','Only relevant complete callback units actually read; no whole world domain approval.'),
('F06-S010','Data/Scripts/012_Overworld/002_Battle triggering/005_Overworld_RoamingPokemon.rb','complete on_enter_map registration93–105','Roaming enter-map callback can skip same-name maps; otherwise calls roam movement and resets roamedAlready. Its default registration precedes Radar enter cancellation and later Safari/Contest enter callbacks under received loader premises.','Relative registration order, not proof every callback produces movement or actual transfer.')]
newfacts=[]
for id,path,unit,meaning,qual in new:
 newfacts.append({'id':id,'source':ident(R/path,R,fixedR),'complete_unit':unit,'meaning':meaning,'premise':premise,'qualification':qual,'reader':'/root/facility_atomic_completion_cloud/f06_canonical_tail','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED'})
dump('necessary-new-meanings.json',{'utc':now,'common_premise':premise,'facts':newfacts,'new_primary_business_values':0,'new_source_fact_ids':'Child namespace only; no parent FAC-A allocation.'})
# Each row is manually authored. Semicolon separates independent meaning components; refs are the complete finite source support set shared by that row, not a mechanical assertion of entailment.
rows='''
3|分类为规则/生物会话/战斗/世界/界面;本合同描述会话动作结果结算入口;证据为静态且未运行|scope
7|六个范围分别为Safari会话世界、单战、捕虫会话时间、捕虫战斗保留、判分结算、公共UI保存Demo|scope
9|普通捕获常规战斗遭遇钓鱼华丽大赛由各primary负责;费用日期奖励接待话术事件必须有Demo证据;脚本入口不证明默认调用|scope
11|保留GR011/013与当前WP37资格的引用范围;不为所有覆盖结果设统一布尔;历史接受不授本次全文信用|history,A0296,A2304,A2321
15|Safari起点四元组、球数捕获数步数决定活动标记属于全局对象;开始写起点结束清空;持久对象不等于已落盘;专门Save与Quit保存有不同门|A0242-59,A0358-67,A0406-17
16|活动会话接待图与SafariMap旗标图并集;接待图按保存起点而非室内外或草丛决定|A0262-64,F06-S003
17|捕虫预算决定保留个体计时起点结束/活动标记;备用队伍NPC下标名次判奖点比赛图接待图选员下标上次墙钟均是会话字段|A0297-310,A0316-36,A2301-11
18|单调起点用于到期;墙钟用于24小时;保存后的单调时钟解释未证|A0304-8,A0318,A0335,A2308
19|比赛图与接待图并集内允许;显式ID或旗标配置累加|A0356,F06-S011
20|已有非nil handled阻止后续覆盖;默认相对注册序漫游Safari捕虫|A0279-80,A2326,A2328-30
21|活动且决定0为未判;活动非0决定或ended为已判;结束变inactive;结束后离判奖图才清理|A0297-310,A0327-36,A0357
27|首次对象起点nil预算捕获步数决定0活动false;进行中与结果待处理区分;结束清字段并刷新|A0242-59,A0290
28|开始覆盖当前图坐标方向预算活动与配置步数;不重置捕获或决定;重复Start保留旧值;非0决定屏蔽计步;Demo正常接待编排未证|A0248-53,A0269,scope
29|结束清起点预算捕获步数决定活动并刷新;无活动前置;普通无活动换图可惰性创建再清空;事件实际编排另域|A0256-65
30|回起点仅转移不End;接待图仍属于活动区域;结果待处理可继续存在|A0263,A0275-8,A0290
34|区域查询先要求活动;接待图或SafariMap任一满足;inactive恒false|A0262-64
35|换图只按区域查询否即End无活动门;无活动也惰性创建清空;活动区域内不动;活动离区清空;步尽球尽退出先决定1回起点|A0260-5,A0273,A0290,A0451
39|一步结束/冲浪步进路径到转移钩子;真handled使当步普通遭遇不再执行|A2290,F06-S009
40|已有truthy handled先跳过;设置恰0跳过;区域外跳过;非0决定跳过|A0266-9
41|合格一步先减;正值直接返回;非正两消息后决定1回起点后handledtrue;故跳过当步遭遇|A0270-4,A2290
42|默认600;配置0禁计步;负配置不是0门并在首个合格步归结束|A0251,A0267,A0270-1,F06-S005
46|仅地图场景回起点;淡出请求保存图xy且向下;下车后转移;非地图跳过但已写决定不回滚;不清会话|A0275-8
47|地图场景缺起点在字段读取失败;正常开始先写起点;非地图不读起点也不转移|A0248,A0275-8,F06-S012
53|公开入口要求单敌候选且允许覆盖;非nil handled或Safari区域外不接管;漫游前置满足会先处理|A0279-80,A2321,A2328-30
54|个体实参直接复用;物种等级走野生生成及创建修饰通知;Safari不走跳战检查或start通知|A0281-2,A0286,A2325,F06-S002
55|场景和Safari对象构造后会话预算复制进战斗;准备环境天气背景时间后动画开战;天气setter与初轮末动画分别;不走普通start/skip/善后/通用结果;规则未由核心清理|A0283-7,A1578-96,A1617-8,A1634,A2323,F06-S013
59|伪对象指向唯一敌个体;fainted恒false影子Mega原始谓词false;捕获标记读false写空操作;owned查询实时全局图鉴|A1533-47,A1568-77
60|Safari独立流程无玩家参战队伍;无普通招式背包换人经验金钱装备结算;野生true训练家false;经验入口空操作|A1566,A1598,A1601,A1605,A1608-9
61|构造未设internalBattle;seen/caught入口各在falsey门返回;Mixin独立owned写仍可发生|A1593,A1603-4,A1678
65|捕获率常规0至255为数学输入域;数据取有效物种属性|A1612-23
67|整数先乘100除1275;捕获因子钳3至20|A1619
68|逃跑基准依次<=45取125、<=60取100、<=120取75、<=250取50、其余25;阈值归较早分段|A1612-6
69|逃跑基准先乘100整数除1275再钳2至20|A1620
70|已识别动作后钳捕获3至20逃跑2至20;发生在未决回合末分支前|A1630-1
71|投球输入为捕获因子乘1275整数除100;因子3和20分别得38和255;不同于直接物种率|A1623
75|专用菜单四命令Ball/Bait/Rock/Run|A1561
77|表头分许可反馈状态消耗后续次序;列名为排版无独立运行断言|layout
79|联合队伍满且箱满时消息并重选无球耗回合随机;通过先扣球刷新再固定Safari球投掷;实际球种和Ultra前门决定折减或普通1.5;HP状态确定捕获暴击或短路四摇共享合同;成功记录存储后core4|A1621-5,A1654-67,A1674-81,F06-S004,F06-S006
80|Bait先反馈动画;随机100<90时整数减半捕获因子;逃跑因子总减半;正常随后回合末|A1626,A1630-4
81|Rock先反馈动画;捕获因子总翻倍;随机100<90时逃跑因子翻倍;随后回合末|A1627,A1630-4
82|Run先逃离音效安全消息;写core3并退出循环;无逃跑概率门|A1628,A1635
83|取消无效直接重选;不扣球不达钳制预算判断逃跑随机|A1629
85|只在最初core0回合分支处理;动作后已钳制;球<=0优先core2;否则严格随机100<5Fe逃跑core3;否则动作消息;天气动画在该分支尾仍可到达|A1630-5
86|专用中止异常被救援;core重写0并结束场景;此前扣球和注册不回滚;剩余预算回写并可触发外层球尽|A1622,A1625,A1636-7,A0287-90
90|Safari seen/caught因内部标记不登记;Mixin未owned写拥有再按图鉴解锁门显示;昵称和普通存储继之;送盒询问字段未设故不出现替队菜单;无Safari经验金钱或内部seen保证|A1593,A1595,A1603-9,A1677-81,A2345-51,F06-S014
94|以下列项规定Safari正常返回后的顺序;前缀异常可阻断后项|A0287-96
96|会话预算从战斗剩余复制回;中止后扣球保留;未消耗时值相同|A0287,A1622,A1636
97|外层预算<=0时core非2才播会话球尽;core2仅抑重复消息;均决定1回起点;最后捕获core4走有消息分支|A0288-90
98|仅core4先总Safari捕获+1再局部捕获+1再最大记录取大|A0291-3,STATS01
99|变量1写core编号;0中止未决、2球尽、3玩家或野逃、4捕获|A0294,A1624,A1628,A1631-2,A1636
100|野生结束通知传物种等级core;位于会话统计变量及球尽转移后;雷达消费者看到的是该时点状态|A0295,A2332-4
101|外层返回core整数;公开覆盖保留非nil整数;漫游和捕虫布尔各按独立包装|A0296,A2304,A2321,A2330
105|分支表按核心预算会话决定消息变量返回分列;表头为布局|layout
107|末球捕获core4预算0会话1回起点;有捕获及会话球尽消息;变量和返回4|SF08
108|末球失败core2预算0会话1回起点;战斗球尽消息外层抑重复;变量返回2|SF08
109|正预算且旧会话决定0时Run core3;会话继续;变量返回3和安全消息|SF10
110|正预算旧会话决定0时野逃core3;会话继续;变量返回3和野逃消息|SF10
111|中止core0实际预算保留;正预算且旧决定0继续;预算0外层消息决定1回起点;变量返回仍0|SF10,SF33
112|任意非专用中止错误不承诺字段或场景自动恢复;具体前缀按实际达到点|A1637,A0445,A1625
118|清理清会话活动预算决定保留备用对手名次判奖点图集;不重置lastContest选员下标timer;构造另将lastContestnil;End保留判奖查询字段|A0297-303,A0333-6,A0357
119|选员setter无校验;比赛/接待图按ID或旗标累加;判奖点方向默认8;对手下标查询为事件接口|F06-S011
120|先写预算活动备用清空保留清空lastContest清空单调起点名次清空;选中成员与备用保留原引用和顺序无治疗;成功尾是选中单员、5个不同NPC下标、决定0endedfalse及计数+1;源实际NPC采样先于party替换，正文次序待裁|A0316-26,F06-S001,STATS03
121|nil下标在读选员处失败已写起始前缀但未缩队采样;正越界nil可正常采样后party[nil]并计数;合法下标正常;负下标选尾但spares按非负位置排除失败从而End重复同对象|A0316-26,A0328,SF31
125|inactive End早退;先拼备用不治不回原顺序;中断跳过保留存储并endedfalse，正常容量检查后昵称存储再endedtrue;首名计wins，空名次可在拼队后失败;再清活动预算等写墙钟刷新;选员判奖点NPC名次保留|A0327-36,A2294-300,SF14,SF15,SF16,STATS04
126|拼队存储统计清理是顺序副作用;异常保留已完成写入;非事务回滚|A0328-36,A2294-300,STATS04
130|默认限时1200秒;开始记录单调时钟起点;class TIME_ALLOWED捕获与debug当前配置分开|A0318,A2308,F06-S005
131|active未决才检查;捕获时限<=0永不到期;正限时elapsed>=limit到期|A0306-8,A2308
132|移动路线解释器消息窗各延期;通过两消息后判奖;正常非淡出pause命令loop可微更新派frame无in_menu门;因此可菜单未关就判奖;不泛化全部UI战斗或实际窗口形态|A2288,A2306-10,SF17
133|active未决且captured limit!=0才创建timer;0无timer;负时限可建而显示下界00:00且不expired;分钟秒显示只在整数变化刷新|A0350-3,A2311,SF18
134|无lastContest返回false;有则墙钟差<86400;Start自身不查故仅事件限频依据|A0304-5,A0316-26
135|存入计时起点不证明重载后单调时钟解释;静态与重载分开|A2308,A0373
139|StartJudging先决定1再判分;地图场景淡出设判奖图xy方向下车转移并请求刷新含同图;非地图仅跳转移|A0347-9,A2310,F06-S015
140|ContestStartOver当前队伍heal/unmega/unprimal再判奖;公共StartOver在捕虫活动门转此而不走中心|A2302,A2310,F06-S007
141|判奖点nil仅地图场景转移读取失败;决定和成功名次已经写入|A0347-9,F06-S015
145|目标在比赛或接待图任一为允许;其它越界|F06-S011
146|离图仅active且越界End(true);跳保留存储;未判时拼队后place读失败并留活动字段|A0356,A0328-32,SF16
147|进入图只要求inactive且无判奖点或不在判奖图就clear;未曾开始也可;保留墙钟选员timer;24h仍按原时间|A0357,A0303-5,SF32
153|公开包装先单敌允许门;随后handled nil且active Contest;注册在漫游Safari后|A2321,A2326,A2328
154|force-single与Safari拒绝先于partner真门再单可战假门;活捕虫单员不足保证接管;给定伙伴双敌走普通2v2且不复制预算K或菜单;普通善后治疗两队并双敌无public单敌通知;取消伙伴或force-single可使单敌覆盖;Demo实际组合未证|A2319-26,A2291,SF35
155|Contest直接入口先start通知再可选生成;普通Battle子类/内部标记真/玩家party和单敌;起始0、复制预算、强制single后prepare;动画内普通开战再after_battle(true);core2/5恢复音乐并模式治疗判奖|A2301-2,A1641-2,A1684-5,F06-S016
156|模式包装不做skip检查;未经普通核心clear_rules不保证规则清理|A2301-4,A2323,F06-S016
160|命令Fight/Ball/Pokemon/Run且标题剩余Sport预算;无普通背包选择|A1643-4
161|Ball直接登记Sport1枚;消费覆写只在预算>0减且不碰背包;登记耗预算;普通回流背包不构成预算退款;球行动占全轮归命令primary|A1642-5,F06-S017
162|固定Sport球走公共捕获和记录;Ultra按实际球前置折减跳普通handler;普通Sport1.5;HP状态确定捕获或暴击/四摇;内部true使caught/seen注册;store落模式保留覆写|A1657-78,A1684-9,F06-S004,F06-S006
163|消费仅正预算减;EOR<=0门独立;itemMenu登记无预算检查;人工零负值不改成有校验|A1643,A1645,A1652-3
167|保留覆写不同于party/box最终接收;三分支如下|A1646-50
168|无旧保留则直接保存新对象引用|A1649
169|旧存在先消息再两方名等级HP上限比较然后确认;确认改保留引用，旧移出该槽;拒绝保留旧且无新最终消息;早先捕获记录不回滚;不推断Owner字段改写或所有外部别名被删|A1646-51,A1688-9,SF21
170|首次或确认替换正常落尾捕获成功消息;拒绝提前return不达该消息|A1647-9,SF21
171|捕获保留不同于结束最终接收;party与storage同时满才早退;箱满但party有位可入队|A1650,A2294-9,SF15
175|先普通EOR;仅正常返回且预算<=0并core0改core3;已经core1/2/4/5不覆盖|A1652-3,SF19
179|以下为Contest动画正常返回后的有序尾;异常可阻断后项|A2302-4
181|会话预算复制战斗剩余值|A2303,SF34
182|恰预算0消息后判奖;负值不触发outer equality但EOR<=0独立|A2303,A1652
183|通用set_outcome写变量1;1/4计wildwon，2/3/5计wildlost;其它不计;无回滚|A2293,A2304
184|wildend位于预算0判奖/转移后;雷达消费当前状态|A2304,A2332-4
185|正常返回布尔core非2且非5;0/1/3/4true，2/5false;Safari整数另列|A2304
186|core2/5动画内已判;预算0尾再判;每次追加3所以正常两次6条|A2302-3,A0346,SF20
192|玩家/NPC共用评分;输入等级六IV当前HP上限率;正总HP和合法数据前提|A2305
194|等级项4乘等级|A2305
195|各IV先浮除31求和乘100最后一次floor;六31为600|A2305,SF23
196|HP项浮除后乘100最后floor;正HPmax前提|A2305,SF23
197|稀有基础60，catch<=120加20且<=60再加20;边界100/80/60|A2305,SF23
198|总分为等级IVHP稀有四项;玩家保留和NPC同式|A2305
202|逐比赛图检查BugContest可用，否再Land;有效map/type成候选;全空先异常且决定1已写未转移|A0338-9,A0347,A2317,SF24,SF25
203|每NPC独立采候选map/type;按当前version exact/0fallback选加权物种等级;空候选异常;直接Pokemon.new绕wild通知;正整数HP范围1到totalhp-1均匀为条件分布;不授零界rand或native输出|A0340-3,A2316-8,A2325,SF24
204|正常8名单选5不同NPC;有玩家保留加1即5或6候选;少于3防御仅人工变体|A0322-3,A0337,A0344,SF25,SF26
205|降分排序;无独立tie-break或稳定性保证|A0345,SF26
209|排名前三追加到旧places;条目含参与下标/玩家负1、物种和分数;重复判奖每次另加3|A0337,A0346,SF20,SF26
210|玩家place只扫描前三;见首负下标返位置0/1/2，否则3|A0311-2
211|信息按实参下标直接访问可读追加第四项;越界或空读取失败;依次变量1名2物种名3分;不推Demo实际读第二批|A0313-5,SF26
212|End先拼队保留接收获胜统计清字段墙钟;实际奖励事件由Demo未知|A0328-36,scope
218|default加载与顺序dispatcher下Roam/Safari/Contest相对覆盖序;各只nilhandled;roam全部门过先接管|A2328-30,A0279-80,A2326
219|物种层Roam先Radar;无模式总门;Roam需要全部候选门且BugContest类别排除;Radar非摇草可取消|A2328-9,A2331
220|生成通知四回调相对序;Safari/Contest无满IV时至多4次重摇全主IV并提前停;有重摇才calc;后续默认开启旗标种类3满IV再地图等级缩放;判奖NPC直接构造绕过|A2325,F06-S002,F06-S005
221|enter-map相关相对序Roam推进、Radar取消、Safari外区End、Contest inactive清理;非穷举所有enter回调|A2328,A2334,A0265,A0357,F06-S010
222|leave-map Contest active越界End(true)|A0356
223|转移步进相对序poison后Safari;truthy handled使后者跳过;Safari转移成功阻止普通遭遇|A0266,A0274,A2290,F06-S009
224|frame相关相对序病毒低电量延时BGM后Contest倒计时;非穷举所有frame回调|A2328,A2307,A2309,F06-S009
225|map/spriteset相对序darkness、location、Contest timer;正常先行回调返回为前提|A0352,A2328,F06-S009
226|Contest入口显式start通知;Safari不发|A0286,A2301
227|两个模式正常尾各显式一次wildend;在预算转移后;不外推普通包装所有正常路径或双重通知|A0295,A2304,A2321
231|Radar使用门无Safari/Contest排除;terrain/table/bicycle/debug/battery顺序;chain是GameTemp|F06-S008
232|live chain让较早Roam跳过;后Radar非摇草取消;模式覆盖可接管;Safari可达core0/2/3/4只有4可增链，Contest普通battle可1/4;非1/4取消;先地图转移可能已清链|A2328-34,A1624,A1628,A1631-7,SF29
236|Safari正配置显示步数剩余/配置及球;非正仅球;active Contest有K显示物种等级预算，无K显示None预算|A0446-9,A0453-5
237|Safari Quit确认结束menu写1回起点，拒绝重开;Contest Quit确认结束menu判奖不End(true)，拒绝重开|A0450-8,SF27
238|active Contest隐藏Bag;Safari不因此隐藏但Safari战斗无普通背包|A0409,A1566,A1643-4
239|专门Save需system且save允许且Safari区域false与Contest活动false;Contest不要求当前地图属于比赛;两个专门退出各独立条件|A0406-10,A0450,A0456,A2289
240|普通Quit无模式门;接受退出进入sharedSave必要overwrite;true/拒绝/被捕获失败false正常返回后均退出scene nil;拒退出仅重开且无save;拒save/overwrite不写仍退出;不End/Judge|A0410-27,SF38,SF39
241|类型值对象图消息及IO正常无无关回调前提;确认save清begun_new_game;safe/count/magic/time先写再compile校验;捕获IO只回退count仍false退出且可能部分文件;uncaught错误不保尾;均未执行|A0399-405,A0422-6,A0371-3,SF40a,SF40b
242|debug Safari正配置方可编辑steps0..99999，球0..99999;Contest正Settings时间可编辑分钟并移动timer及首显示;非正显示无限不可编，和负TIME显示00不同;改零后正常门判断|A0541-55,SF28
246|global whole object为保存供值;活动模式也可经普通Quit进入save;lastContest和四累计stats独立whole stats registration;不声称已写盘成功|A0358-73,SaveSF30d,SaveSF36,SaveSF37,STATS06
247|Safari全部字段在global输入;Contest player仍单员global含spares/K/active/uptime，无先拼队结束判奖;timer输入不证重载时钟显示或战斗局部预算恢复|SaveSF36,SaveSF37,A0373,A2308
248|固定默认14conversion无专门Safari/Contest转换;不能外推任意旧inner兼容或plugins;普通load可做其它转换|A0391-4,SaveSF30e
249|实际接待判奖奖励费用参赛日期Demo链未证;入口存在不证明调用|scope
253|默认Safari600步，Contest1200秒;零配置无限按各自消费门|F06-S005,A0267,A0307
254|map067无SafariMap但可匹配起点;068Safari/outdoor/forest/Forest;028MossRock BugContest，029/030Reception|F06-S003
255|map028省略version编译0;Land21/BugContest21是stepchance非version;十权重和十物种等级详已受领原fact;相同triple合并但此表十槽不变;运行仍查current版本或0fallback|A2312-8,SF24
256|两个完整球record口袋3与价0/300、OnFoe/PokeBall;普通目标各1.5，Ultra实际球前门折减;Beast行为为外域引用;预算来自入口实参|F06-S004,A1654-60,A0249,A0316
260|Safari默认600和调用预算;接待/flag区域;步尽球尽退出先1回起点;离区域清空|A0248-71,A0290,A0451,F06-S005
261|0不计步且UI仅球;负配置首合格步结束|A0267,A0271,A0448,SF06
262|Contest默认1200预算实参5/8 NPC和单队;到期球尽退出败平触发判奖;越界是中断End而非判奖|A0316-26,A0356,A2302-3,A2309,A0457,F06-S005
263|class捕获时限0不expired且无timer;负不expired但timer00:00|A0307,A0350-3,SF18
264|素材帧宿主随机序列Demo编排及保存后时钟未证;不同于可得source已读|unknown
268|Safari非地图回起点跳过;nil起点地图读取失败;人工非正球按正常门;已有非nilhandled保留|A0275-80,A0288,F06-S012
269|选员nil或正越界各自prefix;未判End先拼队再place异常;nil判奖点先名次再读;无map/table异常;空名次查询错误;最终联合满两消息早退无新增本次Dex昵称store且不回滚先前|A0316-36,A0338-49,A2294-9,SF16,SF25,SF31,F06-S015
270|败平加零球可两次判奖;重复入口追加;playerplace前三，info实参可后续;Demo查询未知|A0346,A0311-5,A2302-3,SF20,SF26
271|覆盖未经普通核心规则clear;任意战斗脚本错误不保完整清理;Demo可达性另界|A1637,A2323,F06-S016,unknown
272|全部菜单战斗时钟恢复宿主行为未穷尽;已证pause微更新有限链不被撤销;重载时钟素材播放奖励费用话术未知|A2306-11,unknown
276|静态未运行SF01至40;34新row208children与旧SaveSF30/36至40共36children完整有限接收;列举case标签是导航，不再生行为分母|cases
280|列出跨域primary依赖及GR011/013资格;仅采用本包明确finite contacts;未整域继承历史PASS|scope,history
284|Demo接待判奖奖励费用日期实际编排未知|unknown
285|媒体存在逐帧及native随机序列未知;静态分支分布需明确条件|unknown
286|保存后uptime和墙钟实际语义未知;不同时间基准静态分离保留|A0304-8,A0373,unknown
287|任意脚本异常完整会话队伍预算清理未逐字段验证;已知具体中止不回滚及可失败前缀仍有效|A1636-7,A1651,unknown
288|同分排序无明确稳定保证;实际tie行为未单独执行证明|A0345,unknown
'''
# supplemental source facts below are thin necessary complete local units already read during this child.
extra=[
('F06-S011','Data/Scripts/018_Alternate battle modes/002_BugContest.rb','complete config/query methods54–91','Chosen index setter directly assigns. Judging destination setter stores map/x/y/direction default8. Contest and reception configuration append map IDs or expand string flags over MapMetadata; offlimits checks membership in both arrays. Contestant query tests whether a stored contestant equals input.','Named config meaning, not Demo/event success.'),
('F06-S012','Data/Scripts/018_Alternate battle modes/001_SafariZone.rb','complete pbGoToStart63–80','Only Scene_Map enters fade block and reads start map/x/y; it stages direction2, dismounts then transfers. Absent saved start fails on indexed read after transfer flag assignment. Non-map skips these reads.','Exact already-known helper prefix; default valid start normally established before caller.'),
('F06-S013','Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb','complete prepare_battle82–166 and Safari wrapper118–160','prepare_battle requests matching rule/config weather/environment/backdrop/base/time and flags through setters. Safari setter defaultWeather stores weather, while sendToBoxes setter is no-op; Safari wrapper calls prepare then animation/start without ordinary start_core cleanup/after_battle/set_outcome.','Finite call/preparation contract; actual map metadata/player-resource inputs and successful returns are premises.'),
('F06-S014','Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb','complete ordinary pbStorePokemon5–86 and PeerStore5–36','Normal mixin nickname option/confirm precedes storage. Safari sendToBoxes is unset so ask/must-add party replacement branches are not selected. Peer appends same object if party room; full party calls storage, updates stored box/current box and requests box messages. No normal Safari experience/money contract is added by this receiving path.','Reached successful ordinary default-class receiving only; arbitrary IO/UI/box errors retain earlier prefix.'),
('F06-S015','Data/Scripts/018_Alternate battle modes/002_BugContest.rb','complete pbStartJudging150–167','Decision1 precedes judging; only Scene_Map then fade/stages transfer reads @start entries map,x,y,direction, dismounts, transfers and requests maprefresh. Any read/transfer error preserves earlier decision/rank writes; same-map still refresh requested.','No actual transition/render guarantee.'),
('F06-S016','Data/Scripts/018_Alternate battle modes/002_BugContest.rb','complete pbBugContestBattle361–404','Wrapper explicitly start-notifies then optional generation, constructs ordinary-derived Contest battle with player/foe arrays, start index0 and copied budget, sets single and prepares. Animation runs ordinary battle, after_battle(true), then loss/draw audio restore and ContestStartOver. Input precedes budget copy/equality0 judge/set_outcome/wildend/Boolean tail. No skip check or clear-battle-rules call occurs here.','Inherited ordinary internalBattle true fact separately FAC-A1684-5; no blanket ordinary combat approval.'),
('F06-S017','Data/Scripts/011_Battle/003_Battle_Action/007_Battle_Action_UseItem.rb','complete relevant registered Pokeball handler and command consumer','Pokeball item registers an entire-turn action under ordinary item-command contract; mode consumption override uses session budget. Ordinary no-effect restore-to-bag logic does not credit Contest budget, and capture path handler still requests a throw.','This contact must remain OPEN if the exact full action unit has not actually been read; no new business value inferred.')]
# S013, S014, S017 actual-reading status is checked explicitly by follow-up; they cannot silently grant support.
for id,path,unit,meaning,qual in extra:
 try:src=ident(R/path,R,fixedR)
 except Exception:src={'path':path,'commit':fixedR,'identity_status':'NEEDS_EXACT_PATH'}
 newfacts.append({'id':id,'source':src,'complete_unit':unit,'meaning':meaning,'premise':premise,'qualification':qual,'reader':'/root/facility_atomic_completion_cloud/f06_canonical_tail','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','actual_read':'PENDING_THIN_CONTACT' if id in ('F06-S011','F06-S012','F06-S013','F06-S014','F06-S016','F06-S017') else 'ACTUAL_COMPLETE_UNIT_READ'})
dump('necessary-new-meanings.json',{'utc':now,'common_premise':premise,'facts':newfacts,'new_primary_business_values':0})
records=[]
for row in rows.strip().splitlines():
 line,meanings,refs=row.split('|');line=int(line);components=[]
 for n,m in enumerate(meanings.split(';'),1):components.append({'id':f'F06-C{line:04}-{n:02}','meaning':m,'support_refs':refs.split(',')})
 records.append({'old_locator_id':f'F06-L{line:04}','line':line,'components':components,'disposition':'EXPLICIT_SCOPE_OR_PROVENANCE' if refs in ('scope','history','layout','unknown','cases') else 'CANONICAL_FINITE_MEANINGS_WITH_QUALIFIERS','qualification':'COMPLETE meaning read; source support subject to explicit premises and gap list. No native/full-domain approval.','open_candidate':'F06-ORDER-START' if line==120 else None})
frozen=json.loads((p/'frozen-inputs.json').read_text());wanted={a['line'] for a in frozen['targets']};have={a['line'] for a in records};assert have==wanted,(wanted-have,have-wanted)
dump('canonical-meaning-packet.json',{'schema':'gr8-f06-complete-canonical-meaning-reception/v1','utc':now,'reader':'/root/facility_atomic_completion_cloud/f06_canonical_tail','fixed_B8':fixedB,'fixed_R':fixedR,'formal':ident(B/'deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md',B,fixedB),'whole_formal_actual_read':'1–288 inclusive','original_locator_count':len(records),'canonical_component_count':sum(len(a['components']) for a in records),'count_qualification':'Manually authored complete current F06 meaning components, not a source-language universal atomic denominator; scope/layout/provenance/execution limits explicitly distinguished.','common_premise':premise,'support_resolution':{'Axxxx':'FAC-Axxxx in received-facts.factored.json, ranges inclusive; exact original forward identity and source identities retained.','SFnn':'Complete case with this ID in received-cases.exact.json, not just its old status.','SaveSFnn':'Exact case in parent save-vector-reception.v1.json, SHA620a0a97d4f89c8ebcb65d87ff624f811ad2071190800d40bc5541e36b8217a1, complete36children actually received here.','STATSnn':'FAC-STATS-nn in parent safari-contest-four-stats-consumers.v2.json, full six facts/premises actually received.','F06-Sxxx':'Child necessary-new-meanings.json, actual-read fields govern support.','scope':'Authoritative current formal scope/primary routing; no new source behavioral assertion.','history':'Root-primary bounded historical qualification reference, no independent reopening or inherited FULL.','unknown':'Explicit bounded NOT_EXECUTED/UNVERIFIED facet in current formal; not readable-source-unavailable.','cases':'All34newSF case208children plus oldSave36children received; other catalog WPs retain external primary.','layout':'Table purpose/columns; no extra business atom.'},'structures':records,'global_or_FAC_PASS':False,'new_required':0,'new_optional':0,'new_decision_votes':0,'actual_new_contexts':1,'requested_runtime':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','Fast':False},'actual_runtime':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','Fast':'UNVERIFIED','opaque_id':'UNVERIFIED'},'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})
print('STRUCTURES',len(records),'COMPONENTS',sum(len(a['components']) for a in records))
