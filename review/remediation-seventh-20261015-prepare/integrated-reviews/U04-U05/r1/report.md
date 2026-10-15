# R7-IR U04/U05 r1 独立实际整合复审

结论：**GR7-M03-001、GR7-M03-002、GR7-M07-002 均为 PASS_SCOPED_ACTUAL_INTEGRATION**，仅限下述冻结 MI、原缩窄必修合同与具名前提的静态内容复审。未发现需修订项，未发现阻碍本次有限静态判断的输入缺项。全部行为向量 **NOT_EXECUTED**；不认证运行等价，不登记 ACCEPTED 或 CLOSED。

## 实际身份与固定输入

审者实际 context 为 `01a13fef-cc3c-730e-a5ba-a59a61501034`，来自本选定容器 `CODEX_THREAD_ID`；环境 `ccarenv_b64_Y2NhcmVudl84ZWQ5MWM5MjY5NzA4MTkxYmE0YzIzN2M3NzgyYjg0Zg`。平台 opaque task ID 未暴露，保留 NOT_EXPOSED_UNVERIFIED。父来源线程 `01a13f49-a154-7054-9b04-ce31f924d01c` 不当作本审者 ID。本 context 与父来源及四个排除的作者/候选审者外部 ID 均不同，未创建子任务，未担任作者、候选审者或整合者。U04 作者内部 context 未暴露的资格原样保留，不伪造匹配。

请求 gpt-6.1-sol / ultra / service_tier=default / 普速、禁 Fast；无有效平台配置回参，实际 model、effort、tier、speed 均 **UNVERIFIED**，线程与工具成功不认证配置。

| 角色 | 固定完整提交 | 实际 tree / 子树 |
| --- | --- | --- |
| 本次全文派发 | `95c260d8f3fb4a171675dde877137fcd4c2f1c8d` | 实际 tree 见 review-input-receipt.json |
| 实际整合 MI | `b0eea808887a688d52d28390ac8886fed9c10bcf` | `73ad4ff20527d4bdcf27d55fc17932a232e2f912` |
| MI 正式131份子树 | 同 MI | `dcb3f744d78fa5c4c62994de5e4cf6eb1f886d3b` |
| 实际输入冻结 FI | `d9021aa2d704476f644ef15f1a3b8291653ff8f1` | `7efe118d11965ea842b5522cfa9dd7a8c7842d2d` |
| 基线 B | `e646432c644dec04d306842cc5a559a29c718fbc` | workspace `84f79ec6e772aacbf3a464fde68cdc5a280e2950`；正式 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c` |
| 原合同 | `f622356f3beb9e84ea8cff9db07c7fb382565d3f` | 两批完整七组及其原始绑定 |
| 恢复工具/原计划 | `658488c81f1f3181a488298ab27850c8af951d73` | 先读工具、说明和计划后使用 |
| 参考 R | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | 只重新核具名文件，不认证参考整树 |

已完整读指定 `integration/U04-U05/v1/R7-IR-dispatch.md` 及实际 AGENTS.md。B、MI、派发 Git 树均无 `.agents/.codex` 路径，本容器 `/workspace/.agents` 为空，未发现相关 `.agents/skills`；没有假称使用不存在的项目技能。所有规范分析保持行为描述与源分离，没有复制源表达式进报告、执行参考或实现新框架。

## 本容器恢复及实际字节

原源/反证与实际 MI 分开按四份固定计划恢复，没有借用整合者的本地目录：

| 新目录 | 文件 | 解码/固定输入字节 |
| --- | --- | --- |
| `/workspace/r7-ir-context/U04` | 29 | 5,789,300 |
| `/workspace/r7-ir-context/U05` | 23 | 6,954,154 |
| `/workspace/r7-ir-actual/U04` | 54 | 1,007,157 |
| `/workspace/r7-ir-actual/U05` | 53 | 814,296 |

四次均 BOUNDED_RESTORE_BYTES_VERIFIED；真实 HTTP/身份回执在 tool-evidence。独立审计重新核全部159文件及编码对象，并将项目输入与实际固定 Git blob 完整字节比较。两原合同16个去重 raw-span / JSON-pointer / canonical 绑定均匹配。按固定 R 定向补取 Battler Initialize、Compiler、EggHatching、Species_files 四文件，共72,884字节，核大小/SHA256/blob，仅读不执行。

先核身份和完整正式 diff，再进行内容判断。MI 相对 B 恰为 WP39、WP41、WP34 和两份对应目录五文件；其它126份正式文件相同。完整五文件实际正文/目录均已逐行读，与 B 的相同块及被替换旧行、指定候选逐块对应。11个具名变更片段能从 B 精确重建 MI，片段外字节一致；实际补丁与独立重建补丁完全一致。两目录原225/274行表格行按原字节、原顺序全部保留，新增 BC 六行、SW 六行、PF 九行；BC31/SW35计数及正文导航相符，BR01–31、PF独立编号保持。没有以完整镜像覆盖其它贡献。

U04 候选 `242e1f9fb2fbdf7d609bcdb6de0a95547f9f4c6a` / tree `e375ad3b402f1b5f33493680390b9a123eb56c9d`；独立候选报告 `3d6fcea6c2d5930c4c299278895077079d7afd28` / tree `f60c3975742bca2c4f8e6440e06dc95de8310f0e`。U05 候选 `3acf3e23fd79c3bed1b98d23873bc1f2fd25cafa` / tree `b847cce4fefc4916782228b1fd43898c51abb8f7`；独立候选报告 `e9e47920ee26ecc87e0aaf02e84ec6f33b5cfed7` / tree `54dc605baa3a6bc95439bccefdea7355ab1f79fb`。全部作者17/14文件、候选审者20/24文件均取得、与真实 Git blob 核同，内部非自身 manifest 项全匹配；报告/逐ID内容、读集与执行资格、运输/工具/失败记录均检查。没有执行其中作者或审者程序，也没有把其候选 PASS 继承为当前批准。

## 逐必修判断

| ID | 当前实际条款与独立理由 | 结论 |
| --- | --- | --- |
| GR7-M03-001 | MI WP41 L123、127–128；SW-30–35。合法普通2v1、单玩家业主、开场人数、正式濒死而仍有可战后备、canRun及副本原始速度前提成立。首席 No 写3只令本席不换；同一扫描后席仍选择/绑定P，顺序[0,2,1]，位置治愈60→120后撒菱15至105，正常返回后外层阶段22才消费。单待补席、首席Yes、入口已有3分别核对；必选后备的取消输入不能撤回逃跑。异常只保留已到反馈/决定/绑定/顺序/位置/HP前缀，不保证最终3、回滚或宿主成功。 | PASS_SCOPED_ACTUAL_INTEGRATION |
| GR7-M03-002 | MI WP39 L190；BC-26–31。有效1v3的[3,5,1]，既存濒死3使偏好扫描停止并经回退返回3；3活仍3、3缺席才5。直接己侧0投球随后按全局活同伴序补救为1；显式对侧5直接用5。无活同伴的空对象失败沿WP38既有边界，不新增必失败、退款或普通菜单可达结论。查询只读，无交互取消。 | PASS_SCOPED_ACTUAL_INTEGRATION |
| GR7-M07-002 | MI WP34 L188；PF01–09。仅修无条件“两槽不写入”括注；作者DEERLING合法旗标、母0/月2且未先动态读等具名前提下，母1提交/清特性缓存/重算/条件登记先于子显式1。月1相等、强制0、仓库/战斗守卫、移除旗标、默认SHELLOS、队满、重算/登记/子后段故障及缺玩家/图鉴逐行核验。子同值提交不套亲本相等守卫；重算不保证数值变化或最终缓存仍空。 | PASS_SCOPED_ACTUAL_INTEGRATION |

以上是本审者重新逐条件核 R 源和 MI 内容的判断。精确文件/跨度身份、21行具名前提、独立理由及反证/候选绑定见 per-id.json；源读取范围与未改消费者见 tool-evidence/reading-ledger.json。

## 消费者、正确保留与依赖

M01、M02、C05 非提出者反证及根缩窄原成员均已读。M03-001仅接收非致死继续扫描，未升级作者危害致死终局扩张。WP42 §3.2、阶段21/22及L135不立即退出嵌套调用的正确概括、§8诊断/传播边界，与实际WP41相容；普通逃跑、训练家/伙伴、换人/取消门保持。

M03-002逐条件接收 WP38 §2 的许可、登记、球专用执行、活同伴补救和既有空对象失败；WP47-A §5的目标资格、敌我/邻近及随机回退保持独立。换人消息、梦话、变身者使用false/默认的源调用已核，不把true查询扩为所有目标族。SW/R/E旧向量和BC旧行未改。

M07-002逐条件接收 WP21 §4.1/§6 的动态守卫、显式同值提交和写入次序，WP33 §5.3生成→容量→入队→复位，母系→首个合格永石及原随机通道。BR07、BR27–31逐条保持：子同值提交、两缓存/条件登记、N=0不读不清、末次记录与故障前缀不受亲本新增受体影响。EG-13/EG-20连同固定R孵化调用重新核对：默认子代动态读取先于通常owned/seen-egg；R4-IF01–06连同取图消费者核对：严格超时、强制返回不提交、显式形态参数与个体读取区分、先求形态再找资源、缺资源不撤销已到提交。未认证像素或历史运行。

原七组 direct/transitive 的具名 record→record排程边均为空，这是原绑定事实；本报告没有据此或据无冲突组推断全局依赖满足。上述源/消费者及历史语义相容，在本次冻结实际输入的有限静态范围已满足。**R7-I对本新结果的实际接收、语义/共享目录责任登记、正式接受与关闭仍为 WAIT 相应范围**，任何未满足范围保持 OPEN。本报告仅提供接收证据，不能代根登记 ACCEPTED/CLOSED。

旧56/92证据及所有 B 已有路径没有被 MI 改动（除这五份正式路径）；本次不重新批准旧全局证书。U01旧r1的J01 FAIL在MI中保留，旧M01候选PASS不能移作批准；旧U01及未审返修a3938bbb均未进入实际五份贡献。其余24项/其它批次未覆盖，分母27项/13批不变，optional/policy未采用。

## 执行、工具与交付边界

新增内容证据为 SOURCE_STATIC / DERIVED_VECTOR；审计为 TOOL_VALIDATION。全部行为向量、条件故障、参考程序、独立行为模型、完整模型、真实UI/宿主、Demo、native媒体、真实存档回放新增均0；REFERENCE_OBSERVATION无新增。旧H14/UTIL-03的局部Ruby1进程10输入仅保持原历史资格。L01–L14完整保留，不把可读未读材料冒充limit；未读源补集不认证完整参考树、任意插件或所有组合。

独立审计首轮exit1：审计允许目录误漏本轮新增的原R7 publication证据，将其误列为历史修改；修正精确前缀，并另断言所有B已有路径除五正式文件外均不变后，真实重核exit0，见 audit-command.json。失败说明保存在 session-observations.json；早期探查/读取及被截断后补读的I/O仍在平台，不伪补独立UTC/stdout/stderr。旧作者/候选审者失败资格保持。

唯一成果worktree `/workspace/r7-ir-result` 从固定B创建，分支 `codex/r7-ir-u04-u05-20261015-r1`；创建前精确远端分支查询为空。只写本目录的四个主文件及真实工具证据；不携带候选/MI正文，不改正式、公共台账、main或tag，不force。最终普通推送后的完整commit/tree及所有文件不可变URL全响应体读回，由实际工具I/O和最终返回绑定，避免同一提交自引用。发布证据只证明运输，不改变上述内容结论及后续根门。
