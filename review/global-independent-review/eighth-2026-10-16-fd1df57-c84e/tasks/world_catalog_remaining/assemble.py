from pathlib import Path
import json,hashlib,subprocess,datetime,collections
B=Path('/workspace/pokemon-essentials-clean-room'); R=Path('/workspace/pokemon-essentials'); REPORT=B/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'; P=REPORT/'tasks/world_catalog_remaining'; W=REPORT/'tasks/world_full'; D=W/'delegation'
now=datetime.datetime.now(datetime.timezone.utc).isoformat(); task='/root/world_catalog_remaining'
readset=json.loads((D/'world_catalog_remaining.readset.json').read_text()); frozen=json.loads((D/'world_catalog_remaining.source-facts.frozen.json').read_text()); parent=json.loads((W/'forward-mapping.json').read_text()); extra=[u for u in parent['units'] if u['unit_id'] in ['WFS-093','WFS-094','WFS-095']]
assert len(frozen['units'])==92 and sum(len(u['assertions']) for u in frozen['units'])==386
assert len(extra)==3 and sum(len(u['assertions']) for u in extra)==19
units={u['unit_id']:u for u in frozen['units']+extra}
cat=B/readset['catalog_assigned']['identity']['path']; lines=cat.read_text().splitlines(); primary=readset['catalog_assigned']['ranges']; assigned={n for a,z in primary for n in range(a,z+1)}
manual={}
for l in (P/'manual-atoms.txt').read_text().splitlines():
 k,src,atoms=l.split('|',2); assert k not in manual;manual[k]={'sources':['WFS-'+f'{int(v):03}' for v in src.split(',')],'atoms':atoms.split('~')}
assert len(manual)==322 and sum(len(m['atoms']) for m in manual.values())==1551
receptions={n:json.loads((W/'receptions'/n).read_text()) for n in ['topology-forward.json','pbs-interface-facts.json','weather-shared-facts.v1.received.json','pbs-field-semantics.json','creature-b-dependency-semantic-facts.json']}
ker=json.loads((REPORT/'tasks/kernel_review/file-unit-fact-consumer-spec-matrix.json').read_text()); kernel=[r for r in ker['rows'] if r['fact_id'] in ['KER-F042','KER-F043','KER-F044','KER-F045','KER-F046','KER-F096']]
# Explicit personal reading, independent of received-source-reader credit.
full_paths=[
'Data/Scripts/003_Game processing/001_StartGame.rb',
'Data/Scripts/012_Overworld/002_Overworld_Metadata.rb',
'Data/Scripts/012_Overworld/003_Overworld_Time.rb',
'Data/Scripts/012_Overworld/005_Overworld_Fishing.rb',
'Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb',
'Data/Scripts/010_Data/002_PBS data/019_DungeonTileset.rb',
'Data/Scripts/010_Data/002_PBS data/020_DungeonParameters.rb',
'Data/Scripts/006_Map renderer/004_TileDrawingHelper.rb',
'Data/Scripts/004_Game classes/010_Game_Follower.rb',
'Data/Scripts/005_Sprites/005_Sprite_SurfBase.rb',
'Data/Scripts/012_Overworld/001_Overworld visuals/002_Overworld_Overlays.rb',
'Data/Scripts/002_Save data/001_SaveData.rb',
'Data/Scripts/002_Save data/002_SaveData_Value.rb',
'Data/Scripts/002_Save data/004_Game_SaveValues.rb',
'Data/Scripts/001_Technical/001_Debugging/003_Errors.rb']
partial_paths={
'Data/Scripts/004_Game classes/007_Game_Event.rb':[[1,127]],
'Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb':[[518,561]],
'Data/Scripts/012_Overworld/001_Overworld visuals/003_Overworld_MapTransitionAnims.rb':[[1,76]],
'Data/Scripts/003_Game processing/005_Event_Handlers.rb':[[66,90]],
'Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb':[[42,64]],
'Data/Scripts/013_Items/002_Item_Effects.rb':[[123,167],[276,316]],
'Data/Scripts/012_Overworld/007_Overworld_DayCare.rb':[[386,405],[560,564]],
'Data/Scripts/003_Game processing/003_Interpreter.rb':[[303,426]],
'Data/Scripts/019_Utilities/001_Utilities.rb':[[520,539]],
'Data/Scripts/015_Trainers and player/001_Trainer.rb':[[57,100]],
'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb':[[209,304]],
'Data/Scripts/021_Compiler/001_Compiler.rb':[[72,153],[255,294],[296,485],[690,737],[1020,1117]],
'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb':[[1,140],[1196,1233]]}
# These are manually specified semantic units, not source method enumeration or atom generation.
local=[
('LOCAL-FOLLOWER','Data/Scripts/004_Game classes/010_Game_Follower.rb',[[1,215]],'有效目标后自身through；目标按进入方向位、桥/岩架、优先级及具名非through事件碰撞；不要求全向严格。fancy_move可按当前位置拒绝走through；这里只接MV17。',['MV17']),
('LOCAL-BP-DISPATCH','Data/Scripts/003_Game processing/005_Event_Handlers.rb',[[66,90]],'命名回调按现存插入序调用；没有统一异常捕获/回滚。首异常中断后继；已清角色运动、已写玩家global前缀不补回。',['R7-BP01','R7-BP06','R7-BP07']),
('LOCAL-BP-REPEL','Data/Scripts/013_Items/002_Item_Effects.rb',[[123,167]],'玩家步回调仅repel>0且非冰才减1；减后仍>0直接返回；从2到1不触发续用UI。',['R7-BP01','R7-BP02','R7-BP06','R7-BP07']),
('LOCAL-BP-DAYCARE','Data/Scripts/012_Overworld/007_Overworld_DayCare.rb',[[386,405],[560,564]],'每个玩家步通知调寄养update，先加自身周期，达到256才归0/候选蛋与分享门；空合法寄养周期0正常变1，不等于没有变化。',['R7-BP01','R7-BP02']),
('LOCAL-RODS','Data/Scripts/013_Items/002_Item_Effects.rb',[[276,316]],'三竿分别先计算当前出边；面向可钓且surf标记或当前出边许可，才取本地图对应竿表并等待；true先增battles再主动遭遇，正常条目总true。',['FS01','FS02','FS03','FS04','FS11','FS15','FS17','R5-FS06']),
('LOCAL-PARTY-FIRST','Data/Scripts/015_Trainers and player/001_Trainer.rb',[[57,100]],'pokemon_party筛nil及蛋，允许濒死；first_pokemon取筛后首项，able_party另筛濒死。',['FS12','R6-FS02']),
('LOCAL-COMMON-GLOBAL','Data/Scripts/019_Utilities/001_Utilities.rb',[[520,539]],'全局助手负ID或缺记录false；有记录建event0解释器，正常循环完成显式true。',['FS14','FS16','R5-FS01','R5-FS02','R5-FS03']),
('LOCAL-COMMON-INTERPRETER','Data/Scripts/003_Game processing/003_Interpreter.rb',[[303,321]],'解释器助手不拒负ID，按数组读取；缺记录nil，有记录非战斗子循环完成仍nil，战斗交battle解释器。',['R5-FS01','R5-FS02','R5-FS03','R5-FS04','R5-FS05']),
('LOCAL-SURF-DISPLAY','Data/Scripts/005_Sprites/005_Sprite_SurfBase.rb',[[1,94]],'两水标记都假撤基底；任一真且基点非空读基点，否则读父坐标；显示不主动清基点或ending。',['GR4-SF01','GR4-SF02','GR4-SF03','GR4-SF04','GR4-SF05','GR4-SF06','GR4-SF07']),
('LOCAL-LOCATION','Data/Scripts/012_Overworld/001_Overworld visuals/002_Overworld_Overlays.rb',[[1,47]],'已dispose或fly目的存在先退；曾延迟则清门后重设时刻，窗口update后消息/图身份变销毁；否则.4入1.6留.4出。',['MP26','MP27','WT36','WT39','WT40']),
('LOCAL-HEADBUTT','Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb',[[518,561]],'a=(x+floor(x/24)+1)(y+floor(y/24)+1)，乘2整除5再模10；b=公开ID模10，相等8，方向/绝差门5，其余1；rand10门，1档Low其余High；缺事件无安全坐标门。',['WT23','WT24']),
('LOCAL-CAVE','Data/Scripts/012_Overworld/001_Overworld visuals/003_Overworld_MapTransitionAnims.rb',[[1,76]],'进入先set逃点，退出先erase；15层几何半屏减12/10除15，首.4秒按层延迟插值，随后黑/白tone0及.4覆盖，恢复tone8后等.1；轮只Graphics/Input，正常释放。',['WT34','WT35']),
('LOCAL-COOLDOWN','Data/Scripts/004_Game classes/007_Game_Event.rb',[[1,127]],'秒式读原私有record并严格当前整数>record+secs；日式先to_i，按86400商余及本地日内严格>修正；临时A门独立，失败need_refresh，不清record。',['R5-TIME01','R5-TIME02','R5-TIME03','R5-TIME04']),
('LOCAL-PUSH','Data/Scripts/003_Game processing/003_Interpreter.rb',[[386,418]],'严格通行先门；通过后推数加1、普通移动、条件快照；仅位变声/锁/等moving/解锁。力量包装只在strengthUsed真调用，正常总true；无ensure。',['R5-PUSH01','R5-PUSH02','R5-PUSH03','R5-PUSH04']),
('LOCAL-PBS-PARSER','Data/Scripts/021_Compiler/001_Compiler.rb',[[72,153],[255,294],[383,485],[690,737]],'prepline仅注释空白处理；字段ASCII等号；有schema重复属性保列表。CSV按格式求值，大写可选空为nil；v拒0，m转符号；mV节省略/空次位进入版本0而显式0拒绝。',['WT38','J01-V01／V02','J01-V03','J01-V04','J01-V05','J01-V06']),
('LOCAL-DUNGEON-COMPILE','Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',[[1,68],[1196,1233]],'generic先清DATA，逐节解析、专用校验、通用重复门、register，终检后save。Dungeon专用将area和version拆出并拼id，重复在专用门拒绝；首条可保内存而本表save未到；Tileset无专用修正。',['U01-M01-021-01','U01-M01-022-01','U01-M01-022-02','U01-M01-022-03','J01-V01／V02','J01-V03','J01-V04','J01-V05','J01-V06','J01-V11','J01-V13']),
('LOCAL-CONNECTION-COMPILE','Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',[[104,140]],'六字段解析，首端方向才要求第二端互反；整数首端不做该配对。缺图仅警告分支，不统一拒绝；正常尾save连接档案。',['U01-M01-027-01','U01-M01-027-02','U01-M01-027-03']),
('LOCAL-STARTUP-DIAGNOSTIC','Data/Scripts/021_Compiler/001_Compiler.rb',[[1020,1117]],'直接compile_all无启动预删/异常处理；main仅DEBUG并按发现决定重编，预删每文件SystemCallError救援；普通异常先诊断，诊断正常返后再逐文件尝试删；Reset/SystemExit先原抛。',['J01-V13']),
('LOCAL-BATTLE-TIME','Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',[[209,304]],'环境覆写独立；时段先查地图metadata Cave强2，否则配置TIME_SHADING真才按夜暮其他2/1/0；无outdoor门；新战斗默认0前提来自具名父WFS071消费者边界，不扩成已有重置。',['WT41','WT42','WT43','WT44'])]
# Mechanical identity binding only. Every semantic acceptance is named above/manual-atoms.txt.
def ident(repo,path,commit):
 p=repo/path; data=p.read_bytes(); blob=subprocess.check_output(['git','-C',str(repo),'hash-object',str(p)],text=True).strip(); fixed=subprocess.check_output(['git','-C',str(repo),'rev-parse',f'{commit}:{path}'],text=True).strip()
 return {'repo':str(repo),'commit':commit,'tree':readset['R_tree'] if repo==R else readset['B8_tree'],'path':path,'git_mode':'100644','actual_mode':oct(p.stat().st_mode&0o777),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'blob':blob,'fixed_blob':fixed,'matches_fixed_blob':blob==fixed,'lines':len(data.splitlines())}
Rpaths=set(u['path'] for u in units.values())|set(full_paths)|set(partial_paths)
for f in receptions['topology-forward.json']['facts']:
 Rpaths.update(s['path'] for s in f['sources'])
for f in receptions['weather-shared-facts.v1.received.json']['facts']:Rpaths.add(f['source']['path'])
for f in kernel:Rpaths.update(s['path'] for s in f['sources'])
rids={p:ident(R,p,readset['frozen_R']) for p in sorted(Rpaths)}
formal_paths=[readset['catalog_assigned']['identity']['path']]+[x['path'] for x in readset['dependency_formal']]
bids={p:ident(B,p,readset['frozen_B8']) for p in formal_paths}
contracts={}
for p in [B/'AGENTS.md',REPORT/'inputs/review-SKILL.md',REPORT/'inputs/eighth-global-review-prompt.md',D/'world_catalog_remaining.prompt.md',D/'world_catalog_remaining.readset.json',D/'world_catalog_remaining.source-facts.frozen.json']:
 d=p.read_bytes();contracts[str(p)]={'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'actual_read':'COMPLETE_PERSONAL_READ'}
assert all(i['matches_fixed_blob'] for i in list(rids.values())+list(bids.values()))
all_ids={'schema':'gr8-world-catalog-identities/v1','reader':task,'utc':now,'frozen_input':{k:readset[k] for k in ['frozen_B8','B8_tree','formal_tree','frozen_R','R_tree']},'working_review_HEAD':subprocess.check_output(['git','-C',str(B),'rev-parse','HEAD'],text=True).strip(),'working_review_note':'Review-only descendant is not substituted for B8. All adopted formal/source blobs independently compared to frozen commits.','configuration':{'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','fast':False},'actual':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','platform_id']}},'contracts':contracts,'reference':rids,'formal':bids,'identity_only_no_semantic_credit':True}
(P/'identities.json').write_text(json.dumps(all_ids,ensure_ascii=False,indent=2)+'\n')
contexts={}
def ctx(k,a,z,role):contexts[k]={'range':[a,z],'exact_text':'\n'.join(lines[a-1:z]),'role':role}
for args in [('GLOBAL',1,3,'本目录九正文引用和所有向量静态未执行界限'),('MP',5,8,'地图表头与坐标输入/预期观察列'),('MV',37,40,'移动表头输入/预期'),('BP',119,124,'完整共享夹具、替代前提与独立复位'),('BP-TAIL',134,134,'解释器/自动运动/其他消费者保持和完整追溯'),('DG',266,269,'地牢表头'),('WT',339,342,'时间天气场地表头'),('FS',388,391,'钓鱼表头'),('USE',411,415,'静态环境和冲突处置使用说明'),('DQ',461,466,'临时查询完整共同夹具'),('MR',497,502,'正常读档与条件恢复两套独立夹具'),('SF',536,541,'失败上水转移完整共用夹具及通知时点'),('R5',603,608,'第五轮共同静态前提和异常前缀界限'),('AUTHOR',680,685,'作者输入独立复位和未执行界限'),('R6FS',696,701,'随机阶段完整共用夹具和统计结果'),('J01',727,732,'只索引Generic完整V01–V13、不重复接受/执行'),('J01-TAIL',742,742,'既有DG/DQ/构造播种生成摆放保留与Demo限制')]:ctx(*args)
reverse=[]; seen=set()
def group_for(k):
 if k.startswith('R7-BP'):return ['GLOBAL','MV','BP','BP-TAIL']
 if k.startswith('MP'):return ['GLOBAL','MP']
 if k.startswith('MV'):return ['GLOBAL','MV']
 if k.startswith('DG'):return ['GLOBAL','DG']
 if k.startswith('WT'):return ['GLOBAL','WT']
 if k.startswith('FS'):return ['GLOBAL','FS']
 if k.startswith('GR3-DQ'):return ['GLOBAL','DQ']
 if k.startswith('GR3-MR'):return ['GLOBAL','MR']
 if k.startswith('GR4-SF'):return ['GLOBAL','SF']
 if k.startswith('JXN') or k.startswith('R5-'):return ['GLOBAL','R5']
 if k.startswith('U01'):return ['GLOBAL','AUTHOR']
 if k.startswith('R6-FS'):return ['GLOBAL','R6FS']
 return ['GLOBAL','J01','J01-TAIL']
def topo_for(k):
 if k.startswith('JXN-NAME'):return ['W19','W20','W21','W30']
 if k.startswith('GR3-DQ'):return ['W01','W03','W27','W31']
 if k.startswith('GR3-MR'):return ['W02','W14','W15','W16','W17']
 if k.startswith('GR4-SF'):return ['W10','W26']
 if k.startswith('MP'):return ['W01','W02','W05','W06','W07','W08','W09','W10','W11','W13','W14','W15','W16','W18','W22','W23']
 return []
topodict={f['fact_id']:f for f in receptions['topology-forward.json']['facts']}
for n,line in enumerate(lines,1):
 if n not in assigned or not line.startswith('|'):continue
 fields=[v.strip() for v in line.split('|')[1:-1]]
 if not fields or fields[0] not in manual:continue
 k=fields[0];m=manual[k];seen.add(k);src=[units[v] for v in m['sources']]
 extra_refs=[u[0] for u in local if k in u[4]]
 if k.startswith('DG') or k.startswith('R5-DG') or k.startswith('GR3-DQ') or k.startswith('U01-M01-021') or k.startswith('U01-M01-022') or k.startswith('J01'):
  extra_refs+=['OWN-DUNGEON-FULL','OWN-DUNGEON-DATA-FULL']
 weather=[]
 if k in ['MP22','MP23','WT07','WT08','WT09','WT10','WT11','WT12','WT31','WT32']:weather=[f['id'] for f in receptions['weather-shared-facts.v1.received.json']['facts']]
 qual=[]
 if k=='MP13':qual.append('现有WORLD002同步点：邻图描述不构成当前图豁免，不新增根因。')
 if k in ['MV55','MV56']:qual.append('正常通用短例的遗漏守卫按已全文读WP12及具体源门限制，WORLD003唯一根负责明确moving/jumping与自动flag差异。')
 if k.startswith('J01'):qual.append('本primary为本节索引信息和有限Dungeon/编译接合；Generic原V07–V10/V12的Metrics/Shadow业务完整批准不在本贡献。')
 ckeys=group_for(k)
 atoms=[]
 for i,a in enumerate(m['atoms'],1):
  atoms.append({'id':f'{k}-A{i:02}','assertion':a,'manual_semantic_authorship':task,'source_units':m['sources'],'source_fact_ids':[a['id'] for u in src for a in u['assertions']],'additional_source_facts':extra_refs,'premise_ref':f'{k}.exact_input + context:{",".join(ckeys)}','status':'FINITE_STATIC_SUPPORTED_WITH_STATED_SCOPE','execution':'NOT_EXECUTED'})
 reverse.append({'id':k,'catalog_identity_ref':readset['catalog_assigned']['identity']['path'],'line':n,'exact_original':line,'exact_input':fields[1],'exact_expected':fields[2] if len(fields)>2 else fields[1],'exact_other_columns':fields[3:],'complete_context_refs':ckeys,'manual_assertions':atoms,'manual_assertion_count':len(atoms),'source_units':m['sources'],'topology_fact_refs':topo_for(k),'weather_fact_refs':weather,'source_identity_refs':sorted(set(u['path'] for u in src)|set(topodict[t]['sources'][0]['path'] for t in topo_for(k))),'consumer_facts':[{ 'unit_id':u['unit_id'],'title':u['title'],'facts':u['assertions'],'consumers':u['consumers'],'range':u['range'],'source_identity_ref':u['path']} for u in src],'additional_complete_fact_refs':extra_refs,'qualifications':qual,'evidence':'SOURCE_STATIC / DERIVED_VECTOR','business_execution':'NOT_EXECUTED'})
assert seen==set(manual)
assert sum(r['manual_assertion_count'] for r in reverse)==1551
(P/'reverse-mapping.json').write_text(json.dumps({'schema':'gr8-world-catalog-reverse/v1','reader':task,'utc':now,'catalog_identity':bids[readset['catalog_assigned']['identity']['path']],'ranges':primary,'context_read':[1,742],'primary_lines':416,'vector_count':322,'manual_assertion_count':1551,'atomization':'All semantic strings and boundaries hand-written in manual-atoms.txt after full context read. Assembly only attaches exact original rows, identities, full fact payloads and counts; no punctuation, method, keyword or row-count inference of semantics. Counts cover this finite contribution only.','contexts':contexts,'prose_and_headers_disposition':'Every non-vector primary line is retained verbatim in primary_nonvector_lines; prose contexts are hand-grouped above; blank/separator/header lines carry structure but are not invented behavior atoms.','primary_nonvector_lines':[{'line':i,'exact':l} for i,l in enumerate(lines,1) if i in assigned and not any(r['line']==i for r in reverse)],'records':reverse,'outside_primary_context_lines':326,'unsupported_new_business_execution':0,'unmapped_primary_vectors':0,'whole_world_required_judgment':'NOT_GRANTED'},ensure_ascii=False,indent=2)+'\n')
local_objects=[]
for lid,path,ranges,fact,consumers in local:
 local_objects.append({'id':lid,'reader':task,'source':{'path':path,'ranges':ranges,'identity_ref':path},'fact':fact,'vector_consumers':consumers,'premises':'固定R与B8；仅每个原向量及完整共用夹具给定的合法对象、无额外写入、正常先序或明确首次异常；各替代子例独立复位。','evidence':'SOURCE_STATIC / DERIVED_VECTOR','execution':'NOT_EXECUTED','source_personal_read':'COMPLETE_SPECIFIED_SEMANTIC_UNIT'})
local_objects += [
 {'id':'OWN-DUNGEON-FULL','reader':task,'source':{'path':'Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb','ranges':[[1,1107]],'identity_ref':'Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb'},'fact':'完整生成器的节点谓词、连接、三层布局、256墙表、34/136有序16分支、房间通道几何、装饰次数与图块化、1000次选点与100轮事件/玩家分流均本人全文读；具体人工输入及逐字段/分支结论是reverse322行记录中相关1551子断言的相应子集，不把全文读转成全源原子穷尽。','vector_consumers':[r['id'] for r in reverse if r['id'].startswith(('DG','R5-DG','GR3-DQ'))],'evidence':'SOURCE_STATIC / DERIVED_VECTOR','execution':'NOT_EXECUTED'},
 {'id':'OWN-DUNGEON-DATA-FULL','reader':task,'source':{'paths':['Data/Scripts/010_Data/002_PBS data/019_DungeonTileset.rb','Data/Scripts/010_Data/002_PBS data/020_DungeonParameters.rb','Data/Scripts/006_Map renderer/004_TileDrawingHelper.rb'],'ranges':[[1,222],[1,135],[1,241]]},'fact':'三完整源已独立读，包括缺列表失败、宽容查找差异、全部墙偏移、256邻接与48象限表、奇偶变体、schema/导出、默认值及无writer；逐向量有限数学见reverse，媒体绘制/未涉及minimap等不授主合同全面批准。','evidence':'SOURCE_STATIC / DERIVED_VECTOR','execution':'NOT_EXECUTED'}]
forward_units=[]
for uid,u in units.items():
 adopted=[r['id'] for r in reverse if uid in r['source_units']]
 forward_units.append({'complete_received_unit':u,'source_identity_ref':u['path'],'actual_receiving_reader':task,'reception':'COMPLETE_UNIT_AND_ALL_EXPLICIT_ASSERTIONS_RECEIVED','does_not_transfer_source_FULL_READ':True,'finite_catalog_consumers':adopted,'disposition':'FINITE_PRIMARY_REVERSE_SUPPORT' if adopted else 'CONTEXT_RECEIVED_OUTSIDE_THIS_PRIMARY; parent retains full source-to-formal responsibility'})
forward={'schema':'gr8-world-catalog-forward/v1','reader':task,'utc':now,'frozen_parent':{'units':92,'explicit_assertions':386,'sha256':contracts[str(D/'world_catalog_remaining.source-facts.frozen.json')]['sha256'],'initial_denominator_unchanged':True},'later_parent_supplement':{'units':3,'assertions':19,'ids':['WFS-093','WFS-094','WFS-095'],'actual_read':True,'separate_from_frozen':True},'source_units':forward_units,'topology_complete_reception':receptions['topology-forward.json'],'pbs_gen_complete_reception':receptions['pbs-interface-facts.json'],'weather_complete_reception':receptions['weather-shared-facts.v1.received.json'],'pbs_fields_complete_structure_reception':receptions['pbs-field-semantics.json'],'creature_b_complete_finite_fact_reception':receptions['creature-b-dependency-semantic-facts.json'],'kernel_selected_complete_objects':kernel,'kernel_warning':'Only six explicitly listed objects received; truncated incidental other output NOT adopted. Original consumer open qualifications retained.','local_complete_units':local_objects,'source_identities':rids,'qualification':'All incoming listed objects actually read. Parent full source reading is never reassigned. Local full or bounded source reads are separately inventoried. Extracted explicit assertions are not whole-source/whole-world atom denominator.','business_execution':'NOT_EXECUTED','update_status':'UPDATE_NOT_STARTED'}
(P/'forward-mapping.json').write_text(json.dumps(forward,ensure_ascii=False,indent=2)+'\n')
