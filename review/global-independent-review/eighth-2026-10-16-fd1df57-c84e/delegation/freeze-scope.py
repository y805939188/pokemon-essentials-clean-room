from pathlib import Path
import json, hashlib, shutil, datetime, re

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]
INV=ROOT/'tasks/inventory_denominator'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def write(name,x):
 p=ROOT/name; p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def owner(p):
 if p.startswith('Data/Scripts/'):
  q=p.split('/')[2]
  if q.startswith(('001_','002_Save','010_','021_','999_')): return 'kernel_review'
  if q.startswith(('002_Battle','011_','018_')): return 'combat_review'
  if q.startswith(('013_','014_','015_')): return 'creature_review'
  if q.startswith(('007_','016_','017_')): return 'ui_full'
  if q.startswith('020_'): return 'developer_full'
  if q.startswith('012_') and any(x in p for x in ('WildEncounters','EncounterModifiers','RoamingPokemon','DayCare')): return 'creature_review'
  if q.startswith('019_') and 'Utilities_Pokemon' in p: return 'creature_review'
  return 'world_full'
 if p.startswith('PBS/'):
  n=Path(p).name.lower()
  if any(x in n for x in ('pokemon','trainer','encounter','regional','shadow')): return 'pbs_creature'
  if any(x in n for x in ('move','abilit','type','item','battle')): return 'pbs_battle'
  return 'pbs_world'
 if p.startswith('Text_english_core/'): return 'localization_records'
 if p in ('scripts_combine.rb','scripts_extract.rb','townmapgen.html','animmaker.txt','extendtext.txt'): return 'developer_full'
 if p=='mkxp.json': return 'world_full'
 if p.startswith(('Fonts/','Data/')) or p.lower().endswith(('.exe','.dll','.bmp','.sf2')): return 'preflight_resources'
 return 'reference_metadata'
ref=json.loads((INV/'reference-inventory.json').read_text())
formal=json.loads((INV/'formal-inventory.json').read_text())
groups={}
for x in ref:
 x['primary_task']=owner(x['path']);x['semantic_status']='UNREAD';groups.setdefault(x['primary_task'],{'reference':[],'formal':[]})['reference'].append(x)
for x in formal:
 p=x['path']; part=p.split('/')[2]
 if part=='generic-kernel' or '/generic-kernel-' in p: o='kernel_review'
 elif part=='creature-rpg' or '/creature-rpg-' in p: o='creature_review'
 elif part=='combat-requirements' or '/combat-requirements-' in p: o='combat_review'
 elif part=='engine-overworld' or '/engine-overworld-' in p: o='world_full'
 elif part=='user-interface' or '/user-interface-' in p: o='ui_full'
 elif part=='demo-dx' or '/demo-dx-' in p: o='developer_full'
 elif part=='pokemon-rules' or '/pokemon-rules-' in p:
  nums=[int(v) for v in re.findall(r'wp(\d+)',p)]
  if any(v in (43,44,46,48,50,53) for v in nums): o='combat_review'
  elif any(v in (60,61,69,70) for v in nums): o='world_activities'
  else: o='creature_review'
 else: o='formal_shared'
 x['primary_task']=o;x['semantic_status']='UNREAD';groups.setdefault(o,{'reference':[],'formal':[]})['formal'].append(x)
assert sum(len(v['reference']) for v in groups.values())==432
assert sum(len(v['formal']) for v in groups.values())==131
contract=ROOT/'tasks/history_current/contract.md'
assert len(contract.read_bytes())==36653
assert hashlib.sha256(contract.read_bytes()).hexdigest()=='63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b'
shutil.copyfile(contract,ROOT/'inputs/eighth-global-review-prompt.md')
shutil.copyfile(ROOT/'tasks/preflight_resources/contract/review-SKILL.md',ROOT/'inputs/review-SKILL.md')
config={'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'Fast off'},'actual':dict.fromkeys(['model','effort','tier','speed'],'UNVERIFIED')}
for name,g in groups.items():
 write('delegation/readsets/'+name+'.json',{'schema':'gr8-primary-readset/v1','frozen_B8':B8,'frozen_R':R,'inventory_only':True,'primary_task':name,'scope_expansion':'Read all actual definitions, default/alternative records, caller/receiver and consumers; report newly discovered inputs by exact identity. Primary assignment does not prohibit dependency reads.','counts':{k:len(v) for k,v in g.items()},**g})
 prompt=f'''你是第八轮完整独立全局review任务 {name} 的实际新上下文审者。首先逐行完整读取 {ROOT}/inputs/eighth-global-review-prompt.md（36653 bytes SHA256 63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b，已核字节）及 {REPO}/AGENTS.md；不能只用本任务摘要。用户指定最终态修订技能在 {ROOT}/inputs/review-SKILL.md，适用于最终交接正文，不替代审计合同。
固定输入：规格仓库 {REPO}；B8 commit {B8} tree751dfde81048c81390f89a65ca1d1a565ba8e1ca；正式tree f292698cdd4a8e725525a9be6dc34b75faaf151e。只读参考 /workspace/pokemon-essentials commit {R} tree7589c800b61ba13a13040ed0d686979b80a84fd0。云端路径与Mac历史分列。请求 gpt-6.1-sol / ultra / default普速 / Fast off；实际回显缺失逐字段UNVERIFIED，不能用请求认证实际。
精确primary读集 {ROOT}/delegation/readsets/{name}.json。全部库存只是机械冻结，不授语义信用。读集内全部可审文件、结构、formal clause逐项完整读并双向核；补所有真实caller/receiver/default和备选数据/持久化重载/展示链，新增跨域依赖写明待接收，不以现表封闭范围。与其他任务共享文件允许读取，唯一primary按冻结readset；需要拆分请先交完整子集与边界并报root，不遗漏正文data/coverage/test。
唯一写集 {ROOT}/tasks/{name}/；不得改formal、R、planning/audit、历史报告或其他任务目录，不git commit/push，不安装、不用外部生产服务。root独占公共状态/提交。安全隔离检查先读懂依赖；所有原I/O和exitUTC保留，未运行NOT_EXECUTED。UPDATE_NOT_STARTED。
交付 progress.json、identities.json、reading-ledger.json、forward-mapping.json、reverse-mapping.json、interfaces.json、proposals.json 和 review.md。台账具名实际审者、完整连续区间/结构/条款子断言、前提、事实、消费者与源定位；未读和未接收如实非0，不能改标limit。脚本/搜索/同blob/历史PASS不替代实际完整阅读。分类许可/行政/opaque给精确处置理由；其中有效规则不能豁免。
每条疑似提案按完整合同第八节：稳定ID、双向path/commit/tree/blob/bytes/SHA定位、有限前提、普通对照、最小反例输入步骤、源行为/当前断言差异、正常取消失败异常部分提交、负证据范围、影响、最小正确修订、正确保留scope、精确读写/同步/消费者、验收与回归、历史关联。提案非required；须由实际不同非提案者上下文独立反证和root裁决。必要非作者验收不得由角色改名代替。不能复制参考源码到规格/交接，不写新框架。
完成要给精确已读/未读/未接收分母、证据等级及真实配置/执行边界。过程记录开始更新结束UTC、平台真实ID/日志（若未回显UNVERIFIED）。有限任务只交其确切范围，不声称全系统完成。
'''
 p=ROOT/'delegation/prompts'/f'{name}.md';p.parent.mkdir(exist_ok=True);p.write_text(prompt)
write('delegation/scope-freeze.v1.json',{'schema':'gr8-scope-freeze/v1','utc':now,'B8':B8,'R':R,'native_reference_files':432,'formal_files':131,'mechanical_identity_frozen':True,'semantic_denominator_status':'WP/structural/clause and current supplement closure pending named inventory/history tasks; not falsely complete','primary_assignments':{k:{'reference':len(v['reference']),'formal':len(v['formal']),'readset':'delegation/readsets/'+k+'.json','prompt':'delegation/prompts/'+k+'.md','status':'RUNNING' if k in ['kernel_review','creature_review','combat_review','preflight_resources'] else 'PLANNED'} for k,v in groups.items()},'configuration':config,'independent_counterreview':'Each actual new finding must receive a different actual nonauthor context; no self acceptance; slots used as platform permits without arbitrary concurrency cap','update_started':False})
write('progress.json',{'schema':'gr8-progress/v1','utc':now,'status':'RUNNING','startup':'READY_WITH_LIMITS','phase':'Full denominator freeze and parallel semantic review','B8':B8,'R':R,'native_reference_files':432,'formal_files':131,'semantic_completion':'INCOMPLETE','source_and_formal_counts_are':'INVENTORY_ONLY until actual task ledger acceptance','tasks':{x:{'platform_entry':'/root/'+x,'status':'RUNNING','outputs':'tasks/'+x,'configuration':config} for x in ['inventory_denominator','history_current','preflight_resources','kernel_review','creature_review','combat_review']},'planned_primary_tasks':list(groups),'actual_collaboration_capacity':7,'actual_active_collaboration_contexts_including_root':7,'limits':['Cloud local main/origin-main/tag refs absent; fixed HEAD/tree and live remote main/tag verified separately','No Ruby/.NET/Windows media host installed; static readable material remains in review scope','Full current supplement and structural/clause denominator closure is in progress'],'behavior_executions':0,'behavior_status':'NOT_EXECUTED','update_started':False})
write('findings.json',{'schema':'gr8-findings/v1','status':'IN_PROGRESS','proposals':[],'adjudicated_records':[],'required_count':None,'required_count_reason':'No conclusion until actual independent counterreview and coverage acceptance','update_started':False})
print(json.dumps({k:{q:len(z) for q,z in v.items()} for k,v in groups.items()},ensure_ascii=False))
