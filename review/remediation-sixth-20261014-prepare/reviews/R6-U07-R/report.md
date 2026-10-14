# R6-U07-R 独立候选审查

结论：**CANDIDATE_PASS，7/7，实质退回项 0**。本结论只绑定作者发布 `6f6521983006519a0b55a5414177c71a2b59810e`（workspace tree `53f252f3c2de955f736cadd6180e9c84b92eab79`）下 `candidates/R6-U07/` 的 tree `13ab6f277dba32ba4d4535aca1f8fc450346dec9`。语义 core 为 `6c4966cb1e9e7936d33faa2f79aa2ff368d66492`；三个 mirror 在 core 与发布之间逐字节相同。正式 deliverables 仍是 baseline，本报告没有作整合接受或 CLOSED 登记。

审者逻辑身份 R6-U07-R，由当前独立任务直接完成，没有委派审查、修改候选或作者文件。作者任务为 `01a13ab2-df02-712f-a724-7b7695163036`。委派来源 thread 为 `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`；它不是当前运行任务 UUID 的回显。用户请求 gpt-6.1-sol / ultra / default / 普速。实际 model、effort、tier、speed 及当前平台任务 UUID 未得到可验证回显，全部记 **UNVERIFIED**；没有用 CLI 探测模型配置，也没有因此停审。

## 固定输入与读取边界

已先完整读取适用根 `AGENTS.md`；没有适用的嵌套覆盖。准备提交 `469a268b92daed7b4d28d7fd0da75520cbb7228f` 的完整审者提示 `prompts/R6-U07-R.md`：371765 bytes，SHA-256 `d787ad55e3965afafb1332c7b085c2555dfd86e8fdfcd15607b309ce85cdd1df`，blob `f8b65f62b4101faf554f9898fbe014aaedb3950e`。提示全文分段读完，内嵌合同与独立 `contracts/R6-U07.json` 解析后精确相等；独立合同 258822 bytes，SHA-256 `a0692c80b502e9e4b87b9781b7f7d081d618d27e9fae855e6668dab1a949b9a5`，blob `b935030154677a9dec372f2b4f70941ea5b38a04`。七个 ID 的七组合同、原提案、原反证、root 收窄和接口分别审查，未以作者摘要替代。

正式 baseline `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`；固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。七份指定源码共 5130 行全部读取；另读取缓存单元、焦点常量及必要的战斗包装、Move/Target 与 PBS 夹具上下文。参考只通过固定 Git blob 读取，没有 checkout 修改、加载或执行源实现。

三个正式文件与三个候选 mirror **全文**以 FULL_TEXT_JOIN 阅读：每个相同段输出一次并同时标 B/C 行号，每个不同段分别输出全部 baseline/candidate 行，没有省略相同上下文。WP74 472/495 行、目录 327/327 行、WP67-A 348/348 行。精确身份与候选 diff 在 [paired-document-identities.json](paired-document-identities.json)、[identity-and-diff-checks.json](identity-and-diff-checks.json)。WP74 与目录修改，WP67-A 逐字节未改；全文语义检查没有发现它必须同步修改的冲突。

以下简称 SE＝SceneElements、FN＝Functions、IP＝Interpolation、CT＝ControlsButtons、EX＝ExportImport、BP＝BattleAnimationPlayer、PA＝Scene_PlayAnimations；完整路径、固定 blob/bytes/hash 和实际读取段落见 [read-journal.jsonl](read-journal.jsonl)。WP74/Catalog 行号一律是精确发布 mirror 的行号。

## 逐 ID 独立结论

### R6-DX-AN-001 — PASS（required P2）

SE 678–694 的同图案计数只遍历 0–59；存在性、锁定与被删图案仍读实际选中槽。SE 652–658/830–834 的 Delete 消费该门，579–590 的 Clear 同样使用当前帧守卫。FN 1063–1074 的重编号能把第二使用者从 2 交换到 60；188–211 的滑杆确实允许 60，不是不可达外部构造。

静态逐步验收：未锁槽 0/2 各有使用者时计数 2，Delete 0 可通过；把 2 换到 60 后仍存两者但计数 1，Delete 0 拒绝且不写；换回恢复。只有槽 0 时拒绝，锁定时拒绝，普通图案不受最后个体规则拦截；不存在的选中槽先走既有前置门。Clear 被拒时按既有默认属性处理并保留坐标、图案、焦点及锁，跨帧操作仍以编辑器当前帧同号槽为守卫。取消重编号不产生 60。

候选 WP74 120–123、193、243、470，Catalog 116（AN-M05）、282（B20-C025）决定这些结果。SE 634–650 的快照粘贴/解锁，810–819 的 TAB 按实际帧长度循环，BP 407/802–806 的常规播放槽范围全部保留。没有把计数范围扩大成存储、复制、TAB 或统一播放范围。

### R6-DX-AN-002 — PASS（required P2）

FN 168–173 的 Delete 换集合成员 A→B 而不重绑 canvas；1106–1120 的 Focus 读写当前集合选中成员，仅要求 canvas.update。SE 717–727 的新增单元及 FN 属性/Batch 页面读画布绑定对象；EX 27–45 的 Export、FN 994–1001 的 Save 使用集合成员。缓存加载返回集合别名，清缓存不回滚仍持有的旧引用。

有效位图及菜单宿主正常、A 默认焦点 4：Delete→BACK 后 canvas 仍 A、集合为 B；Focus Target 把 B 改为 1，A 仍 4；add cel 用 A 的 4；save/export 持久或导出 B 的 1，不含加在 A 上的新单元。正常同对象 Focus Target 后新增取 1；Focus 取消不写；明确 Reload B 后新增取 B 的 1。删缩后选中成员 nil 的失败点在 Focus 菜单前，不能许诺显示或恢复。没有把普通同对象路径误写成一律脱离。

候选 WP74 56、225–227、360、440 与 Catalog 120/123 对齐上述引用、保存和取消前提；全文 §3.2、§7.1、§7.4、§11.1、§16 的生产/消费链相容。

### R6-DX-AN-003 — PASS（required P2）

BP 675–697 在播放器构造时取精灵原点与中心；818–840 后续单元写入不会重捕获这些中心。762–765 用已设置直线变换，749–751 是显式 target origin setter。PA 521–564 正常核心建立直线并正常退出恢复精灵；568–579 的球爆是显式覆盖例外。SE 451–488 的预览在 +64 边框偏移之前建播放器。

静态普通对照：捕获 user center (128,224)，之后槽 0 的 user-focus 请求 X=200；同帧普通槽 2 的 user-focus X=128 仍基于捕获中心，请求为 200/128，预览边框后为 264/192。target-focus 同理；Screen 不随中心，双方焦点使用既定直线，无移动时结果与旧普通例相同。没有实际截图、宿主量化或异常退出恢复保证。

WP74 333–335、Catalog 134（AN-M23）足够表达捕获时点及例外。WP67-A 全文，尤其 §9.4 的实际位置变换/独立球爆描述，与固定中心不冲突，未把每帧更新精灵误当每帧重建原点；因此 WP67-A 只核不改可接受。

### R6-DX-AN-004 — PASS（required P2）

逐项核 FN 831–894 的构造和消费，CT 388–420、496–584、751–839 的即时钳制/可选值门。Batch 的 11 项独立值：Pattern [−2,1000]/0，X [−64,576]/0，Y [−64,448]/0，Zoom X 与 Y 各 [5,1000]/100，Angle [0,359]/0，Opacity [0,255]/255，Blending [0,2]/0，Flip False/True（0/1）默认 False/0，Priority 四选项 [0,3] 默认 Front/1，Focus 四选项 User/Target/User and target/Screen，由 canvas 动画默认及兼容映射给出，缺省和兼容旧值 0 均显示 Screen（4）。没有用单元属性当前值代替 Batch 的独立默认。

静态相邻对照：旧 Opacity 17，只勾复选框即写默认 255；仅勾 Zoom X 写 100，不触及 Zoom Y；仅勾 Priority 写 1。未勾或 Cancel 不写，值 0 勾选仍写。默认 focus 旧 0/缺失分别按既有兼容映射，实际菜单选择映射保留。已有共用属性别名仍会联动，空单元及写入门不变。

Gradient FN 624–677：duration 0–50/current或新 5；X/Y ±500；opacity/RGBA 0–255；非 nil 当前值决定初始勾选。合法兼容 cel X=550 打开页面即把工作值钳至 500，确认且勾选写 500；Cancel 仍 550；正常 X=20 仍 20。Y 的相邻负边界同理。全部未勾返回 false 而不写；至少一项勾时未勾项目返回 nil。候选 WP74 256–271、317、Catalog 127/133 含完整表和这些消费边界，R17 即时钳制保持。

### R6-DX-AN-005 — PASS（required P3，覆盖缺口）

原 root 将本项收窄为具名失败覆盖，不能扩成旧全文一律承诺事务回滚。EX 47–84 的保护范围止于读/解码/类型/转换/集合替换；89–126 的转换跳过 nil 帧。SE load 与后续绘制、FN 返回菜单后的更新在该保护范围之外。

类型正确、length=1、frame0=nil、graphic=""、有效空 timing 的外部对象，且文件/菜单/消息宿主正常：解码和类型门通过、转换跳空帧、集合旧 A 已被替换；load 设置 current0、空 graphic 不取素材并 invalidate；返回后 FN 989 的 canvas.update 经 SE 907–919/696–705 消费 frame[i] 时失败。无更早结构守卫，也无恢复 A；缓存共享成员已替换。集合保存、退出清理、BGM 恢复尚未到达；显示/进程/宿主恢复结果未知。

正常有效 frame 导入仍成立；坏编码、错类型及替换前转换失败保留旧集合槽，和越过替换点后的失败分开。WP74 364–366、476、487、Catalog 136 足以决定前缀及停止阶段，不扩大成完整异常事务或未来应保留缺陷的 policy。

### R6-DX-AN-006 — PASS（required P2）

IP 229–263 将 path 与显示 points 分开；263–353 重开 Curve 清显示点，不先清 path，未显示线 BACK 不替换 path；仅在 showline 成立后生成新 path。406–422 的 OK 按已有 path 门、先扩帧、再逐点写 X/Y。

同窗已有非空 P→重开 Curve→端点未齐/线未显示→BACK：显示点清除但 P 保留，OK 按 P 写 X/Y并按需扩帧。首次 Curve 早 BACK 仍 path=nil，OK 不写；显示线后 BACK 则提交新路径。外层 Cancel/BACK 不写。Freehand 首次等待 ESC 以空 PointPath 替换 P，OK 先扩帧再首点失败，扩帧留在内存；记录阶段 ESC 保留已绘点。三套采样的 N / N+2、取整、仅用前 N 和边框坐标全部保留。

WP74 281–288、473 与 Catalog 129 分清旧路径保留、首次无路径和空路径失败。没有把“离开子模式”一律等同外层取消。

### R6-DX-AN-007 — PASS（required P3，仅必修边界）

IP 310–333 的自动中间点采用 0.3333/0.6666，而非精确 1/3、2/3；端点 (0,0)/(300,0) 的数值请求约 99.99/199.98。宿主 Sprite 坐标量化未验证，不承诺整数或实际像素。自动点创建与动画写入不同阶段，外层取消仍不写动画。

WP74 281/473、Catalog 294（B20-D024）补齐必修。原显式拖动四控制点 N5 示例保留：P0=0、P1=1、P2=8、P3=11 的三段 Catmull-Rom 在参数 0、1/4、1/2、3/4、1 请求 X=0、0.3046875、4.375、9.1015625、11。独立精确算术复算仅作静态计算，不执行参考曲线或宿主。此例没有偷换为自动默认中间点。

一般 N 逐步浮点加法端点的位级差异继续是独立 optional；原一般曲线的含端点表述未因本批新增为强制浮点兼容裁决。没有把 optional 并入失败标准，六既有 policy 与运行 limit 均保持。

## 必要接口与历史回归

本次新结论来自上述源码、全文及逐步推导。作者 317 工具检查及 43 载荷回读只作作者证据身份上下文，没有当作本次独立语义验收。七组合同及全部验收/正常/取消/失败对照的结构记录见 [per-id-review.json](per-id-review.json)。

R1 原 WP74 recheck-v4 的 18 项 CLOSED 只保留原 scope。重新核查本次直接触及的最后个体守卫/槽 60、Delete 当前末尾索引、剪贴快照与 Insert 别名、三位图入口、路径取消与先扩帧失败、即时钳制、预览焦点。未改的排序、命名编译、组织器取消、文件矩阵及数量仍在全文，没有据旧 PASS 冒签全模块。

R2 229 控制 / 21 批 / 341 贡献的分母保持独立。已从原 canonical `c0ff33024aea424c68d29f9778fe7c8e807d21e8` 的 28187068-byte regression-legacy-scope 取精确 B20 资格与导航，核对作者七个摘录字段逐值相等，并独立增加相关 B20-C031 等 scope。B20-C025（全帧操作/TAB与0–59工具）、C026（共享音画层/持续0/175而非150示例）、C032（窗口坐标/曲线钳制）、D024（三套采样）重新对当前源码与全文验证；B20-C020 正常退出与异常边界保留；GIR-FD82-003 没有引入源类/API架构要求。未选中的大文件记录没有宣称全文语义审查。

R3 required 23 / criteria 76 与 R4 required 17 / criteria 76，及 B5 qualified 16 / 75 没有混算。按固定历史导航筛选受影响 path/span。R3 数量/命令消息等在 WP67-A 相邻领域没有改动，保持 NOT_AFFECTED；没有猜配动画 finding。R4 GR4-M10-004 的完整默认映射和三条验收重新核查 PA 412–518、战斗 showAnims 包装、raw Move category/Target、PBS 及 WP67-A §9.4.1：六槽/18类型、火系 10→20→30→空、OppMove 11 优先、精确 hitNum 与默认路径分离均保留。映射号是条件夹具，未加载媒体或播放。其余共享目录世界编辑器条目未改，不转移旧语义 verdict。

R5 唯一 92 CLOSED 保持原冻结候选/实际审查及精确 scope；原 OPEN/WAIT、失败与后来纠正的历史不改写。GR5-M12-202 animmaker 的文档限定 optional 不变。当前影响不存在恢复“源组织必须照搬”、原生媒体已验证或源缺陷永久兼容的结论。具体范围见 [regression-review.json](regression-review.json)、[history-origin-verification.json](history-origin-verification.json) 和 [history-round-navigation.json](history-round-navigation.json)。

## 限定与交接

本报告是静态文档候选验收；参考实现执行、行为模型执行、宿主、图像/音频/输入实测、Demo、真实存档/网络/生产服务均为 0。唯一执行的是审查读入/身份校验/独立有限算术/报告验证及 Git 发布工具。工作流截断输出与错误的读取尝试已在 [execution-and-read-coverage.json](execution-and-read-coverage.json) 如实保留并说明恢复方式，没有转成候选 FAIL。

只写 `reviews/R6-U07-R/`。没有修改候选、正式 deliverables、公共 ledger、Mac、main，未 force/delete/merge。没有最小整改建议，因为未发现实质失败；不新增行政验收要求。R6-I 是唯一正式接收与共享文件写者；随后实际整合、共享全文独立复审、接口与精确历史回归、正式接受、最后 CLOSED 仍分别需要登记。本候选 PASS 不替代任何后续阶段。

发布回执采用有限 core→publication 两步，最终固定报告 commit/tree/入口及全部新增载荷的远端全文回读结果见交接回复；[publication-receipt.json](publication-receipt.json) 只记录 core 的已完成回读，不自称覆盖尚未提交的自身。
