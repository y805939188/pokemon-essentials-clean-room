"""Finalize manually reviewed metadata; does not execute reference behavior."""
from pathlib import Path
import runpy,json,re,io,contextlib
O=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):m=runpy.run_path(str(O/'append-projections.py'))
add=m['add'];spec=m['spec'];d=m['d'];R=m['R'];P='Data/Scripts/'
for p,rs,e,r,mp in [
('014_Pokemon/001_Pokemon.rb',[[428,459],[497,524],[1133,1162],[1213,1227]],'设施构造/性格/克隆后续投影','空owner得到默认记录；PID参与未指定性格/特性；指定有效性格可重算，最终设施再算；形态创建可能调用外部规则，不假定所有种固定0；显式clone与Marshal快照分开。','WP55§2.5；WP57§2.4；WP58§3'),
('021_Compiler/002_Compiler_CompilePBS.rb',[[332,389]],'设施基础阶段的数据前向/反向关系','编译先枚举进化ID，再按首条前进化建倒向记录；有效后续过滤None与基础阶段递归不是仅看原PBS该物种有无Evolution字段。','WP54§3；WP76§8'),
('011_Battle/002_Battler/006_Battler_AbilityAndItem.rb',[[466,476]],'宝石计算的暂存副作用','誓约族排除，匹配当前类型后标记GemConsumed并改威力倍率，AI委托后显式清；不是实际消费。','WP52-A§3.2；WP50§3.2'),
('011_Battle/003_Move/012_MoveEffects_ChangeMoveEffect.rb',[[211,232]],'秘密之力准备入口定义','准备字段可被AI调用写入；自带畏缩集合与真实结果集合不同，当前WP47-A§3.3已有合同。','WP52-C§4'),
('011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',[[70,163]],'冰OHKO加载后资格交界','真实原冰目标拒被后加载条款继承别名旁路；独立AI仍拒冰，命中非冰使用者减10保留。','WP54§6.1；WP52-B§2'),
('011_Battle/003_Move/001_Battle_Move.rb',[[1,30]],'新旧会心概率数据','新24/8/2/1，旧16/8/4/3/2；负下标粗伤读取末项的AI缺陷两个表均预计会心。','WP52-A§3.1'),
('011_Battle/001_Battle/005_Battle_ActionSwitching.rb',[[383,421]],'入场位置愿望投影','治愈愿望/月亮舞有可恢复/状态/PP及代际保留门；只核AI愿望替补和位置记录消费者，不扩大全部危害行为。','WP51§3.2；WP52-B§4'),
('011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb',[[319,395]],'Arena技分保护来源','保护族在返回失败前写当前招式成功状态protected；与前段useState及回合末槽消费组合，不能把保护当普通未命中扣技分。','WP56§3'),
('019_Utilities/003_Utilities_BattleAudio.rb',[[1,117]],'设施与回放音频外部读取','nextBattle覆盖优先；对手类型后地图/全局/默认；回放以当前世界选择，不是18键记录媒体完整还原。','WP55§3；WP58§6'),
('012_Overworld/002_Battle triggering/002_Overworld_BattleIntroAnim.rb',[[59,153]],'战斗演出世界外壳','进入in_battle、暂停/恢复音乐、根据当前地点时刻选演出；正常返回清一次性字段/步数再世界淡入；无统一异常ensure，回放共享外壳不是设施治疗包装。','WP53§4/6；WP55§3；WP58§6')]:add(P+p,rs,e,r,mp)
base='deliverables/final-specification-set/'
spec(base+'pokemon-rules/wp53-safari-and-bug-catching-contest.md',[[1,len(Path(base+'pokemon-rules/wp53-safari-and-bug-catching-contest.md').read_text().splitlines())]],'全部当前正文及SF35向量与四主责源、世界/捕获/保存/配置/PBS消费者对照；v3补充表48入口无独有事实未承接。')
spec(base+'combat-requirements/wp47-a-move-attributes-targeting-and-calling.md',[[39,102]],'委托类型、隐藏力量、当前自然恩反应链与AI不模拟该链的有效补充；秘密之力场地/环境表已逐项对照。')
# Exact field projection identities over facility-used species/types already read in bounded displays.
with contextlib.redirect_stdout(io.StringIO()):j=runpy.run_path(str(O/'data-joins.py'))
for kind,path,fields,keys in [('species','PBS/pokemon.txt',['BaseStats','Abilities','Height','Weight','Evolution'],j['usedspecies']),('types','PBS/trainer_types.txt',['BaseMoney','SkillLevel','Flags'],j['usedtypes'])]:
 ls=(R/path).read_text(encoding='utf-8-sig').splitlines();sel=[];current=None
 for i,s in enumerate(ls,1):
  if s.startswith('['):current=s[1:-1]
  if current in keys and (s.startswith('[') or any(re.match(re.escape(f)+r'\s*=',s) for f in fields)):sel.append([i,i])
 add(path,m['merge'](sel),'设施全部使用标识的规则输入字段','所有使用物种/类型字段已读并静态join；无缺物种/性格/类型，44训练家类型无Flags，SkillLevel按BaseMoney回退；None进化不作为有效后续。数据列入不保证资格通过。','WP54§3；WP55§2.5；WP51§2；WP76§8')
# NG all literal fields read; Fling value/ordered-ID equality is an auxiliary check, not full items review.
ls=(R/'PBS/items.txt').read_text(encoding='utf-8-sig').splitlines();ng=[];fl=[];key=None
for i,s in enumerate(ls,1):
 if s.startswith('['):key=s[1:-1]
 if s.startswith('Flags'):
  for f in s.split('=',1)[1].split(','):
   if re.fullmatch(r'NaturalGift_\w+_\d+',f.strip(),re.I):ng.append([i,i])
   if re.fullmatch(r'Fling_\d+',f.strip(),re.I):fl.append({'item':key,'line':i,'flag_value':int(f.strip().split('_')[1])})
add('PBS/items.txt',ng,'自然之恩全部67标志','完整67条类型/威力在有界显示中逐条读取并与当前附表比较；与可恢复/吃果真实执行不混同。','WP52-B§2.1；WP47-A附表§3')
it=next(s for s in d['sources'] if s['path']=='PBS/items.txt');it['auxiliary_data_checks']=[{'kind':'Fling ordered literal flags and identities','records':fl,'result':'20威力组逐组完整有序标识/数值相等，无多余威力组；语义来自Fling前缀/数字守卫和完整现行表人工阅读。','review_extent':'partial','boundary':'不是物品文件578条被动行为的全文审查；只核M09消费的数字标志'}]
for row in d['sources'][:51]:
 row['scope_role']='primary_assigned'
 if row['path'].startswith('PBS/'):
  row.update(review_extent='full',evidence_level='static_full_record_and_consumer_semantic_comparison',pending_semantic_dimensions=[],read_intervals=[[1,row['total_lines']]],semantic_compared_intervals=[[1,row['total_lines']]],unreviewed_intervals=[])
  for s in row['semantic_segments']:
   s['comparison_result']='supported_static_data_consumption';s['boundary']='全部记录及其名单/字段消费语义已读，静态标识join仅辅助；没有编译、生成、执行或全体组合成功保证。'
  row['final_cross_data_result']='全字段/全名单已核：全部候选索引在所指表范围内；只有Tower模板137的STICK持物和249的VICEGRIP招式未在当前活跃PBS登记，通用解析合同分别置空/丢弃（WP76§8.4），不构成当前合同新缺口。Fancy单表86/87重复索引59/97保留权重；未引用Fancy双文件正确排除默认消费。'
  row['cup_termination_comparison']='Pika20×3>50、Poke55×3>155、Fancy30×3>80与长名单无上限校验循环组合可不终止；WP54建议级不均摊/总级整队门与WP55§2.5/§4已经明确给足条件，未把未执行demo事件断言默认必卡。'
 else:
  row['read_intervals']=[[1,row['total_lines']]];row['semantic_compared_intervals']=[[1,row['total_lines']]]
  for s in row['semantic_segments']:
   s['final_comparison']='supported_static；必要消费者已在dependency投影记录补齐；LifeDew独立评分守卫按GR5-M09-001例外，不能以全读等于全supported。'
   s['boundary']='固定R/B5静态行为比较；原范围注释保留阅读过程，最终以final_comparison、双向映射及findings为准。'
# Audit navigation and current-status interpretation were read in earlier windows.
spec('audit/source-traceability.md',[[739,750],[979,990],[1128,1178],[1182,1232]],'M09所有当前来源导航已跟读；只用于追溯，历史PASS不作为本轮证据，未递归历史管理验收。','supplements')
d['unavailable_material_boundaries']=[{'path':'Data/trainer_lists.dat','version':d['source_baseline']['commit'],'material_availability':'absent_from_available_reference_checkout','review_extent':'unreadable','evidence_level':'filesystem_presence_check_and_compiler_contract','behavior_boundary':'13PBS均可得且已全审，正常编译可创建产物；不因raw产物缺失断言常规启动失败。'},{'path':'Data/Map*.rxdata / Data/MapInfos.rxdata','version':d['source_baseline']['commit'],'material_availability':'absent_from_available_reference_checkout','review_extent':'unreadable','evidence_level':'Data directory inventory','behavior_boundary':'Data当前只有Scripts、Scripts.rxdata、messages_core.dat；接待/奖励/播放事件可达性保留未知，不把源码无调用断言功能不存在。'}]
(O/'reading-coverage.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('finalized',len(d['sources']),'source paths; primary all 51 full; further mapping/validation still pending')
