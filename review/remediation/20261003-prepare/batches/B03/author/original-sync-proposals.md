# B03 原规格最小同步建议（未实施）

正式写白名单只有七条最终正文/矩阵/目录路径。下表是给父统筹的逐条裁定输入，不是额外写入授权；原规格与历史记录均保持冻结原字节。当前工具没有跨 source_thread_id 直接发送消息的能力（仅本代理在任务树中），故已在进行中消息给出具体相对路径/行/ID/证据，并把完整建议交给父任务。没有等待常规确认或停止七路径修订。

所有行的项目身份为 B02 接受基线 `9576f00e7d3aeb96f7ca8c42caccfba8f808505e`；参考身份为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。以下参考路径共同前缀为 `Data/Scripts/`；准确 blob/SHA256 在 source-reading-log.json 中。路径及行号为当前冻结原规格的真实位置，不复用原报告被修正过的旧定位。

| 原规格相对路径/条款（冻结行） | finding ID | 证据（参考相对路径/行） | 建议最小范围与状态 |
| --- | --- | --- | --- |
| `specs/overworld/wp11-map-topology-transfer.md` §3.2/4，54–80；§5.1，93 | C037/C052；002/C094/C003 | `004_Game classes/005_Game_MapFactory.rb` 95–178；`003_Game processing/002_Scene_Map.rb` 72–101/119–130/170–179；`012_Overworld/001_Overworld.rb` 297–314；`012_Overworld/001_Overworld visuals/002_Overworld_Overlays.rb` 4–45 | 同图前置处理、201消费者false与直接默认true分开；增加跨界目标方向0边界。原第70行天气20**已有正确值，保留**，只补边缘进入后写/非20秒限定；地点门及生命周期作为本批新增承接建议。父统筹待裁定。 |
| `specs/overworld/wp12-terrain-movement-vehicles.md` §3.2，70–98；§4.1，114–129；§4.2/5，148–192 | C036/C037/C049/C050/C054/C095；C003 | `004_Game classes/004_Game_Map.rb` 143–246；`006_Game_Character.rb` 237–298/405–424/553–744（同一目录）；`008_Game_Player.rb` 431–458/587–599；`012_Overworld/001_Overworld.rb` 494–503；`012_Overworld/004_Overworld_FieldMoves.rb` 891–969 | 改正“始终读移动者当前水域/只拒目标冰”与201默认取消游泳，补前帧移动输入、固定对角/多格/NPC和冰前阻挡退出；补攀瀑实际置位门，不替B14完整三入口。原第166行C035骑行谓词**已正确，不需倒置或降级**。父统筹待裁定。 |
| `specs/overworld/wp13-interpreter-command-matrix.md` §2/101/102/106/111/411/201/205/206/223/231–235/251，12–85 | C037/C039/C040/C041/C042/C053/C067；002 | `003_Game processing/003_Interpreter.rb` 218–267；`004_Interpreter_Commands.rb`（同目录）162–320/383–453/723–750/814–828/933–979/1059–1062；`004_Game classes/003_Game_Picture.rb` 54–161 | 先预读故障、nil两支跳过、1/20秒、无名停止、同层选项合并/取消/隐藏原身份；201排队消费；效果时钟与零时长旧任务。原314/28分类正确，保留。显示主文/窗口不在本批越权同步。父统筹待裁定。 |
| `specs/overworld/wp13-map-events-npc-followers.md` §4/5，79–107；§6，109–151 | C039/C040/C041/C049/C051/C053；WP80-INTAKE-R01 | `004_Game classes/007_Game_Event.rb` 12–21/159–180；`011_Game_FollowerFactory.rb`（同目录）193–273；`012_Overworld/001_Overworld.rb` 536–553；`021_Compiler/004_Compiler_MapsAndEvents.rb` 847–887 | 主正文引用矩阵精确边界及NPC独立合同、补门跟随族/消费者，保留原正确ASCII字面和s:。不将“无Demo”变成没有消费者，不修改历史复审段落。父统筹待裁定。 |
| `specs/overworld/wp13-move-route-matrix.md` §1/15/45/口径，18/39/69/73 | C041/C049；C007 | `004_Game classes/006_Game_Character.rb` 260–298/475–550/660–744 | 1/20秒及路线0等待的帧边界；保留原三字面，只补准确行首前缀、先求值/正常返回、长后缀/非匹配对照；改成引用独立角色条款。父统筹待裁定。 |
| `specs/overworld/wp14-random-dungeons.md` §3.5/4/5/6及例表，96–152/208–212 | C043–C048；C003/WP80-INTAKE-R01 | `012_Overworld/008_Overworld_RandomDungeons.rb` 131–218/353–475/747–1004/1011–1105；`010_Data/002_PBS data/019_DungeonTileset.rb` 59–196；`020_DungeonParameters.rb`（同目录）12–114；`006_Map renderer/004_TileDrawingHelper.rb` 21–73 | 缓冲先X后读改后X、≥20直输尺寸、房间floor/cap、有向抽样、空起点先失败、小图/零房间候选空与旧候选保留、间距max、四零密度失败点；独立图样/邻接/编号合同。保留B01 GR-006三奇数参数构造首次写回失败和所有历史确认，不能补参考writer。父统筹待裁定。 |

此处 Cxxx/002 的全名为 `GIR-FD82-Cxxx`/`GIR-FD82-002`。详细限定、完整原对象/有效二审/扩展和逐向量映射分别见 effective-finding-inputs.json、finding-responses.json、traceability.tsv。公共登记仅提供 registry-proposals.json，由唯一 A-REG 串行处理。原规格同步是否构成额外范围及下游验收依赖，仍须父统筹处理；本作者不自行扩大白名单。
