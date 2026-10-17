import collections
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).resolve().parent
CANDIDATE = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
PLAN = ROOT / 'planning/implementation-routing/r8-20261017'
manifest = json.loads((PLAN / 'routing-manifest.json').read_text())
sections = json.loads((PLAN / 'section-coverage.json').read_text())['sections']
scoped = lambda p: any('/' + d + '/' in p for d in ('engine-overworld', 'user-interface'))
features = [f for f in manifest['features'] if scoped(f['source']['document'])]

# 以下逐行意见来自本上下文已完成的全文阅读；程序只负责序列化及静态身份核对。
REVIEW = '''
323|PASS|地图ID、连接坐标与邻图驻留归宿主地图接入合理；临时查询副作用须依通知和地牢规则验证。
324|PASS|边缘/显式/读档三入口的落位、通知与载具时序属于地图接入编排；不把正常返回当运行证据。
325|PASS|地图更新、邻图实例与地点提示属于接入生命周期；命名材料副作用仍须消费本地化合同。
326|FAIL|恢复两分支与局部记录消费直接依赖WP09存档门，候选仅列WP03/WP05，未登记必要的恢复责任依赖。|WU-06
327|PASS|默认地图接入政策与配置变体可随地图主行保留MZ候选；无自动排除调试能力。
328|PASS|缺图两阶段及取模等失败边界是地图接入的可观察合同；状态仍待验证。
329|PASS|图块、角色、玩家、跟随者五层通行入口是宿主地形接入，领域消费者没有据此被声称实现。
330|PASS|移动开始/完成、输入调度、碰撞链由地图接入承载合理；全局计步通过WP06引用。
331|PASS|载具旗标、上水前跳失败与转移后收尾需要MZ和框架接入；双方已列为伙伴。
332|PASS|本节明确守卫检查点与领域主规则交界，MZ承接许可输入消费可成立。
333|PASS|速度、跑法和地图元数据配置属于同一移动接入验收边界，无需逐配置拆行。
334|PASS|碰撞/岩架/冰滑/上岸失败均是移动入口可观察结果，归MZ候选合理。
335|PASS|解释器结束、续行消费和返回控制是事件接入职责；未声称标准命令全兼容。
336|PASS|命令矩阵作为宿主事件兼容整体粗标合理，完整业务规则留给各领域规格。
337|PASS|事件页、触发、冷却和消去入口形成事件接入边界；主规则没有被运行验证。
338|PASS|等待、身份绑定和具名过场跳过是宿主解释器调度合同，MZ候选合理。
339|PASS|矩阵要点重复主解释器兼容责任，独立粗行可用于同一验收目录，未造成跨去向覆盖。
340|PASS|NPC感知、事件跟随和门路线为地图角色接入，持久数据通过框架共同承接合理。
341|PASS|事件/跟随配置变体仍属于同一地图接入边界。
342|PASS|失联继续、深度和脚本异常是解释器接入失败合同，未被升级成运行通过。
343|PASS|路线安装、等待与推进语义是宿主路线调度，可作为单一MZ候选。
344|PASS|45项路线分派以角色运动/显示入口为主，矩阵粗标合理且与主事件命令分开。
345|FAIL|本节只有取证口径和通行规则归属说明，没有独立待实现能力；应作为路线功能的元数据。|WU-07
346|待查|输入参数、种子全局副作用与地图建立混合；MZ编排可成立，但应明确框架随机/参数所有权，不能仅凭地图目录决定。
347|PASS|尺寸、迷宫、房间、连通和墙修复是独立布局规则；框架候选及与后续宿主摆放分界合理。
348|待查|布局符号到图块和256邻接映射是行为数据，最后写地图是宿主操作；需澄清此行是否只负责接入还是拥有映射规则。
349|待查|房间间距与重试是独立规则，事件/玩家坐标写回属宿主；当前伙伴同时列框架/MZ但未给明确分工。
350|PASS|地牢默认标记与配置变体可在整体验收中保留MZ候选；固定种子未冒称跨实现一致。
351|PASS|种子/构造/生成/摆放失败前缀保留为地牢整体接入验收，引用布局主行。
352|PASS|路径存在、扩展名、窗口皮肤与宿主资源加载属于MZ资源接入；内容身份由WP03引用。
353|PASS|内容到媒体的命名/变体回退属于资源接入合同；动态形态写入仍依赖领域读取而非资源层重做。
354|PASS|缓存有效期、共享与各加载入口失败是宿主资源职责，MZ候选恰当。
355|PASS|音频请求、登记、暂停/记忆/默认覆盖与格式边界是宿主音频接入，未以文件存在证明发声。
356|PASS|资源与音频配置仍是MZ接入验收输入，SF2声明未选定未来实现架构。
357|PASS|各资源失败/回退的来源事实保持，未把缺图一概归一，MZ候选合理。
358|FAIL|本行只覆盖特殊注册，而§1包装的战斗标记、音乐记忆、四预置清理与世界恢复未形成行为单元；章节覆盖仅元数据关联不能替代去向。|WU-01
359|PASS|五组资源资格与演出选择是战前表现接入；调用类别未被反推成真实战斗类型。
360|PASS|闪屏、截图、自编排序列属战前MZ表现，分阶段完成合同清楚。
361|PASS|时长覆盖、中断和宿主重试属于过渡接入失败边界；无需拆分数学时长为战斗引擎功能。
362|PASS|日夜/类别/位置选择默认效果是表现选择规则，MZ候选可成立。
363|PASS|正常返回与异常未恢复、初始化失败等属于战前接入，仍待运行验证。
364|PASS|地图绘制、滚动、自动图块与量化属于MZ视觉接入；镜头数学为显示输入合同。
365|PASS|逻辑层、角色、反射、基点、阴影和附着动画均为可观察表现接入；故障前缀保留。
366|PASS|天气粒子/屏幕/图片/计时器显示属于MZ表现；天气领域身份由框架输入。
367|PASS|可见保持、过渡和轨道时序属于MZ接入，业务状态保留没有被当作容器架构。
368|PASS|世界表现默认配置可跟随同一验收边界，未冒称真实素材存在。
369|PASS|资源、显示许可与天气校验失败为表现接入验收，状态诚实。
370|PASS|时钟谓词、月份季节和月相星座算术属于框架规则，排除色调应用子节合理。
371|PASS|色调缓存与地图场景/outdoor应用门含宿主投影，MZ候选合理。
372|待查|天气概率/意图设置和粒子显示合在一行，框架天气选择与MZ显示边界未具体说明；不直接判已兼容。
373|待查|身份/类别归框架合理，但子节同时包含Snow扰动、Storm闪屏与Sun帧更新；仅框架伙伴与MZ验证提示需进一步明确职责。
374|待查|十二族资格、状态提交与演出混合；保留徽章和摇树算术拆分是进步，其余框架/宿主职责仍需具体边界。
375|PASS|徽章计数/编号资格是独立框架领域规则，拆分合理。
376|PASS|摇树概率与私有ID输入为独立框架算术，未将数值吻合当会话覆盖。
377|PASS|时间/天气/场地不变量可作为相邻已分拆主行的共同验收输入；MZ伙伴含框架。
378|PASS|场地失败与取消主要是地图调用编排，领域规则引用保留，待验证状态合理。
379|PASS|场地与天气默认配置可跟随宿主集成候选；首版没有被批准。
380|PASS|鱼竿面向地形/当前出边检查及物品回调入口属于MZ世界接入，遭遇与库存引用领域主行。
381|待查|咬钩阈值/特性/随机消费与输入时间窗同节；MZ可编排，但需要具体框架随机/概率职责而非通用模板。
382|PASS|四类结果与统计提交时点是钓鱼交互出口，框架/MZ伙伴共同承接可成立。
383|PASS|公共事件替代、内置表现与临时旗标正常清理属宿主接入；未补异常必恢复。
384|FAIL|本行明确依赖捕获球倍率、战斗环境/开场和结果归一，但候选只有WP27/WP36/WP59，缺捕获与战斗消费者责任定位。|WU-06
385|PASS|钓鱼不变量与正常清理可关联本交互整体MZ验收；未将成功钓到等同产生战斗。
386|PASS|出边/无表/取消/超时/公共事件失败属于世界交互接入，状态仍待验证。
387|PASS|鱼竿配置和默认概率可由同一交互粗行消费；最终数值与宿主手感分开。
619|PASS|文本颜色和恢复栈是绘制层表现语义，MZ候选合理。
620|PASS|字形/字体回退是宿主绘制输入，未将字体存在作为像素证明。
621|PASS|对齐、词边界换行和长词边界是排版表现合同，MZ候选恰当。
622|PASS|图像标记测量/绘制及文尾未消费属于表现入口边界。
623|PASS|识别无动作是格式兼容行为，应保留在MZ绘制候选而非自动排除。
624|PASS|§6.1实体解码的入口差异为真实绘制行为，当前范围包含该子节；不是只有口径的虚假功能。
625|PASS|消息替换、四态、共享消息忙暂停和皮肤时机属交互呈现；业务前缀引用领域调用者。
626|PASS|选择取消编码与同轮竞争是UI采样出口，MZ候选合理。
627|PASS|数量参数、逐位编辑及确认/取消属于通用交互合同，未声称业务写入自动成功。
628|PASS|宿主按键/文本输入、光标、预览及图标相位归MZ接入合理；设备映射未被声称验证。
629|PASS|解释器等待、地图微更新、正常出口清理是宿主UI交界。
630|PASS|通用消息默认选项与支持能力属于同一MZ交互边界，没有排除未知鼠标能力。
631|PASS|取消值、资源失败及正常/异常清理事实保留为UI接入验收。
632|PASS|Pokégear按钮与FLY返回链主要是导航编排，MZ候选合理。
633|PASS|区域地图浏览/编辑/飞行选择为MZ地图交互，领域飞行资格与执行通过WP59引用。
634|待查|联系人数据/生命周期归框架正确，但§4.1电话画面与实时拖动同在该行；应明确MZ呈现消费边界。
635|PASS|信号/呼入/冷却、版本与对话选择是电话业务，框架候选合理且MZ仅呈现消费者。
636|PASS|点唱机选曲与默认覆盖属宿主音频交互，遭遇旗标通过WP36领域消费者引用。
637|PASS|工具入口和电话/点唱机不变量可作为相邻主行验收关联；没有新范围批准。
638|PASS|区域回退、公共事件与音频目录失败为交互接入边界，已保留联系人写入前缀。
639|PASS|控制帮助内容、语言选择与页面构造是MZ表现。
640|PASS|翻页、回调摘挂和末页过渡属于帮助场景接入。
641|PASS|BACK空回调、同轮优先序和只读边界属于帮助交互。
642|PASS|标题/载入选择及预览可归MZ导航；正文明确存档读写归WP09/WP10主责。
643|PASS|确认、反馈和退出前保存结果消费是MZ导航边界，持久层主规则已有依赖。
644|PASS|选项即时预览、关闭再应用与语言跳转属于导航接入；存档归属保留。
645|PASS|暂停菜单可见条件、返回和世界请求消费属MZ导航。
646|PASS|PC菜单与子导航是MZ入口，储存/信箱领域状态通过主规格引用。
647|PASS|快捷候选、两列游标、确认/执行与关闭主要为交互编排，框架持久字段消费者保留。
648|PASS|主导航默认配置与支持门属于同一粗标，不等于首版批准。
649|PASS|存档/菜单失败反馈与返回去向为导航接入边界，R8-U01待整改后核对未被升级。
650|PASS|训练家卡场景链与资源生命周期属于MZ表现。
651|PASS|性变/装束资源回退属于MZ资源选择。
652|PASS|正面字段格式与徽章展示属MZ显示；开始时间懒写入必须消费框架持久状态，但正文已明确引用WP09。
653|PASS|唯一BACK出口、懒写入例外与资源边界是训练家卡接入验收。
654|PASS|队伍入口/选择模式与Box Link桥为UI导航，规则主责通过WP25/WP26/WP28引用。
655|PASS|面板、导航与换位目标选择为MZ交互；旧索引失败需在接入联调验证而非修参考。
656|待查|成员命令、奶招和物品/邮件真实写入同节；框架规则已有引用，但候选未具体说明资源提交/失败前缀与MZ消息的所有权。
657|PASS|摘要页面、格式、个性描述与成员导航属于显示数据选择；不把动态形态读取宣称纯读。
658|PASS|招式/缎带/标记交互及写回触发点可由MZ消费领域操作；待验证而非直接拥有领域数据。
659|FAIL|学习/替换与重学完整资格、招式写入及统计直接引用WP30，但此行依赖未列WP30；仅WP17/WP25/WP26/WP28不足以定位学习主责。|WU-06
660|PASS|UI选择与既有业务写入分层作为主行验收关联合理；没有把取消说成全局回滚。
661|PASS|满包/邮件/零候选/FLY桥等交互拒绝和忙暂停属于MZ消费者验收。
662|PASS|盒子入口与四模式、临时储存旗标属交互导航；容器操作引用WP25。
663|PASS|盒/队伍光标、暂持和持久当前盒的操作触发点属接入状态机。
664|待查|取出/存入/拿起/交换/释放真实提交与MZ动画同表；主领域WP25已有依赖，但应明确提交失败与表现失败边界而非只写模板。
665|PASS|图鉴入口区域菜单和观看字段触发点属于UI导航，WP62为记录主责。
666|待查|列表/搜索UI与持久模式Start先写、无结果取消保留混合；WP62已有依赖，但需具体框架提交/MZ草稿职责。
667|待查|条目显示和形态首轮查看即写同节；MZ呈现合理，但记录覆盖应明确由WP62功能消费而非UI重新实现。
668|PASS|集合与图鉴不变量均引用领域主规则，并保留查看写入，粗行可作MZ消费者验收。
669|PASS|盒/图鉴失败及哨兵是界面入口可观察结果，领域规则引用保持。
670|PASS|背包四种入口及过滤游标保存恢复为MZ交互。
671|PASS|口袋游标与排序触发/取消是UI操作时点，持久库存语义引用WP27。
672|PASS|命令菜单与使用返回分层是MZ导航消费，扣物规则留WP28。
673|待查|PC存取/丢弃的库存先后和消息前缀同节；WP27引用正确，仍需把框架提交与MZ等待的具体验收职责登记。
674|待查|商店买卖、库存原地过滤/回退与相机表现混合；WP29已是领域主责，当前行缺精确职责/关联功能说明。
675|PASS|三类交易写入形状作为相邻主行的界面验收约束，MZ候选可成立。
676|PASS|丢弃提示失败前缀、背包空和BP显示边界属MZ消费者验收，未冒称资源已恢复。
677|FAIL|含逃跑尝试/登记退款/阶段及终局状态，整节MZ且无PROTO-ESCAPE或Showdown职责；需拆出领域交界或精确绑定已有协作行。|WU-03
678|FAIL|菜单显示与Mega资格、目标合法性/登记同节；未明确战斗引擎与UI采样分工，不能以MZ通用rationale覆盖领域验收。|WU-03
679|FAIL|登记扣物、复检退款残留、终局二退是持久背包/战斗选择协作，整节MZ且原型为空；需保留UI子节并绑定PROTO-BATTLE-ITEM。|WU-03
680|FAIL|换入换出资格/终局替补/逃跑与显示队伍映射混合；需标明领域引擎与框架责任，不能只有MZ输入问题。|WU-03
681|FAIL|持久招式与战斗招式两次提交、升级同步和暂停是成长协作核心；当前MZ行无PROTO-IN-BATTLE-GROWTH。|WU-03
682|FAIL|投球、敌队移除、接收队列、满队送盒及战斗记忆回填跨三方状态；整节MZ且无PROTO-CAPTURE或协作方。|WU-03
683|PASS|消息、HP/经验条、动画查找/播放与时序为MZ表现；已提交领域反应只是消费者证据，不冒称兼容。
684|FAIL|Safari/捕虫/Palace/Arena与回放覆写不只是表现；目标范围需特殊玩法决定且领域覆盖需引擎协作，当前无对应决策/原型。|WU-03|WU-05
685|PASS|默认选项与规则输入本身可作为MZ战斗表现配置验收；未批准首版。
686|PASS|投球/替补/动画缺失等失败应消费主规则，MZ候选只是界面失败呈现；R8-U06待整改后核对保留。
687|待查|进化演出与物种/后置动作提交混合；引用WP31/WP32合理，需具体说明MZ只呈现与框架提交的边界。
688|待查|孵化显示前后领域提交与命名同节；WP35已依赖，需明确框架提交和MZ表现失败前缀的所有权。
689|PASS|交换演出和不可取消收尾为MZ交互；最终替换与进化规则引用WP26/WP32。
690|FAIL|净化室Shadow特殊体系范围仍待用户决定，当前行未关联DEC-SPECIAL-AND-HOST-SCOPE，且统一MZ掩盖容器删除/成长/净化提交。|WU-05
691|FAIL|名人堂历史克隆、容量裁剪、编号递增和PC门是独立持久规则，与逐成员演出同节；需要框架记录责任和MZ呈现拆分。|WU-04
692|PASS|片尾滚动/输入/恢复及完成标记触发点为宿主场景接入；持久化不被冒称已落盘。
693|PASS|生命周期配置变体可关联主规则作为MZ演出验收输入，特殊Shadow范围另由WU-05处理。
694|PASS|演出取消、失败前缀和未证宿主清理保留，MZ消费者验收不等于领域已实现。
695|FAIL|固定16格损伤矩阵与特殊次数是独立活动规则，不是MZ表现；应框架承担并保留特殊玩法待决策。|WU-02
696|FAIL|对手动作权重与随机消费是独立活动决策规则，应与台词呈现/MZ时间分开。|WU-02
697|待查|临时生命/玩家0优先终局和不可取消输入同节；需明确框架会话状态与MZ采样职责。
698|PASS|地图角色路线、速度/朝向与等待/异常恢复属于MZ宿主接入，特殊玩法决定已登记。
699|待查|转轮时间/停止是MZ，但初始与滑移抽样概率属规则；需明确随机框架与视觉转轮分工。
700|PASS|有效线与奖项优先级拆到框架合理，特殊玩法未自动纳入首版。
701|待查|下注/重玩和输入竞争同节；已列框架伙伴但未明确会话账与MZ控制职责。
702|FAIL|余额离场覆盖、净差统计和部分写入是持久资源规则，不是MZ表现；需框架提交职责与支付动画拆分。|WU-02
703|PASS|入口拒绝和场景异常前缀可作MZ接入验收，余额提交责任需随WU-02修订。
704|FAIL|本节仅冻结依赖、配置及未决，没有独立实现能力，应作为老虎机主行元数据。|WU-07
705|FAIL|22位置有序转轮和频次是中奖规则的行为数据，不能仅因UI目录归MZ；应与FR-000700框架规则明确关联。|WU-02
706|FAIL|铁障碍形状目录是挖矿摆放规则数据，MZ不是规则所有者；主物品61行也被前导元数据漏出。|WU-01|WU-02
707|FAIL|内容与来源边界只是48身份/口袋的来源资格，应关联候选规则；该行不能替代前导61项有序候选的去向。|WU-01|WU-07
708|PASS|候选权重、身份去重和互斥规则归框架合理，仍待用户选择玩法范围。
709|FAIL|加权抽样、占格摆放/重试及层厚分布是独立规则算法，应框架承担，显示位置才交MZ。|WU-02
710|FAIL|镐/锤削层矩阵、铁阻挡与耐久是玩法规则；需与输入/动画忙门分拆到框架和MZ。|WU-02
711|FAIL|坍塌优先级、揭露待领、逐件入包和非幂等结算是框架会话/库存规则；与表现统一归MZ不适当。|WU-02
712|PASS|闪光中断和领取前缀是MZ接入验收边界，框架提交职责应随WU-02明确。
713|FAIL|冻结依赖、固定配置和未决列表不是独立实现功能，应元数据关联挖矿规则/表现主行。|WU-07
714|FAIL|棋盘状态模型、完成谓词与资源参数混合；状态/谓词应框架承担，资源切图/MZ另列。|WU-02
715|FAIL|七模式合法动作与完成规则为独立玩法，不能用特殊UI目录rationale归MZ。|WU-02
716|FAIL|合法动作对排列/角度的提交是玩法规则，按键与导航是MZ接入；此节应区分两种责任。|WU-02
717|FAIL|洗牌、可解性筛选与随机入口是框架规则；不是MZ表现。|WU-02
718|待查|完成/取消规则可由框架消费，动画等待是MZ；当前同节责任不够明确，需避免让MZ成为局面权威。
719|PASS|资源回退、箭头门、切图和音效是MZ表现，特殊范围决定保留。
720|FAIL|局面权威、动作不变量与可达奇偶性属于框架玩法规则，应关联规则主行而非MZ实现。|WU-02
721|FAIL|尺寸/非法模式/可解性缺陷是规则输入域，资源失败和动画输入阻塞为MZ；需分开责任。|WU-02
'''
reviews = {}
for line in REVIEW.strip().splitlines():
    number, status, reason, *finding_ids = line.split('|')
    reviews[f'FR-{int(number):06d}'] = {'status': status, 'reason': reason, 'finding_ids': finding_ids}
assert set(reviews) == {f['feature_id'] for f in features}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

documents = []
identity_errors = []
section_checks = []
for d in manifest['documents']:
    path = d['source']['path']
    if not scoped(path):
        continue
    data = git('show', CANDIDATE + ':' + path)
    work = (ROOT / path).read_bytes()
    source = git('show', 'fd1df570cad987dc3852a3b958f03916e317f7fe:' + path)
    delivery = git('show', '4575e80d041ab0c74a42e2e36399d05791dbaa5b:' + path)
    lines = data.decode().splitlines(keepends=True)
    local_sections = [s for s in sections if s['path'] == path]
    # Independent ATX heading collection, excluding fenced code; compare exact line/title/level.
    parsed, fence = [], None
    for i, line in enumerate(lines, 1):
        fm = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if fm:
            symbol = fm[1][0]
            fence = symbol if fence is None else (None if fence == symbol else fence)
            continue
        if fence:
            continue
        h = re.match(r'^(#{1,6})[ \t]+(.+?)\s*$', line)
        if h:
            parsed.append((i, len(h[1]), re.sub(r'[ \t]+#+[ \t]*$', '', h[2])))
    expected = [(s['line_start'], s['level'], s['title']) for s in local_sections]
    ok = parsed == expected
    if not (work == data == source == delivery and sha(data) == d['source']['sha256'] and ok):
        identity_errors.append(path)
    documents.append({'document_id': d['document_id'], 'path': path, 'bytes': len(data), 'sha256': sha(data),
                      'git_blob': git('rev-parse', CANDIDATE + ':' + path).decode().strip(),
                      'line_count': len(lines), 'heading_count': len(parsed),
                      'read_ranges': [[1, len(lines)]], 'reading_status': 'FULL_BODY_READ_IN_CONTEXT',
                      'method': '分块原文全文读；截断输出已重读补齐。未执行源脚本/业务向量。',
                      'fixed_candidate_equals_worktree_and_source_and_delivery': work == data == source == delivery,
                      'independent_heading_line_level_title_match': ok})
    for s in local_sections:
        row = dict(s)
        row['review_status'] = 'PASS'
        row['review_reason'] = ('源章节已全文阅读；有效标题与映射存在；行为子节继承对应功能，不逐句强编号。'
                                if s['mapping_kind'] == 'behavior-unit' else
                                '源章节已全文阅读；治理/概念/依赖/测试/限制作为关联功能上下文成立，不产生运行信用。')
        if path.endswith('wp70-mining-data.md') and s['level'] == 1:
            row.update(review_status='FAIL', review_reason='H1前导L9–75含61候选权重/形状，只映射为元数据到铁障碍/来源边界；没有候选数据自身去向。', finding_ids=['WU-01'])
        if path.endswith('wp16-pre-battle-transitions.md') and s['line_start'] == 5:
            row.update(review_status='FAIL', review_reason='§1包装为完整行为合同，不能因标题含目的而只作元数据。', finding_ids=['WU-01'])
        if path.endswith('wp68-duel.md') and s['line_start'] == 15:
            row.update(review_status='FAIL', review_reason='§2包含初始化10生命、无取消/平局及准入守卫，应登记行为定位或明确从属规则。', finding_ids=['WU-01'])
        if path.endswith('wp69-slot-machine.md') and s['line_start'] == 9:
            row.update(review_status='FAIL', review_reason='§1有币盒/余额/上限三准入门和难度输入，不能仅以概念元数据承接。', finding_ids=['WU-01'])
        if path.endswith('wp70-mining.md') and s['line_start'] == 9:
            row.update(review_status='FAIL', review_reason='§1公开入口无费用/物品/地形/背包空间门和返回合同属于行为入口。', finding_ids=['WU-01'])
        section_checks.append(row)

results = []
for f in features:
    data = (ROOT / f['source']['document']).read_bytes()
    lines = data.decode().splitlines(keepends=True)
    ranges = f['source']['line_ranges']
    unit = ''.join(''.join(lines[a - 1:b]) for a, b in ranges).encode()
    unit_ok = sha(unit) == f['source']['unit_sha256']
    view_path = PLAN / 'views' / (f['source']['document'].split('/')[-2] + '.md')
    view_rows = [line for line in view_path.read_text().splitlines() if line.startswith('| ' + f['feature_id'] + ' ')]
    view_ok = len(view_rows) == 1 and f['future_plan']['destination'] in view_rows[0]
    state_ok = (f['destination_verification']['status'] == '待验证' and f['future_plan']['stage'] == '待定'
                and f['implementation']['status'] == '未实现' and f['implementation']['acceptance_status'] == '未验收'
                and f['future_plan']['exclusion_decision'] is None)
    r = {'feature_id': f['feature_id'], **reviews[f['feature_id']],
         'source_document': f['source']['document'], 'source_heading': f['source']['heading'],
         'source_anchor': f['source']['anchor'], 'source_ranges': ranges,
         'manifest_pointer': '/features/' + str(manifest['features'].index(f)),
         'destination': f['future_plan']['destination'], 'partners': f['future_plan']['partners'],
         'source_identity_and_unit_hash': 'PASS' if unit_ok else 'FAIL',
         'view_feature_occurrence_and_destination': 'PASS' if view_ok else 'FAIL',
         'independent_states': 'PASS' if state_ok else 'FAIL',
         'upstream_batches': f['upstream']['batches'],
         'upstream_status': f['upstream']['status'],
         'read_source_full_document': True}
    if not (unit_ok and view_ok and state_ok):
        identity_errors.append(f['feature_id'])
    results.append(r)

batch_data = json.loads((ROOT / 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batch-assignment.json').read_text())
batch_checks = []
for d in documents:
    expected = sorted(b['id'] for b in batch_data['batches'] if d['path'] in b['actual_target_write_set'])
    recorded = next(x for x in manifest['documents'] if x['document_id'] == d['document_id'])['upstream']['batches']
    rows = [f for f in features if f['document_id'] == d['document_id']]
    ok = expected == sorted(recorded) and all(sorted(f['upstream']['batches']) == expected for f in rows)
    if expected:
        ok = ok and all(f['upstream']['status'] == '待整改后核对' and not f['upstream']['accepted_events'] for f in rows)
    batch_checks.append({'path': d['path'], 'expected_batches': expected, 'recorded_batches': recorded,
                         'feature_count': len(rows), 'result': 'PASS' if ok else 'FAIL'})

payload = {'schema': 'independent-world-ui-routing-review/v1', 'candidate_commit': CANDIDATE,
           'source_commit': 'fd1df570cad987dc3852a3b958f03916e317f7fe',
           'delivery_commit': '4575e80d041ab0c74a42e2e36399d05791dbaa5b',
           'formal_tree': git('rev-parse', CANDIDATE + ':deliverables/final-specification-set').decode().strip(),
           'reviewer': '/root/world_ui_semantics',
           'configuration': {'requested_parent_model': 'gpt-6.1-sol', 'requested_parent_effort': 'ultra',
                             'actual_model': 'UNVERIFIED', 'actual_effort': 'UNVERIFIED',
                             'actual_tier': 'UNVERIFIED', 'actual_speed': 'UNVERIFIED', 'actual_fast': 'UNVERIFIED'},
           'scope': ['engine-overworld', 'user-interface'],
           'counts': {'documents_full_read': len(documents), 'source_lines_full_read': sum(x['line_count'] for x in documents),
                      'source_bytes_full_read': sum(x['bytes'] for x in documents), 'headings_checked': len(section_checks),
                      'features_reviewed': len(results), 'feature_verdicts': dict(collections.Counter(x['status'] for x in results)),
                      'section_mapping_verdicts': dict(collections.Counter(x['review_status'] for x in section_checks))},
           'identity_errors': identity_errors, 'documents': documents, 'feature_results': results,
           'section_results': section_checks, 'upstream_document_checks': batch_checks,
           'not_read_here': [
               'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md',
               'deliverables/final-specification-set/test-catalog/engine-overworld-wp16.md',
               'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'],
           'limits': ['本结果仅本分工；全局schema/工具负例/远端/隔离由root整合。',
                      '三个catalog由父任务另委新上下文；本子报告不授全文阅读信用。',
                      '未执行Ruby、参考游戏、业务向量、原型或未来框架。',
                      '全文语义阅读信用只授28篇正文；生成view逐功能行ID/去向和状态作机器核对，未伪称逐字人工阅读全文view。'],
           'conclusion': 'FAIL_FIXED_BASELINE_COARSE_CANDIDATE; FINAL_CALIBRATION_PENDING'}
(OUT / 'world-ui-results.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'candidate': CANDIDATE, 'counts': payload['counts'], 'identity_errors': identity_errors,
                  'batch_results': dict(collections.Counter(x['result'] for x in batch_checks))}, ensure_ascii=False))
