<!-- U06-E043; target/location and exact B5 anchor in fragment-manifest.json -->
| TT-26 | 正常合法对局、openhand 开、玩家后手；对手首张已合法提交／删除，玩家 5／对手 4；ACTION→UP→DOWN→BACK | 初始高亮零基 0→零基 4 无牌高亮→0→玩家选牌；牌数／棋盘保持，不提交不存在的牌。邻近玩家先手且仍 5／5 时位置 4 是真实第 5 张；openhand 关闭时 ACTION 不进入查看 |

### 局部消息/翻牌阶段对照

DERIVED_VECTOR / NOT_EXECUTED；与UI目录及主规格同一静态期望，尚未执行。

| 设计 | 前提/输入 | 预期 |
| --- | --- | --- |
| U06-M11-005-TT | Triad合法通知与合法等待确认消息各独立，正常单调钟/更新、无外部改写；普通通知1.4时USE/BACK、随后到≥1.5；另全显结果消息BACK/USE | 通知不提前跳，首到期更新返回；结果BACK不退出/USE退出。结果提示前后永久卡转移沿原规则 |
