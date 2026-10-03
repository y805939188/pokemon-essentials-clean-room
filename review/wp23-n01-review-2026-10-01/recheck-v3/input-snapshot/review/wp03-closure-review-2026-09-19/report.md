# WP03 v4 闭合复审与后续批次建议

日期：2026-09-19。独立 reviewer；本报告及配套材料属于 Reference/Audit 侧，不是 WP80 sanitized 产物。

**结论：PASS（限定范围，PASS_SCOPED）。WP03-R01 最后一项已闭合；本轮无新问题。可以进入下一批 WP04–WP07。**

## 1. 实际对象

工作区：`/Users/dingshinn/Desktop/pokemon-framework-reference/`。固定参考 HEAD 实测仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，describe 为 `v21.1-23-g8c5911e4`；默认机制世代为 8。

| 文件 | 被审 SHA-256 | 字节数 |
| --- | --- | ---: |
| `specs/kernel/wp03-content-identity-and-schema.md` v4 | `7a9c85dae2031c167f172395dc4b769d6bd16575ce48310127249445df079575` | 30257 |
| `planning/review-manifest-2026-09-19.md` | `3cd10b029777538755c279e8b8b1e2f16ca65487754ed0b1084f6f72ada50d12` | 10375 |
| `planning/extraction-plan.md` | `c173587708c9fcaaaaa1a4079bdedaa14d02405871b3fe3cd2ed6d16caeffd78` | 46915 |
| 上轮 v3 复检报告原件 | `3f2d9661cda4d3b96deef7b1bb88b0b30d3274131f8c0837352d5ae8623d3a3a` | 7776 |

本轮固定 23 个输入副本。当前 manifest **21 项完整哈希及字节数全部一致**；20 项是上一轮清单的口径，本轮已新增 v3 复检报告。旧报告原件未改写。相对上轮副本，既有文件仅 WP03 与 manifest 改变；WP03 行为正文只修正枚举存在条件并补静态场景。

文件清单及实际差异见 [input-manifest.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-closure-review-2026-09-19/input-manifest.json)、[changes-from-v3.diff](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-closure-review-2026-09-19/changes-from-v3.diff)。本报告记录实际字节，不将后续状态回填的新哈希冒充本轮被审版本。

## 2. 本轮检查及结果

- 对照 v3→v4 的实际差异和上轮唯一剩余项，核对第 72、260 行及 manifest 对应记录。
- 重新核对 `reference/pokemon-essentials/Data/Scripts/010_Data/002_PBS data/013_Encounter.rb:20–59`。枚举遍历已有数据；正常编译的符号键表中，正版本枚举包含已有目标版本条目和已有版本 0 条目，不生成缺失记录。v = 0 仅包含已有版本 0 条目。
- 四种静态场景现已明确：已有 0/2、仅 0、仅 2、均无，分别产出 0/2、0、2、无，表内容不变。它们与 `get` 回退及 `exists?` 精确检查分别表述，符合源码。
- 沿用上轮相关源文件集合进行完整性核对：55 文件均未改变，Git blob 与固定提交一致。这不是重复全文审查 55 文件。只读 Git 查询退出码均为 0；普通状态为空，ignored 仍有 `.DS_Store`、`PBS/.DS_Store`。详见 [source-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-closure-review-2026-09-19/source-checks.json)。
- 未执行游戏、Ruby、编译器、任意参考表达式或 WP02 生成器；未重做全仓调查。未验证图鉴实际画面、宿主读取失败或其他运行行为。

## 3. 问题处置与范围结论

| 问题 | 处置 |
| --- | --- |
| WP03-R01 剩余的枚举存在条件 | 关闭；v4 第 72、260 行满足上轮验收 |
| WP03-R02、R04、R05、C04 | 继承 v3 复审关闭结论；本轮未发现相关回归 |
| WP03-R03、C01–C03 | 继续关闭 |
| 新阻塞问题或非阻塞建议 | 无 |

通过范围为固定基线上的内容身份、注册/查找/枚举、已述缺失值和状态变化、schema 结构及校验边界、固定规则与作者数据区分、字段责任目录及适用静态场景。未据此确认各内容字段的领域语义全集、全部 PBS 生命周期、动态插件组合或运行结果。

U01–U10 保持既有处置。WP01/WP02 的限定 Reviewed 继续有效；本次通过不代表 WP80 sanitized 通过，也不构成未来架构设计或法律结论。

## 4. 状态登记建议

提取方可以根据本报告登记：

- WP03 → **Reviewed（本报告限定范围）**。
- F01-02 → Reviewed（WP03 身份/注册查找/枚举/缺失值范围）＋Inventoried（各内容类字段语义范围）。
- F02-01 → Reviewed（WP03 schema/已述校验边界/责任目录范围）＋Inventoried（字段语义全集范围）。

其他 Feature 子范围不随之升级，尤其 F02-03 的切换/编译/组合兼容性仍按 WP04 等适用包处理。头尾状态和矩阵可做管理性同步；manifest 保留本轮被审哈希、新哈希与状态差异，不需因此重新提取行为。review 原件不可改写。

Reviewer 本轮未代提取方修改规格、矩阵或 manifest。

## 5. 工作包数量与批次建议

按当前 `extraction-plan.md` 的正式任务表逐行独立统计，得到 **87 个唯一可执行 WP**，并非存在 WP87 这个编号：

- 编号主体系为 WP01–WP80。
- WP47、WP52、WP66、WP67、WP73 五个编号只表示任务族。
- 子包分别为 2、3、3、2、2 个，共 12 个；所以 80 − 5 ＋ 12 = 87。

计数与逐包依赖记录见 [plan-count-and-dependencies.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-closure-review-2026-09-19/plan-count-and-dependencies.json)。WP01–WP03 已通过各自声明范围；按现有任务清单，尚余 84 个可执行包。这个计数不是功能完成率，未来有证据支持的拆分仍可调整计划。

建议默认每批 3–4 包，通常允许 2–5 包。批次以共享证据、依赖就绪和单批工作量为依据，逐包保持身份和状态，批末统一送审。以下是近期候选安排，不替代原计划：

| 批次 | 范围 | 内部关系与前提 |
| --- | --- | --- |
| 下一批 | WP04–WP07，4 包 | PBS 生命周期、扩展/插件、时间随机统计、诊断与 I/O；声明依赖均在 WP01–WP03，没有必须先完成的批内依赖 |
| 随后一批 | WP08–WP10，3 包 | WP08 使用 WP04，WP09 使用 WP06，WP10 接 WP09；可在批内先固定 WP09 的自检版本再做 WP10 |
| 世界基础批 | WP11–WP14，4 包 | WP11 → WP12 → WP13/WP14；若解释器范围过大，可分为 WP11–12 与 WP13–14 两批 |
| 资源交互批 | WP15–WP17，3 包 | WP15 → WP16/WP17；还需前批的地图、本地化与 I/O 范围 |
| 生物基础批 | WP18–WP21，4 包 | WP18 → WP19 → WP20/WP21；依赖已有时间和地图输入；可与上述世界批调整先后 |

以上不是严格按编号连续推进的长期承诺。例如 WP22/WP23 的完整范围需要战斗、成长等后续知识，不能仅为凑连续编号把 WP22–WP25 一律声明完成。计划 Dependencies 是完成知识依赖，不是源码加载顺序，也不意味着开始调查前必须全部通过外审。

同批上游可在完成相关范围自检、固定版本并标注尚未外审后供下游引用；整批交付前回查依赖与回归。一个包有问题时可单独请求修订，不让其污染无关包的审查状态。遇到大包或真实缺口应缩小批次、登记 Partial，不能靠省略消费者/例外赶完指定包数。WP78→WP79→WP80 仍保持既有阶段出口要求。

## 6. 下一步与停止点

可以将本目录的 [下一批执行提示词](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-closure-review-2026-09-19/next-batch-prompt.md) 交给提取模型，先登记本次通过状态，再执行 **WP04–WP07**，四包分别形成产物，统一送审。本提示词是提取侧任务授权文本，不是 reviewer 已执行这些包的证明。

本轮停止于闭合审查、计数/依赖确认及提示词交付；没有开始 WP04–WP07。最终输入一致性与交付文件哈希见 [final-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-closure-review-2026-09-19/final-checks.json)。
