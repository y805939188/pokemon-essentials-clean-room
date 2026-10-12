from pathlib import Path
import json,re,subprocess,datetime
out=Path('review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M02')
r=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
f=Path('deliverables/final-specification-set')
read={
'001_Settings.rb':'1-17,65-78,236-244,342-350,506-515 (本域开关)',
'001_Technical/002_RubyUtilities.rb':'366-388 (随机重载)',
'001_Technical/005_PluginManager.rb':'106-649 (注册/版本/元数据/发现/编译/消费；注释与行为区别)',
'001_Technical/001_Debugging/001_PBDebug.rb':'1-77',
'001_Technical/001_Debugging/002_DebugConsole.rb':'1-48,98-110 (实际读取；其余仅符号盘点)',
'001_Technical/001_Debugging/003_Errors.rb':'1-94',
'001_Technical/001_Debugging/004_Validation.rb':'1-31',
'001_Technical/001_Debugging/005_Deprecation.rb':'1-52',
'001_Technical/002_Files/001_FileTests.rb':'1-484 (主要裁决1-107,181-361；StringInput已读未逐边界审查)',
'001_Technical/002_Files/002_FileMixins.rb':'1-149 (已读；二进制基元未做双向详审)',
'001_Technical/002_Files/003_HTTP_Utilities.rb':'1-83',
'002_Save data/001_SaveData.rb':'1-82',
'002_Save data/002_SaveData_Value.rb':'1-284',
'002_Save data/003_SaveData_Conversion.rb':'1-223',
'002_Save data/004_Game_SaveValues.rb':'1-127',
'002_Save data/005_Game_SaveConversions.rb':'1-420 (14项均盘点及读取；深查范围见capabilities)',
'003_Game processing/001_StartGame.rb':'1-126',
'003_Game processing/002_Scene_Map.rb':'164-186,235-251',
'003_Game processing/003_Interpreter.rb':'369-394 (事件私有冷却与通用变量计时反证)',
'003_Game processing/005_Event_Handlers.rb':'1-298',
'003_Game processing/006_Event_HandlerCollections.rb':'1-123',
'004_Game classes/001_Switches and Variables/003_Game_Variables.rb':'1-25',
'004_Game classes/007_Game_Event.rb':'85-129 (事件私有冷却反证)',
'004_Game classes/008_Game_Player.rb':'116-141,524-558',
'004_Game classes/012_Game_Stats.rb':'1-200',
'011_Battle/008_Other battle types/005_RecordedBattle.rb':'120-137,179-196',
'012_Overworld/001_Overworld.rb':'155-226；核心计步172-218',
'012_Overworld/003_Overworld_Time.rb':'1-230 (月相/星座后段未审)',
'012_Overworld/008_Overworld_RandomDungeons.rb':'422-444 (种子投影)',
'013_Items/004_Item_Phone.rb':'1-92,112-145,162-197,275-375,543-560 (其余词命中非已读)',
'016_UI/013_UI_Load.rb':'190-356 (渲染前段未审)',
'016_UI/014_UI_Save.rb':'1-139',
'017_Minigames/005_Minigame_Lottery.rb':'1-42 (仅种子行为裁决)',
'019_Utilities/001_Utilities.rb':'1-210 (AntiRandom与pbTimeEvent族详审；余后段未审)',
'999_Main/999_Main.rb':'1-60'
}
patterns={
 'save_migration':r'SaveData|Game\.(save|load|start_new)|safesave|EmergencySave|save_count|\.bak',
 'extension':r'EventHandlers|MenuHandlers|HandlerHash|PluginManager|NamedEvent|deprecated_method_alias',
 'io_diagnostics':r'pbDownload|pbPost|HTTPLite|pbRgss|pbGetFile|pbCriticalCode|pbPrintException|PBDebug|Deprecation|rescue|File\.|Dir\.',
 'time_random_steps_stats':r'pbGetTimeNow|Time\.now|System\.uptime|\brand\b|\bsrand\b|Random\.|AntiRandom|pbTimeEvent|\$stats|stepcount|play_time'
}
entries=[]
for p in sorted((r/'Data/Scripts').rglob('*.rb')):
 rel=str(p.relative_to(r/'Data/Scripts'));text=p.read_text()
 tags=[k for k,v in patterns.items() if re.search(v,text)]
 entries.append({'path':str(p.relative_to(r)),'status':'read_semantically' if rel in read else ('inventoried_only' if tags else 'not_reviewed'),'read_extent':read.get(rel),'candidate_groups':tags,'limitation':'仅所列行用于本轮语义审查；全文件名/模式命中不证明全行为覆盖。'})
other=[]
for base in ('PBS','Text_english_core'):
 for p in sorted((r/base).rglob('*')):
  if p.is_file() and p.name!='.DS_Store':other.append({'path':str(p.relative_to(r)),'status':'inventoried_only','reason':'名称盘点；不把PBS世代备份或翻译存在当作已启用/已验证；本轮未全文语义审查。'})
formal=[]
for p in sorted(f.rglob('*.md')):
 t=p.read_text(); own=bool(re.search(r'generic-kernel/wp(05|06|07|09|10)',str(p))) or p.name=='generic-kernel-wp05-06-07-08-09-10.md'
 match=re.findall(r'WP(?:05|06|07|09|10)|wp(?:05|06|07|09|10)',t)
 formal.append({'path':str(p),'role':'primary' if own else ('projection_or_reference' if match else 'searched_for_counterevidence'),'read_extent':'见spec-coverage.json，非全文件获支持' if own else '仅命中/下游相关上下文；见spec-coverage.json和negative-search.json','domain_mentions':sorted(set(match))})
obj={'source_baseline':{'commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','root':str(r)},'method':'全312脚本名称及四组内容模式检索，列明具体阅读范围；全PBS/翻译名称清单；未重做共享整仓字节身份核验。','discovery_patterns':patterns,'scripts':entries,'data_and_translation_inventory':other,'formal_inventory':formal,'unavailable_material':['完整Demo地图/数据库','Graphics/Audio目录','真实插件目录/预编译样本','旧存档样本','可用游戏宿主'],'readable_not_reviewed':['StringInput/FileMixins二进制边界反向合同','全错误/时间/随机调用点的业务消费者语义','74统计字段全部写入链','14迁移涉及对象的所有内部字段与未知旧档组合','月份后月相/星座算法','元数据/PBS备份全部数据项','翻译18文件正文','插件运行中订阅增删/重入/任意元数据畸形组合','归档真实读取及网络/文件故障注入'],'counts':{'scripts':len(entries),'read_semantically':sum(x['status']=='read_semantically' for x in entries),'inventoried_only':sum(x['status']=='inventoried_only' for x in entries),'not_reviewed':sum(x['status']=='not_reviewed' for x in entries),'pbs_and_translation':len(other),'formal_files':len(formal)}}
(out/'source-scope.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
s=(r/'Data/Scripts/004_Game classes/012_Game_Stats.rb').read_text().splitlines()[:62]
a=set()
for l in s:
 if re.search(r'attr_(accessor|writer)',l):a.update(re.findall(r':([a-z_]+)',l.split('#')[0]))
b=set(re.findall(r'^\| ([a-z_]+) \|', (f/'generic-kernel/wp06-stats-directory.md').read_text(),re.M))
check={'evidence_level':'TOOL_VALIDATION','time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool':'Python 3.14.0','command':'python3 '+str(out/'evidence/inventory.py'),'purpose':'核对统计声明与附表成员，不是行为测试','source_count':len(a),'spec_count':len(b),'missing_in_spec':sorted(a-b),'extra_in_spec':sorted(b-a),'side_effects':'本模块inventory/check JSON only'}
(out/'evidence/stats-declaration-check.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
print(obj['counts']);print(check)
