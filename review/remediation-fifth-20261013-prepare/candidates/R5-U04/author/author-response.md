# R5-U04 作者候选

七项必修已形成可复现静态候选，均为 **AUTHOR_STATIC_SUPPORTED / 候选待独立复审**。这是作者验收映射，不是独立 PASS、正式接受或 CLOSED。

固定 B5 `9366d9d17aaeac3b4414236468affa650fb3dd27` / tree `594e65edcb192a19110540245fc1663bae2de007`；参考 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只读。任务合同 `22fba7786b0090a1955ce6211315b0036cddfbcd` / tree `21f3484d167d8cab7a288e0204c72f275414d52e`；准备发布 `93524fe5cf396de2bd01f3c5c1e08ba4b874bc68` / tree `4ade8d22d56b7facb46ad5bd8245a027f0d833c6`。语义报告身份保留 `c0ff33024aea424c68d29f9778fe7c8e807d21e8`，报告固定发布 `f49d870c6fd616ab6736754a218a4553b5acac7f` / tree `e5dc6aaf626885666e7d472865563f0c9bfbdf46`。

| 必修 | 候选接收 | 作者逐项状态 |
| --- | --- | --- |
| GR5-JXN-002 | WP40§5.2.3主合同；WP42/WP47-A引用；ERR01–09 | AUTHOR_STATIC_SUPPORTED |
| GR5-M07-001 | WP40§5.2.1失败布尔生产；FH01–06 | AUTHOR_STATIC_SUPPORTED |
| GR5-M07-002 | WP40§5.2.2节拍器计数；MET01–05 | AUTHOR_STATIC_SUPPORTED |
| GR5-M07-003 | WP39§4.4.1共享插入提案、WP41§4.1.1；RANK01–06 | AUTHOR_STATIC_SUPPORTED |
| GR5-M08-001 | WP47-A四原值、WP46两Shadow HP、WP45天气/双侧四屏障；附表/委派同步；RAW01–09/SH01–09 | AUTHOR_STATIC_SUPPORTED |
| GR5-M08-002 | WP47-B§3.2.1鸟嘴加热自身替身边界；BB01–05 | AUTHOR_STATIC_SUPPORTED |
| GR5-M08-003 | WP43§2.1效果缺省与分类回退，WP47-A引用；FB01–06 | AUTHOR_STATIC_SUPPORTED |

所有必修 static/preserve 条件及正常、拒绝、取消、部分提交、消费者同步见 [finding-responses.json](finding-responses.json)。旧向量与准确 owner/scope 回归见 [regression-results.json](regression-results.json)；源/原提出者/独立反证的固定身份与读域见 [source-reading-log.json](source-reading-log.json)。正文只表达行为；证据与变更记录保存在本目录。

仅本 author 目录发生新增；15份非共享正式镜像与1份WP39片段不改工作树正式文件。共享正式落地及公共登记只有R5-I可做，[fragment-manifest.json](fragment-manifest.json) 绑定B5锚点/插入位置/旧正确行为/依赖。[formal-diff.patch](formal-diff.patch) 可在B5临时投影应用并与镜像逐字核对；[tools/validate_candidate.py](tools/validate_candidate.py) 只做静态重建、路径/范围、JSON、链接和完整bytes/SHA256/blob核验，不执行参考或行为模型。candidate manifest 不含自身哈希、也不内嵌自身 commit/tree；固定候选与证据commit/tree由后继读回回执/父任务绑定。

R5-U03 实际所需贡献 **WAIT**；本批独立候选复审、R5-I整合、实际字节复审和唯一登记均待父任务安排。候选不得提前接受/关闭；上游到达后仅核影响字节。独立审者从固定任务入口 `review/remediation-fifth-20261013-prepare/contracts/R5-U04/reviewer-entry.md` 开始，以本候选 manifest、全部产物及冻结证据为输入，只签限定候选字节。

本 update 新增参考执行0、行为模型0、宿主/Demo0；静态期望是DERIVED_VECTOR，机械校验是TOOL_VALIDATION。R4历史隔离4与R5 review隔离4分别保留、未重跑。optional7/no-required7/政策6及M11-005可选方面未纳入必修。真实媒体、宿主诊断成功、默认Demo可达、无界插件/所有组合与未来兼容政策仍受原限制；没有凭候选授予运行PASS。请求gpt-6.1-sol/xhigh/default普速禁Fast；实际模型/参数未回显，记UNVERIFIED，无额度/认证审计。没有merge/push main、删分支、修改参考或Mac，未启动本批审者。
