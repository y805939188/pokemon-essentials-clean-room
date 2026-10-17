# R8-U05 固定候选独立复审

**结论：候选 PASS，2/2 必修通过；本批未决语义缺口 0。** 本结论只覆盖下列固定候选和两项最低修订。actual integrated PASS、ACCEPTED、CLOSED 均为 PENDING，不能由本次候选 PASS 代替。

## 固定身份与独立性

| 输入 | 完整身份 |
| --- | --- |
| 仓库 | y805939188/pokemon-essentials-clean-room |
| 候选 commit | `1303c92b1468ef0200ca71b75a67a0f9ea4f3e79` |
| 候选 workspace tree | `81e5d0a1d3107434d1856b0f5ed782cc2c8fa144` |
| 作者分支 | `revision/r8-u05-20261017`，读取时指向上述候选 |
| 原输入 commit / tree | `4575e80d041ab0c74a42e2e36399d05791dbaa5b` / `e8fb0884694afee309c57504babf9f849a5f1498` |
| B8 | `fd1df570cad987dc3852a3b958f03916e317f7fe` |
| R8 语义 core | `2460370f1e410bd49cc29e377b89662838aed2b3`，tree `d43c425a3cfed29014f5cdfb94a3f8d947508d5f` |
| 固定参考 R / tree | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 原合同来源 | `5caff3bd1a1b062b48b7eda46777a614921946f3` 原路径，与 C35 恢复位置分别保留 |
| 本次复审分支 | `review/r8-u05-independent-20261017-1303c92`，从固定候选建立，仅增本目录 |

本次为新授权的非作者独立复审，未参与候选编写。主审 /root 负责最终裁决与发布，6 个新建只读辅助 context 分担源、反证和共同载荷核对；辅助结论不是作者自审，也不另计历史业务根或多份正式验收票。实际读取者及范围见 [读账](evidence/read-ledger.json)。用户给定配置为 gpt-6.1-sol / ultra / default；normal、Fast off 来自原 reviewer 合同。没有权威运行 echo，actual model/effort/tier/speed/Fast 逐项 UNVERIFIED，未调用其它模型配置。

选定执行环境在 container_creation 阶段失败（container_service_failed，随后 configuration capabilities 查询失败）。实际使用连接的 GitHub 只读接口恢复固定对象，并以 Git Data API 在独立分支创建提交、非 force 发布和回读；没有本地 git push 命令或 shell 测试的虚构回执。未运行 Ruby、参考程序、游戏、宿主、独立业务数值模型或真实保存回放。哈希/文本比较为 TOOL_VALIDATION，行为场景为 SOURCE_STATIC / DERIVED_VECTOR / NOT_EXECUTED。

## 合同、读集与范围

实际接收 AGENTS.md、报告根 inputs/review-SKILL.md、R8-U05 prompt/readset/reviewer-prompt、manifest 与本批 assignment、contracts.zh.json 的完整 records/22 和 /30、accepted-facts/history/policy/launch 及相关原始根、反审、历史接合。reviewer-prompt 内两份完整合同与 contracts.zh.json 对象逐值完全相等。实际 manifest 为 handoff/cloud-eighth-update-handoff-manifest.json；本批目录没有 manifest.json。

两份候选整文、原基线/B8 两份正文及共享 creature-rpg 测试目录均已读取。固定源的 Settings、Trainer、WildEncounters、Encounter、Compiler001/002/003、Radar 和五份 encounters 文本均由本次实际独立 reader 完整读取；必要 caller、GameData、PIDGEY、移动/Repel 及 reset 来源以完整具名单位读取，未把取回整文件误标成全文语义 FULL。

原完整根使用可直接读取的原 JSON 对象：root-decisions.partial blob `f5a9f5075a6618b90bf6d6e5c53b494792f7609c` 的 /records/22、/30，与当前 root-decisions.partial blob `22778f5401a18c9dabf29504d5c97fa942907a1b` 两对象精确相等。原 gzip 未解压，未声称读过 gzip；恢复其完整原 JSON 语义，并结合当前 findings 两记录、最终 canonical 全对象和共同资格，不以摘要替代。外批 root 载荷按当前独特 qualification/preserve/counter 的 typed purpose 读取，重复精确对象去重，纯身份/调度/传输字段不授外域语义 FULL。

独立工具核验 80/80 继承输入与 45/45 当前 handoff 载荷的固定 commit/path/blob 绑定、完整字节数、SHA256 和 Git blob，18/18 候选文件同样完整取回并核验；这些数量是身份载荷口径，不是新语义 atom 或测试数。独立实现的摘要器经标准 abc/空 blob 校验，并与 GitHub 返回 blob 一致；方法和实测结果见 evidence 伴件。未运行作者 verify.py，它会写作者证据，故只读检查其声明与保留的输出。

## GR8-WORLD-004 — PASS

修改仅为候选 WP61 §3.3 第三项，第 **56** 行；完整镜像 39,292B，SHA256 `74e62547ee478852b67e10191e0989f39d833aa03e28b6d043543484133999d0`，blob `c3f63733f58415fc828b89f9d36657138f4e02dc`，mode 100644。

固定源证据：Settings L17/L359–364 确定世代8及默认 true；Trainer L57–63、L94–100 区分首非蛋与首可战；WildEncounters L186–207 确定 nil → 雷达 → Repel → 后置能力的顺序、严格低于及拒绝清累积。Overworld 的完整 pbBattleOnStepTaken L196–221 只以前置可战计数0拒绝，后备健康10级使混合队伍反例正常可达。

前提：固定 R/B8、合法普通非蛋记录，无插件/并发改队；P0 50级、P1 健康10级，repel=true、雷达=false，无威吓/锐利目光，初始累积 A。六控制均为静态推导，未执行：

| 控制 | 返回与累积 |
| --- | --- |
| P0健康50、野生20、默认 true | false，累积0 |
| P0濒死50、P1健康10、野生20、默认 true | false，累积0 |
| 同混合队伍，配置 false | 选P1；Repel放行，排除后置能力后 true，累积A |
| 混合队伍，野生50，默认 true | 相等不拒绝，true，累积A |
| 有效候选，雷达摇草 true | 在Repel之前 true，累积A |
| 候选 nil，即使雷达 true | 最先 false，累积A |

最强反方：“WP36 已正确，括注可按口语理解，因此只需可选澄清。”WP61 同篇第62行已明确可战排除濒死，旧限定在合法混合队伍下给出相反结果，反方不足以保留错误括注。当前替换准确指向 WP36 §4.3，保留一个主合同，没有复制整套算法。

累计保留：WP36 §4.3 两配置/严格低于/雷达与能力顺序；WP61 第54–55行的100/200/250、冰面不递减、到0消息与续用；Overworld L180–185 在玩家消费者之前捕获 Repel 活动快照。Game_Player L141–186 和 WildEncounters L453–469 验证 GR-011 同次移动消费、独立转向清标记、主动请求包装不写标记；EN-06/07/08 原字节保留。谓词无本地取消；已达清0前缀不承诺异常回滚，允许门通过不承诺实际开战。

## GR8-EXT-CD-002 — PASS

修改仅为候选 WP36 §4.2 第5项，第 **132** 行；完整镜像 31,426B，SHA256 `81cd035b54a5e6466e9810639d4ef7d7e0c7a68132072370588fa36ecfe2c13c`，blob `1d7ec3e7afca3e74adbcff9c68a17380fabecf68`，mode 100644。合同旧导航131不是实际候选行号。

输入域证据：Compiler002 完整遭遇编译 L658–765，特别是 L731–737 的步骤字段整数前缀与缺省逻辑，区别于 L673–688 的槽权重/等级正整数校验；Encounter L62–68 与 GameData 完整登记单位 L78–115 没有追加概率非负验证。Compiler001 的预处理/普通重编译没有为该字段加正数门；Compiler003 L403–442 写回省略非正值是输出规则，不是输入校验，普通编译不先写回。

固定语言文档仅作语义佐证：整数负值除法支持向下取整数商，字符串采用整数前缀，nil/false 以外为真值；据此静态推导 -1 不被缺省替换，⌊-1/200⌋=-1。参见官方 [Integer](https://docs.ruby-lang.org/en/3.1/Integer.html#method-i-2F)、[String](https://docs.ruby-lang.org/en/3.1/String.html#method-i-to_i)、[控制表达式](https://docs.ruby-lang.org/en/3.1/syntax/control_expressions_rdoc.html)。未执行 Ruby 验证。

正常可达前提：合法作者地图5/version0、Land,-1、100/PIDGEY/5/5槽，其余编译依赖合法且登记/装载成功仅为前提；健康普通非蛋 PIDGEY/TANGLEDFEET，无持物/地图/能力修正、自行车或雷达，repel=false、位置类型和回调正常。固定 PBS/pokemon.txt L391–417 证明物种/能力有效，Overworld L196–221 的正常 caller 可通过。

WildEncounters L116–117、L170–173：从 setup 步0/累积0，基础-1给最小步8及宽限阈值5；八次宽限抽样99均先增步后拒绝、不累加，得到步8/累积0。随后常规抽样0对概率-1失败，累积-1；下一次 L120 的向下商为-1，概率-2，再抽0失败，累积-2。修订准确加上非负基础概率及非负当前累加器的前提，并保留负前缀原算法、不钳零。

| 对照 | 静态预期 |
| --- | --- |
| 独立正21、已过宽限步8/累积0、常规99 | 失败得累积21；下次商0、概率21 |
| 基础21、累积21/189/210 | 概率21/21/22，EN-13保留 |
| 同负值常规失败，Repel真 | 先累加再清0 |
| 非步进 | 不加整数商，不推进宽限，不累加 |
| 宽限放大掷拒绝 | 先增步，不累加 |
| setup / reset / trigger真 | setup只重置步数与快照并保累积；reset清两计数；trigger真自身不重置 |
| 缺步骤值/0/空表与雷达 | 前置门先拒绝，合格后才雷达直通 |

正21对照是独立条件状态，**没有把负值的八次宽限前缀套给正21**；正21无修正最小步5.9，六次宽限拒绝即可越过该门。作者 remediation-records 已明确此区别。

最强反方是真实的默认五份文本无负概率、通用 schema 存在正数校验、写回器只输出正步骤值。五文本各有33个显式值（集合2/5/10/20/21/40/50）与19个省略项；它们没有把普通作者输入域缩为非负。上述独立输入/输出链消解该反方，不宣称默认附带地图已故障。

累计保留：WP36 §3.2 原接受域，EN-01–32全部原ID/计数/字节，21/189/210、宽限和常规失败、Repel清零、雷达前门、当前地图快照、版本同值早退与异值装载。PC-F033 完整纠正及四个具名 reset caller 已接收，不能把成功触发写成自动重置。编译错误可阻止后续装载，前一节可能先登记；无本地交互取消，也不添统一回滚。

## 范围、历史与保护检查

独立基线→候选 compare 为 ahead3、behind0、merge-base=原基线，恰18新增文件，全部处于 R8-U05 候选目录（2 mirror、16 evidence）。两份镜像各一个句段替换，其余UTF-8字节相同；288/203行、章节标题和锚点保持；正式规格和公共目录未改。

根目录16项中除review外15项 mode/type/SHA完全相同，包括 deliverables `48820664637b119bd6d7e45770531f0a31912bbd`、audit `a24c0ed74cbc029889bf750105a60afe8c6559a8`、planning `399dbfed0dd52e9f974745794f0126e6825c27b9`、specs `5ccca56ff74088076bdf2aaa59da1898302e5dde`。原review树 `ef5eca48b349d51d2a83944b1fddcdc33a71d047` 的149既有直属项在候选review树 `e39e545d8bdfff47c5ee178a59378e5f6508013c` 全部逐项保留，唯一新增整改目录的递归树未截断、恰18个100644文件。旧报告、旧接受/关闭回执及其它批均受此保护证据覆盖。

当前最终历史 canonical 保留：WORLD004 区别于 GR-011 标记消费；CD002 区别于 GR7-M08-001 活动快照/常规失败清零与 UTIL-03 旧ASCII末LF谓词。原OPEN只在原时点保留，不冒作当前历史阻塞；不重计根或既有7+1执行过程。CREB rawfalse/mail/pinch等facet未被本批采用，不触发外域12源单位采用义务；Encounter计数纠正适用并已核。独立视觉policy未选不阻本批。

本批没有归属optional，选中数0。独立核 batch-assignment 的10项归属与作者 optional-disposition 全相符：U01一项、U06三项、U07一项、U09五项；本批既不选择也不拒绝外批项。tagging-handoff 的两个章节/锚点/行号/行为变化与实际替换完全相符，没有全面重打标或额外公共写入要求。

作者 independent-review.md 是输入入口，不是独立结论；validation/remediation 的 PENDING 状态诚实。作者第一次 stdout 被后次覆盖的情况已在1303完整记录，未冒称不可变首份日志；最后stdout与validation同blob、stderr为空。publication-readback 只证明931b2e50e3ba4fa7bf6ab924ef239d397365a7b9的17文件传输，并明确由后继封存，不冒称证明最终1303。以上作者材料只作可检查声明，本次裁决另有固定源、场景、精确差异与独立身份核验。

## 未决与交接

本批候选返修要求：无。执行环境故障已用固定 GitHub 对象读写路径绕过，不构成本有限静态候选复审的剩余阻塞。没有运行等价、宿主、媒体、保存或完整外域认证。

后续仍须 R8-INTEGRATOR 在唯一正式写集整合，冻结真实整合commit/tree，再由实际非作者完整复核受影响整文件及累计保留；随后分别登记 actual integrated PASS、ACCEPTED、CLOSED。通知修订者与协调任务 `01a14a04-b178-7567-a4eb-0f0bfac9a0d9` 由父任务负责，本次未另发消息。

报告自身最终commit不填未来hash；实际发布与回读凭据见 evidence/publication-readback.json（若为后继凭据提交，其证明范围明确指向前一真实提交），最终完整SHA由真实回读及交付消息绑定。
