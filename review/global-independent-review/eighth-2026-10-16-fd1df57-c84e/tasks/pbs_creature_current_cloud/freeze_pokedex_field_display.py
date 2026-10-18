from pathlib import Path
import json,hashlib,subprocess,datetime
P=Path(__file__).resolve().parent;R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room')
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';RT='7589c800b61ba13a13040ed0d686979b80a84fd0';BC='fd1df570cad987dc3852a3b958f03916e317f7fe';BT='f292698cdd4a8e725525a9be6dc34b75faaf151e'
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat();READER='/root/pbs_creature_current_cloud'
def load(n):return json.loads((P/n).read_text())
def freeze(n,d):
 p=P/n;assert not p.exists();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');b=p.read_bytes();return {'path':n,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def unit(path,repo=R):
 commit,tree=(RC,RT) if repo==R else (BC,BT);b=(repo/path).read_bytes();assert b==subprocess.check_output(['git','show',commit+':'+path],cwd=repo)
 return {'identity':{'repo':str(repo),'path':path,'commit':commit,'tree':tree,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':subprocess.check_output(['git','rev-parse',commit+':'+path],cwd=repo,text=True).strip()},'lines':[1,len(b.splitlines())],'complete_text':b.decode(),'actual_reader':READER}
paths=['Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb','Data/Scripts/010_Data/002_PBS data/008_Species.rb','Data/Scripts/010_Data/002_PBS data/011_Species_Files.rb','Data/Scripts/010_Data/002_PBS data/009_SpeciesMetrics.rb','Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb','Data/Scripts/010_Data/002_PBS data/013_Encounter.rb']
# Source file spellings are resolved against the actual own-full ledger only.
l=load('reading-ledger.json')
for n,needle in [(2,'Species_files'),(3,'SpeciesMetrics')]:
 candidates=[x for x in l['dependencies_full_read'] if needle in x]
 assert len(candidates)==1,(needle,candidates)
 paths[n]=candidates[0]
U=[unit(p) for p in paths]
assert U[0]['lines']==[1,619]
FP='deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md'
FS=unit(FP,B)
common=[
 'Fixed R/B8, known registered species/base/forms/metrics, legal scene lists, normal prior dependencies/resources/message operations and no plugin/extra callback or concurrent mutation.',
 'Original complete primary records were actually read in this context; their separate packets retain all raw values/order/defaults. This packet establishes finite conditional field consumers and exact fixture predicates, not all data-dependent native outcomes.',
 'TownMap/MapMetadata/Point inputs used by the habitat formulas are valid for the stated bounded input domain. Foreign complete default map records are not implicitly accepted, and the package does not establish actual Demo reachability.',
 'A lookup, graphic request, bitmap operation or scene call does not prove final host media/playback/window success. Exceptions retain only the reached prefix; there is no general ensure/rollback guarantee.',
 'Every statement is static comparison after actual complete source/formal reading. The packaging script does not invoke the reference, a selector, a probability model, a numeric formula audit or a native UI.',
 'Existing UI29unit receipt retains /root/ui_wp66 as its original reader. This context separately actually read Entry619 whole on IO e1e7c8/ac3b67/c34b4c/a60bba; no new context/vote or foreign whole-source credit is inferred.'
]
clauses=[]
def a(key,text,formal,source,src_lines):
 clauses.append({'id':'PCR-PD-FIELD-'+key,'assertion':text,'formal':{'path':FP,'lines':formal,'identity':FS['identity']},
  'source_units':[{'index':i,'identity':U[i]['identity'],'lines':src_lines if i==0 else U[i]['lines']} for i in source],
  'premises':common,'actual_reader':READER,'status':'FINITE_ASSERTION_MATCHED_SOURCE_STATIC','evidence':'SOURCE_STATIC / DERIVED_VECTOR / NOT_EXECUTED',
  'scope':'Exact individual field/display predicate only. Neighboring complete methods are included for prerequisites and failure prefixes, not automatic whole-domain acceptance.'})
a('SCENE-REGION','Full scene resolves negative region from current map town-map position or0, then gets that region TownMap.',[120,125],[0],[1,70])
a('BRIEF-NATIONAL','Brief entry uses national base-species definition order when national unlocked.',[147,161],[0,1,4],[72,122])
a('BRIEF-REGIONAL','Brief entry continues after an unlocked regional list yields no number, selecting the first positive number; offset uses that selected list.',[147,161],[0,4],[72,122])
a('FULL-SINGLE-NUMBER','Summary full-single computes regional number and offset before scene start; negative region resolves later for map display and does not recompute number.',[147,161],[0],[574,603])
a('NEGATIVE-LAST-LIST','Full-single region-1 calls regional array indexing and can select the final regional list, independently of national-unlocked brief numbering.',[147,161],[0],[574,603])
a('IMAGE-LAST-RECORD','Dummy preview obtains the last stored gender/form then independently forces shiny=false for each front/back/icon request.',[163,176],[0,4],[138,152])
a('IMAGE-READ-ONLY','Normal preview refresh does not write the last-form tuple or seen/owned/seen-forms tables.',[163,176],[0,4],[138,152])
a('IMAGE-BACK-METRICS','Back preview starts y256 then adds twice selected Metrics back_sprite vertical value; bitmap appearance remains unobserved.',[163,176],[0,3],[138,152])
a('STRUCTURE-NAME','Available forms exclude nonzero records with nil or empty raw FormName before seen checks.',[165,176],[0,1],[154,205])
a('STRUCTURE-REDIRECT','Available forms exclude PokedexForm redirects when display number differs from own form, even with show-all enabled.',[165,176],[0,1],[154,205])
a('STRUCTURE-MULTIPLE','Structurally valid nonzero form sets multiple_forms before seen filtering, even when that form is unseen.',[165,176],[0],[154,205])
a('STRUCTURE-SHOW-ALL','Show-all bypasses seen qualification only; it does not bypass raw-name or redirect structural filters.',[165,176],[0],[154,205])
a('FORM-GENDER-DIFF','Base gender-difference uses male/female front-filename resolution inequality; both nil compare equal and do not prove resource presence.',[165,176],[0,2],[154,205])
a('FORM-SINGLE-GENDER','Single-gender forms check female only for AlwaysFemale and male otherwise; Genderless is labeled as gender2 then displayed as male0.',[165,176],[0,1,4],[154,205])
a('FORM-BASE-COLLAPSE','Two-gender base with equal image resolution checks male then female, emits first qualifying entry only, always displayed as male.',[165,176],[0,2,4],[154,205])
a('FORM-OTHER-GENDERS','Other two-gender forms check male then female; nonempty translated form name stops after first eligible gender; nil/empty can keep both eligible entries.',[165,176],[0,1,4],[154,205])
a('FORM-ORDER','Available entries sort form then gender before genderless normalization.',[165,176],[0],[154,205])
a('FORM-LABEL-EXISTS','An existing label, including empty text, is retained unless neither structural multiple forms nor base gender difference exists, when it is cleared.',[165,176],[0],[154,205])
a('FORM-LABEL-MISSING','Missing label becomes Male/Female, or One Form/Genderless according to gender/multiple-form branch; base same-image fallback One Form is still subject to clearing.',[165,176],[0],[154,205])
a('INFO-SELECTED-DATA','Info obtains selected species/form data and uses its translated species Name; number<=0 displays???.',[147,161],[0,1],[221,301])
a('INFO-OFFSET','Info positive number is reduced by1 only when the precomputed shift flag is true, then formatted with at least3digits.',[147,161],[0],[221,301])
a('INFO-OWNED','Category, size, Pokedex text, footprint, owned icon and Type icons require player owned status.',[147,161],[0,1],[221,301])
a('INFO-UNOWNED','Unowned Info shows category and size placeholders and does not request description/footprint/Type icon drawing.',[147,161],[0],[221,301])
a('INFO-METRIC','Metric height/weight divide stored tenths by10.0, separate from raw parser tenths conversion.',[147,161],[0,1],[221,301])
a('INFO-US-HEIGHT','US height divides stored height by0.254 then rounds and splits total inches into feet and remainder.',[147,161],[0],[221,301])
a('INFO-US-WEIGHT','US weight divides stored weight by0.45359 then rounds and displays pounds after division by10.0; this is independent of Main search0.254 weight behavior.',[147,161],[0],[221,301])
a('INFO-BATTLED','Info USE toggles battled-count versus size; battled count is caught+defeated and does not write owned status.',[147,161],[0,4],[221,301])
a('INFO-TYPES','Owned Info iterates every selected Species types entry and requests each Type icon_position rectangle; it does not truncate the authored Type list to two.',[147,161],[0,1],[221,301])
a('HABITAT-BASE','Encounter inclusion tests every slot record base species, across all types, for equality to selected base species; absent types yields false.',[123,145],[0,1],[302,351])
a('HABITAT-VERSION','Habitat uses each_of_version, retaining the registered symbol-key/array-key fallback defect; single get fallback remains independent.',[123,145],[0,5],[302,351])
a('HABITAT-FILTERS','Each table must contain species, have MapMetadata, lack HideEncountersInPokedex, have town-map position and match displayed region.',[123,145],[0],[302,351])
a('HABITAT-VISIBLE-UNION','All Points whose optional switch is absent or on contribute coordinate candidates; a later visible duplicate can keep a coordinate when the first duplicate is hidden.',[127,145],[0],[302,351])
a('HABITAT-SIZE-FALLBACK','Missing MapSize or nonpositive width retains1x1 shape1; positive width uses supplied shape and ceil(length/width) height within the stated legal domain.',[127,145],[0],[302,351])
a('HABITAT-ASCII','Within the formal finite ASCII0–9/x domain,1–9 occupy equally and0/x do not occupy; the string is not parsed as a single integer or brightness weight.',[127,145],[0],[302,351])
a('HABITAT-ROWMAJOR','Shape index i+j*width yields local x=i/y=j then adds map-position base coordinates; missing tail characters do not supply occupied cells.',[127,145],[0],[302,351])
a('HABITAT-INTERSECTION','A translated occupied coordinate contributes only when in visible Point coordinates; contributions union into truth flags at linear map-grid indexes.',[127,145],[0],[302,351])
a('HABITAT-NONE','Empty resulting point collection shows Area unknown; this does not certify native bitmap output.',[123,145],[0],[353,401])
a('FORM-SELECT-GATE','Forms chooser opens only when more than one available entry exists.',[165,176],[0],[486,556])
a('FORM-SELECT-INITIAL','Chooser initially selects matching gender/form if found, otherwise index0; oldindex=-1 makes its first loop write the selected entry.',[165,176],[0,4],[441,484])
a('FORM-SELECT-WRITE','Every selected-entry write invokes the three-argument last-form setter, whose default shiny=false replaces that tuple field without altering seen/owned or refreshing accessible lists.',[165,176],[0,4],[441,484])
a('FORM-SELECT-LOOP','UP from first wraps to last and DOWN from last wraps to first; arrow visibility does not block wrap.',[165,176],[0],[441,484])
a('FORM-SELECT-CANCEL','Selection change writes on next loop before new input; BACK/USE exits without restoring prior last-form tuple.',[165,176],[0],[441,484])
a('NAV-SPECIES','Entry previous/next scan past unseen species and stop at list ends without wrap.',[147,161],[0],[422,440])
a('NAV-PAGE','Entry LEFT/RIGHT clamp page1..3; ACTION stops prior sound and replays cry only on Info.',[147,176],[0],[486,556])
a('BRIEF-CLOSE','Brief ACTION replays cry; USE or BACK closes; no Forms/Area pages are entered by its loop.',[147,161],[0],[558,574])
a('SCENE-PREFIX','Screen wrapper reaches end-scene only after scene start and body return normally; source has no encompassing ensure for failed resource/native calls.',[147,176],[0],[574,619])

# Original complete fixture inputs copied as text, with manually recorded expected
# coordinate sets. No mask/generator, arithmetic or business surrogate is run.
fixtures=[
 {'id':'U05-HAB01','variation':'Shape10000, width3','expected_points':[[13,12]],'missing_tail_point':[15,13]},
 {'id':'U05-HAB02','variation':'Shape11111, width3','expected_points':[[13,12],[14,12],[15,12],[13,13],[14,13]],'missing_tail_point':[15,13]},
 {'id':'U05-HAB03','variation':'Missing MapSize, separately width0; then independent base Point switch-off/no duplicate, hidden flag, wrong region, missing X cases','expected_points_for_first_two':[[13,12]],'expected_points_for_each_rejection':[]},
 {'id':'U05-HAB04','variation':'Shape10000; first base Point hidden by switch51off and second base Point unconditional visible','expected_points':[[13,12]],'reorder_points':'Same habitat set; distinct WP63 first-record name/detail/heal behavior is not claimed reviewed here.'}
]
fixture_common='Each independent reset: valid region0/speciesX/version0 containing X, no hidden flag, MapPosition(0,13,12), width3, all stated relevant visible Points, valid scene/message/resource/host dependencies and no external mutation. Variations override only stated inputs. NOT_EXECUTED.'
for f in fixtures:
 a('FIXTURE-'+f['id'],'Complete bounded habitat fixture '+f['id']+' matches manually derived set, subject to all complete input premises.',[135,145],[0,5],[302,351]);clauses[-1]['complete_fixture']=f;clauses[-1]['fixture_common']=fixture_common
packet={'schema':'gr8-pokedex-primary-field-display/v1','utc':UTC,'actual_reader':READER,'complete_source_units':U,'complete_formal':FS,'common_premises':common,'clauses':clauses,'manual_atoms':len(clauses),'actual_full_Entry_read_IO':['e1e7c8','ac3b67','c34b4c','a60bba'],'formal_specific_read_IO':'16ed50',
 'primary_inputs':'Five complete Pokemon898 packets, typed-record-facts10R1280 including Forms339/Metrics674/Encounter19/Regional2; primary-field-consumer-bindings.complete.v2 retains26936fields. Original raw read is separate and cannot transfer via this index.',
 'existing_UI_finite_reception':'provider-snapshots/ui-wp66-summary-pokedex-29units.complete.v1.json; prior original reader preserved, no wholeMain/Summary source FULL from this new own Entry read.',
 'open':['All unrelated UI input/layout/framework/native outputs remain outside these exact assertions.','TownMap/MapMetadata actual default fullrecord domain remains original world primary owner; these conditional predicates do not receive their field values.','Whole11consumer/formal acceptance remains OPEN; no new formal finding.'],
 'new_business_or_numeric_model_execution':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
pid=freeze('pokedex-primary-field-display.complete.v1.json',packet)
old=load('reverse-mapping.json');assert old['atom_denominator_frozen_so_far']==2622
freeze('reverse-mapping.v13.frozen.json',old)
old['clauses']+=clauses;assert len({x['id'] for x in old['clauses']})==len(old['clauses'])
old.update(schema='gr8-pbs-current-reverse/v14',utc=UTC,supersedes='reverse-mapping.v13.frozen.json retained',atom_denominator_frozen_so_far=len(old['clauses']),pokedex_primary_field_display=pid|{'atoms':len(clauses)})
(P/'reverse-mapping.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
if paths[0] not in l['dependencies_full_read']:l['dependencies_full_read'].append(paths[0])
l['updated_utc']=UTC;(P/'reading-ledger.json').write_text(json.dumps(l,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':UTC,'packet':pid,'new_atoms':len(clauses),'reverse_atoms':len(old['clauses']),'own_full_source':len(l['dependencies_full_read']),'new_business_or_numeric_execution':0},ensure_ascii=False))
