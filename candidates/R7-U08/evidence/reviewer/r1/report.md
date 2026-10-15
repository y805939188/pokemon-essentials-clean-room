# R7-U08 r1 独立冻结候选复审

结论：四项均为 **PASS_SCOPED_CANDIDATE**，仅绑定下列候选字节和必修局部合同。没有确认实际整合 PASS、正式接受或关闭。实际整合、CG06 共享接收、新 R7-IR、直接/传递依赖及历史回归接收门仍待 R7-I 完成。

## 身份与固定输入

- 审者真实环境回显 `CODEX_THREAD_ID=CODEX_SESSION_ID=01a13ff0-a716-77b3-bbda-7ad40ff90032`；当前角色上下文 `/root`，容器会话 `26695140ff814728b2bdb61aa10da835`。这是环境暴露的实际 ID，不冒充未取得的父级创建 API 回执。真实工具 PID/UTC/退出另见 `tool-evidence/identity.*`。
- 作者外部 task 为 `01a13f7f-ac68-740b-922a-7bf690ebb024`，由固定派发和冻结输入绑定，与审者可见实际 thread ID 不同。作者原证据中的内部 task/context UUID 未暴露资格原样保留，不用相同角色名 `/root` 推定同一上下文，也不伪造内部作者 ID。
- 本次派发固定提交 `95c260d8f3fb4a171675dde877137fcd4c2f1c8d`，实际 tree `577c350364bb4e2eb712325a9095d53d29eeeeb3`；`review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U08/reviewer-dispatch.md` 全文已读。
- 冻结提交 `aa369555b0e8b6c8b077f964b54ed63d3b924f26`，tree `08bd0f362c74ef7645b5bbd70b557489c122ae29`；精确输入为其 `review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U08/candidate-input.json`，72,639 字节，SHA256 `fd2d1379bf6ae8cc753eb2674d333f09ecf6371d268e5f32b61fd36b0873675a`。
- 实际候选提交 `d6e07340aa14eb8b45728020cad018a22d7559b2`，tree `ed37cf1d27414f8f7411f079f1f717e55f3213a3`；唯一作者分支 `codex/r7-u08-author-20261015-wave1`，未 checkout 或改写该分支。
- B 为 `e646432c644dec04d306842cc5a559a29c718fbc`，正式目录 tree `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。R 为 Maruno17/pokemon-essentials 的 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，实际 tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。

先读实际项目 AGENTS.md，随后完整读取固定恢复工具、本批两份恢复计划和原四记录七组合同。原合同固定 `f622356f3beb9e84ea8cff9db07c7fb382565d3f`，不是浮动 HEAD。工作区 `.agents` 为空，B 和派发提交均无跟踪 `.agents/skills`；没有声称应用不存在的技能。合同禁止子任务，本次创建子任务、其它作者/reviewer、模型 CLI 均为 0。

## 独立恢复与字节门

未假设共享目录。原合同/源/反证恢复至 `/workspace/r7-context/R7-U08-reviewer`：**39 文件 / 7,698,787 字节**；候选另恢复至 `/workspace/r7-review-input/R7-U08-r1-d6e07340aa14eb8b45728020cad018a22d7559b2`：**113 文件 / 1,198,309 字节**，其中三个完整镜像和 110 个作者证据文件。两次实际恢复回执已保存在 `tool-evidence/`。恢复文件随后去除写权限，未执行恢复出的作者、参考或 native 程序。

自编 `tools/verify_frozen_inputs.py` 独立重核全部大小/SHA256/Git blob、实际候选 tree 的 100644 模式、113 路径完整差异、B 身份、冻结文件的 tree blob 绑定、作者 manifest 的 109 个具名证据和三个镜像声明、原反证字节区间。候选对 B 的全部差异仅为本批 `candidates/R7-U08/` 下新增；候选正式目录 tree 与 B 一致。结果 `ALL_BYTES_TREE_MODE_SCOPE_MATCH` 只是 TOOL_VALIDATION，下面的语义结论来自重新阅读和独立推导。

三个候选镜像的实际身份：

| 镜像（`candidates/R7-U08/deliverables/final-specification-set/` 下） | 字节 | SHA256 |
| --- | ---: | --- |
| `user-interface/wp67-a-battle-interaction-and-presentation.md` | 78,445 | `f746751b7be6ce908ac374ae3f12baa6c1eadff102f6c1c2b294f8c79e996e44` |
| `user-interface/wp67-b-lifecycle-presentations-and-history.md` | 43,347 | `07d62e44f455fc04ebb9df64aefc323525d40354c3c69de2acb3f60cf6988eca` |
| `test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` | 172,172 | `14ea5f2f375f1035c63e98b611c71feb5dcd1258a6f0b4d6f30e0e45721eed91` |

完整逐文件表、blob、B 旧身份及操作范围见 `review-input-receipt.json`。三个候选全文共 348/213/1030 行均分段实读；与 B 独立全差异核对确认，除 WP67-A 原196/247/248、WP67-B 原141、目录原440及原398后插入四行外，其余字节全部保持。读到的其它章节不由此授予全域新语义认证。

## 逐项结论

| 必修 | 结论 | 独立判断 |
| --- | --- | --- |
| GR7-M13-001 | PASS_SCOPED_CANDIDATE | L247 正确按当下浮点显示 h 与整数总量阈值选色；HP01–04 正确补奇数总量中间态及正常对照，没有修改 K35 或扩大到其它 UI 条。 |
| GR7-J16-001 | PASS_SCOPED_CANDIDATE | L141 将登记限定为先于逐成员视觉；基础准备正常后非空 BGM 先逻辑请求、请求正常返回才登记；空音乐跳过，与源顺序及全文“演出”定义一致。 |
| GR7-J16-002 | PASS_SCOPED_CANDIDATE | L196/L248 仅“闪白→闪光”，撤回无证白色断言；没有采用可选 RGBA 补充或新增像素断言。 |
| GR7-J16-003 | PASS_SCOPED_CANDIDATE | L13 采用“入口＋条件后续”允许方案，分别明确净化返回、存放返回及还有下一项；保留双满提示返回仍清中心及拒绝只停止后续。 |

`per-id.json` 给出全部 17 个原具名向量的前提、预期、独立理由、正常/取消/拒绝/异常/部分提交、正确保留与未满足依赖。它们全部是静态核阅，**17/17 NOT_EXECUTED，执行 0**。

HP 链独立读取了数据框完整1–413、浮点插值394–406、场景更新79–119、HP提交5–34、HP表现219–232、个体能力公式1085–1127和 Pikachu 数据629–655。另定向补取固定 R 的 `Data/Scripts/001_Settings.rb`，实读141–151确认默认 IV/EV 未禁用；因此基础HP35、L50、IV12/EV0给 T101 合法。51→50在半秒的50.5高于阈值50仍绿，到端50黄；26→25在.75秒的25.25高于阈值25仍黄，到端25红。数字临时转换不写显示 h；条宽比例/偶数舍入、1秒目标、Off仍等待及领域HP先提交保持。组件无独立取消；异常不承诺补画或回滚。

名人堂完整1–494与 Audio_Play1–115、Game_System1–100已重新阅读。首逻辑BGM请求时空历史/编号0尚未登记；正常返回后才克隆、追加、编号/裁剪，再到成员建立/视觉链。空音乐正常对照和请求不返回的条件异常均成立。音频消费者自身可先改逻辑状态，不能由请求推出真实发声、保存、自动退出或统一清理。默认蛋收录、正/负/0上限、每次只删一届、编号不回退、PC门、无取消/自动保存及 L22/L24/L33/L35 均保持。

经验完整数据框、领域162–224与实际场景经验驱动283–293独立新读；原 J16 的234–254是伤害动画，未用它支持经验链。满槽前序正常后交付的颜色请求不支持“白色”；两处中性“闪光”充分且最小。1.75秒比例、名义.2秒、SE及等待、经验先写、逐级顺序、无条立即完成、Off仍播放保持。SE失败可在首闪光前停止；某子精灵失败不保证其余交付；不推出像素或统一回滚。

净化室完整包装348–628、资格218–263、演出接点1115–1135与入口1277–1308，以及统一净化/遗迹石1–151、成长工具132–221、Medium1–93、Shadow字段1–160、等级设置173–218和通用存放1–77已独立实读。1000＋400＝1400跨L11，默认包装在首能力窗更新失败前已到等级下限1331，尚未精确写1400/存放/清中心；同级S0一组正常时无下一组询问；两组拒绝只停后续；双满提示正常返回不等于存放成功但仍清中心；遗迹石有空更新接点。候选准确保持这些分支，不决定未来兼容源缺陷的政策。

## 原反证、历史和共享接收

实际读了 C04 原独立成员 `/records/6`、M13 原提案、原规范候选的 verification/dependencies，以及 J16 三份同字节原载荷中的三个完整 new_proposed 与 C14 三个原反证。原更宽/可选建议、载荷时点差异及错误经验定位均保留原资格，没有据作者报告或旧 PASS 代审。

WP23§6/§8.3、SH38/39/43/44/45及附表54–55、WP67-B 的三层选择和跨级边界、当前完整 B17/U05/R4 目录对照均实际核阅。相关旧正确条款除本次 L13外保持原字节。不新增净化领域根因，不编造未从有界材料解析的早期 canonical GR-ID，不继承旧 B17/U05/R4 全域 PASS 或重开旧56/92关闭。

CG06 的固定冲突表及 U02 合同共享范围已读：U02 贡献是 F8截图路径/回退、按入口输入刷新和条件输入资料/解析向量；U08仅在 K35后插入四行及修改 LC-L13。条款可以分别接收，但这不证明 U02 候选或累计合并已经通过。R7-I 必须串行应用这些局部贡献，保存 U02及其它已收贡献，不能用 U08 的完整目录覆盖整合目录。需要新的 R7-IR审真实累计 commit/tree 后，才进入正式接收和依赖关闭。

## 配置、执行与日志资格

审者请求 gpt-6.1-sol / ultra / default 普通速度，禁Fast；有效 model/effort/tier/speed 全部 **UNVERIFIED**，无后端有效回显，不查额度/认证。作者原 xhigh 请求及其 UNVERIFIED 资格保持。真实 thread ID、工具PID或工具退出0均不认证模型配置。

本次 SOURCE_STATIC、DERIVED_VECTOR 与 TOOL_VALIDATION 分列；REFERENCE_OBSERVATION、参考程序、独立完整行为模型、游戏宿主、Demo、native媒体、真实存档回放均为0。不把本批0抹去原R7另有UTIL-03隔离Ruby1进程/10输入的历史事实。L01–L14全部保留；27项/13批分母不变；7 optional、2导航facet、1 no-required、2 policy未采用。

日志限制明确保留：早期 bootstrap/直接阅读存在平台工具调用，但没有逐调用本地分离UTC/PID/stdout/stderr，不倒填。`run_tool.py`启用后的具名检查有真实独立分流；文本阅读元数据在 `reading-receipts.jsonl`，实际输出在平台工具记录，未将作者镜像或参考代码复制到成果分支。截断的目录634–635、Growth/Chamber及历史缺段已实读补齐。报告生成器初次在临时文件有括号语法错误exit1、未写per-id，修正后新调用成功；不是行为失败或已执行向量。初次无界Git fetch因传输过大主动中断exit130/early EOF，随后对95/aa/d6使用blob:none/depth1精确fetch成功；这不影响两份独立有界恢复的完整回执。额外源目录API返回tunnel403，改用固定R的Git元数据及具名blob读取成功，没有把可读依赖伪标limit。详见 `tool-evidence/context-and-extra-inputs.json`。

## 成果运输

唯一成果分支 `codex/r7-u08-reviewer-20261015-r1` 已从固定B创建独立checkout；创建前同名本地/远端成果均不存在。只提交本 `candidates/R7-U08/evidence/reviewer/r1/`，没有携带作者镜像或改正式/公共/main/tag/reference。普通提交与普通push；最终commit/tree、远端分支回参及最后完整逐文件远端回读由实际发布回执/末次工具输出和最终回传绑定，不制造自引用commit或manifest哈希。
