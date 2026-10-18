import json,hashlib,datetime,subprocess
from pathlib import Path
C=Path(__file__).parent;A=C.parent/'creature_a_atomic_reception';R=Path('/workspace/pokemon-essentials');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception';commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def rd(p):return json.loads(p.read_text())
def wr(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def identity(p):
 raw=p.read_bytes();return dict(path=p.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
assert not (C/'io/current-consistency-v8.json').exists()
newnames=['wp22-flags-ai-bug-consumers.v1.json','wp22-item-removal-config-bindings.v1.json'];new=[rd(C/n) for n in newnames]
rev=rd(C/'reverse-mapping.json');seen={x['id'] for x in rev['records']}
for d in new:
 for x in d['records']:
  if x['id'] in seen:assert next(z for z in rev['records'] if z['id']==x['id'])==x;continue
  seen.add(x['id']);rev['records'].append(x)
rev['utc']=utc;wr(C/'reverse-mapping.json',rev)
al=rd(A/'reading-ledger.json');known={x['path'] for x in al['own_full_reads']}
fulladds=[];rereads=[]
for p,capture,readproof in [('Data/Scripts/011_Battle/005_AI/004_AI_MegaEvolve.rb',None,'Actual complete13line cat current exec, previous f1de3f full13'),('PBS/trainers.txt','2026-10-16T10:29:17.212992698Z','Actual whole2963B cat and genuine subprocessUTC in same output')]:
 praw=(R/p).read_bytes();assert praw==subprocess.check_output(['git','-C',str(R),'show',commit+':'+p]);x=dict(repo='R',path=p,commit=commit,bytes=len(praw),sha256=hashlib.sha256(praw).hexdigest(),blob=subprocess.check_output(['git','-C',str(R),'rev-parse',commit+':'+p],text=True).strip(),lines=len(praw.splitlines()),status='FULL_READ_BY_SELF',reader=reader,extent=[1,len(praw.splitlines())],actual_read_evidence=readproof,captured_utc=capture or 'UNRECORDED_PER_CALL',recorded_utc=utc,primary=False,qualification='Actual whole source read, no whole domain or new independent vote. Trainers full raw current only; resource absence conclusion is bounded.')
 if p in known:rereads.append(dict(**x,new_full_credit=0));continue
 al['own_full_reads'].append(x);fulladds.append(x)
partial=[];oldpartial={(x['path'],tuple(x['range'])) for x in al['own_partial_read_spans']}
for name,d in zip(newnames,new):
 for u in d['complete_source_units']:
  k=u['source_identity_key'];sid=d['source_identities'][k]
  if 'PARTIAL' not in sid.get('credit',''):continue
  key=(sid['path'],tuple(u['range']))
  if key in oldpartial:continue
  oldpartial.add(key);x=dict(repo='R',path=sid['path'],bytes=sid['bytes'],sha256=sid['sha256'],range=u['range'],named_units=u['id'],reader=reader,status='PARTIAL_FILE_ACTUAL_COMPLETE_NAMED_UNIT',package=name,recorded_utc=utc,whole_file_credit=False);al['own_partial_read_spans'].append(x);partial.append(x)
wr(A/'reading-ledger.json',al);r_count=sum(x['repo']=='R' for x in al['own_full_reads']);f_count=sum(x['repo']=='B8' for x in al['own_full_reads']);assert r_count==103 and f_count==25
ld=rd(C/'reading-ledger.json');ld['discovered_dependencies']+=fulladds;ld['own_new_complete_named_units'].append(dict(recorded_utc=utc,packages=newnames,newly_recorded_partial_units=len(partial),source_FULL_credit=False,qualification='Complete named source units actually read; existing full identities/parent checks do not grant new whole files.'))
ld['selected_complete_PBS_record_reads'].append(dict(recorded_utc=utc,package=newnames[0],path='PBS/items.txt',actual_complete_projection='693sectionIDs/all680Flags occurrences, 13omissions',actual_read_chunks=['7add83','a78f34','996ece'],whole_PBS_credit=False,whole_record_credit=0,qualification='Full field column, not complete other fields; currentTRAINERS whole separately in full ledger.'))
ld['same_context_full_ledger']=dict(path='../creature_a_atomic_reception/reading-ledger.json',R=r_count,F=f_count,recorded_utc=utc,new_votes=0);wr(C/'reading-ledger.json',ld)
pr=rd(C/'progress.json')
for name,d in zip(newnames,new):pr['meaning_packages'].append(dict(**identity(C/name),actual_reader=reader,manual_atom_count=d['manual_atoms'],whole_domain_acceptance=False))
pr['updated_utc']=utc;pr['manual_parent_groups']=len(rev['records']);pr['primary_clause_atoms']=sum(len(x.get('child_assertions',[])) for x in rev['records']);pr['same_context_current_full_R']=r_count;pr['same_context_current_full_F']=f_count
parentnames=['wp30-formal-parent-dispositions.v1.json','wp22-formal-parent-dispositions.v1.json'];pr['formal_parent_dispositions']=[dict(**identity(C/n),formal_files=1 if n.startswith('wp30') else 2,nonempty_parents=rd(C/n)['nonempty_parent_count'],new_atoms=0,whole_task_acceptance=False) for n in parentnames];pr['wp30_scope_root_status']=dict(classification='NO_REQUIRED_BOUNDED_SCOPE',actual_whole_receipt_received=True,ack='wp30-root-scope-reception-ack.v1.json',old_frozen_parent_open_status_read_with_ack=True);wr(C/'progress.json',pr)
intf=rd(C/'interfaces.json');intf['utc']=utc
for name,d in zip(newnames,new):intf['records'].append(dict(id=f'C-OUT-{len(intf["records"])+1:02}',direction='ACTUAL_OWN_FINITE_CONTRIBUTION_AVAILABLE',**identity(C/name),actual_reader=reader,manual_atom_count=d['manual_atoms'],whole_domain_acceptance=False))
intf['pending_scope_observation']=dict(path='wp30-cancel-dynamic-read-scope.observation.v1.json',status='ROOT_NO_REQUIRED_BOUNDED_SCOPE_ACTUALLY_RECEIVED',ack='wp30-root-scope-reception-ack.v1.json',required=0,optional=0,no_new_contexts_or_votes=True);wr(C/'interfaces.json',intf)
gaps=rd(C/'coverage-gaps.json');gaps['recorded_utc']=utc
for g in gaps['records']:
 if g['id']=='C-FORMAL-EXHAUSTION':
  done={f['path'] for n in parentnames for f in (rd(C/n).get('formal_identities') or {'only':rd(C/n)['formal']}).values()};g['paths']=[p for p in g['paths'] if p not in done];g['already_manually_parent_disposed']=parentnames;g['meaning']='Remaining six complete formal papers are actually full read but all physical/compound parent dispositions are still being explicitly completed. Three papers now have parent ledgers, no range/hash/PASS substitution and no global denominator freeze.'
 if g['id']=='C-SCOPE-OBSERVATION':g['status']='ROOT_NO_REQUIRED_BOUNDED_SCOPE_ACTUALLY_RECEIVED';g['ack']='wp30-root-scope-reception-ack.v1.json'
gaps['records'].append(dict(id='C-ADDITIONAL-ITEM-FULL-FILE',status='AVAILABLE_NOT_WHOLE_READ',path='PBS/items.txt',actual_read='Selected complete50resource items and later named items; all693ID/Flags column. Whole other field records not inferred.',meaning='Full Flags projection does not close wholefile or all item consumer meanings.'))
wr(C/'coverage-gaps.json',gaps)
ap=rd(A/'progress.json');ap['updated_utc']=utc;ap['own_full_reference_total']=r_count;ap['additional_reference_full_read']=r_count-ap['primary_reference_full_read'];ap['own_full_formal_total']=f_count;ap['same_context_C_manual_atoms']=pr['primary_clause_atoms'];ap['same_context_C_read_delta']='io/same-context-C-WP22-read-delta.v8.json';wr(A/'progress.json',ap)
check=dict(recorded_utc=utc,meaning_packages=len(pr['meaning_packages']),manual_groups=len(rev['records']),manual_children=pr['primary_clause_atoms'],all_groups_accepted_false=all(x.get('accepted') is False for x in rev['records']),current_own_full_R=r_count,current_own_full_F=f_count,new_full_files=[x['path'] for x in fulladds],prior_full_current_rereads=rereads,new_partial_units=len(partial),formal_parent_dispositions=pr['formal_parent_dispositions'],primary_catalog_manual_vectors=261,related_growth_manual_vectors=63,related_evolution_manual_vectors=79,original_A102_comparison='Not rerun; lastactual08:33 io/wip-consistency-v3.json remains separate',global_denominator_frozen=False,whole_domain_acceptance=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');assert check['all_groups_accepted_false'] and check['manual_groups']==646 and check['manual_children']==1864
wr(C/'io/current-consistency-v8.json',check);wr(A/'io/wip-consistency-v8.json',check);wr(A/'io/same-context-C-WP22-read-delta.v8.json',dict(recorded_utc=utc,full=fulladds,prior_full_current_rereads=rereads,partial_units=partial,no_new_vote=True))
for p in [A/'review.md',C/'review.md']:
 with p.open('a') as f:f.write(f'\n\n{utc} WIP maintenance v8: same actual context R103/F25 whole reads, C23 meaning packages/646 manual groups/1864 children. Trainers2963B was already ownFULL at07:02; current fullreread adds0, onlyAI13 adds1. WP30 whole286 parent ledger211 and WP22 main114+data77 ledger138 are explicit parent dispositions, not new atoms or domainPASS. WP30 line242 root NO_REQUIRED_BOUNDED_SCOPE whole receipt actually received with immutable ack; no new required/optional/vote. All693current itemID/Flags column read separately from wholePBS; AI and BugContest finite consumers plus ordinary orb permission/Transform and bare mutation distinction frozen. Remaining six full formal parent ledgers, 20declared not-whole PBS and priorA/history obligations continue. Business NOT_EXECUTED; UPDATE_NOT_STARTED.\n')
print(json.dumps(check,ensure_ascii=False))
