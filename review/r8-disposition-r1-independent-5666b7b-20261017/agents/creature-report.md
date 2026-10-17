# Creature R1 独立复审报告

**限定结论：固定候选的本域依赖复核 FAIL。** 原7组中6组已修，CK-DEP-001仍有7项失败。116个旧功能为109 PASS／7 FAIL；6个追加功能均PASS，现122个活跃功能为115 PASS／7 FAIL。此结论没有宣称目标兼容、原型、实现或最终整改通过。

受审候选：`5666b7b912e2fb79b5119283ee6a37401a7071db`；旧候选：`d62b41f4d620e50bb04c80a7505374bd284d8210`；旧独立报告：`a0352c7fba38391afc535525988245701d5ce202`。当前正式来源：`908273093e1f6b27fc58249417675dd62d146224`。候选/旧候选/B8/R8正式树均为`f292698cdd4a8e725525a9be6dc34b75faaf151e`；当前908正式树为`6ae817df5b11eafdec671214b0d04e542ad364bc`。15份正文及3份相关catalog在这些固定提交中逐字节等同；本域没有U02/U03接受后的正文差异。

任务身份`/root/r1_creature`。父任务请求gpt-6.1-sol／ultra／default、Fast off；实际model、effort、service_tier、speed、Fast和云任务UUID均无权威echo，逐字段UNVERIFIED。只读参考SHA在独立仓库`/workspace/pokemon-essentials`核验；没有把clean-room对象库中不含参考对象当作浮动替代依据。

## 全量范围与方法

本域15份正文3634行／396011 bytes、3份catalog840行／146824 bytes；392个正文标题＋30个catalog标题共422个标题，122个活跃功能和158个section-metadata是不同分母。116旧ID各在active恰一次，完整source对象与旧候选相同；6追加ID为722、723、739、740、741、742。本域retired_features和metadata_records均0；另对128个正文及30个catalog元数据章节逐项给出结果，没有把零退役写成漏审。

完整读取旧本域报告、逐116结果、全部CK原finding及CC原finding和30个catalog章节裁定。新读取受影响完整源节/混合表格及必要消费者，18份本域源文实际新读2379行；其余正文信用来自固定旧独立完整阅读。每份文件均重新核Git blob/SHA256/字节；所有81旧PASS的去向、伙伴、理由、问题、原型、阶段等核心字段除新增职责字段外完全相同，新增共同前置按15篇完整依赖节核对；同根因影响范围另行语义重读。没有用作者finding-resolution或工具自检代替上述判断。

旧PASS149/150及各不变量/失败汇总，189融合道具的嵌套选择/场景重入，243礼物领取中的条件图鉴，206/207共享遗忘窗口等均检查传播。保留189/243的框架主责：共享入口与具名UI消费者可以消费这些交界，不要求每次提示再拆ID。FR206的有效§6.3明确同时承战斗版与通用版遗忘包装，其MZ满槽/放弃重试/选择职责可与FR207的战斗同步协作；未要求重复建MZ子项。

## 原7组裁定

| 原finding | 新裁定 | 覆盖及依据 |
| --- | --- | --- |
| CK-META-001 | PASS | WP27 §2.1/2.2全部恢复为722/723；框架数据缺省与MZ逐槽显示分开。 |
| CK-BATTLE-001 | PASS | 147/148/153完整父节扣出739/740/741；PP、可更新持物还原、金钱两阶段有具体各方职责及真实feature_refs。 |
| CK-MZ-001 | PASS | 15原case全部重读，具体框架状态与MZ输入/取消/刷新/提示/事件交界已补；没有机械强拆粗行。 |
| CK-TOOLS-001 | PASS | 154正常装载与742调试新建分开；244编辑/导出具体分责，742/244均target_scope待决策并保专门用户范围门。 |
| CK-MIXED-001 | PASS | 235/236租借两屏与取消后提交、249/250 Triad手选/随机及repeat/trigger全部分责。 |
| CK-DEP-001 | FAIL | 原13case逐项：147/148/187/204/207/221通过；155/157/158/186/190/191/192有遗漏或错误依赖，详下。 |
| CC-CATALOG-F01 | PASS | 原8节共32条Duel695–698误边全部删除，真实35功能与Triad247–252保持；9c全文及Duel独立规则对照已读。 |

各原case、原问题证据、追加子项和受影响旧PASS依据完整保存在JSON的`finding_results`，均未仅抽样。

## R1-CRE-DEP-001 · P3 · FAIL

依赖校准仍把其它单元的具名交界挂到当前ID；补充一组有效路径和理由不能证明它是本行真实依赖。原始wp_refs/文档归属也不能替代准确消费者。

| 功能 | 候选JSON pointer | 独立失败依据 |
| --- | --- | --- |
| FR-000155 | `/features/144/dependencies` | WP24 L196直接规定WP15播放/暂停、WP16备忘恢复/清预置、WP67-A捕获成功等待；feature_refs空且direct_refs仍无三者。新增WP39“伙伴登记…”/WP41“伙伴换人”未说明音频用途。 |
| FR-000157 | `/features/146/dependencies` | 共同WP39现能承参与/布局，原遗漏部分已补；新增WP10“旧标记转换三个容器位置”却是储存迁移内容，与§6.2参与谓词/队伍段无关。 |
| FR-000158 | `/features/147/dependencies` | 新增WP23§8.1和FR749净化室编成/选择器与本§6.3伙伴战后治疗不相干。WP39可承部分善后，但WP42§7.1真实交接未作具名校准。 |
| FR-000186 | `/features/175/dependencies` | L112–122战斗登记/复检/退款仍无WP40/WP42/WP67-A或等效feature_refs；新增WP61驱虫再次使用、WP60种植施肥不能解释此战斗节。 |
| FR-000190 | `/features/179/dependencies` | 治疗/复活混合表仍无真实命令/阶段/UI具名消费者；新增WP21“进化/融合”不说明此族治疗用途，WP23前门引用也不能替代场内消费。 |
| FR-000191 | `/features/180/dependencies` | WP40登记及WP20同步已有覆盖，但新WP23§7/FR488香/净化/TIMEFLUTE不是本ETHER/ELIXIR/主动LEPPA/PPUP族；L220明列WP67-A选择返回仍无校准。 |
| FR-000192 | `/features/181/dependencies` | X道具/Mist/娃娃/笛/球需要实际行动、临时状态及UI交界；新增WP23“教学/糖果/香”和WP64“给予邮件”属于其它效果族，仍无对应WP40/WP67-A等。 |

必要修正：按稳定ID及真实完整源节重新校准这些边；音频补WP15/WP16/WP67-A，战斗各物品族给准确命令/阶段/UI或等效具名feature_refs，并移除或正确说明误挂的迁移、净化室、野外种植、香/邮件边。保留正确共享合同与已补的真实边，不用删正文或重编号解决。

必要消费者新读包括WP15 §6、WP16战前包装、WP39伙伴/善后/音频、WP40 §4.2–4.2.1、WP42 §4/§6/§7.1、WP50消费及持物阶段、WP67-A物品选择/成长/捕获、WP73-A训练家编辑/取消。准确区间及身份在reading_ledger。

## 新增6行与范围保全

| 追加ID | 裁定 | 独立依据 |
| --- | --- | --- |
| FR-000722 | PASS | §2.1完整字段和名称省略默认为框架数据输入合同；L45–63独立、新ID不复用。 |
| FR-000723 | PASS | §2.2三态/逐槽数量/图标遮挡有框架有效属性、MZ实际显示门，L64–72独立而不重叠。 |
| FR-000739 | PASS | §5.5具体划持久列表PP与战斗包装/关联/标识/非变身同步；refs29/191/204/207真实连接WP42/主动PP/成长学习；双原型未运行。 |
| FR-000740 | PASS | §6.4持物写穿/更新还原/捕获接收/伙伴错配具体分责；refs31/61/528/529/577对应WP42/WP47-B/捕获/WP50。 |
| FR-000741 | PASS | §4.4资格及两阶段奖金败款由战斗候选给输入、框架夹限统计、MZ实际变化提示；refs31/421/579是终局/货币统计/奖金标记真实消费。 |
| FR-000742 | PASS | §5.3完整正常/调试对照独立成MZ+框架候选，refs263/265承训练家编辑和取消部分提交；专门DEC及待决策范围门完整。 |

122条当前locator的区间、unit SHA256和文件SHA256全部独立核对通过，活跃功能区间两两重叠0。原source保持首次固定完整对象，父节当前有效范围按子源精确扣除；没有发现纯标题/证据空壳功能。

## Catalog、元数据和可读视图边界

158个section-metadata均为来源/概念/范围/依赖/证据/静态验收导航，非额外实现。9a/9b目录旧功能集合未直接追加739–742，但机器关系147→739、148→740、153→741、154→742由excluded_child_refs显式可解析，旧稳定source仍保原章节身份。HP26–34/PT12–16/PT32–34能够追达真实当前责任，因此对章节粗导航有限接受，不要求每个vector重复列每个子ID。9c各节保持其真实35消费者，原Duel误连修复独立PASS。

另交root的可读视图facet：父147/148整行仅说“排除下列独立去向/验收子单元”而没有739/740，且功能依赖为空；这两条机器正确关系在可读行未显示。153/154的末栏已经显式列741/742，作为反向对照不列同缺口。root统一评估共用生成视图；本域feature主裁定没有把该共用显示问题折算成分类/依赖FAIL。

## 真实阅读台账

下表为本次新读，未列区间使用经身份及字段差分审查后适用的旧完整阅读信用；不声称重读全部4474行。完整Git blob、SHA256、字节、旧报告定位及继承理由逐文保存在JSON。

| 固定908文档 | 本次新读行 |
| --- | --- |
| wp18-creature-identity-species-ownership.md | 373–377 |
| wp20-hp-status-moves-helditem.md | 121–256 |
| wp24-player-trainers-partners.md | 1–295 |
| wp25-party-and-storage.md | 103–220 |
| wp26-acquisition-gifts-and-script-trade.md | 45–208 |
| wp27-bag-and-item-storage.md | 1–223 |
| wp28-item-use-and-training.md | 47–408 |
| wp29-shops-and-exchanges.md | 45–107, 198–202 |
| wp30-growth-learning-and-friendship.md | 79–181, 273–277 |
| wp33-daycare-and-breeding-session.md | 44–106, 202–206 |
| wp35-eggs-and-hatching.md | 89–143, 184–188 |
| wp36-wild-encounters-and-modifiers.md | 276–280 |
| wp57-factory-rentals-and-swaps.md | 1–116 |
| wp64-mail-and-mystery-gift.md | 1–174 |
| wp68-triple-triad.md | 1–154 |
| creature-rpg-wp18-20-24-25-26.md | 48–171 |
| creature-rpg-wp27-28-29-30-33.md | 106–121 |
| creature-rpg-wp35-36-57-64-68.md | 1–183 |

## 逐旧ID裁定

旧81 PASS均维持有依据的PASS；35旧FAIL中28项已修、7项仍FAIL。每项具体reason、继承/重读方法、immutable source等同、候选pointer及finding_refs见机器结果。

| 旧ID | 旧裁定 | 新裁定 | 处置 |
| --- | --- | --- | --- |
| FR-000137 | PASS | PASS | active |
| FR-000138 | PASS | PASS | active |
| FR-000139 | PASS | PASS | active |
| FR-000140 | PASS | PASS | active |
| FR-000141 | PASS | PASS | active |
| FR-000142 | PASS | PASS | active |
| FR-000143 | PASS | PASS | active |
| FR-000144 | PASS | PASS | active |
| FR-000145 | PASS | PASS | active |
| FR-000146 | PASS | PASS | active |
| FR-000147 | FAIL | PASS | active |
| FR-000148 | FAIL | PASS | active |
| FR-000149 | PASS | PASS | active |
| FR-000150 | PASS | PASS | active |
| FR-000151 | PASS | PASS | active |
| FR-000152 | FAIL | PASS | active |
| FR-000153 | FAIL | PASS | active |
| FR-000154 | FAIL | PASS | active |
| FR-000155 | FAIL | FAIL | active |
| FR-000156 | PASS | PASS | active |
| FR-000157 | FAIL | FAIL | active |
| FR-000158 | FAIL | FAIL | active |
| FR-000159 | PASS | PASS | active |
| FR-000160 | PASS | PASS | active |
| FR-000161 | PASS | PASS | active |
| FR-000162 | PASS | PASS | active |
| FR-000163 | PASS | PASS | active |
| FR-000164 | PASS | PASS | active |
| FR-000165 | PASS | PASS | active |
| FR-000166 | FAIL | PASS | active |
| FR-000167 | PASS | PASS | active |
| FR-000168 | PASS | PASS | active |
| FR-000169 | PASS | PASS | active |
| FR-000170 | PASS | PASS | active |
| FR-000171 | FAIL | PASS | active |
| FR-000172 | FAIL | PASS | active |
| FR-000173 | PASS | PASS | active |
| FR-000174 | PASS | PASS | active |
| FR-000175 | PASS | PASS | active |
| FR-000176 | PASS | PASS | active |
| FR-000177 | PASS | PASS | active |
| FR-000178 | FAIL | PASS | active |
| FR-000179 | FAIL | PASS | active |
| FR-000180 | PASS | PASS | active |
| FR-000181 | PASS | PASS | active |
| FR-000182 | PASS | PASS | active |
| FR-000183 | FAIL | PASS | active |
| FR-000184 | PASS | PASS | active |
| FR-000185 | PASS | PASS | active |
| FR-000186 | FAIL | FAIL | active |
| FR-000187 | FAIL | PASS | active |
| FR-000188 | PASS | PASS | active |
| FR-000189 | PASS | PASS | active |
| FR-000190 | FAIL | FAIL | active |
| FR-000191 | FAIL | FAIL | active |
| FR-000192 | FAIL | FAIL | active |
| FR-000193 | PASS | PASS | active |
| FR-000194 | PASS | PASS | active |
| FR-000195 | PASS | PASS | active |
| FR-000196 | FAIL | PASS | active |
| FR-000197 | FAIL | PASS | active |
| FR-000198 | PASS | PASS | active |
| FR-000199 | PASS | PASS | active |
| FR-000200 | PASS | PASS | active |
| FR-000201 | PASS | PASS | active |
| FR-000202 | PASS | PASS | active |
| FR-000203 | PASS | PASS | active |
| FR-000204 | FAIL | PASS | active |
| FR-000205 | FAIL | PASS | active |
| FR-000206 | FAIL | PASS | active |
| FR-000207 | FAIL | PASS | active |
| FR-000208 | PASS | PASS | active |
| FR-000209 | PASS | PASS | active |
| FR-000210 | PASS | PASS | active |
| FR-000211 | PASS | PASS | active |
| FR-000212 | PASS | PASS | active |
| FR-000213 | FAIL | PASS | active |
| FR-000214 | PASS | PASS | active |
| FR-000215 | PASS | PASS | active |
| FR-000216 | PASS | PASS | active |
| FR-000217 | PASS | PASS | active |
| FR-000218 | PASS | PASS | active |
| FR-000219 | PASS | PASS | active |
| FR-000220 | PASS | PASS | active |
| FR-000221 | FAIL | PASS | active |
| FR-000222 | PASS | PASS | active |
| FR-000223 | PASS | PASS | active |
| FR-000224 | PASS | PASS | active |
| FR-000225 | PASS | PASS | active |
| FR-000226 | PASS | PASS | active |
| FR-000227 | PASS | PASS | active |
| FR-000228 | PASS | PASS | active |
| FR-000229 | PASS | PASS | active |
| FR-000230 | PASS | PASS | active |
| FR-000231 | PASS | PASS | active |
| FR-000232 | PASS | PASS | active |
| FR-000233 | PASS | PASS | active |
| FR-000234 | PASS | PASS | active |
| FR-000235 | FAIL | PASS | active |
| FR-000236 | FAIL | PASS | active |
| FR-000237 | PASS | PASS | active |
| FR-000238 | PASS | PASS | active |
| FR-000239 | FAIL | PASS | active |
| FR-000240 | FAIL | PASS | active |
| FR-000241 | PASS | PASS | active |
| FR-000242 | FAIL | PASS | active |
| FR-000243 | PASS | PASS | active |
| FR-000244 | FAIL | PASS | active |
| FR-000245 | PASS | PASS | active |
| FR-000246 | PASS | PASS | active |
| FR-000247 | PASS | PASS | active |
| FR-000248 | PASS | PASS | active |
| FR-000249 | FAIL | PASS | active |
| FR-000250 | FAIL | PASS | active |
| FR-000251 | PASS | PASS | active |
| FR-000252 | PASS | PASS | active |

## 状态、执行和剩余门

所有122功能均去向待验证、阶段待定/未批准、未实现/未验收，来源引文不是兼容证据。四类原型均未运行，实际Showdown commit/格式等仍待决；不以未知原型阻止正确粗标，也不把它们当已通过。33条本域批次绑定行仍待整改后核对，接受事件0；U05/U06/U09及MG31/32未被U02/U03接受回填扩大为ACCEPTED/CLOSED。

本收集脚本实际exit0，156条Git命令回执全部exit0，122个身份/范围检查全PASS。此前只读对象检查曾误在clean-room库查参考SHA并exit128，未写结果；改在独立参考仓库核验成功，未fetch或改参考。这里只执行Markdown/JSON/Git静态分析；Ruby、游戏、业务向量、宿主、Showdown及未来框架执行0，未切分支、提交或修改输入。

输出：[creature-results.json](creature-results.json)；可复现收集：[creature-audit.py](creature-audit.py)。schema/全体生成器/保护及接受回填两处实际差分由root整合。本域所列依赖问题须新固定候选复核；上游、用户范围和原型待办保留。
