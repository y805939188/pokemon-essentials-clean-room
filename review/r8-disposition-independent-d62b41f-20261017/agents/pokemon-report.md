# pokemon-rules 固定基线独立语义复审

结论：**FAIL**。固定候选 `d62b41f4d620e50bb04c80a7505374bd284d8210`；正式子树 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。31份负责文件全部全文阅读：27正文4,919行、4静态测试目录1,144行，共526有效标题；165功能行/165生成view行全部逐项复审。每项判断见 `pokemon-results.json`，PASS仅表示该行粗标在本轮静态范围内合理，绝非Showdown已兼容或实现/验收已完成。

逐项结果：PASS 128；FAIL 37；待查 0。另有2处真实行为被概念元数据吞并，不能由现有165行通过机械计数免除。

实际模型、effort、service tier、速度及Fast没有权威执行echo，均为UNVERIFIED；本子任务独立于作者，未运行Ruby、参考游戏、Showdown、宿主、框架或业务向量。用户clean-document-revision仅作为作者正文纪律读取，没有伪称用于审计报告写作。

## 可复现问题

### POK-S01 · P2 · 核心行为被概念标题规则降为metadata

WP43明确规定未知变化效果失败/伤害效果回退、PP不退及SHADOWSHED不同绑定；WP70定义输入整数转换、低16位公开号及最低五位最长连续匹配。两个完整行为节均被section-metadata笼统关联整篇功能，且均不在任何feature的source.line_ranges内。标题全集映射通过仍不能证明行为去向完整。

功能：现有功能选择器外的源行为；见相关文档元数据映射。

- `deliverables/final-specification-set/pokemon-rules/wp43-types-accuracy-and-damage.md:L29–L36`
- `deliverables/final-specification-set/pokemon-rules/wp70-lottery.md:L19–L26`

必要修正：将这两节登记为真实行为单元或精确并入同验收边界的既有功能行，保留原有ID；给出其去向/归属/问题并更新源选择器和view，禁止改正文或仅改metadata_reason让脚本通过。

### POK-S02 · P2 · Shadow跨战斗/成长/主动道具界面未拆协作

当前四行均框架实现、伙伴框架/MZ、无Showdown和相应原型；正文却含入场/Call/战后量表快照、战斗经验EV暂存、战斗香资格复检退款、持久招式改变不重建场上副本。486的Hyper协作不覆盖这些不同源区间。

功能：FR-000484, FR-000485, FR-000487, FR-000488

- `deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md:L32–L59`
- `deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md:L74–L129`
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md:L175–L218`

必要修正：保留框架持久字段与净化业务，按真实交界拆出或改为协作候选，绑定PROTO-IN-BATTLE-GROWTH/PROTO-BATTLE-ITEM及捕获后快照问题；补WP28/WP40等必要消费者依赖；未知仍待原型，不要求先跑原型才能接受粗标。

### POK-S03 · P2 · 漫游复用个体与逃跑结果写回被框架单方吞并

同一持久个体跨战复用，HP/PP/状态/持物取真实终局结果，含自然回复、对方不还原、总是逃跑、决定0–5与外层布尔/终结记录不同。该行仅框架、无Showdown、无PROTO-ESCAPE，依赖也无WP41。

功能：FR-000519

- `deliverables/final-specification-set/pokemon-rules/wp37-roaming-and-poke-radar.md:L67–L80`
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md:L104–L110`

必要修正：拆出开战/持续个体映射、战斗结果/逃跑/正常及异常交接的协作候选，关联WP41/42及逃跑原型，明确框架持久状态与Showdown战斗输出的所有者。

### POK-S04 · P2 · 持久异常与持物提交没有明确两端责任

Showdown候选适合临时战斗计算，但这些行实际约束持久异常计数、C/I/R/P/Belch写穿与还原记录、LEPPA先持久槽后异身份战斗槽强写、被动/背包两类资源、已消费负选择和世界持物输入。仅列伙伴框架而不说明状态/资源归属无法表达边界；571还把578已列协作的Exp/EV两族整体写成Showdown。

功能：FR-000543, FR-000571, FR-000574, FR-000576, FR-000577, FR-000579

- `deliverables/final-specification-set/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md:L13–L28`
- `deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md:L13–L32`
- `deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md:L72–L133`
- `deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md:L30–L31`
- `deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md:L153–L170`

必要修正：保留纯计算/资格的Showdown候选；对持久写穿、物品/PP两端同步、成长和世界结果拆分或明确协作职责，补WP20/28/42等依赖及对应行为问题。被动持物不扣背包应与主动道具原型分别表述。

### POK-S05 · P2 · 同节UI/资源/宿主时序未按独立验收边界拆分

这些段落实际包含按键仲裁、编辑/搜索/标记、取消、资源请求/回退、精确等待、地图场景门/转移、暂停微更新、普通退出前保存或重复释放。不能用“本篇持久领域状态”这一重复依据将整节留框架；已有462/610等MZ拆分说明清单允许且需要这种不同验收边界。

功能：FR-000465, FR-000489, FR-000505, FR-000520, FR-000522, FR-000580, FR-000582, FR-000585, FR-000590, FR-000591, FR-000596, FR-000598, FR-000600, FR-000601, FR-000608, FR-000611

- `deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md:L250–L278`
- `deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md:L130–L185`
- `deliverables/final-specification-set/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md:L98–L109`
- `deliverables/final-specification-set/pokemon-rules/wp37-roaming-and-poke-radar.md:L81–L96`
- `deliverables/final-specification-set/pokemon-rules/wp37-roaming-and-poke-radar.md:L117–L158`
- `deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md:L23–L48`
- `deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md:L114–L148`
- `deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md:L214–L257`
- `deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md:L65–L135`
- `deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md:L22–L57`
- `deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md:L71–L94`
- `deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md:L120–L173`
- `deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md:L147–L178`
- `deliverables/final-specification-set/pokemon-rules/wp69-voltorb-flip.md:L47–L60`

必要修正：只在真实跨去向/验收界面处拆子节（无需逐句编号）：框架保留领域状态/预算/规则，MZ明确输入、表现、资源和生命周期；对调试子节关联DEC-SPECIAL-AND-HOST-SCOPE。父行line_ranges排除新子行，原ID保留。

### POK-S06 · P2 · 进化演出整节承包了领域提交

492把§5全部列MZ。§5.1确为动画/取消，但§5.2–5.4还规定统计、消耗持物、额外个体克隆/入队/扣球、物种/HP重算、图鉴及学招。MZ/框架伙伴列与一句联调依据没有分出独立领域验收。

功能：FR-000492

- `deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md:L156–L192`

必要修正：至少按§5.1与§5.2–5.4实际责任拆分或精确描述领域提交与演出交接，保留取消与消息等待前缀顺序；不把全部持久行为归表现实现。

### POK-S07 · P3 · 纯证据/向量/范围段被制造为实现功能

这些源节是来源、审计方法、覆盖范围、固定测试向量或冻结依赖/开放问题，没有独立待实现能力。它们却被赋destination/stage/implementation，而实际行为“未知效果回退/彩票匹配”反被概念关键词降级，语义口径不一致。

功能：FR-000478, FR-000480, FR-000482, FR-000500, FR-000539, FR-000553, FR-000573, FR-000618

- `deliverables/final-specification-set/pokemon-rules/wp22-transformation-data.md:L75–L77`
- `deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md:L37–L60`
- `deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md:L239–L241`
- `deliverables/final-specification-set/pokemon-rules/wp32-context-inputs-and-scenarios.md:L124–L137`
- `deliverables/final-specification-set/pokemon-rules/wp44-effect-coverage.md:L5–L10`
- `deliverables/final-specification-set/pokemon-rules/wp46-damage-healing-coverage.md:L83–L86`
- `deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md:L69–L71`
- `deliverables/final-specification-set/pokemon-rules/wp70-lottery.md:L54–L58`

必要修正：保留这些已登记稳定ID的历史导航/处置，不删除或重编号来通过；将当前记录按合同标明为元数据/验收来源并精确关联现有行为。若schema不能表达该身份演进，先增明确迁移/继承设计并验证。

### POK-S08 · P3 · 作者内容缺省/校验与战斗配置被同标Showdown

该节既有战斗独立开关，又有Type/Move作者输入缺省、Category×Power编译校验、本地化Name/Description消费和WP03/04/08的内容约束；目前通篇主要战斗计算的模板依据无法解释这些作者内容由谁拥有。

功能：FR-000537

- `deliverables/final-specification-set/pokemon-rules/wp43-types-accuracy-and-damage.md:L159–L166`

必要修正：按内容作者/编译/本地化与战斗规则输入边界拆分或明确框架内容所有权及Showdown映射，依赖关联WP03/04/08，保留数据一致不等于行为覆盖的限定。

## 机械核对与阅读证明

独立脚本 `pokemon-static-audit.py` 只读固定Git对象/Markdown/JSON；正文/交付/候选逐字节相同；31文件SHA/blob、526标题level/title/line/anchor/hash、165功能单元SHA与选择器、165view行集合/主要字段投影及相关批次保守写集绑定均无机械差异。原始stdout/exit见 `pokemon-command-evidence.json`；细证见 `pokemon-static-evidence.json`。未导入作者routing.py代替独立解析。

生成view全部行通过字段投影核对；重复rationale/questions/state按完整去重字段读取，来源fact_excerpt由完整正文阅读验证，未将工具成功当语义PASS。全部源正文分块输出；工具出现的WP21、WP22、WP23、WP34截断处均随后补读。四catalog全部1–EOF阅读，无未读段。

| 文件 | 全文已读行 | 标题 | 功能 | SHA256 |
| --- | ---: | ---: | ---: | --- |
| wp19-attributes-ability-and-stats.md | 1–268 | 22 | 7 | `5c1e9dd1fec916f6551f6f92880c372fff9161faaee67a0ea71a49cfb73abcf3` |
| wp21-dynamic-forms-and-display.md | 1–327 | 24 | 8 | `80246da274078a7c494dac61d0353e4429fb27d1f106947dc063f47e7c0abc81` |
| wp22-mega-and-primal-reversion.md | 1–114 | 14 | 6 | `33bf91ba9936aeb7f7fd94087df3796f883b2b75f94eb4994b7b13e22305b8e3` |
| wp22-transformation-data.md | 1–77 | 5 | 4 | `022525f7e3899f60b9523147f68ca8d0d06828d55f8d80dc222490dd7a02e20d` |
| wp23-shadow-data-and-vectors.md | 1–241 | 7 | 4 | `1edef789d2540ef727b415e5475bb1642d8b0df86af4d6df3f62be5e9e6bec00` |
| wp23-shadow-hyper-and-purification.md | 1–199 | 17 | 7 | `f5f794b974f4d5c8ce176eda90f9e11fe4d159000800011de0707ccf74ba8fab` |
| wp31-basic-evolution.md | 1–268 | 28 | 7 | `fded72abb92395e5584c237e7f8fbe30c7c885490fb70ec5fcbc12905cbe4592` |
| wp32-context-inputs-and-scenarios.md | 1–140 | 6 | 4 | `3da7f524023bd749a0c515b03e96134a9635e911c7f6c692f7e9a415dce3663b` |
| wp32-contextual-trade-and-post-battle-evolution.md | 1–142 | 15 | 7 | `4ee97f16827c2615e63506f0ca4a231f6b9f4b6fdb09e335c8add7792984f384` |
| wp34-inheritance-and-offspring.md | 1–233 | 30 | 9 | `9145f6fbae54f56416d6b7a39979769ca812dac18cf867e46c07b11cf591d41c` |
| wp37-roaming-and-poke-radar.md | 1–191 | 28 | 8 | `626b38fdb248d3b6a235eae5fb8ea75772e5e4ef19f89129c0a599ffdd756cf9` |
| wp38-capture-and-receiving.md | 1–146 | 12 | 7 | `37bcd3a5e876b6a0b6932265f90d3893e5d8e7f3f574abb0db2078998599b16e` |
| wp43-types-accuracy-and-damage.md | 1–190 | 23 | 7 | `6a09dfad69faa5c0c35991e9fa4eb83646b6f2162427e5bcd3df09c55fded6d3` |
| wp44-effect-coverage.md | 1–188 | 10 | 4 | `c1384960e2446795c42b911cdc2b66aa9ad641c5774b3f90861e33b33854f381` |
| wp44-statuses-stat-stages-and-immunities.md | 1–203 | 19 | 8 | `e144ad75bab96647c12220d7f7e137d534277c169f6ca64d8c6bd06044268943` |
| wp46-damage-healing-coverage.md | 1–89 | 19 | 4 | `3ec4fde8b170f3d40f4b0a0cbfd060198ff4adcc8b25a6b08a00496042723fcb` |
| wp46-damage-multihit-and-healing.md | 1–303 | 28 | 7 | `7e65ae4945ab1cd101b357f3edcadbff2cbaa94630c609244519a688901e1841` |
| wp48-ability-calculation-modifiers.md | 1–238 | 17 | 9 | `19c5799a7949013b85e2c0937860596db6eed875470ac7a12c53ddc4e5268e07` |
| wp50-held-item-effect-coverage.md | 1–71 | 4 | 3 | `b17d23945fe45a7534d09c38e5ca0a1046fede803b014dc24d4652c5e7046628` |
| wp50-held-item-triggers-and-consumption.md | 1–181 | 15 | 6 | `e1038d0eeb359406e8334a4ef51226a1d2625e03776c0d57ccf201d9d5bba8b9` |
| wp53-safari-and-bug-catching-contest.md | 1–288 | 43 | 8 | `1a9c9581d7b91bf5e4dd5474b9e2f4fef4115e795d7122663eb743e55bfaa999` |
| wp60-berry-plants.md | 1–199 | 25 | 8 | `2a742d49f5eff88b0905976cea04eef9c361424906f2a8ed45e00d42906e323c` |
| wp61-field-passive-effects-and-blackout.md | 1–203 | 30 | 8 | `5a1cb7cf45fb6b8b77112e0bc95da9196758cd488a3913bc99f91568ef8b179d` |
| wp62-pokedex-records-regions-and-content.md | 1–197 | 19 | 5 | `68bd52e6720e5549ccb2a55375946bfbc4874ccb3f20e1eb06ccfe761685ede8` |
| wp69-voltorb-flip.md | 1–80 | 10 | 5 | `7fef63bff5ea6b2764636a2bf0319c3baa0df788c15ee2df929e5abb8d7e74e8` |
| wp69-voltorb-layouts.md | 1–85 | 1 | 1 | `23c29f2d8bfa099f1d101bf989f157a309167c3a788b02d74ea7c64a0125513a` |
| wp70-lottery.md | 1–58 | 8 | 4 | `eddd6303b5c298b2f6bf011b647e35e4bf7fe83c274577f21710eef7935e0552` |
| pokemon-rules-wp19-21-22-23-34.md | 1–342 | 14 | 0 | `3efe98849e1ece72cc3e20564fd57d6cb3ba038d8e5cd8acc05310b062f8477a` |
| pokemon-rules-wp31-32-37-38.md | 1–165 | 5 | 0 | `696441752208d844f4a488b120a3a231562a84073aaef54f7b91c2a2f81b13fe` |
| pokemon-rules-wp43-44-46-48-50.md | 1–320 | 12 | 0 | `7dfc5c82ab9029a8e6a35033c393b6f26ae151fe91a2d39582e3a5acf4ea70eb` |
| pokemon-rules-wp53-60-61-62-69-70.md | 1–317 | 16 | 0 | `61bd579cfde9fe9d5dc4e24c4a0fde9631ef0d224715fb1e86f6a0c51cf5242c` |

## 归属、状态及后续边界

捕获FR-000525–531正确保留PROTO-CAPTURE，529把战后接收归框架仍保留交接门；战斗内能力重算/HP刷新457–458、形态调用464、Mega/Primal469–474、战后成就502–504与特殊模式581/583都允许在未知原型条件下作为协作粗标。纯战斗数学/临时状态不能因本文指出持久交界就一概改成框架。

本域165行均去向待验证、阶段待定、未实现、未验收、排除0；没有来源引用升级为Showdown兼容证据。固定源身份、current适用快照分开，原ID未被本复审改动。R8-U06绑定WP19与对应catalog；R8-U03绑定WP60；R8-U05绑定WP61；正文23条功能行的整篇保守绑定及待整改状态正确。U07是历史overlay，未把它虚构成此域正式正文写集。精确章节整改影响仍须接收上游新候选后差分。

所有问题仅要求修订规划清单/映射/去向边界，不要求修改正式正文、修参考或先运行原型。来源事实、异常前缀、静态向量、未选范围与历史身份均须保留。最终必须以协调任务提供的正式整改精确commit重新校准并独立验收；本报告不能提前宣称第八轮最终完成。
