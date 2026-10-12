# U02 attempt-02 有限独立候选复核

最新候选四项均 **PASS（静态文档充分性）**。attempt-01 的三处必修问题已解决，未发现新的必修delta问题，没有剩余返工。行为和静态案例仍 **NOT_EXECUTED**；本结论不构成actual复审、正式接受或CLOSED。

## 固定输入与范围

- 新候选：`9e3b61aed3c2c9e57ce913ceda02b8cfdcbe028e` / tree `d5410c2d0e1e63edb866efbb1837accdf473d896`，作者分支 `remediation-third-u02-author-20261012`。
- 原候选：`a93bcdf7f374d5296ff5302a6cdd29e9a971a044` / tree `b6202a1926de2e070ff33d4e670a64c707bc712b`。
- 原独立报告：`37f47687cd9a23cdb34d89f4e7128ee0f4f634b2` / tree `e417c1f67ebc084e66efa235dba153215f8de219`，`U02/independent-review/attempt-01/`；六文件身份已绑定，没有修改旧报告。
- 固定合同仍为 `28f321de5b2fee1e209b1945597d7aa6d3277330`；本次继续授权只核三处修订与影响范围，复用未变有效PASS，不重做全局或历史review。
- 参考仍只读使用 `Maruno17/pokemon-essentials` 的 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。必要源段定点复读；原除法覆写搜索、qualified语义及其他未变支持按attempt-01精确身份/前提复用。
- U01接受base `3386b4b579098394012ccde3222938d19b4334b7`；批准WP09 blob `d9a256cbc1054cc3ad190f83231bfdfa564ac4a2`保持原字节。原H/S证据没有替换。
- 原独立角色与作者/唯一整合登记员仍分离。本报告新分支 `remediation-third-u02-independent-attempt02-20261012` 从新候选建立，仅写attempt-02六文件；候选、正式规格、main、参考、历史、公共登记均未修改，无force。

## 三处问题解决证据

以下候选路径都位于 `U02/candidate/deliverables/final-specification-set/`。完整精确路径、行号、原问题对照、静态向量与真实读取范围在 [per-id-verdicts.json](per-id-verdicts.json) 和 [input-snapshot.json](input-snapshot.json)。

| 原独立问题 | 有限复核结论 | 新候选证据与固定参考 |
| --- | --- | --- |
| U02-IR-CAM-001（P2，001） | RESOLVED_AT_CANDIDATE_STATIC_LEVEL | WP16 L60及CAM12/13/15–17 L147–152分轴保留整数向下取整/浮点连续商。参考Game_Map L533–559、448–458及RubyUtilities L400–406；整数初始写入证据仍绑定Game_Map与Game_Player。 |
| U02-IR-CAM-002（P3，001） | RESOLVED_AT_CANDIDATE_STATIC_LEVEL | WP16 L62、CAM14/18 L149/153将镜头任务绑定买入/无全局背包卖出的共用画面；全局背包卖出入口/出口均不发该任务，子场景非镜头等待保留。参考PokeMart L242–244、299–320、345–362。 |
| U02-IR-GR3-M03-002-R01（P2，002） | RESOLVED_AT_CANDIDATE_STATIC_LEVEL | WP14 L43、DQ06 L448分开清待播种子/重播与抽样推进；空起点失败后方向/房间/装饰抽样未到，没有正推进或固定宿主零消费保证。参考RandomDungeons L137–177、428–462；密度0与写图顺序另定点核L862–883、916–940、1063–1076。 |

居中数值的有限静态验收一致：整数(0,0)→目标(10,8)，512×384屏幕，终点(384,384)、各0.6秒；0.5秒位置(320,320)仍在途。浮点(0.0,0.0)终点(320,320)、各0.5秒。混合轴终点(384,320)、时长0.6/0.5秒。负整数(−961,−705)的商为(−1,−1)，终点(−833,−577)、0.2秒；同值浮点终点(−960,−704)、0.0015625秒。整数/浮点边缘未钳请求分列为(−896,−640)/(−960,−704)，两者都钳为0。已居中判定使用同一中心规则，没有恢复无条件半格公式或旧任务取消承诺；校验与包装等待门保持。

共用商店画面仍右/左5格、速度5、名义0.5秒且包装等待；背包卖出无这组镜头任务/0.5秒镜头等待，同时没有把其独立演出等待否认。空起点与密度0现在各保具体首次失败的实际随机前缀；原B图未写、旧暂存及查询未驻留保留。精确宿主版本继续UNVERIFIED，不需运行或修改参考证明这次收窄。

这些“解决”仅指独立候选文档问题的处置，未把原canonical finding改为正式CLOSED，也未由作者自登记接受。

## 最新逐项裁决与PASS复用

| Canonical finding | 最新候选裁决 | 依据 |
| --- | --- | --- |
| GR3-M03-001 | PASS | 原速度/方向/双轴/钳边/203与包装/校验/材料限定的有效支持按未变条款复用；整数/浮点数学及商店消费者两处本次重新定点复核。 |
| GR3-M03-002 | PASS | 原驻留/临时/重复查询、种子/暂存/非地牢和失败阶段有效支持按未变条款复用；WP14失败表与DQ06的随机消费修订本次重新复核。 |
| GR3-M03-003 | PASS | WP12、WP13事件等正文完整blob未变；CS01–13及公共前提逐行原字节未变，复用原四项验收PASS。 |
| GR3-M03-004 | PASS | WP11、WP13事件等正文完整blob未变；MR01–13及公共前提逐行原字节未变，复用原五项验收PASS。 |

003/004共26案例的复用只覆盖原条款/案例和前提；因同一测试目录含DQ06的新字节，**不把旧PASS签名转到新的测试整文件blob**。001/002原失败验收项也没有整项转签，采用未变支持＋当前三修订的组合证据。没有重新审229、341或其他领域。

## 独立delta与交付核验

独立比较新旧候选确认**10个允许路径**改变：author-report、author-self-check、candidate-identities、candidate.patch、registration-proposal、traceability-proposal，以及四个候选载体（WP14、WP16、两个世界测试目录）。另四候选完整blob保持原样。八候选base/new完整blob、SHA256和bytes与声明相符；正式、公共、其他批及原独立报告没有变化。

原49条GR3行仅CAM12/13/14、DQ06四行修订，其余45行字节不变；新增CAM15–18四行，共**53个唯一ID**，全部逐行NOT_EXECUTED。两目录原366＋92＝**458条**旧行原字节及顺序保留。003/004的正文与26案例未变声明独立成立。

十二qualified控制的**93次观察点**仍匹配冻结base/旧候选/新候选，去重为**87个(path,case)**；冻结有效文件身份未变，原12控制/33个贡献tuple与有限junction证据按既有qualified范围复用，没有重读全部source/raw/ACT。旧229 CLOSED与341 scoped限制不变；G5仅导航、M02-003不重开、U08未启动。

对精确新候选SHA从远端fetch后，**17个交付文件完整读回字节/blob/SHA256均匹配**。完整patch只目标化八个世界正式对应路径；在临时副本静态check/apply后，八结果完整字节等于候选。作者自检仅是待核实材料，以上结果由本次独立重算取得，不证明行为执行成功。

WP09/kernel两提案完整原字节不变，复用attempt-01有界提案PASS。traceability/registration的delta只增加三处修订、53案例导航及等待原reviewer有限复核阶段，旧003/004 PASS仍按原scope引用，未扩写权限、公共计数、正式接受或整文件签名；两提案的映射/角色范围亦PASS。未来实际应用仍需新actual身份、公共delta与独立actual复审，U01旧签名不能覆盖新WP09字节。

## 限制与发布

无剩余必修或交付阻塞。所有行为/静态案例NOT_EXECUTED；未执行Ruby、游戏、生成器、模拟、编译器、转换器、存档反序列化器或Demo。真实地图、事件、素材、存档样本、宿主画面和默认Demo可达性仍MISSING_MATERIAL；源异常未来兼容为USER_DECISION，不能据候选PASS补签运行或关闭。

模型请求沿固定合同 `gpt-6.1-sol/ultra/default` 接纳，权威model/effort/tier回显均UNVERIFIED；未用隐藏CLI或额度审计。正式接受、actual复审及最终CLOSED继续由独立后续步骤/唯一登记员处理，本报告没有预签。

本目录六文件为input-snapshot.json、report.md、findings.json（无新必修，空数组）、per-id-verdicts.json、output-identities.json、model-request-receipt.json。output-identities绑定其余五完整身份；发布commit/tree及其自身blob由外部正常提交、推送和远端六文件完整读回绑定，避免递归self-SHA。
