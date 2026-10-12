# M10 产物结构校验计划

目的：核对本目录 JSON 可解析、必需字段/枚举/ID 引用有效、固定源码与正式文件锚点路径存在，以及正式文件无本次改动。

命令：`python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M10/validate_review.py`。

版本：共享 baseline 为 Python 3.14.0；校验收据同时记录本次解释器版本与 UTC 起止时间。

输入：本目录的七类产物及额外 inventory/search JSON；参考仅检查锚点文件是否存在，正式路径也只读检查。不会执行或导入参考 Ruby，不加载存档、动画或消息二进制。

输出：结构检查计数及 `PASS_TOOL_VALIDATION_ONLY`；失败明确异常。属于 TOOL_VALIDATION，不是任何行为、游戏、宿主或 Demo 测试。

副作用：仅在本 M10 目录写 `validation-result.json` 并向 `execution.json` 登记此次工具校验。`git diff --exit-code` 为只读检查；不会修改仓库索引或参考。
