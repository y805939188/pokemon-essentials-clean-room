# R8-U06 独立身份、范围与证据资格审计

结论：本子审计未发现输入身份、候选写集、目录保留或发布绑定的阻断项。此结论仅为身份与范围支持证据，不授予 candidate PASS、actual integrated PASS、ACCEPTED 或 CLOSED；行为正确性及受影响整文件语义由独立主审汇总。

审计者为新任务 `/root/identity_scope_audit`，未参与候选写作。固定审查 HEAD `16f986afc1c85e64131f1dc8c6f2477a79c04029`，基线 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`；载荷 `0384629ccf1c2c492ebab611bbbb858f825e9a31`。actual model、effort、tier、speed、Fast 均无权威 echo，逐项 `UNVERIFIED`。没有探测 CLI 或执行作者 `verify_candidate.py`；已只读审查该脚本，确认它会写候选证据且要求作者分支，不能用于本审查工作树。

## 分母与独立结果

所有逐项期望值、观察值、Git 命令 exit/UTC/流摘要均见 [identity-checks.json](identity-checks.json)，重做脚本为 [verify_identity.py](verify_identity.py)。原始来源与当前恢复位置分别核对，未将历史来源统一改成 C35。

| 身份集合 | 分母来源 | 独立结果及资格 |
| --- | --- | --- |
| 继承输入132 | 固定本批 readset 的 `inherited_contents.source_spec_files` 60（39源、21规格）＋`mandatory_root_input` 64＋`additional_mandatory_companions` 8 | 132/132；共11,442,951B，逐项 byte/SHA256/blob/mode、声明的树身份均吻合 |
| 当前恢复别名57 | 上述64根输入中实际具有 `current_recovered_at` 的57项 | 57/57；是第二身份，不另算历史根或新增语义输入 |
| delta72 | `delta_contents.units` 的全批72个身份条目 | 72/72；只有56个不同 repo/commit/path，不能称72个不同文件。U06相关CP002为21、CP01为6；其余条目只作身份核验，未选择其optional |
| F05条件读集10 | `conditional_F05_readset` 六源、三正式单位、一个原候选 | 10/10；六源具名单元另核截取字节/SHA，均吻合；不把具名单位当整源全文语义实读 |
| 作者额外阅读定位157 | `author-reading-ledger.json.actual_additional_source_and_formal_units` | 157/157整文件/范围SHA等声明吻合，仅核定位完整性，不继承作者实读信用 |
| mirror12 | 原11文件写集加已选择F05的WP58 | 12/12；共534,372B；当前工作文件、HEAD、038载荷以及manifest的bytes/SHA/blob均一致 |

这些分母存在交叠，不能相加成新的系统覆盖率。作者132条检查亦逐条映射到本人独立核验所得身份，132/132吻合；没有以作者 `verified=true` 作为验收依据。

## 写集与授权

当前授权来自父协调任务传入的用户决定：本批11必修及3个已采用可选。14项 disposition 的ID、classification、severity、current pointer、原来源/C35恢复绑定及root裁决均与固定合同逐项相同。11个required完整对应本批assignment；3个optional仍为optional，不升必修、不新增历史根。

- AI002只修“20直接＋5复制＝25”计数句，收益是减少覆盖核验歧义；既有行为表保留。
- CP01只修同篇暂停消息括注的先置标记/胜利限定，收益是避免误解既有时序；CP002仍独立。
- F05只替WP58原L105归属短语并指向既有WP76 §7.2，收益是区分辅助返回与实际AI主路径；WP76、RC-W11和RC29继续只读，保WP76-R12/R6-DX-DEBUG-004/GIR-FD82-B029关闭资格。

这三项均落在已授权的低风险理解/验证范围。其它7个optional无代选、无写入；独立视觉policy保持未选。14项四门均仍为false/pending。共享正式整文件、公共追溯/索引及接收台账仍由R8-INTEGRATOR唯一写；本批直接及传递语义前置批次为空，共享文件接收与发布门未被改称语义依赖。

基线至HEAD恰有27个新增文件，全部位于本批candidate目录（15非mirror＋12mirror），无正式目标或其它批改动。提交链为 `4575… → 69492… → 038462… → 16f986…`。B8、基线、载荷与HEAD的正式树均为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。本人只读远端查询：main仍为 `fd1df570cad987dc3852a3b958f03916e317f7fe`，候选分支为固定HEAD；本审查新分支远端尚不存在。参考HEAD仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，参考工作树干净。

## 目录、锚点及引用

独立按整表行多重集及ID比较：三个共享目录原行全部保留，唯一已修改原行是AE族同ID的T02；没有改号或删除旧行。新增Z01–05、M01–04、EV01–02、CV01–05、ST01–05共21个独立ID，原各族计数未被重算。新增7个显式锚点各自唯一，原锚点及标题行保留；镜像内7条Markdown相对文件链接按候选已有文件或正式目标路径投影到固定baseline均可解析，并非声称mirror自含所有依赖。非mirror入口的包内相对文件导航也均存在。正文WP39 §4.3.1、WP19 §5.3、WP30 §4.4、WP42 §4.2、WP52-A §6及WP67-A §9.3的引用/锚点与交接定位对应；WP76引用为文字章节定位。

本人独立从12镜像和基线重建零上下文差异，逐字节等于 `candidate.diff`（32,768B，SHA256 `ab42e9acad64fc9ee53d3e204388c4ee760c02614f477654731ab519c8356fe7`）。目录保留和引用存在只证明结构及范围，不代替控制向量语义判断。

## 命令及回读资格

已读命令40条和发布命令72条的完整记录。ISO UTC起止有序，保留stdout/stderr/exit；有stdout哈希的记录均重算相符。blob读取的stdout为null时，按其固定commit/path独立取完整字节核对bytes/SHA；这类记录有载荷完整性信用，不能冒称公开的语义全文阅读。两次历史receipt分别对69492载荷24文件、038载荷26文件，全部bytes/SHA/blob与相应Git对象一致；不能把旧receipt解释为后继证据文件已自包含。

日志保留两次失败：`commands.jsonl`第16条cached whitespace检查exit2，其后第24/32/40条为exit0；`publication-commands.jsonl`第38条复用浅仓库校验ref的fetch因non-fast-forward拒绝，其后改用每SHA新bare仓库，42条fetch成功。记录中的“forced update”是该浅仓库本地tracking ref提示；实际push argv无force，Git祖先链及远端main也与说明相符。未把这些失败抹成全命令成功。

作者62项静态检查均按TOOL_VALIDATION核读，包括纯算术及登记清点；这些不是本人62项语义审查，也不是Ruby/游戏/宿主/媒体/真实保存回放执行。作者阅读账本明确未捕获原读取窗口UTC/opaque操作ID，本人不能验证其未记录操作发生时间或倒填实读信用。

父主审另行fresh空bare、无alternates从远端回读固定16f全部27文件，见 [candidate-remote-readback.json](candidate-remote-readback.json)。该独立transport证明归父主审，未计为本人语义实读或业务运行。

## 阅读边界及剩余门

本子审查覆盖15份非mirror的全部审计内容：正文/脚本/diff连续阅读，JSON全结构及全部有意义的文字、声明定位和资格分组读取；重复的身份/来源值另以逐字段机器等值核验，方法与修复过的截断范围见 [scope-reading-ledger.json](scope-reading-ledger.json)。未将JSON parse、hash、旧reader FULL或作者自述称为本人source/formal全文语义审读。整批prompt/readset完整语义阅读及12个最终镜像全文由父主审与具名语义分审承担。

身份与范围审计无未决阻断。实际整合尚未发生；整合者需冻结新的实际输入SHA、逐贡献接收、完整核验最终共享整文件，再分别登记actual integrated PASS、ACCEPTED、CLOSED。当前不关闭历史根、不推main、不提交或push本子审计。
