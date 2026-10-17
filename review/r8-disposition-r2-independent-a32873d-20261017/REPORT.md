# R8 去向打标 R2 固定候选独立复核：FAIL

受审候选：`a32873d2860b15d9f5e27727db8f131f4ec433b6`。本报告不修改作者清单来取得通过，不改正式规格、旧审查报告、参考仓库或 main。

**当前固定源粗标不能通过：736 active 行中 708 PASS、28 FAIL，33 metadata 全部 PASS；新增/残留共7项问题（1 P2、6 P3）。** 28行的分类、职责及有效范围可以成立，但其出站依赖含错误章节或异体系功能。三个工具缺陷另计，不摊成736行分类失败。全部736行的去向/职责/拆分 facet 均 PASS，不代表目标兼容或行为覆盖。

R1残留12项中11项PASS，`R1-CRE-DEP-001`仍FAIL（186/190/192）。本轮完整同根检查另外发现25个依赖失败行，包括未改的R1 PASS。字节保全不能证明这些引用有真实用途。`findings.json`给出精确源、候选JSON指针、目标有效范围、复现与必要修正。

当前仍为908/U02-U03两个接受事件；后继0eee/2704标题仅准备。U04尚未正式接受、未实际切换，本身不计本轮失败。正式整改与累计来源回填完成后仍须另行固定候选复审，不能称最终完成。

## 固定输入与资格

全部对象按精确SHA取得，身份、全树和正式树见[evidence/fixed-objects.json](evidence/fixed-objects.json)。入口为R2 README及完整最新review-prompt，root/R2 prompt字节相同。

| 输入 | 固定SHA |
| --- | --- |
| 受审R2 | `a32873d2860b15d9f5e27727db8f131f4ec433b6` |
| R1候选 | `5666b7b912e2fb79b5119283ee6a37401a7071db` |
| R1 FAIL报告 | `8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8` |
| 初候选 / 初FAIL报告 | `d62b41f4d620e50bb04c80a7505374bd284d8210` / `a0352c7fba38391afc535525988245701d5ce202` |
| B8来源 / R8交付 | `fd1df570cad987dc3852a3b958f03916e317f7fe` / `4575e80d041ab0c74a42e2e36399d05791dbaa5b` |
| 当前接受payload | `908273093e1f6b27fc58249417675dd62d146224` |
| U02/U03回执 / actual报告 | `861f7a44a6f763c265a11761ab17a8ec3b55f304` / `548d6bb9a21d0967680445c013e66d9d5661d2d6` |
| 五批回执 / U06回执 | `e042c2f061eb2951a8d662a5987804e3314cb6b4` / `3157ef455fdac41f0bf5485b281ef2e1699c8599` |
| 后继actual报告 | `834888e29f939d0a5ed9478d763deb86eb021211` / `8f71c18480a847348b8450c9df1e7e8194c03985` |
| 准备payload | `49a558f7d5498680ba88d532f3815e07d7844459` / `0eee6d141f33758eda34bd8ebad94a3e2b617f5a` |

只读参考HEAD为`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。作者工作区正式树为B8的`f292698cdd4a8e725525a9be6dc34b75faaf151e`，当前908正式树为`6ae817df5b11eafdec671214b0d04e542ad364bc`，准备0eee正式树为`a46d25e8aead9af2a91c8424b41e2a3c324d108b`。当前语义/locator从908 Git对象读取，不以B8工作区代替。

任务请求`gpt-6.1-sol / ultra / service_tier=default / Fast off`；缺权威创建及实际执行echo，实际model、effort、tier、speed、Fast、云任务UUID逐字段 **UNVERIFIED**。工具广告priority不是default证明，任务路径不是云UUID。六个非作者分工组成同一份独立审查，不算六张接受票。详见[evidence/task-qualification.json](evidence/task-qualification.json)。

## 覆盖与保全

从正式索引/Git独立重算131文档、历史与当前908均2683标题。历史正文4,364,108 bytes，当前4,364,096 bytes。五个领域分配为combat27、creature18、kernel13、Pokémon/世界/UI62、demo11，无遗漏或重复归属。全部721原ID、736 active、33退役完整历史、33 metadata、44原组和12残留逐项对齐，不是抽样。

[reading-coverage.json](reading-coverage.json)逐131篇记录固定身份、原始全文阅读信用、R1信用与本轮真实新读区间/责任人；[section-results.json](section-results.json)逐2683标题连接正文阅读、目录和metadata裁定。沿用先前全文信用仅限字节一致且未受影响facet；变更、非PASS和同根影响按完整有效源单元及必要消费者新读。未声称本轮重新全文阅读131篇，也未把解析字节、枚举标题或作者关键词标签当语义审核。source分工另完整新读38篇相关diff、21新标题正文及5组额外消费者范围。

| 口径 | PASS | FAIL | 待查 |
| --- | ---: | ---: | ---: |
| 原721个ID（含退役） | 706 | 15 | 0 |
| 当前736 active总体 | 708 | 28 | 0 |
| 当前736分类/职责/有效范围 facet | 736 | 0 | 0 |
| 33 metadata | 33 | 0 | 0 |
| R1旧28 FAIL回查 | 25 | 3 | 0 |
| R1旧693 PASS同根回查 | 681 | 12 | 0 |
| R1新增47 active | 34 | 13 | 0 |
| R2新增769 | 1 | 0 | 0 |
| R1失败10 metadata | 10 | 0 | 0 |
| R1通过22 metadata | 22 | 0 | 0 |
| R1残留12 issue | 11 | 1 | 0 |

R1 active失败18项中：14个存续行转PASS，186/190/192仍FAIL，86退役为META33且处理PASS；不能把当前存续17行误报成原18全部。新增769只追加，FR86完整原行加retirement，不复用ID。所有721旧source与d62一致，33退役体移除retirement后逐字段等于d62；32既有退役历史均保留，仅10条导航有明确变更。735存续active分类不变。

全部693旧PASS完整对象、47个R1新增完整对象、22个PASS metadata完整对象均与R1相等，**只证明保全**。本轮新增25个依赖错误即从这些保留区域中发现，未自动继承旧PASS。所有736 current locator/源身份/有效parent-minus-child范围独立重算，无重复行为范围。

[evidence/original183-binding-preservation.json](evidence/original183-binding-preservation.json)逐原183绑定保存并核对batch、required IDs、basis和authority；当前拆分扩展191绑定=17接受+174待核。保留的是绑定义务，未把接受扩成CLOSED或全轮完成。当前注册表与R1逐字节相同，仅U02/U03两事件、直接改源403/588。

44原组使用两个明确口径：原具体case为43 PASS/1 FAIL；当前扩大同根范围为39 PASS/5 FAIL。R1失败9组的原case转为8 PASS/1 FAIL（CK-DEP）。原35 PASS的具体修复保留，但COMBAT-05、WU-06、ROOT-TOOL-01/02在当前同根范围重开FAIL；没有改写旧报告，也没有把一条依赖缺陷重复算为多个分类缺陷。逐组详见[finding-results.json](finding-results.json)。

## 12项残留逐项裁定

| R1 issue | R2 | 依据及传播 |
| --- | --- | --- |
| COMBAT-R1-01 | PASS | 67纯反应父范围扣除L106，新769完整承担真实退出协作，野生决定3/训练家等待与回合末差异、世界/UI职责均保留待验证。 |
| DS-R1-003 | PASS | 261限定WP72§13四层120项；未泛化§7.4原个体编辑，147/148误依赖移除。 |
| CAI-R1-01 | PASS | 76/88/89/98/99/111共享准备、Prankster/GemConsumed、类别/SecretPower、正常清理及异常残留具名分责；不称纯查询或统一回滚。 |
| CAI-R1-02 | PASS | 86完整历史转META33，真实消费者/retirement/coverage同步。 |
| DS-R1-001 | PASS | 七metadata按实际37源组/105唯一消费者重核，world/Home/区域/地牢/训练家/活动/工具误号链修复，允许真实间接导航。 |
| DS-R1-002 | PASS | B17设施/培养与B20 TP/TE及形态门导航修复，静态NOT_EXECUTED保留。 |
| POK-R1-CATALOG-001 | PASS | 724真实消费未知效果回退FB01–06；未拿普通伤害数值替代变化失败。 |
| R1-CATALOG-WP-COLLISION | PASS | 16反向目录节清352条错误边，含728/730；真实81正向case保全。 |
| R1-CRE-DEP-001 | FAIL | 155/157/158/191已修；186/190退款错指WP42§7，192Mist期限错指WP45§7；完整57边又查出244/741。 |
| R1-KF-001 | PASS | META19六组合、META20完整40字段组、META21六边界及7目录节有真实消费者；不逐句新增ID。 |
| R1-KF-002 | PASS | 420 Mega生产点连接471，436编译/插件/主循环/Hangup/恢复用途正确；本域28依赖边完整复核。 |
| ROOT-R1-VIEW-01 | PASS | 全36父/39子/39边、旧29子集和67→769在范围栏有标签链接并可达；736行/33meta/8格全量投影一致。 |

完整case与28原失败ID、18 active、10 metadata记录见[issue-results.json](issue-results.json)、[feature-results.json](feature-results.json)及各agents报告，不把表中的概述替代逐项证据。

## 仍需修复的7项问题

所有JSON指针均指向固定a328，完整可复现证据和修正要求见[findings.json](findings.json)。以下功能编号统一省略`FR-000`前缀。

| 问题 | 等级 | 失败行/后果 | 必要修正 |
| --- | --- | --- | --- |
| COMBAT-R2-DEP-001 | P3 | 61/66/69→739，持物/离场HP/回合末错误连到仅招式与PP同步；完整98边中3错。 | 按实际状态消费删除或替换；68/71真实PP边保留。 |
| R2-CRE-DEP-001 | P3 | 186/190把正常终局退款交外层善后；192把Mist建立/期限交侧清理。 | 退款定位WP42§6/6.0及31；Mist定位WP45§6.2及39。外层治疗不是主动药品治疗。 |
| R2-CRE-DEP-002 | P3 | 244礼物四层工具误连263/265六类PBS编辑器；741奖金统计误连421货币组。 | 按真实工具族删改；奖金得失在420战斗统计组；742真实训练家共享编辑器可保留。 |
| POK-WORLD-R2-DEP-001 | P3 | 20行仍保留异体系/错节依赖，详下表。 | 对照完整有效scope逐边删除/替换，真实共享/间接导航保留。 |
| SOURCE-R2-001 | P2 | 旧accepted回执可授权同路径后继未接受字节。隔离908后继WP04新增一句，重算真实identity/locator，保留旧回执，`routing.errors=[]`。真实当前908/33目标无身份失配。 | 接受资格必须绑定当前实际内容身份或明确receipt-bound范围差分；不能仅路径存在/祖先关系。补陈旧回执负例。 |
| SOURCE-R2-002 | P3 | backfill `.get(default)`保留1776个显式null，未来current coverage schema要求非空字符串；独立合成908schema检查1776错误。 | 合理建模null或规范化并在写核心文件前验证完整 prospective output。真实2704未执行。 |
| SOURCE-R2-003 | P3 | 任意行为节用`ALL_FORMAL_FEATURES`可清空两消费者数组而通过新current checker；WP39§4隔离探针返回[]。 | 豁免限定固定治理文档身份/明确标题，其余行为节拒绝空映射，增加普通行为标题负例。 |

| Pokémon/世界/UI失败行 | 实际错引用 |
| --- | --- |
| 348 | 地牢图块→355音频 |
| 372 | 世界天气→355音频/358战前过渡 |
| 373 | 天气粒子/色调→33战斗中止/355/358 |
| 487 | Shadow成长→25/26换人逃跑失败/配置 |
| 608 | 图鉴显示搜索→670背包入口 |
| 664 | 盒子操作→157/158伙伴参战/战后治疗 |
| 681 | 经验升级UI→25/26 |
| 682 | 捕获接收UI→157/158 |
| 749 | 净化室→157/158/172脚本交换/667图鉴Forms |
| 751 | 雷达摇草→358战前过渡 |
| 754、755 | 世界成长/奖金持物→25 |
| 756、757、759、764 | Safari回起点/捕虫计时/活动退出/失败回程→650训练家卡独立场景 |
| 760 | 树果地图/闪光→358战前过渡/643保存退出 |
| 761 | 种植采摘→186战斗用物/650 |
| 762 | Repel世界再次使用→186战斗用物 |
| 766 | Voltorb翻牌→699 Slot转轮 |

753的作者诊断/语言导航、744的名人堂训练家数据卡、741→579→excluded755、Demo BoxLink经父子导航可达均有真实用途，已保留PASS。没有把“非直连”一概判错，也不因错误incoming而把目标行倒扣FAIL。捕获、背包战斗用物、逃跑、战中成长继续按三方协作候选评估，没有仅凭篇名整篇交Showdown。未知异常仍为源事实与原型待验证，粗标不强求先执行原型。

## 静态工具及阶段资格

在独立干净Git fixture逐字节复制候选，运行未修改作者`run-author-checks.py --phase r2-fixed-source`：7命令全exit0，13输入hash稳定且等于候选；27既有结构负例、9自检、2导航负例、11生成文件一致、12保全通过。使用干净fixture是因为保全器扫描所有untracked路径，隔离审查文件会被误当作者变更；未弱化保全检查。完整I/O见[evidence/replay-actual-command-io.json](evidence/replay-actual-command-io.json)。

root另独立核全部view投影、父子锚点和current范围。作者首次freeze的5项真实错误仍在输入证据中；修后通过不抹去首次失败。全部54个R1→R2改动路径限于routing目录；candidate身份清单84非自身文件+manifest共85文件逐项bytes/SHA/blob/mode/行数核对，R1报告73输入逐文件与固定8c8相同。

独立重放prepare exit0；apply因6个未接受U04正式文件真实exit1，三核心hash未变。736 prepared locator、49 changed-unit ID及21新标题映射独立重算相等；八批33实际目标身份相符，6个实际写集扩展纳入资格。21标题消费者逐项为合理的**准备建议**（11 accepted-source、10 pending-U04），不计入current2683。

UI65 U01只接受§3.1/§4.1，未转授U04 §6.1/§8.1；645/647待同步保持。未来5项真实扩展/共享接受回归与真实current2704全量检查均 **NOT_EXECUTED_AWAITING_U04**，未混入7命令PASS。独立合成JSON/Git负例只证明三项具体工具缺陷，不声称运行了真实2704验收。

只执行Markdown/JSON/Python schema/Git静态工具；Ruby、参考游戏、业务向量、宿主、Showdown/框架原型运行0。输出格式检查的144条空白提示全部为原样Git patch的单空格上下文标记，逐行验证并保留，不改证据求通过；其它报告/JSON/代码的`git diff --check`全通过，详见[evidence/output-whitespace-check.json](evidence/output-whitespace-check.json)。

root审计首次因二进制gzip的`lines:null`误作UTF8失败，已修审查脚本，第二次全量检查通过；源分工隔离探针的构造/归一过程与早期缓存清理亦透明留证。完整2150条原始静态命令日志以gzip保存，原始157,272,665字节的SHA和无损回读证明见[evidence/static-command-log-identity.json](evidence/static-command-log-identity.json)。

## 输出、保护与后续验收

逐行结果、逐组两层结论、131阅读台账、2683章节、7问题、根证据及各领域报告全部在本独占review目录。source事实、current应用、未来计划、去向验证、实现、验收及阶段批准保持独立。全部去向待验证、实现/验收未完成、阶段未批准，排除0；XP工程/特殊玩法/工具范围仍待用户决定。

[evidence/protection-final-precommit.json](evidence/protection-final-precommit.json)记录正式正文diff空、参考仓库clean及远端main/作者/R1报告引用；本报告提交仅新增本review目录。`output-file-manifest.json`为输出字节清单；`publication-proof.json`为首次报告提交从全新无alternates对象库逐文件远端回读证据。最终提交另在交接中给出精确SHA及再次远端回读，不制造包含自身未来SHA的循环证明。

下一步是修复28行依赖和3项工具缺陷，冻结新candidate再独立复核；U04正式接受后再实际累计回填、运行5绑定回归和2704完整检查并复审累计源。四个目标行为原型、用户范围/阶段批准、执行配置权威echo均仍独立待办，不能由本次静态PASS代替。当前结论为 **FAIL**，不是全部上游最终验收。
