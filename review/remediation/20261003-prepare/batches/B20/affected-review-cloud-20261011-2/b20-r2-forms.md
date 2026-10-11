# B20 NEW2 C029 / B05、B07、B08 有界再审

结论：**PASS_BOUNDED_REPAIR_AND_INCREMENTAL_OWNER_INTERFACES**。本范围剩余问题0。NEW2 修复上一轮 AF-01 与 FULL-F03 的同一 C029 调用门缺口；这只是本次有界独立静态判断，不签 actual、正式接受或整包质量结论。

审查 NEW2 `3f521e6dea0b442e4bb174a9715c458416386b37`，tree `49f406a6de8ca2786e5dda27abada19780fdfa05`；前次 NEW1 `1abaefb1db5818ff9404392143c476979d34c21a`。固定入口包 `81d3be653e87e6424d0d8cd38dab14a9aafc97a1` 的 [affected.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/81d3be653e87e6424d0d8cd38dab14a9aafc97a1/review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/affected.md) 及 [repair-navigation.json /all5_groups/2](https://github.com/y805939188/pokemon-essentials-clean-room/blob/81d3be653e87e6424d0d8cd38dab14a9aafc97a1/review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/repair-navigation.json)；作者最终发布读回包 `dbfa219547690f06eac9180f3ecd9dd1091eb49f`，tree `59529b00d2a3704251f6622f3b1d7b55a186dfdc`。入口/作者 completion/scope 的状态只作定位，不作质量通过证据。

本审只读固定源码与变动文本，并新写 Git/JSON/hash/文本元数据核验。完整差异由父审统一核验并引用，本子审未另发差异或复制旧报告正文。所有案例均为 **NOT_EXECUTED**；运行观察0、已证 Demo 链0。没有执行参考游戏、Ruby、编译器、转换器、反序列化器、行为向量或旧脚本；仓库修改0。

## C029 修复核验

旧问题保留在 `680e3988c4144db269e063971991134b8e0bd678` 的 [affected findings.json /findings/0](https://github.com/y805939188/pokemon-essentials-clean-room/blob/680e3988c4144db269e063971991134b8e0bd678/review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/findings.json)，以及 `df1539b67988d4f161b31935752a7f13aec8556b` 的 [FULL findings.json /findings/2](https://github.com/y805939188/pokemon-essentials-clean-room/blob/df1539b67988d4f161b31935752a7f13aec8556b/review/remediation/20261003-prepare/batches/B20/independent-full-candidate-review-cloud-1/findings.json)。原 qualified 合同固定 `41fffb540c6483f5296ea0d33b789b75180d27ed`：[finding-acceptance.json /GIR-FD82-C029](https://github.com/y805939188/pokemon-essentials-clean-room/blob/41fffb540c6483f5296ea0d33b789b75180d27ed/review/remediation-20261003-prepare/finding-acceptance.json)，要求精确物种/道具及0/1结果、绑定形态主规格的求值门、保留实际进入地图未验证。没有从“修复完成”标记反推满足合同。

NEW2 正式 `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md:145–146`、原稿 `specs/demo/wp77-demo-evidence-and-capability-coverage.md:174–176`、目录 `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:278` 与固定 active JSON `bfc6264bf47478bd174412289de2e31f4da2d9a6` /static_cases/3（文件342–470行）一致写明：强制形态存在（含0）先返回；无强制形态时，战斗或仓库状态直接返回存储形态；两状态均假才调用动态处理器。GIRATINA 的 GRISEOUSORB/DistortionWorld 只在处理器实际调用时给1，两者均无给0；不同候选才按主规格提交，后续更新仍归主规格。form_simple 只取强制/存储值，不调用处理器。

固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只读 `/tmp/b20-reference`：`Data/Scripts/014_Pokemon/001_Pokemon.rb:147–166` 给出读取门、简化读取及提交的更新边界；`Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:267–272` 给出限定 GIRATINA 的精确道具/旗标分支。这是源文本对照，并未运行源码或调用 getter。

NEW2 的两处 WP21/WP18 相对链接均解析到该固定 tree 中真实存在的对象；WP21:246–248 与 WP18:150–153 的旧门和不同候选提交条件未改。12 个 active 子例逐一读过，均保持 execution=NOT_EXECUTED、observation=null、quality_verdict=null。目录 C029 的前提和有序预期与 active 对象逐字符串相同；固定 active commit 的整个 JSON blob 与 NEW2 同字节。历史 per-ID 旧对象保留，full19 active map 指向新的 successor，因此不把旧未修预期当本轮有效夹具。

独立相邻静态对照（完整前提在本报告 JSON，均未执行）：

| 前提/消费 | 唯一预期及回归意义 |
| --- | --- |
| 存储0、无强制、持指定宝珠、仓库真，普通读取 | 返回存储0，不调用处理器；旧 AF-01 的1不再由候选推出。 |
| 存储1、无强制、无宝珠/旗标、战斗真，普通读取 | 返回存储1，不由处理器归0；旧反例得到明确处理。 |
| 强制0、存储1、宝珠/旗标均真，任意合法战斗/仓库状态 | 先返回0，不调用处理器或提交。 |
| 两状态假、无强制、存储1，持其它宝珠且旗标假 | 指定道具条件不满足，动态候选0不同后提交；其它宝珠不能替代 GRISEOUSORB。 |
| 两状态假、无强制、存储1且持指定宝珠 | 候选1等于存储值，不提交；不能凭读取推重复后续副作用。 |
| 正常状态、无强制、存储0且持宝珠，读取 form_simple | 仍返回0，无处理器。 |
| 另一合法物种设同样宝珠/旗标 | 依其自身合同，不能从 GIRATINA 规则推出1。 |

正文、原稿补充、目录与 active 对象均保留地图进入和 Demo 实际变形未证、证据③④为0。原稿旧 handler-local 审计由 NEW1:163 移到 NEW2:169，仅因前文插入而移位，整行字节相同；新增外层门补充没有替换该正确历史审计。

## Owner 影响与增量回归

未变内容引用上一轮固定审查身份，并重新核对对象。JSON 保存每个 NEW2 对象的固定 commit/path/blob/SHA256/bytes 及 NEW1、接受 C 的同 blob 比较；不复制旧正文，也不把字节相同当新语义通过。

| Owner | 本次实际有界影响与判断 | 未变支持证据 |
| --- | --- | --- |
| B05 | WP77 实际普通 getter → WP21/WP18 读门及提交边界；作者原空 route 不能豁免该依赖。C029 缺口已静态修复，旧身份、其它形态/属性责任保留。 | 旧审 `680e3988c4144db269e063971991134b8e0bd678` 的 b20-owners-b01-b06.json /owners/4；15 条旧 PLAN 文件身份 C=NEW1=NEW2，B05 旧证据目录 tree相同，16项旧 scoped贡献不转签。 |
| B07 | 本次 C029 未把读取变为经验、库存、升级或进化成功。原 WP30 公共动画读名接口仍由上一轮证据保留，C003 关联消费由父审另组核定。 | 同固定旧审 b20-owners-b07-b12.json /owners/0；8条旧输出身份相同，旧证据目录 tree相同；WP74 正式整文件 NEW1=NEW2；19项贡献保留。 |
| B08 | C029 新调用门与旁边野外等级缩放分开；不增加地图已进入、遭遇已生成或实际孵化/动态演出的证明。WP36 唯一数学输入/消费者仍沿旧审保留，电话修复由父审另一组负责。 | 同固定旧审 b20-owners-b07-b12.json /owners/1；8条旧输出身份相同，旧证据目录 tree相同；WP77 野外缩放旧140→新147及旧152–156→新159–163逐字相同，目录B20-C083第285行相同；17项贡献保留。 |

上述31条 owner 文件身份条目对应28个唯一文件（共享旧目录按实际身份计算）。只核新消费者及邻接回归，不重新签52项旧 owner 接受贡献。B07 的成长数值/库存早退、B08 的全部队伍数学输入及地图/版本快照均未被该形态修复替代；新条款的主规格链接保持领域责任归属。

本范围验收条件已满足：外层门及简单读取明确；动态0/1限定物种/道具并链接 WP21/WP18；不同候选提交与未变值不提交一致；正文/原稿新增补充/目录/active successor 一致；旧 owner 和正确原稿审计保留；运行/Demo证据保持0。余下完整包门和其它修复组由父审合并独立结果，本子审不签实际集成。

完整固定证据身份、行范围哈希、逐 owner 对象比较与7组独立静态反向前提见 [b20-r2-forms.json](b20-r2-forms.json)。
