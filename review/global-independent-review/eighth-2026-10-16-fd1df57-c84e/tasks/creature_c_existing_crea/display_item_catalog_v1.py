import json,re,hashlib,datetime,subprocess
from pathlib import Path
C=Path(__file__).parent;A=C.parent/'creature_a_atomic_reception';R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception';commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def read(p):return json.loads(p.read_text())
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
names={'S':C/'wp21-mechanism-spinda-display.v1.json','H':C/'wp21-handler-meaning-atoms.v1.json','I':A/'facility-individual-producer-complete.v1.json','G':C/'wp30-compound-meaning.v1.json','D':C/'form-data-receiver-supplement.v1.json'};ps={};bindings={}
for k,p in names.items():
 raw=p.read_bytes();d=json.loads(raw);ps[k]={x['id']:x for x in d.get('whole_source_units',d.get('complete_source_units',d.get('source_units',[])))};bindings[k]=dict(path=str(p.relative_to(C)) if p.is_relative_to(C) else '../creature_a_atomic_reception/'+p.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader)
ident={};units=[];raws=[]
def source(k,path):
 raw=(R/path).read_bytes();assert raw==subprocess.check_output(['git','-C',str(R),'show',commit+':'+path]);ident[k]=dict(path=path,commit=commit,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),git_blob=subprocess.check_output(['git','-C',str(R),'rev-parse',commit+':'+path],text=True).strip(),actual_reader=reader,credit='OWN_PARTIAL_COMPLETE_NAMED_UNITS_ONLY; prior ownFULL separately retained where applicable');return raw.decode('utf-8-sig').splitlines(keepends=True)
def met(k,ls,n,label=None,after=0):
 i=next(i for i,l in enumerate(ls) if i>=after and re.match(r'\s*def\s+'+re.escape(n)+r'(?=[\s(;]|$)',l));indent=re.match(r'\s*',ls[i]).group();j=i if re.search(r';\s*end\s*$',ls[i]) else next(j for j in range(i+1,len(ls)) if re.match(r'^'+re.escape(indent)+r'end\s*(?:#.*)?$',ls[j]));uid=k+':'+(label or n);units.append(dict(id=uid,source_identity_key=k,range=[i+1,j+1],text=''.join(ls[i:j+1]),complete_definition=True));return uid
ls=source('effects','Data/Scripts/013_Items/002_Item_Effects.rb');units.append(dict(id='effects:ABILITYPATCH',source_identity_key='effects',range=[1103,1120],text=''.join(ls[1102:1120]),complete_registration=True))
ls=source('debug','Data/Scripts/020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb');units.append(dict(id='debug:SET_ABILITY',source_identity_key='debug',range=[613,660],text=''.join(ls[612:660]),complete_registration=True))
ls=source('party','Data/Scripts/016_UI/005_UI_Party.rb')
for n,label,after in [('initialize','Panel_initialize',164),('pokemon=','Panel_pokemon=',164),('refresh','Panel_refresh',164),('pbUseItem','Scene_pbUseItem',700),('pbHardRefresh','Scene_pbHardRefresh',800),('pbRefresh','Scene_pbRefresh',800),('pbRefreshSingle','Scene_pbRefreshSingle',800),('pbHardRefresh','Screen_pbHardRefresh',950),('pbRefresh','Screen_pbRefresh',950),('pbRefreshSingle','Screen_pbRefreshSingle',950)]:met('party',ls,n,label,after)
for label,lo,hi in [('ITEM_MENU',1374,1392),('ITEM_USE_MENU',1394,1406)]:units.append(dict(id='party:'+label,source_identity_key='party',range=[lo,hi],text=''.join(ls[lo-1:hi]),complete_registration=True))
ls=source('icons','Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb');met('icons',ls,'pokemon=','Icon_pokemon=',82)
ls=source('speciesfiles','Data/Scripts/010_Data/002_PBS data/009_Species_files.rb');met('speciesfiles',ls,'self.icon_bitmap_from_pokemon');met('speciesfiles',ls,'self.icon_filename');met('speciesfiles',ls,'self.sprite_bitmap')
ls=source('item','Data/Scripts/010_Data/002_PBS data/006_Item.rb')
for n in ['initialize','has_flag?','is_key_item?','is_important?','consumed_after_use?']:met('item',ls,n)
ls=source('itemutil','Data/Scripts/013_Items/001_Item_Utilities.rb');met('itemutil',ls,'pbCheckUseOnPokemon');met('itemutil',ls,'pbUseItemOnPokemon')
for k,path,nn in [('rawitems','PBS/items.txt',['ABILITYPATCH','PRISONBOTTLE']),('rawbase','PBS/pokemon.txt',['HOOPA','FURFROU']),('rawforms','PBS/pokemon_forms.txt',['HOOPA,1'])]:
 ls=source(k,path)
 for n in nn:
  i=next(i for i,l in enumerate(ls) if l.strip()=='['+n+']');j=next((j for j in range(i+1,len(ls)) if ls[j].lstrip().startswith('[')),len(ls));raws.append(dict(id=k+':'+n,source_identity_key=k,range=[i+1,j],text=''.join(ls[i:j]),complete_raw_record=True))
own={u['id'] for u in units};claims={};refs={}
def ref(s):
 k,n=s.split('@',1)
 if k=='O':assert n in own;return dict(package='SELF',unit_id=n,actual_reader=reader)
 assert n in ps[k],(k,n);return dict(package=bindings[k]['path'],unit_id=n,actual_reader=reader)
def Cc(v,rr,*ss):claims[v]=list(ss);refs[v]=[ref(x) for x in rr.split('|')]
ifs='H@C21-REG-FURFROU|I@pokemon:form:0|I@pokemon:form=:0|S@speciesfiles:self.sprite_bitmap_from_pokemon:0|S@speciesfiles:self.icon_filename_from_pokemon:0|O@speciesfiles:self.icon_bitmap_from_pokemon'
Cc('R4-IF01',ifs,'t+432001严格超过五日期限，动态候选0与stored1不等。','个体正/背/icon参数求值先提交0，onSet清时间，再匹配0资源。','提交清ability值、calc、条件Dex，不保证所有派生数值改变或最后缓存空。')
Cc('R4-IF02',ifs,'恰t+432000不通过严格>，仍1/t无提交。','独立时间戳nil使候选0，提交并清时间。')
Cc('R4-IF03',ifs,'战斗/仓库各独立提前返回stored1。','forced1非nil优先返回1，三例均不触发此次动态提交。')
Cc('R4-IF04',ifs,'forced0在Ruby中truthy且非nil，返回0用于资源参数。','不提交stored0，故stored1/time仍保。')
Cc('R4-IF05','O@speciesfiles:self.sprite_bitmap|S@speciesfiles:self.front_sprite_bitmap:0|S@speciesfiles:self.back_sprite_bitmap:0','低层物种+显式form1资源请求不自行访问给定个体。','它不能使上游为求参数的个体form读取也变纯读。')
Cc('R4-IF06',ifs,'资源查找前动态提交已完成。','全部候选缺失不回滚form/time前缀；icon包装或宿主后段成功未知。')
spot='S@forms:drawSpot:0|S@forms:pbSpindaSpots:0';spr='S@speciesfiles:self.sprite_bitmap_from_pokemon:0|S@animated:WHOLEFILE'
Cc('U03-SP01',spot,'编号0四锚点(66,50)/(42,48)/(78,14)/(30,12)。','编号2^32-1各锚点右/下30px。','相同合法输入无随机调用，四锚点组不可交换。')
Cc('U03-SP02',spot,'编号各单一四位组偏移分别只改指定S1右/S2下/S2右/S3下/S3右/S4下/S4右2px。','编号1只改S1下2px，其它点不动。')
Cc('U03-SP03',spot,'四形状按逐行literal区间计60/51/122/110逻辑点，未跨形合并。','S3末行仅5..7，S4仅4..8，不能补成对称。','每逻辑点写2×2四像素，尺寸充分是共同前提。')
Cc('U03-SP04',spot,'只读块左上RGBA，非异色偏移(0,-115,-75)、异色(-75,-10,-150)。','RGB200得到(200,85,125)或(125,190,50)，alpha80保左上值。','四像素同结果，另三点原色不各自参与；块外未命中不变。')
Cc('U03-SP05',spot,'低RGB10/20/30按各通道夹0..255得到(10,0,0)或(0,10,0)。','高255得到(255,140,180)或(180,245,105)，不下溢。')
Cc('U03-SP06',spot,'P61440给定重叠点按S1后S2处理两次。','假色200/200/200→200/85/125→200/0/50。','真色→125/190/50→50/180/0，不能去重。')
Cc('U03-SP07',spot+'|'+spr,'有效正面与背面都可进入个体alterBitmap；先资源copy、dispose原，再枚举交付帧。','文件名指定可枚举独立两帧PNG各独立一次，不把帧1处理色输入帧2。','假色两帧原200/100分别200/85/125与100/0/25，个体PID/form不写回。')
Cc('U03-SP08',spr,'蛋分支先返回蛋图，不进入个体Spinda修饰。','低层物种参数sprite入口没有个体PID修饰。','有效物种无alterBitmap保持资源结果，不推默认最终像素相同。')
Cc('U03-SP09',spr,'未匹配ret nil时没有可修饰位图。','加载异常/尺寸越界的native行为未知，不补裁剪/回滚/成功。','没有创建素材、调用宿主或运行参考。')
Cc('U03-SP10',spr,'原生两帧GIF/bitmap若入口仅交付一宿主bitmap，只证明该交付对象一次修饰请求。','内部两帧像素覆盖/显示/时序未知；不称各帧独立终色、不称只首帧或必成功失败。')
patch='I@pokemon:getAbilityList:0|I@pokemon:ability_index=:0|I@pokemon:ability_id:0|I@pokemon:hasHiddenAbility?:0|O@effects:ABILITYPATCH|O@itemutil:pbUseItemOnPokemon|O@item:consumed_after_use?'
Cc('R5U03-M04-001-01',patch,'人工三自然列表枚举索引0/1/2，隐藏空。','Patch最后匹配2是TORRENT，严格取消息身份后写index2并清值cache。','实际getter把>=2当hidden，缺hidden退PID偶数0得到OVERGROW；隐藏判定仍true。','正常effect/outer为true并消费唯一Patch，后读可填cache。')
Cc('R5U03-M04-001-02',patch,'仅两自然时没有index2候选。','Patch false，索引保持、正常outer不消费库存1。')
Cc('R5U03-M04-001-03',patch,'三自然的TORRENT2后还有首隐藏BLAZE2，两枚举都保。','Patch遍历最后匹配BLAZE用于消息。','写2后实际hidden0 BLAZE，正常成功消费。')
Cc('R5U03-M04-001-04','O@debug:SET_ABILITY|I@pokemon:getAbilityList:0|I@pokemon:ability_id:0|I@pokemon:ability_index=:0','Debug第三自然TORRENT2以H标签显示。','选中只写index2/清cache，不强制写TORRENT。','偶数PID下实际OVERGROW/hidden true；取消菜单没有此写。')
Cc('R5U03-M04-001-05',patch,'拒确认直接false。','已index>=2或ZYGARDE门拒，不因第三候选绕过。','仅编号3没有2也拒；各false正常outer不消费。')
Cc('R5U03-M04-001-06',patch,'直接记录人工第三身份未登记不冒有效文本编译成功。','确认后严格GameData Ability取消息身份先失败。','index写点未到，保原索引/未消费，不保证正常返回。')
hoopa='D@effects:PRISONBOTTLE|H@C21-REG-HOOPA|S@pokemon:setForm:0|I@pokemon:form:0|I@pokemon:form=:0|O@party:ITEM_MENU|O@party:ITEM_USE_MENU|O@party:Scene_pbUseItem|O@party:Screen_pbRefresh|O@party:Scene_pbRefresh|O@party:Panel_pokemon=|O@icons:Icon_pokemon=|S@speciesfiles:self.icon_filename_from_pokemon:0|O@itemutil:pbUseItemOnPokemon|O@party:Screen_pbHardRefresh|O@party:Scene_pbHardRefresh|O@party:Panel_initialize|O@item:consumed_after_use?'
Cc('R5U03-M04-002-01',ifs,'默认FURFROU摘要个体精灵请求会先读动态form。','期限后先提交0/清时间/重算条件Dex再查资源；不认证最终像素/cache空。')
Cc('R5U03-M04-002-02',ifs,'恰边界保1，战斗与仓库各保stored1。','forced0只返0，不改stored1/time；显式提交是另入口。')
Cc('R5U03-M04-002-03',hoopa,'正常Party Item→Use，Hoopa0/time nil初读候选0等stored，不提交。','setForm请求1先写stored1/ability nil，yield回调pbRefresh在onSetForm写时间之前。','现有Panel给同pokemon，Icon重新按个体取filename动态读，因时间nil而内层form=0，清时间/重算/Dex。','外层继续原请求1的onSetForm，写新时间但不恢复stored1；随后重算/Dex实际0。','effect真，外层clearAnnotations/hardRefresh和最终单刷新正常；新时间内不再回退，最终0/新时间/瓶子1，KeyItem不消费。')
Cc('R5U03-M04-002-04',hoopa,'已有新鲜时间时回调动态读不返回0，保持请求1。','外层onSet刷新时间，最终1/新时间，瓶子仍1且成功。')
Cc('R5U03-M04-002-05',hoopa,'第一次03结果0/新时间后第二次请求1，回调因时间新鲜不内降，得1/新时间。','再请求0先stored0，onSet清time；每次KeyItem保1。','不能把初次空时间内降推广每次失败。')
Cc('R5U03-M04-002-06','H@C21-REG-HOOPA|I@pokemon:form=:0','直接普通form=1无中途yield动态读。','onSet写新时间，正常最终1；此裸入口不替代普通Party回调主链，同值提交规则保持。')
Cc('R5U03-M04-002-07',ifs,'动态提交成功后匹配资源失败不回滚form/time。','宿主异常呈现和最终UI/返回未知，无素材执行。')
assert len(claims)==29
formal='deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md';fr=(B/formal).read_bytes();fl=fr.decode().splitlines();rows={}
for i,l in enumerate(fl,1):
 m=re.match(r'\| ((?:R4-IF\d+|U03-SP\d+|R5U03-[^ |]+)) \|',l)
 if m:rows[m[1]]=(i,l)
assert set(rows)==set(claims);records=[]
for v,ss in claims.items():
 line,row=rows[v];records.append(dict(id='DIC-'+v,vector=v,formal=dict(path=formal,line=line,complete_raw_row=row),premise='完整原行及本包逐段保存的共同前提；每行独立重置，人工三自然/默认Hoopa或Furfrou/PNG与native不同条件分别保留。前序资源与消息正常至明确观察点，不授实际像素/宿主/素材结果。',complete_source_unit_refs=refs[v],child_assertions=[dict(id=f'DIC-{v}-A{i:02}',meaning=s,complete_source_unit_refs=refs[v],status='MANUALLY_JOINED_BOUNDED_STATIC',whole_parent_acceptance=False) for i,s in enumerate(ss,1)],normal_cancel_failure='Patch先确认/取合法消息身份，后写index/cache，再refresh/display，outer后消费；取消/资格拒无该写，后失败保前缀。Hoopa外层stored先于yield、内动态提交先于外onSet与后calc/Dex；正常刷新不回滚。资源缺失/native未知不造成功输出。',receiver_and_persistence='Source definitions/handlers→实际Party/Debug/按个体sprite或低层显式资源入口→持久form/time/ability_index与cache或位图副本。SP纯色数学不修改PID；宿主帧内部/实际save-reload未执行。',remaining=['有限原向量已逐意义拆；未授全WP28/Debug/UI/PBS/素材或整体C PASS。'],accepted=False))
for u in units:
 ls=(R/ident[u['source_identity_key']]['path']).read_text(encoding='utf-8-sig').splitlines(keepends=True);lo,hi=u['range'];assert ''.join(ls[lo-1:hi]).rstrip('\n')==u['text'].rstrip('\n')
out=dict(schema='gr8-crec-display-item29/v1',recorded_utc=utc,actual_reader=reader,formal_identity=dict(path=formal,bytes=len(fr),sha256=hashlib.sha256(fr).hexdigest(),current_complete_context_read='dee2a5'),complete_original_common_premises=[dict(line=i+1,text=l) for i,l in enumerate(fl) if l.startswith('共同前提：合法非蛋FURFROU') or l.startswith('共同前提：合法非蛋 SPINDA') or l.startswith('全部为 DERIVED_VECTOR')],source_identities=ident,complete_source_units=units,mandatory_complete_source_packet_bindings=bindings,complete_raw_records=raws,records=records,manual_atoms=sum(len(x['child_assertions']) for x in records),actual_current_source_rereads=['f7fd48','6137a3','655378','103a11','325965','b19d5e','95363a','a164c0','793b85'],whole_PBS_credit=False,new_contexts=0,new_votes=0,denominator_frozen=False,whole_domain_acceptance=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
p=C/'display-item-catalog29-meaning.v1.json';assert not p.exists();write(p,out);rv=read(C/'reverse-mapping.json');assert not any(x['id'].startswith('DIC-') for x in rv['records']);rv['records'].extend(records);rv['utc']=utc;write(C/'reverse-mapping.json',rv);pr=read(C/'progress.json');pr['updated_utc']=utc;pr['primary_clause_atoms']=sum(len(x.get('child_assertions',[])) for x in rv['records']);write(C/'progress.json',pr);print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),groups=29,children=out['manual_atoms'],total_groups=len(rv['records']),total_children=pr['primary_clause_atoms'],source_units=len(units),utc=utc)))
