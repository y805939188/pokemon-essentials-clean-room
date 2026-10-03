# WP76 首版交付摘要（设施内容生成与模拟，F18-05）

2026-10-02；规格提取方。依据 `review/wp75-review-2026-10-02/recheck-v4/`（WP75 v4 **PASS_SCOPED，20/20 CLOSED**；WP76 执行提示与 43 份起始来源索引）。**本轮为第五批最后一包 WP76 的首版提取**，完成登记后停止送批末 review；不开始 WP77/78/79/80。

- **主稿**：[wp76-facility-content-generation-and-simulation.md](../../specs/demo/wp76-facility-content-generation-and-simulation.md) `5d243226`／36,040（311 行；磁盘程序化实测）。**入口附表**：[entry-coverage-table.md](entry-coverage-table.md) `8ad84d76`／8,317（六组 **3／2／7／6／5／6＝29 行**结构法实测）。
- **范围**：A 入口与触发（设施设置联动 `pbWriteCup`、外层调试门、生成/复用询问）；B 复用已有列表（ID 迁移、默认列表特例、写回＋反写）；C 候选个体生成（拒绝采样：物种奇偶 BST 门、性格-EV 一致、41 项道具表与专属门、三路合法招式与四支剪枝、组合约束与总威力门、IV 31/EV 均分构造）；D 队伍组建与迭代（槽位序敏感重复判定、同种 10 FIFO、抽 2 即删、更替五支、600/65/40/11 轮常量、九层分层）；E 模拟对战与评级（1% 真实无视觉／99% 估算、效果矩阵 -16/-8/0/4/12/20、Glicko-2 与胜率两式、Elo 备选仅定义）；F 训练家池与写出（200 随机训练家、类型计数缩放、位次权重分配、默认唯一化、PBS 反写与编译往返）。
- **阅读**：主域 4 份 1,346 行全文（338/359/211/438）＋交界定点 10 处（设置入口、列表查询与 PBPokemon 全文、规则 API、反写/编译、无视觉场景全文、名称生成、设置常量、Effectiveness 定位）＋PBS 数据核验（battle_facility_lists 全文、杯赛文件引用关系、demo `Data/` 存在性——**`Data/trainer_lists.dat` 不存在**，读取路径落入 rescue 空表）；WP08/WP44/WP51/WP52-A/B/C/WP54/WP55/WP57/WP72/WP73-A/WP75 已通过合同按引用继承。
- **自检**：[checks.json](checks.json)——9 组验收向量、场景 M01–M24 唯一、附表计数一致、链接解析、净化 0 命中（调用式已全部行为化改写，审计名仅作标识）、首版不伪造 diff。
- **来源身份**：[source-identities.json](source-identities.json)——全文/定点/样本/继承分开登记；开工登记基线与 WP74/WP75 通过身份复测一致；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、Git 清洁。
- **如实登记边界**：候选采样/池补充/队伍取样**无迭代上限**（严格规则可无进展，不补兜底）；重复判定的紧凑/排序结果被丢弃（槽位序敏感）；真实分支战后仅 heal＋持物还原；`cup_fancy_trainers.txt`/`cup_fancy_pkmn.txt`（非 _single）未引用；检查点在游戏根目录 `<id>.rxdata`/`<id>_teams.rxdata`。
- **保持**：WP75 20/20、WP74 18/18、WP72／WP73-A／WP73-B 的 37/37 闭环、WP61（11/11）、WP53、WP37、WP65、WP67-A/B、GR-001～016、WP23-N01 及所有旧批准保持；未创建任务／Agent、未发跨会话消息、未提交／推送；未运行生成器/对局/Monte Carlo/编译器/反序列化/参考行为模拟器。
- **状态**：**ReviewPending（A～F 具名静态范围，首版待统一 review）**——不自行 Reviewed、不宣称通过。

## 停止点

WP76 首版取证、自检与登记完成，停止送第五批批末 review；WP74/75 已通过范围保持，只核新增交界与一致性；若审查发现问题，按原编号修订并复审通过后才继续。
