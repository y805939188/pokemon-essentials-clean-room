# B15 作者候选入口

16 本地贡献、10 主责；六正式路径已修订，未获独立批准，canonical OPEN 与正式接受数量不变。基线 `0cfe99094b76f8d75fded0d638694677855a5f0c`；派发管理资料 `4cb51a33402ec6559a396226239afe308a4b8849`。

- `report.md` / `finding-revisions.json`：每 finding 的修订、准确前后身份、控制对象绑定、合法前提/静态最小反例及邻近反向、来源和限制。
- `formal-identities.json`：六正式文件前后 blob/SHA-256/字节；完整候选 SHA 外部绑定在后继 `../author-draft-1/publication-receipt.json`。
- `catalog-protection.json`：18目录、2,995旧行、2,907其他 owner 原行保护；只修改旧 P29/MG-29，本地新增43行，旧序与重复保持。
- `affected-interface-assessment.json` / `independent-review-request.md`：九组冻结导航的有界作者检查及独立 candidate/actual 派发条件；作者未签发 PASS 或 NOT_AFFECTED。
- `public-registration-suggestions.json`：唯一 A-REG 的串行登记建议，未修改公共台账/index/导航/全局状态。
- `source-limits.json` 与 `../author-draft-1/input-verification.json` / `reading-log.json` / `configuration.json`：输入69身份、整16原finding/PLAN绑定、新受影响静态阅读和未证配置/来源限制。

当前阻塞：原 spec 暂只读合同要求父 A-REG 先登记具体范围再应用。精确三路径补丁及 finding/path/clause/before/after身份见 `../author-draft-1/original-sync-proposal.json` 与 `original-sync.patch`，补丁内容冻结于 `ce4562831689c8c567f15f1d797f7d424e8276d4`（管理提案，非 FIX_BASE）。收到准确 amendment 后按 before 身份应用、核对 proposed_after 并新冻候选，再进行必要独立 review。A056 与 C122 的其它批次贡献不在本次范围，B16 负责其局部交界。

参考固定只读；新例子均 NOT_EXECUTED。作者 metadata 检查只验证保存的文字/身份/范围，运行观察、静态向量执行、demo已证全0。
