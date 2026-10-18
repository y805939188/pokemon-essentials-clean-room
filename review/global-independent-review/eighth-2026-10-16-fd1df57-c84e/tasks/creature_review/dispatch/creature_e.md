# R8 CREATURE 子片 E：工厂租借交换、邮件礼物、Triple Triad

这是主线程后续排期用的独立语义审查任务；此文件不代表该任务已启动。

先完整读取 Library 合同 libfile_f8ff592304d081918512f51317a8ecee（eighth-global-review-prompt.md，36653 bytes，给定SHA256 63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b）与 /workspace/pokemon-essentials-clean-room/AGENTS.md。
冻结 B8=fd1df570cad987dc3852a3b958f03916e317f7fe；workspace tree751dfde81048c81390f89a65ca1d1a565ba8e1ca；formal treef292698cdd4a8e725525a9be6dc34b75faaf151e。R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b；tree7589c800b61ba13a13040ed0d686979b80a84fd0。

请求gpt-6.1-sol/ultra/default普速/Fast off；实际未回显则逐项UNVERIFIED。独占写目录由root派发时明确；不得写其它task、formal、R，不git commit/push，不自行spawn。

完整身份、继承已读来源和初始消费者在 /workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/creature_review/subshards.json 的 slices.id=E。它不是封闭白名单，定义/默认/备选及真实消费者必须追全。旧PASS、检索、脚本枚举不可代读。

## 唯一primary正式文件（每份全文）

- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/creature-rpg/wp57-factory-rentals-and-swaps.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/creature-rpg/wp68-triple-triad.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md

## 唯一primary参考文件（每份全部结构）

- /workspace/pokemon-essentials/Data/Scripts/013_Items/006_Item_Mail.rb

## 必须核对的定义、配置、数据与真实消费者依赖（接收前仍未决）

- /workspace/pokemon-essentials/Data/Scripts/001_Settings.rb
- /workspace/pokemon-essentials/Data/Scripts/002_BattleSettings.rb
- /workspace/pokemon-essentials/Data/Scripts/002_Save data/004_Game_SaveValues.rb
- /workspace/pokemon-essentials/Data/Scripts/002_Save data/005_Game_SaveConversions.rb
- /workspace/pokemon-essentials/Data/Scripts/003_Game processing/005_Event_Handlers.rb
- /workspace/pokemon-essentials/Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb
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
- /workspace/pokemon-essentials/Data/Scripts/016_UI/024_UI_MysteryGift.rb
- /workspace/pokemon-essentials/Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb
- /workspace/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb
- /workspace/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb
- /workspace/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/003_Challenge_ChooseFoes.rb
- /workspace/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb
- /workspace/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/005_UI_BattleSwap.rb
- /workspace/pokemon-essentials/Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb
- /workspace/pokemon-essentials/Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/002_ChallengeGenerator_Pokemon.rb
- /workspace/pokemon-essentials/Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb
- /workspace/pokemon-essentials/Data/Scripts/021_Compiler/001_Compiler.rb
- /workspace/pokemon-essentials/Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb
- /workspace/pokemon-essentials/Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb
- /workspace/pokemon-essentials/PBS/battle_facility_lists.txt
- /workspace/pokemon-essentials/PBS/battle_tower_pokemon.txt
- /workspace/pokemon-essentials/PBS/battle_tower_trainers.txt
- /workspace/pokemon-essentials/PBS/cup_fancy_pkmn.txt
- /workspace/pokemon-essentials/PBS/cup_fancy_pkmn_single.txt
- /workspace/pokemon-essentials/PBS/cup_fancy_trainers.txt
- /workspace/pokemon-essentials/PBS/cup_fancy_trainers_single.txt
- /workspace/pokemon-essentials/PBS/cup_little_pkmn.txt
- /workspace/pokemon-essentials/PBS/cup_little_trainers.txt
- /workspace/pokemon-essentials/PBS/cup_pika_pkmn.txt
- /workspace/pokemon-essentials/PBS/cup_pika_trainers.txt
- /workspace/pokemon-essentials/PBS/cup_poke_pkmn.txt
- /workspace/pokemon-essentials/PBS/cup_poke_trainers.txt

## 共享测试目录全文（跨WP亦整篇读）

- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md
- /workspace/pokemon-essentials-clean-room/deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md

逐结构维护连续reading ledger，复合clause拆全部子断言；两向矩阵file→unit→fact→consumer→spec与clause→source→premise。跟踪正常/取消/异常/部分提交及下游保存、重载。所有未执行向量写NOT_EXECUTED；真实执行逐次绑定已理解命令、固定输入、隔离输出、stdout/stderr、exit、UTC。

疑点使用GR8-CRE-E-NNN稳定暂存ID（root将决定canonical，不自行去重关闭）；每项给source/spec精确行、身份、前提、普通与最小反例、失败边界、负证据、消费者、影响、最小正确修订、保留scope、同步、回归及独立反证待决。没有反例不等于全文已接受。progress.json持续同步；最终明确所有剩余可读未读与跨域待接收，UPDATE_NOT_STARTED。
