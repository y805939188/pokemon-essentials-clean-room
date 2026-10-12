# 静态数据校验计划

目的：核对 WP47-A 的七组调用/复制排除名单及 WP47-B 的号令/安可名单，区分恒定项和世代追加项；辅助语义审查，不执行游戏逻辑。

命令：`python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M07/check-data.py`。

工具版本已读取：Python 3.14.0。输入为 R 固定参考的两个 MoveEffects 文本及 B 正式两份数据附表；不加载 Ruby、不安装软件、不接触存档。只从明确名单区间提取数据身份，忽略注释，逐列比对常/世代追加集合。

预期输出：九组常项/追加项数量、缺失/额外/世代差异与整体结论。只能称 TOOL_VALIDATION，不证明调用候选或运行行为正确。脚本只向标准输出输出 JSON；运行收据与校验输出仅写本 M07 目录。

## 交付结构校验

目的：检查七个要求产物存在、JSON可解析、必备字段及状态/证据枚举、能力ID及引用完整、固定身份和源/正式锚点路径存在。命令：`python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M07/validate-outputs.py`。同为 Python 3.14.0，只读本目录和锚点目标；标准输出为检查计数，收据另写本目录。此项只证明产物结构，不证明语义、游戏运行或全覆盖。
