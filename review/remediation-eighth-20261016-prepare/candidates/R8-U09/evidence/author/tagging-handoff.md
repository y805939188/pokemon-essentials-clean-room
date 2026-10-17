# 给打标任务的有限变更清单

本任务未进行全面打标。以下仅提供实际修改章节/锚点和行为边界；已有标签、全局状态与覆盖由打标任务独立处理。行号按本候选整文件，整合后可移动。锚点按标题slug推导；发布后的渲染锚点由打标任务核对。

## deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md

- L313–339；章节 `6.2 蛋群的固定作者身份目录`；锚点 `#62-蛋群的固定作者身份目录`。
- L383–383；章节 `7. 字段责任目录（字段组粒度）`；锚点 `#7-字段责任目录字段组粒度`。
- 对应问题：GR8-PBS-EGGGROUP-DOMAIN-001。行为/验证变化：WP03新增唯一15项精确作者身份目录与严格接受/拒绝、默认/克隆和前缀边界；WP18引用该目录。

## deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md

- L56–58；章节 `3.1 物种记录的查找身份`；锚点 `#31-物种记录的查找身份`。
- 对应问题：GR8-PBS-EGGGROUP-DOMAIN-001。行为/验证变化：WP03新增唯一15项精确作者身份目录与严格接受/拒绝、默认/克隆和前缀边界；WP18引用该目录。

## deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md

- L127–127；章节 `7. 调试 authoring（调试菜单）`；锚点 `#7-调试-authoring调试菜单`。
- L127–127；章节 `7. 调试 authoring（调试菜单）`；锚点 `#7-调试-authoring调试菜单`。
- L128–128；章节 `7. 调试 authoring（调试菜单）`；锚点 `#7-调试-authoring调试菜单`。
- 对应问题：GR8-CRE-MG-NAME-CANCEL-001。行为/验证变化：WP64区分名称空值停止与ESCAPE返回原名成功；MG-32明确删空+RETURN+Stop及原非空名ESCAPE邻接对照，保获得地先写前缀。

## deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md

- L127–127；章节 `MG：邮件与神秘礼物（MG-01～MG-32）`；锚点 `#mg邮件与神秘礼物mg-01mg-32`。
- 对应问题：GR8-CRE-MG-NAME-CANCEL-001。行为/验证变化：WP64区分名称空值停止与ESCAPE返回原名成功；MG-32明确删空+RETURN+Stop及原非空名ESCAPE邻接对照，保获得地先写前缀。

## deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md

- L145–145；章节 `5.2 页面内容合同（择要）`；锚点 `#52-页面内容合同择要`。
- 对应问题：GR8-UI-003。行为/验证变化：明确非蛋INFO的Shadow仍有底部经验条，避免把心量数值区替换误解为删除经验条；单句低风险解释收益。

## deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md

- L158–158；章节 `8.2 异色重掷（Masuda＋闪耀护符；世代 ≥8 为 6 次）`；锚点 `#82-异色重掷masuda闪耀护符世代-8-为-6-次`。
- 对应问题：GR8-EXT-CD-004。行为/验证变化：BR23才承载末次换号后Owner变化；一个编号修正直接改善既有回归定位，不改算法。

## deliverables/final-specification-set/creature-rpg/wp26-acquisition-gifts-and-script-trade.md

- L138–138；章节 `5. 交界登记（消费者核对，不重复其主规则）`；锚点 `#5-交界登记消费者核对不重复其主规则`。
- 对应问题：GR8-EXT-CD-003。行为/验证变化：将空存储归于录像记录战斗，避免独立实现为回放添加错误空操作或隔离保证；仅交界表一行。

## deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md

- L247–247；章节 `9. 默认行为与配置变体`；锚点 `#9-默认行为与配置变体`。
- L266–266；章节 `12. 未决与未验证`；锚点 `#12-未决与未验证`。
- 对应问题：GR8-CRE-WP31-UNKNOWN-001。行为/验证变化：区分未知作者方法拒绝与绕过编译后到达运行查找的错误，复用已有通用枚举合同；仅两处未决资格。

## deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md

- L228–228；章节 `3.2 招式与物品`；锚点 `#32-招式与物品`。
- 对应问题：GR8-PBS-SHADOW-TYPE-LEGACY-001。行为/验证变化：给出原样本旧式特殊类别及逐招开关对照，避免省略false被误套原SHADOW；不改变默认启用范围。

跨文件影响：WP03唯一15项目录由WP18引用；WP33/WP34正确繁殖角色不改。WP64命名输入与MG-32联动，WP17保持只读；MG-25/29/30/31原行保持，MG总数32、原ID及其它EG/EN/FC/TT逐字保留。UI66A仅INFO底部经验条；WP34只BR24→BR23导航；WP26只记录/回放归属；WP31只两段资格；Shadow附录只原类型分类对照。无新增正式测试ID，无框架/源码变更。

不把上述修改标为执行通过；标签如需区分，应保留SOURCE_STATIC/DERIVED_VECTOR/NOT_EXECUTED。历史UI003 alias为R6-UI-PARTY-003（经GR7-M13-002），不能新增历史根。其它批次、独立视觉policy及已有接受/关闭资格不重标。
