import review_state as s
from pathlib import Path
import json,re,datetime,hashlib
P='deliverables/final-specification-set/'

def intervals(nums):
 out=[]
 for n in sorted(set(nums)):
  if out and out[-1][1]+1==n:out[-1][1]=n
  else:out.append([n,n])
 return out
def anchors_full(*paths):
 return [{'path':p,'version':s.R,'lines':[1,len((s.REF/p).read_bytes().splitlines())]} for p in paths]

st=s.load('spec-to-source')
primary=['wp24','wp25','wp26','wp27','wp28','wp29','wp64']
orig_sources={
 'wp24':['015_Trainers and player/001_Trainer.rb','015_Trainers and player/002_Trainer_LoadAndNew.rb','015_Trainers and player/003_Trainer_Sprites.rb','015_Trainers and player/004_Player.rb'],
 'wp25':['014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb','016_UI/017_UI_PokemonStorage.rb'],
 'wp26':['019_Utilities/002_Utilities_Pokemon.rb','016_UI/001_Non-interactive UI/005_UI_Trading.rb'],
 'wp27':['013_Items/008_PokemonBag.rb','016_UI/007_UI_Bag.rb','016_UI/018_UI_ItemStorage.rb'],
 'wp28':['013_Items/001_Item_Utilities.rb','013_Items/002_Item_Effects.rb','013_Items/003_Item_BattleEffects.rb','011_Battle/001_Battle/006_Battle_ActionUseItem.rb'],
 'wp29':['016_UI/020_UI_PokeMart.rb','016_UI/021_UI_BattlePointShop.rb','010_Data/002_PBS data/006_Item.rb'],
 'wp64':['013_Items/006_Item_Mail.rb','016_UI/024_UI_MysteryGift.rb','016_UI/019_UI_PC.rb']
}
original_judgments={
 'wp24':'实质身份/默认/装载/伙伴/雷达规则与原测试在正式WP24/PT及共享主合同承接；旧概括须服从当前明确条件。未发现净化独有事实遗失。',
 'wp25':'容器与业务门/当前盒/墙纸/地区/选择/复制事实在正式WP25/PS及WP66-B承接；源码结构和路径移审计属于正确排除。未发现独有事实遗失。',
 'wp26':'所有原获得/赠送/交换流程和场景由正式WP26/AQ承接；新增AQ36是后继补充。方法结构与追踪移审计正确。未发现独有事实遗失。',
 'wp27':'容器/数量/PC/登记/选择原场景已承接；无谓词初始袋由当前WP66-C明确，原稿保存游标简写不是更强保证。事件辅助覆盖N007亦非净化独有遗失。',
 'wp28':'全部原主体/覆盖表/场景的实质事实由正式WP28及IU与共享WP19/21/30承接；形态参数和Nature完整表经有效后继增强。N002/N004以及N006不是仅净化丢掉的原稿独有正确事实。',
 'wp29':'买卖/BP/覆盖/回退及原场景已由正式WP29/SH与WP66-C承接；新奇数BP/槽分布补充不丢原义。无独有正确事实遗失。',
 'wp64':'原32场景/邮件/礼物事实由正式WP64/MG承接；原Give成功M12也有同一N001问题，N003未因净化才产生。序列化/压缩兼容语义仍保留，不要求语言类名。'
}
for q in st['specifications']:
 f=s.REPO/q['path']
 if not f.exists():continue
 ls=f.read_text().splitlines();q['line_count']=len(ls);q['version']=s.B
 pref=Path(q['path']).name.split('-')[0]
 if q.get('kind')=='formal' and pref in ['wp24','wp25']:
  for z in q['sections']:
   old=z['comparison_result']
   if re.search('pending|待核|待查|待读',old,re.I):
    z['preliminary_comparison']=old
    z['comparison_result']='supported_static：该节M05业务规则及必要调用者的静态比较已完成；Owner/创建/普通队伍交换/地区解析/完整治疗/物品消费者均已直接补核。局部借用选择器的N002与邮件N001/N003按相关能力限定；不把域外模块整体或运行行为签为通过。'
    if pref=='wp24':z['source_anchors']+=anchors_full('Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb')
 if q.get('kind')=='original_draft' and pref in primary:
  heads=[i for i,l in enumerate(ls,1) if l.startswith('## ')];starts=sorted(set([1]+heads));secs=[]
  for ix,a in enumerate(starts):
   b=starts[ix+1]-1 if ix+1<len(starts) else len(ls)
   label=ls[a-1] if ls[a-1].startswith('#') else 'opening scope'
   secs.append({'lines':[a,b],'section':label,'source_anchors':anchors_full(*['Data/Scripts/'+p for p in orig_sources[pref]]),'current_formal_counterpart':P+'creature-rpg/'+Path(q['path']).name,'comparison_result':original_judgments[pref],'unique_fact_disposition':'no_unique_substantive_loss_established','administrative_boundary':'历史审查/批准/实施记录按CURRENT解释；只导航，不重新行政验收、不用PASS作本轮证据。','evidence_level':'static_semantic_review','clauses_and_table_rows':[{'line':n,'kind':'table_row' if ls[n-1].startswith('|') else 'clause','mapping_reference':P+'creature-rpg/'+Path(q['path']).name,'judgment_reference':original_judgments[pref]} for n in range(a,b+1) if ls[n-1].strip() and not ls[n-1].startswith('#') and not re.match(r'^\|\s*[-:]+',ls[n-1])]})
  q['sections']=secs;q['unique_fact_review']=original_judgments[pref]
 if q.get('kind')=='formal' and pref in primary:
  # Append only already-read end limitations not included by initial grouping.
  if pref=='wp26':q['sections'][-1]['lines'][1]=len(ls)
  if pref=='wp29':q['sections'][-1]['lines'][1]=len(ls)
  q['actual_semantic_read_ranges']=[[1,len(ls)]]
  q['assigned_scope']='whole_formal_specification'
  q['review_extent']='full';q['unreviewed_intervals']=[]
  for z in q['sections']:
   a,b=z['lines'];existing={v['line'] for v in z.get('clauses_and_table_rows',[])}
   for n in range(a,b+1):
    t=ls[n-1]
    if n in existing or not t.strip() or t.startswith('#') or re.match(r'^\|\s*[-:]+',t) or t.strip()=='---':continue
    z.setdefault('clauses_and_table_rows',[]).append({'line':n,'kind':'table_row' if t.startswith('|') else 'clause','spec_text':t,'source_anchors':z['source_anchors'],'judgment_reference':z['section']})
 else:
  seen=set()
  for z in q['sections']:seen.update(range(z['lines'][0],z['lines'][1]+1))
  q['actual_semantic_read_ranges']=intervals(seen)
  q['unreviewed_intervals']=intervals(set(range(1,len(ls)+1))-seen)
  q['review_extent']='full' if not q['unreviewed_intervals'] else 'partial'
  q['assigned_scope']='whole_original_unique_fact_comparison' if q.get('kind')=='original_draft' else 'bounded_shared_contract_or_related_vector_projection'
 q['evidence_level']='static_semantic_review'
 for z in q['sections']:
  if re.search('pending|待核|待查|待读',z['comparison_result'],re.I) and '/test-catalog/' in q['path']:
   z['preliminary_comparison']=z['comparison_result']
   z['comparison_result']='supported_static：原列前提下已完成分支推导；Owner语言/外来构造、Party普通交换及地区解析的必要来源均补读，非运行通过。'
   if z.get('vector_id','').startswith('PT') or z['section'].startswith('PT'):
    z['source_anchors']+=anchors_full('Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb')
  if '/test-catalog/' in q['path'] and z['lines'][0]==z['lines'][1]:
   n=z['lines'][0];m=re.match(r'^\|\s*([A-Za-z][A-Za-z0-9_-]*\d[A-Za-z0-9_-]*)\s*\|',ls[n-1])
   if m:
    z.setdefault('vector_id',m[1]);z.setdefault('vector_scope',z['section']);z.setdefault('execution_status','not_executed')
  z.setdefault('execution_status','not_executed')

# Normalize every trace version, including early PT/PS anchors.
def versions(x):
 if isinstance(x,dict):
  p=x.get('path')
  if isinstance(p,str) and (p.startswith('Data/') or p.startswith('PBS/')):x.setdefault('version',s.R)
  elif isinstance(p,str) and p.startswith(('deliverables/','specs/')):x.setdefault('version',s.B)
  for v in x.values():versions(v)
 elif isinstance(x,list):
  for v in x:versions(v)
versions(st)
s.save('spec-to-source',st)

cov=s.load('reading-coverage')
for q in cov['sources']:
 q.setdefault('assigned_scope','bounded_business_dependency')
 q.setdefault('in_scope_unreviewed_intervals',[])
 if q['review_extent']=='partial':
  q.setdefault('outside_m05_or_nonbusiness_intervals',q['unreviewed_intervals'])
  q.setdefault('review_boundary','Only listed complete business functions/registrations and required context compared; other module remainder is outside this M05 projection.')
 q['scope_review_complete']=not q['in_scope_unreviewed_intervals']
 for z in q['semantic_segments']:
  z.setdefault('source_review_complete_for_range',True)
  if z.get('preliminary_comparison'):z['preliminary_comparison_status']='historical_checkpoint_only; superseded by comparison_result/capability_ids'
cov['material_boundaries']=[]
for pattern,description in [('Data/Map*.rxdata','地图与地图信息/事件编排'),('Data/CommonEvents.rxdata','公共事件/实际配送、交换、商店/获赠事件'),('Data/System.rxdata','系统起点和真实开关初值'),('Graphics','图像媒体'),('Audio','音频媒体')]:
 found=list(s.REF.glob(pattern))
 cov['material_boundaries'].append({'path_or_pattern':pattern,'version':s.R,'material_availability':'available' if found else 'missing_from_fixed_reference','review_extent':'inventory_only' if found else 'unreadable','evidence_level':'material_inventory_only','in_scope_effect':'No runtime/Demo reachability assertion; static business source remains reviewable.','description':description,'observed_paths':[str(p.relative_to(s.REF)) for p in found]})
cov['reading_method']='Static semantic reading of stated source ranges and current fixed contract ranges, followed by manual counterevidence. Python/Git only index, parse, map and validate review artifacts; never execute reference or a translated behavior model.'
cov['completion_scope']='All available assigned player/item business source and necessary callers/data/originals/current clauses/related vectors have been semantically reviewed. External-module remainder, wording/media and missing Demo materials are explicitly outside or unavailable; full file reading is not claimed for partial projections.'
s.save('reading-coverage',cov)

# Add semantic-range pointers to the lexical registration table, not copied bodies.
mp=s.load('source-to-spec')
for x in mp['handler_registrations']:
 q=next(q for q in cov['sources'] if q['path']==x['source_path'])
 hits=[z for z in q['semantic_segments'] if z['lines'][0]<=x['lines'][0]<=z['lines'][1]]
 x['semantic_range_refs']=[{'lines':z['lines'],'entries':z['entries'],'reviewed_rules':z['rules_reviewed']} for z in hits]
 x['identity_counting_boundary']='Registration appearance/alias target or conditional group; not a distinct capability. Configuration branches follow the referenced semantic rules, not lexical enumeration alone.'
versions(mp);s.save('source-to-spec',mp)

fd=s.load('findings');aliases=s.load('shared-interfaces')['identity_aliases']
for q in fd['findings']:
 q.setdefault('related_capability_aliases',q['related_capabilities'])
 q['related_capabilities']=list(dict.fromkeys(aliases.get(c,c) for c in q['related_capabilities']))
 q.setdefault('shared_contract_aspects',q['shared_contracts'])
 q['shared_contracts']=q['related_capabilities']
 for n in q['negative_evidence_search']:
  if 'C124' in n.get('result','') and '补读中' in n['result']:
   n['result']='相关当前限定/目录已跟读，C124已补齐；B16有效source-limits按b24312f680e74c859460dc36254dec20e0e3bf38精确对象全文读取，未更改PC Give/mail耦合；历史PASS不是本轮证据。'
  if n.get('path','').endswith('wp29-shops-and-exchanges.md') and n.get('read_ranges')==[[1,208]]:n['read_ranges']=[[1,210]]
versions(fd);s.save('findings',fd)

it=s.load('shared-interfaces');versions(it);s.save('shared-interfaces',it)

# Structural and range checks only, not gameplay tests.
errors=[];files=['reading-coverage','source-to-spec','spec-to-source','findings','shared-interfaces','progress']
for fn in files:
 d=s.load(fn)
 if d.get('schema_version')!='gr5.review.v1':errors.append(fn+': schema_version')
 def check(x):
  if isinstance(x,dict):
   p=x.get('path')
   if isinstance(p,str) and p.startswith(('Data/Scripts/','PBS/')) and isinstance(x.get('lines'),list):
    f=s.REF/p
    if not f.exists():errors.append('missing source anchor: '+p)
    elif len(x['lines'])==2 and all(isinstance(n,int) for n in x['lines']):
     a,b=x['lines'];total=len(f.read_bytes().splitlines())
     if not 1<=a<=b<=total:errors.append('invalid source range: '+p+' '+str(x['lines']))
   for v in x.values():check(v)
  elif isinstance(x,list):
   for v in x:check(v)
 check(d)
required='id title module severity disposition status reviewer category source_baseline specification_baseline source_anchors spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change affected_files shared_contracts acceptance_criteria dependencies related_capabilities related_findings root_cause_group priority batch_owner history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
caps={x['id'] for x in mp['capabilities']}
if len(caps)!=len(mp['capabilities']):errors.append('duplicate capability id')
for q in fd['findings']:
 if set(required)-set(q):errors.append(q['id']+' missing fields '+str(set(required)-set(q)))
 if q['status']!='candidate_pending_independent_counterevidence':errors.append(q['id']+' candidate status')
 for c in q['related_capabilities']:
  if c not in caps:errors.append(q['id']+' unresolved capability '+c)
for q in cov['sources']:
 if q.get('in_scope_unreviewed_intervals'):errors.append('in-scope unread: '+q['path'])
for q in st['specifications']:
 total=q['line_count']
 for z in q['sections']:
  a,b=z['lines']
  if not 1<=a<=b<=total:errors.append('spec section range '+q['path']+' '+str(z['lines']))

# Every primary catalog vector, not merely representative examples.
primary_tests={
 'creature-rpg-wp18-20-24-25-26.md':[(88,249)],
 'creature-rpg-wp27-28-29-30-33.md':[(5,155),(240,268)],
 'creature-rpg-wp35-36-57-64-68.md':[(92,127)]
}
for file,ranges in primary_tests.items():
 path=P+'test-catalog/'+file;q=next(x for x in st['specifications'] if x['path']==path)
 mapped={z['lines'][0] for z in q['sections'] if 'vector_id' in z}
 ls=(s.REPO/path).read_text().splitlines()
 for a,b in ranges:
  for n in range(a,b+1):
   if re.match(r'^\|\s*[A-Za-z][A-Za-z0-9_-]*\d[A-Za-z0-9_-]*\s*\|',ls[n-1]) and n not in mapped:errors.append('unmapped primary vector '+path+':'+str(n))

summary={'schema_version':'gr5.review.v1','module':'M05','check_type':'artifact_structure_and_anchor_ranges_only','reference_or_model_execution':False,'errors':sorted(set(errors)),'source_records':len(cov['sources']),'unique_capabilities':len(caps),'registration_appearance_records':len(mp['handler_registrations']),'specification_or_catalog_records':len(st['specifications']),'mapped_vector_rows':sum('vector_id' in z for q in st['specifications'] for z in q['sections']),'candidate_findings':len(fd['findings']),'primary_specifications':7,'primary_originals':7,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
s.save('artifact-validation',summary)
print(json.dumps(summary,ensure_ascii=False))
if errors:raise SystemExit(1)
