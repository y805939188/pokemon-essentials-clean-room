"""Record actual bounded receptions and already-read necessary cache/fog source units."""
import collections
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

BASE=Path(__file__).resolve().parent
REPORT=BASE.parent.parent
R=Path('/workspace/pokemon-essentials')
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def read(n):return json.loads((BASE/n).read_text())
def write(n,v):
 b=(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode();(BASE/n).write_bytes(b)
 return {'path':str((BASE/n).relative_to(REPORT)),'bytes':len(b),'sha256':sha(b)}
def identity(path):
 raw=(R/path).read_bytes();fixed=subprocess.check_output(['git','show',COMMIT+':'+path],cwd=R);assert raw==fixed
 return {'repo':str(R),'commit':COMMIT,'path':path,'bytes':len(raw),'sha256':sha(raw),'blob':subprocess.check_output(['git','rev-parse',COMMIT+':'+path],cwd=R,text=True).strip(),'reader':'/root/kernel_atomic_reception','whole_source_read':True}
rootpath=REPORT/'adjudication/root-hash-default-scope-counterreview.v1.json'
raw=rootpath.read_bytes();assert len(raw)==26953 and sha(raw)=='4d664147409b5f29ade6715db8183f8b4c27570b64ab052530fc103c8fb54cb2'
(BASE/'received/root-hash-default-counterreview-4d664147.json').write_bytes(raw)
receipt=write('received/root-hash-default-counterreview-reception.v1.json',{
 'utc':NOW,'provider':'/root','receiver':'/root/kernel_atomic_reception','candidate':'GR8-KAR-001','original_frozen_candidate':'candidate-hash-default-boundary.v1.json','provider_full_payload':{'path':str(rootpath.relative_to(REPORT)),'bytes':len(raw),'sha256':sha(raw)},
 'actual_full_reception':'All fields, embedded complete original proposal, all6 identity checks, all8 counter sections and limits actually read in two untruncated outputs7e61ad/0552cf. Actual I/O io/root-hash-default-counterreview-complete-first.json and -tail.json.',
 'accepted':'NO_REQUIRED_BOUNDED_SCOPE, no objection. Whole WP09 explicitly states missing lookup participates as nil. H1 changes that premise to StringD, so preserves a true callable-source conditional fact but does not refute the finite nil-result rule. Full strongest registration-only/leading phrase/SV08/unnormalized-loadedHash counterarguments retained in provider payload.',
 'required_added':0,'optional_added':0,'new_contexts':0,'new_independent_votes':0,
 'preserve':['nil-default absent-key and explicit wrong-type rejection','presence-based load/newgame supplier and loaded flags','H1 conditional source fact without mandatory nativeHash compatibility','SV08/09 and separately bounded KER001/002/003'],
 'not_claimed':['H1 unreachable or unserializable','source rejects H1','actual Marshal/Ruby/game execution','exact historical missing-key qualification fully received','global save or history PASS'],
 'history':'OPEN exact prior missing-key qualification; no old CLOSED reopened','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})

ledger=read('reading-ledger.json')
for x in ledger['records']:
 if x.get('path')=='Data/Scripts/004_Game classes/005_Game_MapFactory.rb':
  x.update(actual_read_ranges=[[1,506]],whole_file_read=True,reading_evidence=['io/wp09-mapfactory-needed-full-first.json','io/wp09-mapfactory-needed-full-tail.json','io/wp04-independent-connection-cache-complete-module.json'],credit='ACTUAL_COMPLETE_SOURCE_READ; exact prior helper I/O navigation corrected, no new read credit')
 if x.get('path')=='Data/Scripts/012_Overworld/002_Overworld_Metadata.rb':
  x.update(actual_read_ranges=[[1,183]],whole_file_read=True,credit='ACTUAL_COMPLETE_SOURCE_READ; recorded1–145 plus146–actualEOF183; metadata correction adds no read credit')
ledger['updated_utc']=NOW;write('reading-ledger.json',ledger)

c=read('consumer-candidate-dispositions.json')
fog={
 'KAR-CONSUMER-0707':('start_fog_tone_change complete398–407','For nonzero duration, clones current and target tones, stores duration/20.0, then samples stats.play_time into the tone start. Zero duration clones directly and returns without this stats read.','Clone/target/duration assignments precede stats access; failure there leaves their prefix and old/new timer state as reached. No local cancel/rescue/save.'),
 'KAR-CONSUMER-0708':('start_fog_opacity_change complete410–419','For nonzero duration stores initial opacity, float target, duration/20.0, then samples stats.play_time into start. Zero duration directly assigns target.to_f and returns without this stats read.','Earlier initial/target/duration fields remain if later play_time lookup fails; no transaction, local cancel, file write or guaranteed display.'),
 'KAR-CONSUMER-0709':('Game_Map.update complete439–489','Samples System.uptime then stats.play_time before refreshing maps/current-map/events. Scroll/fog displacement use captured uptime; tone/opacity lerp use captured play_time. On elapsed>=duration clears initial and timer, separately per transition.','A failed initial stats read precedes refresh/event/fog writes. Later event/lerp error can retain earlier refresh/scroll/event/channel updates. In-menu suppresses map event.update but common events still update. These fields may be carried by map-factory save object, but this method makes no save call and real renderer/load behavior is outside this receipt.')}
for x in c['records']:
 if x['id'] in fog:
  unit,meaning,prefix=fog[x['id']];x.update(own_full_source_read=True,status='RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN',pending='Caller/actual renderer and save/reload receiver boundaries remain separate.',meaning=meaning,premises_and_failure_prefix=prefix,actual_reader='/root/kernel_atomic_reception',complete_unit=unit,read_evidence=['io/wp09-gamemap-required-full-first.json','io/wp09-gamemap-required-full-tail.json','io/gamemap-playtime-complete-fog-methods-reread.json'])
c['summary']=dict(collections.Counter(x['status'] for x in c['records']));c['updated_utc']=NOW;write('consumer-candidate-dispositions.json',c)
progress=read('progress.json');progress.update(updated_utc=NOW,consumer_candidate_dispositions=c['summary'],own_full_source_reference_occurrences=98,hash_candidate_status='NO_REQUIRED_BOUNDED_SCOPE_ACTUAL_ROOT_COUNTERREVIEW_FULL_RECEIVED',new_complete_proposals=1,new_required_count=0,new_optional_count=0);write('progress.json',progress)
interfaces=read('interfaces.json');interfaces['root_hash_counter_actual_reception']=receipt
interfaces['new_source_units_and_semantic_edges']['ROOT-decisions']='GR8-KER001/002/003 exact complete canonical and original counter contracts actually read and boundedly received. KER001 primary-then-backup orphan branch; KER002 existing readable legacy→empty adaptation boot branch; KER003 formatter no-message. MapSave remains triage-only; emergency no-new-required. No extra votes.'
interfaces['hash_candidate']='One original complete proposal preserved; full real nonproposer root8-section counterreceived via receipt. NO_REQUIRED_BOUNDED_SCOPE; original conditional source fact preserved; no edit started.'
interfaces['updated_utc']=NOW;write('interfaces.json',interfaces)

paths=['Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb','Data/Scripts/004_Game classes/005_Game_MapFactory.rb','Data/Scripts/004_Game classes/001_Switches and Variables/001_Game_Temp.rb']
units=[]
for path,a,b,description in [(paths[0],1,64,'whole cache accessor/helper definition'),(paths[1],383,495,'complete MapFactoryHelper module'),(paths[2],1,94,'whole Game_Temp definition')]:
 lines=(R/path).read_text(encoding='utf-8-sig').splitlines();units.append({'identity':identity(path),'actual_whole_source_reader':'/root/kernel_atomic_reception','complete_unit':description,'range':[a,b],'content':'\n'.join(lines[a-1:b])+'\n','scope':'Exact complete units; recipient independently joins its caller. Original provider FULL not inherited.'})
facts=[
 ('CACHE01','pbLoadRegionalDexes creates Game_Temp only when current global false/nil, then loads regional_dexes.dat only when the accessor is false/nil. Returned [] is truthy and remains cached; false/nil load result is retried next invocation. No local rescue; failed RHS assignment preserves prior cache value after any new temp creation.'),
 ('CACHE02','pbLoadBattleAnimations likewise ensures a temp, but checks pbRgssExists? only when animation cache false/nil. Missing asset leaves cache as is and returns it. Truthy cache suppresses existence check/load; no local error catch or blanket missing-file load fallback.'),
 ('CACHE03','pbLoadMoveToAnim ensures temp; false/nil cache loads move2anim.dat then uses ||[] fallback, storing [] if load returned nil or false. Empty [] is truthy and suppresses later reload; load exceptions do not select fallback and propagate.'),
 ('CACHE04','pbLoadMapInfos ensures temp and caches load_data(MapInfos.rxdata) on false/nil. It has no existence guard/||[] fallback/local rescue. Same temp regional/animation/mapinfo slots are separate and do not invalidate each other on getters.'),
 ('CACHE05','pbClearData if temp exists first sets regional, animation, move mapping and map_infos slots nil in that order. Always then clears MapFactoryHelper; then encounters.setup if both game_map and encounters truthy; then if Tilesets asset exists assigns load_data result to global tilesets. Failure in encounter setup skips tilesets; tileset RHS failure leaves previous global tilesets while earlier invalidations remain. No atomic rollback or local cancel.'),
 ('CACHE06','Game_Temp whole initializer explicitly initializes its listed menu/battle/transfer/etc fields but none of four reopened cache instance fields. Ordinary new object reads them nil through reopened accessors. Replacing temp discards that object cache binding; do not infer all callers replace temp or persisted object serialization execution.'),
 ('CACHE07','MapFactoryHelper.clear separately sets both class caches nil. getMapConnections first assigns [] before load_data. A load/iteration error can leave truthy empty or partly filled connections cache, so later getter can skip load until explicit clear. This failure prefix is distinct from Game_Temp accessor caches.'),
 ('CACHE08','Connection getter discards rows when either map dimension has a zero axis, normalizes each retained row edge to coordinates in place, then appends the same conn object to both endpoint lists. getMapDims initializes its own [] and on per-id cache miss loads Map%03d.rxdata; default rescue catches an ordinary error and caches [0,0]. Zero dimensions and successful dimensions remain truthy per-id until clear; no runtime/native map validity or all-error catch claim.'),
 ('CACHE09','MapFactoryHelper getMapEdge uses zero for N/W, cached dimensions width for E, height for S, default width. eachConnectionForMap yields existing rows and returns for missing entry; mapsConnected? checks endpoint identity in those yields; range predicates use current Graphics geometry and six-tile margin. Cache data validity/connections beyond this bounded definition are not independently approved.')]
packet=write('developer-cache-definitions-contribution.v1.json',{
 'schema':'gr8-complete-finite-source-contribution/v1','frozen_utc':NOW,'provider':'/root/kernel_atomic_reception','recipient':'/root/developer_full_cloud','fixed_R':COMMIT,'source_units':units,
 'facts':[{'id':i,'complete_fact':f,'source_owner':'/root/kernel_atomic_reception','premise':'Unmodified fixed definitions, ordinary accessor/object semantics and actual helper call. load_data/System/native existence and external setup/renderer return values remain explicit conditional inputs.','execution':'NOT_EXECUTED'} for i,f in facts],
 'shared_failure_boundary':'No UI/cancel or local save/write in getters. Cache invalidation mutates memory before later external work, no rollback. pbClearData tileset load changes global memory only; native reads are not executed.',
 'caller_join':'Recipient has actually read Compiler1–4 and must bind its exact direct/startup clear callers itself. This package makes no exhaustive claim which compile branches call pbClearData, nor grants whole Developer/Engine or native asset reception.',
 'io':['io/developer-needed-cache-definitions-complete-reread.json','io/developer-cache-new-gametemp-complete-definition.json'],'open':['all actual caller branch/exception handling and timing not listed','native load_data/pbRgssExists?/Graphics host values','binary asset bodies and real save/reload','arbitrary plugin/reentrant overrides'],'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})
print(json.dumps({'utc':NOW,'root_hash_receipt':receipt,'consumer_summary':c['summary'],'cache_packet':packet},ensure_ascii=False))
