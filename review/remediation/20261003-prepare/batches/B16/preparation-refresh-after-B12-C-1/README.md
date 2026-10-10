# B16 preparation refresh after B12-C

本轮仅完成 B12-C 后的有界只读 delta。正式/原稿/候选/公共登记写入为0，独立复审、G、C和关闭为0。原有40个准备文件按精确身份复用，不导入重写、不执行旧prepare/check/inspect/proposal程序，也不再次运行原稿补丁dry-check。

正式输入为 `8e67f780c204d593d89f364f585d2c6c2fe74631`，tree `ae2f491294eb4f97be6b75f75706c16279f9bf46`。管理包 `e8caada4ab919e48e3dc817f0638ce595fde449c` 经 `git show` 读取，是管理后继，不是正式输入。旧准备固定为 `b48e919cce08058bcd29453232d4eb55aa9e9563`；它仍使用当时的B15-C身份，不伪装成最新完整作者输入。

本轮分支从精确B12-C建立：`codex/cloud-dot-B16-preparation-refresh-1-20261010`。只写本目录。配置请求仍为gpt-6.1-sol/xhigh/default(Standard)，effective **UNVERIFIED**；无模型替换、回参/额度审计或子任务。

| 记录 | 结果与边界 |
| --- | --- |
| [refresh-manifest.json](refresh-manifest.json) | 五个变化输入精确before/current身份与hunk，69个未变输入、旧40文件、六正式输入和五原稿复用；24/20控制与21未批准原稿建议的精确出处 |
| [changed-inputs.diff](changed-inputs.diff) | 五个输入的完整差异流，仅省空白上下文（zero-context），是阅读证据，不是应用补丁或执行向量 |
| [input-delta-analysis.json](input-delta-analysis.json) | 逐变化文件的含义、当前caller边界、B16旧证据及原稿提案影响；不代签affected复审 |
| [accepted-interface-delta.json](accepted-interface-delta.json) | B12新接受限定记录与共有003；沿用旧11个影响导航，新包加B12和B01当前reader导航，共13；不是13批强制全量复审 |
| [control-field-delta.json](control-field-delta.json) | 新包12项缺effective汇总键，但每个值完整存在于当前root；保留旧字段精确绑定，不降低前提/最低验收 |
| [B13-sensitive-inputs.json](B13-sensitive-inputs.json) | B13四条正向、两条反向输入及共有003的具体敏感性和then-latest C释放条件 |
| [verification.json](verification.json) | 作者私有Git/JSON/hash/text核验，零旧程序/来源/行为执行；没有candidate/actual/正式接受结论 |
| [delta-bookkeeping.py](delta-bookkeeping.py) | 本轮新增有限登记工具，仅Git/JSON/hash/text，未导入或执行旧准备程序 |

五个变化输入是WP52-A覆盖数据、WP52-B效果覆盖、WP52-B场地伤害治疗目标评价、WP52-C道具调用控制评价，以及Pokémon规则测试目录。四份WP52固定最终评分身份、复制缺源默认、调用阶段、机制世代、计数和PainSplit职责交接；不能将AI预测/候选评分当成UI选择资格或实际状态写入。测试目录仅追加SF35，所有旧行内容、顺序和重数保持：缩队为一员仍有伙伴时可先走普通双敌/2v2，不能单靠队伍人数推大会接管、Ball菜单或预算消费。

WP65的Save/Safari退出/捕虫退出集合100/010/001/011、WP66A的普通资格与规则多选、nil取消、部分写入和入口差别保持。旧24贡献/20主责分析、来源读取范围及未执行静态设计继续精确复用；B12 scoped PASS只接受B12局部，不替B16/B21完成最低验收。B15的A055/A056/C122依赖结果与仍需B16 UI的工作继续保留。

管理字段差异涉及A058、C114、C115、C117、C118、C120、C121、C122、C123、C124、C125、C126：新包仅省去旧`effective_case_constraints`汇总键。12项的每个前提、行为、反例、最低修改和recheck均逐值与当前root裁决精确相同；其余当前字段和全部原始/批准绑定未变。这里保留旧汇总字段身份与当前root定位，交父任务在下一冻结包恢复汇总键或显式保留旧字段引用；不改冻结包、不增加质量门、不声称存在新行为裁决。

21项原稿建议仍未获精确scope amendment，五原稿before与六未来B16正式输入仍与B15-C同blob。保留原fullpatch/proposed-after身份，不应用、不叠加逐ID补丁，也不因byte相同转为批准。

当前完整作者仍HELD，敏感清单如下；四条正向输入在本轮B12-C仍未变。

| B13写／B16读 | 待B13-C后仅核真实变化 |
| --- | --- |
| WP54 entry eligibility | 空数组提交与nil取消、资格/最少人数、失败阶段与WP66A选择器调用 |
| WP56 Palace/Arena | 补位、状态保留/重置、替补入口攻击记录与UI选择结果区别 |
| WP58 recording/playback | 按位置EXP/物品恢复及异常，索引/身份/返回值和后续恢复次序 |
| creature-rpg测试目录 | 旧行/决定性输入、遭遇和设施边界；其他owner的C003扩展不转给B16 |

B13反向读取B16未来会写的WP65标题/载入/选项/暂停/PC与WP66A队伍/概要，共有qualified003的主责仍B21。B030保持非必修、不加入范围。B13精确candidate/必要affected/G/actual/C普通发布读回后，由父任务在then-latest接受C/tree重冻结真实变化输入与新接受接口，并明确释放完整作者。本轮即便收到B13-C也不自动转完整作者。

U01–U10/G01–G12/AX01–AX20、未读binary/素材/宿主/插件/动态可达性、条件树果WP67与非局部/真实Demo边界全部保留。参考commit/tree未变，本轮新参考语义范围为0；参考/游戏/Ruby/编译/转换/生成/反序列化/行为模拟、runtime观察与Demo证明均为0。规范保持required OPEN229/CLOSED0。后续完整B16仍须独立ultra FULL24/20及必要affected candidate，sole G后独立FULL/affected actual读取两条未过滤流，再sole C；本轮作者核验或发布不替代这些阶段。
