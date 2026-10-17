# R8-U01 返修独立复核

**完整候选结论：PASS（静态范围，附一处非阻断叙述勘误）。**

本结论只绑定新候选 `c877e66d7011e5e1a0bb9b43ba39cbb15255064d` / tree `930c67550a80961dc263ea2e14e5b70e112f8778`，作者分支 `revision/r8-u01-20261017`。原被审候选 `bce1659e01ca33ecafb91464ce1ada32c0499faf` 的失败记录保持原状；[原完整报告](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1a5c6dab85b6638403ef6e42bc97f23e842580b1/review/remediation-eighth-20261016-prepare/independent-reviews/R8-U01/cloud-independent-20261017/report.md) 在 `1a5c6dab85b6638403ef6e42bc97f23e842580b1`，本报告采用新的独占路径，不覆盖原报告。

| 项目 | 结论 | 本次依据 |
| --- | --- | --- |
| R8-U01-REVIEW-LOC-01 修复 | PASS | 两对象六字段准确更正，8处定位全部独立核验 |
| GR8-KER-001 | PASS | 有序删除、五控制、主档门和两个UI调用者边界再次核对 |
| GR8-KER-002 | PASS | 结果空性装配门、默认17项/加载标记、后继验证与语言边界再次核对 |
| 已选 GR8-UI-001 | PASS | 仍仅澄清普通No不调用持久层保存，同节不回滚保持 |
| 完整候选交接 | PASS | 原阻断已消除，无正文/业务范围变更；下列数字勘误不误导实际定位 |
| actual integrated / ACCEPTED / CLOSED | NOT_GRANTED | 需实际整合后另行接收 |

## 原失败项是否全部解决

已重新完整读取新旧两份 JSON，并递归比较全部键值。不是“8处都发生修订”：实际是 **8处重新核验，其中1个对应位置在两份记录中更正，共6字段**；其余7处及全部其它键值不变。

| 文件/指针 | 精确修改 |
| --- | --- |
| `remediation-record.json /records/1/change_locations/0` | line 33→102；短 locator→唯一长前缀 |
| `tagging-handoff.json /changes/4` | 同样两字段；section→`4.1 启动阶段表`；anchor→`#41-启动阶段表` |

新定位见 [record L628–629](https://github.com/y805939188/pokemon-essentials-clean-room/blob/c877e66d7011e5e1a0bb9b43ba39cbb15255064d/review/remediation-eighth-20261016-prepare/candidates/R8-U01/evidence/remediation-record.json#L628)、[tagging L49–53](https://github.com/y805939188/pokemon-essentials-clean-room/blob/c877e66d7011e5e1a0bb9b43ba39cbb15255064d/review/remediation-eighth-20261016-prepare/candidates/R8-U01/evidence/tagging-handoff.json#L49)。独立读取的 WP09 标题在 L97，规则在 L102；长前缀 `| 启动读取 | 先检查默认主档：` 只命中 L102。原失败中“指到未改登记配置行”的问题已消除。

[recheck-location-fix.diff](https://github.com/y805939188/pokemon-essentials-clean-room/blob/c877e66d7011e5e1a0bb9b43ba39cbb15255064d/review/remediation-eighth-20261016-prepare/candidates/R8-U01/evidence/recheck-location-fix.diff) 在主审独立计算中能精确从旧全文重建这两份新文件。其1362字节/SHA256 `594e167502d42957bbaf656b5a6043439b988c61d8cbcd33c5e315ffbda6bd73` 与 binding 一致；原报告的12239字节/SHA256 `002448cc6afa3f0cb20ecfc1694aa56b92450f2ef7298bfb18b6137c84f1d1d7` 也独立重算吻合。

## 八处定位的独立结果

主审从候选全文寻找每个 locator，独立确定最近标题/锚点，再与最初作者输入 `4575e80d041ab0c74a42e2e36399d05791dbaa5b` 的真实行差异比较。没有采用作者脚本输出作为判断替代。

| 项目 | 文件 | 行 | 唯一命中/成对记录/标题锚点/真实diff |
| --- | --- | ---: | --- |
| KER001 | WP10 删除失败 | 228 | PASS |
| KER001 | WP10 有序删除节 | 230 | PASS |
| KER001 | WP09 删除引用 | 139 | PASS |
| KER001 | 同族目录删除组 | 295 | PASS |
| KER002 | WP09 启动读取 | 102 | PASS |
| KER002 | WP65 启动链 | 27 | PASS |
| KER002 | 同族目录结果分层组 | 309 | PASS |
| UI001 | WP65 普通拒绝 | 88 | PASS |

`refresh-locations.py` 的唯一匹配守卫会拒绝非唯一 locator，且核两份记录人口一致、实际改动行和标题/锚点。静态阅读确认其默认分支只读，持久写入均受 `--write` 控制。本复核未执行该 Python 脚本，另以只读 GitHub 内容和独立 JavaScript 复核上述结果。

## 非阻断勘误：旧短前缀实际有三处命中

[recheck-entry.md L12](https://github.com/y805939188/pokemon-essentials-clean-room/blob/c877e66d7011e5e1a0bb9b43ba39cbb15255064d/review/remediation-eighth-20261016-prepare/candidates/R8-U01/evidence/recheck-entry.md#L12) 将旧短前缀描述为 L33/L102“两处”命中。按当前脚本的子串匹配规则，实际是 **L33、L61、L102 三处**，L61 是持久值目录表头；[location-validation.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/c877e66d7011e5e1a0bb9b43ba39cbb15255064d/review/remediation-eighth-20261016-prepare/candidates/R8-U01/evidence/location-validation.json) 已正确记录 `[33, 61, 102]` 并拒绝。

建议入口说明改为“三处”；binding 的根因说明若要完整列举，也应包含 L61。此为非阻断叙述勘误：实际8个 locator、两份记录、唯一性守卫和三命中拒绝结果全部正确，不会再次把标签贴到错误行。因此不把该数字错误等同于原 LOC-01 的可消费定位失败，也不增加新的行为或候选关闭前置门。本报告没有宣称新增说明文字完全无瑕疵。

## 四个 mirror 与完整候选语义重新绑定

已分别从新旧固定 SHA 重新取得四份全文，独立计算 UTF-8 bytes、SHA256、Git blob SHA1，并读取真实 tree mode；全文及全部身份均相等，且与原 manifest 一致。新旧整个 mirror tree 都为 `1058b32df273f01d141a5852a68be01c6f4b4ba5`，未增加、删除或改名文件。

| mirror | mode | bytes | blob |
| --- | --- | ---: | --- |
| WP09 | 100644 | 18749 | `dab9313130cbb775300ac1f86f8de1c08a4bec71` |
| WP10 | 100644 | 26354 | `15ad3bada6b3c1cb1d3712a687abb013f21a0aca` |
| WP05–10目录 | 100644 | 51523 | `d5ea91d6cc01acf303a172d0c4b1055b3c227c12` |
| WP65 | 100644 | 45079 | `42c4db7a924e51e5c1427a0b7c38b43101a68aba` |

本次辅助续审重新完整实读四 mirror，主审重读 WP09 全文、各受影响完整行为节/13行及关键源分支；并重核完整原合同与最初输入同值、固定R/B8和原5caff/C35双来源资格。原完整读集/历史资格的范围与证据见[原读账](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1a5c6dab85b6638403ef6e42bc97f23e842580b1/review/remediation-eighth-20261016-prepare/independent-reviews/R8-U01/cloud-independent-20261017/read-ledger.json)；本轮是同一审者的有界返修续审，没有把未重读的全部历史语料重新登记为FULL，也没有仅凭旧PASS或作者“不变”声明放行。

- **KER001**：固定参考 `001_SaveData.rb` L15–17、L65–68 与 `UI_Load.rb` L216–279 再次支持先P、后单个备份，首删失败不到备份检查，第二失败保孤立备份但下次主档门为假。WP10 L228–246 和目录 L297–307 保留五控制、标题返回/无效档拒绝退出及同意重置分层、提示失败/非捕获异常限制。递归读取与删除不混同。
- **KER002**：固定参考 `StartGame.rb` L21–35、`SaveData.rb` L24–50/L73–80，默认17项/Value加载门和后继 `UI_Load.rb` 的完整行为单位再次核对。无主档、可读旧序列适配空表、有效非空三种结果正确；空表不转换备份/写回，后续有效性/备份/拒删退出/同意正常菜单独立。BACK默认哨兵0、解码异常、WP08/SV02/LZ13/14前提保持。
- **UI001**：WP65 L88仍仅限定不调用持久层保存；L90前置变化不回滚及选择音/false未变。固定 `UI_Save.rb` L100–128 再核普通No与保存调用门。原共享可变地图名、Town/已展开对照、WP11/T11–14/JXN-NAME05的资格保持，不新增命名规则或目录写集。

13个唯一静态场景与 record/tagging 一致，原目录46520字节全文仍为精确前缀。五类删除与八类启动/后继场景全部 **NOT_EXECUTED**。未执行Ruby、游戏、真实旧档/文件故障、独立业务模型或宿主；作者57项和本次8定位工具检查均只是 TOOL_VALIDATION。

## 写集、发布与剩余门

旧→新候选只前进1提交，共20个变化路径，全部位于本批 `evidence/`；两个定位文件仅六字段，其余既有 commands/progress/review-entry 只追加，新增脚本/核验/入口/日志均为文档证据。四 mirror、正式规格、AGENTS、audit/planning、旧报告及旧接收台账没有变化。

本次请求配置继续为 gpt-6.1-sol / ultra / default / normal / Fast off；actual model、effort、tier、speed、Fast 与实际任务UUID无权威echo，保持UNVERIFIED。主审 `/root`，辅助 `/root/evidence_audit`、`/root/ker002` 均为原上下文续审，不新增独立最终验收票。

本复核只向新的本批独占review路径写证据，经已连接GitHub工具创建提交并发布独立分支，非force前进后逐文件完整远端回读。没有本地shell git push/fresh clone执行回执；传输及身份核验不给业务信用。详见[机器结论](recheck.json)、[独立核验证据](verification.json)和后继[远端回读](remote-readback.json)。

新固定候选无剩余阻断项；上述说明数字勘误为非阻断建议。R8-INTEGRATOR仍须实际整合，非作者另读受影响整文件及累计保留、接收共享消费者/历史条件，之后分别登记 actual integrated PASS、ACCEPTED、CLOSED。本次候选PASS不替代其中任何门。协调任务仍由父任务转交。
