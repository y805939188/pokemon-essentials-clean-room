# U02 四项世界合同作者交付

四项 `GR3-M03-001` 至 `004` 已形成八份完整候选镜像、53条逐行 `NOT_EXECUTED` 静态向量及有界共享提案。独立报告 `37f47687cd9a23cdb34d89f4e7128ee0f4f634b2` 对003/004已有PASS；本次只修001/002关联的三个必修点，等待原reviewer有限复核。此为作者交付与自检，不是独立候选判定、实际整合、正式接受或问题关闭；没有签发PASS。父任务须冻结本报告所在修订作者commit/tree，供原独立reviewer有限复核；003/004只在未变条款/案例范围复用已有独立结论。

## 固定输入与工作边界

- 派发：`28f321de5b2fee1e209b1945597d7aa6d3277330` / tree `36748eaaf0d90bf13871281aadc06f0e91ee8f58`。作者分支 `remediation-third-u02-author-20261012`，独立工作树 `/workspace/pokemon-essentials-u02-author`；没有切换共享checkout的分支。
- 原交接H：`d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65` / tree `c8a523150d75c8d1bede346857263ddd00ef0035`；原缺口spec S身份保留在冻结findings，未以已更新WP09替换历史证据。
- U01接受/交接：`3386b4b579098394012ccde3222938d19b4334b7` / tree `f4ce7e8144d4ef4fa637e3fa7a311d80caf8c9f1`；批准WP09 blob `d9a256cbc1054cc3ad190f83231bfdfa564ac4a2`、15963 bytes、SHA256 `d38c2063d8a74531969e6e59df23f0fe6c75123a0f801c7b646fb4efdc1c95f8`。派发中的当前WP09仍为同字节，U01依赖已满足，不等待U03。
- 参考：只读获取 `Maruno17/pokemon-essentials` 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，本环境路径 `/workspace/pokemon-essentials-reference-u02`。该新环境没有预置参考；仅精确fetch/checkout和读文本，未写源文件、未用浮动分支。
- 已读根AGENTS与U02目录全部派发、findings、验收、候选路径、依赖、读写边界、冻结输入、回归及交界材料；对大型配套JSON整文件解析/身份核验并使用完整有效qualified字段、M03局部投影及精确贡献条款/案例，未重复全局review或全量历史raw/ACT。完整canonical四对象的前提、正常/失败/反例、消费者、unknown均未改写。
- 作者请求 `gpt-6.1-sol/xhigh/default`；会话没有权威模型/effort/tier回显，记录 `UNVERIFIED`，未调用隐藏CLI或审后台额度。独立review请求仍为 `gpt-6.1-sol/ultra/default`，作者没有启动或冒充独立reviewer。

## 八个完整候选与逐项映射

候选根：`review/remediation-third-20261012-prepare/U02/candidate/`。全部从当前固定派发正式文件完整复制；与接受base八份字节一致后才有限修订，不用摘录替代整份。八个精确路径和base/new完整blob、SHA256、bytes见 [candidate-identities.json](candidate-identities.json)。

| 候选路径（相对候选根） | 修订范围 |
| --- | --- |
| `deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md` | §3.1.1临时查询；§4读档行；§6.1–6.2记录清空/恢复/失败前缀 |
| `deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md` | §4.3末端按键与早先系统跳过消费者的精确交界 |
| `deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md` | §3.3实例/记录；§4.3严格注释跳过与重新启动 |
| `deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md` | 203行补镜头输入数学/钳边导航与包装差异 |
| `deliverables/final-specification-set/engine-overworld/wp14-random-dungeons.md` | §3.1/§3.1.1临时查询和阶段前缀；§7默认启用未知 |
| `deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md` | §3.1.1镜头方向/双轴计时/钳边/居中/包装 |
| `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` | 追加DQ09、CS13、MR13共35行，全逐行NOT_EXECUTED |
| `deliverables/final-specification-set/test-catalog/engine-overworld-wp16.md` | 追加CAM18共18行，全逐行NOT_EXECUTED |

| finding / 能力 / 新交界 | 正文合同与可核对案例 |
| --- | --- |
| `GR3-M03-001` / `M03-C04` / N07 | WP16§3.1.1与203。CAM01速度1–6/半程/终点；CAM02–05合法方向/无效/双轴各自结束；CAM06–08SnapEdges正常/小地图/钳边仍按原时间结束；CAM09–11事件已有等待、新发即继续、脚本等待及速度0包装即时（低层0不特判）；CAM12–13整数中心/校验/整数与浮点边缘请求；CAM15–17浮点、混合轴、负整数；CAM14共用画面与CAM18背包卖出路径对照及缺资源限制。 |
| `GR3-M03-002` / `M03-C17` / N04 | WP11§3.1.1、WP14§3.1.1。DQ01–02未驻留/重复查询、清种子/重播随机/成功写暂存但不切图/排队；DQ03驻留反例；DQ04非地牢建立反例；DQ05合法连接预检查及一次可多次临时取图；DQ06构造前/构造/生成阶段；DQ07事件摆放异常；DQ08仅玩家失败静默前缀；DQ09成功后后继通知失败。旧单次生成失败范围保留。 |
| `GR3-M03-003` / `M03-C15` / N06 | WP13§4.3、WP12§4.3末段。CS01–03严格108/408与A假/真；CS04词法/非注释反例；CS05–06输入/未运行/事件缺失/失联；CS07–08空值/空数组、长度启动门；CS09页刷新清启动与后续执行条件；CS10阶段中断；CS11–12正常同轮末端可达/消息运动/检测链和优先级对照；CS13迷你系统更新。没有独占输入或必执行A页承诺。 |
| `GR3-M03-004` / `M03-C47` / N05 | WP11§6.1–6.2、WP13§3.3。MR01–03普通两分支进入清记录→地图更新→辅助及同ID重建离开/非重建只进入；MR04–08条件剩余记录异图同IDthrough真、假值不清、缺事件失败/同图跳过；MR09前项保留；MR10–11通知/图更新中断与明确新记录；MR12–13实例消去与记录/快照写入分层。已加载实例可保留不等于已清记录再次恢复。 |

[author-self-check.json](author-self-check.json)逐ID逐验收项绑定条款/案例、canonical前提/反例、相关qualified控制与unknown；独立判定字段为空、接受与CLOSED均为false。

## 必要检查及证据边界

完成的是文本、结构和Git字节检查，结果记录为MATCH/SUCCESS，不能作为行为PASS：

- 初版已完成39份固定输入核验（本次按原身份复用）：H核心11份、当前正式/批准内核16份、固定参考12份，逐份commit/path/blob/SHA256/bytes一致；额外定点消费者的三个参考文件身份另记。没有运行参考。
- 八份完整镜像的base/new身份全部登记；UTF-8、LF、末尾换行、无尾空白及新增源码形态行检查完成，未加入引擎代码/API或Ruby翻译。
- 两测试候选的458条原案例行逐字节保留，53条新增ID唯一、全部逐行 `NOT_EXECUTED`；十二个qualified控制在世界候选中的93个冻结案例行hash观察点仍一致（重复观察点不当独立能力计数）。原229闭合、341 scoped贡献及其其他owner/宿主/资源/未知限定原样保留，旧PASS不转移到新候选。
- `candidate.patch`仅作用于八个正式世界对应路径。只在 `/tmp/u02-patch-byte-check` 的八文件副本运行 `git apply --check` 和实际apply，所得八份字节全部等于候选；没有修改正式正文。初版索引精确17路径allowlist核验及 `git diff --cached --check`（排除patch传输文件）均完成，无正式/公共/其他批/独立review目录变更。标准unified patch空白上下文的单空格是语法前缀，整份新增文件检查将它报作尾空白；patch正文另以 `git apply --check --whitespace=error`、实际apply及完整候选字节核验通过。提交推送后精确fetch回读。
- 有限交界为G2-1/3/5/6/8、G7-1、CHAIN-2与新增N04–07；时钟/步进、天气同型保持7/连接后写20、地牢失败顺序、预读/选项映射、对角和门跟随、通用转场大小写/扩展名等原条款未被本次替换。G5仅未变导航，IHC排除不重新引入；M02-003不重开，U08不启动。

相关原控制ID：C003、C007、C036、C037、C039、C044、C045、C047、C049、C051、C053、C069，均带前缀 `GIR-FD82-`。局部条款/历史贡献是有界支持，不据本作者检查给混合控制/其它owner签完整判定。

未执行：游戏、Ruby、编译器、转换器、反序列化器、Demo、生成器、模拟器以及任何行为/静态案例。只用Git读对象/差异及Python处理文本、JSON元数据和hash，没有执行这些向量或参考代码。真实地图、事件、素材、存档样本、宿主画面与默认Demo可达性继续 `MISSING_MATERIAL`；暂时查询副作用和异图through门的未来兼容政策继续 `USER_DECISION`，不阻塞静态事实补文。

## 共享提案与独立复审入口

WP09正文/两内核目录、Feature Matrix、traceability、公共台账都未写入。提案只在允许附属文件：

- [wp09-proposal.json](wp09-proposal.json)：以批准d9 blob为prior，对§3.2/§4.1提出世界字段导航及正常清记录链投影。
- [kernel-test-proposal.json](kernel-test-proposal.json)：仅给已接受WP05–10目录提出两行读档正常/失败投影，保留SV04/SV06与通知错误合同；另一内核目录无需改。条件异图through仍留在世界辅助案例，不冒充默认读档路径。
- [traceability-proposal.json](traceability-proposal.json)、[registration-proposal.json](registration-proposal.json)：四项和N04–07映射/阶段登记建议；没有改接受计数或关闭问题。

父任务下一入口为固定独立报告 `37f47687cd9a23cdb34d89f4e7128ee0f4f634b2:review/remediation-third-20261012-prepare/U02/independent-review/attempt-01/report.md` 及同目录findings/per-id-verdicts。将最终修订作者commit/tree、[candidate-identities.json](candidate-identities.json)、八候选、[candidate.patch](candidate.patch)及本报告冻结；原reviewer只核三个必修点与必要delta，复用003/004及未变限定证据，不重开全局/历史review。原 [independent-review-task.md](independent-review-task.md) 仅提供角色/权限及不执行边界。共享提案若后来实际承接，必须形成新的实际身份并作独立有界复审；不得转用U01对旧WP09的签名。实际整合与actual复审尚未发生，本作者不预签；最终接受/关闭由唯一登记员按独立actual结果及U07等依赖处理。

没有实质权限或缺失证据阻塞作者交付。提交/推送及fetch结果以最终外部交付的真实commit/tree和回读为准；不在本commit内放递归self-SHA。

## attempt-01 三处局部修订对照与有限复核

固定独立报告：`37f47687cd9a23cdb34d89f4e7128ee0f4f634b2` / tree `e417c1f67ebc084e66efa235dba153215f8de219`；原作者候选：`a93bcdf7f374d5296ff5302a6cdd29e9a971a044` / tree `b6202a1926de2e070ff33d4e670a64c707bc712b`。继续原作者分支，没有合并独立报告分支或写入/覆盖独立报告。

| 独立finding | 精确修订与有限验收 |
| --- | --- |
| U02-IR-CAM-001 | WP16§3.1.1居中段分轴保留整数／浮点。CAM12整数0：终点384/384、各.6秒，.5秒320/320仍在途；CAM15浮点0.0：320/320、各.5秒；CAM16混合：384/320、.6/.5秒；CAM17负整数用floor，终点−833/−577、.2秒，浮点对照−960/−704；CAM13两未钳请求−896/−640与−960/−704分别陈述，仍都钳0。目标/速度校验与包装等待原门保留。 |
| U02-IR-CAM-002 | WP16§3.1.1商店消费者段及CAM14将右/左5格、速度5、.5秒绑定共用画面（买入/全局背包不存在的卖出）；CAM18明确全局背包存在的卖出入口/出口均无该镜头任务，不否定子场景自身演出等待。仅定点读取这两卖出分支，不扩M10全域。 |
| U02-IR-GR3-M03-002-R01 | WP14§3.1.1失败表与DQ06分开待播种子清空/重播和后续抽样推进。空起点首次读坐标失败，后续方向洗牌/房间装饰未到；精确宿主版本UNVERIFIED，不保证空抽样正推进，也不无条件保证零消费。密度0只保实际前序抽样；B原图未写、旧暂存/未驻留保留。旧C044未重开。 |

仅四候选文件发生变化：WP16正文、WP14正文及两个世界测试目录。另四完整候选blob保持原样，其中003/004主合同所在WP11、WP12、WP13事件均未改；CS01–13/MR01–13共26条案例逐行字节仍等于原作者候选。原独立PASS按这个未变条款/案例范围复用，**不转成新测试整文件blob的签名**，不作作者PASS、actual或正式接受。WP09/kernel两提案原字节及其原独立PASS范围保持。

本次修正四条已有案例（CAM12/13/14、DQ06），追加CAM15–18四条，其余初版45条新增案例保持字节，共53条均NOT_EXECUTED；两目录458条原案例仍保留，93个限定控制行hash观察点保持。先前39固定输入及完整qualified语义证据按原精确身份复用；本次不重复全部源/历史证明，只读三finding、相应源段并核delta。限定数学数值是规格文本中的静态验收设计，没有运行插值、Ruby或案例。

正文/共享提案的完整身份与基于固定派发的完整8目标patch已刷新。有限复核需要检查上述三个修订、53案例标注及未变PASS范围的字节证据；模型请求及宿主/真实材料未知仍按原限定，实际整合/公共登记/关闭未发生。最终修订commit/tree及远端字节回读由外部交付绑定。
