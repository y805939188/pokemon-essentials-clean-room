from pathlib import Path
import json,gzip,hashlib,subprocess,collections,itertools,datetime,sys
R=Path('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e');T=R/'tasks/handoff_preparation_cloud';H=T/'handoff';C='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'
def git(*a,repo=None):return subprocess.check_output(['git',*( ['-C',repo] if repo else []),*a])
def sha(b):return hashlib.sha256(b).hexdigest()
start=datetime.datetime.now(datetime.timezone.utc).isoformat();checks=[]
def check(name,truth):
 assert truth,name
 checks.append({'id':name,'result':'PASS_TOOL_VALIDATION'})
d=json.loads((H/'cloud-eighth-update-handoff-manifest.json').read_text());root=json.loads((R/'adjudication/root-decisions.partial.json').read_text());rows=d['records'];byid={x['id']:x for x in rows}
check('33 exact current root IDs and classifications',len(byid)==33 and {i:(x['classification'],x.get('severity')) for i,x in byid.items()}=={x['id']:(x['classification'],x.get('severity')) for x in root['records']})
check('27 required 2P2 25P3 6optional',collections.Counter(x.get('severity') for x in rows if x['classification']=='required')=={'P2':2,'P3':25} and sum(x['classification']=='optional' for x in rows)==6)
check('seven nonempty effective groups',all(len(x['seven_groups'])==7 and all(x['seven_groups'].values()) for x in rows))
check('no self accepted revision or update launch',d['update_started'] is False and all(x['seven_groups']['6_独立裁决']['new_independent_votes']==0 for x in rows))
check('unfrozen core explicit, no invented future identity',d['R8_core']['state']=='PENDING_ROOT_CORE_FREEZE' and d['R8_core']['commit'] is None and d['R8_core']['tree'] is None)
check('64 original/successor identities',len(d['input_payloads'])==64)
for x in d['input_payloads']+d['additional_payloads']+d['source_spec_payloads']['files']:
 b=git('show',x['commit']+':'+x['path'],repo=x.get('repo'))
 check('identity '+x['commit'][:8]+':'+x['path'],len(b)==x['bytes'] and sha(b)==x['sha256'] and hashlib.sha1(('blob '+str(len(b))+'\0').encode()+b).hexdigest()==x['blob'])
check('all operative file spellings resolved',not d['source_spec_payloads']['unresolved_cited_spellings'])
# Lossless graph of all64 full original payloads; machine reconstruction adds no reading credit.
g=json.loads((T/'audit/typed-input-graph.json').read_text());memo={}
def decode(n):
 if n in memo:return memo[n]
 x=g['nodes'][n]
 v=x['value'] if 'value'in x else ({k:decode(z) for k,z in x['object'].items()} if 'object'in x else [decode(z) for z in x['array']]);memo[n]=v;return v
original=json.loads(gzip.decompress((T/'audit/exact-inputs.json.gz').read_bytes()))
check('64 typed graph payloads losslessly reconstruct',len(g['roots'])==64 and all(decode(x['node'])==y['content'] and x['path']==y['path'] and x['phase']==y['phase'] for x,y in zip(g['roots'],original)))
req={i for i,x in byid.items() if x['classification']=='required'};bs=d['batch_assignment'];flat=[i for b in bs for i in b['required_ids']]
check('9 batches unique exact 27 primary IDs',len(bs)==9 and len(flat)==len(set(flat))==27 and set(flat)==req)
check('all six optional write sets empty',all(not x['seven_groups']['4_最小修订合同']['required_target_write_set'] and x['primary_batch'] is None for x in rows if x['classification']=='optional'))
check('8 no-required and4binary separate empty formal writes',len(d['separate_no_required'])==8 and len(d['separate_binary_negative'])==4 and all(not x['formal_write_set'] for x in d['separate_no_required']))
for b in bs:
 bd=H/'batches'/b['id'];read=json.loads((bd/'readset.json').read_text());text=(bd/'prompt.md').read_text()
 check('batch full records/readset '+b['id'],{x['id'] for x in read['records']}==set(b['required_ids']) and all('## '+i+' —' in text for i in b['required_ids']))
check('no cross-batch actual target overlap',all(not(set(a['actual_target_write_set'])&set(b['actual_target_write_set'])) for a,b in itertools.combinations(bs,2)))
check('all31 actual targets unique writer',len(d['file_conflict_graph']['actual_file_writers'])==31 and len({x['path'] for x in d['file_conflict_graph']['actual_file_writers']})==31)
check('first wave conditional9 currently0 launched0',d['dependency_graph']['first_wave_after_common_release_count']==9 and d['dependency_graph']['currently_startable_count']==0 and all(b['author']['actual_task_id']=='NOT_STARTED' for b in bs))
prompt=(H/'cloud-eighth-update-handoff-prompt.md').read_text();check('prompt current33 full sections',all(prompt.count('## '+i+' —')==1 for i in byid))
check('mandatory propagations and exact completed identities','55a843b3ab01d26442f604770f30932e120f923b' in prompt and '136–278' in prompt and '4–68' in prompt and 'WP42§7.1:207' in prompt)
check('no Ruby source body in normative prompt',not any(s in prompt for s in ['def pbUseMove(', 'class Battle::Move::', 'def compile_PBS_file_generic(']))
check('formal tree unchanged fromB8',git('rev-parse','HEAD:deliverables/final-specification-set').strip()==git('rev-parse',d['B8']['commit']+':deliverables/final-specification-set').strip())
changes=git('status','--porcelain','--untracked-files=all').decode().splitlines();check('workspace modifications restricted to own task',all(l[3:].startswith(str(T)+'/') for l in changes))
result={'schema':'r8-bounded-handoff-validation/v1','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version.split()[0],'status':'PASS_TOOL_VALIDATION','checks':checks,'check_count':len(checks),'command':['python',str(T/'validate_package.py')],'semantic_or_behavior_credit':0,'update_started':False}
(T/'verification').mkdir(exist_ok=True);(T/'verification/package-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':len(checks),'records':33,'required':27,'batches':9,'transport_or_tools_are_not_semantic_pass':True}))
