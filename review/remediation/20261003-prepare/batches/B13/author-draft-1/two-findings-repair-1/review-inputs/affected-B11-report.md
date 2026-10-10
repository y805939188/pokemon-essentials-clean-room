# B13 candidate affected — B11

结论：**REQUEST_CHANGES**。有限接口：WP48/WP50覆盖与 shared keys／SoulDew／SkillSwap；独立发现 WP47-B、WP49、WP50主稿的退出入口到 WP58 记录接口。

精确 reviewed candidate：`5845e8084ced280e51c51a4081ec8583a9c2ca39`，tree：`23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c`。正式 FIX_BASE：`8e67f780c204d593d89f364f585d2c6c2fe74631`；publication `1dc5cc80854e02965b9bb7a02c00a7c40d392f89` 仅作派发／证据载体，管理许可 `2b23c82947bcecec4ab059d63048f9b67586575b` 不替代正式基线，也不代表质量通过。

独立判定依据：

- 键的 setting/consumer 分离通过：11真实设置键＋3仅消费者键；sleep不等于sleepclause；SkillSwap 用共享真实目标门；旧 SoulDew 1.5禁门与现代1.2和报名禁持物分开。
- 当前 WP48 与 WP50 覆盖文件字节不变，148/196 身份统计未改；RC24→26及总127→136是 B13 新增未执行设计，没有删除 B11 的行或把搜索计数当调用闭包。
- WP49 属 B11（当前 ownership 导航已核对）。WP49 §3 最终扫描及 WP50 OnStatLoss/EJECTPACK 非EOR消费者表明入场选择不同于“攻击阶段”独立行。WP47-B 攻击消费者不能代替入场消费者。B13-AFFECTED-F1 阻塞本有限接口。

具体阻塞与具名静态反例见 [B029 入场时点问题](../B11/finding-B029-entry-timing.json)。最小返修是 WP58 正文与原稿 §5.2、一个未执行入场对照和必要导航／身份后继；原稿新字节须先获精确范围后继。它沿用 B029，canonical 增量0，B030计数0。

当前输入的精确 commit/path/blob/SHA256、独立发现的接口和逐项结果见 [result.json](result.json)。共享身份只核验一次，见 [共享完整核验](../B02/shared-audit.json) 与 [读证记录](../B02/reading-log.json)：完整未过滤基线→候选 diff 为 4,618,756 bytes，SHA256 `5922c69e025d367e2b6fead68af159e4e70d5ff44112b2c9fcfbfc8912a9d8a6`；69路径＝11精确正式输出＋58本批新材料。11份前后身份和四原稿精确许可均独立相等，7份正式稿保持先前候选字节。232条旧接受收据、所有非11既有路径、共享他方目录行及ID/顺序/多重性保留。此项保护不是复批旧贡献。

按派发请求配置 `gpt-6.1-sol / ultra / default / Standard`；可信后端回显缺失，effective backend 保持 **UNVERIFIED**，按获批 Plan A 继续，不认证后端、无替换或额外任务。完整限制见 [配置与限制](../B02/configuration-and-limits.json)。仅静态文字及新 Git/JSON/hash 元数据核验；reference/Ruby/游戏/行为向量/历史程序执行0，新增9项与总136项设计均未运行。全部继承限制、树果条件67及具名未读不变。

本报告只签该 owner 的 candidate 有限门。FULL/actual/G/C 均不代签；全部非本地／全局义务保持OPEN。WP67-A 扩展仍由B16负责，不解除其准备限制。返修后须绑定新精确候选；actual 另行必要有限复审，不能由相同字节推定通过。
