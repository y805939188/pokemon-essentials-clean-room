from pathlib import Path
from collections import Counter
import ast,datetime,difflib,hashlib,json,re,subprocess,sys
ROOT=Path('/workspace/pokemon-essentials-clean-room');OUT=Path(__file__).resolve().parent
OLD='00b45de642f07cee9953e42f04cce9c35d77346f';NEW='9971fe84896786645cdcda3ab45e5caf7785cabc';CORE='77dc1102feb99e1a5cfdcf1933b143e9228bbfbb'
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6';PRE='review/remediation-sixth-20261014-prepare/candidates/R6-U13/'
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
commands=[]
def git(*args):
 p=subprocess.run(['git',*args],cwd=ROOT,capture_output=True)
 commands.append({'argv':['git',*args],'exit':p.returncode,'stderr':p.stderr.decode()})
 if p.returncode:raise RuntimeError(p.stderr.decode())
 return p.stdout
def read(c,p):return git('show',c+':'+p)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def js(c,p):return json.loads(read(c,PRE+'evidence/'+p))
def paths(c,p=PRE):return git('ls-tree','-r','--name-only',c,'--',p).decode().splitlines()
checks={};payloads=[]
for p in paths(NEW):
 b=read(NEW,p);payloads.append({'commit':NEW,'path':p,'entry':git('ls-tree',NEW,'--',p).decode().strip(),**ident(b)})
checks['frozen_tree']=git('rev-parse',NEW+'^{tree}').decode().strip()=='93ebe95d038954fd0dfb14fd07ac2f95a2485baf'
checks['candidate_payload_count_30']=len(payloads)==30
all_delta=git('diff','--name-only',OLD,NEW).decode().splitlines();checks['only_candidate_paths_changed']=all(p.startswith(PRE) for p in all_delta)
mirrors=paths(NEW,PRE+'mirror/');mp='mirror/deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
ma=[]
for p in mirrors:
 ob=read(OLD,p);nb=read(NEW,p)
 ma.append({'path':p,'old':ident(ob),'new':ident(nb),'unchanged':ob==nb})
checks['eight_mirrors_only_sf30_file_changed']=len(ma)==8 and [x['path'] for x in ma if not x['unchanged']]==[PRE+mp]
ob=read(OLD,PRE+mp);nb=read(NEW,PRE+mp);ol=ob.splitlines(keepends=True);nl=nb.splitlines(keepends=True)
indices=[i for i,(x,y) in enumerate(zip(ol,nl),1) if x!=y]
checks['one_physical_line40_only']=len(ol)==len(nl) and indices==[40]
checks['full_other_rows_and_suffix_equal']=nl[:39]==ol[:39] and nl[40:]==ol[40:]
oldsf=ol[39].decode().strip();newsf=nl[39].decode().strip();cols0=oldsf.split('|');cols1=newsf.split('|')
checks['menu_input_output_prefix_preserved']=all(cols1[i].strip().startswith(cols0[i].strip()) for i in [2,3])
checks['normal_control_and_default_scope_restored']=all(t in newsf for t in ['d两会话正常结束后','正常保存→载入','d会话仍为未开始/已结束态','模式统计字段持久','计时起点等运行时刻值的重载语义仍未知','未执行真实保存/载入','e检索固定参考当前默认保存转换集合与注册者','排除插件/动态追加','e当前默认集合无Safari/捕虫专用格式转换','普通载入无针对两会话的专用格式迁移','不外推任意版本/插件或整个存档都无迁移'])
counts=[]
ct=PRE+'mirror/deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md'
cttext=read(NEW,ct).decode()
for g,n in [('QC',49),('WS',36),('PA',32),('RC',29),('SF',40)]:
 text=nb.decode().split('## BP：',1)[0] if g=='SF' else re.search(r'^## '+g+r'：.*?(?=^## |\Z)',cttext,re.M|re.S).group()
 raw=[l for l in text.splitlines() if re.match(r'^\| SF\d' if g=='SF' else r'^\| [QWP]\d',l)];ids=[l.split('|')[1].strip() for l in raw]
 counts.append({'series':g,'raw_count':len(raw),'unique_count':len(set(ids)),'duplicates':{k:v for k,v in Counter(ids).items() if v>1},'expected':n})
checks['independent_raw_counts_and_unique_match']=all(x['raw_count']==x['unique_count']==x['expected'] for x in counts)
verify=read(NEW,PRE+'evidence/verify_candidate.py').decode();module=ast.parse(verify)
fn=next(n for n in module.body if isinstance(n,ast.FunctionDef) and n.name=='catalogue_rows')
assertions=[n.lineno for n in ast.walk(fn) if isinstance(n,ast.Assert)];ret=next(n for n in ast.walk(fn) if isinstance(n,ast.Return))
checks['author_duplicate_assert_before_indexing_static']=min(assertions)<ret.lineno and 'Counter(ids)' in ast.get_source_segment(verify,fn) and 'dict(zip(ids,raw))' in ast.get_source_segment(verify,ret)
tv=js(NEW,'tool-validation.json');checks['factor_constants_and_semantic_nonproof_separate']=tv['arithmetic']=={'1x100_div205':0,'3x100_div205':1,'r0_less_expected30':True} and tv['expected_constants_not_computed']=={'h24_m0_factor':30,'h24_m1_factor':30} and tv['probability_factor_semantics_proved_by_this_tool'] is False
ho=js(OLD,'historical-regression.json');hn=js(NEW,'historical-regression.json')
oldkeys=['input','fixed_historical_files','affected_path_navigation','R3_R4_exact_scopes_read','R2_exact_owner_contribution_bindings_read','R2_B13_controls','R2_B12_qualified_scope_read','denominators_preserved','historical_verdict_transferred','integrated_regression','reference_or_host_execution']
checks['old74_navigation_and_other_qualification_fields_unchanged']=all(ho[k]==hn[k] for k in oldkeys)
r5=[]
for x,y in zip(ho['R5_exact_scopes_read'],hn['R5_exact_scopes_read']):
 b=read(y['source_commit'],y['source_path']);got=ident(b);entry=git('ls-tree',y['source_commit'],'--',y['source_path']).decode().strip();parts=y['pointer'].strip('/').split('/');data=json.loads(b)
 for part in parts:data=data[int(part)] if isinstance(data,list) else data[part]
 r5.append({'id':y['id'],'source_commit':y['source_commit'],'source_path':y['source_path'],'observed':got,'entry':entry,'identity_and_entry_match':all(got[k]==y[k] for k in got) and entry==y['git_entry'],'qualified_scope_unchanged':x['qualified_scope']==y['qualified_scope'],'fixed_record_scope_match':all(data[k]==v for k,v in y['qualified_scope'].items()),'current_check_unchanged':x['current_check']==y['current_check'],'failure_cause_unknown':y['retrieval_transition']['original_failure_cause']=='UNKNOWN_NOT_RECONSTRUCTED','withdraws_absence': 'did not establish path absence' in y['retrieval_note']})
checks['R5_exact_paths_and_scopes_no_backfill']=len(r5)==3 and all(all(x[k] for k in ['identity_and_entry_match','qualified_scope_unchanged','fixed_record_scope_match','current_check_unchanged','failure_cause_unknown','withdraws_absence']) for x in r5)
binder=read(NEW,PRE+'evidence/bind_history.py').decode();checks['wrong_absence_generator_literal_removed']='Original contract path was not present' not in binder and "b=blob(r5_commit,source_path)" in binder
raw0=read(OLD,PRE+'evidence/reading-ledger.jsonl');raw1=read(NEW,PRE+'evidence/reading-ledger.jsonl');append=raw1[len(raw0):];checks['old_79_ledger_prefix_preserved']=raw1.startswith(raw0) and len(raw0.splitlines())==79
lr=[]
for line in append.splitlines():
 row=json.loads(line);b=read(row['commit'],row['path']);piece=b''.join(b.splitlines(keepends=True)[row['start_line']-1:row['end_line']]);got=ident(b)
 lr.append({'record':row,'identity_match':all(got[k]==row[k] for k in ['bytes','sha256']),'entry_match':git('ls-tree',row['commit'],'--',row['path']).decode().strip()==row['git_entry'],'range_hash_match':len(piece)==row['returned_bytes'] and hashlib.sha256(piece).hexdigest()==row['stdout_content_sha256']})
checks['three_new_converter_ledger_records_match']=len(lr)==3 and all(x['identity_match'] and x['entry_match'] and x['range_hash_match'] for x in lr)
manifest=js(NEW,'candidate-manifest.json');checks['candidate_manifest_full_8_identities_match']=all(ident(read(NEW,x['candidate_path']))==x['candidate'] and ident(read(MAIN,x['formal_path']))==x['baseline'] for x in manifest)
spans=[]
for x in manifest:
 a=read(MAIN,x['formal_path']).decode().splitlines();b=read(NEW,x['candidate_path']).decode().splitlines();sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
 for tag,i,j,k,l in sm.get_opcodes():
  if tag!='equal':spans.append({'path':x['formal_path'],'operation':tag,'old_lines':[i+1,j],'new_lines':[k+1,l],'old_text':a[i:j],'new_text':b[k:l]})
checks['changed37_spans_exactly_rebuild']=spans==js(NEW,'changed-spans.json') and len(spans)==37
checks['old_FAIL_report_remains_bound']=ident(read('3ef4854ef43eac92fd1dc57350e4cf6aa160082b','review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/review-report.md'))['git_blob']=='1b64bdb75f8c4c8be5d4c25094acbd0ec0c0133f'
dm=js(NEW,'repair-01/delta-manifest.json');declared={x['path'] for x in dm['changed_payloads_except_this_manifest']};core_delta=set(git('diff','--name-only',OLD,CORE,'--',PRE).decode().splitlines());checks['finite_core_delta_manifest_complete']=declared==core_delta-{PRE+'evidence/repair-01/delta-manifest.json'}
checks['delta_manifest_all_old_new_identities_match']=all(ident(read(NEW,x['path']))==x['after'] and (x['before'] is None or ident(read(OLD,x['path']))==x['before']) for x in dm['changed_payloads_except_this_manifest'])
rb=js(NEW,'repair-01/remote-readback.json');checks['remote_receipt_bound_to_core_29_payloads']=rb['candidate_commit']==CORE and len(rb['verified_payloads'])==29 and all(ident(read(CORE,x['path']))=={k:x[k] for k in ['bytes','sha256','git_blob']} and read(CORE,x['path'])==read(NEW,x['path']) for x in rb['verified_payloads'])
checks['final_only_publication_receipt_added']=git('diff','--name-only',CORE,NEW).decode().splitlines()==[PRE+'evidence/repair-01/remote-readback.json']
result={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(ROOT),'argv':sys.argv,'runtime':sys.version,'candidate_commit':NEW,'prior_candidate':OLD,'checks':checks,'payloads':payloads,'mirror_identities':ma,'single_line_delta_indices':indices,'sf30_before':oldsf,'sf30_after':newsf,'independent_raw_counts':counts,'R5_bindings':r5,'new_author_ledger_rows':lr,'old_qualification_no_delta_keys':oldkeys,'reference_execution':False,'author_script_execution':False,'host_execution':False,'real_save_load':False,'effective_configuration':'UNVERIFIED','commands':commands,'all_checks_pass':all(checks.values())}
(OUT/'independent-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'all_checks_pass':result['all_checks_pass'],'checks':checks,'candidate_payload_count':len(payloads),'mirror_delta_lines':indices,'raw_counts':counts},ensure_ascii=False))
