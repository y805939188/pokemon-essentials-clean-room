# R7-U09 r1 独立候选复审

**逐项结论：GR7-M14-001、GR7-M14-002 均为 PASS_SCOPED_CANDIDATE。**

本结论只绑定候选 `fe8219b851363860704048642ff30f4fa1e31f97` / tree `d2634c926b236d38896b809651343cae67dd0f5b` 的三份镜像和本报告逐项列明的静态范围。它不登记实际整合 PASS、正式 ACCEPTED 或 CLOSED；其余批次不在本次结论内。

## 输入、身份与授权边界

- 用户具名派发固定提交 `95c260d8f3fb4a171675dde877137fcd4c2f1c8d` / tree `577c350364bb4e2eb712325a9095d53d29eeeeb3` 的完整 `review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U09/reviewer-dispatch.md` 已读。
- 候选冻结提交 `aa369555b0e8b6c8b077f964b54ed63d3b924f26` / tree `08bd0f362c74ef7645b5bbd70b557489c122ae29`；其同目录 `candidate-input.json`、`candidate-restore/R7-U09.json`、`mirror-diffs.patch`、`remote-readback.json` 按固定提交接收。没有以浮动作者分支或当前 HEAD 猜输入。
- 原完整七组合同为 `f622356f3beb9e84ea8cff9db07c7fb382565d3f:review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U09.json`，两项七组均已读。读取原提案、C05 原始非作者反证 `/challenges/4`、`/challenges/5`、最小修订、正确保留、向量与依赖；另独立核其12个具名原始成员的字节切片、SHA256及解析后指针相等。
- 固定 B `e646432c644dec04d306842cc5a559a29c718fbc` 的完整项目 tree 为 `84f79ec6e772aacbf3a464fde68cdc5a280e2950`，正式正文子树为 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。二者用途不混淆。
- 本审者实际环境变量 `CODEX_THREAD_ID` 为 `01a13ff0-c72f-7317-a831-838a4bdd5004`，角色标签 `/root`；环境 `ccarenv_b64_Y2NhcmVudl9jYWUwYWIzYzY1N2M4MTkxOGEzYjk3NDIwM2FmMGQ0ZQ`。父线程 `01a13f49-a154-7054-9b04-ce31f924d01c` 仅为来源，不冒作本 task。
- 作者外部 task 标识由父会话冻结为 `01a13f7f-cfab-7438-bd2a-8565a82af011`，与本实际 thread 不同；作者原证据内部 context 未暴露，保持 `NOT_EXPOSED_UNVERIFIED`，不将两个 opaque 标识自行等同。没有创建子任务、作者、其它 reviewer 或自己的 R7-IR。
- 请求 gpt-6.1-sol / ultra / default 普速、禁 Fast；实际 model、effort、tier、speed 均没有有效平台回参，逐项 `UNVERIFIED`。环境变量 thread、进程 PID 和退出状态不认证有效配置；没有查询额度/认证或发布私有模型流。
- 实际项目 AGENTS.md 已读。工作区、项目、用户级 `.agents/skills` 均不存在，固定派发树中也无 `.agents/skills`；executor skill 列表为空。未用无关技能代替项目技能。

## 独立恢复与实际字节

已先完整读固定 `658488c81f1f3181a488298ab27850c8af951d73` 的恢复工具、原 U09 清单和跨容器说明，再在本容器独立执行两次恢复：原输入25文件／5,703,134字节；候选13文件／357,409字节。回执逐文件含传输、bytes/SHA256/blob。恢复目录保持输入用途，不执行任何作者、参考或 native 程序。

本次还实际 fetch 候选固定 commit，逐文件比较已恢复 HTTP 字节与该 commit 的 Git blob、100644模式和完整对 B 差异。13文件全部为本批 candidates/ 下新增，其中3镜像、10作者证据；作者 manifest 的12个非自身成员均匹配，manifest 自身由固定候选 commit/tree 和冻结完整表绑定。逐项结果见 `audit-result.json`，不是复用整合者哈希结论。

| 候选镜像 | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| pokemon-rules/wp62-pokedex-records-regions-and-content.md | 35484 | 68bd52e6720e5549ccb2a55375946bfbc4874ccb3f20e1eb06ccfe761685ede8 | 2b60da1326ba16bc8d62cc22e3f4c1a751addd62 |
| test-catalog/pokemon-rules-wp53-60-61-62-69-70.md | 69045 | 7a94ee7de7bb271f4de43d5171cbe9c434557fcdd3430e698e527ed8f5607040 | e30ca216c2aeda46dd03550251e1091da78800a7 |
| user-interface/wp66-b-storage-and-pokedex-ui.md | 44008 | a47fec9d90f142b3dae2f8b63157995d71b9c356cb21d000b398753e06f2797d | f41a03d59dcc78979cb1ff45e398cc9fd61ca0c9 |

以上均为 `candidates/R7-U09/deliverables/final-specification-set/` 相对路径。三份候选全文已读，分别197、300、313行；与恢复的 B 完整文本和实际差异对照。独立反向移除授权改动后，其余 B 原字节全部相等：WP62仅原38行替换和157行新增；WP66-B仅254行替换；目录仅标题导航及145–151、153–159的14个新增向量。没有新增条件路径、optional/policy 或其它批次内容。

固定 R `Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的合同具名源／消费者重新读取；另外定向补取 Species、PBS/pokemon、Pokedex Main、Battler ChangeSelf、CatchAndStore 五文件并核固定参考 tree 的条目。参考 tree 元数据查询只定位并验证这些文件，未授予参考整树正文阅读或运行资格。完整路径／范围／身份见 `review-input-receipt.json`。

## GR7-M14-001 — PASS_SCOPED_CANDIDATE

候选 WP62:157、WP66-B:254 与目录153–159，满足 C05 缩窄后的完整单条编号合同。固定源 Entry:589–611、Utilities:380–418 表明，完整单条先由当前地区设置或保存视图选择编号输入，再做地区编号查询与偏移判断，随后场景解析负地图地区；后一步不重算已保存编号。菜单:99–127 能保存全国视图 −1；默认地区表有0/1两份，CHIKORITA在末表第一位且不在表0。Species:165–167和PBS基础节头顺序支持默认全国序152；这里只进行静态数据计数，没有执行参考编号表达式或 UI。

| 向量 | 本次独立逐项判定（均 NOT_EXECUTED） |
| --- | --- |
| C1 | 合法非蛋、已见已拥有、有图鉴、全国解锁、无偏移、地图/前序资源正常；设置关且保存 −1时完整001，摘要/简略152。摘要在开场前覆盖最近见到；不是编号查询写拥有或计数。 |
| C2 | 保存0时目标不在表→编号0→Info「???」，保存1→001；缺/空表的编号查询返回0。候选没有保证缺地图/资源时全场景成功，也没有抹去数据层成员查询失败与主列表回全国的区别。 |
| C3 | 选定 −1时，仅偏移键 −1→000，仅键1→001；偏移测试看选定值，不能按末表物理位置补换键。摘要/简略的偏移分支保持自身规则。 |
| C4 | 设置开且有效当前地区1→001；设置关、保存0、地图仍1→「???」。地区缺省/超表数先归 −1，后续地图解析独立，不能反算编号。 |
| C5 | View前取消不达本次最近见到写入；正常打开后BACK不撤销它，正常返回摘要。排除进入Forms选择器，避免把其另一次覆盖混作退出副作用。 |
| C6 | 最近见到先写，之后启动/资源失败只保留实际前缀；不保证绘图、清理或正常返回，不新增经验/拥有/两计数。没有实际异常注入。 |
| C7 | PD25摘要首个解锁查不到即停／简略继续查找、主列表全国回退与编号保持；R4-PD02普通图像请求及刷新不写false保持，调用方最近见到另计。 |

正确保留另逐条核验：Summary:403–424 与 Brief:70–117 是两个独立编号消费者；Pokedex Main:348–403 仍用自己的列表来源及偏移；Entry:139–152 普通图像请求不改所存异色，Entry:446–483 的形态选择器首轮和移动写入独立于普通刷新。原目录 PD25、R4-PD01–05、R6-PD01–03及WP62其余内容原字节不变。没有把负视图差异泛化为所有编号错误或永久兼容政策。

原提案N01–N08亦逐项对照：N01对应C1，N02/N03对应C2，N05对应C3，N06对应C4及WP62:157超表数回−1规则，N07对应C5/C6。N04关闭全国解锁不会改变完整单条的地区查询；摘要/简略各走自己的解锁分支，不延续152的旧前提。N08所列R4-PD01–05、R6-PD01–03已重新读其全部原前提/预期与相关图像/形态选择消费者，条款原字节保持，未重新授予旧全局PASS。

## GR7-M14-002 — PASS_SCOPED_CANDIDATE

候选 WP62:38 与目录145–151，满足实际玩家／伙伴／对手首发与替换共同登记的最低合同。StartAndEnd:120–242 将己方及伙伴实际出场者带入共同出场；ActionSwitching:274–297 的实际替换也进入相同入口。其先行 peer、呈现和逐成员指令重置在登记前；Battle:658–666仅判有效对象和内部战斗门，无对方阵营限定，接收者由Battle:215绑定战斗玩家。Pokedex:195–219写见过／展示形态，空末次首写、非空保持，然后才刷新可访问列表。

| 向量 | 本次独立逐项判定（均 NOT_EXECUTED） |
| --- | --- |
| C1 | 合法已构造、健康普通雄性BULBASAUR0，静默仅入队see_form=false构成owned-only；排除动态形态/幻觉/变身/插件，battle player等于全局玩家且前序正常。实际己方出场后seen/form真、空last→[0,0,false]，owned保持、两计数不变。 |
| C2 | 原非空last=[0,0,true]保持；同一已见形态重复置同值幂等。普通登记不是总覆盖的最近见到入口。 |
| C3 | 玩家实际替换、伙伴实际首发、对手实际出场，在各自实际到达共同入口时登记；实际出场前取消不达此写。伙伴不改用伙伴自己的图鉴。 |
| C4 | 非内部包装不写这些记录；候选明确排除独立形态提交，未将本门错误扩大到所有战斗副作用或捕获直接写入。 |
| C5 | 未传入实际出场的后备不被此入口登记，原owned-only保持；不是“队伍所有成员”登记。 |
| C6 | 呈现／该成员指令重置先失败则该次共同登记不达；登记后列表刷新失败可保留seen/form/last前缀，不撤销此前入队/拥有或已完成成员写入。 |
| C7 | PD24原两静默入口对照保持：普通静默加入显式seen，静默仅入队see_form=false无seen。地区可访问性仍按既有记录/配置/解锁分支，不新增解锁或无条件可达性。 |

正确保留另逐条核验：Utilities_Pokemon:78–90与121–129构成PD24对照；Battle:668–684与Pokedex:250–272使计数写入独立；ChangeSelf:64–84的倒下登记仍要求对方调用门；CatchAndStore:87–107的捕获队列包装与直接拥有/暗影写入仍分列。没有扩展对方倒下、捕获计数或全局玩家形态提交的门。WP62:39–64、75–90、110–118、196与目录PD24原字节保持。

原提案S01–S08亦逐项对照：S01/C1中地区0新增可访问性仍要求原配置/区域/见过及相应解锁门；S02/C2，S03/S04对应C3，S05/C4，S06由C3及本次重新读取的对方倒下消费者分开核定，S07/C6，S08/C7。没有将首发同门扩大到所有倒下消费者或所有后备。

## CG05、同步与历史接收

CG05共享目录所有者仍为R7-I，相关批次U03/U09。重新读固定冲突组和U03原授权相关scope／GR7-M05-001最低修订：U03涉及碰撞完成与野外步进接点，本批只在PD24/PD25旁追加条款与标题导航；没有修改FP、SF、BP或U03字段。故**本批条款可供按条款接收**，不允许以本完整目录覆盖未来U03贡献；不据此声称U03候选已过审或累计整合无冲突。

WP62完整单条行、WP66-B转引和编号向量均为001的具名required同步；WP62出场行与PD24邻项均为002的required同步，无额外conditional目标。WP66-A摘要、战斗出场/伙伴、WP62及共享目录语义owner仍需R7-I在实际整合时接收；Feature Matrix／source-traceability公共记录由根按原门审定，本审者无写入权。

历史回归并非旧PASS替代：本次重新对照PD24、PD25、R4-PD01–05、R6-PD01–03及Entry的对应消费者。候选没有改变PD31–34、U05-HAB及其它目录原条款；它们的原字节保留不等于此次重新认证所有旧案例。旧56/92关闭边界、27项/13批分母与L01–L14全部保持。

## 执行、日志与剩余门

本次新增证据仅SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION。14项向量均NOT_EXECUTED，异常未注入；REFERENCE_OBSERVATION、独立完整模型、游戏宿主、Demo、native媒体、真实存档/回放均0。默认负视图差异的未来兼容政策仍另决，只阻止未裁定的政策外推，不否定本候选对参考行为的描述。

`tool-io.json` 保留本审者文档审计首次因补充Main不在原C13局部身份表而KeyError退出1，以及补取固定参考tree条目后重新审计退出0的真实分离输出。原工具失败未删除；它不是候选语义失败。两次猜定补充源路径404后，按已恢复身份索引找到正确Species/Catch路径；shell API tree查询403后使用已连接GitHub只读查询恢复固定tree元数据。具名依赖均已补齐，无残留可读材料阻塞，也未把失败改标成L01–L14豁免。

初始读取的工具I/O保留于平台会话，未逐命令单独落盘UTC/stdout/stderr，不能由后继审计回填成初始证据；L14历史资格不变。发布文件只含独立规格评语、身份、回执和文档审计，不复制参考程序正文或私有模型流。

仍未满足：R7-I按条款串行整合及CG05贡献接收；实际累计commit/tree的新独立R7-IR；语义owner、直接/传递/领域依赖及具名历史回归最终接收；根正式ACCEPTED和满足全部条件后的CLOSED。本次候选PASS不自动通过这些门。

唯一成果分支 `codex/r7-u09-reviewer-20261015-r1`，由独立checkout从B创建，创建前远端无同名分支。只普通提交／普通推送本目录证据；未携带作者镜像。先提交推送并完整远端回读，再将首次回读回执纳入后继普通提交；最终再对最终commit所有新增文件完整回读，真实最终commit/tree与逐文件回读通过工具输出和最终交付绑定。manifest不自哈希；不为嵌入自己的最终commit而循环改写。未修改候选、正式文件、公共台账、main、tag或旧r1成果。

首次普通推送已完成：commit `b236a638030cd01bb143706ba54ca523da8b1f56`，tree `e07caedfd01f86d9a8ed5ea575588a951aa006e5`，父提交为固定B；随后远端完整回读12文件／162,537字节全部匹配，前后分支ref一致。`first-push-readback.json` 与 `publication-first-io.json` 为真实回执，本后继提交只补入这些运输证据、此说明及manifest身份，不改审查结论或输入。最终提交完整远端读回另通过最终工具输出绑定。
