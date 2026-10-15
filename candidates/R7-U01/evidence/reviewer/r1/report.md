# R7-U01 第七轮独立候选复审 r1

**结论：GR7-M01-001 = PASS_SCOPED_CANDIDATE；GR7-J01-001 = FAIL_SCOPED_CANDIDATE（需修订）。** 两项原合同均已按全文七组独立核对；16个原向量的预期通过有限静态内容复核，但 J01 新增的一个绝对条件与应保留的合法4000记录/字段默认不相容。候选未修改。

## 输入与独立身份

- 审者实际 context：`01a13f7e-6e91-7224-b3f1-6f126b10d036`，由本容器 CODEX_THREAD_ID 实读；作者 context：`01a13f52-add1-7706-b7ec-54e07e0d7013`，两者不同。opaque平台task ID、实际agent PID未暴露；真实工具进程PID另在工具I/O中登记，不冒充平台task ID。未派生任务。
- 请求：gpt-6.1-sol / ultra / default 普速，禁Fast。实际 model/effort/tier/speed 无有效平台回参，四项均 `UNVERIFIED`。
- 用户指定派发提交：`6ec1d09e9c470954964d72761c83a760ef4f0364`；tree `15f3c40eb9733d04be228b47c6ea52e33c6123b7`。完整读取 `review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U01/reviewer-dispatch.md`（13,755 bytes，SHA256 `8208e2b1370d32aa181f400ab96281f466bba84e526c80472105a9ed9810b0d1`）。
- 真实输入冻结：`58c6427f2ba48aa7dd3b59d4ab1e40c54394fd3a`；tree `41849a965da575666d2b8363125ba14eb46bd6ec`；同精确目录的 candidate-input.json 为15,267 bytes，SHA256 `eb65cf264391fae6e4a7ef1afc0e618f796143e6f8ee7f28f06aa61e0117fce0`，blob `502e4e066df28769e4812c7922e732aacfbb4336`。
- 被审候选：`de550bb9fe5d2b80312b1a4f6f166d2a6aa5fc67`；tree `929ba0be34713780e2438fc7c80e8ffd3d9cc5df`。作者分支只作来源元资料，审查未用浮动tip替代固定输入。
- 原合同：`f622356f3beb9e84ea8cff9db07c7fb382565d3f:review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U01.json`（67,839 bytes，SHA256 `8a22675683f5fe9ac89c369d1abdad0c48548ce64b08e3f3c8345707e366a436`）。B=`e646432c644dec04d306842cc5a559a29c718fbc`，完整tree `84f79ec6e772aacbf3a464fde68cdc5a280e2950`，正式规格子树 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`；R=`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。

已在本容器分别恢复原合同/证据/固定快照40文件、7,539,352 bytes，以及完整候选/作者证据19文件、906,929 bytes；恢复后置只读。固定658488c8工具、两份清单均先全文阅读。原反证、M01原根成员、J01原提案及根独立反证均按精确pointer审读；独立校验raw字节范围和canonical绑定。未假定共享旧目录。项目AGENTS.md已全文读取；B和派发提交无.agents树，本容器相关.agents/skills未提供可用技能。

完整候选对B的19项差异全部是本批candidates新增文件，模式均100644；6份完整镜像的全部hunk与根冻结patch逐字节重算一致。作者manifest的18个非自身成员逐一匹配，manifest自身由候选commit/tree和冻结19文件表绑定。这些是TOOL_VALIDATION，不替代下列内容裁决。逐文件完整身份见 [review-input-receipt.json](review-input-receipt.json)，独立机械证据见 [mechanical-audit.json](tool-evidence/mechanical-audit.json)。

## 需修订：R7-U01-R1-J01-01（P2，新增消费者断言）

位置：候选 `deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md:58`，blob `73e9a4d55d254253a4bc13d9e3908c03ae110eff`。新增文字为“最大量表消费者仅在没有记录时采用4000”。按字面，这把4000输出限定为缺记录；合法已有记录同样可以产生4000。若作者本意只限定缺记录的回退分支，也必须在此写清楚，不能让值与值来源成为同一必要条件。

反例前提：固定R、无schema/登记/查询/消费者覆写；Species已登记RATTATA，Shadow可选输入明确存在且启用，前序转换、终检及I/O正常，各子例独立。仅一个合法[RATTATA]节，GaugeSize省略；其余属性省略。记录成功存在且量表为4000。对合法RATTATA/形态0消费者，形态0专门记录缺席而基础记录命中，最大量表读该记录得到4000。显式GaugeSize=4000也合法，得到相同反例。已有GaugeSize=5000时读5000；没有任何命中记录时才走缺记录回退4000。这四个正常读取观察点必须分开。

依据：固定R `Data/Scripts/010_Data/002_PBS data/011_ShadowPokemon.rb:16–22,35–54` 的正整数接受域、查询和记录默认；`Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:32–39` 的实际消费者。固定B且本候选未改的 `pokemon-rules/wp23-shadow-data-and-vectors.md:61–67` 已正确声明GaugeSize缺省4000。本项原七组“正确保留范围”的默认字段条款要求该规则不变。此处是SOURCE_STATIC + DERIVED_VECTOR；参考/行为均未执行。

最小修订建议：**“最大量表消费者有记录时读取该记录的GaugeSize（字段省略默认4000），无记录时回退4000。”** 保留原5000别名向量、可选启用、其它查询门及省略默认。改动应在新作者版本和新冻结中完成；本审者不修候选，也不要求改正确的Shadow领域正文、参考或未来policy。详情及完整反例前提见 [new-counterexample.json](tool-evidence/new-counterexample.json)。

## 逐项内容与原向量结论

**GR7-M01-001：PASS_SCOPED_CANDIDATE。** WP03:41–42及generic目录:206–208把整数键查找与记录对整数比较分开。独立核TownMap、Metadata、PlayerMetadata、MapMetadata、DungeonTileset声明与共用比较；TownMap最小实例、同类、TerrainTag双身份、Item符号/字符串及EXPSHARE反向消费者均相容。查询覆写不被改成相等规则。比较假为正常布尔值；无取消、保存或部分提交，不推导普通游戏故障或未来永久兼容政策。

**GR7-J01-001：FAIL_SCOPED_CANDIDATE。** 三类接受域、省略/空次位0、显式0拒绝、Species先登记、Shadow夹具启用、正数无需额外同号形态定义、外部身份等价及两个顺序的拒绝位置，均与固定R及已接非作者反证相容。Metrics正形态门/惰性克隆、Shadow和地牢所有整数先试专门身份、直接register覆盖、PBS第二节拒绝、指标No/Yes及直接/启动失败前缀也保留。失败原因仅为上节新增强断言违反默认保留门；13个原向量通过不能覆盖这个额外合法反例。

下表“通过”仅指前提与静态预期的内容核验；全部行为执行状态仍为 **NOT_EXECUTED**。

| 向量 | 独立核对的观察点 | 内容结论 |
| --- | --- | --- |
| GR7-M01-001-V1 | 查找1命中；同一记录对整数1正常为假 | PASS_STATIC_CONTRACT |
| GR7-M01-001-V2 | 同类两个TownMap主身份1比较真；五类无另一数值序号，各查询覆写保持 | PASS_STATIC_CONTRACT |
| GR7-M01-001-V3 | Grass对2真，合法EXPSHARE对符号/字符串真；不推广为普通游戏故障 | PASS_STATIC_CONTRACT |
| J01-V01 | 省略/空版本0、6×4正常查询/保存门 | PASS_STATIC_CONTRACT |
| J01-V02 | 基础5×4与正版本6×4共存；缺版本2回基础 | PASS_STATIC_CONTRACT |
| J01-V03 | cave_1自身区域/版本0；query(cave,1)命中6×4 | PASS_STATIC_CONTRACT |
| J01-V04 | 两个顺序第二节专用诊断分别cave/1及cave_1/0；首条内存保留 | PASS_STATIC_CONTRACT |
| J01-V05 | cave与cave_0可共存；query0先命中后者 | PASS_STATIC_CONTRACT |
| J01-V06 | 三类显式0在转换前拒绝；未知Species枚举拒绝 | PASS_STATIC_CONTRACT |
| J01-V07 | 合法两Species，Metrics别名命中7,8，不克隆；query0走基础门 | PASS_STATIC_CONTRACT |
| J01-V08 | 合法两Species及启用Shadow，别名5000由最大量表消费者读取 | PASS_STATIC_CONTRACT |
| J01-V09 | Metrics/Shadow两个顺序各拒绝第二节；首条元数据/内存保留 | PASS_STATIC_CONTRACT |
| J01-V10 | 省略/空0与正形态正常，基础/正形态共存，正数不额外要求同号形态 | PASS_STATIC_CONTRACT |
| J01-V11 | 完整合法Autotile/Tile组7/23可登记；重复7通用拒绝，缺组先构造失败 | PASS_STATIC_CONTRACT |
| J01-V12 | PBS无交互取消；独立指标编辑No重载，Yes先dat后PBS，后失败不回滚 | PASS_STATIC_CONTRACT |
| J01-V13 | 直接与启动各自前缀；旧dat/先行档案、删除尝试与重抛不合并 | PASS_STATIC_CONTRACT |
| R1-J01-DEFAULT-01/02 | 有记录且省略/显式GaugeSize4000，消费者仍4000；与新增“仅在没有记录”字面条件冲突 | FAIL_STATIC_CLAIM |

原反证没有被作者自审替代：M01完整M03 challenge的有限已读/未读资格保持；J01完整14,166-byte反证（SHA256 `272e946adc8151c4f53c44a561ee8b7e2c176102855e9949f26e0840b812cf63`）及V01–V13已逐项新核。J01的C03 E009/E010与M01 F214/F224来源/错误anchor分开，冻结artifact未改，原错误anchor未重授完整SUPPORTED。

## 正确保留、历史回归与共享接收

KR03–08、KR12、KR14–16保持查询类型/回退、副作用、直接注册/电话默认例外；KL02–06、KL15–16、KL36–39保持可选位、拒绝、直接/启动删除及异常前缀。KL23–26、R6-U14-C06-01–03、WP73-B §7/§7.5和WE-M19/20保持已有字段自身默认与整条缺席克隆、来源后缀、保存时集合决定PBS路径、先档案后PBS及现有布局边界。DG01、DG17–27、GR3-DQ01–09、U01-M01-021/022-01–03保持默认5×5与cave5×4、非空图块集回首条/空集失败、Autotile/Tile完整组和构造/播种/生成/摆放失败前缀。上述旧目录字节完整保留，指定相关条款已作静态相容核；未重新执行这些历史案例、未重发旧全局PASS。Shadow默认4000则对新增第58行提供本次失败反例。

四份条件目标无必要改写：WP14 §3.2/3.3已有参数查询及生命周期转交；Shadow data §3已有正确默认；WP73-B §7/7.5有成功登记、克隆与保存门；DX目录现有指标向量不因新producer补充而矛盾。J01修订应消除改变处的过强表述，而非改掉正确默认。没有采用optional/policy或额外导航facet。

CG01：WP03整数比较贡献可按条款接收；J01第58行先修订。CG02：WP04第114–116/307行与既有失败前缀相容。CG03：generic目录仅附加新向量且旧前缀完整保留。CG04：engine目录仅附加相同向量交叉索引，不产生新运行证明。CG07：matrix/traceability仅附加待接收贡献，旧状态/身份/错误anchor债务保持。以上只是本批贡献的接收意见，没有审其它批次的实际贡献或累计整合tree；R7-I必须按hunk/条款串行接收，不能用整份镜像覆盖共享文件。

## 执行资格、日志限制与后续门

本次新增语义证据限 SOURCE_STATIC / FORMAL_STATIC / DERIVED_VECTOR；工具仅做传输、身份、模式、差异、raw绑定及目录校验。未执行作者程序、参考Ruby/native、独立行为模型、宿主、Demo、媒体或真实存档回放。全部原/新增行为向量NOT_EXECUTED；L01–L14及旧56/92边界保持。19个参考文件的实际新读范围与未读补集见输入回执；未声称全参考树、全项目正文、完整历史根或无限组合已复审。

早期侦察/源读取和初始fetch具有平台工具I/O，但没有另存逐命令UTC/stdout/stderr/PID日志；不回填虚假日志。恢复保留真实HTTP UTC/状态回执；后续机械核验、提交、push及远端读回使用完整记录器。一次额外Item索引查找StopIteration未产生输入，后从固定B追溯定位006_Item并取得固定R独立回执；没有把它说成C13已绑定。对已完成fetch的冗余中断返回“no such process”，原fetch实际成功；均不作语义证据。详细缺口在review-input-receipt.json。

待满足：J01作者修订、新版本冻结与独立候选复审；R7-I接收共享条款并发布真实累计整合commit/tree、精确直接/传递依赖及历史回归；新独立R7-IR审真实累计字节；随后由R7-I决定有限正式接受与关闭。本报告无权登记实际整合PASS、ACCEPTED或CLOSED。分母仍27项/13批。

本次成果仅在唯一 `codex/r7-u01-reviewer-20261015-r1`，从固定B的独立干净checkout产生，仅写 `candidates/R7-U01/evidence/reviewer/r1/`。普通提交/推送及完整远端读回由真实工具回参和外层最终交付绑定；文件不声称包含自身最终commit/hash。首次传输回执若随最终成果入树，只证明其明确列出的前一提交，最终提交仍另作全量远端验证。

初次staged diff检查因原样patch空白上下文行报trailing whitespace（exit2）；该失败日志已保留。首个本地提交当时尚未推送，后继普通提交将patch证据无损封装JSON并移除裸patch，保留原始内容hash。最终发布前重新进行含未跟踪新文件的暂存检查；不把初次未暂存检查的exit0当作完整检查。

首个实际远端发布提交 `3e5f55bb10cd3fbd0eaf91306e1c8d553392d273`，tree `6aebb0c06fbe1623b362c3a2b9663688d25f0977`，普通push成功（exit0）；远端固定URL完整读回24文件／206,085 bytes，逐文件HTTP200、完整bytes/SHA256/blob/mode均匹配，分支tip前后相同。完整回执随tool-evidence/remote-readback-first.json发布。当前后继提交只追加这次真实传输证据、报告运输说明及manifest；最终commit/tree仍由外层独立全量回读绑定，不能把本首轮回执冒充最终提交回执。
