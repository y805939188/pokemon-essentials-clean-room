# 第四轮全局独立 Review · M11 图鉴与旁支玩法

结论：本次有界双向语义审查完成。登记 **1 项 P2 必修：GR4-M11-001**（图鉴保存异色记录，但预览/条目固定请求普通外观的消费规则缺失）。21 个能力样本中，20 项在所列条件内得到 `supported_static` 支持，1 项 `partial`。这些数字不是全域功能分母或全文件通过率。无 P1，不以找够数量为目标。

GR3-M11-001 的四条验收已重新回源核对，当前正文和消费者仍支持，旧 **CLOSED 保持**。新问题涉及外观参数消费，与旧栖息地掩码无同根关系。

## 身份、基线与边界

- 审者：**M11 / thread `01a13017-c27c-7020-a9f8-9bb66eb74f64` / CLI PID 67804**。身份只读取本轮 `tasks/M11-launch.json`；父 thread 为 `01a12fc2-e8c0-7e43-a721-ccfe659d75c8`。未把运行环境内部标签当作父会话身份。
- 请求配置：gpt-6-astra / ultra / default / Fast=false；实际模型回显 **UNVERIFIED**，不作已确认声明。
- 正式 B：`1f36475d22120a0d1175967d5b17d71fe8311d88`，tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`；受审集合 `deliverables/final-specification-set/` 共 131 文件。
- 参考 R：`/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`；commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 逐字身份及材料 readiness 复用共享 `baseline.json`，不重核全仓。当前 `PARTIAL_READY`：脚本/PBS可读；没有 Graphics、Audio、真实地图和完整 Demo；宿主运行未成立。`knownpoint.bmp` / `selpoint.bmp` 的存在按共享基线保留，不误列缺失，不接管 M12 工具审查。
- 仅审查、取证、报告和本目录内数据核验；未修改参考或正式规格、未实现框架、未提交或更改配置、未启动其他 agent。

## 实际盘点与方法

已先读 AGENTS.md、共同任务书、baseline 与身份记录。按脚本入口、配置、数据定义及消费者扩展来源，再以正式正文、附表、测试目录反向核对；不是按旧问题列表逐项复述。

主来源是 `015_Trainers and player/005_Player_Pokedex.rb`、`016_UI/002`–`004` 图鉴、`008`–`011` 齿轮/地图/电话/音乐、`013_Items/004_Item_Phone.rb` 与 `017_Minigames/001`–`007`。追入暂停菜单、物种取图、物品槽增删、遭遇版本枚举、获得包装、地区查询、配置、背景音乐覆盖与地区图鉴编译。`source-scope.json` 逐文件列出 114 个定位结果及直接依赖，区分语义读取锚点和仅盘点；宽检索的附带命中未升级为已审。

本域主正式文件是 12 份正文/附表：WP62；WP63；WP68 Triad/Duel；WP69 Slot/Slot-Reels/Voltorb/Voltorb-Layouts；WP70 Mining/Mining-Data/Lottery；WP71。另读 WP66-B 图鉴部分、三个共享测试目录中的 PD/VF/LT、PG/PL/DU/SL/MN/TP/BX 与 TT，及本域必要共享合同。`spec-coverage.json` 共 23 份文件记录，逐份注明已核合同、支持证据和未审部分；scope/README/测试索引只审相关范围声明和导航，不把历史审批层当本轮语义证据。

新问题的负证据检索覆盖全部 131 正式文件，使用中英图鉴、异色/闪光/shiny、普通外观、忽略/固定/强制等别名与审计符号；读回图鉴记录、WP66-B展示、WP15通用资源、摘要/邮件、调试登记及相关测试的命中上下文。完整搜索词、匹配路径/行和处置见 `negative-evidence.json`。没有把“首篇没写”直接判为缺失。

## 有区分力的已审支持

下表 R 路径均在固定参考 commit 下，短名对应 `source-scope.json` 的完整路径；B 章节均绑定以上正式 baseline。细化前提、分类、未审部分在 `capabilities.json`。

| 能力样本 | 实际核对及准确源锚点 | 当前正式承接 / 本次结论 |
| --- | --- | --- |
| 图鉴记录 | Player_Pokedex 41–69、115–139、195–227、279–358：守卫/登记失败分开；seen与owned独立；首写与覆盖；形态计数只查0/1；可关闭刷新与clear保留解锁 | WP62 §2–4、PD01–05/20–24/26–27；所查分支 supported_static |
| 地区与世代 | Player_Pokedex 315–341；Utilities 380–418；Compiler_CompilePBS 593–628；Settings 17、306–319；Utilities_Pokemon 48–128 | WP62 §3.2/5、WP02配置表、WP26：当前地区分支不查解锁；空表失败与UI回退分离；世代6/7改变新条目展示门，两个静默入口见过写入不同 |
| 栖息地及地图 | Pokedex_Entry 302–351；Encounter 30–35、53–59；RegionMap 94–99、183–228 | WP62 §5.3.1、WP63 §3、WP66-B §7.1、U05-HAB01–04：10000一格/11111五格、缺尾格不亮、可见点并集与地图首条/游标长度并存；旧回归支持 |
| 图鉴搜索/浏览 | Pokedex_Main 338–414、771–848、1224–1238、1255–1283；Pokedex_Entry 154–199、440–483 | WP62 §6、WP66-B §6–7、PD28–34：Start空结果仍写持久排序，Cancel不恢复；形态选择首轮写入且BACK不回滚。异色图像消费另有本轮缺口 |
| 齿轮与地图 | PauseMenu 133–155、206–235；Pokegear 89–113、134–205；RegionMap 70–152、173–244、294–355 | WP63 §2–3、PG P01–11/33–38：持机与TOWNMAP入口互斥；显式区域/无定位回退；隐藏首条不回退；编辑器未修改BACK直接退出；飞行返回及调用方写入分开 |
| 电话 | Item_Phone 18–113、118–143、172–188、227–310、328–407、414–559、583–705；UI_Phone 160–185、210–269；PhoneMessage `try_get`；PBS/phone.txt 3–48 | WP63 §4–5、P14–28/31–32/39–46、PL01–18：无机直写、隐藏再注册、普通反馈先写后失败；再战/来电不同计时；版本/信号/NPC零公共事件失败；每通TP/TE固定一次、TE前四槽均匀 |
| 音乐 | Jukebox 65–148；Game_System 65–81、140–148；Overworld_Metadata 135–149 | WP63 §6/8、P29–30/43–44、WP15：Custom覆盖与March旗标独立，换图清旗标不清覆盖，目录缺失与空列表不能合并 |
| Triad | TripleTriad 13–84、258–346、371–449、638–943、968–1041、1048–1243；PokemonBag 237–299 | WP68 §2–7、TT01–26、WP27 §3.2：量化严格上移、准备副本归并、按槽抽样、maxLevel不扩抽取域、samewins递归/评分差异、无整局取消、direct败局异常、prize覆盖、满钱卖牌仍删 |
| Duel | Duel 94–137、138–313、320–327 | WP68 Duel §2–6、D01–12：16格损失逐支对照；敌权重3:4:4:2→3:4:4；特殊只一次；双归零玩家判负；动作菜单BACK不退出。移动请求不当坐标回滚保证 |
| Slot | SlotMachine 8–99、147–272、313–455 | WP69 Slot §1–6、S01–16：简单取小/困难取大滑移，重复USE重抽同轮；重玩帧DOWN可先扣币；信用0与持久余额0不同；离场只记净差，支付触顶清剩额 |
| Voltorb | VoltorbFlip 126–219、356–523、667–704 | WP69 Voltorb §2–6、VF01–18：免费格行或列无雷、严格F/G门、1000次失败仍末盘；已揭可标记；领取先写余额；等级1可重开而等级2–8踩雷倒置夹限失败 |
| Mining | Mining 42–64、266–438、474–527、529–645 | WP70 Mining §2–6、M01–22：候选权重不是最终出现率；物品位置内层无上限；中心铁厚2/3分叉；49损耗坍塌先于全挖完但仍领奖；闪光后才登记、逐件部分成功、重复领取非幂等 |
| Lottery | Lottery 5–46；PokemonStorage 388–395；Utilities 516–519 | WP70 Lottery §2–5、LT01–16：日期seed和重播种；7/00007五位匹配；蛋不排除、队伍先遇优先；第二遍也含队伍；空洞可在写结果前失败；同变量按末项覆盖；检索不发奖 |
| Tile Puzzle | TilePuzzles 189–238、250–366、369–508、511–607 | WP71 §2–10、T01–26及空态反向：7模式主要动作；默认4×4与2×3/3×2异常分开；完成先于输入、完成BACK真/进行中BACK假；默认模式6/7五步非完成静态证明及箭头/暂持显示门 |

本域七个小游戏未定位独立 `MECHANICS_GENERATION` 分支；不因此断言数据替换不影响 Triad。其卡值消费已加载物种基础值/类型，默认世代8和备份数据全量另有边界。此次只深查图鉴新获得展示的世代6/7门，不声称穷尽代际组合。

## 新问题与反证结果

**GR4-M11-001 · P2 · REQUIRED · 实现信息不足**

参考记录可以是 `[性别0,形态0,异色true]`；主列表选中物种预览却固定请求普通前图（`016_UI/003_UI_Pokedex_Main.rb` 766–768）。完整与简略条目在共同刷新中也固定普通外观，用于 Info 图、Forms 前/背图与物种图标（`016_UI/004_UI_Pokedex_Entry.rb` 139–151，入口 5–67/71–116/582–617）。取图服务直接消费这个参数，普通请求不因为保存的异色true转去异色目录（`014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb` 64–68/253–258；`010_Data/002_PBS data/009_Species_files.rb` 3–34/47–52/86–89）。

WP62 §2/4 记录异色，WP66-B §6/7描述形态显示；但两者未说明此固定普通请求。已经记载的“进入形态选择器首轮写false”发生在另一步：在不进入选择器的主预览/Info上，图像已经普通，而末次异色true仍保留。不能用清除图鉴记录来仿造显示结果。

最小静态对照：合法已见/拥有的雄性 BULBASAUR 基形，末次true/false各一组，其余条件相同；假设普通与异色资源均存在且不同。两组图鉴预览和Info均请求普通，保存值分别保持true/false。当前正式合同允许实现方把整组三元组用于通用资源选择，得到异色外观，无法仅凭合同排除。简略条目同理；仅异色已见仍可满足形态列表资格，也不增加异色切换项。

全规格反证命中主要是：WP15按传入参数选资源；WP17物种图标可读闪光参数；WP66-A摘要编号染红和邮件个体快照；WP72调试登记异色；WP62记录本身。它们都不能决定图鉴消费者传什么参数。相关正文/测试未发现补足条款。源端全脚本检索只定位现有两处图鉴消费者定义，读回完整与简略调用、资源透传及配置，未见固定环境覆写改变该规则。插件未查明，不外推。

建议只补**参考事实层**与成对未执行向量，在WP62/WP66-B及对应测试目录同步；保留普通刷新不写记录与Forms选择器已有写入差别，不改变WP15通用合同，也不替未来产品决定是否增加异色浏览。准确前提、影响、范围、验收及排除声明全部见 `findings.json`。本项以 M11 主责登记，WP66-B 为 M10 交界投影，供父汇总者去重。

另核过而未成 finding 的怀疑：Triad同身份多槽抽牌后的扣减位置由WP68引用的WP27按序扣减合同承接；Voltorb高等级踩雷、Mining位置无界重试、老虎机信用耗尽未自动退出、彩票无兑奖事件均已如实保留，不因参考异常再报“规格需修”。

## 历史回归

仅本域相关旧必修 **GR3-M11-001**。固定历史导航：

- 原问题：`d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65:review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/findings.json` 的该ID。
- U05实际独立验收：`1cb48da29e9363a2947eb16c75461bc3e76ae726:review/remediation-third-20261012-prepare/U05/actual-integration/independent-review/attempt-01/per-id-verdicts.json` 的该ID；受审actual为 `6eb83dc0f4c9b2cbaf4bc5a6a972387a49ae4ea1`。
- 正式接受：`c2eb74c7cbcf8a190d5e902d871fbce44904efd6:review/remediation-third-20261012-prepare/registration/U05-formal-acceptance.json`。

这次新读当前WP62 §5.3.1、WP66-B §7.1、WP63 §3及U05-HAB01–04，独立推演1格/5格/缺尾格、缺省/宽0、首条隐藏仍可并集点亮、版本枚举缺陷保留四组条件。`regression.json` 逐验收标准和消费者登记 `supported`，含义严格为 supported_static；不迁移旧PASS、不改旧身份或CLOSED。

## 执行、限制与未审

执行前已记录 `validation-plan.md`。实际仅运行本目录的只读字面数据比较，Python 3.14.0；命令、UTC起止、输入、输出、exit code 0、副作用见 `execution.json` / `data-validation.json`。

- Slot-Reels：全部66位置及图案频次一致。
- Voltorb-Layouts：75行原始五参数、补足的一格数及固定乘积一致；最大固定乘积3456。
- Mining-Data：61候选、13铁形状的顺序/身份/权重/尺寸/占位/掩码一致；48物品身份及口袋一致，权重总2370。

这是 **TOOL_VALIDATION**，不是 EXECUTED_MODEL、EXECUTED_REFERENCE 或 EXECUTED_HOST_OR_DEMO。没有执行游戏、Ruby参考路径、随机生成器、对局模拟、图鉴反例、编译、反序列化或真实存档。其余推导为 SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR，执行状态单列 NOT_EXECUTED。

明确未审：所有真实地图/NPC入口、台词实参、小游戏奖励兑换事件与限次/刷新；Graphics/Audio/字体实际呈现、宿主输入与异常恢复；老虎机最终中奖率、Voltorb接受分布、挖矿布局/不可终止可达率、Triad五抽联合分布；拼图非默认尺寸完整可达性/最短解；图鉴全部战斗/回放/孵化/进化写入者、搜索尺寸子页所有导航和locale；全量物种/形态/地区表顺序、备份世代/PBS配置组合、翻译全文、序列化输入、外部插件与动态调用。可读而未审的文件在 `source-scope.json` 逐项保留为仅盘点，不能计作缺功能。

本次没有修改全局Feature Matrix或共享进度，遵守唯一写入目录；能力样本与交界投影交给父汇总者整合。完成产物后结束，不继续扩大范围。

## 产物

必需：`report.md`、`capabilities.json`、`spec-coverage.json`、`findings.json`、`regression.json`、`execution.json`、`progress.md`。

补充：`source-scope.json`、`negative-evidence.json`、`review-identity.json`、`validation-plan.md`、`data-validation.json`，以及本目录的数据核验和报告组装脚本。所有输出仅在 M11 目录。
