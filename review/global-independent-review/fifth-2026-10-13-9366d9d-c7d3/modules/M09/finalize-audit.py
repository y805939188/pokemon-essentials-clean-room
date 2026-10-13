"""Normalize audit references and close metadata after manual semantic review.
No reference code, behavior model, game data compilation or runtime is executed.
"""
from pathlib import Path
import json,collections,re
O=Path(__file__).parent;R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials');F='deliverables/final-specification-set/'
def read(n):return json.loads((O/n).read_text())
def write(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
d=read('reading-coverage.json');V=d['source_baseline']['commit'];B=d['specification_baseline']['commit']
def merge(rs):
 out=[]
 for a,b in sorted(rs):
  if out and a<=out[-1][1]+1:out[-1][1]=max(out[-1][1],b)
  else:out.append([a,b])
 return out
def gaps(rs,n):
 out=[];last=0
 for a,b in rs:
  if a>last+1:out.append([last+1,a-1])
  last=max(last,b)
 if last<n:out.append([last+1,n])
 return out
def adddoc(path,rs,note,kind='specifications'):
 row=next((x for x in d[kind] if x['path']==path),None)
 if row is None:row={'path':path,'version':B,'material_availability':'available'};d[kind].append(row)
 n=len(Path(path).read_text().splitlines());rs=merge(row.get('read_intervals',[])+rs);row.update(total_lines=n,read_intervals=rs,semantic_compared_intervals=rs,unreviewed_intervals=gaps(rs,n),review_extent='full' if rs==[[1,n]] else 'partial',evidence_level='static_semantic_consumer_projection',note=note)
def addsrc(path,rs,entry,note,mp):
 row=next(x for x in d['sources'] if x['path']==path)
 row['semantic_segments'].append({'line_ranges':rs,'entry_points':entry,'rules_and_comparison':note,'spec_mapping':mp,'comparison_result':'supported_static_dependency_projection','boundary':'只核M09所需消费者，完整外域仍由其主责审查。'})
 merged=merge(row.get('read_intervals',[])+rs);row['read_intervals']=merged;row['semantic_compared_intervals']=merged;row['unreviewed_intervals']=gaps(merged,row['total_lines'])
addsrc('Data/Scripts/011_Battle/003_Move/010_MoveEffects_Healing.rb',[[637,695]],'灭亡歌/同命条款消费者','灭亡歌针对AllBattlers逐目标写4与来源；同命User只写整体标志，逐目标条款正常不被调用，世代7连续限制在整体门。','WP54§6')
addsrc('Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb',[[177,185]],'BothSides默认目标数收尾','侧类未设数量，沿默认0；全场成员目标与双侧无目标效果分离。','WP51/52-A目标枚举；WP54条款')
addsrc('PBS/moves.txt',[[3382,3391],[6225,6235]],'同命/灭亡歌目标字段','DESTINYBOND目标User、PERISHSONG目标AllBattlers；同命的逐目标条款不等于默认整招禁止。','WP54§6；WP52-B§4')
adddoc(F+'demo-dx/wp76-facility-content-generation-and-simulation.md',[[1,115],[207,279]],'已在前一阅读阶段核M09模板/名单的编译和消费交界：§5.7/8.4/10.8及默认未引用Fancy；中间生成策略/模拟工具全域属M12，不在M09本轮全部重审。')
adddoc(F+'pokemon-rules/wp46-damage-multihit-and-healing.md',[[40,40],[208,220]],'LifeDew反证所需真实恢复入口；不以实效合同替代AI独立评分门。')
adddoc('CURRENT-DELIVERY.md',[[1,len(Path('CURRENT-DELIVERY.md').read_text().splitlines())]],'首阶段已全文读：仅解释现行接受状态覆盖原稿纯历史PENDING，不重做历史行政验收或援引PASS作本轮证据。','supplements')
for row in d['specifications']:
 n=len(Path(row['path']).read_text().splitlines());row.setdefault('total_lines',n)
 rs=row.get('read_intervals',[])
 if rs==[[1,n]]:row['review_extent']='full';row['unreviewed_intervals']=[]
for row in d['sources'][:51]:
 row['remaining_assigned_semantic_scope']=[]
 for s in row['semantic_segments']:
  note=s.get('rules_and_comparison','')
  if any(x in note for x in ['待核','待续','待跟读','待实效','待读','待全部','待M01']):
   s['initial_read_note']=note
   s['rules_and_comparison']=note+'【最终闭合：所述待查已由当前正文/附表/原稿或必要消费者投影完成；LifeDew与纹理局部缺项单独见GR5-M09-001/002，非全supported。】'
  s['review_status']='reviewed_all_assigned_available_semantics'
  if 'Conversion' in note or '纹理' in note:s['final_comparison']='partial：默认不消费说明正确；未消费评分体+14可选缺项GR5-M09-002。'
  if s.get('lines')==[231,322] and 'Healing.rb' in row['path']:s['final_comparison']='partial：其余已述规则静态支持；LifeDew独立评分门缺漏GR5-M09-001。'
  if '负wins' in note:s['malformed_input_boundary']='正常会话胜场从0递增；直接传负数会产生负下标，当前公式没有下限夹限，不据括号范围要求补造夹限；非法人工输入非默认可达，不另立必修。'
d['scope_completion']={'assigned_primary_source_files':38,'assigned_pbs_files':13,'assigned_available_semantic_review_complete':True,'unread_available_primary_ranges':[],'remaining_required_dependency_review':[],'note':'审查完成不等于全部supported、候选最终确认或动态执行完成。'}
write('reading-coverage.json',d)
s=read('source-to-spec.json');t=read('spec-to-source.json')
# Bring final source projections into the forward map without rerunning semantic inference.
pathrows={x['path']:x for x in s['source_paths']}
allc={x['id']:x for x in s['capabilities']}
for row in d['sources']:
 sr=pathrows[row['path']]
 sr.update({k:row.get(k) for k in ('review_extent','material_availability','unreviewed_intervals','evidence_level','scope_role')})
 # Last three explicit additions are external projections; old segments keep stable IDs.
 for seg in row['semantic_segments'][len(sr['segments']):]:
  idn=f"SRC-{s['source_paths'].index(sr)+1:03}-{len(sr['segments'])+1:03}"
  cids=['M09.FACILITY.CLAUSES'] if 'Healing.rb' in row['path'] or row['path']=='PBS/moves.txt' else ['M09.AI.CANDIDATES','M09.FACILITY.CLAUSES']
  sr['segments'].append({'id':idn,'line_ranges':seg['line_ranges'],'entry_points':seg['entry_points'],'capability_ids':cids,'comparison':seg['rules_and_comparison'],'status':'supported','support_boundary':'supported_static 必要消费者投影；非外域全量审查。','spec_clause_ids':[],'mapping_basis':'最终具名消费者收尾'})
  for c in cids:allc[c]['source_anchors'].append({'path':row['path'],'version':V,'line_ranges':seg['line_ranges'],'segment_id':idn,'entry_points':seg['entry_points']})
 for ss,seg in zip(sr['segments'],row['semantic_segments']):
  ss['final_comparison']=seg.get('final_comparison',seg.get('comparison_result','supported_static'))
# Optional omission belongs to one local body; do not label the default action wrong.
c=allc['M09.AI.TYPE_ABILITY_VALUE'];c['status']='partial';c['related_findings']=['GR5-M09-002'];c['support_boundary']='supported_static 默认候选不消费纹理目标体、其它已述类型/能力估值；纹理未消费体的+14局部规则可选补全，见P3候选。'
for doc in t['documents']:
 for clause in doc['clauses']:
  if doc['path'].endswith('wp52-a-generic-numerical-and-status-evaluation.md') and clause['lines'][0]==215:
   clause.update(status='partial',related_findings=['GR5-M09-002'],support_boundary='默认User不消费正确；局部评分体+14未承接，可选补全。')
# Register manual final-binding judgments, based on dispatcher semantics already read.
judgments={
'REG-0495':('superseded','被REG-0497对同效果同族后写覆盖；真实最终评分读EchoedVoice，不保留前一FuryCutter评分。'),
'REG-0497':('effective','同键后写覆盖REG-0495；当前WP52-B已明确。'),
'REG-0548':('copy_source_absent_no_write','本目标评分族没有RemoveProtectionsBypassSubstitute源键；不覆盖REG-0547已有RemoveProtections。'),
'REG-0737':('copy_source_absent_no_write','Mimic评分实际在目标族，本整体族复制缺源；不产生Sketch整体评分。'),
'REG-0745':('copy_source_absent_no_write','SwitchOutUserDamagingMove评分在整体族，本目标族缺源；保留REG-0744已有Parting降阶评分。')}
for r in s['registration_ledger']:
 if r['id'] in judgments:r['final_binding_status'],r['final_binding_judgment']=judgments[r['id']]
 elif r['operation']=='copy':r['final_binding_status']='copy_with_existing_source_in_this_group';r['final_binding_judgment']='逐体复核的同族复制；具体供给/目的身份见本行及当前附表。'
 elif r['operation']=='addIf':r['final_binding_status']='conditional_fallback';r['final_binding_judgment']='直接键未找到才按条件登记序取首个匹配；两组资格清单与18类型映射已逐项读。'
 else:r['final_binding_status']='effective_direct_registration'
 if r['source_key']=='SetUserTypesToUserMoveType' and r['group']=='MoveEffectAgainstTargetScore':r['related_findings']=['GR5-M09-002'];r['status']='partial';r['default_consumer']='User零目标，不消费本体；可选完整接口缺项。'
 if r['source_key']=='HealUserAndAlliesQuarterOfTotalHP' and r['group']=='MoveEffectAgainstTargetScore':r['related_findings']=['GR5-M09-001'];r['status']='missing'
# Avoid repeating the same long anchor objects thousands of times; all IDs resolve to exact path/version/range below or in reverse map.
for cap in s['capabilities']:
 cap['source_segment_ids']=sorted({a['segment_id'] for a in cap.pop('source_anchors')})
 cap['spec_clause_ids']=sorted({a['clause_id'] for a in cap.pop('spec_anchors')})
 cap['test_vectors']=list({(a['path'],a['vector_id']):a for a in cap['test_vectors']}.values())
s['anchor_resolution']={'source_segment_ids':'source_paths[].path/version + source_paths[].segments[].id/line_ranges/entry_points','spec_clause_ids':'spec-to-source.json documents[].path/version + clauses[].id/lines/section','registration_ids':'registration_ledger[].id/path/version/lines/group/source_key/copy_destination_keys'}
s['validation_notes']=['注册索引曾将续行copy延伸至下一登记，最终改为按实际外层结束行界定并复核；当前没有AI/Handlers等误抽目的键。','786为本轮实读文件中的登记调用数量，仅索引完整性计数，绝不作为语义完成证明。','行为结论来自reading-coverage逐段比较；条款行级链接按已审行为族与具名登记连接，聚合来源不是每个来源都独立证明整条款。']
t['effective_supplements']=d['supplements'];t['dependency_contract_projections']=[x for x in d['specifications'] if x['path'] not in {y['path'] for y in t['documents']+t['test_documents']}]
t['original_draft_disposition']=d['original_drafts'];t['unavailable_material_boundaries']=d['unavailable_material_boundaries']
write('source-to-spec.json',s);write('spec-to-source.json',t)
f=read('findings.json');f['resolved_scope_observations'].append({'topic':'Factory负胜场直接参数','disposition':'no_required_revision','source':'ChooseFoes88–129与完整164行生成函数','current_contract':'WP57§2.1给min(wins div7,7)；正常会话胜场由0递增','reason':'未误加下限夹限；直接绕过正常计数传负值属于非法人工输入，其负下标行为审过但不扩张默认0..7描述为拒绝/夹限保证。'})
write('findings.json',f)
print('normalized sizes',[(n,(O/n).stat().st_size) for n in ['reading-coverage.json','source-to-spec.json','spec-to-source.json']])
