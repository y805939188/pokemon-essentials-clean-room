# R7-U07 r1 独立实际累计整合复审

**GR7-M12-001：PASS_SCOPED_ACTUAL_INTEGRATION。** 仅对固定 MI 的 P3 缩窄必修合同、C1–C6及具名消费者作静态内容判断；无本限定范围的阻塞发现。全部行为向量 **NOT_EXECUTED**。不授予其它必修、全局、运行等价、ACCEPTED 或 CLOSED。

## 固定身份与独立资格

| 对象 | 完整身份 |
| --- | --- |
| 全文派发 | `72c93538d6e6cc15cb0be15ccfc3b8268d4b0af7:review/remediation-seventh-20261015-prepare/integration/wave3/v1/dispatch/R7-U07-R7IR.md`，先直接读全文 |
| B | `e646432c644dec04d306842cc5a559a29c718fbc`；workspace `84f79ec6e772aacbf3a464fde68cdc5a280e2950`；正式子树 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c` |
| 实际 MI | `e54f54a2cb32e546eabd46aaf53ed45b30a8af89`；workspace `b3b6b166b69d2e4dc513cd8d72950b47306191fd`；正式131文件子树 `e1dfe28acd4f559b22da505238ef3a899aed4542` |
| 实际 FI | `b98fa82f8a08b5630ac568cbe8c34f607f623cfb`；tree `eaf9f0831cea151c8a77ad716ad4c8fc5b71dc66` |
| R | `Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只读 |
| U07候选 | `2649ed2bd2cc3afdfa636cd643fc1975de5eae32`；tree `6b2e6a6122cb24b330a052137750dc985908e796` |
| 新r2候选审查 | `1bd0799d1819ef87c3c383a7f8e50d78756333c4`；tree `b82145b91a4f03999ec96b8cce0046982dab0b23` |

本容器直接可见 `CODEX_THREAD_ID/CODEX_SESSION_ID` 为 **`01a1403a-ee84-70fc-9167-0ced3e03c036`**，逐一不同于全文合同41个排除身份，包括作者、旧r1、新r2、整合者和父线程。本次未创建任何AI辅助agent、子任务、子会话或模型调用；没有查询额度或认证状态。平台内部opaque context/创建回执未暴露，作者内部opaque原资格保留，不从`/root`或PID推断身份。真实进程PID/UTC与所见线程分开记于 [运行身份观察](evidence/runtime-identity-observation.json)。

请求 gpt-6.1-sol / ultra / default / 普通速度、禁Fast；没有有效配置回参，实际 model/effort/tier/speed 均 **UNVERIFIED**。本可见线程提供独立上下文区分，不能认证有效配置。旧r1因合同前辅助AI任务而WAIT未豁免，其内容PASS未迁移；r2资格只是本次输入，不代替实际MI独立判断。

## 恢复、读取与字节核验

先全文读实际AGENTS、固定658488c81f1f3181a488298ab27850c8af951d73的恢复工具、跨容器说明和原计划，再执行已读工具。原输入在本容器恢复 **23文件 / 5,526,711字节**；实际冻结输入恢复 **185文件 / 4,584,535字节**。FI计划95348字节，SHA256 `7de7bb34e4760317301ea19d6ed05a4db68422ccf059726773211d39d66f2d00`。未借用整合者目录，未执行作者程序或参考/native程序。

原七组、原提案、实际C05反证和根缩窄原始成员已读；全部契约绑定89处重新核原始字节区间。完整MI的17份指定正文/目录、完整B两目标和源码具名链重新阅读；audit/matrix/DX三个本批涉及的完整当前共享文件已读。具名补取WP73-B、WP74/WP75相邻工具条款和WP77；准确全读/局部读/只核字节范围见 [reading-ledger](evidence/reading-ledger.json)，不把检索或退出0算成内容阅读。

全部208个恢复成员重新核bytes/SHA256/blob；作者manifest31项、新r2 manifest95项非自身声明匹配，manifest自身由固定文件身份和输入commit/tree绑定。随后取得不可变候选/r2/派发Git对象，32份作者和96份r2完整blob及对B全差异与快照逐一相等，派发全文与最初所读字节相等。实际Git MI/FI树已核；逐一读取131个正式Git blob完整字节，比对FI与具名快照，得到 **30改变 / 101相同**，并由全部字节重新计算正式树为`e1dfe28acd4f559b22da505238ef3a899aed4542`。这些只是身份/工具证据；未对131份全文统一授予语义PASS。

U07两完整实际目标等于批准候选字节：

| MI文件 | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| WP55 | 24678 | `226c00f62dd915bc089e41f640c2bff1ec707a3845d683e4bfb75221ad8047c6` | `5699f935e49c60448a5dbbc252d50af7591df17b` |
| combat目录WP54/55/56/58 | 35869 | `7bcdfa69b2432991e81f540ffdc699a409bc4b0396c13f056abaa952da5e1422` | `c738f1d47a3de885d723588f8982774a18f0e436` |

实际WP55 L93–95、L126及目录L104–116是本批三片段；目录六行L110–115。每片段、每向量的0基半开字节区间及独立hash/blob见 [per-id](per-id.json)，B身份及全部移除/新增片段见 [累计字节审计](evidence/cumulative-byte-audit.json)。片段以外两目标字节保持，原WS/QC/PA/RC行保留。

## C1–C6独立判断

共同强前提完整保留：合法直接训练家索引0、类型、姓名及胜负台词，两次表读取一致；有效受伤非空玩家、Tower、明确无等级调整、非debug skip，场景构造与此前依赖正常。它不是默认PBS或普通Demo可达性断言。

| 向量 | 实际条款与静态理由（全部NOT_EXECUTED） |
| --- | --- |
| C1 | 候选[]/模板[]、建议3：短名单零迭代返回初始空队NPC，会话补台词后包装先治疗；记录战斗继承构造在空对手门拒绝。生成与拒绝阶段不同。 |
| C2 | 只改候选[0]而模板仍[]：实际尝试缺失条目创建即失败；尚未进入包装、未治疗。 |
| C3 | [0,1]/两合法模板和独立[0]/一合法模板各按原序返回2/1；不补齐、不最终整队校验，不承诺整个对局成功。 |
| C4 | 无等级调整返回nil，未保存EXP数组；之后玩家物品身份按位置保存，对手物品表[]。不混同nil与[]，原提案较宽经验快照论被排除。 |
| C5 | 依赖正常的debug skip在治疗/调整/构造前清临时记录并true；UI nil取消是独立入口，不提交、保留P。不能代替空候选。 |
| C6 | 治疗已提交；记录对象局部初始化不清全局旧记录；构造拒绝早于正常还原、末尾清记录、胜负统计，旧记录可留而本次统计不增。没有统一回滚或未来政策强制。 |

依据为本次重新读R的ChooseFoes39–83、Trainer163–194、BattleChallenge95–104/196–203、ChallengeData21–49、ChallengeBattles40–96、ChallengeRules9–14/61–116、RecordedBattle15–22/228–232和Battle98–103。报告只陈述行为与取证定位，不复制/转译源实现。

## 反向消费者、历史与共享接收

C05将原P2缩窄为受控工具边界P3：保留短名单1/2原序、空训练家表/非整数随机另路，撤回“所有空内容在创建失败”和“本无调整例已存经验”的全称。WP55§3是通常调整流程，已显式转引WP54§4；WP54§4.1无调整nil例外与本次§2.5限定共同控制C1，不需越权扩修。

WS-W31、QC-Q46、WS-W29/W35及空列表/start/end相邻对照逐条件保持。WP57/FC-17的空工厂池仍设置临时人数再抽取/创建，和普通对手零次迭代不同；WP76作者生成器debug门、非终止风险、1%真实无视觉战斗/99%估算仍分层。WP39空队构造门早于非空全濒死的参与者/业主门；不因此改BC19/20或WP41决定3后继续扫描。

先前已接收U04/U05/U09八份实际文件逐字保持，并读完整当前文件与两组旧实际报告。领域交叉重新检查：WP34显式同值子代/动态亲本提交和BR/PF；WP62全局形态登记与内部出场包装门、PD24；WP66-B形态浏览/普通图像/独立编号消费者各有独立门。C1零创建不新增对手构造登记，玩家治疗不等于一切构造/记录副作用事务化。这里只检查相容性，不重签旧三/两项接受结论。

累计journal的 **28文件 / 72片段（既有56＋新16）** 逐片段对齐B锚点、批准候选、原独立批准ID和实际MI；更早U04/U05的11片段另由八文件保护。其它批次只核当前贡献保留与相容，不新授其语义PASS。audit/matrix的U01→U02同EOF插入、各独立锚点及作者时点标签保留；DX目录同EOF明确 **先U11旧工具组，后U10新TOOL-AN**。WE-M17、AN-M09局部变更与新尾组并存，T-WP74/F18-03未覆盖相邻T-WP75/F18-04。WP74工具仅图像请求，未承诺.anm/PNG编码/自动导入桥；WP75两BMP存在与区域底图缺失、extendtext请求和WP77零Demo证据分层保持。

root audit/matrix追加当前阶段说明。导航JSON另保留前一阶段status/reception三处行政变化，候选不是整文件逐字相同；已单列差异且其余字段完全相同。未将候选时点待审标签覆盖根当前状态，也未从当前接收指针推本次已接受/关闭。

27必修/13批、旧56/92边界保持；7 optional、2导航facet、1 no-required、2policy未采用。U03 r2待结果未整合，其它7份wave2实际审查仍各绑定原MI/FI；新MI不是它们自动获审。原排程/冲突空集不能替代直接、传递、领域、共享与历史责任。

**剩余门归R7-I**：接收本结果精确commit/tree；登记WP55、WP54、WP39、WP57、WP76语义owner，combat共享目录及audit/matrix receiver；登记WS-W31/QC-Q46/取消与无调整/FC-17/GN/后阶段门的精确历史和直接/传递责任；随后分别决定正式ACCEPTED与CLOSED。本审者未自行登记或关闭。

## 工具、限制与成果边界

SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION分开。新增参考观察/进程、行为模型/独立完整模型、宿主、Demo、native媒体、真实存档/回放、异常注入均0；所有行为NOT_EXECUTED。L01–L14全文保留于证据文件，旧H14局部Ruby1进程/10输入不回填本任务。可读但未读的其它材料仍是未读，不冒称限制或完整源树批准。

两次早期机械失败如实保留：U01报告路径误用r1导致404；候选导航JSON与实际行政字段不同导致断言失败。纠正后完整重核通过，仅获TOOL_VALIDATION。初始若干读取没有独立落盘每命令UTC/PID/三流；平台I/O、恢复HTTP回执与现存stderr保留，不补造。另一次空列表探查IndexError和shell API tunnel403分开登记，非规格缺陷、非认证状态查询、非自动审批拒绝。

唯一隔离checkout由B建立，分支 `codex/r7-ir-u07-20261015-r1`；仅本目录四主文件及真实工具证据普通commit/push。不携带MI正文、候选镜像、公共台账，不改main/tag，不force。manifest不自哈希；最终commit/tree和全部文件不可变URL完整响应体读回在外部返回绑定，避免自引用。
