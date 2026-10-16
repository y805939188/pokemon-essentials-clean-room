# r6_b 有限剩余接收报告

结果：**READY_FOR_PARENT_RECEPTION**。固定合同 `9a3eac8900fea93fee562d520a98edaf1e232fe6`；本组 16 个唯一 canonical、87 个完整案例对象、14 条边、R6/B8 两版 audit 全文及 1 个 Float facet 已完成独立有限静态接收。新增必修发现 0，必要未读 0，真实不可得静态输入 0。没有抽样，也没有开展新一轮全系统 review。

本读者实际 context `01a144a3-6ff4-7409-afdd-7ab11fd31030`，独立于目标作者 `01a143b2-d42d-7797-8bbe-c60266de7007`。未 spawn。请求配置为 gpt-6.1-sol／ultra／default／Fast off，实际 model/effort/tier/speed/Fast 无权威回显，全部 **UNVERIFIED**。Git 作者身份不作为独立配置证明。

当前功能基线 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；参考 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。实际读取工作树与固定身份一致；合同提交的正式正文及 audit 对 B8 无差异。P0、目标 C 只提供恢复与待审输入，旧 PASS 不移作本次签名。

| 本组 canonical | 完整 cases | 本读者核得的首要规则（其余正常／取消／错误前缀逐例见台账） |
| --- | ---: | --- |
| R6-B-001 | 5 | 图块集编号先成功读成7；缺对象在访问通行属性时抛错，局部替换诊断仅有7/map5，未读坐标层。 |
| R6-B-002 | 5 | 首行ASCII免费族生成提示后才接收；初钱1000/包0，生成提示与接收内部获得消息期间均1000/0；正常添加后1。 |
| R6-DX-E001 | 6 | Species实际Types使用一般池(false,false)；Apply Yes只给父工作槽，父Yes校验去重去空→register→dat→PBS；三项原序全保留，Pokemon查询复制全表。 |
| R6-DX-E002 | 5 | 退出Yes档案先于writer；No重载；writer先从非零形态收后缀，再选同后缀条目，五组相等只省非零节。 |
| R6-DX-AN-001 | 5 | 存在、锁定先判；最后使用者计数只扫0–59；0/2两未锁使用者可删0，2↔60后计数1拒绝，换回可删。 |
| R6-DX-AN-002 | 7 | 正常同对象Focus Target写position1，后续新增读取同一动画故取1。 |
| R6-DX-AN-003 | 5 | 构造捕获center128/224；同帧槽0请求X200后槽2仍按捕获锚点请求128，预览+64得264/192；不逐cel重捕获。 |
| R6-DX-AN-004 | 6 | 11项分别核构造和消费：Pattern[-2,1000]/0,X[-64,576]/0,Y[-64,448]/0,ZoomX/Y[5,1000]/100,Angle[0,359]/0,Opacity[0,255]/255,Blend[0,2]/0,Flip0,PriorityFront1,Focus依canvas兼容映射。 |
| R6-DX-AN-005 | 4 | 正常有效结构导入解码→类型→旧focus转换→槽替换→load，缺图警告不等于类型拒绝；宿主结果未测。 |
| R6-DX-AN-006 | 6 | 已有P重开Curve只清显示points；无showline时BACK未替换path，外层OK仍按旧P先扩帧再写XY。 |
| R6-DX-AN-007 | 5 | 自动点乘0.3333/0.6666，请求99.99/199.98而非精确100/200；宿主Sprite量化未知。 |
| R6-DX-DEBUG-001 | 4 | 空的一槽、max999、请求2：add正常全入2/true后消息2，入口无预检/返回值门。 |
| R6-DX-DEBUG-002 | 4 | 地图转移正常后warp尾直接refresh，按地图E1/E2后公共C1/C2各刷新一次，随后clear need_refresh、returntrue；不把转移内部刷新重复计入。 |
| R6-DX-DEBUG-003 | 8 | 无消息/解释器/三自动移动/早键/菜单请求且静止时，按住F9登记后消费；call_debug先清flag再SFX。 |
| R6-DX-DEBUG-004 | 6 | amount0在所有开关门前return，空buffer无echo/append/flush/文件。 |
| R6-DX-DEBUG-005 | 6 | 非空Bert直接赋名，不查询默认性别或用户名。 |

[reception-ledger.json](reception-ledger.json) 逐 ID 绑定完整原七组、提案、父前提和当前全部字段用途，逐 87 case 给独立理由与准确对象身份。共享对象的逐记录指针、完整值身份及全部字段用途在 [shared-field-reception.json](shared-field-reception.json)。两版 audit 分别为 1844／1896 行，旧全文与 B8 每个新增/替换行均实读；同字节段经重构相等后精确别名一次计功，未用 hash 检查代替业务阅读。审计文档涉及的其它工作包只作为完整历史/追溯文本处理，未被重新签成这些源领域的全量通过。

几处疑点已有明确反证，均不新增 canonical：Refresh map 直接置位后会显示消息，消息微更新可消费请求，故只保留精确观察点；AN-M09 的越界仅适用于原 selected≥新长度，旧 0/1 对照及尾追加在 B8 已写明，原 GR7-M15-002 不重开；指标输出的路径/省节/查询/保存前缀与 B8 KL23–26 对齐，GR7-J01-001 的 R7 整根不在此重签。Debug 加道具旧 §5.2 标签按准确 GR7-H08-001 后继读 §5.3；日志旧 §9 通过 B8 L279 明确到 §8.1。F9 的三自动移动门与强制路线 WAIT 分开。完整最强反解释见 [proposal-counters.json](proposal-counters.json)。

历史候选接收、实际内容通过、5c 登记资格、b7 正式接受、4df CLOSED 保留各自生成时点；早期 ACTUAL pending、formal_acceptance=false、CLOSED=false 不改写。当前逐 ID 接收没有替目标作者移用历史签名，也不授配置认证的全局 INTEGRATED_PASS。共享目录同一实际文件不按三个批次重复计整文件通过，WP67-A 的 NO_CANDIDATE_DELTA 门也保留为只读消费者。

[interfaces.json](interfaces.json) 提供 14 条完整边的独立理由，以及每个 producer 的准确 R 身份/实读片段、B8 消费者、全部案例及正常/取消/失败/部分提交。特别给 D 接合 Types 伪类型字段→一般池→保存→个体查询，指标缺条目克隆与字段默认/后缀/档案/PBS，以及 AI 日志与 Arena 状态分层。B 的 producer 已完整可读；D 的三个共同接口仍由 D 真正接收必要其它贡献后收口，本报告不替其签字，不把下游接收步骤当成 B 缺依赖。

Float recurrence 仍是独立 optional P3；必修默认中间点 0.3333／0.6666 与显式四点 N5 向量分别支持。未选择永久兼容源异常的政策，也未把宿主量化/像素误差并入必修。宿主输入、窗口、渲染、音频、错误恢复、真实存读档、Demo 和动画素材缺口继续保留。可得静态材料的未读与这些运行限制分列；本组必要静态材料没有缺失。全部新行为向量、参考程序、完整模型、宿主和 Demo 执行均为 **0／NOT_EXECUTED**；Git/JSON/hash/精确重构仅 TOOL_VALIDATION。没有运行旧脚本、游戏、动画工具或行为模拟。

[reading-ledger.json](reading-ledger.json) 给出实际语义读片；完整文件身份仅用于固定字节，不把局部片段冒充整源文件签名。[verification.json](verification.json) 核 23 个 decoded 输入的 mode/blob/bytes/SHA、87 个案例完整规范对象身份、44=38 精确别名、两版 audit 的精确重构与 B8 正式树；机械成功不产生语义信用。87 案例对象是完整冻结分母，不把复合行的无关领域一并认证。冻结索引内原 UNREAD/PENDING 是 P0 历史字段，当前接收结果以本报告和新台账为准。

用户指定发布分支 `codex/r8-final-r6-b-20261016` 优先于旧 prompt 分支。本次仅写本组独占目录，普通 commit/push；发布提交由最终交付回复外部绑定，不编造自身未来 SHA。发布后对全部新增载荷作一次独立远端完整字节回读，核文件集合/mode/blob/bytes/SHA/tree；不生成递归回执。父接收者与主审仍独占累计整合及 task-final。

**UPDATE_NOT_STARTED**。未整改、未改正式规格、未合并 main、未开始 TS 开发。
