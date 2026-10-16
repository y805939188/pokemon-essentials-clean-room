# r6_c 有限独立接收报告

状态：**READY_FOR_PARENT_RECEPTION**。UPDATE_NOT_STARTED。

固定合同 `9a3eac8900fea93fee562d520a98edaf1e232fe6`；目标作者提交 `a96ec67a948e3fc86b25ad407cd977b6752e2d77`；B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`；参考 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。
实际独立上下文 `01a144a3-93e1-76b5-94f8-5183b7b5000d`，不同于目标作者 `01a143b2-d42d-7797-8bbe-c60266de7007`；自行 spawn 0。用户指定发布分支 `codex/r8-final-r6-c-20261016` 覆盖包内旧分支名，写入仅限本目录。

14 个完整七组合同及原提案、100 个完整案例（含父前提及复合回归）、33 条完整边、2 项既有 optional、PARTY004 完整 NO_REQUIRED 已逐项接收；本包必要可得未读对象 0。新增 required/optional/policy/limit/no-required 均 0。P0 原未读快照保留在 frozen-denominator，不冒充当前状态。

每项均反向核对当前 B8 实际条款和目录，R 的定位范围扩至必要方法结束及真实调用者。完整输入字段的同值部分仅经可逆精确别名接合，生成视图和 hash 本身不授阅读信用。逐 ID、逐案例的独立推导分别在 reception-ledger.json、case-reception.json；读片、身份及截断补读在 reading-ledger.json。

## 逐项接收

### GR6-O-001

等待/咬钩/窗口/上钩四阶段按到达守卫消费；加速另抽一次等待取小。普通成功4次、无遭遇或等待取消1次、未咬2次、超时3次、自动成功3次；开始/消息/动画/结束失败分别只留已到达前缀。计数先增，清理无ensure保证。

5–10执行段数+1且首空段；0.500无输入继续，下一轮0.510输入先于严格>超时；自动仍等输入，跳过最后随机和成功消息。直接等待不消费battles/遭遇；物品回调true后先battles+1再请求。全局公共事件true替代内置，解释器助手空返回仍内置，负ID门分入口。

已排除把窗口时长提前到咬钩前或动画异常后仍抽取、把成功true等同开战、把自动当作无输入；B8逐阶段及R5-FS成对入口均已覆盖。

接收案例：12。R 必要读片：18, 17, 03；B8：engine-overworld/wp60-fishing.md:37-88；engine-overworld/wp13-map-events-npc-followers.md:100；test-catalog/engine-overworld-wp11-15-59-60.md:392-409,638-641,677-678,696-712。

### GR6-O-002

每次update局部从0计，循环先+1；第101轮Graphics.update正常返回才清0，再查地图/等待/分派。终止清列表返回true，外层仍推进并再计空列表早退轮。

98注释无额外请求；99在终止后请求一次；100在终止前一次。116自行推进后false让出，下一update重新计数；106为计时等待且true，不能替代116对照。Graphics异常早于清0和后继分派；不额外Input.update，深度>100门独立。

最强反证99条看似未过阈值，但终止后仍有空列表轮；已按完整execute_command/command_end接合，未发现差异。

接收案例：6。R 必要读片：03；B8：engine-overworld/wp13-map-events-npc-followers.md:64-100；test-catalog/engine-overworld-wp11-15-59-60.md:714-725。

### R6-DX-COMP-001

运行中菜单先建消息窗，直接compile_all(true)；发现/兼容改写→PBS→动画→登记地图/公共事件→文本→消息。无启动main的导入、预删、局部诊断/清单删除/异常转换；正常返回才完成消息及释放。

唯一合法Status/Power40在条目校验拒绝，之前types/abilities等已保存，当前moves表可留新前缀、坏条不登记、旧moves.dat保持（直接入口）。启动同态仅诊断正常后尝试删除，Reset/SystemExit原抛，缺PBS早于清单建立另论。未登记007直接不导入，启动可导入，999排除。

旧启动条款在其入口仍正确；直接入口的不同失败前缀已单列。缺宿主Demo不满足合法成功夹具，不能用当前缺档否定条件合同。

接收案例：4。R 必要读片：39, 40, 41, 42, 44, 45；B8：generic-kernel/wp04-pbs-lifecycle.md:21-55,163-172,271-282；demo-dx/wp75-project-conversion-and-authoring-tools.md:35-62；demo-dx/wp72-debug-contexts-and-controls.md:267-275；test-catalog/generic-kernel-wp02-03-04.md:77-79；test-catalog/demo-dx-wp72-73-74-75-76-77.md:377-385。

### R6-DX-COMP-002

三个观察面分开：区域缓存A预载后直接编译合法B，档案B而编号/成员A；区域单项或全量反写消费A写PBS，档案仍B。冷缓存首次读B；编辑器总Yes档案C→清区域缓存→反写重读C，No不走此保存链。

动画编译从盘集合B建关联，有有效名才写两档案，不清预载集合/关联A；零有效名保旧盘M是另门。新Game_Temp使其区域/动画缓存重新读取具备前提，不清MapFactoryHelper独立连接/尺寸缓存。pbClearData定义不证明直接编译调用它；Reload system cache仅宿主请求。反写覆盖打开后失败可留部分PBS，不回滚B。

排除把文件重编译、重建临时会话、编辑器只清集合、宿主reload四入口并成广播失效。当前正文已覆盖这些最强相反解释。U14 primary仍交D接合。

接收案例：7。R 必要读片：02, 04, 05, 09, 12, 15, 36, 38, 40, 41, 42, 43；B8：generic-kernel/wp04-pbs-lifecycle.md:217-225,259-269；demo-dx/wp75-project-conversion-and-authoring-tools.md:44；demo-dx/wp74-battle-animation-authoring-and-exchange.md:417-446；demo-dx/wp72-debug-contexts-and-controls.md:267-273；demo-dx/wp73-a-content-editors.md:158-168；pokemon-rules/wp62-pokedex-records-regions-and-content.md:95-118；test-catalog/generic-kernel-wp02-03-04.md:80-85；test-catalog/demo-dx-wp72-73-74-75-76-77.md:386-390。

### R6-DX-COMP-003

普通分节在prep前只跳首列#或物理空白；缩进独立注释删后为空却不再略空。A完整、B节头后B内该行拒绝：A已登记，B未yield/登记，终检/save未到。首节前同输入报缺初始节。

专用trainers预处理后略空，接受该注释。行内#先于schema/CSV删后缀，引号不保护；q取预处理后的整值，不恢复#后缀或端空白。已有其它入口登记Alpha#Beta可写出，再编译仅Alpha；不能推全部字符串往返或随附语料受影响数量。

正常首列#、空行、无#文本和trainers对照均成立；失败不是类型校验也不是所有PBS拒注释，已由B8分层。

接收案例：8。R 必要读片：41, 42, 43；B8：generic-kernel/wp04-pbs-lifecycle.md:66-100,217-225；generic-kernel/wp03-content-identity-and-schema.md:138-158；test-catalog/generic-kernel-wp02-03-04.md:73-75,86-90。

### R6-UI-001

选择A送盒后，默认Peer成功存同一A→调用者删A→送盒暂停；暂停内party=[B,C,D,E,F]、N未入队、四类记忆未左移。消息返回才移位清尾，再N入队；入队暂停返回后才回填新槽初始道具。

去向BACK99在sendToBoxes0送N盒，选人BACK回去向；2移除送盒项且不可取消。送盒消息异常保已存/删而后续未到；双满默认Peer兜底缺消息能力的更早失败先于删A，不能套消息内前缀。图鉴/命名等已完成动作不回滚。

最终队伍相同不足以否定暂停观察点；CP08已明确更早的默认Peer失败而非泛称存盒失败也必删除。伙伴/录制终局不在此签字。

接收案例：9。R 必要读片：11, 13, 14, 20；B8：user-interface/wp67-a-battle-interaction-and-presentation.md:218-232；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:951-969。

### R6-UI-002

Safari Ball以party_full? && storage.full?拒绝；双满提示正常返回后next重选，未扣球/投球/回合末。队伍有位且盒全满仍放行；队满盒有位也放行。

放行先球数-1→刷新→投球请求；后续异常不退球保证。Run决定3；末球未捕获且仍0先球尽决定2，无先行逃逸抽样；成功捕获/接收需另门才决定4，Safari未设满队去向询问。

“盒满即拒”被1人/满盒反例排除，正文两域均已改为合取；放行不等于捕获成功。

接收案例：5。R 必要读片：14, 16, 17, 20；B8：user-interface/wp67-a-battle-interaction-and-presentation.md:300-305；pokemon-rules/wp53-safari-and-bug-catching-contest.md:73-90；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:971-981。

### R6-UI-PARTY-001

构造markings=[]；仅旧Integer迁移成六槽，不填空/短数组。Summary显示(markings[i]||0)不写值；ACTION直接比较缺值>0在提交前失败，显式0无操作，正数清副本。

输入BACK>USE>ACTION>方向互斥；BACK+ACTION安全弃稿，USE+ACTION仅USE。OK结果不同才整体写并true，Cancel/BACK无提交。先编辑别槽再缺槽ACTION仍不提交且正常隐藏/返回未到。Storage直接Mark无ACTION分支，保持独立正常对照。

最强反向为“显示0/旧迁移已补齐”，均被定义排除；B8明确默认空与异常边界，不把所有Mark都判失败。

接收案例：9。R 必要读片：01, 21, 27, 29；B8：creature-rpg/wp18-creature-identity-species-ownership.md:164-188；user-interface/wp66-a-party-and-summary-ui.md:180-190；user-interface/wp66-b-storage-and-pokedex-ui.md:114-122；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:983-997。

### R6-UI-PARTY-002

重学先按等级表顺序去重未会，再把first_moves中未会且不在等级候选的项前置，最终去重。GROWL与非首项重叠仍[TACKLE,GROWL]；独有CURSE才前置；已会AMNESIA不加，配置关忽略first_moves。

BULBASAUR0/L2/仅会兼容AMNESIA的合法字段夹具与重复诊断列表分列；非空首绘才有取消/教学交互。拒教学或核心false回列表，BACK拒退出后再确认退出false，成功教学才reminder+1/true。满槽/HM和背包TR追加记录、队伍Use不追加的包装保持。

A31首项重叠不辨序，但RL02已用非首项GROWL辨序；不把first_moves误作全部蛋招表。空候选首绘失败沿当前已有独立条款，未新增根因。

接收案例：9。R 必要读片：21, 27, 32, 46；B8：creature-rpg/wp30-growth-learning-and-friendship.md:159-176；user-interface/wp66-a-party-and-summary-ui.md:192-220；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:999-1013,629-635。

### UI-ST-001

Storage队伍选择0..6：末按钮UP→5，DOWN→0，左右沿含末按钮序列回绕；普通成员上下±2。方向本身不写集合。

末按钮USE在整理返回-1收面板回盒-2，在存入返回-3走Exit确认；BACK在存入走Continue确认。不能把Party主UI或图鉴导航当Storage端点。模式内空槽守卫在选择后单列。

普通成员±2规则不能推末按钮UP到4；B8已写端点例外和模式消费者，无缺口。

接收案例：4。R 必要读片：29；B8：user-interface/wp66-b-storage-and-pokedex-ui.md:53-86,124-133；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:288-297。

### UI-ST-003

Forms已有有序多项仅USE进入选择器；首轮oldindex=-1必写last_form_seen三参、异色缺省false。UP/DOWN首尾模回绕，移动后下一轮先写/刷新再受理退出，BACK/USE不回滚。

直接末次写不刷新可访问/已见/拥有/已见形态；返回普通列表重建，搜索态重跑并夹索引；读末次形态字段和普通图像。单项不开选择器，物种上下跳未见且停端，页面左右夹1..3。资源失败只保已到达写入，不保证收尾。

箭头隐藏不是回绕守卫；单项BULBASAUR不能验证多项首写。正文和PD/DX成对消费者已覆盖两项最强反向。

接收案例：7。R 必要读片：23, 24, 25；B8：user-interface/wp66-b-storage-and-pokedex-ui.md:230-257；pokemon-rules/wp62-pokedex-records-regions-and-content.md:71-91,147-177；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:306-317；test-catalog/pokemon-rules-wp53-60-61-62-69-70.md:187-197。

### UI-ST-005

Storage先独立方向repeat覆盖（UP>LEFT>RIGHT>DOWN），再动作互斥；盒动作JUMPUP>JUMPDOWN>SPECIAL>ACTION(mode0)>BACK>USE；队伍动作ACTION(mode0)>BACK>USE。

方向后USE能选新格；JUMP+BACK只切盒，本轮不退出；非整理ACTION门假继续BACK；SPECIAL在盒名仍消费。方向切盒辅助正常完成含Input.update，后续动作重新查询；currentBox在辅助返回后写。暂持不允许退出且切盒保留；Mark副本方向后BACK>USE独立。普通命令、Summary、图鉴主/子页有各自顺序。

排除整轮一个统一快照、全UI同一优先序和切盒请求即提交；B8逐阶段及输入刷新后查询已明确。

接收案例：7。R 必要读片：29；B8：user-interface/wp66-b-storage-and-pokedex-ui.md:53-133；user-interface/wp17-messages-windows-input.md:119-123；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:288-304,908-912。

### GR6-UI-BAG-001

BP包装先原地过滤同一stock的重要已持有项；speech nil请求默认欢迎+说明两条，普通自定义文本只请求该一条。正常购买取消返回也共同两告别后clear_mart_prices。

首问候异常：过滤已提交、画面未到；画面异常：问候已返回而告别/清覆盖未保证。库存不恢复。原价格/半价显示怪癖、购买统计及回退保留；只证请求次序，不证真实事件/音效。

“自定义仍先默认两条”和“取消恢复stock或总清覆盖”都被直接包装次序排除；B8完整分支已覆盖。

接收案例：6。R 必要读片：31；B8：creature-rpg/wp29-shops-and-exchanges.md:86-100；user-interface/wp66-c-bag-item-storage-and-shop-ui.md:116-136；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:1016-1025,342-355。

### GR6-UI-BAG-002

Bag确认Yes后先成功提示，提示正常返回才每次remove1共qty次（不检查）并刷新；PC确认后整批remove(qty)检查成功→刷新→成功提示。5丢3终态均2，提示内库存分别5/2。

提示异常或三行自动忙暂停时Bag未删/后刷新未到，PC已删/刷新；数量0或No均无成功提示无删。重要品Bag正常无Toss，PC直接拒绝。共享逐字两行A/LF/B/LF/C仍busy，入口只在!busy恢复，brief也不越门；短消息正常返回为独立对照，未运行宿主。

聚合终态相同无法抹掉提示前后差异；不把成功字样当已删，PC无容量预检，源码与三篇正文一致。

接收案例：7。R 必要读片：06, 07, 19, 28, 30；B8：creature-rpg/wp27-bag-and-item-storage.md:115-125；user-interface/wp66-c-bag-item-storage-and-shop-ui.md:64-90；user-interface/wp17-messages-windows-input.md:82-100；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:1026-1030,334-358。

## 历史裁决与边界

R6候选、实际MI `86bbc99`、5c登记资格、b7正式接受和4df关闭分别保留原时点；旧FAIL/WAIT、撤销、原提案及后继clarifier没有改写为新通过。历史actual A/B/C/D/E与本续接包A/B/C/D分开，不把formal_review_primary_groups当本包owner。共享root/common与五实际原报告及5c整体资格由D收口。

PARTY003：Shadow非满级EXP条的绘制请求与实际可见效果分层，原optional保留；Storage暂持预览与swap后变化为不同动作，UI-ST002原optional保留。PARTY004原required提案的“上轮Summary命令持续”被块局部变量及完整调用链反证；最终NO_REQUIRED保留，旧隔离实验只作历史证据，本轮未运行。

## 给父接收者及D

interfaces.json提供14项完整producer事实及33边的原阶段／当前消费接合。第三个U14联合接口中，本包只签具名data/language/cache消费者，不加U14 primary或根因计数。三接口整体仍由D实际读取各必要贡献后收口；本包不等待无关包，也未代签GR6-F-002、GR6-F-V004或父级task-final。缺本次D最终联合结果只保留对应父级接口OPEN，不阻塞已完成的C独立部分。

可回读证据根即本目录；原始完整对象通过固定合同中的readset/decoded-index和其精确身份回读，不另下载全仓、不复制参考代码或大体积原始行政包。

## 执行与真实限制

新参考行为／模型／宿主／原生媒体／真实存档／Demo执行均0；旧恢复脚本与游戏未执行。仅静态阅读、对象解码、可逆重构、Git身份／目录／文件字节验证及报告数据生成。请求配置gpt-6.1-sol/ultra/default普速/Fast off；实际这些字段无可靠回显，全部UNVERIFIED。

条件化输入查询、图形/音效请求和正常返回前提不证明真实键盘时序、像素、声音、宿主恢复或真实Demo可达。没有把可得未读内容列为宿主限制。原异常是参考事实，不替用户选择未来兼容政策。不整改、不改正式规格、不合并main、不开发TS；不签B8全局PASS。

发布后的普通commit和完整远端回读结果由外部提交回执绑定，文件不写自身未来commit/tree。
