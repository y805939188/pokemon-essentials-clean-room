"""Write M09 audit metadata only. No reference/model execution."""
from pathlib import Path
import json,runpy,sys,contextlib,io
O=Path(__file__).parent
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
p=O/'reading-coverage.json'; d=json.loads(p.read_text()); V=d['source_baseline']['commit']; B=d['specification_baseline']['commit']
def merge(rs):
 out=[]
 for a,b in sorted(rs):
  if out and a<=out[-1][1]+1:out[-1][1]=max(out[-1][1],b)
  else:out.append([a,b])
 return out
def add(path,ranges,entry,rule,mapping):
 row=next((s for s in d['sources'] if s['path']==path),None)
 if row is None:
  row={'path':path,'version':V,'total_lines':len((R/path).read_text(encoding='utf-8-sig').splitlines()),'material_availability':'available','evidence_level':'static_semantic_dependency_projection','review_extent':'partial','scope_role':'necessary_dependency_projection','semantic_segments':[]};d['sources'].append(row)
 seg={'lines':ranges[0] if len(ranges)==1 else None,'line_ranges':ranges,'entry_points':entry,'rules_and_comparison':rule,'spec_mapping':mapping,'comparison_result':'supported_static_dependency_projection','boundary':'只核M09消费者所需投影，不声称完成外部主责文件全部行为；未执行参考或模型。'}
 if not any(s.get('entry_points')==entry for s in row['semantic_segments']):row['semantic_segments'].append(seg)
 old=row.get('read_intervals',[])
 if row['review_extent']=='full':old=[[1,row['total_lines']]]
 for s in row['semantic_segments']:
  if s.get('lines'):old.append(s['lines'])
  old.extend(s.get('line_ranges',[]))
 row['read_intervals']=merge(old+ranges)
 row['semantic_compared_intervals']=row['read_intervals']
 gaps=[];last=0
 for a,b in row['read_intervals']:
  if a>last+1:gaps.append([last+1,a-1])
  last=max(last,b)
 if last<row['total_lines']:gaps.append([last+1,row['total_lines']])
 row['unreviewed_intervals']=gaps
 row['unreviewed_scope']='列出未审行属其它模块完整行为，M09必要投影已按段比较；不得据本记录推外域全通过。'
def spec(path,ranges,note,kind='specifications'):
 row=next((s for s in d[kind] if s['path']==path),None)
 if row is None:row={'path':path,'version':B,'material_availability':'available'};d[kind].append(row)
 n=len(Path(path).read_text().splitlines());rs=merge(row.get('read_intervals',[])+ranges);row.update(total_lines=n,read_intervals=rs,semantic_compared_intervals=rs,review_extent='full' if rs==[[1,n]] else 'partial',evidence_level='static_semantic_contract_comparison',note=note)
 gaps=[];last=0
 for a,b in rs:
  if a>last+1:gaps.append([last+1,a-1])
  last=max(last,b)
 if last<n:gaps.append([last+1,n])
 row['unreviewed_intervals']=gaps
# All displayed parameter/power/failure ranges were actually read and compared by the reviewer.
for mode,label,rule in [('params','委托参数/排除集合','逐项核上下降序列、侧交换13项；仿效/借助/梦话/模仿/写生/号令/安可具体字符串与代际追加，注释排除不生效。'),('power','委托基底/固定伤害/击数','逐公式核整数/实数与取整、速度/重量/HP/PP/累计/场域条件；AI自身替代的随机/多击/反击估计仍以WP52为准，未把实效直接冒充AI。'),('failure','委托目标资格','逐门核类型/能力可变、免疫/既有记录/候选/持物与招式黑名单；无消息查询分离状态提交；瞌睡施加走普通睡眠资格而非到期查询。')]:
 oldargv=sys.argv;sys.argv=[str(O/'read-delegates.py'),mode,'0','0']
 with contextlib.redirect_stdout(io.StringIO()):m=runpy.run_path(str(O/'read-delegates.py'))
 sys.argv=oldargv
 for path,a,body,keep in m['blocks']:
  ranges=merge([[a+j+1,a+j+1] for j in keep]);entry=label+': '+body[0].split(' < ')[0].replace('class Battle::Move::','')
  add(str(path.relative_to(R)),ranges,entry,rule,'WP52-A/B/C对应效果行；WP44参数附表；WP47-A/B默认排除与物品映射；实效由M08主责')
P='Data/Scripts/'
rows=[
('003_Game processing/005_Event_Handlers.rb',[[1,96]],'事件有序通知','命名回调按登记插入序逐一调用，不因返回值自动停止；覆盖者自己的handled门避免后写。','WP53§8'),
('003_Game processing/006_Event_HandlerCollections.rb',[[1,96]],'事件/菜单分派','事件缺项无调用；具名登记覆盖同键；世界事件位置与menu条件分属入口。','WP53§8'),
('012_Overworld/001_Overworld.rb',[[197,257]],'步进遭遇到模式覆盖','可战与遭遇门后先发物种钩子；double前受force_single，双敌只走普通start，尾部清force；Safari计步早返在前。','WP53§3/8'),
('012_Overworld/002_Battle triggering/005_Overworld_RoamingPokemon.rb',[[135,228]],'漫游优先覆盖','已漫游/搭档/雷达/75%门，按可遇集合抽取并强制单敌；已有handled不改。漫游先于Safari/捕虫；不是模式绝对优先。','WP53§8.1–8.2'),
('013_Items/005_Item_PokeRadar.rb',[[161,221]],'雷达物种/生成通知投影','物种重写及force_single；位置闪光通知按生成阶段执行；无Safari独有禁门，判奖直构不进入。','WP53§8'),
('011_Battle/004_Scene/001_Battle_Scene.rb',[[90,112],[175,274]],'回放中止和消息计时','可中止BACK一次派发；普通消息文字完成后1秒关闭，可中止只加速文字不跳尾计时；暂停原3秒被录像覆为普通。','WP58§6；WP67-A§9/10'),
('011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',[[368,400],[637,734]],'回合末裁判/替补前后','灭亡同侧来源检查调用条款判决；决定门先于一般尾部，普通补位后再尾清；Arena覆写super后判与再次补位符合WP56。','WP54§6；WP56§3；WP58§5'),
('011_Battle/007_Other battle code/004_Battle_Peers.rb',[[45,66]],'出入场持久形态交界','离场通知可改持久形态且夹HP上限；设施还原不是深快照，BURMY等非明确恢复字段仍可能保留。','WP55§3；WP58§6'),
('011_Battle/002_Battler/001_Battle_Battler.rb',[[101,118],[438,496]],'HP写穿/不可移物','HP写穿关联个体；邮件优先、变身例外、Mega动态绑定后物种物品组合；物种查询与变身分开。','WP56§3；WP52-C§3；WP47-B§5'),
('011_Battle/002_Battler/002_Battler_Initialize.rb',[[129,150],[223,242]],'入场暂存重置投影','普通初始化清行动记录、Pinch等；Arena自身累计不属于此处字段，实际pbRecordBattlerAsParticipated不调用孤立复位。','WP56§2/3'),
('014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',[[178,201]],'BURMY离场持久形态','只有战斗结束且参与者才按环境变披蓑；设施只还等级/物品/治疗和MegaPrimal不泛称恢复所有原字段。','WP55§3；WP58§6'),
('011_Battle/003_Move/012_MoveEffects_ChangeMoveEffect.rb',[[750,785],[985,1018],[1080,1105],[1178,1193],[231,310]],'黑名单追加与秘密之力','仿效世代6追加拖出两族；借助世代6追加自然之力/两回合和状态拖出；梦话资格真传特殊可用；秘密之力先场地后环境写取值供AI，不模拟真实后段。','WP52-C§4；WP47-A附表§1'),
('011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb',[[800,816]],'安可世代追加','世代7追加6调用族；镜面反射常排不重复追加。','WP52-C§5.3；WP47-B附表§1'),
('011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',[[1287,1583]],'委托类型完整映射','隐藏力量按图标位置类型次序含妖精；旧代威力从60位或、当前固定60；自然恩前缀/完整数值与空身份异常分离；石板17/存储碟17/卡带4及天气/场地不合并资格。','WP52-A§3；WP52-B§2/6；WP47-A§3及附表§2/3'),
('011_Battle/003_Move/002_Move_Usage.rb',[[128,161]],'芳香幕无消息查询','模式破坏者先绕；目标或存活盟友有效芳香幕即拒，消息假不显示但仍拒。','WP52-C§5.3；WP47-B§4'),
('010_Data/002_PBS data/006_Item.rb',[[198,255]],'不可失物内容组合','ARCEUS/MULTITYPE、SILVALLY/RKSSYSTEM先门和8种具名组合逐项对照；无匹配可空假。','WP52-C§3；WP47-B附表§2'),
('011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',[[140,144],[174,216],[362,411],[822,845],[1090,1656]],'AI计算委托/离场投影','读取所有所需命中/伤害四槽/会心/优先级登记，复制保同族；AI显式替代ANALYTIC/STAKEOUT/相性/会心仍用自身规则；Prankster写后清；危急退出训练家需canSwitchOut，Arena禁止，回合末只召回。','WP52-A§3；WP48§2–7；WP56§3；WP58 RC26'),
('011_Battle/007_Other battle code/009_Battle_ItemEffects.rb',[[102,129],[445,477],[690,1082],[1084,1089],[1126,1145],[1164,1171],[1208,1217],[1237,1271],[1509,1575]],'AI物品计算及录像退出','全部AI用户计算/命中/会心与非树果目标计算实读；AI排树果且GemConsumed事后清；目标会心登记空故误传无基线效应。EjectPack查换出门，EjectButton绕普通换出，RedCard随机后备与消费在拘束拒绝前；均可进入录像换人结果流。','WP52-A§3；WP50§2/3/5；WP56§3；WP58 RC26')]
for path,rs,e,r,mp in rows:add(P+path,rs,e,r,mp)
base='deliverables/final-specification-set/'
for path,rs,n in [
('pokemon-rules/wp44-effect-coverage.md',[[1,180]],'阶级参数全部当前65表、复杂K01–K22以及多项下降，与AI取statUp/statDown投影比对；其余非M09范围未全审。'),
('pokemon-rules/wp44-statuses-stat-stages-and-immunities.md',[[45,54],[76,80]],'瞌睡施加普通睡眠查询与到期专门查询当前已有明确分离；WP52-A术语不是新的不同守卫合同，不立文字类必修。'),
('combat-requirements/wp47-a-attributes-targeting-calling-data.md',[[1,212]],'七调用入口全部名单、三类型持物映射、自然恩67条与AI委托门对照；附表不是AI独立模拟真实击后链。'),
('combat-requirements/wp47-b-control-items-coverage-data.md',[[1,105]],'号令/安可、不可移物组合、Fling全部默认分组与AI输入投影比对，非完整真实执行审查。'),
('pokemon-rules/wp48-ability-calculation-modifiers.md',[[1,188]],'完整AI委托所需命中/伤害/会心/优先级合同，AI自有估计替代先于通用委托，主责M08。'),
('pokemon-rules/wp50-held-item-triggers-and-consumption.md',[[13,71],[113,131]],'AI委托参数与消费副作用分离；记录退出及自然恩真执行/AI预测边界。'),
('user-interface/wp67-a-battle-interaction-and-presentation.md',[[283,317]],'特殊模式公开命令/反馈、计时、Arena实际连续裁判、回放条件化目标窗口已承接；资源与绘制细节仍静态/宿主边界。')]:spec(base+path,rs,n)
spec('review/wp53-delivery-2026-10-02/revision-v3/entry-coverage-table.md',[[1,81]],'原稿明确引用的有效行为附表全读：48入口规则已由现行WP53正文与SF向量承接；没有当前正文未承接的独有事实。旧PASS不作本轮证据。','supplements')
# Register formal WP54–58 already fully read and compared in prior context windows.
for path in sorted(Path(base).rglob('wp*.md')):
 if any(path.name.startswith(x) for x in ('wp54-','wp55-','wp56-','wp57-','wp58-')):
  spec(str(path),[[1,len(path.read_text().splitlines())]],'全部正文/附表/案例/边界已实读并与本轮源语义分段对照；来源双向映射继续整理。')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=O/'progress.json';g=json.loads(p.read_text());g.update(phase='bidirectional_mapping_and_remaining_shared_projections',next_actual_range='补完数据标志/构造与少量规则消费者投影；写完整双向映射、反证处置与最终覆盖检查',complete=False);g['pending_analysis_questions']=['GR5-M09-001保留候选，模块内反证完成后仍需父会话独立裁定；Yawn/Conversion排除必修，详见最终处置'];p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
(O/'progress.md').write_text('# M09 进度\n\ncomplete=false。38 主责脚本、13 PBS 全记录、15 正式稿及附表、全部分配向量、15 原稿已逐段读取比较。已补 AI 委托参数/排除名单/威力/目标资格/计算处理器及模式调用交界，并全读 WP53 v3 行为补充表。\n\n当前候选：GR5-M09-001，Life Dew 独立评分可恢复门缺漏，candidate_pending_independent_counterevidence，未自签最终必修。\n\n下一实际范围：数据标志/构造及少量剩余消费者；双向条款/注册映射；最终覆盖与 JSON 校验。仅静态，无参考或模型执行，实际模型参数 UNVERIFIED。\n')
print('saved',len(d['sources']),'source rows;',len(d['specifications']),'spec rows')
