# A-07：WP30–WP32 独立复审报告

结论：**REQUIRES_REVISION_SCOPED**。新增 5 项（P2×2、P3×3）；未得出任何整包 PASS。四份原稿与四份最终正文（含 WP32 附表）均全文阅读，GR44／BE35／CX38 共117条主范围测试逐条对应；WP66-A 的两条重学测试只属依赖定点。

## 固定身份与独立性

- 项目固定基线：`e1e01bb18d824931e54f182dd61af5a9f908ba85`。
- 参考只读基线：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。
- 首判于 2026-10-03 17:11:24 UTC 保存于 `independent-judgment.md`，未改写；五项候选均经来源收尾保留。
- 未读其他组或根审关于本批 WP30–32 的结论。先前获授权 X-A-CAPTURE-PARTNER/X-A-EDIT-CACHE 定名比较材料的知识如实保留；本批依赖正文的旧PASS不作为当前结论。
- 原授权 Astra／Ultra 沿用；Standard 速度没有可核验回显，记 UNVERIFIED，未改设置。未启动子代理。

## 范围与覆盖

| 工作包 | 实质阅读范围 | 结论 |
| --- | --- | --- |
| WP30 | 六曲线/反向边界、经验与EV全部主分支、等级/经验工具、两版学习/遗忘/重学、友好度/亲密、配置/直接消费者 | REQUIRES_REVISION_SCOPED：047/048/049 |
| WP31 | 全部方法注册、五入口/统一门、提交/复制/取消、调用入口、默认样本和全部BE测试 | REQUIRES_REVISION_SCOPED：050 |
| WP32 | 情境家族、战前/逐击/濒死/战后记录、捕获移动、交换/事件、35身份/57数据行和全部CX测试 | REQUIRES_REVISION_SCOPED：051；既有伙伴持物问题传播 |

日志 98 行；具语义范围的参考文件 49 个；来源覆盖 49 行；对应表 302 行（含117测试、57内容行、35情境身份、64进化注册身份）。数量只作导航，不替代语义审查或证明整包通过。

本批新读全文：成长曲线、战斗经验/学习、进化注册、进化演出、重学界面、世界天气和战斗存储接点。Pokemon/Species/Shadow、通用道具工具、物品处理器、队伍/储存/交换、时间和配置等同一审查人前批的固定版本全文阅读具名复用，并对本批关键段重新读取。日志区分当前、复用与定点；PBS只认57条和具名样本，战斗/UI依赖只认日志范围。主行为族进行了源→规格与规格→源、原稿→净化→测试三个方向核对。

## 新发现

| ID | 级别 | 主题 |
| --- | --- | --- |
| RUN-A-047 | P2 | 经验缩放合同缺少先整除5和基础份额为零的早退门 |
| RUN-A-048 | P2 | 空重学候选在初次绘制时失败，不能正常进入空列表取消 |
| RUN-A-049 | P3 | 战斗学招遗忘选择实际使用单个体摘要画面 |
| RUN-A-050 | P3 | 进化完成前可见新种白色剪影 |
| RUN-A-051 | P3 | 三成员捕获替换示例需显式声明队伍容量已满 |

完整结构化字段见 `findings.json`。下面项目/参考定位分别绑定上述固定提交。

### RUN-A-047 — 经验缩放合同缺少先整除5和基础份额为零的早退门

**当前文字与来源差异**：计算步骤写成÷5→等级因子→向下取整→参与/共享加1，未声明÷5处已先截断；份额形成后≤0早退也未进入步骤表。曲线章节的整数除法提示仅限定该表，战斗测试使用整除锚点不能区分。 基础参与/共享各份额先各自整数除法；份额结果≤0时在任何训练家/缩放修正前返回。缩放开时经验先整除5，再乘浮点等级因子、下取整及按资格加1；关时整除7。护符、亲密及当前已实现的幸运蛋还分别有整数截断。

**项目定位**：`specs/creature-rpg/wp30-growth-learning-and-friendship.md:86-102`；`deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md:89-105`；`deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md:134-143`；`deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:71-85`

**参考定位**：`Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb:100-163`；`PBS/pokemon.txt:237-261`；`Data/Scripts/002_BattleSettings.rb:102-117`；`Data/Scripts/010_Data/002_PBS data/008_Species.rb:68-75`

**最小向量前提**：普通内部野生战斗，经验开；默认CATERPIE等级2、基础经验39已倒下，参与记录仅玩家非Shadow非蛋可战斗成员A。A也为默认CATERPIE（Medium成长）、等级3、经验27、六项EV均0且上限余量充分。 默认缩放开、均分关，无Exp All/Exp Share、同拥有者ID与语言，无护符、无经验物品处理器（当前与初始都无物品）、亲密效果关；EV输入有效且无升级/形态额外干预。

- 基础78；先整除5得15；等级因子(14/15)^2.5≈0.8415732866；最终floor(15×因子)+1=13，A经验27→40，仍等级3。
- 若按未限定的实数÷5保留15.6，末尾才取整会给14（经验41），因此原测试整除数不能证明公式充分。
- 额外数据配置对照：合法基础经验1的等级1目标，均分开启、两名有效参与且无共享，各基础份额整数截断为0即返回，不会靠缩放后的+1产生收益。

**影响**：独立实现可以在默认内容与等级下每次多给1点经验；低基础份额的配置还会错误产生经验及统计，改变升级边界。

**最小修正**：用独立数学文字标出每次整数截断的位置、两个分配份额分别截断后相加、基础结果≤0早退门，以及后续整数倍率的取整；补78例和零份额例。

**确定性复核**：CATERPIE L2→参与者L3固定例必须+13而非+14。 基础份额0在缩放前结束，经验/经验统计不变；既有先行EV写入不回滚。 GR08–GR18原整数例仍成立，并明确GR15无有效参与者而非参与记录空。

### RUN-A-048 — 空重学候选在初次绘制时失败，不能正常进入空列表取消

**当前文字与来源差异**：WP30正确给空候选，但只写界面不可教、没有写启动失败。WP66-A原稿/最终稿及A32进一步明确声称照常打开空列表、BACK或空USE后确认并false。 候选计算返回空表后，包装仍无条件调用开场；初次绘制在进入选择循环之前取所选候选并查询招式数据。空候选无论游标取何索引都返回空，严格招式读取不接受空参数，故在此发生参数校验异常。正常选中/取消分支尚未到达。

**项目定位**：`specs/creature-rpg/wp30-growth-learning-and-friendship.md:158-162`；`deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md:165-169`；`specs/ui/wp66-a-party-and-summary-ui.md:177-181`；`specs/ui/wp66-a-party-and-summary-ui.md:200-200`；`specs/ui/wp66-a-party-and-summary-ui.md:247-247`；`deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md:179-183`；`deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md:202-202`；`deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:190-190`

**参考定位**：`Data/Scripts/016_UI/022_UI_MoveRelearner.rb:19-49`；`Data/Scripts/016_UI/022_UI_MoveRelearner.rb:52-107`；`Data/Scripts/016_UI/022_UI_MoveRelearner.rb:150-199`；`Data/Scripts/010_Data/002_PBS data/005_Move.rb:18-39`；`Data/Scripts/010_Data/001_GameData.rb:97-104`；`Data/Scripts/001_Technical/001_Debugging/004_Validation.rb:12-29`；`PBS/pokemon.txt:237-261`

**最小向量前提**：有效普通CATERPIE等级1，非蛋非Shadow，当前恰好掌握TACKLE与STRINGSHOT；最初招式记录为空；默认重学更多配置开。 通过直接重学入口打开，具备有效世界/显示上下文及所需字体、图片、类型数据，所有前序构造正常完成；没有外部事件在入口前屏蔽空候选，也无插件或异常拦截改变路径。

- 等级表只有两招在等级1及以下且都已掌握，得到空候选。
- 初始绘制右侧所选招式数据时出现参数校验错误；尚未到达BACK/USE选择或放弃确认。没有教学、提醒教学统计不变；包装没有正常false返回保证。
- 候选计算本身仍可正常返回空；若外部调用者先屏蔽空候选，后果另列，不能据缺失Demo事件推定其一定屏蔽。

**影响**：最终规格会要求一个参考入口没有提供的正常空状态交互；空候选测试A32的预期与可证明控制流相反。

**最小修正**：保留候选为空的领域规则；另外登记裸重学入口初始绘制失败及外部守卫未证明。修正WP66-A和A32，不把异常规范化为正常取消或修改reference修复。

**确定性复核**：从候选→开场→首次绘制→严格查招式逐跳核对，确认异常先于任何选择循环。 为非空候选保留拒教/取消不退出/满槽放弃再选/确认退出/成功计数原有测试。

### RUN-A-049 — 战斗学招遗忘选择实际使用单个体摘要画面

**当前文字与来源差异**：战斗版学习及遗忘选择描述为战斗队伍界面，而通用版才称摘要界面。 战斗包装与通用包装都传单个体列表进入摘要的遗忘画面，不是玩家选择队伍成员的画面。消费者返回招式槽或-1，并执行非调试不可遗忘HM的门。

**项目定位**：`specs/creature-rpg/wp30-growth-learning-and-friendship.md:144-158`；`deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md:151-165`；`deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:87-93`

**参考定位**：`Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb:247-270`；`Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb:441-455`；`Data/Scripts/013_Items/001_Item_Utilities.rb:630-637`；`Data/Scripts/016_UI/006_UI_Summary.rb:184-207`；`Data/Scripts/016_UI/006_UI_Summary.rb:1232-1268`；`Data/Scripts/016_UI/006_UI_Summary.rb:1355-1365`

**最小向量前提**：普通可显示战斗，玩家在场非蛋非Shadow成员有4个合法招式，新学招合法且未掌握；资料/图片正常，非调试。 学习询问中确认遗忘，尚未选择要遗忘的招式。

- 打开该单个体摘要的4个旧招＋1个新招布局。
- BACK返回-1至学习层；选择旧招返回该招槽（HM另有拒绝门），不存在先选择队伍成员这一层。

**影响**：成长规格与WP42已正确描述的学习界面冲突，可能产生错误界面流程或UI测试。

**最小修正**：两处战斗队伍界面统一为单个体摘要遗忘画面；保持战斗版结果同步与通用版机器PP分支差异。

**确定性复核**：战斗与通用包装均对接摘要遗忘合同；返回单位是招式槽而非队伍槽。

### RUN-A-050 — 进化完成前可见新种白色剪影

**当前文字与来源差异**：目标形态在完成前不可见。 开场最初隐藏新种展示，但动画启动即设置可见和白色覆盖，从零尺寸逐轮放大，与旧种交替缩放；成功闪白后才恢复新种正常颜色。全程隐藏与白色剪影不同。

**项目定位**：`specs/pokemon-rules/wp31-basic-evolution.md:175-178`；`deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md:152-155`；`deliverables/final-specification-set/user-interface/wp67-b-lifecycle-presentations-and-history.md:41-48`

**参考定位**：`Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb:22-81`；`Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb:99-125`；`Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb:152-177`；`Data/Scripts/005_Sprites/010_PictureEx.rb:290-322`；`Data/Scripts/005_Sprites/010_PictureEx.rb:362-459`；`Data/Scripts/005_Sprites/010_PictureEx.rb:483-508`

**最小向量前提**：普通CATERPIE→METAPOD已获有效目标并进入可取消动画；旧/新种图像均有效且有非透明像素、没有外部遮挡，显示更新和时间推进正常。 从缩放动画自身计时起已约2.6秒（第一个放大段到达大尺寸），未取消，也尚未结束约9秒动画。

- 新种展示已可见并放大，白色覆盖仍为满值，因此可见其轮廓；尚未进行成功提交或恢复新种正常颜色。
- 若此后取消，最终切回旧种；取消之前已经显示过的剪影不被追溯抹除。

**影响**：独立动画实现可能错误地只显示旧种直到结束，与同包前句及WP67-B双展示交替规则不一致。

**最小修正**：改为新种以白色剪影参与交替缩放，成功结束后显露正常颜色；初始隐藏、动画可见、成功揭示三阶段分别描述。

**确定性复核**：在初始开场、首轮新种放大、成功揭示三个时间点，分别核对不可见/白色剪影/正常颜色。

### RUN-A-051 — 三成员捕获替换示例需显式声明队伍容量已满

**当前文字与来源差异**：[A,B,C]捕获X替换A后直接给出[B,C,X]及三份记录左移结果，但未声明容量变体或它只是抽象移动示意。 只有队伍已满且接收策略允许/要求替换时才开放旧成员送盒。默认上限6，3成员直接追加新捕获者并补初始持物，不移动L0/K/D。已到达替换分支的左移算法本身正确。

**项目定位**：`specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md:84-90`；`specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md:146-146`；`specs/pokemon-rules/wp32-context-inputs-and-scenarios.md:133-133`；`deliverables/final-specification-set/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md:84-90`；`deliverables/final-specification-set/pokemon-rules/wp32-context-inputs-and-scenarios.md:133-133`；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md:70-70`

**参考定位**：`Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb:15-80`；`Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb:5-23`；`Data/Scripts/015_Trainers and player/001_Trainer.rb:65-83`；`Data/Scripts/001_Settings.rb:219-220`

**最小向量前提**：默认队伍上限6、普通玩家队伍恰为[A,B,C]，无伙伴、无外部重排；对应L0=[10,20,30]、K=[1,3,0]、D=[0,49,5]，正常战斗接收捕获X。 有有效储存、接收策略为询问或强制入队；此前捕获/命名正常返回。观察接收完成而世界战后扫描尚未开始的状态。

- 不显示选择A送盒的替换选择器，队伍直接变[A,B,C,X]。
- 三份记录仍[10,20,30]/[1,3,0]/[0,49,5]，索引3不存在；不会形成原示例的左移值。
- 要使原向量成为可达捕获流程：显式配置最大容量3、队伍3满、有空盒、接收策略允许替换并明确选送A；或改用默认6成员满队例。

**影响**：当前CX22缺少使目标分支可达的配置前提，自动测试照默认设置会观察追加而非替换。

**最小修正**：补齐容量3及替换/盒子前提，或换六成员例；若仅保留抽象数组关系，应标成不覆盖捕获入口可达性的算法示意。

**确定性复核**：默认容量6、3成员断言追加且三表不移动；容量3、3成员满队且选A送盒断言左移并末槽空。

## 既有根因、已排除疑点与受限结论

- RUN-A-044（新增计数0）：TR首招记录会影响重学候选；WP66-A最终174-177已正确区分背包与队伍两入口，不将A-06缺口扩大成全交付集未记。
- RUN-A-045（新增计数0）：WP31原215/245、最终192/222正确记满级糖果取消仍消费，作为对照，不重新报错。
- X-A-CAPTURE-PARTNER（新增计数0）：WP32原/最终25/65的当前持物读取位于已知伙伴捕获还原错配之后；顺序本身正确，不可把还原后当前物品等同成员自身初始物品。引用先前独立交叉审查，待根审统一canonical ID。
- TradeSpecies自身物种比较导致默认互换不进化，是被规格准确登记的参考行为；不新增规格错误。
- WP32-N02两次交换收尾位置及进化无待学项条件页的重复释放已有具名限制；本轮不证明宿主第二次正常抵达，不报告必定双进化。
- 检查/提交、事件触发true/实际成功、D转R/直接进化、世界天气/战斗天气均保持分层。未知标识、坏数据、资源缺失的全宿主恢复未作闭合。
- 表外成长曲线非单调按快照保留。固定常数算术只核本文具名数字，未执行参考公式或任何行为模拟。
- 原稿历史状态/哈希只作身份导航，不继承其正确性；本批P2尚未经过新一轮命名第二审。

## 限制与交付

真实运行观察0，证明Demo链0。未运行Ruby、游戏、编译器、生成器、反序列化加载或行为模拟器；未改reference、正式规格、全局矩阵/中央账本、实现代码或框架。U01–U10、G01–G12、既有20个AX保留。

交付 `report.md`、`findings.json`、`reading-log.tsv`、`source-coverage.tsv`、`equivalence.tsv`、`checkpoint.json`、`independent-judgment.md`。仅A分支新增A-07目录；发布后报告本地/远端相同精确commit，再按串行授权继续A-08。全部A主审完成后才读取设施还原的中立简报；该复核首判→比较→发布完成后，才做新排队X-A-C05-RECHECK，绝不提前读其报告。
