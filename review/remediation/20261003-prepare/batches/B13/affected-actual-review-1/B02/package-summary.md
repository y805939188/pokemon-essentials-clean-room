# B13 affected actual 独立复审

Reviewed ACT：`d81562bfe0e79ca4df3233ada38fa09e800bdafc`，tree：`ae6ca9bd055f6feca3657db7bd511b2be682d897`。

冻结派发包 `996e4f04bcc34b992c9cc4d25db9548850266a06` 是report-only后继，未作为被审目标。candidate `db9e6ed1997efe5bf94dac952aad44fd3b9ebd21` 仅作为精确版本证据，正式接受前驱为B12-C `8e67f780c204d593d89f364f585d2c6c2fe74631`。

| owner | ACT结论 |
| --- | --- |
| [B02](../B02/report.md) | NOT_AFFECTED |
| [B03](../B03/report.md) | NOT_AFFECTED |
| [B04](../B04/report.md) | NOT_AFFECTED |
| [B07](../B07/report.md) | NOT_AFFECTED |
| [B08](../B08/report.md) | NOT_AFFECTED |
| [B09](../B09/report.md) | PASS_SCOPED |
| [B10](../B10/report.md) | PASS_SCOPED |
| [B11](../B11/report.md) | PASS_SCOPED |
| [B12](../B12/report.md) | PASS_SCOPED |
| [B14](../B14/report.md) | NOT_AFFECTED |
| [B15](../B15/report.md) | NOT_AFFECTED |

11个owner均有新ACT结论；4 PASS_SCOPED、7有具体依据的NOT_AFFECTED，REQUEST_CHANGES 0。角色阻塞为空，最小返修范围为空。

两份完整未过滤流已独立核验：前驱→ACT 215路径／22,882,597 bytes／SHA-256 `b06a8747eb313d0e27803ba86d37d031c95e708bd981ebddc301c6998b1f72d5`；candidate→ACT 97路径／16,259,629 bytes／SHA-256 `6c28b82aa419abc0b6546f1f304edea54f9f69ba6ea220b66030b3d9f58057ef`。每条路径均分类；没有用局部差异替代完整流。

11正式输出及153证据副本逐一核验，232旧接受的原始公共记录、完整限定回执及全部既有目录模式／blob保护通过；8新登记仍pending。完整根／扩展／最低验收、来源界限、剩余贡献者与WP67-A的B16边界保持。原稿4补丁按scope1及WP58 scope2的精确before→after序列应用，许可不等于质量通过。

候选F1入场时点修复在ACT有限接口仍成立；B027 nil取消精确返回nil(null)、空列表提交精确返回false，活动／非活动队伍后态、默认UI人数门及回合末延后选择分开。实际Ice资格与AI拒冰／当前HP估量隔离，11设置／3消费者键、SoulDew和SkillSwap原门保持。详见[B11当前有限复核](../B11/actual-entry-and-return-recheck.json)。

2168项新Git／JSON／hash／text元数据检查通过。仅静态设计复核，reference／Ruby／game／行为向量／历史程序执行0，fresh reference reads 0。请求gpt-6.1-sol／ultra／default／Standard保留，实际后端UNVERIFIED（已批准Plan A）；未探针、降级或新开任务。

本包只签11 affected actual有限角色。FULL actual和根C未代签；14/21批、232已接受、8新pending、229 OPEN／0 CLOSED及B16等待B13-C状态不由本包改变。B030增量0，非局部义务未关闭。

[结构化索引](package-index.json)、[共享完整核验](shared-actual-audit.json)、[配置与限制](configuration-and-limits.json)、[读取记录](reading-log.json)、[新元数据检查程序](verify-new-actual-metadata.py)。报告commit由外部发布读回回执绑定，避免自引用。
