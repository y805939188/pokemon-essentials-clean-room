# 第四次全局独立审查：M04 个体规则

结论：本次有界双向语义审查确认 **1 条新的 P2 必修问题 GR4-M04-001**。其余已核分支按 `supported_static` 或 `partial` 登记；不作全域通过、全功能覆盖或运行成功结论。正式规格与参考文件均未修改。

## 身份与固定输入

- 审者：M04，独立 CLI thread `01a12fdc-618e-7ea1-be11-c267b26fdb3d`，PID `61899`；来自只读 `tasks/M04-launch.json`。父 thread 是 `01a12fc2-e8c0-7e43-a721-ccfe659d75c8`，不是本审者身份。本报告没有用内部 `/root` 标签冒充父会话。
- 请求模型为 `gpt-6-astra`、reasoning effort `ultra`、service tier `default`、禁 Fast；实际模型配置回显 **UNVERIFIED**，不声称确认。
- 正式 B：`1f36475d22120a0d1175967d5b17d71fe8311d88`，tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`。131 文件身份使用共享 `baseline.json` 与 `delivery/2026-10-12/formal-identities.json`，未重核整仓。
- 参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只读根 `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`。
- 已读 AGENTS.md、共同任务书、baseline、launch。只写本 M04 目录，没有派生 agent、提交、push、安装、网络访问或框架实现。所有锚点只供审计，不要求未来保留源符号、对象关系或 API。

## 本轮范围及方法

先从个体主定义、形态注册、Mega/Shadow 扩展、数据定义和调用入口发现能力，再反向检查 WP18/19/20/21/22/23。读了 6 份主稿、2 份数据附表；两份混合测试目录只核本域所列条目，另读 scope 的材料/证据限定。WP15 资源消费与 WP77 GIRATINA 读取说明用于反证，共在 `spec-coverage.json` 登记 13 份文件的实际合同范围。

源端先用 `rg` 检索相关目录/符号，后追读必要 caller、override、handler、配置和数据定义。`source-scope.json` 保存对全部 **312 个脚本**的候选发现规则与完整候选路径，并盘点有关默认/备份 PBS 和 18 份翻译文件。191 条候选记录包含脚本、PBS、翻译；**候选命中不是已读数量，更不是功能分母**。每个语义已读文件都有范围，未读命中归 `inventoried_only`；缺失宿主/媒体单列，不能拿材料缺失抹掉可读的静态规则。

双向核验以正常、分界、异常、世代/配置条件为单位：源能力是否在正式集承接；正式断言与静态测试是否有源依据。仅对确认的问题执行全 131 正式文件的别名反证搜索，不把其它文件未通读说成全套语义审核。全局 Feature Matrix 未写入；本轮能力贡献只留本目录，供主汇总者整合。

## 已核支持与边界

`capabilities.json` 共 **26 个有界能力样本：17 supported、9 partial**。supported 仅表示所列条件的 `supported_static`；不是 26 个全部功能。以下是辨别力较高的核验，不以历史 PASS 替代：

| 合同组 | 关键正常/边界/异常核验 | 精确证据导航 |
| --- | --- | --- |
| 物种与创建 | 缺省字段与形态继承；同基物种设置不切形态；初始化性格已缓存；创建复检返回0仍提交，关闭复检/非零初始形态跳过 | CAP001–002；Species 151–220、Compiler 448–484、Pokemon 1159–1225；WP18 §3–4、CI-25–28 |
| 所有权与复制 | 外来比较 id/名字，语言不参与；训练家现有语言复制；副本 PP 独立、markings 和 Shadow 暂存EV共享边界 | CAP003–004；Owner 19–70、Pokemon 838–905/1133–1150、Shadow 212–219；CI-10–22、SH41 |
| 类型/性别/闪光 | 性别31/32与127/128分界；单性别守卫；普通与超级异色独立缓存；世代6前阈值8、之后16；PID/owner变化不自动清缓存 | CAP005–006；Pokemon 312–418、GenderRatio 40–82、Settings 135–137；ST21–33/41–45 |
| 特性/性格/描述 | 隐藏槽缺失回自然但索引保留；显式特性不验物种；性格覆盖存在时可清表现缓存而不重派；25性格映射；原始IV的速度先于特攻环序 | CAP007–008；Pokemon 424–545、Nature 30–173、Summary 589–634；WP19 表N/个性表、ST60–66 |
| 数值与生命 | EV3→4整除档位、Nature第二次取整、基础HP1特例、禁用IV/EV只影响计算；濒死且上限增加可回正；存活HP最低1；蛋HP0保异常但清准备/Hyper | CAP009–010；Pokemon 244–306/1073–1126、Shadow 22–26；ST01–20、HP-05–11 |
| 招式与持物 | 五项列表新增只移首一次；已会招移尾保PP；首招整表保重复；负PP提升计数失败时已改计数但保旧PP；未知持物在个体与战斗入口结果不同 | CAP011–012；Pokemon 551–723、Move 15–47、Battler 85–89；HP-18–26/35–39 |
| 形态 | forced0优先，战斗/仓库不动态求值；裸同值提交仍执行；FURFROU恰5天/超1秒；ARCEUS火为10；ROTOM同值可删空，KYUREM压缩跳项，NECROZMA旧超形态跳过 | CAP013–015；FormHandlers注册文件及Pokemon 147–184；WP21 §3–4、FM13–20/36–43 |
| 图像与尺寸 | 四形状逐行点集、PID位组/锚点、2×2共享采样与重叠；分帧PNG与原生位图不同；尺寸低位输入与两阶段取整，默认段65410起而基准65510 | CAP017–018；FormHandlers 41–140、Species_files 65–109、AnimatedBitmap 14–205、Utilities_Pokemon 243–271；SP/SZ测试族 |
| Mega/Primal | 48目标条件/BaseStats；SLOWBRO0→2而1不合格；RAYQUAZA PP0仍有资格；BANETTITE；METAGROSS默认HP异常；业主环/次数门；Primal移宝珠后身份假且裸解除不动 | CAP019–021；MegaEvolution 6–81、ActionOther 67–199、PBS具名节；ME02–10/13/15/19–21/26 |
| Shadow与净化 | 131量表/招序、25性格下降行；G0仍Shadow，重复建立非幂等；H4/5 EV落普通分支；S121恢复请求96；香先友好后减量；TIMEFLUTE门不相交；净化室跨级首窗口失败与遗迹石对照 | CAP022–025；Shadow本体、ShadowPokemon_Other、ExpAndMoveLearning 59–89/160–184、Item_Utilities 132–221；SH相关向量 |
| 净化室数学 | 任一有向属性有利而非复合倍率；单NORMAL自环T2/F2；四NORMAL外圈T14，NORMAL中心F7；G15→8→1→0；LUGIA要求九组节奏，删除朝向可漂移 | CAP026；PurifyChamber 52–262；WP23 §8、附表§2、SH29–35 |

这里的简称均可在 JSON 中解析为 R 固定 commit 下完整路径。表内没有声称已执行这些行为。形态注册文件完整读过不等于所有76物种的全部调用/PBS/跨流程组合都通过。

## 新问题与反证

### GR4-M04-001 · P2 · REQUIRED · 状态或时序错误

WP18 §3.4 第151行把图像列作 `form_simple` 消费者。R 的 `Data/Scripts/010_Data/002_PBS data/009_Species_files.rb:92–109,123–124` 则在按个体取正/背精灵和图标时求值普通动态形态。上游精灵入口 `003_Pokemon_Sprites.rb:49–60,124–134` 与摘要 `006_UI_Summary.rb:117–134` 均确实接入该路径。普通形态读取的状态门在 `001_Pokemon.rb:147–165`。

最小静态反例：合法非蛋 FURFROU，存储形态1、无强制形态、非战斗/仓库、时间戳t，当前t+432001秒，期间没有其它动态形态读取。仅按个体取图就会先把形态提交为0、清时间戳，再选择资源；按错误的简化读取合同则保留形态1与旧时间戳。恰t+432000秒、战斗/仓库状态和强制形态分别是反向对照。若比较实际画面，另需对应图片存在；**状态求值/提交发生在资源选择前**这一事实不依赖本轮素材运行。

全 131 正式文件搜索了 `form_simple/简化形态`、`取图/图像读取/按个体`、`FURFROU/HOOPA/限时/5天`、`动态形态/读取副作用`，并读命中上下文：

- WP18 正確区分了两类形态读取，却误分配图像消费者。
- WP15 §4.1 只概括按个体形态取图，没有指定两类读取之一。
- WP21 §3.2-R03 保留读取副作用，但回指既有派生规则，未消除 WP18 的明确误述。
- WP77 第145–146行及 B20-C029 正確说明 GIRATINA 的普通/简化读取守卫，未把该规则连接到图像消费。
- FM07 与 U03-SP07–10 分别核限时形态、个体修饰/帧，没有本反例的消费者连接。

因此这不是“全套缺动态形态能力”的结论，而是一个具体消费者归属错误。详见 `findings.json` 的完整反例/验收要求及 `negative-evidence-search.json` 的全套命中路径/行号。建议去掉 WP18 的图像泛称，明确个体取图的动态求值及守卫，并新增到期取图对照。只要求规格准确承接 R 事实，不要求保留源 API 或实现架构。

本项与 GR3-M04-001 的 SPINDA 像素数学属不同规则，关系为 **new**；不重开旧关闭记录，第二轮未知关联为 null。等待主汇总者安排一次独立反证/去重。

## 历史回归

- **GR3-M04-001：CLOSED 保持。** 本轮重新核四形状全部43行点集、8个位组、坐标/色彩/重叠、按个体/蛋/物种入口及PNG独立帧/原生宿主位图边界。WP21 §3.2-R03 与 U03-SP01–10 支持这些验收要求，未发现本范围回归。
- **GR3-M05-001：CLOSED 保持，历史主责仍为M05。** 因合同落在本域 WP18 §7.4，本轮核尺寸辅助投影：原始IV/PID输入、完整15分段两端、203/209/210mm及s113先取整得到280mm。脚本检索只定位定义，不宣传默认用途已启用。
- 历史固定验收分别引用 `08fc8828229c14ab4a540db417d08194ba194a31` 的 U03 `per-id-verdicts.json` 和 `c2eb74c7cbcf8a190d5e902d871fbce44904efd6` 的 `U03-formal-acceptance.json`；当前核验绑定 B，不把旧PASS移签。具体 criterion/consumer 与限制见 `regression.json`。

## 执行证据

先写 `validation-plan.md`，后运行 `check-data.py`，Python **3.14.0**，退出码 **0**。`execution.json` 记录实际命令、UTC起止、输入、stdout/stderr与副作用。核得48个Mega条件/BaseStats、47石/1环、131个Shadow量表/有序招式、25性格下降行、四斑点逐行点集均 **MATCH**，结果见 `data-check-output.json`。

证据种类为 **TOOL_VALIDATION**：只比较文本数据，未执行参考、PBS编译、随机服务或独立行为模型。四形状60/51/122/110点只是全行点集比较的附加统计，不以点数相同替代形状一致。所有正常/异常/数学场景为 SOURCE_STATIC＋SPEC_STATIC＋DERIVED_VECTOR，execution_status 单列 NOT_EXECUTED。

## 可读未审与材料限制

- 可读未审：Gen5–8备份与默认的全部差异；pokemon_metrics 的完整布局数据；131 Shadow配置以外的18招效果和4道具字段全量消费；多数训练家/遭遇/繁殖/进化/捕获生成调用链；设施EV255后续培养边界；战斗PP同步、伙伴持物还原、Mega菜单取消/追击/终局/AI/回放的完整链；净化室储存选择负位置/暂持/容量完整交互；标记UI/迁移、所有76物种跨流程组合；18份翻译逐文案。具体已读切片与未读候选可逐文件查 `source-scope.json`。
- 无可验证完整材料：Graphics/Audio、地图与完整Demo；继承共享 PARTIAL_READY。根两张BMP存在不填补精灵和界面素材缺口；未读取为图像证据。Ruby可用不代表参考或宿主已运行。
- 未执行：参考Ruby行为、游戏宿主/Demo、PBS编译与载入、图像像素/原生动画帧、真实存档、行为模型。未伪造运行结果；数据校验不升级上述状态。
- 净室检查：所读合同主要使用独立数学/行为描述；本轮未发现需单列的代码拷贝或架构强制问题。未对所有131正文进行净室全面审计。

本模块的计划内取证、反证、回归与产物已完成；不继续无限自审。
