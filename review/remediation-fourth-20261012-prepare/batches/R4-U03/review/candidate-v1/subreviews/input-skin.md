# R4-U03 input-skin 独立候选子审

**PASS：GR4-M10-001、GR4-M10-002，仅指定候选静态范围。** 未作 ACTUAL_PASS 或接受/关闭登记。

候选 `58cd8b1585f17199a65c7b82afadbe0e326d9d30` / tree `c1b72453613645ac5e9928e748364348c1bd179c`；固定B `1f36475d22120a0d1175967d5b17d71fe8311d88`；固定R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；任务包 `08a57fb55118914a74ac1ffaf617647c01df8938`。已读取前置 `2b60c7bd0dce8d972e34a9d86a8f6cf6a3b1dd65` 的 freeze-and-publication.json 身份与R4-U03条目。

真实任务 `/root/input_skin`；可见 `CODEX_THREAD_ID=01a130e0-003f-7306-ac36-38168276603b`。请求 gpt-6.1-sol / ultra / default / Fast=false；实际回显 UNVERIFIED。

新增参考／模型／宿主或Demo行为执行均为0，**NOT_EXECUTED_THIS_UPDATE**。证据只有 SOURCE_STATIC、SPEC_STATIC、DERIVED_VECTOR、TOOL_VALIDATION。

## GR4-M10-001 — PASS

| 原标准序号 | 原标准 | 结果及依据 |
| --- | --- | --- |
| 1 | 仅凭正式集可唯一推出上述命令2/0与数字合法/越界四分支。 | PASS。候选WP17 L97、103–107与132–143分列取消>0/<0/=0、合法确认及越界等待；源码Messages L730–748、772–792和180–201确定不同出口顺序。两命令入口先方向/帮助更新再BACK，取消0只忽略BACK，仍可同轮USE；逐位数字先编辑且USE成立时不处理BACK。 |
| 2 | 增加单键对照、UP+USE与越界UP+USE+BACK案例，标NOT_EXECUTED。 | PASS。测试目录L713–732的R4-CM01–04/R4-NM01–04明确独立正常循环/查询真值前提，含单USE/BACK、DOWN+USE、UP+USE以及[3,3]初3的UP+USE+BACK越界等待；全部NOT_EXECUTED。 |
| 3 | 保留U05物品数量/商店与光标命名合同，不把其顺序统一化。 | PASS。WP66-C L88–108与B完整字节一致，数量入口各自首动作顺序保留；WP17命名段L191–192及B04-M07–09、U05-QN01–04原测试行未改。只对受影响旧GR3-M10-002的范围作静态复核，不重签历史。 |
| 4 | 如未来声称物理键可达/真实UI通过，须另供宿主证据；本修订不要求先运行。 | PASS。WP17 L107、143与测试L715明确给定trigger/repeat查询为条件推导，未声称物理键可达或真实UI通过。此标准的证据边界符合要求，宿主执行本次为NOT_EXECUTED_THIS_UPDATE。 |
| 5 | 事件数字消费者另用默认取消等于初值的夹具；例如初1同轮UP+USE+BACK确认2，不能把通用取消−1称为该事件默认。 | PASS。WP17 L141与R4-NM04（测试L732）使用事件一位初值1/默认取消1；R Interpreter L325–334真实调用ChooseNumber，Messages L93–112说明默认设定清独立取消值，结果为2写变量/请求刷新；独立BACK返回并写1。 |

独立质疑（全部为未执行的静态条件推导）：

- 普通及帮助入口各自独立：DOWN+USE+BACK，取消−7；另仅把取消改0；再改2。 → 方向先0→1并帮助更新；取消−7返回−7，取消0返回更新后确认1，取消2返回取消编码1。取消2的值相同不意味着同一出口。 质疑统一确认/取消优先及“BACK成立即消费本轮”；候选取消编码+4.1足以区分三支。 证据：R Messages L733–748、775–792；SpriteWindow_text L864–883；C WP17 L97、105。
- 逐位初9，同轮UP+USE+BACK；独立初0，DOWN+USE+BACK；独立初1，UP+BACK且USE假。 → 分别编辑个位回绕到0并确认0、回绕到9并确认9、编辑到2后按BACK返回固定取消−1。 质疑把编辑写成范围夹限/整数整体加减，或把方向先更新误当作必确认。候选5.2与5.4共同正确覆盖；未要求新增超出finding的多方向裁决。 证据：R SpriteWindow_text L624–730；Messages L180–201；C WP17 L122、128、134。

未发现本项必修问题；最小修复与重新验收要求为空。

## GR4-M10-002 — PASS

| 原标准序号 | 原标准 | 结果及依据 |
| --- | --- | --- |
| 1 | 给出选项命中、系统命中、两个通用备用依次命中及全缺的结果。 | PASS。WP15 L34–45给消息/菜单各自四级冷链及首命中停止；无选项对象取配置首项，系统记录缺失/空名进入通用备用；R MessageConfig L35–85一致。R4-SK01–04（测试L742–745）覆盖选项、系统、两备用依次命中和全缺。 |
| 2 | 相同素材条件下，冷读取Missing得到Custom而显式设置Missing后读取为空，标未执行。 | PASS。R4-SK02/05（测试L743、746）在相同可解析Custom/备用前提下，冷Missing选Custom，独立显式完整Missing后保存空且后读不冷回退；WP15 L45及WP17 L88承接。向量均NOT_EXECUTED。 |
| 3 | 空w标签保持原直接清空合同；不把逻辑空值等于所有既有窗口统一无皮肤。 | PASS。WP17 L35、88与R4-SK06（测试L747）保留空w直接清单窗皮肤；WP15 L47将逻辑空/单窗失败/实际呈现分开。R Messages L444–450为空标签直接赋空，Options L499–503/514–518先写选项再设逻辑缓存再交预览；暖实例源基类失败返出后覆盖仍可继续刷新，候选未推统一无皮肤。 |

独立质疑（全部为未执行的静态条件推导）：

- 冷Missing→读；独立显式完整Missing→再读；独立已取到Selected后只改选项索引而不显式设置。 → 冷读Custom；显式设置后读逻辑空；已取得结果后仅改索引不会自行重跑冷链。 质疑缓存空当未初始化、每次读取都从当前选项重求以及通用nil直接结论；WP15 L36–45按状态准确区分。 证据：R MessageConfig L35–85；C WP15 L34–45；测试R4-SK02/05 L743、746。
- 正常暖Speech/Menu预览窗口，改到Missing；独立空w标签；独立直接设置nil或空名称且该原始请求不可解析。 → 预览先写对应选项再显式设逻辑空字符串，读回空交该窗口换肤；空w直接清单窗皮肤；nil/不可解析空名称不启用默认链。暖换肤基类先释放定制资源后失败返出，文本/命令覆盖仍可刷新取色，逻辑空不决定稳定旧图/统一空肤/崩溃。 质疑把两个入口或暖实例与冷链合并；也质疑从基类提前返回推出整个预览无后续。候选L47及SK06的边界成立。空字符串本身仍走图像解析，只有不可解析前提才断言空结果。 证据：R Options L499–503、514–518；SpriteWindow L856–868、877–901；SpriteWindow_text L258–273、1118–1124；Messages L444–450；C WP15 L47、WP17 L35/88、测试L747。

未发现本项必修问题；最小修复与重新验收要求为空。

## 限定回归与读取记录

旧GR3-M10-002只复用原qualified身份；WP66-C完整字节与B相同，B04-M07–09及U05-QN01–04原测试行逐字相同。另静态读共享数量、钱店与BP源循环，确认各入口原顺序未被新条款统一化。不重开或补签旧229/341/全部GR3。

下表是本审者实际读取范围；JSON另有完整blob、bytes、SHA256和指针。准备约束与两项finding完整读取；大体量根输入元数据仅读绑定/执行/所有权相关字段，未重复全域语义审查。

| commit | 路径 | 实际范围 |
| --- | --- | --- |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | `AGENTS.md` | [[1, 297]] |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | `review/remediation-fourth-20261012-prepare/tasks/R4-U03/reviewer.md` | [[1, 19]] |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | `review/remediation-fourth-20261012-prepare/tasks/R4-U03/batch-contract.json` | [[1, 194]] |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | `review/remediation-fourth-20261012-prepare/tasks/R4-U03/read-scope.json` | [[1, 890]] |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | `review/remediation-fourth-20261012-prepare/tasks/R4-U03/findings-input.json` | ["whole targeted records"]；/authority, /canonical_root_records/2, /canonical_root_records/3 |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | `review/remediation-fourth-20261012-prepare/tasks/R4-U03/handoff-findings.md` | [[649, 891], [892, 1129]] |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | `review/remediation-fourth-20261012-prepare/batches/R4-U03/author/acceptance-map.json` | ["whole targeted records"]；/records/2, /records/3 |
| 2b60c7bd0dce8d972e34a9d86a8f6cf6a3b1dd65 | `review/remediation-fourth-20261012-prepare/freeze-and-publication.json` | ["identity fields and whole R4-U03 task entry"]；/task_package_commit, /task_package_tree, /author_start_commit, /formal_input_commit, /reference_commit, /task_packages/2, /model_request_contract |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | `review/remediation-fourth-20261012-prepare/resource-scope.json` | [[1, 96]] |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | `review/remediation-fourth-20261012-prepare/input-verification.json` | ["binding, model, execution, ownership and relevant scope fields; large identity arrays not semantically rereviewed"] |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | `review/remediation-fourth-20261012-prepare/dispatch-plan.json` | ["binding, model, execution, ownership and relevant scope fields; large identity arrays not semantically rereviewed"] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/007_Objects and windows/011_Messages.rb` | [[1, 235], [270, 312], [375, 400], [437, 454], [680, 808]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb` | [[60, 91], [245, 273], [624, 739], [742, 783], [784, 935], [981, 1040], [1040, 1055], [1056, 1099], [1108, 1138], [1163, 1294]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/003_Game processing/004_Interpreter_Commands.rb` | [[300, 345], [665, 682]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/016_UI/019_UI_PC.rb` | [[1, 25], [105, 160]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/007_Objects and windows/002_MessageConfig.rb` | [[1, 100]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/007_Objects and windows/004_SpriteWindow.rb` | [[788, 920]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/016_UI/015_UI_Options.rb` | [[1, 35], [198, 223], [450, 525]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/001_Settings.rb` | [[440, 485]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/001_Technical/004_Input.rb` | [[1, 31]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/001_Technical/002_Files/001_FileTests.rb` | [[112, 145]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/001_Technical/002_RubyUtilities.rb` | [[385, 397]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/016_UI/018_UI_ItemStorage.rb` | [[110, 126], [287, 341]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/016_UI/020_UI_PokeMart.rb` | [[477, 535]] |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | `Data/Scripts/016_UI/021_UI_BattlePointShop.rb` | [[332, 392]] |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` | [[27, 42], [83, 150], [152, 199]] |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | `deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md` | [[29, 65]] |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` | [[547, 549], [675, 678], [711, 787]] |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | `deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md` | [[78, 115]] |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | `deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md` | [[115, 133], [174, 198]] |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | `deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md` | [[23, 27], [45, 68]] |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | `deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md` | [[169, 169]] |
| 1f36475d22120a0d1175967d5b17d71fe8311d88 | `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` | ["full relevant candidate diff base context; existing naming/quantity row comparisons"] |
| 1f36475d22120a0d1175967d5b17d71fe8311d88 | `deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md` | ["full relevant candidate diff base context; existing naming/quantity row comparisons"] |
| 1f36475d22120a0d1175967d5b17d71fe8311d88 | `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` | ["full relevant candidate diff base context; existing naming/quantity row comparisons"] |
| 1f36475d22120a0d1175967d5b17d71fe8311d88 | `review/remediation-third-20261012-prepare/U05/acceptance-checklist.json` | ["whole specified GR3-M10-002 record only"]；/required5/1 |
| 1f36475d22120a0d1175967d5b17d71fe8311d88 | `review/remediation-third-20261012-prepare/registration/U05-formal-acceptance.json` | ["whole specified GR3-M10-002 record only"]；/independent_actual_review/actual_verdicts/GR3-M10-002 |

## 限制

- 仅指定精确候选两项及必要消费者/限定旧范围；不是ACTUAL_PASS、ACCEPTED_SCOPED或CLOSED，未登记任何接受/关闭。
- 本更新新增行为执行0；所有新增反例是给定查询/逻辑资源前提下静态推导，未证明物理输入、UI、宿主、媒体、像素或完整Demo。
- 真实释放后画面/对象失效效果、外部插件行为未知；未来兼容政策未代选。
- 全批完整字节/整批其它finding由父任务聚合；本子审只绑定自身范围及实际读取记录。

剩余阻塞：无。补充独立皮肤核对task为 `/root/input_skin/skin_countercheck`，thread未回显，未猜测。
