# B06 stage 1 repair 1 作者后继报告

本包限定修复固定独立报告中的 `B06-S1-R1-N001` 与 `B06-S1-R1-N002`，继续同一作者 A-B06、同一 `remediation/20261003-prepare/batch-B06` 分支。作者文档检查完成，七项新候选全部等待下一轮独立 Ultra；本报告没有独立通过、实际整合通过或关闭结论。

固定请求变更来源为 [`e12791309ace5458da29fd91c7bed70ac4175700` 的独立报告](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e12791309ace5458da29fd91c7bed70ac4175700/review/remediation/20261003-prepare/batches/B06/review-stage-1-round-1/report.md)，原被审候选为 `3c5b280b8ffdbcfb93d0410e2195c79e35b8178c`，本次直接父提交为作者证据 `806c969105f4f2aca916708013ad54f972524d5e`，原已接受基线为 `ae230e76e9c041f39c28948321d0960804c02388`。固定报告及证据完整读取记录见 [review-reading-receipt.json](review-reading-receipt.json)。两个新增 ID 的原对象、来源、局部登记状态完整保留在 [review-new-findings-inputs.json](review-new-findings-inputs.json)，没有改成原全局 finding ID。

父任务明确授权在同一分支作两项有界返修、新增后继记录、普通提交/推送及远端回读。原 `author-stage-1/` 的 15 件历史作者证据保持原字节；独立 `review-stage-1-round-1/` 的 11 件输入固定在来源提交，没有覆盖或并入作者分支。新候选精确 SHA/tree/文件身份由随后仅新增的 [candidate-manifest.json](candidate-manifest.json) 冻结；后继记录不冒充历史证据。

## N001：兼容识别的行边界

旧候选把兼容文本限定为整段仅有指定格式，排除了末尾 LF 和包含其它行的文本。现将定义改为文本中首个完整匹配行：该行只含小写 `box` 和一串 ASCII 十进制数字；行首为文本开头或 LF 后，行尾为文本末尾或 LF 前。取得该行数字后，先把背景内存记录写为整数，再作可用性判断。空值/空文本的只显示不写回、不可用编号回退写入、已缓存且未重读的限制、正常初始化/素材前提、正常退出不回滚内存写入均保留。

这是固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的 `Data/Scripts/016_UI/017_UI_PokemonStorage.rb` 378–396 行（决定分支 384–386 行）与官方语言说明的人工静态推导。官方锚点说明区分行边界与整段文本边界；字符串按正则取值采用首个匹配子串。没有运行对应表达式或行为模型。[Ruby Regexp 官方说明](https://docs.ruby-lang.org/en/3.1/Regexp.html#class-Regexp-label-Anchors)、[Ruby String 官方说明](https://docs.ruby-lang.org/en/3.1/String.html#method-i-5B-5D)。

相对于父提交，本次正式差分仅涉及以下三条路径，完整差分见 [repair-delta.patch](repair-delta.patch)，此前七项的八路径全量差分见 [full-stage-formal-diff.patch](full-stage-formal-diff.patch)：

| 相对路径 | 返修条款/ID | 精确变化 |
| --- | --- | --- |
| `deliverables/final-specification-set/creature-rpg/wp25-party-and-storage.md` | §3.4 兼容附录；§10 自有 PS 导航 | 父 94 行定义替换、95 行样本后新增两行、父 201 行计数由 38 改 42 |
| `specs/creature-rpg/wp25-party-and-storage.md` | §3.4 显示读取条目；C120/N001 | 仅父 77 行兼容定义最小同步，其余原稿条款保持 |
| `deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md` | PS 目录及 PS-39～42 | 仅扩展自有 PS 标题并追加四行；所有原有目录正文和向量原字节保持 |

新增向量及反向对照都属于静态预期，没有执行结果：

| ID/对照 | 固定输入边界 | 静态预期及观察点 |
| --- | --- | --- |
| PS-33 ↔ PS-39 | 原 `box2` 与末尾增加一个 LF；后者字节 `62 6f 78 32 0a` | 同为整数 2；先写整条背景记录，再判可用、显示；正常退出后内存仍为 2，没有磁盘保存断言 |
| PS-40 | `prefix`、LF、`box2` 依次组成的文本 | 第二行是首个完整匹配行；整条记录转为 2，正常显示/退出前提下仍为 2 |
| PS-41 | 无 LF 的单行 `box2x` | 仅观察兼容识别结束点：没有完整匹配行，没有文本转整数写回；不推定后续显示或退出成功 |
| PS-42 | `box3`、LF、`box2` 依次组成的文本 | 首个匹配行取得 3；后面的匹配行不覆盖首个结果；正常前提下内存/显示为 3 |

原 PS-32～36 的锁定/解锁、旧文本转换、空文本/空值对照保持原字节；不扩大为任意字符串可以成功归一或正常显示的承诺。C120 的 WP66-B 原稿及最终 UI 贡献仍归 B16，未写。

## N002：来源读取范围越界

历史 `author-stage-1/source-reading-log.json` 的 B06-SR-03 声称读取 1–135 行，而固定 `Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb` 实际只有 124 行。旧脚本切片静默截断，因此与整文件相同的哈希不能证明 125–135 行存在或被读。历史记录和旧脚本均保持，明确勘误记录在本后继 [source-reading-log.json](source-reading-log.json)，重新完整读取的有效范围为 1–124。

新 [document_integrity.py](document_integrity.py) 先验证整数范围 `1 <= start <= end <= 实际行数`，无效即拒绝；之后才构造切片并计算哈希。作者重新校验十份固定源文本的 17 个有效跨度。两条文档范围正例 1–124、124–124 接受；五条反例 1–135、125–125、0–124、124–1、1–0 全部在哈希前拒绝，注入的哈希观察函数调用数均为 0。证据见 [source-range-validation.json](source-range-validation.json)。这七条执行检查只验证文档范围工具，参考程序与游戏行为向量执行数仍为 0。

A033 的正文、原稿同步条款和 PT-32～34 不变；本修复纠正证据可信度，没有改动检查/装载入口语义。

## 七项回归与边界

固定独立报告中 A032/A033/A035/A036/A037/A038 的 `PASS_SCOPED` 只属于旧 `3c5b280…` 候选；C120 因 N001 为 `REQUEST_CHANGES`，N002 阻止整体证据包可接受。本包逐一保留来源结论，未把六项旧结论移植为新候选通过。

| 七项原 ID 后缀 | 后继静态向量 | 保留/返修结果 |
| --- | --- | --- |
| A032 | PT-29～31 | 正文、原稿及三行向量原字节保持 |
| A033 | PT-32～34 | 行为及三行向量原字节保持；纠正 B06-SR-03 范围证据 |
| A035 | PS-29～30、37～38 | 复制条款/原稿和四行向量原字节保持 |
| A036 | PS-11、31 | 捕获入队/最早空盒对照及原稿同步原字节保持 |
| A037 | AQ-04、36 | 满队与五成员反向对照原字节保持；只读 WP26 不写 |
| A038 | BG-30～31 | Give 菜单/执行守卫分离、原稿及两行向量原字节保持 |
| C120（B06 贡献） | PS-32～36、39～42 | 原五行不变，修复兼容定义并追加四行；B16 贡献未涵盖 |

七项现共 25 行静态向量：旧 21 行与独立证据行哈希完全相同，新增 4 行。另核 10 个保护条款、17 个保护整文件及 PT-22/23，全部保持原已接受基线身份。作者检查结果见 [static-validation.json](static-validation.json)；全七项回应、前提、来源、反例/反向对照、行哈希见 [finding-responses.json](finding-responses.json)。

参考独立 Git 的 SHA 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree 为 `7589c800b61ba13a13040ed0d686979b80a84fd0`，范围检查时工作区 clean。参考内容未进项目 Git，未改 ignore、未推参考、未运行 Ruby/游戏/编译/转换/生成/反序列化/模拟器/求解器。实际运行观察 0、已证 demo 事件链 0、行为向量执行 0。U01–U10、G01–G12、AX01–AX20、具名未知、真实 demo/素材/宿主/插件组合未证状态保留。

本作者请求模型 `gpt-6.1-sol / Max`，仅在不支持 Max 时才允许 xhigh；服务档位继续 Standard/default。实际生效配置未独立核验，按方案 A 披露请求值；本轮没有配置变更、派生作者或独立复审任务。

下一步由父任务安排针对新固定候选的全七项独立 Ultra；作者不发起复审、不整合、不关闭、不改公共登记，A-REG 为唯一公共写入者。A034/A059/C103 继续等待 B03 实际整合的独立 Ultra 通过及父任务新的受影响输入冻结、精确剩余三项写入范围；未接受的 `f8d0599de751299b7535242a654de7919caeb88d` 和 `cdb689ba7f20ec8699329015fc5bdd520ca3a037` 没有被作为已接受前提。恢复点见 [resume-checkpoint.json](resume-checkpoint.json)，登记建议见 [registrar-proposals.json](registrar-proposals.json)。`whole_B06_ready=false`、公共登记写入 0、关闭 0。
