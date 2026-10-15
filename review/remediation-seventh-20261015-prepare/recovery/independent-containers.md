# 跨独立容器的固定输入、证据与候选恢复

本说明补充既有准备，不改变27项/13批合同，不启动或重新派发作者。原精简prompt及完整合同仍固定于 `f622356f3beb9e84ea8cff9db07c7fb382565d3f`；启动记录及首次发布回执固定于 `e1fc80c90a0bb5a7eeb00087bd7f95ed63faec1c`。本补充自己的发布commit由最终回传在包外绑定，禁止用浮动分支代替固定输入。

当前整合环境恢复后仍是 `/workspace/pokemon-essentials-clean-room`，分支 `codex/remediation-seventh-20261015-cloud`；原缓存、参考、已解码证据和启动失败日志均保留。没有重跑全包核验，没有重试CLI或创建作者/reviewer。这里的本地空任务记录不能证明父会话或其它容器没有活动任务；去重以父会话真实task/context及派发登记为准。

## 哪些成果可以跨容器取得

Git中已发布的合同、26份精简prompt、批次/冲突图、启动身份/恢复记录、旧失败及发布回执可按上述固定commit/path获取。R7原始证据在固定C2 `4580645dfbfec4a3c7ccbad56ae293cc619b0d25` 的无损gzip对象中。固定B为 `e646432c644dec04d306842cc5a559a29c718fbc`；参考R为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，仓库 `Maruno17/pokemon-essentials`。

`/workspace/r7-input-cache`、`/workspace/r7-evidence`、`/workspace/r7-reference`、`/workspace/r7-launch-logs`、`/workspace/r7-remote-readback` 是本整合环境的本地目录。独立容器不会自动共享它们，不得把原prompt中的这些绝对路径直接当成新容器已存在的文件。原Mac路径只是历史来源元资料，不连接Mac、不伪称路径相同。

## 独立容器的有界恢复

本补充提供 `recovery/batches/R7-Uxx.json` 和标准库工具 `tools/restore_container_context.py`。每批清单只含原七组明确引用的文件/snapshot、binding_id对应原载荷、C13身份/输入/原绑定表及L01–L14；另含该批固定源/正式输入身份。每批7–11个逻辑证据文件，解码约1.3–6.2MB；不读取80MB Manifest、不扫描完整core索引、不恢复19GB全包。具体数量见 `selection-summary.json`。

工具从不可变远端URL读取合同、prompt、指定gzip及固定源/正式文件。编码对象核大小和Git blob；解码结果核原bytes/SHA256/Git blob。固定输入也逐文件核这三项。恢复只是传输/身份验证，不获得语义PASS或运行信用；下载的源、脚本、native文件一律只读，不执行。

父会话应先从本补充最终固定commit取出并阅读工具及本批清单。若该容器已有所需Git对象，可用 `git show <本补充固定commit>:review/remediation-seventh-20261015-prepare/tools/restore_container_context.py` 读取；无须切换、reset或合并当前checkout。也可从同一固定commit的GitHub raw URL取出两文件到 `/workspace/r7-bootstrap/tools/` 和 `/workspace/r7-bootstrap/recovery/batches/`。不要直接运行未读的下载程序。

读取后运行，例如：

```bash
python3 /workspace/r7-bootstrap/tools/restore_container_context.py \
  --plan-directory /workspace/r7-bootstrap/recovery/batches \
  --batch R7-U01 \
  --destination /workspace/r7-context/R7-U01
```

已有本仓库完整本补充checkout时，直接运行仓库内同名工具即可。默认同时恢复固定读输入；只有另有已核固定源/正式checkout时才可加 `--evidence-only`。目的目录必须新建。连接失败保留部分文件和失败回执；在同一容器、同一目录加 `--resume` 重试，只复用已匹配的精确字节，不覆盖冲突字节，不另建替代任务。传输内部只对连接/429/5xx最多重试3次。

恢复成功后得到：

| 目录 | 用途 |
| --- | --- |
| `dispatch/delegation/contracts/R7-Uxx.json` | 原七组完整合同，固定f622356f |
| `dispatch/delegation/prompts/R7-Uxx-author.md`、`-reviewer.md` | 原精简入口，固定f622356f |
| `evidence/tasks/R7-C13/` | 本批引用的原提案、反证和身份绑定，保留原逻辑路径 |
| `evidence/tasks/R7-C17/limits-and-alias-reception.json` | 当前用途的L01–L14边界 |
| `evidence/tasks/R7-C01/`（部分批次） | 七组明确指向的额外独立接收文件 |
| `inputs/project/` | 固定B及具名历史commit的正文/索引快照，只读 |
| `inputs/reference/` | 固定R的被引用参考文件快照，只读 |
| `transport/` | 本次实际取得的gzip编码对象，供精确恢复重试 |
| `recovery-receipt-<UTC>.json` | 每个真实HTTP/复用结果、身份、路径映射、完整/部分状态 |

这些是有界文件快照，不是完整reference Git checkout；不能因此声称参考整树、宿主或所有依赖已重新核验。U10/U11两个旧identity原commit为NOT_ASSERTED，清单另记固定B相同字节的真实恢复定位，保留原资格；未来导航勘误等尚不存在的输出不下载，不造旧输入。

父会话在原prompt前追加以下路径说明即可，不必改写原冻结prompt：实际可写项目用本容器checkout；原 `/workspace/r7-evidence` 映射到 `<destination>/evidence`，原 `/workspace/r7-reference` 映射到 `<destination>/inputs/reference`；固定正文读取 `<destination>/inputs/project/<path>`。作者只写实际项目的 `candidates/R7-Uxx/<完整目标路径>` 及本批证据。恢复输入目录保持只读。若原七组追溯中出现新的具体依赖，保留精确locator并由R7-I定向补取，不能把可读但未恢复材料改标为limit。

## 作者候选与reviewer结果另行传回

本工具只恢复冻结输入，不含任何作者候选，也不创建candidate-input.json。原任务仍由父会话按真实task ID去重派发；CLI旧PID1417已在创建thread前退出，不能当活动作者。

独立作者容器完成后，交付平台导出的候选文件/补丁或平台给出的真实结果commit。范围仅 `candidates/<batch>/`，并带完整artifact-manifest、原B身份、新字节身份、实际context和作者证据；维持原prompt“不自行提交/推送”的指令，使用平台成果传输，不额外授权作者修改正式分支。只回报容器绝对路径不足以交付；未跟踪新文件也必须包含在导出中。

R7-I取得结果后，在新的接收暂存目录检查真实差异和逐文件身份，确认无formal/reference/公共台账越权写入，再登记冻结候选输入。若平台给出真实可fetch结果commit，可普通只读fetch、按固定路径读回，不合并整个作者分支到正式整改分支。无法取得完整产物时保留WAIT，不以作者口头PASS替代。

reviewer独立容器还必须取得R7-I冻结的candidate-input.json及相应候选完整文件/证据，绑定真实作者context、结果commit/tree或逐文件bytes/SHA/blob。只有固定原证据恢复成功而无候选时，reviewer仍不能开审。审者输出同样通过平台成果传回，R7-I逐身份接收。候选PASS、实际整合后的新R7-IR PASS、ACCEPTED、CLOSED保持原门；分母27项/13批不变。

## 本补充的实际验证范围

已在同一选定环境的新隔离目录，通过不可变远端URL完成U01的40文件/7,539,352字节恢复，不读取本环境旧证据目录；随后 `--resume` 全部复用匹配字节且没有HTTP读取。U08另核同一编码对象对应三个逻辑路径的并发恢复，14文件/5,750,326字节（evidence-only）。真实回执见 `probe-U01-remote.json`、`probe-U01-resume.json`、`probe-U08-shared-object.json`。

这是隔离目录恢复试验，不是实际独立容器执行证明；本工具无创建容器或任务能力。未重新验证其它12批全部源输入的远端传输或运行行为，也未启动作者/reviewer。模型有效配置仍UNVERIFIED；L01–L14、SOURCE_STATIC/DERIVED_VECTOR/TOOL_VALIDATION及宿主/Demo/native媒体/真实存档回放的原边界完整保留。
