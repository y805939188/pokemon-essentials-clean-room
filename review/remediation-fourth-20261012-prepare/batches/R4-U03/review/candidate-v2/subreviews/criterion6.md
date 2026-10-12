# R4-U03 candidate-v2 标准6有限独立复验

**PASS**。固定候选 `d7875398e130b5bfa621c55d6c016ee0f8965cf7` / tree `8c763de4279e5140e64cd0a9fe58a820ea2cb92b`；报告起点 `165b01ce06ff88e5c5f50df7a11d017417ed1213` / tree `8938c8ff5578fcbb3bd1d5f7a456ab569810fbae`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。任务 `/root/forms_pokedex`，真实可见thread `01a130df-c0bc-77de-8587-1bfc63810031`（CODEX_THREAD_ID）。普通/default速度、Fast=false；实际回显UNVERIFIED。

原标准6（整批第30条，SPEC_STATIC）：普通刷新保留true/false原记录与多项Forms选择器首轮写false分开；多项选择器反向例需独立合法多项夹具。

只复验PD05 L220、DX05 L785的前提修订及四组必要对照。两行已明确默认RATTATA、显示全部关闭、基础male0与Alolanmale1均已见（可仅异色）、初始[0,1]确在可列列表且>1。正式差异仅两行输入前提，预期和NOT_EXECUTED未变；新镜像与候选正文逐字匹配。

| 独立对照 | 完整关键前提、推导与结果 |
| --- | --- |
| MATCHED_MALE_ALOLAN — PASS | 固定R默认数据，DEX_SHOWS_ALL_FORMS=false，无插件/额外改写。；合法RATTATA基础0和具名且展示自身的Alolan1；物种/metrics/地区/玩家/已见或拥有入口资格、前序界面/消息/输入及条件资源正常。；各案例独立重置，尚未发生其它形态浏览写入；进入选择器首轮仅BACK、其余输入查询假。条件媒体不作为实际存在/像素/宿主通过证明。；基础雄性0及Alolan雄性1均已见（可仅异色），末次[0,1,true]；初始[0,1]确在可列列表，可列项>1。<br>基础male0可列；具名两性Alolan先查雄档且雄档已见，列male1并停止该形态的性别遍历。按形态/性别排序，初始匹配male1；首轮先三参写入该项false，再处理BACK；退出不回滚。<br>结果：[0,1,true] → [0,1,false] |
| FEMALE_ONLY_MISMATCH_REVERSE — PASS | 固定R默认数据，DEX_SHOWS_ALL_FORMS=false，无插件/额外改写。；合法RATTATA基础0和具名且展示自身的Alolan1；物种/metrics/地区/玩家/已见或拥有入口资格、前序界面/消息/输入及条件资源正常。；各案例独立重置，尚未发生其它形态浏览写入；进入选择器首轮仅BACK、其余输入查询假。条件媒体不作为实际存在/像素/宿主通过证明。；独立改为基础male0已见、Alolan1仅female已见（任一异色），maleAlolan1未见；合法雄性异色Alolan1个体经最近见到入口形成末次[0,1,true]，不登记seen_forms；可列项>1。<br>列表含male0/female1，初始male1不匹配；索引回首项male0，首轮BACK前写[0,0,false]，退出不回滚。此反向现在不满足修订向量的maleAlolan1已见/匹配前提，所以不再构成歧义；既有反向正文/PD31/34/B38保持。<br>结果：[0,1,true] → [0,0,false] |
| ORDINARY_REFRESH_BEFORE_SELECTOR — PASS | 固定R默认数据，DEX_SHOWS_ALL_FORMS=false，无插件/额外改写。；合法RATTATA基础0和具名且展示自身的Alolan1；物种/metrics/地区/玩家/已见或拥有入口资格、前序界面/消息/输入及条件资源正常。；分别独立使用合法既存[0,1,true]及[0,1,false]；只普通主预览/Info/Forms刷新，未进入选择器，也无调用方另写最近见到。<br>刷新读取末次性别/形态，图像参数固定false；刷新本身不写末次表，存储true/false分别保持；不能以首轮写入解释进入前普通请求。<br>结果：true/false原记录各保持；图像请求普通 |
| SINGLE_BULBASAUR — PASS | 独立合法默认BULBASAUR雄性0，已见/拥有、末次[0,0,true]，可列项仅1、正常依赖、无插件；Forms页USE尝试进入，或仅普通刷新。<br>入口要求可列项>1；单项不进入选择器，不产生首轮写入，普通刷新仍不改末次。<br>结果：保持[0,0,true]，无该首轮写入 |

源锚点：Pokedex_Entry139–199、446–478、506–511；Player_Pokedex61–69、129–139、195–227；Pokedex_Main766–768；Settings307–311；Species175–195；PBS RATTATA基础469–479/Alolan74–87。正式锚点：WP62 158–168；WP66-B204–217；PD31/34 146/149、PD05 220；B38 285、DX05 785。均按固定commit实际重新读取；没有以作者自评代签。

原独立质疑仍成立于独立femaleAlolan-only状态，但该状态已不满足新向量前提。旧PD31、PD34、B38行与v1完整相等；WP62/WP66-B正文完整字节相等。核对的是本标准所需分支，不新增这些整文件或其它29条语义签名。

新增行为执行 **0 / NOT_EXECUTED_THIS_UPDATE**。这里只执行Git/JSON/字符串身份工具核验与报告写入；未调用参考函数、行为模型、宿主、UI、物理输入或Demo。普通/异色媒体及正常依赖仍为条件前提；真实像素/裁切和插件未知。

原6项/29条证据仅按 `0bdfd26ef95ced597db5d924a69d0e35de9a188b` 与父绑定snapshot `a44a5c692252fc991ac591708199df14e6751ce1` 的原限定scope复用，未重做、未重新签成v2 PASS。本报告只给标准6的候选静态PASS，不登记actual/接受/关闭或提前关闭依赖。标准6无剩余阻塞。

实际read-ledger（完整identity/hash和JSON指针在同名JSON）：

| commit | path | 本次实际内容范围/指针 |
| --- | --- | --- |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/001_Settings.rb | 307–311 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb | 61–69;129–139;195–227 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb | 139–199;446–478;506–511 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/016_UI/003_UI_Pokedex_Main.rb | 766–768 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | Data/Scripts/010_Data/002_PBS data/008_Species.rb | 175–195 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | PBS/pokemon.txt | 469–479 |
| 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | PBS/pokemon_forms.txt | 74–87 |
| d7875398e130b5bfa621c55d6c016ee0f8965cf7 | deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md | 158–168 |
| d7875398e130b5bfa621c55d6c016ee0f8965cf7 | deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md | 204–217 |
| d7875398e130b5bfa621c55d6c016ee0f8965cf7 | deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md | 146–149;210–222 |
| d7875398e130b5bfa621c55d6c016ee0f8965cf7 | deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md | 285–285;775–787 |
| d7875398e130b5bfa621c55d6c016ee0f8965cf7 | review/remediation-fourth-20261012-prepare/batches/R4-U03/author/candidate-v2/author-report.md | 1–11 |
| d7875398e130b5bfa621c55d6c016ee0f8965cf7 | review/remediation-fourth-20261012-prepare/batches/R4-U03/author/candidate-v2/criterion-6-response.json | 1–69 |
| d7875398e130b5bfa621c55d6c016ee0f8965cf7 | review/remediation-fourth-20261012-prepare/batches/R4-U03/author/candidate-v2/correction-and-verification.json | 1–633 |
| d7875398e130b5bfa621c55d6c016ee0f8965cf7 | review/remediation-fourth-20261012-prepare/batches/R4-U03/author/candidate-v2/derived-vectors.json | /records IDs R4-PD05 and R4-DX05 only; checked against exact candidate rows |
| 0bdfd26ef95ced597db5d924a69d0e35de9a188b | review/remediation-fourth-20261012-prepare/batches/R4-U03/review/candidate-v1/criteria-results.json | /records/29 only; prior criterion6 original wording/objection; other29 not re-reviewed |
| d7875398e130b5bfa621c55d6c016ee0f8965cf7 | AGENTS.md | full content read in previous turn; bytes equal previous review AGENTS; no new instructions or semantic expansion |
