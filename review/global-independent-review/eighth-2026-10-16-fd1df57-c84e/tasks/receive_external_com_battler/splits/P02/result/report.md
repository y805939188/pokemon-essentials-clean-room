# P02 有限接收报告

结论 **BOUNDED_REVIEW_COMPLETE_FOREIGN_CUMULATIVE_JOINS_OPEN**。9 结构、146 正向子断言（含 pbInitEffects 的 125 条）、12 分配反向子断言及本片要求的 6 个必要消费者全部核验；本片主责/必要语义未读 0，新增 required/optional/policy 0。未签父任务最终接收或 B8 全局 PASS。

合同固定于 `02c8206651676effe40ff9a33dbb70998b79c1b1`；目标作者提交 `5cf9503a99a855c06a8ac9c932e6778b57e71049`；B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。内嵌旧合同只作既有证据来源，不覆盖最新用户授权。

E007 初始化源 1–325 行完整阅读，C0152–C0160 全覆盖。125 个状态初始化逐字段核验，非抽样。全部原断言含义、前提、源与独立理由见 [reception-ledger.json](reception-ledger.json)，分母见 [frozen-denominator.json](frozen-denominator.json)。

- 构造独立 DamageState，先空白再非接力，不等于真实派出；空白各字段默认不走专用持久入口。
- Dummy 先拒蛋，复制显示/计算值，清参与者并标记；裸调用不清旧能力/物品/招式。实际离场延迟攻击先 new 空白，交叉解除在复制前；来源在场则复用现有 Battler。
- 正常复制→接力/非接力效果→伤害 reset 顺序成立；逐槽生成战斗招，Shadow 实际覆写另核；无统一异常回滚或自动完整能力获得链。
- 七阶级和 18 接力项保留/重施；正 LaserFocus/LockOn 设 2，PowerTrick 以新原值交换，Mega Gengar/不可失去能力例外；其它清理、ProtectRate=1、七组存活场上交叉解除逐项成立。Illusion 清后按业主段与显示秩末位择取，不取原数组末槽；持久异常来自新个体。
- pbUpdate 先持久重算再等级/HP/总HP，Transform 保留五值及 fullChange 类型/能力；不重建招式/重置全部状态。pbReset 只做具名清理，不推 captured/dummy/身份全清。
- participants 只记活对侧当前存活对方的队伍下标并去重，玩家/收益及成长门由消费者再筛；空集合不由 ExpAll 自动补足。

FC42-GROWTH.01（CORE 成长分配）及 .02（CORE/CREA_C 成长、学招取消、零收益和重算）累计 OPEN；本地与具名必要源接点已核，不签完整外域，原边界见 [interfaces.json](interfaces.json)。H01、中央累计、IF04/全局 task-final 由父整合。

完整消费者和强制八事实在同一组上下文完成，见 [P01A/interfaces.json](../../P01A/result/interfaces.json)。[阅读台账](reading-ledger.json)、[有限反证](proposal-counters.json) 与 [组报告](../../P01A/result/report.md) 给出完整共享证据/限制。行为/模型/游戏/native/UI/音频/存档 **NOT_EXECUTED / 0**，**UPDATE_NOT_STARTED**。只写授权 result/，独占分支普通发布，不整改、不改规格、不合并。
