本任务是实际独立上下文 `/root/world_topology_audit` 对 WP11 世界拓扑、转移、生命周期、恢复与命名材料的有限静态审读贡献。它不代表整项 world_full、WP12/13 全部条款、整共享测试目录全部推导或整系统完成。`UPDATE_NOT_STARTED`；未改参考、正式规格或其它任务目录，未 commit/push、安装或再 spawn。

固定输入为 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。首次看到的工作树 HEAD `7478d8daf357d569ac12bea211b4b5f257861930` 是合法报告后继；按固定输入 blob 核验，没有要求报告 HEAD 等于 B8。57 个实际 source/formal 载荷均与固定字节相符。完整 prompt 36,653 bytes / SHA256 `63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b`、根 AGENTS 与 3,598-byte review-SKILL 已全文阅读并核身份。该 skill 自身说明不用于审计报告；本报告按审查合同保留证据与过程边界。

已全文读 29 份参考 Ruby、2 份参考 PBS，以及 WP11、WP12、WP13 主文与 742 行共享 engine catalog 四份正式文件。另 22 个载荷只读具名完整定义/连续范围，其余真实未读在 `reading-ledger.json` 的 `unread_ranges` 明列。Game_Map565、MapFactory506、Character1023、Event302、Player616、Interpreter454、StartGame126、Scene_Map252、Overworld750、两类元数据、跟随及显示/天气、通知与存档值均按完整文件或完整具名定义阅读；大文件连续分块无缺口，早期截断合读输出不授予完整信用。机械结构索引是词法方法头和同缩进末端索引，**不是 Ruby AST 或完整分支解析**；1,245 个索引方法头中 751 个完整定义已读，330 个连接到本次具名事实，其余逐项保留其它领域/未读处置。

WP11 冻结为 89 个行为条款行单元、304 个显式拆分断言，其余非空行均作标题、追溯或明确范围处置；31 个事实和 7 条接口见正反矩阵。所有 WP11 行均有本轮阅读与反向支持或具名候选/条件，未把对象指针或名称存在视为支持。共享目录全文阅读与语义反查分开：612 是表行数，含标题/辅助行，**不是测试或需求分母**；其中 79 行选择拓扑、恢复、命名与身份交界反查，其它 533 行明确在本任务反查范围外。WP12/13 只接受通行、实例、解释器绑定身份、跟随转移与冲浪临时字段这些交界，不授予两 WP 全部条款通过。详细 clause 分母形成于完整 WP11 文本阅读和详细源读开始之后，是**迟冻结**，不能倒填为审前已冻结；初始文件身份冻结和这一程序性局限都保留。

已连通的有限链包括：连接作者字段→编译接受→运行锚点/双向索引/零尺寸过滤→首有效目标；NoAdd 查询→实际建立/通知→地牢种子/暂存前缀→不驻留；跨缘通行与同图双端通行区分→身份/落位→音乐与天气输入；显式请求/执行分层→车辆/音频缺图分期→重建通知位置→跟随/显示；读档进入通知→局部记录清空→更新→条件恢复（含异图同 ID through 真异常）；命名共享材料→全局玩家/继续预览/保存信息窗→显式内容保存/材料重载。物理地图、Demo、声音、像素和真实保存往返均没有从静态链升级。

提出两项独立根因。原 `proposals.json` v1 保留为 15,315 bytes / SHA256 `ff22cdc95393a3ac21a5930134540e8e5c562be636db3e3e509a1207aa149845`，来源完整身份在 `proposal-evidence-bindings.json`。实际非提出者 `/root/counter_world_first` 已独立反证两项并建议 required/P3；root 已有限采纳两项为 required/P3，严格保留独立反证的新前提；提出者没有自裁，全局/历史及接口关闭尚未完成。

- **GR8-WORLD-001**：一次已进入邻图摆放的异常可保留后继摆放抑制；明确外层捕获继续并撤掉失败条件后，同实例再次摆放、同实例重建与清帮助缓存都不提供独立恢复。正常完成、进入前失败和末尾之后失败分开。没有默认继续游戏、永久软锁或未来复制私有标记的保证。
- **GR8-WORLD-002**：有连接分支的最终显示范围门也检查当前图。人工20×20 A/B、512×384、SnapEdges假、玩家静止，明确速度0右移100格后只给一次生命周期，A/B显示12800/10240均达到排除门3328，可正常返回空驻留集合而全局当前引用仍为旧A；紧接当前图查询才报空。右移26格只删A、保B，容器可转而返回B而全局仍旧A。第二次生命周期、默认非零速度循环和普通保存UI时机不得套同终态。直接在精确空表观察点保存/预览只是有明确前提的后继链，非实际文件观察。

002 原提案 public scroll 定位 `507–530` 不完整，已由独立审者指出并由本人编号重读修正为 `497–518`；原 v1 不覆盖，准确更正与26格边界、独立报告 SHA 单列于 `proposal-errata-and-counter-reception.json`。两根因只共享未来写文件，不互为事实前提，不合并成一项。最小写集均是 WP11 和共享测试目录；WP16 相机、WP09 持久值、WP65 预览是同步接收边界。保留现有临时查询/局部恢复、同图/异图入口、音乐失败分期、进入/离开通知、六格门、无连接分支和全部正确旧向量；未来兼容参考异常另由 policy 决定。

还完成两项实际非提出者反证：`refutation-pbsw002.json` 支持最小 P3 修订，默认 PBS[051] 已有识别的 Dungeon=true，而缺真实 Map051、编译 dat 实际装载和可达性分别未知，WP14 两处与 WP11 L37 不能把可得标记本身并入缺材料。`refutation-ui001.json` 则确认保存信息窗在拒绝前可修改共享名称的源事实，但提出有效反证：WP65同节已明确确认前更改不回滚，按信息窗完成后→No分支观察点可限缩“无副作用”，故建议 no-required 或 optional 澄清，root 已选择 optional，不计 required。PBSW002 已由 root 有限采纳为 P3；两项意见都没有把命名内存变更误作写盘。

具名接收 `/root/pbs_world_record_audit` 的 CONNECTION/MAP/GLOBAL/TOWN 有限字段事实、19 条连接行值与 GEN01–GEN10 接口，按本轮 Map/Factory/MapMetadata/compiler/命名实际 receiver 核前提。本人另全文读默认 metadata33 / connections40 与 Metadata81 / PlayerMetadata95 / GameData 通用定义，未把其它 reader 的全文件信用转到本上下文。地牢构造/种子入口347–450与通知消费者1063–1107自读；深层生成数学不作本任务全审接受，GEN09/10 精确子事实已接收并核 caller 前提，覆盖 GR3-DQ06 的 antiring2×2 与已映射密度0失败阶段；其它 DQ 外层案例保留给定生成结果前提。没有继承旧 PASS 或 kernel 报告总论；通知、Value、编译实际定义另读，未见到的 kernel/CRE 全条款不宣称接收。

真实执行边界：参考行为观察0、独立行为模型0、完整宿主/Demo0、原生媒体0、真实保存重放0；所有行为向量 `NOT_EXECUTED`。`ruby --version` 实际返回127，不安装。当前目录有限资源 probe 未找到 Map*.rxdata / CommonEvents / System / Tilesets / Game.ini / Game.rxproj，仅限制对应真实地图和宿主观察；可读脚本和条款缺读继续记未读，不列 L01。57项身份、JSON解析、引用与范围机械一致性检查通过，只授 TOOL_VALIDATION，不授业务成功或全域覆盖。

请求配置为 gpt-6.1-sol / ultra / default普速 / Fast off；实际 model、effort、tier、speed、平台 agent/session ID 均未回显，逐项 `UNVERIFIED`。逻辑任务路径不冒充平台 UUID。开始字段是首次本地登记时点，晚于初始阅读；真正 turn 起始 UTC 未回显，单次早期工具读取 UTC/stdout/stderr 未单独落盘，不能倒填。准确分离见 `progress.json`、`execution.json`。root 可从本目录证据接收此限定贡献；全局剩余阅读、其它工作包/接口、历史资格和最终发布均不由本任务冒充完成。
