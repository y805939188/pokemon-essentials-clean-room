# 批次B · F17-01～06 拟议矩阵增量

仅为单一整合者的逐行提案，不是全局矩阵替换文件；以下规格链接按建议合入后的主库 review 目录解析。本地新稿实际位于独立工作区同名 specs 路径。不得将冻结上下文导回主库。

| Feature ID | Domain | Feature | Short description | Classification | Reference locations | Specification status | Confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F17-01 | D17 | Duel | 玩家与事件角色的独立动作对决、临时生命和胜负返回 | UI | E32；001_Minigame_Duel.rb全文及路线／身份调用 | ReviewPending（独立并行批次B，D-A～E入口／四动作16组合／权重与特殊一次／回合终局／地图提交及异常；尚未外审／待统一合入登记）＋Inventoried（Demo事件、媒体／宿主与运行） | 中 | specs/ui/wp68-duel.md；12场景；无主动退出；同归零判负；WP77与WP78→79→80保留 |
| F17-02 | D17 | Triple Triad | 卡面／库存／选牌／翻转／结算与买卖 | Creature RPG | E32、E04；002_Minigame_TripleTriad.rb全文及库存／物种／图鉴读取 | ReviewPending（独立并行批次B，T-A～G方向与价格／仓库与取得／候选与规则／状态机／连锁与AI／转移／买卖；尚未外审／待统一合入登记）＋Inventoried（最终分布、Demo／运行与异常兼容取舍） | 中 | specs/creature-rpg/wp68-triple-triad.md；24场景；最大等级无抽牌消费、direct败局错扣具名；可选通用玩法，非未来结构 |
| F17-03 | D17 | Slot Machine | 代币准入、下注／停止、奖项、重玩与离场净额提交 | UI | E32、E13、E14；003_Minigame_SlotMachine.rb全文 | ReviewPending（独立并行批次B，S-A～F守卫／有序转轮与滑移／有效线和奖项／状态机／支付与统计／异常；尚未外审／待统一合入登记）＋Inventoried（最终收益分布、机器事件、宿主／运行） | 中 | specs/ui/wp69-slot-machine.md及wp69-slot-reels.md；16场景；支付计时／旧余额耗尽检查／重玩额外投币分列 |
| F17-04 | D17 | Voltorb Flip | 棋盘候选／校验、提示／标记、得分／级别和逐次支付 | Pokémon Rules | E32、E13；004_Minigame_VoltorbFlip.rb全文 | ReviewPending（独立并行批次B，V-A～E入口／75候选与1000次回退／翻格与标记／结束支付／踩雷夹限异常；尚未外审／待统一合入登记）＋Inventoried（最终棋盘概率、真实降级失败／宿主表现与Demo） | 中 | specs/pokemon-rules/wp69-voltorb-flip.md及wp69-voltorb-layouts.md；18场景；零余额可入，无下注；不将异常降级写成正常规则 |
| F17-05 | D17 | Lottery | 日期号码写入、公开拥有者尾号匹配、扫描及结果变量 | Pokémon Rules | E32、E13；005_Minigame_Lottery.rb全文及集合／变量消费者 | ReviewPending（独立并行批次B，L-A～E日期种子／号码转换／两遍含蛋扫描及并列／结果与变量失败／静态场景；尚未外审／待统一合入登记）＋Inventoried（开奖与兑奖事件／奖品表／日期锁，U01） | 中 | specs/pokemon-rules/wp70-lottery.md；16场景；检索不发奖、不增加领奖统计；WP77补事件 |
| F17-06 | D17 | Mining | 候选／摆放、工具／损耗、揭露与逐件领取 | UI | E32、E14；006_Minigame_Mining.rb全文及背包／物品数据 | ReviewPending（独立并行批次B，M-A～F入口／61候选与13铁形状／布局重试／工具及揭露／终局结算／失败；尚未外审／待统一合入登记）＋Inventoried（最终分布、默认不终止可达频率、Demo／宿主与运行） | 中 | specs/ui/wp70-mining.md及wp70-mining-data.md；22场景；坍塌／放弃保留已揭成果，逐件非整批原子 |

以上“静态范围”不表示独立审查通过。置信度不替代ReviewPending。F17-07／WP71不在本批，不改其原行；U01–U10以及Demo、宿主、媒体、插件和最终全局出口均保留。
