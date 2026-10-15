# R7-U04 作者候选交付

状态：**CANDIDATE_READY_NOT_REVIEWED**。作者只提交 GR7-M03-001、GR7-M03-002 的最小候选；未自签独立 review、正式接受或关闭。

## 固定输入、环境与恢复

云端执行环境已由等待工具实际返回 ready，仓库为 `/workspace/pokemon-essentials-clean-room`。实际作者 task/context ID 未被平台暴露，保持 NOT_EXPOSED_UNVERIFIED；父来源线程 ID 只作派发来源，见 execution-context.json。请求 gpt-6.1-sol/xhigh/default 普速、禁 Fast；真实 model/effort/tier/speed 均无有效回参，UNVERIFIED。

实际获取输入分支 `codex/remediation-seventh-20261015-cloud` 后 FETCH_HEAD 完整等于 `4bd152023b4bcb3dd5a3654deffe75aeebc40f10`，已完整读取其中首波派发。完整两项七组合同固定 `f622356f3beb9e84ea8cff9db07c7fb382565d3f`；恢复工具/清单固定 `658488c81f1f3181a488298ab27850c8af951d73`。根 AGENTS.md 已读，固定 B 与派发提交均未包含 `.agents/skills`，不声称使用不存在的技能。

工具及清单先全文读取，再在本容器执行默认完整批次恢复；未假定整合者的共享目录。真实命令：

```text
python3 /workspace/r7-bootstrap/R7-U04/tools/restore_container_context.py --plan-directory /workspace/r7-bootstrap/R7-U04/recovery/batches --batch R7-U04 --destination /workspace/r7-context/R7-U04
```

退出 0，BOUNDED_RESTORE_BYTES_VERIFIED，29 文件、5,789,300 字节；编码大小/blob、解码及固定输入 bytes/SHA256/blob 全部匹配。作者随后重新计算29文件身份，并核对合同12处原始字节切片/JSON pointer 的 canonical SHA。真实 HTTP 及身份回执见 recovery-receipt.json，预期定位见 input-identities.json。这是有界文件快照，不是完整参考 Git checkout，也不是整树、宿主或语义 PASS。固定 R 文件逐一恢复，参考整树身份未由本次独立重新核验。

固定 B：`e646432c644dec04d306842cc5a559a29c718fbc`；根 tree `84f79ec6e772aacbf3a464fde68cdc5a280e2950`，正式子树 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。成果分支创建前本地/远端同名均不存在，初始工作区干净、唯一工作树在 B；普通创建 `codex/r7-u04-author-20261015-pilot1`，未 reset、force 或操作整合者分支。

## 精确贡献与保留

- GR7-M03-001：只修改 WP41 §5.1 野生替补成功措辞，说明决定3写入后同次后席提示/选择/绑定/顺序/派出/非致死入场可继续；以 WP42 阶段21调用正常返回、阶段22再消费正决定解释退出。新增 SW-30～SW-35，包含完整2v1、单待补席、首席Yes、入口已决定、必选界面取消与显示/选择/入场异常前缀。位置恢复及HP各自提交，不保证异常回滚或最终3。未采用原作者更宽的危害致死终局扩展。
- GR7-M03-002：只修 WP39 §5 辅助查询括注与有界例外，查询为存活偏好，首个既存濒死对象可经回退返回。新增 BC-26～BC-31：[3,5,1] 原始结果3、首3存活仍3、首3不存在得5；己侧0直接投球解析恢复目标1，显式对侧5直接使用5；无活同伴失败只保留 WP38 既有合同，不重开必修。无普通菜单必选错或捕获必失败的结论。
- 两个正文场景计数及目录标题随新增条目同步。三个文件均是固定 B 的完整字节镜像起点；镜像内其它条款与所有旧目录行原样保留。WP38、WP42、WP47-A 只读不改；默认/false 的换人消息、梦话、变身者与通用招式目标族不扩大为 true 查询合同。

精确基线/新 bytes、SHA256、Git blob 及行区间见 artifact-manifest.json；各项读写集、原非作者缩窄裁决、每向量前提/预期/阶段、取消/失败/部分提交和未满足依赖见 per-id.json。clause-contributions.patch 是零上下文审计差异，供 R7-I 按条款串行整合，不能以完整镜像覆盖其它批次贡献。无 conditional/optional/policy 路径采用。

## 验证与证据资格

已全文读取完整派发、两项七组、R7-M01/M02 已接收反证和根记录；源/消费者只按 reading-ledger.json 的精确连续范围计读。WP39/WP41/共享测试目录全文读取并保留旧向量；WP38 §2、WP42决定/阶段/诊断边界及WP47-A目标构造按具名范围读取，不假称它们全文语义核验。历史没有旧 PASS 被采用，旧向量与关闭边界保留；已恢复但未读的其它内容不被改标为 limit。

作者 validate.py 只检查输入/候选字节身份、范围、旧条款与旧向量保留、ID/计数、JSON绑定及交付完整性；validation.json 与 public-command-log.jsonl 提供真实命令、退出及可发布输出。该工具不实现战斗行为、不执行恢复的参考程序；哈希及退出0均不提供独立语义 PASS。早期侦察/读取命令仅保留平台 tool I/O，未捏造其缺失的独立 UTC/stdout/stderr 文件；session-observations.json 只逐项注明对应真实输出与资格。未推送原私有模型流或参考源表达式。

首次暂存检查中，审计补丁的标准空白上下文行被新增文件空白检查标为 exit2；已将审计件改为零上下文差异，重做暂存检查 exit0。该失败及后续实际结果均保留在公共命令日志，不把后继成功改写成首次成功。

SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION 分层；新增12个静态目录向量及 SW-35 的独立故障子例，全部领域执行 NOT_EXECUTED。作者新增参考运行、独立行为模型、真实UI/宿主、Demo、native媒体、真实存档回放均0。L01–L14完整保留；R7整体先前局部Ruby运行不归本任务；27项/13批分母、7 optional/2额外导航facet/1 no-required/2 policy不采用，以及旧56/92关闭边界均不变。

## 传输与尚待接收

普通提交只包含 `candidates/R7-U04/`；普通 push 只去 `codex/r7-u04-author-20261015-pilot1`。不修改正式文件、公共台账、旧证据、参考、main、tag或整合分支。提交身份由包外实际 Git commit/tree 绑定，避免自引用哈希；manifest 自身身份由实际 Git tree 绑定。

候选载荷已普通提交并推送：commit `2b9941a3d76f4fccc07cd50cc63414e9ed3f31df`，tree `4bdcf08628c880a6d4f922d57e7efe470944fb82`，直接父提交为固定 B。随后对该 commit 的全部15个候选文件、261,894字节通过不可变远端 HTTP URL 实际下载；每个完整响应体与对应 Git blob 逐字节相等，下载前后 ls-remote 均指向该完整 commit。真实回执 remote-readback-payload.json；可复现工具 remote_readback.py。该传输结果不授语义或独立 review 资格。

本次再以普通证据追加提交携带上述回读回执、回读工具及更新后的清单/日志；三个正文/目录镜像与已回读载荷完全一致。追加提交的最终完整 commit/tree 在包外交付，并对最终远端全候选字节再次回读。最终回读通过平台 tool I/O 回传，不把含自身 commit 身份的回执无限递归提交进同一 commit。所有需交付的新建候选文件及证据均在成果分支内，bootstrap和输入快照不进入候选。

候选完成后交 R7-I 校验差异与身份、冻结 candidate-input.json，再由不同真实 context 的独立 ultra 审者复核。本作者未创建 reviewer。候选 PASS、实际整合后的新 R7-IR PASS、ACCEPTED、CLOSED 四门均未达到。无作者排程前置批次不表示消费者、历史回归或接收依赖已经满足；依赖未满足不提前关闭。
