# 术语

| 术语 | 在规格中的含义 | 对应规则 |
| --- | --- | --- |
| 参考快照 R、发行 v21.1 | 两个分别标识的来源。涉及版本差异的行需按来源解读。 | [适用版本与兼容模式](versions-and-compatibility.md) |
| 机制世代 | 决定部分默认配置及直接消费分支的游戏规则参数。配置还可能被作者逐条覆盖。 | [配置词典](../spec/core/rule-configuration-and-data-variants.md) |
| 作者数据、PBS | 作者输入的内容及其文本形式。读取单值、登记条目、整表终检和保存是可区分的阶段。 | [作者数据生命周期](../spec/core/pbs-lifecycle.md) |
| 内容身份、形态、成员 | 物种内容标识和形态描述静态内容；具体成员还持有等级、状态、持物等个体数据。 | [内容身份](../spec/core/content-identity-and-schema.md) · [个体与物种](../spec/creatures/creature-identity-species-ownership.md) |
| 当前属性、静态属性 | 战斗中可临时变化的属性与作者内容定义的平时属性有不同的作用期。 | [内容与迁移](../spec/authoring/portable-content-identity-and-migration.md) |
| 持物来源实例 | 参与归属判定的具体一件道具。同名物品可来自两个不同来源。 | [捕获结算](../spec/battle/portable-capture-held-items.md) |
| 战后提交、回程、冷读 | 业务结果写入、玩家在目的地落位及旧事件退场、由独立读取者重新读取已保存数据，分别有各自的完成条件。 | [战后提交与存档](../spec/world/portable-defeat-return-and-saving.md) |
| 快照 | 在指定时点保存的展示值。名人堂的历史记录应能与随后变化的当前队伍分别查询。 | [名人堂](../spec/ui/portable-hall-of-fame.md) |
| 静态推导、静态向量 | 由规格给定的输入、条件、步骤及预期。每个测试编号应连同入口、适用版本及前置条件阅读。 | [测试目录](../vectors/README.md) · [可移植预期](../vectors/portable-expectations.md) |
| 未验证、未执行 | 前者标记证据尚未覆盖的条件或结果；后者记录某个观察或测试没有运行。 | [范围与证据](scope-and-evidence.md) |
