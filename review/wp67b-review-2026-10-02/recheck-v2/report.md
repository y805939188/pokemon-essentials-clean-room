# WP67-B 修订 v2 有限复审

2026-10-02；静态证据及文本／身份核验。

**结论：REQUEST_CHANGES，当前仍不能进入WP37。原16项中11项CLOSED，5项PARTIAL；没有新增问题编号。** 剩余为R01、R02、R05、R14、C01，其中R05剩余仅数值表述，降为P3；剩余合计3项P2、2项P3。主要行为修订已接受，本轮只需收紧下面的附表引用、摘要前提和计数。

被审主稿：`de32309ac0bf9cf58f843583bb0b35d5cd8de26072d22cee0eaee81f6db35f11`／60,068字节；v2附表：`d782efb11a2279d4f509bef7f05024ef0664b5bcb885fa05b53712bf5d351427`／12,410字节。16份输入已固定，见[inputs.json](inputs.json)及其中对应[input-snapshot](input-snapshot/specs/ui/wp67-b-lifecycle-presentations-and-history.md)。

## 1. 已关闭与机械核验

| 项目 | 结论 |
| --- | --- |
| WP67B-R03 | 光标BACK退格、空文本OK与键盘Esc分开；空结果清昵称；L07与附表同步。 |
| WP67B-R04 | 两个直接入口的前序写入与演出内写入分开，计数归零归迈步侧；L09和附表两行一致。 |
| WP67B-R06 | 五层取消去向已分开，MOVE正常可达，SWITCH目标取消与详细菜单返回正确。 |
| WP67B-R07 | REPLACE原始空值/假值相等门及不经拒蛋门明确；L32与独立附表行一致。 |
| WP67B-R08 | WITHDRAW双满拒绝、只入盒、盒满队伍有位失败仍清源三分支正确，未混同通用领取。 |
| WP67B-R09 | 迈步入口先跳过零心量，正心量本步降到合格才提示，编成变化不补提示。 |
| WP67B-R10 | 外层无可战斗门、全队标注与选中许可分开；濒死非Lugia与Lugia例外、取消结果变量均正确。 |
| WP67B-R11 | 删除遗迹石恒真业务返回，保留场景收尾透传及底层具体值未证，与孵化包装区分。 |
| WP67B-R12 | TIMEFLUTE门错配、无净化提交但正常消费和香类三种消息分支均正确；L21与附表同步。 |
| WP67B-R13 | 中心独存SUMMARY不打开摘要与持握单成员分支、摘要返回游标均正确。 |
| WP67B-R15 | 三处被指出的源码赋值/创建语句已改行为文字，新回应未重抄这些语句；字段值对照与审计标识不当作源码抄录。 |

登记第九十七轮／TSV v72核验通过：manifest §1的1,161条完整身份＋2条旧无哈希行、TSV的1,066条唯一记录，完整哈希／短标签／字节均与磁盘一致。两份diff分别按冻结v1严格重建主稿与附表，10及4个hunk均精确匹配，未执行作者校验脚本。旧§2／§3／§4仅插入、标题和历史保留；既有文件仅主稿、矩阵F16-06、manifest、主TSV四份变化。

34个场景定义唯一、原L01–L28全部保留、新增L29–L34；入口附表34行计数正确。**唯“旧场景改7行”不符实测，见C01。** 登记文件身份正确和这一描述性计数错误分别判定。详见[registration-checks.json](registration-checks.json)。

26份依赖规格、10份批准依据、上轮审查材料、21份先前实读来源及37份起始来源身份均保持；合并40份不同来源对HEAD核对一致。reference固定`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`且Git清洁。WP67-A累计17项、WP65八项、GR-001～016、WP23-N01等旧结论保持关闭；WP23跨级失败和WP32-N02宿主未决未重开。

## 2. 五项剩余修订

### WP67B-R01 · P2 · 满级糖新增行改变了附表中“同上”的指向

位置：[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:10](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:10>)；[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:11](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:11>)；[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:12](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:12>)；[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:13](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:13>)。

**已接受**：默认开启、无等级变化的独立入口、取消仍成功消费，以及L29均已修正。

**剩余问题**：新增满级糖行的“状态写入／返回”单元现在只有“配置关闭或无目标→无效提示、不进演出、不消费”，但紧随的进化石行仍以“同上”作为该栏内容，战后与事件行又连续“同上”。这已经不能明确指向第一行的成功提交序列，反而把糖果专属配置/失败条件带给其它入口。首版原先的相对引用在插入后失去原含义。

**最小对照**：将满级糖配置关闭，另选非Shadow且能用所选进化石进化的成员：石的入口仍会进入不可取消演出，完成后按道具系统消费；不能因糖果配置关闭而产生糖果无效分支。

**修订范围**：将这三行状态栏改为明确的共享进化成功提交序列引用（或短写该序列），分别保留自身取消/返回/消耗规则；不要借用满级糖配置。升级工具入口可明确保留非满级稀有糖调用者，避免新增满级入口时丢失普通路径。无需改已正确的L29。

来源：[reference/pokemon-essentials/Data/Scripts/013_Items/002_Item_Effects.rb:388](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/013_Items/002_Item_Effects.rb:388>)；[reference/pokemon-essentials/Data/Scripts/013_Items/002_Item_Effects.rb:922](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/013_Items/002_Item_Effects.rb:922>)。

### WP67B-R02 · P2 · 交换图鉴附表仍未限定“同进化”只共享显示门

位置：[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:15](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:15>)；[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:33](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:33>)；[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:34](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:34>)。

**已接受**：主稿§3.3已准确分列三类后续，并说明候选列表不等于实际学到的数量；L30与孵化附表行已修正。

**剩余问题**：“收到者图鉴”行仍将可见流程写为“新种条件页同进化”，没有说明只共享四个显示条件，也未写交换页内收尾。该表的进化页行现在明确按待学列表空/非空分两种收尾，所以无范围限定的借用仍会混入错误条件。下一行仅把WP32-N02风险挂在“自定义条目”后，也不能替代交换图鉴页本身的收尾合同。

**最小对照**：交换收到者无交换进化目标，但此前未拥有且其它图鉴门全真：仍存在页内不淡出收尾与外层通常收尾；不能因没有待学列表而套进化的列表分支，也不宣称宿主一定安全。

**修订范围**：在收到者图鉴行注明共享的仅是配置、此前未拥有、持图鉴、已解锁四门；交换只要实际打开条件页，页内就有不淡出收尾，外层仍有通常收尾，不检查进化待学列表。保留WP32-N02宿主未决，并说明收到者无交换进化目标也存在这两个调用位置。

来源：[reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb:232](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb:232>)；[reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:157](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:157>)；[reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:198](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:198>)。

### WP67B-R05 · P3 · 附表2.5秒旁的换算符号写反

位置：[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:32](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:32>)。

**已接受**：正文、L10和附表的2.5秒自然推进、USE/BACK提前推进及不撤销交换均已修正。

**剩余问题**：附表括注却写成“50逻辑单位×20/秒”，与同一单元格的2.5秒结论不相容。50个单位在每秒20单位的速率下应相除；此处是剩余的数值表述错误，优先级收窄为P3。

**最小对照**：数学核对50÷20＝2.5；正文、场景、附表使用同一时长与按键提前推进规则。

**修订范围**：改为“50个逻辑时间单位÷每秒20单位＝2.5秒”，或直接删掉换算括注而保留已正确的2.5秒行为。不要改成按宿主实际帧率换算。

来源：[reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:179](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:179>)；[reference/pokemon-essentials/Data/Scripts/007_Objects and windows/011_Messages.rb:805](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/007_Objects and windows/011_Messages.rb:805>)。

### WP67B-R14 · P2 · 上限0“裁空并失败”的摘要漏了原记录为空前提

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:187](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:187>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:200](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:200>)；[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:64](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:64>)；[review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:65](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/entry-coverage-table.md:65>)。

**已接受**：§7.1的详细条款和L33正确写出了“从空数组/编号0开始”，这一路径的编号、PC门和静态失败点正确。

**剩余问题**：§9、§10及附表两行却省掉该初始状态，重新概括为上限0就裁空、PC进入必在空记录处失败。来源每次只删除最早一届，不会清空既有数组。例如配置变体下原已有一届非空记录A、编号1，本次登记非空记录B：追加后只删A，留下B、编号2；PC仍可取到B，不会因最新记录为空而在该处失败。

**最小对照**：对照L33：上限0、已有合法非空记录A、编号1、非空正常队伍生成B、资源正常；登记后历史为[B]、编号2，PC读取B，不触发“最新记录为空”的这处错误。该输入是有界配置/既有记录对照，不冒充默认新游戏。

**修订范围**：把所有“上限0→数组空→PC失败”摘要明确限定到原历史为空（完整L33还取原编号0）的前提，或直接引用L33该前提；补已有记录A的最小对照，保留一次只删一届。只修本包，不扩展存档迁移规格，不改参考清空记录。当前§7.1/L33正确内容保留。

来源：[reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:120](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:120>)；[reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:77](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:77>)；[reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:178](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:178>)；[reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:452](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:452>)。

### WP67B-C01 · P3 · 附表总数已正确，但旧场景改动行数应为6而非7

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:279](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:279>)；[review/wp67b-delivery-2026-10-01/revision-v2/delivery-summary.md:7](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/delivery-summary.md:7>)；[review/wp67b-delivery-2026-10-01/revision-v2/revision-response.md:12](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/revision-response.md:12>)；[review/wp67b-delivery-2026-10-01/revision-v2/checks.json:131](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/revision-v2/checks.json:131>)。

**已接受**：v1附表28行、v2附表34行及七组8/5/3/10/4/2/2均独立核实正确；34个场景定义ID唯一。

**剩余问题**：交付摘要、回应、checks、末检和主稿v2注记一致声称旧L01–L28有7行修订。逐行比较绑定的冻结v1与v2后，实际只有L07、L09、L10、L14、L20、L21六行发生变化，另外22行逐字相同；L29–L34是六个新增ID。原覆盖计数问题已修正，但本轮同一计数自检材料仍留一处误报。

**最小对照**：程序化得到：旧定义28个＝原样22个＋修改6个；新增6个，总定义34个。附表数据行另计34，不能混用两个计数。

**修订范围**：在v3当前有效说明中纠正v2改动计数为6，列实际ID；v3自身修改/新增案例另按v2基线实测。旧v1/v2冻结材料与旧manifest历史保留，在新回应中更正，不覆盖旧交付。不要为了凑7行修改无关案例。

证据：冻结v1与当前v2的案例逐行比较，完整结果见registration-checks.json。

## 3. 下一步

按[next-task-prompt.md](next-task-prompt.md)，由原提取方仅修上述五项，交付WP67-B revision-v3后停止送复审。11项关闭结论保持，避免再全文重写；只有受影响的句子、附表单元、最小场景对照和当前材料说明需要变化。所有v1/v2旧交付与独立review材料留史。

本reviewer只新增本目录文件并固定输入；未改主稿、上游或reference，未执行游戏／UI／演出／行为模型、真实存档或媒体，未创建任务／Agent、未发跨会话消息、未提交／推送。未启动WP37或整体double review。
