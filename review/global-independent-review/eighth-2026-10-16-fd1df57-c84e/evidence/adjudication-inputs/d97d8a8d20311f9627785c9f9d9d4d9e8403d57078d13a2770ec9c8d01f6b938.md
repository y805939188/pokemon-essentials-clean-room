# 第八轮 external_pbs_creature_backups 独立审查证据

当前结论为 **REVIEW_INCOMPLETE**，任务登记为 `FAILED`：约定的全量逐文件、逐结构、逐条款双向审查尚未完成。本包是可核对的未闭合证据交付，不能用于全量 PASS、全局无必修结论或整改启动。`UPDATE_NOT_STARTED`。

实际审者是当前 `/root` 上下文；未启动子审者。主审的独立反证、最终分类和贡献接收均待完成。同一上下文的续读、角色命名和脚本检查没有增加独立性。

## 固定身份与授权

| 对象 | commit | tree |
| --- | --- | --- |
| 规格 B8 | `fd1df570cad987dc3852a3b958f03916e317f7fe` | `751dfde81048c81390f89a65ca1d1a565ba8e1ca` |
| B8 正式规格目录 | 同上 | `f292698cdd4a8e725525a9be6dc34b75faaf151e` |
| 参考 R | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 固定委派输入 | `30cfed0996003b6ebf4b5c51cc04f31ca9255440` | `d43467098a680d1562eeeb9572410204b8ea0d49` |

实际云端规格根为 `/workspace/pokemon-essentials-clean-room`，参考根为 `/workspace/pokemon-essentials`。参考克隆 origin 实际为用户 fork `y805939188/pokemon-essentials`；启动检查另查到声明上游 `Maruno17/pokemon-essentials` 的 HEAD/master 为同一 R 提交。历史 Mac 路径不作为当前文件位置；历史分支、工作树和保护状态没有据此获得核验。

唯一写目录为本目录 `review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/external_pbs_creature_backups/`，唯一报告分支为 `codex/r8-external-pbs-creature-backups-20261016`。本次用户指令授权本目录报告的 commit 和普通 push，取代固定委派文件中原 `tasks/pbs_creature_backups/` 写目录及禁止提交要求。其他限制继续适用：不改 main/tag、正式规格、参考、公共台账和其他任务目录，不整改。

固定委派 prompt、readset、完整全局 prompt、技能和 AGENTS 均已经全文读取。`inputs/` 保存五份固定提交的精确字节副本，完整身份见 `identities.json` 的 I01–I05。适用技能为固定输入中的 clean-document-revision，仅约束交接正文最终态；它不替代阅读与反证合同。

## 实际分母与阅读

| 分母 | 实际已读 | 未完整读／未读 | 最终接收 |
| --- | --- | --- | --- |
| primary 文件 16 | 完整 12，部分 1 | 整份未读 3 | 0 |
| primary 节记录 6712 | 完整读 3675 | 部分 1，未读 3036 | 0 |
| primary 行位置 102507 | 24047 | 78460 | 不作为语义条款分母 |
| primary 字节 4692651 | 已读区间 599942 | 4092709 | 不作为语义接收计数 |
| 字段／类型／槽位物理行 89067 | 16682 | 72385 | 不作为复合子断言分母 |
| 已扩展、具名依赖 59 | 19 份全文：13 参考、6 正式规格 | 40 份可得未读 | 0；扩展分母仍未封闭 |

完整阅读的 12 份为四代各自的 `encounters.txt`、`pokemon_forms.txt`、`pokemon_metrics.txt`。10 份按原始连续区间读取；Gen7/8 metrics 另逐份读取了保留所有标识和四个字段字面值的完整顺序结构表，未用同 blob 身份代替阅读。生成脚本后来核对每节恰有四个唯一预期字段，仅为表示无丢失的机械检查，不追加语义信用。早先被截断的整文件显示不计为完整阅读，后续连续读区间见台账。

Gen5 `pokemon.txt` 仅读到第 1060 行：BULBASAUR 至 WIGGLYTUFF 共 40 份完整记录，ZUBAT 仅段头与 Name。第 1061–16902 行未读。Gen6 第 1–18640 行、Gen7 第 1–20863 行、Gen8 第 1–23115 行的基础物种文件整份未读。上述数据全部可得，不能改列材料限制。

`reading-ledger.json` 枚举全部 6712 节、每节行区间、字节区间和字段／类型／槽位行位置，逐项区分已读未接收、部分读和可得未读。物理行与节的枚举不等同复合语义条款分解。完整每字段事实—消费者—规格映射尚未形成；语义子断言总分母为 `NOT_ESTABLISHED`，未映射项非零。`forward-mapping.json` 中所有节的完整映射仍为待完成。

六份全文读过的正式规格是 WP02、WP04、WP18、WP21、WP36、WP62。全文阅读不能认证其中全部断言：当前仅登记 20 条有限反向核对笔记，仍含待拆的复合区间，独立接收为 0。全部 formal clause 的精确子断言分母尚未建立；不能用这 20 条笔记充当全部正式规格分母。相关测试目录和其他具名正文仍有缺读。

## 已读事实与疑点处置

12 条静态事实笔记涉及普通发现不激活 backup、物种字段与形态继承、查表回退、metrics 默认／延迟创建、显示偏移、遇敌编译、版本查询／枚举差异、当前地图快照、野生生成、作者编辑保存／取消和图鉴别名。这些事实各带有限前提、精确源与规格身份及未闭合消费者，见正反映射。它们不是全量通过或已接收结论。

唯一具名疑点 `GR8-XPCB-001` 起于版本迭代的键形态与登记键不同：正常登记下，map5 同时有 v0/v1 时，查询 `(5,1)` 选 v1，枚举版本 1 则先产 v0 再产 v1。四份 encounters 的 map5v0 有 STARLY 的 PokeRadar 槽，而 v1 没有；图鉴区域页在其隐藏／区域／可见 Point 等前提成立时会聚合该迭代结果。

完整回读当前 WP36 §3.1 与 WP62 §5.3 后，二者已明确写出该对照及消费者前提。因此本上下文将其作为“新增必修提案”的疑点撤回；保留原疑点、有限反例、负证据范围、正确保留 scope 和主审独立反证要求。没有将本地撤回冒充独立的 `no-required revision` 裁决，历史 ID 和关闭关系仍 `UNVERIFIED`。

最终分类计数为 required 0、optional 0、no-required revision 0、policy 0、limit 0，含义是尚无经独立接收的分类；不是已经完成审查后的零发现。`NO_REQUIRED_UPDATE` 未成立。

## 尚未闭合的工作

`gaps.json` 给出每份 primary 未读区间和 40 份已定位可得未读依赖的固定身份。包括 Pokemon 实际 getter／创建、MultipleForms、战斗和其他 UI 消费者、设置、枚举／成长／进化等硬编码资料、作者菜单、持久化与转换、相关正式条款和测试目录。继续扩展的完整依赖总分母尚未封闭。

`interfaces.json` 登记九条开放组合链及其精确缺口；目前接收数为 0。`creature_b` 的道具贡献尚未接收，没有因委派文件允许共享便假定其事实已获信用。R6/R7 有效补充与历史资格尚未独立恢复；旧 PASS 未授予本轮阅读或接收信用。

这些可得缺读和待接收项阻塞本任务完成。没有已证基础设施障碍阻止继续阅读，也没有把它们改名为宿主、opaque 或材料限制。

## 配置、执行与日志边界

请求配置为 `gpt-6.1-sol / ultra / default / Fast off`。实际 model、effort、tier、Fast 回显逐项均为 `UNVERIFIED`；用户给出的 source thread ID 是 `01a13f49-a154-7054-9b04-ce31f924d01c`，本实际平台 session ID 未回显。最早机器记时记录为 `2026-10-16T07:56:45.625890+00:00`，不冒充精确首动作时间。

本轮行为执行 0；参考编译、writer、游戏、存档、宿主显示及行为向量全部 `NOT_EXECUTED`。库存、哈希、解析坐标、JSON 校验、Git 传输和远端读回属于工具检查，不计为行为测试。未安装软件，未触及生产服务、真实存档或参考写入。

`preflight-io.json` 保存已仪表化预检的原 stdout/stderr、exit 和 UTC；发布检查另保存相应实际 I/O。源码显示属于私有平台工具流，`semantic-notes.json` 记录可见回执和实际区间；没有声称已经公开发布、可外部恢复或远端读回完整私有平台流。完整平台原始流导出为 `UNVERIFIED_NOT_EXPORTED`。若主审要求全部原流的公开投影，该证据缺口仍未满足。

## 交主审的可复制正文

> 接收 external_pbs_creature_backups 的未闭合证据包；先读本 review.md、progress.json、coverage.json 和 gaps.json，再按 identities.json 核对固定载荷。B8/R 仍为本报告列出的提交。此次仅报告专属目录提交和普通 push 获授权，正式规格与参考未整改。
>
> 当前 16 份 primary 中 12 份完整读、1 份部分读、3 份未读；6712 节中 3675 完整读、1 部分、3036 未读，全部待最终接收。完整字段／条款双向映射未完成，相关消费者与测试有具名可得未读，扩展分母未封闭。不得以本包宣布该分片全量 PASS 或 NO_REQUIRED_UPDATE。
>
> 请由实际不同、非提案者上下文独立核对 GR8-XPCB-001 的有限前提、源键形态与当前 WP36/WP62 明确条款，再作最终分类和接收；本地仅撤回“新增必修提案”。其他剩余阅读按 reading-ledger 的精确未读区间继续，不继承工具、同 blob 或历史 PASS 信用。UPDATE_NOT_STARTED。

## 文件与发布恢复

八项要求的交付为 `progress.json`、`identities.json`、`reading-ledger.json`、`forward-mapping.json`、`reverse-mapping.json`、`interfaces.json`、`proposals.json`、本 `review.md`。补充文件保存原输入、语义笔记、库存、覆盖、缺口及实际执行边界；工具源码仅构造坐标／报告和检查身份，不能代替语义阅读。

先冻结本语义证据 core，再由后继 `publication.json` 绑定实际 core commit/tree、载荷 manifest 和普通 push／完整回读结果。`payload-manifest.json` 不包含自身未来身份；其身份由后继发布记录固定。最终发布提交及最终逐文件回读由交付消息给出，避免文件自含未来 commit 的递归。
