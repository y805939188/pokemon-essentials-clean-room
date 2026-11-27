# 普通能力重算与濒死状态

**独立实现规则 · V1-04**　WP19／WP30

原版 [WP19](attributes-ability-and-stats.md) 的静态推导是最大 HP 增加时可能让 0 HP 因差额而变正。改良：普通能力重算前已濒死的成员维持 0 HP；明确具有复活效果的操作另按该效果处理。不要据此改写[成长流程](growth-learning-and-friendship.md)中其他入口或原版兼容选择。

静态验收用例见[可移植向量](../../vectors/portable.json)。对应编号为 V1-04-A。
