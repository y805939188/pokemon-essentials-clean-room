# 5.3 进化整数参数正式规格候选：独立差异复审 r1

**结论：PASS；未发现 P1–P3 实质问题。** 五份正式文件忠实纳入已独立复核的净化调查，并保留发行 v21.1 与参考 R 的差异。此结论只针对本地固定候选；它尚未被协调者正式接收，也不代表运行或框架验收。

## 固定对象和范围

- 工作树：`/Users/dingshinn/Desktop/pokemon-framework/.worktrees/reference-integer-spec-20261025`，分支 `codex/spec-integer-evolution-20261025`，HEAD **`6af2f193a5852e12ee6e17152d382efdbccdb40e`**，检查时 clean。基线 `dae67763071cfe135b99f90639d71425410b1ed3`；内容提交 `f9b649b76e156f8c04109c074e9e238892d6588e`，后续 `6af2f19` 仅补检查资格记录及说明。未修改该固定工作树。
- 基线正式树 `93dc967b4cdb653359afc123d3b8b318d6475fdd`，候选正式树 `12332a44bbd5de91af3a7393490ef334ee4d4891`。`BASELINE.json` 的 131 份正式文件路径、blob 和 SHA-256 与实际基线一致。相对基线仅五份正式文件修改，合计 **128 增、4 删**；其它 126 份未变。额外 11 个新增文件均位于 `review/step5-3-evolution-integer-20261025/`，为支持材料与逐字节复制的净化输入；旧正式导航、历史封印、台账、规划未改。
- 本轮先核工作区与 reference 的 `AGENTS.md`、`PROJECT-GUIDE.md` 及交接状态；读五文件完整相关合同和基线差异、支持材料、前序独立报告及按原字节复制的输入。**此次没有再读取原版 Ruby、框架 TS 或输入快照中的 TS；未运行 Ruby、原版、GUI、NW.js、框架或项目测试。** 前序调查独立报告为原调查 `independent-review-r1/REPORT.zh.md`，SHA-256 `bab8e525b8698e623c1e57527bd210dce2474bcd8f22a779d1c98c2531c63a5d`；本轮核对其复制件及六份候选输入逐字节一致。

## 内容复核

| 改动 | 独立结论 |
| --- | --- |
| WP31 §3.9 与 §3.8 | **PASS。** 表中恰好是固定名单的 30 项，逐项逻辑 Integer→PBS `u`，无 `i`/`v` 例外。`-1/0/1/+1/01/空/缺/1.0/1e2/1x`、内侧空文本、前导零和大整数的接受域及失败阶段与净化证据一致。24 项等级阈值及其余参数用途、无附加 level/count/location/region 域门、EventAfterDamageTaken 的事件编号用途均准确。§3.8 的单/复数合并已限定参考 R。 |
| WP03 §5.1、§5.2 | **PASS。** 新文字把 30 项逻辑整数映射到 `u`，不改通用 `i/u/v` 定义；必需参数行按版本区分 R 的条目门、v21.1 基础终检失败与显式形态放过缺值。没有把 R 的规则回套到发行 tag。 |
| WP04 §4.5 | **PASS。** 行预处理、CSV 尾缺值与内侧空文本、初次文本消费、R 条目缺参门、基础/形态全表整数转换、当前条目登记与本表保存的顺序分层清楚。v21.1 单数不消费、R 单/复数均消费；显式形态缺参的发行缺陷有前提且未升级为未来兼容要求。既有合并段也限定 R。 |
| BEINT 与 S53-INT | **PASS。** `BEINT-L01–L12` 将核心十边界、`-0/00`、四个大整数映射到封存的 30×6×16＝2880 条静态向量；`BEINT-D01–D05/V01–V03` 和 `S53-INT-01–07` 补足领域、版本、阶段对照。两目录新增 ID 唯一，交叉链接与净化 CSV 目标存在。向量和正文均标 **SOURCE_STATIC／DERIVED_VECTOR、NOT_EXECUTED**，没有声称原版运行、保存 I/O、CI 或框架测试通过。 |
| 版本和政策边界 | **PASS。** 正文并列发行 `ea7b5d56d2436591160983c4e641a2ceee2d875a` 与参考 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；未为实施者选定目标版本。JS 安全整数只是未来表示/兼容政策，不被写成参考拒绝上限；无资源耗尽保证。 |

## 检查资格与剩余事项

`review/step5-3-evolution-integer-20261025/CHECK-QUALIFICATION.json` 的失败和修正资格均经独立重核：普通全包 `git diff --check` 在基线至 `f9b649b` 的新增封存 CSV 上 **exit 2**，恰有 **2912** 条 CRLF 行尾诊断，仅涉及 `BOUNDARY-VECTORS.csv` 2881 行和 `METHOD-BINDINGS.csv` 31 行；不能称默认全包通过。只检查五份正式文件为 **exit 0**。临时使用 `core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol` 的全包检查为 **exit 0**，保留通常三项空白检查，只允许数据原有的 CRLF 行尾；CSV 字节及持久配置未变。`f9b649b..6af2f19` 不改正式文件或封存输入，且明确保留初次失败、没有 amend 历史。此为文档运输格式资格，不是行为执行证据。

仍需协调者按既定流程接收或整改候选，并在实际整合提交上核身份及资格；旧根导航的第七轮文字未由此候选改写。本报告不签 `ACCEPTED`、不更新 reference `main` 或 `.handoff/STATUS.md`，没有 push/merge。用户请求独立 `gpt-6-sol/ultra`、Standard/nonFast；执行环境未回显有效模型、推理档位或服务档位，均记 **UNVERIFIED**。
