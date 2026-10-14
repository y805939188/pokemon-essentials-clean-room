import datetime, hashlib, json, sys
from pathlib import Path

ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
BASE=ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'
OUT=Path(__file__).parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=json.loads((OUT/'counter.json').read_text())
assert not r['issues']
for q in r['input_files']:
    data=(BASE/q['path']).read_bytes()
    assert len(data)==q['bytes'] and hashlib.sha256(data).hexdigest()==q['sha256']
m=json.loads((BASE/'cloud-sixth-update-handoff-manifest.json').read_text())
fixed=[json.loads(v)for v in(OUT/'fixed-input-byte-validation.jsonl').read_text().splitlines()]
assert len(fixed)==691 and all(q['matches']for q in fixed)
ledger=[{'at':now,'material':'main prompt narrative outside82 JSON blocks','status':'ACTUALLY_READ_COMPLETE_NARRATIVE','range':'all19124characters in two contiguous projected outputs','qualification':'JSON blocks separately parsed/compared; narrative projection excludes full JSON.'}]
for index,q in enumerate(m['normative_records']):
    ledger.append({'at':now,'id':q['id'],'status':'CURRENT_FIELD_PROJECTION_ACTUALLY_READ','fields':['identity_and_verdict.classification','minimum_revision_contract.rule','minimum_revision_contract.root_scope_override','acceptance_and_regression.conditions_and_vectors','dependencies_and_receivers.primary_batch'],'additional_primary_input_decision_fields_read':index<17,'semantic_summary':'Finite rule/scope/acceptance read; seven-group equality, completeness and actual identities independently checked. No full external source reread or behavior execution claimed.'})
ledger.append({'at':now,'material':'sixD evidence layer objects','status':'ACTUALLY_READ','summary':'SOURCE_STATIC/DERIVED_VECTOR; bounded tools and reference/model/host NOT_EXECUTED, no aggregate probe counts promoted.'})
ledger.append({'at':now,'material':'manual28 role and field projection','status':'CHECKED','summary':'A xhigh owncandidate; R ultra WAIT_DEPENDENCY; full14batch+EV equality for both roles; shared narrative already read in main.'})
(OUT/'reading-ledger.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n'for q in ledger))
r.update({'status':'FINAL_HANDOFF_COUNTER_COMPLETE_CURRENT_INPUTS_FROZEN','completed_at':now,'fixed_input_full_byte_checks':{'files':691,'bytes':sum(q['bytes']for q in fixed),'issues':0,'execution_or_new_source_read_credit':0},'seven_groups_complete_nonempty_and_cross_document_equal':65,'current_semantic_projection_records_read':65,'identity_omissions':'28manual entries and116 supplements fixed by root, current identities verified;12administrative identities unified.','template_disposition':'20regex hits:14 futureupdate-root paths,5 futureCLI examples,1 shell redirection. Explicit narrative requires actual path binding before any launch; no fixedA/P identity placeholder or empty mandatory contract.','batch_projection_disposition':'Main batch JSON omits duplicate scope_contracts; all56 IDs locally resolve to the65 complete seven-group records. Manual28 files additionally carry own fullbatch scope_contracts.','remaining':[],'runtime':{'validation_python':sys.version,'validation_script_process_exit':0,'validation_script_sha256':hashlib.sha256((OUT/'check-handoff.py').read_bytes()).hexdigest(),'reference_execution':0,'remote_fetch_by_C':0},'scope_not_promoted':'Git byte identity/transport checks do not grant source semantic or host PASS. Required remain OPEN_NOT_UPDATED; future update NOT_STARTED.'})
(OUT/'counter.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
status={'at':now,'task':'R6-C handoff-final-counter','state':'COMPLETE_FROZEN','pending':0,'input_files':r['input_files'],'normative':65,'required':56,'optional':8,'withdrawn':1,'float_facet':1,'policy':7,'limits':14,'unique_primary_batches':14,'conflicts':24,'formal_paths':54,'manual_entries':28,'EV_actual_A_byte_checks':115,'actual_tree_mode_blob_checks':7833,'fixed_input_byte_checks':691,'unresolved':[],'source_execution':0,'public_mutations':0,'actual_model_effort_tier_speed_uuid':'UNVERIFIED','canonical_task_name':'/root/combat_review'}
(OUT/'task-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
report='''# R6-C 最终handoff独立反证

当前输入核验已冻结，pending0。MainPrompt1,966,897 bytes、manifest15,094,661 bytes，准确SHA见counter/task-status。65条裁决56required/8optional/1撤销，Float1/policy7/limits14分列；14唯一主批、54正式路径、24冲突对及28未启动A/R入口一致。

正文非JSON说明全文读完；65条当前rule/scope/acceptance/primary字段投影实际阅读，首次截断K003/B001/B002已另完整补读。七组解析/精确比对且mandatory关键字段非空。C001仅本handler false、C002慢菜单/快已登记执行与WP40主定位、AN007只近似默认点必修、六D证据层保留纠正。UI-PARTY004撤销不入主批，C_AF001仅并F-V001。

115个EV恢复展开真实A commit及完整report path，逐对象完整bytes/SHA/blob核验一致。7833载荷实际tree/path/mode/blob一致；另外691源/正式/补充/行政载荷53,659,416字节完整读取作身份核验，不新增语义全文或执行credit。A3541/652548542、P3601/660631471的完整远端readback与manifest逐身份相等；这一远端fullread由root执行，C没有独立重fetch全包。

28入口bytes/SHA/blob/mode/type与116补充mode/type/仓库字段缺项已由root修订，12行政身份已统一，本次最新整集重验无差异。Prompt/入口自身份完整，最终handoff commit/tree由外部B发布回执绑定，未造递归selfhash。

20模板regex命中为14未来工作根、5示例命令和1重定向，正文明确启动前核定实际路径/allowlist/candidate。不是未展开事实合同或已存在身份。28入口NOT_STARTED，审者先WAIT_DEPENDENCY等待真实candidate；示例未执行。主批不重复前文65合同，但56ID均在同Prompt完整七组内可恢复；各手动入口还带本批fullscope。

最初缺mode schema KeyError与日志限制、批次全dict比较重复scope省略的格式误报、截断投影补读均保留，不记源/规格缺陷。只写本目录，不新审源、不参考/模型/host执行。后继B实际发布/完整读回仍由root确认，本counter不提前授发布PASS。
'''
(OUT/'report.md').write_text(report)
(OUT/'validation-corrections.json').write_text(json.dumps({'at':now,'attempt1':'KeyError supplement mode, before inner logs persisted. Outer failed tool invocation preserved; no fabricated per-command times.','attempt2':'Wholebatch dict comparison flagged omitted duplicate scope_contracts; remainingfields identical and local65 complete records satisfy56 fullscopes, corrected parser.','input_revisions':'Initial9.279MB not final closure; latest15.094661MB verified.','read_projection':'Initial17 output clipped; K003/B001/B002 complete bounded re-emission.','freezer_attempt1':'Inline finalizer syntax error before any code/mutation; corrected saved script.','source_execution':0},ensure_ascii=False,indent=2)+'\n')
files=[]
for path in sorted(OUT.rglob('*')):
    if not path.is_file()or path==OUT/'manifest.json':continue
    raw=path.read_bytes();files.append({'path':str(path.relative_to(ROOT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(OUT/'manifest.json').write_text(json.dumps({'at':now,'files':files,'self':'Excluded selfhash; finalB Git tree externally binds complete directory','file_count_including_self':len(files)+1,'pending':0},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'frozen_at':now,'input_sizes':[q['bytes']for q in r['input_files']],'input_sha256':[q['sha256']for q in r['input_files']],'counter_files':len(files)+1,'pending':0,'issues':0,'EV':115,'treechecks':7833,'fixed_bytechecks':691,'fixed_bytes':sum(q['bytes']for q in fixed)},ensure_ascii=False))
