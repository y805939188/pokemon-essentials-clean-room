# 可移植规则的静态验收

本规格定义独立实现可采用的行为与验收条件。采用方应标明所用规格版本及所采用的规则。若目标是复现 Pokémon Essentials v21.1，仍按冻结的原版规格判定；本规格不覆盖原版事实。

下表列出每组输入、步骤与预期所在的规则。全部 38 条可从同一个 [JSON 文件](portable.json) 按编号读取。

| 编号 | 规则 | 预期数 | 性质 |
| --- | --- | ---: | --- |
| V1-01 | [道具预留、消费与退还](../spec/battle/portable-item-reservation.md) | 3 | 独立实现规则 |
| V1-02 | [捕获结算与持物归属](../spec/battle/portable-capture-held-items.md) | 4 | 独立实现规则 |
| V1-03 | [战后提交、回程与存档](../spec/world/portable-defeat-return-and-saving.md) | 5 | 独立实现规则 |
| V1-04 | [普通能力重算与濒死状态](../spec/creatures/portable-fainted-stat-recalculation.md) | 1 | 独立实现规则 |
| V1-05 | [主动 HP 道具的资格与效果](../spec/creatures/portable-active-hp-items.md) | 2 | 独立实现规则 |
| V1-06 | [作者内容身份、属性与旧档迁移](../spec/authoring/portable-content-identity-and-migration.md) | 4 | 独立实现规则 |
| V1-07 | [语言切换与事件输入](../spec/ui/portable-language-and-event-input.md) | 3 | 独立实现规则 |
| V1-08 | [选曲的逻辑身份与来源](../spec/world/portable-music-selection.md) | 4 | 原版规则的验证补充 |
| V1-09 | [名人堂登记、快照与浏览](../spec/ui/portable-hall-of-fame.md) | 3 | 独立实现规则 |
| V1-10 | [多属性 AI 基础倍率](../spec/battle/portable-ai-type-effectiveness.md) | 5 | 独立实现规则 |
| V1-11 | [运行能力与诊断分级](../spec/core/portable-runtime-capabilities-and-diagnostics.md) | 4 | 独立实现规则 |

## 使用条件

每个变体独立使用给定初始状态，只有步骤明示时才沿用上一阶段。实例、地图和文档字节标记均为抽象夹具身份。每项预期的初始条件、步骤和结果必须一起使用。

上述 38 条均为静态预期，运行状态为 `NOT_RUN`。其他实现、宿主或平台需自行执行相应验收。

双打、超级进化、长尾持物组合、完整 Demo、完整媒体播放、玩家安装包与真实系统兼容性不从上述结果外推。走路缓存、打包分块、宿主接口名、目录布局、签名配置、性能采样留在对应实现／分发记录。原版进化整数 PBS 参数已另有修订，本补充不重复修改。

## 独立框架的功能用例

下表按功能列出 8 组、101 条独立框架用例。各例的 `given` 描述起始条件，`when` 给出操作，`then` 给出可观察的结果。它们与上表 V1 系列分别编号，均为静态预期。[按编号读取功能用例](portable-framework-cases.json)

| 用例前缀 | 功能 | 检查重点 |
| --- | --- | --- |
| FRIENDSHIP | [旧档友好度迁移](../spec/core/portable-friendship-save-migration.md) | 明确选槽、预览与确认，限定字段的精确替换，以及写入不确定时的恢复 |
| OWNER | [操作归属](../spec/core/portable-operation-ownership.md) | 浏览、持有成员及子操作分别怎样影响保存和遭遇；旧操作能否影响新时间线 |
| SETTLEMENT | [正式战果授权](../spec/core/portable-operation-ownership.md) | 当前获准的生产者与本场结果、内容和代次的绑定，以及低阶能力的边界 |
| GRANT | [一次性奖励](../spec/creatures/portable-one-time-grants.md) | 接收模板、容量、奖励与领取标记的共同提交、重试与冷读 |
| INSTALL | [作者内容与安装](../spec/authoring/portable-content-identity-and-migration.md) | 独立再生成两份完整产物、目标占用、正式内容只读 |
| WORLD | [世界通知与完成步](../spec/world/portable-world-notice-and-movement.md) | 失败通知、到达派发、两类随机抽取及失效的续接 |
| MANUAL | [手动存档](../spec/ui/portable-manual-save.md) | 空槽变为占用时重新询问、明确选择的手动槽及写入边界 |
| STRATEGY | [可选训练家策略](../spec/battle/portable-trainer-strategy.md) | 记录、类型及缺省的优先级；合法候选、拒绝与重试 |
