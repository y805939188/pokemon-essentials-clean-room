import json,pathlib,subprocess,hashlib,datetime,collections
P=pathlib.Path(__file__).parent;R=pathlib.Path('/workspace/pokemon-essentials');B=pathlib.Path('/workspace/pokemon-essentials-clean-room');BASE=P.parent.parent;NOW=datetime.datetime.now(datetime.timezone.utc).isoformat();C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';BC='fd1df570cad987dc3852a3b958f03916e317f7fe'
def read(n):return json.loads((P/n).read_text())
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def sha(b):return hashlib.sha256(b).hexdigest()
L=read('reading-ledger.json')
path='Data/Scripts/002_BattleSettings.rb'
if path not in {x['path'] for x in L['own_full_reads']}:
 raw=(R/path).read_bytes();L['own_full_reads'].append(dict(repo='R',commit=C,tree='7589c800b61ba13a13040ed0d686979b80a84fd0',path=path,bytes=len(raw),sha256=sha(raw),blob=subprocess.check_output(['git','rev-parse',C+':'+path],cwd=R,text=True).strip(),lines=len(raw.splitlines()),status='FULL_READ_BY_SELF',reader='/root/creature_a_atomic_reception',extent=[1,len(raw.splitlines())],source_of_read='1–92,93–108,108–140 through EOF actually rendered/read',recorded_utc=NOW,semantic_time_utc='UNRECORDED_PER_CALL',primary=False,qualification='Settings definition credit only, no wholeconsumerdomain transfer'))
path='Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb';raw=(R/path).read_bytes();norm=('\n'.join(raw.decode('utf-8-sig').splitlines()[607:653])+'\n').encode()
if not any(x['path']==path and x['range']==[608,653] for x in L.get('own_partial_read_spans',[])):
 L['own_partial_read_spans'].append(dict(repo='R',commit=C,path=path,range=[608,653],named_units='on_end_battle evolve_and_black_out complete handler; pbEvolutionCheck complete method',status='PARTIAL_FILE_ACTUAL_READ_SPAN',reader='/root/creature_a_atomic_reception',bytes=len(raw),sha256=sha(raw),lines=len(raw.splitlines()),normalized_span_bytes=len(norm),normalized_span_sha256=sha(norm),recorded_utc=NOW,semantic_time_utc='UNRECORDED_PER_CALL'))
save('reading-ledger.json',L)
S=read('sourcefact-consumer-receptions.json');money=read('core-money-reception.v1.json')
if not any(x.get('package')=='kernel-forward.v1.json#/CAR-KERNEL-F03/F04' for x in S['named_contributions']):
 S['named_contributions'].append(dict(package='kernel-forward.v1.json#/CAR-KERNEL-F03/F04',source_path='tasks/core_atomic_reception/kernel-forward.v1.json',source_parent_bytes=money['package_bytes'],source_parent_sha256=money['package_sha256'],original_reader='/root/core_atomic_reception',receiver='/root/creature_a_atomic_reception',adopted_complete_fact_ids=money['adopted_complete_fact_ids'],received_complete_objects=money['received_complete_objects'],original_local_receipt='core-money-reception.v1.json',later_own_source_timing_qualification='core-money-reception.scope-clarification.v1.json',qualification='Only2 complete selected objects/common premises/sourceunits received; not all6 parent facts',own_source_full_read_granted=False,recorded_utc=NOW))
S['recorded_utc']=NOW;save('sourcefact-consumer-receptions.json',S)
A=read('manual-atomic-clauses.json');D=read('old-locator-disposition.json');RS=json.loads((BASE/'tasks/coverage_acceptance_incremental/dispatch/creature_a_atomic_reception.readset.json').read_text())
assert len(D['rows'])==1430 and len({x['id'] for x in D['rows']})==1430
assert len(A['atoms'])==6939 and len({x['id'] for x in A['atoms']})==6939
assert len(S['facts'])==102 and len({x['id'] for x in S['facts']})==102
ids={x['id'] for x in A['atoms']};parents={x['id'] for x in D['rows']};referenced=[]
for row in D['rows']:
 for id in row.get('manual_children',[]):assert id in ids,(row['id'],id);referenced.append(id)
 assert bool(row.get('manual_children')) or row.get('decomposition')=='COMPLETE_BOUNDED_TYPE_DISPOSITION',row['id']
assert len(referenced)==len(set(referenced))
for x in A['atoms']:
 if x.get('old_locator'):assert x['old_locator'] in parents,x['id']
 assert x.get('business',x.get('runtime','NOT_EXECUTED'))=='NOT_EXECUTED',x['id']
assert [x['id'] for x in S['facts']]==[x['id'] for x in RS['full_original_source_fact_records']]
for x,y in zip(S['facts'],RS['full_original_source_fact_records']):assert x['original_complete_record']==y,x['id']
# Exact current bytes against fixed Git, a metadata check not another semantic read.
verified=[];errors=[]
for x in L['own_full_reads']:
 repo=R if x['repo']=='R' else B;commit=C if x['repo']=='R' else BC;raw=subprocess.check_output(['git','show',commit+':'+x['path']],cwd=repo)
 assert len(raw)==x['bytes'] and sha(raw)==x['sha256'],x['path']
 assert (repo/x['path']).read_bytes()==raw,x['path']
 verified.append(dict(repo=x['repo'],path=x['path'],sha256=sha(raw),bytes=len(raw)))
for key in ['own_complete_units','own_partial_read_spans']:
 for x in L.get(key,[]):
  raw=subprocess.check_output(['git','show',C+':'+x['path']],cwd=R);assert sha(raw)==x.get('file_sha256',x.get('sha256')),x['path'];a,b=x.get('range',x.get('lines',[]));assert 1<=a<=b<=len(raw.splitlines()),(x['path'],a,b,len(raw.splitlines()))
# Parent evidence identities are rechecked without conferring receipt of unreceived sibling objects.
for x in S['named_contributions']:
 path=x.get('source_path');expect=x.get('sha256',x.get('source_parent_sha256'))
 if path and expect:assert sha((BASE/path).read_bytes())==expect,path
# Save actual read-only Git command outputs and UTC honestly now, rather than backfilling original calls.
checks=[]
for name,cmd,cwd in [('R-status',['git','status','--porcelain'],R),('R-head',['git','rev-parse','HEAD','HEAD^{tree}'],R),('B-formal-tree',['git','rev-parse',BC+':deliverables/final-specification-set'],B)]:
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(cmd,cwd=cwd,capture_output=True);end=datetime.datetime.now(datetime.timezone.utc).isoformat();checks.append(dict(name=name,command=cmd,cwd=str(cwd),started_utc=start,ended_utc=end,exit_code=p.returncode,stdout=p.stdout.decode(),stderr=p.stderr.decode()));assert p.returncode==0
assert checks[0]['stdout']=='',checks[0]['stdout'];assert checks[1]['stdout'].splitlines()==[C,'7589c800b61ba13a13040ed0d686979b80a84fd0'];assert checks[2]['stdout'].strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
res=dict(schema='gr8-cre-a-wip-consistency-check/v1',utc=NOW,result='CONSISTENT_BOUNDED_WIP_NOT_GLOBAL_PASS',checks=dict(old_locators=1430,behavior_parents=sum(bool(x.get('manual_children')) for x in D['rows']),typed_parents=sum(x.get('decomposition')=='COMPLETE_BOUNDED_TYPE_DISPOSITION' for x in D['rows']),manual_records=len(A['atoms']),parent_referenced_children=len(referenced),original_facts_exact_unchanged=102,sourcefact_specific_joins=102,own_full_R=sum(x['repo']=='R' for x in L['own_full_reads']),own_full_F=sum(x['repo']=='B8' for x in L['own_full_reads']),named_contribution_entries=len(S['named_contributions']),partial_complete_unit_groups=len(L.get('own_complete_units',[]))+len(L.get('own_partial_read_spans',[]))),source_identities_verified=verified,read_only_command_captures=checks,qualification='Shape/identity/orphan check only; no automated semantic acceptance of facts, child clauses, actual native execution or globally frozen denominator.',business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
save('io/wip-consistency-v3.json',res);print(json.dumps(dict(utc=NOW,result=res['result'],checks=res['checks']),ensure_ascii=False))
