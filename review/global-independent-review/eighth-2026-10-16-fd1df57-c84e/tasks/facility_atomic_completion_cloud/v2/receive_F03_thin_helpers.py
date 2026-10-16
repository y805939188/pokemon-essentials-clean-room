import datetime, hashlib, json, pathlib, subprocess

v = pathlib.Path(__file__).resolve().parent
utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(n): return json.loads((v/n).read_text())
def save(n, o): (v/n).write_text(json.dumps(o, ensure_ascii=False, indent=2)+'\n')
def sha(b): return hashlib.sha256(b).hexdigest()
f = load('forward-mapping.json'); r = load('reverse-mapping.json')
assert len(f['atoms']) == 2380
identity = f['source_identities']['R08']
raw = subprocess.check_output(['git', '-C', identity['repo'], 'show', identity['commit']+':'+identity['path']])
assert len(raw) == identity['bytes'] and sha(raw) == identity['sha256']
lines = raw.decode().splitlines(keepends=True)
units = []
for name, lo, hi in [('global_getter',4,7), ('battle_delegate',9,11), ('eligible_helper',14,16), ('moveto2_class',55,63), ('event_query_class',68,72), ('begin_speech',91,96)]:
    text = ''.join(lines[lo-1:hi]); units.append({'id':name,'source':'R08','lines':[lo,hi],'text':text,'bytes':len(text.encode()),'sha256':sha(text.encode())})
premise = 'Fixed R/B8/no later override; ordinary valid global/session/player/rules/table/message objects and normal prior dependencies to the stated observation. Static reached calls, reference assignments and explicit failure prefixes only; no Ruby/game/native execution. Save native serialization/IO and engine selection remain qualified by prior finite receipts, not inferred from these helpers. Direct invalid/tool inputs do not assert ordinary Demo reachability.'
specs = [
 ('global_getter4–7','Falsey global challenge triggers construction and assignment of a new BattleChallenge; truthy existing value is returned directly without validation, reset or cloning. A constructor failure occurs before the assignment, and this getter adds no rescue.',[15]),
 ('battle_delegate9–11','Public battle helper calls the current global challenge pbBattle and returns that result directly; it adds no decision write, AddWin, save, argument transformation or rescue.',[118,120]),
 ('eligible_helper14–16','The variadic eligibility helper ignores its supplied arguments and calls current challenge rules.ruleset.hasValidTeam? on the current player party. It is the existence-of-team query, not final selected-team validity, and has no independent inProgress guard or local rescue.',[110]),
 ('moveto2_class55–63','Save-position helper moveto2 writes x, then y, then real_x=x*REAL_RES_X, real_y=y*REAL_RES_Y, then prelock_direction=0. Its body contains no ordinary moveto transfer/events/vehicle/heading update. Later arithmetic failure leaves earlier coordinate writes; normal temporary-save and restoration use this thin helper rather than ordinary map transfer.',[63,131]),
 ('event_query_class68–72','Game_Event in-challenge query delegates through the global challenge getter to the challenge in-challenge method, whose current meaning is inner inProgress even while resting; it does not read a separate event-local flag or clear pause.',[113]),
 ('begin_speech91–96','Begin-speech helper first checks inProgress and returns literal ellipsis when inactive before loading trainers. Active path separately loads trainers for currentChallenge, reads nextTrainer, then uses a truthy selected record field2 as the FRONTIER_INTRO_SPEECHES lookup key; falsey selected record returns ellipsis.',[112]),
 ('begin_speech91–96','Begin-speech helper has no broad rescue: active table/index/message lookup failures propagate after the preceding calls. The falsey-record ellipsis branch does not establish a fallback for every malformed record or message failure; graphics fallback is separately bounded by existing FAC-A2254.',[112,133]),
]
facts = []
for number, (loc, assertion, receivers) in enumerate(specs,2381):
    a={'id':f'FAC-A{number:04}','source':'R08','unit_locator':loc,'assertion':assertion,'formal_receivers':[f'F03-L{x:04}' for x in receivers],'premise':premise,'pending_dependencies':[],'status':'NECESSARY_F03_THIN_HELPER_STATIC_MEANING','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud'}
    facts.append(a); f['atoms'].append(a)
    for line in receivers:
        r['mappings'].append({'formal_clause':f'F03-L{line:04}','formal_child_id':f'FAC-F03-THIN-{number}-{line}','atomic_assertion':a['id'],'meaning':assertion,'source':'R08','source_unit':loc,'premise':premise,'status':'FINITE_NECESSARY_SOURCE_JOIN','pending_dependencies':[],'relation':'EXPLICIT_NEW_THIN_HELPER_MEANING'})
packet={'schema':'FAC-F03-necessary-thin-helper-new-meaning-reception/v2','utc':utc,'reader':'/root/facility_atomic_completion_cloud','source_identity':identity,'complete_units':units,'facts':facts,'actual_read':'Complete R08 first101 lines earlier in this actual context; fresh complete4–16/55–72/91–96 delivered in tools cell2c? (tool receipt text retained in session); all six complete units printed without truncation. Prior own full R08 fixed identity remains separate.','premise':premise,'existing_graphic_qualification':'FAC-A2254 already explicitly excludes resolver-before-begin and fallback-setter failures; no new graphic finding or source atom.','new_required':0,'new_optional':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
# Do not fabricate an opaque tool receipt ID; actual content/ranges and file identity are the evidence.
packet['actual_read']='Complete R08 first101 lines earlier in this actual context; fresh complete4–16/55–72/91–96 delivered without truncation. All six complete units below actually read, with original LF preserved and exact fixed-source identity. No inherited reader FULL.'
name='F03-thin-helper-complete-new-meanings.v2.json'; save(name,packet)
f.setdefault('v2_increments',[]).append({'path':name,'count':len(facts),'ids':[x['id'] for x in facts],'utc':utc});f['bounded_denominator']=len(f['atoms']);save('forward-mapping.json',f);save('reverse-mapping.json',r)
l=load('reading-ledger.json');l.setdefault('v2_additional_source_reads',[]).append({'utc':utc,'packet':name,'actual_read':'Fresh complete R08 units4–16/55–72/91–96, all visible and no truncation. Earlier wholeR08 reused by fixed reference.','qualification':'Seven actual thin-helper meanings; graphics already qualified inA2254; no new business/native execution or whole domain approval.'});l['updated_utc']=utc;save('reading-ledger.json',l)
b=(v/name).read_bytes();print(json.dumps({'packet':name,'bytes':len(b),'sha256':sha(b),'facts':len(facts),'assertions':len(f['atoms'])}))
