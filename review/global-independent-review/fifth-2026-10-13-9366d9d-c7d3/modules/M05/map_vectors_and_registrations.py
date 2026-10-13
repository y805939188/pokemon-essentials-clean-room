import review_state as s
from pathlib import Path
import json,re,subprocess
P='deliverables/final-specification-set/'
S='Data/Scripts/'
paths={'bag':'013_Items/008_PokemonBag.rb','util':'013_Items/001_Item_Utilities.rb','effect':'013_Items/002_Item_Effects.rb','beffect':'013_Items/003_Item_BattleEffects.rb','mail':'013_Items/006_Item_Mail.rb','item':'010_Data/002_PBS data/006_Item.rb','acq':'019_Utilities/002_Utilities_Pokemon.rb','tools':'019_Utilities/001_Utilities.rb','trade':'016_UI/001_Non-interactive UI/005_UI_Trading.rb','party':'016_UI/005_UI_Party.rb','summary':'016_UI/006_UI_Summary.rb','storage':'014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb','boxes':'016_UI/017_UI_PokemonStorage.rb','bagui':'016_UI/007_UI_Bag.rb','pcitem':'016_UI/018_UI_ItemStorage.rb','ready':'016_UI/016_UI_ReadyMenu.rb','pc':'016_UI/019_UI_PC.rb','mart':'016_UI/020_UI_PokeMart.rb','bp':'016_UI/021_UI_BattlePointShop.rb','gift':'016_UI/024_UI_MysteryGift.rb','battleitem':'011_Battle/001_Battle/006_Battle_ActionUseItem.rb','player':'015_Trainers and player/004_Player.rb','trainer':'015_Trainers and player/001_Trainer.rb','pokemon':'014_Pokemon/001_Pokemon.rb','phone':'013_Items/004_Item_Phone.rb','phoneui':'016_UI/010_UI_Phone.rb','passive':'011_Battle/007_Other battle code/009_Battle_ItemEffects.rb','lifecycle':'011_Battle/002_Battler/006_Battler_AbilityAndItem.rb','usemove':'011_Battle/002_Battler/007_Battler_UseMove.rb','moveitem':'011_Battle/003_Move/011_MoveEffects_Items.rb','attribute':'011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb','end':'011_Battle/001_Battle/002_Battle_StartAndEnd.rb','command':'011_Battle/001_Battle/009_Battle_CommandPhase.rb','relearn':'016_UI/022_UI_MoveRelearner.rb','card':'016_UI/012_UI_TrainerCard.rb'}
def A(*items):
 return [{'path':S+paths.get(k,k),'version':s.R,'lines':[a,b]} for k,a,b in items]
def whole(k):
 p=S+paths[k];return (k,1,len((s.REF/p).read_text().splitlines()))
st=s.load('spec-to-source')

def add_cases(rel,ranges,resolver,scope):
 path=P+'test-catalog/'+rel;ls=(s.REPO/path).read_text().splitlines()
 q=next((q for q in st['specifications'] if q['path']==path),None)
 if not q:
  q={'path':path,'version':s.B,'kind':'test_catalog','material_availability':'available','sections':[],'effective_supplements':[]};st['specifications'].append(q)
 q['line_count']=len(ls)
 for a,b in ranges:
  for n in range(a,min(b,len(ls))+1):
   t=ls[n-1];m=re.match(r'^\|\s*([A-Za-z][A-Za-z0-9_-]*\d[A-Za-z0-9_-]*)\s*\|',t)
   if not m:continue
   id=m[1];got=resolver(id,n,t)
   if not got:continue
   cap,anchors,result,status=got
   sec={'lines':[n,n],'section':scope+' / '+id,'vector_id':id,'vector_scope':scope,'input_and_expected_row':t,'source_anchors':anchors,'capability_id':cap,'status':status,'comparison_result':result,'evidence_level':'supported_static' if status=='supported' else 'static_semantic_review','execution_status':'not_executed'}
   q['sections']=[v for v in q['sections'] if not (v['lines']==[n,n])]+[sec]

def fixed(cap,anchors):return lambda id,n,t:(cap,anchors,'supported_static：按该行明示前提逐项静态推导一致；非执行通过。','supported')
add_cases('creature-rpg-wp18-20-24-25-26.md',[(209,249)],fixed('creature.acquisition',A(('acq',1,231),('trade',193,243),('party',1504,1560))),'AQ')
add_cases('creature-rpg-wp27-28-29-30-33.md',[(5,40)],fixed('inventory.container',A(whole('bag'),('bagui',145,179),('bagui',421,704),('pcitem',247,376),('ready',180,331))),'BG')
def iu(id,n,t):
 if not id.startswith('IU-'):return None
 num=int(id.split('-')[-1]);cap='item.active-healing';anchors=A(('util',329,383),('effect',403,713),('beffect',66,182),('beffect',329,532))
 if 9<=num<=17 or num in [49,50]:cap='item.active.ev';anchors=A(('util',384,484),('effect',714,833),('effect',995,1078))
 elif num in [18,19,54,56]:cap='item.active.ability';anchors=A(('util',129,328),('util',485,500),('effect',834,994),('pokemon',916,969))
 elif 20<=num<=25 or num==58:cap='item.learning';anchors=A(('util',579,748),('effect',26,122),('effect',380,402),('party',1083,1164))
 elif 26<=num<=31 or num in [43,55]:cap='item.battle-consumption';anchors=A(whole('battleitem'),('beffect',1,328),('command',100,138))
 elif 32<=num<=34:cap='item.active.battle-stat';anchors=A(('beffect',214,328),('beffect',533,712))
 elif 35<=num<=39:cap='item.field-tools';anchors=A(('effect',26,402),('effect',598,627))
 elif 40<=num<=42:cap='item.active-dispatch';anchors=A(('util',640,777),('bagui',421,594))
 elif 44<=num<=48 or num==57:cap='item.fusion';anchors=A(('effect',1122,1524),('party',746,800),('party',1204,1218))
 elif num==59:anchors=A(('party',1278,1323),('util',329,347))
 result='supported_static：该固定入口与所列前提的局部预期吻合；能力整体partial不自动否定此正常向量。'
 if num in [45,46,57]:result+=' 未包含SPECIAL改变成员集合，不能据此反证GR5-M05-002。'
 if num==50:anchors=A(('018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb',201,218),('util',384,450));cap='item.facility-replay'
 return cap,anchors,result,'supported'
add_cases('creature-rpg-wp27-28-29-30-33.md',[(41,105)],iu,'IU')
add_cases('creature-rpg-wp27-28-29-30-33.md',[(106,121)],fixed('item.active-healing',A(('util',348,383),('util',640,777),('effect',628,713),('beffect',155,182),('beffect',501,532))),'R4-U04-PP')
add_cases('creature-rpg-wp27-28-29-30-33.md',[(122,155)],fixed('shop.transactions',A(('mart',598,748),('mart',1,78),('bp',446,525),('bp',1,45),('player',58,81),('003_Game processing/003_Interpreter.rb',433,449))),'SH')
def gr(id,n,t):
 num=int(id.split('-')[-1]);
 if num<8:return None # growth curves, outside M05 item interface
 if 8<=num<=24 or 45<=num<=48:return fixed('item.passive-calculation',A(('011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',5,224),('passive',1693,1748)))(id,n,t)
 return fixed('item.learning' if num in list(range(25,35))+list(range(49,54)) else 'item.active.ability',A(('util',129,484),('util',579,639),('tools',429,488),whole('relearn'),('pokemon',916,969),('party',1504,1560)))(id,n,t)
add_cases('creature-rpg-wp27-28-29-30-33.md',[(156,214)],gr,'GR M05 interface')
add_cases('creature-rpg-wp27-28-29-30-33.md',[(240,257)],fixed('item.field-tools',A(('util',552,578),('effect',289,355))),'U03-IF')
add_cases('creature-rpg-wp27-28-29-30-33.md',[(258,268)],fixed('item.active.ability',A(('util',222,328))),'U03-EX')
def mg(id,n,t):
 num=int(id.split('-')[-1]);cap='mail.transfer' if num<=13 else 'gift.mystery'
 anchors=A(whole('mail'),('pc',58,105),('util',778,854),('pokemon',552,599)) if num<=13 else A(whole('gift'),('016_UI/013_UI_Load.rb',281,356),('acq',118,151),('bag',58,115))
 status='supported';result='supported_static：逐行固定前提与已读分支一致；未执行。'
 if num==12:status='partial';result='contradiction_static：源在持物赋值前读取mail，失配自清后失败；GR5-M05-001，不能称MG-12静态通过。'
 if num==1:status='partial';result='队伍索引前提下supported_static；对盒中/暂持摘要并不按持有者之后队伍位置，GR5-M05-003。'
 return cap,anchors,result,status
add_cases('creature-rpg-wp35-36-57-64-68.md',[(92,127)],mg,'MG')

UI='user-interface-wp17-63-65-66-67-68-69-70-71.md'
add_cases(UI,[(198,243)],fixed('party.membership',A(whole('party'),whole('summary'),whole('relearn'),('util',579,854))),'PT UI M05 business projection')
def bx(id,n,t):
 num=int(id[1:])
 if num<=19 or num==36:return fixed('party.storage',A(whole('boxes'),whole('storage'),('pc',148,237)))(id,n,t)
 return None
add_cases(UI,[(244,287)],bx,'BX storage only')
add_cases(UI,[(288,328)],fixed('shop.transactions',A(whole('bagui'),whole('pcitem'),whole('mart'),whole('bp'))),'BG UI')
def pg(id,n,t):
 if id.startswith('PL'):return fixed('phone.contacts',A(whole('phone'),whole('phoneui')))(id,n,t)
 k=int(id[1:])
 if 12<=k<=28 or k in [31,32,39,40,41,42,45,46,47]:return fixed('phone.contacts',A(whole('phone'),whole('phoneui')))(id,n,t)
 if k in [1,2]:return fixed('inventory.selection-registration',A(('016_UI/001_UI_PauseMenu.rb',217,237)))(id,n,t)
 return None
add_cases(UI,[(53,130)],pg,'PG phone M05 projection')
def tc(id,n,t):
 if id in ['TC03','TC05','TC08']:return fixed('player.profile-resources',A(whole('card'),('015_Trainers and player/003_Trainer_Sprites.rb',1,68)))(id,n,t)
 return None
add_cases(UI,[(185,197)],tc,'Trainer card business')
def supplements(id,n,t):
 if id.startswith('B16-'):
  if id in ['B16-003','B16-004','B16-A044','B16-A048','B16-B035','B16-C003','B16-C117','B16-C120','B16-C125','B16-C126','B16-D023']:
   return fixed('party.membership' if id not in ['B16-B035','B16-C117','B16-D023'] else 'shop.transactions',A(whole('party'),whole('summary'),whole('boxes'),whole('bagui'),('mart',598,718),('bp',446,525),whole('relearn')))(id,n,t)
 elif id.startswith('U05-MV'):return fixed('mail.transfer',A(('party',934,1020),('boxes',1902,1933)))(id,n,t)
 elif id.startswith('U05-QN'):return fixed('shop.transactions',A(whole('pcitem'),whole('mart'),whole('bp')))(id,n,t)
 elif id.startswith('U05-RF'):return fixed('item.battle-consumption',A(whole('battleitem'),('command',100,138),('end',405,512)))(id,n,t)
 elif id.startswith('U05-NG'):return fixed('item.move-operations',A(whole('usemove'),whole('lifecycle'),('attribute',1339,1380),whole('passive')))(id,n,t)
 return None
add_cases(UI,[(584,614),(659,711)],supplements,'Current B16/U05 M05 business supplements')
add_cases('combat-requirements-wp39-40-41-42-45.md',[(232,245)],fixed('item.battle-consumption',A(whole('battleitem'),('command',100,138),('end',405,512),('011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',597,780))),'U04-RF')
add_cases('combat-requirements-wp47-ab.md',[(98,110)],fixed('item.move-operations',A(whole('usemove'),whole('lifecycle'),('attribute',1339,1380),whole('passive'))),'U04-NG')
def hi(id,n,t):
 if id.startswith('HI') or id.startswith('U04-'):return fixed('item.passive-lifecycle',A(whole('passive'),whole('lifecycle'),whole('usemove')))(id,n,t)
 return None
add_cases('pokemon-rules-wp43-44-46-48-50.md',[(165,234)],hi,'HI and U04 held-item projections')

def ai_items(id,n,t):
 selected=False
 if 43<=n<=77:selected=id.startswith('I') or id in ['S07','S09']
 elif 78<=n<=141:selected=id in ['N02b','N02c','N02d','N05','N07','S01','S08','S10']
 elif 142<=n<=215:selected=id in ['B08','B12b','B17','B24','B25','B35','B37','B39','B52','B62','B63']
 elif n>=216:selected=id in [f'C{i:02}' for i in range(1,21)]+['C34','C42','C43','C48','C53','C54','C55','C58']
 if not selected:return None
 return fixed('item.ai',A(('011_Battle/005_AI/003_AI_UseItem.rb',1,220),('011_Battle/005_AI/008_AI_Utilities.rb',163,229),('011_Battle/005_AI/008_AI_Utilities.rb',387,898),('011_Battle/006_AI MoveEffects/007_AI_MoveEffects_Items.rb',1,376)))(id,n,t)
add_cases('combat-requirements-wp49-51-52.md',[(43,282)],ai_items,'AI/AE/BE/CE item projections; line identifies repeated IDs')

# Effective supplements are fixed-object navigation plus current B5 bindings, not reused verdicts.
supp=[
 {'id':'B07-current-item-growth-controls','path':'review/remediation/20261003-prepare/batches/B07/integration-stage-1/finding-registration.json','version':s.B,'actual_read':'WP28/WP30 current qualifications, minimum revisions, formal clause and static row bindings for A020/A024/A026/A039–A049/B008/C003','boundary':'Only current effective controls and B5 resulting text used; historical PASS not evidence.'},
 {'id':'B16-current-business-trace','path':'review/remediation/20261003-prepare/batches/B16/author-draft-1/traceability.json','version':s.B,'actual_read':'003/004/006/A044/A048/B035/C003/C117/C118/C120/C124/C125/C126/D023 current controls, body/appendix and catalog bindings','boundary':'M05 business projection; no recursive historical management re-audit.'},
 {'id':'B16-effective-source-limits','path':'review/remediation/20261003-prepare/batches/B16/candidate-1/complete-after-R-B16-F01-1/source-limits.json','version':'b24312f680e74c859460dc36254dec20e0e3bf38','material_availability':'available_in_exact_git_object','actual_read':'whole source-limits document','boundary':'No runtime or reference/model execution inherited.'},
 {'id':'WP73A-v4-coverage','path':'review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md','version':s.B,'actual_read':'all four sections/all table rows; current B19 successor precedence','boundary':'Historical appendix used only for bounded counterevidence, not its verdict.'},
 {'id':'B19-current-editor-successor','path':'review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-2/complete-candidate-1/full24-traceability-successor.json','version':'7be976f821a49aa22dadec52cf6165c4e1d0887b','material_availability':'available_in_exact_git_object','actual_read':'WP73-A related 003/C003/C005/C017–C023 current_body_clauses/current_catalog_rows','boundary':'Current CE01–20/B19 related rows read; no source text adapter exception found.'}
]
st['effective_supplements']=supp
for q in st['specifications']:
 n=Path(q['path']).name
 if any(t in n for t in ['wp28','wp30','wp19']):q['effective_supplements']+=['B07-current-item-growth-controls']
 if any(t in n for t in ['wp25','wp26','wp27','wp28','wp29','wp64','wp65','wp66','user-interface-']):q['effective_supplements']+=['B16-current-business-trace','B16-effective-source-limits']
 if 'wp73' in n or 'demo-dx-' in n:q['effective_supplements']+=['WP73A-v4-coverage','B19-current-editor-successor']
 q['effective_supplements']=list(dict.fromkeys(q['effective_supplements']))
s.save('spec-to-source',st)

# A lexical locator of registrations already semantically read. Never executes reference code.
d=s.load('source-to-spec');d['handler_registrations']=[]
pattern=re.compile(r'((?:ItemHandlers|Battle::ItemEffects|Battle::PokeBallEffects|Battle::AI::Handlers)::(\w+))\.(addIf|add|copy)\(')
for f in sorted((s.REF/'Data/Scripts').rglob('*.rb')):
 text=f.read_text();ms=list(pattern.finditer(text))
 if not ms:continue
 rel=str(f.relative_to(s.REF));q=next((q for q in s.load('reading-coverage')['sources'] if q['path']==rel),None)
 # Only dedicated item rankings and the complete item-effects AI file are part
 # of this identity table; other AI item consumer functions are in coverage.
 ms=[m for m in ms if 'Battle::AI::Handlers::' not in m[1] or m[2]=='ItemRanking' or f.name=='007_AI_MoveEffects_Items.rb']
 if not ms:continue
 assert q,('registration_file_not_read',rel)
 for pos,m in enumerate(ms):
  start=text.count('\n',0,m.start())+1
  end=(text.count('\n',0,ms[pos+1].start()) if pos+1<len(ms) else len(text.splitlines()))
  method=m[3];tail=text[m.end():]
  if method=='copy':header=tail[:tail.index(')')];symbols=re.findall(r':([A-Za-z][A-Za-z0-9_]*)',header);ids=symbols[1:];copy_from=symbols[0]
  else:
   key=re.match(r'\s*(?::([A-Za-z][A-Za-z0-9_]*)|["\']([^"\']+)["\'])',tail)
   assert key,(rel,start)
   ids=[key[1] or key[2]];copy_from=None
  family=m[2]
  cap='item.ai' if 'Battle::AI::Handlers::' in m[1] else ('item.passive-lifecycle' if 'ItemEffects::' in m[1] else ('item.capture-balls' if 'PokeBallEffects::' in m[1] else 'item.active-dispatch'))
  assert any(z['lines'][0]<=start<=z['lines'][1] for z in q['semantic_segments']),('registration_not_in_read_range',rel,start)
  affected=[]
  for id in ids:
   if id in ['DNASPLICERS','NSOLARIZER','NLUNARIZER','REINSOFUNITY']:affected.append('GR5-M05-002')
   if id in ['HPUP','PROTEIN','IRON','CALCIUM','ZINC','CARBOS','HEALTHFEATHER','MUSCLEFEATHER','RESISTFEATHER','GENIUSFEATHER','CLEVERFEATHER','SWIFTFEATHER','HEALTHWING','MUSCLEWING','RESISTWING','GENIUSWING','CLEVERWING','SWIFTWING','POMEGBERRY','KELPSYBERRY','QUALOTBERRY','HONDEWBERRY','GREPABERRY','TAMATOBERRY','ABILITYCAPSULE','ABILITYPATCH','DIREHIT','DIREHIT2','DIREHIT3'] and cap=='item.active-dispatch':affected.append('GR5-M05-004')
  d['handler_registrations'].append({'source_path':rel,'version':s.R,'lines':[start,end],'family':m[1],'registration_kind':method,'identities_or_condition_group':ids,'copy_source_identity':copy_from,'capability_id':cap,'status':'partial' if affected else 'supported','evidence_level':'static_semantic_review' if affected else 'supported_static','related_findings':sorted(set(affected)),'semantic_comparison_reference':'reading-coverage.json exact source semantic segments + capability comparison + current spec/test mapping','locator_only':True,'execution_status':'not_executed'})
d['handler_family_definitions']=[{'family_group':'active','source':S+paths['util'],'lines':[1,128],'capability_id':'item.active-dispatch','includes_empty_families_and_defaults':True},{'family_group':'held','source':S+paths['passive'],'lines':[1,265],'capability_id':'item.passive-lifecycle','includes_empty_families_and_defaults':True},{'family_group':'ball','source':S+'011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb','lines':[1,31],'capability_id':'item.capture-balls','includes_empty_families_and_defaults':True}]
s.save('source-to-spec',d)
