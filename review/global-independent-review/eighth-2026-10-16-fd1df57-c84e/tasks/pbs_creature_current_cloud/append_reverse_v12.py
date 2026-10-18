from pathlib import Path
import json,datetime,hashlib,subprocess
P=Path(__file__).resolve().parent;R=Path('/workspace/pokemon-essentials');C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';UTC=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
F='deliverables/final-specification-set/';WP=F+'creature-rpg/wp24-player-trainers-partners.md';S=F+'generic-kernel/wp03-content-identity-and-schema.md';AI=F+'combat-requirements/wp51-ai-action-selection-and-skill.md';PT=F+'test-catalog/creature-rpg-wp18-20-24-25-26.md'
packet=json.loads((P/'trainer-type-and-trainers92.complete.v1.json').read_text());sources=packet['complete_necessary_source_units'];atoms=[]
audio_path='Data/Scripts/008_Audio/002_Audio_Play.rb';b=(R/audio_path).read_bytes();assert b==subprocess.check_output(['git','show',C+':'+audio_path],cwd=R)
audio={'source_identity':{'repo':str(R),'commit':C,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','path':audio_path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':subprocess.check_output(['git','rev-parse',C+':'+audio_path],cwd=R,text=True).strip()},'complete_unit_range':[1,89],'complete_body':'\n'.join(b.decode().splitlines()[:89])+'\n','actual_read_chunk':'5a6a70','qualification':'Whole contained StringToAudio/Resolve/BGMPlay/Fade/Stop methods; later ME/SE family OPEN.'}
def add(id,doc,line,meaning,unit_indices,facts=()):
 atoms.append({'id':id,'formal':{'path':doc,'lines':[line,line]},'assertion':meaning,'sourcefact_ids':list(facts),'source_units':[{'identity':sources[i]['source_identity'],'lines':sources[i]['complete_unit_range']} for i in unit_indices],'actual_reader':'/root/pbs_creature_current_cloud','status':'FINITE_ASSERTION_MATCHED_SOURCE_STATIC','premises':['Fixed source/current normal valid input objects, normal earlier called dependencies and no plugin or concurrent mutation.','All stated fixture premises and entry-specific cancellation/failure prefixes retained. Only this exact assertion is accepted; not the complete parent paragraph, arbitrary callbacks or host output.'],'qualification':'Complete source/formal units actually read and manually compared. Cases are static designs, not executed; script only serializes manually selected meanings.'})
for names,value in [(['Male','male','M','m','0'],0),(['Female','female','F','f','1'],1),(['Unknown','unknown','Other','other','Mixed','mixed','X','x','2'],2)]:
 for ordinal,name in enumerate(names):
  add(f'PCR-TRTYPE-GENDER-ALIAS-{value}-{ordinal}',S,167,f'Exact TrainerType Gender CSV token {name!r} maps to integer{value}; no general long-word case folding is applied.',[0],['PC-F016'])
for names,value in [(['Male','male','M','m','0'],0),(['Female','female','F','f','1'],1)]:
 for ordinal,name in enumerate(names):
  add(f'PCR-TRMEMBER-GENDER-ALIAS-{value}-{ordinal}',S,168,f'Exact Trainer member Gender token {name!r} maps to integer{value}; Unknown/Mixed/2 are not declared member aliases.',[1],['PC-F017'])
for id,doc,line,meaning,us,fs in [
 ('NAME-DEFAULT',S,107,'Missing Type raw name is Unnamed; displayed name subsequently looks up TRAINER_TYPE_NAMES.',[0],['PC-F016']),
 ('GENDER-DEFAULT',S,107,'Missing Type gender is2, and Type female? is false for that value.',[0],['PC-F016']),
 ('MONEY-DEFAULT',AI,21,'Missing Type BaseMoney is30; this parser/constructor path does not apply an editor range cap.',[0],['PC-F016']),
 ('SKILL-DEFAULT',AI,21,'Missing SkillLevel takes the effective BaseMoney, retaining explicit0 rather than treating it as absence.',[0],['PC-F016']),
 ('SKILL-LIVE',WP,149,'Trainer skill_level resolves current TrainerType data; AITrainer subsequently copies the value in its initialization stage.',[0,2,5],['PC-F031','PC-F074']),
 ('GENDER-LIVE',WP,83,'Trainer gender is obtained from TrainerType, and Owner.new_from_trainer copies that value; Unknown remains2 in Owner.',[0,2,7],['PC-F030','PC-F031']),
 ('NAME-NONAME',WP,52,'Trainer full_name returns personal name alone for case-insensitive NoName Type flag; otherwise localized type name then personal name.',[0,2],['PC-F031']),
 ('FLAGS-CASE',AI,23,'AI starts by copying authored flags and uses exact case-sensitive membership there, unlike Type has_flag? case-insensitive query.',[0,2,5],['PC-F074']),
 ('CONSTRUCTOR',WP,49,'Trainer constructor strictly resolves type first, then stores name, generates32-bit id, calls host-language helper, and initializes empty party; returned language requires that helper to complete.',[2],['PC-F031']),
 ('PUBLIC',WP,50,'public_ID masks the low16 bits of the supplied/current id; secret_ID shifts right16 on the supplied/current id.',[2],['PC-F031']),
 ('FOREIGN-ID',WP,51,'make_foreign_ID repeats random32-bit generation until different from its own id; it has no fixed retry bound.',[2],['PC-F031']),
 ('LOAD-TYPE',WP,156,'pbLoadTrainer rejects unknown type before querying a Trainer record.',[1,3],['PC-F030']),
 ('LOAD-EXACT',WP,157,'Type/name/version lookup is exact; a missing Trainer record returnsnil, with no automatic version0 fallback.',[1,3],['PC-F030']),
 ('LOAD-NAME',WP,158,'The first configured rival type whose variable is a String replaces only the created runtime trainer name; even empty String passes that class check.',[1],['PC-F018']),
 ('LOAD-ITEMS',WP,158,'to_trainer clones the trainer items outer array and copies localized lose text before constructing members in raw order.',[1],['PC-F018']),
 ('LOAD-MEMBER',WP,158,'Member defaults and override sequence use the complete WP18 constructor/NPC clauses; later load-event hooks may overwrite them and are not assumed absent unless stated.',[1],['PC-F018']),
 ('CHECK-NONDEBUG',WP,164,'Nondebug type/trainer check returns true before any registry lookup, distinct from the loader error path.',[3],['PC-F030']),
 ('CHECK-DECLINE',WP,257,'Debug missing type declined and still absent yields false from type check and outer trainer check when interpreter cleanup returns normally.',[3],['PC-F030']),
 ('MISSING-FALLBACK',WP,165,'pbMissingTrainer raises in nondebug mode for a missing exact record; this is a separate caller from pbLoadTrainer returningnil.',[3],['PC-F030']),
 ('FREE-VERSION',WP,167,'The free-party helper scans versions0 through255 and returns the first missing key, else-1.',[1,3],['PC-F030']),
 ('DEBUG-PREFIX',WP,166,'Reached debug creation registers then saves Trainer data before name-corpus/PBS conversion; later failure does not undo those earlier steps.',[3,10,11],['PC-F022','PC-F030','PC-F078']),
 ('MONEY-GUARD',WP,138,'Both money settlement methods reject when internalBattle or moneyGain is false; loss additionally checks NO_MONEY_LOSS.',[6],[]),
 ('MONEY-REWARD',WP,139,'Reward stage sums each opponent team maximum level times that trainer base_money, then independent AmuletCoin and HappyHour doubles, before player wallet assignment.',[2,6,8],['PC-F031']),
 ('MONEY-PAYDAY',WP,139,'PayDay is a later independent positive-amount stage with the same two doubles; both stages derive actual gain after wallet clamp before stats/message.',[6,8],[]),
 ('MONEY-NOCHANGE',WP,141,'A stage with nonpositive actual wallet change does not increment gained statistic or display its reward message.',[6,8],[]),
 ('MONEY-LOSS',WP,140,'Loss uses player-only team maximum level and the capped badge multiplier index, limits to current money, then writes wallet before actual-loss stats/message.',[6,8],[]),
 ('AUDIO-LAST',WP,182,'Ordinary trainer battle BGM scans supplied trainer order and retains the last nonnil Type battle field; stored empty String overwrites earlier content then falls back.',[4],['PC-F032']),
 ('AUDIO-VICTORY',WP,183,'Ordinary trainer victory selection applies the same last-nonnil rule, then prefixes the selected request name for BGM playback through the victory result.',[4],['PC-F032']),
 ('AUDIO-FROMTYPE',WP,184,'FromType preserves a nonnil raw type field including empty String; nil alone reaches map/global/default conversion.',[4],['PC-F032']),
 ('AUDIO-PRELOAD',WP,186,'Each applicable next-battle preset clones and returns first; the selection helper does not clear any preset.',[4],['PC-F032']),
 ('INTRO-EMPTY',WP,188,'Nil/empty IntroBGM returns before memory selection and playback request.',[4],['PC-F032']),
 ('INTRO-EXISTING',WP,192,'Existing memorized BGM prevents the intro helper changing memory or pending cue delay before request delivery.',[4],['PC-F032']),
 ('INTRO-CUE',WP,193,'Without memory, pending delay causes delay=nil and cue memorized with position0 before the intro playback request.',[4],['PC-F032']),
 ('INTRO-CURRENT',WP,194,'Without memory or pending delay, current BGM and current position are stored; only the position query is rescued to0.',[4],['PC-F032']),
 ('INTRO-PREFIX',WP,196,'Memory/delay writes precede playback request; a later playback exception has no local rollback or broad rescue.',[4],['PC-F032']),
]:add('PCR-TRAINER-'+id,doc,line,meaning,us,fs)

# Additional complete PT audio fixtures are added below before serialization.
fixture_meanings={
 41:'Ordered[A,B] choosesB for ordinary battle and victory requests.',
 42:'Ordered[B,A] choosesA, retaining order dependence.',
 43:'A laternil preserves earlierA and does not force map fallback.',
 44:'No type candidate reaches corresponding mapM.',
 45:'Missing map metadata with a valid map object reaches corresponding globalG.',
 46:'Map empty text is skipped, reaching globalG.',
 47:'Nil map/global candidates reach distinct Battle trainer/Battle victory defaults.',
 48:'Valid empty-text map/global fixtures reach the same separate defaults.',
 49:'Stored empty final type field overwritesA, then ordinary helper falls to mapM.',
 50:'Direct FromType preserves the same stored empty field without map fallback.',
 51:'Direct FromType fieldnil falls to converted mapM.',
 52:'Direct FromType nonemptyA is returned as the field request without requiring the ordinary converted representation.',
 53:'Battle and victory presets separately winXb/Xv and are not cleared by selection.',
 54:'Wild battle/victory/capture helpers independently select their W/V/C map fields.',
 55:'Missing map metadata selects the three distinct Gb/Gv/Gc global fields.',
 56:'Nil or valid empty-text map/global fields select the three distinct wild/victory/capture defaults; no actual sound/wait is inferred.',
 57:'One preset at a time changes only its corresponding component of the three-request tuple.',
 58:'Absent memory plus pending cue clears delay and memorizesQ/0 before delivering introI.',
 59:'ExistingR/9 memory retains that pair and pending delay at the pre-playback memory stage.',
 60:'Absent memory/delay remembers currentA/17 before introI.',
 61:'Only position-query failure is rescued, producingA/0 before introI.',
 62:'Nil/empty intro returns without changing existingR/9 or pending cue at this helper.',
 63:'All three independent presets Xb/Xv/Xc win their own request families and are not cleared here.'
}
formal=(Path('/workspace/pokemon-essentials-clean-room')/PT).read_text().splitlines()
for number,meaning in fixture_meanings.items():
 index=number+101;raw=formal[index-1];cells=raw.split('|');assert cells[1].strip()==f'PT-{number:02}'
 add(f'PCR-PT-AUDIO-{number:02}',PT,index,meaning,[4],['PC-F032'])
 atoms[-1]['complete_formal_fixture']={'id':cells[1].strip(),'input_and_premises':cells[2].strip(),'expected_static_result':cells[3].strip()}
 atoms[-1]['necessary_audio_conversion_unit']={'identity':audio['source_identity'],'lines':[1,39],'scope':'Complete StringToAudio and Resolve methods actually read. RPG constructor and native playback must meet the fixture normal premises; no host result is observed.'}
 atoms[-1]['evidence']='SOURCE_STATIC / DERIVED_VECTOR / TEST_NOT_EXECUTED'

rev=json.loads((P/'reverse-mapping.json').read_text());assert len(rev['clauses'])==2398
prior=P/'reverse-mapping.v11.frozen.json';assert not prior.exists();prior.write_bytes((P/'reverse-mapping.json').read_bytes());known={x['id'] for x in rev['clauses']};assert all(a['id'] not in known for a in atoms)
d={'schema':'gr8-pbs-current-trainer-audio-alias-finite-reverse/v1','utc':UTC,'actual_reader':'/root/pbs_creature_current_cloud','complete_atoms':atoms,'complete_additional_contained_audio_unit':audio,'primary_record_packet':'trainer-type-and-trainers92.complete.v1.json','mandatory_companions':['mandatory-locator-clarification.v3.json','mandatory-message-range-clarification.v1.json'],'actual_formal_reads':['ced024','3067a2','bd195a','9e3f9b','f7832f','fc26ed'],'actual_source_reads':['790d87','39fb14','e127f0','827dcf','3fc0ae','5a6a70','d594fd','1c9146'],'scope':'All declared19type/10memberGenderaliases; explicit TrainerType consumer/default/load/settlement/audio predicates and23 complete named audio fixtures. Only those finite assertions, not all WP24, all69PT or host behavior.','numeric_execution':'No new business or numeric-expression model executed; this script only copies complete already read fixture strings and serializes manually written source meanings. Prior numeric audit is separately registered.','remaining':'PlayerMetadata/host language mapping beyond the helper call, every UI/AI/phone/rematch callback, native media/save/reload and other unreceived predicates remain OPEN. All72/20record read credit remains this original context; no second vote.','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','new_findings':[],'new_contexts':0,'new_votes':0}
out=P/'trainer-audio-alias-reverse-addendum.v1.json';assert not out.exists();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
rev['clauses']+=atoms;rev['schema']='gr8-pbs-current-reverse/v12';rev['utc']=UTC;rev['supersedes']='reverse-mapping.v11.frozen.json retained';rev['atom_denominator_frozen_so_far']=len(rev['clauses']);rev['trainer_audio_alias_addendum']={'path':out.name,'new_atoms':len(atoms),'type_gender_aliases':19,'member_gender_aliases':10,'complete_PT_audio_fixtures':23,'current':len(rev['clauses']),'remaining_exact_EggGroup_directory':15};(P/'reverse-mapping.json').write_text(json.dumps(rev,ensure_ascii=False,indent=2)+'\n')
l=json.loads((P/'reading-ledger.json').read_text());l['dependencies_partial_read'].append({'path':audio_path,'lines':[1,89],'actual_read_chunk':'5a6a70','complete_units':['StringToAudio1–14','Resolve24–39','BGMPlay52–68','Fade71','Stop74–89'],'qualification':'Onlycontainedmethods, not wholeAudiofile/native outcome.'});l['formal_partial_read'].append({'path':AI,'lines':[15,39],'actual_read_chunk':'fc26ed','complete_units':['whole§2技能值/标记/次序19–27; neighboring§1tail/§3prefix actually displayed, not complete§3 credit']});l['updated_utc']=UTC;(P/'reading-ledger.json').write_text(json.dumps(l,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':UTC,'path':str(out),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'new_atoms':len(atoms),'reverse_atoms':len(rev['clauses'])},ensure_ascii=False))
