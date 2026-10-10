# B13 原稿精确范围许可 2

裁定：**GRANTED_EXACT_FIXED_PATCH_SCOPE_ONLY**。本次仅许可 `specs/combat/wp58-battle-recording-and-playback.md` **§5.2** 的固定新补丁；before 行104换为 after 行104–110，其余字节不变。提案发布版为 `c52c0df80bcba45ac77f8da2cdee264890846327`，返修提交为 `235c9a599f20346bf82add2fa1d7220f5bfacdb2`，入口为 `author-draft-1/two-findings-repair-1/original-scope-proposal-2/README.md`。

固定组合补丁 SHA256：`8d186d65c9eb2bc0e03a27728bfa0ea8476f4753bb863054b41cdb3b79459b0d`；Git blob：`9c02854cb826e12a7ea82e6830fd1effd444d014`；3211字节。精确 before 来自 `1dc5cc80854e02965b9bb7a02c00a7c40d392f89`，其 SHA256 为 `6e18f9970fc7a104a5522ff93b9cde1af2e33996301ad6a766d148d2cda42dfe`；精确 after 为 `0dbd9207664b04d6ea869c5252bb91c8f4559eff0072656ea733f0a4043b5bc4`。正式 FIX_BASE 仍为 B12-C `8e67f780c204d593d89f364f585d2c6c2fe74631`，当前 before publication 不替代正式基线。

## 有限范围裁定

B029 原最低修订和确定复核要求完整非随机替补辅助入口的消费者链及 phase／owner／候选门。独立 affected `4a75ca146e10062e469a42a9610bc3026861a34c` 的 B13-AFFECTED-F1（B09/B11）指出：已有完整来源说明把 EjectPack／EmergencyExit／WimpOut 只放在攻击阶段，漏掉当前 WP41／WP49／WP50 已接受合同的入场最终扫描，且将“当轮不再行动”误延伸到开场首命令前。该时点遗漏是同根 B029，故以下固定条款均属于其既有范围：

- 攻击后替补的行动限定与开场首命令前分开。
- 开场／普通入场最终退出扫描、真实事件及逐入口门、首真即停、同一消费者追加／消费和首命令前时点。
- EjectPack 先消费再选择、负选择的记录及部分提交；能力取消与物品消费区别。
- 回合末只离场、后段补位才选择；随机强制、内部战斗 W16 与 Arena 候选限定继续保持。

独立 FULL `e03b7c2824105c5925cb9d64079bf653b03a41f4` 的 B13-R01/B027 仅要求修正 nil 取消返回的结构化验收证据。本次不增加 B027 原稿许可，不借此改 WP54/WP55/WP56 或已接受 B09/B11 合同，不增加 canonical/B030，不触及 W16/W24/W25 的既有字节。完整 before／patch／after 已读，静态文本补丁精确重建匹配；当前作者原稿仍为 before，登记者未应用原稿。

## 应用与后续

作者可在整个 before 身份匹配时仅应用该固定 whole.patch，并确认整个文件等于精确 proposed-after，随后发布、冻结完整新候选。旧 scope-amendment-1 及 pending 提案原件保持；旧许可不自动扩展至新字节。如补丁／路径／条款变化，应另交精确提案。

父任务协调原独立 FULL/B09/B11 角色对新冻结候选做必要增量复核；旧 SHA 上的 NEEDS_REVISION/REQUEST_CHANGES 不被本许可改变。本次只签范围，不代审 source、修复质量、反例或净稿一致性。完整当前控制及全部 candidate／affected／G／actual／C 门保持。

本提交仅新增范围与静态身份材料，正式仍 **14/21**，canonical **229 OPEN / 0 CLOSED**；G/C未发生，B16仍等待B13-C。无运行时观察、已执行行为向量或新增任务。
