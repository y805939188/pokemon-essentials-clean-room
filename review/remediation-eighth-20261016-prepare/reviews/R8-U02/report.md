# R8-U02 独立候选复审

结论：**PASS（仅固定候选；GR8-KER-003）**。未发现本批必须继续修正的候选问题。正式文件尚未整合，**actual integrated review = NOT_STARTED，ACCEPTED = false，CLOSED = false**。

本报告由本次非作者复审上下文形成。未修改候选或正式规格，未执行 Ruby、游戏、原生宿主或行为模型。源码结论为 SOURCE_STATIC，场景为 DERIVED_VECTOR / NOT_EXECUTED，Git／字节检查为 TOOL_VALIDATION，三者不混记。

**固定输入与输出范围**

| 输入 | 固定身份 |
| --- | --- |
| 受审候选 | `8b69bca8bf9141276425a963f350b19048bb2b51`；tree `98c3f3ad5d091c4fc9980ffe9f8375a7e3a51156` |
| 原审查基线 | `4575e80d041ab0c74a42e2e36399d05791dbaa5b` |
| B8 | `fd1df570cad987dc3852a3b958f03916e317f7fe` |
| 原版参考 R | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；tree `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 语义 core | `2460370f1e410bd49cc29e377b89662838aed2b3`；原33合同来源 `5caff3bd1a1b062b48b7eda46777a614921946f3` 与 core 恢复位置分别保留 |
| 候选镜像 | `review/remediation-eighth-20261016-prepare/candidates/R8-U02/mirror/deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md` |
| 候选完整文件 | mode `100644`；41,768 B；blob `d895aa9d0df2024d9bcd99f1d954d8a5685f6211`；SHA256 `70d794ed63d4ff1f98ed21a9aecfea4923063d10a45e69965e7dad294678adb2` |
| 原正式 WP04 | 41,805 B；blob `4ecfdfac8fda26fdcf10e137c3169023531770fb`；SHA256 `db4ea6ffc4d7ec3fbc50659411cba7a026234be13ed16faaaaec964762dea20f` |

实际项目位于 `/workspace/pokemon-essentials-clean-room`，参考仓库位于 `/workspace/pokemon-essentials`；项目内没有 `reference/pokemon-essentials` 目录，未据文档示意路径猜测。获取的远端 `codex/remediation-eighth-20261017-4575` 当时 HEAD 等于固定候选。输出仅位于本报告所在的 `reviews/R8-U02/`，独立分支为 `codex/review-r8-u02-20261017-8b69`；输出提交身份以最终答复及远端分支回读的实际完整 SHA 绑定，不预填自身未来 hash。

本批 assignment 仅含 `GR8-KER-003`。同一候选提交另含 U03/WP60 镜像和协调证据；它们被识别为独立写集，不由本报告签收。初始对旧工作区树果材料的定位性阅读不授 U03 复审信用。

**逐项证据与最强反方**

下表源码行号均相对于固定 R 的 `Data/Scripts/`。正式／候选行号均为 WP04 的完整320行文件。

| 检查项 | 独立证据与反方处理 | 判定 |
| --- | --- | --- |
| 实质修正 | 候选 §5.2 L196 仅删“并提示「Changes made to file X」”37字节。`021_Compiler/001_Compiler.rb:924–938` 的改变分支构造格式化结果，随后覆盖写入；没有把该字符串交给输出消费者。两个真实更名、读整文件、仅改变才整写及固定路径均保留。 | PASS |
| formatter 是否隐式输出 | 完整 `001_Technical/001_Debugging/002_DebugConsole.rb:1–233`：L172–181及颜色／字体依赖只产生字符串；L36–45和L60–128的真实输出包装器显式调用输出。`module_function` 声明不补输出行为。最强“名称似输出／函数内部会打印”反方不成立。 | PASS |
| 上层是否打印返回值 | Compiler L940–947依序处理两个固定文件；L993–1018不消费修改函数返回值，L1020–1036进入内容后续和独立进度／完成输出。`020_Debug/003_Debug menus/002_Debug_MenuCommands.rb:1335–1344` 的完成消息也只在正常到达时独立请求。最强“返回值后来被打印”反方不成立。 | PASS |
| 正常／不变与输入边界 | 两种匹配更名都保留；已用新拼写且无匹配时不覆盖。源码匹配发生在属性行开头，不把任意文本同名片段当属性更名；本修订没有扩展输入域。更新器无交互确认或取消门。 | PASS |
| 失败与部分提交 | 读入早于覆盖；覆盖打开／写入失败向上传播，已打开覆盖后可能截断或部分写。第一个文件成功而第二个失败不撤回先前写入。候选 §3.2–3.3、§6（L36–57、L270–282）保留启动局部诊断／删除／转换与直接入口的区别；未新增事务或全量恢复承诺。 | PASS |
| 其它输出与累计保留 | 删除限定于该特定提示，未改为“编译静默”。§3.3、§5.3的正常完成／地图警告、§6异常及保存前缀均保留。全文件比较证明其余字节完全相同，测试目录及原接受／关闭记录未修改。 | PASS |
| 引用／验收同步 | 已读完整 `test-catalog/generic-kernel-wp02-03-04.md`（236行）。KL17固定路径、KL02–05及KL37–39入口／异常／完成场景不承诺该提示。正式集、planning、audit 检索仅原WP04 L196含该错误短语。章节、链接、现有ID未变，无必须的公共索引或目录改动。 | PASS |

原 counter 的 `necessary_sync` 曾提出 focused changed/unchanged vector；其最小修订同时使用条件措辞。原5caff prompt和最终完整合同 §5 的 `no_forced_new_tests` 明确不因补例有益而强制扩写，required target 仅WP04。候选 change-record 已承接 changed/unchanged 等四个静态场景；不据旧建议把正确目录未新增条目判为缺修。镜像相对链接按其未来正式目标位置解释，未要求把整个正式目录复制进候选树。

**边界场景复核**

以下全部为静态推导，未执行文件失败注入或参考行为。

| 场景 | 完整关键前提 | 独立推导 |
| --- | --- | --- |
| CHANGED | 固定默认formatter，无插件覆写；固定文件可读，存在匹配旧属性行，其余I/O正常 | 分别更名为VictoryBGM／Power；整文件覆盖写；无该特定提示请求。正常后续进度输出仍可到。 |
| UNCHANGED | 同样前提，已经新拼写，无其他匹配 | 不覆盖写，也无该提示请求。不能外推为没有其它编译输出。 |
| WRITEFAIL | 匹配且读入／格式化成功，覆盖打开或后续写入失败 | 异常传播；覆盖打开成功后可留截断／部分内容。格式化没有在失败前请求成功提示。启动及直接入口后续处理分别按原合同。 |
| SECOND-FILE-FAIL | trainer_types已正常重写，之后moves读／写失败 | 前一个文件结果不回滚，后继编译阶段未到；两个更新步骤均未请求该提示。若前一个文件自身失败，则第二个文件尚未处理。 |

默认源文本搜索及完整formatter／调用链未发现相反定义。辅助反方还只读解压核对固定 `Data/Scripts.rxdata` 的单个 Main 单位（49行，1,197 B，SHA256 `da24a2220936c6d44ddc60f180aed37beede022012d7addc99b5562ed07c52e1`），并读取外置 `999_Main/999_Main.rb:1–60`；无增加相反的 Console／Compiler 输出接合。该解压不求值、不执行 Ruby。动态插件、任意 monkey patch、宿主隐藏钩子和真实控制台画面不在静态结论内，不能宣称“所有扩展环境完全无声”。

**完整读取、历史与去向**

读取明细与责任见 `reading-ledger.json`。主审读取AGENTS、本批reviewer prompt全文及author prompt唯一差量、完整GR8-KER-003七组合约／assignment、完整候选与原句差量、change-record全部、协调记录及完整catalog。源相关完整函数／调用单位及formatter全文由主审重读，另由实际独立辅助反方核对。原5caff完整prompt、原counter完整对象、当前root envelope与findings的对应对象由辅助合同审者完整接收；重复对象按精确内容相等去重，不能把重复路径算额外审者或投票。

完整batch readset的结构、5个source/spec身份、64个root输入、8个额外伴件及继承／delta读集共79个固定载荷身份均独立机械验证通过。**机械读取与哈希核验不授79份全文语义FULL**。相关原根、counter、最终合同及当前历史资格作语义接收；其它领域全局payload只作不可变来源／导航，未重新审432源文件或131正式文件。三份accepted-facts/history/policy伴件的相关typed values接收：CREB身份／邮件／berry细节、WP39输入及视觉／设施policy没有被本批有限输出修订采纳，不开启其源单位复审或写集；未选optional继续未选。

GR8-KER-003的canonical root及P3必修分类保留，与GR7-M16-001活动Main、GR7-M04-101插件保护及GR7-J01-001复合节头仍按已接收历史区分。旧OPEN／UPDATE_NOT_STARTED是原快照时点，当前必要历史／消费者状态按最终root资格接收，不用旧快照重新阻断这次已获授权的候选复审。旧报告、旧关闭回执、root分类和统计均原字节留存；本报告不为已有历史增加新根或反复计票，也不把历史42个任务ID误称42个独立context。

去向影响限于WP04 §5.2 的输出边界澄清；不改变既有分类或章节去向，不授整篇重新打标完成。PBS编译owner可按本报告核实该句的有限行为。audit／planning目前没有需要改变的错误输出断言，实际整合若出现新公共贡献，仍由R8-INTEGRATOR逐项接收。

**验证与剩余门**

`verification.json`及其真实工具日志确认：候选只在原WP04做一次精确文字替换；基线到候选仅新增两个独立批次镜像／change-record及一个协调文件；deliverables、specs、planning、audit和AGENTS无变化。B8、基线和候选的正式树均为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。参考HEAD正确且工作区干净。

剩余工作是R8-INTEGRATOR将已审候选按真实冻结输入整合；实际非作者复核受影响正式全文及累计保留／共享贡献；随后主审分别登记ACCEPTED和CLOSED。本批无直接／传递语义前置批次，无候选修正阻塞。U03结果由其独立复审负责，不能用本报告替代。

用户告知本云任务创建请求为gpt-6.1-sol／ultra／default；两个辅助复核的实际spawn参数也显式指定gpt-6.1-sol／ultra，没有使用默认低推理审者或重复CLI配置探针。实际服务model／effort／tier／speed／Fast无权威runtime echo，逐字段仍记UNVERIFIED；请求参数不冒充服务端认证。

支持文件：`input-manifest.json`、`readset-identity-checks.json`、`verification.json`、`commands.jsonl`、`reading-ledger.json`、`review-result.json`。`verification-run.json`绑定实际exit／UTC及原始`verification.stdout.txt`、`verification.stderr.txt`；内部Git载荷读取仅存stdout身份hash，避免在新报告复制参考源码。可复跑 `verify-inputs.py` 作固定输入机械核验；它不执行参考实现。新写入仅本批独占review目录；不合并main，不force。
