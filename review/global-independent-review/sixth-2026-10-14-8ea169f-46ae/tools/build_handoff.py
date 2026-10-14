"""Generate the complete Chinese handoff only with actual frozen core and publication objects."""
import argparse,datetime,hashlib,json,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1];REPO=ROOT.parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--publication',required=True);a=ap.parse_args()
def get(p):return json.loads((ROOT/p).read_text())
def put(p,x):(ROOT/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def g(*args):return subprocess.check_output(['git',*args],cwd=REPO)
core=get('publication/core-binding.json');P=a.publication
assert len(P)==40 and g('cat-file','-t',P).strip()==b'commit'
Ptree=g('rev-parse',P+'^{tree}').decode().strip()
Pdir=g('rev-parse',P+':'+str(ROOT.relative_to(REPO))).decode().strip()
readback=get('publication/core-A-retry01/readback.json')
assert readback['commit']==core['core_commit'] and readback['all_full_bytes_match']
records=get('findings/normative-records.json');batches=get('handoff/batch-assignment.json')
fixed=get('control/fixed-inputs.json');coverage=get('coverage/final-coverage.json')
evidence=get('findings/evidence-binding-index.json')
aliases=get('findings/aliases-and-tombstones.json');policies=get('findings/policy-records.json');limits=get('findings/limit-records.json')
assert len(records)==65 and policies['count']==7 and limits['count']==14
source=get('coverage/reference-payloads-current.json');formal=get('coverage/formal-payloads-current.json')
supplements=get('tasks/R6-H/subtasks/supplement-inventory/effective-supplement116.json')
blobmap={x['path']:x for x in get('inventory/workspace-tracked.json')}
for x in supplements:
 if x['path'] in blobmap:
  x['git_blob']=blobmap[x['path']]['git_blob'];x['workspace_tree']=fixed['workspace_tree']
 x['purpose_and_reading_scope']=x.get('inspection',x.get('use'))
manifest={
 'schema':'pokemon-clean-room.r6-update-handoff.v1','created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'fixed_project_inputs':fixed,'r6_core':core,'r6_report_publication':{'commit':P,'workspace_tree':Ptree,'report_directory_tree':Pdir,'report_root':str(ROOT.relative_to(REPO))},
 'handoff_self_binding':'external final publication receipt and final chat bind this file and prompt; no recursive self-hash',
 'source_materials':source,'formal_materials':formal,'effective_supplement_materials':supplements,
 'fixed_history_and_admin_payload_registry':get('tasks/R6-H/payload-identity-and-reading-registry.json'),
 'report_core_full_remote_payload_identities':readback['entries'],
 'reading_and_bidirectional_coverage':coverage,'matrix_catalog':get('coverage/matrix-catalog.json'),
 'full_structure_block_ledger':{'path':'coverage/global-reverse-block-index.json','commit':core['core_commit'],'finite_blocks':20379,'complete_range_and_identity_counter':'tasks/R6-K/global-coverage-counter/report.md'},
 'normative_records':records,'classification_counts':get('findings/adjudication-counts.json'),
 'optional_records':[x for x in records if x['identity_and_verdict']['classification']=='optional'],
 'no_required_revision_records':[x for x in records if x['identity_and_verdict']['classification']=='no_required_revision'],
 'optional_facets':get('findings/optional-facets.json'),'policy_records':policies,'limit_records':limits,
 'aliases_tombstones_and_accepted_negative_hypotheses':aliases,'evidence_binding_index':evidence,
 'accepted_facts':{'combat_no_target_reflection':get('tasks/R6-C/accepted-facts.json'),'phone_current_contract':get('tasks/R6-O/phone-recheck.json'),
                  'data_accepted_rules':'tasks/R6-D source-to-spec-matrix.jsonl and full consumer/rule catalogs at frozen core',
                  'legacy_profile_facts':'tasks/R6-B compat-unit-forward.json / compat-field-index.json / semantic-notes.md at frozen core'},
 'batch_contracts':batches,'dependency_graph':get('handoff/dependency-graph.json'),'file_conflict_graph':get('handoff/file-conflict-graph.json'),
 'task_register':get('control/task-register-current.json'),'execution_phases':get('execution-evidence.json'),
 'historical_qualification':{'R1':'original WP scopes; no invented total','R2':{'controls':229,'batches':21,'exact_owner_contributions':341},
  'R3':{'controls':23,'standards':76,'M09_optional_historical_U08_not_started':True,'M02_no_required':True},
  'R4':{'current_controls':17,'current_standards':76,'B5_controls':16,'B5_standards':75,'summary_residue_only':True},
  'R5':{'closed_required':92,'P2':51,'P3':41,'open':0,'optional':7,'no_required':7,'independent_policy':6,'limits':13,
   'native':410,'schema':568,'additional':158,'shared_receipts':21,'dependency_receipts':18,'solewriters':85,'original_contributions':262,'admin_transfer':6,'corrections':3},
  'scope_source':'tasks/R6-H/report.md and complete fixed-object projections at frozen core; old FAIL/MISMATCH/LF errata retained'},
 'state_semantics':{'review':'COMPLETE_FINITE_STATIC_SCOPE_WITH_REQUIRED_REVISIONS','required':'OPEN_NOT_UPDATED','optional':'NOT_AUTOMATICALLY_AUTHORIZED',
  'policy':'NOT_SELECTED','limit':'FINITE_STATIC_AVAILABLE_REVIEWED_RUNTIME_OR_METADATA_UNKNOWN',
  'candidate_PASS_is_not_integrated_PASS':True,'integrated_PASS_is_not_formal_acceptance':True,'acceptance_is_not_CLOSED_before_dependencies':True},
 'update_started':False,'update_status':'UPDATE_NOT_STARTED'}
put('cloud-sixth-update-handoff-manifest.json',manifest)

draft=ROOT/'tasks/R6-O/handoff-contract-draft/preamble.md'
assert draft.is_file(),'independent Chinese contract draft must be received'
intro=draft.read_text()
binding=['# 第六轮云端有限整改完整中文启动合同','',
 '本文件是供用户另行手动启动的新任务合同。当前独立review与交接准备已完成，云端update尚未启动。请把本文件全文提交给后续任务；不可只复制ID表、链接或未展开模板。',
 '', '## 实际冻结与发布绑定','',
 '| 对象 | 准确身份 |','| --- | --- |',
 '| 正式输入main | `'+fixed['main']+'` |',
 '| workspace/formal tree | `'+fixed['workspace_tree']+'` / `'+fixed['formal_tree']+'` |',
 '| 准确delivery lightweight tag | `'+fixed['delivery_tag']+'` → 固定main，保持原指向 |',
 '| R commit/tree | `'+fixed['reference_commit']+'` / `'+fixed['reference_tree']+'` |',
 '| R6 semantic core commit/workspace tree | `'+core['core_commit']+'` / `'+core['core_workspace_tree']+'` |',
 '| R6 core report-directory tree | `'+core['core_report_directory_tree']+'` |',
 '| R6 report publication commit/workspace tree | `'+P+'` / `'+Ptree+'` |',
 '| R6 publication report-directory tree | `'+Pdir+'` |',
 '| report root | `'+str(ROOT.relative_to(REPO))+'` |',
 '| 本地项目 / origin | `'+str(REPO)+'` / `y805939188/pokemon-essentials-clean-room` |',
 '| 本地R / 来源 | `'+str(REPO/'reference/pokemon-essentials')+'` / `Maruno17/pokemon-essentials` |',
 '', '本机绝对路径是固定恢复入口，云端实际挂载/checkout路径另记，不伪称相同。P是报告发布身份，不替代固定main。交接自身commit/tree由外部最终发布回执绑定；本文件不能包含自己的未知最终对象身份。',
 '', '核心报告全部'+str(readback['files'])+'载荷/'+str(readback['bytes'])+'字节已完整远端对象读回，比对bytes/SHA256/Git blob与目录tree一致。首次推送120s超时和先行读回失败保留；普通重试和成功新记录不覆盖失败。后继handoff自身仍须完整读回。', '',intro]
body=binding+['', '## 裁决与完整逐项合同','',
 '规范65＝64完整原提案＋1有界精度项，56必修（39P2/17P3）、8可选、1无需修订。浮点递推facet另1；policy7＝原6＋GR6-POL-001，limits14＝L01–L13刷新＋L14。原proposal阶段PENDING/支持意见按生成时点保留，当前identity_and_verdict及非提出者root裁决优先。',
 '', '下列每条均展开身份、双向证据、前提/对照/最小反例/失败前缀、最小修订/保留scope、验收回归、独立裁决及依赖/接收。共同证据ID精确内容位于本节后完整证据身份表，可用固定core Git对象和准确path恢复全部原输出；不能以仅名称/旧PASS/相同blob当新批准。', '']
for x in records:
 body+=['### '+x['id']+' · '+x['identity_and_verdict']['classification']+' · '+(x['identity_and_verdict']['severity'] or '无需级别'),'',
         '```json',json.dumps({k:v for k,v in x.items() if k!='original_full_proposal'},ensure_ascii=False,indent=2),'```','']
body+=['## 共同证据完整绑定','', '下表的数据不是链接集合替代合同：各ID的规则/反例/验收已在上文展开；这里提供原始证据逐载荷身份和固定对象恢复方式。','',
       '```json',json.dumps(evidence,ensure_ascii=False,indent=2),'```','',
       '## 可选方面、政策、限制与撤销','',
       '```json',json.dumps({'optional_facets':manifest['optional_facets'],'policy_records':policies,'limit_records':limits,'aliases_and_tombstones':aliases},ensure_ascii=False,indent=2),'```','',
       '## 14有限候选批次的实际路径与入口','',
       '| 主批 | 必修ID | 作者入口 | 独立审者入口 |','| --- | --- | --- | --- |']
for b in batches['batches']:
 body.append('| '+b['id']+' | '+', '.join(b['required_ids'])+' | '+b['author']['logical_id']+' | '+b['reviewer']['logical_id']+' |')
for b in batches['batches']:
 body+=['', '### '+b['id']+' '+b['title'],'','```json',json.dumps({k:v for k,v in b.items() if k!='scope_contracts'},ensure_ascii=False,indent=2),'```']
body+=['', '## 完整依赖/冲突/唯一接收','', '```json',json.dumps({'first_wave':batches['first_wave_all_independent_candidate_batches'],'first_wave_count':14,
  'unique_primary_batch':batches['unique_primary_batch'],'file_solewriters':batches['formal_file_solewriter'],
  'dependency_graph':manifest['dependency_graph'],'file_conflict_graph':manifest['file_conflict_graph']},ensure_ascii=False,indent=2),'```','',
  '首波14个candidate任务没有跨批作者阻塞边，因为它们都消费已冻结的本轮事实；24个冲突对通过各批mirror和R6-I唯一实际写者处理，不允许并行改正式文件。100节点/110边的候选审查、共享接收、整合独立复验、正式接受/关闭门仍真实阻塞closure。当前协作工具容量4（root占1），未来CLI/cloud实际容量首次核一次，不宣称无限。','',
  '## 真实可用本地CLI启动与查询例','',
  '本机codex-cli 0.162.0-alpha.17.2的help与实际exec/JSON/start/exit已验证；以下是本地CLI入口，没有虚构cloud flags。云端用户在其新任务中提交本完整合同，平台能力/模型未回显记UNVERIFIED。','',
  '```sh','codex exec -C <实际隔离项目路径> -m gpt-6.1-sol -c model_reasoning_effort="xhigh" -c service_tier="default" --json --color never -o <update-root>/logs/R6-U01-A.last.md - < <update-root>/prompts/R6-U01-A.md',
  'codex exec -C <实际隔离项目路径> -m gpt-6.1-sol -c model_reasoning_effort="ultra" -c service_tier="default" --json --color never -o <update-root>/logs/R6-U01-R.last.md - < <update-root>/prompts/R6-U01-R.md',
  'cat <update-root>/task-register.json','tail -n 40 <update-root>/logs/R6-U01-A.stdout.jsonl','tail -n 40 <update-root>/logs/R6-U01-A.stderr.log','codex agents','```','',
  '尖括号是必须先解析并记录的真实目录，不能原样运行。启动前把本批完整逐ID合同、冻结身份、精确read/write集合、替身/依赖/验收、禁止事项和日志要求写成实际prompt文件；将stdout/stderr完整另存，记录真实PID/UTC/exit及thread.started UUID。命令示例不代表任务已经启动，也不保证未来云端安装此CLI。无需检查额度/认证或追查未回显配置。','',
  '## 完成和发布','',
  '逐required ID只允许在独立作者候选、非作者审查、唯一写者实际整合、共享完整文件/所有有效接口、精确历史回归、正式接受均成立后登记CLOSED。关闭分母必须恰为56，不能把可选、政策、限制或旧92计进去；不满足的直接/传递依赖保持OPEN。实际源缺读、材料或身份问题逐依赖登记，不能转为PASS。','',
  '先冻结整改语义core，再由后继有限发布/交接回执绑定实际commit/tree/path/bytes/SHA/blob，普通推送独立修订分支后逐新增载荷完整远端读回。相同输入缓存可以复用，不代语义新读；不递归自哈希、不无尽追加回执。若创建草稿PR则附准确链接，main/tag/force/delete/环境释放仍不在本合同默认授权。','',
  '本报告与交接包原始状态：`UPDATE_NOT_STARTED`；`update_started:false`。只有用户另行手动提交此合同的新任务才记录自己的真实启动状态。','']
(ROOT/'cloud-sixth-update-handoff-prompt.md').write_text('\n'.join(body))
put('handoff/generation-check.json',{'records':len(records),'required':56,'optional':8,'no_required':1,'policy':7,'limits':14,
 'core':core['core_commit'],'publication':P,'unique_primary_assignments':len(batches['unique_primary_batch']),
 'first_wave':14,'prompt_contains_all_65_expanded_records':True,'update_started':False})
print(json.dumps({'prompt_bytes':(ROOT/'cloud-sixth-update-handoff-prompt.md').stat().st_size,
                 'manifest_bytes':(ROOT/'cloud-sixth-update-handoff-manifest.json').stat().st_size,'core':core['core_commit'],'publication':P,'update_started':False}))
