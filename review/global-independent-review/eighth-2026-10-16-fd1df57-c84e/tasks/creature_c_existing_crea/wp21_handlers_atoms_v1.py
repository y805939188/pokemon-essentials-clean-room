import json,re,hashlib,datetime,subprocess
from pathlib import Path
P=Path(__file__).parent;R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room')
utc=datetime.datetime.now(datetime.timezone.utc).isoformat();src='Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb';formal='deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md'
s=(R/src).read_text();fl=(B/formal).read_text().splitlines();rows=[]
def add(name,claims,receiver,remaining='Default/backup actual item/move/species/form PBS values and all transitive callers remain separately audited; source definition is audited even without default caller.'):
 rows.append((name,claims,receiver,remaining))
add('UNOWN',['创建rand28给0..27，无已有形态/蛋守卫。'],'Pokemon.initialize recheck_form tail: only storedform0 and enabled; truthy result form= then optional reset_moves')
add('SPINDA',['alterBitmap原样转交给pbSpindaSpots(pkmn,bitmap)，不改变form/PID。'],'Species.sprite_bitmap_from_pokemon selected non-egg effective species callback; exact PNG/native frame delivery is separately bounded')
for name in ['CASTFORM','CHERRIM','MELOETTA','AEGISLASH','WISHIWASHI','CRAMORANT']:
 add(name,['离场候选无条件返回0；不使用battle/usedInBattle/endBattle附加门。'],'Battle::Peer actual leaving callback then candidate form=')
for name,item in [('GROUDON','REDORB'),('KYOGRE','BLUEORB')]:
 add(name,[f'getPrimalForm持{item}返回1，否则nil。','定义本身不写形态或次数；Primal方法/战斗caller另接。'],'Pokemon.getPrimalForm/makePrimal; Battle pbPrimalReversion')
add('BURMY',['创建用pbGetEnvironment：Rock/Sand/Cave→1，None→2，其它→0。','离场先要求endBattle和usedInBattle都真；然后读battle.environment同映射，未满足返回nil。','创建环境服务与战斗对象环境是两个不同实际输入。'],'Pokemon ctor / Battle::Peer leaving')
add('WORMADAM',['仅创建环境Rock/Sand/Cave→1、None→2、其它→0；无离场hook。'],'Pokemon ctor')
add('ROTOM',['形态招顺序OVERHEAT/HYDROPUMP/BLIZZARD/AIRSLASH/LEAFSTORM，找当前列表首个属于集合的槽。','form>0索引form-1取目标；未登记目标当nil。只有此时目标nil且有旧槽且numMoves1才试THUNDERSHOCK，缺失抛错。','之后才因已会目标置nil；不再重检保底，合法form1唯一OVERHEAT同值裸提交可删成空。','有旧槽且目标nil则删除该槽后消息；有目标直接同Move.id=并消息；无旧槽有目标才pbLearnMove(...,true)。','同槽id=保原对象/提升计数，当前PP按新total钳制；通用pbLearnMove满槽替换生成新对象或放弃，蛋/Shadow拒绝，既有form写不回滚。'],'Pokemon.form=/setForm→onSetForm; PokemonMove.id=; ItemUtilities.pbLearnMove; UI bottle/fusion finite package', 'ROTOMCATALOG外层同值守卫已有限UI接收；所有其它item caller/PBS须逐对象绑定。')
add('GIRATINA',['先持GRISEOUSORB→1；否则当前map安全导航metadata.has_flagDistortionWorld→1；否则0。','宝珠条件先短路；无地图/元数据时可安全回0。'],'Pokemon.form dynamic getter')
add('SHAYMIN',['fainted?或statusFROZEN或当前isNight?任一真返回0；其它nil不改变。','从左到右短路，白天不等于无条件返回1。'],'Pokemon.form')
add('ARCEUS',['先hasAbilityMULTITYPE，不符nil；不读持物表。','17编号1..8,10..18，无9；依序检查每编号plate/Z两物，首命中返回编号，无持物0。','1FISTPLATE/FIGHTINIUMZ，2SKYPLATE/FLYINIUMZ，3TOXICPLATE/POISONIUMZ，4EARTHPLATE/GROUNDIUMZ，5STONEPLATE/ROCKIUMZ，6INSECTPLATE/BUGINIUMZ，7SPOOKYPLATE/GHOSTIUMZ，8IRONPLATE/STEELIUMZ。','10FLAMEPLATE/FIRIUMZ，11SPLASHPLATE/WATERIUMZ，12MEADOWPLATE/GRASSIUMZ，13ZAPPLATE/ELECTRIUMZ，14MINDPLATE/PSYCHIUMZ，15ICICLEPLATE/ICIUMZ，16DRACOPLATE/DRAGONIUMZ，17DREADPLATE/DARKINIUMZ，18PIXIEPLATE/FAIRIUMZ。'],'Pokemon.form→hasAbility/item queries')
add('DARMANITAN',['离场返回2*(pkmn.form/2)，当前Ruby整数除法，1→0、3→2；无终战/濒死门。'],'Peer leaving')
add('DEERLING',['读取返回pbGetSeason，不本地写回或存季节快照。'],'Pokemon.form; same handler object copied toSAWSBUCK')
add('KYUREM',['入场仅当前form1/2返回+2，其它nil；wild参数不参与。','离场当前form>=3返回-2；无终战/濒死门。','提交0：ICEBURN/FREEZESHOCK→GLACIATE；FUSIONFLARE/FUSIONBOLT→SCARYFACE；目标未登记跳过，已会则置nil并在当前迭代内compact，否则同Move.id=。','提交1：GLACIATE→ICEBURN，SCARYFACE→FUSIONFLARE；提交2对应FREEZESHOCK/FUSIONBOLT，各目标存在且未会才替换。','白黑形态不直接相互专属招转换；归0遍历内compact可跳过前移项，[GLACIATE,ICEBURN,FUSIONFLARE]→[GLACIATE,FUSIONFLARE]。'],'Pokemon.form=/Peer entering+leaving; PokemonMove id setter', '入离场时序及Fusion tool具体caller须与完整有限UI包/实际Battle source绑定。')
add('KELDEO',['hasMoveSECRETSWORD真→1，其它0。'],'Pokemon.form')
add('GENESECT',['检查SHOCKDRIVE1、BURNDRIVE2、CHILLDRIVE3、DOUSEDRIVE4，首命中；全无0。'],'Pokemon.form')
add('GRENINJA',['仅form2且(fainted?或endBattle)返回1；其它nil。'],'Peer leaving')
add('SCATTERBUG',['创建读当前全局$player.secret_ID%18，无本地player空保护；无随机抽取。'],'Pokemon ctor; copySPEWPA/VIVILLON')
for name,days in [('FURFROU',5),('HOOPA',3)]:
 add(name,[f'getForm在time_form_set falsey或pbGetTimeNow.to_i > time_form_set.to_i+{days}*86400时0，其它nil；恰界不回退。','onSetForm按请求form>0写当前整秒时间，否则nil；使用请求参数，不重新读当前实际storedform。','提示型setForm在写form/清缓存后yield才运行本hook；yield可重入动态读而改变storedform，外层仍按原请求写时间。'],'Pokemon.form dynamic / form= / setForm; UI Hoopa finite fullchain', '真实系统时钟/异常转换与全部插件callback未运行；瓶子完整UI有限包已接，不能扩大为全融合。')
add('ESPURR',['读取直接返回pkmn.gender；可触发gender懒缓存，非纯字节读。'],'Pokemon.form; copyMEOWSTIC')
add('PUMPKABOO',['创建rand100一次；<5→3，<20→2，<65→1，否则0，概率5/15/45/35。'],'Pokemon ctor; copyGOURGEIST')
add('XERNEAS',['开始无条件候选1。','离场仅endBattle真→0，其它nil。'],'Battle starting / Peer leaving')
add('ZYGARDE',['离场form>=2且(fainted?或endBattle)返回form-2，其它nil。'],'Peer leaving')
add('ROCKRUFF',['先form_simple>=2返回nil；否则夜1，日0。','simple读取forced||stored，不触发getForm递归；有效强制形态更早由普通form入口返回。'],'Pokemon.form/form_simple')
add('LYCANROC',['创建先evening→2，再night→1，其它0；时段可能各自行读时间。'],'Pokemon ctor')
add('SILVALLY',['无RKSSYSTEM返回nil；有才查17memory编号1..8,10..18，无9，按序首匹配，未匹配0。','依次FIGHTING/FLYING/POISON/GROUND/ROCK/BUG/GHOST/STEEL、FIRE/WATER/GRASS/ELECTRIC/PSYCHIC/ICE/DRAGON/DARK/FAIRY MEMORY。'],'Pokemon.form→ability/item')
add('MINIOR',['创建rand7..13闭区间。','入场仅form>=7且wild真返回form-7；玩家入场不强制流星。','离场form<7返回+7，无终战门。'],'Pokemon ctor / Peer entering+leaving')
for name in ['MIMIKYU','EISCUE','MORPEKO']:
 add(name,['离场仅fainted?或endBattle真返回0，其它nil。'],'Peer leaving')
add('NECROZMA',['离场form>=3且(fainted?或endBattle)返回form-2。','onSetForm旧/新任一>2立即返回，不改招式。','正常归0依次遗忘SUNSTEELSTRIKE/MOONGEISTBEAM并消息；若最终无招pbLearnMoveCONFUSION。','正常form1/2尝试SUNSTEELSTRIKE/MOONGEISTBEAM，pbLearnMove(...,true)；目标解析先于蛋/Shadow拒绝，拒绝或取消不回滚已写form/删除。'],'Pokemon form setters / Peer leaving / generic learning')
add('TOXEL',['创建nature_id属于LONELY/BOLD/RELAXED/TIMID/SERIOUS/MODEST/MILD/QUIET/BASHFUL/CALM/GENTLE/CAREFUL则1，其它0。','读表现性格身份，不读nature_for_stats覆盖。'],'Pokemon ctor; copyTOXTRICITY')
add('SINISTEA',['创建rand100<10→1，其它0；单次抽取。'],'Pokemon ctor; copyPOLTEAGEIST')
add('MILCERY',['item_id在STRAWBERRYSWEET/BERRYSWEET/LOVESWEET/STARSWEET/CLOVERSWEET/FLOWERSWEET/RIBBONSWEET内时index+(PID%9)*7，否则0。','无额外随机；同PID持物对应稳定口味与装饰编号。'],'Pokemon.form')
add('ALCREMIE',['创建rand63得0..62，9口味×7装饰。'],'Pokemon ctor')
add('INDEEDEE',['读取pkmn.gender，同gender懒缓存语义。'],'Pokemon.form')
for name,item,move in [('ZACIAN','RUSTEDSWORD','BEHEMOTHBLADE'),('ZAMAZENTA','RUSTEDSHIELD','BEHEMOTHBASH')]:
 add(name,[f'开始候选持{item}→1，否则0。',f'开始个体改写先目标{move}存在再持物匹配；每个IRONHEAD槽直接id={move}。',f'离场仅endBattle真候选0，并每个{move}槽id=IRONHEAD；非终战不改，终战不重检持物/IRONHEAD存在。','目标还原身份缺失时idsetter解析先失败，该槽仍原标识，前序动作不回滚；同Move提升计数保留/当前PP受新total钳制。'],'Battle starting forms + actual changePokemon hook / Peer leaving')
add('URSHIFU',['创建rand2得0/1，无事件编号消费。'],'Pokemon ctor')
add('CALYREX',['归0先遗忘GLACIALLANCE/ASTRALBARRAGE并消息。','再用已写基础形态species_data等级/教学/蛋招表去掉其它不可得招，无当前等级限制；消息后置nil，遍历完统一compact。','为空pbLearnMoveCONFUSION；form1/2分别尝试GLACIALLANCE/ASTRALBARRAGE(...,true)。','无NECROZMA式oldForm>2守卫；已会/蛋/Shadow/交互放弃按generic学习入口，form及此前删除不回滚。'],'Pokemon form setters / generic learning')
add('RATTATA',['蛋创建若有当前map、metadataTownMapPosition并且get_species_form(base,region).form==region则返回region，否则0。','缺指定form会由get_species_form回base，比较不等则0；不是单凭地区号强造记录。'],'DayCare::EggGenerator.inherit_form; copy17regional targets')
for name,region in [('PIKACHU',1),('KOFFING',2)]:
 add(name,[f'读取先form_simple>=2→nil；否则当前map.metadataTownMapPosition首分量=={region}→1；其余0。','缺map/metadata位置可回0；复制目标共享该handler对象。'],'Pokemon.form; regional evolution/copy targets')

unitmap={}
for m in re.finditer(r'^MultipleForms.register\(:(\w+), \{\n',s,re.M):
 end=s.index('\n})',m.end())+3;unitmap[m.group(1)]=(s.count('\n',0,m.start())+1,s.count('\n',0,end)+1,s[m.start():end])
assert {r[0] for r in rows}==set(unitmap)
b=(R/src).read_bytes();assert subprocess.check_output(['git','-C',str(R),'show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+src])==b
identity=dict(path=src,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),reader='/root/creature_a_atomic_reception',full_read_chunks=['3e0bda','554cc5','b7057f'],fixed_R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b')
units=[];records=[]
for i,(name,claims,receiver,remain) in enumerate(rows,1):
 a,z,body=unitmap[name];uid='C21-REG-'+name;units.append(dict(id=uid,identity=identity,range=[a,z],text=body,complete_registration=True))
 loc=[j+1 for j,l in enumerate(fl) if name in l]
 records.append(dict(id=f'C21-R{i:03}',formal=dict(path=formal,matching_lines=loc),species=name,premise='Fixed valid Pokemon/registries and explicit branch-specific input. Ruby nil/false/numeric0 remain distinct. Bare definition candidate is not automatically committed; consumer chooses form=/setForm or no write. All primary source bytes own actual FULL; no new context/vote.',child_assertions=[dict(id=f'C21-R{i:03}-A{n:02}',meaning=c,source_units=[uid],status='SOURCE_DEFINITION_SUPPORTED_BOUNDED',parent_acceptance=False) for n,c in enumerate(claims,1)],actual_receiver=receiver,normal_cancel_failure='Definition-specific writes/returns are stated above. form=/setForm write form and clear ability cache before hook; hook/yield/registry/calc/dex errors preserve reached prefix. Learning refusal/cancel changes no selected new slot but does not erase earlier form/deletions.',remaining=remain,accepted=False))
copies=[]
for m in re.finditer(r'MultipleForms.copy\(([^)]*)\)',s,re.S):
 names=re.findall(r':(\w+)',m.group(1));copies.append(dict(source=names[0],targets=names[1:],range=[s.count('\n',0,m.start())+1,s.count('\n',0,m.end())+1],text=m.group(0),meaning='At copy-time resolve source current mapping and bind identical object to each target; subsequent source reregister does not retarget existing copies; in-place mapping mutation visible through aliases; absent source no-op.'))
assert len(copies)==9 and sum(len(x['targets']) for x in copies)==27
payload=dict(schema='gr8-cre-c-wp21-complete-handler-meaning-atoms/v1',recorded_utc=utc,actual_reader=identity['reader'],source_units=units,records=records,complete_copy_statements=copies,manual_atom_count=sum(len(x['child_assertions']) for x in records),registration_count=49,copied_targets=27,remaining=['SPINDA full helper pixel/math and frame-consumer atoms separately pending','HandlerHash mechanism/constructor/form mutation full formal clauses separately pending','Display markings/ribbons/contest complete consumers, migration and actual records separately pending'],business='NOT_EXECUTED',update='UPDATE_NOT_STARTED',new_contexts=0,new_votes=0)
f=P/'wp21-handler-meaning-atoms.v1.json';f.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
d=json.loads((P/'reverse-mapping.json').read_text());assert not any(x['id'].startswith('C21-R') for x in d['records']);d['records']+=records;d['utc']=utc;(P/'reverse-mapping.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
pr=json.loads((P/'progress.json').read_text());pr['updated_utc']=utc;pr['primary_clause_atoms']=sum(len(x.get('child_assertions',[])) for x in d['records']);(P/'progress.json').write_text(json.dumps(pr,ensure_ascii=False,indent=2)+'\n');o=f.read_bytes();print(json.dumps(dict(utc=utc,groups=len(records),atoms=payload['manual_atom_count'],bytes=len(o),sha256=hashlib.sha256(o).hexdigest())))
