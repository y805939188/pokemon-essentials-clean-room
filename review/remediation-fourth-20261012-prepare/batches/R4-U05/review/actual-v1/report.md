# R4-U05 精确 actual 独立复审

**GR4-M12-001：ACTUAL_PASS_SCOPED。** 四项验收、当前 editor→PBS→runtime 有限握手及本批整合身份均 PASS；无局部返修项、无本次审查技术阻塞。本报告只覆盖具名 actual、两正式文件与列明消费者，不登记接受或关闭，也不代替 U06 最终跨批门。

| 绑定 | commit / tree |
| --- | --- |
| actual | `60db7c78ce3fd8a90e0ca34127eba07ecbcc650e` / `075c851d7f528ce2a409cd16b311534c7d1971a4` |
| actual 父提交 | `aa2922fe2196e60c6d30b3fe93cc9c5d51aac618` |
| 任务发布 | `9c00413d06dad3929c1fb90e827d8384d001acc5` / `2b5c9fad5832045c6797314d8c8fdb6ed24cf993` |
| 原候选 | `2332c5523b6e98ae5c2e7be3ada78c6f6d4eaf9b` / `ffd02b689d1bde6018e1de22fa1483c0997ffdf3` |
| 原独立候选报告 | `3f9f12c4cce364a8a95ac2798d0d0a0e16bccb90` / `1a4342591267dedbfbcbcc71cd74ad65fcb904b6` |

本次继续同一 reviewer 任务 `/root`。父实际派发记录通过冻结任务包绑定 reviewer thread `01a130d6-b94c-710a-aa16-8c1dcb9d8028`，这项来源记录与候选报告自身的 thread 回显 **UNVERIFIED** 分开；原报告字节未重写。请求 `gpt-6.1-sol / ultra / default / Fast=false`，实际参数回显仍 **UNVERIFIED**。只读辅助任务 `/root/evidence_audit` 独立复算完整身份与限定保护，不是正式接受签名。独立分支 `review/r4-u05-actual-independent-20261012` 从精确任务发布创建，只新增本 `actual-v1/` 目录。

## 四项验收与实际消费者

| 项目 | 裁决 | actual 检查结论 |
| --- | --- | --- |
| AC1：整集空 Land21、源不变、后缀及未保存层次 | PASS | 亲读 WP73-B §6.1/§6.2/§11 与 WE-M11-E01 a/c。源(5,0) Land零槽/21/s、目标(7,1)未占用，Copy成功但未总保存：只在目标保留率21/s，无Land类型，可再新增Land，源不改。No消副本以原档案有源、无目标及重载成功为前提。 |
| AC2：非空独立复制、冲突、单类型反向对照 | PASS | WE-M11 保留合法非空Land槽、21/s，目标编辑不改源，精确目标冲突拒绝；E01 b 从独立源状态 Copy 到已注册且未用Cave，保留Cave(x0)/复制率21，源Land不变。 |
| AC3：Copy、PBS与实际遇敌分层 | PASS | 亲读 actual WP04 §5.5、WP36 §3.1–3.3/§9 与 WP73-B §6.4–6.5。Copy过滤在登记阶段；PBS省空类型是随后写出步骤。编辑/保存/重载/调试包装不重装当前地图快照；不推定真实遇敌结果。 |
| AC4：执行证据边界 | PASS | actual正文及向量保持静态/NOT_EXECUTED。本次参考、模型、宿主/Demo行为执行0；历史4条单列。此项判断的是证据分级，不能读作功能运行通过。 |

候选静态读源、正常可达性与反例证据在原独立报告中已完成。固定 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、完整源身份及两正式文件都未变，故按合同复用其精确缓存；本次另外亲读实际消费者并完成新的有限整合判断，没有把候选 PASS 自动复制为 actual PASS。

| 当前 actual 消费者 | 有限握手结论 |
| --- | --- |
| WP04 §5.5 | 只输出非空类型，正率写第二字段、零率可省略；Land0→省略→21以合法非空槽及成功文件步骤为前提。它不解释尚未保存时目标类型列表，也不补回Copy丢弃的空条目。 |
| WP36 §3.1–3.3/§9 | 精确存在性与版本0查询回退分开；当前快照装载与登记分开。真实异值版本且上下文存在、或实际地图装配才可重装；同值早退。宽限4/累加器210在同值时保持，实际装配后0/210；不保证一步开战。 |
| WP73-A §5–7 | 选择器按各入口返回取消结果，登记、档案/PBS与消费者分层；遭遇主体归WP73-B。没有统一补回空条目或取消恢复全部消费者的承诺。 |
| WP72 §8.3 | 默认调试菜单只承接编辑器入口与淡入淡出包装；原固定源中该包装不调用遭遇装载。没有隐藏快照刷新保证。 |
| 已接受 U02 WP75 §8.6 | 35条文本转换、路线脚本正常求值后的前缀调度与范围移动链接均按原合同。转换或前缀匹配不产生地图遭遇快照刷新，也不改变Copy的登记/保存阶段。 |
| 已接受 U03 WP17 §4/§4.1/§5.1–5.4 | 普通命令允许取消时BACK先于USE；逐位数字的USE先于BACK、越界USE仍等待。二者是具名输入组件的条件规则，不能推成所有编辑器统一优先序。U05以合法返回、成功Copy及No重载为前提，不推定物理同轮输入或新增登记副作用。 |

独立质疑：U03“空数组USE可返回0”及数字同轮竞争是否使零槽复制前提无效？零槽指遭遇类型的槽集合，编辑命令和已注册Land/Cave选择集合不是同一个空数组；成功Copy前提经过地图/版本返回值与冲突门。当前输入合同没有使该正常可达状态消失。No结果仍取原档案，不能从BACK名称推断恢复进入时的所有内存状态。

公共提案已读 actual `batches/R4-U02/author/integration-proposals.json`：其 editor registry→PBS→current runtime map snapshot 项要求本次有限握手，WP75 §8.6只追加范围行为链接，没有要求新增正文。旧 U02 接受记录明确把本项留待U05/U06，未预签本 actual；本次对上述当前消费者独立判断后，**NO_EXTRA_FORMAL_EDIT_REQUIRED**。U03共享提案对普通命令/数字输入的分层处置与当前文本一致；不扩大到其它提案或最终U06接受。

## 整合完整性、保护与发布

完整字节独立复算结果：actual两文件精确等候选；26已接受正式文件精确等实际父提交；其余103精确等B `1f36475d22120a0d1175967d5b17d71fe8311d88`。131路径集合及bytes/SHA256/blob均匹配机器包；这只是分组完整性核验，不重做131篇语义review。

| actual 正式文件（均在 deliverables/final-specification-set/ 下） | bytes | SHA256 / blob |
| --- | ---: | --- |
| `demo-dx/wp73-b-world-editors.md` | 41130 | `b82fbb32bd1ca9119d39a606ffe690fa670ba10ec86208f39f94f41b4552dc47` / `25514e1add5aadf480ac2506914e3859b1dd5936` |
| `test-catalog/demo-dx-wp72-73-74-75-76-77.md` | 106211 | `8bf390bd2a34540e73a35d57021eafaab6300afa1240f3bbb1fd3ae8b0a3ec0c` / `5cce7151364a06ef9ea44fabca3c40cdeaabd570` |

actual正式binary diff精确等原候选diff，14193 bytes、SHA256 `f67bce94011caeb1461d7677b109840dbc81065671e1b919bb32eb90775b8cea`。作者10份及原候选review8份完整字节、目录集合逐字保留，既有WE-M10/12/13/14、CV-M28/30、GN-M14–20保护缓存继续有效。旧GR3-M12 BMP/评级及其它GR3/229/341只复用原qualified身份、not_reexecuted，不重开或补签。

父→actual共23个变化路径：两正式、作者10份、候选review8份、registration两检查及登记员status-ledger准备元数据。登记账确实有待审更新，不能称完全未改；actual和任务发布仍接受16、CLOSED0，U05接受为空，未提前登记actual裁决。本 reviewer没有写任何账或正式文件。

使用本 reviewer此前独立远端对象库作缓存，重新fetch精确任务发布；完整比较actual的23份载荷版本和任务发布增量5份版本，共28份、768118字节，commit/tree及文件bytes/SHA256/blob均一致。没有复制本地对象或设置alternates，没有全历史重新下载或重复旧包语义签署。[validation.json](validation.json)含逐文件读回身份；[identity.json](identity.json)、[criteria-results.json](criteria-results.json)、[read-ledger.json](read-ledger.json)分别绑定输入、裁决与必要阅读。报告普通push后再次fresh fetch完整新增交付，后继回执记录报告提交，最终commit/tree及最后完整读回由最终响应外部绑定。

## 限制与剩余门

本次新增行为执行 **NOT_EXECUTED_THIS_UPDATE，0次**。历史第四review四条 **M01×1/M02×2/M12评级结算×1** 保持原隔离执行范围，评级未调用遭遇编辑器，不用于证明Copy运行。JSON/哈希/字节/差异检查均TOOL_VALIDATION；向量均DERIVED_VECTOR/NOT_EXECUTED。

真实UI、媒体、物理输入、地图/完整Demo及外部插件仍未证，未来兼容政策未代选。这些不阻塞本合同静态事实验收。当前 **ACTUAL_PASS_SCOPED** 仅为唯一登记员接受U05的审查前提；本报告不登记ACCEPTED_SCOPED/CLOSED，U06最后跨批与关闭门仍待执行。不修改参考、用户数据、main或标签，不删除分支。
