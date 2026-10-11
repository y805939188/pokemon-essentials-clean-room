# B20 三项拟议阻塞的独立反证检查

本记录仅检查父任务所列三项，结论：**三项均支持有界阻塞，但必须使用下列收窄理由与验收条件**。本记录不是 FULL、affected 全包或 actual 门，不签正式接受。

固定审查 NEW：`1abaefb1db5818ff9404392143c476979d34c21a`，tree `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85`。基线 C：`de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`。入口：`9a46a131ba2f7ea82b6eed823aa892cb57b0fba7:review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/affected.md`。派发：`669997ac28258f26d0bafc81b1d081abb407a3a1`。参考固定：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，只读 `/tmp/b20-reference`。

只作 Git 固定对象读取、文本静态检查与自写 JSON/hash 元数据读取；未运行游戏、Ruby、编译器、转换器、反序列化器、行为向量或旧执行脚本。以下反例均为静态分支判断，NOT_EXECUTED。没有改仓库、提交或推送，也未复制参考源码或旧证据正文。完整无过滤差异仍由入口固定的唯一发布流承载，本记录不另行复制。

## 1. C029：形态消费门

支持阻塞 NEW 局部条款，不能扩大成旧 WP21 全包重审。

NEW `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md:139`、同 NEW 共享目录 `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:278`、同 NEW `review/remediation/20261003-prepare/batches/B20/author-draft-1/per-ID-remediation-and-static-cases.json:133–137` 把消费 getter 且没有强制覆盖作为 0/1 分支的充分前提。C `deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md:246` 已保留战斗中或仓库中读取存储形态、不触发动态处理器的门；固定参考 `Data/Scripts/014_Pokemon/001_Pokemon.rb:147–152` 支持该门，`Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:267–271` 则仅支持处理器内部宝珠/旗标 0/1 分支。

最强替代解释是“getter被消费”仅指动态处理器确实已经进入。如果这样明确限定，该分支本身正确。但 NEW 用的是一般 getter，案例也只排除强制覆盖，并未给出主规格求值门链接；合法的战斗/仓库读形态仍满足所写前提而不必得到所写 0/1 结果。原 qualified 合同 `41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json#/GIR-FD82-C029/minimum_revision` 明确要求与形态主规格的求值门链接，`root_adjudications` 也要求保留外层求值门。因此这是本批承接缺口，不是引入新义务。

有界验收：NEW 本地条款链接并继承 WP21 的强制形态、战斗、仓库门；0/1 规则明确仅用于动态处理器被实际求值的分支。新增案例及 JSON 同步明确这些前提，并以战斗/仓库读取存储值作为相邻反向对照。保留 GIRATINA/GRISEOUSORB 的正确身份和 Demo 未证明。原稿审计中定点 FormHandlers 注册分支的定位本身正确，不要求清洗旧审计。入口路由及派发表未列 WP21 consumed 路径，不能凭此推定旧 owner 整体受影响或要求改旧正文。

## 2. C028：缺资料与非法输入被混并

支持阻塞 NEW 的缺失回退承接和文字/案例一致性；不能报告成要求“所有失败总有非空替代文本”。

NEW 正式 WP77 `:115`、原稿 `specs/demo/wp77-demo-evidence-and-capability-coverage.md:139`、共享目录 `:277` 和 per-ID JSON `:124` 把没有相应资料表述为底层失败。C `deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md:145` 规定：合法类型下无适用训练家资料为空文字；遭遇请求版本缺失先回退版本 0，均缺资料或三个候选表都空则为空文字；空训练家队伍、非法参数/物种另外保留失败边界。固定参考 `Data/Scripts/013_Items/004_Item_Phone.rb:506–531` 及 `Data/Scripts/010_Data/002_PBS data/013_Encounter.rb:30–35` 分别支持这些区分。

最强替代解释是“不保证总有替代”只是拒绝非空有意义文本的普遍保证，这一限制本身可以成立；NEW 也说随机取值归已接受 WP63。但句子实际以“没有相应数据时的底层失败”为条件，新增反向案例未承接该合同的确定空文字/版本回退，容易把合法缺资料改写为异常。因此应以缺失边界混并和承接缺口阻塞，而不称底层所有失败都被错误定义、不要求新兜底。原 qualified 合同同固定 acceptance 文件 `#/GIR-FD82-C028/minimum_revision` 已要求缺失回退由 WP63 承接；B15 的真实消费接口支持本项范围。

有界验收：明确链接/继承已接受 WP63 的随机来源与缺失边界；无训练家数据为空文字、遭遇请求版回退 0、均无资料/三表空为空文字。空队伍、非法类型/物种仍不承诺保护，避免扩大成总有替代。正式条款、被本批新增的原稿条款、目录和 JSON 同步；加入这些合法缺资料的静态对照并维持 NOT_EXECUTED、联系人注册链未证。不能要求修改已正确的旧 WP63。

## 3. C003：CN 新增错误释义

支持阻塞 NEW 新增目录和其 JSON 的局部一致性，属于新增错误，不能算旧案例错误或重开旧 C003 贡献。

NEW 共享目录 `:270` 的 B20-C003 和 per-ID JSON `:32` 把 CN 解释为金银铜钱。C 与 NEW 均保留的 `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md:47` 区分金钱窗、代币窗与战斗点窗；C 与 NEW 共享目录 CV-M14 `:157` 已正确规定 CN 为代币窗。固定参考 `Data/Scripts/007_Objects and windows/011_Messages.rb:330–343,587–589` 将 CN 消费绑定到玩家代币数量的窗口；没有金银铜三级货币语义。

最强替代解释是“金银铜钱”只是泛称钱币；但上下文正在区分兼容格式码的唯一消费含义，而 G 已是金钱窗，旧正文和旧案例已经有明确代币语义。此泛称既不准确也无证据支持，不能用它取代已接受绑定。不是从游戏领域常识额外要求新功能。

有界验收：只把 B20-C003 和 JSON 的 CN 释义改为代币窗，与 WP17/CV-M14一致；其他正确的资源顺序、ASCII、CommonEvent、B19 四行保护等内容保留。旧 195 个 ID 顺序/重复次数和既有 CV-M14 原文无需改变，本项只对应 B04 WP17 的有支持接口，不扩大到全部共享 C003 owner。

## 独立重算的关键输入身份

下列 SHA256/字节数由本次直接读取固定 Git blob 重算，不依赖作者断言；全路径与行号见上文，不复制旧正文。

| 固定对象及路径 | SHA256 | bytes |
| --- | --- | ---: |
| NEW `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md` | `5808fd55a3d8f8788ab02400f976fd5af5325652fb80ee3f128744ae53fdfad0` | 27032 |
| NEW `specs/demo/wp77-demo-evidence-and-capability-coverage.md` | `d3520f2a7c23bfe8032cbe393f01ec83536e3ad7f1645dc2f8b7720353fcf412` | 45176 |
| NEW `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` | `6e9e463d4f6b7d7591d0d30e457787b759c56c4a3638080a15e92e63eb84cc45` | 100779 |
| NEW `review/remediation/20261003-prepare/batches/B20/author-draft-1/per-ID-remediation-and-static-cases.json` | `87f5986d76df0c320e55783d3ad5b46394156c555e58ad43abf70d5a9ae8e215` | 19433 |
| C `deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md` | `5d1f03aee8b83046a86f52ae4c1ed701d905e3559676e3a448998c6e216a7a01` | 34492 |
| C `deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md` | `138c3d5220a096640dd1e6308e701fe6d280b3e45be578a22b8d41fe43c094d2` | 32854 |
| C `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` | `a95a28b20b47bc333fcb8eb08432d2b2f7ab897e97045397baf73f8d634281ca` | 29252 |
| REF `Data/Scripts/014_Pokemon/001_Pokemon.rb` | `3a7f233156f09a6d2e3729bdaa9d1962bfa946aaaa7403042aaea5dcdcdf8cb4` | 42638 |
| REF `Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb` | `09697fb94d9e8565049cb45401cbb0bf7e610203068417bdc70741add590ae97` | 23576 |
| REF `Data/Scripts/013_Items/004_Item_Phone.rb` | `81519d2fb0b6926ac2ca08f693e2f08e3800878628ba90f5a7d2a314ff1c60f4` | 25386 |
| REF `Data/Scripts/010_Data/002_PBS data/013_Encounter.rb` | `d7ebeb1d00434f5da96165ad407101a14d007bce03fa0d0e267c5ee293c183f7` | 2267 |
| REF `Data/Scripts/007_Objects and windows/011_Messages.rb` | `88e72c557c53da5a72e4d5b4de7431bbfbd03f4f8f27bcf44ac231a5141b8536` | 25224 |

结论的剩余限制：本记录未检查父任务负责的其他 owner 或整份目录保护，因此不能据三项判断旧 308 贡献整体保持或整体回归；应由父任务已有全量影响与保护证据提供。三项均不授权实际运行、改参考、改正文、签 actual 或正式接受。
