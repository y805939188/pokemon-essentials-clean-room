# receive_elr_records_a 有限独立核验

结论：**READY_FOR_PARENT_RECORD_RECEPTION**。本组 **2,756/2,756 对、5,512/5,512 字段**已逐值完整呈现并实际阅读，原头六个、必要完整定义和本域有限反向条款接合完成；本有限合同未读、未接收均 **0**。新增提案/required均 **0**。这份贡献供父接收者继续七接口整合，主审保留全局task-final；**UPDATE_NOT_STARTED**。

## 固定输入与独立性

合同固定 `d14a4bf68776ac7aacf54065c28ed982a054c8a8`，载荷输入 `805468320bf8a44499f6d59f53820215b27899fb`，原受审报告 `90b9e27ef03feb2c018bb2f258b5e0d5aaed012b`。B8固定 `fd1df570cad987dc3852a3b958f03916e317f7fe`，正式tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。

实际thread/session为 `01a14489-ff6c-768f-a559-703851d89034`，由具名环境变量回显（chunk `87bda3`），与原作者、父接收者排除名单均不同。本上下文未编写正式规格，未自行spawn。请求gpt-6.1-sol / ultra / default普速 / Fast off；实际model、effort、tier、speed、Fast、agent ID无权威回显，逐项 **UNVERIFIED**；不以session认证配置。初始UTC与逐读UTC未倒填。

本地spec为 `/workspace/pokemon-essentials-clean-room`，R为 `/workspace/pokemon-essentials`。从固定合同创建独占分支 `codex/r8-elr-records-a-20261016`；写集只有 `continuation/parts/records_a/`。未写正式正文、R、父公共台账、其它parts、main或tag；用户授权范围内普通commit/push。

## 覆盖与阅读证据

| 域 | 实际完整记录范围 | 对数 |
| --- | --- | ---: |
| ABILITY_DESCRIPTIONS | 1–252 | 252 |
| ABILITY_NAMES | 1–266 | 266 |
| ITEM_DESCRIPTIONS | 1–252、254–665 | 664 |
| ITEM_NAMES | 1–730 | 730 |
| ITEM_NAME_PLURALS | 1–730 | 730 |
| MOVE_DESCRIPTIONS | 1–114 | 114 |

九片连续视图覆盖固定view第1–2774行，凭证依次为 `16a076`、`e92756`、`1b3c0e`、`c6e956`、`50e2e8`、`1d79d7`、`437f9c`、`b558d5`、`202b57`，没有截断或记录缺段。每条完整值对应两个相等字段，逐记录的ID、完整字面值、原R位置/哈希、视图行与读片、完整意义/前提profile、producer/getter、反向条款和未决，均在 [reception-ledger.json](reception-ledger.json) 中。共享语义完整写于 [semantic-profiles.json](semantic-profiles.json)，无以批量状态模板代替值阅读。

原始键与译文相等前提已独立按R逐对核实；每个unit的全部非身份字段、原forward全部字段、六个完整fact_group与固定805输入严格相等，未丢业务字段。原FULL_READ/WAIT_ROOT、原审者归属保留，不转授当前信用。纯身份索引只按具名ID/path/行/记录号/键哈希/值哈希用途处理。原readset全部字段保存在 [frozen-denominator.json](frozen-denominator.json)，ID集与实际读值视图、原索引精确相等。工具生成、解码和哈希信用均为0。

本组与父既有433对无重叠；ITEM_DESCRIPTIONS R253准确跳过，MOVE_DESCRIPTIONS R115–725不在本组。父原literal_read_here总数439还含六个头，初次433计数断言因此失败；诊断后按kind=record核为433，旧失败保存在 [original-semantics-validation.json](original-semantics-validation.json)。未按头或跨文件序号虚增记录数，也未批准六个原文件的范围外内容。

完整读取固定全局prompt、AGENTS、review-SKILL、父接收prompt、START、COMMON、records_a prompt/readset及全部原业务字段。`clean-document-revision`明确不用于审计报告；本次无正文修订。首次巨大导航/readset输出截断、错误路径、源输出截断与后继补读均在 [reading-ledger.json](reading-ledger.json) 留存。先读d14父报告后发现其与805不同，已另完整读取固定805版；后来状态不冒原输入。

## 实质结论与双向接合

完整Intl823行、WP08全文、GameData全文、Ability全文，以及Move/Item完整必要schema、构造缺省、getter、三家族全部producer、generic驱动、活跃分节/CSV/枚举、目录排序/递归、常量辅助与两个完整调试菜单均已独立读至结束。准确范围与固定commit/path/mode/blob/bytes/SHA见 [definitions.json](definitions.json)。原定位不足时已扩到必要完整定义；没有把外域巨文件无关玩法纳成全文批准。

六域原头及其首内容均决定合法哈希输入。原文件都带UTF-8 BOM、采用LF；导出器另写CRLF，两种事实分列。本组全部原键/译文相同，无逆转义标记、反斜线、首尾空白、控制字符或连续空白段，不因此把其它域五处差异删除。源分节预处理先于逆转义，只有键规范化；首条内容决定形态，分片起点、域号、TM数字后缀不改变原文件解释。

必要链为PBS真实字段/缺省→唯一身份登记/构造→三家族终检读取real_*→set默认game哈希（默认core同键过滤）→作者编译语言文件→显式当前语言加载→同域文本getter。直接getter依当前语言game→core→原输入，空串命中保留；默认语料用于收集/导出。set重建、add保留旧值的定义区别保持。本组三producer实际均set。三类名称、独立复数、描述及文本键不与游戏对象ID/注册数混同。

266特性名称与252描述不按行号配对；道具别拼如Thunder Stone/Thunderstone保持独立键；复数直接用real_name_plural，并不从单数计算。道具描述中的招式叙述仍归道具文本域，招式描述中的效果/回合数仍是文本数据；不能据叙述推出战斗、地图或其它玩法已实现。所有本域原forward的WP08-30/51/130/153/155及必要上下文已反向核对，见 [reverse-mapping.json](reverse-mapping.json)。现有通用合同及域getter已覆盖本记录意义，WP08非目标不复制语料，未提出仅为复制内容的新required。

[finite-vectors.json](finite-vectors.json)给出13组完整有限普通/缺译/空译/结构错误、set/add、导入/导出、取消与失败/部分提交对照。作者选B后取消不切游戏语言A、不写导出；确认覆盖后先删再写不原子。完整导入先打开截断输出，后解析失败不恢复；单文件解析无该输出副作用。先节已入内存不等于产物成功，结构错误与格式化错误按入口分层，不把UI后续窗口转换混到查找阶段。

本轮曾检查“双Text_前缀”假设。完整菜单1474先原位修改所选字符串，1475读取的是同一个已去前缀对象；导入器再加一次Text_后访问正常目录。该假设遗漏了别名/原位修改，现已撤销，详见 [audit-notes.json](audit-notes.json)。它不是待裁决新提案，不增加required或独立票。撤销不改变真实先截断/失败前缀。

## 剩余真实边界

本shard必要原记录值、原业务字段、共享定义与有限接合均已完成，无本组容量或材料阻塞。父仍须实际接收本贡献及其余shards；父现有433对不能与本组重复计数。本组不签ELR-I01–I07最终完成。具体未接范围逐个列于 [interfaces.json](interfaces.json)：全部35PBS必要原值/备份启用、125反向source-linkage、178二进制键链接、其它消息生产者与完整WP04贡献、UI36/Dex7/图像家族/PictureSprite后继、SaveData/Value/SaveValues/StartGame、地图名/物品/提示后继、历史原合同及canonical/alias、目标213载荷当前语义/用途收口均留父整合。

GR8-ELR-001仅保留合同所述主审有限required/P3与历史canonical OPEN，不重新投票、不按标题去重、不重开R7的27。optional、Float、policy、limit等历史分类不在本组自动采用或关闭。

参考行为、独立模型、完整宿主/Demo、原生媒体、真实保存/重放新增执行均 **0 / NOT_EXECUTED**。真实翻译显示、原生加载器、媒体、工程可达与任意插件覆写另按父边界，不以这些限制免除可读值债务。只运行自己已理解的Git/Python校验与呈现工具；没有安装或执行恢复的旧脚本。

## 发布与接收方法

六件核心台账及补充意义、完整定义、13组向量、反向条款和纠错凭证均在本独占目录。先冻结core普通提交，再有限发布绑定实际core身份；[publication-receipt.json](publication-receipt.json)由后继提交记录core的逐载荷远端回读，不写自身未来hash。最终消息给实际发布C、checkout tree及本shard task tree。

远端仅完整回读自身新增/改变载荷，逐文件核集合、mode/blob/bytes/SHA和目录tree；固定805/R/B8输入复用已核身份，不重新下载213文件。远端传输与机械一致性不授新的语义信用。原平台完整私有流未导出，只有真实chunk凭证及固定视图/定义恢复定位，逐读UTC与分离stderr无回显字段保持UNVERIFIED。
