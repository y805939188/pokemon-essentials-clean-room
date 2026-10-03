# GR-001～003 有界复审（2026-10-01）

**结论：REQUEST_CHANGES。GR-002、GR-003可关闭；GR-001保留OPEN_PARTIAL，暂不进入下一批GR或新WP。** 规则修订大体正确，剩余是GR-001若干具体样例把双引号写成了反引号，造成输入与预期不一致。本次不新增问题编号。

## 被审对象与机械核验

| 包 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| specs/kernel/wp04-pbs-lifecycle.md | `63fe6933bdd47f361a96195c138276b94c0919d0286f230a90134ea18b6ba594` | 25,112 |
| specs/kernel/wp08-localization.md | `074662540214264206c988245e1fbf5c7d6d202279da1a215650e7c8a5ce912b` | 20,394 |
| specs/kernel/wp10-migration-failure-recovery.md | `07ccae9ab040cd6c85b22ea4a70bd0b1a8dfe72ce735aab68c82cec22fb0c917` | 23,833 |

manifest §1 1,066条、主TSV v56 971条全部与磁盘一致，无重复；阶段最终身份一致。三份diff从正确冻结基线逐hunk应用后3/3精确重建当前字节。只改变三份目标规格、矩阵与两份行政清单，第一组31项通过材料未动；reference固定commit且Git清洁。WP04／08／10沿既有清单覆盖在manifest登记，未要求为它们额外添加主TSV行。

## GR-001：位置规则正确，字面样例仍需修正

**已正确**：WP04 §4.2已区分存在后续字段的检查与单值／末字段；§9.2的对应引号样例和checks.json四条向量使用正确输入。四条JSON向量经解码后的完整input、expected_flags和球标志预期，与原finding逐一相同，不存在JSON转义层差异。

**剩余位置**：

- `specs/kernel/wp04-pbs-lifecycle.md:81`：括注中PokeBall例子的包围符是反斜线＋反引号。
- `review/gr001-gr003-revision-2026-10-01/revision-response.md:17,23–25`：原问题说明及前三条验收表样例同样误用反引号。

错误样例的包围码点是 **U+005C U+0060**，正确输入必须是 **U+005C U+0022**。这不是单纯的排版差异：若非末字段实际含反引号而没有双引号，参考不会进入双引号重组／剥除分支，保留的标记使球标志匹配为false；回应表却为该写法标了true。Markdown代码跨度也被内部反引号打断，无法把这些数据当成无歧义验收输入。

下面的数据直接取自已核实的正确JSON向量；代码标记只用于显示，内部反斜线和双引号是实际输入字符：

| 输入 | 预期Flags | 球标志 |
| --- | --- | --- |
| `\"PokeBall\"` | `\"PokeBall\"` | false |
| `\"PokeBall\",Other` | `PokeBall`、`Other` | true |
| `Other,\"PokeBall\"` | `Other`、`\"PokeBall\"` | false |
| `PokeBall` | `PokeBall` | true |

补修只需统一上述错误文字、回应表及必要身份登记。保留已正确的§9.2／JSON向量和规则，不修改reference，不运行编译器。详细码点证据见[literal-checks.json](literal-checks.json)。

## 可关闭的两项

- **GR-002 CLOSED**：WP08§6.3及四组场景准确写出首条数字决定形态、Map数组先拒、行数检查次序和输出先截断；非数字哈希与合法三行数组对照正确，原运行时回退规则未改。
- **GR-003 CLOSED**：WP10场景已与第108行一致，跳过占用新槽；三个既定结果[C,A]、[A,A]、[C,D]及正常分支清理旧字段保持正确，未理想化参考行为。

这些结论限定于本次GR修订的具名静态范围，不扩张原包批准范围，也不宣称运行验证。

## 下一步

按[GR-001最小补修提示](next-task-prompt.md)处理后，再做一次定点复审。WP08／WP10保持当前已核验字节，不重做两项已关闭内容。GR-004～016仍未处理，第一组三包31项及N01已通过范围保持；不启动WP65。

本次只新增审查目录；未修改被审规格、矩阵、登记、外部review原件或reference。未运行参考代码／编译／迁移／翻译器，未操作真实存档／翻译文件，未创建任务／Agent、未发跨会话消息、未提交／推送。

[逐项结论](findings.json) · [登记与差异核验](registration-checks.json) · [来源](source-checks.json) · [最终完整性检查](final-checks.json)
