# R8 CREATURE 子片 C：成长学习、形态、Mega/Primal、Shadow、进化

这是主线程后续排期用的独立语义审查任务；此文件不代表该任务已启动。

先完整读取 Library 合同 libfile_f8ff592304d081918512f51317a8ecee（eighth-global-review-prompt.md，36653 bytes，给定SHA256 63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b）与 /workspace/pokemon-essentials-clean-room/AGENTS.md。
冻结 B8=fd1df570cad987dc3852a3b958f03916e317f7fe；workspace tree751dfde81048c81390f89a65ca1d1a565ba8e1ca；formal treef292698cdd4a8e725525a9be6dc34b75faaf151e。R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b；tree7589c800b61ba13a13040ed0d686979b80a84fd0。

请求gpt-6.1-sol/ultra/default普速/Fast off；实际未回显则逐项UNVERIFIED。独占写目录由root派发时明确；不得写其它task、formal、R，不git commit/push，不自行spawn。

完整身份、继承已读来源和初始消费者在 /workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/creature_review/subshards.json 的 slices.id=C。它不是封闭白名单，定义/默认/备选及真实消费者必须追全。旧PASS、检索、脚本枚举不可代读。

## 唯一primary正式文件（每份全文）

- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/pokemon-rules/wp22-transformation-data.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/pokemon-rules/wp32-context-inputs-and-scenarios.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md

## 唯一primary参考文件（每份全部结构）

- /workspace/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb
- /workspace/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb
- /workspace/pokemon-essentials/Data/Scripts/014_Pokemon/002_Pokemon_MegaEvolution.rb
- /workspace/pokemon-essentials/Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb

## 必须核对的定义、配置、数据与真实消费者依赖（接收前仍未决）

- /workspace/pokemon-essentials/Data/Scripts/001_Settings.rb
- /workspace/pokemon-essentials/Data/Scripts/002_BattleSettings.rb
- /workspace/pokemon-essentials/Data/Scripts/002_Save data/004_Game_SaveValues.rb
- /workspace/pokemon-essentials/Data/Scripts/002_Save data/005_Game_SaveConversions.rb
- /workspace/pokemon-essentials/Data/Scripts/003_Game processing/005_Event_Handlers.rb
- /workspace/pokemon-essentials/Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb
- /workspace/pokemon-essentials/Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb
- /workspace/pokemon-essentials/Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb
- /workspace/pokemon-essentials/Data/Scripts/010_Data/002_PBS data/011_ShadowPokemon.rb
- /workspace/pokemon-essentials/Data/Scripts/010_Data/002_PBS data/012_Ribbon.rb
- /workspace/pokemon-essentials/Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb
- /workspace/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb
- /workspace/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb
- /workspace/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon.rb
- /workspace/pokemon-essentials/Data/Scripts/014_Pokemon/004_Pokemon_Move.rb
- /workspace/pokemon-essentials/Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb
- /workspace/pokemon-essentials/Data/Scripts/015_Trainers and player/001_Trainer.rb
- /workspace/pokemon-essentials/Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb
- /workspace/pokemon-essentials/Data/Scripts/015_Trainers and player/003_Trainer_Sprites.rb
- /workspace/pokemon-essentials/Data/Scripts/015_Trainers and player/004_Player.rb
- /workspace/pokemon-essentials/Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb
- /workspace/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb
- /workspace/pokemon-essentials/Data/Scripts/016_UI/022_UI_MoveRelearner.rb
- /workspace/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb
- /workspace/pokemon-essentials/Data/Scripts/019_Utilities/001_Utilities.rb
- /workspace/pokemon-essentials/Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb
- /workspace/pokemon-essentials/Data/Scripts/021_Compiler/001_Compiler.rb
- /workspace/pokemon-essentials/Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb
- /workspace/pokemon-essentials/Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb
- /workspace/pokemon-essentials/PBS/Gen 5 backup/abilities.txt
- /workspace/pokemon-essentials/PBS/Gen 5 backup/moves.txt
- /workspace/pokemon-essentials/PBS/Gen 5 backup/pokemon.txt
- /workspace/pokemon-essentials/PBS/Gen 5 backup/pokemon_forms.txt
- /workspace/pokemon-essentials/PBS/Gen 5 backup/types.txt
- /workspace/pokemon-essentials/PBS/Gen 6 backup/abilities.txt
- /workspace/pokemon-essentials/PBS/Gen 6 backup/moves.txt
- /workspace/pokemon-essentials/PBS/Gen 6 backup/pokemon.txt
- /workspace/pokemon-essentials/PBS/Gen 6 backup/pokemon_forms.txt
- /workspace/pokemon-essentials/PBS/Gen 6 backup/types.txt
- /workspace/pokemon-essentials/PBS/Gen 7 backup/abilities.txt
- /workspace/pokemon-essentials/PBS/Gen 7 backup/moves.txt
- /workspace/pokemon-essentials/PBS/Gen 7 backup/pokemon.txt
- /workspace/pokemon-essentials/PBS/Gen 7 backup/pokemon_forms.txt
- /workspace/pokemon-essentials/PBS/Gen 7 backup/types.txt
- /workspace/pokemon-essentials/PBS/Gen 8 backup/abilities.txt
- /workspace/pokemon-essentials/PBS/Gen 8 backup/moves.txt
- /workspace/pokemon-essentials/PBS/Gen 8 backup/pokemon.txt
- /workspace/pokemon-essentials/PBS/Gen 8 backup/pokemon_forms.txt
- /workspace/pokemon-essentials/PBS/Gen 8 backup/types.txt
- /workspace/pokemon-essentials/PBS/Shadow Pokémon backup/items_shadow_pkmn.txt
- /workspace/pokemon-essentials/PBS/Shadow Pokémon backup/moves_shadow_pkmn.txt
- /workspace/pokemon-essentials/PBS/Shadow Pokémon backup/shadow_pokemon.txt
- /workspace/pokemon-essentials/PBS/Shadow Pokémon backup/types_shadow_pkmn.txt
- /workspace/pokemon-essentials/PBS/abilities.txt
- /workspace/pokemon-essentials/PBS/moves.txt
- /workspace/pokemon-essentials/PBS/pokemon.txt
- /workspace/pokemon-essentials/PBS/pokemon_forms.txt
- /workspace/pokemon-essentials/PBS/ribbons.txt
- /workspace/pokemon-essentials/PBS/types.txt

## 共享测试目录全文（跨WP亦整篇读）

- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md

逐结构维护连续reading ledger，复合clause拆全部子断言；两向矩阵file→unit→fact→consumer→spec与clause→source→premise。跟踪正常/取消/异常/部分提交及下游保存、重载。所有未执行向量写NOT_EXECUTED；真实执行逐次绑定已理解命令、固定输入、隔离输出、stdout/stderr、exit、UTC。

疑点使用GR8-CRE-C-NNN稳定暂存ID（root将决定canonical，不自行去重关闭）；每项给source/spec精确行、身份、前提、普通与最小反例、失败边界、负证据、消费者、影响、最小正确修订、保留scope、同步、回归及独立反证待决。没有反例不等于全文已接受。progress.json持续同步；最终明确所有剩余可读未读与跨域待接收，UPDATE_NOT_STARTED。
