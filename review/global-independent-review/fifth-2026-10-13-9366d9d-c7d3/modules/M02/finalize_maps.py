from record import *
from build_maps import anchors, units
# Only actual finite consumer/counterevidence scopes receive signoff, never whole shared documents.
D=[
('engine-overworld/wp11-map-topology-transfer.md',[(74,150)],'start metadata world_entry mapfactory mapnotify','M02 world recovery projection; full topology excluded'),
('engine-overworld/wp13-map-events-npc-followers.md',[(26,64),(94,106)],'start metadata world_entry timer','persistent records/Cut Scene boundaries; full interpreter/events excluded'),
('engine-overworld/wp13-interpreter-command-matrix.md',[(10,45),(136,140)],'timer variables switches selfswitches varhelpers','read full shown rows but only state/timer/failure projections signed'),
('engine-overworld/wp15-resource-matching-and-audio.md',[(20,48),(115,163)],'resources file system','file/resource/audio persistence projection; actual media not signed'),
('engine-overworld/wp59-world-time-weather-field-moves.md',[(22,99)],'calendar','clock/calendar/tone input contract only'),
('user-interface/wp65-title-load-options-pause-and-pc.md',[(24,144)],'main load_ui save_ui emergency default_values start','startup/save/settings only; preview rendering paragraphs read as context, not full UI signoff'),
('user-interface/wp63-pokegear-map-music-and-phone.md',[(68,131)],'phone_add phone_time phone_frame deprecation','phone timing/legacy entry/failed-public-query counterevidence; no full phone module signoff'),
('demo-dx/wp72-debug-contexts-and-controls.md',[(56,74),(230,241)],'debug console variables switches','debug logging and variable bounds only'),
('demo-dx/wp75-project-conversion-and-authoring-tools.md',[(187,188),(260,275)],'copy_move varhelpers','copy/move and variable helper projections; whole conversion tool not signed'),
('creature-rpg/wp33-daycare-and-breeding-session.md',[(51,75),(103,103),(165,176)],'daycare conversion_data stats','deposit statistics and migration counterevidence; only read matched paragraphs earlier'),
('creature-rpg/wp28-item-use-and-training.md',[(31,68),(105,155)],'condition handlers','handler copy/conditional resolution and teaching statistics projection'),
('pokemon-rules/wp21-dynamic-forms-and-display.md',[(256,302)],'condition conversion_data','handler sharing and markings migration projection only'),
('combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md',[(238,256)],'debug','ordinary exception wrapper counterevidence; loot text outside M02'),
('combat-requirements/wp51-ai-action-selection-and-skill.md',[(15,31),(106,106)],'debug','AI ordinary failure continuation projection'),
('combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md',[(15,48)],'handlers','combination utility consumer; exact source attachment below'),
('combat-requirements/wp58-battle-recording-and-playback.md',[(25,62),(87,116),(135,147)],'record file stream','recorded randomness/file-input projection'),
('pokemon-rules/wp60-berry-plants.md',[(1,197)],'berry_init berry conversion_data','entire current text read for negative evidence; only plant defaults/pick stats/absence of legacy mapping compared to source'),
('pokemon-rules/wp70-lottery.md',[(1,57)],'lottery variables varhelpers','entire shown lottery contract read; seed/state/variable boundary projection signed'),
('generic-kernel/wp03-content-identity-and-schema.md',[(31,57)],'validation','M01 validation/identity boundary only'),
('generic-kernel/wp04-pbs-lifecycle.md',[(38,49)],'errors main','M01 compiler exception projection; exact compiler source attached below')]
for rel,rr,keys,note in D:
 path=F+rel;p=Path(path);lines=p.read_text().splitlines();cs=[]
 for lo,hi,sec,kind,txt in units(lines):
  if not any(a<=lo<=b for a,b in rr):continue
  aa=anchors(keys)
  if 'wp54-' in rel:aa=[{'path':'Data/Scripts/019_Utilities/001_Utilities.rb','version':RV,'lines':[1,47],'entry':'combination iterator'},{'path':'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb','version':RV,'lines':[110,191],'entry':'combination consumers'}]
  if 'wp04-' in rel:aa.append({'path':'Data/Scripts/021_Compiler/001_Compiler.rb','version':RV,'lines':[1084,1117],'entry':'compiler error branch'})
  cs.append({'section_or_vector':sec,'lines':[lo,hi],'unit_kind':kind,'current_unit':txt,'source_anchors':aa,'result':'consumer/counterevidence projection only; '+note})
 covered=set(i for a,b in rr for i in range(a,b+1));unread=[]
 for i in range(1,len(lines)+1):
  if i in covered:continue
  if unread and unread[-1][1]==i-1:unread[-1][1]=i
  else:unread.append([i,i])
 mutate('spec-to-source','specifications',{'path':path,'version':B,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'review_extent':'partial','material_availability':'available_text','evidence_level':'static_bounded_consumer_projection','text_read_ranges':rr,'clauses':cs,'effective_supplements':[],'unreviewed_intervals':unread,'not_whole_document_signoff':True,'scope_note':note},'path')
# Audit index is source navigation, not evidence that any former pass applies here.
for rel,rr in [('audit/source-traceability.md',[(352,471),(1576,1577),(1642,1650)]),('planning/feature-matrix.md',[(152,156),(162,166),(318,319)]),(F+'scope-statement.md',[(86,126)])]:
 p=Path(rel);d={'path':rel,'version':B,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'review_extent':'partial','material_availability':'available_text','evidence_level':'scope_or_navigation_only','text_read_ranges':rr,'clauses':[],'effective_supplements':[],'unreviewed_intervals':'all other sections; administrative/history packages not recursively re-reviewed','not_behavioral_PASS_evidence':True}
 mutate('spec-to-source','specifications',d,'path')
# Narrow source-to-spec statuses are observations of contract presence, not final mandatory verdicts.
p=P/'source-to-spec.json';d=json.loads(p.read_text())
for x in d['capabilities']:
 if x['id'] in ['M02-MIGRATION-BERRY','M02-MIGRATION-MARKINGS']:x['classification']=['Generic Kernel','Pokémon Rules']
 elif x['id'] in ['M02-STATS','M02-STATS-DERIVED','M02-MIGRATION-DAYCARE','M02-MIGRATION-PLAYER-DEX']:x['classification']=['Generic Kernel','Creature-RPG']
 elif x['id']=='M02-MAP-RESTORE':x['classification']=['Generic Kernel','Engine / Overworld Integration']
 x['review_extent']='full_for_named_capability_scope'
 x['material_availability']='available_source_text; runtime/material restrictions as stated'
d['global_feature_matrix_projection']=[{'feature_id':fid,'matrix_path':'planning/feature-matrix.md','matrix_version':B,'review_result':state,'local_related_findings':ids,'write_policy':'Local projection only. Shared global Feature Matrix not modified under user scope restriction.'} for fid,state,ids in [
 ('F01-03','supported_static notification/menu mechanisms; conditional removal candidate',['GR5-M02-002']),('F01-04','supported_static plugin mechanism; U09 remains unresolved',[]),('F01-05','supported_static scoped time/steps/seed/stateful selection; ordinary helper input profile partial',[]),('F01-06','supported_static diagnostics with critical completion candidate',['GR5-M02-005']),('F01-07','supported_static wrappers/HTTP; archive stream candidate and host/material unknowns',['GR5-M02-003']),('F03-01','supported_static value registry/defaults; primitive-value boundary candidate',['GR5-M02-001']),('F03-02','supported_static migration selection/directory; old berry I/O data candidate',['GR5-M02-004']),('F03-03','supported_static startup/new/continue; real maps missing',[]),('F03-04','supported_static scoped recovery/backup/emergency; host/file effects unexecuted',[]),('F03-05','74 declaration rows and finite writer rules compared; missing event writers and BP won source unresolved',[])]]
(P/'source-to-spec.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Regression evidence is current source/current contract comparison; history only disambiguates identity.
reg={'schema_version':'gr5.review.v1','source_baseline':RV,'specification_baseline':B,'execution_status':'NOT_EXECUTED_THIS_REVIEW','regressions':[
 {'id':'GR4-M02-001','result':'supported_static','current':'WP06 §3.4 / TM15–19','source':'Utilities157–192 + Variables1–25','history':'130452d902530140331c21064a3188b7887f72ae M02 findings/probe-result-v2 read only'},
 {'id':'GR4-M02-002','result':'supported_static capture/propagation; exact Ruby2.6 exception from historical receipt only','current':'WP07 §4.2 / IO16–20','source':'HTTP1–83','execution':'No GR5 HTTP or Ruby call'},
 {'id':'GR4-M02-003','result':'supported_static conditional probability and state transitions','current':'WP06 §5.4 / TM20–23','source':'Utilities73–98','execution':'No statistical model/reference execution'},
 {'id':'GR3-M02-001','result':'supported_static current notification exception contract','current':'WP05 §3.3 / EP22–27','source':'Event1–91/Collections42–65/Overworld172–187'},
 {'id':'GR3-M02-002','result':'supported_static current duplicate persistence identity contract','current':'WP09 §3.1.1 / SV12–17','source':'SaveData_Value1–284'},
 {'id':'GR3-M02-003','result':'NO_REQUIRED','current':'WP65 §4.2 supplies both success messages; WP10 §5.2 separates actual backup state','source':'UI_Save1–24','reopened':False,'note':'Historical initial candidate wording was read solely for identity; current user NO_REQUIRED instruction and current counterevidence preserved.'}],
 'counterevidence_dismissals':[
 {'observation':'PBDebug ordinary errors may be swallowed even outside debug/internal logging gates','current_contracts':['WP42 §8','WP51 §2/4','WP72 §8.1'],'resolution':'already supported_static; no duplicate finding'},
 {'observation':'File.move is copy then source deletion with partial failure','current_contracts':['WP75 §11'],'resolution':'already supported_static; no duplicate finding'},
 {'observation':'daycare deposit increments before validity/capacity checks','current_contracts':['WP33 §3.2'],'resolution':'already supported_static; no duplicate finding'},
 {'observation':'nonarchive existence differs from first-byte readability','current_contracts':['WP15 §3.1'],'resolution':'already supported_static; no duplicate finding'},
 {'observation':'variable nil defaults, direct/utility refresh and 5000 boundary','current_contracts':['WP70 §2/5','WP72 §4.2'],'resolution':'removed from candidate001; only remaining boolean-value distinction retained'},
 {'observation':'phone migration can meet missing class-level lookup after a successful add','current_contracts':['WP63 §4.5–4.6','WP10 §4 phone global-object limitation'],'resolution':'shared consumer projection recorded; no new root for already documented missing lookup'}]}
(P/'regression-and-counterevidence.json').write_text(json.dumps(reg,ensure_ascii=False,indent=2)+'\n')
print('Supplementary projections and regression boundaries recorded')
