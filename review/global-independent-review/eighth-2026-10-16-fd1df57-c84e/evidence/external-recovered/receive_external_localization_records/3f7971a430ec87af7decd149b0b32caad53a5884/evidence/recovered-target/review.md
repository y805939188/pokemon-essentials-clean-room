> 当前接口续审结论见 [continuation-review.md](continuation-review.md)：5组有限完整接收、2组部分接收；原同18个局部依赖仍6,655行本人未读，35PBS正文未接收。下文保留首交付时点的7组NOT_RECEIVED快照，不冒充当前状态。

# 第八轮独立审读：external_localization_records

本上下文已完整审读 primary 的18文件、841,275 bytes、21,466物理行、10,697条键/译文记录及18个文件头结构（合计10,715结构单元、21,394记录字段），primary未读0。primary正式文件分配为0；为双向核验另完整读取WP08、WP69主文和附表，部分读取WP15与共享测试目录。此为有限任务交付，**不构成全系统PASS或接口接收完成**。当前状态为 `WAIT_ROOT_RECEPTION_AND_INDEPENDENT_COUNTERREVIEW`、`UPDATE_NOT_STARTED`。

## 固定输入、授权与路径

- B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`。
- R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。实际容器spec为`/workspace/pokemon-essentials-clean-room`，参考为`/workspace/pokemon-essentials`；Mac历史路径单列在identities，不冒称其准备资料或其它worktree已经核验。
- 合同commit `30cfed0996003b6ebf4b5c51cc04f31ca9255440`；任务prompt、完整全局prompt、指定skill和AGENTS已完整读取。全局prompt36653 bytes/SHA256 `63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b`。指定clean-document-revision全文已读；其最终态正文规则不替代本审计规范，本任务不修正式正文。
- 最新用户授权替代旧任务prompt的写目录及禁止commit/push规则：唯一分支`codex/r8-external-localization-records-20261016`，唯一写集为本目录。未spawn，未整改；不改公共台账、正式规格、main、tag、R或他人目录。
- cloud本地main和origin/main缓存缺席；实时远端main/tag均解析为B8。没有用reset或覆盖其它分支掩盖差异。原参考origin是用户fork，contract upstream Maruno17另列，固定commit/tree一致。

## 完整覆盖与资格

| primary文件 | 完整记录 | 连续物理行 | 资格 |
| --- | ---: | --- | --- |
| ABILITY_DESCRIPTIONS.txt | 252 | 1–508 | FULL_READ |
| ABILITY_NAMES.txt | 266 | 1–536 | FULL_READ |
| ITEM_DESCRIPTIONS.txt | 665 | 1–1334 | FULL_READ |
| ITEM_NAMES.txt | 730 | 1–1464 | FULL_READ |
| ITEM_NAME_PLURALS.txt | 730 | 1–1464 | FULL_READ |
| ITEM_PORTION_NAMES.txt | 102 | 1–208 | FULL_READ |
| ITEM_PORTION_NAME_PLURALS.txt | 102 | 1–208 | FULL_READ |
| MOVE_DESCRIPTIONS.txt | 725 | 1–1454 | FULL_READ |
| MOVE_NAMES.txt | 761 | 1–1526 | FULL_READ |
| POKEDEX_ENTRIES.txt | 1028 | 1–2060 | FULL_READ |
| RIBBON_DESCRIPTIONS.txt | 78 | 1–160 | FULL_READ |
| RIBBON_NAMES.txt | 70 | 1–144 | FULL_READ |
| SCRIPT_TEXTS.txt | 3305 | 1–6614 | FULL_READ |
| SPECIES_CATEGORIES.txt | 650 | 1–1304 | FULL_READ |
| SPECIES_FORM_NAMES.txt | 268 | 1–540 | FULL_READ |
| SPECIES_NAMES.txt | 898 | 1–1800 | FULL_READ |
| TRAINER_TYPE_NAMES.txt | 48 | 1–100 | FULL_READ |
| TYPE_NAMES.txt | 19 | 1–42 | FULL_READ |

逐记录键和值均实际显示阅读，相等字段以一个完整字面值明确同时代表两字段，差异字段分别显示；记录i精确对应物理行2i+3/2i+4。此是无损全结构视图，不按样本、搜索命中或相同blob授信用。三次显示截断的缺段均单独完整重读；原视图及恢复区间保留。BOM/CRLF、bytes/SHA/blob由机械校验另列，不升级为语义证明。

正向映射逐记录继承具名域事实组：完整原始键/值→过滤/逆转义/规范键→成功编译载荷→显式语言加载→真实文本getter/脚本入口→WP08当前合同。正式正文不复制整套语料；名称、生态叙述和技能描述作为文本数据处置，不冒称其玩法已经接线。WP08完整逐条读取，子断言、源位置、有限前提和待接收条件在reverse-mapping分列。共享测试LZ01–LZ41完整行及限定说明已读，全部新向量NOT_EXECUTED。

已补读：完整823行翻译服务，相关PBS替换/形态追加/默认持久化/顶层路径选择，七类数据构造与getter，调试导出/导入完整菜单单位，启动/载入语言选择直写单位，完整Slot456行、动画包装228行及必要缓存/IconSprite入口。补读依赖共26文件，8份全文（R5/B3），18份部分范围；这些部分文件合计仍有6,782行未读，精确连续已读/未读区间逐文件登记，不把它们改标limit。非primary源文件只按reading-ledger记载的真实区间授信用，不把局部单元覆盖扩大为整文件批准。

## 事实与疑似提案

语料18域全部为哈希键/译文材料；domain编号不把物种名、招式名变成数组索引。运行game→core与作者默认core/game分层正确。存在5条键/译文差异：ITEM_DESCRIPTIONS R253；SCRIPT_TEXTS R1991、R2043、R2061、R2202。它们分别保留空格或换行差异；当前WP08键规范化与译文值分离的合同已容纳，不作为新required。普通导入、缺译、空译、作者取消及截断旧产物分别核对，未用理想往返代替源行为。

**GR8-ELR-001（疑似缺项，建议P3，尚未裁决）**：Slot的7个图像身份经语言查找后交动画/精灵入口；完整WP08指定消费者表、WP15对应接点、完整WP69及附表没有给出Slot这一消费者接点。有限反例是在有效当前语言把转轮图A映射为可加载的同尺寸B，A仍存在：实际源请求B；只照当前列举集合固定Slot原身份的实现会请求A。缺译对照请求A。身份角色、源/正文完整载荷身份、前提、普通对照、取消/失败/部分提交、负证据范围、最小建议修订、保留scope、验收与历史待查已写入proposals.json。没有运行宿主或修改正文。

此提案只能由实际不同的非提出者上下文独立反证、检查其它主合同覆盖及历史别名后交主审裁决。required已裁决0、独立反证已接收0，不能把这些0解释成NO_REQUIRED_UPDATE。其它资源匹配63处仅为跨域导航，不据字符串存在增加已确认问题。

## 未读、未接收与执行边界

- primary未读0/18文件、0/10,697记录；主审尚未接收18/18文件的本任务贡献，不能把本地已读冒称全局已接收。
- 新发现默认/备用PBS依赖35份均可读但本上下文UNREAD、NOT_RECEIVED，精确path/commit/tree/blob/bytes/SHA在库存与identities。其主责分属PBS当前、备用及战斗领域；不以语料替代这些全文或玩法核验。
- incoming接口7组，收到0、未接收7：kernel/WP08；编译生命周期；默认/备用PBS；messages_core及脚本归档；所有UI/战斗图像caller；世界/保存/消息/物品后继消费者；历史资格/原limit/当前有效补充。接口条目给出准确已知路径和现有证据。18文件的局部阅读不因它们未接收而虚改为未读，接口也不因局部映射而关闭。
- `messages_core.dat`存在且963270 bytes，未在本上下文解码或语义阅读；`messages_game.dat`在此固定R中不存在。可恢复资料未读不改标opaque/宿主limit；其它UI资源caller只定位的部分同样保持UNREAD/待主责接收。
- 新参考行为执行0、独立行为模型0、完整宿主/Demo0、原生媒体0、真实存档/重放0。所有反例与回归为SOURCE_STATIC/DERIVED_VECTOR，NOT_EXECUTED。Python/Git只作资料呈现与身份/传输核验。
- 请求gpt-6.1-sol/ultra/default/Fast off；平台未逐项回显model/effort/tier/speed/agent/session，实际均UNVERIFIED。只有当前平台逻辑上下文及source thread引用可见，不虚造服务配置或独立审者。
- evidence保留公开读取视图及受控命令I/O。完整私有平台事件流没有导出，资格UNVERIFIED；早期定位错误、显示截断、缺失缓存及恢复路径具名保留，历史I/O与exit/UTC不倒填。

## 交付与主审入口

progress.json、identities.json、reading-ledger.json、forward-mapping.json、reverse-mapping.json、interfaces.json、proposals.json及本review.md为主交付。evidence内含合同、逐记录完整视图、连续源单位视图、机械库存、原始定位I/O及执行边界。publication-receipt.json在后继发布提交绑定实际core commit/tree、目录tree和逐文件完整远端回读；此正文不写自身未来commit。所有核心文件完整远端回读结果只证明传输身份，不增加语义阅读信用。

主审可按本目录普通Git blob完整读入，先检查未接收队列、实际独立反证与历史去重，决定有限事实接收及GR8-ELR-001分类。后续整改须另行手动委派，本任务没有启动。
