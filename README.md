# Pokémon 行为规格

供使用任意语言从零开发的实现者按任务查规则、选择兼容模式并设计测试。先选一项开发任务。第二列给出参考版本的行为，第三列给出对应案例或可选的独立实现规则。

| 开发任务 | 参考版本的行为 | 验收案例与兼容模式 |
| --- | --- | --- |
| 创建个体、队伍和仓库 | [个体身份与拥有者](spec/creatures/creature-identity-species-ownership.md) · [队伍与盒子](spec/creatures/party-and-storage.md) | [获得、满队与移动案例](vectors/identity-party-and-acquisition.md) |
| 从野外遭遇进入战斗和捕获 | [遭遇抽取](spec/world/wild-encounters-and-modifiers.md) · [参战者](spec/battle/battle-context-and-participants.md) · [捕获与接收](spec/creatures/capture-and-receiving.md) | [捕获后的持物归属](spec/battle/portable-capture-held-items.md) · [跨域流程](reference/behavior-sequences.md) |
| 在回合中使用物品 | [行动顺序](spec/battle/commands-obedience-and-action-order.md) · [道具使用条件](spec/creatures/item-use-and-training.md) | [预留、消费与退还](spec/battle/portable-item-reservation.md) |
| 导入作者内容 | [身份与字段](spec/core/content-identity-and-schema.md) · [编译与失败阶段](spec/core/pbs-lifecycle.md) | [作者身份与旧档迁移](spec/authoring/portable-content-identity-and-migration.md) · [版本默认值](reference/generation-settings.md) |
| 解析进化参数并判定进化 | [方法、守卫、首个目标与提交次序](spec/creatures/basic-evolution.md) | [发行版与参考 R 的语法、失败阶段和整数表示策略](reference/evolution-parameter-compatibility.md) · [六入口边界向量](vectors/evolution-integer-boundaries.csv) |
| 结算战败并恢复游戏 | [终局结算](spec/battle/growth-end-of-round-and-battle-outcomes.md) · [野外回程](spec/world/field-passive-effects-and-blackout.md) · [保存与继续](spec/core/save-startup-continue.md) | [一次结算、回程、存档拒绝与冷读](spec/world/portable-defeat-return-and-saving.md) |
| 登记或浏览名人堂 | [登记、上限、按键顺序与空历史](spec/ui/lifecycle-presentations-and-history.md) | [快照隔离、编号与空列表退出](spec/ui/portable-hall-of-fame.md) |
| 选择存档槽或迁移旧友好度 | [原版保存入口](spec/core/save-startup-continue.md) · [友好度](spec/creatures/growth-learning-and-friendship.md) | [手动覆盖确认](spec/ui/portable-manual-save.md) · [显式迁移与恢复](spec/core/portable-friendship-save-migration.md) |
| 发放一次性奖励 | [礼物与接收](spec/creatures/acquisition-gifts-and-script-trade.md) | [容量、领取标记与重试](spec/creatures/portable-one-time-grants.md) |
| 处理进行中的操作 | [移动与转移](spec/world/map-topology-transfer.md) · [战斗终局](spec/battle/growth-end-of-round-and-battle-outcomes.md) | [操作归属与结算来源](spec/core/portable-operation-ownership.md) · [待处理通知与到达](spec/world/portable-world-notice-and-movement.md) |
| 为训练家选择战斗策略 | [参考版本的 AI](spec/battle/ai-action-selection-and-skill.md) | [作者配置与合法行动](spec/battle/portable-trainer-strategy.md) |
| 编写跨语言验收 | [来源、环境与未验证边界](reference/scope-and-evidence.md) | [按功能找测试](vectors/README.md) · [可移植 JSON 预期](vectors/portable.json) |

## 按领域查找

- [核心规则与存档](spec/core/README.md)
- [个体、队伍与道具](spec/creatures/README.md)
- [战斗与设施](spec/battle/README.md)
- [地图、遭遇与场地事件](spec/world/README.md)
- [交互、演出与小游戏](spec/ui/README.md)
- [内容制作与开发工具](spec/authoring/README.md)

## 选择规则

参考正文描述指定版本的可观察状态、默认值、动作次序、异常和保留项。遇到“可移植”章节，先看它给出的模式和适用前提。标为 V1-08 的章节补充原有选曲行为的验证前提。相同输入在两种模式下可以有不同的正确预期。

[术语](reference/terms.md) · [版本与兼容模式](reference/versions-and-compatibility.md) · [参考资料](reference/README.md) · [可移植场景](vectors/portable-expectations.md)
