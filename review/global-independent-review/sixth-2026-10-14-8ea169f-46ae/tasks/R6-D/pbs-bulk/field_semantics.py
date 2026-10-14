"""PBS author-contract review manifest and rule applications, not a game model.

Human-authored behavioral rules are separate from deterministic data joins.
No PASS is generated. Cross-domain effect algorithms are explicit handoffs.
"""
import audit as a, relations as r, build_mappings as b
from collections import defaultdict,Counter
from pathlib import Path
import re,json
S=b.SRC;F=b.SPEC;L=b.L;CP=b.CP;PARSER=S+'021_Compiler/001_Compiler.rb';WRITER=S+'021_Compiler/003_Compiler_WritePBS.rb'
SP=r.SCHEMA_DIR+'008_Species.rb';CO=b.CORE;DC=S+'012_Overworld/007_Overworld_DayCare.rb';PKDEX=S+'015_Trainers and player/005_Player_Pokedex.rb'
WP18=F+'creature-rpg/wp18-creature-identity-species-ownership.md';WP19=F+'pokemon-rules/wp19-attributes-ability-and-stats.md';WP20=F+'creature-rpg/wp20-hp-status-moves-helditem.md';WP30=F+'creature-rpg/wp30-growth-learning-and-friendship.md';WP34=F+'pokemon-rules/wp34-inheritance-and-offspring.md';WP62=F+'pokemon-rules/wp62-pokedex-records-regions-and-content.md';WP73B=F+'demo-dx/wp73-b-world-editors.md'
TCI=F+'test-catalog/creature-rpg-wp18-20-24-25-26.md';TST=F+'test-catalog/pokemon-rules-wp19-21-22-23-34.md';TITEM=F+'test-catalog/creature-rpg-wp27-28-29-30-33.md';TBERRY=F+'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'

# These defaults were independently read in the constructors; they are review
# data about observable omission, not code translated into a future model.
DEFAULT={
 'types':{'Name':'Unnamed','IconPosition':0,'IsSpecialType':False,'IsPseudoType':False,'Weaknesses':[],'Resistances':[],'Immunities':[],'Flags':[]},
 'abilities':{'Name':'Unnamed','Description':'???','Flags':[]},
 'moves':{'Name':'Unnamed','Type':'NONE','Category':'Status','Power':0,'Accuracy':100,'TotalPP':5,'Target':'None','Priority':0,'FunctionCode':'None','Flags':[],'EffectChance':0,'Description':'???'},
 'items':{'Name':'Unnamed','NamePlural':'Unnamed','PortionName':'missing; query falls back to singular name','PortionNamePlural':'missing; query falls back to plural name','Pocket':1,'Price':0,'SellPrice':'floor(purchase price/2)','BPPrice':1,'FieldUse':0,'BattleUse':0,'Flags':[],'Consumable':'true except important items','ShowQuantity':'missing; effective query depends on importance','Move':None,'Description':'???'},
 'berry_plants':{'HoursPerStage':3,'DryingPerHour':15,'Yield':[2,5]},
 'pokemon_metrics':{'BackSprite':[0,0],'FrontSprite':[0,0],'FrontSpriteAltitude':0,'ShadowX':0,'ShadowSize':2},
 'shadow_pokemon':{'GaugeSize':4000,'Moves':[],'Flags':[]},
 'pokemon':{'Name':'Unnamed','FormName':None,'Types':['NORMAL'],'BaseStats':'every main stat 1','GenderRatio':'Female50Percent','GrowthRate':'Medium','BaseExp':100,'EVs':'every main stat 0','CatchRate':255,'Happiness':70,'Abilities':[],'HiddenAbilities':[],'Moves':[],'TutorMoves':[],'EggMoves':[],'EggGroups':['Undiscovered'],'HatchSteps':1,'Incense':None,'Offspring':[],'Height':1,'Weight':1,'Color':'Red','Shape':'Head','Habitat':'None','Category':'???','Pokedex':'???','Generation':0,'Flags':[],'WildItemCommon':[],'WildItemUncommon':[],'WildItemRare':[],'Evolution':[],'Evolutions':[]},
}
DEFAULT['pokemon_forms']={**DEFAULT['pokemon'],'PokedexForm':'own positive form number','MegaStone':None,'MegaMove':None,'UnmegaForm':0,'MegaMessage':0}
INIT={'types':(33,46),'abilities':(23,28),'moves':(41,56),'items':(119,137),'berry_plants':(28,34),'pokemon':(175,220),'pokemon_forms':(175,220),'pokemon_metrics':(59,68),'shadow_pokemon':(46,53)}
SPECIES_INHERIT=set(r.SPECIES)-{'Name','FormName','Evolution','Evolutions'}
SPECIES_INHERIT|={'Evolution','Evolutions'}

def C(path,lo,hi,meaning):return {'location':L(path,lo,hi),'meaning':meaning,'scope':'author-field consumption or cross-domain entry only; downstream algorithms owned by named domain'}
def details(fam,key):
    src=[];cons=[];formal=[];vectors=[];norm='Explicit value replaces prior value for this field; no additional family-specific mutation.';handoff=[];gap=[]
    if fam in {'pokemon','pokemon_forms'}:
        formal=[L(WP18,60,101)];vectors=[L(TCI,33)]
        if key in {'Name','FormName','Category','Pokedex'}:
            cons=[C(SP,223,240,'Raw text selects the matching localized name/form/category/entry domain.'),C(S+'016_UI/004_UI_Pokedex_Entry.rb',247,266,'Owned entry view consumes category, stored tenths dimensions and localized description.')];formal+=[L(WP62,151,154)]
            if key=='FormName':cons+=[C(PKDEX,203,227,'Form name participates in distinct seen-form vs last-form mapping gates.')];formal+=[L(WP62,86,90)]
        elif key=='PokedexForm':
            cons=[C(PKDEX,203,227,'Ordinary registration resolves display-form data before its name gate; last-seen uses original form name.')];formal+=[L(WP62,86,90)];vectors+=[L(TST,132,138)]
        elif key=='Types':
            norm='Deduplicate and remove empty entries; preserve full remaining order, without a two-type cap.';src=[L(CP,325,329)];cons=[C(CO,313,334,'Return a copy of the complete effective form type list; membership resolves a Type identity.')];formal+=[L(WP19,32,37)];vectors+=[L(TST,60)]
        elif key=='BaseStats':
            norm='Require six positive author columns in HP/attack/defense/speed/special-attack/special-defense order. Convert to named stats; missing/nonpositive direct-construction entries fill 1, not PBS acceptance of zero.';src=[L(CP,292,300),L(SP,185,190),L(S+'010_Data/001_Hardcoded data/008_Stat.rb',59,104)];cons=[C(CO,1065,1070,'Copy six named values for stat calculation.'),C(CO,1099,1117,'Feed effective base stats into existing stat-calculation domain.')];formal+=[L(b.WP03,180,188),L(WP19,128,139)];vectors+=[L(b.TEST,93,96),L(TST,11,25)]
        elif key=='EVs':
            norm='Read repeated (Stat identity, positive yield) pairs; later repeated same stat replaces earlier. Fill omitted main stats with zero. This is defeated-species yield, not the creature training EV table.';src=[L(CP,301,306),L(SP,185,190)];cons=[C(CO,908,913,'Copy main-stat yields into the battle EV-gain input.'),C(S+'011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',59,87,'Battle EV distribution reads the copied yield, then modifiers and existing growth-domain limits.')];formal+=[L(b.WP03,182,184),L(WP30,116,123)];vectors+=[L(b.TEST,93,96)]
        elif key=='BaseExp':
            cons=[C(CO,224,227,'Expose species/form base experience.'),C(S+'011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',100,105,'Multiply by defeated level at existing battle experience entry.')];formal+=[L(WP30,89,97)];handoff=['WP30 complete experience allocation, qualifiers, multipliers, truncation and commit sequence.']
        elif key=='GrowthRate':
            cons=[C(CO,190,221,'Resolve the growth-rate identity for level/experience conversions.')];formal+=[L(WP19,117,124),L(WP30,48,75)];handoff=['Hardcoded growth tables and formulas belong to growth domain; PBS selects the identity.']
        elif key=='GenderRatio':
            cons=[C(SP,255,257,'Classify fixed vs probabilistic gender record.'),C(CO,340,354,'Resolve gender-ratio identity and derive/cache gender from fixed-kind or low PID byte.')];formal+=[L(WP19,39,48)];vectors+=[L(TST,31,35)]
        elif key in {'Abilities','HiddenAbilities'}:
            cons=[C(CO,424,489,'Natural and hidden ordered slots select ability; missing slot follows the documented fallback, candidate enumeration preserves indices.')];formal+=[L(WP19,62,75)];vectors+=[L(TST,36)];handoff=['Ability internal effects, activation and phases belong to WP48/49 and AI consumers.']
        elif key=='CatchRate':
            cons=[C(S+'011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb',206,219,'Use species catch rate only when no explicit catch rate argument supplied.')];formal+=[L(F+'pokemon-rules/wp38-capture-and-receiving.md',31,40)];handoff=['Capture formula and ball rule domain; no 255 compiler cap is inferred from editor limits.']
        elif key=='Happiness':
            cons=[C(CO,1187,1188,'Creation directly takes species happiness without a range clamp.')];formal+=[L(WP30,184,187)];gap=['C07: PBS accepts nonnegative values above255 and normal creation copies them; unqualified persistent0..255 statement needs parent adjudication.']
        elif key in {'Moves','TutorMoves','EggMoves'}:
            if key=='Moves':
                cons=[C(CO,620,641,'Filter levels in authored order, retain last duplicate move, take trailing capacity, create fresh full-PP slots.')];formal+=[L(WP20,125,132)];norm='Keep authored ordered (nonnegative level, registered move) pairs; no sort or compile-time dedup.'
            elif key=='TutorMoves':
                cons=[C(CO,708,714,'Membership in tutor/level/ancestral egg-move sources establishes compatibility.')];formal+=[L(WP20,145,150)];norm='Keep registered move list; duplicate entries do not change this membership predicate.'
            else:
                cons=[C(SP,339,345,'An empty effective egg list may fall back to the previous species/form for compatibility.'),C(DC,113,122,'Breeding reads raw effective egg list with separate parental/configuration gates.')];formal+=[L(WP20,149),L(WP34,119,130)]
            vectors+=[L(TST,226,237)];handoff=['Interactive teaching/cancel/consumption and battle synchronization WP20/28/30; breeding ordering WP34.']
        elif key=='EggGroups':
            cons=[C(DC,29,36,'Ditto membership chooses breeding roles.'),C(DC,530,547,'Undiscovered veto; otherwise shared group or Ditto relationship before gender gate.')];formal+=[L(WP34,22,49)];vectors+=[L(TST,224,226),L(TST,249)]
        elif key=='HatchSteps':
            cons=[C(DC,62,67,'Egg creation copies the effective species hatch-step count.')];formal+=[L(WP34,83,94)];handoff=['Step acceleration and actual hatch transitions belong to WP35.']
        elif key in {'Incense','Offspring'}:
            cons=[C(SP,305,319,'Incense gates recursive ancestry selection.'),C(DC,54,59,'After baby-species resolution, sample nonempty offspring list uniformly by list entries.')];formal+=[L(WP34,54,71)];vectors+=[L(TST,227,228)]
            if key=='Offspring':norm='Base entry stores strings until full base-species validation; form entry resolves registered species immediately. Preserve duplicates as sampling weight.';src=[L(CP,332,339)]
        elif key in {'Evolution','Evolutions'}:
            norm='Plural list is assigned first in schema order, repeated singular entries append in own appearance order. Require parameters when method declares one. Defer base target/parameter identity conversion, derive reverse ancestor with documented first-found/form precedence.';src=[L(CP,311,324),L(CP,341,365),L(CP,487,523)];cons=[C(SP,277,319,'Expose forward evolutions separately from chosen predecessor and baby ancestry.'),C(SP,376,386,'Minimum-level query consumes the selected reverse method/parameter.')];formal+=[L(b.WP04,152),L(WP34,62)];vectors+=[L(b.TEST,141,147)];handoff=['All evolution condition callback algorithms WP31/32; PBS owns ordered identities, parameter kinds and reverse-link construction.']
        elif key in {'Height','Weight'}:
            norm='After accepted unsigned decimal syntax, store max(1,nearest-integer(10×value)); missing ordinary record stores1, omitted species-form field inherits base.';src=[L(CP,308,310)];cons=[C(CO,898,905,'Expose dimensions in tenths.'),C(S+'016_UI/004_UI_Pokedex_Entry.rb',247,266,'Owned entry uses metric/US presentation from stored tenths.')];formal+=[L(b.WP04,96,98),L(WP62,154)];vectors+=[L(b.TEST,89,92)]
        elif key in {'Color','Shape'}:
            cons=[C(S+'016_UI/003_UI_Pokedex_Main.rb',358,373,'Use effective last-seen-form color and body-shape identity in list/filter data.')];formal+=[L(b.WP03,209,262),L(WP62,151,154)];vectors+=[L(b.TEST,137,140)]
        elif key in {'Habitat','Generation'}:
            cons=[C(SP,391,450,'Generic editor/property view and PBS writeback consume descriptive values; named omission rules apply.')];formal+=[L(WP18,79),L(b.WP04,216,219)];vectors+=[L(b.TEST,120,123)]
            norm='Keep enum Habitat or signed integer Generation; these are descriptive, not the world Area encounter lookup or MECHANICS_GENERATION setting. Exact direct member/symbol/key search found only schema/default/inheritance/editor/writeback references.'
        elif key in {'WildItemCommon','WildItemUncommon','WildItemRare'}:
            cons=[C(CO,579,582,'Expose the three ordered wild-held-item pools.'),C(S+'012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb',383,404,'Configured probability selects a pool, then samples an entry; equal three pools choose the first pool.')];formal+=[L(F+'creature-rpg/wp36-wild-encounters-and-modifiers.md',178,186)];norm='Keep each ordered registered-Item pool. A species form inherits all three pools only when all three properties are absent; defining one prevents inheritance of the others.';src=[L(CP,479,484)];handoff=['Full encounter creation modifiers and random outcomes belong to WP36.']
        elif key=='Flags':
            cons=[C(SP,243,264,'Case-insensitive keyword predicates; first DefaultForm_N sets base form.'),C(DC,75,89,'Mother/Everstone form inheritance markers.'),C(S+'012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb',34,43,'Legendary/Mythical/UltraBeast creation hook under configuration.'),C(S+'011_Battle/005_AI/009_AITrainer.rb',40,51,'Configured wild AI skill override from the same marker families.')];formal+=[L(WP18,101),L(WP34,96,99)];vectors+=[L(TCI,15),L(TST,230,231)];handoff=['UltraBeast ball modifiers WP38 and AI/encounter rules are named downstream consumers.']
        elif key in {'MegaStone','MegaMove','UnmegaForm','MegaMessage'}:
            cons=[C(S+'014_Pokemon/002_Pokemon_MegaEvolution.rb',6,53,'First matching species/unmega-form with stone OR known move selects target; message selector is data-driven.')];formal+=[L(F+'pokemon-rules/wp22-mega-and-primal-reversion.md',25,35),L(F+'pokemon-rules/wp22-mega-and-primal-reversion.md',58)];vectors+=[L(TST,132,138)];handoff=['Combat permission, pending selection, cancel, owner allowance and transformation commit belong to WP22/40.']
    elif fam=='types':
        p=r.SCHEMA_DIR+'003_Type.rb';formal=[L(b.WP03,282)];src=[L(p,33,46)]
        if key=='Name':cons=[C(p,49,52,'Localized Type name from raw author text.')];gap=['C05 omitted-name default not explicit in formal Type contract.']
        elif key=='IconPosition':
            cons=[C(S+'016_UI/006_UI_Summary.rb',465,470,'Select type icon strip position.'),C(S+'011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',1302,1311,'Order Hidden Power candidate type buckets, ties retain registration order.')];formal+=[L(F+'combat-requirements/wp47-a-move-attributes-targeting-and-calling.md',94,96)];gap=['C05 omitted icon-position0 default not explicit.']
        elif key=='IsSpecialType':cons=[C(p,54,55,'Classify type physical vs special.'),C(r.SCHEMA_DIR+'005_Move.rb',79,89,'Use per-type category when per-move category configuration is disabled.')];formal+=[L(b.WP43,159,161)];gap=['C05 omittedfalse default not explicit.']
        elif key=='IsPseudoType':cons=[C(S+'020_Debug/001_Editor_Utilities.rb',147,154,'Exclude pseudo types from editor selector.'),C(S+'011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',1302,1311,'Exclude pseudo types from Hidden Power candidates.')];formal+=[L(b.WP43,47),L(F+'combat-requirements/wp47-a-move-attributes-targeting-and-calling.md',96)];gap=['C05 omittedfalse default not explicit.']
        elif key in {'Weaknesses','Resistances','Immunities'}:
            norm='Deduplicate within the individual list; validate referenced types at whole-table finalization. Conflicting memberships are not rejected: weakness before resistance before immunity.';src+=[L(CP,149,171)];cons=[C(p,61,67,'Read defending type matchup contribution.'),C(p,130,139,'Multiply each defense-type contribution with ordinary empty-product1.')];formal+=[L(b.WP43,43,47)]
        elif key=='Flags':cons=[C(p,57,59,'Case-insensitive generic marker query; no authored Flags in this corpus.')];formal+=[L(b.WP03,282)]
    elif fam=='abilities':
        p=r.SCHEMA_DIR+'004_Ability.rb';formal=[L(b.WP03,95,100)];src=[L(p,23,28)];vectors=[L(b.TEST,113)]
        if key in {'Name','Description'}:cons=[C(p,31,38,'Query the matching localized name or description domain.'),C(CP,190,199,'Collect name and description keys into message hashes.')]
        else:cons=[C(p,41,43,'Case-insensitive flag membership.'),C(S+'016_UI/001_Non-interactive UI/003_UI_EggHatching.rb',252,268,'FasterEggHatching consumed once per qualifying non-egg-party scan.')];formal+=[L(F+'creature-rpg/wp35-eggs-and-hatching.md',73,81)]
        handoff=['Every ability identity may be selected by species; phase/effect implementations are WP48/49, not a second per-record PBS algorithm obligation.']
    elif fam=='moves':
        p=r.SCHEMA_DIR+'005_Move.rb';src=[L(p,41,56)];formal=[L(b.WP03,91,102)];vectors=[L(b.TEST,102),L(b.TEST,106,108)]
        if key in {'Name','Description'}:cons=[C(p,65,72,'Localized move display text.'),C(S+'014_Pokemon/004_Pokemon_Move.rb',62,63,'Known-move wrapper exposes localized text.')];gap=['C05 raw name/description omission defaults not explicit.']
        elif key=='TotalPP':cons=[C(S+'014_Pokemon/004_Pokemon_Move.rb',15,18,'New known move starts with computed full PP.'),C(S+'014_Pokemon/004_Pokemon_Move.rb',42,47,'Base PP plus floor(base PP×PPUps/5).')];formal+=[L(WP20,152,160)];vectors+=[L(TST,44,47)]
        elif key=='Flags':cons=[C(b.MV,130,143,'Case-insensitive anchored move-kind predicates.'),C(p,75,77,'Generic case-insensitive marker query including Metronome exclusion caller.')];formal+=[L(F+'combat-requirements/wp47-a-move-attributes-targeting-and-calling.md',190,199)];handoff=['Sound/Contact/Powder/etc. feed combat/AI predicates; their complete downstream algorithms are WP43/44/47/48/49.'];gap=['C05 omittedempty flags default not explicit as an author default.']
        elif key=='FunctionCode':cons=[C(b.MV,57,68,'Bind digit-prefixed legacy name or symbolic effect name; absent implementation has explicit fallback.'),C(S+'011_Battle/003_Move/004_Move_BaseEffects.rb',10,17,'Generic unsupported Status effect fails; damage category proceeds normally.')];formal+=[L(b.WP43,29,35)];handoff=['Every record has precise source effect/fallback and formal effect-identity links in move-effects-bidirectional-locations.json; internal effect algorithms handed to combat review.']
        else:
            cons=[C(S+'014_Pokemon/004_Pokemon_Move.rb',50,61,'Forward numeric/enum fields from registered move.'),C(b.MV,34,49,'Copy fields into battle move inputs before later dynamic overrides.')]
            if key in {'Category','Power'}:norm='Status with positive power rejects current record; damage category with zero/omitted power warns and becomes Status; other positive damage values retained.';src+=[L(CP,211,218)];formal+=[L(b.WP04,137,146)]
            if key=='EffectChance':cons+=[C(S+'011_Battle/003_Move/003_Move_UsageCalculations.rb',489,498,'Shield Dust gate first; external positive override or authored chance; >100 returned before doubling/debug branch.')];formal+=[L(b.WP43,157)];gap=['C05 omission0 default not explicit.']
            if key=='Priority':formal+=[L(F+'combat-requirements/wp47-a-move-attributes-targeting-and-calling.md',73)];gap=['C05 omission0 default not explicit.']
            if key in {'Type','Accuracy'}:cons+=[C(p,203,204,'Display type remains authored type; commented alternatives are inactive.'),C(p,398,399,'Display category and accuracy return stored values.')]
            handoff+=['Target identity and numeric properties feed combat/AI domains; their dynamic target construction, category, order, accuracy and damage rules are not duplicated in PBS review.']
    elif fam=='items':
        p=r.SCHEMA_DIR+'006_Item.rb';src=[L(p,119,137)];formal=[L(b.WP27,45,67)];vectors=[L(TITEM,299,304)]
        if key in {'Name','NamePlural','PortionName','PortionNamePlural','Description'}:
            cons=[C(p,140,164,'Names and description localize separately; missing portion singular/plural fall back to corresponding ordinary singular/plural.'),C(S+'016_UI/020_UI_PokeMart.rb',21,48,'Shop consumes portion names and appends move name for machines.')];formal+=[L(b.WP03,108)];vectors+=[L(b.TEST,116)]
            if key in {'Name','NamePlural','Description'}:gap=['C05 raw omission defaults not explicit; omitted plural does not derive singular or pluralize it.']
        elif key in {'Price','SellPrice','BPPrice'}:
            cons=[C(S+'016_UI/020_UI_PokeMart.rb',68,87,'Cash shop uses qualified session override or data buy/sell price and importance/positive-sell gate.'),C(S+'016_UI/021_UI_BattlePointShop.rb',68,74,'BP shop uses qualified shared buy override or data BP price.')];formal+=[L(F+'creature-rpg/wp29-shops-and-exchanges.md',110,123)];vectors+=[L(TITEM,137,150)];norm='Nonnegative integer, including0, without compiler/constructor resource cap. Missing SellPrice uses integer half purchase; absent BPPrice1.'
        elif key=='Pocket':cons=[C(S+'013_Items/008_PokemonBag.rb',58,107,'Select configured pocket for quantity, capacity, add, remove and authored-order auto sorting.')];norm='Positive integer at PBS input; no here-proven array-bound validation. Valid configured pocket is a runtime prerequisite.'
        elif key=='FieldUse':cons=[C(S+'013_Items/001_Item_Utilities.rb',644,704,'Route on-creature use, direct Bag use and machines to distinct callers.')];formal+=[L(b.WP03,147,151)];vectors+=[L(b.TEST,100)]
        elif key=='BattleUse':cons=[C(S+'011_Battle/001_Battle/010_Battle_AttackPhase.rb',69,87,'Route registered item action to creature/move, battler, ball or direct use family.')];formal+=[L(b.WP03,148,151)]
        elif key=='Move':cons=[C(S+'013_Items/001_Item_Utilities.rb',710,730,'Machine reads taught move; missing move returns false, confirmed successful learn consumes only by effective consumption predicate.'),C(DC,104,111,'Configured breeding machine inheritance iterates any Item with a Move field, not just a machine-flag inference.')];formal+=[L(WP34,120),L(WP20,141,149)];handoff=['Teaching full cancel/PP/record layers WP28/30; setting Move alone does not grant a FieldUse machine classification.']
        elif key=='Flags':
            cons=[C(p,167,201,'Case-insensitive keyword families classify importance, machines, mail, ball, berry, fossil, mulch, stone, etc.'),C(S+'011_Battle/003_Move/011_MoveEffects_Items.rb',403,436,'Fling prefix eligibility and first complete numeric flag, at least10.'),C(S+'011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',1338,1370,'NaturalGift prefix guard, first full pattern, conditional target Type identity and numeric power.')];formal+=[L(F+'combat-requirements/wp47-a-move-attributes-targeting-and-calling.md',64,67)];vectors+=[L(TITEM,306)];handoff=['Exact Fling/NaturalGift embedded inputs are inventoried separately; all item effects and AI algorithms WP47-B/50/52.']
        elif key in {'Consumable','ShowQuantity'}:
            cons=[C(p,189,201,'Importance gates effective consumption; show-quantity is explicit truth or non-important.'),C(S+'013_Items/001_Item_Utilities.rb',683,699,'Successful selected use family invokes effective consumption; cancellation/failed use does not itself consume here.')];formal+=[L(b.WP04,223,225)];vectors+=[L(b.TEST,159,161)]
    elif fam=='berry_plants':
        p=r.SCHEMA_DIR+'007_BerryPlant.rb';src=[L(p,28,42)];formal=[L(b.WP60,43,49)];vectors=[L(TBERRY,52,61)]
        if key=='Yield':norm='Two numbers are nonnegative minimum candidate and positive maximum candidate; reverse pair if second<first, then expose ordered minimum/maximum.';cons=[C(b.BERRY,83,92,'Compute old/new yield from normalized range.')];formal+=[L(b.WP60,136,143)]
        else:cons=[C(b.BERRY,97,159,'Require planted and positive elapsed time; use hours×3600 and drying per hour with named mulch/old-vs-new mechanisms.')];formal+=[L(b.WP60,72,98)]
    elif fam=='pokemon_metrics':
        p=r.SCHEMA_DIR+'010_SpeciesMetrics.rb';src=[L(p,59,80)];formal=[L(b.WP03,56),L(WP73B,160,164)];vectors=[L(b.TEST,63,66)];gap=['C06 authored partial form metrics use per-field defaults, whereas missing whole record query clones base; formal lacks explicit authored-default table.']
        if key=='ShadowSize':cons=[C(S+'010_Data/002_PBS data/009_Species_files.rb',156,173,'Species/form-specific shadow assets take priority; otherwise request generic Shadow/N from size, including0.')];formal+=[L(F+'engine-overworld/wp15-resource-matching-and-audio.md',59,63),L(WP73B,134,137)];gap+=['C08: 0=None is an editor label; resource selector itself does not suppress generic0.']
        else:cons=[C(p,71,80,'Back/front offsets doubled; front altitude subtracts doubled amount; shadow X applies only to opponent slots.')];formal+=[L(WP73B,130,132),L(WP73B,162)]
        norm='Authored metric record missing fields uses numeric defaults, even for a nonzero form. A wholly missing query creates base defaults or clones all five base metric groups; those are separate entries.'
    elif fam=='shadow_pokemon':
        p=r.SCHEMA_DIR+'011_ShadowPokemon.rb';src=[L(p,11,22),L(p,35,53)];formal=[L(b.WP23,61,67)];vectors=[L(TST,167,176)]
        if key=='GaugeSize':cons=[C(b.SHADOW,32,43,'Resolve optional per-form/base gauge size, else4000; adjustment clamps to resolved max.')]
        elif key=='Moves':cons=[C(b.SHADOW,114,139,'Preserve authored list order; retain runtime-defined move IDs until MAX_MOVES, else SHADOWRUSH fallback if defined.')];norm='Compiler enum validation is distinct from runtime existence filtering; do not treat invalid author ID as a silently skipped successful compile.'
        else:cons=[C(p,56,58,'Case-insensitive generic flag query; no Flags in the131 authored rows.')]
        handoff=['Only optional author schema, identity/base fallback and gauge/moves entry wiring here; Shadow stages, hyper, purification and combat algorithms WP23/40/43.']
    assert cons,(fam,key)
    return src,cons,formal,vectors,norm,handoff,gap

def run():
    a.bind();records=r.readrecords();actual={(x['family'],f['key']) for x in records for f in x['fields']};rules=[]
    for fam,schema in r.SCHEMAS.items():
        p=r.SCHEMA_DIR+r.SOURCE_FILE[fam]
        for key,shape in schema.items():
            src,cons,formal,vectors,norm,handoff,gap=details(fam,key)
            decl=[]
            for n,line in enumerate((a.ROOT/p).read_text().splitlines(),1):
                if re.search(r'"'+re.escape(key)+r'"\s*\]?\s*(?:=>|=)\s*\[:',line):decl.append(L(p,n))
            omission={'base_or_record_default':DEFAULT[fam][key],'kind':'record_constructor_default'}
            if fam=='pokemon_forms':
                if key in SPECIES_INHERIT:omission={'kind':'inherit_base_when_field_missing','base_or_record_default':'effective base field','special':'Moves/Evolution empty lists inherit too; wild-item fields inherit only when all3 absent.'}
                elif key not in {'FormName','PokedexForm','MegaStone','MegaMove','UnmegaForm','MegaMessage'}:raise AssertionError((fam,key))
                src+=[L(CP,448,484)]
            rule={'rule_id':'AUTHOR.'+fam+'.'+key,'family':fam,'field':key,'appears_in_assigned_data':(fam,key) in actual,'schema_shape':shape,'schema_source':decl,'omission':omission,'constructor_source':L(p,*INIT[fam]),'normalization_and_override':norm,'normalization_source':src,'property_repetition':'Evolution appends after any plural Evolutions; all other same-spelling properties take later authored value. Unknown legal properties ignored by schema iteration.','necessary_consumers':cons,'formal_clauses':formal,'related_existing_vectors':vectors,'formal_assessment':'PROPOSED_GAP_FOR_PARENT' if gap else 'FINITE_RULE_MAPPING_REVIEWED','gap_proposals':gap,'cross_domain_handoffs':handoff,'premises':['Unique valid record identity, legal lexical fields and required enum registries available at the correct compilation phase.','No additional plugin/override, no earlier exception; ordinary warning/localization/host dependencies return normally as explicitly needed.','Runtime mutation, UI completion and downstream effect success are not inferred from author data acceptance.'],'shared_parser_sources':[L(PARSER,72,77),L(PARSER,95,143),L(PARSER,255,292),L(PARSER,384,435),L(PARSER,438,483),L(PARSER,690,736),L(CP,26,67)],'shared_formal_parser':[L(b.WP03,122,151),L(b.WP03,153,176)],'review_status':'HUMAN_RULE_REVIEW_COMPLETED_WITH_PROPOSALS; NOT_PASS'}
            # Source-native export overrides are described behaviorally, and
            # scope handed to K for complete writer lifecycle auditing.
            export='Generic writeout omits false/empty arrays; typed zero normally survives; source suffix chooses files. No byte-roundtrip guarantee.'
            esrc=[L(S+'010_Data/001_GameData.rb',235,241),L(WRITER,23,60)]
            if fam in {'pokemon','pokemon_forms'}:
                export='Species writeout maps six columns back, writes dimensions as tenths/10, skips empty form name, Generation0 and HabitatNone; forward Evolution only with parameters converted to text. Forms suppress fields equal to base with coupled wild-item comparison.';esrc=[L(SP,391,450),L(WRITER,174,290)]
            elif fam=='items':export='Omit default half sell-price/BP1 and use-family0; emit Consumable=false for non-important items, omit true or importance-overridden raw state.';esrc+=[L(p,252,267)]
            elif fam=='moves':export='Also omit Power/Priority/EffectChance0; this does not change these fields in memory.';esrc+=[L(p,401,405)]
            elif fam=='pokemon_metrics':export='Only nonzero-form records select suffix paths; equal-to-base full metric groups suppress nonzero-form section, not selected file. Altitude0 omitted.';esrc=[L(p,89,98),L(WRITER,291,350)]
            elif fam=='shadow_pokemon':export='No Shadow records means no Shadow output; section form0 omitted from header, positive form retained.';esrc=[L(p,60,67),L(WRITER,356,358)]
            rule.update(export_behavior=export,export_sources=esrc,export_formal=[L(b.WP04,184,191),L(b.WP04,199,227)])
            rules.append(rule)
    a.save('field-semantic-rules.json',rules)
    # Verify that every rule's premise-bearing source/contract/vector range was
    # actually model-visible, independently of raw data inventory.
    ledger=[json.loads(x) for x in (a.OUT/'reading-ledger.jsonl').read_text().splitlines()];seen=defaultdict(set)
    for x in ledger:
        if x['mode']=='model_visible_contiguous_read':seen[x['path']].update(range(x['start_line'],x['end_line']+1))
    missing=[]
    for rule in rules:
        groups=rule['schema_source']+[rule['constructor_source']]+rule['normalization_source']+[x['location'] for x in rule['necessary_consumers']]+rule['formal_clauses']+rule['related_existing_vectors']+rule['shared_parser_sources']+rule['shared_formal_parser']+rule['export_sources']+rule['export_formal']
        for z in groups:
            absent=[n for n in range(z['start_line'],z['end_line']+1) if n not in seen[z['path']]]
            if absent:missing.append({'rule_id':rule['rule_id'],'path':z['path'],'requested':z,'missing_lines':absent})
    a.save('field-rule-reading-gaps.json',missing)
    a.save('field-semantics-summary.json',{'actual_family_fields':len(actual),'actual_fields_with_rule':sum(x['appears_in_assigned_data'] for x in rules),'including_omission_only_fields':len(rules),'missing_rule_definitions':[list(x) for x in actual if not any(z['family']==x[0] and z['field']==x[1] for z in rules)],'missing_required_reading_ranges':len(missing),'status':'CONTINUE_READING' if missing else 'RULE_REVIEW_COMPLETE_FOR_PARENT_ADJUDICATION_NOT_PASS','gap_affected_fields':sum(bool(x['gap_proposals']) for x in rules),'semantic_effect_internal_algorithms':'explicitly outside PBS scope; exact entry bindings/handoffs retained'})
    print(json.dumps(b.read('field-semantics-summary.json'),ensure_ascii=False,indent=2))
    unique={}
    for x in missing:
        key=(x['path'],min(x['missing_lines']),max(x['missing_lines']));unique[key]=True
    print('REQUIRED_READ_RANGES',json.dumps(list(unique),ensure_ascii=False))

if __name__=='__main__':
    a.append('command-log.jsonl',{'time':a.now(),'script':'field_semantics.py','script_sha256':a.sha(Path(__file__).read_bytes()),'purpose':'human-written author-field semantics and mandatory reading coverage verification; not a behavior model'})
    run()
