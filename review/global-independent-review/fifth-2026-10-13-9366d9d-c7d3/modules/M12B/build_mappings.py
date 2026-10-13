"""Index firsthand semantic decisions into source/spec directions; not a verifier."""
from assemble_review import *
rc=json.loads((P/'reading-coverage.json').read_text())
B='Demo / Developer Experience'
capdefs={
'D01':('Debug entry gates and menu dispatch','WP72 §§2–3/9','DEBUG belongs to each caller; restricted tri-state and effect closing differ by menu.'),
'D02':('World state and session debugging','WP72 §4','Warp, switch/variable evaluation, daycare, roamers, session counters and mutation ordering.'),
'D03':('Player, collection and inventory debugging','WP72 §5','Resources, phone, identity, batch population/clear, capacity and registration side effects.'),
'D04':('Nonbattle individual diagnostic edits','WP72 §6','Every handler, cancellation/default, egg/setup filtering, state/PP/identity/shadow/clone/delete consequences.'),
'D05':('Test battle construction','WP72 §7.1–7.2','Normal generators and load notifications already run before eventual BACK; capacity and side size guards.'),
'D06':('Battle inspection, settings and exit refresh','WP72 §7.3/7.6','Side/party/battler identity, snapshot observations, weather/terrain and Mega edits, named return refresh only.'),
'D07':('Battle individual two-layer edits','WP72 §7.4','Persistent write-through versus local battle fields, move synchronization and form override ordering.'),
'D08':('Four-layer editable battle effect whitelist','WP72 §7.5/§13','All120 values/defaults/ranges/reset semantics; current target rendering versus chooser versus stepper.'),
'D09':('Debug logging and tool dispatch','WP72 §8','Two logging gates, flushing/report boundaries, named tool entry ownership and file effects.'),
'E01':('Property input and nested editing contracts','WP73-A §§2–3/6','All scalar/reference/structured properties, default/reset/back/confirmation, alias and self-duplicate boundaries.'),
'E02':('Shared lists, selectors and previews','WP73-A §5','Input precedence, identity-preserving order toggle, cancel identity, index boundaries and normal disposal.'),
'E03':('Trainer-type and item record editing/creation','WP73-A §§4.1/4.3/6','ID and input flow versus actual registered text; immediate registration/archive/PBS; default projection loss.'),
'E04':('Trainer record and party authoring','WP73-A §4.2','Editable member parameter table, duplicates/keys, mandatory first member and nested immediate type persistence.'),
'E05':('Species authoring and evolution representation','WP73-A §§2/4.4/6','Validation, unit scaling, plural-empty evolution working view, singular write and reverse graph rebuild timing.'),
'E06':('Global, player and map metadata authoring','WP73-A §4.5; WP73-B §4','Global0/player allocation/map selection; all data properties and suffix/save rules.'),
'E07':('Regional dex authoring','WP73-A §4.6','Main independent clone, child entry/exit compaction, unique positioning, empty-save nontermination and cache clear.'),
'W01':('Map connection authoring','WP73-B §3','Canvas operations, coordinate scales, adjacency/orphan rule, touched-edge replacement and separate save/exit.'),
'W02':('Terrain tag authoring','WP73-B §5','Registered tag choices, sparse ID comparison, autotile48 writes and saved alias lifecycle.'),
'W03':('Encounter authoring and current-map snapshot','WP73-B §6','Pair/version/type/slot operations; zero-chance archive/PBS/compile chain; runtime snapshot not broadcast.'),
'W04':('Creature sprite metrics authoring','WP73-B §7','Interactive positioning/shadow and all/single automatic formulas; lazy metrics creation and writer path-selection.'),
'W05':('Invalid tile repair','WP73-B §8','Autotile/passages validity, all map/event pages, per-map changed-only save and zero-ID valid boundary.'),
'A01':('Animation lifecycle, collections and cache','WP74 §§2–3/7/12/16','Temporary versus cached collection, two confirmations, detached canvas, zero entries and resize boundary.'),
'A02':('Animation cel canvas and attributes','WP74 §§4–5','All25 semantic fields, hit selection, locked guards, coordinate offsets, slot60 and property preview limits.'),
'A03':('Animation frame/range operations','WP74 §§6/8.1–8.5','Copy/insert aliasing, clear current-frame guard, ranges, integer/real interpolation and batch/slide controls.'),
'A04':('Animation path drawing and sampling','WP74 §8.6','Catmull–Rom initial curve, arc-length resampling and freehand rounding, zero segments and expand-before-failure.'),
'A05':('Animation timing authoring','WP74 §9','Five timing types, selection ordering,7optional channels/duration and confirmation-only commit.'),
'A06':('Animation preview playback','WP74 §10','Fixed20fps, focal transforms and priorities, visibility, visited-frame timing and overlapping gradient state.'),
'A07':('Animation exchange and legacy conversion','WP74 §§11–14','Single/batch differences, resource-before-decode ordering, allocation/truncation and partial file effects.'),
'A08':('Animation association compilation','WP74 §15','Active prefix matching/side map, last-wins, write only if any valid mapping and stale files/slot associations.'),
'A09':('Animation editing control widgets','WP74 §17','Buttons/text/checkbox/sliders, construction versus arrow rounding and optional values; inactive helpers separate.'),
'G01':('Facility generation entry and reuse','WP76 §§3–4','Setup reaches DEBUG wrapper, query/default and choice/cursor rules, ID migration and full writeback.'),
'G02':('Facility candidate sampling','WP76 §5','All species/EV/nature/move/item distributions,41items/13gates, shared Sketch cache and raw template creation.'),
'G03':('Facility pool/team iteration and tier allocation','WP76 §6','Rules copy/current original phases; duplicate criteria, targets20/600, all five replacement cases, eleven rounds and nine tiers.'),
'G04':('Facility simulation and rating math','WP76 §7','1% actual/99% estimate, snapshots/settlement, nonstandard Glicko step, draw behavior and scaling/rounding.'),
'G05':('Facility trainer allocation and persistence','WP76 §§8–9','Empty-trainer loop/shortcut, weights and duplicates, current-members stopping, default toggling, archive/PBS and name-generation bounds.'),
'M01':('Demo configuration facts and cross references','WP77 §§3–8','All9 assigned root data bodies and concrete consumers; config/static evidence distinguished from events/runtime.'),
'M02':('Demo event and runtime evidence gaps','WP77 §§1–2/9–13','Twelve missing chain families and host/media gaps; no asserted inexistence or runnable demonstration.'),
'S01':('Safe resource copy decision versus write location','WP73-A §5; WP74 §13.3','Source/existing comparison resource/write destination can be separate; equality/prompt uses comparison location.'),
'S02':('Archive, PBS and runtime consumer synchronization','WP73-A §6; WP73-B §§6/7; WP74 §16; WP76 §8.4','Shared identity for registration/archive/write/recompile/reload/snapshot phases; consumers project it without duplicate capability counts.'),
'R01':('Root-owned conversion observations: independent counterevidence','WP75 related sections only','Seven root observations checked against direct slices; root full-source ownership is not inherited independent signoff.')}
caps={k:dict(id='M12-'+k,title=n,classification=[B],state='supported',support_boundary='supported_static: only fixed R/B5 behavior within documented legal inputs and named failure paths; no executed UI, reference code, model, media or host validation.',current_spec_anchors=s,semantic_comparison=t,source_anchors=[],semantic_groups=[],related_findings=[]) for k,(n,s,t) in capdefs.items()}
for k in ['D01','D09','E01','E02','A09','S01','S02']:caps[k]['classification']+=['Generic Kernel','User Interface']
for k in ['D04','D07','D08','G02','G04']:caps[k]['classification']+=['Pokémon Rules','Combat Requirements']
for k in ['W01','W02','W03','W04','W05','A06','M01','M02']:caps[k]['classification']+=['Engine / Overworld Integration']
for k in ['E03','E04','E05','E07','G01','G03','G05']:caps[k]['classification']+=['Creature-RPG']

def primary_cap(r,g):
 p=r['path'];a=g['lines'][0]
 if p.endswith('001_EditorScreens.rb'):
  return (['W03'] if a<345 else ['E03'] if a<448 else ['E04'] if a<692 else ['E06'] if a<822 else ['E03'] if a<926 else ['E05'] if a<992 else ['E07'] if a<1252 else ['A01','A07'])
 if 'TerrainTags' in p:return ['W02']
 if 'MapConnections' in p:return ['W01']
 if 'SpritePositioning' in p:return ['W04']
 if p.endswith('001_Editor_Utilities.rb'):return ['E02'] if a<16 or a>=64 else ['S01','A07']
 if p.endswith('002_Editor_DataTypes.rb'):return ['E01']
 if p.endswith('003_Editor_Listers.rb'):return ['E02']
 if p.endswith('001_Debug_Menus.rb'):return ['D01','D06'] if a>=260 else ['D01']
 if p.endswith('002_Debug_MenuCommands.rb'):
  return ['D02'] if a<269 else ['D05','D02'] if a<548 else ['D03','D02'] if a<960 else ['D03'] if a<1148 else ['D09']
 if p.endswith('003_Debug_MenuExtraCode.rb'):return ['D02'] if a<553 else ['A07','S01'] if a<668 else ['W05'] if a<744 else ['D01','E02']
 if p.endswith('004_Debug_BattleCommands.rb'):return ['D06'] if a<423 else ['D08']
 if p.endswith('005_Debug_BattlePkmnCommands.rb'):return ['D07'] if a<807 else ['D07','D08']
 if p.endswith('006_Debug_BattleExtraCode.rb'):return ['D08']
 if p.endswith('007_Debug_PokemonCommands.rb'):return ['D04']
 if p.endswith('001_AnimEditor_SceneElements.rb'):
  return ['A09'] if a<100 else ['A02'] if a<358 else ['A01','A06'] if a<513 else ['A02','A03'] if a<729 else ['A02']
 if p.endswith('002_AnimEditor_ControlsButtons.rb'):return ['A09']
 if p.endswith('003_AnimEditor_Interpolation.rb'):return ['A04']
 if p.endswith('004_AnimEditor_ExportImport.rb'):return ['A07']
 if p.endswith('005_AnimEditor_Functions.rb'):
  return ['A01'] if a<188 else ['A02'] if a<376 else ['A05'] if a<679 else ['A03'] if a<928 else ['A01','A09']
 if p.endswith('001_ChallengeGenerator_Data.rb'):return ['G03'] if a<276 else ['G01']
 if p.endswith('002_ChallengeGenerator_Pokemon.rb'):return ['G02']
 if p.endswith('003_ChallengeGenerator_Trainers.rb'):return ['G05']
 if p.endswith('004_ChallengeGenerator_BattleSim.rb'):return ['G03','G04'] if a<135 else ['G04']
 raise ValueError(p)
for r in rc['records']:
 if r.get('assigned_role')!='primary':continue
 for g in r['semantic_ranges']:
  ks=primary_cap(r,g);g['capability_ids']=[caps[k]['id'] for k in ks]
  g['spec_anchors']='; '.join(caps[k]['current_spec_anchors'] for k in ks)
  g['rules']=g['rules'].replace('inspect callers needed to classify dormant helper','only these helpers call each other; no outer static consumer located').replace('working observation001','GR5-M12-101').replace('possible untouched-save change','confirmed untouched BP1→0 and absent portion names→???; GR5-M12-102')
  for k in ks:
   anchor=dict(path=r['path'],version=RV,lines=g['lines'],symbol=g['entry'],supporting_fact=g['rules'])
   caps[k]['source_anchors'].append(anchor);caps[k]['semantic_groups'].append(dict(source=anchor,result='supported_static except named candidate/gap exclusions below'))
# Bounded secondary anchors; each is an actual direct read, not a new capability count.
def deps(k,needles):
 for r in rc['records']:
  if r.get('assigned_role') in ['primary','specification','original','supplement','effective_supplement','demo_material_boundary','outside_root_demo_data_scope']:continue
  if any(n in r['path'] for n in needles):
   caps[k]['source_anchors'].append(dict(path=r['path'],version=r['version'],lines=r.get('content_read_ranges',[]),supporting_fact='; '.join(g.get('rules','') for g in r.get('semantic_ranges',[])),role='necessary_dependency' if k!='R01' else 'independent_counterevidence'))
deps('D01',['Event_HandlerCollections','Event_Handlers','Scene_Map.rb','UI_Load','UI_PauseMenu','UI_Party','UI_PokemonStorage','Scene_ChooseCommands'])
deps('D02',['Game_Switches','Game_Variables','011_Messages','ShadowPokemon_Other','UI_PurifyChamber','Utilities.rb'])
deps('D03',['Item_Phone','Trainer_LoadAndNew','Player_Pokedex','001_Settings'])
deps('D04',['001_Pokemon.rb','Player_Pokedex','Item_Utilities','011_Messages'])
deps('D05',['Trainer_LoadAndNew','015_Trainer.rb','Overworld_EncounterModifiers'])
deps('D06',['Battle_CommandPhase','Battle_Battler','Battler_Initialize'])
deps('D07',['Battle_Battler','Battler_Initialize','001_Pokemon.rb','Player_Pokedex'])
deps('D08',['011_Messages','001_Settings'])
deps('D09',['PBDebug','Errors.rb','999_Main'])
deps('E01',['011_Messages','007_Evolution','015_Trainer.rb'])
deps('E02',['SpriteWindow_text','MapFactory','TileDrawingHelper','GameData.rb'])
deps('E03',['006_Item.rb','014_TrainerType.rb','GameData.rb','Compiler_WritePBS','Trainer_LoadAndNew'])
deps('E04',['015_Trainer.rb','Trainer_LoadAndNew','Compiler_WritePBS','011_Messages'])
deps('E05',['008_Species.rb','Compiler_WritePBS','Compiler_CompilePBS','007_Evolution'])
deps('E06',['016_Metadata','017_PlayerMetadata','018_MapMetadata','Compiler_WritePBS'])
deps('E07',['MiscPBSData','Compiler_WritePBS','008_Species'])
deps('W01',['MapFactory','TileDrawingHelper','Compiler_WritePBS'])
deps('W02',['011_TerrainTag','Game_Map.rb'])
deps('W03',['013_Encounter.rb','013_EncounterType','Overworld_WildEncounters','Overworld_Metadata','Compiler_WritePBS','Compiler_CompilePBS'])
deps('W04',['010_SpeciesMetrics','Compiler_WritePBS','AnimatedBitmap'])
deps('W05',['Compiler_MapsAndEvents'])
deps('A01',['MiscPBSData','BattleAnimationPlayer','SpriteWindow_text'])
deps('A02',['BattleAnimationPlayer','Battle_Scene.rb'])
deps('A03',['BattleAnimationPlayer'])
deps('A05',['BattleAnimationPlayer','001_FileTests'])
deps('A06',['BattleAnimationPlayer','AnimatedBitmap','RPG_Cache','Battle_Scene.rb'])
deps('A07',['MiscPBSData','BattleAnimationPlayer','001_FileTests'])
deps('A08',['Compiler_CompilePBS','Scene_PlayAnimations','MiscPBSData','GameData.rb'])
deps('G01',['BattleChallenge','ChallengeRules','Challenge_Rulesets','011_Messages','Challenge_Data'])
deps('G02',['Challenge_Data','Challenge_Rulesets','008_Species','PBS/moves','PBS/pokemon','Item_Utilities','001_Pokemon.rb'])
deps('G03',['Challenge_Rulesets','ChallengeRules','Challenge_Data'])
deps('G04',['Battle_DebugScene','Battle_CommandPhase','Battle_Battler','001_Pokemon.rb','003_Type.rb'])
deps('G05',['Challenge_Data','Challenge_Rulesets','Compiler_WritePBS','Compiler_CompilePBS','Utilities.rb','PBS/trainer_types'])
deps('M01',['PBS/','StartGame','RegionMap','EncounterModifiers','FormHandlers','007_Evolution','DungeonParameters','RandomDungeons','Item_Phone','Utilities_Pokemon','013_EncounterType','Compiler.rb'])
deps('S01',['001_FileTests'])
deps('S02',['GameData.rb','Compiler_WritePBS','Compiler_CompilePBS','MiscPBSData','Overworld_WildEncounters','Overworld_Metadata','010_SpeciesMetrics'])
deps('R01',['Compiler_MapsAndEvents','FilenameUpdater','Scripts.rxdata'])
for k,fs in {'E03':['101','102'],'D04':['103'],'D07':['103'],'S01':['104']}.items():
 caps[k]['state']='partial';caps[k]['related_findings']=['GR5-M12-'+v for v in fs]
 caps[k]['support_boundary']+=' The named source behavior differs from, or is not fully distinguished by, the current contract; proposed disposition awaits independent counterevidence.'
caps['G05']['state']='partial'
caps['G05']['known_boundary']='Current WP76 §9.2 describes gender grammar selection/retry/truncation/case, but does not enumerate the random-name syllable and format data tables. Tables were read in full. Exact default invented-name vocabulary is a content compatibility policy, not presumed mandatory; optional follow-up, no new required finding.'
caps['E07']['inactive_definition_boundary']='The three old evolution-family display helpers only reference each other; no outer static caller located. Main regional-dex family fill uses a separate species-family operation. No promise of an additional available menu.'
caps['A09']['inactive_definition_boundary']='ArrayCountSlider and unused optional-widget external setters are definition-only paths, with unresolved names; active constructor/click/value consumers checked independently. No expanded usability promise.'
caps['M02']['state']='unresolved';caps['M02']['support_boundary']='Static gap classification supported; event chains, media and real runtime cannot be verified from missing material. This is a reviewed evidence limitation, not unread available source.'
caps['M02']['source_anchors']=[dict(path=r['path'],version=RV,material_availability=r['material_availability']) for r in rc['records'] if r.get('assigned_role')=='demo_material_boundary']
caps['R01']['state']='partial';caps['R01']['support_boundary']='Counterevidence only: four root observations confirmed/narrowed as substantive candidates, two excluded as required, one optional clarification. Full root-owned primary scope not signed by M12B.'
# Parent-owned media/tool identity is a projection, not an extra independently supported capability.
parent_projection=dict(id='M12-ROOT-TOOLS',state='not_reviewed',owner='root',identity_record='../M12/reading-coverage.json',scope='Root files, external exe/media and full converter beyond M12B direct slices',boundary='Parent actual-read identity reused for ownership and navigation only. No independent full-source claim.')
save('source-to-spec.json',{**base,'method':'Behavioral capability identities group primary files and shared consumers. Each primary semantic range points to one or more identities; overlapping evidence is never summed as separate unique functionality.','capabilities':list(caps.values()),'parent_projection':parent_projection,'execution_status':'STATIC_ONLY_NO_REFERENCE_OR_MODEL_EXECUTION'})
# Section decisions were made by reading whole source/contract, before this serialization.
section_caps={
'wp72':{'1':['D01','D02','D03','D04','D05','D06','D07','D08','D09'],'2':['D01','D07','S02'],'3':['D01'],'4':['D02'],'5':['D03'],'6':['D04'],'7':['D05','D06','D07','D08'],'7.1':['D05'],'7.2':['D05'],'7.3':['D06'],'7.4':['D07'],'7.5':['D08'],'7.6':['D06'],'8':['D09','S02'],'9':['D01','D09'],'10':['D02','D04','D07','D09'],'11':['D01','D02','D03','D04','D05','D06','D07','D08','D09'],'12':['D01','D09','M02'],'13':['D08']},
'wp73-a':{'1':['E01','E02','E03','E04','E05','E06','E07'],'2':['E01','E03','E05','S02'],'3':['E01'],'4':['E03','E04','E05','E06','E07'],'4.1':['E03'],'4.2':['E04'],'4.3':['E03'],'4.4':['E05'],'4.5':['E06'],'4.6':['E07'],'5':['E02','S01','A07'],'6':['S02','E01','E03','E04','E05','E06','E07'],'7':['W03','E06','A01'],'8':['E01','E03','E04'],'9':['E01','E03','E04','E07'],'10':['E01','E02','E03','E04','E05','E06','E07'],'11':['S02','M02']},
'wp73-b':{'1':['W01','W02','W03','W04','W05','E06'],'2':['W01','W03','W04','S02'],'3':['W01'],'4':['E06'],'5':['W02'],'6':['W03','S02'],'7':['W04','S02'],'8':['W05'],'9':['W01','W02','W03','W04'],'10':['W01','W02','W03','W04','W05'],'11':['W01','W02','W03','W04','W05'],'12':['S02','M02']},
'wp74':{'1':['A01','A02','A03','A04','A05','A06','A07','A08','A09'],'2':['A01','A02','A05'],'3':['A01'],'3.3':['A01','A06'],'3.4':['A05','A07'],'4':['A02'],'5':['A02'],'6':['A03'],'7':['A01','A02'],'8':['A03'],'8.6':['A04'],'9':['A05'],'10':['A06'],'11':['A07'],'12':['A01','A07'],'13':['A07'],'13.3':['S01'],'13.4':['A07'],'14':['A07'],'15':['A08'],'16':['A01','A07','A08','S02'],'17':['A09'],'18':['ROOT'],'19':['A01','A02','A03','A04','A05','A06','A07','A08','A09'],'20':['A01','A02','A03','A04','A05','A06','A07','A08','A09'],'21':['M02','S02']},
'wp75':{'1':['ROOT','R01'],'2':['ROOT','R01'],'3':['ROOT'],'4':['ROOT'],'5':['R01'],'6':['ROOT'],'7':['R01'],'8':['R01'],'9':['R01'],'10':['R01'],'11':['R01'],'12':['ROOT','R01'],'13':['ROOT'],'14':['ROOT'],'15':['R01'],'16':['ROOT','R01'],'17':['ROOT','R01'],'18':['ROOT','R01']},
'wp76':{'1':['G01','G02','G03','G04','G05'],'2':['G01','G02','G03','G04','G05'],'3':['G01'],'4':['G01'],'5':['G02'],'6':['G03'],'7':['G04'],'8':['G05'],'9':['G05'],'9.1':['G02'],'9.3':['G03','G05'],'10':['G01','G02','G03','G04','G05'],'11':['G01','G02','G03','G04','G05'],'12':['M02','S02']},
'wp77':{'1':['M01','M02'],'2':['M01','M02'],'3':['M01','M02'],'4':['M01'],'5':['M01'],'5.4':['M01','D03'],'6':['M01'],'7':['M01','D09'],'8':['M01'],'9':['M02'],'10':['M01','M02'],'11':['M01','M02'],'12':['M01','M02'],'13':['M01','M02']}}
def choose(doc,section):
 d=section_caps[doc]
 while section not in d and '.' in section:section=section.rsplit('.',1)[0]
 return d.get(section,d.get('1',[]))
# Intern anchors once. Per-unit IDs resolve to exact paths, versions and ranges in this file.
anchor_index={};anchor_list=[]
def intern(a):
 key=json.dumps({k:a.get(k) for k in ['path','version','lines','symbol','material_availability']},sort_keys=True)
 if key not in anchor_index:
  q=dict(a);q['anchor_id']=f'SA{len(anchor_list)+1:04d}';anchor_list.append(q);anchor_index[key]=q['anchor_id']
 return anchor_index[key]
cap_anchor_ids={k:[intern(a) for a in c['source_anchors']] for k,c in caps.items()}
# Rows exact-mapped to each effect's own declaration and current input dispatcher.
effect_source=R/'Data/Scripts/020_Debug/003_Debug menus/006_Debug_BattleExtraCode.rb'
es=lines(effect_source);oldcat=lines(Path('review/wp72-delivery-2026-10-02/revision-v2/battle-effects-catalog.md'))
effects=[]
for i,l in enumerate(oldcat,1):
 if l.startswith('| ') and l.split('|')[1].strip() not in ['审计标识','---']:
  token=l.split('|')[1].strip()
  if not re.fullmatch('[A-Za-z0-9]+',token):continue
  matches=[j for j,t in enumerate(es,1) if re.search(r'PBEffects::'+re.escape(token)+r'\s*=>',t) and not t.lstrip().startswith('#')]
  if len(matches)!=1:raise ValueError(('effect declaration',token,matches))
  effects.append((token,i,matches[0]))
assert len(effects)==120
sections=[];units=[]
for doc,p in main_files.items():
 body=lines(p);headings=[]
 for i,l in enumerate(body,1):
  m=re.match(r'^(#{2,3})\s+(\d+(?:\.\d+[a-z]?)*)\.?\s+(.*)',l)
  if m:headings.append((i,len(m[1]),m[2],m[3]))
 for j,(ln,depth,sec,title) in enumerate(headings):
  end=next((q[0]-1 for q in headings[j+1:] if q[1]<=depth),len(body))
  ks=choose(doc,sec);state='supported'
  if 'ROOT' in ks:state='not_reviewed' if ks==['ROOT'] else 'partial'
  elif 'M02' in ks:state='unresolved' if ks==['M02'] else 'supported'
  sections.append(dict(path=str(p),version=BV,section=sec,title=title,lines=[ln,end],material_availability='available_text',review_extent='full_text',source_scope='root-owned except direct counterevidence slices' if doc=='wp75' else 'assigned or necessary shared slice',capability_ids=[caps[k]['id'] if k!='ROOT' else 'M12-ROOT-TOOLS' for k in ks],source_anchor_ids=list(dict.fromkeys(a for k in ks if k!='ROOT' for a in cap_anchor_ids[k])),state=state,evidence_level='SPEC_STATIC + SOURCE_STATIC; no execution',comparison='Text read completely. Compare subordinate clause/table/vector units and named source rule groups; supported is limited to static inputs/outputs/ordering, never host execution.'))
 current='1';last_header=0
 for i,l in enumerate(body,1):
  m=re.match(r'^#{2,3}\s+(\d+(?:\.\d+[a-z]?)*)',l)
  if m:current=m[1];last_header=i;continue
  if not l.strip() or l.startswith(('#','---','>')):continue
  # Ignore separator/header rows, retain every substantive table row and each prose/list clause line.
  if l.startswith('|'):
   cells=[x.strip() for x in l.strip('|').split('|')]
   if all(re.fullmatch('[-: ]+',x or ' ') for x in cells):continue
   if i<len(body) and body[i].startswith('|') and re.fullmatch(r'[|\s:\-]+',body[i]):continue
  ks=choose(doc,current);kind='table_row' if l.startswith('|') else 'clause';status='supported';note='Direct source comparison supports the stated behavior and boundaries (supported_static).'
  related=[]
  if doc=='wp75':status='partial';note='Full current text read; M12B independently checked only root-observation-related source slices. Other WP75 behavior remains root-owned, not independently signed here.'
  if ks==['ROOT']:status='not_reviewed';note='Text read and parent actual-read identity reused; source primary ownership remains root. Not an unread assigned body.'
  if ks==['M02']:status='unresolved';note='Missing event/media/host evidence explicitly retained; available static material reviewed, no runtime claim.'
  # Exact affected clauses; adjacent correct general contracts remain supported.
  if doc=='wp73-a' and i in [84,101]:status='partial';related=['GR5-M12-101'];note='Input/ID/save sequence supported; registered raw text actually falls back to defaults, unlike stored-text implication/explicit plural claim.'
  if doc=='wp73-a' and i==99:status='partial';related=['GR5-M12-102'];note='Save chain supported but untouched BP1→0 and absent portion-name→??? defaults are missing.'
  if doc=='wp72' and i in [129,160,206]:status='partial';related=['GR5-M12-103'];note='Outer direct registration gate cannot suppress inner ordinary form submission; on-field battle setter also reaches it. Other listed field gates not generalized.'
  if doc=='wp74' and i in [368,374]:status='partial';related=['GR5-M12-104'];note='Optional clarification: comparison resource versus final write path differ for the third-destination variant; ordinary same-path behavior supported.'
  if doc=='wp76' and current=='9.2':status='partial';note='Gender/retries/case/truncation supported; exact syllable/format table data not enumerated. Optional content-compatibility boundary, not a required new algorithm finding.'
  aa=list(dict.fromkeys(a for k in ks if k!='ROOT' for a in cap_anchor_ids[k]))
  ef=re.match(r'^\| (E\d{3}) \|',l)
  if doc=='wp72' and ef:
   n=int(ef[1][1:])-1;t,oldln,sln=effects[n]
   aa=[intern(dict(path=str(effect_source.relative_to(R)),version=RV,lines=[sln,sln],symbol=t,supporting_fact='This exact whitelist identity/type/default/range row; no table copied')),
       intern(dict(path=str(effect_source.relative_to(R)),version=RV,lines=[182,452],symbol='display/chooser/input/reset dispatch',supporting_fact='Reset and type semantics independently checked, including−2→−1 distinction'))]
   kind='effect_parameter';note=f'Individually compared {ef[1]} with {t}; behavioral layer/type/default/range/ACTION reset preserved. Original catalog line {oldln}; not inferred from count equality.'
  units.append(dict(unit_id=f'{doc}-L{i:04d}',path=str(p),version=BV,section=current,lines=[i,i],kind=kind,claim_locator=(l.split('|')[1].strip() if l.startswith('|') else re.sub(r'[*`]', '', l)[:85]),claim_sha256=hashlib.sha256(l.encode()).hexdigest(),capability_ids=[caps[k]['id'] if k!='ROOT' else 'M12-ROOT-TOOLS' for k in ks],source_anchor_ids=aa,state=status,comparison_result=note,related_findings=related,evidence_level='SOURCE_STATIC/SPEC_STATIC',execution_status='NOT_EXECUTED'))
# Every named test/vector is a separate reverse-map unit, including meaningful repetitions.
vector_caps={
'DG':['D01','D01','D01','D01','D02','D02','D02','D02','D02','D03','D03','D04','D04','D04','D04','D04','D05','D05','D07','D08','D06','D06','D09','D09','D01','D02','D02','D03','D02','D03'],
'CE':['E01','E01','E03','E03','E03','E04','E04','E04','E04','E03','E05','E06','E07','E07','E01','E01','E01','E02','E02','S02'],
'WE':['W01','W01','W01','W01','W01','E06','W02','W02','W02','W03','W03','W03','W03','W03','W04','W04','W04','W04','W04','W05','W05','S02'],
'AN':['A01','A02','A02','A02','A02','A02','A03','A03','A01','A01','A01','A02','A03','A03','A03','A03','A03','A04','A04','A05','A05','A05','A06','A07','A07','A07','A07','A07','A08','S02','A09','M02','A01'],
'GN':['G01','G01','G01','G02','G02','G02','G02','G02','G02','G02','G03','G03','G03','G03','G04','G04','G04','G04','G04','G04','G03','G03','G05','G05'],
'DM':['M02','M01','M01','M01','M01','M01','M01','M01','M01','M01','M01','M01','M01','M01','M01','M02']}
bs={'B19-C008':['D01','D03'],'B19-C009':['D02'],'B19-C011':['D07'],'B19-C012':['D04','D07'],'B19-C013':['D03'],'B19-C018-string':['E01'],'B19-C018-evolution':['E01'],'B19-C019':['E01','E06'],'B19-C021':['E01','E04'],'B19-C022':['E05','S02'],'B19-C023':['E04'],'B19-C004':['W03'],'B19-C005':['W03','S02'],'B19-C016':['W04','S02'],'B19-C007-whitelist':['D08'],'B19-C003-pocket':['E03'],'B19-003-neutral':['E01','D08'],'B20-003':['A03'],'B20-C003':['A07','R01'],'B20-C007':['R01'],'B20-C020':['A05','A07'],'B20-C024':['ROOT'],'B20-C025':['A03'],'B20-C026':['A06'],'B20-C027':['R01'],'B20-C028':['M01','D03'],'B20-C029':['M01','D04'],'B20-C030':['R01'],'B20-C031':['A01','A07'],'B20-C032':['A04'],'B20-C033':['A02'],'B20-C034':['R01'],'B20-C051':['R01'],'B20-C083':['M01'],'B20-D024':['A04'],'B20-INTAKE-R01':['A08','R01']}
test=F/'test-catalog/demo-dx-wp72-73-74-75-76-77.md';vectors=[]
for ln,l in enumerate(lines(test),1):
 if not l.startswith('| '):continue
 ident=l.split('|')[1].strip();m=re.match(r'(DG|CE|WE|AN|CV|GN|DM)-M(\d+)',ident)
 if m:
  pre,num=m[1],int(m[2]);ks=['R01'] if pre=='CV' else [vector_caps[pre][num-1]]
 elif ident.startswith('B17-PA040'):ks=['G02']
 elif ident in bs:ks=bs[ident]
 elif re.match(r'WE-[EC]\d+',ident):ks=['W03']
 elif ident in ['ID','---']:continue
 else:
  # Other named cases in the fully read catalog retain their exact line identity.
  if not re.match(r'[A-Z][A-Za-z0-9-]*\d',ident):continue
  ks=['S02']
 state='supported';note='Manually checked all stated inputs/normal/boundary outcomes against source and current contract; supported_static, not executed.'
 if 'ROOT' in ks:state='not_reviewed';note='Text read; source/tool primary ownership root only.'
 elif ks==['M02']:state='unresolved';note='Vector states unavailable material/runtime; reviewed as evidence boundary, not executable proof.'
 elif 'R01' in ks:state='partial';note='Root-related source anchors independently checked only for listed seven observations; remaining root vector fields are not a fresh full-source signoff.'
 related=[]
 if ident=='B20-C034':related=['M12-OBS-002','M12-OBS-005'];note='Six call patterns are line-anchored rather than whole-string. Revisit label alone does not make wild empty branches receive trainer-only patch.'
 if ident in ['CE-M05','CE-M08','CE-M10']:note+=' These vectors do not specify the default textual outputs of newly created records; candidate101 is not disproved by their ID/cancel examples.'
 vectors.append(dict(id=ident,path=str(test),version=BV,lines=[ln,ln],input_output_sha256=hashlib.sha256(l.encode()).hexdigest(),capability_ids=[caps[k]['id'] if k!='ROOT' else 'M12-ROOT-TOOLS' for k in ks],source_anchor_ids=list(dict.fromkeys(a for k in ks if k!='ROOT' for a in cap_anchor_ids[k])),state=state,comparison_result=note,related_findings=related,execution_status='NOT_EXECUTED_THIS_REVIEW'))
save('spec-to-source.json',{**base,'method':'All seven main current texts and all current Demo/DX vector rows read. The index serializes independent semantic comparisons; it does not infer support from headings, filenames or matching counts. WP75 full text is read for context, but full source remains root-owned.','sections':sections,'clause_and_table_units':units,'vectors':vectors,'source_anchor_catalog':anchor_list,'effective_supplements':[r for r in rc['records'] if r.get('assigned_role')=='effective_supplement'],'original_comparison':'original-comparison.json','supported_boundary':'All supported units mean supported_static only; exact named candidate exceptions override generic supported headings; missing host/event/material evidence remains unresolved.'})
save('reading-coverage.json',rc)
print('capabilities',len(caps),'sections',len(sections),'clause/table units',len(units),'vectors',len(vectors),'anchors',len(anchor_list))
