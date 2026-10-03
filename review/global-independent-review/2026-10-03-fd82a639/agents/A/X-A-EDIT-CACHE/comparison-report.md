# X-A-EDIT-CACHE 第二阶段比对

2026-10-03 15:52:08 UTC。先前四份阶段一文件保持原字节；独立首判保存于 2026-10-03 15:43:54 UTC，早于以下 C 记录与 root 旧疑点的授权读取。固定项目和参考提交、完整前提及静态向量沿用 independent-judgment.md/json。仅核对 root 指派的 11 个 C finding 及 C005 的指标扩展，不新增 RUN-A finding、不重复统计 WP72/73，不改正式规格、C 报告或任何参考文件。

## 授权输入

- `01fa3c2f36923127eff9168abe142aca8b6d787b` · `review/global-independent-review/2026-10-03-fd82a639/agents/C/C-01/findings.json`：findings IDs RUN-C-001/002/003/004/005/007 only；ID/正文行 24,80,152,216,312,498。
- `02ad5b24f8adea87cff94447a807912d2660391c` · `review/global-independent-review/2026-10-03-fd82a639/agents/C/C-01-S1/findings.json`：findings ID RUN-C-013 only；ID/正文行 413。
- `d894d127c7d83de065f2d78a2223866cd5652367` · `review/global-independent-review/2026-10-03-fd82a639/agents/C/C-01-S2/findings.json`：findings IDs RUN-C-016/019/021/022; existing_findings_extensions ID RUN-C-005 only；ID/正文行 22,277,436,518,695。
- `e2b00662b2515e2a8c82d1037a5f8d0fc254d0a5` · `review/global-independent-review/2026-10-03-fd82a639/root/language-semantics-review-note.md`：complete authorized note；ID/正文行 1–9。

读取时用固定 Git 对象解析后仅输出授权 ID；没有打开其它当前 C 发现。根旧疑点是争议材料，不作权威结论。

## 对应与裁定

| 首轮 ID | A 独立场景 | 比对结论 | A建议 | C建议 | 有界说明 |
| --- | --- | --- | --- | --- | --- |
| RUN-C-001 | XA-SW-PREFIX | CONFIRMED | P3 | P2 | 字面码点判断一致；A 保留 P3 建议，统一优先级由 root 裁定。 |
| RUN-C-002 | XA-SW-DEPENDENCY | CONFIRMED | P2 | P2 | 原值读写与表达式依赖不是同一层；自引用反例与常量对照一致。 |
| RUN-C-003 | XA-CANCEL-TYPE | CONFIRMED | P3 | P2 | 两个子型前提丢失已独立证实；A 保留 P3 建议。 |
| RUN-C-004 | XA-ENCOUNTER-LAYERS | CONFIRMED | P2 | P2 | 只绑定0→PBS省略→默认21的文件往返；不把旧地图快照混为同一根因。 |
| RUN-C-005 | XA-ENCOUNTER-LAYERS | CONFIRMED | P2 | P2 | 绑定保存/编译/同值版本写入不重装当前快照；变化版本与地图进入才装配。补读淡入淡出及计数包装，无隐藏遭遇重装。 |
| RUN-C-007 | XA-EFFECT-CATALOG | CONFIRMED | P2 | P2 | 120项逐项对照一致，最终包缺目录；匹配数量只为辅助证据。 |
| RUN-C-013 | XA-SINGLE-PLAYER-BREAK | CONFIRMED_LANGUAGE_CONDITIONAL | P2 | P2 | 非lambda break 的目标为已返回的创建调用；源注册/调用链支持LocalJumpError，宿主最外层反馈未证。 |
| RUN-C-016 | XA-METRICS-LAYERS | CONFIRMED_WITH_EXPLICIT_SAVE_TIME_PREMISE | P2 | P2 | 路径由保存时非0形态后缀产生；五组相等也按保存时比较；预览导致空后缀懒登记需另列。 |
| RUN-C-019 | XA-WEATHER-CANCEL | CONFIRMED | P2 | P2 | 列表取消/None与概率BACK不同；W2/30返回及父保存门一致。 |
| RUN-C-021 | XA-IV-EV-MATERIALIZE | CONFIRMED_IV_EV_WITH_POST_JUDGMENT_MAPSIZE_CHECK | P2 | P2 | 首判独立覆盖IV/EV；MapSize部分在比对阶段依据先前已读子页及新读元数据定义确认，不倒算为盲审首判。 |
| RUN-C-022 | XA-SPECIES-EVOLUTION-KEY | CONFIRMED | P2 | P2 | 复数编辑键与单数写出键不同；父No、父Yes、显式反写及整体重编译四段与首判一致。 |
| RUN-C-005 extension | XA-METRICS-LAYERS | CONFIRMED | P2 | P2 | 预览先消费登记；已布局战斗精灵普通update不重新取指标，保存/重载不广播重定位。 |

## break 与 return 的关键区别

RUN-C-013 的来源分支使用 break。普通非lambda块的 break 关联接受该块的创建调用；这里注册值先通过 proc 创建，创建调用已返回，后来才由 MenuHandlers 直接调用。它不会因为调用侧处于菜单循环就自动退出那个循环。标准 Ruby 下，这个分支在消息之后、选择角色之前抛 LocalJumpError。

root 旧记录第5–7行把疑问放在“包围方法／载入执行上下文是否已返回”上；那是分析非lambda return 时需要区分的目标，不能用来否定此处 break 的已结束创建调用。这个修正来自首次独立判断和具体源调用链，与 [Ruby 3.1 Proc 官方文档](https://docs.ruby-lang.org/en/3.1/Proc.html) 的 Lambda and non-lambda semantics / Orphaned Proc 一致。root 本轮授权消息也说明已撤回混淆前提；本报告仍自行依据源链及语言规则判断。

结论仅到本地菜单调用链异常上抛。Scripts.rxdata 未解包，宿主版本、外层捕获后的消息、恢复、重启或退出进程均未验证；不能把静态语言错误写成实测崩溃。C-013 自身已保留这些前提，因此可确认其有界静态失败记录，无需凭旧疑点继续悬置已明确的 break 目标。

## 比对阶段补充与限定

- RUN-C-005：新增阅读参考 `Data/Scripts/007_Objects and windows/002_MessageConfig.rb:544–591`，包装只管理淡入淡出与淡出计数，没有重装遭遇数据；保存和编译后的旧快照结论保持。
- RUN-C-013：补读 `Data/Scripts/003_Game processing/005_Event_Handlers.rb:97–112`，注册容器保存原值，无转换成lambda或立即执行；与先前 `006_Event_HandlerCollections.rb:83–86,118–123`、菜单调用127–145一致。
- RUN-C-021 的 MapSize 是首轮记录超出 A 首判条目的附加范围。第一阶段已读 `002_Editor_DataTypes.rb:730–738`，但首判没有给它结论；比对后补读 `010_Data/002_PBS data/018_MapMetadata.rb:1–138`。原字段未指定，打开该子页即建立宽0/空有效格文本，直接BACK返回此结构；父No丢弃新局部值，父Yes经 `001_EditorScreens.rb:793–816`登记与保存。宽1–30是打开宽度数字输入后的约束，不约束只打开子页即BACK的路径。此确认标为比对阶段补充，不伪称盲审首判已涵盖。
- RUN-C-016：四种登记集合均按保存时判定。仅“编辑前非0与基础相等”不足以省略非0记录；本场景只改基础时通常变为不等。非0查询的空后缀默认也不能写成继承基础后缀。C原记录与这些限定不矛盾。
- RUN-C-022：父Yes只重登记被选中的A；其它物种B的旧前身条目暂留登记/档案，随后PBS成功整体编译才按剩余正向边重建。No后另行反写会触发单数字段的参数转文本，不能反推仅打开父页就触发。
- RUN-C-001/003：事实和必要修订无争议，仅优先级建议不同。A 的 P3 原建议保留；本报告不私自改为 C 的 P2，也不替 root 做统一优先级裁定。

除上述具名扩展与前提澄清，没有发现需要推翻 C 指派记录或 A 首判的反证。11个 finding 与1个既有扩展均在上述范围得到第二判断；这不等于对应整 WP 通过。

## 证据与发布边界

第一阶段的77条阅读映射及120行目录对应保持不变；新读取材料在 comparison-reading-log.tsv 单独列出。首次与比对后的参考阅读均只读固定参考；运行观察0、已证明demo链0，U01–U10、G01–G12、20AX保持。仅以文本字段比对检查120项，不执行参考或用模型程序模拟规则。阶段一字节身份只为“首判先于首轮且不被改写”的必要校验记录于 checkpoint.json，不建立全仓哈希台账。
