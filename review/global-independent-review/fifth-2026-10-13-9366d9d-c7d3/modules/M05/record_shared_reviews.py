"""Record completed bounded comparisons; never a substitute for reading."""
import review_state as s
import json

P='deliverables/final-specification-set/'
LOG=s.ROOT/'shared-review-log.json'
def record(path, ranges, source_patterns, result, status='supported'):
    d=json.loads(LOG.read_text()) if LOG.exists() else {'schema_version':'gr5.review.v1','module':'M05','comparisons':[]}
    q={'path':P+path,'version':s.B,'actual_semantic_ranges':ranges,'source_patterns':source_patterns,'status':status,'comparison_result':result,'evidence_level':'supported_static' if status=='supported' else 'static_semantic_review','scope':'M05 consumer projection only, not whole external-module certification','execution_status':'not_executed'}
    d['comparisons']=[x for x in d['comparisons'] if x['path']!=q['path']]+[q]
    LOG.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
    record('generic-kernel/wp02-rule-configuration-and-data-variants.md',[[41,203]],['001_Settings.rb','002_BattleSettings.rb'],'配置词典逐项对照默认值及派生门；M05资源/背包/治疗/教学/球/野外/持物交界支持。其它展示行已读但不作为外模块全审。')
    record('generic-kernel/wp03-content-identity-and-schema.md',[[1,240]],['006_Item.rb','014_TrainerType.rb','015_Trainer.rb','017_PlayerMetadata.rb','001_GameData.rb'],'身份/严格与容错查询、schema、价格缺省吻合；Item其它缺省字段/ShowQuantity线索单独保留有界未决，不据责任目录认定已承接。','partial')
    record('generic-kernel/wp04-pbs-lifecycle.md',[[94,110],[153,178]],['002_Compiler_CompilePBS.rb','003_Compiler_WritePBS.rb'],'Move→Item/Item→Metadata与BerryPlant非枚举依赖支持；通用反写读取实际字段，编辑器错键另见N005，不承诺文本无损。')
    record('generic-kernel/wp09-save-startup-continue.md',[[59,82]],['004_Game_SaveValues.rb'],'player/bag/storage持久单元与new-game生产值匹配；不重做整个启动/写档合同。')
    record('generic-kernel/wp10-migration-failure-recovery.md',[[78,100]],['005_Game_SaveConversions.rb'],'M05背包四变量改名及笛标记迁移的条件和分流匹配。')
    record('engine-overworld/wp15-resource-matching-and-audio.md',[[69,85]],['003_Trainer_Sprites.rb','006_Item.rb','007_Item_Sprites.rb'],'训练家登记门、套装回退、道具unknown/back/机器类型/持物图标的业务选择吻合；媒体未执行。')
    record('engine-overworld/wp60-fishing.md',[[1,144]],['002_Item_Effects.rb','Overworld_Fishing.rb'],'三竿45/70/95与1.5倍、不封顶；首非蛋加速；auto仍需输入；无表仍演出/不遇敌；恢复与统计分层已承接。')
    record('pokemon-rules/wp60-berry-plants.md',[[20,183]],['006_Overworld_BerryPlants.rb','007_BerryPlant.rb'],'四覆盖物数学、壶不耗、施肥先写后耗且取消不回滚、采摘预检与外层reset分离支持；事件可达未证。')
    record('pokemon-rules/wp61-field-passive-effects-and-blackout.md',[[48,66],[116,155]],['002_Item_Effects.rb','001_Overworld.rb','001_Pokemon.rb','004_PokemonStorage.rb'],'Repel耗尽提示、友好持物修正、逃脱点不同于治疗点、存盒治疗保留待进化/治疗不还原物品均有合同。')
    record('engine-overworld/wp59-world-time-weather-field-moves.md',[[181,232]],['004_Overworld_FieldMoves.rb','002_Item_Effects.rb','016_UI_ReadyMenu.rb'],'徽章/查找/快捷门分别定义；HONEY→SweetScent天气先行无值与外层成功不等于遭遇成立。')
    record('combat-requirements/wp51-ai-action-selection-and-skill.md',[[1,156]],['003_AI_UseItem.rb','002_AI_Switch.rb','008_AI_Utilities.rb','010_AIBattler.rb','001_Battle_AI.rb'],'M05投影：主动物品完整资格扫描先于偏好；AI上下文与缺招索引失败退出整段；SITRUS估1、蘑菇错组、治状态方向、复活排序、后备持久物近似及残余各项均已明确，不以真实效果替代估量。')
    record('combat-requirements/wp51-ai-decision-defaults.md',[[1,92]],['003_AI_UseItem.rb'],'全部HP/状态/复活/X道具身份、别名与数量对照支持；不是实际效果登记。')
    record('combat-requirements/wp52-c-items-calling-and-control-evaluation.md',[[1,208]],['008_AI_Utilities.rb','007_AI_MoveEffects_Items.rb','010_AIBattler.rb','003_AI_MoveEffects_BattlerOther.rb','009_AI_MoveEffects_SwitchingActing.rb'],'全部物品评级与即时食用效用及物品操作预测已对照；ASPEAR拼写、腐蚀方向、查封/魔法空间、投掷/偷换/回收、不消费实际资源均明确。非物品其它行仅作为上下文读取。')
    record('combat-requirements/wp52-c-item-control-coverage-and-data.md',[[1,191]],['008_AI_Utilities.rb','007_AI_MoveEffects_Items.rb'],'215基础身份/15档、46直接7复制、39类型增幅+18宝石条件完整对应；数量为辅助定位，结论来自逐处理器和表值语义对照。')
    record('combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md',[[37,110],[114,141],[178,210]],['011_AIMove.rb','010_AIBattler.rb','007_AI_ChooseMove_OtherScores.rb','006_AI_ChooseMove_GenericEffects.rb','003_AI_MoveEffects_BattlerOther.rb'],'物品有效性/会心目标误传、跳目标树果、清GemConsumed、对焦镜估计与真时机差别、治状态果门、等级偏好消费者有界支持。')
    record('combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md',[[25,61],[77,197]],['004_AI_MoveEffects_MoveAttributes.rb','005_AI_MoveEffects_MultiHit.rb','006_AI_MoveEffects_Healing.rb','006_AI_ChooseMove_GenericEffects.rb'],'物品修正投影：自然之恩数据、飞行宝石杂技、香草两回合门、大根估量、天气伞/岩/膜/种子/靴/光黏土均吻合；未将预测当实际逐击。')
    record('combat-requirements/wp52-b-effect-coverage.md',[[88,112]],['006_AI_ChooseMove_GenericEffects.rb'],'天气和地形收益匹配身份组与持物条件的有界投影支持。')
