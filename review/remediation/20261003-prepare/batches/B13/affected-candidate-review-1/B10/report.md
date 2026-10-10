# B13 candidate affected — B10

结论：**PASS_SCOPED**。有限接口：B010 加载后 Ice OHKO 资格、非冰专用阈值；WP43/44/46 与实际/AI分离，B018目录保护。

精确 reviewed candidate：`5845e8084ced280e51c51a4081ec8583a9c2ca39`，tree：`23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c`。正式 FIX_BASE：`8e67f780c204d593d89f364f585d2c6c2fe74631`；publication `1dc5cc80854e02965b9bb7a02c00a7c40d392f89` 仅作派发／证据载体，管理许可 `2b23c82947bcecec4ab059d63048f9b67586575b` 不替代正式基线，也不代表质量通过。

独立判定依据：

- 当前 WP43、WP44覆盖、WP46主稿及覆盖四输入在 FIX_BASE 与 candidate 全字节一致；逐有限条款对照 B13 主稿、杯赛附表及新增 Q43-Q47。
- 固定默认加载后、无额外覆盖、ohkoclause=false 的 Ice族不因目标冰类型本身拒绝；ohkoclause=true 拒绝。仍有等级、坚硬及一般目标资格；专用阈值不等于必中或必定倒下。
- 非冰使用者示意阈值30+50−50−10=20：随机19通过、20不通过，是未执行设计。原非冰−10保留；AI 自身 Ice目标拒绝及估量合同不被实际别名覆盖结论改写。
- B018 当前既有覆盖族保持，其他 owner 覆盖文件无差异；127旧目录ID仍在、9新增设计独立重算136，不把文本设计计为实测或全贡献通过。

本有限接口未发现候选引入的新缺陷；该结论不处置其他 owner 的阻塞或整个 owner 的历史质量。

当前输入的精确 commit/path/blob/SHA256、独立发现的接口和逐项结果见 [result.json](result.json)。共享身份只核验一次，见 [共享完整核验](../B02/shared-audit.json) 与 [读证记录](../B02/reading-log.json)：完整未过滤基线→候选 diff 为 4,618,756 bytes，SHA256 `5922c69e025d367e2b6fead68af159e4e70d5ff44112b2c9fcfbfc8912a9d8a6`；69路径＝11精确正式输出＋58本批新材料。11份前后身份和四原稿精确许可均独立相等，7份正式稿保持先前候选字节。232条旧接受收据、所有非11既有路径、共享他方目录行及ID/顺序/多重性保留。此项保护不是复批旧贡献。

按派发请求配置 `gpt-6.1-sol / ultra / default / Standard`；可信后端回显缺失，effective backend 保持 **UNVERIFIED**，按获批 Plan A 继续，不认证后端、无替换或额外任务。完整限制见 [配置与限制](../B02/configuration-and-limits.json)。仅静态文字及新 Git/JSON/hash 元数据核验；reference/Ruby/游戏/行为向量/历史程序执行0，新增9项与总136项设计均未运行。全部继承限制、树果条件67及具名未读不变。

本报告只签该 owner 的 candidate 有限门。FULL/actual/G/C 均不代签；全部非本地／全局义务保持OPEN。WP67-A 扩展仍由B16负责，不解除其准备限制。返修后须绑定新精确候选；actual 另行必要有限复审，不能由相同字节推定通过。
