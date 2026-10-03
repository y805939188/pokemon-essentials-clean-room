# WP02 附表重新生成与一致性检查记录（2026-09-19）

本轮按 wp02-recheck-2026-09-19 第 7 节要求，在参考目录之外的临时输出目录重跑自有取证/生成流程并核对结果。参考源码全程只读，未运行游戏/编译器/Ruby 脚本，未执行任意源码表达式（求值器为显式有限形式解析）。

## 1. 输入基线

- 设置文件：`reference/pokemon-essentials/Data/Scripts/001_Settings.rb`、`002_BattleSettings.rb`（commit `8c5911e4`）
- 设施名单：`reference/pokemon-essentials/PBS/battle_facility_lists.txt`
- 生成/复核脚本（本轮修订后）：`analysis/inventory/wp02_settings_common.py`、`wp02_settings_inventory.py`、`wp02_build_appendix.py`
- 工作目录：`/Users/dingshinn/Desktop/pokemon-framework-reference/analysis/inventory/`
- 临时输出目录：`analysis/inventory/out/`（在 reference/ 之外）

## 2. 执行的命令与结果

| # | 命令（cwd = analysis/inventory） | 结果 |
| --- | --- | --- |
| 1 | `mkdir -p out && python wp02_build_appendix.py out/wp02-settings-inventory-appendix.md` | 写出 236 行；counts: 001=88、002=30、gen=47、setting-derived=1、methods=3、meta=3；unevaluated=无（全部求值）；facility refs=10、candidates=12、unreferenced=[cup_fancy_pkmn.txt, cup_fancy_trainers.txt] |
| 2 | `python wp02_settings_inventory.py` | 控制台统计与生成器一致（118 常量、47 世代派生、阈值分组 12 组、3 方法型、3 元信息、无未求值） |
| 3 | `grep -n "APPLY_HAPPINESS_SOFT_CAP\|SCALED_EXP_FORMULA\|VERSION\|ERROR_TEXT" out/…` | 五个关键值正确：APPLY_HAPPINESS_SOFT_CAP=false（派生列保留 =AFFECTION_EFFECTS）；SCALED_EXP_FORMULA=true；VERSION="21.1"；ERROR_TEXT=""；MKXPZ_VERSION="2.4.2/c9378cf" |
| 4 | awk 校验第 3、4 表（逐定义清单）每行竖线数 | 0 异常（全部为 5 列）；无未转义裸竖线 |
| 5 | `diff out/wp02-settings-inventory-appendix.md ../../specs/kernel/wp02-settings-inventory-appendix.md`（覆盖前） | 60 行差异，均为本轮预期修订（生成路径说明、5 个关键值、附表 7.5 设施集合重写等） |
| 6 | `cp out/… ../../specs/kernel/wp02-settings-inventory-appendix.md && diff out/… ../../specs/kernel/…` | diff exit 0：重新生成结果与最终交付附表**完全一致** |

## 3. 核对项汇总

| 核对项 | 结果 |
| --- | --- |
| 118 唯一常量、3 方法型、3 元信息集合保持 | 通过 |
| 5 个已指出值（F1 表） | 通过（见命令 3） |
| 表格列数（逐定义表 5 列、无裸竖线） | 通过 |
| 设施引用集合可从字段清单复算（10 = 1 DefaultTrainerList×2 + 4 TrainerList×2，去重） | 通过；目录候选 12、未引用 2 个已区分 |
| 未求值项 | 无（显式报告，不静默） |
| 重新生成与交付附表一致 | 通过（diff exit 0） |

## 4. 未执行的验证（明确标记）

- 未运行游戏、编译器或原 Ruby 脚本（按约束不执行）。
- 未在隔离容器重跑整套流水线（审查方亦未成功下载归档；本地重新生成已覆盖交付附表全部内容）。
- 未重新扫描全部 312 个 Ruby 文件重算 41 文件/139 行（沿用本轮既有实测，未独立重算）。
- 设施名单之外的专用读取路径全集未调查（归 WP04）。
