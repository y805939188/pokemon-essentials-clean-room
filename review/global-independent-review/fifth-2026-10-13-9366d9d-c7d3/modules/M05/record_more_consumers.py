import review_state as s
D=s.load('consumer-read-plan')
rows={
1:('模拟估分持物+10；真实对战分支记录双方物，正常返回先治疗再还原、仅此不是始终事务','WP76'),
2:('Poltergeist失败预测按物存在与有效性；四危害评分中等技能按靴子/飘浮/间伤免疫剔后备','WP52-A/B'),
6:('生成个体重复判定：同种同槽序先判，或持物+性格+全EV相同；未原地排序招式','WP76'),
7:('聚气评估有效会心物各身份+10，不用倍数累加，基础伤害招门+15','WP52-A'),
8:('生成候选41持物/13物种门、Focussash概率、低高等级果替换/技能与道具再校；机器教学候选快照','WP76'),
9:('所有持物进化与道具使用族/球扣减/交换持物，已扩展读取完整注册块；不以常见Pokémon规则替代','WP31/WP32'),
11:('持物形态Arceus17(+Z)/Silvally17/Genesect4/原始二珠/锈剑盾，工具表全部onSetForm旋转/删除/学习与缺招区别','WP21/WP28'),
13:('Safari球不扣背包而专用ballcount先减；盒满在动作前拒；捕获即记录存放、无球终结；异常0清场','WP37/WP38'),
14:('所有物品变更AIhandlers全读：交换/赠予/夺取/毁物符号、MagicRoom到期nil保持、强制吃果各评分门、Fling真实基底委托','WP52-C'),
16:('个体物品/mail与进化检查工具：Everstone/BattleBond统一拒；first-match进化，成功后持物消费另handler','WP20/WP31'),
18:('捕虫大会SPORTBALL专有计数、直接注册跳人工资格流程、存放只候选替换、回合末无球3','WP37/WP38'),
19:('Acrobatics预估飞行宝石特例、会心正负与旧表取尾、LuckyChant逐来源；自然之恩失败预测不提交','WP52-A/B'),
22:('宫殿局部选招仅CHOICEBAND限制，与三讲究全普通门不相同；Torment简化','WP56'),
26:('得到/拾取/奖品三包装的add不预检、消息先后和false部分写入；SOOTSACK入场煤灰消费者另read','WP27/WP61'),
27:('换人评估靴子免危害/浮空、后备HP损失评分，睡眠与呵欠持果可治拒换、完整困对方检查含持物','WP51'),
28:('战斗debug设置物写穿实体/在场；邮件创建在先设物后，无信箱Give中间读取错误；移除清mail','WP72'),
29:('wants_item基础表→中等特化→投掷/轻技增减；强制消耗值逐身份，ASPEARBERRY匹配内键不同导致-6，保存负分门','WP52-C'),
30:('野外全encounter源449行：驱虫参照非蛋/可用配置、雷达绕过、笛正负1–4级夹限、持物先于能力遭遇率；野生物品桶抽样/Charm再抽','WP36/WP37'),
33:('debug显示两类个体当前持物，失效宽容显示-；纯显示值无物品变更','WP72'),
37:('HM标记遍历物品定义；动态显示type/damage全部代码在禁用块，不当真实规则；实际回字段值','WP20/WP43/WP66-A'),
39:('debug个体设物无背包成本，先item再mail、取下清mail；球记录所有身份选择不消费球；复制caller另读','WP72'),
45:('编译事件所有物品/钱消费者：35旧映射、item/hiddenitem两页、自开关仅接收真、SellItem免费预检与收费先扣钱后给予、旧money比较含边界，未运行转换器','WP75/WP27/WP29'),
47:('AI预估真实handler读取且GemConsumed清理、目标果不算；ZoomLens预测与真判断不同；会心目标物层误传U物但默认空族','WP52-A/WP51'),
49:('AI后备飘浮用持久物品ID/能力，无在场有效性','WP51/WP52-A'),
52:('通用高技能命中反应评分仅handler存在性+8，不执行反应；SheerForce只挡AfterMove项，OnBeingHit保留','WP52-A'),
72:('能力物品消费者：Unburden、Magician/Pickpocket转C/I、BallFetch回球/Harvest/Pickup改R/I/序号、Frisk世界方区别、气体移除Unnerve重新检查','WP49/WP50')}
for i,(rules,target) in rows.items():
 q=D['files'][i];ranges=q['ranges']
 if 'registration_full_ranges' in q and i in [2,7,19,28,39,52,72]:ranges=[{'lines':a,'entries':['whole registration']} for a in q['registration_full_ranges']]
 if i==27:ranges=q['ranges'][:2]+[{'lines':a,'entries':['whole registration']} for a in q['registration_full_ranges']]
 # A few inventory context snippets extend beyond the exact reviewed block; use only known intervals.
 if i==9:ranges=[{'lines':[257,275],'entries':['Shedinja']},{'lines':[339,452],'entries':['six held-item evolution families']},{'lines':[512,617],'entries':['six active item + trade families']}]
 if i==11:ranges=[{'lines':a,'entries':['complete item/form handler']} for a in [[164,176],[221,314],[329,406],[509,542],[562,587],[614,633],[653,691],[699,729]]]
 if i==16:ranges=[{'lines':[546,600],'entries':['item/mail']},{'lines':[974,1058],'entries':['evolution wrappers']}]
 if i==14:ranges=[{'lines':[1,376],'entries':['entire item AI effect file']}]
 if i==18:ranges=[{'lines':[1,83],'entries':['entire BugContestBattle file']}]
 if i==30:ranges=[{'lines':[1,449],'entries':['entire wild encounter file']}]
 if i==45:ranges=[{'lines':[1,40],'entries':['replacement dictionary']},{'lines':[771,808],'entries':['convert_to_item_event']},{'lines':[1135,1576],'entries':['fix_event_use entire']}]
 s.source(q['path'],[(x['lines'][0],x['lines'][1],'; '.join(x['entries']),rules,[target],'源语义已实读；共享当前合同对应章节反查中，不声称完整外模块通过') for x in ranges],'business_consumer_projection')
 q['status']='semantic_read_comparison_in_progress';q['rules_reviewed']=rules;q['reviewed_ranges']=[x['lines'] for x in ranges];q['spec_targets']=[target]
s.save('consumer-read-plan',D)
s.source('Data/Scripts/011_Battle/005_AI/008_AI_Utilities.rb',[(163,229,'完整基础物品评分表','全部基础身份与-9..10值，未匹配默认为0由caller实现',['WP52-C附表 §3'],'已语义实读待附表全比'),(387,898,'全部46直接+7复制+2条件ItemRanking','每身份条件/种类/正负/HP值/类型表/宝石18属性与<=5+2；目录不是实际效果消费',['WP52-C §2/附表'],'已逐handler审读；共享AI主责')],'shared_item_evaluation')
s.source('Data/Scripts/011_Battle/005_AI/001_Battle_AI.rb',[(84,163,'AI handler defaults全','评分nil保持输入、失败假、should_switch首真、ItemRanking空返回原分',['WP51','WP52-C'],'supported_static注册框架')],'shared_dependency')
S=s.load('supplemental-consumers')
for i,x in enumerate(S['entries']):
 if i<2:rule='天气/场地完整评分；延长物+4、伞只挡中等附加、种子±8独立接地；不执行真实道具效果';target='WP52-B'
 elif i<14:rule='状态/临时状态/浮空评分完整注册；对应治果预先拒效、红线反迷恋-15、铁球与气球预测门，保持技能层及非执行差异';target='WP52-A'
 elif i<19:rule='节拍器+7；同键后登记覆盖前；三墙光黏土+5和现墙/HP守卫；评分独立真实期限';target='WP52-B'
 elif i==19:rule='PowerHerb为二回合评分最先原分返回，排后续Truant/回合末伤害/保护惩罚；真实消耗不在此';target='WP52-B'
 elif i<25:rule='BigRoot恢复评分+5与预估×1.3，LiquidOoze/可恢复/HPAware门；扎根/水环基础+8/15';target='WP52-B'
 else:rule='束缚有效头带/爪+5；MentalHerb三限制无用门、讲究锁增减/挑衅无锁预判；治疗封锁只Leftovers/毒BlackSludge补选';target='WP52-C'
 s.source(x['path'],[(x['lines'][0],x['lines'][1],x['entry'],rule,[target],'完整注册体已读；待共享正文逐条比较')],'business_consumer_projection');x['status']='semantic_read_comparison_in_progress';x['rules_reviewed']=rule;x['spec_target']=target
s.save('supplemental-consumers',S)
s.source('Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb',[(1,77,'Peer与NullPeer全文','入队-1、满队盒治疗保ready、存储失败显示普通服务缺口；创建/入场/离场形态钩子；NullPeer未用',['WP25','WP26','WP38','WP21'],'supported_static共享接口；盒满异常前提不默改')],'acquisition_consumer')
s.source('Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb',[(1,134,'记录器全文','TrainerInfo数组/非数组失败、记录party/items/动作，成功registerItem后记目标/招式；StorePokemon空实现',['WP58','WP24','WP28'],'源已读待回放主合同对照'),(135,287,'播放模块/身份重建全文','播放按原items/InternalBattle重新登记动作，可调用bag消耗；无额外假造库存；4槽限制；重建ID/姓名徽章但其它默认',['WP58','WP24','WP28'],'源已读待共享合同对照')],'shared_business_caller')
s.source('Data/Scripts/002_Save data/004_Game_SaveValues.rb',[(1,8,'player save','默认Unnamed/首训练家类型、字段类校验、原对象load/save',['WP09','WP24'],'supported_static'),(90,102,'bag/storage save','新建默认Bag/Storage；旧保存物直接加载',['WP09','WP25','WP27'],'supported_static')],'persistence_projection')
s.source('Data/Scripts/002_Save data/005_Game_SaveConversions.rb',[(205,240,'v20 bag/player conversions','lastpocket读后清lastPocket大小写不匹配留旧字段；clone选择表/登记原引用/ready/default、角色号加1',['WP10','WP27'],'源已读待迁移合同对照')],'persistence_projection')
s.source('Data/Scripts/016_UI/023_UI_PurifyChamber.rb',[(431,511,'手动WITHDRAW/交换/替换','取出预先pbBoxesFull；自动存储再删除，物品仍属个体对象；caller存取限制不同',['WP23','WP25','WP26'],'AQ29取出守卫supported_static'),(560,604,'自动净化收编','先净化再通用store再清shadow，无该段额外全满门；UI检查所需形态保留',['WP23','WP26'],'需沿WP23自动路径解释，非手动取出全称'),(1287,1294,'pbPurifyChamber入口','seen标志先置再开场，字段输入保持',['WP23','WP24'],'supported_static')],'acquisition_consumer')
s.source('Data/Scripts/018_Alternate battle modes/002_BugContest.rb',[(180,196,'参赛队伍借出尾段','选中单成员为新party、其余存otherparty',['WP37','WP25'],'supported_static'),(205,224,'pbEnd完整','还回其它party在前，非中断命名存候选，最后清候选/结束字段/地图刷新',['WP37','WP26'],'AQ28supported_static')],'acquisition_consumer')
s.source('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',[(68,141,'球资源debug完整','Safari/Contest可改球计数、时间；不消费背包',['WP72'],'supported_static'),(555,591,'治疗/赠送debug完整','逐个heal；SilentAdd正常目标预判消息，失败仅容量提示',['WP72','WP26'],'supported_static'),(778,837,'背包debug完整','忽略add结果、fill/clear的登记与口袋保留',['WP72','WP27'],'supported_static'),(842,1143,'所有玩家debug控制','钱币BP钳制/24徽章/跑鞋/图鉴许可/电话/BoxLink/角色/服装/名字随机ID；图鉴内部不主审',['WP72','WP24','WP63'],'源已读待WP72相关交界对照')],'business_consumer_projection')
s.source('Data/Scripts/020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb',[(1091,1132,'礼物创建/复制全部入口','MysteryGift现对象传入、clone后party store忽略返回提示成功；storage优先party否则caught并恢复原currentbox',['WP72','WP64','WP25','WP26'],'源已读待WP72投影')],'business_consumer_projection')
s.source('Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb',[(87,107,'pbRecordAndStoreCaughtPokemon完整','先seenowned与条件dex、shadow标记，再存放，最后clearcaught；异常无总回滚',['WP38','WP26'],'supported_static捕获边界')],'shared_item_effects')
s.source('Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb',[(634,645,'物品储存助手card单件包装','数量/单件add/remove共用helpers，不等价注册Item身份',['WP68','WP27'],'supported_static'),(704,730,'创建卡牌工作表相关完整','拷贝各卡数量至独立slot表，add结果未查、cap用永久表maxSize',['WP68'],'源已读待目录投影'),(982,1036,'TriadStorage除总数末尾','存储MAX999/length+1/查询边界/预检添加删除；与bag算法共享但Species身份输入',['WP68','WP27'],'supported_statichelper消费者；未声称全卡牌游戏审查')],'shared_inventory_consumer')
s.source('PBS/pokemon.txt',[(18565,18588,'ZYGARDE基础完整节','普通特性0AuraBreak/1PowerConstruct，无hidden；default特例胶囊资格反例',['WP28','WP19'],'GR5-M05-004具体数据前提')],'counterexample_data')
s.source('PBS/pokemon_forms.txt',[(1730,1764,'ZYGARDE全部三备选形态节','形态1继承普通双特性；2/3只PowerConstruct且hidden也同；不把形态2/3用来证明基础胶囊拒绝',['WP21','WP28'],'supported_static具名边界')],'counterexample_data')
s.checkpoint(['消费来源首轮74文件计划的物品相关函数/注册已全部实质读取（外模块未覆盖正文区间仍partial）；补搜snake_case AI调用，追加31完整消费者注册/函数已读','AI物品评级基础表与46直接/7复制/2条件处理器387–898逐段已读；全部默认项与物品效果分层，未运行AI或模型','保存/迁移、回放、净化间、捕虫大会、卡牌共用储存、调试获取等业务caller已补读；剩余是当前合同反查及缺漏补读','四条候选已写findings；GR5-M05-004保持unresolved待最后目录/补充反证，不自签必修'],['核验剩余未记录精确源范围（工具/配置/HTTP/特殊野外caller）','完整当前共享合同与相关向量对照；解决源映射中的pending','最终整理source-to-spec/shared-interfaces/报告和七产物结构检查'])
