# B08 完整作者候选交接

本轮已从 WIP `d6367692610c83fd24bd1ab8d2ab0cfa6757314d` 恢复，执行基线保持 `759eee80ce7856570fde2de12d5dcf98ce7e6017`，分支保持 `remediation/20261003-prepare/batch-B08`，RUN_ID 保持 `20261003-prepare`。原预算暂停记录是不可变历史；当前额度 UNKNOWN，既有 Standard/default 服务档位及累计30,000 Credits上限未变，不声明额度恢复，未登录或读取认证材料。

**作者修订、四原稿同步、静态目录与批次证据已完成，等待独立复审。** 本目录不是独立 review、批准或关闭记录。完整候选40位 SHA 与普通 push/主repo回读在作者最终回执提供；不把提交自身的 SHA 写成自指字段。

## 原稿授权与应用

父任务明确批准 WIP 中 v2 原样补丁，SHA256 `05b75bcafcb1fd9359e9a35e935e8b7cbb7dd038a0f3349a1172d1fe3ba88f25`，仅限提案四路径／枚举条款／对应 B08 finding。应用前四原稿仍匹配冻结前身份，应用后四份完整 blob／SHA256／bytes 均与拟后身份完全一致。没有扩大条款；范围批准不代表正确性批准，也不转移历史 review。

- [父任务授权与前置核验](parent-authorization-and-preapply.json)
- [实际应用与整文件锁记录](original-application.json)
- [四原稿完整应用差分](authorized-originals-WIP-to-candidate.diff)

`author-stage-1`全部25文件保持 WIP 字节，包括 v1/v2 未批准提案、暂停记录、自检和原先待批准状态。stage2追加当前授权/应用及修订交接，不改写旧提案状态。历史 author/review/acceptance 及公共登记均不变。准备/批准/应用次序仍仅标为 `AUTHOR_SELF_REPORT_ONLY`，哈希和时间戳不冒充独立历史见证。

## 十二份内容输出与自检

[output-identities.json](output-identities.json)列出八正式输出＋四获准原稿的基线／WIP／候选完整 blob、SHA256、bytes。[全部内容差分](all-output-predecessor-to-candidate.diff)覆盖这十二路径。它是完整无过滤 Git 差分的补充；复审必须另读基线→完整候选及 WIP→完整候选的**无路径过滤**差分，包含两阶段全部批次管理/证据文件。

[document-self-check.json](document-self-check.json)记录作者自检：17贡献／9主责、精确 v2 应用、WP34 原稿和正文严格只读、旧目录 ID 顺序/反例/反向对照保留、其他责任批完整章节字节保持、15新增静态行与5修订旧行，以及原稿/净化正文/静态目录的具名行为关系。恢复后只额外去掉 EG-20 和 RM33 前截断表格的空行，行文字未改；这两目录重新冻结并纳入 R-B07 影响。BR25 原无结尾换行，追加 BR26 的必要换行继续单列。

十二份内容输出 `git diff --check` 通过。无过滤 repository diff 的空白检查会把已保存 unified-diff/patch 中必要的单空格“空上下文行”标为 trailing whitespace；这些证据保留精确字节，相关告警逐项分类，不能把该完整检查写成无条件 PASS。新增静态行均属于连续有表头/分隔行的 Markdown 表格。JSON/字节/文档检查没有运行行为向量。

## 控制、输入与阅读范围

[17贡献映射](finding-contribution-map.json)提供原 ID→正文→附表/数据→静态行/反向对照→授权应用→登记建议。完整原 finding 与 approved acceptance 对象仍在 `author-stage-1/fixed-contribution-controls.json`，绑定精确 WIP，规范化哈希与基线合同均相符；全部 current_qualifications、effective_case_constraints、根项、二审、扩展裁决及历史来源原文保留。本轮只完成 B08 分配贡献，不抹去共同根其他责任。

[输入与当前输出重冻结](input-freeze-and-current-output-refreeze.json)：79计划输入仍按77基线／2原报告绑定；79中10项现在改变（6正式＋4原稿），另2正式目录来自合同写入/补充输入身份。十二输出都给当前精确身份；其余输入和额外72身份保持。身份核验与导航不冒充79项全部全文语义读取。

[参考读取日志](source-reading-log.json)继承 WIP 全部具名限制与此前实际 R-B07/受影响 B04 阅读限制，追加恢复后的实际重读范围。恢复容器另行建立的独立参考 clone `/workspace/reference-B08-resume`为精确 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`且干净，只读。未执行游戏、Ruby、编译、转换、生成、反序列化、行为模拟、求解器、媒体或历史 verifier；runtime0／Demo链0／执行向量0。U01–U10／G01–G12／AX01–AX20及未读配置、二进制、地图/事件、素材、宿主、容量、插件、动态/旧入口限制完整保留。没有源码复制、逐行伪码、语言翻译或新框架设计。

## 五个 B07 反向读者与待复审事项

[dependency-and-reverse-impact.json](dependency-and-reverse-impact.json)给五路径前/后完整身份、WIP身份、单路径完整差分、B07条款/用例/调用与数据前提及未触及责任行：

1. 正文 `creature-rpg/wp36-wild-encounters-and-modifiers.md`。
2. 目录 `creature-rpg-wp27-28-29-30-33.md`。
3. 目录 `creature-rpg-wp35-36-57-64-68.md`。
4. 目录 `pokemon-rules-wp19-21-22-23-34.md`。
5. 目录 `pokemon-rules-wp31-32-37-38.md`。

旧 B07 批准保留为历史，不能自动转移。下一关由父任务安排：独立 gpt-6.1-sol Ultra/Standard R-B08 对完整候选17/9及全部控制复审，另行独立受影响 R-B07 Ultra/Standard 候选复审；作者不担任 reviewer。

B04 WP15–17及WP28/WP30等当前消费者保持字节不变，作者未识别新增资源/音频/文字/数量条款影响；独立 R-B07及父任务仍需决定是否触发新增 B04 门。如影响成立，必须另有独立 B04 候选及actual Ultra。B12大会完整修订、B19编辑器/缓存、B20 WP77数学引用、B16专业 UI、B09伙伴接收/还原等仍归原责任批。

A-REG 普通actual integration之后，同样需精确actual的 R-B08及独立受影响 R-B07 Ultra、任何必要 B04门，再由父C验收。本文不 dispatch 下游、不 merge main、不关闭 ID。[A-REG-proposals.json](A-REG-proposals.json)仅为逐ID本批登记建议；公共写入0，OPEN229／CLOSED0保持。

请求配置继续 gpt-6.1-sol/xhigh/Standard，review Ultra/Standard；无可信有效回显，仍为 `UNVERIFIED`，按用户方案A不追加认证询问。概要机读交接见 [candidate-handoff.json](candidate-handoff.json)。
