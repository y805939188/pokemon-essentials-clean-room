# COM-ABILITY-ITEM 第八轮独立语义审查

状态为 `PRIMARY_LOCAL_COMPLETED_GLOBAL_RECEPTION_OPEN`；调度状态 `WAIT_DEPENDENCY`。本域没有建立新的可复现差异，新增 candidate 0、已裁决 required 0；数据、重载及历史资格接收尚未闭合，不能据此宣布全局 `NO_REQUIRED_UPDATE`。`UPDATE_NOT_STARTED`。

实际审者 `/root/com_ability_item`。请求 `gpt-6.1-sol / ultra / default普速 / Fast off`；实际 model、effort、tier、speed、平台 session ID 均逐字段 `UNVERIFIED`。可查逻辑入口为 `/root/com_ability_item`；平台私有执行流不声称已公开发布。

固定 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。本域六份精确输入的 bytes/SHA256/blob 全部与冻结读集一致。合同、技能、本域 prompt/readset 的当前字节又与固定报告 commit `78287d85f2ea54e465de2747a6aca82f3245125f` 逐项绑定相同，见 `fixed-report-input-binding.json`。远端/全局保护核验由 root 主责，不在此重复授信。

## 实际阅读与双向接合

本人全文阅读四件正式文件，共 762 行：WP48、WP49、WP50 主文、WP50 覆盖附表；两份共享 catalog 另完整阅读 669 行。连续窗口、逐文件身份和原始可见来源在 `reading-ledger.json`、`read-operations.json`；`formal-evidence/` 是已读当前正式字节的后续证据副本，不新增阅读次数。

两份主参考文件共 5,156 行，由 `/root/com_move` 本轮真实全文阅读，来源、完整所有家族事实、原 I/O 入口在 `received-contributions.json`。本域完整接收 48 个能力家族（267 个展开配对）、32 个物品家族（196 个展开配对），包括四个空家族的真实调用/中性回退；未把原审者的 `FULL_READ` 标成本人 `FULL_READ`，也不制造第二个全局源分母。80 家族的手写语义合同、463 个具体身份/别名及各 source range、消费者与当前规格在 `source-facts.json`、`forward-mapping.json`。

本人另完整读 Battler006 全 476 行、TriggerEffects 全 218 行、Ability 数据定义全 45 行和 BattleSettings 全 140 行；实际追读 Battler001 有效性/速度/重量、UseMove 扣 PP/阻招/变色/舞者/每击/蒸汽机、Priority136–279、Switching303–469、Battle 全局存活/天气/场地/拾取序、EOR436–539/597–781，以及 EmergencyExit 与 NaturalGift 完整定义。其余相关 Battler、Move、CORE、AI、CreatureB 来源只按实际具名事实/范围接收，未升级为本域全文件或其它 formal 主责批准。

`reverse-mapping.json` 对 441 个正文、表行或管理/范围记录保留 1,479 个具体分句/表格条件与结果定位，分别绑定家族、具体身份、调用前提、失败/部分提交和消费者；另保留结构行处置。分句数量是定位口径，不能当作全系统独立需求数；密集身份映射仍由 463 个配对事实分别保留。历史接受/关闭等文字只读而未继承批准，逐项待 root/history owner 接收。

两共享 catalog 的相关 116 条有限向量均已接收：AB01–25 共 25；HI01–36 加 HI10a–f 共 42；U04-HI01–03 共 3；WP49 AB 阶段 31；SE01–15 共 15。每条连同完整共同前提、独立变化、正常/失败/取消/异常前缀接收，见 `shared-vector-reception.json`。其它 catalog 行全文用于一致性阅读，其源主责继续归 Move/AI。所有向量 `NOT_EXECUTED`。

## 具名消费者接合与保留

- 半血退出保留严格整数半界、恢复先清标记、野生敌方实际存活人数、训练家回合末仅离场及负选择；不补全局 HP 监听。
- 每击顺序保留 T 能力→吐导弹→U 能力→T 物品，以及 U 损血后的立即恢复检查；JABO→ORAN 自耗→NaturalGift 下一击当前身份失败的已提交前缀不回滚。
- 精神香草仅清 Disable 计数；身份消费者、正计数自然到期、初始化/变身重置分别核对，未把本地治疗写成完整后继许可。
- 蒸汽机在附效/额外畏缩/减伤果消费之后，按当下类型、非无效、非零 calcDamage、非替身、当前普通有效及中央资格请求增量＋6；无独立强行/模式破坏者屏蔽。SE15 只证明已写阶级的静态故障前缀，不证明运行故障注入。
- 入场退出扫描为每个速度序成员先降阶物品、再跨半能力，首真即停。CORE-F049 的 MagicRoom 到期描述仅接收为再次查询缓存 `pbPriority(true)`；该分支自己不重算速度，不扩成逐项动态重排。原贡献文件保持。
- 气体结束重调入场不等于完整换入；紧张感解除可以重复扫描；天气/场地到期与默认建立通知、回合末显式早退点及当前身份重读保持。
- C/I/R/P/Belch、持久个体写穿、主动库存和正常终局还原分别接合；共生、回收/拾取、可强制果和普通食果门各有范围。主动 SITRUS 请求量、AI 估量与被动持物链分别保留。

全固定 `Data/Scripts/**/*.rb` 的能力/物品 add/copy 字面负证据检索命中 449 语句，主两源外 0；仅为这条“未见其它文件追加”静态声称提供支持，不能证明任意动态插件。见 `negative-registration-search.json`。

## 剩余接收与执行边界

`interfaces.json` 有六个有限已接收接口、两个开放接口：

1. `IF-AI-ABILITY-PBS-AND-RELOAD`：root 已确认默认及 Gen5–8 能力 PBS 五路径、1,122 个路径记录实例尚无完整实际读者（库存身份见 `pending-inventory.json`，不是语义阅读）；完整作者输入→编译→缓存→重载仍非零。CreatureB 六物品数据路径 3,154 个路径记录、实际 schema/注册/持久写回/保存资料与完整主动战斗道具定义的有限贡献已收到，但不据此关闭全部能力数据和重载链。可读文本缺接收不是宿主 limit。
2. `IF-AI-HISTORY-STATUS`：历轮接受/关闭、当前有效补充/policy/limit 与本域资格字段待 root/history owner 的实际接收。本域不以旧 PASS、相同 blob 或当前名字计数代替。

本轮实际参考行为、独立行为模型、完整宿主/Demo、原生媒体、真实保存/回放执行均为 0。身份、解析、JSON、计数与负检索是工具核验，均未计作行为执行。生成阶段一次路径根索引错误、一次读取字典缺键导致的工具失败如实保留在 `tool-failures.json`；修正后 JSON/身份一致性检查正常，失败未冒充成功行为。

只写本 task 独占目录；R、formal、planning/audit、历史、公共状态均未改；没有 commit、push、安装或启动整改。后续仅需接收具名开放载荷并核完整当前接口，若出现新反例另交 candidate，由 root 安排实际不同非提出者反证后裁决。
