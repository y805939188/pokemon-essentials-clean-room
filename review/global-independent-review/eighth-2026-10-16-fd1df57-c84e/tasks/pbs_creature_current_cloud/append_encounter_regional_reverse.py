from pathlib import Path
import json, hashlib, copy, datetime
P=Path(__file__).resolve().parent
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(n):return json.loads((P/n).read_text())
def freeze(n,d):
 p=P/n;assert not p.exists();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');b=p.read_bytes();return {'path':n,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
d=load('encounter19-regional2.complete.v1.json');M={x['id']:x for x in d['manual_finite_meanings']}
F36=d['complete_formal_units'][0]['identity'];F62=d['complete_formal_units'][1]['identity']
# Original package retained. Locator-only correction after exact heading read IO
# 1f3550, plus complete formal prose 3dc5f3,1d247b,470b69,63e600,cc1534.
correct={
 'ER01':[[49,54]],'ER02':[[56,67]],'ER03':[[56,67]],'ER04':[[56,67]],
 'ER05':[[84,98]],'ER06':[[69,82],[124,138]],'ER07':[[49,54]],
 'ER13':[[29,45],[55,57],[75,75]],'ER18':[[95,118]],'ER19':[[108,118]],'ER20':[[108,118]]}
locator={'schema':'gr8-encounter-regional-exact-formal-locator/v1','utc':UTC,
 'mandatory_for':'encounter19-regional2.complete.v1.json','original_retained':True,
 'corrections':[{'id':key,'original_complete_meaning':M[key],'correct_formal_ranges':value,
   'meaning_change':False,'note':'Original statement/source unit intact. This correction replaces only overbroad or misplaced formal navigation ranges; all complete formal text is included in the original package.'} for key,value in correct.items()],
 'qualification':'ER18 negative-region number lookup and ER20 unlocked? handling are additional source facts, not independently asserted new formal promises. Only the explicitly formal-backed subassertions in reverse addendum are matched.',
 'source_units':'All23 complete source units retained; no source-body omission from this locator correction.',
 'actual_full_read_IO':['1f3550','3dc5f3','470b69','1d247b','63e600','cc1534'],
 'new_formal_finding':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
locid=freeze('mandatory-encounter-regional-formal-locators.v1.json',locator)
clauses=[]
def atom(key,er,text,lines=None):
 m=M[er];ranges=([lines] if lines else correct.get(er,[m['formal']['lines']]))
 clauses.append({'id':'PCR-ER-'+key,'formal':{'path':m['formal']['path'],'ranges':ranges},
  'assertion':text,'complete_provider_meaning':'encounter19-regional2.complete.v1.json#/manual_finite_meanings/'+str(list(M).index(er)),
  'source_units':[{'identity':d['complete_source_units'][a['index']]['identity'],'lines':d['complete_source_units'][a['index']]['lines']} for a in m['source_units']],
  'actual_reader':'/root/pbs_creature_current_cloud','premises':d['common_premises'],
  'status':'FINITE_ASSERTION_MATCHED_SOURCE_STATIC','mandatory_companions':['mandatory-encounter-trigger-counter-clarification.v1.json',locid['path']],
  'evidence':'SOURCE_STATIC / DERIVED_VECTOR / NOT_EXECUTED',
  'qualification':'This individual assertion only; original complete record order/field data and extra source-only facts are not collapsed into whole-domain acceptance.'})

# Exact catalog fields, not26 new callbacks or any future UI ordering mandate.
for c in d['complete_EncounterType_catalog']:
 for field,value,desc in [('id',c['id'],'registered fixed author identity'),('type',c['type'],'type classification'),('effective_trigger_chance',c['effective_trigger_chance'],'effective default trigger probability')]:
  atom('CAT-'+c['id']+'-'+field,'ER05',f"EncounterType {c['id']} {desc}: {value}.",[84,98])
  clauses[-1]['value']=value;clauses[-1]['source_registration_lines']=c['source_lines'];clauses[-1]['scope']='Fixed catalog content; original registration ordinal retained in complete provider data, no UI sorting requirement inferred.'

specs=[
 ('QUERY-EXISTS','ER01','Exact existence query does not fall back to version0.'),
 ('QUERY-GET','ER01','Single get prefers requested version and falls back to map version0.'),
 ('QUERY-ORDER','ER01','Encounter enumeration sorts map ID then version.'),
 ('QUERY-ENUM-DEFECT','ER01','With normal symbol keys, v>0 enumeration can produce both v0 and requested version because fallback check uses an array key.'),
 ('COMPILE-CLEAR','ER02','Encounter compilation clears registry before processing files; no rollback of the reached clear or earlier registered sections.'),
 ('COMPILE-HEAD','ER02','Map/version decimal-prefix conversion and omitted version0 determine the actual composite identity.'),
 ('COMPILE-PRIOR','ER02','The prior section merges/sorts/registers before collision rejection of the new header; final archive save is later.'),
 ('COMPILE-SLOT','ER03','Existing type and digit-immediately-comma identify a slot; negative-leading weight instead fails as a type line.'),
 ('COMPILE-POSITIVE','ER03','Slot weight and levels are positive integers; unknown species rejects, omitted max becomes min, current level maximum and min<=max are enforced.'),
 ('COMPILE-REPLACE','ER04','Repeated type declaration replaces its prior slots independently of rate inheritance.'),
 ('COMPILE-RATE','ER04','Nonempty rate uses integer prefix; omitted/empty same-section rate retains previous value or takes type default.'),
 ('COMPILE-MERGE','ER04','Equal species and level bounds merge weights; final slots sort weight descending then species string ascending.'),
 ('SNAPSHOT-RATES','ER06','Setup creates fresh rate/table containers, copies rates and Marshal-clones slots from the selected registered record.'),
 ('SNAPSHOT-COUNTERS','ER06','Setup clears step_count but retains accumulator; reset_step_count independently clears both.'),
 ('TRIGGER-TRUE','ER06','A true radar or ordinary trigger return itself resets neither counter.'),
 ('VERSION-SAME','ER07','Integer validation precedes same-value early return; same value leaves snapshot and counters unchanged.'),
 ('VERSION-CHANGE','ER07','Different integer stores version then conditionally setups map when both required contexts exist.'),
 ('EDITOR-NEW','ER08','New encounter set rejects map/version collision and registers initially empty rates/types.'),
 ('EDITOR-COPY-EMPTY','ER08','Whole-set copy retains all rates and suffix but omits empty type entries; nonempty slots are cloned independently.'),
 ('EDITOR-DELETE','ER08','Confirmed set deletion affects registry before total-save decision.'),
 ('EDITOR-YES','ER09','Total encounter Yes saves archive before PBS and does not refresh the current-map snapshot.'),
 ('EDITOR-NO','ER09','Total encounter No reloads registry from archive without refreshing current-map snapshot.'),
 ('EDITOR-KEY','ER10','Changing set map/version moves the registry key, without writing global encounter_version.'),
 ('EDITOR-TYPE-NEW','ER10','Type keys, including empty lists, exclude new-type selection; a rate-only residual does not. New list starts empty with type default rate.'),
 ('EDITOR-TYPE-COPY','ER11','Single-type copy retains an empty target type and copied source rate, distinct from whole-set copy.'),
 ('EDITOR-TYPE-DELETE','ER11','Deleting a type removes both its rate and slot list.'),
 ('EDITOR-RATE','ER12','Rate editor accepts0..255, including legitimate0.'),
 ('EDITOR-TYPE-MOVE','ER12','Type rename moves rate and slot list to an unused key.'),
 ('EDITOR-SLOT-DEFAULT','ER12','New slot starts weight20, first Species base identity, and levels5/5.'),
 ('EDITOR-SLOT-COPY','ER12','Editing uses a slot clone, copying inserts an independent clone, deletion requires confirmation.'),
 ('EDITOR-SLOT-LIMITS','ER13','Slot editor offers positive weight1..999 and levels1..current maximum; reversed bounds swap after editing.'),
 ('EDITOR-SLOT-CANCEL','ER13','Species/form selection cancel preserves old identity; property-list BACK without save prompt still returns the edited slot to its caller.'),
 ('WRITER-EMPTY','ER14','PBS writer does not output nil or empty encounter type lists.'),
 ('WRITER-ZERO','ER14','Rate<=0 is omitted from the type line; successful later compile restores nonzero type default, while default-zero methods remain0.'),
 ('WRITER-LEVELS','ER14','Equal level bounds write a single level; unequal bounds write both.'),
 ('REG-HEADERS','ER15','Regional headers define an indexed cross-input list and reject a repeated index even when its first list is empty.'),
 ('REG-SPECIES','ER15','Species words use uppercase/strip and the two Nidoran aliases before exact registry lookup.'),
 ('REG-HOLES','ER15','Missing indexes fail at the final list pass; explicitly empty indexes and cross-file out-of-order completion are allowed.'),
 ('REG-ORDER','ER16','Authored regional line/token order forms the flattened numbering sequence.'),
 ('REG-DUPLICATE','ER16','Repeated species within one regional list reject in final validation; the same species in another list is allowed.'),
 ('REG-SAVE','ER16','Completely empty input can save an empty regional collection; successful compilation does not clear existing regional cache.'),
 ('REG-CACHE','ER17','Regional data lazily retains the whole loaded table in Game_Temp until an independent invalidation.'),
 ('REG-NUMBER','ER18','Regional number uses first matching base-species position+1, with0 for missing/empty list or unknown identity.'),
 ('REG-MEMBERS','ER18','Member query returns nil for negative/missing/empty regional list and otherwise an outer clone.'),
 ('REG-LENGTH','ER18','Negative regional length counts base species; missing positive list length is0.'),
 ('REG-UNLOCK-INITIAL','ER19','Only unlock index0 starts true; clear resets records while retaining unlocks.'),
 ('REG-COUNT','ER19','National count/seen-any use base registry; regional count/seen-any iterate members and fail if member query returns nil.'),
 ('REG-COUNT-UNLOCK','ER19','Regional counting does not check unlock.'),
 ('REG-ACCESS-CURRENT','ER20','Current-region accessible mode checks one selected region for seen content and ignores unlock state.'),
 ('REG-ACCESS-ORDER','ER20','Other accessible mode orders unlocked seen regional lists before unlocked seen national.'),
 ('REG-LOCK','ER20','Lock/unlock negative or out-of-range values target national and always recompute accessible lists.'),
 ('REG-NATIONAL-UNKNOWN','ER20','National-unlocked membership short-circuits true even for an unknown species identity.'),
 ('REG-EXPORT-CACHE','ER21','Regional export consumes retained cache, so successful compile can leave archive and subsequent exported PBS with different content.'),
 ('REG-EDITOR-CLONE','ER22','Regional main editor clones each cached list before reorder/copy/delete/fill.'),
 ('REG-EDITOR-CHILD-NO','ER23','Regional child entry compacts before initial clone, and return compacts again; child No therefore compresses holes.'),
 ('REG-EDITOR-CHILD-EMPTY','ER24','Regional child Yes has no terminating progress for an empty list; direct main blank-save is a separate path.'),
 ('REG-EDITOR-MAIN-YES','ER25','Regional main Yes orders archive save, cache invalidation, PBS export, message and exit; a later failure preserves reached prefix.'),
 ('REG-EDITOR-MAIN-NO','ER25','Regional main No discards working lists without saving or cache invalidation; Cancel continues.'),
 ('REG-EDITOR-FAMILY','ER26','Main family fill concatenates unique families from first unseen base species in definition order, with Species family ordering and valid-acyclic premises.')
]
for key,er,text in specs:atom(key,er,text)
old=load('reverse-mapping.json');assert old['atom_denominator_frozen_so_far']==2485
assert len({x['id'] for x in old['clauses']}|{x['id'] for x in clauses})==len(old['clauses'])+len(clauses)
freeze('reverse-mapping.v12.frozen.json',old)
add={'schema':'gr8-encounter-regional-reverse-addendum/v1','utc':UTC,'actual_reader':'/root/pbs_creature_current_cloud',
 'complete_packet':'encounter19-regional2.complete.v1.json','mandatory_locator_companion':locid,'common_premises':d['common_premises'],
 'new_atoms':len(clauses),'catalog_atoms':78,'consumer_atoms':len(specs),'clauses':clauses,
 'scope':'All26 catalog identities/classes/defaults and bounded individual producer/query/editor/cache assertions only. No whole WP36/WP62/WP73 or habitat/movement/battle transitive acceptance.',
 'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
add_id=freeze('encounter-regional-reverse-addendum.v1.json',add)
old['schema']='gr8-pbs-current-reverse/v13';old['utc']=UTC;old['supersedes']='reverse-mapping.v12.frozen.json retained'
old['clauses']+=clauses;old['atom_denominator_frozen_so_far']=len(old['clauses']);old['encounter_regional_addendum']=add_id|{'atoms':len(clauses),'catalog_atoms':78,'consumer_atoms':len(specs)}
for x in old['clauses']:
 if x['id'].startswith('PCR-DIR-003_EggGroup-'):
  x['root_adjudication']={'id':'GR8-PBS-EGGGROUP-DOMAIN-001','classification':'required','severity':'P3','receipt':'egggroup-root-decision-reception.v1.json','global_history_and_equivalent_directory':'OPEN','future_correction':'UPDATE_NOT_STARTED'}
old['directory_refinement']['current_EggGroup15']='ROOT_CLASSIFIED_REQUIRED_P3_FIXED_AUTHOR_DOMAIN; formal amendment/history/equivalent-directory reception remain OPEN'
(P/'reverse-mapping.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
p=load('proposals.json');p['utc']=UTC;p['mandatory']=[{'id':'GR8-PBS-EGGGROUP-DOMAIN-001','alias':'PC-QUERY-EGGGROUP-DOMAIN-01','classification':'required','severity':'P3','root_complete_contract_receipt':'egggroup-root-decision-reception.v1.json','bounded_scope':'Explicit incorporation of all15 fixed valid EggGroup author IDs only','status':'ROOT_CLASSIFIED_BOUNDED; GLOBAL_HISTORY_AND_EQUIVALENT_DIRECTORY_RECEPTION_OPEN','counting':'Root existing stable finding only; no new independent context/vote or inferred global count increment.'}]
p['status']='One root-classified bounded required P3 with full-history/equivalent-directory condition OPEN; no optional finding. Review continues.'
p['finite_review_requests'][0].update(status='ROOT_CLASSIFIED_BOUNDED_REQUIRED_P3_GLOBAL_HISTORY_OPEN',canonical_id='GR8-PBS-EGGGROUP-DOMAIN-001',root_receipt='egggroup-root-decision-reception.v1.json',new_required=0)
(P/'proposals.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':UTC,'mandatory_locator':locid,'reverse_addendum':add_id,'new_atoms':len(clauses),'current':len(old['clauses']),'root_required_canonical':'GR8-PBS-EGGGROUP-DOMAIN-001','new_business_or_numeric_execution':0},ensure_ascii=False))
