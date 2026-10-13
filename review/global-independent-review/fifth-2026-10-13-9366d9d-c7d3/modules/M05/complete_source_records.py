import review_state as s
import re, hashlib

for path,a,b,entry,rules,targets in [
 ('Data/Scripts/004_Game classes/008_Game_Player.rb',600,616,'Bike mount/dismount complete','Already mounted/dismounted early return; mount marks/counter/vehicle/BGM/SE then clears radar; dismount clears flag/vehicle/map BGM.',['WP12 §5.1','WP37 §8.1']),
 ('Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb',791,832,'Sweet Scent complete direct tool','Non-None world weather returns before animation/encounter; ordinary effect gets current encounter type and explicit request; failure gives message; Honey caller still returns true.',['WP59 §5.3–5.4','WP28 §4']),
 ('Data/Scripts/012_Overworld/005_Overworld_Fishing.rb',1,110,'All fishing procedures','Begin/end common-event fallback; first non-egg ability; 45/70/95 thresholds times1.5 without cap; waiting min-of-two; input-before-timeout and strict >; auto disables timeout but waits input; caller encounter/statistics separate.',['WP60 fishing §3–10','WP28']),
 ('Data/Scripts/001_Technical/002_Files/003_HTTP_Utilities.rb',1,83,'HTTP full context; M05 GET consumer','GET host exception empty, non-map raw return, non200 empty,200 body/file; string convenience catches ordinary exceptions. POST read for separation only, not execution or historical test adoption.',['WP07 §4','WP64 §5']),
 ('Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb',450,469,'Explicit encounter request complete','Writes type first, chooses/hooks one or optional second, nil early return retains type/force flag; normal battle return clears both then true. Fish/Honey caller does not turn absent battle into refund.',['WP36 §7','WP60 fishing §7','WP28']),
 ('Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb',433,436,'Separator only','No executable branch between plant interaction and harvest helper.',['WP60 berry']),
 ('Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb',1037,1044,'Card total and storage close','Total sums all slot counts; helper container separate from bag.',['WP68 §3','WP27']),
 ('Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb',1045,1138,'Card purchase full caller','Owned base species/name sort; initial and post-confirm affordability; quantity max99; preflight then add then money; unchecked add result, normal cleanup only.',['WP68 §7','WP24']),
 ('Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb',1139,1244,'Card sale full caller','List per slot but sale qty sums identity; integer quarter unit price then qty; money first then unchecked deletion; cancel/no confirmation no transfer, price zero exceptional branch.',['WP68 §7','WP24']),
 ('Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb',1245,1300,'Card list/gift full caller','Viewing no inventory change; give uses try species then can_add before add and true, no add return recheck.',['WP68 §3/§7','WP27'])]:
 s.source(path,[(a,b,entry,rules,targets,'supported_static bounded business-consumer comparison; no execution')],'business_consumer_projection')

def intervals(nums):
 out=[]
 for n in sorted(set(nums)):
  if out and out[-1][1]+1==n:out[-1][1]=n
  else:out.append([n,n])
 return out

d=s.load('reading-coverage')
di=s.load('data-inventory')
for q in di['sources']:
 ls=(s.REF/q['path']).read_text(encoding='utf-8-sig').splitlines()
 literal=[];business=[];other=[]
 for n,l in enumerate(ls,1):
  m=re.match(r'\s*([A-Za-z_]+)\s*=',l)
  if m and m[1] in ['Name','NamePlural','PortionName','PortionNamePlural','Description']:literal.append(n)
  elif m or l.startswith('['):business.append(n)
  else:other.append(n)
 q['actual_semantic_line_ranges']=intervals(business)
 q['unreviewed_intervals']=intervals(literal)
 q['excluded_nonbehavioral_intervals']=intervals(other)
 q['in_scope_unreviewed_intervals']=[]
 q['review_boundary']='Every business-field row was reviewed via full baseline table and lossless variant-difference views. Literal display wording is excluded M10 content; comments/separators have no extra business contract.'
 rec={'path':q['path'],'version':s.R,'sha256':q['sha256'],'line_count':q['line_count'],'role':'primary_item_data_business_fields','review_extent':'partial','material_availability':'available','evidence_level':'static_semantic_business_field_review','semantic_segments':[{'lines':[1,q['line_count']],'actual_semantic_line_ranges':q['actual_semantic_line_ranges'],'entries':'All item identities and business fields; wording excluded','rules_reviewed':q['semantic_review']['reviewed_rules'],'spec_targets':q['semantic_review']['spec_targets'],'comparison_result':'supported_static routing/data flags with explicit field/catalog gaps in M05.item.data / GR5-M05-004; not literal-text certification','execution_status':'not_executed'}],'unreviewed_intervals':q['unreviewed_intervals'],'excluded_nonbehavioral_intervals':q['excluded_nonbehavioral_intervals'],'in_scope_unreviewed_intervals':[],'review_boundary':q['review_boundary'],'detail_record':'data-inventory.json#'+q['path']}
 d['sources']=[x for x in d['sources'] if x['path']!=q['path']]+[rec]
s.save('data-inventory',di)

# Classify designated whole files separately from bounded dependencies.
primary_tokens=['015_Trainers and player/','013_Items/','004_PokemonStorage.rb','002_Utilities_Pokemon.rb','005_UI_Party.rb','006_UI_Summary.rb','007_UI_Bag.rb','016_UI_ReadyMenu.rb','017_UI_PokemonStorage.rb','018_UI_ItemStorage.rb','019_UI_PC.rb','020_UI_PokeMart.rb','021_UI_BattlePointShop.rb','022_UI_MoveRelearner.rb','024_UI_MysteryGift.rb','005_UI_Trading.rb','009_Battle_ItemEffects.rb','011_MoveEffects_Items.rb','006_Battle_ActionUseItem.rb']
for q in d['sources']:
 q['assigned_scope']='whole_file' if any(t in q['path'] for t in primary_tokens) else 'bounded_business_dependency'
 if q['path'].startswith('PBS/') and 'items' in q['path']:q['assigned_scope']='all_business_fields'
 q.setdefault('in_scope_unreviewed_intervals',[])
 if q['review_extent']=='partial':
  q.setdefault('outside_m05_or_nonbusiness_intervals',q['unreviewed_intervals'])
  q.setdefault('review_boundary','Only the listed complete functions/registrations and required callers are M05 consumer projections. Remaining lines belong to the external module, not a claim of full-file semantic coverage.')
 if q['assigned_scope']=='whole_file' and q['unreviewed_intervals']:
  q['in_scope_unreviewed_intervals']=q['unreviewed_intervals']
 for seg in q['semantic_segments']:
  # Correct preliminary swapped end-of-battle package labels.
  if any(t in q['path'] for t in ['Battle_ExpAndMoveLearning','Battle_EndOfRoundPhase','Battle_StartAndEnd']):
   seg['spec_targets']=[t.replace('WP41','WP42') for t in seg['spec_targets']]
s.save('reading-coverage',d)

s.checkpoint(['共享合同主物品投影已完成逐条对照；新增钓鱼/HTTP/主动遭遇尾部和卡片商店完整caller记录','所有主动物品/PBS业务字段语义范围已具体化；名称描述只作M10文字边界，未伪称全文措辞审查'],['完成唯一能力/共享接口映射、逐测试向量绑定及补充版本记录','核验候选全字段和审查产物一致性后报告'])
