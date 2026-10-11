# B20 candidate：B13–B18 已接受 owner 的独立有界影响复审

固定审查 NEW `1abaefb1db5818ff9404392143c476979d34c21a`，tree `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85`；基线 C `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`，tree `88a400af08253bea8d97ee2ef2fa6636f0900f92`。入口包 `9a46a131ba2f7ea82b6eed823aa892cb57b0fba7` / tree `3397ef849f652c47506b492dabc32c51f5a12c76`；读回包 `272885cca76c36cd04dde27b6be2c654759ec4c2`。本子报告不作 ACT 门或正式接受，不转移旧签名。

结论：**B15 有一项 P2 有界阻塞（B20-AFF-B15-F01）**。B13、B14、B16、B17、B18 在下面实际支持的影响范围内未见新增阻塞；这些判断不是整包质量 PASS，也不重复接受这些 owner 的旧贡献。仅静态 Git/JSON/hash/text 与固定参考源码阅读；所有案例 NOT_EXECUTED，运行观察与 Demo 已证链均为 0。没有执行 Ruby、参考游戏、编译器/转换器/反序列化器、行为表达式/向量或历史脚本，没有编辑仓库。

## 固定合同与保全证据

- `AGENTS.md` 已读，参考只读、行为中立输出及不复制参考代码规则保持。
- 原 owner 合同：commit `41fffb540c6483f5296ea0d33b789b75180d27ed`，`review/remediation-20261003-prepare/batches.json`，JSON pointers `/12`–`/17`。原整体 blob `9dd98a6b96d49294d214f7e9a53eac8738c1484c`，SHA256 `3758c04581500a29c0fa8dd727d8d6026a4ed2934c42b1778b1ff18e6fdbb02f`。
- B20 重新派发：commit `669997ac28258f26d0bafc81b1d081abb407a3a1`，`review/remediation/20261003-prepare/batches/B20/refreeze-after-B19-C-1/dispatch.md`、`author-contract.json`、`source-limits.json`、`catalog-preservation-locks.json`、`control-and-acceptance-overlay.json`；owner map `accepted-interface-map.json` pointers `/interfaces/12`–`/interfaces/17`，blob `265041e0830bd47130492e314c67520bb738f562`，SHA256 `80dde444746b204e6d2a1985da7d41e5bb51e8ae3e2557b9847e8c91055ee28c`。这些是范围与输入身份，不作为作者质量断言。
- 本次入口 `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/affected.md` 与 `affected-routes.json` 已读；实际 reader 判断按下面源码/正文消费条件补全，例如 B17 的 WP67-A 动画播放侧不能因为 routes 仅列 WP67-B 输入而被排除。
- 独立按原合同写路径比对：B13 7 路径、B14 6、B15 6、B16 6、B18 13 全部 C/NEW blob 相同；B17 5 路径只有共享 demo 目录变化。B13–B18 各 `acceptance-stage-1/` 下所有旧输出 C→NEW 零变化。map 中这些 owner 的 8/24/16/24/12/8 项旧 scoped receipts（共 92 项）保留，未被本判断重签。其余旧 308 接受贡献的全局保全由主报告独立核验。
- 独立解析共享目录全部 Markdown 数据行：C 195 项，NEW 214 项；旧 195 first-cell ID 序列逐项等于 NEW 前 195 项，顺序/重复次数原样；193 行逐字相同，仅 AN-M23（C/NEW 行 126）与 CV-M18（行 161）变动；追加 19 行（NEW 269–287）。PA040 三行（235–237）、B19 17 行（245–261）逐字相同。没有以目录数量推出语义通过。
- 共享目录固定路径 `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`：C blob `17ea088afe9e3fb67e4cbeaf5a7e6faa2eff940d` / SHA256 `ffd8992eef39f39892709d5dd591780669c97a0bd59dda9cc0f55818fee2e9f1` / 90084 bytes；NEW blob `a4a5279c9826d87e9663780c6e35a92cc733ffef` / SHA256 `6e9e463d4f6b7d7591d0d30e457787b759c56c4a3638080a15e92e63eb84cc45` / 100779 bytes。
- 唯一完整未过滤差异流仅固定引用 commit `f325f625f879105f7811713d9a38cc58da875de2` 与入口 `entry.json` 所给路径/blob/SHA256/bytes；没有生成/复制新的完整流或旧证据包。

## 各 owner 的实际有界范围及判断

| owner | 旧合同/真实消费范围 | 本次影响及判断 |
| --- | --- | --- |
| B13 | WP54 资格/条款，WP55 设施会话按位置经验/持物还原，WP56 Palace/Arena 补位不重置，WP57 租借/交换取消仍提交，WP58 录制/回放入口与攻击后替补消费；003 局部独立复制义务。旧 ACT `d81562bfe0e79ca4df3233ada38fa09e800bdafc`，报告 `d984a0f59c8843aa8391fde0a797101c1b421412`。 | WP74 复制/插帧/动画映射是实际呈现侧交界；不能把编辑器属性快照与 WP58 记录字段序列化语义混同，也不能从呈现推设施还原/替补资格变化。NEW WP74:184–200 分开 Copy/Paste 独立与 Insert 属性联动；396–399 分开映射重编译和公共动画精确拼接；WP58:53/103/140/158–162 保存动画开关、呈现随机不入记录、普通播放包装与中止/终局区别均未修改。WP54–58 主体和其目录无变；NEW WP77:132–134/180 保持设施配置/消费者存在但接待链未证。**实际交界有界受影响，未见新增阻塞；旧参赛/恢复/补位/录制义务未被改写。** |
| B14 | WP59 时间/天气/钓鱼与场地转移；WP60 树果阶段/通知；WP61 中心识别≠构造、回程部分写入、个体/队伍/存储治疗。旧 ACT `d48197f365c39925f795c1d325988c0d74e59979`，报告 `1f86ae64188689b0179f20125dda7ef715e95152`。 | WP75:218–227 治疗旧文本是 WP61 恢复命令的真实消费者：首字符门早于拼接/去空白，精确两形，少删1条和单命令持续增长保持。源 MapsAndEvents:1150–1190 支持，不执行。新事件 Recover All 参数0由 C/NEW WP61:147–151 承接：默认存储治疗 false 时队伍+箱内全体，true 时仅队伍；不把它称为旧仅队伍循环的等价运行测试。源 Interpreter_Commands:1099–1107 支持。WP75:20/25/361 保持中心识别≠构造与不保证无误判；WP77:54/179–182 保持 Home 回程与未证地图链。世界时段/天气/钓鱼/树果正文及目录相同，WP74 编译映射没有修改这些领域的时钟/天气/输入消费。**有界治疗/识别交界受影响，未见新增阻塞；其它 B14 义务有实际条款与字节保全支持。** |
| B15 | WP62 图鉴形态/搜索状态、WP63 地图点/联系人注册/公开旧入口缺陷/电话每通固定抽样及缺失回退，WP64 邮件与共享礼物个体。旧 ACT `fd44556f877a400337eb893757d91f1adfa856ba`，报告 `4b3ff8dff1733aa8249c75a8b494e87ad93fc472`。 | **受影响且阻塞 B20-AFF-B15-F01**：新增 WP77 电话五标记及 C028 目录为 WP63 的真实 reader。正常 TP 来源=max(current,start) 的联系人队伍，TE 来源为联系人地图/当前全局遭遇版本、Land→Cave→Water 前最多4槽均匀，TN/PN/TM绑定正确；但 NEW115/原稿139/目录277 对缺数据写成失败，丢失已接受空文字及版本0回退分型（见下）。WP75:64/72/84 新 CommonEvent 可达块进入电话登记参数；源 MapsAndEvents:479–491/562–567/603–625/694–721 支持先收集后每块一支，且 WP63:85/99/108–129 的先写后反馈失败、公开版本恒0/旧入口缺陷未被“再战版本分支”当作正常进度证明。图鉴搜索、邮件/礼物路径无新增消费者条件改写、已接受正文及三目录原样。 |
| B16 | WP65 启动/选项/屏幕倍率请求；WP66-A/B/C 队伍摘要/BoxLink旧索引部分写入/交换持Y/有限槽及BP显示；003/C003局部入口义务。旧 ACT `29b21fe188cce4e76f5a2f566f9144f1c3f53239`，报告 `191e669c72282e0c11217df2e7f80ed5c377dbd7`。 | WP74:39–57/71–75 为编辑器屏幕/资源/缓存状态的有界交界：有效缓存复用、无文件临时集合、首槽空对象分别保留；目录异常不承诺统一释放/屏幕/BGM恢复；正常返回后恢复到系统存储倍率值，而非擅自钳回合法选项。源码 AnimEditor_Functions:1144–1169 支持清理及屏幕恢复顺序；旧 WP65:115–125/138–139/235/246 的选项内存/落盘与宿主未证分开保持，B16-C115目录仍原字节。NEW未重新定义 BoxLink/摘要/物品消费或使资源缺口成为所有UI入口失败。**实际生命周期交界受影响，未见新增阻塞；其它资格/索引/消费义务有界保持。** |
| B17 | WP67-A 战斗交互与动画查找，WP67-B 生命周期演出末帧取消/成功提交/异常清理边界，WP76 设施作者正常AI与直接辅助入口区别；PA040目录三例。旧 ACT `5501314ecead8aa072868794a95dc026a5f0a3f5`，报告 `6d5fb7f267b65f2aba01837ce0f87488b0723220`。 | 实际 WP67-A reader必须纳入：NEW WP74:396–399 的 Move/OppMove 前导空白处理和 Common直接拼接均与固定 Compiler_CompilePBS:1274–1318、Scene_PlayAnimations:412–423/492–518 一致；保留末槽覆盖、槽号关联/需重编译、零有效条目旧映射不清、Opp命中不翻转与播放侧首个 Common匹配。WP67-A:239–244 的开关/缺数据静默不播/公共首匹配没被改为作者编辑器可达性保证。WP74:75的异常边界与 C/NEW WP67-B:171/184/194 的未证演出异常清理一致，不把编辑器目录门扩大为进化/孵化/交换通用兜底。WP67-B:19–20/35–58 的取消/提交及目录 B17-PC119-last/flash（651/653）原样；WP76直接调试失败/正常AI边界未改；PA040三行逐字保留。**动画实际reader、生命周期与共享目录受影响，未见新增阻塞。** |
| B18 | WP68 卡仓/抽样域，WP69老虎机，WP70挖矿，WP71七模式/默认4×4五步不完成与表外1×1；三只读全目录保全。旧 ACT `c211767166b18799122c1e39b9f08afce6b0c92b`，报告 `fd0a6d7556839ab1daa8ca6c64a12ead833de13f`。 | WP74目录枚举/具名图加载与UI素材边界为局部交界；WP77:138–140/183 仅登记 Game Corner 与静态规格依赖、事件缺失仍不证明可玩。NEW未触碰卡牌/老虎机/挖矿/拼图的状态、随机域、资源载入消费者或奖励条件；WP71:102–107/120–126/149–151 仍用其自身背景/主图/完成门，不借用WP74目录门保证正常或异常恢复。原合同13写路径及三目录字节相同，包括 B18 新反例/完成分支；WP74 §3.4仅本编辑器子选择器不是全局UI目录承诺。**局部素材/证据reader受影响，未见新增阻塞；其余已接受玩法范围无新语义影响，有实际消费条件与完整字节保全支持。** |

## B20-AFF-B15-F01 — 电话缺失数据的已接受回退被写成底层失败

优先级 **P2**；阻塞 NEW 在 B15 电话数据来源/缺失回退接口的 candidate gate。不是要求添加“所有输入必成功”保证。

问题位置（均固定 NEW）：

1. `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md:115`：将“没有相应训练家/遭遇数据”称作“底层失败”。blob `3d1ca36c98b662e46d3e9aa257031e71c4f0f123`，SHA256 `5808fd55a3d8f8788ab02400f976fd5af5325652fb80ee3f128744ae53fdfad0`，27032 bytes。
2. `specs/demo/wp77-demo-evidence-and-capability-coverage.md:139`：同一错误分型。blob `cba9c34c45c31aedb1e3ae58a6b38ecbe39dd3e3`，SHA256 `d3520f2a7c23bfe8032cbe393f01ec83536e3ad7f1645dc2f8b7720353fcf412`，45176 bytes。
3. 共享目录 `.../demo-dx-wp72-73-74-75-76-77.md:277`，B20-C028 把“缺资料”作为底层失败反向预期；其固定NEW身份见保全段。

已接受对照（C和NEW逐字相同）：`deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md:123/145`，以及已接受目录 PL16/PL17（127/128），明确无训练家数据返回空文字；TE无记录/三表空亦空文字、请求遭遇版本缺失先回退0、TP空队伍不承诺同样保护。WP63 blob `ea9949228095b575d789dfccd880ba430b721d85`，SHA256 `138c3d5220a096640dd1e6308e701fe6d280b3e45be578a22b8d41fe43c094d2`，32854 bytes。

原 qualified 最低修订也明确要求“保留随机来源/缺失回退由WP63承接”：commit `41fffb540c6483f5296ea0d33b789b75180d27ed`，`review/remediation-20261003-prepare/finding-acceptance.json#/GIR-FD82-C028/minimum_revision`（整体 blob `e178e5706771f5f7465bcf3351b5c632a5d68bab` / SHA256 `54e4c86be3db493a5463ce4bcdef81c7184f1a1d89e6b3bbea358f14cc347225`）。引用WP63随机源同时另写“缺数据失败”并不能保持该回退。

静态反例（NOT_EXECUTED）：合法训练家联系人请求 max(current,start)=2，但该版训练家资料缺失；TP返回空文字，不在该处抛异常。TE使用合法地图与整数全局遭遇版本7，版本7不存在而版本0存在且有Land，则从版本0前最多4槽抽一次；版本7和0都缺，或Land/Cave/Water三表都空，则TE为空文字。它们与训练家数据存在但队伍为空（抽样后取字段可能失败）、非法物种、非法参数类型是不同前提。NEW的笼统失败反向分支会使下游实现错误地拒绝合法缺失资料/版本回退输入。

固定参考 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`：

- `Data/Scripts/013_Items/004_Item_Phone.rb:414–436/506–531`：播放开始一次TP/TE抽样、TP缺资料空文字、TE缺记录/三表空空文字、各有效随机域；文件SHA256 `81519d2fb0b6926ac2ca08f693e2f08e3800878628ba90f5a7d2a314ff1c60f4`，25386 bytes。
- `Data/Scripts/010_Data/002_PBS data/013_Encounter.rb:30–35`：合法请求版本不存在则取该地图版本0；文件SHA256 `d7ebeb1d00434f5da96165ad407101a14d007bce03fa0d0e267c5ee293c183f7`，2267 bytes。

验收条件：仅修复 B20 的两份WP77同段、B20-C028行及该行实际静态fixture，明确继承/准确区分上述缺资料空文字、遭遇版本0回退、三表空，与空队伍/非法参数/非法物种异常；保留每通开始只抽一次TP/TE、成员次数不去重、槽位均匀不按普通遭遇权重、max(current,start)、联系人地图而非玩家地图/队伍等正确绑定。以可读静态夹具至少列缺训练家资料、请求版缺失而0有记录、双版都缺、三表空四种对照；保持 NOT_EXECUTED 和 Demo链0。不得修改已接受WP63/旧PL16/PL17或参考来配合新错误，也不得重写其它旧目录行。

## 其它静态源绑定与限制

所有路径在同一固定参考commit/tree下仅阅读相关文本：

| 源路径 | 已读消费位置 | SHA256 / bytes |
| --- | --- | --- |
| `Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb` | 473–505、550–625、635–721、1135–1200；训练家块收集/电话参数、治疗词法与产物 | `3fd9c8c754f3af9bb6204b2492d266fb252cbcd8771593a6650f70601b9b13cc` / 75159 |
| `Data/Scripts/003_Game processing/004_Interpreter_Commands.rb` | 1099–1107；Recover All实际成员集合 | `1dd0032d67120227b3868b006774f8a15fd61cde7be984227215710af2a6d45b` / 44850 |
| `Data/Scripts/020_Debug/002_Animation editor/005_AnimEditor_Functions.rb` | 23–64、504–600、951–965、1144–1169；目录枚举先于子窗口、正常清理/屏幕/BGM恢复 | `45868878e6e6a2e13ad76679070da424258e95f4e9b3abd816d4266a25f32a2a` / 46603 |
| `Data/Scripts/020_Debug/002_Animation editor/004_AnimEditor_ExportImport.rb` | 7–8；RTP各目录进入，无目录存在性筛门 | `6cc201893a697506ce54317b8e5462bedcd25cecc1da73bb82c1bd6afb016369` / 4897 |
| `Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb` | 1274–1318；映射重建、Move/OppMove词法及写出门 | `d24fe0388c78e4ab321dbfb6248c454fb3fe99933305c26bf2639068113dfbae` / 54958 |
| `Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb` | 412–443、492–530；真实播放reader、Opp命中、Common精确拼接 | `ae97c79199a514f951cd96727e6a52d4163fc30ebbd6d5771db4fb165a420f2a` / 23190 |

本子报告未单独签 WP36 数学门：WP77 新平衡等级reader已界定，交由同一主复审的 B08 范围独立核验；本子报告不把作者的人工数值或NOT_EXECUTED目录当运行验证。WP15/17更深局部资源保护由 B04 owner 路负责；此处只确认 B16/B17/B18 reader不能从文件保护推目录保护或异常统一恢复。没有剩余工具/输入阻塞；唯一剩余质量阻塞为 B20-AFF-B15-F01。
