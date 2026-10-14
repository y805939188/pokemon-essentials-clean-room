import collections, datetime, hashlib, itertools, json, re, subprocess
from pathlib import Path

ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
BASE=ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'
OUT=Path(__file__).parent
OUT.mkdir(exist_ok=True)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
commands=[]; issues=[]
def git(args,cwd=ROOT,binary=False):
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(['git',*args],cwd=cwd,capture_output=True)
    commands.append({'argv':['git',*args],'cwd':str(cwd),'started_at':started,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,'stdout_bytes':len(p.stdout),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr':p.stderr.decode(errors='replace'),'kind':'READ_ONLY_OBJECT_METADATA_OR_BYTES_NOT_SOURCE_EXECUTION'})
    if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace'))
    return p.stdout if binary else p.stdout.decode().strip()
def check(ok,name,**details):
    if not ok:issues.append({'check':name,**details})
def nonempty(x):return x is not None and x!='' and x!=[] and x!={}
prompt_raw=(BASE/'cloud-sixth-update-handoff-prompt.md').read_bytes()
manifest_raw=(BASE/'cloud-sixth-update-handoff-manifest.json').read_bytes()
t=prompt_raw.decode();m=json.loads(manifest_raw)
chunks=re.findall(r'```([^\n]*)\n(.*?)\n```',t,re.S)
jsons=[json.loads(body)for label,body in chunks if label=='json']
prompt_records=jsons[:65]; by={q['id']:q for q in m['normative_records']}
check(len(by)==65 and len(prompt_records)==65,'65_UNIQUE_RECORDS')
check(collections.Counter(q['identity_and_verdict']['classification']for q in by.values())=={'required':56,'optional':8,'no_required_revision':1},'COUNTS_56_8_1')
projection_keys=['identity_and_verdict','bidirectional_evidence','premises_and_counterexample','minimum_revision_contract','acceptance_and_regression','independent_adjudication','dependencies_and_receivers']
for q in prompt_records:
    ident=q['id'];target=by[ident]
    check(all(q[k]==target[k]for k in projection_keys),'PROMPT_MANIFEST_SEVEN_GROUP_EQUAL',id=ident)
    for key in projection_keys:check(nonempty(q.get(key)),'SEVEN_GROUP_NONEMPTY',id=ident,field=key)
    if q['identity_and_verdict']['classification']=='required':
        pre=q['premises_and_counterexample'];rev=q['minimum_revision_contract']
        for name,value in {'source':q['bidirectional_evidence']['source'],'formal':q['bidirectional_evidence']['formal'],'input':pre['input_domain'],'ordinary_control':pre['ordinary_control'],'minimal_counterexample':pre['minimal_counterexample'],'evidence_layers':pre['evidence_levels_and_execution'],'failure_prefix':pre['failure_cancel_partial_commit'],'rule':rev['rule'],'preserve_scope':rev['preserve_correct_scope'],'acceptance':q['acceptance_and_regression']['conditions_and_vectors'],'nonproposer':q['independent_adjudication']['non_proposer_records']}.items():check(nonempty(value),'MANDATORY_FIELD_NONEMPTY',id=ident,field=name)
check(jsons[65]==m['evidence_binding_index'],'FULL_EV_INDEX_EQUAL')
special=jsons[66]
for pkey,mkey in [('optional_facets','optional_facets'),('policy_records','policy_records'),('limit_records','limit_records'),('aliases_and_tombstones','aliases_tombstones_and_accepted_negative_hypotheses')]:check(special[pkey]==m[mkey],'SPECIAL_FULL_CONTRACT_EQUAL',field=pkey)
check(len(m['optional_facets'])==1 and m['policy_records']['count']==7 and m['limit_records']['count']==14,'FACET_POLICY_LIMIT_COUNTS')
batch=m['batch_contracts'];check(len(batch['batches'])==14,'14_BATCHES')
prompt_batches=jsons[67:81]
check(prompt_batches==[{k:v for k,v in q.items()if k!='scope_contracts'}for q in batch['batches']],'ALL14_BATCH_FIELDS_EQUAL')
for item in batch['batches']:
    check({q['id']for q in item['scope_contracts']}==set(item['required_ids']),'BATCH_SCOPE_IDS_EXACT',batch=item['id'])
    for q in item['scope_contracts']:
        check(all(q[k]==by[q['id']][k]for k in projection_keys),'BATCH_FULL_SCOPE_EQUALS_LOCALLY_EXPANDED_RECORD',id=q['id'])
required={q['id']for q in by.values()if q['identity_and_verdict']['classification']=='required'}
assigned=[k for q in batch['batches']for k in q['required_ids']]
check(set(assigned)==required and len(assigned)==56 and len(set(assigned))==56,'UNIQUE56_PRIMARY')
paths={path for q in batch['batches']for path in q['candidate_formal_paths']}
check(len(paths)==54,'54_PATHS')
expected={tuple(sorted([a['id'],c['id']])):sorted(set(a['candidate_formal_paths'])&set(c['candidate_formal_paths']))for a,c in itertools.combinations(batch['batches'],2)if set(a['candidate_formal_paths'])&set(c['candidate_formal_paths'])}
fg=m['file_conflict_graph'];actual={tuple(sorted([e['from'],e['to']])):sorted(e['paths'])for e in fg['edges']}
check(actual==expected and len(actual)==24,'24_CONFLICTS_EXACT')
last=jsons[81]
for key,value in [('first_wave',batch['first_wave_all_independent_candidate_batches']),('first_wave_count',batch['first_wave_count']),('unique_primary_batch',batch['unique_primary_batch']),('file_solewriters',batch['formal_file_solewriter']),('dependency_graph',m['dependency_graph']),('file_conflict_graph',m['file_conflict_graph'])]:check(last[key]==value,'FULL_RECEIVER_GRAPH_EQUAL',field=key)
check(not m['update_started'] and m['update_status']=='UPDATE_NOT_STARTED','NO_UPDATE_STARTED')
for q in batch['batches']:
    check('NOT_STARTED'in q['state'],'BATCH_NOT_STARTED',batch=q['id'])
    for role in ['author','reviewer']:
        check('NOT_STARTED'in json.dumps(q[role]),'FUTURE_ROLE_NOT_STARTED',batch=q['id'],role=role)
check('R6-UI-PARTY-004'not in assigned and by['R6-UI-PARTY-004']['identity_and_verdict']['classification']=='no_required_revision','WITHDRAWN_STAYS_EXCLUDED')
check('AF001'not in assigned and 'C AF001'in by['GR6-F-V001']['minimum_revision_contract']['root_scope_override'],'AF_ONLY_FV001')
core=m['r6_core']['core_commit'];pub=m['r6_report_publication']['commit'];formal=m['fixed_project_inputs']['main'];ref=m['fixed_project_inputs']['reference_commit']
for commit,tree,dir_tree,cwd,report in [(core,m['r6_core']['core_workspace_tree'],m['r6_core']['core_report_directory_tree'],ROOT,str(BASE.relative_to(ROOT))),(pub,m['r6_report_publication']['workspace_tree'],m['r6_report_publication']['report_directory_tree'],ROOT,str(BASE.relative_to(ROOT))),(formal,m['fixed_project_inputs']['workspace_tree'],m['fixed_project_inputs']['formal_tree'],ROOT,'deliverables/final-specification-set'),(ref,m['fixed_project_inputs']['reference_tree'],None,ROOT/'reference/pokemon-essentials',None)]:
    check(git(['rev-parse',commit+'^{tree}'],cwd)==tree,'ACTUAL_COMMIT_TREE',commit=commit)
    if report:check(git(['rev-parse',commit+':'+report],cwd)==dir_tree,'ACTUAL_DIRECTORY_TREE',commit=commit,path=report)
check(git(['rev-parse',m['fixed_project_inputs']['delivery_tag']])==formal,'DELIVERY_TAG_FIXED')
evchecks=[]
for ident,q in m['evidence_binding_index'].items():
    path=str(BASE.relative_to(ROOT))+'/'+q['path'];expected_recovery='git show '+core+':'+path
    check(q['recovery']==expected_recovery and q['commit']==core,'EV_ACTUAL_A_PATH_EXPANDED',id=ident)
    data=git(['show',core+':'+path],binary=True)
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    ok=len(data)==q['bytes']and hashlib.sha256(data).hexdigest()==q['sha256']and blob==q['git_blob']
    check(ok,'EV_ACTUAL_OBJECT_BYTES_IDENTITY',id=ident,path=path)
    evchecks.append({'id':ident,'path':path,'commit':core,'bytes':len(data),'identity_matches':ok,'semantic_source_read_credit':0})
treescache={}
def tree(commit,cwd=ROOT):
    key=(commit,str(cwd))
    if key not in treescache:
        data=git(['ls-tree','-r','-z',commit],cwd,binary=True);rows={}
        for row in data.split(b'\0'):
            if not row:continue
            meta,path=row.split(b'\t',1);mode,typ,obj=meta.decode().split();rows[path.decode()]={'mode':mode,'type':typ,'git_blob':obj}
        treescache[key]=rows
    return treescache[key]
payload_count=0;fixed_byte_checks=[]
for key in ['source_materials','formal_materials','effective_supplement_materials','report_core_full_remote_payload_identities','report_publication_full_remote_payload_identities','fixed_history_and_admin_payload_registry']:
    for q in m[key]:
        cwd=ROOT/'reference/pokemon-essentials'if key=='source_materials'else ROOT
        commit=q.get('commit',core);path=q['path'];item=tree(commit,cwd).get(path)
        check(item is not None,'PAYLOAD_ACTUAL_PATH_EXISTS',family=key,path=path,commit=commit)
        if item:
            check(nonempty(q.get('mode'))and nonempty(q.get('type')),'PAYLOAD_MODE_TYPE_OMITTED',family=key,path=path)
            check(item['git_blob']==q['git_blob']and ('mode'not in q or item['mode']==q['mode']),'PAYLOAD_MODE_BLOB_MATCH',family=key,path=path)
            if key in ['source_materials','formal_materials','effective_supplement_materials','fixed_history_and_admin_payload_registry']:
                data=git(['show',commit+':'+path],cwd,binary=True)
                ok=len(data)==q['bytes'] and hashlib.sha256(data).hexdigest()==q['sha256']
                check(ok,'FIXED_INPUT_FULL_BYTES_SHA256_MATCH',family=key,path=path)
                fixed_byte_checks.append({'family':key,'path':path,'commit':commit,'bytes':len(data),'matches':ok,'semantic_reading_credit':0,'source_execution':0})
        payload_count+=1
receipts=[]
for rel,count,bytecount,commit in [('publication/core-A-retry01/readback.json',3541,652548542,core),('publication/report-P/readback.json',3601,660631471,pub)]:
    raw=(BASE/rel).read_bytes();r=json.loads(raw)
    check(r['commit']==commit and r['files']==count and r['bytes']==bytecount and r['all_full_bytes_match']==True,'REMOTE_READBACK_RECEIPT_MATCH',path=rel)
    check(len(r['entries'])==count,'READBACK_ENTRY_COUNT',path=rel)
    mk='report_core_full_remote_payload_identities'if commit==core else'report_publication_full_remote_payload_identities'
    actual_by={q['path']:q for q in r['entries']}
    check(set(actual_by)=={q['path']for q in m[mk]},'MANIFEST_RECEIPT_PATHS_EXACT',family=mk)
    for q in m[mk]:check(all(q[k]==actual_by[q['path']][k]for k in ['commit','workspace_tree','directory_tree','bytes','sha256','git_blob','mode']),'MANIFEST_RECEIPT_IDENTITY_EXACT',family=mk,path=q['path'])
    receipts.append({'path':rel,'sha256':hashlib.sha256(raw).hexdigest(),'files':count,'bytes':bytecount,'all_full_bytes_match':r['all_full_bytes_match'],'qualification':'Owner actual remote readback receipt; C does not claim independently fetching remote bytes.'})
manual=[]
for q in m.get('manual_entry_prompts',[]):
    path=BASE/q['path'];raw=path.read_bytes();text=raw.decode();logical=q['logical_id'];role=logical[-1];bid=logical[:-2];target=next(v for v in batch['batches']if v['id']==bid)
    data=[json.loads(body)for label,body in re.findall(r'```([^\n]*)\n(.*?)\n```',text,re.S)if label=='json']
    check(len(data)==2 and data[0]==target and data[1]==m['evidence_binding_index'],'MANUAL_FULL_BATCH_EV_EQUAL',id=logical)
    check(q['state']=='NOT_STARTED' and '该入口未启动'in text and 'UPDATE_NOT_STARTED'in text,'MANUAL_NOT_STARTED',id=logical)
    check(core in text and pub in text,'MANUAL_FIXED_A_P',id=logical)
    check(('xhigh'if role=='A'else'ultra')in text.split('# 第六轮云端有限整改完整中文启动合同')[0],'MANUAL_ROLE_EFFORT',id=logical)
    if role=='R':check('WAIT_DEPENDENCY'in text.split('# 第六轮云端有限整改完整中文启动合同')[0],'REVIEWER_REAL_CANDIDATE_DEPENDENCY',id=logical)
    missing=[k for k in ['bytes','sha256','git_blob','mode','type']if k not in q]
    check(not missing,'MANUAL_ENTRY_PAYLOAD_IDENTITY_MISSING',id=logical,missing=missing)
    if not missing:check(q['bytes']==len(raw)and q['sha256']==hashlib.sha256(raw).hexdigest()and q['git_blob']==hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),'MANUAL_ENTRY_PAYLOAD_IDENTITY_MATCH',id=logical)
    manual.append({'logical_id':logical,'path':str(path.relative_to(ROOT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),'state':q['state'],'metadata_missing':missing})
check(len(manual)==28,'28_MANUAL_ENTRIES')
q=m['complete_chinese_prompt_payload']
check(q['bytes']==len(prompt_raw)and q['sha256']==hashlib.sha256(prompt_raw).hexdigest()and q['git_blob']==hashlib.sha1(b'blob '+str(len(prompt_raw)).encode()+b'\0'+prompt_raw).hexdigest(),'MAIN_PROMPT_PAYLOAD_IDENTITY')
check(len(chunks)==84 and len(jsons)==82,'COMPLETE_JSON_SEGMENTS')
template_hits=[]
for no,line in enumerate(t.splitlines(),1):
    if re.search(r'\{\{[^}]+\}\}|\bTBD\b|\bTODO\b|INSERT_[A-Z]|REPLACE_ME|<[^>]+>',line):template_hits.append({'line':no,'text':line})
result={'at':now,'task':'R6-C handoff-final-counter','input_files':[{'path':'cloud-sixth-update-handoff-prompt.md','bytes':len(prompt_raw),'sha256':hashlib.sha256(prompt_raw).hexdigest()},{'path':'cloud-sixth-update-handoff-manifest.json','bytes':len(manifest_raw),'sha256':hashlib.sha256(manifest_raw).hexdigest()}],'normative_count':65,'required_optional_withdrawn':[56,8,1],'batches':14,'formal_paths':54,'conflict_pairs':24,'separate_float_facet':1,'policy_count':7,'limit_count':14,'EV_actual_A_bytes_verified':len(evchecks),'payload_actual_tree_path_mode_blob_checks':payload_count,'manual_entries':manual,'receipts':receipts,'template_hits':template_hits,'issues':issues,'update_started':False,'reference_execution':0,'metadata':{'canonical_task_name':'/root/combat_review','model_effort_tier_speed_UUID':'UNVERIFIED'},'scope':'Actual fixed-input objects/tree paths, prompt-manifest field equality/completeness, EV full bytes, manual entry metadata and future state. No repeated full source semantic reading or remote full-payload readback claim.'}
(OUT/'counter.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'ev-path-byte-validation.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n'for q in evchecks))
(OUT/'fixed-input-byte-validation.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n'for q in fixed_byte_checks))
(OUT/'command-log.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n'for q in commands))
print(json.dumps({k:v for k,v in result.items()if k not in ['manual_entries','receipts','scope','metadata','input_files']},ensure_ascii=False,indent=2))
