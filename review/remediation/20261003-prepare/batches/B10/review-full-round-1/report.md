# B10 候选 1 独立 full_review

**PASS_SCOPED**。本角色在冻结 `3c6365a4ce35c3ef08e6ba53fd81a426ffd026aa` 上的七项本地贡献、两项主责 minimum 及全部十项 must_review 已满足；没有阻塞 finding、必需返修或待本角色补读项。结论仅为 `INDEPENDENT_FULL_SCOPED_R_B10_CANDIDATE_REVIEWER` 的有限候选复审。其他 affected 角色、实际整合和最终全局验收仍由各自门槛承担。

| 身份 | 完整值 |
| --- | --- |
| reviewed candidate | `3c6365a4ce35c3ef08e6ba53fd81a426ffd026aa` |
| reviewed tree | `441fe0ac3f9276e54e467ea816aae1acebdf4556` |
| author branch | `codex/cloud-dot-B10-author-1-20261009` |
| accepted predecessor | `aef4e56ca2f7514f54b0c976fbdb400caef138b9` |
| frozen downstream contract | `c4eed12c0b9963fd65e296dcc4ce1940b5277570` |
| published draft | `b4164864e22c5745b863882238a69de63f2aae2a` |
| original REPORT / approved PLAN | `93e10babe0b9c9ef8b3f5277754541b447beeeb4` / `41fffb540c6483f5296ea0d33b789b75180d27ed` |
| independent report branch | `codex/cloud-dot-B10-full-review-1-20261009` |
| worktree | `/workspace/b10-full-review` |
| report commit | 发布后外部完整 SHA；不回填自身提交，不等于 reviewed candidate |

remote 的 fetch/push URL 均为 `https://github.com/y805939188/pokemon-essentials-clean-room.git`；首次 `ls-remote` 作者分支和拉取所得 FETCH_HEAD 均为 reviewed candidate。独立分支/工作树直接由这个准确提交建立，未派生子任务，也未等待或代替 affected 复审。只在本角色指定目录新增四份报告。

已读根 `AGENTS.md`、本候选派发包、绑定、完整 c4 合同及 `handoff/cloud-dot-20261009/original-contract.md` / `local-extra-rules.md`。仓库和环境没有可用 `.agents/skills`。请求配置保留 `gpt-6.1-sol / ultra / default（Standard）`；本云端委派任务没有可信 backend 回显，按派发包和人类 Plan A 记 **UNVERIFIED**。没有明确 unsupported/downgrade 回报，没有切模型/降档、配置/凭据变更或配额探测；缺回显不扩成新门槛。

完整冻结身份、对照差异、原稿应用和独立源/参数/保存核验见 [identity-checks.json](identity-checks.json)。七控制、两 minima、十项派发要求、11 shared003 扩展和15静态设计逐项结果见 [findings.json](findings.json)。作者的参数图和自检仅用于定位与声明比对；本报告的质量判断来自自行检查固定参考文本、候选条款、原稿及目录，不消费作者自检为独立 PASS。

| 控制 | 独立结果与证据 |
| --- | --- |
| GIR-FD82-003 | PASS_LOCAL_CONTRIBUTION。净化 WP46 的 OHKOIce 行去掉源父子类/保存检查组织，保留原定义、默认条款加载且无后续覆盖条件、专用准确率及AI区别。延迟来源使用计算输入与席位关系行为，保留必要身份、持久写回和真实清理副作用。完整11扩展裁决逐项保留；本地扩展为 B/B-03 的 WP46 OHKO，其余具名扩展路径相对接受前驱字节不变，不据此批准其他 contributor 或关闭003。 |
| GIR-FD82-B010 | PASS_LOCAL_CONTRIBUTION。WP43原/净及WP46的冰OHKO入口一致。独立核原定义和较后条款、PBS与AI：默认加载且无覆盖、条款假、双方L50、非冰U、冰T、q30、无结实/其它前门，资格不因冰类型拒绝；专用阈值20，r19可中/r20落空；冰U阈值30。条款真/目标L51/有效结实各自拒绝，仍不承诺必中或必倒。TD25–26保留独立对照。 |
| GIR-FD82-B015 | PASS_LOCAL_CONTRIBUTION。WP45/WP46原/净补齐复制来源当前个体数值之前的交叉清理：当前存活成员指向保存来源席的着迷、紧咬、黑色目光、Octolock、天空摔；正锁定计数连位置清除，束缚清计数/来源且保留束缚招式身份。来源仍在场、目标/来源不可用、别席、零锁定计数有分立对照；替补仍在该席也不保住新关系，后续失手/无效不回滚。正常尾部恢复来源失败记录/清辅助值，早退归零但不补尾部。既有R10原行保持，P06–07补边界。 |
| GIR-FD82-B016 | **PASS_PRIMARY_MINIMUM**。自行从固定参考常量及已读共享消费者逐65项核对象、项目、请求量和顺序，全部与候选及正确原表一致。Shift Gear速度+2先于攻击+1，反馈两级后一级；速度+6对照只升攻击。V-create速度→防御→特防各−1，速度−6仅略过首项，对侧全灭整组略过，成功项不回滚。两项镜甲参数仍独立在附表§2.4及主文§5.3，中央模式破坏者与招式预检分开；SS38–40原行及SS41–42完整。 |
| GIR-FD82-B017 | **PASS_PRIMARY_MINIMUM**。WP44原/净委派已由WP46正文/原稿/两覆盖表接收。PBS→实际效果→普通目标门→HP/持物写回→两端恢复物品入口独立核查。一次m=floor((U.hp+T.hp)/2)，U先T后，各自上限；51/60与150/200→60/100，合计201→160。奇数和及异上限不重算m，局部恢复不重查可恢复资格，单独HealBlock不拦；未绕替身/保护在前门拦。局部扣HP不新增普通直接伤害、受伤或跨半登记，也不清旧记录；恢复达到半HP按共享规则清跨半。均分反馈后U→T物品检查，即使相等HP；双有效ORAN的50/100→60/60并各消费持物，持久HP/持物写回，检查有条件。MH39–44逐行有正反例。 |
| GIR-FD82-B018 | PASS_LOCAL_CONTRIBUTION。净化六主组独立重算30/22/44/23/4/16，共139且唯一。原139逐行身份、顺序和归属不变；六组既有身份/归属正文不变。HP均分另列1项，总140和旧139分母明确区分。域外组标签1/45/20/28/29/9与枚举一致，不增删效果来凑数，不制造缺失行为或声明全集覆盖。 |
| GIR-FD82-C011 | PASS_LOCAL_CONTRIBUTION。独立核防御/特防交换读取、菜单初读、写入和当页缓存。原100/200且空间正，防御输入300→缓存防御300、战斗200/300、子菜单重入200/300；独立特防输入400→缓存特防400、战斗400/100、重入400/100。空间关对照同名读写。原/净正文和TD22–24一致，非变身/仅子菜单/无重置、回合推进或总退出刷新限制完整。 |

13个正式路径的完整候选 bytes、Git blob、SHA256与长度全部匹配派发候选清单。完整未过滤接受前驱→候选/c4→候选/草稿→候选分别包含37/32/12个路径，正式路径13/13/5；每个变化路径、diff SHA256/长度及hunk坐标已保存。正式条款的完整hunk逐段审阅。接受前驱比较中的五个c4行政新增路径，包括 cloud-takeover 的旧 registration 派发包，与c4字节相同；精确复用其已发布独立登记报告 `88931e4674351ff7d667c5c29af64ea7079ecdab` 的限定登记/统计/53读8写结论。此复用不转成B10行为通过，也不递归恢复历史证明树。

五个具名原稿的草稿before及候选intended_after全匹配授权收据，固定proposal补丁blob/哈希保持，实际只涉及12个hunk。原WP44正确65参数和除HP委派行之外其余原表行逐字保持；原WP46的139行身份及归属逐字保持。提案补丁与Git重新输出的diff有不同header/context格式，接受依据是固定授权补丁身份和五份准确结果字节，没有要求不同格式的diff文本相同，也没有自行应用或修复原稿。

两目录独立检查全314条已接受旧原行：combat159、pokemon-rules155，全部原始字节、顺序和multiplicity保留。派发所称227是其中不含连字符的ID行72+155；BC/CM/SW的87行也纳入本角色检查，没有被数字摘要遗漏。两目录只增加15个具名静态设计：TD22–26、SS41–42、MH39–44、P06–07；ID唯一，原R10及其它所有者完整section保持，15行各自前提、有序结果、逆向/邻接边界与对应正文一致。静态设计不代表已执行行为或运行观察。

公共approval-ledger、traceability-successor、finding-ledger、final-integration-review、最终README/index与scope-statement均与接受前驱blob相同。未把作者候选标成正式接受，没有写公共登记、改参考、改历史报告或其他review目录。当前仍10/21接受批次、194接受贡献、canonical229OPEN/0CLOSED；B10/B15正式写串行、其他贡献者与future affected gates保留。

参考通过Git获取固定 `Maruno17/pokemon-essentials` 提交 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 到独立 `/tmp/b10-full-reference`，只读静态核对19个具名源/数据文件的相关段；逐65常量比对不冒称该大文件全部行为分支已覆盖。审计里只保存定位/哈希/独立行为结果，不输出源码片段或未来类结构。HP均分、实际行动入口/物品检查时点、OHKO原定义/默认条款/AI、延迟回合末/来源初始化/当前存活枚举、空间菜单/有效读取及共享HP/持物入口均自行核对。

保留U01–U10、G01–G12、AX01–AX20及完整具名未读/未验证范围：Data/Scripts.rxdata和其它二进制/序列化资料、执行文件/宿主DLL与mkxp.json、真实地图/事件、媒体/图像/音频/字体/音源及宿主输出/容量、八个杯赛名单引用文件和pokemon_metrics样本、备份/生成目录、实际插件组合/动态调用/deprecated别名/EventScene/动态阴影可达性、真实Demo链、条件性67树果及其余非本地责任。参考程序、Ruby、游戏、编译器、转换器、生成器、反序列化器、保留作者/reviewer代码和行为模拟器均未运行；仅临时Git/hash/JSON/text账务核对。已执行行为向量、runtime observations、proven Demo chains均为0。

本有限范围结束。没有本角色具体阻塞或下一冻结返修要求。父统筹仍须按各自派发范围消费同一准确候选的B04/B08/B09/B05/B14独立affected结论后才可AREG-G；本报告不决定那些角色的影响处置。整合后另冻结实际SHA，再取得full与required affected actual结论及完整前驱→实际/候选→实际差异，才可AREG-C。main合入、canonical关闭和第三轮全局review均不属于本次授权。
