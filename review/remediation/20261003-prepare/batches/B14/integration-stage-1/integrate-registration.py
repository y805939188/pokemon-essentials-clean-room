"""Current pre-freeze G navigation completion; owned document bookkeeping only.
The initial one-time registration recipe is superseded before first freeze.
This driver edits only own G metadata and the24 pending TSV tails.
"""
import bookkeeping as k
import json,copy,csv,io,pathlib,hashlib
G=k.G;BP='review/remediation/20261003-prepare/batches/B14/';P='review/remediation/20261003-prepare/'
reg=json.loads((G/'finding-registration.json').read_text());oldreg=copy.deepcopy(reg)
before_registration=k.identity((G/'finding-registration.json').read_bytes(),(G/'finding-registration.json').as_posix(),'FIRST_COMPLETED_PREFREEZE_G_METADATA')
first_snapshot=k.identity((G/'intended-snapshot.json').read_bytes(),(G/'intended-snapshot.json').as_posix(),'FIRST_COMPLETED_G_SNAPSHOT_DESCRIPTION_HELD_BY_COORDINATOR')
source=k.obj(k.C,BP+'candidate-1/contributions.json')['contributions'];review=k.obj(k.B['report_bindings'][0]['report_commit'],BP+'review-round-3/contribution-review.json')['records'];overlay=k.obj(k.C,BP+'candidate-2/fix-response.json')['successor_local_traceability'];by={a['id']:a for a in source}
# Explicit document-specific navigation after precise current clause/frozen mapping rereads.
plan={
'GIR-FD82-002':{'WP59':[('§5.7/§7','FLY cleanup and conditional signpost reader')]},
'GIR-FD82-003':{'WP59':[('§2/§4.5/§5.1–5.3/§6','Local capability/display concepts, stages and independent state')],'Berry':[('§2–3/§5.1/§6.1/§8','Per-plot state, settlement entry, dispatch and invariants')],'WP61':[('§2/§3.2/§7.3','Shared handled state, ordered notices and restoration identity')],'Fishing':[('§2/§6.1–6.2','Retained temporary-state/start/end caller reader; no additional repair claimed')]},
'GIR-FD82-C003':{'WP59':[('§3.5/§4.3','Qualified time data and connected duration ordering'),('§5.3/§5.4/§5.7/§7','C2 shared FLY prerequisite/exception overlay via WT28/39/40')],'Fishing':[('§6.1','Valid start-event prerequisite and restored FS16')],'WP61':[('§5/§6.2','Poison configuration/period and infected-member daily fixture')],'Berry':[('§5.2','C2 shared BP18 timestamp/early-return fixture; no new root or repair')]},
'GIR-FD82-C007':{'WP59':[('§3.5','Complete hourly data/cache input')],'Berry':[('§3.3/§5.4','Preserved sample/default, rounding and conditional content boundary')]},
'GIR-FD82-C086':{'WP59':[('§5.3/§5.7','DIVE and independent surfacing entries')]},
'GIR-FD82-C087':{'WP59':[('§5.3','Full obstacle markers and facing-event qualification')]},
'GIR-FD82-C088':{'WP59':[('§5.3/§5.4/§5.7/§7','Travel fields and C2 FLY normal/throwing callback overlay')]},
'GIR-FD82-C089':{'WP59':[('§5.6','Shared field presentation/caller boundary')]},
'GIR-FD82-C091':{'WP59':[('§3.3','Calendar candidate matching and independent name writes')]},
'GIR-FD82-C092':{'WP59':[('§4.1/§4.5','Splash reset/ordinary update and display guards')]},
'GIR-FD82-C093':{'WP59':[('§4.1/§4.5','Nine-weather data/resources and display guards')]},
'GIR-FD82-C094':{'WP59':[('§4.3/§4.5','Enter duration0/connected20 and display consumption')]},
'GIR-FD82-C095':{'WP59':[('§5.3/§5.7','WATERFALL activation gate and outer result boundary')]},
'GIR-FD82-C097':{'WP59':[('§5.8','Escape producer/clearer and presentation order')],'WP61':[('§7.1','Escape producer/consumer cross-reference')]},
'GIR-FD82-C098':{'Fishing':[('§2/§3.1/§8/§9','Current-square outward passage/facing terrain boundary')]},
'GIR-FD82-C099':{'Fishing':[('§2/§4/§9','Input-before-strict-timeout boundary fixture')]},
'GIR-FD82-C100':{'Berry':[('§2–3/§5.1/§5.4','Stored mulch, frozen mechanism and settlement entry'),('§5.2','C2 common duration/stage/timestamp overlay')]},
'GIR-FD82-C101':{'Berry':[('§6.2','Watering writes and current-config feedback')]},
'GIR-FD82-C102':{'Berry':[('§5.3','Nonzero sparkle qualification/empty-ground exclusion')]},
'GIR-FD82-C103':{'WP61':[('§3.1–3.2','Any-mover erasure, cap and notice order')]},
'GIR-FD82-C104':{'WP61':[('§2/§3.1–3.2','Actual movement versus direct post-step/NPC/ordinary entries')]},
'GIR-FD82-C105':{'WP61':[('§3.2/§9','Battery suppressors, latch and configuration')]},
'GIR-FD82-C106':{'WP59':[('§5.8','Cave geometry/color/time requests')],'WP61':[('§7.1','Preserved escape/presentation cross-reference')]},
'WP80-INTAKE-R01':{'WP59':[('§4.2','ASCII Weather grammar; correct original preserved')]}}
assert set(plan)=={r['id'] for r in reg['dispositions']}
records={};oldpaths=set();newpaths=set()
for ordinal,rec in enumerate(reg['dispositions']):
 ident=rec['id'];r=review[ordinal];assert r['id']==ident
 docplans=copy.deepcopy(plan[ident]);shared=ident in ['GIR-FD82-003','GIR-FD82-C003','GIR-FD82-C007']
 if shared:docplans['WP59']+=[('§3.5/§3.6','C3 separate consumer explanation/protected consumer neighbor')]
 designs={label:[dict(document_label=label,selector=sel,description=desc,scope_role='Named reviewed local contribution/retained reader; actual interpretation pending',provenance=[rec['author_record'],rec['full_candidate_disposition']],quality_interpretation='PENDING_EIGHT_EXACT_ACT_ULTRA_GATES') for sel,desc in items] for label,items in docplans.items()}
 locations=[k.bind_current_document(k.DOCUMENT_LABELS[label][1],ds) for label,ds in designs.items()]
 originals=set(by[ident]['original_application_paths'])
 for ov in overlay:
  if ov['id']==ident:originals.update(l['path'] for l in ov.get('locations',[]) if l['path'].startswith('specs/'))
 if shared:originals.add(k.DOCUMENT_LABELS['WP59'][0])
 for path in sorted(originals):
  label=next(label for label,paths in k.DOCUMENT_LABELS.items() if path in paths)
  if label=='WP16':continue
  ds=copy.deepcopy(designs.get(label,[]))
  if ident=='GIR-FD82-003':ds=[dict(document_label='WP59',selector='§3.5/§3.6',description='C3 approved original suffix/protected consumer; no original architecture neutralization',scope_role='C3 original synchronization and retained neighbor context',provenance=[rec['C3_successor']],quality_interpretation='PENDING_EIGHT_EXACT_ACT_ULTRA_GATES')]
  assert ds,(ident,path)
  for d in ds:d['scope_role']='Current original counterpart of the named qualified contribution/overlay; no broader original write or whole-document approval'
  locations.append(k.bind_current_document(path,ds))
 if ident=='GIR-FD82-C092':
  for path in k.DOCUMENT_LABELS['WP16']:
   locations.append(k.bind_current_document(path,[dict(document_label='WP16',selector='§5.1.1',description='Single approved splash sentence; frozen overlay §5.1 remains historical audit label',scope_role='Exactly one authorized original/final sentence',selection_kind='SINGLE_AUTHORIZED_SPLASH_SENTENCE',provenance=[rec['candidate_AREG_overlay_records'][0]['old_entry'],dict(commit=k.C,path=BP+'candidate-2/amendment-application.json')],quality_interpretation='PENDING_EIGHT_EXACT_ACT_ULTRA_GATES')]))
 if shared:
  final=k.DOCUMENT_LABELS['WP59'][1];ds=[dict(document_label='WP59',selector='§9',description='C3 final WT01–WT44 navigation only',scope_role='Final navigation clause, not original §9 dependencies',provenance=[rec['C3_successor']],quality_interpretation='PENDING_EIGHT_EXACT_ACT_ULTRA_GATES')]
  current=next(l for l in locations if l['path']==final);extra=k.bind_current_document(final,ds)
  for field in ['clauses','clause_bindings','current_heading_locators']:current[field]+=extra[field]
 oldpaths.update(l['path'] for l in rec['current_formal_locations']);newpaths.update(l['path'] for l in locations)
 rec['current_formal_locations']=locations;rec['current_locator_derivation']=(G/'clause-location-bindings.json').as_posix()+'#records/'+ident
 rec['candidate_AREG_overlay_records_role']='Frozen author audit fields retained verbatim as history; current_formal_locations supplies current document/section association.'
 rec['current_G_quality_interpretation']='PENDING_ALL_EIGHT_EXACT_ACT_ULTRA_GATES; navigation completion is writer bookkeeping only'
 records[ident]=dict(record_key=rec['record_key'],frozen_mapping_inputs=[rec['author_record'],rec['full_candidate_disposition'],rec['C3_successor']],current_formal_locations=copy.deepcopy(locations),derivation='Explicit per-document design from frozen qualified mappings and exact current clause reread; every named sibling is expanded and exact heading tokens do not match descendants.',retained_fishing_reader=ident=='GIR-FD82-003',canonical_scope_added=False,actual_quality_verdict=None)
assert oldpaths<=newpaths
for old,new in zip(oldreg['dispositions'],reg['dispositions']):
 for field in ['complete_current_control_fields','complete_minimum_acceptance_fields','upstream_obligations','downstream_obligations','source_lineage','current_test_rows','candidate_AREG_overlay_records','original_application_paths','candidate_receipts','original','approved_acceptance','whole_original_object_sha256','whole_acceptance_object_sha256']:assert old[field]==new[field],(new['id'],field)
k.save('clause-location-bindings.json',dict(run_id=k.B['run_id'],stage='B14-G',status='CURRENT_PREFREEZE_NAVIGATION_NOT_QUALITY_REVIEW',records=records,record_count=24,formal_scope=dict(original=5,final=7,total=12),policy='Frozen combined labels retain exact audit identities; current per-document locators are derived here. No foreign same-number match. WP16 single sentence binds5.1.1 and exact bytes; parent5.1 is context only.',all_actual_gates_pending=8,acceptance=False,new_canonical=0))
k.save('finding-registration.json',reg)
public_before=[];byreg={r['id']:r for r in reg['dispositions']}
for path in [P+'approval-ledger.tsv',P+'traceability-successor.tsv']:
 before=pathlib.Path(path).read_bytes();public_before.append(k.identity(before,path,'FIRST_COMPLETED_PREFREEZE_G_PUBLIC'));accepted=k.git(k.A,path);assert before.startswith(accepted)
 reader=csv.DictReader(io.StringIO(before.decode()),delimiter='\t');cols=reader.fieldnames;allrows=list(reader);assert len(allrows)==194
 out=io.StringIO(newline='');writer=csv.DictWriter(out,fieldnames=cols,delimiter='\t',lineterminator='\n')
 for row in allrows[170:]:
  rec=byreg[row['finding_id']];ob=json.loads(row['remaining_obligations']);assert ob['batch']=='B14'
  ob.update(current_clause_bindings=(G/'clause-location-bindings.json').as_posix()+'#records/'+rec['id'],pre_freeze_metadata_correction=(G/'pre-freeze-navigation-correction.json').as_posix(),current_locator_quality='Pending all8 ACT reviewers; writer navigation self-check only');row['remaining_obligations']=json.dumps(ob,ensure_ascii=False,separators=(',',':'))
  if 'current_clause_inputs' in row:
   v=json.loads(row['current_clause_inputs']);v.update(formal=rec['current_formal_locations'],current_clause_bindings=ob['current_clause_bindings'],pre_freeze_metadata_correction=ob['pre_freeze_metadata_correction']);row['current_clause_inputs']=json.dumps(v,ensure_ascii=False,separators=(',',':'))
  writer.writerow(row)
 pathlib.Path(path).write_bytes(accepted+out.getvalue().encode())
oldconfig=copy.deepcopy(k.B['configuration']);newconfig=copy.deepcopy(oldconfig)
newconfig['admitted_evidence']='Externally supplied coordinator observation of supported actual CLI xhigh/default Standard, thread.started, turn.started and94 completed original-run commands; no observed setting incompatibility/error/silent downgrade. Not a writer-observed or effective-backend certificate.'
newconfig['coordinator_observed_original_execution']=dict(model='gpt-6.1-sol',effort='xhigh',service_tier='default documented Standard',events=['thread.started','turn.started'],completed_commands_original_run=94,setting_incompatibility_observed=False,setting_error_observed=False,silent_downgrade_observed=False,evidence_source='External coordinator continuation instruction',backend_effective='UNVERIFIED under approved Plan A')
newconfig['continuation_actual_parameters']='Externally supplied same gpt-6.1-sol/xhigh/default documented Standard; no writer probe/settings change.'
def replace_config(v):
 if isinstance(v,dict):
  if v==oldconfig:return copy.deepcopy(newconfig)
  return {a:replace_config(x) for a,x in v.items()}
 if isinstance(v,list):return [replace_config(x) for x in v]
 return v
for path in G.glob('*.json'):
 if path.name in ['intended-snapshot.json','integration-manifest.json']:continue
 value=json.loads(path.read_text());after=replace_config(value)
 if value!=after:path.write_text(json.dumps(after,ensure_ascii=False,indent=2)+'\n')
k.save('pre-freeze-navigation-correction.json',dict(run_id=k.B['run_id'],stage='B14-G',status='AUTHORIZED_PREFREEZE_METADATA_COMPLETION_SELF_CHECK_ONLY',observations=[dict(issue='Early six-final instruction reused in current full ACT request',resolution='Current12 paths are five original/seven final including WP16; frozen earlier labels preserved at original input.'),dict(issue='Combined foreign labels and first-number/prefix lookup gave wrong/incomplete heading association',resolution='All24 current records explicitly derived per document, all named range/combined sections retained, true Fishing shared003 reader and exact WP16 single-sentence5.1.1 bindings.')],first_completed_snapshot_description=first_snapshot,before_registration=before_registration,before_public_TSVs=public_before,current_mapping=(G/'clause-location-bindings.json').as_posix(),reading=dict(final_WP59=[1,333],final_Fishing=[1,144],final_Berry=[1,197],final_WP61=[1,199],final_WP16=[136,165],original_WP16=[157,193],original_selected_counterparts='Exact headings and bounded corresponding clauses at supplied C3; all approved bytes preserved.',truncations_supplemented=['Final WP61 78–128','Original Fishing35–74/114–136 and Berry36–75/90–135/168–177'],in_scope_unread_remaining=[]),config_evidence=newconfig,privacy_scope='Complete own new records and new public content only; unchanged historical predecessor locator remains byte-exact. Approved216 copies are identity-checked and never rewritten.',canonical_OPEN=229,canonical_CLOSED=0,new_canonical=0,accepted_stats='9/21;170accepted142touched109primary;minimum109;strict100+9pending',accepted_B14=0,pending_contributions=24,public_total=194,actual_commit=None,actual_reviews_dispatched=0,actual_gates_pending=['FULL','B02','B03','B04','B06','B07','B08','B09'],C='NOT_PERFORMED',runtime_observations=0,proven_Demo_chains=0,behavior_vectors_executed=0,reference_or_historical_program_execution=0,writer_independent_PASS=False,acceptance=False))
print('Current bindings24 completed; both24-row TSV tails refreshed with all170 accepted row bytes intact.')
