# 报告发布与独立读回

报告固定提交为 `680e3988c4144db269e063971991134b8e0bd678`，tree 为 `4e2858fe6d52e9b36ede5a54a9ad730c05764108`；基点为作者最终读回包 `272885cca76c36cd04dde27b6be2c654759ec4c2`。审查对象仍为 NEW `1abaefb1db5818ff9404392143c476979d34c21a` / tree `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85`。

该提交通过普通 push 发布到 `refs/heads/review/b20-affected-cloud-20261011-1`。随后新建独立 bare Git 仓库，以明确远端 URL 和 ref 进行网络 fetch；没有本地 object alternates 或对象共享。全部 16 个报告输出，包括根输出清单本身，均从远端取回并逐字节、blob、SHA256、bytes 核对；JSON 全部解析成功。

[report-readback.json](report-readback.json) 保存这次远端读回及全部 16 个输出身份。该凭据固定报告提交，不嵌入自身后继提交哈希。本目录后继发布提交仅增加本 README、读回 JSON 和 [output-manifest.json](output-manifest.json)。后继提交将普通推送并再次独立读回全部 19 个输出；最终准确 commit/tree 及核验结果由最终回复绑定，避免自引用或无限递归读回。

根 [报告](../report.md) 和 [问题与验收条件](../findings.json) 的结论保持 `REQUEST_CHANGES_SCOPED_AFFECTED_CANDIDATE`，3 个局部 P2 阻塞。发布和读回仅证明报告身份与保留边界，不构成 actual 门或正式接受。
