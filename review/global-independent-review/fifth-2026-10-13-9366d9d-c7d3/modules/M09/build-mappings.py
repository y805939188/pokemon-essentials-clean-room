"""Audit index over already manually reviewed material; not a behavior model.
All writes stay in the M09 directory. Lexical links never establish support by themselves.
"""
from pathlib import Path
import json,re
O=Path(__file__).parent;W=Path.cwd();R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
d=json.loads((O/'reading-coverage.json').read_text());V=d['source_baseline']['commit'];B=d['specification_baseline']['commit']
common={k:v for k,v in d.items() if k not in ('sources','specifications','original_drafts','supplements')}
F='deliverables/final-specification-set/'
prim=[]
for p in Path(F).rglob('wp*.md'):
 if re.match(r'wp(51|52-[abc]|53|54|55|56|57|58)-',p.name):prim.append(p)
prim.sort(); names={p.name:str(p) for p in prim}
# Capabilities are behavioral families; registration occurrences do not create new capabilities.
labels=[('AI.SKILL_FLAGS','AI 上下文、技能与动作阶段'),('AI.SWITCH_POLICY','换人意愿及否决'),('AI.REPLACEMENT','替补候选与残余估计'),('AI.ITEM_ACTION','主动道具选择'),('AI.CANDIDATES','招式和目标枚举、重定向'),('AI.TARGET_SCORE_PIPELINE','失败预测与评分合成'),('AI.SELECTION','分数转权重及随机登记'),('AI.GENERIC_MODIFIERS','通用评分修正'),('AI.ROUGH_CALCULATION','粗类型、能力值、伤害、命中与会心'),('AI.STAT_EVALUATION','阶级变化评分'),('AI.STATUS_EVALUATION','异常状态与持续记录评分'),('AI.TYPE_ABILITY_VALUE','类型变化与能力价值'),('AI.FIELD_EVALUATION','天气、场地、危害和侧效应评分'),('AI.POWER_MULTIHIT','特殊基底、多击、蓄力和反击评分'),('AI.HEALING','恢复、吸取、持续伤害与牺牲评分'),('AI.LIFEDEW_SCORE','生命水滴的独立评分守卫'),('AI.PROTECTION','保护、反伤、墙和命中控制评分'),('AI.ITEM_VALUE','物品评级与消费效用'),('AI.ITEM_EFFECTS','主动持物操作评分'),('AI.CALLING','调用、复制与混合效果评分'),('AI.CONTROL','换人、拘束、行动顺序和PP控制评分'),('AI.DISPATCH','评分登记、默认、复制和条件组'),('SAFARI.SESSION','Safari 会话、区域和预算'),('SAFARI.BATTLE','Safari 独立战斗'),('CONTEST.SESSION','捕虫会话、计时和队伍恢复'),('CONTEST.BATTLE','捕虫战斗与保留候选'),('CONTEST.JUDGING','捕虫判分、排序和结算'),('WORLD.MODE_INTEGRATION','世界事件、菜单、保存和模式竞争'),('FACILITY.ELIGIBILITY','参赛资格和队伍组合'),('FACILITY.CUPS','默认杯赛和模式参数'),('FACILITY.LEVEL','等级调整及经验还原'),('FACILITY.CLAUSES','战斗条款及实际消费'),('FACILITY.SESSION','设施会话、计数和保存'),('FACILITY.OPPONENTS','对手索引与候选消费'),('FACILITY.DATA','完整设施数据记录的消费语义'),('FACILITY.ROUND','单场包装、清理和胜负返回'),('VARIANT.PALACE','Palace 性格、选招、压半和换人'),('VARIANT.ARENA','Arena 心技体、判决和顺序替补'),('FACTORY.GENERATION','租借候选生成及排除'),('FACTORY.INTERACTION','租借、交换和对象身份'),('RECORD.LIFECYCLE','录像提升、导出和持久化'),('RECORD.INITIAL','录像初始字段与复制'),('RECORD.ACTIONS','动作登记和回放分派'),('RECORD.RANDOM_SWITCH','随机及替补结果流'),('RECORD.LIMITS','回放布局、外部依赖与中止限制')]
ids={i+1:'M09.'+a for i,(a,b) in enumerate(labels)}
caps={ids[i+1]:{'id':ids[i+1],'title':b,'module':'M09','status':'supported','support_boundary':'supported_static：固定R与B5、本轮实际阅读的具名语义范围；不是运行、跨版本、图形资源或任意插件扩展通过。','source_anchors':[],'spec_anchors':[],'test_vectors':[],'related_findings':[],'unique_identity_policy':'与共享接口交叉引用，不按handler、别名或重复数据行重算能力。'} for i,(a,b) in enumerate(labels)}
caps[ids[16]].update(status='missing',support_boundary='静态审查结果：当前表行缺独立评分守卫；GR5-M09-001仍待父会话独立反证与最终裁定。',related_findings=['GR5-M09-001'])
caps[ids[24]]['presentation_boundary']='公开命令、球数、投球/饵/石/怒/吃反馈有合同；固定像素、局部时间片、资源实际播放未作为逐帧兼容要求，UI投影见共享接口。'
caps[ids[35]]['data_boundary']='全部13文本文件/全记录逐段读；列举内容通过规则消费，不承诺独立实现必须复制原demo姓名/台词/全部队伍内容。无默认编译产物可运行确认。'
caps[ids[45]]['status']='partial';caps[ids[45]]['support_boundary']='supported_static 已述局部回放行为；地图事件/编译运行对象/媒体资源与宿主效果不可得或未执行，完整重放等价未获支持，当前规格已保留这些边界。'
def select(row,a,b):
 p=row['path'];f=Path(p).name
 if '/005_AI/' in p:
  n=int(f[:3]);return {1:[1,6,22] if a<80 else [22],2:[2,3],3:[4],4:[1],5:[5,6,7] if b>287 else [5,6],6:[10] if b<571 else [13],7:[8],8:[3,44] if a<99 else ([12] if b<163 or (a>=231 and b<387) else [18]),9:[1],10:[3] if a<185 and b>55 else ([18] if a>=423 and b<563 else [3,9,11,12]),11:[9]}[n]
 if '/006_AI MoveEffects/' in p:
  n=int(f[:3]);return {1:([20] if b<=168 else [13,20]) if a<466 else [13,15,20,21],2:[10,13,15],3:[11] if b<=655 else ([12] if b<=1114 else [21]),4:[14] if b<=535 else ([13,17] if b<=1409 else [9,14,17]),5:[14],6:[15,16] if a==231 else [15],7:[19],8:[20,14,15,17],9:[21]}[n]
 if 'Clauses.rb' in p:return [32]
 if 'SafariBattle' in p:return [24]
 if 'BugContestBattle' in p:return [26]
 if 'PalaceBattle' in p:return [37]
 if 'ArenaBattle' in p:return [38]
 if 'RecordedBattle' in p:return [41,42,43,44,45]
 if '001_SafariZone.rb' in p:return [23,24,28]
 if '002_BugContest.rb' in p:return [25,26,27,28]
 if 'Challenge_BattleChallenge.rb' in p:return [39,40] if a>=365 else [33]
 if 'Challenge_Data.rb' in p:return [34,35] if a>=100 else [29,33,34]
 if 'Challenge_ChooseFoes.rb' in p:return [39] if a>=85 else [34,35]
 if 'Challenge_Battles.rb' in p:return [41,45] if a>=99 else [31,36,41]
 if 'UI_BattleSwap.rb' in p:return [40]
 if 'Challenge_ChallengeRules.rb' in p:return [29,30]
 if 'Challenge_Rulesets.rb' in p:return [29,30]
 if 'Challenge_EntryRestrictions.rb' in p:return [29,30]
 if 'Challenge_LevelAdjustment.rb' in p:return [31]
 if 'Challenge_BattleRules.rb' in p:return [30,32]
 if p.startswith('PBS/') and any(x in f for x in ('battle_facility','battle_tower','cup_')):return [35,34,39]
 # External dependency: selected consumer projection only.
 if '/003_Move/' in p:return [9,10,11,12,14,15,17,19,20,21,32]
 if 'AbilityEffects' in p or 'ItemEffects' in p:return [9,12,18,19,21,38,44]
 if '/002_Battler/' in p:return [3,9,10,11,15,18,19,37,38,43,44]
 if '/001_Battle/' in p:return [1,5,6,7,24,26,32,36,37,38,43,44,45]
 if 'BattleAudio' in p or 'BattleIntroAnim' in p or '/004_Scene/' in p:return [24,36,38,45]
 if 'Event_' in p:return [22,28]
 if '/012_Overworld/' in p or 'PokeRadar' in p or 'Map' in p:return [23,25,28]
 if '/021_Compiler/' in p:return [29,34,35,39]
 if 'Pokemon.rb' in p or 'Species.rb' in p or 'FormHandlers' in p:return [29,31,35,36,39,45]
 if 'Settings' in p:return [1,4,9,13,23,25,29,30,35,37,39]
 if p=='PBS/pokemon.txt':return [29,30,35,39]
 if p=='PBS/items.txt':return [18,19,24,26,35]
 if p=='PBS/moves.txt':return [5,12,14,16,35]
 if 'TrainerType' in p or 'trainer_types' in p:return [1,34,35]
 return [28,33,35,41,45]
# Manual document-section allocation, keyed by the printed section number; line units retain exact anchors.
docmap={
'wp51-ai-action':{'1':[1],'2':[1],'3.1':[2],'3.2':[3],'3.3':[3],'4':[4],'5':[5,6,7],'6':[1,2,3,4,5,6,7],'7':[1,22,44]},
'wp51-ai-decision':{'1':[4],'2':[4],'3':[4],'4':[2],'5':[1,4]},
'wp52-a-generic':{'1':[1,6,22],'2.1':[6],'2.2':[8],'3.1':[9],'3.2':[9],'3.3':[9],'4.1':[10],'4.2':[10],'4.3':[10,13],'5':[11],'6':[12],'7':[20,22],'8':[6,8,9,10,11,12]},
'wp52-a-evaluation':{'1':[22],'2.1':[20],'2.2':[10],'2.3':[11],'2.4':[12],'3.1':[8],'3.2':[12],'4':[12],'5':[13,14,15,17,18,19,20,21],'6':[22]},
'wp52-b-field':{'1':[6,22],'2.1':[14],'2.2':[14],'3':[14],'4':[15,16],'5.1':[13],'5.2':[13],'6':[17],'6.1':[17],'6.2':[17],'7':[13,14,15,17],'8':[13,14,15,17,22]},
'wp52-b-effect':{'1':[22],'2.1':[13,15,17],'2.2':[13,15],'2.3':[14],'2.4':[14,17],'2.5':[14],'2.6':[15,16],'2.7':[14,15,17],'3':[13],'4':[13,14,15,17,22]},
'wp52-c-items':{'1':[6,22],'2.1':[18],'2.2':[18],'3':[19],'4':[20],'5.1':[21],'5.2':[21],'5.3':[21],'6':[12,13,21],'7':[18,19,20,21],'8':[18,19,20,21,22]},
'wp52-c-item-control':{'1':[22],'2.1':[18],'2.2':[13,19,20,21],'2.3':[12,21],'2.4':[19],'2.5':[20],'2.6':[21],'3':[18],'4':[18],'5':[18,19,20,21],'6':[18,19,20,21,22]},
'wp53-':{'1':[23,24,25,26,27,28],'2':[23,24,25,26,27,28],'3':[23],'4':[24],'5':[25],'6':[26],'7':[27],'8':[28],'9':[23,24,25,26,27,28],'10':[23,24,25,26,27,28],'11':[28],'12':[28]},
'wp54-entry-eligibility':{'1':[29],'2.1':[29],'2.2':[29],'2.3':[29],'3':[29],'4.1':[31],'4.2':[31,36],'5':[30],'6':[32],'6.1':[32],'7':[29,30,31,32],'8':[29,30,31,32]},
'wp54-entry-rules':{'1':[30],'2':[30],'3':[29,30],'4.1':[29,30],'4.2':[29],'4.3':[31],'4.4':[30,32],'5':[32]},
'wp55-':{'1':[33,36],'2.1':[33,30],'2.2':[33,34],'2.3':[33],'2.4':[33],'2.5':[34,35],'2.6':[39,40],'2.7':[33,40],'3':[36],'4':[33,34,35,36],'5':[33,34,36],'6':[33,35],'7':[33,36]},
'wp56-':{'1':[37,38],'2.1':[37],'2.2':[37],'2.3':[37],'2.4':[37],'2.5':[37],'3.1':[38],'3.2':[38],'3.3':[38],'4':[37,38],'5':[37,38],'6':[37,38],'7':[37,38]},
'wp57-':{'1':[39,40],'2':[39],'3':[40],'4':[40],'5':[39,40],'6':[35,39],'7':[39,40],'8':[39,40],'9':[39,40]},
'wp58-':{'1':[41],'2':[41],'3':[42],'4':[43],'5.1':[44],'5.2':[44],'5.3':[37,38,43,44],'5.4':[44,45],'6.1':[45],'6.2':[42,45],'6.3':[43,45],'6.4':[45],'6.5':[36,45],'7':[41,42,43,44,45],'8':[41,42,43,44,45],'9':[45]}}
def secids(name,section):
 dic=next(v for k,v in docmap.items() if name.startswith(k))
 key=section
 while key and key not in dic:key=key.rpartition('.')[0]
 return dic.get(key,sorted({i for ls in dic.values() for i in ls}))
# source segment index retains manually written rule comparisons verbatim (no reference source code).
source_records=[]
for row in d['sources']:
 rec={k:row.get(k) for k in ['path','version','total_lines','review_extent','material_availability','evidence_level','unreviewed_intervals','scope_role']};rec['segments']=[]
 for j,s in enumerate(row.get('semantic_segments',[]),1):
  rs=s.get('line_ranges') or ([s['lines']] if s.get('lines') else row.get('read_intervals',[]))
  if not rs:rs=[[1,row['total_lines']]]
  nums=select(row,min(a for a,b in rs),max(b for a,b in rs));cs=[ids[n] for n in nums]
  anchor={'path':row['path'],'version':V,'line_ranges':rs,'entry_points':s.get('entry_points',s.get('rules','semantic data segment')),'segment_id':f"SRC-{len(source_records)+1:03}-{j:03}"}
  note=s.get('rules_and_comparison',s.get('rules',s.get('note','')))
  rec['segments'].append({'id':anchor['segment_id'],'line_ranges':rs,'entry_points':anchor['entry_points'],'capability_ids':cs,'comparison':note,'status':'partial' if 16 in nums else 'supported','support_boundary':'supported_static 已述范围；LifeDew单独见候选，不把整文件判通过。' if 16 in nums else 'supported_static 固定文本与当前合同对照，运行/外部域全量不在此结论。','original_mapping_note':s.get('spec_mapping','')})
  for cid in cs:caps[cid]['source_anchors'].append(anchor)
 source_records.append(rec)
# All literal add/copy/addIf registrations were semantically read beforehand.
regs=[]; sourcefiles=[R/s['path'] for s in d['sources'] if '/005_AI/' in s['path'] or '/006_AI MoveEffects/' in s['path']]
pat=re.compile(r'Battle::AI::Handlers::(\w+)\.(addIf|add|copy)\(')
for p in sorted(sourcefiles):
 lines=p.read_text().splitlines()
 for j,line in enumerate(lines):
  m=pat.search(line)
  if not m:continue
  end=j;op=m[2]
  if op=='copy':
   while end+1<len(lines) and not lines[end].split('#',1)[0].rstrip().endswith(')'):end+=1
  elif not line.rstrip().endswith(')'):
   while end+1<len(lines) and lines[end]!=')':end+=1
  header='\n'.join(lines[j:end+1])
  args=header[header.find('(')+1:]
  if op=='copy':keys=re.findall(r'"([^"]+)"|:(\w+)',args);keys=[x or y for x,y in keys]
  else:
   k=re.match(r'\s*(?:"([^"]+)"|:(\w+))',args);keys=[k[1] or k[2]] if k else ['<nonliteral>']
  rel=str(p.relative_to(R));row=next(s for s in d['sources'] if s['path']==rel);sn=next((s for s in source_records if s['path']==rel),None)
  segs=[s for s in sn['segments'] if any(a<=j+1<=b for a,b in s['line_ranges'])];cids=sorted({c for s in segs for c in s['capability_ids']})
  specs=[]
  for sp in prim:
   if not sp.name.startswith(('wp51-','wp52-')):continue
   for n,line2 in enumerate(sp.read_text().splitlines(),1):
    hits=[k for k in keys if k!='<nonliteral>' and re.search(r'(?<![\w])'+re.escape(k)+r'(?![\w])',line2)]
    if hits:specs.append({'path':str(sp),'version':B,'lines':[n,n],'keys':hits})
  regs.append({'id':f'REG-{len(regs)+1:04}','path':rel,'version':V,'lines':[j+1,end+1],'group':m[1],'operation':op,'source_key':keys[0],'copy_destination_keys':keys[1:] if op=='copy' else [],'conditional_key':keys[0] if op=='addIf' else None,'capability_ids':cids,'spec_anchors':specs,'semantic_segment_ids':[s['id'] for s in segs],'evidence_level':'manual_full_body_review_plus_lexical_identity_index','counting_boundary':'仅注册出现，不是新增能力数；copy缺源/重复覆盖按读过的分派规则判。'})
# Clause units: each heading, table row, prose paragraph, list item and separator (non-semantic metadata is labelled).
def units(lines):
 out=[];i=0;sec='';title='document preamble'
 while i<len(lines):
  s=lines[i]
  if not s.strip():i+=1;continue
  a=i+1
  if s.startswith('#'):
   m=re.match(r'#+\s+(\d+(?:\.\d+)*)\.?\s*(.*)',s)
   title=s.lstrip('# ').strip()
   if m:sec=m[1]
   else:sec=title.split('：',1)[0]
   out.append((a,a,'section',sec,title,s));i+=1;continue
  kind='table_row' if s.startswith('|') else ('list_item' if re.match(r'(?:[-*]|\d+\.) ',s) else 'paragraph')
  if re.fullmatch(r'\s*[-|: ]+\s*',s):kind='format_separator'
  if kind=='paragraph':
   while i+1<len(lines) and lines[i+1].strip() and not lines[i+1].startswith(('#','|','- ','* ')):i+=1
  b=i+1;out.append((a,b,kind,sec,title,'\n'.join(lines[a-1:b])));i+=1
 return out
bykey={}
for r in regs:
 for k in [r['source_key']]+r['copy_destination_keys']:bykey.setdefault(k,[]).append(r)
keypattern=re.compile(r'(?<![\w])(?:'+'|'.join(re.escape(k) for k in sorted(bykey,key=len,reverse=True))+r')(?![\w])')
primary_segments={ss['id'] for sr in source_records if sr['scope_role']=='primary_assigned' for ss in sr['segments']}
reg_index={r['id']:r for r in regs}
docs=[]
for p in prim:
 rows=[];lines=p.read_text().splitlines()
 for a,b,kind,sec,title,content in units(lines):
  nums=secids(p.name,sec);cids=[ids[n] for n in nums]
  matches=[]
  for key in set(keypattern.findall(content)):matches.extend(r['id'] for r in bykey[key])
  # LifeDew missing applies only to the substantive table/formula, not every healing row.
  missing=p.name.startswith('wp52-b-field') and a==119
  if not missing:cids=[c for c in cids if c!=ids[16]]
  if not cids:cids=[ids[15]]
  sourceids=sorted({sid for rid in matches for sid in reg_index[rid]['semantic_segment_ids']}) if matches else sorted({an['segment_id'] for c in cids for an in caps[c]['source_anchors'] if an['segment_id'] in primary_segments})
  row={'id':f'SPEC-{len(docs)+1:02}-{len(rows)+1:03}','lines':[a,b],'unit_kind':kind,'section':title,'clause_identity':content[:180] if kind in ('table_row','section') else f'{title} / L{a}–{b}','capability_ids':cids,'source_segment_ids':sourceids,'registration_ids':sorted(set(matches)),'status':'missing' if missing else ('partial' if ids[45] in cids else 'supported'),'support_boundary':'当前LifeDew比例行缺评分守卫，见GR5-M09-001候选。' if missing else 'supported_static 已读语义；外域/执行/素材边界按正文保留。','evidence_level':'manual_semantic_comparison_with_mechanically_indexed_line_identity'}
  if kind in ('section','format_separator'):row['claim_kind']='navigation_or_structure; not counted as behavior'
  rows.append(row)
  an={'path':str(p),'version':B,'lines':[a,b],'section':title,'clause_id':row['id']}
  for c in cids:caps[c]['spec_anchors'].append(an)
 docs.append({'path':str(p),'version':B,'review_extent':'full','material_availability':'available','evidence_level':'static_semantic_full_document_comparison','unreviewed_intervals':[],'current_effective_supplements':[],'clauses':rows})
# Test vectors have explicit family assignment, no claim they were executed.
testdocs=[]
for spec in d['specifications']:
 if '/test-catalog/' not in spec['path']:continue
 p=Path(spec['path']);rs=spec['read_intervals'];rows=[]
 for a,b,kind,sec,title,content in units(p.read_text().splitlines()):
  if not any(x<=a and b<=y for x,y in rs):continue
  m=re.match(r'\| ([A-Z]{1,2}-?\d+[a-z]?) \|',content)
  nm=p.name
  if 'wp49-51-52' in nm:
   prefix=sec if sec in ('AI','AE','BE','CE') else 'AI'
   nums={'AI':[1,2,3,4,5,6,7],'AE':[6,8,9,10,11,12],'BE':[13,14,15,17],'CE':[18,19,20,21]}.get(prefix,[1,6])
  elif 'wp54-55-56-58' in nm:
   prefix=sec if sec in ('QC','WS','PA','RC') else 'QC'
   nums={'QC':[29,30,31,32],'WS':[33,34,35,36],'PA':[37,38],'RC':[41,42,43,44,45]}.get(prefix,[29,33,37,41])
  elif 'creature-rpg' in nm:nums=[39,40]
  else:nums=[23,24,25,26,27,28]
  cids=[ids[n] for n in nums]
  vector_id=((sec+'-'+m[1]) if sec in ('AI','AE','BE','CE','QC','WS','PA','RC') else m[1]) if m else None
  row={'id':vector_id if m else f'TESTMETA-L{a}','lines':[a,b],'unit_kind':kind,'capability_ids':cids,'source_segment_ids':sorted({an['segment_id'] for c in cids for an in caps[c]['source_anchors'] if an['segment_id'] in primary_segments}),'status':'supported','support_boundary':'supported_static 向量设计与源条件/期望比较；NOT_EXECUTED，无独立动态PASS。'};rows.append(row)
  if m:
   for c in cids:caps[c]['test_vectors'].append({'path':str(p),'version':B,'lines':[a,b],'vector_id':vector_id,'execution_status':'NOT_EXECUTED'})
 testdocs.append({'path':str(p),'version':B,'review_extent':'full' if rs==[[1,len(p.read_text().splitlines())]] else 'partial','read_intervals':rs,'unreviewed_intervals':spec.get('unreviewed_intervals',[]),'scope_boundary':'只审M09具名向量，其余模块向量不在分配范围。','clauses':rows})
for doc in docs:
 doc['current_effective_supplements']=[{'path':x['path'],'version':B,'role':'当前有效数据/注册附表'} for x in docs if x['path']!=doc['path'] and (Path(x['path']).name.split('-')[0:2]==Path(doc['path']).name.split('-')[0:2])]
 if 'wp53-' in doc['path']:doc['current_effective_supplements'].append({'path':'review/wp53-delivery-2026-10-02/revision-v3/entry-coverage-table.md','version':B,'role':'原稿所引行为覆盖附表；全读，无独有遗失事实'})
# Backfill each source segment with concrete reverse clause IDs after semantic allocation.
for sr in source_records:
 for ss in sr['segments']:
  ss['spec_clause_ids']=[c['id'] for doc in docs for c in doc['clauses'] if ss['id'] in c['source_segment_ids']]
  ss['mapping_basis']='人工分段规则比较；精确身份用registration_ledger补至登记体，章节聚合行通过能力族定位，外部消费者只共享投影。'
  ss['specification_status']='missing_candidate' if ids[16] in ss['capability_ids'] else 'supported_static'
policy={'method':'所有判读先于本索引生成：主责源全文逐段、当前合同和原稿完整比对；此脚本只编号/连接行锚，字面命中/计数不构成语义证明。','capability_count_policy':'共享身份只建立一次；capability状态不由注册数/向量数推算。','source_range_policy':'必要外部源仅记录实际投影；完整模块行为不向M08/M01/M11/M12等外域扩张。','formal_units_policy':'每节、段、列表项、表行和本域测试向量有行锚；数据/注册身份附加精细源登记链接，非代码翻译。'}
(O/'source-to-spec.json').write_text(json.dumps({**common,'mapping_policy':policy,'capabilities':list(caps.values()),'source_paths':source_records,'registration_ledger':regs},ensure_ascii=False,indent=2)+'\n')
(O/'spec-to-source.json').write_text(json.dumps({**common,'mapping_policy':policy,'documents':docs,'test_documents':testdocs,'original_draft_disposition':d['original_drafts'],'effective_supplements':d['supplements']},ensure_ascii=False,indent=2)+'\n')
print('wrote',len(caps),'capabilities;',len(regs),'registrations;',len(docs),'formal docs;',sum(len(x['clauses']) for x in docs),'formal clause units;',sum(len(x['clauses']) for x in testdocs),'test units')
print('unmapped registration bodies',[x['id'] for x in regs if not x['semantic_segment_ids']])
print('missing exact-name formal appearances',[(x['id'],x['group'],x['source_key']) for x in regs if not x['spec_anchors']])
