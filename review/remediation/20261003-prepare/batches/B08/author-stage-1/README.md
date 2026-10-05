# B08 作者交接：正式输出已修订，原稿授权待定

RUN_ID：20261003-prepare。独立作者分支：`remediation/20261003-prepare/batch-B08`；精确父基线：`759eee80ce7856570fde2de12d5dcf98ce7e6017`。本目录是 A-B08 自检与交接材料，不是独立复审、批准或规范 ID 关闭记录。

本次冻结是**正式八输出与证据的可审阅草案**。四份必要原稿同步尚无父任务明确路径/条款批准，因此原稿保持基线字节，不能声明 B08 已全部完成或满足原稿/净化稿一致性验收。当前完整候选 40 位 SHA、普通 push 和回读结果在作者最终交接及外部提交回执提供，避免在提交内部要求自指 SHA。

## 精确输入与控制

- [input-freeze.json](input-freeze.json)：79 项计划输入（77 绑定本执行基线，2 绑定原报告 `93e10babe0b9c9ef8b3f5277754541b447beeeb4`），全部 blob／SHA256／bytes 匹配合同。
- [additional-input-identities.json](additional-input-identities.json)：固定计划 7 项、额外 B07 输出 11 项、不可变历史证据 52 项、当前管理 2 项的身份。身份核验不冒充全文语义阅读。
- [fixed-contribution-controls.json](fixed-contribution-controls.json)：17 个固定贡献的原 findings 完整对象与批准 acceptance 完整对象；全部 current_qualifications、effective_case_constraints、根项、反例、二审和扩展裁决原文保留，规范化哈希已核对。历史 raw 或 Max 字样不覆盖当前裁决和 C 合同的 xhigh 纠正。
- [project-bounded-reading.json](project-bounded-reading.json) 与 [source-reading-log.json](source-reading-log.json)：项目有界读取导航及自己容器参考文本读取范围。不得把搜索导航、whole-file 哈希或局部重读升级为全部 79 项全文语义复核。

## 正式修订与关系

[贡献映射](finding-contribution-map.json)逐项列出 17 贡献／9 主责的正文、附表或数据、静态行、反向对照、原稿门及登记建议。正式差分为 [formal-predecessor-to-candidate.diff](formal-predecessor-to-candidate.diff)，精确输出身份为 [output-identities.json](output-identities.json)。主要变化如下：

| 贡献 | 正文及静态关系 |
| --- | --- |
| A052 | WP33 正确先行门保持；DC-08 限定 Ditto 前提，BR26 分离兼容周期与直接生成/领取。WP34 正文、既有数据映射严格只读。 |
| A053 | WP35 区分核心无显式形态写入与演出动态查询；EG-13、EG-20 保留 DEERLING 月2/月1/强制形态对照及图鉴提交次序。 |
| 003 | WP36 查询/枚举反例与入口差异保留；WP37 改为领域状态与邻接关系，漫游先于雷达及兼容失败反例保留。组织证明见 [审计](source-to-behavior-audit.json)，全部共同根与其他扩展仍待各责任批。 |
| A034／C007／C084／C085 | WP37 完整 KYOGRE 四键邻接、伙伴启动后段取消、临时/持续首次与复遇生成、通知48与参战52、双存在门；RM33–37，原 RM01–32 不改。 |
| C003／B026 | EN-01/15/16 修正阶段与随机前提；EN-32 保留伙伴先行导致普通2v2、绕开单敌大会覆盖/预算的反例。WP53 完整修订仍归 B12。 |
| C004／C005／C080／C096 | WP36 专用解析、重复类型槽替换/概率继承、拒绝阶段、登记/文件/当前地图快照，以及整数校验/同值早退/异值装载；EN-26/27/29/30。 |
| C079／C081／C082／C083 | 精确 HUSTLE/PRESSURE/VITALSPIRIT 身份及 GUTS 负对照、31位回绕、contest/冲浪机会与类型分层、全部队伍人口标准差与平衡级公式；EN-25/28/01/31。WP77 数学引用建议归 B20。 |

[document-self-check.json](document-self-check.json)确认 8 个正式路径、17/9 控制、15 新静态行、5 修订旧行、全部旧 ID 顺序与其他责任批完整章节字节保留。BR25 原文件没有结尾换行，追加 BR26 所需换行单列记录，BR25 行文字保持。所有数值为静态合同与手工对照，未执行向量程序。

## 四原稿必要改动：精确批准待定

当前有效提案：[original-sync-request-v2.json](original-sync-request-v2.json) 和 [original-sync-prepared-v2.patch](original-sync-prepared-v2.patch)，补丁 SHA256 为 `05b75bcafcb1fd9359e9a35e935e8b7cbb7dd038a0f3349a1172d1fe3ba88f25`。四条路径、条款、分配 ID、原稿前/拟后完整字节身份均已给出。仅做 `git apply --check`，没有应用。v1 保留为未批准提案历史，不转移批准。

必要性证据：WP33 原 DC08 越过 Shadow/Undiscovered；WP35 原不改形态全程保证被默认 DEERLING 月2场景查询推翻；WP36 原无条件重装、31位钳制、能力译名与缺失解析/缓存/数学合同不满足有效 C 项；WP37 原仅四键无邻接、遗漏临时生成及条目关联门、通知来源过强。具体最低修订与具名前提以固定完整控制和 v2 精确差分为准。正确原条款与历史审查材料保持。

合同明确要求先完成有界读取和可审阅差分，再获得父任务对 B08 精确路径/条款批准；B07 六原稿旧授权不能使用。准备/写入次序只能标为 `AUTHOR_SELF_REPORT_ONLY`，时间戳和哈希不证明历史次序。批准收到之前四原稿不写；批准之后仅应用对应完整补丁并重新冻结、检查和交接。

## 受影响复审与登记

[dependency-and-reverse-impact.json](dependency-and-reverse-impact.json)提供五个改变 B07 反向读者的完整前/后 blob／SHA256／bytes、单路径完整差分、B07 条款/静态行和不变消费者身份。79 个计划输入中的 6 项改变，另 2 个改变的正式输入分别记入写入/补充输入；所有八输出身份均已冻结。R-B07 旧批准只保留为历史，不能转移。

独立 R-B08 应在原稿门解决后核全部 17/9 与完整无过滤父→候选差分；另需独立受影响 R-B07 的候选 Ultra/Standard。A-REG 普通 actual integration 后，两项同样须绑定精确 actual SHA 与完整差分作受影响 Ultra 复审，再由父 C 验收。B04 WP15–17 输入保持不变，作者未识别新增条款影响，独立 R-B07／父任务仍须判断；如影响成立，保留独立 B04 候选/actual 门。本作者没有担任独立 reviewer，也没有派发下游任务。

[A-REG-proposals.json](A-REG-proposals.json)仅为本批登记建议；公共计划/导航/ledger 不写，OPEN229／CLOSED0 保持。B16 A048/C003/D023、B09 B013/CP20 及各共同根其他责任贡献均保留。

## 运行与边界

自己容器独立 clone 的参考位于 `/workspace/reference-B08`，HEAD 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，后续只读、工作树干净；未改参考或 ignore，未将源码跟踪进主 repo，未向参考 push。主工作区为 `/workspace/batch-B08`，只有单作者整文件责任，无派生/并行写其他范围。四共享目录的原字节身份与锁定范围见 [scope-and-locks.json](scope-and-locks.json)；无外部租约服务回执，不声称平台锁已阻断其他容器。

请求模型 gpt-6.1-sol、xhigh、Standard；review 请求 Ultra。无可信有效配置回显，保留 `UNVERIFIED`；按用户方案 A 不增加认证询问。U01–U10／G01–G12／AX01–AX20、全部具名未读和素材/配置/插件限制保留；游戏／Ruby／编译／转换／生成／反序列化／行为模拟／历史 verifier 均未运行，runtime0／Demo链0／执行向量0。自己的 Git／哈希／JSON／文档字节核对不作为运行行为证据。

## 安全暂停检查点

父任务因预算监测阻塞要求立即暂停；额度 UNKNOWN，不等于0或超限。当前修改仅保存为 WIP，不是已复审候选。详见 [pause-checkpoint.json](pause-checkpoint.json) 的真实未提交状态、剩余事项和恢复步骤。无父任务明确恢复指令前不继续修订/审查；四原稿仍待 v2 精确批准。未重新登录、读取认证或更换账户。
