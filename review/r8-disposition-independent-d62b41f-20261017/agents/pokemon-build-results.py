import json, hashlib, subprocess, datetime, re
from pathlib import Path
O=Path('review/r8-disposition-independent-d62b41f-20261017/agents')
C='d62b41f4d620e50bb04c80a7505374bd284d8210'
P='planning/implementation-routing/r8-20261017/'
def get(p):return subprocess.check_output(['git','show',C+':'+p])
m=json.loads(get(P+'routing-manifest.json'))
e=json.loads((O/'pokemon-static-evidence.json').read_text())
notes='''454 属性身份派生及缓存属于框架持久个体；战斗临时类型/特性效果明确在域外。
455 等级经验换算和缓存是持久领域接口；战斗逐级成长由独立协作条目承接。
456 IV/EV存储、培养额度、设施正常例外和性格数据由框架维护；计算/HP刷新已拆457/458。
457 持久公式与场上使用映射列为协作候选，未以相同公式证明刷新兼容。
458 HP上限重算、濒死复活和战斗刷新跨状态已列协作并绑定战中成长原型。
459 本节是持久字段及重算的不变量，对457/458的引用可作为框架规则关联保留。
460 非法输入/缓存/原始存储边界归框架，来源反例未变成目标兼容决定。
461 注册/复制、创建/读取规则及作者映射可由框架拥有，战斗消费者已另列464。
462 个体斑点的像素、分帧和素材边界独立列MZ，未把数学向量当呈现证据。
463 形态提交、招式/PP改写及条件图鉴登记归框架；战斗调用时机另列464。
464 战斗入离场/捕获触发与持久形态反馈已列协作，等待版本和行为原型合理。
465 标记编辑的确定/取消/动作键、仓库与摘要差异及缎带分页裁图未拆MZ责任。
466 形态查询/提交守卫及展示存储的不变量可由框架拥有，UI具体缺口另由465定位。
467 框架负责坏形态/时间/缎带接口失败可行；本行引用的编辑失败仍受465拆分影响。
468 默认处理器与季节/时间配置为框架输入；未承诺跨战斗周期组合已验证。
469 个体资格、背包环与业主额度、战斗刷新同列协作可表达输入交界。
470 持久个体Mega目标查询、数据顺序及强制形态归框架；不冒充战斗许可。
471 许可/登记/取消/执行及持久回读已列协作，来源裸接口差异保留。
472 Primal入场、持物与持久形态回读是独立协作候选，没有套用Mega额度。
473 捕获、世界/设施/裸终局不同善后被协作边界保留。
474 资格丢失、部分提交和AI入口按协作候选保留，没有声称全部兼容。
475 默认Mega数据需框架内容与Showdown规则/格式映射共同核对，协作粗标可接受。
476 宝珠、环来源和不消费规则跨框架资源与战斗资格，协作候选可接受。
477 METAGROSS固定数据差异及HP向量需两端映射，协作待验证而非兼容已证。
478 来源与范围只有审计来源/证据限度，被制造为独立待实现功能。
479 心量表下降表为框架领域内容；特殊范围待用户决定且未自动排除。
480 本节是成长/净化室独立向量，已有主规则，测试设计不应另计独立实现功能。
481 可选内容身份/量表/招式及道具数据可由框架持有，启用范围保持待决策。
482 来源与证据只有静态取数/核对限度，不存在独立待实现功能。
483 Shadow标志、量表、复制和暂存字段可由框架拥有，范围仍待用户决定。
484 派入、Call及战后索引通知混在量表下降节，缺Showdown职责与捕获后快照交界。
485 持久招式刷新与战斗香不会重建场上副本的例外需协作，框架/MZ不能替代该边界。
486 Hyper随机、服从、反伤及场上类型列协作，范围未被擅自排除。
487 战斗经验/EV暂存与净化UI恢复合一，未列Showdown协作及战中成长原型。
488 战斗香登记/复检/退款、持久状态和场上招式差异未绑定背包战斗道具协作原型。
489 净化室编成、选择器取消、暂持/交换/取出与领取UI需独立MZ验收，未拆分。
490 五类进化条件与作者前向/反向关系属于框架领域规则；战后记录生产不由本行冒充。
491 统一守卫、顺序和返回/缓存副作用属于框架判断接口。
492 整个进化提交节放MZ，连统计/持物消费/额外个体/物种HP图鉴学招提交均未拆框架验收。
493 入口返回、取消与消耗的编排归框架可行，具体演出缺口由492定位。
494 进化目标/保留/消耗不变量由框架维护，演出引用不新造第二实现。
495 进化失败、取消、编号可复用及复制前置是框架领域边界。
496 世代独立配置和未知方法政策保留，未把来源反例强制变成实现要求。
497 情境身份和输入契约数据归框架，零样本未被视作功能不存在。
498 默认进化条目是框架作者内容，保持自身物种比较等来源差异。
499 地图/天气具名数据作为框架判定输入可以接受，不据数据宣称事件可达。
500 固定算术/状态对照是验收向量，主规则在WP32，不应新增独立待实现功能。
501 检查时读取当前环境/队伍/个体的领域合同归框架，持久与场上输入不混同。
502 K/D记录生产、席位身份及清零已列协作，有别于框架消费条件。
503 成长→捕获接收→善后→战后进化的次序已列协作并绑定成长原型。
504 捕获替换、成员索引与成就接收者已列协作并绑定捕获原型。
505 交换条件/提交与图鉴页双收尾的宿主重复释放风险混为框架，缺MZ生命周期验收。
506 事件编号、集合快照、返回命中与领域提交不同属于框架编排，编号未擅自消费。
507 坏输入和既有提交前缀保留为框架领域边界，未把运行未知升级为已证。
508 单次亲本归一与物种/招式角色是框架育种领域规则。
509 前身/熏香/后代采样/地区蛋形态输入属于框架育种与内容规则。
510 基础蛋、母系/永石提交、性格及特性通道属于框架，条件图鉴副作用仍保留。
511 招式继承顺序、角色门、去重保后和槽位截断由框架负责。
512 IV遗传数量、力量道具冲突与抽取池为框架规则，未假造第三持物。
513 球、异色轮首读取/缓存及病毒收尾为框架生成规则。
514 一次生成次序、条件化随机次数及亲本动态读取由框架维护。
515 直接工具不重查兼容、空通道及缓存边界均为框架生成失败合同。
516 遗传世代配置与未知组合保留，阶段待定诚实。
517 漫游配置、惰性位置和终结状态由框架维护，数据开关不冒充已开启。
518 地图进入推进及候选许可属于框架世界规则，随机候选和类别空失败保留。
519 同一漫游个体真实战斗HP/PP/异常/持物回写及总是逃跑被框架单方吞并，无逃跑协作门。
520 雷达规则与摇草动画/0.5秒等待混为框架，未拆MZ表现和宿主更新验收。
521 雷达候选、异色三层与结果驱动连锁更新由框架世界业务负责可行。
522 取消/保存合同内含完整调试按键画面，需MZ验收及调试范围待决策引用。
523 漫游/雷达默认配置及资源ID为框架内容；未知真实素材/随机序列保留。
524 位置/候选空值/异常清理边界为框架世界业务合同，未虚构安全回退。
525 捕获菜单、扣球登记、目标再解析及挡球列协作，并绑定捕获原型。
526 捕获数学保持协作候选，未以数值向量当行为兼容证据。
527 球族、实时战斗重量与成功后个体效果列协作并绑定原型。
528 移出敌队、经验、终局、形态及接收队列提交次序列协作。
529 战后图鉴/命名/容量/替换由框架拥有且仍绑定捕获原型，分层合理。
530 Shadow抢夺许可/属主/接收与普通捕获的接口列协作，未抹掉已知分支。
531 捕获失败/媒体/特殊模式边界作为协作候选保留，未认定无原型等于不可收尾。
532 本次类型/相性主要为战斗计算，Showdown候选合理；文档另有被metadata吞掉的§2.1。
533 命中分层、随机门与异常入口属于战斗内算法，Showdown候选合理。
534 会心概率/覆盖/亲密门为战斗算法，版本世代格式待固定。
535 普通伤害输入/倍率/舍入为战斗计算，未宣称公式一致即行为已证。
536 伤害/计划损失/HP提交分层为战斗执行，框架消费关联仍需后继验证；未作已兼容结论。
537 PBS作者缺省、类别×威力校验、本地化字段和战斗配置同节全交Showdown，需拆框架内容边界。
538 本节战斗不变量与合法输入边界可由Showdown调查承接，未补官方规则。
539 只有范围/核对方法、来源计数及共享责任口径，不应生成独立待实现功能。
540 114项效果的对象/参数/次序及唯一主规则为战斗行为目录，Showdown候选可接受。
541 状态/域外效果族的责任目录仍是战斗行为范围，待验证而非宣称实现完成。
542 默认招式效果绑定数据可作为Showdown承载调查输入，不能证明目标默认数据相同。
543 持久异常/计数与场上字段同步为本节核心，Showdown单方标签未给框架写回边界。
544 异常资格/提交/同步/条款为战斗逻辑，可由Showdown调查承接。
545 状态期限、初始化/濒死和局部清理为战斗规则，持久边界问题见543。
546 阶级查询/提交/镜甲反射及专门预检为战斗内行为，粗标Showdown可接受。
547 状态招式有界族和逐组件资格/部分成功为战斗逻辑。
548 阶级参数、直接重写、成员池与顺序为战斗规则，不依标识名推断实现。
549 计算读取与局部期限/清理属于战斗消费者，未冒充持久历史。
550 战斗配置、查询与提交不同及部分成功规则可由Showdown调查承接。
551 142项实际合同与主文链接为战斗行为范围目录，可作为承载候选。
552 域外行为目录关联对应战斗主规格，未被升级为已实现；仍需分项版本比对。
553 覆盖边界只有审计责任和范围声明，不是独立待实现功能。
554 自然之恩续击消费者为战斗内特殊行为边界，可由Showdown调查；永久写回风险另见574。
555 整次/逐击/中断及自然之恩异常前缀为战斗执行，未把静态向量当已运行。
556 多击、蓄力、连用及具体随机门属于战斗规则。
557 固定伤害/反击/记录是战斗算法，HP写回仍须关联持久接口验证。
558 动态威力/类别/输入替代与誓约是战斗内规则，未把名字代替算法。
559 治疗/吸取/持续建立和HP均分为战斗执行，指定例外已保留待比对。
560 反伤/自损/同归与Shadow HP效果是战斗规则，未以静态正例承诺终局。
561 当前招式配置/样本是战斗调查输入，未宣称完整历代复刻。
562 场上能力有效性及消费者门为战斗内规则，Showdown候选合理。
563 速度/重量/行动输入为战斗计算；沉重球消费需跨域核对，未被宣称已覆盖。
564 类型/命中/会心特性修正为战斗算法，固定顺序和静默差异保留。
565 伤害倍率位置/量值及模式破坏者门为战斗规则，未假定同名效果相同。
566 状态/阶级免疫查询为战斗逻辑，未把视为状态写成永久字段。
567 这里只提供阻止/保证资格，不执行完整逃跑或换人，Showdown候选可接受。
568 核心直接规则和共享主规格均为战斗依赖，未将缺登记视为无功能。
569 特性注册/别名配对目录是战斗调查范围，不以计数证明兼容。
570 失败/入口/舍入和前向责任仍有战斗行为约束，粗标Showdown可接受。
571 32族目录中Exp/EV两成长族已由578列协作，本表整节仍Showdown，映射责任不一致。
572 宝石/减伤果类型映射为战斗数据输入，Showdown候选可以接受且仍待比对。
573 覆盖边界只给审计范围和域外引用，不应另造待实现功能。
574 C/I/R/P/Belch、持久写穿/共生/消费/终局还原及持久成长查询混在Showdown单方。
575 速度/重量/命中/伤害倍率及计算标记是战斗计算，消费主边界另见574。
576 LEPPA按持久槽读取后强写异身份战斗槽、主动背包与被动持物消费区别未列协作。
577 受击/退出道具的C/I与永久对象转移、负选择已消费和自然之恩异常前缀需协作边界。
578 成长持物与回合末消费明确列协作，仍待固定版本和行为验证；非已验证结论。
579 核心表含EXPSHARE/奖金与其它世界持物输入，未来责任仍笼统Showdown，需精确归属关联。
580 Safari会话与地图场景限定转移同节，需拆世界状态/预算与MZ回起点表现验收。
581 Safari专用战斗/预算/捕获/逃离列协作与捕获原型，未假设普通格式覆盖。
582 捕虫会话缩队与暂停微更新倒计时/定时器/判奖转移混节，未拆MZ边界。
583 Sport预算、普通战斗接入和保留结果列协作并保留捕获原型。
584 评分/对手生成/名次查询属于框架活动规则，范围待用户决定。
585 完整暂停UI、专门Save/普通Quit Game、保存前缀与调试菜单被框架单行吞并。
586 活动默认配置和样本值由框架维护，特殊范围未被自动排除。
587 活动会话失败/重复判奖/异常前缀可归框架，宿主未知及范围决策仍保留。
588 树果持久领域字段与作者内容校验属于框架，R8-U03保守绑定正确。
589 生命周期/重植与离线追赶属于框架领域规则。
590 新旧显示更新的调用门、土壤/植物图形与闪光动画混在时间结算框架行。
591 背包选择、确认取消/消息等待微更新、自身开关与外层reset需拆框架/MZ验收。
592 新旧产量公式与数据对调属于框架规则。
593 植物领域及提交不变量可由框架维护，UI消费者需按591另拆。
594 失败/取消/时间回拨的领域边界可归框架，未承诺资源实际成功。
595 树果配置/内容常量为框架输入，动画ID未被当作已验证呈现。
596 完成移动/碰撞、微更新、煤烟/自动运动、低电量和Repel选择UI均未拆MZ消费者。
597 行走友好计数/概率/集合属于框架领域规则。
598 野外毒伤领域写入与批次音效/红闪及全队失能转移混为框架，需MZ验收。
599 病毒编码、日期推进与战斗传播引用属于框架持久规则，仍需跨域按主规格消费。
600 回程目的地状态/治疗与场景门/载具/伙伴清理/转移刷新混为框架，需MZ分界。
601 持久字段与完整调试UI、资源/编译审计入口混节，缺MZ及调试范围决定引用。
602 野外配置和周期常量由框架维护，未以世代号替代独立开关。
603 领域失败/异常/未知边界归框架可行，未虚构所有路径转移或回滚。
604 图鉴记录字段及派生缓存由框架维护，记录与图像维度分离。
605 图鉴入口的接收者、内部门与直接写入属于框架记录合同；战斗/捕获调用次序需联调，主捕获行已绑定原型。
606 图鉴身份、形态、性别映射和缓存行为属于框架领域规则。
607 区域内容/编号/解锁、作者缓存及栖息地格集合可由框架拥有，MZ展示另应608承接。
608 暂停入口、搜索/排序/形态选择器写回、图像请求与Info展示全节未拆MZ。
609 Voltorb棋盘生成/阈值及1000次回退由框架规则维护，范围待用户决定。
610 导航/标记/翻牌的MZ去向及框架伙伴明确，可作为UI粗标候选。
611 状态结算内§4.1精确输入仲裁和局部动画/等待时序未拆MZ验收。
612 高级别倒置夹限及已写奖励/失败前缀属于框架会话规则，未来兼容政策待决。
613 玩法取消、数据异常与奖励保留的领域边界由框架维护，MZ伙伴及范围待定诚实。
614 75项有序候选为框架内容数据，未把固定清盘乘积当期望收益。
615 日期/随机/变量写入编排由框架服务候选承接可行；宿主变量接点须后继固定。
616 队伍/盒检索顺序与并列由框架拥有可行；被metadata吞掉的§3匹配数学另列文档缺口。
617 名字/位置/匹配数三项顺序提交可由框架维护，变量适配及坏输入政策待定。
618 冻结依赖/旧批准与开放问题是交接元数据，不应新增独立待实现功能。'''
notes=dict((int(l.split(' ',1)[0]),l.split(' ',1)[1]) for l in notes.splitlines())
assert set(notes)==set(range(454,619)),(len(notes),set(range(454,619))-set(notes))
findings=[]
def finding(id,severity,title,ids,evidence,reason,repair):
 findings.append(dict(id=id,severity=severity,title=title,feature_ids=['FR-%06d'%i for i in ids],evidence=evidence,reason=reason,necessary_fix=repair))
finding('POK-S01','P2','核心行为被概念标题规则降为metadata',[],[
 {'source':'pokemon-rules/wp43-types-accuracy-and-damage.md','lines':[29,36],'heading':'2.1 效果身份缺省与无实现回退'},
 {'source':'pokemon-rules/wp70-lottery.md','lines':[19,26],'heading':'3. 匹配规则与领域概念'}],
 'WP43明确规定未知变化效果失败/伤害效果回退、PP不退及SHADOWSHED不同绑定；WP70定义输入整数转换、低16位公开号及最低五位最长连续匹配。两个完整行为节均被section-metadata笼统关联整篇功能，且均不在任何feature的source.line_ranges内。标题全集映射通过仍不能证明行为去向完整。',
 '将这两节登记为真实行为单元或精确并入同验收边界的既有功能行，保留原有ID；给出其去向/归属/问题并更新源选择器和view，禁止改正文或仅改metadata_reason让脚本通过。')
finding('POK-S02','P2','Shadow跨战斗/成长/主动道具界面未拆协作',[484,485,487,488],[
 {'source':'pokemon-rules/wp23-shadow-hyper-and-purification.md','lines':[32,59]},
 {'source':'pokemon-rules/wp23-shadow-hyper-and-purification.md','lines':[74,129]},
 {'source':'test-catalog/pokemon-rules-wp19-21-22-23-34.md','lines':[175,218]}],
 '当前四行均框架实现、伙伴框架/MZ、无Showdown和相应原型；正文却含入场/Call/战后量表快照、战斗经验EV暂存、战斗香资格复检退款、持久招式改变不重建场上副本。486的Hyper协作不覆盖这些不同源区间。',
 '保留框架持久字段与净化业务，按真实交界拆出或改为协作候选，绑定PROTO-IN-BATTLE-GROWTH/PROTO-BATTLE-ITEM及捕获后快照问题；补WP28/WP40等必要消费者依赖；未知仍待原型，不要求先跑原型才能接受粗标。')
finding('POK-S03','P2','漫游复用个体与逃跑结果写回被框架单方吞并',[519],[{'source':'pokemon-rules/wp37-roaming-and-poke-radar.md','lines':[67,80]},{'source':'test-catalog/pokemon-rules-wp31-32-37-38.md','lines':[104,110]}],
 '同一持久个体跨战复用，HP/PP/状态/持物取真实终局结果，含自然回复、对方不还原、总是逃跑、决定0–5与外层布尔/终结记录不同。该行仅框架、无Showdown、无PROTO-ESCAPE，依赖也无WP41。',
 '拆出开战/持续个体映射、战斗结果/逃跑/正常及异常交接的协作候选，关联WP41/42及逃跑原型，明确框架持久状态与Showdown战斗输出的所有者。')
finding('POK-S04','P2','持久异常与持物提交没有明确两端责任',[543,571,574,576,577,579],[
 {'source':'pokemon-rules/wp44-statuses-stat-stages-and-immunities.md','lines':[13,28]},
 {'source':'pokemon-rules/wp50-held-item-triggers-and-consumption.md','lines':[13,32]},
 {'source':'pokemon-rules/wp50-held-item-triggers-and-consumption.md','lines':[72,133]},
 {'source':'pokemon-rules/wp50-held-item-effect-coverage.md','lines':[30,31]},
 {'source':'pokemon-rules/wp50-held-item-triggers-and-consumption.md','lines':[153,170]}],
 'Showdown候选适合临时战斗计算，但这些行实际约束持久异常计数、C/I/R/P/Belch写穿与还原记录、LEPPA先持久槽后异身份战斗槽强写、被动/背包两类资源、已消费负选择和世界持物输入。仅列伙伴框架而不说明状态/资源归属无法表达边界；571还把578已列协作的Exp/EV两族整体写成Showdown。',
 '保留纯计算/资格的Showdown候选；对持久写穿、物品/PP两端同步、成长和世界结果拆分或明确协作职责，补WP20/28/42等依赖及对应行为问题。被动持物不扣背包应与主动道具原型分别表述。')
finding('POK-S05','P2','同节UI/资源/宿主时序未按独立验收边界拆分',[465,489,505,520,522,580,582,585,590,591,596,598,600,601,608,611],[
 {'source':'pokemon-rules/wp21-dynamic-forms-and-display.md','lines':[250,278]},
 {'source':'pokemon-rules/wp23-shadow-hyper-and-purification.md','lines':[130,185]},
 {'source':'pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md','lines':[98,109]},
 {'source':'pokemon-rules/wp37-roaming-and-poke-radar.md','lines':[81,96]},
 {'source':'pokemon-rules/wp37-roaming-and-poke-radar.md','lines':[117,158]},
 {'source':'pokemon-rules/wp53-safari-and-bug-catching-contest.md','lines':[23,48]},
 {'source':'pokemon-rules/wp53-safari-and-bug-catching-contest.md','lines':[114,148]},
 {'source':'pokemon-rules/wp53-safari-and-bug-catching-contest.md','lines':[214,257]},
 {'source':'pokemon-rules/wp60-berry-plants.md','lines':[65,135]},
 {'source':'pokemon-rules/wp61-field-passive-effects-and-blackout.md','lines':[22,57]},
 {'source':'pokemon-rules/wp61-field-passive-effects-and-blackout.md','lines':[71,94]},
 {'source':'pokemon-rules/wp61-field-passive-effects-and-blackout.md','lines':[120,173]},
 {'source':'pokemon-rules/wp62-pokedex-records-regions-and-content.md','lines':[147,178]},
 {'source':'pokemon-rules/wp69-voltorb-flip.md','lines':[47,60]}],
 '这些段落实际包含按键仲裁、编辑/搜索/标记、取消、资源请求/回退、精确等待、地图场景门/转移、暂停微更新、普通退出前保存或重复释放。不能用“本篇持久领域状态”这一重复依据将整节留框架；已有462/610等MZ拆分说明清单允许且需要这种不同验收边界。',
 '只在真实跨去向/验收界面处拆子节（无需逐句编号）：框架保留领域状态/预算/规则，MZ明确输入、表现、资源和生命周期；对调试子节关联DEC-SPECIAL-AND-HOST-SCOPE。父行line_ranges排除新子行，原ID保留。')
finding('POK-S06','P2','进化演出整节承包了领域提交',[492],[{'source':'pokemon-rules/wp31-basic-evolution.md','lines':[156,192]}],
 '492把§5全部列MZ。§5.1确为动画/取消，但§5.2–5.4还规定统计、消耗持物、额外个体克隆/入队/扣球、物种/HP重算、图鉴及学招。MZ/框架伙伴列与一句联调依据没有分出独立领域验收。',
 '至少按§5.1与§5.2–5.4实际责任拆分或精确描述领域提交与演出交接，保留取消与消息等待前缀顺序；不把全部持久行为归表现实现。')
finding('POK-S07','P3','纯证据/向量/范围段被制造为实现功能',[478,480,482,500,539,553,573,618],[
 {'source':'pokemon-rules/wp22-transformation-data.md','lines':[75,77]},
 {'source':'pokemon-rules/wp23-shadow-data-and-vectors.md','lines':[37,60]},
 {'source':'pokemon-rules/wp23-shadow-data-and-vectors.md','lines':[239,241]},
 {'source':'pokemon-rules/wp32-context-inputs-and-scenarios.md','lines':[124,137]},
 {'source':'pokemon-rules/wp44-effect-coverage.md','lines':[5,10]},
 {'source':'pokemon-rules/wp46-damage-healing-coverage.md','lines':[83,86]},
 {'source':'pokemon-rules/wp50-held-item-effect-coverage.md','lines':[69,71]},
 {'source':'pokemon-rules/wp70-lottery.md','lines':[54,58]}],
 '这些源节是来源、审计方法、覆盖范围、固定测试向量或冻结依赖/开放问题，没有独立待实现能力。它们却被赋destination/stage/implementation，而实际行为“未知效果回退/彩票匹配”反被概念关键词降级，语义口径不一致。',
 '保留这些已登记稳定ID的历史导航/处置，不删除或重编号来通过；将当前记录按合同标明为元数据/验收来源并精确关联现有行为。若schema不能表达该身份演进，先增明确迁移/继承设计并验证。')
finding('POK-S08','P3','作者内容缺省/校验与战斗配置被同标Showdown',[537],[{'source':'pokemon-rules/wp43-types-accuracy-and-damage.md','lines':[159,166]}],
 '该节既有战斗独立开关，又有Type/Move作者输入缺省、Category×Power编译校验、本地化Name/Description消费和WP03/04/08的内容约束；目前通篇主要战斗计算的模板依据无法解释这些作者内容由谁拥有。',
 '按内容作者/编译/本地化与战斗规则输入边界拆分或明确框架内容所有权及Showdown映射，依赖关联WP03/04/08，保留数据一致不等于行为覆盖的限定。')
failed={int(v['feature_id'].split('-')[1]) if 'feature_id'in v else 0 for v in []}
failed={int(x.split('-')[1]) for f in findings for x in f['feature_ids']}
byid={}
for f in findings:
 for fid in f['feature_ids']:byid.setdefault(fid,[]).append(f['id'])
features=[f for f in m['features'] if '/pokemon-rules/' in f['source']['document']]
results=[]
manifestlines=get(P+'routing-manifest.json').decode().splitlines()
line_byid={re.search(r'FR-\d+',l).group():n for n,l in enumerate(manifestlines,1) if '"feature_id": "FR-' in l}
viewlines={x['feature_id']:x['view_line'] for x in e['view_checks']}
for f in features:
 no=int(f['feature_id'].split('-')[1]);fid=f['feature_id']
 results.append({'feature_id':fid,'verdict':'FAIL' if no in failed else 'PASS','reason':notes[no],'finding_refs':byid.get(fid,[]),'source_document':f['source']['document'],'source_heading':f['source']['heading'],'source_line_ranges':f['source']['line_ranges'],'destination':f['future_plan']['destination'],'manifest_line':line_byid[fid],'generated_view_line':viewlines[fid],'source_identity_verdict':'PASS','status_separation_verdict':'PASS','upstream_binding_verdict':'PASS'})
status={'PASS':sum(x['verdict']=='PASS'for x in results),'FAIL':sum(x['verdict']=='FAIL'for x in results),'待查':sum(x['verdict']=='待查'for x in results)}
inputs=['AGENTS.md',P+'README.md',P+'review-prompt.md',P+'routing-manifest.json',P+'section-coverage.json',P+'views/pokemon-rules.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/DELIVERY.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/cloud-eighth-update-handoff-prompt.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batch-assignment.json']
inputids=[{'path':p,'sha256':hashlib.sha256(get(p)).hexdigest(),'bytes':len(get(p))}for p in inputs]
record={'schema':'r8-pokemon-independent-review.v1','reviewer_task':'/root/pokemon_semantics','candidate_commit':C,'formal_tree':e['formal_tree'],'outcome':'FAIL_FIXED_BASELINE_COARSE_ROUTING','outcome_scope':'仅pokemon-rules 27正文及对应4静态测试目录；不代表全仓总审，不是最终整改验收','requested_configuration':'父任务请求gpt-6.1-sol/ultra/default；本子任务继承父配置','actual_configuration':{k:'UNVERIFIED'for k in ['model','effort','service_tier','speed','Fast']},'counts':e['counts'],'feature_verdict_counts':status,'findings':findings,'results':results,'documents':e['reading_ledger'],'input_identities':inputids,'catalog_review':[{'document':d['path'],'verdict':'PASS','reason':'已完整语义读所有静态案例与追加向量；作为验收设计元数据关联领域功能，未标为已执行或已实现。','headings':d['heading_count'],'read_ranges':d['full_semantic_read_ranges']}for d in e['reading_ledger']if '/test-catalog/'in d['path']],'pending':['Showdown固定版本/世代/格式及所有原型未运行，目标行为兼容仍待验证','Shadow、特殊玩法和调试等目标范围仍待用户明确决定，未自动排除','R8-U03/U05/U06正式整改整合后按新精确commit回填再复核','全仓schema/validator/隔离/main保护及远端发布由父审负责，本子报告不冒称已独立完成该全局范围']}
(O/'pokemon-results.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
md=['# pokemon-rules 固定基线独立语义复审','',f'结论：**FAIL**。固定候选 `{C}`；正式子树 `{e["formal_tree"]}`。31份负责文件全部全文阅读：27正文4,919行、4静态测试目录1,144行，共526有效标题；165功能行/165生成view行全部逐项复审。每项判断见 `pokemon-results.json`，PASS仅表示该行粗标在本轮静态范围内合理，绝非Showdown已兼容或实现/验收已完成。', '',f'逐项结果：PASS {status["PASS"]}；FAIL {status["FAIL"]}；待查 {status["待查"]}。另有2处真实行为被概念元数据吞并，不能由现有165行通过机械计数免除。','', '实际模型、effort、service tier、速度及Fast没有权威执行echo，均为UNVERIFIED；本子任务独立于作者，未运行Ruby、参考游戏、Showdown、宿主、框架或业务向量。用户clean-document-revision仅作为作者正文纪律读取，没有伪称用于审计报告写作。','', '## 可复现问题','']
for f in findings:
 md.extend([f'### {f["id"]} · {f["severity"]} · {f["title"]}','',f['reason'],'','功能：'+(', '.join(f['feature_ids'])or'现有功能选择器外的源行为；见相关文档元数据映射。'),''])
 for s in f['evidence']:
  path='deliverables/final-specification-set/'+s['source'];a,b=s['lines'];md.append(f'- `{path}:L{a}–L{b}`')
 md.extend(['','必要修正：'+f['necessary_fix'],''])
md.extend(['## 机械核对与阅读证明','','独立脚本 `pokemon-static-audit.py` 只读固定Git对象/Markdown/JSON；正文/交付/候选逐字节相同；31文件SHA/blob、526标题level/title/line/anchor/hash、165功能单元SHA与选择器、165view行集合/主要字段投影及相关批次保守写集绑定均无机械差异。原始stdout/exit见 `pokemon-command-evidence.json`；细证见 `pokemon-static-evidence.json`。未导入作者routing.py代替独立解析。','','生成view全部行通过字段投影核对；重复rationale/questions/state按完整去重字段读取，来源fact_excerpt由完整正文阅读验证，未将工具成功当语义PASS。全部源正文分块输出；工具出现的WP21、WP22、WP23、WP34截断处均随后补读。四catalog全部1–EOF阅读，无未读段。','','| 文件 | 全文已读行 | 标题 | 功能 | SHA256 |','| --- | ---: | ---: | ---: | --- |'])
for d in e['reading_ledger']:md.append(f'| {d["path"].split("/")[-1]} | 1–{d["lines"]} | {d["heading_count"]} | {d["feature_count"]} | `{d["sha256"]}` |')
md.extend(['','## 归属、状态及后续边界','','捕获FR-000525–531正确保留PROTO-CAPTURE，529把战后接收归框架仍保留交接门；战斗内能力重算/HP刷新457–458、形态调用464、Mega/Primal469–474、战后成就502–504与特殊模式581/583都允许在未知原型条件下作为协作粗标。纯战斗数学/临时状态不能因本文指出持久交界就一概改成框架。','','本域165行均去向待验证、阶段待定、未实现、未验收、排除0；没有来源引用升级为Showdown兼容证据。固定源身份、current适用快照分开，原ID未被本复审改动。R8-U06绑定WP19与对应catalog；R8-U03绑定WP60；R8-U05绑定WP61；正文23条功能行的整篇保守绑定及待整改状态正确。U07是历史overlay，未把它虚构成此域正式正文写集。精确章节整改影响仍须接收上游新候选后差分。','','所有问题仅要求修订规划清单/映射/去向边界，不要求修改正式正文、修参考或先运行原型。来源事实、异常前缀、静态向量、未选范围与历史身份均须保留。最终必须以协调任务提供的正式整改精确commit重新校准并独立验收；本报告不能提前宣称第八轮最终完成。'])
(O/'pokemon-report.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'feature_counts':status,'findings':len(findings),'report':str(O/'pokemon-report.md'),'results':str(O/'pokemon-results.json')},ensure_ascii=False))
