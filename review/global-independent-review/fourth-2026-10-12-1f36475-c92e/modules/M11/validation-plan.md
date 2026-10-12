# M11 只读数据核验预案

目的：检查三个正式附表与固定参考字面数据之间的转写关系，以及附表内数量、占位与常数乘积。该核验是 TOOL_VALIDATION，不是行为测试或参考游戏执行。

命令：`python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M11/validate-data.py`。共享基线提供 Python 3.14.0；实际脚本同时记录自身解释器版本与 UTC 时间。

输入：参考 R 的 SlotMachine、VoltorbFlip、Mining 三个脚本文本；正式 B 的 slot-reels、voltorb-layouts、mining-data 三个 Markdown 附表；物品 PBS 文本。只按字面解析数组/表格，不加载 Ruby、不调用随机数、不创建布局、不解释事件。

预期输出：有序转轮 66 格及频次；Voltorb 75 行的原始五参数、补足数与乘积；Mining 61 候选、13 铁形状的身份/权重/尺寸/掩码/占位数，以及 48 身份与口袋的核验结果。输出只含摘要、行号和不一致清单，不保存参考源代码。

副作用：只生成本 M11 目录内 `data-validation.json`；不写参考、正式规格、真实存档或全局状态。宿主、媒体、行为、概率分布和动态生成仍未执行。

收尾行政核验：使用 `python3` 内联脚本检查七个必需产物可读、JSON字段/证据枚举、ID引用、源与正式锚点路径存在，以及样本计数。结果只写本目录 `artifact-validation.json` 并追加 `execution.json` 的 TOOL_VALIDATION 记录。该步骤仅验证产物结构，不验证行为结论、运行能力或完整覆盖。
