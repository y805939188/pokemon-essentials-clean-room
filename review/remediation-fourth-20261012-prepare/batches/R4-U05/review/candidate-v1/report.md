# R4-U05 候选独立复审

裁决：**GR4-M12-001 PASS；限定 CANDIDATE_PASS**。四项合同验收均满足，未发现需要修订的问题。本结论仅绑定下述真实候选，不是实际整合 PASS、ACCEPTED_SCOPED 或 CLOSED。

| 输入 | 精确身份 |
| --- | --- |
| 真实候选 C | `2332c5523b6e98ae5c2e7be3ada78c6f6d4eaf9b` / tree `ffd02b689d1bde6018e1de22fa1483c0997ffdf3` |
| 作者证据后继 A | `db5a0b91c544c67cd72521a0a236a1386cf8242a` / tree `386d14eba496e72e7ee62b2aea73ae6d207af637` |
| 固定任务包 S | `08a57fb55118914a74ac1ffaf617647c01df8938` / tree `8fc388710e3433890416f6d01247fd09df9d2ea8` |
| 正式基线 B | `1f36475d22120a0d1175967d5b17d71fe8311d88` / tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a` |
| 参考 R | `Maruno17/pokemon-essentials`，`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0` |

复审者是本次新任务 `/root`，独立于作者 thread `01a130c4-6a34-7221-b8d4-20e3e887600e`；只读辅助任务 `/root/evidence_audit` 独立复算字节、范围及历史绑定。当前 reviewer thread ID 未回显，记 **UNVERIFIED**；来源 thread `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2` 只作来源身份，不冒作 reviewer thread。请求 `gpt-6.1-sol / ultra / service_tier=default / Fast=false`，实际模型、effort、tier 与 Fast 回显均 **UNVERIFIED**，没有后端/额度审计。工作树 `/workspace/r4-u05-review`，分支 `review/r4-u05-independent-20261012` 从精确 A 创建；本 reviewer 只新增本目录材料。

## 验收结果

| 项目 | 裁决 | 独立依据及候选位置 |
| --- | --- | --- |
| AC1：整集空 Land21，源不变、目标无类型但率保留；后缀和未保存层次 | PASS | WP73-B §6.1/§6.2/§11 与 WE-M11-E01 a/c 明确源 `(5,0)`、目标未占用 `(7,1)`、Land 零槽、率21、后缀s、无插件/外改；登记与档案/PBS分开；No 成功重载且原档案无目标时副本消失。 |
| AC2：非空独立复制及单类型空 Land→Cave 反向对照 | PASS | WE-M11 限定合法非空槽，保留 Land/21/s、目标槽修改不改源、冲突拒绝；WP73-B §6.2 与 E01 b 明确 Cave 已注册且本集未用，复制后 Cave(x0)/21 存在，新增集合排除 Cave，源 Land 不变。 |
| AC3：PBS 省空类型与 Copy 分开，不扩成运行遇敌差异 | PASS | WP73-B §6.4 及 E01 说明将登记过滤和后续 PBS 写出明确分为两步；§6.5 未改，E01 明确快照不重装，不推定实际遇敌变化。WP04/WP36相邻合同无冲突。 |
| AC4：本修订无宿主运行要求，执行须独立记录 | PASS | 正文原静态范围、WE-M11/E01 的 NOT_EXECUTED 与作者证据一致。本审查没有参考、模型或宿主/Demo行为执行；此 PASS 判断的是证据分级与验收边界，不能读作 runtime PASS。 |

逐项详细条件、对照、路径与限制另见 [criteria-results.json](criteria-results.json)。无 REQUIRES_CHANGES 项，无最小修复请求；不以措辞偏好制造返工。

## 源行为与独立质疑

实际读取固定 R 的 `Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb` 1–340，及合同六份完整文件身份；另读取消返回、淡入淡出包装、遭遇快照装载及版本写入。源追溯和完整 bytes/SHA256/blob 见 [identity.json](identity.json)，逐读取结论见 [read-ledger.json](read-ledger.json)。源仅用于读源分析，没有 checkout、执行、修改或转译。

独立质疑一：零槽是否只是非法人工结构，正常进入/返回是否会清理？新增类型在进入槽编辑前即建立空条目并设默认率，BACK 返回负取消值；槽编辑返回不清除条目。父列表按类型条目列出零槽，故 Land(x0)/21 是正常可达状态。Land 默认21、Cave 默认5均已读数据定义。

独立质疑二：登记或菜单包装是否补回被过滤类型，残留率是否排除再次新增？整集 Copy 逐项复制全部率，独立遍历类型时跳过零槽，随后直接登记；构造/登记没有按概率键补回类型。菜单只经淡入淡出进入编辑器；固定 Scripts 的定义/caller 检索没有另一覆盖。类型列表及新增/单类型 Copy 的未用集合按类型条目判断。目标没有 Land 条目时，即使率仍21，也可以再次新增 Land。

独立质疑三：是否混同两种 Copy，或破坏非空条目？单类型 Copy 在复制槽之前就建立目标空类型，源零槽仍得到 Cave(x0)，率复制为21而不取 Cave 默认5。整集含非空 Land 时建立目标类型并逐槽复制；合法槽中的值是权重、物种身份、等级，独立目标槽编辑不改源。混合边界静态推导：Land 零槽/21 与 Cave 非空/5 同在源集时，目标保留两项率，仅保留 Cave 类型及独立槽，源两项都不改。候选“全部率、只为含槽类型建立条目”的一般规则支持该结果；不要求作者再增加重复向量。

独立质疑四：No 后是否必然回到刚进入的内存状态，PBS 是否能解释 Copy 后列表？No 实际从原档案重载，故 E01 c 必须有“原档案含具名源状态、不含目标、重载成功”的前提；候选已具名，不把内存前态当档案。PBS 写出另遍历非空类型，不在 Copy 时发生，无法解释未保存目标的编辑列表。编辑/登记/保存/重载路径与默认菜单包装均不调用遭遇快照装载，现有 WP36 快照合同保持。

以上都是 SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR（未执行）；没有伪装成真实窗口或游戏观察。

## 作者声明和有限回归

C 的父提交为 S，A 的父提交为 C；A 仅补作者发布/远端读回两份回执，两个正式文件在 C/A 字节相同。S→C 全10 changed paths 与作者回执相符，均为两个批准正文及本批 author 证据；B→C 仅两个正式文件改变。完整正式文件身份与作者声明一致：

| 文件 | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| `demo-dx/wp73-b-world-editors.md` | 41130 | `b82fbb32bd1ca9119d39a606ffe690fa670ba10ec86208f39f94f41b4552dc47` | `25514e1add5aadf480ac2506914e3859b1dd5936` |
| `test-catalog/demo-dx-wp72-73-74-75-76-77.md` | 106211 | `8bf390bd2a34540e73a35d57021eafaab6300afa1240f3bbb1fd3ae8b0a3ec0c` | `5cce7151364a06ef9ea44fabca3c40cdeaabd570` |

独立复算完整正式 diff 为14193 bytes，SHA256 `f67bce94011caeb1461d7677b109840dbc81065671e1b919bb32eb90775b8cea`，`git diff --check` 通过。其余129正式文件未改；WP73-B §1–5、§6.3、§6.5–10、§12+完整字节等 B；测试目录扣除 WE-M11 改行与新增 E01 整块后，其余完整字节等 B，包含 WE-M10/12/13/14、CV-M28/30、GN-M14–20。工具验真细节见 [validation.json](validation.json)。未执行作者 `verify-batch.py`，独立使用 Git/Python只读字节、JSON和范围检查。

只核本 finding 的全文词组反证，候选131正式 Markdown 全集检索命中28行；手工阅读 WP73-B §6/§10–12、WE-M10–14/E01、WP04 §5.5、WP36 §3.1–3.3/§9、WP73-A 共享选择器/生效/归属、WP72 §8.3。其它空类型命中属于音乐、训练家、战斗类型或卡牌，不提供遭遇 Copy 补回条目合同。未重做全局语义 review。完整命中见 [negative-search.json](negative-search.json)。

旧 GR3-M12-001 是 BMP/地图页面材料、GR3-M12-002 是评级结算累计，与本 finding 不同根因。共享目录旧 CV/GN 字节、WP75/WP76正文与旧报告没有被改写；沿用原固定接受 tuple/CLOSED 与 qualified 证据，未重跑或重签历史。R4-U05 的 selected_original229/selected_exact341 均为空；其它229/341仅原 qualified 身份复用。本批未改 WP35/EG-13/20、WP34 §7、正式/公共台账、CURRENT-DELIVERY、交付导航或旧接受材料。

固定第四 review `130452d902530140331c21064a3188b7887f72ae` 的执行目录确有 **4 条**历史 EXECUTED_REFERENCE：M01×1、M02×2、M12评级结算×1，均隔离原函数，非完整宿主。M12评级未调用遭遇编辑器，不能为此 finding 提供运行通过。历史4条保持原限定、不重新认证；本次新增行为执行为 **NOT_EXECUTED_THIS_UPDATE，0次**。Git/哈希/JSON/差异检查只计 TOOL_VALIDATION。

## 范围与后续门

当前完整编辑器宿主、真实UI/媒体/物理输入、完整Demo、外部插件均未执行或未建立，未来兼容政策未代选；这些不阻塞合同所要求的静态事实修订。无本批必修问题及技术阻塞。

报告仅覆盖真实候选 C 的 GR4-M12-001 与列明消费者/保护回归。唯一登记员仍须按合同整合并给出 actual commit/tree，届时才能做独立实际整合检查。候选 PASS 不自动转为 ACTUAL_PASS，不登记接受/关闭。报告提交及发布回执采用后继绑定，最终提交身份在最终响应中给出；普通 push 后从新空对象库 fresh fetch 并完整读回本报告域所有文件。没有写 main、标签、作者正文、参考或用户数据，也没有删除分支。
