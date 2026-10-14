# R6-U13-R recording-save 独立辅助审读

冻结候选为 `00b45de642f07cee9953e42f04cce9c35d77346f`，tree `6708f580d5a02f874a1a24a95d7c0649b10c393b`。本审者 `/root/recording_save` 未参与候选撰写，只写本目录，不切分支、提交或编辑候选/正式稿。职责为 GR6-F-V005 与 GR6-F-S001，并核保存/播放接口。**V005：限定静态 PASS。S001：FAIL，唯一发现为删去 SF30 两个正确回归对照。** 源事实、活动保存可达性及故障前缀本身通过静态核对；不能据此把整个 S001 判通过。

请求配置是 gpt-6.1-sol / ultra / default tier / default speed。没有有效 actual 回显，model、effort、tier、speed、平台 UUID 全部 **UNVERIFIED**。root 已说明公开协作工具仅列 priority、不能传 default，回执只给逻辑任务名。本报告是非作者补充静态意见，不声称完成符合指定配置的正式候选验收，不签 CANDIDATE_PASS、INTEGRATED_PASS、正式接受或 CLOSED；没有启动 CLI 验配置。

固定正式输入为 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`；R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。以下源行号属于此 R，正式旧行属于此 main，新行属于冻结 candidate 镜像。源定位仅用于审计，不成为未来实现结构要求。

## 阅读与身份

先全文读根 AGENTS。提示通用合同、责任 ID 的七组与 original_full_proposal 均完整语义阅读；重复 payload_identity 用 JSON 结构核对；prompt 首个 JSON 与 `contracts/R6-U13.json` 相等。末尾 115 个共同恢复身份全部读过，恒定 commit/tree/用途字段作结构检查。大输出截断不算全文；责任 S001 的紧凑语义重读、原提案及 generator counter 的 675–735 补读修复相应缺口。

`reading-ledger.jsonl` 是本人后续实际呈现范围、输入 bytes/SHA/blob、argv/cwd/UTC 台账；`initial-reading-attestation.json` 诚实区分记录助手建立前的阅读，无补造原读取 UTC。五份正式/候选全文以成对完整文本审读：相同行同时标两侧位置，变更/删除行分别呈现，包含全部文本而非只有 diff。`full-reading-coverage.json` 核五份全文联合行区间均无缺口：WP56、WP58、WP53、combat 测试目录、pokemon 测试目录。`reviewed-diff.patch` 保存同一五份已审差集。

本人直接读固定 R blob：Palace 1–245、ActionSwitching 1–469；PauseMenu 1–321、MenuHandlers 文件 1–123、UI_Save 1–139、StartGame 1–126、SaveData 1–82、Value 1–284、SaveValues 1–127、Conversion 1–223、SaveConversions 1–420、Overworld_Metadata 1–183、Safari 1–196、BugContest 1–441；RecordedBattle 1–287、Challenge_Battles 1–144。必要交互消费者为 Messages 1–34 及 380–755（窗口创建/清理、完整消息显示、确认和选项单元）；Stats 150–197（含完整游戏时间及最近保存时间单元）。未把其它 Messages/Stats 行冒称已读。共享正式消费者为 WP09 全文 1–179、WP65 §§4/6 全单元 83–101/148–176、WP17 86–101/251–270。

七份原反证缓存均全文读完，并与冻结共同 bytes/SHA/Git blob 一致，全部固定 blob 完整字节读回相等。最初命名 R 对象库 ENOENT，后用本仓库已取回的固定 R 对象，不 checkout；最初 core `git show`/`ls-tree` 失败发生于本地 core 对象未可用，不能认定路径不存在。本审者当时的路径错误推断已撤回，失败 stderr 保留在 `evidence-recovery-checks.json`；root 的 `../counter-remote-recovery.json` 随后完整读回七个 fixed-ref/path，解除 membership 未知。远端回读为 root 证据，本人语义阅读为本目录账本，二者分开。原大对象取回完成后，本人追加七个 fixed5210/path 本地全文字节读回，全部 exit0/相等，core report tree 等于 `e1f08b1a8bada95edb1dcfbaf6b34417f787c771`，成功记录为 `core-local-recovery-success.json`，不删除原失败。

`identity-validation.json` 新核 41 个载荷检查：八份正式与八份候选冻结字节、18 个源单位的 frozen index、七个 counter 固定 blob及 root 远端回执。计数独立重数 QC49/WS36/PA32/RC29/SF40，均唯一；pokemon 测试 BP 起全部共享后缀字节不变。常数工具核 1/205 → 0%、3/205 → 1%、h24/m0 或 m1 的基础 30、r0 命中、正同值非严格增加。此为 TOOL_VALIDATION/DERIVED_CONSTANTS，不是原源或行为模型执行。两次受控文档验证因中文全角冒号解析错误 exit1，`attempt-1-*`、`attempt-2-*` 保留；修正后 exit0，stdout/stderr/独立退出及 UTC 收据俱在。本轮原参考执行、writer、真实保存/读档、完整模型、宿主/媒体/Demo 全为 0。

## GR6-F-V005：PASS（限定静态）

| 七组 | 实际判断 |
| --- | --- |
| identity_and_verdict | canonical V005、聚合别名 F-008、required/P2 保持；原提案 GR6-F-008 不是新根因，原历史待裁字段未重写。 |
| bidirectional_evidence | Palace 184–243 的概率、最佳候选与后段标记，ActionSwitching 9–33/77–105 的合法存活后备和登记，反向对应新 WP56 78–80、PA-P32 新测试 141；旧 WP56 78 的数学最大表述已被限定。 |
| premises_and_counterexample | 活使用者 h24、无状态修正/旧标记 false、无灭亡歌1/无招轮数>5早分支、唯一合法非活动存活后备 1/205、无换人阻碍、正常登记、r0：最大初值0不建立 best，基础30命中，后段先写标记 true，再登记并返回 true。3/205 相邻对照为1%，同基础30却走最佳早返，标记保持 false。实际 HP>0 与整数百分比0分开，不能把0%等同倒下。 |
| minimum_revision_contract | 新 WP56 78 正确说仅严格增大初始0才建立候选、同值保留先者；79–80 保持早返/后段差异、概率数值和随机门不变。没有加入未来API或永久缺陷兼容政策。无需修订。 |
| acceptance_and_regression | PA-P32 a–d覆盖0/1%、无合法后备及正同值；PA-P12 新121的“标记真/返回假”、PA-P24 新133早返保留原标记、P25未命中写假保持。概率表、状态加减和 h25/h50 门全文保留。常数核与静态推导分列，未执行换人程序。 |
| independent_adjudication | 对确定候选作新非作者反证：尝试“0%必倒下”“数学最大0也必建best”“两个分支的相同概率应有相同标记”，均被固定合法检查/严格门/早返位置否定。支持责任修订，配置验收仍 UNVERIFIED。 |
| dependencies_and_receivers | 唯一主批 U13；WP56 和 combat 目录镜像交 root 接收，追溯/矩阵仅 root 更新；共享文件其它 ID 的接合及整合后全文新验另行登记，当前意见不覆盖它们。 |

候选身份：WP56 bytes19053、SHA `fee7a028ad9b1db8fae48145b092b18efc89757db943eb6e3f234ace7c111368`、blob `0ff4bc7581fa77266d28ed2477c9dd68ed1edde5`；combat 目录 bytes33561、SHA `e6336cc59798b5f02dfe92c0e799344a3aa652627b2adfacbe6861562537f1c8`、blob `cc28e3400d3bab787ce66c18156c45bcba6e5829`。路径在 candidate `mirror/deliverables/final-specification-set/` 对应正式路径下。

## GR6-F-S001：FAIL（唯一缺口：正确测试对照被删除）

| 七组 | 实际判断 |
| --- | --- |
| identity_and_verdict | canonical S001、聚合别名 F-009、required/P2 保持；不把普通 Quit Game、专用模式退出、Save 隐藏另算根因。 |
| bidirectional_evidence | MenuHandlers 101–116 无 condition 的项保留；PauseMenu 254–272 专门 Save 有系统/区域/活动门，304–321普通 Quit Game 无该门。UI_Save 100–128 → Game.save 111–125 → Value 48–52/279–283 → SaveData 57–61，SaveValues 3–8/76–81整体玩家/全局对象，无活动对象排除。Safari 42–47及 BugContest171–196产生活动和分离队伍，Metadata31–34持有。新 WP53 15/239–241/246–247正确接合。 |
| premises_and_counterexample | 默认正常持久值/对象图、地图/UI/确认依赖正常，Safari区域内活动或未到期有效捕虫，无无关更新回调；接受普通退出、保存及必要覆盖，writer成功前提下serializer可收到活动Safari字段，或 player单员+global备用队伍/K/计时起点。仅证明可达，不证明实际文件写入或计时恢复。模式退出分别回起点/判奖，普通退出没有这些动作。 |
| minimum_revision_contract | **FAIL**：旧 SF30 formal40 的 b“正常结束后保存→载入，非活动会话及统计持久、运行时刻语义未证”、c“无 Safari/捕虫相关转换”都是正确控制。新 SF30 candidate40 只留下模式可见集合，b/c被删除；SF36–40不含替代。新 WP53 246–249仍正确，不能代替测试目录中的具体控制。 |
| acceptance_and_regression | **FAIL**：S001-A–E核心设计由 SF30/36–40覆盖，失败前缀和异常界限正确，但删除上述正常/转换对照违反通用合同保留正常案例及最小改动要求。root独立搜索 SF全文和 WP53 244–249后确认、采纳此缺口。 |
| independent_adjudication | 最强反证为更早守卫/handler覆盖/序列化排除，固定已读默认链中无这些模式门。支持核心源事实；反对当前整 ID通过，只因具名目录回归损失。报告没有转授作者工具PASS/旧PASS。 |
| dependencies_and_receivers | 唯一主批U13；WP53、pokemon目录交root。WP09持久前缀、WP65正常返回退出及四组合、WP17更新机会、活动时钟未证都要在实际整合版本保留并复验。补回两个 subcase后重新绑定改动载荷并作非作者复审；不能让原审查覆盖补丁。 |

失败/拒绝证据具体边界如下：拒绝 Quit Game 只刷新重开，正常保存未调用；接受退出后拒 Save 或满足异存档警告门时拒覆盖，保存画面正常返回 false，Quit Game忽略返回仍执行场景置空。接受保存后先清新游戏未保存标记；Game.save先校验调用参数，再写 safesave、保存计数、magic、最近保存时刻（Stats173–188可刷新游戏时间和锚点）；随后取值/校验及写档。被捕获 IO/SystemCallError 只减保存计数，其它完成前缀不回滚；取值类型错误不在捕获集合，正常清理及退出尾部不保证到达。参数校验在正常持久前缀前、取值校验在前缀后，二者不能合并。消息正常返回和无无关回调是必要条件，未承诺冻结时钟。WP65旧“进程结束”只作为脚本场景置空定位，不能继承为真实宿主进程实测。

**最小修订**：在新 SF30 保持当前三项可见性对照，另补 d“正常结束后正常保存并加载：会话仍非活动、统计持久，计时起点等运行时刻语义未证”；e“固定转换集合没有 Safari/捕虫专用转换，普通载入无此格式迁移”。保留原门与静态/未执行标签，不恢复“活动中均不可保存”。若只作为 SF30 的子例，不新增ID，SF总数仍40；无需扩大源/宿主执行。该文本供唯一写者或作者在新版本中落实，本审者未改候选。

补回 c 的源侧独立核：Conversion 51–65/158–209按版本选择及运行登记转换，SaveConversions全文十四个默认注册分别处理树果、跟随者、寄养、背包、玩家编号、图鉴、选项、天气、统计、标记、电话、笛子和碰撞统计，不访问两模式会话字段。固定 Data/Scripts 全域 `register_conversion` 查询只定位该机制/默认集合；Save data五文件的 Safari/BugContest 有界负查询 exit1/无匹配，与全文阅读合用，证据见 `conversion-negative-evidence.json`。结论仅是当前默认集合无专用模式转换，不是全部存档没有迁移、不保证任意插件或旧对象图的加载成功。

被审失败版本身份：WP53 bytes51237、SHA `1a9c9581d7b91bf5e4dd5474b9e2f4fef4115e795d7122663eb743e55bfaa999`、blob `5acc4f03fcecd49001325ff218034f00aff8a20a`；pokemon目录 bytes61342、SHA `13a364b5184c706b5214939f397a0690ffe7c0346c7f1a93a586a21fbd5acba2`、blob `d694096c7f706a2b8a7e67b1525243794c589927`。

## 记录、播放与精确历史接口

源 Challenge_Battles40–97：调试跳过清临时记录；正常包装完成恢复后先清临时记录，仅胜/负/平重新放导出；异常早于此位置不保证清空。102–105提升把临时值写全局再清临时，无临时值时也可覆盖旧全局为无值。播放不是文件删除或记录写入。RecordedBattle121–125每命令阶段建四席；198–222只在玩家侧消费一轮，固定索引0–3处理两侧/伙伴槽，AI侧不再次推进；4以外不消费。默认1v1的非空2/3席访问不存在战斗者由具体指令族决定，逃跑只写决定例外。WP58新63/67/83/136/156保持这些数值/清理/残留边界；不新增mandatory或把具名额外观察当完整播放PASS。

本人从固定 `d81562b…:review/remediation/20261003-prepare/batches/B13/author-draft-1/original-and-acceptance-controls.json` 实读 `/controls/0,3,6,7/complete_current_control_fields`：B13/003保必要模式、格式与行为身份，移非必要源组织；B018数量与行为存在分开；B028连续裁判/补位保留；B029完整替补消费者，不能用直接调用数量删域。`historical-scope-extract.json`保完整责任投影；003原全扩展与作者具名投影不全等是合法范围投影，不是源事实缺陷，`identity-validation.json`已分别核共同字段和投影成员。

新全文显示 PA-P12/P24/P28、RC-W16/W22b/W24/W25/W26及 WP58 §5.2 保留；新数为RC29且W22b未丢。WP53伙伴/force-single前提与SF35均保留，保存时玩家单员不推出大会一定接管。history_payload独立 peer 回执核固定 B12/B026 original `/87`、approved `/GIR-FD82-B026`、legacy `/controls/84/historical_identity_scope_reuse`及B13资格；它是peer历史证据，不能写成本审者已全文读全部大历史文件。共享pokemon非SF后缀完整新读且字节不变，R3/R4/R5其它资格由具名历史辅助审查承担，不转移旧PASS。本报告仅在实际相交span上给新判断，保持R1原WP限定、R2 229/21/341、R3 23/76、R4当前17/76与B5旧16/75、R5唯一92 CLOSED的原分母与未执行界限。

整合条件仍为：S001目录修订重审；root唯一接收，收齐共享候选后核实际全文与接合；按精确历史资格/生产消费接口复验；配置障碍准确登记并按后继授权处理；随后分别记录正式接受与关闭。当前没有整合后载荷，本报告不覆盖未来编辑。真实保存/重载时钟、宿主窗口/进程、地图事件可达性、媒体/完整Demo和未绑定插件组合均未执行，继续保持未知。
