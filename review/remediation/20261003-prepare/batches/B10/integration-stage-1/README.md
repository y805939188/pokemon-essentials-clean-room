# B10-G 实际整合交接

状态 **INTEGRATED_PENDING_ACTUAL，C未接受**。候选3c6365a4ce35c3ef08e6ba53fd81a426ffd026aa的full/B04/B08/B09/B05均PASS_SCOPED，B14有据NOT_AFFECTED；报告与reviewed SHA分开，[六门收据](candidate-gate-receipts.json)已按远端和manifest核验。

13正式文件保持候选精确字节；五原稿保持授权intended_after，正确65/原139和旧227目录行不变。24独立报告原字节复制入本整合树，完整作者/候选包原字节继承。两个公共TSV仅追加7条pending贡献，旧194行及header保持；交接页只加前缀、历史后缀逐字保持。正式接受仍10/21、194贡献，canonical229OPEN/0CLOSED。

[限定逐ID登记](finding-registration.json)、[正式及报告复制身份](formal-copy-identities.json)、[公共差异](public-registration-delta.json)、[实际复审派发](actual-review-request.json)。actual完整SHA/tree由提交推送后的外部ref/FETCH_HEAD交付，无self-SHA回填。全量actual及B04/B08/B09/B05 actual、B14独立actual影响判断均须绑定该SHA；完整未过滤前驱→actual及candidate→actual差异保留。不能用候选PASS/同blob替代实际gate，不能因B14候选NOT_AFFECTED删实际比较。

父以gpt-6.1-sol/ultra/default创建规定独立角色，最多3任务，各自只写派发报告目录。所有required actual gates满足才C接受；随后B11重冻35读8写，B11+B15无计划RW/WW冲突可有限并行，B10/B15此前仍串行。[剩余批次计划](remaining-batches-plan-summary.json)只用原PLAN/冻结合同作依赖和估时说明，不扫描历史日志或扩为全局审计。

G为xhigh父统筹单公共写者；只消费精确独立结论并做Git/文本/身份账务校验，未重判行为。参考、编译/转换/生成/反序列化、历史作者/审者程序、行为向量执行均0，runtime/Demo0，完整source limits及具名未知保留，无main合入/force push。
