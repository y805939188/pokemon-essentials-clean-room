# R7-U05 作者交付

状态：**CANDIDATE_READY_NOT_REVIEWED**。本轮只处理 GR7-M07-002（required/P2），不代表候选独立 PASS、实际整合 PASS、ACCEPTED 或 CLOSED。

## 固定输入与实际环境

执行环境已由 starting 进入 ready；本容器项目 `/workspace/pokemon-essentials-clean-room`。开始时为干净 `work` 分支，HEAD 为固定 B `e646432c644dec04d306842cc5a559a29c718fbc`。以 B 创建唯一成果分支 `codex/r7-u05-author-20261015-pilot1`；没有 reset、force 或覆盖既有成果。父会话的查重陈述只按派发引用，不自行认证全局无任务。

完整读取指定准备提交 `4bd152023b4bcb3dd5a3654deffe75aeebc40f10` 的 `review/remediation-seventh-20261015-prepare/delegation/pilot-dispatch/R7-U05-author.md`，再完整读取固定 f622356f 的 JSON 七组合同及原作者入口、658488c8 的恢复工具／本批清单／恢复说明。dispatch-identities.json 记录逐文件身份。首波合同内部 df3553d6 是历史准备定位；本次入口固定为用户指定 4bd15202，语义合同仍按其指定的 f622356f，不以浮动 HEAD 替代。pilot 仅覆盖旧入口“不提交／不推送”的传输限制。

已读项目 AGENTS.md。固定 B 及容器 `/workspace/.agents` 没有可读的相关 `.agents/skills` 文件；未虚构或借用其它项目技能。固定准备提交的树核对另记 commands.json。

读取恢复程序后在**本容器新目录**运行：

`python3 /workspace/r7-bootstrap/R7-U05/tools/restore_container_context.py --plan-directory /workspace/r7-bootstrap/R7-U05/recovery/batches --batch R7-U05 --destination /workspace/r7-context/R7-U05`

exit 0，23 文件／6,954,154 字节，BOUNDED_RESTORE_BYTES_VERIFIED；编码对象的大小／blob、解码结果及固定输入的大小／SHA256／blob均按清单核验，复核见 validation.json。recovery-receipt.json 保留真实 HTTP 回执。原路径映射到本容器 evidence、inputs/reference 和 inputs/project；没有假定共享整合者目录。只恢复有界快照，未读取80MB Manifest、未恢复完整报告树，也没有认证完整参考 checkout/tree 或宿主。

另按已读原作者精确定位补取固定参考 `001_Compiler.rb`，核原 git blob 后读 L422–435，见 supplemental-restore.json；B 的 WP33 §5.3、EG-13／EG-20 从本地固定 Git 对象定向只读。所有源／正式／历史读取范围和身份见 read-set.json；目标 WP34 与共享测试目录均完整阅读。原 C05 challenge 及原作者／根裁决按精确 raw 字节成员和 canonical SHA 复核；只采用 C05 已接收的缩窄合同，不升级原作者更宽负证据或旧全文搜索资格。

## 最小变更与作者核对

完整候选镜像均从固定 B 原字节建立。WP34 仅替换原 L188（§9 第10条）：删除无条件“两槽个体不被写入”，保留不主动直接重写遗传字段及寄养等级／经验边界；补明亲本读取可能填派生值，以及既有 WP21 守卫允许且返回形态不同才提交亲本形态、清缓存、重算与条件登记。强制、战斗／仓库、相等守卫保持。

目录只在原 R4-IV 前插入 R7-U05-PF01–09，明确作者 DEERLING 加母系旗标、数据合法已装载为前提。覆盖月份2母0→1先于子1、月份1无亲本变化而子同值0仍提交、强制0、storage／战斗守卫、移除旗标、默认 SHELLOS、队满、分阶段异常和缺玩家／图鉴对照。未创建或运行该数据夹具。每条输入、预期、合同原向量映射和阶段见 per-id.json。

正常链的母方提交先于子代赋值；重算不保证数值改变或最终缓存仍空。生成链没有交互取消。队满检查晚于生成，不入队、不复位已有蛋标记／计数；已到母方／登记前缀保持。重算、登记或子代后段故障只描述已到前缀，不补自动回滚、宿主恢复或存档保证。

不采用 §5.2 可选交叉引用或任何 optional/policy；不修改 WP21／WP33 已正确规则。母系→首个合格 Everstone 的顺序、子代显式同值提交、全部随机通道和默认 SHELLOS BR27–31／N=0 保持。EG-13／EG-20、R4-IF01–06 按已有静态资格保留，不补签历史运行。

## 验证与边界

validate.py 是本批自编的**文档／身份机械校验工具**，未翻译或模拟参考行为。实际命令、UTC、stdout／stderr、exit 见 commands.json；validation.json 记录初次完整工具结果。校验两份镜像旧／新身份、所有23恢复文件与7个编码对象、原 raw/canonical 成员、WP34仅一行变化、目录移除新增段后完整等于B、正式tree与写入范围。artifact-manifest.json 覆盖全部交付文件（递归自指文件明确排除；其身份由实际候选 commit/tree 绑定）。

SOURCE_STATIC、DERIVED_VECTOR 与 TOOL_VALIDATION 分开；所有行为向量 NOT_EXECUTED。参考／独立行为模型／宿主／Demo／native媒体／真实存档回放新增均0。旧 H14/UTIL-03 单进程10输入保持原聚合时点资格，不能算本作者运行。初始探查未逐命令落独立文件，平台工具 I/O 保留；此处记录的命令是后续真实重核，未伪补初始日志。一次试读错误的非现存目录路径已用 rg 定位实际 catalog；一次 GitHub API 目录读取遭403，未据此判技能不存在；仅由实际 Git 树核对。

请求配置 gpt-6.1-sol／xhigh／service_tier=default 普速、禁 Fast；没有有效配置回参，实际 model／effort／tier／speed 一律 UNVERIFIED。实际 context ID 来自环境回显，平台 task ID 无明确回参，见 per-id.json。未创建子作者或 reviewer。

L01–L14、27项／13批分母、7 optional／2导航facet／1 no-required／2 policy未采用、旧56／92关闭边界全部保持。作者无前置批次不表示没有领域／接收依赖。仍待 R7-I 验完整差异并冻结 candidate-input.json、不同实际 context 的 ultra 独立复审、R7-I 串行按 clause 整合及责任者接收、新 R7-IR 对实际整合 commit/tree 复审和最终根接收。不得据本作者机械检查关闭问题。

## 成果传输

唯一普通推送目标为 `codex/r7-u05-author-20261015-pilot1`。内容提交 `85d117a38247e6bd3198aad5957ee213727ebd89`（tree `95df956471d9b2f188e4f3383f3c068dc4acecc0`，直接父为固定 B）已普通 push，exit 0。实际 `ls-remote`／fetch 回读同一完整提交，再由不可变远端 raw URL 完整取得13个候选文件、181,814字节，全部与发布 Git blob 完整字节相等，见 remote-content-readback.json；未只以本地路径或哈希口述替代传输。

该首次回读回执、真实 push I/O 与本段一并纳入最终证据封装提交；最后普通推送并再次实时核最终 commit/tree 与全部候选文件。最终 commit/tree 与该最后回读由平台最后工具 I/O 及返回消息绑定，避免在同一提交内循环自指。正式正文镜像从首次内容提交起保持不变。无 main／tag／整合分支或正式路径写入。统筹须冻结后另派独立审者；本作者完成封装后停止写入候选，不担任独立 reviewer。
