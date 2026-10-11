# M04个体规则交界审查

独立root；固定身份见baseline/各finding/矩阵。源与静态场景执行0。

| 链 | 正常 | 失败/边界 | 判定 |
|---|---|---|---|
| 内容→创建→形态→统计/图鉴 | 直接记录默认与PBS验证分开；性格能力重算先缓存；形态0复检可再抽，0仍提交 | withMoves=false不挡form回调，只挡moves；recheck关闭或非零初形态不调用；图鉴读取可先填gender/shiny | SUPPORTED_STATIC；A022旧FINAL邻接误句不复用 |
| IV/EV/Nature→能力→HP | 先EV整除4再等级再Nature；HP1特例；HP差值保持伤量 | 减上限存活最低1，濒死增上限会复活；存储255设施例外不被计算/禁用正规化 | SUPPORTED_STATIC；设施全创建由M09 |
| 形态提交→学习/UI→字段 | 先form/cache，再handler，再stats/dex；直改保槽/up并钳PP | ROTOM同值删空、KYUREM边压缩跳项、学习取消不回滚form；解析缺招先失败 | SUPPORTED_STATIC；M10真实UI另核 |
| 持物/捕获→伙伴/队伍→终局 | I为可更新记录，部分消耗写穿，无伙伴同步可保持正确 | 实际伙伴参与集合与满队移位player列表分离时旧送盒成员被写后继物；M04不能用普通消耗单签全捕获 | PARTIAL待M05/M06/M07/M08 root整合，原B013范围保留 |
| Shadow→步/战斗→Hyper/招式 | Nature储存表、256步和chamber每步不同；有效状态与存储flag分开 | G0可写Hyper提示但query假；香缺Flags常规拒，笛成功消费却净化早退；已有准确合同无重复新ID | SUPPORTED_STATIC局部；M06/M07/M11完整消费者 |
| 净化→EV/EXP→等级窗口→接收 | S0同等级可越窗口，普通Math F/T与九组14门可计算 | 跨级chamber屏无update首窗口失败，先S/V/Shadow/level已提交；遗迹石有空callback；到达存放后双满仍清源 | SUPPORTED_STATIC源链；完整储存选择UI及媒体M10 |
| 编号→精灵→帧 | 非蛋有效资源copy后逐帧施四斑点；正背皆可，纯species入口不同 | 静态位置/形状/2×2采样/两组RGB缺最终合同；越界和真实位图未知 | PARTIAL，GR3-M04-001；M03/M10交界 |

缎带缺持有删除、TIMEFLUTE、零招模型、Primal还原术语等定点候选已与完整允许集核对；已有准确条款时不再新增finding。未用getter/任意插件/语义外输入不被虚构成当前默认能力通过。
