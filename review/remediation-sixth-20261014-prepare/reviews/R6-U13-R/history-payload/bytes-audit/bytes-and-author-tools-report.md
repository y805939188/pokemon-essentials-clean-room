# R6-U13-R 字节、历史身份与作者脚本审计

## 结论与审读边界

冻结候选 commit `00b45de642f07cee9953e42f04cce9c35d77346f`、tree `6708f580d5a02f874a1a24a95d7c0649b10c393b` 的字节/路径/身份核验通过；作者工具的成功输出不能扩大成完整语义、历史回归或正确子例保存证明。作者 R5 原路径不存在的证据说明与固定对象相矛盾，故本辅助的**作者证据审计为 FAIL，必须修正后复核**。父审读另已独立确认 S001 原正常 b/c 控制丢失，候选总体 FAIL。本辅助未另判八个修订 ID 的语义，未签候选 PASS，也未转移历史结论。

只写本 `bytes-audit/` 目录；未切分支、提交、修改候选/正式稿/参考源，未运行、导入任何作者脚本，也未运行参考、行为模型、serializer 或宿主。actual model、effort、tier、speed、UUID 全部 **UNVERIFIED**；未检查认证、CLI 模型或运行配置。一次辅助文本协查 spawn 尝试因 thread limit 返回失败，没有子 agent 启动；此事不能证明任何配置资格。

## 冻结对象与 prepare 基线

- 23 个候选载荷逐项核查 fixed commit 的 exact path、mode、type、bytes、SHA256、Git blob，并比对工作区：8 mirror + 15 evidence，全部 `100644 blob`、工作区为常规文件、逐字节相等。逐项收据：`candidate-payload-identities.json`。
- `candidate-manifest.json` 八项 candidate 身份均匹配冻结镜像。prepare `469a268b92daed7b4d28d7fd0da75520cbb7228f` 的八份作者镜像与同提交八份正式文件均等于 fixed main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6` 原件；八份 candidate 镜像均有变化，candidate commit 中正式路径仍等于 fixed main。prepare 身份不能记为 candidate commit 身份。见 `baseline-bindings.json`。
- 独立重建 37 条 changed-spans 与作者 JSON 全等。`git diff --check PREP CANDIDATE` 成功，冻结提交相对 prepare 的变化仅为八份镜像及候选 evidence。见 `independent-mechanical-validation.json`。
- 六份指定 JSON、四份 Python 与 AGENTS 已完整呈现并阅读，共 18 段；各文件完整行域、bytes/SHA/blob 与段 SHA 见 `reviewer-segment-reading-ledger.json` 和 `reviewer-reading-ledger.md`。初读 UTC 未单独留回显，账本明确 `NOT_RECONSTRUCTED`，没有伪造回执。

## 输入与作者阅读账本

独立核对 118 项声明：prompt/contract/AGENTS 三项、28 source + 8 formal、72 bidirectional contract payload、7 counter packets，bytes/SHA/blob/所声明行数全部相符。固定 prompt 的首 JSON 区块与固定 contract 原字节相同（仅排除 contract 最后 LF）；72 条作者 payload 检查从 prepare 合同逐项重建全等。见 `input-and-contract-identities.json`。

作者 reading-ledger 的 79 条 commit/path/git-entry、整文件身份、合法行域、returned_bytes、stdout_content_sha256 全部可从固定原件重算，required source/formal/counter 的区间覆盖没有 gap。见 `author-reading-ledger-mechanical-audit.json`。这是账本与文件一致性的证明；不能据此证明下游工具显示未截断，或模型确实读懂了内容。prompt 的人工区间与“fully read”文字不是有命令/UTC回执的程序断言。

environment-snapshot 的 prepare HEAD/tree、fixed main formal subtree、fixed R tree 全部独立核对一致。它记录作者当时 prepare 环境，不能用其中 HEAD 替换当前 candidate 冻结身份；请求配置也不构成实际配置回显。

## 全部历史对象与指针

最终已从本地固定对象核验完整原件，未使用候选复制正文代替历史原件：

|核验对象|独立结果|
|---|---|
|prepare 中历史导航输入|3,283,387 bytes，SHA256 `789fe2806041016c31fb1d7907eff663dc803bc4c21bebb018ad0f1c3eccf406`，blob `534ed3e48528156bccc7a5ecf3422062fda83521`，全部匹配|
|c0ff fourth/third/legacy 三份原件|exact commit/path/mode/type、bytes/SHA/blob 全部匹配；legacy 为 28,187,068 bytes，SHA256 `6c9193d4b700b55f13326882f6e7ef53fd0e01cc1a2940798aa5192b8a690129`，blob `62e1b5e89aa612f8796ec951000578d188286ff7`|
|74 条 affected-path navigation|从 prepare 输入精确重建；每条 frozen_record 与 qualified_scope_binding JSON 指针可解，record/scope canonical SHA、scope_keys 和归属元组全部匹配|
|14 条 R3/R4 scope|固定指针原范围与 candidate projected scope 全等|
|9 条 R2 owner contribution|legacy contributions 231–239 的原资格范围全等；B12 controls/84 的范围也全等|
|d815 B13 controls|原文件 465,872 bytes / SHA256 `d060c52f545cdefec9d0e5d476668231003db72ae8d7459fe45256974537ae31` / blob `75414a45944ae4823fd2d23be231890309c2c489` 匹配；八条 assigned scope 均与有界投影及 scope_rule 全等|
|R5 两枚 exact blob、三个 findings|两个 blob 身份、finding ID/指针、八字段投影，以及 prepare 内 R5-U04 合同声明的原 f49d commit/path 全部匹配|

74 条导航的 owner 核对保留原 schema 区别：25 条 legacy `/controls` 原件使用 `primary_owner`，49 条其它记录使用 `batch_owner`；导航的 required tuple 统一称 batch_owner。核对的是显式归一化后的原 owner，未把原控制对象缺少 batch_owner 字段误判成归属丢失。

B13 第一控制是有界投影：删除 extensions、extension_decisions、minimum_revision、determinate_recheck 后，再加入完整的受影响路径 extensions；不是原控制对象逐字段全量复制。投影边界原样保留，不能因此转签 B13 全部历史质量。

最终完整收据：`historical-payload-identity-audit.json`；汇总：`historical-final-summary.json`。canonical hash 使用 UTF-8、JSON keys sorted、compact separators、无结尾 LF。

恢复前本地 c0ff commit/原 blob 与两枚 R5 blob 不可用，原 direct Git 失败和首轮 `historical_errors=77` 保存于 `object-recovery-transition.json`。独立 GitHub exact-ref/path 调用先验证三枚 c0ff API sha；随后两份小原件 blob 身份和 14 scope 核验成功，legacy fetch_blob 曾返回 Transport closed。这段失败/部分成功收据保留在 `c0ff-remote-payload-receipt.json`，没有用最终成功覆盖。root 后续恢复对象 pack，本辅助再用只读 Git 完成全部原件及指针检查；**legacy BODY_PENDING 已解除**。

## 作者脚本实际能力及缺口

|脚本及位置|实际覆盖|不能据此证明的范围|
|---|---|---|
|verify_candidate.py:33–75|从作者 ledger 区间计算 required source/formal/counter 覆盖；固定 prompt 身份、嵌入 contract、AGENTS 身份|没有核验 ledger 的片段 hash/returned_bytes/git-entry，也没有确认下游未截断或语义阅读；prompt 初读区间及 attestation 是直接写入|
|verify_candidate.py:77–111|72 固定载荷身份、八镜像 baseline/new 身份与 changed spans；限定作者分支；候选镜像+任意 evidence 前缀 allowlist|evidence 不是有限 15 文件 allowlist；身份相符不证明 clause/locator 行范围的行为语义。其 diff-check 是调用时工作树检查；本审读另核了固定 PREP→candidate diff|
|verify_candidate.py:120–137|未获例外的原目录行文本相等；预设目录数量|先转字典再 `len(newrows)==len(set(newrows))`，字典键天然唯一，不能发现重复行；SF 字典同样不能检测重复。当前独立 raw rows 与 distinct IDs 均为 QC49/WS36/PA32/RC29/SF40，确实没有重复，但作者逻辑没有证明此事|
|verify_candidate.py:125–137|允许 W13、P14/P15/P16、W18、SF01/SF30 整行变化|例外行内部没有逐子例保存断言。尤其 SF30 整行排除后，父审读指出的原正确 b/c 控制丢失不会触发该工具。本文核验这一程序盲点，不另作 S001 语义签字|
|verify_candidate.py:139–148|WP40 删除指定补句后整体相等；两次整数除法和一次比较|h24 两个 factor 字段直接写常量 30，没有从参考规则推算；不能把它们当运行模型或完整独立算术验证|
|bind_history.py:17–68|复制有限导航，读取三历史 JSON、指定 scope、B13 有界投影、两 R5 blob 的三个 finding 投影|没有独立核 nav 引用的每个 pointer/record_sha/owner tuple，也没有把声明身份与输入合同逐项比较；本审读另行完成这些检查|
|bind_history.py:39,67,69–89|写 current_check、new_author_regression_checks 等说明并明确不转移历史 verdict|这些检查文字及 COMPLETE 状态为直接写入，不执行 WP40/suffix 精确保留断言，也不验证十条行为/消费者结论。其范围不能超出其它审读另有证据的检查|
|read_unit.py:19–35|读取固定对象、计算全文及段摘要、输出段正文并追加 ledger|ledger 在 print 前写入，不能证明下游成功完整显示或实际阅读；未校验 start/end 正常域，未知 kind 会落到 prepare。当前 79 条的域与摘要本审读另行核正|
|edit_candidate.py:4–15,73–75,128–129|路径限定 candidate mirror；多数锚文本/行前缀唯一；八文件硬编码编辑|没有整份 baseline hash gate、事务回滚或语义保存验证；中途失败可留下部分编辑、再次运行会失败。它是作者修改工具，不是独立验收工具|

四脚本实际运行入口包含写证据或写镜像操作，所以本审读只静态阅读全文，没有执行它们。独立机械验证为 reviewer-owned `independent_bytes_audit.py`，其命令/exit/输出摘要见 `audit-command-receipts.json`。工具源码静读也不能证明候选执行历史真实性。

## R5 获取说明的可证更正

bind_history.py:65 和三个 R5 输出写“Original contract path was not present at declared f49d object”。独立本地固定对象和 GitHub exact f49d ref/path 均证明两路径存在，返回 blob 正是 `bbdee0813200953d50abf647b73341466d5559c9` 与 `7b21312f9f3512bfdd57e21a17cfb83096074050`；bytes/SHA 也全部相符。原声明出处是 prepare 固定 `review/remediation-fifth-20261013-prepare/contracts/R5-U04/contract.json` 的 input identities，详细 JSON 指针留在历史收据。

**此项是验收门必须修正，不是建议。**必须把作者获取说明限定为“当时本地对象不可用，改以 exact blob 恢复”，不能写成不可变 commit 中原路径不存在；复核作者输出的三个 retrieval_note 以及 bind_history.py:65 后才能解除本证据阻断。证据：`r5-f49d-remote-path-receipt.json`。此更正不否定两原件恢复后的字节身份或三个 scope 投影。

## 剩余边界

本辅助没有剩余对象/字节可获取性 blocker，未新增或复制任何 28MB legacy 正文缓存。剩余验收阻断是作者 R5 获取说明必须修正，以及父审读独立判定的 S001 正常控制保存失败。所有历史质量与新行为结论不因本身份核验而转签；实际运行配置资格仍全 UNVERIFIED。
