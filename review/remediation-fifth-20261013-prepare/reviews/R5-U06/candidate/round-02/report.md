# R5-U06 v2 独立候选有限复验 round-02

固定 v2 候选 **18项全部 PASS_SCOPED_CANDIDATE**。145条验收通过，其中**仅3条是本轮有限复验新签署，142条复用原未变范围签名**；未重审其余16项或扩大旧scope。候选必修返修0；actual、正式接受、CLOSED均未签。U02、U03、U04、U05贡献门继续 **WAIT**，实际字节整合/验收及U08/唯一接受回执仍未到。

同原独立审者真实任务 `01a1352f-333a-77a9-bf84-d250e499e00c`，原签名 `1ed7f3c07773fdeae946da7c04ef7fc93d5a90ef` / tree `374c53054eea8eeadd66f8c0e6b10fda6a425b6a`。原 round-01 保持冻结；本轮只写用户明确授权的 round-02 六份review载荷，原冻结入口的 round-01输出位置据此定向扩展，未扩张18项业务范围或改作者/正式公共台账。

候选 `5ab3af08f9159a37d416241f82f59e4c0390670b` / tree `ed0316dd2909253442a7eab8567d15b62f8f4460`；证据 `b3b5d74c19aa4cb7c4b4623731c8454a2b5b56b0` / tree `1fe69168ce67e13e99ce6cf84c2f1699b0a50c73`。固定合同 `22fba7786b0090a1955ce6211315b0036cddfbcd`、B5 `9366d9d17aaeac3b4414236468affa650fb3dd27`、只读R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`均保持。入口 author/revision-v2.json 作为待核声明，裁决来自实际Git差异、固定源、接收字节和独立重放。

| ID | v2限定候选 | 验收 | 本轮新签署 | actual/接受/关闭 |
| --- | --- | --- | --- | --- |
| GR5-M10-001 | PASS | 9/9 | 142未变签名中的本项 | WAIT |
| GR5-M10-002 | PASS | 7/7 | 142未变签名中的本项 | WAIT |
| GR5-M10-003 | PASS | 7/7 | GR5-M10-003/C03 | WAIT |
| GR5-M10-004 | PASS | 6/6 | 142未变签名中的本项 | WAIT |
| GR5-M10-005 | PASS | 9/9 | 142未变签名中的本项 | WAIT |
| GR5-M10-006 | PASS | 6/6 | 142未变签名中的本项 | WAIT |
| GR5-M10-007 | PASS | 8/8 | 142未变签名中的本项 | WAIT |
| GR5-M10-008 | PASS | 7/7 | 142未变签名中的本项 | WAIT |
| GR5-M10-009 | PASS | 7/7 | 142未变签名中的本项 | WAIT |
| GR5-M10-010 | PASS | 7/7 | 142未变签名中的本项 | WAIT |
| GR5-M10-011 | PASS | 9/9 | GR5-M10-011/C01, GR5-M10-011/C04 | WAIT |
| GR5-M10-012 | PASS | 8/8 | 142未变签名中的本项 | WAIT |
| GR5-M10-013 | PASS | 10/10 | 142未变签名中的本项 | WAIT |
| GR5-M11-001 | PASS | 6/6 | 142未变签名中的本项 | WAIT |
| GR5-M11-002 | PASS | 8/8 | 142未变签名中的本项 | WAIT |
| GR5-M11-003 | PASS | 9/9 | 142未变签名中的本项 | WAIT |
| GR5-M11-004 | PASS | 9/9 | 142未变签名中的本项 | WAIT |
| GR5-M11-005 | PASS | 13/13 | 142未变签名中的本项 | WAIT |

- **GR5-M10-003/C03 PASS**：D/E前提现在明确B为有效字符串、T存在时为有效字符串/不存在为null，原刺激的T=null不再与前提矛盾。刺激/预期逻辑请求均未变。主审和原分组审者直接复核固定R的可选T门及最终命名：D请求B_bg/B_message/B_base0/B_base1；E仅B_night_base0命中时共用该平台前缀，bg/message各自保留基础。static-vectors、E040、共享fragment、fragment-manifest、formal-diff.patch、finding回应和revision入口同步；不推实际加载/像素结果。
- **GR5-M10-011/C01、C04 PASS**：仅将C向量与正文的.475采样改成内部点.48，.725保留。固定R创建起点、2/20帧时长及非负浮点时差截取整数的源锚保持。独立算术得到.48/.725的区间号1/3；128×32/4得到32×32，只验证逻辑切片/索引。原.475反例仍为0，不再作为帧1向量。WP15镜像、共享测试提案、edits、fragment-manifest、patch、static-vectors、finding回应及manifest完整身份一致。未执行参考函数、行为模型或宿主。

独立差异/身份核查：142个author criterion记录全同；16个其他finding完整记录全同；43编辑中41个全同，仅E021/E040分别包含授权的一处采样替换和两行缺T前提/一处采样替换；106向量中103个记录全同，3个改动向量的预期均未变。24拟目标中22个完整blob相同，只有WP15和engine-overworld共享测试目录拟字节变化。15共享片段中14全同，变化的E040片段及10个共享目标保持R5-I/WAIT，不实际写共享正式文件。

从固定B5唯一完整锚重建24目标/43编辑，14直接镜像核同；独立零上下文git apply重放与完整proposed bytes/SHA256/blob一致。v2候选13个修改/新增载荷、后继证据1个新增载荷均读取完整Git对象字节并核身份，其余未变身份复用；manifest对应42个候选/证据载荷全部核对。候选与证据tree逐一等于给定值，正式131文件tree仍为 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。

必要回归：原303不同path/line旧行及前轮独立枚举1418个旧ID物理行，均在v2重放中逐行原字节保留。旧regression-results和consumer-consistency作者文件整份未变；35精确旧history/11共享合同的原固定身份与限定scope签名复用，未重开或转签旧接受/关闭。142签名的每条原commit/path/pointer、规范记录hash以及当前scope复用依据在criterion-results与regression-results中逐一列明。共享测试整份blob改变不等于扩大其它consumer范围：差异只限已核三处，其它向量、期望和提交阶段不变。非阻塞WP63措辞未采用，未改变已通过的M11-005字节。

执行计数分列：历史R4隔离参考记录4，历史R5review隔离参考记录4；round-01和本round-02新增参考/行为模型/宿主/Demo执行均0。106静态向量仍为DERIVED_VECTOR / NOT_EXECUTED。差异、字节、Git、patch和数学检查仅TOOL_VALIDATION。旧R5-REF-004两进程/五观察的资格未改变，本次不复跑、不借用。optional7、no-required7、政策6、M11-005内optional和冻结13限制继续隔离。

请求gpt-6.1-sol / ultra / default / 普速 / 禁Fast；实际模型、推理、服务、速度回显均UNVERIFIED，不审计认证/额度。无新增候选阻塞；上游WAIT及实际字节关闭条件保留。未改正式规格、作者字节/台账、reference、冻结历史或main，未碰Mac，未增批次或重开全局review。

逐条签署与复用依据见 [criterion-results.json](criterion-results.json)，取证见 [source-reading-log.json](source-reading-log.json)，必要回归见 [regression-results.json](regression-results.json)，独立重放/算术和普通推送读回回执见 [independent-validation.json](independent-validation.json)，完整范围/文件身份见 [review-manifest.json](review-manifest.json)。[原round-01冻结签名](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1ed7f3c07773fdeae946da7c04ef7fc93d5a90ef/review/remediation-fifth-20261013-prepare/reviews/R5-U06/candidate/round-01/report.md)保持；本轮最终commit/tree由交接绑定，避免自哈希递归。

发布通道：shell Git推送返回认证不可用，改用已连接GitHub的Git-data接口创建独立分支并做非强制提交/更新。该通道保留普通快进发布语义；不强推、不移动main。完整载荷仍逐份远端读回核对。
