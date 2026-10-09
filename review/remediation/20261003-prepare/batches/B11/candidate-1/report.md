# B11 完整有界候选：待独立 Ultra

正式 FIX_BASE 为 `0cfe99094b76f8d75fded0d638694677855a5f0c`，tree `f938411894a3e7aeb98fd002f3aef60725cd247f`；管理派发为 `4cb51a33402ec6559a396226239afe308a4b8849`，不替代正式输入。独立作者分支为 `codex/cloud-dot-B11-author-1-20261009`。本包完成作者修订，尚无独立 PASS、G、actual 复审、C 或 canonical 关闭。冻结的完整候选 SHA、远端读回和完整 diff 由发布后的报告提交记录于 `remote-readback.json`，并由作者交付给父统筹；不向候选回填自身 SHA。

35 个计划输入、6 个完整原 finding/PLAN 验收对象及 current/root/extension 限定的身份与相等证明，按发布草案 `a9c0af2203840c3e68d8775e920155d0ade5b820` 精确复用。`evidence-reuse.json` 列每个对象的完整 commit、blob、SHA256、字节数；只复用准确版本和已经具名的语义阅读范围，不重读全部历史，也不冒称完整源码语义覆盖。原报告固定 `93e10babe0b9c9ef8b3f5277754541b447beeeb4`，PLAN 固定 `41fffb540c6483f5296ea0d33b789b75180d27ed`，静态参考固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

父统筹在源线程 `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2` 读取上述发布草案的完整 `original-sync-proposal.json`（blob `098b9009b07d82ca9141ade18d65704c19627b2e`）后，明确批准 B11 专属 GIR-FD82-B019 原稿范围：WP47-A §5.1 两个 hunk，WP47-B §3.1 幽灵诅咒行一个 hunk。批准只涉及精确 before/完整 patch/after，是父协调范围批准，非质量通过，不继承 B10 原稿授权。`scope-amendment-receipt.json` 已记录来源、批准范围、完整补丁及应用前后身份。两处均精确应用并核对通过；其余原稿不变。草案目录旧报告中的“等待批准/未应用”是原版本历史，由本候选状态接续，不改写旧报告。

批准的原 8 正式路径中改动 7 路径，WP49/51/52 测试目录整文件不变；另应用批准的 2 原稿，共 10 路径边界、9 路径实际变化。8 个净化规格/测试输出与发布草案逐字节相同，原稿 after 严格等于已批准提案。全部输入/输出完整身份见 `input-identities.json`、`output-identities.json`。未写公共台账、index、导航、全局覆盖、其他批次、main 或参考。

| Finding | 修订与受保护前提 | 静态正反设计 |
| --- | --- | --- |
| GIR-FD82-A046 | WP50 §4 衔接已接受 WP28 主动 HP 身份/库存与持物触发/记录，AI 估量保持独立；正确半血、可恢复、树果、强制食用、RIPEN/CHEEKPOUCH 与共生顺序保留 | HI34：H101/105 请求25/26；HP1变26/27；主动HP80/H101实际增21并减库存，普通持物高于半血拒，持物记录不等同库存 |
| GIR-FD82-B003（主责） | WP47B §6 在完整字面 `skillswapclause` 共同门下解释 SkillSwap 局部表及旧 SB-A01；保持 `CONFIRMED_DEPENDENCY_CONTEXT_NO_NEW_ROOT`，不恢复“新局部根因”早期说法；已接受 WP39/WP54 不变 | SB-A07：共同门真，目标拒且不进行成对赋值/得失回调，外层 PP 不回退；A08 只改简写键 `skillswap`，未启 canonical 门，合法局部交换按既有顺序 |
| GIR-FD82-B007 | WP48 §3/WP50 §3.1 明确全程0.1kg，初下限→有效能力（破格只跳能力）→有效物品→末下限，连接已接受 WP38 沉重球消费者 | AB24：1180→590，率45−20=25，满血无状态x8；仅抑制能力1180、率45/x15；300kg用3000、率75/x25。HI35：2360的能力/物品四组合，区分物品抑制与能力跳过 |
| GIR-FD82-B014 | WP47B 换出保持实计成功击数>0及所有后段门，保留根裁决“中间calcDamage=1、真实损HP=0”，不改写为所有中间量0；已接受 WP41 不变 | SB-S08：合法物理急速折返命中 EISCUE/ICEFACE 原始形态0，中间1/实损0/成功击1，形态1并允许后续换出；S09仅改失手，击数0、形态0、不换 |
| GIR-FD82-B018（主责） | WP48 只修3族、WP50只修6族数标签与复制语句/新增身份口径，身份列完全保持；133直接+15复制新增=148，165直接+31复制新增=196；11/21是复制语句数。保留 D010 同根、INTAKE-C01 分开及非本地贡献 | AB25/HI36：原稿与净化稿配对差集空，复制源不重复计新增，跨族配对不按名称去重。只证明静态身份统计，不证明每项行为覆盖 |
| GIR-FD82-B019（主责） | 净化稿及本次批准原稿均按当前实际 U 动态查询构造与重定向，类别单目标/敌方与实际列表1分开；最终 T 接受诅咒。既有追击/不可重定向/位置门、龙箭先扩展再坚毅/螺旋尾、吸引顺序保持 | MA-T07：幽灵 CURSE 原始User→当前RandomNearFoe，初选seat3被seat1跟我来吸引，最终seat1诅咒，U101→51；T08仅清吸引，seat3诅咒；T09接地精神场广域战力类别AllNearFoes，实际列表1也不进重定向；T10非幽灵默认User空列表，仅自身能力级变更，无诅咒代价 |

每条 finding 的完整 current/root/extension 控制、原对象绑定、局部条款、状态顺序、正反例和限制保留于 `contribution-proposals.json`，不是仅用表格摘要替代控制。6 项贡献、3 项主责、0 新根因。B018 的 B10 已接受贡献保持；B13 的 RC24（含 W22b）与历史23/126传播仍待 B13，未替 B13 修订，也不把其归 B14。A046/B003/B007/B014 的非本地主责或贡献不被本作者重新接受。

`owner-row-protection.json` 与 `author-static-checks.json` 核对两追加测试目录完整原字节仍为输出前缀，旧行/顺序/重复保持；WP49/51/52目录全文件及其余15个测试目录文件字节不变。仅追加13条静态设计，全部未执行。`family-label-recount.json` 核对9个标签及所有身份列，与精确旧枚举一致。正式10路径默认 `git diff --check` 为0错误。统一diff档案中的空上下文行必须保留单个空格，全包默认 whitespace 检查会报告这些数据行；不宣称全包默认检查通过，不删除档案字节以掩盖提示。

`formal-changes.patch` 只表示全部批准正式路径差异，不能替代完整 diff。发布后 `full-candidate.diff`/`remote-readback.json` 将明确绑定无路径过滤的 `git diff --binary --full-index FIX_BASE FROZEN_CANDIDATE`，包括所有作者草案与候选管理材料。旧 `author-draft-1/frozen-draft-full.diff` 仍只绑定旧草案提交，不得当作本候选差异。报告提交若只增加发布证据，必须另列 SHA 并核验正式输出不变。

独立派发合同见 `independent-review-dispatch.json/md`：R-B11 对准确冻结候选做 mandatory FULL；B07/B09/B10 按冻结影响映射做独立有界影响裁决。实际影响或既定必须门存在时，另做必要 affected Ultra PASS_SCOPED；无影响则需准确版本和条款/调用者/数据/条件的独立 NOT_AFFECTED 依据。作者保护检查不等同这些结论，也不因共同文件/ID自动重审整批。全部 required candidate 门完成后才由父 A-REG 串行 G；新 actual 必须另做 FULL 及必要 affected 门，完整看接受前驱→actual及candidate→actual全部差异，不能转授候选结论。全部 actual 门后才可 C。B12/B21需等待本批正式接受。

全部静态/未证限制原样保留于 `source-limits.json`：U01–U10/G01–G12/AX01–AX20、具名未读/二进制/素材/媒体/字体/宿主配置容量/插件动态调用/实际地图事件/Demo/样本/备份gen及条件67树果等不升级。参考、游戏、Ruby、编译、转换、生成、反序列化、行为模拟器、历史作者/审者程序执行为0；行为向量执行、运行观察、已证Demo均0。只运行新 Git/JSON/文本/hash账务检查，无行为测试声明。

作者 requested 为 gpt-6.1-sol/xhigh/default Standard，可信后端参数回显未暴露，effective 按用户 Plan A 记 UNVERIFIED；配置分栏见 `configuration.json`。本作者不代独立 Ultra、不派生子任务。父统一安排最多3活跃任务；修订后若有 REQUEST_CHANGES，由 xhigh 作者产出新准确 SHA，再独立 Ultra。本候选无剩余作者侧批准/身份阻塞；剩余事项是独立 candidate/actual 门和父串行登记，尚未接受或关闭，不扩大为第三轮全局 review。
