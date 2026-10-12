# R4-U03 独立候选复审

裁决：**REQUIRES_CHANGES**。7项中6项PASS，GR4-M11-001需局部返修；30条标准为29 PASS、1 REQUIRES_CHANGES。问题是新增选择器向量的必要性别前提不足，图鉴固定普通外观的正文修订本身成立。

绑定候选 `58cd8b1585f17199a65c7b82afadbe0e326d9d30`，tree `c1b72453613645ac5e9928e748364348c1bd179c`；任务包 `08a57fb55118914a74ac1ffaf617647c01df8938`，证据后继 `f28d1376a736ea75405cf6e9aeb4a58349618f41`。固定B为 `1f36475d22120a0d1175967d5b17d71fe8311d88`，R为 Maruno17/pokemon-essentials `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。本报告只裁决候选事实规格与必要受影响回归，未进行实际整合审查、接受或关闭登记。

| finding | 裁决 | 独立核对结论 |
| --- | --- | --- |
| GR4-M04-001 | PASS | 个体正/背/图标先动态形态求值；严格5天门、强制0/1、战斗/仓库守卫及缺资源不回滚准确；WP35/EG-13/20保持。 |
| GR4-M06-001 | PASS | 双不同Power固定2+余池1；合法Knot+Power为1+4，gen5为1+2，同Power只计一次；WP34正确主规则保持。 |
| GR4-M10-001 | PASS | 命令BACK可优先，取消0仍允许USE；逐位编辑先于USE，越界USE挡住同轮BACK；事件默认取消值另立对照。 |
| GR4-M10-002 | PASS | 四级冷默认链、缓存空结果、显式失败和空w操作准确分开；暖实例/预览不冒称实际画面通过。 |
| GR4-M10-003 | PASS | 两格式化路径的词边界/严格额外2单位门准确；AB、A B、显式换行、pg与宽22/21对照成立，消费者可见性保留未知。 |
| GR4-M10-004 | PASS | 18×6共108格逐项对R一致，22空、84种非空身份在PBS登记；原始类别、两目标门、8→5→2→TACKLE边界、OppMove和hitNum分层准确。 |
| GR4-M11-001 | REQUIRES_CHANGES | 普通预览/Info/Forms/简略入口固定false且不清记录正确；标准6的两条多项向量缺性别匹配前提。 |

## 唯一必修问题：R4-U03-REVIEW-001（P3）

候选图鉴测试目录 `pokemon-rules-wp53-60-61-62-69-70.md:220` 的R4-PD05，以及UI测试目录 `user-interface-wp17-63-65-66-67-68-69-70-71.md:785` 的R4-DX05，只规定已见基础0、Alolan1和末次 `[0,1,true]`，却断言首轮写 `[0,1,false]`。这些前提不能保证当前雄性形态1在可列列表。

完整合法反例：固定默认R、无插件、显示全部形态关闭；RATTATA基础雄性0已见、Alolan1仅雌性已见（可仅异色），Alolan雄性1未见；所有条目入口/地区/metrics/前序界面与条件资源依赖正常。独立合法雄性Alolan1异色个体经最近见到入口把末次设 `[0,1,true]`；该入口不登记已见表。可列项>1，但具名Alolan只列雌项。进入Forms选择器，不移动、首轮BACK，当前雄性形态1不匹配，参考先选择排序首项基础雄性0并写 `[0,0,false]`，再退出不回滚。此为SOURCE_STATIC/DERIVED_VECTOR，未执行宿主或真实数据写入。

精确源证据：R `004_UI_Pokedex_Entry.rb:154–199,446–478` 的性别资格、排序、初始匹配和写入先于BACK；`005_Player_Pokedex.rb:61–69,128–140,195–227` 的已见与末次分离；Settings:311默认显示全部关闭；PBS RATTATA两性与具名Alolan数据。现有正确WP62:166–168、WP66-B:208–210、旧PD31:146、PD34:149和B38:285已经承接“当前末次不可列→首项”，不能被新向量覆盖。

影响仅限新增验收：实现若照错误无条件预期测试，会把参考正确的首项回退判错，或为通过测试绕过性别资格。最小修复仅给两个新向量补“基础雄性0、Alolan雄性1已见（可仅异色）”，或明确初始 `[0,1]` 确在可列列表；保留预期 `[0,1,false]`、普通刷新保留true和单项BULBASAUR对照。对应镜像证据按新候选同步，无需重写正文或返工全域。

复验须能唯一推出匹配例 `[0,1,false]`，并保持仅雌Alolan、雄性末次不可列的旧反向合同 `[0,0,false]`；所有设计继续标未执行。问题的完整机器记录、影响、最小修复和验收在 [findings.json](findings.json)；原30条逐标准原文及依据在 [criteria-results.json](criteria-results.json)。

## 身份、受影响回归与执行边界

独立核验12批准正式文件完整字节一致（552242 bytes），候选修改域为12正式+12作者证据，证据后继只加发布回执；30条标准与固定canonical原文一致、46静态设计身份/行/状态一致。身份一致不等于全部设计行为合格，PD05/DX05的前提问题仍阻断。

11个保护文件完整字节保持；相关SPINDA、孵化A053、U05数量/商店/命名、栖息地与性别/首项旧合同仅在受影响范围复核。旧229/341只保留B08/GIR-FD82-A053精确candidate/actual/independent-report tuple与qualified scope；其它历史复用/not_reexecuted，不补签全部23/229/341。详细读取范围、元数据和账指针见 [read-ledger.json](read-ledger.json)、[scope-identity.json](subreviews/scope-identity.json) 及其余独立具名子审。

第四review历史4次隔离原函数回执归属保持M01×1、M02×2、M12×1，包括捕获异常与第一次拟正常对照失败；未重跑。**本批新增参考/模型/宿主或Demo行为执行全为0，NOT_EXECUTED_THIS_UPDATE**。Git/JSON/完整字节/表格静态数据和发布校验为TOOL_VALIDATION，不是行为测试。未声称真实UI、字体、物理组合键、媒体/像素/动画、地图/完整Demo或外部插件通过，未来兼容政策未代选。

## 审者与发布范围

根任务 `/root`，真实可见thread `01a130de-2480-707d-a4fe-c7056c71c02e`，独立于作者thread `01a130c4-16b9-749d-8f40-e5ae1487e02e`。请求 gpt-6.1-sol / ultra / default / Fast=false；实际模型/后端回显UNVERIFIED，不猜测或审计后端。各辅助审者真实thread和分工见具名子审与 [identity.json](identity.json)。

仅在分支 `review/r4-u03-independent-20261012` 新增本批自身 `review/` 材料；未代修候选、修改参考或真实数据、写正式/公共账/main、接受/关闭、删除或force推送。普通推送后用全新无本地alternates对象库fresh fetch，逐完整blob字节比较全部树、报告工作字节及12正式候选字节；已冻结报告commit/tree由后继 [publication.json](publication.json) 记录。最终回执提交自身身份由最终fresh核验和交接回复给出，避免自嵌hash。

剩余阻断仅R4-U03-REVIEW-001；实际整合身份尚未提供，未作ACTUAL_PASS，候选裁决也不转为实际接受。
