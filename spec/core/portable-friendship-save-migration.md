# 玩家存档的显式友好度迁移

本页描述可选独立框架的存档工具。它只在玩家选定既存存档并确认时，把所选成员显式保存的 `friendship: 256` 改为 `255`。普通读取、标题画面和继续游戏均保留旧值。原版的成长与友好度、存档行为另见[成长、学习与友好度](../creatures/growth-learning-and-friendship.md)和[存档、启动与继续](save-startup-continue.md)。本文的结果来自公开独立实现与其中的测试定义。以下编号对应[声明型用例](../../vectors/portable-framework-cases.json)。

## 哪些成员可以选择

纯预览要求正安全整数 `schema`、队伍数组和 `storage.boxes` 数组；每箱须有 `slots` 数组。按队伍下标、再按箱号及槽号遍历，只跳过箱中值为 `null` 的空槽。队伍中的每一项都要验证，值为 `null` 时返回 `invalid-input` 并指出该队伍位置。成员的 `id` 和 `species` 都是非空字符串；同一 ID 在全队和各箱只能出现一次，包括没有友好度字段的成员。可选 `form` 是非负安全整数，省略时在身份描述中显示 0。候选记录含路径、所在位置与成员身份、原值 256、结果 255。例如，同名物种的成员可凭 `$.party[0].friendship` 和 `$.storage.boxes[0].slots[1].friendship` 分别选择。见 FRIENDSHIP-01、FRIENDSHIP-02。

|输入值或选择|预览及确认的结果|
|---|---|
|省略字段，或整数 0 至 255|保留省略或原值。当前版完整玩家存档另要求友好度字段存在。|
|256|列为候选；只改确认的目标。|
|257 至 9007199254740991|列为 `outOfScope` 并保留原值。|
|其它可序列化值，如负数、小数、字符串或非安全整数|拒绝 `invalid-input`，给出问题位置。|
|省略路径选择、显式空数组、合法子集|分别选全部、零项、指定项。子集仍按候选遍历顺序排列。|
|重复路径、非字符串、候选以外的路径|拒绝 `invalid-selection`。|

作者物种、形态和覆盖项中的 `happiness` 有单独的作者迁移计划和显式输出目录。作者 schema 1 接受非负安全整数并给出使用旧版值域的兼容提示；schema 2 的显式值限整数 0 至 255。省略的覆盖仍可继承；把已选的 256 改为 255 后若还剩 257，仍无法升级到标准域。作者工具保留源目录，并将每个原文件逐字节备份到新输出目录的 `.friendship-original/`。输出中的 `manifest.json`、`species.json` 和 `overlays.json` 若原本存在，则以双空格缩进的 JSON 加一个换行重新序列化；其它原有文件在输出中逐字节复制。两种计划各自处理自己的数据。见 FRIENDSHIP-18。

## 快照、选择和收据

完整语义快照只接受 `null`、布尔、字符串、有限数（排除负零），以及递归符合这些条件的普通对象和密集数组。对象原型须为 `Object.prototype` 或 `null`，数组原型须为 `Array.prototype`；只接受自有、可枚举的字符串数据属性，数组的 `length` 是可不枚举的例外。访问器、符号键、隐藏字段、带额外键的数组、循环引用及会在 JSON 中丢失的值导致 `invalid-snapshot`。不调用 getter；无环的共享子对象可在各处分别展开。见 FRIENDSHIP-03、FRIENDSHIP-04。

数组保持原次序。对象把自有键按 JavaScript 默认字符串排序（UTF-16 码元）递归重建，再以紧凑的 `JSON.stringify` 序列化，无尾换行。其对象枚举规则使数组索引键（0 至 4294967294 的规范十进制键）仍先按数值升序输出，其它键按前述字符串顺序；`__proto__` 作为普通自有键保留。对快照字符串按 UTF-8 计算 SHA-256，编码为小写十六进制。文件的原始字节另行核验。见 FRIENDSHIP-03、FRIENDSHIP-13。

计划主体含 `version: 1`、`kind: "player-friendship-256-to-255"`、`beforeSnapshot`、`afterSnapshot`、各自的 `beforeHash`、`afterHash`、完整 `candidates`、选中的 `targets` 及 `outOfScope`。主体的规范化摘要为 `planHash`。纯确认重新从原快照和所选路径构造整份计划；篡改或不完整为 `invalid-plan`。另传的确认必须精确匹配 `planHash` 和有序目标路径，否则为 `confirmation-mismatch`。摘要用于校验完整性。见 FRIENDSHIP-05。

完整现状与原快照及结果快照均不符时为 `stale-plan`，包括只改好部分目标或改动无关字段。两快照相同优先返回 `unchanged`；否则，现状已经是完整结果为 `already-applied`，现状仍是完整原快照为 `applied`。成功返回独立数据副本和外部收据。收据主体为 `version`、`kind`、`planHash`、`beforeHash`、`afterHash`、`targets`、`originalSnapshot`、`afterSnapshot`，另附对主体计算的 `receiptHash`。存档中不写迁移标记。见 FRIENDSHIP-05、FRIENDSHIP-06。

## 应用确认和失败状态

应用预览先完整校验当前游戏与选定存档。它绑定应用代际及写入修订、内容对象身份及其完整指纹、完整状态、真实持久目标、原始字节摘要和宿主持久状态。取得的句柄只对应应用私下保存的计划，展示列表是副本。活动中的互斥操作可阻止预览或确认。确认取得独占权，在异步等待后重查绑定并完整校验候选。应用写入递增修订，即使完整游戏值改回，旧修订的句柄仍会被拒绝。若检查时文件仅有空白变化、内容对象被等值替换或宿主持久字段变化，本次确认也会被拒绝。要迁移改变后的目标，须重新预览。若只有外部字节变化，且这次拒绝发生在提交前、没有重入，原句柄仍保留；把字节精确还原且其它绑定仍相符后可用它重试。写入重入即使在回调中被捕获，仍会使操作失效。见 FRIENDSHIP-08、FRIENDSHIP-09、FRIENDSHIP-11。

|确认或取消时的状态|可见结果与后续动作|
|---|---|
|未执行句柄取消|返回 `cancelled`，零写入并丢弃句柄；再次取消或使用无效句柄为 `unknown-preview`。|
|空选择或没有候选|返回 `unchanged` 和当前原始字节摘要，持久状态报 `committed`；无文件替换、备份包或内存安装。|
|完成后取消或再次确认|取消返回 `preview-completed`，句柄保留。再次确认要重查代际、修订、内容、内存和持久结果的全状态、真实目标、结果字节摘要及完成时宿主身份。一致为 `already-applied` 或原有 `unchanged`，过期则拒绝。|
|确认时，提交前重新读取选定存档抛错|返回 `refused / confirmation-rejected`，释放写入锁。本次确认未调用提交，也未安装内存副本。|
|提交调用明确返回未提交|返回 `refused / persistence-not-committed`，释放写入锁。|
|提交调用本身抛错或明确返回结果未知|返回 `reload-required / persistence-unknown`，保留写入锁。重启后检查实际存档及恢复包。|
|已持久提交|先读回目标、摘要、完整结果和原宿主身份，再安装内存副本，读回完整内存并再次核查目标与宿主捕获。安装抛错后若实际结果仍全部相符，可返回带诊断的 `applied`。|
|提交已确认，但随后读回抛错或无法核实安装|返回 `reload-required / committed-install-unverified`，保留已提交事实和写入锁。安装内存前的目标读回和安装后的最终读回均适用。重启后核实并载入，不自动写回旧字节。|

见 FRIENDSHIP-08、FRIENDSHIP-10、FRIENDSHIP-11、FRIENDSHIP-12；常规失败处理见[迁移、失败与恢复](migration-failure-recovery.md)。

## 存档编码和恢复

**Node 单文件**使用既存、本地、实际路径无别名的常规文件。预览读取原字节，以 UTF-8 解码并解析 JSON，经内容及可选物种解析器完成存档迁移与完整校验。提交时再次核对真实目标及内容，完整校验候选并与已批准的语义结果比较；输出是 `Buffer.from(JSON.stringify(prepared.state), "utf8")`，无另加换行。原文件的排版、键序和换行在 `original.raw` 中逐字节保留。见 FRIENDSHIP-13。

**MZ 本地手动槽**只接受已存在、编号为 1 至最大手动槽数的整数槽。把原文件字节读为 UTF-8 压缩字符串，经 `zipToJson` 解压，`JSON.parse` 保留宿主类封套，取 `contents.system._psGame`。若识别为 `pokemon-framework-json`，必须正好有 `encoding`、数值 `version: 1` 和字符串 `data` 三个自有字符串键，再对 `data` 解析 JSON。早期未封装输入交给原有完整验证流程。预览对宿主持久对象及全局索引捕获身份；从保留原型的独立副本编码，排除 `_psSaveInfo`、`_psSaveWarning`、`_psSaveError` 这三个运行诊断。见 FRIENDSHIP-09、FRIENDSHIP-14。

MZ 确认从所选槽的原宿主对象出发，只替换 `contents.system._psGame` 为上述三键封套，内层 `data = JSON.stringify(prepared.state)`，外层 `encoded = JSON.stringify(contents)`。宿主的 `jsonToObject` 须正确还原类及框架快照并通过完整校验，两份已校验状态的 JSON 序列化须相同。还须满足 `zipToJson(jsonToZip(encoded))` 的结果与 `encoded` 逐字相同。把压缩字符串按 UTF-8 转成目标文件字节。框架字典中的 `@` 和 `constructor` 保持数据含义；不经过普通保存，不更新全局索引、保存时间或常规备份。见 FRIENDSHIP-14。

正式地图事件先让当前解释器指令推进并完成本帧，随后展示所选及范围外数量。选择期间只暂停所属地图场景的 `updateMain`，消息、输入、渲染和 Graphics 帧继续。默认选择及取消均为第 1 项，仅第 0 项确认。离场或终止释放模态并使迟到选择无效；普通保存或载入在途时拒绝预览。直接脚本的 `previewFriendshipMigration(slot, paths?)` 不取得场景暂停，调用方须使宿主持久状态在异步操作期间稳定。见 FRIENDSHIP-15。

两种端口都先在目标旁建立 `<file>.friendship/preparing-*`，写入并同步 `original.raw`、`candidate.raw` 及 `receipt.json`。物理收据记录目标、编码、源 schema、前后字节摘要、内容身份及指纹、纯计划和收据；其 `id` 是主体规范化摘要，收据文件采用规范 JSON 加一个换行。同步并重命名目录形成完整 `<file>.friendship/<id>/` 后，写同目录目标临时文件；核对所有权和原字节摘要，以一次重命名替换目标。中断可能留下准备文件或临时文件；替换后抛错必须按实际字节判定。此约定针对本地同目录重命名与可执行同步的文件系统。见 FRIENDSHIP-13、FRIENDSHIP-16。

恢复先核实收据、自有目录与目标绑定、两份原始字节摘要和重新计算的纯收据。`inspect` 根据目标实存字节返回 `old`、`new` 或 `unknown`，相同摘要先判 `new`。`complete` 和 `restore-original` 仅对可识别版本执行；已是所需版本时无写入，未知内容、读不到的目标或不明恢复临时文件均不会被覆盖。恢复保留字节原件及收据；MZ 只处理实际保存目录的目标，显式恢复后要求重载。见 FRIENDSHIP-16、FRIENDSHIP-17。

## 迁移后的普通运行规则

标准域是整数 0 至 255。迁移后的 255 可正常计算，未选 256 和范围外的 257 继续保留原始数据，在普通变更或亲密度查询中仍属越界。道具端接受 `vitamin`、`wing`、`evberry`、`powder`、`energyroot`、`revivalherb`；越界时抛出 `friendship-out-of-domain`，普通道具计划不消耗物品或改动原游戏。在有效域使用不支持的方法则为 `unknown-friendship-method`。道具端原有缺值回退为 70。战斗端只接受 `levelup`、`battleitem`、`faint`、`faintbad`，对于缺值、越界或不支持的方法返回 `null` 并跳过变更。见 FRIENDSHIP-07。
