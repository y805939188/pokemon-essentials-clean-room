from pathlib import Path
import json,hashlib,datetime,shutil
root=Path(__file__).resolve().parents[1]
load=lambda p:json.loads((root/p).read_text())
def write(p,x):
 q=root/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
common=(root/'delegation/prompts/reference_metadata.md').read_text()
def make(name,reference,formal,dependencies=None,note=''):
 for x in reference+formal:x['semantic_status']='UNREAD'
 write('delegation/readsets/'+name+'.json',{'schema':'gr8-first-wave-readset/v1','primary_task':name,'reference':reference,'formal':formal,'dependency_readsets':dependencies or [],'boundary_note':note,'inventory_only':True})
 text=common.replace('reference_metadata',name)+f'\n本任务特别范围：{note}\n依赖读集：{dependencies or []}。这些是内容读取与最终接收依赖，材料已存在时可独立开工；不是等待其它task写正式规格。请实际完整读这些依赖中与本任务规则有关的全部上下文。\n'
 (root/'delegation/prompts'/f'{name}.md').write_text(text)
 wave.append(name)
wave=[]
for name in ['world_full','ui_full','developer_full','pbs_battle','pbs_world','pbs_creature','localization_records','formal_shared','world_activities','reference_metadata']:
 x=load('delegation/readsets/'+name+'.json')
 # Existing domain prompts and exhaustive primary readsets are already frozen.
 wave.append(name)
ref={x['path']:x for x in load('tasks/inventory_denominator/reference-inventory.json')}
formal={x['path']:x for x in load('tasks/inventory_denominator/formal-inventory.json')}
sub=load('tasks/combat_review/subshards.json')
write('delegation/combat-subshards.snapshot.json',sub)
domain=load('delegation/readsets/combat_review.json')
owned={x['path'] for x in domain['reference']};seen=set();fmseen=set()
for s in sub['subshards']:
 primary=[ref[p] for p in s['reference_primary'] if p in owned]
 external=[p for p in s['reference_primary'] if p not in owned]
 seen.update(x['path'] for x in primary);fmseen.update(s['formal_primary'])
 if s['id']=='COM-CORE':
  write('delegation/readsets/combat_core.running.json',{'current_actual_context':'/root/combat_review','reference':primary,'formal':[formal[p] for p in s['formal_primary']],'dependency_paths':external,'semantic_credit':'Only actual ledger and cross-domain acceptance'})
  continue
 name=s['id'].lower().replace('-','_')
 make(name,primary,[formal[p] for p in s['formal_primary']],['combat_review'],f"精确子范围 {s['id']}，原COM-CORE由实际/root/combat_review继续。跨域依赖路径{external}；接口依赖{s['dependencies']}。全篇共享catalog即使分配另一primary，相关clauses仍须自行核与具名接收。")
left=[ref[p] for p in sorted(owned-seen)]
if left: make('combat_presentation',left,[],['combat_review','ui_full'],'战斗域原始readset中子分片未列的全部源文件（含Scene presentation），完整读输出请求/输入/动画与UI WP67主合同接合。不得拿静态请求当实际像素/声音观测。')
assert fmseen=={x['path'] for x in domain['formal']}
resource=load('delegation/readsets/preflight_resources.json')
media=[x for x in resource['reference'] if x['path'].startswith('Fonts/') or x['path'].endswith(('.bmp','.sf2','messages_core.dat','Scripts.rxdata'))]
make('resource_media_serialized',media,[],['preflight_resources','kernel_review','world_full','ui_full'],'字体8、SF2、BMP、Scripts.rxdata/Main/messages_core可审全结构与全部消费者。实际二进制程序/IL/shader由/root/preflight_resources继续；其recovered-resource-evidence可按receipt借用（先核身份），恢复不是语义阅读。安全反序列化不得执行不受控对象，所有字段/记录/文字/采样关系完整处置。')
write('delegation/first-wave.json',{'schema':'gr8-first-wave/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_commit':'fd1df570cad987dc3852a3b958f03916e317f7fe','reference_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','dispatchable_now':True,'semantic_status':'NOT_STARTED_OR_PARTIAL_DEPENDENCIES; no PASS implied','collaboration_slots':{'capacity':7,'active_including_root':7},'cli_probe':{'status':'FAILED','reason':'failed to initialize in-process app-server client: Read-only file system (os error 30)','actual_new_cli_review_contexts':0},'jobs':[{'id':n,'prompt':'delegation/prompts/'+n+'.md','readset':'delegation/readsets/'+n+'.json','write_set':'tasks/'+n+'/','state':'PLANNED_NOT_LAUNCHED','requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'Fast off'}} for n in wave],'count':len(wave),'simultaneous_writes':'Each job owns a distinct report directory; source/formal/planning/audit/history remain read-only; root owns public ledgers and commits','launch_method':'Parent should use actual available independent cloud contexts. Local codex exec was tested and is not usable here; no fabricated runnable CLI instructions. All jobs read complete original contract and follow latest cloud path mapping when received.','excludes_running':['inventory_denominator','history_current','preflight_resources','kernel_review','creature_review','combat_review'],'update_started':False})
print(json.dumps({'first_wave':wave,'count':len(wave),'combat_source_leftovers':len(left),'resource_media_files':len(media)},ensure_ascii=False))
