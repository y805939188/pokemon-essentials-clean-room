# 第四次全局独立审查交付入口

**有限全局审查完成：17项必修（11 P2、6 P3），无P1；新增可选/未决规范finding为0。**12领域、独立反证CA/CB和14条独立交界链均已完成。能力覆盖和运行未知没有被关闭；未修订正式规格，未实现引擎，未合并main，未启动云端update。

固定正式B `1f36475d22120a0d1175967d5b17d71fe8311d88`（tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`）；固定R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（tree `7589c800b61ba13a13040ed0d686979b80a84fd0`）。报告分支 `codex/review-fourth-20261012-1f36475-c92e`。

## 阅读顺序

1. [最终报告](final-report.md)与[规范问题摘要](findings-summary.md)；[完整findings](findings.json)为当前规范结论。
2. [覆盖说明](coverage-summary.md)、[来源→能力→规格](source-to-spec-coverage.json)、[131文件→来源](spec-to-source-coverage.json)。300为可交叠范围记录，不是全功能分母；25共享契约单主责。
3. [23项GR3回归](regression-third-23.json)、[旧229/341限定账](regression-legacy-scope.json)、[跨模块整合](junction-review.md)/[JSON](junction-review.json)。
4. [实际执行证据](execution-evidence.json)、[未审/资料/政策限制](limits-and-missing-materials.md)。4次隔离原函数执行；完整宿主/Demo为0。
5. [后续批次建议](proposed-update-batches.json)、[共享文件唯一写者](shared-file-owners.json)。只是任务书准备，尚未启动整改。

完整中文交接正文 `cloud-fourth-update-handoff-prompt.md`、机器manifest `cloud-fourth-update-handoff-manifest.json` 和 `publication-receipt.md/json` 在独立后继提交加入。终局消息提供这些文件的固定远端链接和校验身份；早期报告冻结commit可能不含后继文件，不把相对路径暂缺误认为语义审查未完成。最终发布commit下可直接读取全部文件。

## 审者与取证

[实际进度/任务入口](progress.md)、[机器进度](progress.json)、[模型请求与CLI说明](tasks/runtime-request.md)。父会话真实ID `01a12fc2-e8c0-7e43-a721-ccfe659d75c8`；各启动回执记录真实thread ID/PID/日志。全部请求astra/ultra/default禁Fast已接纳，实际回显UNVERIFIED。

M01–M12的[独立原稿目录](modules/)，[CA裁决](modules/CA/verdicts.json)、[CB裁决](modules/CB/verdicts.json)、[J原证据交界报告](modules/J/report.md)，以及[根整合/去重](counterreview-and-dedup.json)。初审原稿不回写；POST初审P2在规范结论中收窄P3，其余精确化也以根findings为准。来源定位只作审计，不是新引擎的API或类结构。

[baseline.json](baseline.json)/[readiness.md](readiness.md)记录现场观测；[保护快照](evidence/workspace-protection-before.json)和[131身份](evidence/formal-identity-check.json)可复核。源R独立仓库只读，根BMP确实存在，媒体/地图/完整工程和游戏宿主限制明确保留。

[schema说明](schema.md)、[findings schema](findings.schema.json)。正式/source锚点分别相对固定B/R；模块辅助证据相对各artifact_origin，不能把其相对文件名误当根路径。审查辅助脚本/探针仅用于本轮取证，不是生产框架或后续自动运行授权。

阶段性输入清单/取证文件保留生成字节；其中待J、待反证或初审P2等标签不表示终局。当前裁决以根findings、regression、junction、progress及后继publication-receipt为准，不回写已消费输入制造新签名。
