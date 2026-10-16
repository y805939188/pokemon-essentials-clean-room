"""Persist this reader's explicit finite semantic notes; no source execution."""
from pathlib import Path
import datetime,json
O=Path(__file__).resolve().parent
inventory=json.loads((O/'current-programs-v2/inventory.json').read_text())
facts=[]
def fact(id_,summary,source,consumer,spec,premise,disposition='SOURCE_STATIC_PENDING_RECEPTION'):
    facts.append({'id':id_,'reader':'/root/preflight_resources','summary':summary,'source':source,'consumer':consumer,'spec':spec,'premise':premise,'evidence_level':'SOURCE_STATIC','execution_status':'NOT_EXECUTED','disposition':disposition})
wp15='deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md'
wp16='deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md'
wp74='deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md'
wp75='deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md'
notes={
1:'Two independent inclusive atlas predicates apply horizontal A and vertical C offsets before normalized coordinates; position uses translation and projection.',
2:'Vertical blur coordinates sample source texel y−1/y/y+1, normalized after offset; projected position does not translate.',
3:'Horizontal blur coordinates sample source texel x−1/x/x+1, normalized after offset.',
4:'Position is projected after a supplied matrix; texture coordinates normalize; supplied color passes through.',
5:'RGBA averages three supplied texture samples with equal one-third weights, including alpha.',
6:'Autotile row determines frame-count lookup before atlas predicate multiplication; frame-count nonzero and index-in-range are required. Animation remainder splits into eight columns and row offset.',
7:'Supplied sprite transform precedes projection; enabled tiled and untiled pattern coordinates use different inverse-size factors and supplied zoom denominator.',
8:'Projected translated position and normalized texture coordinates pass supplied color.',
9:'Projected translated position and normalized texture coordinates.',
10:'Position-only projection with z0/w1.',
11:'Separable six-by-six Lanczos sample weights clamp absolute kernel argument away from zero, normalize each axis, accumulate36RGBA samples; sums and supplied sizes are premises.',
12:'Brightness multiplies supplied RGB and forces alpha1.',
13:'Sample, weighted luma(.299,.587,.114) gray mix, RGB tone addition, alpha opacity multiplication, RGB color mix, in that order.',
14:'Sample unchanged RGB and multiply alpha by supplied alpha.',
15:'Sample unchanged RGB and multiply alpha by interpolated color alpha.',
16:'Output supplied interpolated RGBA.',
17:'Output texture sample without additional arithmetic.',
18:'Output supplied constant RGBA.',
19:'Sample, weighted luma gray interpolation; preserve alpha.',
20:'Gray then additive RGB tone then alpha opacity then RGB color then RGB flash; alpha unaffected by RGB mixes.',
21:'Source-over approximation: source alpha times opacity; destination alpha times remaining source coverage; alpha sum; zero resultant alpha preserves source RGB, otherwise weighted normalized RGB.',
22:'Linear mix frozen→current scene by supplied progress, without local progress clamp.',
23:'Transition-map red clamped between progress and progress+vague, then divided by vague; mix current→frozen by that alpha. No local zero-vague guard.',
24:'RGB↔HSV conversion uses tiny denominators, adds supplied hue and wraps through fractional conversion; original alpha preserved.',
25:'Optional pattern modulo coordinates and normal/add/subtract RGB blend precedes gray,tone,alpha opacity,color,invert,bush. Pattern blend clamps before interpolation; strict y<bushDepth drives final alpha factor.',
26:'GLSLES prelude selects mediump float; desktop prelude empties highp/mediump/lowp qualifiers.',
28:'Fragment-shader compile-time macro declaration only; attachment and producer unknown.',
29:'GLSLES compile-time macro declaration only; attachment and producer unknown.',
32:'Rectangle texture aliases plus half chroma-coordinate scale; native concatenation choice unknown.',
33:'Unit chroma-coordinate scale macro alternative; native concatenation choice unknown.',
34:'Legacy fixed-function projected position and color passthrough.',
35:'Legacy interpolated color output.',
36:'Legacy fixed-function position/color/texture-coordinate passthrough.',
37:'Texture alpha forced1 before multiplying all components by color.',
38:'Texture RGBA multiplied by color RGBA.',
48:'External OES sampler with required extension, sampled RGBA multiplied by color.',
58:'Sampled alpha forced1, then RGBA multiplied by color.',
59:'Sample red/blue exchange, alpha forced1, then multiply color.',
60:'Sample red/blue exchange, preserve sampled alpha, then multiply color.',
61:'Sample RGBA multiplied by color.',
62:'Supplied constant color output.',
63:'Supplied sine and cosine-minus-one parameters form center-relative transform before projection; pass texture coordinates; point size1.'}
for row in inventory:
    if row['kind']!='GLSL_LITERAL_OR_PRELUDE':continue
    n=int(row['id'].split('-')[1])
    if n in [27,30,31,64,65,66]:
        summary={27:'Animation-dimension diagnostic format string.',30:'Attribute-error diagnostic fragment.',31:'Message-digest attribute-length diagnostic.',64:'Compressed-library dictionary containing incomplete HTML/JavaScript-looking text, not a coherent shader or browser program.',65:'JPEG precision diagnostic.',66:'JPEG quantization-table diagnostic.'}[n]
        d='INVENTORY_ONLY_NONPROGRAM_TYPED_LITERAL'
    else:
        summary=notes.get(n)
        if summary is None:
            if 39<=n<=47:
                group=(n-39)//3; matrix=(n-39)%3
                summary=f'YUV conversion coefficient family{matrix}: Y red channel; chroma uses '+['three separate R planes','shared chroma RA channels','shared chroma AR channels'][group]+', chroma coordinate scale supplied by macro. Add family offset then per-component dot products; force alpha1 then multiply RGBA color.'
            elif 49<=n<=57:
                group=(n-49)//3; matrix=(n-49)%3
                summary=f'YUV conversion matrix family{matrix}: Y red channel; chroma uses '+['shared AR channels','shared RA channels','three separate R planes'][group]+'. Add family offset, matrix multiplication, force alpha1 then multiply RGBA color; same v_texCoord used for all samplers.'
            else:raise ValueError(n)
        d='CONDITIONAL_LITERAL_FACT_NATIVE_SELECTION_LIMIT_L04_L05'
    fact('RES-SH-'+row['id'],summary,{k:row[k]for k in ['path','start','end_exclusive','sha256','lines']},['native shader construction/selection/supplied uniforms/texture state UNVERIFIED','mkxp.json optional scaling declarations; not proven wiring'],[wp16+' §3.3/§4/§6; high-level consumer only, no active literal selection proved'], 'Read literal in full; external samplers, precision, array bounds, denominators and native activation remain explicit premises.',d)
an=[
('AN01','No arguments print help and wait for ENTER; with arguments only argument0 is used.',[15],'§18.1','TOOL-AN-07'),
('AN02','Missing XML path and named reader-constructor IO exception request diagnostic and exit1; other exceptions are not unified.',[12,15],'§18.1','TOOL-AN-08'),
('AN03','All XML is parsed before any image-output loop. Root mismatch can return empty collection; output name and ordered pattern records come from reader attributes.',[13,14,15],'§18.1/§18.3','TOOL-AN-06/14'),
('AN04','Absent/empty x ignores remaining rectangle attributes; present x parses x,y,width,height as nonnegativeInt32, accepting zero; missing/overflow differ from FormatException.',[10,11,14],'§18.1','TOOL-AN-05/09/10/11/12/13/16'),
('AN05','Pattern list count determines width960,height192 for0 or192*ceil(n/5); index i slot(192*(i mod5),192*floor(i/5)); destination offsets96−w,96−h and dimensions2w,2h.',[1,4,15],'§18.2','TOOL-AN-01/02/03'),
('AN06','Missing image path diagnoses and skips only that image; original index still increments so no compacting; existing undecodable image is distinct failure.',[15],'§18.2/§18.3','TOOL-AN-04/17'),
('AN07','Weak cache reuses live images; alpha images retained, nonalpha uses Bitmap copy and transparent-color request from top-left pixel; library effects unobserved.',[7,8,9,15],'§18.2','TOOL-AN-15'),
('AN08','Rectangle IsEmpty library result controls whole-image fallback; interpolation enum5 and draw-unit enum2 are requested; no local96 cap.',[15],'§18.1/§18.2','TOOL-AN-10/16'),
('AN09','Each animation Save(name) occurs after its pattern loop; no selected encoder parameter or .anm bridge. Later failure cannot erase successful earlier file by any visible rollback.',[15],'§18.3','TOOL-AN-06'),
('AN10','XML exception diagnostic contains unmatched placeholder; IO diagnostic differs. Finally closes/disposes via requested external calls; cleanup does not certify file success.',[14,15],'§18.3','TOOL-AN-14'),
('AN11','ParseXmlInt accepts any Int32 and has FormatException-only failure path; metadata contains this method but Main parsing routes to nonnegative parser.',[10,11,14],'§18.1; unused helper is audit fact','NOT_APPLICABLE_no_default_caller')]
for id_,summary,methods,section,vector in an:
 fact('RES-'+id_,summary,{'path':'animmaker.exe','methods':methods,'identity_ref':'source-identities.json#animmaker.exe','full_CIL':'evidence/current-animmaker-cil.stdout'},['independent author CLI; documentation animmaker.txt; no default in-game invocation located'],[wp74+' '+section,'test-catalog/demo-dx: '+vector],'All preceding metadata/reader/image/filesystem operations normal unless this fact names their failure; external .NET effects not executed.')
ext=[
('EXT01','Business entry uses named mutex: duplicate returns0 and stops; creation failure−1 remains distinct and can continue; close only valid handles.','0x401352–0x4013c2;0x4013c9–0x4013e3','§14进入门/重复退出','EXT-10'),
('EXT02','Top-level enumeration requires case-sensitive class substring Afx: and title substring RPG Maker XP; no process-ownership check.','0x40129c–0x401352','§14进入门','EXT-09'),
('EXT03','Independent exact #32770 dialog title branches Script,Show Text,Comment,Batch Text Entry; each requests frame then firstEDIT geometry.','0x4013e8–0x401598','§14四目标表','EXT-01/02/03/04/05/06'),
('EXT04','Requested frame/editor sizes are840×240/800×176,840×144/800×72,840×164/800×92,840×444/800×372. Flags preserve position,z,activation; returns ignored.','0x4013e8–0x401598','§14四目标表/请求顺序','EXT-01/02/03/04/08'),
('EXT05','Batch button1 and2 handles queried separately; existing ones request positions(25,392)/(150,392), preserve size,z,activation; missingEDIT does not suppressbuttons.','0x401530–0x4015d5','§14Batch独立控件','EXT-04/06/07'),
('EXT06','After target iteration requestSleep150ms then recheck marker; marker disappearance exits and does not restore geometry. No independent business cancel.','0x4015d5–0x4015ff','§14退出与前缀','EXT-05/11'),
('EXT07','Interpreter SyntaxError diagnostic can suggest tool for opening-parenthesis lines but does not start executable or repair script.','Data/Scripts/003_Game processing/003_Interpreter.rb:137–181','§14解释器建议','EXT-12')]
for id_,summary,offset,section,vector in ext:
 fact('RES-'+id_,summary,{'path':'extendtext.exe','offset_or_consumer':offset,'identity_ref':'source-identities.json#extendtext.exe','disassembly':'evidence/current-extendtext-disasm.stdout;current-extendtext-aligned.stdout'},['independent Win32 author tool; extendtext.txt; interpreter diagnostic only'],[wp75+' '+section,'test-catalog/demo-dx R7-U11-'+vector],'Normal API/query calls and stable windows within loop; supplied returns only select visible branches; geometry/ownership/timing never observed.')
fact('RES-LOAD01','One inert archive record contains titleMain and compressed49-line loader. Loader discovers nonhidden directories, sort-loads current directory scripts before recursively sorted folders; error layers preserve ScriptError vs ordinary traceback handling.',{'path':'Data/Scripts.rxdata','range':[0,594],'decoded':'current-serialized/Main.rb','identity':'current-serialized/Main.identity.json'},['scripts_extract.rb','scripts_combine.rb','Data/Scripts/999_Main/999_Main.rb'],[wp75+' §12.4'],'No loader evaluation, Ruby deserialization callbacks, encrypted-game boot or native selection observed.')
fact('RES-COMP01','XP,VX,Ace are mutually distinct legacy definitions, with different constructor defaults, target predicates, tables, animations and audio alias/clone/position behavior. They are not one merged default Pokemon database.',{'path':'Game.exe','units':['RPG-37','RPG-38','RPG-39'],'lines':3448},['current file loader and source reopenings; no native profile selection proved'],['GR6-POL-001 retained; active consumer contractsWP15/WP16/WP75'],'Use one exact conditional profile; native selection/dynamic values absent.','INDEPENDENT_POLICY_NOT_SELECTED')
fact('RES-COMP02','CurrentSprite/Cache/Weather definitions replace specific legacy methods; default animation/weather loops use current runtime clocks and registeredweather. Constructor defaults differ from deserialized field values.',{'paths':['Data/Scripts/001_Technical/006_RPG_Sprite.rb','Data/Scripts/007_Objects and windows/001_RPG_Cache.rb','Data/Scripts/005_Sprites/008_Sprite_AnimationSprite.rb','Data/Scripts/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb']},['Spriteset_Global','Game_Screen','Audio_Play and Game_System current consumers'],[wp15+' §5/§6',wp16+' §4.5/§5.1'],'Normal loading in declared sorted order, matching schema and no plugin replacement. Full downstream engine consumer closure remains pending.')
fact('RES-TOWN01','Two actual8×8BMP marker structures contain all128pixels; page positions8-pixel icons within supplied cellsize, existing points before selected overlay. RegionPNG remains missing.',{'paths':['knownpoint.bmp','selpoint.bmp','townmapgen.html'],'pixels':'current-bmp-all-pixels.json'},['townmapgen.html createMapPoint/showMapPoints'],[wp75+' §13.3','CV-M30'],'Source pixel values/DOM requests only; no browser load or visual result.')
for row in inventory:
 if row['kind']!='C_TEMPLATE_FRAGMENT':continue
 number=int(row['id'].split('-')[1]);kind='NATIVE_JIT_TEMPLATE_FRAGMENT'if number not in[67,714,715,716]else'FALSE_PROGRAM_CANDIDATE_TYPED_BYTES'
 fact('RES-C-'+row['id'],'Conditional native code-template literal; substitutions, selected call target and surrounding generator determine executable meaning.'if kind=='NATIVE_JIT_TEMPLATE_FRAGMENT'else'Punctuation/character-table bytes, not a coherent executable C program.',{k:row[k]for k in ['path','start','end_exclusive','sha256','lines']},['Ruby310 native generator assembly/substitution selection UNVERIFIED'],['L04 native/generator boundary; no copied interpreter architecture requirement'],'Literal fully read; helper names are interface names, not proof of helper semantics or activation.',kind)
(O/'forward-map.json').write_text(json.dumps({'schema':'r8.resource.forward.v1','reader':'/root/preflight_resources','updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'facts':facts,'new_behavior_execution':0,'native_global_closure':False},ensure_ascii=False,indent=2)+'\n')
reverse=[]
for item in facts:
 if item['id'].startswith(('RES-AN','RES-EXT','RES-LOAD','RES-COMP','RES-TOWN')):
  for target in item['spec']:reverse.append({'spec_clause_or_vector':target,'source_fact':item['id'],'premise':item['premise'],'support':'FINITE_STATIC_SUPPORTED_PENDING_INDEPENDENT_RECEPTION','excluded':'native execution/runtime equivalence'})
(O/'reverse-map.json').write_text(json.dumps({'schema':'r8.resource.reverse.v1','rows':reverse,'clause_granularity':'named compound sections and individual vectors; not a complete all-formal-clause map','unmapped_other_clauses':'pending domain primary readers; not upgraded by source-fact pointer'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'finite_fact_records':len(facts),'reverse_named_bindings':len(reverse),'required_accepted':0,'independent_reception':'PENDING'}))
