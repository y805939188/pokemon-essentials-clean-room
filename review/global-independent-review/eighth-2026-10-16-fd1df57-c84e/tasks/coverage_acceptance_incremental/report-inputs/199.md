# R8 world PBS 全记录独立审计贡献

本贡献已完成固定 R 的 18 份 primary 数据、2400 条顶层记录的实际语义阅读；逐条值、字段、顺序、重复字段和精确行定位见 [records.json](records.json)、[forward.json](forward.json)。24980 个字段定位均能解析到具名逐字段语义。这里的完成资格只覆盖这些数据记录及明确列出的静态接口，不代表完整 world、UI、COM-FACILITY 或全部正式条款已闭合。没有未读 primary 记录；仍有可读且待其他 primary 接收的跨域后继，见 [interfaces.json](interfaces.json)。

所有行为均为 **NOT_EXECUTED**：参考运行 0、模型行为运行 0、宿主行为运行 0。仅执行读取、身份/结构/引用验证与审计报告写入。规格更新 **UPDATE_NOT_STARTED**，没有改参考、正式规格或开发框架，没有 commit、push、安装或再启动代理。

## 身份与实际阅读资格

- 逻辑审者 `/root/pbs_world_record_audit`。请求 gpt-6.1-sol、ultra、default、Fast off；平台未回显实际模型、effort、tier、speed、opaque agent/session ID，均为 **UNVERIFIED**。不以请求值冒充实际值。
- R commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- B8 commit `fd1df570cad987dc3852a3b958f03916e317f7fe`，tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`。合法报告后继 HEAD 不改变本次判断的固定对象。
- 已全文读任务输入 36653 bytes，SHA256 `63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b`；已全文读 AGENTS、inputs/review-SKILL.md 及委派清单。应用清洁文档修订约束，本任务只形成候选与证据，没有启动正式修订。
- 真实开始 UTC `2026-10-16T02:58:59Z`。完成快照 UTC、每个固定 blob、SHA256、字节数及工作字节与固定对象的比较见 [identities.json](identities.json)。连续阅读范围及其 FULL/PARTIAL 资格见 [reading-ledger.json](reading-ledger.json)。原传入清单的 INVENTORY_ONLY/UNREAD 仅为来件状态，现已显式另记本人实际阅读状态，不把机械库存算作语义阅读。

## 冻结的输入记录分母

| primary 文件 | 行 | 记录 | 用途与覆盖门 |
|---|---:|---:|---|
| `PBS/Gen 5 backup/berry_plants.txt` | 321 | 64 | 备用作者输入；不由默认非递归发现自动选用；缺 ROSELI/KEE/MARANGA |
| `PBS/Gen 6 backup/berry_plants.txt` | 336 | 67 | 备用作者输入；与默认同字节关联 |
| `PBS/Gen 7 backup/berry_plants.txt` | 336 | 67 | 同上 |
| `PBS/Gen 8 backup/berry_plants.txt` | 336 | 67 | 同上 |
| `PBS/berry_plants.txt` | 336 | 67 | 当前默认；3 个属性/记录 |
| `PBS/cup_fancy_pkmn.txt` | 620 | 618 | 当前 battle_facility_lists 未引用的完整备用表，仍逐行审读 |
| `PBS/cup_fancy_pkmn_single.txt` | 256 | 254 | fancycupsingle/fancycupdouble 都显式引用此表 |
| `PBS/cup_little_pkmn.txt` | 371 | 369 | littlecupsingle/littlecupdouble |
| `PBS/cup_pika_pkmn.txt` | 286 | 284 | pikacupsingle/pikacupdouble |
| `PBS/cup_poke_pkmn.txt` | 365 | 363 | pokecupsingle/pokecupdouble |
| `PBS/dungeon_parameters.txt` | 30 | 2 | cave/forest，基础版本 0，25 个属性出现 |
| `PBS/dungeon_tilesets.txt` | 28 | 2 | 图块集 7/23，23 个属性出现，含重复条目 |
| `PBS/map_connections.txt` | 40 | 19 | 每条 6 分量，实际锚点仍需地图尺寸 |
| `PBS/map_metadata.txt` | 398 | 69 | 稀疏地图 ID，259 个属性出现 |
| `PBS/metadata.txt` | 33 | 3 | 全局 0 与玩家 1/2，26 个属性出现 |
| `PBS/phone.txt` | 48 | 3 | Default、Jeff、Susie，41 个重复消息字段 |
| `PBS/ribbons.txt` | 401 | 80 | 80 身份/图标格位，240 个属性出现 |
| `PBS/town_map.txt` | 36 | 2 | Essen/Tiall，31 个属性出现，其中 27 个 Point |

总数 2400。结构分母另计 1641 个具名属性出现、9440 个杯表顶层字段、114 个连接分量。forward 的 24980 字段还保留分节身份、每行 EV 分量及全部四个招式位置，故不能与顶层字段相加混称一种分母。

默认 berry 与 Gen6–8 的固定 blob 都为 `d8c10bd5f730bc386589a63d27033e11cfe0ed4b`、SHA256 `afd5e62c4e453c6281d6d57a6284928e597de790a61d1a8ff1edeae17600aabc`。已完整读默认与 Gen5；Gen6–8 按完整身份和全部有效语义关联去重，未声称三份额外独立全文阅读或独立读者。18 路径、15 个不同字节输入的分母均保留。所有表的注释、分节、可选字段与重复出现顺序已纳入用途及覆盖门；结构脚本仅复核，不替代阅读。

## 记录到消费者的实际结果

[字段合同](field-contracts.json) 有 10 个具名组；[逐字段语义](field-semantics.json) 明确每个实际字段的单位、坐标、标识、缺省与选项门；[正向矩阵](forward.json) 给出 record→field→fact→consumer→formal；[反向矩阵](reverse.json) 的 25 条是精确子断言→全部相关 source-record→premise，不冒充全正式条款 census。需要更细的地牢接口，可用 [interface-facts.json](interface-facts.json) GEN01–GEN10。

树果的 332 个版本记录全部关联当前 67/备用 64 条身份。默认有 13 组完整参数元组，`3小时/15每小时/2..5` 只有 CHERI/CHESTO/PECHA/RAWST/ASPEAR 五项。小时转秒、整小时失水、缺省、覆盖物、浇水与收获正常/拒绝/失败前缀按实际 BerryPlants 471 行全文核对；未把未选用备份推成运行世代开关。构造缺省确为 3/15/2..5，与默认多数分布是两个命题。

1888 行杯表的原编号、物种、持有物、25 类性格、EV 代码原序和四个招式槽位完整保留。全体非空字面物种/道具/招式 ID 在默认记录头中存在，性格与 EV 代码有效；这是 TOOL_VALIDATION 身份复核，未执行编译、创建或战斗。已全文读 Challenge_Data 219 行以及对应编译/反写片段，区分解析时缺值、未知招式过滤/回退、直接创建的 EV 分配及反写依赖；当前 1270 行被四个被引用文件覆盖，另外 618 行仍是完整已审作者数据。每行是否被 Trainer PokemonNos 索引、规则×物种×队伍有限组合及会话恢复后继仍需 COM-FACILITY 主责接收，不能由字面 ID 合法推成全部可用或全部可达。

地牢两组参数与两组图块集的四种有限条件配对全部核对：当前 cell10×10/corridor2 均为偶数，跳过标准只读参数奇数写回的构造失败门；full/full 下 20 个节点、70% 请求 14 房间，不保证实际地图/摆放成功。512×384 只作为明确输入前提时得 66×52。映射条目、重复随机候选、自动/普通图块编号、单双墙、2×2 对齐、−8 北墙偏移及正装饰密度逐项核对。已全文读 RandomDungeons 1107 行及 WP14 全文；保留生成前/后种子消费、重绘不清旧矩形、逐格图块前缀、事件失败与仅玩家失败的不同结果。GEN01–10 精确限定种子三级优先、清 S、全局重播、重绘继续消费、无回滚及外层地图建立前提。没有给 Map051 补造实际 tileset、dungeon_area、事件、种子、终止或宿主随机结果。

地图元数据 69 项保留稀疏 ID、68 个位置、7 个 MapSize、全部天气强度（含 Rain100/Rain0/Storm50）、8 类 Flags、Dark/Dungeon/Safari/Dive 门。`[051] Dungeon=true` 是实际可读的识别字段。全部 19 连接都是互反方向配对，偏移单位为格；实际边锚点仍依赖地图尺寸。全局 Home 是 `(3,7,5,8)`，玩家 1/2 未显式给 Home；外观、初始金钱 3000、POTION 和六类音频保留各自身份及回退，不能由名字证明资源存在或起始过程成功。实际 world 审者的 IF-W01/W02/W05、W01–06/W19–21/W27–30 按具名有限事实接收，不继承 whole world PASS。

TownMap 两个区域与 27 个有序 Point 完整读。Cedolan 两个格子各自有点且共享飞行目的地；Berth/Faraday 只有开关 51/52，没有治疗三元组；同区域没有重复坐标。实际 RegionMap 审者全文读 356 行，已接收其首个同坐标返回、普通/wallmap 可见门、治疗字段和 MapSize 仅按长度偏移等有限消费者事实；这些不证明图片、实际飞行或转移。

Phone 全部 41 个原消息字段、转义与占位符保留顺序。已全文读 Phone706、PhoneMessage100 及 WP63：整套 current→start→Default 回退，字段不跨套合并；Default 常规 75% 配对、Jeff/Susie 无 Body 故常规始终 Body1+Body2；End 只在常规分支追加；再战 flag1 在播放前已推进到 2。时间谓词本次补读 Time1–82 核 05–10、14–17、17–20 小时边界。消息内容本身不会创建联系人、开启再战或播放电话；训练家/遭遇/本地化/时钟及完整电话 UI 后继仍有接收边界。

Ribbon 80 个身份与图标 0..79 保留；重复显示名/描述不合并 ID。实际持有顺序和 8 列、64×64 裁切作有限 source 检查；IconPosition 不作授予条件，描述不作赛事/设施实际奖励证据。全授予/净化/保存链待其主责接收。地图 Flags 另具名读取 Box Link、Giratina、ScaleWildEncounterLevels、LocationFlag 和 BugContest 设置入口的精确片段；调用/进化参数/会话启动未由单独标记推成既成事实。

## 正式侧阅读与独立接收

本人全文读 WP02、WP60、WP54 entry-rules-and-cup-data（109 行的具名数据文档）、WP55、WP76、WP63、WP14，以及 pokemon-rules-wp53-60-61-62-69-70 的全部 317 行测试目录。全文文字阅读只授 text-read；各组实际接收的子断言、源范围和前提仍受 reverse 限定。未把共享测试目录中其他领域的文字阅读算成其语义验证。

本人仅部分读 WP11 25–43、WP03 313–359、WP04 57–147/210–258、WP21 258–280、WP66-A 130–182；engine 目录只实读 266–313、461–476、648–697、727–742（DG01–43/DQ01–09/R5DG/R7-U01 及相关上下文）。这些未授本人全篇或完整 clause 接收。全 WP54 主合同、WP57 与全部设施复合测试尚未完成本贡献的接收；WP54 数据文档的 full-read 不等于所有 WP54 文档 full-read。

实际 `/root/kernel_review` 已读的 schema/Compiler 定义按精确 KER-F014/F029/F040/F041/F128/F129 等有限事实接收；其自身报告明确 0 个 PBS，本贡献不反向把 18 项扩成它的 73 项数据审读。实际 `/root/world_topology_audit` 和 `/root/ui_navigation_audit` 的接口使用具名来源、范围与未接收后继；不借旧 PASS、作者归属或计划代理抵充当前事实。

## 两个候选已获 root 限定 required P3 裁决

完整最小改动合同、固定 source/spec 身份与定位、普通/最小反例、正常/失败/取消/部分提交前缀、负证据、正确保留、同步与验收见 [proposals.json](proposals.json)。root 于 2026-10-16T03:24:16.568952+00:00 将两项限定采纳为 required P3；精确接收见 [root-decision-reception.json](root-decision-reception.json)。仍待全局历史去重与接口闭合，不是本轮最终总数或全局完成。proposals.json 保留裁决前作者快照；当前分类以 root 接收件为准。

| ID | 精确问题 | 最小修订与保留 | 实际非作者反证 |
|---|---|---|---|
| GR8-PBSW-001 | WP60 §3.3 L45 的“多数”元组在完整默认分母仅 5/67；13 组全分布可核 | 只换成具名五例或准确示例；保留构造缺省 L48/L177、全部 CHERI 公式/BP 向量与生命周期 | `/root` 独立全文读 67 条、BerryPlant 定义和 WP60 后建议 SUSTAINED_REQUIRED_NARROW_P3；[附件](../../coverage/root-pbsw-001-counterreview.json)；root 已限定 required P3，全局条件待闭合 |
| GR8-PBSW-002 | WP14 L48/L284、WP11 L37 把可读 `[051] Dungeon=true` 标记与实际地图/运行缺材料合列 | 只分开“随附 PBS 已标记”和“Map051/实际编译装载/tileset-area-event/进入查询及 Demo 未知”；保留全部生成种子/异常/部分写入条件 | `/root/world_topology_audit` 独立尝试 runtime-only 善意解释后支持最小 P3；[附件](../world_topology_audit/refutation-pbsw002.json)；root 已限定 required P3，全局条件待闭合 |

001 的单个 RAZZ 不同值仅是最小区分记录；真正否定“多数”的证据是完整 67 条分母与 5/67，不能用单反例冒充统计反证。002 的 PBS 字面配置也不证明已经成功编译、保存、装载或可进入；修订必须保留这些前提。

## 剩余与交付验证

当前未闭合的可读跨域工作包括每行杯表的 TrainerNos/规则×队伍适配及设施会话尾链、全部 Ribbon 授予/净化/保存、完整地图生命周期/音频/天气/黑屏回程、多处 Flag 的调用者、树果 item/bag/时钟/消息/旧存档转换总链，以及 Phone 训练家/遭遇/本地化/完整 UI。它们不能笼统改称“宿主限制”。已明确列在 interfaces 的 remaining/excludes，不用 partial 混充全通过。Map051 工程与图块素材、真实地图尺寸、媒体、实际编译 dat 装载、宿主版本/时钟/随机/执行结果另为真实材料或执行边界。

机器复核只检查 JSON 可解析、18 项固定字节身份、2400 记录/字段计数、24980 个字段语义引用、杯表字面登记身份与报告路径；它们不是参考行为测试。早期输出截断的孔洞已按 ledger 范围补读；少数只读路径/引用命令失败未运行任何参考行为、未改变源。精确工具调用总数与平台未回显 ID 不编造。

唯一写集为本 task 报告目录。最终可接收状态：**ALL18_RECORD_SEMANTICS_COMPLETE_BOUNDED_INTERFACES_PARTIAL_NO_GLOBAL_PASS**；root 的限定分类不授全局完成或更新资格；本贡献没有启动更新。

完成快照 UTC `2026-10-16T03:25:26.554255+00:00`。已通过 [validation.json](validation.json) 的 57 项固定身份和全部字段引用复核；这是 TOOL_VALIDATION，行为仍为 NOT_EXECUTED。
