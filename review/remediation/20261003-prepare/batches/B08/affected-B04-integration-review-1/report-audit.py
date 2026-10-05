import pathlib,json,hashlib,gzip,subprocess,re,collections,shutil
R=pathlib.Path('/workspace/pokemon-essentials-clean-room');T=pathlib.Path('/tmp/b08-b04-actual');D=R/'review/remediation/20261003-prepare/batches/B08/affected-B04-integration-review-1'
X='49c21538e72b7a5873972cd00fcae1ee390cce64';B='759eee80ce7856570fde2de12d5dcf98ce7e6017';C='0f35a393d9de467cd5f7e695b6072687bb582186';S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
checks=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a,cwd=R):return subprocess.check_output(['git',*a],cwd=cwd)
def obj(n):return json.loads((D/n).read_text())
def ck(n,v):checks.append(dict(check=n,pass_=bool(v)));assert v,n
def flat(ranges):return {n for a,z in ranges for n in range(a,z+1)}
ck('isolated branch remains exact actual before report commit',git('rev-parse','HEAD').decode().strip()==X and git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/review-B08-affected-B04-integration-1')
status=git('status','--porcelain','--untracked-files=all').decode().splitlines();prefix=str(D.relative_to(R))+'/'
ck('only new independent directory written',bool(status) and all(x[:2]=='??' and x[3:].startswith(prefix) for x in status))
shutil.copyfile(T/'verify_report.py',D/'report-audit.py')
for p in sorted(D.glob('*.json')):json.loads(p.read_text());ck('valid JSON '+p.name,True)
for p in sorted(D.glob('*.jsonl')):
 ck('valid JSONL '+p.name,all(isinstance(json.loads(x),dict) for x in p.read_text().splitlines()))
input_=obj('independent-input-validation.json');first=obj('first-judgment.json');ab=obj('affected-boundaries.json');ho=obj('handoff.json');compare=obj('A-REG-comparison.json');log=obj('source-reading-log.json')
ck('independent input exactly1321 passing',len(input_['checks'])==1321 and all(x['pass_'] for x in input_['checks']) and input_['all_checks_pass'])
ck('first judgment hash independently fixed',first['independent_input_validation_sha256']==sha((D/'independent-input-validation.json').read_bytes()) and first['decision']=='PASS_SCOPED' and first['before_detailed_A_REG_validation_comparison'])
ck('author comparison binds first judgment',compare['first_judgment_sha256']==sha((D/'first-judgment.json').read_bytes()) and compare['first_judgment_before_detailed_validation_comparison'])
ck('exact actual and bounded two keys',ab['actual']==X and ho['reviewed_actual']==X and ho['report_commit_parent_must_equal']==X and ab['actual_tree']==git('rev-parse',X+'^{tree}').decode().strip() and len(ab['cases'])==2 and {x['key'] for x in ab['cases']}==set(ho['scope']))
ck('no semantic/parent/global expansion',ho['status']=='PASS_SCOPED' and not any(ho[k] for k in ['whole_B08_semantic_approval','whole_B04_35_23_reapproval','other_two_actual_reviews_replaced','parent_C_acceptance']) and not ab['full_B08_semantic_approval'])
ck('no findings roots repairs closures public writes',not obj('new-findings.json')['findings'] and not ho['required_repairs'] and all(ho[k]==0 for k in ['new_defects','public_or_history_edits','canonical_ID_closures','downstream_dispatched','reference_execution','behavior_vectors_executed','runtime_observations','proven_demo_chains']))
events=[json.loads(x) for x in (D/'fresh-reading-events.jsonl').read_text().splitlines()];rr=collections.defaultdict(set)
for e in events:
 b=pathlib.Path('/tmp/rb04-reference',e['path']).read_bytes();ck('fresh range file hash '+e['path']+':'+str(e['start']),sha(b)==e['file_sha256'] and len(b)==e['bytes'] and e['reference_commit']==S and 1<=e['start']<=e['end']<=len(b.decode().splitlines()));rr[e['path']].update(range(e['start'],e['end']+1))
ck('21/36/1200 actual source count',len(rr)==21 and len(events)==36 and sum(map(len,rr.values()))==1200 and log['fresh_file_count']==21 and log['fresh_range_events']==36 and log['fresh_unique_lines']==1200)
for e in log['files']:
 ck('complete fresh read/unread partition '+e['path'],flat(e['read_ranges'])==rr[e['path']] and flat(e['read_ranges']).isdisjoint(flat(e['unread_ranges'])) and flat(e['read_ranges'])|flat(e['unread_ranges'])==set(range(1,e['line_count']+1)))
 ck('reference exact blob '+e['path'],e['git_blob']==git('rev-parse',S+':'+e['path'],cwd='/tmp/rb04-reference').decode().strip())
for a in ab['cases']:
 for e in a['source']:ck('source citation actually freshly read '+e['path']+':'+str(e['start']),e['commit']==S and set(range(e['start'],e['end']+1))<=rr[e['path']])
 for e in a['actual_formal_inputs']:
  b=git('show',X+':'+e['path']);ck('actual caller cited hash '+e['path'],e['commit']==X and e['sha256']==sha(b) and e['bytes']==len(b))
for e in obj('project-reading-log.json')['files']:
 b=git('show',X+':'+e['path']);ck('actual project read hash/range '+e['path'],e['sha256']==sha(b) and e['bytes']==len(b) and all(1<=a<=z<=len(b.decode().splitlines()) for a,z in e['read_ranges']))
di=obj('diff-identities.json');ck('full actual frozen identities and131/74',di['actual']==X and di['baseline']==B and di['candidate']==C and di['full_path_counts']==[131,74] and di['final_three_actual_files_in_both_full_diffs'])
for e in di['full_diff_artifacts']:
 z=(D/e['archive_path']).read_bytes();b=gzip.decompress(z);ck('lossless full diff '+e['archive_path'],sha(z)==e['archive_sha256'] and len(z)==e['archive_bytes'] and sha(b)==e['sha256'] and len(b)==e['bytes'] and b==(T/e['path']).read_bytes() and b==git(*e['command'][1:]));ck('complete unfiltered actual diff131/74 '+e['archive_path'],len(re.findall(rb'^diff --git ',b,re.M))==len(e['paths']) and len(e['paths']) in [131,74])
for e in di['focused_diffs']:
 b=(D/e['path']).read_bytes();ck('focused diff exact '+e['path'],sha(b)==e['sha256'] and len(b)==e['bytes'] and b==git(*e['command'][1:]))
config=obj('configuration-receipt.json');ck('exact requested configuration and UNVERIFIED no probes',config['requested']['model']=='gpt-6.1-sol' and config['requested']['reasoning']=='Ultra' and config['requested']['service_tier']=='Standard(default)' and set(config['effective'].values())=={'UNVERIFIED'} and config['quota_probes']==0 and config['auth_or_config_probes']==0 and config['subagents_spawned']==0)
readme=(D/'README.md').read_text()
for target in re.findall(r'\]\(([^)]+)\)',readme):ck('README artifact link '+target,(D/target).is_file())
for p in D.iterdir():
 if p.suffix in ['.gz','.diff']:continue
 b=p.read_bytes();ck('report text newline '+p.name,b.endswith(b'\n') and not b.endswith(b'\n\n'));ck('report ordinary text no trailing whitespace '+p.name,all(x.rstrip(b' \t')==x for x in b.splitlines()))
ck('isolated reference remains unchanged',git('rev-parse','HEAD',cwd='/tmp/rb04-reference').decode().strip()==S and git('status','--porcelain',cwd='/tmp/rb04-reference')==b'')
ck('reference not tracked by own report',all(not x[3:].startswith('reference/') for x in status))
artifact_ids=[dict(path=p.name,bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in sorted(D.iterdir()) if p.name not in ['artifact-manifest.json','report-validation.json']]
manifest=dict(actual=X,actual_tree=ab['actual_tree'],report_parent=X,report_sha='EXTERNAL_FULL_SHA_AFTER_ORDINARY_COMMIT_PUSH_READBACK',artifacts=artifact_ids,self_exclusions=['artifact-manifest.json','report-validation.json'],no_source_code_copied=True,source_reference_program_execution=0)
(D/'artifact-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
for e in artifact_ids:ck('artifact manifest independent byte recheck '+e['path'],sha((D/e['path']).read_bytes())==e['sha256'] and (D/e['path']).stat().st_size==e['bytes'])
report=dict(actual=X,status='PASS_REPORT_INTEGRITY',check_count=len(checks),checks=checks,all_pass=True,artifact_manifest_sha256=sha((D/'artifact-manifest.json').read_bytes()),artifact_count_before_self_exclusions=len(artifact_ids),reference_execution=0,behavior_vectors_executed=0,runtime_observations=0,proven_demo_chains=0,scope='Report identity/citation/footprint verification; not extra behavioral coverage or any other actual reviewer verdict')
(D/'report-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),all_pass=True,files=len(list(D.iterdir())),manifest_sha256=report['artifact_manifest_sha256']),ensure_ascii=False))
