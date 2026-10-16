import json,hashlib,datetime,re,subprocess
from pathlib import Path
C=Path(__file__).parent; Base=C.parent.parent; R=Path('/workspace/pokemon-essentials'); B=Path('/workspace/pokemon-essentials-clean-room'); reader='/root/creature_a_atomic_reception'; utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=Base/'delegation/external-battler-finite-provider-reception-input.v1.json'; raw=p.read_bytes(); d=json.loads(raw); assert len(raw)==36783 and hashlib.sha256(raw).hexdigest()=='19dba14539d33874a7c49fe2275d03d1966d39ad121943e44f59fe40e19f866d'
ids=d['finite_reception_assignments']['CREA']; facts=[x for x in d['full_consumer_facts'] if x['id'] in ids]; assert len(facts)==5
parents=[x for x in d['exact_source_parent_identities'] if x['evidence_id'] in {x['source']['evidence_id'] for x in facts}]; assert len(parents)==5
sp=C/'received/battler-five-complete-19dba145.json'; assert not sp.exists()
write(sp,dict(parent=dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()),complete_common_envelope={k:v for k,v in d.items() if k not in ['full_consumer_facts','exact_source_parent_identities']},complete_selected_facts=facts,necessary_parent_identities=parents,actual_read_chunks=['fb2bd9','914276'],not_received_other_facts=19))
ident={}; units=[]; commit=d['fixed_R']
def source(k,path,whole=False):
 r=(R/path).read_bytes(); assert r==subprocess.check_output(['git','-C',str(R),'show',commit+':'+path]); ident[k]=dict(path=path,commit=commit,bytes=len(r),sha256=hashlib.sha256(r).hexdigest(),git_blob=subprocess.check_output(['git','-C',str(R),'rev-parse',commit+':'+path],text=True).strip(),actual_reader=reader,scope='Own complete necessary units only; own prior sourceFULL separately retained, no credit transfer.'); ls=r.decode('utf-8-sig').splitlines(keepends=True)
 if whole: units.append(dict(id=k+':WHOLE',source=k,range=[1,len(ls)],text=''.join(ls),complete_definition=True))
 return ls
def method(k,ls,n):
 i=next(i for i,l in enumerate(ls) if re.match(r'\s*def\s+'+re.escape(n)+r'(?=[\s(;]|$)',l)); indent=re.match(r'\s*',ls[i]).group(); j=i if re.search(r';\s*end\s*$',ls[i]) else next(j for j in range(i+1,len(ls)) if re.match(r'^'+re.escape(indent)+r'end\s*(?:#.*)?$',ls[j])); units.append(dict(id=k+':'+n,source=k,range=[i+1,j+1],text=''.join(ls[i:j+1]),complete_definition=True))
ls=source('pokemon','Data/Scripts/014_Pokemon/001_Pokemon.rb')
for n in ['level=','form','form=','hp=','status=','able?','egg?','heal_status','item=','calc_stats']: method('pokemon',ls,n)
source('persistentmove','Data/Scripts/014_Pokemon/004_Pokemon_Move.rb',True)
ls=source('shadow','Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb'); units.append(dict(id='shadow:HP_ALIAS_AND_METHOD',source='shadow',range=[22,26],text=''.join(ls[21:26]),complete_definition_and_alias=True))
for n in ['hyper_mode','shadowPokemon?']: method('shadow',ls,n)
ls=source('other','Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb'); units.append(dict(id='other:BATTLER_OVERRIDE_CLASS',source='other',range=[183,221],text=''.join(ls[182:221]),complete_class=True))
source('peer','Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb',True)
ls=source('battler','Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb')
for n in ['level=','form=','hp=','status=','statusCount=','item=']: method('battler',ls,n)
ls=source('init','Data/Scripts/011_Battle/002_Battler/002_Battler_Initialize.rb'); method('init',ls,'pbInitPokemon')
ls=source('change','Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb'); method('change',ls,'pbSetPP')
ls=source('main','Data/Scripts/011_Battle/001_Battle/001_Battle.rb'); method('main',ls,'initialize'); method('main',ls,'pbRandom')
ls=source('battlemove','Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb'); method('battlemove',ls,'initialize'); method('battlemove',ls,'total_pp'); units.append(dict(id='battlemove:PP_ATTRIBUTES',source='battlemove',range=[1,12],text=''.join(ls[:12]),complete_declarations=True))
for x in parents: assert ident[{'E170':'pokemon','E174':'shadow','E177':'persistentmove','E025':'other','E078':'peer'}[x['evidence_id']]]['sha256']==x['sha256']
joins=[]
def J(id,uu,meaning,qualifications,remaining): joins.append(dict(id=id,disposition='ACCEPTED_BOUNDED_WITH_EXPLICIT_QUALIFICATIONS',complete_source_unit_ids=uu,complete_meanings=meaning,qualifications=qualifications,remaining=remaining))
J('RX-POKEMON-SET',['battler:level=','battler:hp=','battler:status=','battler:statusCount=','battler:item=','battler:form=','pokemon:level=','pokemon:hp=','pokemon:heal_status','pokemon:status=','pokemon:able?','pokemon:egg?','pokemon:item=','pokemon:form=','pokemon:calc_stats'],[
 'Battler.level=先写local，再由persistent level=检验1..max；越界时local已写而persistent exp/level未写。成功persistent先求最小EXP，再exp与level提交。',
 'Battler.hp=先写to_i局部，再请求persistent夹0..totalhp；局部值不由persistent夹限回读。persistent零HP请求heal_status并清ready_to_evolve。',
 'Persistent status=先拒不可用，再try_get/报错/提交；Battler先改Truant/Toxic/local status，persistent拒绝或失败不回滚前缀，后续计数与scene仅到达才执行。',
 'Persistent item=忽略未知truthy身份；Battler先try_get归nil并写local/persistent nil，所以同一未知输入可清持物。',
 'form=先stored/ability值nil，再handler、calc、条件Dex；同值没有短路。calc先改totalhp，再正HP或正差量门调整HP，随后五能力。异常保已到前缀。'
],['HP零对蛋heal_status早返，蛋旧status/count保留，但ready_to_evolve仍清。','form=只清@ability值，不清@ability_index/forced_form；不得把cache泛词扩成索引清零。'],['Native UI/实际save-reload未执行；非全Battler/CREA验收。'])
J('RX-POKEMON-PP',['persistentmove:WHOLE','battlemove:PP_ATTRIBUTES','battlemove:initialize','battlemove:total_pp','change:pbSetPP'],[
 'Persistent pp=夹0..total_pp；total由基础PP+基础×ppup整除5，计数非法使负上限时可失败。','Battle::Move的@pp是独立普通accessor，构造复制realMove.pp而非共享标量。','pbSetPP先写BattleMove.pp，再仅realMove存在/ID仍同/非Transform时经persistent pp=写回。','错ID或Transform保持persistent PP；persistent失败保local PP前缀。'
],['Matching realMove对象引用不表示PP字段天然共享；必须到专门同步入口。'],['不授全部com_move效果/调用穷尽。'])
J('RX-SHADOW-HP',['shadow:HP_ALIAS_AND_METHOD','pokemon:hp=','pokemon:heal_status','pokemon:egg?'],[
 '加载的guarded alias保存普通persistent hp=；wrapper先调用该入口，之后结果@hp<=0才raw hyper_mode=false。','普通setter失败则后清Hyper未到；蛋状态清除守卫与该wrapper互相独立。'
],['Loaded固定默认alias顺序；不由此证明插件重复定义/任意重载相同。'],['可选Shadow内容安装与host运行未执行。'])
J('RX-SHADOW-BATTLER',['other:BATTLER_OVERRIDE_CLASS','shadow:hyper_mode','shadow:shadowPokemon?','init:pbInitPokemon','main:pbRandom'],[
 '旧pokemonIndex>0且inHyperMode?才在base init前清旧raw Hyper；slot0、fainted或有效G0不由此清。','base init先拒蛋，再逐字段复制，后绑定@pokemon/index并构造BattleMoves；失败保此前旧Hyper清除与已到局部复制。','base成功后Shadow仅在SHADOW类型存在时改场上单类型，再仅玩家本人席位执行battle心量表下降；不刷新场上招式。','Hyper进入先守未濒死/Shadow/非有效Hyper/本人席位，再battle.pbRandom(G)<=M/4，先raw Hyper真再display。','obedience非Hyper/无move/SHADOW type直接true，其余直接bare rand(100)<20。'
],['默认Battle.pbRandom是bare Kernel rand委派，不是Random#rand；obedience不经过Battle.pbRandom覆盖。','旧清除读的是有效Hyper query，不能写成所有旧raw flag恒清。'],['Recorded/custom RNG、宿主具体抽样与全初始化effects链不在本有限接收。'])
J('RX-PEER',['peer:WHOLE','main:initialize','pokemon:form','pokemon:form=','pokemon:hp='],[
 'Battle constructor非空队伍守卫后设置Peer.new；NullPeer为不同未用类，默认不选择它。','Normal leaving先拒nil Pokemon，求getFormOnLeavingBattle；truthy候选且与有效form不同才persistent提交，0在Ruby中truthy。','随后仅HP>totalhp才clip，再调用changePokemonOnLeavingBattle；动态getter/handler/setter各自可能已改状态，无回滚。','该方法不通用解除Mega/Primal或所有capture/termination状态；starting/entering与各caller职责独立。','NullPeer entering/leaving空方法，store只在partyspace时append并返回-1，不替换默认Peer行为。'
],['完整Peer定义接收含正常/Null区别；不以一种Peer推另一种默认效果。'],['所有动态注册handler、完整终战/捕获语义仍由独立包限定。'])
assert {x['id'] for x in joins}==set(ids); assert all(u in {z['id'] for z in units} for j in joins for u in j['complete_source_unit_ids'])
forms=[]
for path in ['creature-rpg/wp20-hp-status-moves-helditem.md','pokemon-rules/wp19-attributes-ability-and-stats.md','pokemon-rules/wp21-dynamic-forms-and-display.md','pokemon-rules/wp22-mega-and-primal-reversion.md','pokemon-rules/wp23-shadow-hyper-and-purification.md']:
 path='deliverables/final-specification-set/'+path; r=(B/path).read_bytes(); forms.append(dict(path=path,commit=d['fixed_B8'],bytes=len(r),sha256=hashlib.sha256(r).hexdigest(),actual_reader=reader,credit='Own prior actual wholeformal read reused, no new independent review.'))
out=dict(schema='gr8-crec-battler-finite-reception/v1',recorded_utc=utc,receiver=reader,external_original_reader=d['source_actual_reader'],input=dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),selected_complete_fact_ids=ids,actual_read_chunks=['fb2bd9','914276']),frozen_selected_input=dict(path=str(sp.relative_to(C)),bytes=sp.stat().st_size,sha256=hashlib.sha256(sp.read_bytes()).hexdigest()),common_premises='固定B8/R，默认类加载且无插件，合法接收器及前序数据/资源/消息正常至所述观察点。普通/蛋/Shadow、场上/持久层分列。每写点为顺序能力，非原子事务。',source_identities=ident,complete_necessary_source_units=units,current_source_reread_chunks=['3764c0','68fcbe','3df31f'],current_formal_identities=forms,finite_joins=joins,source_identity_checks='Five exact parent identities plus all own necessary units fixedGit match; mechanical checks add zero semantic reading credit.',formal_new_finding=False,original_provider_objects_preserved=True,not_received='Other19facts/810atoms/fullBattler10/global scope acceptance not inferred.',new_contexts=0,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
op=C/'battler-finite-reception.v1.json'; assert not op.exists(); write(op,out); print(json.dumps(dict(path=op.name,bytes=op.stat().st_size,sha256=hashlib.sha256(op.read_bytes()).hexdigest(),complete_facts=5,complete_necessary_units=len(units),utc=utc)))
