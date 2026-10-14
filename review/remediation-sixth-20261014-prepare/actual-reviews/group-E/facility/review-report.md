# group-E facility：F001/F002 实际整合非作者复审

**GR6-F-001：INTEGRATED_CONTENT_PASS。GR6-F-002：INTEGRATED_CONTENT_PASS。** 这是冻结实际整合载荷的有限静态内容结论。两项没有剩余必要正文修订；原 WP66-A 接收条件已实际落实并完成本次联合全文复验。有效模型配置仍 **UNVERIFIED**，公共台账同步仍按整合输入 **DEFERRED / 未应用**；本辅助没有签发配置合格的 INTEGRATED_PASS、正式接受或 CLOSED。

本次继续原独立非作者 `/root/facility`，未参与候选或正式内容编写。冻结实际 commit `86bbc99b28d93db4ed9d6897daf5f3725ccd1808`，workspace tree `67e8c55d520fa8cad2928cb4b95e24c3ed602d5a`，formal tree `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。只在 `actual-reviews/group-E/facility/` 写报告、自己编写的文档/身份核验及读取账本；未切分支、提交、改正式文件或旧报告，未执行作者脚本、参考定义或回调。

## 准确身份、全文阅读与既有证据复用

下列均为本次新读的实际正式全文，语义审查没有以 hash 或旧候选 PASS 代替。

| 实际正式载荷 | 新读完整物理范围 | bytes | SHA256 | Git blob |
| --- | --- | ---: | --- | --- |
| combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md | 1–156 | 27791 | ce75fa71462b015963efb374f35325a8572698d86ab8d7595362a10675ca9148 | 5e424c11be607c4da3ecf6bcc2b5684706655cd3 |
| combat-requirements/wp55-facility-session-and-restoration.md | 1–150 | 23528 | 7d44312c84538220f024fdb32b9f840e0fd1b5d5c5ae961067fe61e9fe2e078c | 41050e9487f2b342d588ed0ba60860268d3436d5 |
| test-catalog/combat-requirements-wp54-55-56-58.md | 1–177 | 33561 | e6336cc59798b5f02dfe92c0e799344a3aa652627b2adfacbe6861562537f1c8 | cc28e3400d3bab787ce66c18156c45bcba6e5829 |
| user-interface/wp66-a-party-and-summary-ui.md | 1–150，151–267 | 45706 | 2a5ed9d7b30ae7f309381d96ef01d33b21324793e1761d8ef7cea8a90a4dac49 | 00acb05350a3cbd4fce1cc0ecf74cb3c845ae07f |

适用 AGENTS 1–297 新全文读。当前 `contracts/R6-U13.json` 为 **370944 UTF-8 bytes**、SHA256 `f202a22b1faf72a80edd2d663b9326bf4a9b9be4409fe88780835de909b08473`、blob `8c05e33d56064ff5a79ea25545f696b6156f4543`；469a 准备、00b45 旧候选、9971 修后候选、86bbc actual 四者原字节相等。曾将字符数 354597 作为字节数的上游说明已纠正，不存在合同格式/字节差量。本辅助仍完整新读当前 F001/F002 对应记录的全部七组、`original_full_proposal` 及追加范围纠正；[独立投影与身份核验](actual-identity-and-regression-checks.json)保留准确 `/scope_contracts/<index>` 与源身份。F001 首次合并输出被截断，200–350 补读覆盖缺段，不能单凭首次 `full_payload_emitted` 字段声称模型完整看见。

`integration/U01-U14-final-composite-20261014/actual-review-input.json`：152860 bytes，SHA256 `4671c1c31f18858a7719e88533029d746c62dfb77d4239cbb0cae633e79863da`，blob `ccf79b03165573f27070a417a2e3d986907f6623`。本次完整语义读其与本域有关的四个 files、U10/U13 批次、全部 resolution/receiver_delta/root_edits/review_requirements、共同状态与 admin 条件，投影为 [actual-input-relevant.json](actual-input-relevant.json)，范围 1–245、246–453；源投影规则及身份见账本。没有对其余 49 个实际文件作本辅助的语义签名。

旧 root FAIL 的发布 commit 为 `3ef4854ef43eac92fd1dc57350e4cf6aa160082b`、tree `365067fae180bed745a67fb6bb538b1429dc76ed`；完整 root 报告新读 1–67，15216 bytes、SHA256 `60a922db1c570c99bca9fe9c9a520881e1ff94487c9fc05a012517da4b9d6dea`、blob `1b64bdb75f8c4c8be5d4c25094acbd0ec0c0133f`。旧 FAIL 属 S001 两正确控制删失及证据说明问题，F001/F002 当时内容 PASS 且 F002 实际消费者同步未完成。修后 PASS 发布 `411b563309a4e642e628dcf8289e36c6fe3fd37f`、tree `c34fc75d13828a49322203455073d475431395bc`；完整 repair-01 报告新读 1–74，11273 bytes、SHA256 `1445036698ffb92561fd87c121310ee65dac157f038b7ab098e5ccb21710970a`、blob `04df5bf6c83056ed44697f379a306ed5f3476d32`，绑定修后候选 `9971fe84896786645cdcda3ab45e5caf7785cabc`。旧 FAIL 不被回写；修后候选 PASS 不提前替代 actual 验收。

本人旧完整七组报告及读取账本从 3ef 精确回读、身份复核后有限复用：固定源 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；七个关联反证完整载荷、共同证据恢复、通用 prompt 与负责原提案已在同一原审查完整语义阅读。本次对其中固定源、反证和精确历史的 26 条读取记录逐项重核 bytes/SHA/blob；[核验文件](actual-identity-and-regression-checks.json)明确标为 `PREVIOUS_SEMANTIC_READ_EXACT_IDENTITY_RECHECK_NOT_FRESH_SEMANTIC_READ`，不把身份重核算成新全文阅读。当前新增 source join 静读 Rulesets 1–239、UI_Party 完整多选单元 1051–1139、Challenge_Data 1–50、Challenge_BattleChallenge 1–363、SaveValues 65–86；固定源剩余上下文和保存消费链按旧准确读集复用。没有检出或执行参考源。

## GR6-F-001：七组实际裁定

1. **身份与裁决。** required/P3、无别名，唯一主批 R6-U13。实际修订仍限取消清理范围和有效开始→取消→结束组合；既有 W30 空原队伍边界没有重复新增为另一根因，也没有把原提案扩大为全生命周期错误。

2. **双向证据。** 实际 WP55:55/57、WS-W13:79/W36:102，回链固定 Challenge_BattleChallenge:79–93（外层结束先回收）、124–126（取消只委派内层）、270–304（取消/内层结束/完整 reset）、345–362（六计数）。原取消只清列明内层字段，保留外层当前身份、规则/配置、六计数及内层轮次上限。进行中守卫位于原队伍无条件赋值之后。保存传递消费依旧为 Challenge_Data:4–7 → GlobalMetadata:33/88 → SaveValues:76–81 → SaveData_Value:279–283 → SaveData:57–61，登记的是全局对象图，不证明真实保存成功。

3. **前提与反例。** W13/W36 使用有效 tower、原队伍 O/活动 E、上限 3、历史当前/上次/最大胜场 5 和交换 2、前序开始保存正常返回。取消恢复 O 并清即时状态，保留 tower/六计数/上限；再结束按取消后决定 0 回收当前为 0/0，上次/最大仍 5/2，然后身份 −1，玩家队伍被清空的原队伍值 nil 覆盖，非进行中早返，两调用没有新保存或地图刷新。W36 的决定 1 直接结束、无快照取消、取消后不重新报名再开始、未开始就结束各按独立初态核对，没有将这些条件混成一个轨迹。地图接待事件必执行该组合仍未证明。

4. **最小修订及实际接收。** WP55:55 明列清理/保留，57 明列外层顺序和组合；WS:79/102 给输入、预期与邻近对照，WP55:136 的场景数 36 对齐。actual WP55/战斗目录分别与修后候选精确同字节，且本次重新读实际全文确认语义；没有剩余必要修订。

5. **验收与历史回归。** WP55:48/52–54/56/61–65/128、WS-W14–16/W28/W29/W30/W35 对固定 baseline 均逐字保持。当前 `§2.3` 的取消“只做重置”边界须连同 :55 的精确字段范围解读，未又引入“整个挑战对象全清”。新读 9366 的 WP55:48–65 与 13fddb 目录 WS:77–99，重验正确控制，保留旧 W30，而不是用旧 PASS 免验新组合。

6. **独立裁定与反证。** 新接合再次尝试“取消会清外层身份”“结束先挡非进行中”“所有字段都清”“重新开始仍换入已清报名”等反向；固定完整 reset、外层委派及开始/结束顺序均排除。完整原反证范围与当前合同同身份，未恢复被撤回或超出前提的声明。结果 **INTEGRATED_CONTENT_PASS**，限定静态内容。

7. **依赖与接收者。** R6-I 实际写入已冻结，WP55/共享目录本域接合本次新审通过。WP09/10 的整体保存对象与失败分层没有本项新增语义需求；实际全局公共登记、其它领域 shared 内容和有效配置资格仍由父审查单独处理，本辅助不将两项签名扩为全批正式接受。

## GR6-F-002：七组实际裁定

1. **身份与裁决。** required/P2、无别名、唯一主批 R6-U13。范围仍为界面人数读取值的正数容量前提、读取值与最终公开最大长度的区别；既有空数组报名和子集添加不是新根因，旧 UI-PARTY-004/stale-command→Summary 推断没有恢复。

2. **双向证据。** 实际 WP54:19/45/47，QC-Q48/Q49:58/59，WP66-A:132/238 对照固定 Rulesets:5–11/27–46/70–78/176–223/229–238，完整多选 UI_Party:1051–1139，接收 Challenge_Data:38–50 与 Challenge_BattleChallenge:135–137/200–203。预检按最少合格成员而不普遍用最终最大数；加入门是 `number > 0` 才限容量，焦点是已选数恰等于读取人数且刚新增，CONFIRM 仍独立调用最终判断、显示第一条错误并继续。

3. **完整正常与负数对照。** 以下按 fresh actual WP54/Q48/Q49 与 fresh actual WP66-A 全文合读，均为静态派生向量，未执行界面。

| 输入与前提 | 加入、焦点与最终结果 |
| --- | --- |
| 默认原始人数 0，最少 1，无成员/组合限制，A/B 非空合法 | 预检真；A/B 注记 FIRST/SECOND，无容量拒绝或自动 CONFIRM 焦点。确认两人先过 min1，再报 max0 首错并回选择；空确认先报 min1 首错。BACK 精确 nil、不提交。 |
| 显式设人数 1，合法 A/B | A 新增后焦点 CONFIRM；B 加入被拒、仍 NOT ENTERED；确认精确返回 [A]。 |
| 显式设人数 3，合法 A/B/C/D | 第三次新增后焦点 CONFIRM；D 加入拒绝；确认按位次返回 [A,B,C]。 |
| 原始规则构造 −1，配置最大 6，合法六员 | 界面读取也是公开 max6，正数容量门生效，第六次新增焦点 CONFIRM。 |
| 标准样本构造 −1，符合成员、种类、持物规则的六员 | 界面读取原始 −1，加入人数门不生效；第六次新增无自动 CONFIRM 焦点。最终公开 max6，合法六员确认可过；工具直接最终判断七员报 max6 首错，不声称普通六槽 UI 能选七员。 |
| 显式 set 人数 −1 | 最少/最大夹为 1，区别于带负数的构造。 |
| 正常取消 nil / 工具或替换 UI 产出空数组 | nil 不提交、不覆盖报名/活动队伍，包装精确 nil；空数组是已提交结果，覆盖报名、包装精确 false，进行中还立即清活动队伍。普通 min1 CONFIRM 不能据此宣称可提交空数组。 |

非正读取值没有放宽最终资格。焦点不等于自动提交，人数相等还必须“本轮新增”；正常 3/4 人杯、最少人数不足不开画面、取消与 No Entry 重排均保持。

4. **最小修订和接收条件落实。** 原候选具体写集只含 WP54/战斗目录、WP66-A 属具名非阻塞领域依赖；通用合同指定 R6-I 唯一正式写者、实际 shared 全文复审在接收后。原复审允许后置但阻塞实际通过的条件没有撤销，本次已落实。3ef `facility/wp66-a-receiver-payload.json` 完整新读 1–39，4382 bytes、SHA256 `5d87aedfdbe5b5a37cea2840c7dcc17be25654f70e983d51721bbe1374199c61`、blob `cb363bf03b18f50f4b9378a0e0731a8efa38ad93`。实际 WP66-A:132 精确等于其完整 proposed line：正读取人数才挡加入，焦点按读取值恰相等且新增，引用 WP54 §2.1 并明确最终资格独立。actual:238 的最少人数守卫与首错留屏继续正确。**旧具名内容接收阻塞在此冻结 actual 的本域内容层解除，无需新的正文修订。**

5. **验收、共享保留与历史资格。** U10 `d3554f9479fadcd1255cf8103b19e4aa88e1825b` 的 WP66-A 全载荷为 45461 bytes、SHA256 `c539dc29e22f7469cbad3ca3a2ccbdd31cac240f03f1ec1c28804108406838e1`、blob `84f5deb658f59ae39cd7c392c89cfc9c05a2615c`。在该完整字节上只替换旧 receiver line，所得 **完整文件等于 actual**，增量 245 bytes；全部其它行保留，U10 §6/§7/§8 及失败/回归限定没有被 root receiver edit 覆盖。WP66-A 与上一实际 9d5b 同字节，但本轮此前尚未收到的新实际 WP54/QC 已联合新审。WP54:47、QC-Q01/Q31、WS-W28/W29/W35 逐字保留；当前 raw QC49/WS36 等于唯一 ID 数，无重复。R2 B027 的旧 NEEDS_REVISION→定向修复、d815 完整限定、167296 第237精确五元组与恢复的精确 control-coverage blob `8c8f6adcdbf83a605afe3ccd6530dcba32752977` 按 3ef 原完整语义记录有限复用，本次重新核准确字节/资格载荷；旧记录未取得 d984 commit 元数据，本次也不声称对该 commit 作新读取。当前 nil/[] 接收 joined source 与实际正文/目录新读复核保留其正确限定。

6. **独立裁定与反证。** 新 join 再次排除默认 0 被最少预检挡死、0 阻止第二位、负数一律读 6、最终拒绝等于活动空数组提交、自动焦点等于提交和普通 UI 能选七员这些反向。旧 generator 的 stale-command 假说经已读取的 Ruby 2.6.10 block 局部反证纠正；本次没有新执行 Ruby 或 Summary，也没有把先前反证模型执行当作本次源执行。结果 **INTEGRATED_CONTENT_PASS**，限定上述 actual 内容。

7. **依赖与接收者。** 原 WP66-A 接收已发生，四份 fresh actual full files 与生产/消费链及 U10 shared 原内容相容。root_edits/receiver_delta 都明示不凭接收载荷增加候选 PASS、不接收旧 FAIL 整包；本次签名只解本域 actual 内容条件。shared 其余 ID 的非作者判断、公共追溯/矩阵同步、正式接受/关闭与配置资格仍需分层处理。

## 共同条件与未执行边界

actual 输入状态为 `ACTUAL_COMPOSITION_PENDING_INDEPENDENT_REVIEW`，administrative `planning/feature-matrix.md` 与 `audit/source-traceability.md` 更新由 R6-I 延后到独立实际复审之后。本辅助没有改这些正式台账，不能把公共同步记为已经完成；需实际精确同步、公共登记复审及父审查所辖共享范围通过后才有后续正式接受/关闭依据。R1 原 WP、R2 229/21/341、R3 23/76、R4 当前17/76与 B5旧16/75、R5唯一92 CLOSED 的旧准确范围沿用而不扩大；本报告没有新 required、别名、计数或 optional/policy 提升。

请求配置为 gpt-6.1-sol / ultra / default tier / default speed、禁 Fast。公开协作元数据只列 priority、无 default 参数，也没有有效的本次 model/effort/tier/speed/平台 UUID 回显，均 **UNVERIFIED**。本次继续原辅助、不新 spawn、不重启、不用 CLI 探配置，不查 token/认证。有限静态内容判断与模型配置资格分列；本报告不是配置合格签名。

本次新增参考定义/回调执行、作者 helper 执行、隔离 writer、完整可执行独立行为模型、宿主/Mac/UI/Demo、真实保存/加载/录像反序列化与真实服务操作均 **0**。新增工具只有自己编写的文档/身份/原行保留检查；它们不能证明运行行为。地图事件可达性、原生媒体/界面、宿主和重载计时等原未知边界未提升。具体失败尝试、截断和补读诚实保存在 [reading-ledger-notes.json](reading-ledger-notes.json)；成功实际 UTC/argv/exit 与全文范围、bytes/SHA/blob 在 [reading-ledger.jsonl](reading-ledger.jsonl)，本地 stdout 逐次保留，不倒补未捕获时间或失败原因。

**最小必要修订：无（本辅助负责 F001/F002 的冻结实际内容）。剩余阻塞：有效配置资格、公共同步及父审查覆盖的其余 actual 范围、正式接受和 CLOSED 均未由本报告认证。**
