# R8 WORLD：解释器、事件、跟随与路线独立子审

本子审基于 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`、R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。B8 workspace/formal tree、R tree及最初22个读集文件的 bytes/SHA/blob 均核符；开始时工作 HEAD 是审查发布后继 `f350383ed5208f66f72760b5a39c08892d61d247`，没有据后继 HEAD 改换受审基线。实际审者入口 `/root/world_interpreter`；请求配置为 gpt-6.1-sol / ultra / default 普速 / Fast off，实际 model、effort、tier、speed、opaque platform/session ID 均 `UNVERIFIED`。

本任务只写 `tasks/world_interpreter/`，未改 R、正式规格、planning/audit、历史、父目录或 root 公共状态，未 commit/push/install/spawn，未启动整改。`UPDATE_NOT_STARTED`。

全文实读7个指定R文件、3篇指定WP13正式文档，以及742行共享目录的全部上下文；目录assigned范围内169个真实向量均逐行阅读并作反向核对，包含附加MR18–22。本人合计读33个参考文本：22个全文、11个依赖文件为精确区间PARTIAL；另3formal及1catalog全文。ledger保留28段可得依赖未读范围，未把它们改标宿主/材料limit。非assigned目录条目只有上下文阅读信用，没有其所属领域的源支持批准。

正向基表手工登记136个语义单元、469个显式事实；晚补4单元30事实单独存于 `source-supplement.json`，没有改写父会话正在接收的基表。反向基表330条映射、1,007个手工拆出的断言键，覆盖96个命令矩阵行、46个路线矩阵行、169个assigned向量及3篇正文/附录/边界/导航。紧凑断言键需与 `clause-text-context.json` 的完整原条款及前提一起读。脚本只绑定位置、导出原文和校验引用，数量不是全WORLD/全系统原子总分母，也不因存在指针而授予批准。

重点保留并核过：页重选同页/有效新页/无页区别；NPC各触发入口与持续更新许可；三种消去入口及其索引差异；绑定图/当前图/跟随实例身份；脚本开关真值与严格布尔比较；101预读故障；隐藏选项后的取消映射；106/15/124及效果的时钟单位；强制安装、原路线保存、空路线、动作状态推进、任一行三前缀；跟随者保存数据/会话实例、领队链、条件位移和门编译210消费。正常、缺对象、取消无接口、异常及已提交前缀分别列明，没有把源故障理想化或设为未来永久实现结构。

共两条提案，均已由root实际独立读证后裁为有界required P3；本子审没有自行分类required。

- `GR8-WORLD-INT-001`：117携父事件编号但新子解释器取当前图绑定；相连A父/B子下，私有键分别为父[A,7]、子[B,7]。实际非提出者 `/root/world_full` 已全文反证支持有限P3缺项建议；root另直接读完整Interpreter/WP13事件/SceneMap及必要生产单元，于2026-10-16T04:47:36.604449Z裁为有界required P3，见 `../../adjudication/root-world-int001-reception.json`。历史精确根去重/全局接收仍OPEN。失联时父仍A/0、子B/0，不能说父也被重绑。原提案 `cf0d6a58…` 精确冻结保留。
- `GR8-WORLD-INT-002`：直接119缺标签时正常true返回、体内不改位置，外层推进下一条；B8矩阵和未决项仍只留“未验证”。完整候选另给正常命中/缺失/末尾/向后有限一步、合法与非标准作者列表、异常前缀对照。root实际非提出者全文读完整候选及直接119/121/末尾/外层推进、完整IM01–41，于2026-10-16T04:49:30.817146Z裁为有界required P3，见 `../../adjudication/root-world-int002-counterreview.json`。旧资格仍OPEN。

WORLD001/002保持root原canonical边界：001只有进入摆放失败且外层捕获继续后的同实例抑制；002保留单次speed0远移、26格对照、保存分叉及第二生命周期门。这里没有重复这两根因，也没有新增默认恢复、永久软锁、真实保存成功或宿主继续声称。

接口共11项，7项已有某一有限事实接收，7项仍含OPEN范围；两个数字不是互斥分区。WI-MENU和WI-MSG由UI_FULL实际有限接收；WRR的8个完整事实单元143原子已由本人全文接收，并保存精确selected snapshot。天气176原子本人未读，只有先前传回的类型/在途门短接合。WI-ROUTE/WI-TERRAIN/WI-IDENTITY已由world_full以WORLD-RCP-WI-003有限接收；WI-SAVE、WI-KERNEL、WI-FISH、WI-SHOP、WI-TRAINER及其它完整foreign formal/历史资格仍保留具名OPEN。收到某个有限源事实不等于WP05/09/15/16/17/29/60/65/66或整个WORLD通过；接口状态不是互斥统计分区，部分已收事实的同一接口仍有未收formal范围。

本轮没有参考行为、独立行为模型、游戏宿主、Demo、媒体或真实存档I/O执行，新增行为运行数0，全部向量 `NOT_EXECUTED`。只执行文本读取、JSON解析、位置/身份/一致性机械检查。完整工程/输入/媒体/宿主的缺失只限制对应运行观察；当前可得文本未读与依赖待收另外计。

读取的原始stdout/stderr在本次平台工具流；不可将它们声称为已发布公共raw stream。原静态读取命令的逐次UTC/底层exit未由本任务同时持久化，记 `UNVERIFIED`，不倒填。两次错误路径查询只显示文件不存在，随后准确路径已完整补读，不授错误调用阅读信用。后继 `validation.json` 只记录本次真实有限载荷校验及其实际I/O，不能替代语义或运行证明。

八件主交付为 `progress.json`、`identities.json`、`reading-ledger.json`、`forward-mapping.json`、`reverse-mapping.json`、`interfaces.json`、`proposals.json`、本报告。支持交付另有原提案冻结、INT002完整独立记录、source-supplement、完整clause文本上下文、WRR精确接收snapshot/receipt、生成脚本及validation。任务输出已完成供父接收；两项root有限裁决已收到，全局语义接收/历史去重仍OPEN，不能由本子审宣称56R/13formal或全系统完成。
