# R8-U09 独立候选复审

结论：**candidate PASS_SCOPED，7/7**（2 required、5 已采用 optional）。未发现需要候选返修的语义问题。只授予固定候选的静态语义门；**actual integrated PASS 未审，ACCEPTED/CLOSED 未授予**。父协调任务：`01a14a04-b178-7567-a4eb-0f0bfac9a0d9`。

## 固定输入与独立性

- 仓库：`y805939188/pokemon-essentials-clean-room`。
- 候选：`6fddcf1af27169cdd31eabf42cc947b3424f18f8`；tree `73f9899227a39e2205e914c379047b657b8174cf`；mirror tree `2ebaaa2d8e14d138e4555e704a18ab0966379fba`；分支 `revise/r8-u09-20261017`。
- 唯一父提交/基线：`4575e80d041ab0c74a42e2e36399d05791dbaa5b`；tree `e8fb0884694afee309c57504babf9f849a5f1498`。
- 参考：`y805939188/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 语义 core：`2460370f1e410bd49cc29e377b89662838aed2b3`；正式规格 subtree 保持 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。
- 本次证据分支：`review/r8-u09-independent-20261017`。报告不自填未来 enclosing SHA；实际发布身份由后继回读证据及最终交付绑定。

本次为新委派的非作者审查。主审负责七项合同接收、授权/历史资格合并、九对完整文本的远端身份与精确差异核验及报告发布；四个独立语义子上下文分别实读其受影响候选/基线全文与全部适用源/原提案/反证/消费者，另一个子上下文审计全局证据资格。MG审者另启一个只读反方。已知本次共7实际context，不是7个历史根或重复票。源 FULL 信用只归实际reader，主审不继承其 FULL。

请求为 gpt-6.1-sol / ultra / default / normal / Fast off；模型、effort、tier、speed、Fast均缺权威运行回显，逐项 **UNVERIFIED**。选定执行环境在container_creation阶段失败；已通过连接的GitHub接口完成静态读取和普通Git对象/分支发布。没有shell、Ruby、编译器、游戏、业务替代模型或真实保存回放运行。

## 逐项裁决

| ID | 分类 | 结果 | 候选位置 |
| --- | --- | --- | --- |
| GR8-PBS-EGGGROUP-DOMAIN-001 | required | PASS | WP03 §6.2/L313–339/383；WP18 §3.1/L56–58 |
| GR8-CRE-MG-NAME-CANCEL-001 | required | PASS | WP64 L127–128；Creature catalog MG-32/L127 |
| GR8-UI-003 | optional | PASS | WP66A L145 |
| GR8-EXT-CD-004 | optional | PASS | WP34 L158 |
| GR8-EXT-CD-003 | optional | PASS | WP26 L138 |
| GR8-CRE-WP31-UNKNOWN-001 | optional | PASS | WP31 L247/266 |
| GR8-PBS-SHADOW-TYPE-LEGACY-001 | optional | PASS | WP23附表 L228 |

### 1. GR8-PBS-EGGGROUP-DOMAIN-001

15精确身份/原标签与固定R一致；唯一WP03目录由WP18引用。Humanlike/Field接受，HumanShape/UnknownGroup登记前拒绝；base clear、forms clone及已登记前缀保持；DITTO+PICHU经Undiscovered先门仍为0。

最强反方及处置：可扩展、通用集合算法和源导航已存在，但不能唯一决定无扩展作者成员域；若整合发现真正已明确纳入的完整等价表，须合并/撤销重复目录贡献。

### 2. GR8-CRE-MG-NAME-CANCEL-001

六命名控制6/6静态接合；空返回且Yes才停止，非空原Gift的ESCAPE（含先删空）成功；No重入、Create初空、Manage非空替换、obtain_text前缀及三层不写均准确。MG25/29–32和邮件/领取链保留。

最强反方及处置：正确WP17可组合解释旧领域取消，但旧WP64未定义窄义且局部承诺相反；候选用返回值门消除歧义，不新增取消API。

### 3. GR8-UI-003

非蛋INFO未满级普通/Shadow均用当前普通exp进度请求128基准偶数舍入底条，满级不请求，不取saved_exp；心量/文字门和成长储存不改。

最强反方及处置：旧Exp区可合理限于数值区，故仍optional；本次有限澄清不升级required，不授像素观察。

采用理由：低风险理解收益：区分经验数值区与底条，避免将心量替换误读为删除底条。

### 4. GR8-EXT-CD-004

BR24→BR23仅一指针；BR23 N2末次PID后Owner首次读取、BR24首轮成功/N0不读不清均保持；无算法/向量/随机次数改动。

最强反方及处置：完整正文算法和相邻案例已自足，无required行为缺口；不否定有限导航修正。

采用理由：低风险验证收益：一处具名导航改正到现有末次换号/Owner对照。

### 5. GR8-EXT-CD-003

空收服存储正确归到录像记录战斗；回放仍按WP58 §6.2–6.4副本、实时依赖、正常终局/中止分层；不从helper推出普通设施捕获可达。

最强反方及处置：WP58已完整正确，交界表可用简称；所以仍optional，仅一行澄清，不新增回放覆盖。

采用理由：低风险理解收益：空存储归属精确，避免为回放虚增保护或隔离保证。

### 6. GR8-CRE-WP31-UNKNOWN-001

作者未知方法在当前species/form登记前拒绝；绕编译条目仅在实际严格查找到达时失败，guard/先成功可避后坏条；64身份/52意义组、None/Level/五检查/BE01–37和host未验证保持。

最强反方及处置：WP03/04已给拒绝，旧未定位没有承诺接受/静默；不建立坏运行数据新公共API。

采用理由：低风险理解/验证收益：复用既有enum合同，分开作者拒绝与绕编译可达错误。

接收边界：L266守卫按§4五类进化检查有限理解；action_after_evolution直接扫描自身无这些守卫。不得将候选扩成所有运行入口统一guard保证。

### 7. GR8-PBS-SHADOW-TYPE-LEGACY-001

原SHADOW显式special=true；有效装入原SHADOW/SHADOWRUSH且有效类型仍SHADOW，perMove=true物理/false特殊；Power55、PP0、自抗、默认未启用与战斗Shadow相性分层保持。

最强反方及处置：有限附表并未承诺逐字段重建全部备份，故不能升级required；PP0不禁止直接分类查询。

采用理由：低风险验证收益：补明确真实样本值及合法开关对照，避免误套省略默认false。

## 完整证据覆盖与保留

已接收根AGENTS、review-SKILL、当前reviewer-prompt/author-prompt共用前言及完整assignment、七条完整合同、完整readset结构、适用accepted-facts/history/policy资格、原5caff U09 prompt全文，以及各项原提案、真实非提出者反证、root裁决/最终canonical关系。七合同与author received-contracts逐对象相同。原33合同中的本批四项保留5caff原commit/path与C35恢复位置双身份；三新增项保留C35 delta原来源；本次读取位置不替换历史来源。

读集按本批适用范围处理：delta72中本批 **45完整单位＝WP31 13 + MG10 + SHADOW22**，均由具名非作者实际读完；另完成EggGroup完整必要源单位、UI源单元、九份候选及基线全文、WP17/WP33/WP58必要全文、BR/BE目录与邮件/领取消费者。其余27 delta及继承64 root inputs/8 companions中的外批业务对象保持导航和原资格，不冒称本次重新审查其它32根。详细range/blob/reader见[input-ledger.json](input-ledger.json)与[semantic-receipts.md](semantic-receipts.md)。

主审新做的文档检查：

- 九份基线268187B、候选271588B，逐份blob/bytes/SHA256与固定manifest一致。
- 从九份完整基线应用13处唯一精确替换，逐字复现九份候选；声明替换外全部内容保持。
- 完整mirror远端tree无截断，恰9个普通文件；覆盖层缺席文件不表示删除。
- 共享Creature catalog仅MG-32一行变化；127个原ID及顺序保持：EG20、EN32、FC17、TT26、MG32。MG25/29/30/31及Factory/Triad/E旧贡献保持。
- 基线到候选compare仅本批26个新增文件（9 mirror +17 author证据），没有正式规格、main、原报告、公共索引变更。
- 作者artifact seal中25个非自身文件的全部字节与SHA256均独立复核匹配。

这些是TOOL_VALIDATION，语义裁决来自逐项源/条款/反例接合。未重跑作者42检查，未将22个静态control当业务执行；六MG命名控制6/6为静态推导。

作者阅读记录仍有资格限制：80 events及14份全文回顾性声明不证明所有报告载荷均由作者实读；AGENTS显式事件和MG236–428作者FULL未证。作者MG窄范围声明未冒称428行。本次非作者实际读完整MG1–428并补齐邮件根资格、21730B修正伴件及12源完整单位；**不能倒填作者FULL**。这不构成当前候选的残余语义缺陷，也不给作者全流程合规背书。

INFO控制覆盖普通/Shadow、旧经验5959对应20级/宽64、旧经验5460宽0、满级不请求、saved_exp区别、初绘后BACK及失败前缀；不授像素观察。SHADOW控制保有效装入、有效类型、Power55/PP0、true/false直接分类、未知Type只在实际查询到达失败；不授备份默认启用或所有组合支持。WP31保64身份/52意义组、None/Level/guard/先成功及BE01–37；不从故意坏数据推新公共输入域。录像helper条件诊断与普通产品捕获可达性分开。

五optional均有具体、有限的理解或验证收益；未替其它5 optional作选择，独立视觉policy未选择。UI003仍为`GR8-UI-003 → GR7-M13-002 → R6-UI-PARTY-003`。全球39/29/10为原修订条目口径；旧PASS/OPEN/WAIT/UPDATE_NOT_STARTED按真实生成时点保留。本次不重开旧关闭或新增历史根。

旧执行资格继续保持7数学/有限证书过程+1环境探针；旧PBS摘要1的原ID/I/O/exit/OS UTC为UNVERIFIED、alias_UNRESOLVED，不能另计第8数学过程。本次新增业务运行0；可得材料没有伪装成limit。

## 未决依赖与接受门

本批直接/传递语义编辑前置均0，候选语义阻塞0。剩余为：

1. R8-INTEGRATOR按局部贡献合并共享整文件并冻结真实actual commit/tree；尤其WP03/WP18及共享Creature catalog不能以本镜像整份覆盖他批贡献。
2. 实际非作者读取实际整合受影响全文、跨批贡献及累计保留，单独裁actual integrated PASS。EggGroup若找到已明确纳入的完整等价目录，须实际核验并合并/撤销重复贡献。
3. 主审随后独立登记ACCEPTED和CLOSED；公共audit/planning同步仅由唯一writer按精确贡献决定。

证据传输成功、candidate PASS都不等于实际整合或正式接受。本审仅写本批独占review证据；不改候选、正式规格、main或原报告，不force，不执行Ruby。
