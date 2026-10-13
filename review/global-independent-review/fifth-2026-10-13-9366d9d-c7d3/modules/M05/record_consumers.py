import review_state as s
D=s.load('consumer-read-plan')
rows={
0:('TOWNMAP仅无pokegear且持有；选飞行目标后关闭暂停并调用飞行，否则刷新','WP63 §2.1'),
3:('球选择按is_poke_ball筛选并按名字排序；取消返回旧身份','WP73-A §3.4'),
4:('进化复制同体clone改物种、清昵称标记持物缎带、普通球、重算治疗、直接入队图鉴','WP31/WP26'),
5:('价格覆盖严格规范化身份；买>0、卖>=0×2；省卖沿正买；非正保留','WP29 §5.2'),
10:('道具编辑属性schema回填/保留后缀，删除即时；新建ID派生去重/口袋0取消/价旧-1由控件夹限，手工文本键未进构造字段','WP73-A §4.3；新文本字段线索反证中'),
12:('Item格式化有效才real_name否则-；Ball格式化非空严格查name','WP73-A §3.4'),
15:('转换助手先严格查变量物品，再清变量；顺序成对取首个匹配，奇数尾忽略；物种目标严格解析，未移除库存','WP13/WP27/WP77待语义反查'),
17:('设施持物解析缺失归空，to/from持物身份；创建直接赋物/固定IV与EV总额整分，inspect努力项原样接收','WP54/WP76/WP19'),
20:('设施限制：部分开放条款允许分支为空；itemlist/无物/禁SoulDew/唯一持物；小杯禁莓汁/深海牙','WP54/WP56'),
21:('物品列表按原名忽略大小写排序，显示原定义序号；NEW哨兵/图标清空','WP73-A §5'),
23:('寄养物品消费：双亲香、Everstone形态与性格、机器Move不另查machine、LightBall伏特攻击、力量项固定IV计入3/5预算、DestinyKnot、Shiny/OvalCharm；无消耗持物','WP33/WP34'),
24:('种植Berry/Mulch过滤、先写地块统计再移除且不核结果；施肥后取消种植保留肥；喷壶首持有序且不耗；采收先can_add再统计/add/自开关；四肥料数学另补全','WP60树果/WP27'),
25:('设施战前治疗/记录双方持物，正常返回后复原等级、治疗、还原物品；中途异常无ensure保证','WP54/WP58'),
31:('Poltergeist：目标无物/物无效失败，否则提示；不消费','WP47-A'),
32:('debug加物忽略add结果仍显示成功；fill先clear，定义顺序每项入，重要1，有限容量跳过后者；empty保留登记/last pocket语义','WP72背包控制；仍待补完整关联头尾'),
34:('StrengthSap先取目标有效攻击并降阶；LiquidOoze反伤/HP物复检，否则可治且BigRoot1.3取整','WP46'),
35:('野外Pickup非蛋/技能/空手/10%后过滤数据两池长度、等级窗口加权；HoneyGather身份存在/空手/等级概率','WP61 §7'),
36:('致命伤裁剪：替身先、画皮/冰脸早退；满血层Sash/头带10%，标记后续才消费','WP43 §7'),
38:('束缚成功非替身/活/旧未束时GripClaw期限8或旧6，默认5或6；不消耗','WP47-B'),
40:('item通用编译条目空校验/终检五消息表；Trainer非空队/等级/昵称/招式去重/IV EV单项总/幸福/球类别验证','WP04/WP24'),
41:('Acrobatics无物或本招Gem已标×2；三墙LightClay8；NaturalGift旗标不同解析门/空物后续异常；Plate/Memory/Drive表另完整补读','WP47-A/WP45'),
42:('PowerHerb只首次蓄力决定速攻；快蓄力效果动画消息后消费，半无敌动画区别；前序失败可未消费','WP46/WP47-B'),
43:('write_items转通用导出；设施清单物品不存在留空，其它字段严格读取；不替代真实文件写入验证','WP04/WP76'),
44:('RingTarget改单类型免疫，IronBall地面对飞行提早中性；命中/伤害/会心完整物品层顺序不受moldBreaker；Micle读清；额外畏缩物允许倒下用户查询','WP43/WP50'),
46:('战斗招式显示伤害仅委托持久显示，注释旧分支不可当生效','WP43/WP67-A'),
48:('旧道具解析upper并trim后严格找，失败位置错误，不自动创建','WP04/WP75'),
50:('回合末BigRoot治疗、BindingBand按来源当时有效性、LEFTOVERS黑泥/珠类/拾取能力阶段再读；全回合循环到指定点才终止','WP41/WP45/WP50'),
51:('逐击calcDamage且非替身下目标可濒死有效物；反伤立即U补血；RoomService建立、Gem整招消费、SheerForce后段门、目标/用户/退出先后','WP42/WP49/WP50'),
53:('逃跑先训练家/禁止门，鬼/技能/烟球先于拘束；duringBattle跳确定逃脱和捕捉门但保留上层禁跑；物不消费','WP40/WP50'),
54:('人工BattleUse1-5全部UI选人/选招/选球目标/cursor保存分支','WP28/WP67-A'),
55:('迷恋写入后DestinyKnot中央资格反施，再治物/治能力；不消费红线','WP44/WP50'),
56:('初始化记录双方C到I、R为空/mega标记目录；天气场地只正期限/来源存在/有效物延长8；全能力后全物品种子通知','WP39/WP45/WP50'),
57:('挖矿每获物单件直接add并成功/空间消息，单失败不停止后件','WP70/WP27'),
58:('吸血LiquidOoze先反伤并即时物品补血，普通可治BigRoot请求×1.3取整','WP46/WP50'),
59:('讲究锁不存在招时清；讲究当前有效才限制；AV仅命令阶段且MeFirst例外；地面免疫/粉末护目镜/保护接触物品完整门','WP40/WP43/WP44/WP50'),
60:('正常终局先捕获收编与病毒、场景EndBattle、逐角色CancelChoice退款，再玩家侧全party按I还物；对方不该层还原','WP41/WP38/WP28'),
61:('角子机CoinCase门、coins0拒/满拒','WP69/WP24'),
62:('使用主链全读：Metronome记录、Choice锁行动结束、Gem记录清理；多击每击重读物品、反伤即时恢复、Sash提示消费、减伤果附效后消费；异常捕捉不回滚前缀','WP42/WP43/WP47-A/WP50'),
63:('ExpAll玩家许可或包有；ExpShare当前或I资格；EXPCHARM×3/2与幸运蛋当前优先I fallback；EV无场上有效性、先物品后病毒及上限','WP30/WP50'),
64:('VoltorbCoinCase与满金币门，不要求coins>0','WP69/WP24'),
65:('战斗成员初始化读取持久当前item_id并保留个体/索引，用于后续写穿','WP20/WP39'),
66:('捕获存放最后交换引发队列左移I；入队更新I；球失败不退款、OnCatch后保存球/形态/招式；CatchingCharm倍关键捕获系数','WP38/WP28/WP25'),
67:('完整优先重算才抽道具先制，局部只速/优先；能力与物品档胜出判定后显示/消费，不每次重抽','WP40/WP50'),
68:('战斗物品setter宽容失效归空写穿；有效性不含存在门；不可移邮件/Mega/变身/物种映射；地面、天气、粉末接触、还原/回收记录setter','WP20/WP43/WP47-B/WP50'),
69:('MegaRing目录快照按标志，玩家包与NPC物品列表分别查；提示选首个持有身份无则默认名','WP22/WP24'),
70:('PriorityAbility优先提示，否则物品；物品行动仅存活使用者按类别执行；决定正退出','WP40/WP50/WP28'),
71:('脱壳先于拘束、AmuletCoin/LuckIncense原ID标奖金不查有效性；入场能力后物/恢复、首个EjectPack/危急逃避停；靴子逐危害且不妨碍毒吸菱','WP40/WP45/WP50/WP24'),
73:('全部27默认球效果家族与缺注册回退/19倍率身份、Friend/HealBall持久提交；主概率与捕获归M06','WP38')
}
for i,(rules,target) in rows.items():
 q=D['files'][i]
 s.source(q['path'],[(x['lines'][0],x['lines'][1],'; '.join(x['entries']),rules,[target],'源语义已审；按共享主合同补全逐条对照中，不宣称整个外模块完成') for x in q['ranges']],'business_consumer_projection')
 q['status']='semantic_read_comparison_in_progress';q['rules_reviewed']=rules;q['spec_targets']=[target]
s.save('consumer-read-plan',D)
# Remove source code snippets from search index; path+line suffices for navigation.
p=s.ROOT/'consumer-search.txt';p.write_text('\n'.join(':'.join(x.split(':',2)[:2]) for x in p.read_text().splitlines())+'\n')
s.source('Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',[(1,153,'全部turn/choice/lock/confusion/called move','行动结束讲究锁，混乱伤害后物品检查，simple调用前提',['WP40','WP42','WP50'],'supported_static调用投影'),(154,578,'pbUseMove全文','计数/物品/循环/提前失败/异常后缀与共通后段，所有分支已读',['WP42','WP50'],'supported_static物品消费者投影'),(579,762,'pbProcessMoveHit全文','按击计算→反应→即时补血→主/附效→弱化果消费；NaturalGift空物异常前缀',['WP47-A','WP50'],'supported_static')],'business_consumer_projection')
s.source('Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb',[(1,161,'BerryPlantData全文','生命周期/重种/产量与四种mulch增减；消费不回滚；源注释旧机械更新与实际caller分开',['WP60'],'待完整树果正文对照'),(162,307,'berry displays/events全','湿度/阶段视觉取身份；事件匹配berryplant；旧update调用默认false，真实媒体未证',['WP60','WP16'],'源已读，表现M10')],'business_consumer_projection')
s.source('Data/Scripts/011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb',[(1,198,'全部四球族/所有注册','缺省false/原率/空通知；19倍率各身份与HP/capture交界，治球/友好球；只失败callback计失败',['WP38'],'静态共享投影；M06概率主责')],'shared_item_effects')
s.checkpoint(['跨战斗物品消费者的真实调用层已读：完整UseMove762行、逐击/后段/回合末/终局退款/优先重算/捕获/成长/有效性/直接核心；保持共享唯一规则投影','道具球全部四家族198行、树果植物全471行及BerryPlant数据45行已实读；寄养物品消费者已逐函数读','新建道具/类型和训练家败词的文本字段线索已通过通用register不存在键转换的静态核查；现行WP73-A反证继续中','source-to-spec/spec-to-source尚在完成共享映射；所有当前已读源的有限消费者区间已写coverage'],['剩余AI/形态/设施/编译/调试消费者源','现行共享规则逐章对照与全部向量映射','精确参数和编辑器候选反证及最终覆盖校验'])
