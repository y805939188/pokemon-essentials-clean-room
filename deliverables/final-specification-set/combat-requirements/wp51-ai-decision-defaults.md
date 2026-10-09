# WP51 决策默认数据与有界目录附表（净化正文；批次 12）

分类：combat-requirements 数据附表；性质：实现独立行为数据。

本附表为净化正文的一部分：按统一交接将批准输入 WP51《决策默认数据与有界目录》转写为独立行为数据，不含源文件路径与行号（源定位集中登记于 `../../audit/source-traceability.md` 批次 12 条目）。数据影响 AI 偏好，不替代真实道具 WP28 或持物 WP50 效果。源身份仅审计，不提出未来结构。全部内容为静态证据；**无运行确认**（见 `../scope-statement.md`）。

## 1. HP 道具估量

「真/假」为 REBALANCED_HEALING_ITEM_AMOUNTS；当前真。只有已通过真实道具资格才入偏好候选。999 是估计表常量，不是实际 HP 上限。完整列表的资格扫描、未提供所选招式索引及整阶段异常边界见主稿 §4；未列入本表的合法物品也先查资格。

| 物品 | 真 | 假 |
| --- | ---: | ---: |
| POTION | 20 | 20 |
| SUPERPOTION | 60 | 50 |
| HYPERPOTION | 120 | 200 |
| MAXPOTION | 999 | 999 |
| BERRYJUICE | 20 | 20 |
| SWEETHEART | 20 | 20 |
| FRESHWATER | 30 | 50 |
| SODAPOP | 50 | 60 |
| LEMONADE | 70 | 80 |
| MOOMOOMILK | 100 | 100 |
| ORANBERRY | 10 | 10 |
| SITRUSBERRY | 1 | 1 |
| ENERGYPOWDER | 60 | 50 |
| ENERGYROOT | 120 | 200 |

RAGECANDYBAR 只有 RAGE_CANDY_BAR_CURES_STATUS_PROBLEMS 假时加入 HP 表 20，真时进全异常表。SITRUSBERRY 表值 1；后续分支比较 SITURUSBERRY 的拼写未命中它，所以不按理想四分之一补写。实际主动请求量由 [WP28 §5.1](../creature-rpg/wp28-item-use-and-training.md) 的完整回复量表给出：总 HP101/105、当前 HP1 时 SITRUSBERRY 请求25/26，实际 HP26/27；AI 估量仍1，持有触发另由 WP50 负责。

## 2. 治疗/复活类别

| 类别 | 默认有序身份 |
| --- | --- |
| FULL_RESTORE_ITEMS | FULLRESTORE |
| ONE_STATUS_CURE_ITEMS | AWAKENING, CHESTOBERRY, BLUEFLUTE, ANTIDOTE, PECHABERRY, BURNHEAL, RAWSTBERRY, PARALYZEHEAL, PARLYZHEAL, CHERIBERRY, ICEHEAL, ASPEARBERRY |
| ALL_STATUS_CURE_ITEMS | FULLHEAL, LAVACOOKIE, OLDGATEAU, CASTELIACONE, LUMIOSEGALETTE, SHALOURSABLE, BIGMALASADA, PEWTERCRUNCHIES, LUMBERRY, HEALPOWDER |
| ALL_STATS_RAISE_ITEMS | MAXMUSHROOMS |
| 复活优先值 5 | REVIVE |
| 复活优先值 7 | MAXREVIVE, REVIVALHERB, MAXHONEY |

单异常与全异常的真实效果仍由 CanUseInBattle 门区别，不能仅按这个表治疗任意异常。全阶组取错 stat_raise 的快照分支见主稿 §4，不改原数据。

## 3. X 道具完整身份与请求量

| 物品 | 阶级 | 请求量 |
| --- | --- | --- |
| XATTACK | ATTACK | 设置真 2／假 1 |
| XATTACK2 | ATTACK | 2 |
| XATTACK3 | ATTACK | 3 |
| XATTACK6 | ATTACK | 6 |
| XDEFENSE | DEFENSE | 设置真 2／假 1 |
| XDEFENSE2 | DEFENSE | 2 |
| XDEFENSE3 | DEFENSE | 3 |
| XDEFENSE6 | DEFENSE | 6 |
| XDEFEND | DEFENSE | 设置真 2／假 1 |
| XDEFEND2 | DEFENSE | 2 |
| XDEFEND3 | DEFENSE | 3 |
| XDEFEND6 | DEFENSE | 6 |
| XSPATK | SPECIAL_ATTACK | 设置真 2／假 1 |
| XSPATK2 | SPECIAL_ATTACK | 2 |
| XSPATK3 | SPECIAL_ATTACK | 3 |
| XSPATK6 | SPECIAL_ATTACK | 6 |
| XSPECIAL | SPECIAL_ATTACK | 设置真 2／假 1 |
| XSPECIAL2 | SPECIAL_ATTACK | 2 |
| XSPECIAL3 | SPECIAL_ATTACK | 3 |
| XSPECIAL6 | SPECIAL_ATTACK | 6 |
| XSPDEF | SPECIAL_DEFENSE | 设置真 2／假 1 |
| XSPDEF2 | SPECIAL_DEFENSE | 2 |
| XSPDEF3 | SPECIAL_DEFENSE | 3 |
| XSPDEF6 | SPECIAL_DEFENSE | 6 |
| XSPEED | SPEED | 设置真 2／假 1 |
| XSPEED2 | SPEED | 2 |
| XSPEED3 | SPEED | 3 |
| XSPEED6 | SPEED | 6 |
| XACCURACY | ACCURACY | 设置真 2／假 1 |
| XACCURACY2 | ACCURACY | 2 |
| XACCURACY3 | ACCURACY | 3 |
| XACCURACY6 | ACCURACY | 6 |

当前 X_STAT_ITEMS_RAISE_BY_TWO_STAGES 真。AI 按对应当前阶级和请求量排序；真实中央反向/单纯/封顶由 WP44/28，预计可用不代替提交。

## 4. 普通换人处理器目录

每项完整条件和概率在主稿 §3.1，按下表登记序先愿换，再中等以上否决（源文件与起行见追溯条目）。

ShouldSwitch（11 项，登记序）：perish_song、significant_eor_damage、cure_status_problem_by_switching_out、wish_healing、yawning、asleep、battler_is_useless、foe_absorbs_all_moves_with_its_ability、absorb_foe_move、sudden_death、high_damage_from_foe。

ShouldNotSwitch（4 项，登记序）：lethal_entry_hazards、battler_has_super_effective_move、battler_has_very_raised_stats、battler_is_immune_via_wonder_guard。

## 5. 责任与未决

本包负责基础 AI 决策顺序、技能/标记、普通换人目录与后备评分、主动道具分类、Mega 与候选权重抽取。通用目标评分、状态/阶级数值与基础预测由 WP52-A；具体场域/伤害/恢复/多目标效果 WP52-B，物品/调用/控制评分 WP52-C。技能 0 不等同无任何偏好（野生稳定槽重复仍在），特殊模式入口不代表本包完成设施策略。全局 AI 覆盖与运行/插件组合保留。
