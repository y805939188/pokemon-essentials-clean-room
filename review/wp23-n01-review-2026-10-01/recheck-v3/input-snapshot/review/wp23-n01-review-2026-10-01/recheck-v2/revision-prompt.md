# N01 v3 最小收尾修订

在 `/Users/dingshinn/Desktop/pokemon-framework-reference` 工作。读本目录 report、findings、input-manifest、current-summary-checks。原 WP23-N01-R01／C01 仍 OPEN，但不再重做已正确的外层成员门／Select／不回滚／直接调用合同。

## 1. 固定预检

复测本轮 1120 个输入与对应快照、5 个外部输入和 reviewer 原件索引。reference 维持 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 且 Git 清洁。WP23 本轮被审 v2 为 `cda848c3172f63d213a64674d7d39662e3c332018e6bb414bda54450a4ad655b`／47,455；冻结 v1／v2 材料和 reviewer 原件不回写。

## 2. R01 只剩一句操作表文字

主稿 §8.1 第 134 行不要再写“确认中选 Yes 均继续选人”。改为：

- BACK 的 Continue Box operations?：Yes 继续，No／取消确认退出。
- Close Box 的 Exit from the Box?：Yes 退出，No／取消确认继续。
- 退出才返回 nil。

可核对并采用 `proposed-confirmation-fix.diff`，该建议未应用。只改该句与必要的 N01 v3 状态／历史说明，不重写已经正确的三层正文、W34、十条对照或其它 WP23 规则。新回应纠正 v2 回应中重复的“均继续”表述；旧 v2 回应留史。

## 3. C01 必须在最后测量

不要复用 v1 的 `c406e644…`／`bb766c24…`，也不要把本次报告中的 v2 值当成下一稿固定目标。

按此顺序完成：

1. 主稿与 WP32 身份行定稿。
2. wp23-fixed、wp32-fixed、self-checks、boundary-checks 和必要 N01 当前状态同步完毕；此后先停止改动它们。
3. 从磁盘重新测量最终 self-checks／boundary-checks 的完整 SHA-256 和字节，更新当前活动摘要 §3 的两条引用。
4. 测量摘要最终身份，传播至当前 TSV／manifest，登记新材料。
5. **最后执行只读 `check-summary-final.py`**。先读该脚本确认只检查两条当前引用；结果必须 all_match=true、退出码 0。若之后任何上游 JSON 再变，重新测量并重复传播。

当前活动摘要两条引用保留“当前”语义时，必须匹配最终磁盘字节。不得仅将测量过程写为 pass，不核对最终状态。

## 4. 可写范围与交付

范围继承上一轮 N01 有限修订白名单：WP23 仅上述一句及状态／历史；WP32 仅必要 WP23 身份行；矩阵仅 N01 待审版本；当前 fixed／self／boundary／活动摘要与 N01 观察的必要状态和身份传播；manifest／主 TSV。

新建 `review/wp23-n01-delivery-2026-10-01/revision-v3/` 放回应、最终检查、固定身份和差异／绑定。所有 v1／v2 回应、checks、差异与绑定保持历史不动。新回应从该目录链接本轮 reviewer 的相对路径为 `../../wp23-n01-review-2026-10-01/recheck-v2/…`，不要多退一级。

差异相对**本轮 recheck-v2/input-snapshot**生成，精确重建目标。全量当前登记核对之后，再检查两条摘要引用；两层都成立。最终 manifest／TSV 检查不要被登记进它们自己从而制造目标身份循环；如有阶段，明确阶段和最后一段。

仅用三条最小验收即可：

- 两种确认的 Yes／No 行为在操作表、正文和新回应中一致。
- self／boundary 最终磁盘身份与摘要引用一致，摘要最终身份与登记一致。
- 其它行为、46 个 W 场景及所有冻结材料未改，变更在白名单内。

N01 仍为 REVISED_PENDING_REVIEW（v3），备妥材料后停止送定点复审；不自批关闭、不进入 GR 或其它包。既有已关闭编号和其它批准范围保持。

只做静态规格与自有文本／哈希／JSON／差异检查；不运行参考代码／表达式、游戏、生成器、解释器、编译／转换、插件、网络或真实输入；不实现框架、不创建任务／Agent、不发其它会话消息、不提交／推送。
