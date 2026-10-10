import subprocess,json,hashlib,re,collections,shutil
from pathlib import Path
r=Path('/workspace/pokemon-essentials-clean-room');a=r/'review/remediation/20261003-prepare/batches/B13/author-draft-1';a.mkdir(parents=True,exist_ok=True);p=Path('/tmp/B13-packet');base='8e67f780c204d593d89f364f585d2c6c2fe74631';ref='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';refrepo='/tmp/B13-reference-full'
def git(*args,repo=r):return subprocess.check_output(['git','-C',str(repo),*args])
def ident(data):return {'git_blob':subprocess.check_output(['git','hash-object','--stdin'],input=data,cwd=r).decode().strip(),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
def write(name,obj): (a/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
c=json.loads((p/'B13-downstream-contract.json').read_text());cs=json.loads((p/'original-and-acceptance-controls.json').read_text())
# Preserve complete controls and all management scope as exact source bytes, in own directory only.
for name in ['B13-downstream-contract.json','original-and-acceptance-controls.json','independent-review-requirements.json','affected-interface-map.json','catalog-locks.json','preparation-reuse-and-input-delta.json']:
 shutil.copyfile(p/name,a/name)
complete=(r/'review/remediation/20261003-prepare/batches/B09/candidate-2/source-limits.json').read_bytes();(a/'inherited-source-limits.json').write_bytes(complete)
limits=json.loads((p/'source-limits.json').read_text());limits.update({'author':'A-B13 only','current_reference_text_repository':'https://github.com/Maruno17/pokemon-essentials','reference_fixed_commit':ref,'reference_fixed_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','full_reference_checkout_executed':False,'reference_objects_fetched':True,'fresh_semantic_read_only':'Exact ranges in source-reading-log.json; whole Git path/name searches are text navigation only. Unlisted file/range content not claimed read.','new_bookkeeping_scripts':'/tmp/B13-edit.py, /tmp/B13-edit-recording.py, /tmp/B13-catalog.py, /tmp/B13-proposals.py, /tmp/B13-evidence.py and later own verification only; no historical programs executed','effective_configuration':'UNVERIFIED; requested xhigh author / ultra independent per packet; no model/CLI/native/quota audit','complete_inherited_limits_verbatim':{'path':str((a/'inherited-source-limits.json').relative_to(r)),**ident(complete)}});write('source-limits.json',limits)
reads=[];excerpts=[]
pattern=re.compile('条款|clause|冰|OHKO|经验|还原|取消|nil|多选|Arena|Palace|回放|心之水滴|范围|U01|G01|AX01|共享|子类|源对象|净化|族|语义')
for item in c['planned_reads']:
 i=item['input'];data=git('show',i['commit']+':'+i['path']);actual=ident(data);assert all(actual[k]==i[k] for k in ['git_blob','sha256','bytes']),i['path']
 own=item['path'] in c['allowed_formal_write_paths'];historic=item['path'].startswith('review/');original=item['path'].startswith('specs/');selected=[]
 if not item['path'].endswith('.json'):
  for num,l in enumerate(data.decode().splitlines(),1):
   if pattern.search(l):selected.append({'line':num,'text':l})
  # Limit to navigational bounded evidence, never imply whole-file semantic certification.
  selected=selected[:8]
 excerpts.append({'path':i['path'],'input_commit':i['commit'],'bounded_navigation_excerpt':selected,'not_full_read_proof':True})
 reads.append({**item,'identity_verified':True,'handling':'COMPLETE_OWN_SCOPE_COMPARE' if own else ('IMMUTABLE_CONTROL_AND_TARGETED_RECORD_REUSE' if historic else ('TARGETED_ORIGINAL_COMPARE' if original else 'UNCHANGED_CURRENT_DEPENDENCY_QUALIFIED_REUSE_AND_BOUNDED_LOOKUP')),'source_semantic_quality_pass_claim':False})
write('planned-inputs-52.json',{'management_packet':'e8caada4ab919e48e3dc817f0638ce595fde449c','formal_FIX_BASE':base,'formal_tree':c['accepted_baseline_tree'],'count':len(reads),'current':50,'immutable_original':2,'records':reads,'complete_historical_reread':False,'identity_is_not_semantic_read':True})
write('bounded-input-navigation.json',{'status':'READING_NAVIGATION_NOT_COVERAGE_CERTIFICATE','records':excerpts})
# Bind complete own canonical and acceptance objects by equality at their immutable sources.
orig=json.loads(git('show',c['fixed_original_findings']['commit']+':'+c['fixed_original_findings']['path']));approved=json.loads(git('show',c['fixed_approved_acceptance']['commit']+':'+c['fixed_approved_acceptance']['path']))
def find(obj,id):
 if isinstance(obj,dict):
  if obj.get('id')==id:return obj
  for v in obj.values():
   hit=find(v,id)
   if hit is not None:return hit
 elif isinstance(obj,list):
  for v in obj:
   hit=find(v,id)
   if hit is not None:return hit
for x in cs['controls']:
 assert find(orig,x['id'])==x['whole_original_object'],x['id'];assert find(approved,x['id'])==x['whole_approved_acceptance_object'],x['id']
write('control-binding-verification.json',{'all_8_whole_original_and_approved_equal':True,'current_qualified_controls_retained':True,'primary_ids':c['primary_finding_ids'],'contributions':c['contribution_finding_ids'],'B030_required':False,'canonical_state_changed':False})
# Complete catalog row locks, full per-row old/new proof, all old IDs survive in order with multiplicity.
def sections(s):
 out={};section=None
 for l in s.splitlines():
  if l.startswith('## '):section=l.split('：')[0][3:].split(':')[0]
  elif re.match(r'^\| (?:Q\d+|W\d+\w*|P\d+|[A-Z]{2}-\d+) \|',l):out.setdefault(section,[]).append(l)
 return out
def ids(rows):return [x.split('|')[1].strip() for x in rows]
locks=[]
for f in c['allowed_formal_write_paths'][-2:]:
 old=git('show',base+':'+f).decode();new=(r/f).read_text();os=sections(old);ns=sections(new);changes=[];added=[]
 for sec,rows in os.items():
  newrows=ns[sec];oldids=ids(rows);newids=ids(newrows);retained=[id for id in newids if id in set(oldids)];assert retained==oldids,(f,sec)
  od=dict(zip(oldids,rows));nd=dict(zip(newids,newrows));assert len(od)==len(rows);assert len(nd)==len(newrows)
  for id in oldids:
   if od[id]!=nd[id]:
    assert (f.endswith('combat-requirements-wp54-55-56-58.md') or (sec=='FC' and id=='FC-10')),(f,sec,id)
    changes.append({'series':sec,'id':id,'before':od[id],'after':nd[id]})
  for id in newids:
   if id not in od:added.append({'series':sec,'id':id,'text':nd[id]})
  if f.endswith('creature-rpg-wp35-36-57-64-68.md') and sec!='FC':assert rows==newrows,(sec,'other owner changed')
 locks.append({'path':f,'before':ident(old.encode()),'after':ident(new.encode()),'old_counts':{k:len(v) for k,v in os.items()},'new_counts':{k:len(v) for k,v in ns.items()},'old_ID_order_multiplicity_preserved':True,'other_owner_rows_byte_equal':True,'changed_old_rows':changes,'added_static_rows':added,'executed':0})
write('catalog-preservation.json',{'records':locks,'historical_count_correction':{'fixed_catalog_actual':{'QC':42,'WS':34,'PA':27,'RC':24,'total':127},'wrong_historical_labels':{'RC':23,'total':126},'new_catalog_actual':{'QC':47,'WS':35,'PA':28,'RC':26,'total':136},'delta':9,'immutable_historical_reports':['review/wp80-delivery-2026-10-03/batch-13/checks.json','review/wp80-delivery-2026-10-03/batch-13/clause-disposition.md','review/wp80-delivery-2026-10-03/batch-13/round-168-final-checks.json'],'historical_reports_edited':False,'no_missing_vector_or_behavior_inferred_from_bad_label':True}})
# Exact fresh source/read/caller/data locations, no source body copied into deliverables.
ranges={
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb':('38-50','B027; nil vs empty list submission and length return'),
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb':('196-230','B027; setParty active player write then registration; start holds old party'),
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb':('1-99','EXP save+adjust before item save; normal restore ordered player/enemy; no wrapper ensure'),
'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/004_Challenge_LevelAdjustment.rb':('1-82','complete EXP for both sides; same-level skip; per-index restore and partial failure'),
'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/005_Challenge_BattleRules.rb':('1-103','11 exact setting keys; 3 consumer-only keys; no shorthand sleep key'),
'Data/Scripts/011_Battle/007_Other battle code/006_Battle_Clauses.rb':('1-175;190-244;245-273','B003/B010/B025; user-side checkpoint differs from last-user draw; loaded Ice alias resolves parent; exact clause gates'),
'Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb':('70-134','original Ice target check and dedicated non-Ice accuracy penalty'),
'Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb':('360-402;700-719','save Perish source before faint clear; positive decision early exit'),
'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb':('279-351;540-573','startup all-entry path; positive-decision phase exits; selfKO ordinary judge'),
'Data/Scripts/011_Battle/008_Other battle types/004_BattleArenaBattle.rb':('1-200','success slot versus cumulative totals; opening resets, count>=3, persistent HP zero, sequential replacement preserves state'),
'Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb':('1-104;132-218;303-340;376-387','owner/candidate gates; helper closure; only participating callback at normal entry, no Arena active callback'),
'Data/Scripts/011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb':('23-145;153-255','Teleport/damage-switch/PartingShot/BatonPass nonrandom owner branch; forced switches random branch'),
'Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb':('154-173','ordered target switches/item/ability/self switch consumers during attack'),
'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb':('367-408','EmergencyExit/WimpOut owner branch; EOR defers vs attack direct choice'),
'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb':('447-471;1525-1563','EjectPack/EjectButton owner branch, RedCard random and candidate/immunity gates'),
'Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb':('64-84;174-234;236-257','returned switch value appends including -1; playback increments independent cursor; Arena record/playback inherit lifecycle'),
'Data/Scripts/014_Pokemon/001_Pokemon.rb':('1083-1098','HP/stat arithmetic legality for qualified data fixtures'),
'Data/Scripts/016_UI/005_UI_Party.rb':('1051-1141','default multi-entry confirms final legality; nil cancellation; empty wrapper boundary not normal UI claim'),
'PBS/moves.txt':('4562-4572;5718-5727;5961-5971','SHEERCOLD q30 OHKOIce; BatonPass user target; Growl normal status accuracy100'),
'PBS/pokemon.txt':('3-29;629-654;3453-3481;3508-3538','Bulbasaur/Pikachu/Lapras/Eevee identities, ordinary abilities, HP/stat values, legal Growl/PerishSong/BatonPass learn levels')}
sourcelog=[]
for f,(lines,purpose) in ranges.items():
 data=git('show',ref+':'+f,repo=refrepo);sourcelog.append({'repository':'reference','commit':ref,'path':f,'read_ranges':lines,'purpose':purpose,**ident(data),'whole_file_identity_not_full_semantic_read':True})
searches=[]
for pattern in ['pbRecordBattlerAsActive','pbRecordBattlerAsParticipated','pbOnAllBattlersEnteringBattle','pbSwitchInBetween','pbGetReplacementPokemonIndex']:
 raw=git('grep','-n',pattern,ref,'--','Data/Scripts',repo=refrepo).decode();locs=[]
 for l in raw.splitlines():
  pathline=l.split(ref+':',1)[1];m=re.match(r'(.+?):(\d+):',pathline);assert m;locs.append({'path':m[1],'line':int(m[2])})
 searches.append({'symbol':pattern,'scope':'all Data/Scripts tracked text at fixed reference','matches':locs,'count':len(locs),'text_navigation_only':True})
write('source-reading-log.json',{'reference_commit':ref,'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','records':sourcelog,'searches':searches,'unlisted_ranges_unread':True,'reference_execution':0,'behavior_vectors_executed':0,'whole_search_is_not_source_branch_coverage':True,'reused_proof':'Frozen controls full root+extension and qualified counterexamples; old exact metadata identifies immutable local proof. No full history/program rerun.'})
# Full four-file B12 delta, only necessary current interfaces refreshed.
paths=[x['path'] for x in json.loads((p/'preparation-reuse-and-input-delta.json').read_text())['changed_planned_current_inputs']];delta=git('diff','--binary','--no-ext-diff','--no-textconv','1d06c45cc0a744fca181ac80ee573cc9ebb9b862',base,'--',*paths);(a/'B12-four-input-delta.patch').write_bytes(delta)
write('B12-interface-refresh.json',{'four_current_input_delta':ident(delta),'paths':paths,'consumption':['Current B12 OHKOIce prediction still rejects Ice; do not replace actual target gate with AI prediction.','AI scores/power are read-only and do not perform true attack switching, HP restoration or item writes. PartingShot/BatonPass scoring does not bound actual attack-stage recording consumer reachability.','New B12 score/caller receipts and corrected field labels retained; no B12 formal outputs edited and no reapproval claimed.','Same four exact inputs are current-C hashes in planned-inputs-52; changed observations and B12 scope do not expand B13 formal writes.'],'new_behavior_execution':0})
# Package input/output identities, parent frozen base only.
outputs=[]
for f in c['allowed_formal_write_paths']:
 data=(r/f).read_bytes();before=git('show',base+':'+f);outputs.append({'path':f,'input':ident(before),'output':ident(data),'changed':before!=data})
write('formal-output-identities.json',{'FIX_BASE':base,'FIX_BASE_tree':c['accepted_baseline_tree'],'allowed_paths':c['allowed_formal_write_paths'],'records':outputs,'formal_output_count':7,'changed_count':sum(x['changed'] for x in outputs),'role':'AUTHOR_SELF_CHECK_NOT_INDEPENDENT_REVIEW'})
print('verified',len(reads),'planned inputs;',len(cs['controls']),'complete controls;',len(outputs),'formal outputs; catalog',[(x['old_counts'],x['new_counts']) for x in locks])
