import json,hashlib,datetime,subprocess
from pathlib import Path
C=Path(__file__).parent;A=C.parent/'creature_a_atomic_reception';E=C.parent/'counter_ecb_transform_existing_crea';B=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception'
def read(p):return json.loads(p.read_text())
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
cl=read(C/'reading-ledger.json');al=read(A/'reading-ledger.json');known={(x['repo'],x['path']) for x in al['own_full_reads']};added=[]
for x in cl['entries']+cl['discovered_dependencies']:
 path=x.get('path');actual=x.get('own_full_read_identity',x)
 if x.get('current_status')!='FULL_READ_CURRENT_SCOPE' or not path or not any(t in path for t in ['PBS/types.txt','PBS/ribbons.txt','backup/types.txt','008_AnimatedBitmap.rb']):continue
 key=('R',path)
 if key in known:continue
 raw=(R/path).read_bytes();assert hashlib.sha256(raw).hexdigest()==actual['sha256'];assert raw==subprocess.check_output(['git','-C',str(R),'show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+path]);row=dict(repo='R',path=path,commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',bytes=len(raw),sha256=actual['sha256'],blob=actual.get('git_blob'),lines=len(raw.splitlines()),status='FULL_READ_BY_SELF',reader=reader,extent=[1,len(raw.splitlines())],source_of_read='Same actual context C complete source reading; no new independent credit. Package '+x.get('actual_read_package','wp21-mechanism-spinda-display.v1.json'),semantic_time_utc='UNRECORDED_PER_CALL',recorded_utc=utc,primary=False,qualification='Only actual own fullsource read; not full A/C consumer/formal/PBS acceptance.');al['own_full_reads'].append(row);added.append(row);known.add(key)
ev=read(E/'evidence.json')
for x in ev['formal_identities'].values():
 key=('B8',x['path'])
 if key in known:continue
 row=dict(repo='B8',path=x['path'],commit=x['commit'],bytes=x['bytes'],sha256=x['sha256'],blob=x['git_blob'],lines=x['lines'],status='FULL_READ_BY_SELF',reader=reader,extent=[1,x['lines']],source_of_read='Same actual context bounded ECB counterreview complete formal read; exact chunks retained in counter evidence.',actual_read_chunks=x['actual_output_chunks'],semantic_time_utc='UNRECORDED_PER_CALL',recorded_utc=utc,primary=False,qualification='No new independent reviewer/vote; bounded NO_REQUIRED reasoning only, not whole file acceptance.');al['own_full_reads'].append(row);added.append(row);known.add(key)
write(A/'reading-ledger.json',al);nr=sum(x['repo']=='R' for x in al['own_full_reads']);nf=sum(x['repo']=='B8' for x in al['own_full_reads']);delta=dict(recorded_utc=utc,added_count=len(added),added_full_reads=added,current_same_context_full_R=nr,current_same_context_full_F=nf,new_contexts=0,new_independent_reviewers=0,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
if (A/'io/same-context-C-and-ECB-read-delta.v3.json').exists():
 assert not added;delta=read(A/'io/same-context-C-and-ECB-read-delta.v3.json')
else:write(A/'io/same-context-C-and-ECB-read-delta.v3.json',delta)
names=['wp31-registry-meaning-atoms.v1.json','wp21-handler-meaning-atoms.v1.json','wp23-shadow-lifecycle-meaning-atoms.v1.json','battle-consumer-delta.v1.json','default-transformation-records.v1.json','mega-menu-entry-consumers.v1.json','shadow-data-vectors.v1.json','wp30-compound-meaning.v1.json','wp32-context-meaning.v1.json','type-ribbon-data.v1.json','wp21-mechanism-spinda-display.v1.json','wp31-wrappers-commit-meaning.v1.json'];manifest=[]
for name in names:
 p=C/name;raw=p.read_bytes();d=json.loads(raw);atoms=next(d[k] for k in ['manual_atoms','manual_atom_count','manual_assertion_count'] if k in d);manifest.append(dict(path=name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader,manual_atom_count=atoms,whole_domain_acceptance=False))
rv=read(C/'reverse-mapping.json');count=sum(len(x.get('child_assertions',[])) for x in rv['records']);assert count==sum(x['manual_atom_count'] for x in manifest)==736;assert len({x['id'] for x in rv['records']})==len(rv['records']);assert all(x.get('accepted') is False for x in rv['records'])
for file,key in [('forward-mapping.json','manual_meaning_packages'),('interfaces.json','records'),('progress.json','meaning_packages')]:
 d=read(C/file);d[key]=[dict(id=f'C-OUT-{i:02}',direction='ACTUAL_OWN_FINITE_CONTRIBUTION_AVAILABLE',**x) for i,x in enumerate(manifest,1)] if file=='interfaces.json' else manifest;d['utc' if file!='progress.json' else 'updated_utc']=utc
 if file=='forward-mapping.json':d['qualification']='Nine original authoredforwardfacts plus twelve complete manual meaning packages; no automatic semantic PASS or independent credit for structural index.'
 if file=='progress.json':d.update(manual_parent_groups=len(rv['records']),primary_clause_atoms=count,same_context_current_full_R=nr,same_context_current_full_F=nf);d['initial_counts']['dependency_pbs'].update(actual_full=10,not_full=20)
 if file=='interfaces.json':d['bounded_external_counterreview']=dict(path='../counter_ecb_transform_existing_crea/counterreview.json',classification='NO_REQUIRED_BOUNDED_SCOPE',root_decision='PENDING',scope='Separate finite counterreview, no C whole-domain acceptance')
 write(C/file,d)
cl['same_context_full_ledger']=dict(path='../creature_a_atomic_reception/reading-ledger.json',R=nr,F=nf,recorded_utc=utc,new_votes=0);write(C/'reading-ledger.json',cl)
ap=read(A/'progress.json');ap.update(updated_utc=utc,own_full_reference_total=nr,additional_reference_full_read=nr-ap['primary_reference_full_read'],own_full_formal_total=nf,same_context_C_read_delta='io/same-context-C-and-ECB-read-delta.v3.json',same_context_C_manual_atoms=count);write(A/'progress.json',ap)
review=(C/'review.md').read_text();review=review.replace('2026-10-16T08:33:14.209197+00:00',utc).replace('30份 PBS 中4份可选 Shadow 原文件全文读，26份没有授予全文信用','30份 PBS 中10份原文件全文读（4份可选 Shadow、当前类型／缎带与四代类型备份），20份没有授予全文信用').replace('R90/F20',f'R{nr}/F{nf}').replace('九份冻结人工意义包','十二份冻结人工意义包').replace('198 个具名父组／606 个子断言',f'{len(rv["records"])} 个具名父组／{count} 个子断言').replace('当前继续：WP21机制／展示／Spinda；WP31剩余完整复合条款与成功提交；','WP21机制／展示／Spinda及WP31守卫／成功提交已有完整有限后继包，仍不自动全域批准。当前继续：剩余完整复合条款；');review+='\n外部 ECB002 有限反证另在 tasks/counter_ecb_transform_existing_crea/；完整8节结论 NO_REQUIRED_BOUNDED_SCOPE，源码联合trace成立而当前跨篇规则未证明必修缺项，root终裁待实际接收。0新增context／票。\n';(C/'review.md').write_text(review)
ar=(A/'review.md').read_text();ar+='\n'+utc+' 同一实际审者读账增量 v3：R'+str(nr)+'/F'+str(nf)+'；C十二有限意义包'+str(count)+'手工子断言。A1430旧父行与6939记录、102原facts保持原字节／分母限定，PBS与具体consumer OPEN未自动闭合。ECB002有限反证完成，不授A/C整体批准。\n';(A/'review.md').write_text(ar)
check=dict(recorded_utc=utc,package_count=len(manifest),manual_groups=len(rv['records']),manual_children=count,all_groups_accepted_false=True,same_context_full_R=nr,same_context_full_F=nf,source_read_delta=delta['added_count'],initial_C_pbs_whole=10,initial_C_pbs_not_whole=20,whole_domain_acceptance=False,denominator_frozen=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');write(C/'io/current-consistency-20261016T0857.json',check);print(json.dumps(check))
