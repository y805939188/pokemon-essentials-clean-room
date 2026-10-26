# Pokémon Essentials 净室行为规格

本项目提取Pokémon Essentials的功能、游戏规则、逻辑、状态变化和用户行为，为未来从零开发独立TypeScript实现提供规格依据。参考只读，规格保持实现无关，战斗／AI保留完整范围。

**当前交付：第八轮29项必改（2P2／27P3）、10项选入可选、9批实际整合已在限定R8静态内容范围内接受闭环；10组接合获最终独立PASS，内容阻塞0。** 第八轮已于2026-10-18经[PR #1](https://github.com/y805939188/pokemon-essentials-clean-room/pull/1)正常合入main，合并提交为 `dae67763071cfe135b99f90639d71425410b1ed3`。

从[当前交付](CURRENT-DELIVERY.md)或[第八轮交付导航](review/remediation-eighth-20261016-prepare/DELIVERY.md)开始。

- [正式行为规格](deliverables/final-specification-set/README.md)
- [第八轮最终报告与限定范围](review/remediation-eighth-20261016-prepare/final-report.md)
- [最终关闭决定](review/remediation-eighth-20261016-prepare/closure/final/decision.json)、[39项逐项记录](review/remediation-eighth-20261016-prepare/closure/final/per-id.json)
- [开发交接](review/remediation-eighth-20261016-prepare/handoff/development-handoff.md)、[已知限制](review/remediation-eighth-20261016-prepare/handoff/known-limits.md)
- [实现去向清单](planning/implementation-routing/README.md)、[框架路线图](planning/framework-roadmap/README.md)
- [第八轮实际合并与仓库收尾（固定后继记录）](https://github.com/y805939188/pokemon-essentials-clean-room/blob/8fdb6f093ed6aed65e840b8b616c1184f8d2c59b/review/remediation-eighth-20261016-prepare/closure/final/repository-closeout/README.md)

第八轮冻结正式规格为131份（111正文／17 catalog／3 shared），子树 `93dc967b4cdb653359afc123d3b8b318d6475fdd`；参考R为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。这些身份绑定第八轮交付，后继规格补充按各自记录读取，不自动计入本轮关闭数量。

**有限静态关闭不证明完整运行等价。** L01–L14、有效配置UNVERIFIED、SOURCE_STATIC／DERIVED_VECTOR_NOT_EXECUTED、新增业务运行验证0，以及较宽原生／宿主／媒体／存档／回放与未来政策未知继续保留。736项去向的验证、阶段批准、实现与目标验收及四协作原型仍保留各自待验证范围。冻结报告内当时的待发布／待同步描述不回写；实际发布结果见上述固定后继记录。

历史入口：[第七轮](delivery/2026-10-16-seventh/README.md)（[最终入口tag](https://github.com/y805939188/pokemon-essentials-clean-room/tree/delivery/seventh-round-closed-final-20261016)）、[第六轮](delivery/2026-10-14-sixth/README.md)、[第五轮保全计划](review/remediation-fifth-20261013-prepare/integration/final-publication-plan/merge-cleanup-plan.md)、[第四轮](delivery/2026-10-12-fourth/README.md)、[第三轮](delivery/2026-10-12/README.md)、[第二轮](delivery/2026-10-11/README.md)。旧阶段文字、原报告、候选、FAIL／WAIT和各轮限定关闭范围完整保留。

第八轮main交付标签：`delivery/eighth-round-closed-final-20261018`；实际仓库收尾记录标签：`delivery/eighth-round-repository-closeout-20261018`。
