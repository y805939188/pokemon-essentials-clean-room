# WP72 战斗效果可编辑集合行为化目录（120 项；WP72-R11 附件）

2026-10-02；WP72 首审修订 v2 附件（revision-v2）。本目录是**行为化数据表**：逐项给出调试战斗效果编辑器的可编辑项、行为含义（参考侧注释的直译）、值类型、默认值与范围/哨兵。**不复制源表结构/表达式**；效果名为审计标识。类型语义见主稿 §7.5（布尔／整数／成员下标／招式／道具五种输入行为）。源码位置 `020_Debug/003_Debug menus/006_Debug_BattleExtraCode.rb`（注释标注的不可编辑项不在此目录——主稿已登记白名单外不可编辑）。

机械统计：成员 83＋阵营 22＋全场 13＋席位 2＝120 项（与主稿 §7.5 一致）。

## 1. 成员效果（83 项）

| 审计标识 | 行为含义 | 类型 | 默认 | 范围/哨兵 |
| --- | --- | --- | --- | --- |
| AquaRing | Aqua Ring applies | boolean | false（未生效） | — |
| Attract | Battler that self is attracted to | battler-index | -1（无目标/None） | -1(None)或存在的成员下标 |
| BanefulBunker | Baneful Bunker applies this round | boolean | false（未生效） | — |
| Bide | Bide number of rounds remaining | integer | 0 | 0–99 |
| BideDamage | Bide damage accumulated | integer | 0 | 0–999 |
| BideTarget | Bide last battler to hurt self | battler-index | -1（无目标/None） | -1(None)或存在的成员下标 |
| BurnUp | Burn Up has removed self's Fire type | boolean | false（未生效） | — |
| Charge | Charge number of rounds remaining | integer | 0 | 0–99 |
| ChoiceBand | Move locked into by Choice items | move | nil（None） | nil(None)或对应数据 ID |
| Confusion | Confusion number of rounds remaining | integer | 0 | 0–99 |
| Curse | Curse damaging applies | boolean | false（未生效） | — |
| DefenseCurl | Used Defense Curl | boolean | false（未生效） | — |
| Disable | Disable number of rounds remaining | integer | 0 | 0–99 |
| DisableMove | Disabled move | move | nil（None） | nil(None)或对应数据 ID |
| Electrify | Electrify making moves Electric | boolean | false（未生效） | — |
| Embargo | Embargo number of rounds remaining | integer | 0 | 0–99 |
| Encore | Encore number of rounds remaining | integer | 0 | 0–99 |
| EncoreMove | Encored move | move | nil（None） | nil(None)或对应数据 ID |
| Endure | Endures all lethal damage this round | boolean | false（未生效） | — |
| FlashFire | Flash Fire powering up Fire moves | boolean | false（未生效） | — |
| Flinch | Will flinch this round | boolean | false（未生效） | — |
| FocusEnergy | Focus Energy critical hit stages (0-4) | integer | 0 | 0–4 |
| FollowMe | Follow Me drawing in attacks (if 1+) | integer | 0 | 0–99 |
| RagePowder | Rage Powder applies (use with Follow Me) | boolean | false（未生效） | — |
| Foresight | Foresight applies (Ghost loses immunities) | boolean | false（未生效） | — |
| FuryCutter | Fury Cutter power multiplier 2**x (0-4) | integer | 0 | 0–4 |
| GastroAcid | Gastro Acid is negating self's ability | boolean | false（未生效） | — |
| Grudge | Grudge will apply if self faints | boolean | false（未生效） | — |
| HealBlock | Heal Block number of rounds remaining | integer | 0 | 0–99 |
| HelpingHand | Helping Hand will power up self's move | boolean | false（未生效） | — |
| HyperBeam | Hyper Beam recharge rounds remaining | integer | 0 | 0–99 |
| Imprison | Imprison disables others' moves known by self | boolean | false（未生效） | — |
| Ingrain | Ingrain applies | boolean | false（未生效） | — |
| JawLock | Battler trapping self with Jaw Lock | battler-index | -1（无目标/None） | -1(None)或存在的成员下标 |
| KingsShield | King's Shield applies this round | boolean | false（未生效） | — |
| LaserFocus | Laser Focus certain critial hit duration | integer | 0 | 0–99 |
| LeechSeed | Battler that used Leech Seed on self | battler-index | -1（无目标/None） | -1(None)或存在的成员下标 |
| LockOn | Lock-On number of rounds remaining | integer | 0 | 0–99 |
| LockOnPos | Battler that self is targeting with Lock-On | battler-index | -1（无目标/None） | -1(None)或存在的成员下标 |
| MagnetRise | Magnet Rise number of rounds remaining | integer | 0 | 0–99 |
| MeanLook | Battler trapping self with Mean Look, etc. | battler-index | -1（无目标/None） | -1(None)或存在的成员下标 |
| Metronome | Metronome item power multiplier 1 + 0.2*x (0-5) | integer | 0 | 0–5 |
| MicleBerry | Micle Berry boosting next move's accuracy | boolean | false（未生效） | — |
| Minimize | Used Minimize | boolean | false（未生效） | — |
| MiracleEye | Miracle Eye applies (Dark loses immunities) | boolean | false（未生效） | — |
| MudSport | Used Mud Sport (Gen 5 and older) | boolean | false（未生效） | — |
| Nightmare | Taking Nightmare damage | boolean | false（未生效） | — |
| NoRetreat | No Retreat trapping self in battle | boolean | false（未生效） | — |
| Obstruct | Obstruct applies this round | boolean | false（未生效） | — |
| Octolock | Battler trapping self with Octolock | battler-index | -1（无目标/None） | -1(None)或存在的成员下标 |
| Outrage | Outrage number of rounds remaining | integer | 0 | 0–99 |
| PerishSong | Perish Song number of rounds remaining | integer | 0 | 0–99 |
| PerishSongUser | Battler that used Perish Song on self | battler-index | -1（无目标/None） | -1(None)或存在的成员下标 |
| PickupItem | Item retrievable by Pickup | item | nil（None） | nil(None)或对应数据 ID |
| PickupUse | Pickup item consumed time (higher=more recent) | integer | 0 | 0–99 |
| Pinch | (Battle Palace) Behavior changed at <50% HP | boolean | false（未生效） | — |
| Powder | Powder will explode self's Fire move this round | boolean | false（未生效） | — |
| Protect | Protect applies this round | boolean | false（未生效） | — |
| ProtectRate | Protect success chance 1/x | integer | 1 | 1–999 |
| Rollout | Rollout rounds remaining (lower=stronger) | integer | 0 | 0–99 |
| Roost | Roost removing Flying type this round | boolean | false（未生效） | — |
| SlowStart | Slow Start rounds remaining | integer | 0 | 0–99 |
| SmackDown | Smack Down is grounding self | boolean | false（未生效） | — |
| SpikyShield | Spiky Shield applies this round | boolean | false（未生效） | — |
| Spotlight | Spotlight drawing in attacks (if 1+) | integer | 0 | 0–99 |
| Stockpile | Stockpile count (0-3) | integer | 0 | 0–3 |
| StockpileDef | Def stages gained by Stockpile (0-12) | integer | 0 | 0–12 |
| StockpileSpDef | Sp. Def stages gained by Stockpile (0-12) | integer | 0 | 0–12 |
| Substitute | Substitute's HP | integer | 0 | 0–999 |
| TarShot | Tar Shot weakening self to Fire | boolean | false（未生效） | — |
| Taunt | Taunt number of rounds remaining | integer | 0 | 0–99 |
| Telekinesis | Telekinesis number of rounds remaining | integer | 0 | 0–99 |
| ThroatChop | Throat Chop number of rounds remaining | integer | 0 | 0–99 |
| Torment | Torment preventing repeating moves | boolean | false（未生效） | — |
| Trapping | Trapping number of rounds remaining | integer | 0 | 0–99 |
| TrappingMove | Move that is trapping self | move | nil（None） | nil(None)或对应数据 ID |
| TrappingUser | Battler trapping self (for Binding Band) | battler-index | -1（无目标/None） | -1(None)或存在的成员下标 |
| Truant | Truant will loaf around this round | boolean | false（未生效） | — |
| Unburden | Self lost its item (for Unburden) | boolean | false（未生效） | — |
| Uproar | Uproar number of rounds remaining | integer | 0 | 0–99 |
| WaterSport | Used Water Sport (Gen 5 and older) | boolean | false（未生效） | — |
| WeightChange | Weight change +0.1*x kg | integer | 0 | −99,999–99,999 |
| Yawn | Yawn rounds remaining until falling asleep | integer | 0 | 0–99 |

## 2. 阵营效果（22 项）

| 审计标识 | 行为含义 | 类型 | 默认 | 范围/哨兵 |
| --- | --- | --- | --- | --- |
| AuroraVeil | Aurora Veil duration | integer | 0 | 0–99 |
| CraftyShield | Crafty Shield applies this round | boolean | false（未生效） | — |
| EchoedVoiceCounter | Echoed Voice rounds used (max. 5) | integer | 0 | 0–5 |
| EchoedVoiceUsed | Echoed Voice used this round | boolean | false（未生效） | — |
| LastRoundFainted | Round when side's battler last fainted | integer | -2（哨兵——编辑复位按 −1） | -1–99 |
| LightScreen | Light Screen duration | integer | 0 | 0–99 |
| LuckyChant | Lucky Chant duration | integer | 0 | 0–99 |
| MatBlock | Mat Block applies this round | boolean | false（未生效） | — |
| Mist | Mist duration | integer | 0 | 0–99 |
| QuickGuard | Quick Guard applies this round | boolean | false（未生效） | — |
| Rainbow | Rainbow duration | integer | 0 | 0–99 |
| Reflect | Reflect duration | integer | 0 | 0–99 |
| Round | Round was used this round | boolean | false（未生效） | — |
| Safeguard | Safeguard duration | integer | 0 | 0–99 |
| SeaOfFire | Sea Of Fire duration | integer | 0 | 0–99 |
| Spikes | Spikes layers (0-3) | integer | 0 | 0–3 |
| StealthRock | Stealth Rock exists | boolean | false（未生效） | — |
| StickyWeb | Sticky Web exists | boolean | false（未生效） | — |
| Swamp | Swamp duration | integer | 0 | 0–99 |
| Tailwind | Tailwind duration | integer | 0 | 0–99 |
| ToxicSpikes | Toxic Spikes layers (0-2) | integer | 0 | 0–2 |
| WideGuard | Wide Guard applies this round | boolean | false（未生效） | — |

## 3. 全场效果（13 项）

| 审计标识 | 行为含义 | 类型 | 默认 | 范围/哨兵 |
| --- | --- | --- | --- | --- |
| AmuletCoin | Amulet Coin doubling prize money | boolean | false（未生效） | — |
| FairyLock | Fairy Lock trapping duration | integer | 0 | 0–99 |
| FusionBolt | Fusion Bolt was used | boolean | false（未生效） | — |
| FusionFlare | Fusion Flare was used | boolean | false（未生效） | — |
| Gravity | Gravity duration | integer | 0 | 0–99 |
| HappyHour | Happy Hour doubling prize money | boolean | false（未生效） | — |
| IonDeluge | Ion Deluge making moves Electric | boolean | false（未生效） | — |
| MagicRoom | Magic Room duration | integer | 0 | 0–99 |
| MudSportField | Mud Sport duration (Gen 6+) | integer | 0 | 0–99 |
| PayDay | Pay Day additional prize money | integer | 0 | 0–Settings::MAX_MONEY |
| TrickRoom | Trick Room duration | integer | 0 | 0–99 |
| WaterSportField | Water Sport duration (Gen 6+) | integer | 0 | 0–99 |
| WonderRoom | Wonder Room duration | integer | 0 | 0–99 |

## 4. 席位效果（2 项）

| 审计标识 | 行为含义 | 类型 | 默认 | 范围/哨兵 |
| --- | --- | --- | --- | --- |
| HealingWish | Whether Healing Wish is waiting to apply | boolean | false（未生效） | — |
| LunarDance | Whether Lunar Dance is waiting to apply | boolean | false（未生效） | — |
