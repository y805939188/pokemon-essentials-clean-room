import json,re,hashlib,datetime,subprocess
from pathlib import Path
C=Path(__file__).parent;R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception';commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def read(p):return json.loads(p.read_text())
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
identities={};units=[];raws=[]
def source(k,path,credit='OWN_PRIOR_FULL_ACTUAL_READ_REUSED'):
 raw=(R/path).read_bytes();assert raw==subprocess.check_output(['git','-C',str(R),'show',commit+':'+path]);identities[k]=dict(path=path,commit=commit,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),git_blob=subprocess.check_output(['git','-C',str(R),'rev-parse',commit+':'+path],text=True).strip(),lines=len(raw.splitlines()),actual_reader=reader,credit=credit);return raw.decode('utf-8-sig').splitlines(keepends=True)
def method(k,ls,n):
 i=next(i for i,l in enumerate(ls) if re.match(r'\s*def\s+'+re.escape(n)+r'(?=[\s(;]|$)',l));indent=re.match(r'\s*',ls[i]).group();j=i if re.search(r';\s*end\s*$',ls[i]) else next(j for j in range(i+1,len(ls)) if re.match(r'^'+re.escape(indent)+r'end\s*(?:#.*)?$',ls[j]));u=dict(id=k+':'+n,source_identity_key=k,range=[i+1,j+1],text=''.join(ls[i:j+1]),complete_definition=True);units.append(u);return u['id']
ls=source('daycare','Data/Scripts/012_Overworld/007_Overworld_DayCare.rb');units.append(dict(id='daycare:WHOLE',source_identity_key='daycare',range=[1,len(ls)],text=''.join(ls),complete_definition=True))
ls=source('pokemon','Data/Scripts/014_Pokemon/001_Pokemon.rb')
for n in ['initialize','species_data','form','form=','gender','male?','female?','genderless?','ability_index','ability_index=','hasHiddenAbility?','nature','nature=','shiny?','givePokerus','calc_stats','egg?','learn_move','getMoveList','hasMove?','hasItem?']:method('pokemon',ls,n)
ls=source('species','Data/Scripts/010_Data/002_PBS data/008_Species.rb')
for n in ['self.get_species_form','has_flag?','get_evolutions','get_family_evolutions','get_previous_species','get_baby_species','get_family_species','breeding_can_produce?']:method('species',ls,n)
ls=source('dex','Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb')
for n in ['register','refresh_accessible_dexes']:method('dex',ls,n)
ls=source('time','Data/Scripts/012_Overworld/003_Overworld_Time.rb')
for n in ['pbGetTimeNow','pbGetSeason']:method('time',ls,n)
ls=source('forms','Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb')
for n,lo,hi in [('REG-DEERLING',322,327),('REG-RATTATA',744,753)]:units.append(dict(id='forms:'+n,source_identity_key='forms',range=[lo,hi],text=''.join(ls[lo-1:hi]),complete_registration=True))
units.append(dict(id='forms:REGIONAL-COPY',source_identity_key='forms',range=[755,758],text=''.join(ls[754:758]),complete_copy_statement=True))
ls=source('settings','Data/Scripts/001_Settings.rb')
for n in ['MECHANICS_GENERATION','EGG_LEVEL','SHINY_POKEMON_CHANCE','POKERUS_CHANCE','BREEDING_CAN_INHERIT_MACHINE_MOVES','BREEDING_CAN_INHERIT_EGG_MOVES_FROM_MOTHER']:
 i=next(i for i,l in enumerate(ls) if re.match(r'\s*'+n+r'\s*=',l));units.append(dict(id='settings:'+n,source_identity_key='settings',range=[i+1,i+1],text=ls[i],complete_statement=True))
for k,path,names in [('base','PBS/pokemon.txt',['PIKACHU','RAICHU','PICHU','MARILL','AZUMARILL','AZURILL','NIDORANfE','MANAPHY','PHIONE','SHELLOS','DEERLING','DITTO','ZIGZAGOON']),('formraw','PBS/pokemon_forms.txt',['ZIGZAGOON,1','DEERLING,1','DEERLING,2','DEERLING,3','SHELLOS,1'])]:
 ls=source(k,path,'OWN_COMPLETE_NAMED_RAW_RECORDS_ONLY')
 for name in names:
  i=next(i for i,l in enumerate(ls) if l.strip()=='['+name+']');j=next((j for j in range(i+1,len(ls)) if ls[j].lstrip().startswith('[')),len(ls));raws.append(dict(id=k+':'+name,source_identity_key=k,range=[i+1,j],text=''.join(ls[i:j]),complete_raw_record=True))
claims={};refs={};rrefs={}
def Cc(v,*ss,extra=(),rr=()):claims[v]=list(ss);refs[v]=['daycare:WHOLE']+list(extra);rrefs[v]=list(rr)
for v,ss in {
'BR01':['初槽男/女满足male门，仅交换一次；后母女/父男。','后续所有parent_data与species_parent使用交换后对象，不继续按原槽命名。'],
'BR02':['Ditto为genderless，初Ditto/男或Ditto/女均触发单次交换。','交换后母可为男性；species_parent按Ditto组选择非Ditto方，非按“母一定女”的假设。'],
'BR03':['四种槽序的单次交换和father_ditto派生move_father/move_mother各自完整保留。','非Ditto男作为move_father且!female，原EggMoves已知FAKEOUT进入候选。','非Ditto女在这四fixture落female move_father而被父侧门拒；move_mother为非female Ditto，也不进入母侧。','PICHU原始EggMoves含FAKEOUT；候选后仍经逆去重/末四与learn_move。'],
'BR04':['get_baby_species(true,item1,item2)逐前身检查宝宝incense。','PICHU没有incense，PIKACHU/RAICHU不论SEAINCENSE都回PICHU。','AZURILL有SEAINCENSE，MARILL/AZUMARILL无该物留MARILL，有该物回AZURILL。'],
'BR05':['NIDORANfE的Offspring两项.sample，各半；结果不是由子代PID性别随机替换物种。','MANAPHY的Offspring唯一PHIONE，总选PHIONE；不假装周期兼容先行门不存在。'],
'BR06':['区域值2只有确有对应ZIGZAGOON form2的条件下handler才回2。','无对应记录时get_species_form回退base，form不等2而回0。','当前具名raw仅ZIGZAGOON1，原向量“存在2”保为条件fixture，不伪称默认存在2。'],
'BR07':['SHELLOS基础带InheritFormFromMother。','读species_parent.form后显式egg.form=，允许非零与同值；即使相同也有提交副作用。'],
'BR08':['mother_data先于father_data遍历，逐个要求族内/物种旗标/持EVERSTONE。','首个合格parent.form读取后egg提交并break；父优先仅当母不合格。','旗标比较忽略大小写，不能把原Everstone大小写变体当缺标。'],
'BR09':['仅母持EVERSTONE时候选nature数组仅母nature对象。','单元素sample仍写egg.nature，计算覆盖与表现缓存保持分层。'],
'BR10':['新蛋constructor calc_stats已按初PID缓存nature。','set_shininess只清shiny和改PID，不清nature，所以模25由0变1仍保HARDY。','有EVERSTONE时inherit_nature更早显式覆盖该表现性格，薄荷覆盖不由此创建。'],
'BR11':['inherit_ability选择女/非Ditto能力亲本，不追加未写的族内门。','其隐藏索引>=2时rand100<60才写索引，否则保蛋原索引/缓存。','下游ability_id按物种实际能力表回退，继承索引不保证同特性身份。'],
'BR12':['普通能力分支另抽rand100，小于80继承该index。','否则(index+1)%2，能力缺口按实际getter回退，不创造缺失登记。'],
'BR13':['后代level表仅等级严格大于egg.level的共有已知招进入此通道。','L5且蛋L1通过，只有一方掌握不通过；Ditto也参加两方hasMove检验。'],
'BR14':['候选逆序后集合去重再逆序，保每ID最后出现位置。','只遍历最后MAX_MOVES4项去learn_move；它与constructor既有招式的移动/槽满行为仍按learn_move。'],
'BR15':['后代PICHU且VOLTTACKLE登记，任一族内亲本持LIGHTBALL就末尾追加。','父符合即可，不要求它是常规母侧；仍经过后续去重/截断。'],
'BR16':['inherit_count初3，无Knot/Power时六main项sample3不重复。','每项各从随机亲本取原iv，未选项保创建随机IV。'],
'BR17':['世代>=6且任一方hasItem DESTINYKNOT才总数改5。','Power固定项会从此总数扣除，不是额外五项加固定项。'],
'BR18':['普通每个体单持物，两件不同Power占满两槽，不能同时有Knot。','总数仍3，两不同stat各固定并移除，各扣1。','仅从余4项sample1；没有5-2分支。'],
'BR19':['两POWERWEIGHT合并同HP key的两个候选值。','sample亲本值只写一次HP、只扣一次，再从余5项sample2，总3。'],
'BR20':['只有族内亲本的poke_ball进入候选。','随后删除MASTERBALL/CHERISHBALL所有相等项，空则保constructor默认POKEBALL。'],
'BR21':['族内双亲普通/超级球各一个候选。','数组sample两项等概率赋给egg.poke_ball；不是按拥有者或母方固定优先。'],
'BR22':['双方Owner.language不等且世代8加6，SHINYCHARM再加2，总8。','每轮先egg.shiny?，命中break，不清该true或改PID。','未命中才清普通缓存nil并抽两个16bit组成新PID；没有循环尾补查询。'],
'BR23':['N2：轮首PID25/owner0算false，清nil再换26；次轮26false，清nil再换16。','退出后16未读，普通缓存nil。','Owner.id改16后首读d0为true；若此前错误补尾读会留下false且Owner变更不失效。'],
'BR24':['初PID0/Owner0在首轮shiny?命中true，立即break无重掷。','N0在循环前return，不读取也不清已有普通缓存；较早登记填缓存仍会保留。'],
'BR25':['rand65536<POKERUS_CHANCE3为命中，阈值3不包含随机3。','给新未感染蛋调用givePokerus，先stats+1，再取strain1...16。','感染time=1+strain%4并打包pokerus位字段；后失败不自动减统计。'],
'BR26':['默认PICHU原EggGroups Undiscovered，使compatibility在Ditto关系等级前返回0。','周期egg_chance数组compat0为0，OVALCHARM也仍0。','直接generate_egg只要求占2槽；collect先生成再容量检查，不重查兼容或egg_generated。','有容量且后续正常才push并reset，不能把周期守卫追加给工具。'],
'BR27':['SHELLOS母系form0显式提交，即使子代已有0也清ability值/calc/条件Dex。','Pokedex.register读species_data/gender/shiny，填性别/普通异色缓存，再写seen与对应form位。','末次原空才首写，owned/seen_egg不由该方法写；蛋步5120不清，返回生成尚未入队。'],
'BR28':['缺全局player或pokedex时form已提交/calc已到，但安全导航跳register。','因此本链没有填gender/shiny或Dex写入。','已有非空last_seen时仍写seen/forms和读两缓存，保旧last三元组。'],
'BR29':['N0 shiny通道直接return，保此前母系提交登记填的结果。','没有此前读取的合法对照仍缓存nil；首次将来读取才计算。','N>=1轮首/末次nil与旧nature缓存规则保留，不补循环尾读。'],
'BR30':['form先写/ability清后calc失败，register未到。','refresh_accessible_dexes失败位于seen/forms/首last与两缓存之后，不回滚。','collect先完成generate，party_full随后raise，未入队且egg标记/计数未reset，先前登记保。','该生成链没有交互cancel，不把条件故障说默认必失败。'],
'BR31':['母系同值0先显式提交。','Everstone循环再查母合格时显式同值0提交并break，不读父1。','取消母资格才父1提交；非零SHELLOS母系照旧。','所有实际提交保WP21顺序，选择门与随机通道无改写。']
}.items():Cc(v,*ss)
for v,ss in {
'R7-U05-PF01':['作者只加InheritFormFromMother给DEERLING，默认原记录无该标。','月份2 pbGetSeason1，母form getter先提交0→1/清ability/重算/条件Dex，返回后才egg显式提交1。','不保证HP等数值必变或最终ability仍空；没有直接改亲本Owner/IV/EV/EXP步骤。'],
'R7-U05-PF02':['月份1得到季节0等母stored，getter不调用form=。','egg显式赋0仍同值提交，不能添加parent getter相等门。'],
'R7-U05-PF03':['母forced0非nil优先返回0，不动态提交stored。','egg仍显式提交0，forced字段不是母stored写回。'],
'R7-U05-PF04':['母战斗或仓库守卫各独立提前返回stored0。','egg赋0仍提交；只是给定守卫条件，不证明对应UI能启动生成。'],
'R7-U05-PF05':['移除作者母系flag恢复默认DEERLING后inherit_form不读该parent.form。','无合格Everstone时本链不触发母季节提交，不推广所有其它入口。'],
'R7-U05-PF06':['默认SHELLOS没有季节handler。','子代同值提交、N0缓存与母系→首永石顺序沿BR27–31；不重计为新增parent提交。'],
'R7-U05-PF07':['先完整生成后collect发现party_full。','已有母1/calc/Dex保留，未push且egg_generated/step未reset。','无交互cancel撤销亲本。'],
'R7-U05-PF08':['母calc失败：stored1与ability nil已到，Dex与egg赋值未到。','母Dex refresh失败：已到seen/form/cache/last前缀保，egg赋值未到。','母完成而egg后段失败：全部母前缀保，egg按自身已到阶段记录，不自动回滚。'],
'R7-U05-PF09':['缺player或Dex时母仍提交1/calc但跳登记。','随后egg仍显式1并受相同安全导航门，不在此调用需要player的collect。'],
'R4-IV01':['世代8两不同Power无Knot，固定HP31/Atk31。','剩四stat只选一继承0，三项保持初1，总继承3。'],
'R4-IV02':['Knot+另一方PowerWeight合法两件持物，总数5。','HP固定31后剩5选4为0，最后一项保初1。'],
'R4-IV03':['只改世代5忽略Knot数目提升，总3。','HP固定后只选余2为0，三项保初1。'],
'R4-IV04':['两PowerWeight同stat候选HP31/30各一，等概率单次写。','只扣1，总3，余五选2为0，三保初1。']
}.items():Cc(v,*ss)
assert len(claims)==44
for v in claims:
 refs[v]+= ['pokemon:initialize','pokemon:form','pokemon:form=','species:has_flag?']
 if v.startswith('BR') and int(v[2:]) in [1,2,3,26]:refs[v]+=['pokemon:gender','pokemon:male?','pokemon:female?','pokemon:genderless?']
 if v in ['BR04','BR05','BR07','BR08','BR15']:refs[v]+=['species:get_baby_species','species:get_family_species','species:get_family_evolutions','species:get_evolutions','species:breeding_can_produce?']
 if v in ['BR10','BR22','BR23','BR24']:refs[v]+=['pokemon:nature','pokemon:nature=','pokemon:shiny?','settings:MECHANICS_GENERATION','settings:SHINY_POKEMON_CHANCE']
 if v in ['BR11','BR12']:refs[v]+=['pokemon:ability_index','pokemon:ability_index=','pokemon:hasHiddenAbility?']
 if v in ['BR13','BR14','BR15']:refs[v]+=['pokemon:learn_move','pokemon:getMoveList','pokemon:hasMove?']
 if v=='BR25':refs[v]+=['pokemon:givePokerus','settings:POKERUS_CHANCE']
 if v in ['BR27','BR28','BR29','BR30','BR31'] or v.startswith('R7-'):refs[v]+=['dex:register','dex:refresh_accessible_dexes','pokemon:calc_stats','pokemon:gender','pokemon:shiny?']
 if v.startswith('R7-'):refs[v]+=['forms:REG-DEERLING','time:pbGetTimeNow','time:pbGetSeason']
 if v=='BR06':refs[v]+=['forms:REG-RATTATA','forms:REGIONAL-COPY','species:self.get_species_form']
 if v.startswith('R4-IV') or v in ['BR16','BR17','BR18','BR19']:refs[v]+=['settings:MECHANICS_GENERATION','pokemon:hasItem?']
 refs[v]=list(dict.fromkeys(refs[v]))
 if v in ['BR03','BR04','BR15','BR26']:rrefs[v]+=['base:PICHU','base:PIKACHU','base:RAICHU','base:DITTO']
 if v=='BR04':rrefs[v]+=['base:AZURILL','base:MARILL','base:AZUMARILL']
 if v=='BR05':rrefs[v]+=['base:NIDORANfE','base:MANAPHY','base:PHIONE']
 if v in ['BR07','BR27','BR28','BR29','BR30','BR31'] or v.startswith('R7-'):rrefs[v]+=['base:SHELLOS','base:DEERLING','formraw:SHELLOS,1','formraw:DEERLING,1','formraw:DEERLING,2','formraw:DEERLING,3']
 if v=='BR06':rrefs[v]+=['base:ZIGZAGOON','formraw:ZIGZAGOON,1']
uids={x['id'] for x in units};assert all(u in uids for vv in refs.values() for u in vv)
formal='deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md';fr=(B/formal).read_bytes();rows={}
for i,l in enumerate(fr.decode().splitlines(),1):
 m=re.match(r'\| ((?:BR\d+|R7-U05-PF\d+|R4-IV\d+)) \|',l)
 if m:rows[m[1]]=(i,l)
assert set(rows)==set(claims);records=[]
for v,ss in claims.items():
 line,row=rows[v];records.append(dict(id='BRV-'+v,vector=v,formal=dict(path=formal,line=line,complete_raw_row=row),premise='完整原行及各BR27/PF/IV共同前提全保；每行独立复位，默认/作者附旗标/条件缺源/随机给值/不同配置分别说明。合法loaded记录不声称已编译；依赖、消息和资源正常至对应观察点。',complete_source_unit_ids=refs[v],complete_raw_record_ids=list(dict.fromkeys(rrefs[v])),child_assertions=[dict(id=f'BRV-{v}-A{i:02}',meaning=s,complete_source_unit_ids=refs[v],status='MANUALLY_JOINED_BOUNDED_STATIC',whole_parent_acceptance=False) for i,s in enumerate(ss,1)],normal_failure_cancel='generate按顺序构造→form→nature→ability→moves→IV→ball→shiny→Pokerus→calc；各阶段异常保已到母/蛋/Dex前缀。collect生成后容量拒绝不撤销先前登记，正常push后才reset。此生成无交互cancel；接口和随机过程不伪装已运行。',consumer_persistence='DayCare原parent引用与新egg构造；Species原字段与前身/族内资格→具名继承→Pokemon持久容器/缓存→Pokedex.register→生成返回/party领取。A已接Save17顶层对象图有限合同保持，未执行native跨root别名/实际dump-load。',remaining=['全部此组有限意义已拆，未授wholeDayCare/所有PBS字段/所有配置组合/全域PASS；原source reader保留。'],accepted=False))
for u in units:
 ls=(R/identities[u['source_identity_key']]['path']).read_text(encoding='utf-8-sig').splitlines(keepends=True);lo,hi=u['range'];assert ''.join(ls[lo-1:hi]).rstrip('\n')==u['text'].rstrip('\n')
out=dict(schema='gr8-crec-breeding44/v1',recorded_utc=utc,actual_reader=reader,formal_identity=dict(path=formal,bytes=len(fr),sha256=hashlib.sha256(fr).hexdigest(),actual_current_read_chunk='dee2a5'),source_identities=identities,complete_source_units=units,complete_raw_records=raws,records=records,manual_atoms=sum(len(x['child_assertions']) for x in records),common_premise_text='BR27–31 SHELLOS与PF DEERLING作者flag及R4IV单持物共同前提保原formal完整段落；各记录无继承假定缺省资格，BR06仅有form2条件化fixture，不称默认form2存在。',actual_current_read_chunks=['1ceb19','3f58ee','22e341','cd988c','4306c3','fd0a97','09f43c','460dc9','2dc2ec','900178','b204a8'],whole_PBS_credit=False,new_contexts=0,new_votes=0,denominator_frozen=False,whole_domain_acceptance=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
p=C/'breeding-catalog44-meaning.v1.json';assert not p.exists();write(p,out);rv=read(C/'reverse-mapping.json');assert not any(x['id'].startswith('BRV-') for x in rv['records']);rv['records'].extend(records);rv['utc']=utc;write(C/'reverse-mapping.json',rv);pr=read(C/'progress.json');pr['updated_utc']=utc;pr['primary_clause_atoms']=sum(len(x.get('child_assertions',[])) for x in rv['records']);write(C/'progress.json',pr);print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),groups=44,children=out['manual_atoms'],total_groups=len(rv['records']),total_children=pr['primary_clause_atoms'],source_units=len(units),raw_records=len(raws),utc=utc)))
