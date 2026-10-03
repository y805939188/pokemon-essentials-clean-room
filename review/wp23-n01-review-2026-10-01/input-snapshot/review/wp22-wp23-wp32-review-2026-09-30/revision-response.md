# WP23三项修订、N01同步与WP22／WP32回填回应

2026-09-30；提取方。依据[独立首审报告](report.md)（`e97d0e677d71e3e6179e483d84e215b835fc46243cb1ed1a6b3e33bcaddc919c`，15,276字节）与[revision-prompt](revision-prompt.md)（`84bbaff63954ce96269440aee9c6124dab18b6bf259664c05c9342a11d4d30b7`，9,071字节）。**R01～R03均回源核实成立并修订，WP23仍ReviewPending；WP22／WP32按已获PASS_SCOPED管理回填。** 本回应不是独立复审或自行判CLOSED。

## 1. 固定预检与适用性

报告§1全部13项完整SHA-256／字节、876项磁盘输入与876项input-snapshot、current-hashes.tsv和输入JSON完全匹配；本轮reviewer列出15件及final-checks原件均保护。上一轮828及更早806／782／755／734／707／677／644／613／589／548／521快照与各轮已列原件匹配。预存18,342个非Git文件留有完整哈希基线；没有报告固定后的额外变化，未覆盖或回退他人工作。

reference仍为`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，普通Git状态干净。预检见[revision-v2/preflight-checks](../wp22-wp23-wp32-delivery-2026-09-30/revision-v2/preflight-checks.json)。只运行自有文本／哈希／集合／固定算术检查，未运行参考Ruby、游戏、UI、网络或旧交付写入脚本。

## 2. WP23-R01（核实成立）

实际回读：Chamber:348–628、582及1073；Other:17–58／119；Items:132–220；Pokemon:199–206；GrowthRate:78–82；PBS RATTATA:469–475。全Scripts查找仅一处PurifyChamberScreen定义，未见同名顶层更新方法、重开或method_missing转发。Screen与Scene两个接收者明确分开，遗迹石Screen的空更新方法形成对照。

- 主稿§6.2改为分入口提交／失败表：跨级先设等级／能力与升级分支友好，在首个能力变化窗口调用所传Screen更新时缺方法失败，早于确认键检查；不能到达后续学招／进化、精确最终经验、命名、存放或清中心。
- 失败前净化统计、Shadow／Hyper清除、缎带、原招恢复／首招、V恢复并清V、清S、等级赋值／能力重算及升级友好均已经发生；无回滚，中心仍引用已部分改变的对象。
- §7净化室、§8.3领取与O03补“确实到达存放”的前提；同等级恢复（包括S0）不进该窗口，遗迹石有空回调，不共享缺方法点。W24限定遗迹石可到达取消点；W38／W39限定S0同等级及前序呈现正常。
- 新增W43–W45与附表固定向量：默认RATTATA Medium、L10／E1000、G0、S416、V有效。独立常数算术得请求332、目标E1332，1331≤1332<1728；实际等级设置先写下限E1331，窗口失败后仍是1331，未精确写1332／未存放／未清中心。S0和遗迹石对照分列。没有执行等级工具或UI。

已审WP30等级工具规则未改；没有给参考Screen补方法，也不将此固定失败泛化为所有净化入口均失败。

## 3. WP23-R02（核实成立）

回读Shadow:100–102、Pokemon构造1159–1225、Other:20、Chamber:361–395／497–507。构造没有初始化Shadow字段、查询可返回nil；净化明确写false；替换直接比较原始返回结果，普通放置仅按真假分支。

主稿§8.1、W33／新增W46及附表、当前O04概括已同步：nil／nil通过该门、nil／false拒绝、false／false通过；“都非Shadow”不等于两个原始值相等。非Shadow蛋替换例增加原始结果匹配前提。没有把这项门当作全部操作成功保证；缺蛋／最后可战斗成员守卫等已核实部分保持，不改WP25旧规则。

## 4. WP23-R03（核实成立）

回读Other:201–213、Shadow:104–105、Battle:93、RubyUtilities:366–387，并核对已审WP55§2.5／第87与124行数值0合同。普通默认Battle把数值0交给原始数值随机，得到[0,1)浮点；M4000的阈值1000包含整个区间，无需抽样就能判定分支。

主稿H01、W12、未决与附表／self／boundary已补：其余进入门通过时写Hyper存储标志真、请求进入提示；有效查询因G0仍假，同前提后续调用可再次写入／提示。正G的1001/4000公式保留；自定义小M、插件／改写随机、回放输入不套本默认分支，U05跨宿主／跨实现边界不关闭。

## 5. N01实际同步；N02保留

N01回读Move_Usage:294–304与Battler_UseMove:669–675确认无目标阵营门，替身不早退，画皮／结冻头早退。只改WP31旧第114行“对对方”的条件摘要为本场实际记录次数、目标范围引用WP32具名规则，并加批准同步尾注；全文件同一错误概括仅此一处。基础阈值、提交、取消及旧关闭编号不改，WP31继承原限定Reviewed。

旧WP31完整身份`0b40917c3a0c9b942f004dd5fb6bc75addf749d154e162e75e06a2f001806d91`／39,554字节保留；新身份见§7。真正引用完整身份的WP23／WP32依赖表及活动fixed／self／boundary级联；没有全局替换历史哈希。WP31单点行为差异单独为wp31-basic-evolution.diff；WP23／WP32的引用变化在各自文末身份表，可与WP23自身R01～R03修改及WP32纯管理回填分开审计。

N02按独立结论CONFIRMED_STATIC／RETAIN_RUNTIME保留：两个收尾位置静态已确认，第二次viewport释放是否继续仍未决。未改WP26，不宣称必然双进化、必然异常或运行确认。九项观察的当前处理记录已同步；O03到达前提、O04原始值相等与本轮R项不混为已获复审关闭。

## 6. WP22／WP32管理性回填

两包主附表头尾分别回填**Reviewed（限定静态范围，2026-09-30独立首审PASS_SCOPED；管理性回填）**，范围严格继承报告§4。WP22为A～F个体／战斗分层、Primal、还原与默认数据；WP32为A～F情境／记录／世界通知／队伍移位／交换与事件静态合同。N02运行、U01／媒体／插件等不包含在回填范围；WP32引用WP23只限已核实交界，不表示WP23整体通过。

F06-08单列WP22限定Reviewed与WP23修订v2 ReviewPending，F09-04为WP32限定Reviewed，前向Inventoried保留。WP23→WP22、WP32→WP22／WP23和WP31必要身份引用均用实际最终字节，WP23明确“批内修订稿，尚未外审”。两包其它已接受行为未改。先前WP62／WP38及C03已获受理，本轮没有再编辑那些规格或旧回应。

## 7. 被审与当前身份、差异

| 文件 | 本轮被审／固定输入SHA-256（字节） | 当前SHA-256（字节） | 分类／差异 |
| --- | --- | --- | --- |
| `specs/pokemon-rules/wp22-mega-and-primal-reversion.md` | `c3f4130c8a755361426f20e60485d2f76a937abd7fb18d1e8833a677a6091099`（24,859） | `894fa8e0d18dc7a5823e8c51b85cefd23f9f955b08fde6a7621533a48b8302f3`（25,402） | 纯管理回填：头尾状态／范围／被审身份；无行为变化；[diff](revision-diffs/wp22-mega-and-primal-reversion.diff) |
| `specs/pokemon-rules/wp22-transformation-data.md` | `e2b3943a4c7d0c0d820171217b5058e7649da55534bd5e5337363e3bbfc3335c`（6,027） | `310956bf2c308626f3035b86fd256e35e68fdc58d340c3d941e07f8cdc9a03e3`（6,410） | 纯管理回填：头尾状态／被审身份；数据未改；[diff](revision-diffs/wp22-transformation-data.diff) |
| `specs/pokemon-rules/wp23-shadow-hyper-and-purification.md` | `cd8b5e244e181bf8c57e483f0364ac315457b9292c9d003523c9a030e79d1c19`（34,418） | `1a11060e2a1a2c37052734fb8d264655f8179ec6bca0d122cbc07b8afafe6f4c`（40,939） | R01–R03行为／失败／场景；WP22／WP31纯身份引用另列于文末依赖表；新增WP55合同依据；[diff](revision-diffs/wp23-shadow-hyper-and-purification.diff) |
| `specs/pokemon-rules/wp23-shadow-data-and-vectors.md` | `416ac4110b8eac8b0e05858f381144c24ae893cb8ad0303854eda1c323cb5d15`（12,071） | `afeab7580e39bc0a0dc78d3d6ae13f9f0e4db321101dc78600452670b0888abe`（13,534） | R01–R03固定向量／前提及修订状态；原数据目录未改；[diff](revision-diffs/wp23-shadow-data-and-vectors.diff) |
| `specs/pokemon-rules/wp31-basic-evolution.md` | `0b40917c3a0c9b942f004dd5fb6bc75addf749d154e162e75e06a2f001806d91`（39,554） | `8ea81dcefff940ff6232db1268cc908a8dd6f1d344070786ec8e411dd74ac155`（40,087） | N01批准的单点行为摘要＋维护尾注；不改其它主规则；[diff](revision-diffs/wp31-basic-evolution.diff) |
| `specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md` | `480879bd8eb777938c301a8241dff4e16f4990378543b47fddb2e9af0a2f76de`（29,515） | `931c8b05f580bea154e68e8134c7c51a4714c4ebad58523af5c57056320fd193`（30,346） | 管理回填＋N01实际同步状态；WP22／WP23／WP31依赖表纯完整身份级联；N02行为未改；[diff](revision-diffs/wp32-contextual-trade-and-post-battle-evolution.diff) |
| `specs/pokemon-rules/wp32-context-inputs-and-scenarios.md` | `869cbbaafb6dab2c9bd2da0c2711a7443b2ae88b8007e238f5c156acc53c498d`（9,798） | `5ae30fa1105776063a7455ff41ffbecc41a984a0a9482a5a6970f190063d8ca0`（10,203） | 纯管理回填；数据与场景未改；[diff](revision-diffs/wp32-context-inputs-and-scenarios.diff) |
| `planning/feature-matrix.md` | `a3d2b53960307f6b51244e1c4c97554cddd1f192cc9387fe5751292a6bb32a07`（55,829） | `ff645588705c714a8acc69295ad5d201b85e39717562a7ac158fb24220b331bd`（56,091） | 仅F06-08／F09-04分范围状态；[diff](revision-diffs/feature-matrix.diff) |

17份新差异均相对**本轮首审input-snapshot**并绑定最终目标，不是中间版本；完整基线／当前身份及分类见[diff-bindings](../wp22-wp23-wp32-delivery-2026-09-30/revision-v2/diff-bindings.json)。没有空diff。旧六份回填diff与其bindings保持原件、仅核对到本轮首稿快照；未将旧中间目标冒称本轮当前。manifest／TSV按既有追加历史方式续记，检查结果文件属于本轮测量输出，不制造自身差异哈希循环。

## 8. 登记、验证与停止

manifest§1／§2.1／§3／§4续第六十四轮，主TSV续v39，补登本轮reviewer16件、此回应／17份差异与修订审计材料，保留原874／778行及完整历史替代链。当前场景25／46／38＝109；46条依赖绑定（新增WP55已审随机合同依据）；来源66文件身份（补RubyUtilities、GrowthRate及此前未登记的Battle文件，只对本次具名段作语义复核）。

最终全量身份、字节、短标签、JSON／链接、差异重建、876项预期修改白名单、旧原件／快照与reference固定状态见[validation-results](../wp22-wp23-wp32-delivery-2026-09-30/validation-results.json)。自有脚本只处理文本／哈希／集合／固定算术；没有执行参考模型、真实地图／存档／输入／网络，没有实现框架。

**完成本次三项修订、N01同步、两包回填及必要身份级联后，备妥有限复审并停止。** 不启动主线下一批，不接管用户另行安排的独立任务；未创建Agent／任务、未发送其它会话消息、未提交／推送。Demo、宿主、媒体、插件、U01–U10和WP78→WP79→WP80出口保留。
