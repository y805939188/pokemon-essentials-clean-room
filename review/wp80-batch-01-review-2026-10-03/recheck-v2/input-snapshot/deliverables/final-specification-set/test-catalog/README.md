# 静态测试目录索引（WP80 净化规格集）

本目录按「分类/包」组织静态推导场景条目。每条记录：**ID、输入／前提、推导预期**——全部为静态推导，**不是已执行测试**；素材、宿主输出与运行表现按 `../scope-statement.md` 保留。

## 目录

| 文件 | 覆盖 | 条目 | 对应净化正文 |
| --- | --- | --- | --- |
| [engine-overworld-wp16.md](engine-overworld-wp16.md) | 世界绘制与视觉过渡＋战前过渡（批次 1，v2 修正后） | WR01–WR16、BT01–BT16 | `engine-overworld/wp16-world-rendering-and-visual-transitions.md`、`engine-overworld/wp16-pre-battle-transitions.md` |

## 使用约定

- 条目 ID 在净化正文中引用（正文 §示例场景 指向本目录）。
- 预期列为静态推导：实现方据此设计可执行测试时，环境前提（素材存在性、宿主行为）须单独验证。
- 目录条目与正文同步维护；新增/修订条目需在对应批次检查记录中登记。
