# WP07 规格：诊断、文件与 HTTP

| 字段 | 内容 |
| --- | --- |
| 工作包 | WP07（诊断、文件与 HTTP） |
| 关联功能 | F01-06（诊断与错误反馈，D01）、F01-07（文件与 HTTP 支持，D01） |
| 分类 | Generic Kernel（基础 I/O 与诊断）；路径与函数名是参考侧取证记录，不是未来框架的文件/网络 API |
| 参考基线 | `reference/pokemon-essentials/` @ commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（WP01 固定） |
| 输入 | 证据包 E03、E05、E08、E11（文件/资源/控制台）、E30（下载调用者）；HTTP 包装与实际调用者；调试入口 |
| 前置依赖 | WP01（基线）、WP03（内容身份），均已 Reviewed |
| 规格状态 | **ReviewPending（WP07 自身范围）**：2026-09-19 提交外部 review |
| 证据等级 | 全部为静态证据：已定位 / 静态确认 / 数据样本确认；**无运行确认** |

## 1. 目的、范围与非目标

**目的**：明确基础 I/O 的成功、失败与反馈——文件遍历/存在性/读写、HTTP 下载与提交、异常与错误的记录/提示/恢复分别在哪一层发生、以什么形式表现（异常、空结果、错误记录、用户提示）。后续包据此判断"某失败会如何呈现、能否被调用方区分"，而不是各自重新追踪 I/O 包装。

**范围**（WP07 自身声明范围，extraction-plan 第 2.1 节 (a) 类）：

1. WP07-A：文件访问层（遍历、存在性、读写、资源解析、保存目录）。
2. WP07-B：HTTP 下载/提交（包装、失败归一、响应使用与文件落盘）。
3. WP07-C：诊断与错误反馈（异常格式化、错误日志、调试日志、控制台、用户提示）。
4. WP07-D：失败层次与边界（各层失败形式对照与共用面）。
5. F01-06、F01-07 中属于 WP07 部分的状态更新。

**非目标**：

- 不提取编译触发与编译失败副作用（WP04 主规格）、插件错误机制（WP05 主规格，共用诊断面引用）。
- 不提取资源选择与播放（WP15）、神秘礼物等业务消费者（WP64）、编辑器行为（WP73）。
- 不访问真实远端，不证明外部服务可用；不运行游戏或任何参考脚本；不修改 `reference/`。

## 2. 概念与术语

- **文件访问层**：目录遍历、存在性探测、读写包装与资源路径解析（含加密归档感知）。
- **HTTP 包装**：下载（GET）与提交（POST）的薄封装及其失败归一。
- **诊断面**：异常格式化、错误日志文件、调试日志文件、控制台输出与用户提示的集合。
- **失败归一**：包装层把多种失败条件合并为同一返回值（nil/空字符串），调用方无法从中区分失败原因。
- 影响域编号 Dxx 见 module-map；证据状态五档定义见总览第 7 节。

## 3. WP07-A：文件访问层

### 3.1 遍历与目录操作（`S/001_Technical/002_Files/001_FileTests.rb`，本轮核实）

- `Dir.get`（按过滤列举并排序）、`Dir.all`（递归整树）、`Dir.all_dirs`（递归目录）、`Dir.create`（逐级建目录）、`Dir.delete_all`（删除目录全部内容）。
- `safeGlob`：带重音路径兼容的 glob；`safeIsDirectory?`/`safeExists?` 为标记弃用的兼容包装（弃用警告机制归调试面）。

### 3.2 存在性与读写（本轮核实）

| 入口 | 成功 | 失败形式 | 证据 |
| --- | --- | --- | --- |
| `pbRgssExists?` | 返回是否存在（加密归档感知，经一字节探测） | 不适用（布尔） | 282–286 行 |
| `pbGetFileChar` | 返回文件首字节 | ENOENT/EINVAL/EACCES/EISDIR/RGSSError/MKXPError → **nil** | 315–333 行 |
| `pbGetFileString` | 返回文件全部内容 | 同上 → **nil** | 344–361 行 |
| `pbRgssOpen` | 打开文件（普通文件或归档读取转 StringInput） | 归一化路径后打开；失败行为未逐分支验证 | 292–311 行 |
| `pbTryString` | 文件可读且非空返回路径 | 否则 nil | 335–338 行 |

**失败归一**：读取包装层对"文件缺失"与"读取失败/权限/目录错误"均返回 nil——**调用方无法区分**（读取返回 nil ≠ 文件缺失；如 move2anim 的 `|| []` 只捕 nil 返回，不证明文件缺失也回退，WP03 第 3.3 节同例）。

### 3.3 资源路径解析（RTP 与扩展名回退）

- `RTP.exists?` / `getImagePath` / `getAudioPath` / `getPath`：按扩展名候选查找（图像 png/gif；音频 wav/ogg/mp3/midi/mid/wma）；找不到时 `getPath` 返回原输入。
- `pbResolveBitmap`（图像）/`pbResolveAudioSE`（音频）：找到返回真实路径，找不到返回 **nil**；`pbBitmapName` 找不到则返回原输入。
- `RTP.eachPath` 当前仅产出 `./`（MKXP 兼容遗留；`Game.rgssad` 存在时改由归档读取）。
- 保存目录：`System.data_directory`（OS 相关：Windows `%APPDATA%`、Linux `$HOME/.local/share`、macOS `$HOME/Library/Application Support`）。

### 3.4 写入面（本轮观察到的静态入口）

- 序列化保存（编译产物 .dat、PluginScripts.rxdata、MapInfos、动画映射等，WP04/WP05 引用）。
- 文件追加：`errorlog.txt`（异常日志，见 5.1）、`Data/debuglog.txt`（调试日志，仅 `$DEBUG && $INTERNAL`，见 5.2）。
- HTTP 下载落盘（4.1）：响应体写入指定文件。

## 4. WP07-B：HTTP 下载与提交

### 4.1 包装行为（`S/001_Technical/002_Files/003_HTTP_Utilities.rb`，本轮逐行阅读）

| 入口 | 行为 | 失败形式 |
| --- | --- | --- |
| `pbDownloadData(url, filename, authorization)` | GET（固定旧 Firefox UA、no-cache、可附 authorization）；状态 200 且有 filename 则写文件、无则返回 body | 异常 → `""`；状态非 200 → `""` |
| `pbPostData(url, postdata, filename)` | POST form-urlencoded（键值逐字节转义）；同上分文件/正文返回 | 异常 → `""`；状态非 200 → `""` |
| `pbDownloadToString` / `pbPostToString` | 薄包装返回数据 | 异常 → `""` |
| `pbDownloadToFile` / `pbPostToFile` | 薄包装写文件 | 异常被吞没（无返回值） |

限定：仅匹配 `http://`（正则 `^http://`，未覆盖 https）；无重试（depth 参数未使用）；**无错误传播**——调用方只看到空结果，无法区分网络失败、非 200、写入失败。外部服务可用性未验证；神秘礼物等业务消费者归 WP64。

## 5. WP07-C：诊断与错误反馈

### 5.1 异常与错误日志（`S/001_Technical/001_Debugging/003_Errors.rb`，本轮逐行阅读）

- 异常类：`Reset`（重启信号）、`EventScriptError`（携带地图/事件定位的消息）。
- `pbGetExceptionMessage`：Hangup → "脚本超时，游戏将重启"；ENOENT → "File X not found"；回溯中的脚本段映射名称。
- `pbPrintException`：格式化（版本、`Essentials::ERROR_TEXT`、异常类、消息、10 行回溯（内部版 25 行））→ 追加写入 `errorlog.txt` → 打印完整消息（0.5 秒内按住 Ctrl 可复制）。与插件错误的 `pluginErrorMsg` 同一模式（WP05 引用同一诊断面）。
- `pbCriticalCode`：关键段包装——`Reset`/`SystemExit` 原样抛出；其他异常打印；Hangup 额外抛 `Reset`（重启）。

### 5.2 调试日志与控制台（本轮核实）

- `PBDebug`（`001_PBDebug.rb`）：`logonerr` 包装异常记录；`log`/`log_header`/`log_message`/`log_ai`/`log_score_change` 累积日志，仅 `$DEBUG && $INTERNAL` 时写入 `Data/debuglog.txt`（AI 调试带 `[AI]` 标记）。
- `Console`（`002_DebugConsole.rb`）：调试模式输出窗口；`echo_h1/h2`（标题）、`echo_li`（进度）、`echo_error`/`echo_warn`（错误/警告）、`markup_style`（着色）；`Kernel#echo/echoln` 仅调试模式输出。
- 三层用户反馈：`print`（消息框，玩家可见）、控制台 echo（调试输出，开发者可见）、errorlog.txt/debuglog.txt（文件，事后可查）——不同受众与持久性，不能混为一谈。

## 6. WP07-D：失败层次与边界

| 层 | 失败形式 | 调用方可区分性 |
| --- | --- | --- |
| 文件读取包装 | nil（缺失/权限/目录错误同归） | 不可区分原因，只能按 nil 处理 |
| HTTP 包装 | `""` / nil（网络失败/非 200/写失败同归） | 不可区分原因；无重试 |
| 编译/内容错误 | 异常 + `FileLineData` 位置报告（WP04 主规格） | 可定位文件/节/键/行 |
| 插件错误 | 输出 + `Kernel.exit!`（WP05 主规格） | 进程终止，无恢复 |
| 未捕获异常 | `pbPrintException` → errorlog + 打印；Hangup → Reset 重启 | 进程级处理 |
| 调试日志 | 仅 debug+INTERNAL 写 debuglog.txt | 非用户反馈 |

边界：编译触发与失败副作用归 WP04；插件错误归 WP05；资源选择/播放归 WP15；神秘礼物下载归 WP64；编辑器诊断归 WP73。本包只定义通用 I/O 与诊断面，各业务的失败语义归相应领域包。

## 7. 默认行为与配置变体

- **基线默认**：读取失败归一 nil；HTTP 失败归一空结果；未捕获异常记录 errorlog 并打印；调试日志仅 debug+INTERNAL 启用。
- **支持但未默认启用**：`Essentials::ERROR_TEXT`（供第三方追加的错误头内容，默认为空）；内部版 25 行回溯（`$INTERNAL`）。
- **未验证组合**：HTTPS/代理/重试行为（无证据）；归档模式（Game.rgssad）下的读取分支（无材料）；外部服务可用性。
- 参考快照行为、官方版本预期、未来目标分开标记；本包只记录第一类。

## 8. 可复核性与静态场景

### 8.1 复核方式

| 事实 | 复核方式 |
| --- | --- |
| 文件遍历/读写/资源解析 | 阅读 `S/001_Technical/002_Files/001_FileTests.rb` |
| HTTP 包装 | 阅读 `S/001_Technical/002_Files/003_HTTP_Utilities.rb` |
| 异常与错误日志 | 阅读 `S/001_Technical/001_Debugging/003_Errors.rb` |
| 调试日志 | 阅读 `S/001_Technical/001_Debugging/001_PBDebug.rb` |
| 控制台输出 | 阅读 `S/001_Technical/001_Debugging/002_DebugConsole.rb` |
| 保存目录 | `001_FileTests.rb:248–256`（`System.data_directory`） |

### 8.2 静态推导场景（未运行，待运行验证）

| 场景 | 输入 | 推导预期 |
| --- | --- | --- |
| 读取缺失文件 | `pbGetFileString("Data/none.dat")` | 返回 nil（与读取失败同归，不区分） |
| 读取返回空值回退 | `load_data(...) || []` 形式 | 仅在返回 nil/false 时回退；文件缺失是否触发未验证（WP03 同例） |
| HTTP 非 200 | 下载返回状态 404 | 返回 `""`；有 filename 时不写文件 |
| HTTP 异常 | 网络不可达 | 返回 `""`（无错误传播、无重试） |
| 资源回退 | `RTP.getImagePath("x")` 无 png 有 gif | 返回 gif 路径；全无则返回原输入 |
| 未捕获异常 | 任意脚本异常 | 追加 errorlog.txt 并打印；Hangup 额外抛 Reset |
| 调试日志 | `$DEBUG && $INTERNAL` 为真/假 | 真：写 debuglog.txt；假：不落盘 |

## 9. 证据与来源（traceability）

- **本轮复核（2026-09-19）**：逐行阅读 `003_HTTP_Utilities.rb`（83 行）、`003_Errors.rb`（94 行）；阅读 `001_FileTests.rb` 关键段（1–120、250–370）；`001_PBDebug.rb` 前 60 行；`002_DebugConsole.rb` 前 70 行；RTP/资源解析与保存目录段。
- **继承同基线既有记录**：E03、E05、E08、E11（文件/资源/控制台抽查，本轮已扩展为分层清单）；E30（下载调用者，神秘礼物归 WP64）。
- 全部静态证据；**无运行确认**；未访问任何远端。

## 10. 未决问题

1. HTTPS/代理/重试与响应码细分类行为（无证据）。
2. 归档模式（Game.rgssad）下各读取分支（无材料）。
3. 写入失败（磁盘满/权限）在各写入面的表现（未运行）。
4. `pbRgssOpen` 的失败分支全集。
5. 外部服务可用性与业务消费者的失败语义（归 WP64 等）。

## 11. 状态与后续

- WP07 自身范围（第 1 节五项）已提取并自检，状态 **ReviewPending**，提交外部 review。
- **WP07 完成 ≠ F01-06/F01-07 完成**：各业务失败语义需领域包闭合（编译 WP04、插件 WP05、资源 WP15、礼物 WP64）；Feature Matrix 按聚合规则分别显示。
- 后续包引用本文的失败层次时，不得把包装函数名或路径约定当作未来框架的 I/O API；发现与本文冲突的新证据时，先修订本文并通知受影响包。
