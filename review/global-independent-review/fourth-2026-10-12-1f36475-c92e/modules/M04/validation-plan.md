# 运行前验证计划

目的：核对正式数据附表与固定参考文本的数据对应关系，减少人工逐行核对漏项；不运行参考 Ruby、编译器、游戏、位图或行为模型。

命令：`python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M04/check-data.py`

工具版本：共享 baseline 为 Python 3.14.0；实际执行记录另写本目录 execution.json。

输入：R 的顶层 pokemon_forms/items，Shadow Pokémon backup 中 shadow_pokemon；Shadow 扩展的性格常数表；FormHandlers 的四块形状数据。B 的 WP22/23 附表和 WP21 区间表。全部只读。

区分能力：精确检查 48 Mega 条件/基础值、131 Shadow 物种量表/招式顺序、25 Nature 下降行、SPINDA 每行标记点集，而非仅检查行数；空、重复、漏行/错值会出现断言失败。验证不得把逐字数据一致性称为行为测试。

输出：检查项数量、匹配结果及固定输入锚点清单；失败时停止并解释失败来自检查器还是正式事实。

副作用：检查器仅 stdout，不修改输入；外层将执行收据及 stdout 保存到 M04。无网络、安装、参考加载、真实存档、图片生成。

## 收尾产物校验（运行前登记）

目的：检查必需字段、枚举、唯一ID、引用文件存在、能力/finding相互引用和覆盖文件数。不检行为、不升级任何supported结论。
命令：`python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M04/validate-artifacts.py`。
版本：Python 3.14.0。输入：本目录7项必需产物及source-scope；只读正式/参考路径存在性。输出：结构校验结果和计数；副作用仅外层向execution.json追加执行收据。
