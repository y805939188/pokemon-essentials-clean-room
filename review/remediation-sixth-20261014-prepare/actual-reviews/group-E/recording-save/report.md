# R6 actual group-E：recording-save 独立辅助内容复审

冻结实际整合 `86bbc99b28d93db4ed9d6897daf5f3725ccd1808`，workspace tree `67e8c55d520fa8cad2928cb4b95e24c3ed602d5a`，formal tree `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`：**GR6-F-V005 与 GR6-F-S001 各七组均为 INTEGRATED_CONTENT_PASS，限定 SOURCE_STATIC。** 修复后的 SF30 d/e 已写入实际正式测试目录，两个活动保存及异常前缀没有在共享整合中丢失；Palace 严格正最大值与后段标记分流也完整落盘。本轮未发现需正文修订的缺口。

本审者 `/root/recording_save` 是原非作者辅助审读者，未参与候选或正式稿撰写。本轮只写本目录，未切分支、提交、改正式稿/台账/旧报告，不派生新任务，不用 CLI 探配置。请求 gpt-6.1-sol/ultra/default tier/default speed；actual model、effort、tier、speed、平台 UUID 全为 **UNVERIFIED**。本内容意见不签整个56项的 INTEGRATED_PASS、配置合格验收、正式接受或 CLOSED。

旧 FAIL 仍绑定 `00b45de642f07cee9953e42f04cce9c35d77346f`，报告发布 `3ef4854ef43eac92fd1dc57350e4cf6aa160082b`；修订审查绑定 `9971fe84896786645cdcda3ab45e5caf7785cabc`，发布 `411b563309a4e642e628dcf8289e36c6fe3fd37f`。旧结果和局部未执行边界均保留，本轮新增判断绑定实际组成，不用候选 PASS 代替实际全文复审。

## 输入、完整阅读与工具层次

固定源 R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。新读取 actual-review-input 的相关 `/files`、U10/U11/U13 `/batches`、全部 `/root_edits`、`/resolutions`、`/receiver_delta`、`/review_requirements`、`/administrative_sync` 与状态/执行边界，完整投影和实际 JSON pointers 在 `actualcommon-projection.json`、`actualfiles-projection.json` 及账本中。输入共53个变更文件、56个 required IDs，本报告只签责任两项及其明确接点。

完整新 U13 合同 bytes370944、SHA256 `f202a22b1faf72a80edd2d663b9326bf4a9b9be4409fe88780835de909b08473`、blob `8c05e33d56064ff5a79ea25545f696b6156f4543`。本人完整读取并解析469a/00b45/9971/86bbc四处载荷，strict equality 且实际字节/身份全相等；没有合同格式或语义差异。责任 `/scope_contracts/6`（V005）、`/7`（S001）的完整七组、original_full_proposal、原证据/反证与通用要求，明确复绑本人3ef旧完整阅读资格；新通用字段再次完整呈现。`contract-qualification-binding.json` 分开新完整机器读取与旧语义资格，不冒称本轮重新语义审读全部八项合同。

以下五份**实际正式文件全部新完整语义读取**，不是只看 diff 或绑定旧正文：

| 实际正式路径（均在 deliverables/final-specification-set/） | 新完整行范围 | bytes | SHA256 | Git blob |
| --- | --- | --- | --- | --- |
| pokemon-rules/wp53-safari-and-bug-catching-contest.md | 1–288（分1–144、145–288） | 51237 | 1a9c9581d7b91bf5e4dd5474b9e2f4fef4115e795d7122663eb743e55bfaa999 | 5acc4f03fcecd49001325ff218034f00aff8a20a |
| combat-requirements/wp56-palace-and-arena-variants.md | 1–141 | 19053 | fee7a028ad9b1db8fae48145b092b18efc89757db943eb6e3f234ace7c111368 | 0ff4bc7581fa77266d28ed2477c9dd68ed1edde5 |
| combat-requirements/wp58-battle-recording-and-playback.md | 1–181 | 26575 | 91afabffb2bc6def0f1db64835b1833751613392a26735ba863994ed49d7f061 | a5c353899283ff599042779ce960fcd1061ec881 |
| test-catalog/combat-requirements-wp54-55-56-58.md | 1–177 | 33561 | e6336cc59798b5f02dfe92c0e799344a3aa652627b2adfacbe6861562537f1c8 | cc28e3400d3bab787ce66c18156c45bcba6e5829 |
| test-catalog/pokemon-rules-wp53-60-61-62-69-70.md | 1–286（分1–91、92–188、189–286） | 63657 | 023684dbcb844df2b51855f165baa778cc6c3c5bf1b4c8aca93e8eabef268341 | 13eb3ec4f418e1736c886cb5840ba743a264a85f |

实际必要消费者的新完整单元为：WP09全1–179；WP65 §§4/6（83–101、148–176）；WP17消息/选项单元59–124及状态更新251–270；WP38全1–146；WP18创建/上下文164–224；WP66-A Mark180–185；WP67-A捕获/存储210–239及模式299–311；WP62写入32–83及展示147–177；WP40命令45–77及Mega/Call/Shift274–302；WP55包装/失败114–133；WP42终局166–192；UI测试目录U10消息观察点、容量和Mark完整单元947–994（呈现到1001，不把后面的重学表冒称完整审读）。这些是责任相交单元，不冒称相应大文件全部全文。

固定源既有18个完整/必要阅读单位的 bytes/SHA/blob与旧3ef真实范围再次核相等，资格清单在 `identity-and-coverage-checks.json/same_source_qualification_bindings`；其中 Palace、ActionSwitching、PauseMenu、Save/Value/Metadata、Messages/Stats、Conversion/SaveConversions、RecordedBattle/Challenge_Battles 的实际旧范围继续适用，不声明本轮重读全部源。新接口回源的精确范围另在 `reading-ledger.jsonl`：SafariBattle279–502（含完整构造/模式/开始单位）、BugContestBattle1–83、CatchAndStoreMixin1–111与112–221（完整存储/登记/投球单位；数学尾部不作全文声明）、Battle_Peers默认类1–60（呈现至74）、Utilities_Pokemon1–11与8–67（完整联合门、昵称/存储单位）、Storage1–42/119–154、Trainer69–89、Pokemon构造1159–1227、Summary Mark1078–1192及Options1193–1231/Scene1270–1341、ActionOther1–66、WildEncounters211–218、Overworld步进197–218、BattleStarting125–201与306–442（实际呈现范围119–205、300–435、436–444）。其它源行未计入新完整阅读。

自有 `check_actual.py` 仅做有限文档/hash/行覆盖/原始数量检查，exit0 收据为 `execution-receipt.json`、stdout/stderr。它核了实际 commit/workspace/formal tree、相关八个 input文件身份、五份新全文联合范围无缺口；前四文件实际字节精确等于9971镜像。pokemon完整 SF 前缀精确等于U13修订，完整非 SF 后缀精确等于U11，保留全部新Dex和旧共享条款。先保存原始行序列再重数 QC49/WS36/PA32/RC29（含W22b）/SF40，各原始数与唯一数相等。这些机械结果不签语义 PASS。

根 AGENTS 新全文读完。初次宽文件导航及过大投影/旧历史导航出现截断，均不算全文；后续五正文、必要JSON投影及单元分段输出无截断。两次错误猜测正式 WP38/WP41 basename 的固定提交查询确实返回 path-not-exists，随后找到正确名称；不把猜错的文件名当作证据缺失。`navigation-reading-attestation.json` 保留区别；未捕获的早期 UTC 不重建。

## GR6-F-V005：INTEGRATED_CONTENT_PASS

| 七组 | 实际版本的新判断 |
| --- | --- |
| identity_and_verdict | PASS。V005/F-008、required/P2、单一根因与原提案身份不变；责任合同完整同身份。实际WP56及PA系列新全文读，并绑定86bbc，不代签其它Arena/设施项。 |
| bidirectional_evidence | PASS。固定Palace184–243及ActionSwitching9–33/77–105的已完整实读同源条件，对应实际WP56 78–80及PA-P32第141行。源“严格大于初值0才建立best”与正文候选、反例和后段消费者双向相接，未把整数0%当倒下。 |
| premises_and_counterexample | PASS。h24、无状态修正/早分支/换人阻碍、旧标记false、唯一合法存活1/205、r0：百分比0不建立best，基础30命中，后段先标记true再登记首合法并返true；3/205为1，仍基础30却最佳早返、标记false。无合法后备为标记true/返false，两个正同值后备保先者。条件有效，未以畸形HP或实际运行补证。 |
| minimum_revision_contract | PASS。实际WP56 78明确初值0、无候选、严格增大和正同值保先者；79–80保早返跳标记与后段先写标记的差异，概率门和状态修正没有改。实际目录具名P32四子例落盘，无需修订。 |
| acceptance_and_regression | PASS。新完整PA-P01–32读得P10/P11概率档、P12无后备、P24早返、P25未命中、P32相邻0/1%及同值对照均保留。因子30依据固定源静态推导；工具不独立计算概率语义。新WP58关于Palace随机不入录像、实际登记与回放分层及WP40实际命令接点一致；不因同因子推相同标记。 |
| independent_adjudication | PASS。新实际全文反向检验“0%即倒下”“数学最大为0也必建best”“早返与后段都必须写标记”“不变候选可直接充当实际签名”，前三项被固定合法/严格门/早返否定，最后一项由本次实际全文和接口新读代替。配置合格验收仍UNVERIFIED。 |
| dependencies_and_receivers | PASS（责任内容接点）。实际WP56→combat PA目录及WP58/普通换人登记接点均接通；保留源行为身份与数据身份，不增加未来源类组织。公共feature-matrix/source-traceability同期登记由R6-I在实际审查门后执行；本报告不宣称已同步、正式接受或关闭。 |

## GR6-F-S001：INTEGRATED_CONTENT_PASS

| 七组 | 实际版本的新判断 |
| --- | --- |
| identity_and_verdict | PASS。S001/F-009、required/P2及原根因保持；普通Quit Game、专门Save、两模式专用退出仍是同合同内不同入口。实际SF30-d/e恢复正确控制，不新增ID、不撤销00b45的旧FAIL。 |
| bidirectional_evidence | PASS。固定MenuHandlers101–116、PauseMenu254–272/304–321→UI_Save100–128→Game.save111–125→Value/SaveData→整体player/global的旧完整源链，反向对应新实际WP53 239–248、WP09 127–131、WP65 88–100/167–174及SF30/36–40。无活动对象排除或普通Quit门被新增；源查询与实际正文均给明确可达前提。 |
| premises_and_counterexample | PASS。活动Safari区域/未到期有效捕虫、有效玩家/地图/登记值类型/对象图/资源/确认/写入、无无关更新/到期回调，确认退出、保存和必要覆盖正常返回时，活动会话可进入serializer输入。捕虫player仍[S]、global含spares/K/计时起点，不先拼队或判奖。仅是静态可达，计时起点重载语义仍UNKNOWN。 |
| minimum_revision_contract | PASS。实际WP53 15/239–248、SF01/30/36–40正文明示专门Save隐藏与普通Quit分开；SF30第40行 d正常结束保存→普通载入、e固定当前默认转换集合精确来自修订，前提、模式统计、clock未知和NOT_EXECUTED都保留。未恢复全活动禁存或把默认无专用迁移扩大为任意插件/版本/整个存档無迁移。无最小正文修订。 |
| acceptance_and_regression | PASS。完整实际SF01–40含A/B/C活动对象图、拒Quit、拒Save/覆盖、caught IO与未捕获异常全部具体分支；恢复正常/转换独立控制。SF35伙伴/force-single与新U10联合容量、捕获保留/统计接点不冲突；完整pokemon目录保U11 Dex新增记录消费者，未以表行存在代语义判断。 |
| independent_adjudication | PASS。新反向检验专门Save门是否阻止普通Quit、正常载入是否证明活动时钟恢复、false保存是否阻止退出、未捕获异常是否保证退出、单员是否保证大会覆盖、盒全满是否一律挡Safari球、拒替换是否撤销已捕获记录：由分别的源门/前缀、实际正文与具名新单元否定；每条仅限其已述正常或失败前提。 |
| dependencies_and_receivers | PASS（责任内容接点）。实际WP09、WP65、WP17及WP53对象/菜单/时钟链新读一致；实际WP38/WP67-A/U10表、WP18/WP66-A、WP62和共享pokemon目录具体接点已新核。WP66-A人数接收与WP54/QC属同组另一责任审者的实际审查，本报告不替该责任签名。公共同步/配置/正式接受与CLOSED仍分层待办。 |

失败前缀在实际版本保持：拒Quit只刷新重开、无保存；接受Quit后拒Save或在异存档＋新游戏未保存门下拒覆盖，保存调用前返回false，普通退出忽略值仍置空场景。接受保存先清新游戏未保存标记，正常持久前缀写safesave/count/magic/最近时刻，随后取值/校验；被捕获IO/SystemCallError只回退count、文件可截断或部分写，正常返回false仍退出。取值类型等未捕获异常保已写前缀，不保证画面清理/退出尾部；参数校验在前缀前，与取值校验分开。实际WP65“进程结束”的旧简称只按该段正常返回的场景置nil理解，不提升为宿主进程实测或异常尾部保证。

实际WP17 261–267保微更新地图/非淡出门、各入口调用时序及异常清理非保证；WP53 132/241、SF17/37保未到期与无无关回调前提。消息窗显示期间到期回调受门推迟，暂停命令循环本身并非全冻结；确认/反馈正常返回后若有其它更新，不能据本例承诺活动对象永不改变。SF30 d已正常结束的控制也不承诺所有载入统计字段绝不变化，只保两模式统计持久和会话非活动态。

## 新共享消费者与精确历史接点

**容量和保留。** 新实际WP67-A304、UI U10-SF01–05第969–977行与WP53 79/SF07相同：仅玩家队伍满且全部当前盒满才拒Ball；拒绝消息正常返回后next，扣球、投球和本次回合末未到。仅箱满而队伍有位、或队伍满而箱有位均放行。固定Utilities4–6、Storage30–32/141–146及Trainer81–83共同支持联合门，Safari439–449顺序支持拒绝前缀；异常在扣球后不自动退球。捕虫覆盖的pbStorePokemon58–77在公共记录入口90–104之后，拒更换只不保新个体，不撤销图鉴/捕获计数；正常最终接收先拼队再检查联合容量（WP53 125/171/269、SF15/21/22，Utilities33–43）。这与保存活动K/spares是不同消费者，不合并成所有捕获必入队或所有盒满皆失败。

**伙伴与单员。** 实际WP53 154/SF35保旧B12/B026的准确前提。新固定WildEncounters211–218为force-single/Safari先假、伙伴先真、单员假后置；Overworld197–218实际产生两敌候选，BattleStarting356–373只对单敌且允许覆盖派发；171–201伙伴参与及306–329正常善后相接。故活动缩队[S]不保证大会接管：伙伴分支普通2v2不传入/回写大会预算、不覆写K、普通击败治两队且无单敌结束通知；无伙伴或force-single真才可按剩余门接管。既不把序列化单员推成遭遇单员门必胜，也不否定明确前提下的正常接管。

**WP18与局部摘要。** 实际WP18 179/205仍为新建空markings列表、捕获沿原个体，不因持久化补成六零；WP66-A182–184把独立ACTION缺槽异常限定在非战斗Mark入口。新固定Pokemon1190、Summary1078–1191和Options/Scene支持缺失/显式零及BACK/USE优先。捕获去向的See summary由Mixin65–68以inbattle=true打开，Summary1292–1295不进入普通Options，因此不能把缺槽ACTION泛化为该捕获查看摘要一定失败。空列表本身也不是整体Player/Global保存类型错误；若此前真实发生局部异常，本轮活动保存例的正常依赖前提已不成立，不能制造保存必失败的新结论。

**录像与持久消费者。** 实际WP58全新读，63/156明确四席、玩家侧一次命令消费、AI侧不再推进；非空伙伴2/3席是否失败依指令族，不把逃跑写决定也说成必解引用。WP40新命令/Call/Shift单元与固定ActionOther21–35及旧完整RecordedBattle资格相接：实际行动登记和录像钩子分开，撤销改选Call/Shift可保旧槽，不保证均空。Challenge40–105旧完整资格对应实际WP55 116–130/RC-W03–05/15：正常包装善后后清临时，仅胜/负/平重放导出；调试先清，未捕获异常前缀不保证到清点；提升把临时值覆盖全局并清临时，播放不删除/更新记录。整体global随保存与回放副本仍可写实时图鉴是不同接点。

实际WP62 42/44、WP42 177–179与WP58 150、RC-W22/W22b第170–171行仍准确分出全局形态登记与按队伍下标读参战标志：首发下标0例可写BURMY形态1，后备下标1仅换入席0例不能用“实际参战”替代标志。实际WP62 174–176和新R6-PD01–03第158–166行保U11选择器首末回绕/下一循环写false、BACK不撤销；它没有移动战斗参战标志或将存档时钟证明扩大。

历史资格按 `historical-qualification-binding.json` 复绑已完整责任投影：固定d81562b的B13 `/controls/0,3,6,7/complete_current_control_fields`（003/B018/B028/B029）。新实际保必要模式/共享身份/格式，不新增源组织；B018的RC W22b及新29数量独立重数；B029的RC W16/W24/W25/W26、WP58§5.2完整生产消费时点保留，不能以直接调用计数删域；B028连续第3/4/5轮与首次三轮边界在实际PA-P28及WP56仍完整。B12/B026的旧具名peer资格与本人新SF35回源分列，不冒称本人新全文读巨型旧历史。R1原WP限定、R2 229/21/341、R3 23/76、R4当前17/76与旧16/75、R5唯一92 CLOSED的原分母及未执行限制没有被本两项内容结论改写；不签整个R1–R5历史新全局PASS。

## 剩余门与未执行

公共同步在冻结actual input中明确为R6-I的 **DEFERRED_UNTIL_INDEPENDENT_ACTUAL_REVIEW**，目标 `planning/feature-matrix.md`、`audit/source-traceability.md`；尚未写入或审查这些最终公共登记字节。本报告将它列为同步pending，不把既定后置台账责任误作当前已修正文的缺口。其它责任ID的实际审查、WP66-A人数接收、完整共享总接合、配置障碍的准确处理、正式接受、CLOSED登记仍由root分层完成，本报告不越签。

本轮参考程序、作者脚本、serializer/独立行为模型、fake/isolated writer、真实保存/读档、真实录像播放、宿主窗口/进程、地图事件可达性、媒体/Demo执行均为0。只有自有有限文档检查执行，SOURCE_STATIC、DERIVED预期与TOOL层分开。重载单调时钟、未绑定插件/动态组合、宿主效果继续UNKNOWN。两责任ID无正文最小修订；若后续改动这些冻结内容/接点，须按新载荷另审。
