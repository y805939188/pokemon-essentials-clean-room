# R8-U06 可选项与倒下音频第二语义检查

结论：在下列本人实际读取范围内，GR8-AI-001、GR8-UI-FAINT-AUDIO-001 两项必修及 AI002、CP01、F05 三项已采用可选均有原源支持，未发现语义阻塞。本报告是有界第二检查，不授予整批 candidate PASS、actual integrated PASS、ACCEPTED 或 CLOSED；未完整读取的整批输入明确列于末尾和独占 ledger，须由主审本人另行接收。

实际审阅上下文为 `/root/optional_audio_review`，不同于候选作者。请求配置 gpt-6.1-sol / ultra / default / 普速 / Fast off；无权威 echo，actual model、effort、tier、speed、Fast、opaque UUID 均 UNVERIFIED。没有执行 Ruby、游戏、宿主、媒体、保存/回放或行为模拟。

冻结输入：候选 `16f986afc1c85e64131f1dc8c6f2477a79c04029`；基线 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`；原源 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。本人只读身份核验确认：基线为候选祖先；R HEAD 匹配且工作树空；12 个 mirror 的 SHA256 均匹配 manifest；12 mirror 与已回读载荷 `0384629ccf1c2c492ebab611bbbb858f825e9a31` 字节身份相同；正式 subtree 与基线相同。工具核验只提供对象/保留证据，不替代语义阅读。

以下 M 指 `review/remediation-eighth-20261016-prepare/candidates/R8-U06/mirror/deliverables/final-specification-set/`，F 指 `deliverables/final-specification-set/`，R 路径均相对 `/workspace/pokemon-essentials/`。

## 逐项结论

| 项目 | 候选精确位置 | 本人对照及判定 |
| --- | --- | --- |
| GR8-AI-001 required | M `combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md` L215–221；M `test-catalog/combat-requirements-wp49-51-52.md` L170、L351–363 | 通过有限语义核对。原始槽类型发现与伤害招计算类型匹配已明确分开；世代≥6首槽、旧代全槽、排伪类型/已有类型；候选发现不滤 PP，helper 只排有限总 PP 正且当前 PP0，并查伤害/计算类型，不添加 Disable/Taunt 等完整资格。首匹配只 +14 一次；无匹配保传入分。普通 User/0 不消费该目标贡献，也没有把整候选断言为100。传入100的114/100、旧代后槽114、PP0/no-other-match100及多个候选仍114均与固定R一致。原 AE-T02 ID 保留，CV五例另计。 |
| GR8-AI-002 optional | M WP52-A L225；评级行为表 L227–243 | 通过。R 全族20条直接登记、3次copy共5目标，展开25身份；改动仅计数句。附表本有25，全部修正表、copy源、SYMBOISIS/GULPMISSLE/PROPELLORTAIL字面、默认/技能/有效性资格保持。它仍为可选，不据计数说明新增缺失行为或必修根。 |
| GR8-UI-FAINT-AUDIO-001 required | M `user-interface/wp67-a-battle-interaction-and-presentation.md` L258–280，尤其L268–278 | 通过。专用 `_faint` 形态→基础同后缀优先；有专用则默认100/1秒d22。只有普通命中则请求75且长度同用75，1秒夹具d29。双缺d12且独立 `Pkmn faint` 音效仍登记。已命中零长各保100/75请求但d2，不合并双缺。数据框从自身轨道并发；全部轨道结束后的另次聚合观察才完成；d不是总阻塞/墙钟/固定update次数。Off仍演出，HP先写与scene正常返回后正式faint清理、不保证异常回滚均正确。 |
| GR8-UI-BATTLE-END-MARK-001 / CP01 optional | M WP67-A L241；既有正确主体L79–89 | 通过。括注仅改为两条胜利入口先置位再请求胜利BGM，没有把失败/平局或非零decision泛化为置位。新普通scene初始false，decision1先true后BGM，暂停等输入；只换decision2/5则不经success，全显后启动计时，首次正常访问elapsed≥3关闭。BGM异常前已写true的前缀保持。普通按键与abort链分开。 |
| GR8-COM-RECORD-DEBUG-RNG-001 / F05 optional | M `combat-requirements/wp58-battle-recording-and-playback.md` L105；记录主合同L39–85、L91–168 | 通过。仅把“调试场景随机仅呈现”改为辅助选择随机不经记录入口、直接返回与实际AI主路径分开，并导航WP76§7.2。普通设施/回放factory产生Scene；生成器DebugScene但controlPlayer=true使普通主命令先走AI，debug=true的Party走AI。直接helper三菜单分支返Bag1/Call4/Fight0有选择意义；Fight单数move字段在抽样前失败，不补成功随机招式；target空−1、party空nil/至多50次yield独立。仍不经RecordedBattle随机入口。没有建立新的受支持debug API、重开WP76-R12/R6-DX-DEBUG-004/GIR-FD82-B029或改变正常策略/记录流。 |

## 原源证据与最强反方

AI001：本人直接读取固定R `Data/Scripts/011_Battle/006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb` L785–822完整失败/评分处理器；`005_AI/001_Battle_AI.rb` L84–113完整必要registry/wrappers；`005_AI/005_AI_ChooseMove.rb` L23–87、L232–324完整候选与评分定义；`005_AI/010_AIBattler.rb` L292–313完整PP/helper；`010_Data/001_Hardcoded data/017_Target.rb` L1–90含User默认0；PBS/moves.txt L5802–5810完整CONVERSION记录。最强“普通User0不会消费，因此无须补评分”反方只支持保留原接线，不能否定现存直接查询的有限定义。候选已保留此区别。AI002另直接读 `005_AI/008_AI_Utilities.rb` L231–382全部20add/5copy。

FAINT：本人完整读取 CP002 exact-inputs 指定的全部R必要单位，详细逐路径/区间见 ledger。关键为 `004_Scene/008_Battle_Scene_Animations.rb` L610–657完整倒下定义及L202–215完整数据框轨道；`004_Scene/004_Scene_PlayAnimations.rb` L313–326完整共同循环；`010_Data/002_PBS data/009_Species_files.rb` L183–244完整查找/长度；PictureEx的登记/排期/执行/完成必要完整单位；Audio.rb L1–154全文及Audio_Play必要默认/SE完整定义。领域次序由Battler_ChangeSelf L1–151与Battle_Battler L107–112直接复核。最强“不必抄所有固定视觉常量”反方仍成立于其它粒子/颜色/轨迹；它不能生产本入口的75、10+2及专用优先。候选只补有限请求，无扩大视觉policy。

CP01：直接读取Scene_Initialize L1–11、Scene L230–265/L408–419、StartAndEnd L405–512全部完整必要定义，并补读MESSAGE_PAUSE_TIME及普通包装/经验胜利入口。原提案与真实非作者counter全文已读；“同篇主体已正确，局部只是归因精修”的最强反方得到保留，所以仍为optional。

F05：本人直接读完整DebugScene 1–106、CommandPhase 1–265、RecordedBattle 1–287、Challenge_Battles 1–144及完整factory 204–206、RuledBattle 377–438，未执行。原65366B候选全部非源码字段已读；其6份内嵌源码内容已与本人直接阅读的固定R单位逐一校验完全相同，所有单位metadata亦已读。最强普通产品范围反方成立：正常记录/回放与WP76主体本已正确。候选仅做所授权局部归属精修，没有把内部未消费helper升级成必需产品功能。

## 可选选择与共享保留

当前主任务明确要求“11必改…及3采用可选”，并逐名要求核对AI002计数、CP01胜利标记、F05随机归属，故本次审阅将三项作为已采用optional接收。主审提供了该当前用户原句。本子上下文未独立取得作者当时选择动作的原始聊天记录，因此不声称检索验证过历史授权原话。dispositions记载的三项理由分别是计数降低核验歧义、同篇括注纠正先后与胜利限定、单文件短语导航既有WP76；均有明确低风险理解/验证收益，符合本次授权范围。没有选择其它7项optional或独立视觉policy，没有改变required分母。

本人全文读四份受影响候选：WP52-A L1–259、WP58 L1–181、WP67-A L1–368、共享AI目录L1–363。按基线与候选的完整差异区间核验，AI文件仅L215–221/L225与目录T02/独立CV组变化；WP58仅L105变化。WP67-A其它变动属于同批COM同步，已全文接收其保留关系但不在本报告重审该COM原源。

共享只读伴件实际接收：WP52覆盖表L180–216仍含F/G及25计数；WP47-A L21–37真实纹理随机改变合同；WP51 L127–155保ScoreMoves、q/权重及登记；WP76 L158–169主AI/直接helper/异常恢复；RC目录header与全部29行L156–190及全局静态前提。RC-W11仍区分执行与评估随机。WP58五元组、18初始属性、RC29全部ID/计数均保持；上述只读文件的固定基线/候选对象身份全部相同。BT K01–K59完整L360–426已读，K34胜利对照及K35 Off保持。WP15音频L131–190、WP16调度L293–313、WP74范围/共享播放器必要单位及scope/异常保留已读。

## 实际覆盖与未完成范围

五项完整当前合同已读；AGENTS、review-SKILL、候选README/独立入口、history/policy/accepted-facts三个伴件已全文读。原CP01提案+counter、原CP002提案+counter与exact-inputs所有R单位已接收。精确输入、source/formal单位身份、整文件范围和证据读取状态详见 `optional-reading-ledger.json`。

本子检查没有完整读取整批5555行reviewer-prompt、4474行readset及其全部历史根/原38合同；已完整读prompt L1–385，五项全文合同从contracts.zh.json精确record接收，F05 conditional读集已接收。未读其它8份候选整文件；未全文读author-reading-ledger全部157单位条目、input-identity-checks全部132条、commands/publication-commands全部I/O、全dispositions其余9项及全candidate.diff。被截断初始输出不给完整阅读信用；它们是可得未读，不能标为材料limit。此处没有以作者FULL或其它审者信用替代本人阅读。因此本报告只提供这五项的第二语义支持，不能独自满足整批完整独立验收门。主审需要在最终报告中按其本人实际覆盖处理以上余项。

候选、正式规格、公共索引、旧报告、R、main、tags均未由本上下文改动；仅写本报告和独占ledger，未提交。运行观察/真实Demo/媒体/宿主仍0，四个接受门继续分离。
