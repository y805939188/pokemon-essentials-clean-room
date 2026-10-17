# Creature R3 独立复核：仅当前源校准 facet FAIL

固定候选为 `c0f62d973180679134f2eb1a488c1dc359c8658f`，当前正式源从固定 Git 对象 `5f87743293290de2e219ecdd6c19e88280f60c9a` 读取，正式子树独立核为 `93dc967b4cdb653359afc123d3b8b318d6475fdd`。工作区 B8 正文未被当作 current。

**122 active：119 PASS / 3 FAIL；116 原 ID：113 PASS / 3 FAIL。** FR173 / FR227 的当前源差分注记错配归入 root 合并 P3 `R3-SOURCE-ATTRIBUTION-001`（local alias `R3-CRE-CAL-001`）；FR204 把单项 EV 越额称作总量越额，归入 root 合并 P3 `R3-EV-BOUNDARY-001`（local alias `R3-CRE-CAL-002`）。local alias 不另增问题计数。三个失败只限当前源校准 facet；全部 122 行分类、职责、有效范围和依赖 facet PASS。R2 两项 creature 问题、R1 本域残留及原七组具体 case 均 PASS；没有把正确修复重新算为依赖 FAIL。

完整逐行、逐组、逐边和读取身份见 [creature-results.json](creature-results.json)，固定输入、完整六文件差异及静态 Git 回执见 [creature-evidence.json](creature-evidence.json)。本分工没有执行作者校验或业务工具；全局回执/工具接收门由 root 的独立核验另行给出。

## 新增问题 R3-CRE-CAL-001 · P3

问题是作者把实际当前源差分注释成另一项行为，类别相同不能使这种校准陈述通过。当前 locator / file identity 是正确的；不需要新增功能 ID，也不要求改正式源或设计目标实现。

| 行及候选 JSON 指针 | final5f 实际有效源 | 错配及可区分反例 |
| --- | --- | --- |
| FR-000173，`/features/161/differences/1` | WP26 §5 L122–142，其中变化为 L138：录像**记录**战斗的收服存储为空操作；回放另按 WP58 §6.2–6.4 的副本、实时依赖和正常结束/中止合同 | 注记却称神秘礼物 ESC 返回原非空名/空文停止。真实回放的玩家侧消耗品指令可以消费实时背包，正常终局也可触发普通收尾；不能用记录战斗存储空操作推导回放隔离。Gift 命名注记没有校准这一差异。 |
| FR-000227，`/features/215/differences/1` | WP36 §4 L115–161，其中变化为 §4.2 L132：接受的负概率前缀可有负累加器，整数商向下取整且不钳零 | 注记却称 Repel 默认首非蛋（含濒死）/替代首可战成员；该规则在 B8 / 908 L143 已存在。负前缀下累加器 −1 的整数商为 floor(−1/200)=−1，不能截成 0；Repel 成员选择不能证明这项运算。 |

同一错配还存在于 `revisions/r3/feature-source-deltas.json` 的 records 13 / 15，以及 `source-file-reassessment.json` 的 records 7 / 9（source fact 与 future reassessment）；统一 `source-refinement-patch.json` 的 records 18 / 20 复制了对应 after 字段。全部精确指针、固定源身份、反例与最小修复在结果 `new_findings[0]` 中。

最小修复是把 173 的当前差分注记改为记录/回放交界，把 227 改为负概率/负累加器的整除与不钳零，并同步重建补丁和派生证据。244 的真实 Gift 命名注记及既有 Repel 规则保留。这里不把源接受回执否定，也不把分类、职责和范围一并扣为 FAIL。

## R3-EV-BOUNDARY-001 的 creature case：FR204

`/features/192/differences/1`、`feature-source-deltas.json /records/14/source_fact_delta`、`source-file-reassessment.json /records/8/source_fact_reassessment` 都把模板说成“超 EV 总量”。实际 final5f WP19 §5.3 L174/178 的正常模板是 HP255、攻击255、其它0，**总量恰为510**；单项 HP 超过252，先在 [0,−3] 的单项区间失败，尚未到总量夹限。WP30 §4 L122 的实际当前新增条款正是这项单项越额对照。

可区分对照为同一模板 HP 产出1与0：两者都先在 HP 单项夹限失败，不能以总量已经510、此次产出0来避免该失败。已有255存量不自动修复，此接收者 EV/经验未写；此前其它接收者和回调前缀不保证回滚。最小修复是将注记改为单项越额/负单项余量首失败，保留总量510及其它边界，并同步补丁 records19。分类/职责/依赖和成长协作候选保持 PASS；此 case 不与 root 的 combat29/32、world456重复计算。

## R2 依赖问题与完整边集

原本域 17 行共有 57 条 feature 出站边，本轮完整核对其历史处置；当前为 55 条：四条错误目标替换、两条 Gift/PBS 错族边删除，其余 51 条真实用途保留。55 条当前边均逐条有源/目标有效范围、身份、用途及限定判断，见 `dependency_edge_results`；57 条旧边的当前状态见 `original_dependency_edge_results`。不是抽样，也不是整行字节相等后直接转授 PASS。

| 具体 case | R3 裁定及依据 |
| --- | --- |
| 186 / 190 → 31 | PASS。WP28 登记预扣与复检退款留下物品身份，WP42 §6 L177、§6.0 L183–191 在正常共同终局按残留身份退款后清选择。外层 §7 / 32 的伙伴治疗已去掉，不冒充主动药品或退款。 |
| 192 → 39 | PASS。WP28 L282 的 GUARDSPEC 读写 Mist、同种正值拒绝、成功设五回合；WP45 §6.2 L127 真实承担建立与侧期限。§7 / 40 的交换/清理不能替代建立，已移除。 |
| 244 删除 263 / 265 | PASS。GiftMaster、当前会话、Export、人工线上是独立四层；WP73-A 六类 PBS 编辑器不是 Gift 编辑器实际调用。241 载体和 243 管理 Receive 的领取调用保留。 |
| 741 → 420 | PASS。WP24 §4.4 按实际余额差累计，battle_money_gained/lost 在 WP06 stats §6 L82–83 / 420；421 的 §7 只有商店、币、BP、煤灰等字段。 |
| 742 → 263 / 265 | PASS 保留。缺失训练家交互新建实际共享训练家类型/训练家建队、嵌套保存与取消前缀；区别于 Gift 错族。 |
| 741 → 579 → 755 | PASS 保留。579 明确排除子行 755，而 755 精确拥有 WP50 L167 的奖金持物输入。允许这条显式间接导航，不要求重复最小 ID。 |

R1 原七个依赖 case（155/157/158/186/190/191/192）全部逐项保留或复核，R2 同根扩展 244/741 均修正。147→739 的 PP 子导航、739 的 29/191/204/207 学习/同步、740 的终局/物品生产/捕获边界、723 的逐槽显示与跨槽数量对照全部保留真实用途。incoming 错引用不反授目标功能 FAIL。

七个当前变化的目标有效范围 1 / 2 / 29 / 32 / 204 / 330 / 596 已重新读当前完整有效单元；新替代目标 39 / 420 与正常终局 31 另按实际用途新读。其余目标沿固定 R2 有身份的完整语义阅读信用，并逐边核当前有效单元身份、原用途与非影响边界。未把整个文件相等当作真实依赖证明。

## 累计变化、目录和新标题消费者

本域 18 篇 primary = 15 正文 + 3 catalog，分配仍为 116 原 ID / 122 active / 0 retired / 0 metadata-record。158 条 section-metadata 逐条与历史和当前导航核对，全部 PASS；没有把它们混进全局 33 metadata 分母。

完整读本域六文件累计差异，并新读五个变更功能单元的完整 final5f 正文及必要消费者：

| 变化 | 源与去向校准 |
| --- | --- |
| WP18 / 137 | 15 个精确蛋群作者身份、未知拒绝、基础默认/形态克隆分别由 WP03 和物种合同承担；框架内容输入职责合理。 |
| WP26 / 173 | 记录战斗存储与回放分层仍可由现有消费者索引承载，分类/职责/范围 PASS；当前差分注记 FAIL 如上。 |
| WP30 / 204 | 实际源的普通非 Shadow EV 单项负余量首失败与 WP19 / WP42 一致；接收者尚未写 EV/经验和此前已有前缀分开，非内部设施早门保留。成长协作候选合理；“超总量”注记的校准 FAIL 如上。 |
| WP36 / 227 | 负概率前缀/累加器运算在既有框架触发规则范围；当前差分注记 FAIL 如上。 |
| WP64 / 244 | 非空原名 ESC 可成功、空文停止才 nil；先改共享个体获得地不因后来停止而恢复。既有框架载体/状态与 MZ 输入职责足够。 |
| Creature 9c catalog MG32 | RETURN 删空并确认停止、已有非空名 ESC 成功、Receive 后未改短语即取消三对照与 WP64 一致；244 是真实消费者。 |

没有 creature primary 所拥有的新标题。另完整核对三个跨域新标题中的 creature 消费者：WP03 §6.2 → 137/214，两个 EV 静态目录新节 → 204；源身份、标题-only hash、raw Markdown heading hash、有效单元及消费者均核对。它们在结果中标为 supplementary，不与 kernel/combat/Pokémon 的标题归属重复计数。静态目录不是实现功能，也不是已运行的测试。

## 继承、根结果对账与限制

固定 R2 报告为 `0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add`。完整 prose 读取 R2 REPORT 与 creature report；mandatory findings、feature、finding、issue、reading、section 数组和本域全部结构结果完整解析。物理文件逐项等于固定 Git 输入。本域 116 old / 122 active / 7 group / 1 residual issue 的逐字段投影与根结果一致；两项 R2 finding 的完整 cases 同根 findings 相等。解析全局数组不冒称重做其它领域语义审查。

所有 122 行的不可变 source、future plan 和 functional scope 逐字段等于 R2，当前 locator/unit/file 身份从 final5f 独立核。继承仅对固定旧全文信用中未改变、未受当前源或消费者变化影响的 facet 有效。六个变化文件按未变段继承，变化有效单元和必要目标 fresh；本轮没有声称重新全文读完 18 篇。读取 ledger 逐篇保存历史/当前身份、实际 fresh 区间和先前信用路径。

原七组具体 case 和当前组 scope 均 PASS，新 173/204/227 的校准问题单列，未凭无关新问题重开旧 case。持久 PP / 持物 / 捕获 / 主动战斗道具 / 战中成长继续保持协作验证边界。框架、Showdown、MZ 的粗标不代表目标版本兼容、原型完成或用户批准首版范围。

请求配置为 gpt-6.1-sol / ultra / default / normal / Fast off；实际 model、effort、tier、speed、Fast 和 cloud UUID 缺权威 echo，逐字段 UNVERIFIED。它们是资格限制，不编造成执行失败。本分工只是单份独立审查的一部分，不增算接受票。

只执行静态 Markdown / JSON / Git / Python 审查；Ruby、游戏、业务场景、宿主、Showdown/框架原型运行均为 0。未修改作者候选、正式规格、参考、main 或旧 review，未提交。只读探索曾发生一次区间拼接 TypeError 与一次 WP58 路径未命中，修正后完成；截断的混合输出另按明确区间补读，不授未读信用。源接受门与全局工具结论由 root 另核，目标去向仍待验证、阶段未批准、实现/目标验收未完成。

首次输出格式探针误把 `git diff --no-index --check` 的“有文件差异”退出码1当作空白错误；该次 stdout/stderr 均空，尚未写验证结果。后继按退出码0/1与实际诊断输出分别判断，全部报告/JSON/Python格式检查通过，真实过程保存在 `creature-validation.json`。
