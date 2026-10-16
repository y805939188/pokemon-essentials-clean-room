# R8 early_r5_u01_u02 有限独立接收报告

**本组独立部分已完成：48/48 完整合同、294/294 原始 schema 检查已实读并逐项对照。两个必要跨组接口尚未闭合，整体状态为 `INCOMPLETE_EXTERNAL_INTERFACES`，不签 `READY_FOR_COORDINATOR_CONSOLIDATION`。`UPDATE_NOT_STARTED`。**

这是原冻结派发中的一组贡献，交原接收者和主审整合，不新增审查层。不据本报告批准整个 H 任务、共享文件、其它 producer、正式接受、关闭或全局 B8。

## 固定输入与独立性

合同包含提交为 `9abf7bfc87274fb37f08d9f77a1bcb53f53d3ecd`。目标为 `11c057d9aed330c16312470f80f13d180f8e1e65`，checkout tree 为 `2fcef25ee9903bd7e28dec21f6fc2d970c221f77`，目标任务 tree 为 `bb0cb15506d2abc9e6b84abe1391048776de6997`；前接收检查点为 `ab44ee8c5ffd53ded7d5bc37ae6f15e6ed3ba8d8`。

B8 固定 `fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`。只读 R 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。实际云端目录分别为 `/workspace/pokemon-essentials-clean-room` 和 `/workspace/pokemon-essentials`。

实际接收 context `01a144a2-6391-7388-bd56-eef0d345301c`，由环境 `CODEX_THREAD_ID` 单独回显（平台输出 `0e775b`），不同于目标作者 `01a143b2-fc07-7339-ab2f-055dba6bc023`，也不同于前接收 context。未自行 spawn。请求 model/effort/tier/speed/Fast 分别为 gpt-6.1-sol/ultra/default/普通/off，实际五项均无权威回显，逐项 `UNVERIFIED`；UUID 回显不证明这些参数。

完整读了本组 prompt/readset、相邻派发 README、共同前提、aggregation 接合规则、强制 policy clarifier、内嵌全局 prompt、适用 AGENTS 和 review skill。clean-document-revision 明确将审计记录排除出其正文修订工作流，本报告按审计要求保留旧失败及后继限定。原完整 357 行 readset 的文件集合、mode/blob/bytes/SHA 和两层目标 tree 均独立核对，共 12,034,301 bytes；全部身份匹配不等于全部 357 文件正文已读。

恢复在独占目录内隔离 bare 中普通 fetch 精确 target/previous/contract，复用已有对象；36 个惰性载荷的压缩/解码身份均匹配。首次缺 promisor 配置导致恢复失败，补齐配置后从空目的重做成功。一次字典绑定验证误用列表顺序比较，改为完整多重集合比较后核过；没有赋予失败尝试语义信用。旧脚本、游戏及恢复出的程序未执行。

## 覆盖与实质结果

| 冻结人口 | 本次结果 | 凭据 |
| --- | --- | --- |
| R5-U01 34 合同 / 248 检查 | 全部完整接收其局部静态意义 | `reception-ledger.json`，每 ID 与每 criterion 各有本次理由 |
| R5-U02 14 合同 / 46 检查 | 全部完整接收其局部静态意义 | 同上；含 JXN 与全部 16 个地牢有序条件 |
| 本组原 native 条件 192 | 在完整原合同及原 schema 定义中保留、对照 | 不新增为另一验收分母 |
| 完整对象 784 / 字典项 2571 / 绑定 12655 | raw/expanded/原始指针与多重集合一致；业务值实际呈现、读懂、按语境判定 | `reading-ledger.json`、`evidence/object-identities.json.gz`、`evidence/presentations.json` |
| 固定 R 的 80 个文件、B8 的 34 个文件 | 实读所需完整定义、调用链和完整相关条款/向量范围 | `evidence/source-reading.json`；不是这些文件整篇或全系统签名 |

48 个 ID 及 294 个 criterion 的精确集合在 `frozen-units.json`。`evidence/adjudications.json` 是实读后逐条写出的 48 项论证和 294 条检查理由；装配脚本只关联这些既有判断及原始定义，不从旧 PASS、哈希或工具成功自动生成业务结论。每个完整原提案的事实、普通对照、反例、前提、失败/取消/部分提交、保留范围、反向条款及依赖保持原对象可回读身份，不删成导航。

原值用可逆呈现及精确同值关联阅读，并另补原始 criterion、完整业务目录/数值和当前 R/B8 上下文。`original_actual_text`、旧路由、行号或 label 这样的字段名称不构成跳过业务值的理由。相同字节只能复用呈现，不能自动批准另一 ID 的语境。早期截断的大输出没有计入全文信用，后续已用连续小段及完整对象呈现补读。

本组没有新增 B8 必修、optional 或 policy 提案。最强无需修改解释成立：B8 已在具体主合同及必要投影承接本组反例，而非只留源定位。重要核对结果如下，其余逐项理由见台账。

- 作者数据：浮点点号整数化、六列能力顺序、八词布尔与精确内联枚举、定长尾项和显式空重复值、类别/威力矩阵、区域编号缺口、全局0/玩家1/Home 的登记及保存顺序均已明确。普通未知属性与训练家专用杂行的接受门分开。
- 反写：形态0/None 省略后再编译继承、遭遇负版本变0及重复节前缀、电话姓名逗号改变三元身份、非重要 Consumable=false 保留，均区分写出当场内存与后续再编译，不承诺无损或原子。
- 文本：默认 core 过滤、替换/追加、地图同桶、键与译文值、脚本来源/解码/提交顺序、条件括号编码、先分节后逆转义及先截断输出已相接。地图名原地展开、改变后的查找键、空译消费者回退与继续预览的全局名先行规则分别保留。
- 内核：变量 false/nil、两类开关、条件处理器删除/清空、ASCII 内存流、64/4 迁移表及6/7/8槽、关键段0/main1、派生时间查询副作用、随机参数分派及整数 byte 索引位置都按真实入口前提核对，没有扩大到宿主成功或未来必备 API。
- 世界：页/路线41的原始值比较、绑定图私有键与当前图角色目标、墙钟冷却、强制路线同步首项及空路线悬置、对角零距离、原地跳跃、直接钓鱼公共事件 nil 返回、力量预检后计数/快照、202落位、脚本开关不同消费判据、采摘等待重植、355辅助双推进均与 B8 成对结果一致。
- 地牢：34/136 各8条全部逐行核对，包含每个旧墙/error子分支、首命中优先、上/下墙类别和 void/corridor 填地差异、清第一墙但保第三层、未列层不写。未匹配仅请求重绘，其它重算掩码重绘后抛错；局部成功不清旧重绘标记，也不证明全局连通、终止、摆放或 seed 一致。

## 历史资格与保留限定

完整原 packet、criterion、scope/current/accepted 绑定及四份原 header 按原阶段读取。原 U02 header 的 `actual_bounded_verdict=PASS`、`U02_formally_accepted=false`、`CLOSED=false`、`whole_shared_file_acceptance=WAIT_ALL_CONTRIBUTIONS` 同时保留；不能把它们抹成一个最终状态。当前逐项快照的 false 也不反向否定后继由唯一激活来源确定的状态；该全局解析属于尾组。

candidate FAIL、actual 局部 PASS、owner operations、接受、关闭候选和唯一激活各守原输入/时点；不把旧 FAIL/WAIT/MISMATCH 改写为本次 PASS。旧五份报告身份已由前接收后继恢复，原 UNVERIFIED 保留在原时点，新证据只给身份信用。前接收的 U03 消费条件、Summary/Party/FURFROU/BACK 和瓶子顺序仍只按其有限范围作上下文，不能借以重签未接的整个外组 producer。

后继已取得尾组固定回执 `76471376a7b0a42cfcf030a404fc91afb0a94835`，由非目标作者、非提出者 context `01a144a2-a554-77a2-997c-09b15efd7020` 给出两项裁决。本组已完整读其报告和裁决：`EVIDENCE-001` 确认28长值/48出现的业务证据分类缺陷，同时28/28在B8已有正文，不能据此推B8缺行为或历史结论一概无效；`POLICY-002` 确认 numeric? 的单末尾 LF 静态边界，未来兼容仍未选择。它不能套给 PBS 单行 f/b/枚举，不改 B8、不重开历史92/第七轮27。本组只接必要语义，不重复尾组全体policy主责。

## 真实剩余与整合入口

本组可得必要原合同/criterion/定义的未读、未接收差集均为0。以下是实际跨组缺口，不是本组抽样残留，也不是宿主材料限制：

1. **`IF-EXTERNAL-M05-006` OPEN**：四道具默认及 Flags/数量谓词的真实完整 producer 接收回执尚未取得。受影响的是 GR5-M01-011/preserve/01、GR5-M01-016/static/06、preserve/01 的主责引用接合。本组已核 B8 真实引用及自身份名/消费位事实；不冒充已收上游。
2. **`IF-GLOBAL-STAGE-SHARED` 最终组合 OPEN**：实际已收到上述尾组回执，接收其阶段资格，并把本组有关的16条shared、6条依赖边与当前48份producer事实逐一相接，见 `evidence/tail-interface-reception.json`。原候选 OPEN92/CLOSED0 与唯一激活后的历史 CLOSED92/OPEN0 分时点保留；不反写旧状态。尾组12:44记录的0/80外组收据早于本组核心发布，不表示现在仍没有本组凭据。原接收者/主审可直接使用两方实质凭据接合，但含尚缺core producer的最终组合不能全签；无需新增审查层。

原接收者/主审可直接消费本组 48/294 凭据，并在取得尚缺 producer 事实后完成对应组合接合；无需新增一轮审查。其它冻结 shard 的 primary 未被本组重签。真实地图/公共事件安排、原生归档、媒体/UI、实际存档和完整编译往返均未新增执行，限于相应观察点；没有用这些限制豁免已可读定义。

## 发布与执行

唯一写集为本报告目录；分支明确为 `codex/r8-final-early-r5-u01-u02-20261016`。只普通 commit/push 本组报告证据，不改正式规格、planning/audit、R、main/tag，不强推、不合并、不开始 TS 开发。解码/JSON/Git/范围呈现工具均只作恢复和静态证据，语义信用0；参考、独立行为模型、宿主、Demo、原生媒体及真实存档新增执行均0，向量 `NOT_EXECUTED`。

核心提交及远端隔离逐文件 mode/blob/bytes/SHA、集合、checkout/本组目录 tree 回读记录见 `publication.json`。后继回执提交以最终平台工具输出和交付消息绑定，避免把自身提交哈希递归写进自身。传输完成不会关闭上列两个接口，也不会改变 `UPDATE_NOT_STARTED`。
