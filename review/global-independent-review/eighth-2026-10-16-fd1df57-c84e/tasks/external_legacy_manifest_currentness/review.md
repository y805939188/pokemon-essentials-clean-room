# 第八轮独立审查：legacy manifest 当前用途

结论为 **INCOMPLETE_NO_PASS，待主审接收**。指定历史正文已连续全文读完；逐复合断言的现行用途与全部跨域接收尚未完成，不能认证库存原有的零资格缺口，也不能给出全局 PASS。整改未启动。

实际审者是本次外部分派的 `/root` 新上下文，非原库存作者。没有创建子审者；本上下文对疑点的反向分析不冒充不同上下文的独立反证。主审保留最终裁决和公共台账写权。

## 固定输入与写权限

规格仓库为 `y805939188/pokemon-essentials-clean-room`，B8 为 `fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree 为 `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree 为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。只读参考 `Maruno17/pokemon-essentials` 固定于 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree 为 `7589c800b61ba13a13040ed0d686979b80a84fd0`。

任务 prompt、readset、完整 global prompt 与用户指定 skill 从载体提交 `30cfed0996003b6ebf4b5c51cc04f31ca9255440` 完整读取；适用根 AGENTS 也已全文读取。各载荷的 bytes、SHA256、blob、mode、精确行范围与恢复方法见 [evidence-catalog.json](evidence-catalog.json)。`git show <commit>:<path>` 可恢复对应原件；本报告没有复制参考 Ruby 实现。

原任务的“共享容器不提交”要求被本次用户明确覆盖：唯一报告写集是本目录，唯一可推送分支是 `codex/r8-external-legacy-manifest-currentness-20261016`。隔离 worktree 为 `/workspace/r8-external-legacy`，原云端仓库为 `/workspace/pokemon-essentials-clean-room`，参考为 `/workspace/pokemon-essentials`。Mac 历史路径另列于 [identities.json](identities.json)，云端没有据此声称已核 Mac 原工作区、备份或全部未跟踪材料。未改 main、tag、正式规格、参考、planning/audit、公共台账或他人任务目录。

## 阅读分母与未完成部分

主载荷 `planning/review-manifest-2026-09-19.md` 整体为 4,127 行、1,420,152 bytes，SHA256 `7935075a2d5c14c0b5ad48c151a055ba1ee79783996afd2aea6c55c78c6c3d5e`，blob `14ee98eb2d9f62bf3d4451dab334ff6714b00723`。

| 分母 | 已读 | 未读 | 主审未接收 |
| --- | ---: | ---: | ---: |
| primary 1933–2079、2849–4114，共 1,413 行 / 627,400 bytes | 1,413 | 0 | 1,413 |
| 四段导航 1–65、1835–1932、2795–2848、4115–4127，共 230 行 | 230 | 0 | 230 |
| manifest 其余 2,484 行 | 0 语义阅读信用 | 2,484 | 未授接收 |
| primary 内容段落 881 个 | 881 | 0 | 881，现行事实继承未逐原子断言闭合 |
| primary 阶段标题 151 个、布局行 381 个 | 532 | 0 | 532 |

其余 manifest 行属于既有类型/身份索引的库存范围，本任务没有授予其语义全文阅读信用。不能把这个处置扩大到本次 881 个混合内容段落。

[frozen-primary-structure.json](frozen-primary-structure.json) 保留阅读前冻结的逐物理行 offset、长度和摘要；其中旧 `UNREAD` 是冻结时状态，后续状态以 [reading-ledger.json](reading-ledger.json) 和 [purpose-dispositions.json](purpose-dispositions.json) 为准。后一文件逐一覆盖全部 1,413 个物理结构，关联 21 组具名后继理由及未闭合用途；没有用日期或搜索结果将内容段落免审。

**原子断言分母仍为 UNFROZEN。** 物理行分母先冻结了，但复合段落没有全部拆成前提、事实、案例、资格及消费者子断言。这是本次未满足完整审查合同的实质缺口，不是可改标为材料或宿主限制的事项。881 个内容段落均保守保留未闭合义务；其中已核的有限事实也没有使整段变成已接受。逐段路由和成组后继理由不能替代逐断言认证。

补充阅读包括 extraction-plan 全文、根与 R7 现行交付导航全文、正式 README/范围全文、WP23 全文 199 行、WP66-B 全文 313 行、N01 v3 旧复审全文及 R7 导航勘误全文。两份正式文的全文阅读不等于两份文件所有条款已反向验收；本任务完整反向接收文件数为 **0**。source-traceability、feature-matrix、测试目录和 R 源码只给目录中列明范围的信用。大库存 JSON 只完整读其 top-level/sections 用途声明；`lines` 数组机械解析不算全文读。history-navigation 的大段显示及若干定位搜索曾截断，未据此给 whole-file 信用。

## 已确认的用途关系

`extraction-plan.md:3` 仍正向引用 manifest 作为“当前执行进度”的一部分。这是有效消费者，不能因 manifest 无 B8 字串或日期旧而把全部历史行为排除。该计划也有更早阶段的任务顺序与授权，本轮以实际用户授权和固定审查合同为准。[bounded-consumer-search.json](bounded-consumer-search.json) 保存有边界的字面搜索；它只用于定位，不证明所有动态、继承或同义引用不存在。

N01 的 1935/1937/1939 与详细记录 3380/3388/3397 有具体修正链：初稿的空格放置概括、外层成员门、Select 公开返回门及 BACK/Close 两种 Yes 语义逐次校正。B8 WP23 §8.1、WP66-B §2.2/§4.4 和 SH34 仍保留正确三层合同。已完整读相关选择、放置/替换、移动/删除、基础容器及新游戏存储注册范围，建立五条有有限前提的正反向事实映射，见 [forward-mapping.json](forward-mapping.json)、[reverse-mapping.json](reverse-mapping.json)。这些是明确存在的继承，不是代表其余段落的抽样证书。

在前序呈现正常、基础储存与相应资格成立的有限前提下：空映射格继续选择；有成员后仍须选 Select 才返回位置；BACK 确认 Yes 继续、No/取消退出，Close Box 确认 Yes 退出、No/取消继续；空返回不撤销此前完成的切盒或取出。直接有效队伍位置的成功放置/删除缺最后可战斗守卫，不能据此补造普通 UI 队伍选择可达性。默认 40×30 基础容器下的特殊负位置指向盒 38 格 29。确认包装、输入服务、所有特殊位置后续 Item/Mark/暂持分支及完整保存/重载仍分别保留未闭合义务。

2849 的车辆/步数/跟随/脚本异常/缺图一致性也已全文读到；2855–2858、GR004/005/011 与 WP80 batch3 给出了可追索的更正和后继。当前相关 R 源、B8 各条款和消费者尚未完整接收，已在 [interfaces.json](interfaces.json) 具名，不能把该段归为无行为行政信息。

WP37、WP61、编辑器、动画、转换器、设施生成、WP78/79 和 WP80 等版本序列分别记录了缓存/PP/路线/异色数学、blackout 可达性、No 后保留 PBS/共享写入、浅拷贝/部分文件、非幂等、EV/终止条件及覆盖判断的具体修正。21 组说明仅用于保留这些事实的阶段与后继关系，不认证相应当前全链。旧作者“语义变化为零”、同字节或旧 PASS 均不转授 B8 当前批准。R7 的 27 项有限静态关闭也不等于本次全局完成。

## 疑点及主审入口

[proposals.json](proposals.json) 保存 `R8-LMC-H001`：WP66-B §12.4 / audit 的 N01“待专项处理”与 WP23/SH34“已闭合”的资格表述疑点。完整路径/身份、有限普通对照、最小阅读反例、保留范围、建议读写与验收、依赖均已登记。

同时保留重要反向证据：B21 README/范围 §当前批准身份明确要求按原时点保留旧“待审”状态，根当前交付又提供更晚阶段资格。因此提出者目前认为有充分理由走 **no-required revision**，但这只是提出者判断；没有声称完成独立反证或主审裁决。当前新确认 required 数为 **0**，本地疑点 ID 不冒充公共 GR8 canonical ID。主审需用实际不同、非提案者上下文复核该资格，再决定接收、撤销或另行分配 canonical ID。

## 证据与执行边界

本文新增业务证据仅为有界 `SOURCE_STATIC` 和纸面 `DERIVED_VECTOR`。所有业务向量 **NOT_EXECUTED**；参考行为观察、独立行为模型、游戏/兼容宿主、Demo、原生媒体、真实保存/回放均为 **0**。Git、JSON、哈希、边界和远端字节回读属于 `TOOL_VALIDATION`，不计业务成功。没有运行参考 Ruby、转换器、生成器或历史执行脚本。

请求配置为 `gpt-6.1-sol / ultra / default / Fast off`；实际 model、effort、tier、speed/Fast、平台执行 session/log ID 均未回显，逐字段 **UNVERIFIED**。输入中的 source-thread ID 仅是来源线程，不能认证本次真实执行 ID。开始、最后更新、阅读结束与发布阶段 UTC 分列在 progress/发布回执；平台原始完整调用日志未导出，不能虚构 stdout/stderr 或时点。

[gaps.json](gaps.json) 给出全部 881 个待闭合段落 ID、两段未接收范围及执行/配置缺口。主审仍需完成原子断言冻结、逐段现行事实/接受用途、必要当前消费者和不同上下文接收。收到本报告只接收其真实已读和有限映射，不能据此把公共 `current_qualification_unread_lines=0` 升级为“用途审查已完成”或“未接收为零”。

发布身份和完整远端回读见 [publication.json](publication.json)。此文件绑定可自洽的先前 core；最终 tip 的完整回读另由交接结果给出，避免在文件内要求哈希自引用。
