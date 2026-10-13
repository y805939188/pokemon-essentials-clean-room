# R5-U03 WING 候选限定复验 — limited-wing-01

**限定候选 PASS。** 原唯一返修 `GR5-M05-004/static/04` / `R5U03-M05-004-02` 已补足消费前提；本轮新语义复验1项，其余59条static PASS和10项实际PASS仅按准确未变贡献/记录身份复用，完整11项语义重审0。候选必需返修为空。

候选/作者证据 commit `6ced99e1279bc947bfbc63d33ceaeb240b8f9f02`，tree `bb27f8dfee659ea77738c29cd989accabccee469`。原作者基线d84、提案9fab、冻结22f与原独立actualFAIL1eda完整身份见[manifest](review-manifest.json)。只签此固定候选的新一行及必要消费范围；**actual-02尚未提供或复审，候选PASS不授actual PASS、正式接受或CLOSED。** 原actual8b/1eda的FAIL记录保留。

## 新前提与消费路径

新目录第294行的WING输入是“须有合法作者记录，且为非重要物品、有效消费为真（Consumable省略或true）”。原目标/余量/库存1/独立正常使用前提及EV+1、扣1、重算预期均未变。完整新行461bytes，SHA256 `11c61cf1eaaa3cf78adbf47fb06dfbfc67afa46372cbeacf8178f0dffacc9c08`，候选目录UTF8字节偏移48464。旧387bytes行及其反例的固定签名仍在原报告。

固定R Item132–133对非重要物品缺省消费为真、显式true保留；189–197再次通过重要性和消费位。Effects762–832给六FEATHER→WING同能力+1及上限处理器，复制不改变记录消费属性。Utilities401–443在余量足/qty1时写对应EV并重算、正常后段返回真；袋消费者684–686与队伍消费者743–747同时要求效果真和有效消费真才扣qty。本向量库存1使正常上限/库存取小后qty1，因此各身份只改对应EV+1、重算并扣1。正常资源/界面/后段返回仍是静态前提，不认证运行。

原合法非重要 `Consumable=false` WING仍可使EV+1而不扣库存，但现在不满足“有效消费为真”；重要物品也不满足新前提。没有把false改成非法记录、把效果真等同可消费，或把复制效果当成复制数据。正常取消/资格或效果失败不扣、已完成效果后再取消不回滚、后段异常保留已写前缀、既有部分成功按传入qty扣减规则保持。当前WP27有效消费矩阵与WP28 §3.6的U01-O025 false反写/再编译例外均不改变，候选行与必要消费者相容。详见[新限定裁决](criterion-results.json)及[有限回归](regression-results.json)。

## 同步与未变复用

独立比对新候选与d84：只有 `/vectors/45/input`、U03 `/operations/49/new_text`（零基第50项）、专属目录294行及对应派生补丁/manifest改变；69中另68完整向量对象、52中另51操作对象、81中另80目录行、16中另15正文投影、31共享片段及28既有载荷保持。原expected和premises完整对象不变。当前作者一行增量patch与9fab提案patch完整3597bytes相同；完整B5投影/增量补丁回放和当前manifest身份由[独立工具核验](independent-validation.json)绑定，未拿作者validator替代独立审查。

本轮独立结构套件567项TOOL_VALIDATION均PASS，另保留2处历史MISMATCH；当前manifest的38个artifact完整身份匹配。oldactual8b的一行scratch回放只验证提案投影，不是actual-02已存在或已复审的证明。

原1eda的59条static PASS逐记录指针/hash已独立核实，未变10项签名只对应原具名范围；M05-004其它4条参数/资格static继续按精确未变资格复用。没有新签这些范围、扩大必修分母、签整共享文件或将旧actualPASS转到尚不存在的actual-02。两处冻结历史整文件SHA MISMATCH保持原裁决，原v2漏检与actualFAIL不回写，精确历史owner/scope和未变证据继续复用；不重新下载全局证据或重开global review。

U01→U03限定上游门SATISFIED沿原固定接受回执及1eda门状态复用。接下来只允许R5-I机械接入这一已审候选行并冻结actual-02，再由原审者定向核精确实际增量和必要消费影响；无需重新进行完整11项审查。8共享整文件、U08及关闭激活仍WAIT全部贡献/相应精确验收，正式接受、CLOSED及公共登记写入均0。

## 发布与执行限制

原非作者 `/root` 与原语义/结构子审完成本次有限复验。请求gpt-6.1-sol/ultra/default普速禁Fast，实际模型/推理/服务回显UNVERIFIED；平台任务UUID未暴露，不拿source thread或环境ID替代，未审计额度/认证。R4历史隔离执行4、R5review历史隔离执行4分别复用且未重跑；**本update新增参考/模型/宿主/Demo行为执行0**。69向量仍DERIVED_VECTOR/NOT_EXECUTED，新增JSON/Git/hash/patch检查仅TOOL_VALIDATION。原宿主/媒体/完整Demo/真实存档/其它组合/optional/兼容政策限制保留。

只新增 `review/remediation-fifth-20261013-prepare/reviews/R5-U03/candidate/limited-wing-01/`，未改作者/正式/公共登记或原候选与actual报告，未merge/push main、未访问Mac。普通推送 `codex/r5-u03-independent-review-20261013`；[后继读回回执](remote-readback.json)固定核心6新增载荷完整bytes/SHA256/blob，最终7载荷在固定发布commit完整读回。发布身份与候选受审身份分别绑定，读回不授actual/接受/关闭。
