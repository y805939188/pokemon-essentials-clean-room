# R4-U03 候选独立子审：动态形态取图与图鉴普通外观

固定候选 `58cd8b1585f17199a65c7b82afadbe0e326d9d30` / tree `c1b72453613645ac5e9928e748364348c1bd179c`；B `1f36475d22120a0d1175967d5b17d71fe8311d88`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；报告证据树 `f28d1376a736ea75405cf6e9aeb4a58349618f41`，任务包 `08a57fb55118914a74ac1ffaf617647c01df8938`。任务 `/root/forms_pokedex`，真实可见 thread `01a130df-c0bc-77de-8587-1bfc63810031`（CODEX_THREAD_ID）；请求 gpt-6.1-sol / ultra / default / Fast=false，实际回显 UNVERIFIED。

结论：GR4-M04-001 **PASS**；GR4-M11-001 **REQUIRES_CHANGES**，仅第6标准的两条新多项向量前提不足。固定普通外观、保留异色记录及选择器首轮写入正文规则均支持。未自修、未接受/关闭、未签actual或全域。

## 本次剩余问题

**FP-M11-VECTOR-PRECONDITION · P3**：图鉴测试目录220行 R4-PD05 与UI测试目录785行 R4-DX05缺少初始雄性Alolan1可列的前提。

独立合法反例：固定默认数据、DEX_SHOWS_ALL_FORMS=false；基础male0已见、Alolan1仅female已见（任一异色均可），maleAlolan1未见。再对合法非蛋雄性Alolan1异色个体调用最近见到，末次成为[0,1,true]，该入口不登记seen_forms。前序场景、metrics、消息、输入及媒体正常，无插件。可列表为male0/female1，项数>1；普通刷新仍保持true。进入选择器不移动即BACK时，初始male1匹配失败、回首项，首轮实际静态推导写[0,0,false]且不回滚；新增两行却指定[0,1,false]。

源依据：Settings303–311；Player_Pokedex61–69、129–139、222–227；Pokedex_Entry154–199、446–478。既有正确反向：候选WP62 164–168、WP66-B208–210、PD31/PD34（测试目录146/149）。源与正文均已明确性别门和不匹配回首项，因此这不是普通图像主规则错误，也不重开旧CLOSED。

最小修复：只把R4-PD05/R4-DX05独立夹具明确为基础0与Alolan1均雄档已见（可仅异色），或明确初始[0,1]确在可列列表；同步作者向量镜像/映射。修订后应唯一推出[0,1,false]，继续保留仅femaleAlolan1/末次male1不匹配回[0,0,false]及BACK不回滚的反向；所有向量仍未执行。

## 逐验收标准

### GR4-M04-001 — PASS

| 原序号 / 批次序号 | 类型 | 结果 | 原标准与独立依据 |
| --- | --- | --- | --- |
| 1 / 1 | STATIC | PASS | 只凭正式集可区分物种内容记录读取与按个体精灵/图标取图；不再声称图像统一用简化形态。<br>WP18 151–152纠正内容记录与按个体取图分类；WP15 64、WP21 183明确正背精灵/图标/摘要继承普通动态读取。源Species_files 92–109/123–139与Pokemon 113–166支持，未从显式参数入口反推整链纯读。 |
| 2 / 2 | STATIC | PASS | 给定t+432001反例推出形态0/时间戳空；t+432000仍1；守卫和强制形态对照准确。<br>WP21 183及R4-IF01–04完整限定合法非蛋FURFROU、整数t、forced为空、运行状态/重算/图鉴依赖正常、无插件、此前未查询；严格超432000秒提交0清时间戳，恰阈值保持1/t。forced=0返回0而不提交；battle/storage/forced1分别阻断该动态提交。 |
| 3 / 3 | STATIC | PASS | 说明状态求值先于图像匹配；不把无素材当作静态入口不可分析，不宣称真实像素/游戏通过。<br>WP15 64与R4-IF01/06将求值/提交放在图像匹配之前；所有候选缺失仍不回滚，但未保证图标包装或摘要后续成功。源形态读取发生在查图之前；真实媒体、像素与宿主未证。 |
| 4 / 4 | RUNTIME | PASS | 本轮不要求运行参考/宿主；如以后执行，须独立记录输入/工具/输出与素材前提。<br>本次新增行为执行0；仅SOURCE_STATIC、SPEC_STATIC、手工DERIVED_VECTOR与Git/JSON/哈希TOOL_VALIDATION。向量NOT_EXECUTED；未来执行须另立素材、输入、工具和输出回执。此PASS表示本次执行边界满足，不表示行为运行通过。 |
| 5 / 5 | SPEC_STATIC | PASS | 保留WP35/EG-13/20已正确的动态孵化合同；显式物种资源接口仅在输入形态已求值时为纯消费，不外推调用者。<br>WP35和孵化测试目录B→C完整字节相同；已回读WP35 106–117/165、EG-13/20及孵化源动态参数求值链，保留A053原qualified分层。R4-IF05显式形态事先给定，不扩张上游纯读保证。SPINDA旧限定段/向量亦未变。 |

### GR4-M11-001 — REQUIRES_CHANGES

| 原序号 / 批次序号 | 类型 | 结果 | 原标准与独立依据 |
| --- | --- | --- | --- |
| 1 / 25 | STATIC | PASS | 仅读正式集合即可判定末次异色true时主列表选中预览、完整Info/Forms前后图及图标、简略Info均请求普通外观。<br>WP62 158–160和WP66-B 152/204/217列明主列表选中预览、完整Info前图、Forms前背图及物种图标、摘要完整单种、简略Info固定异色false，仍消费末次性别/形态。源Main 766–768、Entry139–151、各入口5–116/582–617支持。 |
| 2 / 26 | STATIC | PASS | 普通预览/Info刷新不改变保存的异色true；与进入Forms选择器首轮写false的已有合同明确分开。<br>正文与R4-PD01/02、R4-DX01–03区分普通刷新与摘要最近见到写入/多项选择器首轮写入。对合法既存[0,0,true]/false，刷新不清异色；选择器首轮三参写入另用默认false。源读取129–139、Entry139–151/446–478支持。 |
| 3 / 27 | STATIC | PASS | 有同性别/形态的末次true/false成对向量，及仅异色已见的形态资格对照；不将资源回退误作固定普通选择的原因。<br>R4-PD01/02、R4-DX01/02提供同雄性0形态true/false成对；PD03/DX04给仅异色已见与普通请求的分离。源seen_form? 61–69任一异色资格与check_graphic_file 3–34固定false没有闪光目录候选，普通选择不归因资源回退。 |
| 4 / 28 | STATIC | PASS | 不改WP15通用按属性取图合同，不把规则推广到队伍/摘要/战斗个体外观；新向量标记未执行。<br>WP15通用按所给属性匹配及回退正文B→C保持；本批仅对其个体形态入口作M04必要修订，未改变shiny选择规则。WP62 160和UI目录787明确不扩到队伍/摘要本体/战斗个体外观。新向量NOT_EXECUTED。 |
| 5 / 29 | RUNTIME_OPTIONAL | PASS | 不以当前无媒体/宿主阻止事实修订；如后来运行，应另提供正常/异色相异资源、命令输入及实际输出记录，不能把本轮静态推导标成执行。<br>本次执行0，普通/异色相异媒体仅为条件前提，不宣称UI、物理输入、联网、像素/动画/完整Demo通过；素材/宿主缺席不阻塞静态事实判断。 |
| 6 / 30 | SPEC_STATIC | REQUIRES_CHANGES | 普通刷新保留true/false原记录与多项Forms选择器首轮写false分开；多项选择器反向例需独立合法多项夹具。<br>REQUIRES_CHANGES：R4-PD05(220)、R4-DX05(785)独立RATTATA夹具只写已见基础0/Alolan1及末次[0,1,true]，未保证雄性Alolan1已见或初始项可列。合法仅雌Alolan1已见可使列表含male0/female1，保存male1不在其中，首轮写首项[0,0,false]而非新增行声称[0,1,false]。源Entry154–199/446–478和候选WP66-B210、PD31/34明确支持这条反向；局部修复见FP-M11-VECTOR-PRECONDITION。 |

## 独立质疑与旧范围回归

M04质疑了显式参数入口被误外推为整链纯读、forced0被误当提交、资源缺失被误当不求值或回滚。WP18 150–154、WP15 63–67、WP21 177–196及IF01–06均准确限定；正/背/图标各独立重置，摘要需前序构造正常。没有剩余M04反例。

M11质疑了把普通请求归因回退、清true后达到普通外观、仅异色已见无法列出及摘要写入被归到刷新；正文与PD01–04/DX01–04均排除此错误。再以仅雌Alolan已见但末次雄Alolan的合法多项反向发现上述P3问题。

- GIR-FD82-A053：PASS_SCOPED_PRESERVATION。完整批准前提/最小修订/静态反例已读；孵化核心不显式改形态与演出动态读取分开，DEERLING月2->1、月1->0及强制/战斗/仓库早门复用同源形态合同。WP35/EG13/20字节完整保留；不签旧229全域、不重开。
- GR3-M04-001：PASS_SCOPED_PRESERVATION。WP21 §3.2-R03和U03-SP01–10完整段字节保留；动态形态入口修订未改变编号组/锚点/2×2左上采样/重叠/颜色或PNG限定/GIF未知。源SPINDA注册及物种取图修改副本入口回读。
- GR3-M11-001：PASS_SCOPED_PRESERVATION。WP62 §5.3.1完整段和U05-HAB01–04/PD31–34保留；源可见点并集、正宽逐字符/缺尾/default1及门与新增普通外观不干涉。该PASS限定旧栖息地承接；新PD05/DX05问题不重开旧CLOSED。

## 实际读取与身份

完整读取AGENTS、reviewer、batch-contract、read-scope；完整读取两项canonical finding与handoff（M04 1–274，M11 1614–1874）及author acceptance-map相应完整记录。完整正式12文件B→C差异均已读；其它finding仅检查本批差异对两项的邻接影响，不代签其语义。

所有实际commit/path/ranges、JSON指针、完整blob哈希及12候选正式文件身份详见同名JSON的read_ledger / candidate_formal_file_identities。下表列当前source/正式内容读取范围（不把全字节哈希当全文件语义审查）：

| commit | path | 实际内容范围 |
| --- | --- | --- |
| f28d1376a736ea75405cf6e9aeb4a58349618f41 | AGENTS.md | 1–297 |
| f28d1376a736ea75405cf6e9aeb4a58349618f41 | review/remediation-fourth-20261012-prepare/tasks/R4-U03/reviewer.md | 1–19 |
| f28d1376a736ea75405cf6e9aeb4a58349618f41 | review/remediation-fourth-20261012-prepare/tasks/R4-U03/batch-contract.json | 1–194 |
| f28d1376a736ea75405cf6e9aeb4a58349618f41 | review/remediation-fourth-20261012-prepare/tasks/R4-U03/read-scope.json | 1–890 |
| f28d1376a736ea75405cf6e9aeb4a58349618f41 | review/remediation-fourth-20261012-prepare/resource-scope.json | 1–96 |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | review/remediation-fourth-20261012-prepare/tasks/R4-U03/findings-input.json | /authority; complete canonical_root_records entries GR4-M04-001 and GR4-M11-001 |
| 08a57fb55118914a74ac1ffaf617647c01df8938 | review/remediation-fourth-20261012-prepare/tasks/R4-U03/handoff-findings.md | 1–274; 1614–1874 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | review/remediation-fourth-20261012-prepare/batches/R4-U03/author/acceptance-map.json | /status and complete /records entries GR4-M04-001 and GR4-M11-001 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | review/remediation-fourth-20261012-prepare/batches/R4-U03/author/derived-vectors.json | /records IDs R4-DX05,R4-PD05 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/010_Data/002_PBS data/009_Species_files.rb | 1–150 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/014_Pokemon/001_Pokemon.rb | 105–222 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb | 1–156; 322–329; 412–440 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb | 1–146; 225–270; 282–316 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/016_UI/006_UI_Summary.rb | 90–154; 1200–1235 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb | 1–114; 120–231 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/016_UI/003_UI_Pokedex_Main.rb | 264–297; 406–456; 754–781 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb | 1–217; 226–278; 313–484; 495–619 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb | 1–119; 202–243 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/012_Overworld/003_Overworld_Time.rb | 194–207 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/001_Settings.rb | 303–313 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/010_Data/002_PBS data/008_Species.rb | 175–195 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | PBS/pokemon_forms.txt | 1–35; 70–90; 1630–1664 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | PBS/pokemon.txt | 1–32; 469–497 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md | 117–157 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md | 19–74 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md | 94–112; 134–215 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md | 11–45; 63–95; 117–184 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md | 142–155; 196–219 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md | 263–292 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md | 142–150; 200–222 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md | 773–787 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/creature-rpg/wp35-eggs-and-hatching.md | 96–125; 155–170 |
| 58cd8b1585f17199a65c7b82afadbe0e326d9d30 | deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md | 18–35; 66–78 |
| 1f36475d22120a0d1175967d5b17d71fe8311d88 | delivery/2026-10-12/evidence-navigation.json | /original_third_review,/old21_229_341,/qualified_scope_packet,/old_scope_and_runtime_not_promoted |
| 41fffb540c6483f5296ea0d33b789b75180d27ed | review/remediation-20261003-prepare/finding-acceptance.json | /GIR-FD82-A053 complete |
| 63244b0fc182734a8c808002e0244a2bce946859 | review/remediation-third-20261012-prepare/U07/actual-integration/qualified-regression-reuse.json | GIR-FD82-A053 identity/navigation records only |
| 1f36475d22120a0d1175967d5b17d71fe8311d88 | review/remediation-third-20261012-prepare/U03/findings.json | complete record GR3-M04-001 |
| 1f36475d22120a0d1175967d5b17d71fe8311d88 | review/remediation-third-20261012-prepare/U05/findings.json | complete record GR3-M11-001 |
| 1f36475d22120a0d1175967d5b17d71fe8311d88 | review/remediation-third-20261012-prepare/registration/finding-ledger.json | records GR3-M04-001 and GR3-M11-001; original identity navigation only |

工具核验：固定C tree匹配；WP35/孵化测试整文件字节相同，SPINDA正文/向量与栖息地正文、HAB/PD31–34行均保留；正式diff --check退出0。这些是TOOL_VALIDATION，不是行为运行。

## 执行与限制

**NOT_EXECUTED_THIS_UPDATE；本批新增行为执行0。** 未调用参考函数、行为模型、图像/动画/宿主、UI、物理输入或完整Demo。只执行Git/rg/JSON抽取、哈希/文本保留核验与报告写入。历史GR4的4次原函数回执不计本次执行，也不作为本两项行为运行证明。

媒体、真实像素/裁切/宿主失败、外部插件及地图事件仍未知；相异普通/异色资源仅为条件夹具。未来异色浏览政策未代选。只签固定候选两finding范围，actual整合/接受/关闭需后续独立门。
