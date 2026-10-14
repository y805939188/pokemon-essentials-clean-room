# R6-H / supplement-inventory 独立报告

本子任务在唯一写目录 `tasks/R6-H/subtasks/supplement-inventory/` 完成其分配的有效补充全文、原稿 primary 结构关系、root inventory/assignment 结构反证和资源工具证据资格核查。**未提出新的必修 finding；这不是全项目游戏语义 PASS，也不代替主领域审者的新语义阅读或 R6-H 的历史回执裁决。**

固定输入独立验证：main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6` 的 tree=`6ab3429170d2762607fbc2237014c3a160449fa1`；正式 subtree=`1046fbb657882e84b3dfc6d017943a9edf7782e5`；R commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的 tree=`7589c800b61ba13a13040ed0d686979b80a84fd0`。本任务 actual model/effort/tier/speed/UUID 均 UNVERIFIED。未查询配置、认证或额度。

## 实际读与分母

| 载荷 | 本轮实际范围 | 身份与用途 | 不可外推部分 |
| --- | --- | --- | --- |
| `planning/coverage.md` | 1–287 全文 | 当前覆盖支撑与分层历史导航；历史来源覆盖、阅读、字符串命中三种计数明确分开（171–186、254–259） | 历史无缺口、旧 PASS 不代替第六轮行为结论 |
| `planning/feature-matrix.md` | 1–499 全文；131–230 曾显示截断，181–199 重新实际阅读 | 113 高层 Feature 的归属/当前与历史状态；每条规则唯一 primary，跨域引用（264–271） | 113 不是具体 requirement 数；92 表中的旧 OPEN_REQUIRED 是生成时点 |
| `audit/source-traceability.md` | 1–1761 连续全文 | 当前/历史来源与原稿身份审计；全部 T 条目及补充/第三/第五轮后继读完 | 旧被审哈希/已读声明不签新字节或新阅读 |
| 正式 `README.md` | 1–167 全文 | 使用/范围入口，111 正文＋17 测试族＋1 索引＋2 根入口=131 | 历史“当前”与候选接受层必须按后继回执解释 |
| 正式 `scope-statement.md` | 1–153 全文 | 约束全正式集；素材/宿主/运行边界 | 静态不证明真实宿主或完整 Demo |
| 正式 `test-catalog/README.md` | 1–125 全文 | 17 测试族导航；静态设计非执行 | 条目数不是贡献数或实际执行数 |
| 原 `specs/demo/wp01-baseline-and-evidence-scope.md` | 1–156 全文 | 保留基线/材料范围输入，明确不提取具体游戏规则（24–30、108–110） | 不新增游戏正文或行为分母 |
| 原 `specs/kernel/wp02-settings-inventory-appendix.md` | 1–236 全文 | 参考侧逐定义取证；118 常量、3 方法、3 元信息分开；引用/候选不是语义全覆盖（174–205、232–236） | 不变成未来 API；生成身份不等于新的游戏需求 |
| 全原稿 `specs/**` 113 | 全路径/blob/hash/bytes/lines、全2422个标题及表结构；111其余原稿不在本子任务做游戏语义复审 | 113 个原稿全部有 primary 去向（详见逐行矩阵） | 结构解析不自动成为语义 PASS |

有效补充**可得路径口径为116=三份当前支撑＋113原稿**。其内部类型必须保留：三份当前支撑、111个以正式正文为 primary 的二级原稿、两份保留审计/范围原稿。独立保留载荷口径为5=三份支撑＋两份保留原稿。它们不增加独立游戏 requirement 分母；不能把116、5、113、111、131相加当“游戏覆盖总数”。三份正式共享入口本身已包含于131，亦不另加。

## 双向 primary 核查

`specs113-primary-matrix.json` 为完整113行的 source→primary，并有 source blob/hash/精确 T clause/输入行；`primary113-reverse.json` 为正式131行的反向原稿关系；`forward-matrix.json` / `reverse-matrix.json` 补充本任务资格事实与 consumer、当前 clause、前提。

- 111个正式分类正文各有一个对应原稿，无缺 primary 正文、无无归属原稿。
- WP16 战前过渡原名含 `-appendix`，正式 primary 去掉该后缀，audit 192–203 明确承接；这是重命名关系。
- WP01 原稿由正式 scope 范围承接，audit 354–365 明确无独立游戏正文。
- WP02 设置附表由正式 WP02 词典承接，行号/检索仍为原批准取证锚点，audit 220–231 明确未整表复制。
- 17测试族及其README、根README/scope按派生测试/使用/范围身份处理；不能要求每个测试索引具有一个新增游戏原稿。
- 111原稿与正式正文当前字节可能不同；本核查不转移旧批准或 blob PASS，也不据原稿头部旧 ReviewPending 重开历史控制。共享入口的第五轮历史段明确留史（正式 README 153–167、scope 139–153、测试README111–125；三补充相应末段）。有效当前92关闭/精确proposed选择由父 R6-H 的 activation/report-index 专项核验裁定，本子任务未借这些旧段推翻该回执。

## root inventory 与 assignment 反证

独立从固定 Git 对象重新枚举、取 blob 并对比。`reference-inventory-countercheck.json`：432路径/字节/hash/blob/mode/commit无缺漏、无重复或错误；`formal-inventory-countercheck.json`：131同样无错误。`formal-block-countercheck.json` 验证20,379有限块覆盖所有正式非空行恰好一次，无交叠、越界、空白误计或未知路径。**20,379含标题、表头、分隔符和历史行政块，不能解释为20,379个行为条款。**

`workspace-inventory-countercheck.json` 与 `workspace-types-full.json` 覆盖固定main全部38,093个blob：正式131、当前支撑3、原稿113、历史review或当前登记证据37,763、生成清单/生成程序5、侦察规划导航5、其余行政metadata73。类型是完整路径/blob的用途处置，并非对37,763个历史/登记payload逐语义认可；有效阶段资格仍按任务专项证据。

R6-C/O/K 当前库存合并确实覆盖128正式域文件与312个Scripts路径，未发现虚构路径。共享三个正式入口由本子任务实际全文读取。其余120参考路径按冻结D/B prompts与root资源分配可定位：D104（PBS73＋核心文本18＋字体8＋两serialized＋两BMP＋mkxp），B15（根作者工具/程序/metadata），I1（SF2）。故**分配规划覆盖432**；实际全局语义完成状态不由分配表推造，需各审者 ledger/matrix 与 root 汇总。此处不声称C/O/K/B/D已读完。

## 资源审计证据资格反证

全文读懂 root `tools/inventory.py:1–47`、`audit_resources.py:1–316`、`audit_binaries.py:1–468`。没有执行原root默认main。只把完整已理解的静态解析工具复制到本目录，将ROOT重绑至从固定R对象独立提取的六个输入，输出限 `resource-check/`。六输入与参考工作树逐字一致，哈希/输入绑定见 `resource-check/binding.json`。两个新解析器退出0，stdout/stderr/exit见 `logs/fresh-*.json`；新payload与root两份完整payload（仅独立身份字段分开）相等，见 `resource-countercheck.json`。

SF2本次结构范围：九表25,786记录含sentinel、1,524 voice links、2,000,710 PCM点和guard/gap全部统计；106空选择，42 nominal range＋2非零ignored terminal观察保留，`format_conformance_claim=false` / host UNKNOWN。默认滤波调制器的外部版本文本歧义仍是条件投影；未选择真实宿主政策。固定 `mkxp.json:1–159` 全文读，64–66只给MIDI SoundFont配置接线，不能证明当前实际MIDI、输出或样本可听。

PE结构范围：五文件全部固定身份、分区/导入/导出/COFF/resource/CLI heap与15 CIL方法的完整字节解码；仅工具结构。Game60个可读block（shader、兼容脚本等）的存在不能打包成机器码opaque limit；B/root仍分别承担新语义阅读。本次不把全部字符串扫描当逐字符串语义通过，不把 `all_instruction_bytes_decoded` 当完整CIL业务或依赖实现验证，不替B审者读取逐指令业务。

普通对照/最小反证：SF2配置名存在但真实MIDI材料缺失，已解析PCM不能推出实际声音；同样PE导入或selected literal存在并不推出路径可达；106个空声部选择不会因“1,524 links”统计成为播放成功。正式WP15已全文新读1–220，132/148/162/194/201/216–219明确把逻辑登记/请求与实际宿主发声/媒体分开。因此当前解析证据无需把可选资源兼容政策扩成必修游戏合同，也不允许因unknown host而关闭可读静态范围。

## 结论与剩余边界

本分配范围全文未读0、结构未处理0；`reading-ledger.jsonl` 的自动读记录永远不自动标语义PASS，独立判读在本报告及矩阵中。findings为独立空数组，由root保留最终裁决权。参考程序执行0，独立行为模型0，完整host/Demo0；新解析为TOOL_VALIDATION，资源/登记推导为STATIC/DERIVED，不借旧结果。其他领域当前全部unit/clause语义及父R6-H六发布载荷/回执历史资格不在本子任务结论中关闭。未改formal/specs/planning/audit/reference/旧报告，未git切换、提交、push或启动update。
