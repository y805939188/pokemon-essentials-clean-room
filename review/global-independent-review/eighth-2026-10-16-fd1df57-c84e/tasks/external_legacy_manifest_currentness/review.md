# 第八轮独立审查：legacy manifest 当前用途

**指定 primary 的现行用途审读已完成，待主审实际接收。** 156 个有意义的版本／审查／授权事件、881 个完整内容段落均已有具体用途、后继和现行主合同路由；用途未裁定为 0。本文不授全系统 PASS，也不代替其他 primary 的全部源／条款／消费者验收。整改未启动。

实际审者为本次外部分派的 `/root` 新上下文，非原库存作者。没有 spawn；提出者没有以角色改名代替独立反证。主审保留公共台账、canonical ID、最终接收和裁决。

## 输入与权限

B8：`fd1df570cad987dc3852a3b958f03916e317f7fe`；workspace tree：`751dfde81048c81390f89a65ca1d1a565ba8e1ca`；formal tree：`f292698cdd4a8e725525a9be6dc34b75faaf151e`。R：`Maruno17/pokemon-essentials` 的 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree：`7589c800b61ba13a13040ed0d686979b80a84fd0`。

固定载体 `30cfed0996003b6ebf4b5c51cc04f31ca9255440` 的任务 prompt/readset、完整 global prompt、用户指定 skill，以及 B8 根 AGENTS 均已全文读取。源／规格的 commit、tree、path、mode、blob、bytes、SHA256、实际范围见 [evidence-catalog.json](evidence-catalog.json)，可用 `git show <commit>:<path>` 恢复。报告不复制参考 Ruby 实现。

用户本次授权覆盖原共享容器禁止提交要求，唯一写集是本目录，唯一分支为 `codex/r8-external-legacy-manifest-currentness-20261016`，只普通 commit/push。隔离 worktree `/workspace/r8-external-legacy`；原云端规格 `/workspace/pokemon-essentials-clean-room`；只读 R `/workspace/pokemon-essentials`。Mac 历史路径单列，未冒称云端已核其备份或所有工作区字节。

## 分母与实际阅读

主载荷为 `planning/review-manifest-2026-09-19.md`，整体 4,127 行／1,420,152 bytes，SHA256 `7935075a2d5c14c0b5ad48c151a055ba1ee79783996afd2aea6c55c78c6c3d5e`，blob `14ee98eb2d9f62bf3d4451dab334ff6714b00723`。

| 本任务分母 | 已读／已判 | 未读／未判 | 主审未接收 |
| --- | ---: | ---: | ---: |
| primary 1933–2079、2849–4114：1,413 行／627,400 bytes | 1,413 | 0 | 1,413 |
| 内容段落：881 | 881 | 0 用途未判 | 881 |
| 有意义事件：156（第16–171轮） | 156 | 0 用途未判 | 156 |
| 阶段标题151、布局行381 | 532 | 0 | 532 |
| 四段导航：1–65、1835–1932、2795–2848、4115–4127 | 230 | 0 | 230 |

这些分母相互重叠，不能相加为需求数。事件是版本、复审或授权的完整语义单元，事件内分别处理行为／案例、批准资格、身份、技术边界和工作顺序；没有按标点、JSON字段或脚本方法数造“原子需求”。每个段落均连到一个事件，物理行仍逐项有 offset/长度/SHA；压缩摘要和详细段落均已实际读过，不由同义或同 blob 代读。

物理结构在首次 primary 阅读前冻结；156 个语义事件是在全文读完后的本次用途审查阶段冻结，未倒填审前时间。此前 v1 把所有881段一概保留为未拆解，混淆了历史用途判断与全引擎唯一原子分母；v2 已逐事件、逐段裁定。原 v1 和发布证据仍可从 Git 历史恢复。

完整台账为 [semantic-purpose-freeze.v2.json](semantic-purpose-freeze.v2.json)、[event-judgments.v2.tsv](event-judgments.v2.tsv)、[semantic-purpose-review.v2.json](semantic-purpose-review.v2.json)、[purpose-dispositions.json](purpose-dispositions.json)。后者覆盖全部1,413结构，不将混合行为段整体降为 inventory_only。原冻结文件中的 UNREAD 是冻结时状态，现态由 reading-ledger 和 v2 台账给出。

manifest 其余2,484行未授本上下文语义全文阅读信用，保留既有身份索引范围；不能把其处置扩给本次881段。两份正式 WP23（199行）和 WP66-B（313行）已全文读；另为2849五项交界实读具名完整 R 定义／连续范围和B8条款，详列 E-V2。其他当前formal的身份／路由不冒充本上下文全文读或全部条款反向接受。

## 现行用途的裁定依据

本次采用正向资格和具体后继，不以日期旧或没有B8字串推导无用途：

1. manifest:3–4 明定其用途为固定版本、供review按文件/身份/行号引用并保留旧条目；4115–4127 更明确“旧第170/171轮及此前所有行保持其时点”“旧hash不表示当前新字节”，并分开原输入批准、新输出与actual复审。这是旧事件的具体身份／阶段限定。
2. B21正式README/范围:5–9明确旧待审按原时点保留、九原输入限定批准不转授新输出。B8根 CURRENT-DELIVERY 与 R7导航提供更晚的27项有限静态交付状态；R8完整合同又要求全部当前formal/R重新审读。旧PASS、作者自检和计数均不能成为当前批准。
3. extraction-plan:3确实仍把manifest用于“当前执行进度”。因此其现行用途包括进度谱系、版本恢复、原输入批准出处、回归线索和曾经的范围限制；不能排除整个manifest。该引用也不把所有旧草稿和旧授权升为B8规范或本次权限。
4. 对每个具体事件，手写判断给出实际修正链和当前主合同：例如WP37首次PP/缓存/异色概括由100/101轮修正；WP61毒循环与missing-home由107/108轮修正；编辑器的No回滚、动画缓存、转换幂等、生成EV等均按其后继修订保留反例，不沿首稿强断言。

按段落职能分列：339段版本化行为／资格、77段混合摘要、42段原输入批准出处、113段旧预检过程、161段产物／身份记录、149段旧工作顺序与范围。所有881段均全文读；这只是用途分类，不是881个独立引擎需求。任何有效行为仍保留为版本化来源和回归输入，并连到当前正文、data/coverage、test-catalog及实际primary；身份字段的inventory许可不豁免同段其他断言。

旧“未执行”仅说明当时证据；本轮执行另计。旧“未读”不能自动转为当前缺材料或宿主limit。有限静态、不得用自检自批、源缺陷不理想化、clean-room不搬源架构等有效资格由当前AGENTS/global合同独立保留。旧stop/no-agent/no-push等是阶段授权记录，本轮服从最新用户授权。准确规则见 [purpose-rules.v2.json](purpose-rules.v2.json)。

## 两条关键现行继承链

N01 的1935/1937/1939及3380/3388/3397已逐次比较：v1空格→false概括由外层成员门纠正，Select公开返回门与BACK/Close两种确认语义经v3收尾。B8 WP23§8.1、WP66-B§2.2/4.4及SH34继承的是正确三层合同。正常入口、特殊负位置、直接有效队伍位置分列；空返回只取消本次新位置提交，先前完成的切盒/取出不回滚；直接调用删除缺最后可战斗门，不能据此补造普通UI队伍选择可达性。基础40×30容器、构造/保存登记和实际放置/替换/删除消费者均有具名范围；所有特殊位置后继、真实保存和宿主不由此全批。

2849 的五项旧一致性声称已各自完整用途核验，并新增五条有限现行事实：

- **载具**：事件201通过守卫排队后，两场景消费者显式保留游泳；直接省参传送取消，骑行按目的地许可独立处理。进入通知的force_cycling又有自己的时点。
- **计步**：运动开始的逻辑坐标／距离／条件离格，与完成后合格玩家入口的全局计步分开；强制路线／解释器早退保持，不能重复定义或用距离没增推步数必不变。
- **跟随／路线**：实际位置通行入口和strict能力分开；同轴1/2格、其他直接定位、临时through恢复及持久记录写回分别限定。两次一步尝试不承诺一定到达。
- **脚本异常**：SystemExit和名为Reset的类原样抛出，其他进入事件上下文错误；不等于成功或全回滚，终端宿主呈现另列。
- **缺图**：显式传送有音频时先读目标图而可提前失败，无音频可到重建；它没有读档重建ENOENT的调试选图/取消和非调试报错分支。前缀状态随入口和失败阶段不同。

以上逐完整定义/连续范围实读当前R与B8具体条款，同时完整接收固定WORLD的12个具名记录及其前提，未把整个贡献的FULL_READ转给本上下文。证据在 [world-interface-reception.v2.json](world-interface-reception.v2.json)、E-V2和正反矩阵。共10条有限事实映射服务这些用途判断，不能推广为其余所有域已通过。

## 其他primary的精确交接

[current-primary-contribution-routes.v2.json](current-primary-contribution-routes.v2.json) 对131份当前formal逐份绑定原冻结唯一primary、B8身份及20组固定贡献／readset路由，包含正文、附表/data/coverage与配套测试。当前源事实的全量接收继续属于这些不同primary；本任务没有把881段用途责任交走，也没有用贡献文件存在/计数/PASS代替语义接受。

路由固定于载体30cfed0，给出具体commit/tree/blob/bytes/SHA，而不只说“交给某域”。可用的WORLD、UI、CRE、CORE、Kernel、Move/Ability/AI/Facility、Developer及根共享贡献分别可恢复。CRE-D完整贡献在该固定载体的本路由中不可得，只绑定其准确readset并标UNRECEIVED，不能凭当前后来可能的进度补造。其他贡献已有的外域、历史和全量消费者OPEN也不在本任务中升级；准确其他primary接受和后续delta由主审接合。

因此：本任务primary的**用途未读／未判为0**；主审对本贡献的未接收仍为1,413物理行／156事件。不同current primary的引擎语义、材料、数据与消费者未接收另列，不能以这个用途审查清零全局台账。见 [interfaces.json](interfaces.json) 与 [gaps.json](gaps.json)。

## 疑点、执行和发布

`R8-LMC-H001`保留于proposals：WP66-B/audit的N01待处理与WP23/SH34闭合表述存在阅读资格疑点，连同B21明确保留旧阶段记录的强反向证据交主审。提出者倾向no-required，但实际不同上下文反证和root裁决尚未完成；当前新确认required为0，本地ID不是公共canonical GR8 ID。不整改。

新增业务执行全部 **NOT_EXECUTED**：参考观察、独立行为模型、游戏/宿主/Demo、原生媒体、真实存档/回放均0。静态文本、JSON、哈希、Git与远端字节回读只授TOOL_VALIDATION。实际model/effort/tier/speed/Fast、opaque session/log ID未回显，逐字段 **UNVERIFIED**；来源线程ID不认证执行ID。UTC按真实记录分阶段列出，未导出的平台完整I/O及最终平台退出时刻不倒填。

更新仍仅本报告目录、同一专用分支普通提交推送。既有v1 core/成功与失败回执保留；本次最终tip的commit/tree和全部文件远端完整字节回读由最终工具结果及交接给出，避免文件自哈希循环。主审需独立接收此有限完成的用途贡献，不能据此宣称整系统审查完成。
