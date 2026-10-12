# J：独立跨模块有限静态取证报告

本轮14条具名链：supported 6、partial 8；新增J实质问题0，关联已有GR4问题8。这不是14次运行通过，更不是历史80项新PASS。

- 固定B `1f36475d22120a0d1175967d5b17d71fe8311d88`，tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`。
- 固定R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 实际thread ID按J-launch.json：`01a1301e-5efe-7062-a4bf-e260d9361396`；请求 gpt-6-astra / ultra / default / noFast，实际模型回显 **UNVERIFIED**。
- 身份/readiness复用共享baseline与J输入清单。M11启动时未冻结，本报告未读取、等待或接受其提交；图鉴交界直接按固定B/R审查。
- 原函数、隔离验证、游戏、UI、编译、存档与完整Demo均 **NOT_EXECUTED**。资料可读不等于运行成功；本轮Python仅用于报告与锚点校验。
- 仅写J目录；没有修改正式规格、参考、历史或共享聚合，没有提交/push、启动agent或实现框架。

## 逐链结果

| ID | 有限链 | 状态 | 已有问题关联 |
| --- | --- | --- | --- |
| GR4-J01 | 翻译/PBS → 登记/导入 → 电话运行消息 | partial | GR4-M01-001, GR4-M01-002 |
| GR4-J02 | 保存/恢复游戏变量 → 墙钟计时查询 → 地图刷新 | partial | GR4-M02-001 |
| GR4-J03 | 冲浪状态/临时基点 → 转移 → 精灵定位/解释器等待 | partial | GR4-M03-002 |
| GR4-J04 | 动态形态 → 能力重算/图鉴 → 资源请求（含孵化） | partial | GR4-M04-001 |
| GR4-J05 | PP补给 → 战斗/野外资格 → PP写回与道具数量 | partial | GR4-M05-001 |
| GR4-J06 | 育种亲本单持物 → 继承预算 → 静态向量 | partial | GR4-M06-001 |
| GR4-J07 | 战斗选择登记 → 取消/退款 → 下一轮或正常终局 | supported | 无新增 |
| GR4-J08 | 自耗树果 → 续击属性/基底查询 → AI只读预测 | supported | 无新增 |
| GR4-J09 | 设施临时等级/替换队伍 → 退出还原 → 统计/保存 | supported | 无新增 |
| GR4-J10 | 同轮文本/数量/命令输入 → UI提交 → 状态恢复 | partial | GR4-M10-001 |
| GR4-J11 | 图鉴记录/MapSize → 可访问列表/可见点 → 栖息地显示 | supported | 无新增 |
| GR4-J12 | 工具单项导出/导入 → 集合保存/关联编译 → 动画资源消费者 | supported | 无新增 |
| GR4-J13 | 捕获/赠送接收 → 容量/队伍盒子 → 图鉴与部分提交 | supported | 无新增 |
| GR4-J14 | 新游戏 → 遭遇/战斗 → 接收 → 保存继续：静态流程边界 | partial | 无新增 |

## 关键归属与修订护栏

M01译文导入/占位、M02变量计时、M03冲浪残留、M04动态取图、M05主动PP资格、M06育种预算测试、M10通用输入竞争分别保持单一已有根因。消费端新增定位不增加finding数量。具体主责/消费者建议在shared-capabilities.json；这不是未来实现架构。

**孵化护栏：**GIR-FD82-A053仅具名投影亲审。DEERLING存储形态0、2月、steps1、无强制形态且非战斗/储存，在前置媒体/消息正常时，先计数归0和核心写入，再由演出实参读取动态形态而提交1，随后才通常拥有/见过蛋。WP35§5.2、§9及EG-13/EG-20已经准确。M04建议删除WP18的图像泛称是相容的；不能把“参数式取图函数不自行求值”改写成“孵化调用者没有求值”。

电话Default重复覆盖候选已完成全131正式材料同义反证，WP03/WP04/KR14–16/KL36已承接，故拒绝新增；具体检索在candidate-counterevidence.json。其余没有新增missing/contradiction裁决，不用该检索冒充131文件全新语义验收。

## 每条亲审范围与证据

### GR4-J01 翻译/PBS → 登记/导入 → 电话运行消息

**结论：partial。** Default重复候选经全131同义检索被现有准确条款反证，保留GR3 CLOSED；译文合并与普通占位问题仅关联M01，不新增J根因。

主责：WP08 本地化；电话PBS身份子合同由WP03单独主责，WP04与WP63引用。
生产者：phone.txt重复属性候选与联系人/Default节；Text_语言_core/game文本域导入。
状态写入：电话记录登记；终检登记PHONE_MESSAGES候选；译文按规范键或索引逐项合入；电话生成再战请求时旗标1→2。
消费者：当前/起始版本/default电话消息选择；当前语言game→core→原文查找；电话分段与姓名/物种/地图替换后交消息窗口。

前提/配置：合法电话身份/可读输入；依赖数据和宿主调用正常；本次无扩展覆写；联系人可进入生成/播放；语言加载按独立阶段成立；PhoneMessage schema重复属性候选；PHONE_MESSAGES域22；LANGUAGES及PHONE_REMATCHES配置；电话显示姓名与数据身份不同；翻译导入和PBS编译是两种输入格式。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 合法单默认集经编译终检形成候选；联系人两版本均缺时选默认候选，再查当前语言，最终不保证显示原候选字面。 |
| 失败 | 联系人同三元重复在第二次登记前拒绝，前项内存保留；文本完整导入先打开输出，解析失败不能保证旧产物恢复；显示失败可发生在再战旗标已推进之后。 |
| 取消 | 作者导入的外部菜单取消未重新审；运行生成没有撤销旗标的局部事务；本链不把UI退出解释为恢复译文或电话状态。 |
| 重复 | 两个Default节A/B后节整条替换（已正确承接）；同一翻译域后节只覆盖同键并留前节独有项（M01-001），这两种合并不能统一。 |
| 顺序 | PBS候选登记→终检收集；翻译导入与语言加载另行发生；运行先选候选再本地化→生成期旗标提交→播放。 |

已审：沿通用编译实际PhoneMessage存在性覆写、登记、终检到电话消费者；同域译文后键覆盖/重复节逐项合并与运行回退；普通占位插入与后续消息窗口分层；非字面特殊参数只关联M01既有问题。
未审：全部文本域/所有翻译文件往返；跨文件次序所有组合、实际电话公共事件与可达性；宿主占位特殊字符执行未复跑；不沿用M01隔离回执为J运行证据。

静态向量（均NOT_EXECUTED）：
- GR4-J01-V1：同一合法电话输入依序Default Intro A、B；联系人版本均缺 → 候选仅B；显示再经语言表。与KR14/KL36一致。
- GR4-J01-V2：同一翻译哈希域前节K1=A、K2=B，后节K1=C → K1=C、K2=B；为M01-001的同根交界，不另立问题。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb` L4–68,1237–1268：通用登记前探测、Phone专用身份规范化、终检文本收集。
- `Data/Scripts/010_Data/002_PBS data/021_PhoneMessage.rb` L15–26,36–69,72–88：联系人三元查询与Default探测区别。
- `Data/Scripts/010_Data/001_GameData.rb` L78–85：直接登记后项替换。
- `Data/Scripts/001_Technical/003_Intl_Messages.rb` L376–384,437–489,511–528,589–631,774–823：译文导入、加载、回退与占位阶段。
- `Data/Scripts/013_Items/004_Item_Phone.rb` L414–503：实际选择/状态提交/播放消费者。
- `PBS/phone.txt` L3–13：默认电话重复属性候选存在。

B正式锚点：
- `deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md` L121–134 / §5.2：Default与联系人重复规则已准确。
- `deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md` L82–92：通用编译消费者与Default例外。
- `deliverables/final-specification-set/generic-kernel/wp08-localization.md` L27–32,44–67,98–119：运行回退正确；本轮既有译文合并与占位问题。
- `deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md` L140–145：电话候选/再战写入/播放。
- `deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md` L33–35,76–76 / KR14–16 / KL36：反证排除新Default问题。

历史映射：G1-4, G1-5, G7-4, N01；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J02 保存/恢复游戏变量 → 墙钟计时查询 → 地图刷新

**结论：partial。** 保存本身不增强计时记录的有效性；M02-001为唯一相关根因。M02-003依用户裁决不需修订，与本链无新增关系。

主责：WP06变量计时语义；WP09持久单元、WP11/13刷新为消费者投影。
生产者：秒数或天数设置入口；存档变量单元恢复。
状态写入：变量槽存入开始墙钟与期限；查询不成立清变量为0；设置/清零均直接刷新地图。
消费者：墙钟有效查询；地图事件/公共事件刷新；正常保存再取变量整体、继续加载同一持久单元。

前提/配置：有效游戏变量槽和时间记录，合法数字期限；当前地图刷新依赖正常；继续加载值类型有效；不添加离线自动触发或默认调用者假设；合法变量范围；秒数负值夹0；天数负值夹0；t为设置时Unix秒，d为天数，期限=(t mod 86400)+86400d−t；游戏时间游玩锚点与墙钟记录不同。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 正期限且经过时间严格大于期限时返回真、保留记录；保存/继续可保留该变量数据。 |
| 失败 | 未到、恰到或非正期限均假并清0；设置天数不是通常的日历倒计时；保存类型/IO失败与计时查询失败分开。 |
| 取消 | 设置/查询无取消接口；保存UI拒绝不调用保存，也不撤销此前计时查询清0。 |
| 重复 | 成功查询重复可保持真；一次未到期查询清0后再查仍假，不能把它当无副作用轮询。 |
| 顺序 | 变量写入先于地图刷新；继续先恢复变量再恢复地图。查询清0后下一次成功保存会记录0；并非读档自动清计时。 |

已审：变量生产、破坏性查询、保存取值与恢复绑定；查询为假后的地图即时刷新；变量未加载/非法边界仅按已读守卫。
未审：任意损坏数组、所有变量编号边缘和刷新中的重入；实际旧档迁移/保存IO/运行计时；没有默认脚本调用者证据，不猜Demo事件使用。

静态向量（均NOT_EXECUTED）：
- GR4-J02-V1：槽v=[t0,10]；t=t0+10，正常查询及刷新 → false、槽0；随后t0+11再次查询仍false。独立初态[t0,10]在t0+11查询则true且保留。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/019_Utilities/001_Utilities.rb` L157–191：变量计时三入口及写后刷新。
- `Data/Scripts/004_Game classes/001_Switches and Variables/003_Game_Variables.rb` L12–24：槽读写与默认0。
- `Data/Scripts/002_Save data/004_Game_SaveValues.rb` L42–47：变量整体保存/恢复。
- `Data/Scripts/002_Save data/002_SaveData_Value.rb` L239–248,271–282：未加载恢复与保存汇编。
- `Data/Scripts/003_Game processing/001_StartGame.rb` L63–103,111–124：继续/地图恢复与保存失败。
- `Data/Scripts/004_Game classes/004_Game_Map.rb` L429–445：事件/公共事件刷新消费者。

B正式锚点：
- `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md` L25–50：时间来源已分层；变量计时缺口关联M02-001。
- `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md` L59–81,92–96,107–115：变量持久目录、地图恢复与保存失败。

历史映射：G2-1, G2-2, G2-6, G9-6, CHAIN-2, N03, N05；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J03 冲浪状态/临时基点 → 转移 → 精灵定位/解释器等待

**结论：partial。** 同一M03根因影响状态、显示和命令进度，不能分别计三个新问题。

主责：WP12载具状态；WP59场地动作提交；WP11/16/13分别消费转移/显示/等待。
生产者：上水或成功上岸前跳；显式转移的取消游泳参数。
状态写入：先冲浪/统计/底座再尝试上水前跳；上岸跳成功才写底座及ending标志；仅合格玩家步后通知清底座，ending为真才继续清结束状态。
消费者：Scene_Map转移与玩家moveto/载具外观覆写；SurfBase以残留基点定位；解释器见ending_surf提前等待。

前提/配置：有效地图/玩家/载具配置；明确前跳失败或无完成步后通知的时段；同图保留游泳转移与默认取消游泳转移分列；无额外插件清理；转移cancel_swimming真/假；玩家移动外观配置、面对水域与落点通行；地图场景/玩家事件/底座存在三道清理门。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 上/下水动作正常到合格步后通知才收尾；清理后精灵回跟随位置，结束冲浪等待门解除。 |
| 失败 | 上水前跳拒绝时前缀已提交；转移及取消载具自身不清两个临时字段；取消游泳只可能隐藏底座显示，不等于清字段。 |
| 取消 | 确认上水前拒绝不进入提交；提交后的转移中断不是事务撤销。 |
| 重复 | 残留非空时显示反复消费同一基点；ending真会持续阻解释器，直到相应清理发生；不推一定永远残留。 |
| 顺序 | 冲浪置位/统计→基点→前跳；转移重建显示不是步后通知；解释器等待门在通常命令处理前。 |

已审：两个临时字段全脚本读写检索；实际转移、玩家moveto/外观覆写及两个下游消费者。
未审：真实地图落点和屏幕位置；所有场地招式/边缘切图组合；无限等待或宿主自动恢复不作结论。

静态向量（均NOT_EXECUTED）：
- GR4-J03-V1：上水写入后前跳失败；无合格步后通知；同图显式保游泳转移 → 临时基点无转移清零保证；重新显示仍读取基点。正常合格步后通知为独立清理对照。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb` L692–751：上水提交/上岸标志/步后清理。
- `Data/Scripts/003_Game processing/002_Scene_Map.rb` L72–101,121–133,165–175：转移及默认201消费不清临时字段。
- `Data/Scripts/004_Game classes/008_Game_Player.rb` L64–100,262–266,575–592：实际覆写不补清理。
- `Data/Scripts/005_Sprites/005_Sprite_SurfBase.rb` L44–79：残留基点影响定位。
- `Data/Scripts/003_Game processing/003_Interpreter.rb` L103–123：结束标志阻解释器。

B正式锚点：
- `deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md` L164–173：提交与步后门准确。
- `deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md` L295–301 / §7 L296：转移重置保证与实际链不符。
- `deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md` L59–71：实际转移参数及状态消费者。

历史映射：G2-3, G9-5, CHAIN-8；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J04 动态形态 → 能力重算/图鉴 → 资源请求（含孵化）

**结论：partial。** M04建议按其具名个体取图范围修订与旧孵化合同相容；本轮独立检查确认该有限消费者投影，不重开A053。

主责：WP21动态求值，WP18提交副作用；WP15资源与WP35/67-B孵化为消费者。
生产者：个体动态形态读取；DEERLING季节和FURFROU到期处理器。
状态写入：变化时存储形态、特性缓存、能力与图鉴见过记录；孵化核心字段先写，演出读取后才通常拥有/见过蛋。
消费者：物种内容读简化形态；按个体前/背精灵和图标读取动态形态；孵化蛋图/裂纹请求的调用实参先取动态形态。

前提/配置：无forced形态，非战斗/非储存才求动态；资源与消息必须实际到达查询点；DEERLING普通非Shadow、存储0、剩余1步、2月；媒体/玩家/图鉴有效，跳过命名、无额外改写；季节=(月份−1) mod 4；FURFROU缺时间戳或严格超5天回0；DEERLING命名形态数据与FURFROU剪毛形态存在；资产缺失。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 到期FURFROU按个体取图先回0及提交，再请求图像；DEERLING2月在孵化早期取图实参求值时0→1。 |
| 失败 | 形态变化可先于资源解析/显示失败发生，没有资源失败即回滚形态的保证；是否到达查询受更早资源/宿主阶段限制。 |
| 取消 | 拒绝孵化命名不撤销此前形态/核心提交；不虚构可取消孵化。 |
| 重复 | 相同动态结果再次读取不再触发形态变更提交；forced或battle/storage门直接返回；核心直接孵化重复不是防重入口。 |
| 顺序 | 计数先归0→孵化核心写入→调用者取form→完整提交→资源函数；参数式资源函数不自行求值，不代表调用者未求值。 |

已审：普通form/简化form、完整提交、数值重算与图鉴映射；按个体取图及参数式取图的调用位置区别；孵化步后→核心→蛋图/裂纹→揭示→拥有/见过蛋完整具名链。
未审：所有物种动态处理器；真实图像存在/像素、孵化演出或原函数执行；GIR-FD82-A053其余旧贡献与全部229/341控制。

静态向量（均NOT_EXECUTED）：
- GR4-J04-V1：EG-20完整前提：DEERLING存储0、月2、steps1；无forced/battle/storage → steps0，核心提交；蛋图实参取form得1，存储1/重算/登记已见；通常拥有及见过蛋随后发生。月1或forced为独立对照。
- GR4-J04-V2：FURFROU形态1，缺时间戳，按个体取图；独立显式形态参数1取图 → 前者先提交0再取图；后者本层仅消费参数，不求个体动态形态。若调用者已动态求值则另论。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/014_Pokemon/001_Pokemon.rb` L113–115,147–184,1099–1127：简化内容读取与动态提交/重算。
- `Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb` L322–328,422–431：季节与五天形态。
- `Data/Scripts/012_Overworld/003_Overworld_Time.rb` L201–203：季节公式。
- `Data/Scripts/010_Data/002_PBS data/009_Species_files.rb` L37–68,92–109,118–139：显式参数与个体资源请求分层。
- `Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb` L49–69,124–138：真实精灵/图标调用。
- `Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb` L13–40,84–129,212–221,252–267：孵化完整消费者时序。
- `Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb` L195–218：形态登记使用简化物种数据并映射展示形态。
- `PBS/pokemon_forms.txt` L1397–1408,1635–1661：具名形态数据。
- `Data/Scripts/016_UI/006_UI_Summary.rb` L117–135：摘要实际调用个体精灵/图标。

B正式锚点：
- `deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md` L140–153：L151图像泛称是M04既有矛盾。
- `deliverables/final-specification-set/creature-rpg/wp35-eggs-and-hatching.md` L93–117,163–165：孵化合同已准确，不得倒退。
- `deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md` L23–30 / EG-13 / EG-20：限定旧投影与反向对照。
- `deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md` L157–163,177–181：个体资源副作用与限时形态。
- `deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md` L48–50：资源个体入口投影。

历史映射：G4-8, G5-4, CHAIN-5, N08；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J05 PP补给 → 战斗/野外资格 → PP写回与道具数量

**结论：partial。** M05一条根因，战斗与UI/数量交界只引用，不新计。

主责：WP28主动道具资格；WP20 PP写回、WP40战斗登记、WP27库存为投影。
生产者：主动ETHER/MAXETHER/ELIXIR/MAXELIXIR/LEPPABERRY选择。
状态写入：成功PP恢复封顶；符合条件的场上副本PP同步；野外成功后扣数量；战斗登记先扣、失败复检按J07退款。
消费者：战斗资格家族；队伍/背包使用包装；场上未变身且同槽同招式副本。

前提/配置：有效非蛋非Hyper目标和缺PP招式；道具在袋且为消费品；区分HP0与可战斗目标、主动LEPPA与被动持物；默认PBS FieldUse/BattleUse；回复10/全满；最大PP>0；场上同步要求未变身且同招式。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | HP>0缺PP的合法目标战斗可登记；野外回复成功才扣；场上副本满足同步门才写穿。 |
| 失败 | HP0非蛋仍可在野外恢复PP，但战斗资格拒绝且尚未扣物；满PP/无有效总PP不生效。 |
| 取消 | 野外招式/数量取消不扣；战斗目标/招式取消不登记；已登记取消按J07。 |
| 重复 | 一次回复使PP满后再次使用失败，不能重复扣；多件/别名按同门。 |
| 顺序 | 战斗目标选择允许非蛋进入招式选择，随后资格拒HP0；不是UI先过滤所有濒死者。 |

已审：五物品家族别名、两上下文资格、实际战斗选择caller；PP辅助与野外扣减包装、战斗登记时机。
未审：被动LEPPA恢复；AI所有道具策略、全部异常招式索引；真实队伍界面输入。

静态向量（均NOT_EXECUTED）：
- GR4-J05-V1：普通非蛋HP0，TACKLE PP0/35，ETHER库存1，无其它拒绝门 → 野外选该招→PP10、库存0；独立战斗初态资格拒→PP0、库存1；HP>0为正常对照。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/013_Items/003_Item_BattleEffects.rb` L155–186,501–531：战斗可战斗门/别名/效果。
- `Data/Scripts/013_Items/002_Item_Effects.rb` L632–684：非战斗PP条件和取消。
- `Data/Scripts/013_Items/001_Item_Utilities.rb` L367–382,644–686,710–775：封顶、同步、消费与非蛋通用门。
- `Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb` L100–137：资格先于登记。
- `Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb` L265–284：目标选择只预排蛋，招式取消重选。
- `Data/Scripts/014_Pokemon/001_Pokemon.rb` L264–270：able与HP0区别。
- `PBS/items.txt` L3294–3333,5242–5250：默认用途/别名身份。
- `PBS/moves.txt` L5326–5336：静态PP向量所用TACKLE最大PP35。
- `Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb` L165–177：战斗通用道具资格实际覆写，不取消PP家族HP门。

B正式锚点：
- `deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md` L112–129,202–206：缺战斗HP门是M05-001；保留正确退款合同。
- `deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md` L99–114：登记/复检/退款。

历史映射：G6-1, G6-2, G7-3, G7-5, CHAIN-3, N12；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J06 育种亲本单持物 → 继承预算 → 静态向量

**结论：partial。** 仅测试向量根因关联M06，不改正确WP34，也不发明额外持物能力。

主责：WP34继承预算；WP20单持物身份为前提，测试目录为消费者。
生产者：两亲本规范化持物身份；世代与力量道具映射。
状态写入：先默认预算3；gen≥6且一方Knot才5；每种力量能力写入并扣预算一次；余下不同能力从剩余池取得。
消费者：后代IV与最后能力重算；BR16–19测试向量。

前提/配置：正常两亲本、每只单一持物；没有扩展多持物或替换处理器；实际生成入口不接独立继承预算；MECHANICS_GENERATION；DESTINYKNOT与六件Power为独立身份；默认IV初始化保持未继承项。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 单Knot+单Power在gen≥6为1固定+4其它；无Knot为3总项。 |
| 失败 | 双不同Power不能同时再持Knot，故BR18的5−2分支不可由其前提满足；正文正确而测试不一致。 |
| 取消 | IV继承内部无取消；寄养领取取消未审，不补回滚。 |
| 重复 | 双方相同Power只占一个能力项、从两值择一；不同Power占两项，剩1；再次生成另一个蛋重新抽取。 |
| 顺序 | 预算在力量项前计算；力量项去重并逐项扣；不把两种数量规则并列当无前提可选。 |

已审：生成caller→IV继承→末次calc_stats；单一持物规范化查询、不同道具数据、正文与BR18关系。
未审：随机抽样运行、全部遗传通道；亲本Demo获取/寄养事件与时间；多持物插件前提不存在于本链。

静态向量（均NOT_EXECUTED）：
- GR4-J06-V1：母POWERWEIGHT、父POWERBRACER，gen8，合法单持物 → 固定HP/ATTACK两项+随机不同1项，总3；BR18应只保3−2。
- GR4-J06-V2：一方DESTINYKNOT、另一方POWERWEIGHT，gen8；独立gen5 → gen8总5（1+4）；gen5总3（1+2）。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/012_Overworld/007_Overworld_DayCare.rb` L21–51,173–212：产生后代/预算/力量去重/剩余池。
- `Data/Scripts/014_Pokemon/001_Pokemon.rb` L551–576：每亲本单持物。
- `PBS/items.txt` L766–774,1423–1439：三个身份互异。

B正式锚点：
- `deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md` L128–133：正确正文。
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md` L239–242 / BR16–19：BR18错误预算分支。

历史映射：G5-5, G5-6；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J07 战斗选择登记 → 取消/退款 → 下一轮或正常终局

**结论：supported。** 限定生命周期投影supported；不重签U04-RF整套执行或全部战斗引擎。

主责：WP40选择生命周期；WP28效果资格、WP42终局、WP27库存投影。
生产者：合法战斗物品选择。
状态写入：登记选择并扣库存；效果成功清物品身份；失败退款保留身份；下一命令/正式失能清选择；正常终局撤销选择可再次退款。
消费者：攻击阶段物品分派；取消与正常战斗结束；下一命令阶段、正式失能。

前提/配置：普通内部战斗、有效库存/容量/消费者；重复退款例无伙伴、无中间失能/换人/清选择；宿主提示正常；消耗属性和物品BattleUse家族；玩家与非玩家业主资源；球家族4独立，无统一效果失败退球。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 成功效果正常返回清物品身份，终局不再退；取消未执行选择退回后清选择。 |
| 失败 | 资格复检失败退物但不清身份；退物容量不足报错保留此前前缀。 |
| 取消 | 取消调用退款→撤Mega→清选择；正常执行失败不是调用取消。 |
| 重复 | 执行失败已经退一次后，若同轮正常终局仍有身份可再退；次轮清选择/正式失能清选择不再退。 |
| 顺序 | 登记先写选择再扣；终局接收捕获/场景结束之后才撤销选择，因此先前阶段异常不保证退款到达。 |

已审：登记→消费→失败复检→退款→残留→终局/下轮/失能的实际链；成功效果返回不以true判退款；显式取消后清选择。
未审：完整毒伤胜利夹具与所有终局原因（只检到达终局后的消费者）；宿主异常后的全局恢复；Safari/捕虫等覆写不纳入普通链。

静态向量（均NOT_EXECUTED）：
- GR4-J07-V1：后备T缺1HP，POTION2、两名存活使用者顺序指T，容量正常；执行后当轮到正常终局 → 登记2→0，首件治满清身份，次件复检失败退至1留身份；终局再退至2。只改下一命令先到则保持1。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb` L34–75,87–147：登记/扣退/清身份。
- `Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb` L5–23,174–180：取消与下轮清理。
- `Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb` L69–88：实际效果分派。
- `Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb` L479–511：正常终局退款消费者。
- `Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb` L69–88：正式失能清选择。

B正式锚点：
- `deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md` L97–114：分入口清理已准确。
- `deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md` L112–131：库存/效果投影。
- `deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md` L177–191：正常终局可重复退款与异常边界。

历史映射：G6-2, G7-5, CHAIN-3, N12；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J08 自耗树果 → 续击属性/基底查询 → AI只读预测

**结论：supported。** 保留旧准确异常和范围；局部失败不得改成必然崩溃/正常还原或AI也失败。

主责：WP47-A自然之恩重读合同；WP50消费状态；WP46击循环；WP52-B预测投影。
生产者：NATURALGIFT首击、目标JABO反伤；使用者ORAN半血自动消费。
状态写入：首击HP、反伤、回复、当前/还原/可回收/拾取/吃果状态；持久持物写穿；背包不扣。
消费者：下一击真实基底查询；正常招式结束消费守卫；AI当前状态失败/基底查询。

前提/配置：沿WP47-A§3.1.1完整合法夹具；有效PARENTALBOND，U ORAN H160/h81，T JABO首击后存活；排除共生/压制/保护/替身/画皮/冰脸/失手/免疫/睡冻/换人/紧张感/治疗封锁/RIPEN/CHEEKPOUCH及额外回调；提示正常；ORAN自然之恩毒/80与恢复10；JABO物理反伤总HP整除8；AI失败门与基底1→0转换。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | h101对照反伤后81>半血，ORAN仍在；第二击重读80，正常结束再耗。 |
| 失败 | h81→61→71并自耗；第二击空持物身份访问先失败，早于默认1与第二击HP写入；前缀不回滚。 |
| 取消 | 已经起用的本地击循环无玩家取消；失能/睡冻/目标全倒停止与取消选择不同。 |
| 重复 | 目标JABO首击耗掉不重复反伤；单击对照ORAN已空时结束消费守卫跳过；不把多击初检当每击重跑。 |
| 顺序 | 真实每击重读当前持物；AI在消费前只读当前ORAN可正常得到80，不执行JABO→ORAN链。 |

已审：首击HP提交→被击道具→使用者HP物品检查→持物清除→逐击calcDamage基底重读；当前有ORAN的AI只读查询与真实反应链分开；普通计算先会心再基底，吸收早返排除。
未审：精确全伤害数值、获得PARENTALBOND操作链；AI完整候选评分与全随机策略；局部异常后宿主继续/退出/保存是否发生。

静态向量（均NOT_EXECUTED）：
- GR4-J08-V1：完整U04-NG01前提 → 81→61→71、ORAN空；第二击基底查询局部失败；对照h101不自耗，单击不进入第二查询。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb` L1338–1379：起用/类型/逐击基底/结束消费。
- `Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb` L364–386,1311–1330：ORAN/JABO效果。
- `Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb` L212–243,315–323：门/消费记录/清物。
- `Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb` L5–45：反伤后即时查询。
- `Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb` L403–429,623–664,683–701：每击写入和后续循环。
- `Data/Scripts/011_Battle/003_Move/003_Move_UsageCalculations.rb` L239–253：普通会心先于基底。
- `Data/Scripts/011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb` L1423–1435：只读资格与真实基底复用。
- `Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb` L45–53：有效亲子爱与单目标真实计划两击。
- `PBS/items.txt` L5252–5260,5721–5727：ORAN与JABO配置。
- `PBS/moves.txt` L5581–5591：默认自然之恩物理及效果身份。
- `Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb` L272–286：持物效果成功后的真实消费调用。
- `Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb` L85–89：清持物写穿关联个体。

B正式锚点：
- `deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md` L55–71：续击失败准确。
- `deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md` L113–121：消费投影准确。
- `deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md` L54–54：AI对应为B，不误指C。

历史映射：G6-3, N13；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J09 设施临时等级/替换队伍 → 退出还原 → 统计/保存

**结论：supported。** 限定静态链支持；不把设施脚本能力升级为Demo会话已运行。

主责：WP55会话主责；WP54单场经验还原；WP57租借提交；WP09保存投影。
生产者：会话开始/报名或租借提交；设施单场等级策略。
状态写入：保存原队伍引用并替换玩家队伍后安全保存；双方完整EXP按位置记录、临时改级；调整返回后才记持物；单场结果计胜负但不自动写会话决定/加胜；会话结束另回收记录。
消费者：单场正常返回EXP与持物还原；取消/结束队伍恢复；会话类型统计与安全保存。

前提/配置：有效规则、队伍、对手与地图/保存宿主；按位置对应若要正确恢复必须保持两侧成员顺序/身份；不预设深拷贝；临时等级策略/适用侧；显式会话决定/加胜；安全保存返回false与传播异常分层。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 单场正常返回依位置恢复EXP、再双方治疗/解除变换/恢复持物，之后记录像/统计；会话正常结束另恢复原队伍。 |
| 失败 | 调整/战斗/还原中失败只保留到达前缀，无统一确保恢复；安全保存false仍执行后续坐标恢复，传播异常可跳过。 |
| 取消 | 会话取消有原队伍才恢复并reset，不保存；工厂交换取消仍提交当前租借集合但不增交换数。 |
| 重复 | 显式加胜可重复增加；结束重置后再结束先把玩家队伍设为已空原队伍字段，再非进行中返回。 |
| 顺序 | 会话记录回收早于会话reset；单场胜利布尔不等于会话决定；临调记录是EXP不是仅等级，不能按新成员身份自动匹配。 |

已审：经验/等级写入口、调整/还原与单场真实顺序；会话队伍引用、取消、重复结束、胜次统计；工厂选入/交换提交与保存位置临时替换。
未审：完整设施名单/随机生成/评级；真实接待收费领奖地图事件；旧GR3-M09-001可选事项继续暂缓。

静态向量（均NOT_EXECUTED）：
- GR4-J09-V1：两成员不同EXP/持物，临调后交换其位置，再正常还原 → 按当前位置恢复旧EXP/物品，不能保证按成员身份正确；不主张正常用户流程一定重排。
- GR4-J09-V2：活动会话取消；独立初态正常结束后再结束 → 取消恢复并重置不保存；重复结束可把队伍写为空。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/004_Challenge_LevelAdjustment.rb` L28–78：完整EXP、位置还原。
- `Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/001_Challenge_ChallengeRules.rb` L61–80：策略主入口/双侧便利门。
- `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb` L40–104：真实单场还原与统计。
- `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb` L79–103,200–229,243–281,292–318,345–361,388–427：会话队伍/取消/保存/工厂交界。

B正式锚点：
- `deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md` L72–103：单场EXP与失败顺序。
- `deliverables/final-specification-set/combat-requirements/wp55-facility-session-and-restoration.md` L54–65,101–130：队伍引用、统计/保存分层。

历史映射：G3-3, G4-1, G4-2, CHAIN-4；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J10 同轮文本/数量/命令输入 → UI提交 → 状态恢复

**结论：partial。** 只补通用命令/逐位数字缺口；不把旧正确物品数量/光标命名合同重计为新问题。

主责：WP17输入原语；WP66-C/29数量业务与WP13变量提交为投影。
生产者：光标命名同轮按键；共享物品数量与金钱商店数量输入；通用命令/逐位数字。
状态写入：命名helper先编辑，确认返回后caller写昵称；商店返回数量后再确认/容量/资源提交；事件数字返回写游戏变量并标记刷新。
消费者：命名调用者（孵化/赠送）；买入/物品使用包装；解释器103与普通/帮助菜单。

前提/配置：静态同轮查询成立；正常窗口/音效/输入返回；各入口保持自身顺序，不假设同一物理设备必产生组合；逐位数字最小/最大/取消编码；商店价格/上限；共享数量初值；光标命名与键盘模式区分。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 文本需确认才返回；数量返回非零仍要业务确认/容量；合法数字可本轮编辑后提交变量。 |
| 失败 | 数字USE越界蜂鸣继续，同轮BACK不执行；窗口异常不保证恢复等待/可见性；购买资源复查失败不提交。 |
| 取消 | 共享数量BACK+USE→0；普通可取消命令BACK+USE→取消编码；数字合法USE+BACK→确认值；命名BACK+USE只删除。 |
| 重复 | 商店方向重复+USE仅编辑等待；下一轮仅USE才返回；各次成功业务提交保持，后来退出不回滚。 |
| 顺序 | 先组件更新再数字确认；命令组件导航先于结果；光标实际移动消耗本轮；商店交易确认在数量返回之后。 |

已审：光标命名方向消耗轮与SPECIAL/ACTION/BACK/USE顺序；共享数量BACK优先、商店方向优先，后续确认/提交；普通命令允许取消时BACK优先；逐位数字先编辑，USE压过BACK与越界分支；正常退出窗口可见性/帮助显示和事件等待标志交接。
未审：BP商店本次未沿源重审（沿旧限定证据）；真实键盘/手柄竞争、全部命名特殊上限；所有UI异常资源释放、跨场景重入。

静态向量（均NOT_EXECUTED）：
- GR4-J10-V1：共享数量和商店各初值1/上限≥11，同轮RIGHT重复+USE触发 → 共享返回1；商店改11仍等待，下一轮仅USE才返11。
- GR4-J10-V2：逐位数字合法编辑与USE+BACK同轮；独立越界编辑对照 → 合法返回本轮新值；越界只蜂鸣继续，未取消；关联M10-001。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/016_UI/025_UI_TextEntry.rb` L658–717,743–785：光标操作/结果/包装。
- `Data/Scripts/016_UI/018_UI_ItemStorage.rb` L276–337：共享数量顺序与显示恢复。
- `Data/Scripts/016_UI/020_UI_PokeMart.rb` L477–538,598–646：商店顺序与交易提交。
- `Data/Scripts/007_Objects and windows/011_Messages.rb` L166–205,721–801：通用命令/数字竞争。
- `Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb` L687–730：数字先编辑。
- `Data/Scripts/003_Game processing/004_Interpreter_Commands.rb` L325–334：结果变量/地图刷新/等待清除。

B正式锚点：
- `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` L92–121,146–171：命名已准确；通用命令/数字差异关联M10-001。
- `deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md` L88–108,124–158：数量竞争与业务提交分层已准确。

历史映射：G7-1, G7-3, CHAIN-3, N15；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J11 图鉴记录/MapSize → 可访问列表/可见点 → 栖息地显示

**结论：supported。** 仅具名图鉴/地图交界supported；不接受、等待或假定M11结论。

主责：WP62图鉴记录与Area集合；WP63地点首条查询、WP66-B显示为不同投影。
生产者：捕获/赠送/形态登记（接收入口详J13）；遭遇表与MapPosition/MapSize、区域Point/游戏开关。
状态写入：seen/owned/form/last-seen及可访问图鉴刷新；Area每次构建局部格集合，无持久栖息地图层写入。
消费者：可访问区域列表；遇表按版本枚举与目标物种匹配；Area点亮/unknown显示；区域地图游标与名称/详情/治疗点对照。

前提/配置：固定B/R直接源审，不消费M11报告；正常01形状、合法区域/地图元数据和遭遇物种；当前UI/资源/消息正常；媒体实际不可验证；USE_CURRENT_REGION_DEX/解锁与seen门；当前遭遇版本、HideEncountersInPokedex；Point可见开关；MapSize宽/形状。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 宽3/形状11111只亮5格；仅已登记存在的可见Point相交；重复同格按集合点亮。 |
| 失败 | 物种不在表/地图元数据缺/隐藏/区域不同均不贡献；无点显示unknown；不添加任意坏数据兜底。 |
| 取消 | Area查看无取消回滚语义，本地格集合非持久；图鉴浏览其它写入不在本链重新审。 |
| 重复 | 重复登记同形态是布尔写；Area重新计算，不叠加重复点；同格后一可见Point可使Area亮，首条隐藏仍让WP63查询空。 |
| 顺序 | 图鉴seen驱动可访问列表，不是Area点亮条件；Area来自表而非捕获地点历史；版本单次get正确回退不能替代each枚举。 |

已审：记录与刷新、Area表枚举→物种→元数据→mask→可见并集→绘制；v>0枚举回退键不一致的已知缺陷；区域地图长度定位和首条同格查询，不与Area并集混用。
未审：M11任何未冻结提交；全部图鉴筛选、历史记录清理和语言体型转换；真实地图、Point完整有效性、任意非01/越界输入。

静态向量（均NOT_EXECUTED）：
- GR4-J11-V1：MapPosition=(0,13,12)，宽3，S=10000；所有需用点可见 → 仅(13,12)亮；11111为五格，尾格(15,13)不亮；区域游标按长度可到尾格。
- GR4-J11-V2：同格首Point开关51关闭、第二Point无门 → Area可亮；WP63名称/详情/治疗取首条仍空。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb` L24–45,147–160,195–227,315–332：状态写入/刷新/形态。
- `Data/Scripts/010_Data/002_PBS data/013_Encounter.rb` L30–35,53–68：查询/枚举分层。
- `Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb` L302–390：占位和可见点交集到显示。
- `Data/Scripts/016_UI/009_UI_RegionMap.rb` L89–100,183–190,211–230：长度定位与首条查询。

B正式锚点：
- `deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md` L73–78,116–139：记录与Area准确。
- `deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md` L198–200：条目页投影。
- `deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md` L44–48：首条同格规则。

历史映射：G3-4, G7-2, N17；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J12 工具单项导出/导入 → 集合保存/关联编译 → 动画资源消费者

**结论：supported。** 有限单项/显式关联链supported，不扩为默认类型映射数据充分或批量工具全部通过。

主责：WP74作者交换/关联规则；WP04编译时机、WP67-A播放与WP15资源投影。
生产者：选中动画.anm导出/导入；集合改名保存；Move/OppMove关联编译。
状态写入：导入替换当前内存槽，集合保存另外确认；有效映射才写关联和集合；零有效保留旧磁盘映射；集合与映射缓存独立。
消费者：战斗按侧映射查槽并叠hit号；类型/类别回退再TACKLE（本次仅核回退流程，未审默认表全集）；选中集合槽和媒体消费者。

前提/配置：有效动画对象和当前选中槽、可读写目标；宿主/媒体正常是假设；若希望播放看到新映射，缓存须未加载或已失效；编译写盘本身不是清当前映射缓存；Move:/OppMove:有效注册招式身份与Common:精确名称；单项.anm不包含媒体复制；集合/映射文件与当前缓存分开。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 非空名导出选中单项；导入成功替内存槽，之后保存/编译/缓存消费各是独立步骤。 |
| 失败 | 导入坏编码返回选择循环；缺图警告时槽已替换；零有效关联编译不清旧文件，播放仍可能旧关联；异常不补原子回滚。 |
| 取消 | 空导出名不写；导入BACK不改；编辑器不保存但退出时清集合缓存，按原落盘状态重载。 |
| 重复 | 同侧有效关联后槽覆盖；重复编译有有效项仍写；已缓存映射不会因另一步写盘自动更新。 |
| 顺序 | 外部交换不直接更新运行集合/映射；播放先查关联，再读集合槽，再到媒体请求。 |

已审：单项导出取消/失败、导入替换先于缺图警告；编辑器保存/退出→集合缓存失效；编译有效/零有效与后槽覆盖；运行显式映射/回退/槽消费；不把文件写出当资源存在。
未审：批量导入导出与资源安全复制所有分支；默认类型动画映射数据全集（M10-004仍由主责处理，不在J重新判缺失）；所有逐帧播放器、真实.anm解码/媒体/编译执行。

静态向量（均NOT_EXECUTED）：
- GR4-J12-V1：原映射含TACKLE；把最后有效Move名改普通名并保存、再编译；缓存初为空 → 零有效不重写映射，播放器仍可取旧槽关联；不证明那个槽或媒体成功显示。
- GR4-J12-V2：同侧两个合法Move:TACKLE名称先槽a后槽b → 映射取b；OppMove另域。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/020_Debug/002_Animation editor/004_AnimEditor_ExportImport.rb` L20–83：单项格式/替换/取消/失败。
- `Data/Scripts/020_Debug/002_Animation editor/005_AnimEditor_Functions.rb` L994–1001：保存与退出分开。
- `Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb` L1274–1282,1295–1319：从空映射到有条件写入。
- `Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb` L39–53：集合/映射缓存消费者。
- `Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb` L412–443,469–525：显式关联、回退和槽消费。

B正式锚点：
- `deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md` L335–343,394–421：作者/编译/缓存/播放交界已准确。

历史映射：G8-2, G8-3, G9-4, CHAIN-6, N18；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J13 捕获/赠送接收 → 容量/队伍盒子 → 图鉴与部分提交

**结论：supported。** 接收部分提交链supported；图鉴先写不等于个体必已入队/盒；固定R/B独立检查不依赖M11。

主责：WP38捕获接收；WP26赠送独立入口；WP25容量与WP62图鉴投影。
生产者：合法球登记与成功捕获队列；普通/静默赠送个体。
状态写入：成功捕获先移对方队伍/效果/来源/形态再排待接收；终局捕获计数/见过/拥有/末次形态先于命名/实际存储；队伍/盒子写入及当前盒更新；失败不撤销前序图鉴。
消费者：默认战斗Peer与储存接收扫描；满队替换菜单；图鉴可访问/条目显示；玩家/储存持久单元。

前提/配置：本链普通内部战斗/默认Peer、有效玩家与存储；无伙伴投影；初始双满预检与后段容量变化/直接触达分开；宿主和提示在各向量指定点前正常；HEAL_STORED_POKEMON、送盒档位0/1/2；更频繁显示新物种配置仅赠送门；捕获条目省略该配置；see_form与静默两入口不同。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 队伍有位先入队；满队当前盒再其余盒首空；捕获首次拥有可展示后再命名存放。 |
| 失败 | 默认菜单双满先拒不扣球；后段若触达双满，默认Peer缺消息入口可在返回前失败，已有图鉴/命名/可选治疗保留；赠送内层容量拒绝外层仍可true。 |
| 取消 | 捕获询问档取消=送盒，强制档取消重选；成员选择取消重回菜单；拒绝昵称不取消接收；赠送同意后空文本清名。 |
| 重复 | 相同物种可再次获得，拥有布尔保持、捕获计数可增；待接收循环全部正常完成才清队列，异常后不称重入幂等。 |
| 顺序 | 捕获队列图鉴在容量存储前；赠送获得消息/图鉴/昵称之间有等待，后置复检可与入口结果不同；保存只取实际已写状态。 |

已审：球资格的双满门→成功排队→终局先图鉴后接收；队伍有位/满队送盒/储存扫描、满盒局部失败；赠送三次容量检查和返回值分层；静默加入与仅入队静默see_form差别。
未审：捕获概率/球表全集；伙伴合并参与集合的错物还原旧控制（仅复用其限定证据，不重审整CP21/22）；Safari/捕虫覆写、实际容量变化事件、真实存档。

静态向量（均NOT_EXECUTED）：
- GR4-J13-V1：未拥有X，初始容量通过；到后段存储时双满，默认Peer → 可能已捕获计数/已见/拥有/昵称后于存储兜底失败；不承诺原子撤销或正常返回。
- GR4-J13-V2：合法已有个体、see_form=false；静默加入 vs 仅入队静默，队伍有位 → 静默加入显式已见+拥有；仅入队静默仅拥有，本调用不写已见。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/013_Items/003_Item_BattleEffects.rb` L28–63：球菜单容量守卫。
- `Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb` L5–106,165–200：接收/队列/提交顺序。
- `Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb` L4–36：默认存储与全满失败。
- `Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb` L231–251：可选治疗后扫描。
- `Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb` L4–90,96–129：赠送三层复检与静默差别。
- `Data/Scripts/011_Battle/001_Battle/001_Battle.rb` L658–674：内部战斗计数/见过门。
- `Data/Scripts/002_Save data/004_Game_SaveValues.rb` L3–8,97–102：玩家和储存持久单元。

B正式锚点：
- `deliverables/final-specification-set/pokemon-rules/wp38-capture-and-receiving.md` L90–118：队列/接收/全满失败合同。
- `deliverables/final-specification-set/creature-rpg/wp26-acquisition-gifts-and-script-trade.md` L63–89：赠送与部分提交。
- `deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md` L50–64：不同入口图鉴顺序。

历史映射：G3-1, G3-2, G3-4, G3-5, CHAIN-1；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

### GR4-J14 新游戏 → 遭遇/战斗 → 接收 → 保存继续：静态流程边界

**结论：partial。** 静态交接可定位，但缺完整工程且未执行；整体状态partial而非missing规格或端到端支持。

主责：各领域单主责；J仅记录端到端静态交接，不设新的总事务主规格。
生产者：启动初始化/新游戏注册值；合法场地步进遭遇与生成个体。
状态写入：玩家/背包/存储/变量默认值与地图/遭遇上下文；实际战斗效果与接收提交（J13）；保存取值写盘/继续恢复未加载值、重新建遭遇上下文。
消费者：地图步进门、WildBattle覆盖门/核心；战斗正常终局接收；保存UI确认/保存/继续地图恢复。

前提/配置：系统/地图/事件/媒体与合法初始队伍、捕获道具须由完整工程提供；普通流程无DEBUG跳过/模式覆写、异常与额外改写；当前材料不包含上述完整工程，不补造初始授予/遭遇可达事件；起始地图/位置与注册新游戏值；遭遇版本/表/地形/可战斗成员/步进门；捕获容量/送盒选项；save magic_number/safesave/类型与已加载标志。

| 边界 | 本次独立核对 |
| --- | --- |
| 正常 | 条件齐全才有静态连接：新值→地图/遭遇→战斗→接收→玩家/储存保存→继续加载。各入口结果不是单一通关布尔。 |
| 失败 | 无起始图/系统材料不能证明启动；无可战斗成员步进遭遇早退；战斗覆写/异常可跳过正常链；保存类型失败在打开前、IO失败仅回退save_count，继续可在地图恢复失败。 |
| 取消 | 保存确认拒绝不写盘；接收/命名取消语义由J13；标题与覆盖存档额外确认不能替代领域提交回滚。 |
| 重复 | 新游戏只初始化有值且未加载/强制重置项；继续会话统计再增；重新建立遭遇服务，不从持久全局字段推定临时触发器跨档保持。 |
| 顺序 | 保存捕获后的真实状态须正常到保存取值；先接收部分提交后保存只可能保存实际前缀；没有总事务、可玩Demo或成功恢复保证。 |

已审：初始化对系统/起始地图依赖；新游戏值加载→遭遇setup；步进生产候选→生成/可覆盖战斗→正常核心返回；J13接收后玩家/存储随正常保存恢复；保存取消、IO/类型失败、继续地图重建条件。
未审：真实新游戏→初始队伍/图鉴/球授予→遭遇地图→捕获→继续完整Demo；所有遭遇概率和战斗轮次；用户输入/媒体；任意旧档转换/断电/损坏文件恢复；不存在运行通过声明。

静态向量（均NOT_EXECUTED）：
- GR4-J14-V1：所需工程数据齐全、合法授予和遭遇前提已成立、普通捕获正常接收并成功保存 → player含队伍/图鉴、storage含盒子写入通过各自注册单元恢复；地图/遭遇随后恢复；这是条件静态交接而非实测。
- GR4-J14-V2：本次固定参考材料状态 → 真实地图/系统/完整Demo交接未证；不制造端到端PASS。

R源锚点（仅审计，不复制源码）：
- `Data/Scripts/003_Game processing/001_StartGame.rb` L4–16,39–104,111–124：新游戏/继续/保存与地图依赖。
- `Data/Scripts/002_Save data/004_Game_SaveValues.rb` L3–8,35–47,63–102：相关持久单元。
- `Data/Scripts/012_Overworld/001_Overworld.rb` L172–218：步进与遭遇守卫。
- `Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb` L7–27,445–468：上下文setup/生成通知/主动请求。
- `Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb` L356–440：覆盖门/核心开战/返回分层。
- `Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb` L479–511：正常终局接收交接。
- `Data/Scripts/002_Save data/001_SaveData.rb` L24–60：读取/转换写回/汇编先于覆盖写。
- `Data/Scripts/002_Save data/002_SaveData_Value.rb` L239–282：已加载门与新游戏/汇编。
- `Data/Scripts/016_UI/014_UI_Save.rb` L100–121：UI确认/覆盖确认/保存结果。

B正式锚点：
- `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md` L85–115：启动/继续/保存边界。
- `deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md` L151–158：步进全链。
- `deliverables/final-specification-set/pokemon-rules/wp38-capture-and-receiving.md` L104–118：接收提交。
- `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md` L5–27：配置/入口非可玩证据。

历史映射：G2-6, G3-1, G9-2, G9-4, G9-6, CHAIN-2；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。

## 历史与交付边界

junctions.json的historical_coverage完整保留共享导航54 junction + 8 chain + 18 new chain各条原normal/failure scope、固定身份、原对象摘要及后继绑定。其整条status仍为not_reviewed；有本次有限投影的标historical_qualified_evidence_reused并列GR4-Jxx，其余not_reviewed。共享导航验证不转成语义通过。

GR3 CLOSED不重开；旧229/341的每条限定scope保留，A053也仅增加上述孵化投影；可选GR3-M09-001继续暂缓，GR4-M02-003依用户指令不需修订。没有新的GR4-J-001待质疑；已有模块问题的最终独立质疑/接受由父会话处理，本报告不替代该步骤。

新游戏至保存继续只建立条件静态交接。真实起始队伍/图鉴/球授予、遭遇地图、接待事件和完整Demo缺材料，故J14为partial，不将工程缺项判成不存在能力，也不制造运行成功。

产物：report.md、junctions.json、shared-capabilities.json、findings.json、execution.json、progress.md。附read-log.json、candidate-counterevidence.json与审计生成/校验工具，均位于J目录。
