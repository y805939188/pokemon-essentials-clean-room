import review_state as s
for path,a,b,entry,rules,targets in [
('Data/Scripts/010_Data/002_PBS data/016_Metadata.rb',1,81,'Metadata全部','起始money3000/PC空、home空、Bill回退/音频空/后缀；编辑数值与文本界限不同',['WP24','WP27','WP29','WP03']),
('Data/Scripts/010_Data/002_PBS data/007_BerryPlant.rb',1,45,'BerryPlant数据全部','3h/15干燥/2–5产量默认、倒置原地reverse、四喷壶顺序、9次重种4+4阶段',['WP60']),
('Data/Scripts/016_UI/010_UI_Phone.rb',1,271,'Phone全','可见名单/注册与就绪统计；持久实时移动与取消还位、隐藏删除/可见稳定分组、三排序；现记录呼出',['WP63 §4–5']),
('PBS/trainers.txt',1,118,'全部训练家节与成员字段','所有默认参战队伍/版本/物品池及held物；两份FULLRESTORE保重复，物种Shadow输入可得不等于可选数据启用',['WP24','WP39','WP23']),
('PBS/trainer_types.txt',1,401,'全部类型数据','全部身份/性别/奖金、可省Skill回落BaseMoney、leader/champion音频覆盖；内容值与功能规则分开',['WP24 §5','WP03']),
('PBS/metadata.txt',1,33,'全局与两个玩家角色','3000/POTION与空默认差异、home和Bill、两角色资源字符串；音频缺失WildCaptureME需调用者回落',['WP24','WP27','PT41–63']),
('PBS/phone.txt',1,48,'默认/Jeff/Susie三消息组','通用与时段问候、body/body1/2、battle request/remind、end；按版本/默认回落消费；不据文本证明demo事件可达',['WP63 §5'])]:
 s.source(path,[(a,b,entry,rules,targets,'supported_static领域数据/业务投影；实际载入/媒体/宿主/事件未执行')],'data_or_business_consumer')
s.source('Data/Scripts/010_Data/001_GameData.rb',[(78,145,'ClassMethodsSymbols全部','register直接构造，无旧name字段转换；存在性/严格宽容/实例/枚举/保存；用于物品与类型的新建字段反证',['WP03','WP73-A'],'supported_static低层，新建文本丢失线索待完整负证'),(212,243,'InstanceMethods全部','身份相等/Schema取属性/false空数组省略，不把未提交name字段写回来',['WP03','WP04'],'supported_static')],'shared_data_dependency')
s.source('Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb',[(342,443,'TrainerType editor/new完整','已有schema路径与新建手工名键区别、IDs/三性别/0–255钱/新建立即保存反写',['WP73-A §4.1','WP24'],'新建名称丢失线索待反证'),(445,599,'Trainer battle editor全','八物品与队伍槽；同键覆盖/重键删除；lose_text手工键不匹配；外层确认与嵌套保存分层',['WP73-A §4.2','WP24'],'多数supported_static；败词丢失待候选'),(601,687,'TrainerPokemonProperty全','完整20字段、MAX_MOVES/空物种/招式去重、IV EV共享结构，返回不独立确认',['WP73-A §4.2','WP24'],'supported_static'),(689,774,'Metadata/player editor完整','最小未用ID、缺角色拒绝、schema回填/保suffix和保存',['WP73-A §4.5'],'supported_static')],'business_consumer_projection')
s.source('Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb',[(1,65,'通用PBS反写全入口','按suffix分文件/写字段省nil/重复属性逐行；存储读取真实字段不使用编辑器原名变量',['WP04','WP73-A'],'supported_static文本投影；未写R'),(447,506,'TrainerType/Trainer反写全部','TrainerType通用写；Trainer主与成员schema，lose文本从real_lose_text导出',['WP04','WP24'],'supported_static')],'shared_data_dependency')
d=s.load('data-inventory')
for f in d['sources']:
 f['semantic_review']={
  'business_fields':'All enumerated records identity/pocket/prices/field-use/battle-use/consumable/quantity/move/flags manually compared in full baseline table or grouped variant differences; parser equality alone is not semantic evidence.',
  'baseline_primary':'PBS/items.txt',
  'variant_review_artifact':'item-variant-differences.txt (all 484 rows read; grouped identical deltas are a lossless data view, not a behavior execution)',
  'reviewed_rules':['field-use routing and machine importance','battle-use routing and missing-handler defaults','case-insensitive flags and Fling/NaturalGift consumer syntax','price data defaults vs resource setter limits','default consumption and explicit false vs important items','Shadow optional files lack Scent','Gen5/6/7 alternate machine identities/prices and absent MegaRing flag are data variants, not runtime generation switching'],
  'spec_targets':['WP02 data activation','WP03 identity/schema','WP27','WP28','WP29','WP38','WP47-A/B','WP50','WP64'],
  'comparison_result':'supported_static data-driven routing; exact active effect parameter catalog remains partial; literal names/descriptions are not requirements to reproduce'
 }
 f['review_extent']='partial';f['evidence_level']='static_semantic_business_field_review';f['unreviewed_semantic_fields']=['literal display names/portion names/descriptions (M10 presentation projection only, not analyzed for wording accuracy)']
s.save('data-inventory',d)
d=s.load('spec-to-source')
for q in d['specifications']:
 fp=s.REPO/q['path']
 if fp.exists():
  q['line_count']=len(fp.read_text().splitlines())
  for section in q['sections']:section['lines'][1]=min(section['lines'][1],q['line_count'])
s.save('spec-to-source',d)
