# R4-U04 精确 actual 独立复审

结论：**GR4-M05-001 — PASS / ACTUAL_PASS_SCOPED**。四条验收均满足，当前实际生产者与具名消费者的交界一致，未发现本批必修阻塞。结论只覆盖下列冻结 actual、当前消费者和合同范围；本审者没有登记 ACCEPTED_SCOPED 或 CLOSED。

| 身份 | 精确绑定 |
| --- | --- |
| actual commit | `ede6a0714d29843c2ca896af6187ae1dc97a9d8a` |
| actual tree | `21b917b2f5267ec4b9f3a0d69b135b0011e43f49` |
| actual 整合 parent | `0cf49785b67baa911deb4ff8acfa9cc64395ce8a` |
| 任务发布 commit / tree | `cfc19190f6596896524f2fc9577471577a3306de` / `ff8f0730a6eee0cb0966d5f3e06c90557b883b8d` |
| 候选 commit / tree | `1c2cdcbe6509839a19fd3c48c8a412a6c19e161a` / `fcd0cff8a0830b7e3a8860f8e84c55c5bb793ec3` |
| 原独立候选证据 | 报告 `ec98b2e53fac1651ac6f9f55d260c041827851ef`，发布后继 `c10aaea975c0b0e87a88de9d536e2ab2afb45f0b` |
| 固定参考 / 正式 B | R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；B `1f36475d22120a0d1175967d5b17d71fe8311d88` |

继续同独立审者 `/root`、thread `01a130d5-fcbe-7506-9573-e758528ad023`。请求 gpt-6.1-sol / ultra / default / Fast=false；实际参数回显 **UNVERIFIED**。辅助任务仍为 `/root/source_eligibility` 和 `/root/consumers_regression`，只读取证；本审者裁决。未参与正式修订、未修改参考或真实数据，没有将作者或登记员自述直接作实际结论。

独立工作树 `/workspace/r4-u04-independent-actual-review`，分支 `review/r4-u04-independent-actual-20261012` 从任务发布提交起步。唯一新增写域为本批 `review/actual-v1/`。任务发布后继只用作任务与交付证据输入；实际语义绑定上述更早冻结的 actual，未换成分支当前状态。

## 四项实际验收

| 项 | 结果 | actual 证据与结论 |
| --- | --- | --- |
| 1：五主动物品资格 | **PASS** | actual WP28 L204–212 独立列五种默认身份及两上下文资格：战斗目标非蛋且 HP>0，场外无此存活门，通用门与复活资格保持。当前完整文本等已审候选，固定 R 的两族资格及别名证据未变。 |
| 2：反例与量值 | **PASS** | actual WP28 L208–216、目录 L108–114 保持独立重置夹具。HP0 战斗拒绝位于登记前，库存1、PP0、HP0；普通场外 ETHER／主动 LEPPABERRY／ELIXIR 得 PP10、库存0、HP0，MAX 两种得 PP35。HP不由PP恢复改变。 |
| 3：正常／失败／边界与当前交界 | **PASS** | 目录 L114–120 的 HP1、满PP、取消、30→35封顶、多槽对照及原同步／复检／退款规则均保留；本次亲读 actual 当前 WP67-A、WP20／WP40、WP17／WP66-C。当前 WP51 AI缺索引与 WP50 被动LEPPA依然不同入口。 |
| 4：执行边界 | **PASS（边界验收）** | actual WP28 L216 和目录 L108 保持 DERIVED_VECTOR／NOT_EXECUTED。本复审新参考、模型、宿主／Demo行为执行均0；四次原隔离执行没有转授给PP向量。 |

机器可读逐标准结果与完整夹具保存在 criteria-results.json、findings.json。数学和状态推导沿原限定向量：0/35加10得10；30/35仅增5；回满35；全招逐槽恢复并以正增量决定成功。多槽相同招标识由已接受 WP20 的标识赋值边界允许，不把普通学习去重扩大为所有数据状态不变量。向量全部未执行。

## 本次有效 actual 检查

本次质疑重点是：U03 已进入实际分支后，消费者是否改变取消／拒绝／数量规则，使候选原语义不再成立。审者亲读 actual WP67-A L117–147，而不是用候选时 B 的消费者签名替代。当前整文件为 U03 已接受 `5dd6789b22e03b85bb81ae73b9c65a1fab585186` 的完整字节，blob `531f6e009e8b8e155191c8af1cecf2b04e0ab708`、74619 bytes、SHA256 `b80b13f518d205b29855a051aa8dfdb4d8288b7d2f1630b75d6b9b84def49d92`。

WP67-A L130 仍规定类型2选招取消回成员选择、成员提交被拒留在成员循环；L136 明确拒绝时库存未动且未登记，L137 明确全部资格通过后才登记并扣减。其完整物品交互 §5 虽仍等 B，本次仍绑定当前整文件；实际新增动画查找条款在 §9.4／§9.4.1，不覆盖上述物品阶段。因此 HP0 的PP拒绝不能写成统一UI预过滤，选招取消也不能被写成直接退出物品菜单。

实际 WP20 §5.4–5.5 保留恢复封顶、持久／战斗两侧及同标识／未变身同步边界；当前 WP40 §4.2／4.2.1 保留登记先扣与执行复检、退款残留／正常返回清消费身份。HP0 战斗拒绝没有本次登记身份，所以没有本次执行退款或残留；登记后中途变化则仍进入原复检合同，不能借正常向量删掉该分支。

WP17 L109–143 的通用逐位数字先编辑，再处理 USE；合法值同轮确认，越界USE继续等待且不处理同轮BACK。WP66-C L78–108 的共享按件数量采用 BACK→USE→方向，商店另采用方向→USE→BACK。两合同明确独立，不构成主动PP的统一资格门。默认五种主动PP场外上限仍1、战斗每次1，不从通用数字或商店输入规则推出额外的多件消费或取消结果。

actual author/shared-proposals.md 已完整读取。当前 WP20／WP40／WP67-A 的引用可直接消费新 WP28；本次消费者和完整身份记录为必要 actual 握手补充，无额外共享正式修补要求。未改公共 traceability、共享正文或登记台账。

## 精确整合与未变证据复用

实际执行 validate-actual.py，结果 `PASS_ACTUAL_IDENTITY_PARTITION_AND_SCOPE_ONLY`。两份 U04 正式文件完整 bytes／SHA256／blob 与候选一致：

| 文件 | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| WP28 | 48461 | `b165c26cfe985bccc99741349dd857faa35a7252ec40fc2f7c28bd6e9fd6d374` | `bba5e7f7347293ece2ef7c6b87c403ac89e21734` |
| 道具测试目录 | 39992 | `cbf077aa3f00a3b82ba7e6e3c89352eadfd0fb3632d25817d78fa3c08967d2f9` | `eb088929e6d746fda080897c558de518f7d71f03` |

131正式文件精确分区为：2份U04等候选，24份已接受U01／U02／U03等整合前父提交，105份等B。actual 对整合 parent 的正式差异仅两份批准文件；actual→任务发布没有正式差异。22份作者／原独立候选证据完整字节保留，7份当前消费者完整身份独立核对，WP67-A和WP17同时核对U03接受输入。登记员的本批完整新增交付路径按固定前检查点 `d305ba47f31ecfde747b763682e87f32abe54888` 界定，共50条；它们在发布核验中完整读回，不把旧全仓或历史证据重新下载／重审。

GR3-M05-002 探测仪正文及旧向量保持原限定字节；GR3-M07-001 的登记／退款残留和当前WP40／WP67-A消费者仍相容。只做受影响保留与交界复核。其余GR3／旧229／341仍为 `historical_qualified_evidence_reused/not_reexecuted`，没有补签全历史、换新owner或扩大运行范围。U03既有接受也没有直接签给本次U04新生产者；本报告另完成当前实际握手。

## 执行、发布与余下阶段

本次 **EXECUTED_REFERENCE=0、EXECUTED_MODEL=0、EXECUTED_HOST_OR_DEMO=0；NOT_EXECUTED_THIS_UPDATE**。Python／Git 身份、JSON、分区、写域及完整字节读回属于 TOOL_VALIDATION。固定R语义证据按精确commit／blob复用并有限回读必要源段，未重做312脚本全扫描、完整历史下载或全球review。

原第四review仍有M01×1、M02×2、M12×1共4次隔离原函数调用，保留初始化／替身及各原域限制，M05没有运行记录；它们不是本次PP或真实宿主通过。媒体、真实按键、像素、地图、存档、Demo、全部外部覆写／世代替换仍未运行认证。未来异常兼容政策未代选。

报告普通push到独立实际review分支。fresh fetch以原独立远端对象缓存为基础取得新交付对象：完整核新增报告、50条实际任务交付、24份已接受实际正文及当前具名消费者；105份未变B正文核精确缓存身份。后继 publication.json 绑定报告 commit／tree及完整读回结果，最终后继身份由返回值给出，避免自嵌递归身份。

本批 actual 必修阻塞：**无**。唯一登记员收到本限定结论后可按其授权处理U04接受；本审者没有写该接受或关闭动作。U05实际门与U06最终整合／关闭仍属于后续阶段，main及正式正文未由本审者修改。
