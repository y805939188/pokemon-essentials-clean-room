# 第八轮手动整改handoff五根增量准备

状态为 `READY_PENDING_ROOT_CORE_FREEZE`，`UPDATE_NOT_STARTED`。

以 `adjudication/root-decisions.partial.json` 的38条记录为唯一当前分类依据，原33条ID、分类和严重度保持不变，补入五条已有根裁决：WP31 unknown可选、CP002有限濒死音频必修、SHADOW旧式类别样本可选、CP01结束标记措辞可选、MG既有非空名称ESCAPE必修。合计29 required（2P2/27P3）及9 optional；独立视觉精度政策1条保持UNSELECTED，分开于此计数。

入口为 `handoff/cloud-eighth-update-handoff-prompt.md`，同规范数据为 `handoff/cloud-eighth-update-handoff-manifest.json`。`handoff/records-index.json` 精确解析全部38条完整合同，原33条引用固定恢复包全文，新增5条全文在 `handoff/contracts.delta.zh.json`；没有重复复制原12MB证据。九批更新prompt位于 `handoff/batches/R8-U01` 至 `R8-U09`，每批绑定原完整prompt/readset、有效共同门与本批新增合同，原正文继续作为执行前必读全文。

CP002与CP01归U06的WP67-A整文件writer，保持独立根因；CP01只在用户另选后纳入。MG归U09的CreatureE子范围，必改WP64§7及共享catalog的MG32输入/邻近控制。目录由R8-INTEGRATOR整文件唯一正式writer接合Factory/Triad/E及EG/EN/FC/TT/MG贡献，保32条、原ID、别名前缀与原副作用预期。WP31有效preserve明确64个注册身份与52个手工意义分组，原9102B记录不覆写。所有optional与视觉政策均保持未选。

已核对唯一必修主批次、两图、公共整文件写权和零新增语义先后边。原九批required正文与master对应完整章节逐节精确相等，调度对象与原batch-assignment精确相等；原master独有不必修、binary、撤回与待接收语义由具名支援读者完整接收。机械核等只支持去重，不产生语义阅读信用。完整阅读资格和载荷身份见 `reading-ledger.json`，范围见 `remaining.md`，机械检查见 `verification/validation.json`。

本任务写集仅 `tasks/handoff_final_five_root_deltas/`；没有Git/index、source、formal、公共索引或其它报告写入，没有启动整改或业务运行。root全局core、历史与接口仍待封账；未来真实core/enclosing commit由外部后继发布入口绑定，不伪造自身hash，也不把观察HEAD称最终core。
