import json, re, hashlib, datetime, subprocess
from pathlib import Path
C=Path(__file__).parent; A=C.parent/'creature_a_atomic_reception'; R=Path('/workspace/pokemon-essentials'); B=Path('/workspace/pokemon-essentials-clean-room')
utc=datetime.datetime.now(datetime.timezone.utc).isoformat(); reader='/root/creature_a_atomic_reception'; commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def read(p): return json.loads(p.read_text())
def write(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
identities={}; units=[]
def source(key,path,credit='OWN_FULL_ACTUAL_READ_REUSED'):
 raw=(R/path).read_bytes(); assert raw==subprocess.check_output(['git','-C',str(R),'show',commit+':'+path])
 identities[key]=dict(path=path,commit=commit,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),git_blob=subprocess.check_output(['git','-C',str(R),'rev-parse',commit+':'+path],text=True).strip(),lines=len(raw.splitlines()),actual_reader=reader,credit=credit)
 return raw.decode('utf-8-sig').splitlines(keepends=True)
def whole(key,path):
 ls=source(key,path); units.append(dict(id=key+':WHOLE',source_identity_key=key,range=[1,len(ls)],text=''.join(ls),complete_definition=True)); return ls
def method(key,ls,name,occ=0):
 starts=[i for i,l in enumerate(ls) if re.match(r'\s*def\s+'+re.escape(name)+r'(?=[\s(;]|$)',l)]
 i=starts[occ]; indent=re.match(r'\s*',ls[i]).group(); j=next(j for j in range(i,len(ls)) if re.match(r'^'+re.escape(indent)+r'end\s*(?:#.*)?$',ls[j]))
 uid=f'{key}:{name}:{occ}';units.append(dict(id=uid,source_identity_key=key,range=[i+1,j+1],text=''.join(ls[i:j+1]),complete_definition=True)); return uid
fp=A/'facility-individual-producer-complete.v1.json'; fraw=fp.read_bytes();fd=json.loads(fraw)
identities.update(fd['source_identities']);units.extend(fd['whole_source_units'])
pk=(R/identities['pokemon']['path']).read_text().splitlines(keepends=True)
for n in ['hp=','type1','type2','hasType?','shiny?','super_shiny?','super_shiny=','nature','nature=','nature_for_stats','nature_for_stats=','hasNature?']:method('pokemon',pk,n)
whole('nature','Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb')
whole('stat','Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb')
whole('gender','Data/Scripts/010_Data/001_Hardcoded data/002_GenderRatio.rb')
whole('moveall','Data/Scripts/014_Pokemon/004_Pokemon_Move.rb')
ls=source('facility','Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb')
for n in ['self.fromInspected','initialize','convertMove','createPokemon']:method('facility',ls,n)
ls=source('exp','Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb');method('exp',ls,'pbGainEVsOne')
ls=source('items','Data/Scripts/013_Items/001_Item_Utilities.rb')
for n in ['pbJustRaiseEffortValues','pbRaiseEffortValues','pbMaxUsesOfEVRaisingItem','pbUseEVRaisingItem']:method('items',ls,n)
ls=source('effects','Data/Scripts/013_Items/002_Item_Effects.rb','OWN_PARTIAL_COMPLETE_REGISTRATIONS_ONLY')
units.append(dict(id='effects:VITAMINS_AND_HPFEATHER',source_identity_key='effects',range=[714,772],text=''.join(ls[713:772]),complete_registrations=True))
ls=source('settings','Data/Scripts/001_Settings.rb')
for n in ['MECHANICS_GENERATION','MAXIMUM_LEVEL','SHINY_POKEMON_CHANCE','DISABLE_IVS_AND_EVS','NO_VITAMIN_EV_CAP']:
 i=next(i for i,l in enumerate(ls) if re.match(r'\s*'+n+r'\s*=',l));units.append(dict(id='settings:'+n,source_identity_key='settings',range=[i+1,i+1],text=ls[i],complete_statement=True))
ls=source('summary','Data/Scripts/016_UI/006_UI_Summary.rb','OWN_PARTIAL_COMPLETE_METHOD_ONLY');method('summary',ls,'drawPageTwo')
raws=[]
for key,path,selected in [('base','PBS/pokemon.txt',['BULBASAUR']),('tower','PBS/battle_tower_pokemon.txt',[])]:
 ls=source(key,path,'OWN_COMPLETE_NAMED_RAW_RECORDS_ONLY')
 if key=='base':
  for name in selected:
   i=next(i for i,l in enumerate(ls) if l.strip()=='['+name+']');j=next((j for j in range(i+1,len(ls)) if ls[j].lstrip().startswith('[')),len(ls));raws.append(dict(id=key+':'+name,source_identity_key=key,range=[i+1,j],text=''.join(ls[i:j]),complete_raw_record=True))
 else:
  for n in [3,5,117]:raws.append(dict(id='tower:line'+str(n),source_identity_key=key,range=[n,n],text=ls[n-1],complete_raw_record=True))
claims={}; refs={}
def Cc(n,rr,*ss):claims[f'ST{n:02}']=list(ss);refs[f'ST{n:02}']=rr.split('|')
calc='pokemon:calcHP:0|pokemon:calcStat:0|pokemon:calcIV:0|pokemon:calc_stats:0|stat:WHOLE';HP='pokemon:calc_stats:0|pokemon:hp=:0';nat='pokemon:nature:0|pokemon:nature=:0|pokemon:nature_for_stats:0|pokemon:nature_for_stats=:0|pokemon:hasNature?:0|nature:WHOLE';shiny='pokemon:shiny?:0|pokemon:super_shiny?:0|pokemon:super_shiny=:0';fac='facility:self.fromInspected:0|facility:initialize:0|facility:convertMove:0|facility:createPokemon:0|pokemon:initialize:0|pokemon:calc_stats:0|stat:WHOLE';vit='items:pbRaiseEffortValues:0|items:pbMaxUsesOfEVRaisingItem:0|items:pbUseEVRaisingItem:0|effects:VITAMINS_AND_HPFEATHER|settings:NO_VITAMIN_EV_CAP|settings:MECHANICS_GENERATION'
Cc(1,calc,'HP45/31/0/L50：EV整除0，内层121×50整除100得60。','再加L50与10得120。')
Cc(2,calc,'EV252整除4得63，(90+31+63)×50整除100得92。','HP92+60=152。')
Cc(3,calc,'B100/IV31/EV0/L100内层231。','HP231+110=341。')
Cc(4,calc,'B255/IV31/EV252/L100内层604。','HP604+110=714。')
Cc(5,calc+'|settings:DISABLE_IVS_AND_EVS','禁用开关只在计算局部把IV/EV都视为0。','HP200+110=310，原IV/EV存储不变。')
Cc(6,calc,'base==1先于禁用/普通公式返回1。','任意所给合法L/IV/EV都不能绕过此早返。')
for n,base,iv,ev,level,mult,out in [(7,49,31,0,50,100,69),(8,49,31,0,50,110,75),(9,49,31,0,50,90,62),(10,37,30,0,30,110,39),(11,60,0,0,50,110,71),(12,100,0,3,100,100,205),(13,100,0,4,100,100,206),(14,100,0,7,100,100,206),(15,100,0,8,100,100,207)]:
 inner=((base*2+iv+ev//4)*level)//100; assert (inner+5)*mult//100==out
 Cc(n,calc,f'EV{ev}整除4得{ev//4}；B{base}/IV{iv}/L{level}内层整数{inner}。',f'加5后乘N{mult}再整除100得{out}，未合并两次整除或四舍五入。')
Cc(16,HP,'先算新totalhp122，再按差2调整旧HP80。','hp=最终夹到0..新totalhp，得82。')
Cc(17,HP,'旧HP0但hp_difference2>0使写回门通过。','max(0+2,1)=2，故静态上复活为2。')
Cc(18,HP,'旧HP0且上限差0或负，不通过写回门。','totalhp已改，HP仍0。')
Cc(19,HP,'旧存活5且差-10仍通过@hp>0门。','max(-5,1)=1，再hp夹限得1。')
Cc(20,HP,'旧HP130高于旧上限125，新上限120先写。','差-5产生125，hp=再夹到新上限120。')
for n,pid,chance,out in [(21,0,128,1),(22,127,128,1),(23,128,128,0),(24,31,32,1),(25,32,32,0)]:Cc(n,'pokemon:gender:0|gender:WHOLE',f'合法可变性别记录female_chance={chance}，缓存nil时用PID低8位{pid}。',f'严格小于门结果性别{out}；等于阈值属男。')
Cc(26,'pokemon:ability_index:0','缓存nil/false时PID最低bit派生索引。','PID0/1分别0/1，索引缓存后PID单独变更不自动清它。')
Cc(27,nat,'Nature登记顺序完整25项，派生取PID % Nature.count对应keys。','给定0/1/5/24/25/777/1000分别HARDY/LONELY/BOLD/QUIRKY/HARDY/BRAVE/HARDY。','查询后存缓存；该顺序不由能力修正表排序替代。')
for n,pid,owner,d,s,ss in [(28,0,0,0,True,True),(29,1,0,1,True,False),(30,16,0,16,False,False),(31,0x10000,0,1,True,False),(32,0x12341234,0,0,True,True),(33,0xFFFFFFFF,0xFFFFFFFF,0,True,True)]:
 a=pid^owner;assert ((a&0xffff)^((a>>16)&0xffff))==d
 Cc(n,shiny+'|settings:SHINY_POKEMON_CHANCE',f'独立未缓存读取：PID={pid}、Owner.id={owner}，两半异或d={d}。',f'默认阈值16：普通={s}；超级按d==0得{ss}。','普通与超级的缓存各自独立计算，不由一项读取强制填另一项。')
Cc(34,'moveall:WHOLE','基础20，ppup0/1/2/3使total20/24/28/32。','ppup=先写计数，再仅把现PP夹至新total；增加计数不补PP。')
Cc(35,'moveall:WHOLE','计数没有0..3域校验，4被写入。','total20+20×4整除5=36。')
Cc(36,'moveall:WHOLE','计数-1被写入且total为16。','现PP按新0..16夹限，非法常规计数并未自动归零。')
Cc(37,'moveall:WHOLE','计数-6先写，计算total=-4。','后续clamp(0,-4)区间反转而失败；当前PP赋值未完成，原PP保留。','-4是可读公式结果而非成功写入的PP。')
Cc(38,'pokemon:initialize:0|pokemon:gender:0|pokemon:ability_index:0|pokemon:shiny?:0|pokemon:super_shiny?:0|nature:WHOLE','普通constructor calc_stats已调用nature_for_stats并按PID填性格。','性别/异色/能力索引按各自首次读取门再派生，ST21–33合法fixture仍分别成立。','构造前序随机/Owner/数据正常是共同条件，不把全缓存一概说成构造时已填。')
Cc(39,nat+'|pokemon:initialize:0','普通构造经calc_stats已填nature缓存。','单独更改personalID不失效缓存，无参hasNature仍真并保原性格。')
Cc(40,nat,'合法nature_for_stats覆盖触发calc但优先覆盖。','nature=nil在覆盖存在时不calc，原表现缓存nil使无参hasNature假。','显式读取nature才按PID重填，此后hasNature真。','仅calc且覆盖仍在不读取表现nature，故不填回它。')
Cc(41,shiny,'先普通d0缓存true，超级仍nil。','PID改16后超级首算false，普通旧true保留。')
Cc(42,shiny,'两个已缓存true不联动失效。','清普通nil并改PID16仅重算普通false。','超级原true保留。')
Cc(43,shiny,'super_shiny=true先写超级且普通置true。','直接shiny=false只写普通，保超级true。','允许显式覆盖得到与当前数学判定不一致组合。')
Cc(44,shiny,'普通已算结果在PID单独改变后保留。','先写普通nil才允许下次按新PID重算。')
Cc(45,'pokemon:types:0|pokemon:type1:0|pokemon:type2:0|pokemon:hasType?:0','types克隆完整species.types，三项不截断。','hasType严格解析T3并在完整数组include为true。','兼容type1/type2只读前两，缺第二才回第一；不改变完整数组。')
Cc(46,vit,'默认世代8令NO_VITAMIN_EV_CAP=true。','维生素effect显式传此值，绕过100门而仍守252/510。','100+10得110，随后calc与幸福/UI，后继异常不回滚EV。')
Cc(47,vit,'设置100封顶意味着no_ev_cap=false。','当前100使pbRaiseEffortValues在总额/增量计算前返回0。','首剂零增长使effect false，正常caller不消耗该失败剂。')
Cc(48,'exp:pbGainEVsOne:0','有效Shadow心阶段<=3且saved_ev存在，当前与暂存先都计入evTotal。','单项剩余252-240-10=2，收益10夹至2。','写saved_ev而非当前ev；实际调用还须Battle收益/当前持物/病毒前提。')
Cc(49,nat+'|pokemon:calc_stats:0','计算覆盖B存在时calc_stats取B.stat_changes。','表现性格A保原缓存，显示读取仍A。')
Cc(50,nat,'已有计算覆盖时设表现性格只写表现缓存。','nature=不调用calc，因此已有数值不变。')
Cc(51,'pokemon:level=:0|settings:MAXIMUM_LEVEL','level101大于默认max100，raise在写level/exp前。','原level缓存与exp保留；不是先夹为100。')
Cc(52,calc,'ivMaxed ATTACK真令calcIV对该项取常量31。','@iv原Hash不改，只有有效计算输入被替代。')
Cc(53,calc+'|settings:DISABLE_IVS_AND_EVS','禁用配置令calcHP/calcStat局部IV/EV为0。','stored IV、ivMaxed、EV均不归零，状态和计算分层。')
Cc(54,HP,'濒死升级若新totalhp增大，hp_difference>0门仍通过。','按增量复活，非统一濒死保护；与ST17同实际写点。')
Cc(55,calc,'EV3的整除项0，EV4整除项1。','有效EV输入增加1，但最终能力是否增加仍依后续L/100整除。')
Cc(56,fac,'SUNKERN第3物理行是RELAXED/HP,SA具名双项模板。','constructor先零六EV，createPokemon直接写510/2=255到两项。','总510，不经EV_STAT_LIMIT252夹限。','calc_stats只读255，取255整除4=63而不规范化存储。')
Cc(57,fac,'三个互不重复有效努力项时每项510整除3=170。','三项总510，其余0；公式不保证每模板超252。','原目录其余合法前提仍须成立；独立原始默认DROWZEE行117为QUIRKY/HP,ATK,SA，并非把其性格伪称RELAXED。')
Cc(58,fac,'人工明确四项HP/ATTACK/DEFENSE/SPECIAL_ATTACK，各510整除4=127。','新个体总508，剩2没有分配语句。','此四项变体不冒默认原PBS具有该行，也不推广重复项。')
Cc(59,fac+'|settings:DISABLE_IVS_AND_EVS','模板直接写255/255与禁用计算开关无关。','后calc的IV/EV局部0不改变stored两项255。')
Cc(60,calc+'|nature:WHOLE','BULBASAUR完整原BaseStats按pbs_order映射为HP45/Atk49/Def49/SpAtk65/SpDef65/Speed45。','L50/IV31/EV0中性[120,69,69,85,85,65]。','LONELY只Atk+10/Def-10，得[120,75,62,85,85,65]。')
Cc(61,calc+'|nature:WHOLE','BRAVE登记序2，未缓存PID模25为2可派生。','升攻击降速度，得[120,75,69,85,85,58]，防御不降。')
Cc(62,calc+'|nature:WHOLE','ADAMANT升攻击降特攻，Bulbasaur得[120,75,69,76,85,65]。','人工五非HP基础50/L100/IV0/EV0各修正前105。','攻击105×110整除100=115，特攻105×90整除100=94，其余105。')
Cc(63,calc+'|nature:WHOLE','HARDY/DOCILE/SERIOUS/BASHFUL/QUIRKY登记序0/6/12/18/24且stat_changes空。','五者均中性[120,69,69,85,85,65]。','完整25表20有各一升一降，五者无修正，缓存/覆盖不因该表重派。')
Cc(64,'summary:drawPageTwo:0|pokemon:calcIV:0','原始IV全31并列，固定环序HP/Atk/Def/Speed/SpAtk/SpDef。','PIDmod6=3起始Speed，相等不替换，选Speed。','原31mod5=1，对声音警觉语义；不由Stat登记序误选SpAtk。')
Cc(65,'summary:drawPageTwo:0','同并列IV31，PIDmod6=4起始SpAtk。','选择SpAtk余数1，对应爱恶作剧语义；30短语为独立本地化语义非逐字承诺。')
Cc(66,'summary:drawPageTwo:0|pokemon:calcIV:0','原Atk31/Speed30，PIDmod6=3先见Speed30仍被后Atk31替换。','速度Hyper上限只影响calcIV，不改summary读取原iv。','选Atk31余数1，爱大闹；不按有效能力/计算性格。')
Cc(67,fac,'固定第5行CATERPIE/FOCUSBAND/QUIRKY/HP,ATK/TACKLE,STRINGSHOT完整原行。','L50/IV31、数据正常返回时两EV255，其余0，总510。','重算不改255，常规培养252/510门独立存在。','本包不接受1888杯模板整体、不转移WP28/WP76全主责。')
assert len(claims)==67
unitids={u['id'] for u in units}; assert all(uid in unitids for us in refs.values() for uid in us)
formal='deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md';fraw=(B/formal).read_bytes();rows={}
for i,l in enumerate(fraw.decode().splitlines(),1):
 m=re.match(r'\| (ST\d+) \|',l)
 if m:rows[m[1]]=(i,l)
assert set(rows)==set(claims)
records=[]
for v,ss in claims.items():
 line,row=rows[v];children=[dict(id=f'STV-{v}-A{i:02}',meaning=s,complete_source_unit_ids=refs[v],status='MANUALLY_JOINED_BOUNDED_STATIC',whole_parent_acceptance=False) for i,s in enumerate(ss,1)]
 records.append(dict(id='STV-'+v,vector=v,formal=dict(path=formal,line=line,complete_raw_row=row),premise='完整原行的合法普通/非蛋/非Shadow/默认或指定人工与配置条件分别保留。缓存是否已填按每行次序；数据、随机与前序UI正常到指定观察点。未执行目标代码/编译/宿主/存档。',child_assertions=children,normal_cancel_failure='数学pure计算没有取消；setter和重算按实际赋值次序保前缀。PP非法负上限写计数后失败；level越界先拒；EV effect先改EV/calc/幸福后UI，失败不回滚。设施先构造/物/PID/性格/幸福/Move再直写EV/IV重算，非原子交易。',receiver='Pokemon/Species/Nature/Move/Stat定义→具名设施或培养/Battle增量入口→持久对象与场上/摘要读取；原raw EV/IV/缓存保持独立。SavedData对象图有限接合沿A已接17顶层值，不声称native多root别名/实际重载验证。',raw_records=['base:BULBASAUR'] if v in ['ST60','ST61','ST62','ST63'] else ['tower:line3'] if v in ['ST56','ST59'] else ['tower:line117'] if v=='ST57' else ['tower:line5'] if v=='ST67' else [],remaining=['全部具名原行的有限静态推导已拆；非整体WP19/设施/物品/摘要/存档批准。','ST57默认三项原行/性格与数值公式分别限定，不扩成默认RELAXED/HP,ATK,SA存在性断言。'] if v=='ST57' else ['未运行native/UI/游戏；无全域分母冻结或新独立票。'],accepted=False))
count=sum(len(x['child_assertions']) for x in records)
for u in units:
 ident=identities[u['source_identity_key']];ls=(R/ident['path']).read_text(encoding='utf-8-sig').splitlines(keepends=True);lo,hi=u['range'];assert ''.join(ls[lo-1:hi]).rstrip('\n')==u['text'].rstrip('\n'),u['id']
out=dict(schema='gr8-crec-stat-catalog67/v1',recorded_utc=utc,actual_reader=reader,formal_identity=dict(path=formal,bytes=len(fraw),sha256=hashlib.sha256(fraw).hexdigest(),actual_current_read_chunks=['f32349']),source_identities=identities,complete_source_units=units,complete_raw_records=raws,producer_packet_binding=dict(path='../creature_a_atomic_reception/'+fp.name,bytes=len(fraw) if False else len(fp.read_bytes()),sha256=hashlib.sha256(fp.read_bytes()).hexdigest(),qualification='54 complete original producerunits copied with original actual reader; old86 not required or adopted.'),records=records,manual_atoms=count,actual_current_source_rereads=['36fc3b','deddf4','c9136f','ebf803','64df79','506e8a','14f1e9','ddb3fb','6ca5b9','ccefa2'],whole_PBS_credit=False,whole_domain_acceptance=False,denominator_frozen=False,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
p=C/'stat-catalog67-meaning.v1.json'; assert not p.exists();write(p,out)
rv=read(C/'reverse-mapping.json');assert not any(x['id'].startswith('STV-ST') for x in rv['records']);rv['records'].extend(records);rv['utc']=utc;write(C/'reverse-mapping.json',rv)
pr=read(C/'progress.json');pr['updated_utc']=utc;pr['primary_clause_atoms']=sum(len(x.get('child_assertions',[])) for x in rv['records']);write(C/'progress.json',pr)
print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),groups=len(records),children=count,total_groups=len(rv['records']),total_children=pr['primary_clause_atoms'],source_units=len(units),utc=utc)))
