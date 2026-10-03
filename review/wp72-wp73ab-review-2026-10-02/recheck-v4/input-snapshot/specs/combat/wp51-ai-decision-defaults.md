# WP51 决策默认数据与有界目录 v2（限定管理回填）

状态：**Reviewed（限定静态范围，2026-09-28首审PASS_SCOPED；管理性回填）**。范围为[WP51主稿](wp51-ai-action-selection-and-skill.md)A～E对应的决策默认数据与有界目录；数据表内容不变。数据影响AI偏好，不替代真实道具WP28或持物WP50效果。源身份仅审计，不提出未来结构。

## 1. HP道具估量

“真／假”为REBALANCED_HEALING_ITEM_AMOUNTS；当前真。只有已通过真实道具资格才入偏好候选。999是估计表常量，不是实际HP上限。

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

RAGECANDYBAR只有RAGE_CANDY_BAR_CURES_STATUS_PROBLEMS假时加入HP表20，真时进全异常表。SITRUSBERRY表值1；后续分支比较SITURUSBERRY的拼写未命中它，所以不按理想四分之一补写。

## 2. 治療／复活类别

| 类别 | 默认有序身份 |
| --- | --- |
| FULL_RESTORE_ITEMS | FULLRESTORE |
| ONE_STATUS_CURE_ITEMS | AWAKENING, CHESTOBERRY, BLUEFLUTE, ANTIDOTE, PECHABERRY, BURNHEAL, RAWSTBERRY, PARALYZEHEAL, PARLYZHEAL, CHERIBERRY, ICEHEAL, ASPEARBERRY |
| ALL_STATUS_CURE_ITEMS | FULLHEAL, LAVACOOKIE, OLDGATEAU, CASTELIACONE, LUMIOSEGALETTE, SHALOURSABLE, BIGMALASADA, PEWTERCRUNCHIES, LUMBERRY, HEALPOWDER |
| ALL_STATS_RAISE_ITEMS | MAXMUSHROOMS |
| 复活优先值5 | REVIVE |
| 复活优先值7 | MAXREVIVE, REVIVALHERB, MAXHONEY |

单异常与全异常的真实效果仍由CanUseInBattle门区别，不能仅按这个表治疗任意异常。全阶组取错stat_raise的快照分支见主稿§4，不改原数据。

## 3. X道具完整身份与请求量

| 物品 | 阶级 | 请求量 |
| --- | --- | --- |
| XATTACK | ATTACK | 设置真2／假1 |
| XATTACK2 | ATTACK | 2 |
| XATTACK3 | ATTACK | 3 |
| XATTACK6 | ATTACK | 6 |
| XDEFENSE | DEFENSE | 设置真2／假1 |
| XDEFENSE2 | DEFENSE | 2 |
| XDEFENSE3 | DEFENSE | 3 |
| XDEFENSE6 | DEFENSE | 6 |
| XDEFEND | DEFENSE | 设置真2／假1 |
| XDEFEND2 | DEFENSE | 2 |
| XDEFEND3 | DEFENSE | 3 |
| XDEFEND6 | DEFENSE | 6 |
| XSPATK | SPECIAL_ATTACK | 设置真2／假1 |
| XSPATK2 | SPECIAL_ATTACK | 2 |
| XSPATK3 | SPECIAL_ATTACK | 3 |
| XSPATK6 | SPECIAL_ATTACK | 6 |
| XSPECIAL | SPECIAL_ATTACK | 设置真2／假1 |
| XSPECIAL2 | SPECIAL_ATTACK | 2 |
| XSPECIAL3 | SPECIAL_ATTACK | 3 |
| XSPECIAL6 | SPECIAL_ATTACK | 6 |
| XSPDEF | SPECIAL_DEFENSE | 设置真2／假1 |
| XSPDEF2 | SPECIAL_DEFENSE | 2 |
| XSPDEF3 | SPECIAL_DEFENSE | 3 |
| XSPDEF6 | SPECIAL_DEFENSE | 6 |
| XSPEED | SPEED | 设置真2／假1 |
| XSPEED2 | SPEED | 2 |
| XSPEED3 | SPEED | 3 |
| XSPEED6 | SPEED | 6 |
| XACCURACY | ACCURACY | 设置真2／假1 |
| XACCURACY2 | ACCURACY | 2 |
| XACCURACY3 | ACCURACY | 3 |
| XACCURACY6 | ACCURACY | 6 |

当前X_STAT_ITEMS_RAISE_BY_TWO_STAGES真。AI按对应当前阶级和请求量排序；真实中央反向／单纯／封顶由WP44／28，预计可用不代替提交。

## 4. 普通换人处理器目录

文件`005_AI/002_AI_Switch.rb`；每项完整条件和概率在主稿§3.1，按下表登记序先愿换，再中等以上否决。

| 族 | 审计身份 | 起行 | 合同 |
| --- | --- | ---: | --- |
| ShouldSwitch | perish_song | 177 | WP51 §3.1 |
| ShouldSwitch | significant_eor_damage | 192 | WP51 §3.1 |
| ShouldSwitch | cure_status_problem_by_switching_out | 233 | WP51 §3.1 |
| ShouldSwitch | wish_healing | 294 | WP51 §3.1 |
| ShouldSwitch | yawning | 318 | WP51 §3.1 |
| ShouldSwitch | asleep | 374 | WP51 §3.1 |
| ShouldSwitch | battler_is_useless | 424 | WP51 §3.1 |
| ShouldSwitch | foe_absorbs_all_moves_with_its_ability | 448 | WP51 §3.1 |
| ShouldSwitch | absorb_foe_move | 508 | WP51 §3.1 |
| ShouldSwitch | sudden_death | 556 | WP51 §3.1 |
| ShouldSwitch | high_damage_from_foe | 574 | WP51 §3.1 |
| ShouldNotSwitch | lethal_entry_hazards | 608 | WP51 §3.1 |
| ShouldNotSwitch | battler_has_super_effective_move | 633 | WP51 §3.1 |
| ShouldNotSwitch | battler_has_very_raised_stats | 668 | WP51 §3.1 |
| ShouldNotSwitch | battler_is_immune_via_wonder_guard | 685 | WP51 §3.1 |

## 5. 责任与未决

本包负责基础AI决策顺序、技能／标记、普通换人目录与后备评分、主动道具分类、Mega与候选权重抽取。通用目标评分、状态／阶级数值与基础预测由WP52-A；具体场域／伤害／恢复／多目标效果WP52-B，物品／调用／控制评分WP52-C。技能0不等同无任何偏好（野生稳定槽重复仍在），特殊模式入口不代表本包完成设施策略。全局AI覆盖与运行／插件组合、WP78→79→80保留。

本轮记录：2026-09-28 [独立首审报告](../../review/wp50-wp51-wp52a-review-2026-09-28/report.md)／[有限修订提示](../../review/wp50-wp51-wp52a-review-2026-09-28/revision-prompt.md)；依据报告§4授权限定Reviewed回填；默认数值／登记数据及前向责任不变。被审首稿v1完整身份 `f3837410a9c41617495d2691e69f2e7baa11e7e5c3d7521f618a0f1472ad6c09`（4,811字节）保留历史，当前新字节不冒充被审对象；其它已支持范围、运行未决与阶段出口保留。
