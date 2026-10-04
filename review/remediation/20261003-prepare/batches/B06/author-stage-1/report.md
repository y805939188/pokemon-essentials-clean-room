# B06 作者阶段 1：七项贡献候选

本阶段只处理 **A032/A033/A035/A036/A037/A038/C120**。这是七项作者候选，待父任务安排限定范围的独立复审和实际整合核验；**不是完整 B06 或十项贡献 READY，也不是独立 PASS 或关闭结论**。A034/A059/C103 的本地及复合修订均未开始。

分支：`remediation/20261003-prepare/batch-B06`。精确接受起点：`ae230e76e9c041f39c28948321d0960804c02388`，tree `049d235d9f132f40717742e2e012c43a81df16b8`。批准计划仍为 `41fffb540c6483f5296ea0d33b789b75180d27ed`；本阶段范围由父任务同一作者线程中的明确后继授权收窄和扩展，原批准计划、原审查、公共登记均未改写。

模型请求为 `gpt-6.1-sol / Max / Standard(default)`；只在 Max 不支持时才允许 xhigh。方案 A 披露：**实际生效配置未独立核验**，本记录不把请求值当作平台执行凭据。

## 实际正式范围

原 B06 五条白名单：

- `deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md`
- `deliverables/final-specification-set/creature-rpg/wp25-party-and-storage.md`
- `deliverables/final-specification-set/creature-rpg/wp27-bag-and-item-storage.md`
- `deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md`
- `deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md`

另有下表三份原规格的明确最小同步，共八条正式路径。下表 ID 均沿用 `GIR-FD82-`，没有新增 finding 编号。

| ID | 原规格相对路径／条款 | 已纠正的原文问题 | 固定参考证据（静态） |
| --- | --- | --- | --- |
| A032 | `specs/creature-rpg/wp24-player-trainers-partners.md` §3.3 命名第 2 点 | 首词与去数字候选都要求非空且严格小于上限；等长继续，保留完整用户名处理后的截断回退 | `019_Utilities/001_Utilities.rb` 247–282；`001_Settings.rb` 49–60 |
| A033 | 同路径 §8 未知类型条目 | 装载/注册的类型错误与检查入口分开；非调试检查直接 true，调试拒绝新增且类型仍缺失时 false | `015_Trainers and player/002_Trainer_LoadAndNew.rb` 4–10、70–96、108–124 |
| A035 | `specs/creature-rpg/wp25-party-and-storage.md` §4.1 复制行 | 未满队伍忽略显式目标索引，追加后压缩；盒目标才按显式格写入 | `014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb` 178–203；`015_Trainers and player/001_Trainer.rb` 65–83 |
| A036 | 同路径 §11.2 捕获存储顺序行 | 返回盒 2 的向量补齐盒 0/1 满、当前盒 3 满与盒 2 格 0 空的前提 | 上述储存文件 231–251 |
| C120 | 同路径 §3.4 显示读取条目 | 查看可把旧文本转整数、把不可用背景写为基础编号；空值/空文本只默认显示而不改记录 | `016_UI/017_UI_PokemonStorage.rb` 378–396、424–434、593–613、1020–1062；上述储存文件 63–76、101–117 |
| A038 | `specs/creature-rpg/wp27-bag-and-item-storage.md` §4.3 给予守卫及防御性检查说明 | 菜单要求至少一名非蛋成员且物品可携带；濒死非蛋也满足；后段提示不构成菜单资格 | `016_UI/007_UI_Bag.rb` 479–520；上述训练家文件 57–72；`010_Data/002_PBS data/006_Item.rb` 189–197 |

表中参考路径均相对于固定仓库的 `Data/Scripts/`，参考 SHA 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，在主仓库外独立获取且保持 clean。证据的完整路径、行区间和哈希见 [source-reading-log.json](source-reading-log.json)。未改变调查宿主的真实用户名。

A033 原规格 §7 的概述按限定授权逐字保留；新的 §8 明确把两种检查入口列为该概述的例外。净化正文同时修正 §7 的过宽不变量。原 WP26 的 A037 满队前提本来正确，未同步修改；C120 原/净化 WP66-B 均留给 B16。净化 WP26 的既有 AQ-01～35 导航也保持原样，新附加的 AQ-36 对照通过本阶段分配表明确登记。

## 条款与静态向量

| ID | 净化正文／目录变更 | 确定预期与反向对照 |
| --- | --- | --- |
| A032 | WP24 §3.3；PT-29/30/31 | `abcdefghi1` → `Abcdefghi`；9 字符 `abcdefgh1` 保留数字；去数字后仍等长继续完整用户名回退 |
| A033 | WP24 §7 不变量 7、§8；PT-32/33/34 | 调试未知且拒绝新增 → false；非调试直接检查 → true；直接装载同一未知类型 → 错误；§5.3 对照表未动 |
| A035 | WP25 §4.1；PS-29/30/37/38 | [A] 复制 B，显式索引 0 或 5 均为 [A,B]、源保留同一 B；盒目标可覆盖；满队 false 且不改 |
| A036 | PS-11 修前提、PS-31 反向对照 | 当前盒 3 满，0/1 满 → 2；若 0 也有位则 → 0，盒 2 保持空 |
| A037 | AQ-04 修前提、AQ-36 反向对照 | 满队 6 名静默赠送只入盒 3/0；5 名时只追加第 6 名；均 true，无命名/图鉴展示/消息 |
| A038 | WP27 §4.3；BG-30/31 | 仅蛋无给予命令；加入濒死非蛋成员则有；构建菜单不改数量/队伍 |
| C120 | WP25 §3.4 状态表与兼容附表；PS-32～36 | 盒 5：未解锁 16 → 显示/记录 5；旧文本转整数 2；空文本/空值只显示 5、不写回；已解锁 16 保留 |

共登记 21 个分配给本阶段的静态向量，其中 19 个追加行，既有行只修改 PS-11/AQ-04。全部按明确的正常数据、初始化/素材、无相关回调或插件改写前提作文本核对，未执行游戏测试；C120 的内存记录写入不声称已保存到磁盘或实际渲染成功。

逐 ID 的原对象哈希、当前限定、条款、源证据、测试行及前后状态见 [finding-responses.json](finding-responses.json)。十个原 finding 与批准 acceptance 的完整对象均保存于 [finding-inputs.json](finding-inputs.json)，逐字对象身份重新与固定 Git 文档核对，不用历史 raw 措辞扩张有效裁决。

## B03 交界与恢复位置

批准计划的 B03 写集合与本阶段八条写集合没有交集；本阶段写集合与 B03 计划读集合也无交集。**B03 写集合与 B06 读集合仍共享** `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md`，其接受起点 blob 为 `f4ca72c08b72b50720b6c1c59be71d8ca1c4051b`，SHA-256 为 `a76e5a025a09e2ec2b50c6c5f252ed51cf1be633cdfbca00e647c74b1cba4bf7`。

七项候选采用直接命名/检查、基础队伍/盒操作、无队伍改写回调的静默赠送、菜单构建与正常初始化盒显示；没有引用未接受 B03 的运动、载具、步进通知、候选钩子或音频结论。已冻结 WP24 §4.1、§5.1、§6.1、§6.4 及 PT-22/23 的哈希，并逐字保留 B05 的 CI/HP 和另一共享目录的 IU/SH/GR/DC。B03 的七条计划写路径及父任务所报六份 `specs/overworld/wp11–14` 原稿同步路径也保持原接受版本；扩展物理交集仍为空，不由此推断语义依赖消失。

A034 的伙伴/雷达启动与后段取消、A059 的选曲/引子记忆与移动 BGM、C103 的煤灰擦除与步进通知，**均继续等待父任务提供 B03 实际整合且独立 Ultra 通过的后继及受影响输入重冻结**。`f8d0599de751299b7535242a654de7919caeb88d` 与交接 `cdb689ba7f20ec8699329015fc5bdd520ca3a037` 仅用于先前只读冲突调查，未被当作接受前提。

继续同一作者线程和本分支，恢复入口为 [resume-checkpoint.json](resume-checkpoint.json)，冻结段落/测试/整文件身份在 [preservation-freeze.json](preservation-freeze.json)。父任务还须明确剩余三项的精确写入范围；本阶段不会自行放开该门。

## 作者静态检查与登记边界

`python3 review/remediation/20261003-prepare/batches/B06/author-stage-1/verify-static.py` 已完成八条路径及精确原稿条款差异检查、21 行向量身份检查、完整共享段保留、30 条 B05 输入身份、十对完整 canonical 对象及固定参考 clean/tree/文本哈希核对。结果见 [static-validation.json](static-validation.json)。精确差异附件采用 `--unified=0`，避免把合法的补丁空格上下文当成新增尾空格；附件身份见 [patch-identities.json](patch-identities.json)，完整上下文可直接比较冻结 Git 提交。该脚本只读取文档、Git 身份及文本字节，不执行参考行为或模拟预期。

公共登记唯一写入者仍为 A-REG；这里只提供 [registrar-proposals.json](registrar-proposals.json)，不应用、不关闭。独立复审和实际 integration 均未启动；无新的 finding、无原审查/批准计划变更。保留 U01–U10、G01–G12、AX01–AX20、具名未知、真实 Demo/素材/宿主/插件组合未证边界；运行观察 0、已证 Demo 事件链 0、参考执行 0。
