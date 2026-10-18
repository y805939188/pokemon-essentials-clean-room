import json,hashlib,datetime,subprocess
from pathlib import Path
C=Path(__file__).parent;A=C.parent/'creature_a_atomic_reception';R=Path('/workspace/pokemon-essentials');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception';commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def rd(p):return json.loads(p.read_text())
def wr(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def ident(p):
 raw=p.read_bytes();return dict(path=p.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
assert not (C/'io/current-consistency-v10.json').exists()
names=['wp23-shadow-move-fallback-binding.v1.json','wp23-default-source-and-loader-bindings.v1.json'];ds=[rd(C/n) for n in names];rev=rd(C/'reverse-mapping.json');known={x['id'] for x in rev['records']}
for d in ds:
 for x in d['records']:assert x['id'] not in known;known.add(x['id']);rev['records'].append(x)
rev['utc']=utc;al=rd(A/'reading-ledger.json');fullknown={x['path'] for x in al['own_full_reads']};p='Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb';assert p not in fullknown;raw=(R/p).read_bytes();assert raw==subprocess.check_output(['git','-C',str(R),'show',commit+':'+p]);newfull=dict(repo='R',path=p,commit=commit,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),blob=subprocess.check_output(['git','-C',str(R),'rev-parse',commit+':'+p],text=True).strip(),lines=201,status='FULL_READ_BY_SELF',reader=reader,extent=[1,201],actual_read_evidence='Actual contiguous current tool outputs1–120 then121–201; complete literal factory/class body.',recorded_utc=utc,semantic_time_utc='UNRECORDED_PER_CALL',primary=False,qualification='Whole source actual reading, finite ShadowShed factory/PP boundary only; no wholecombatPASS/newvote.');al['own_full_reads'].append(newfull)
partial=[];oldpartial={(x['path'],tuple(x['range'])) for x in al['own_partial_read_spans']}
for name,d in zip(names,ds):
 for u in d['complete_source_units']:
  sid=d['source_identities'][u['source_identity_key']]
  lines=(R/sid['path']).read_text(encoding='utf-8-sig').splitlines();assert '\n'.join(lines[u['range'][0]-1:u['range'][1]]).rstrip()==u['text'].rstrip(),u['id']
  if 'PARTIAL' not in sid['credit']:continue
  key=(sid['path'],tuple(u['range']))
  if key in oldpartial:continue
  oldpartial.add(key);x=dict(repo='R',path=sid['path'],bytes=sid['bytes'],sha256=sid['sha256'],range=u['range'],named_units=u['id'],reader=reader,status='PARTIAL_FILE_ACTUAL_COMPLETE_NAMED_UNIT',package=name,recorded_utc=utc,whole_file_credit=False);al['own_partial_read_spans'].append(x);partial.append(x)
r_count=sum(x['repo']=='R' for x in al['own_full_reads']);f_count=sum(x['repo']=='B8' for x in al['own_full_reads']);assert(r_count,f_count)==(106,25)
pr=rd(C/'progress.json');pr['updated_utc']=utc
for name,d in zip(names,ds):pr['meaning_packages'].append(dict(**ident(C/name),actual_reader=reader,manual_atom_count=d['manual_atoms'],whole_domain_acceptance=False))
pr['manual_parent_groups']=len(rev['records']);pr['primary_clause_atoms']=sum(len(x['child_assertions']) for x in rev['records']);assert(pr['manual_parent_groups'],pr['primary_clause_atoms'])==(654,1890);pr['same_context_current_full_R']=r_count;pr['same_context_current_full_F']=f_count;pn='wp23-formal-parent-dispositions.v1.json';pd=rd(C/pn);pr['formal_parent_dispositions'].append(dict(**ident(C/pn),formal_files=2,nonempty_parents=pd['nonempty_parent_count'],new_atoms=0,whole_task_acceptance=False))
ld=rd(C/'reading-ledger.json');ld['discovered_dependencies'].append(newfull);ld['own_new_complete_named_units'].append(dict(recorded_utc=utc,packages=names,new_partial_units=len(partial),whole_sources_new=1,qualification='All units/source slices actual ownread, equality check0 semanticcredit; currentMoves740 literal retrieval only, not740complete records.'));ld['same_context_full_ledger']=dict(path='../creature_a_atomic_reception/reading-ledger.json',R=r_count,F=f_count,recorded_utc=utc,new_votes=0)
interfaces=rd(C/'interfaces.json');interfaces['utc']=utc
for name,d in zip(names,ds):interfaces['records'].append(dict(id=f'C-OUT-{len(interfaces["records"])+1:02}',direction='ACTUAL_OWN_FINITE_CONTRIBUTION_AVAILABLE',**ident(C/name),actual_reader=reader,manual_atom_count=d['manual_atoms'],whole_domain_acceptance=False))
gaps=rd(C/'coverage-gaps.json');gaps['recorded_utc']=utc
for x in gaps['records']:
 if x['id']=='C-FORMAL-EXHAUSTION':
  done={x['path'] for x in pd['formal_identities'].values()};x['paths']=[p for p in x['paths'] if p not in done];x['already_manually_parent_disposed'].append(pn);x['meaning']='Three remaining wholeformal papers have actually fullread source/context packages, explicit compound physical-parent ledgers continue. Six papers now have parentdispositions; no global denominator/domainPASS.'
gaps['records'].append(dict(id='C-CHAMBER-NEGATIVE-POSITION-FOLLOWUP',status='EXPLICIT_FORMAL_UNRESOLVED_NOT_CALLED_SAFE',formal='wp23-shadow-hyper-and-purification.md:199',meaning='N01 normalboxmember/negativeleak/validdirectparty three layers reviewed. Leakedmember laterholding/moving allvariants notexhaustively traced; available source/consumer scope retained precisely, notmateriallimit or globalPASS.'))
ap=rd(A/'progress.json');ap['updated_utc']=utc;ap['own_full_reference_total']=r_count;ap['additional_reference_full_read']=r_count-ap['primary_reference_full_read'];ap['same_context_C_manual_atoms']=1890;ap['same_context_C_read_delta']='io/same-context-C-WP23-read-delta.v10.json'
check=dict(recorded_utc=utc,meaning_packages=len(pr['meaning_packages']),manual_groups=654,manual_children=1890,all_groups_accepted_false=all(x.get('accepted') is False for x in rev['records']),current_own_full_R=r_count,current_own_full_F=f_count,new_full_files=[p],new_partial_units=len(partial),formal_parent_artifacts=pr['formal_parent_dispositions'],formal_parent_count=sum(x['nonempty_parents'] for x in pr['formal_parent_dispositions']),formal_papers_with_parent_ledgers=6,remaining_primary_formal_papers_for_parent_ledger=3,primary_catalog_manual_vectors=261,related_growth_manual_vectors=63,related_evolution_manual_vectors=79,original_A102_comparison='Not rerun; lastactual08:33 io/wip-consistency-v3.json retained',global_denominator_frozen=False,whole_domain_acceptance=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');assert check['all_groups_accepted_false'] and check['formal_parent_count']==944
for p,data in [(C/'reverse-mapping.json',rev),(A/'reading-ledger.json',al),(C/'reading-ledger.json',ld),(C/'progress.json',pr),(C/'interfaces.json',interfaces),(C/'coverage-gaps.json',gaps),(A/'progress.json',ap),(C/'io/current-consistency-v10.json',check),(A/'io/wip-consistency-v10.json',check),(A/'io/same-context-C-WP23-read-delta.v10.json',dict(recorded_utc=utc,full=[newfull],partial_units=partial,new_votes=0))]:wr(p,data)
for p in [C/'review.md',A/'review.md']:
 with p.open('a') as f:f.write(f'\n\n{utc} WIP maintenance v10: own samecontext FULL R106/F25, C26meaningpackages/654groups/1890children/allacceptedfalse. WP23 main199+data241 parent350/manual50groups freeze and3previous parentartifacts together sixpapers944nonempty, no common denominator. Optional data remain unactivated; all131/18/4/25tablevectors exactrawbindings, realScreen/Snil/S0/1331prefix/N01three layers/rawnilfalse preserved. SourceMissingEffect fallback vs rawPP0 guard frozen, currentMoves740 onlyliteral retrieval. Three remaining formal parentledgers,20declared not-wholePBS and priorA/history/negativeleakfollowup OPEN continue. NOT_EXECUTED/UPDATE_NOT_STARTED/no newvotes.\n')
print(json.dumps(check,ensure_ascii=False))
