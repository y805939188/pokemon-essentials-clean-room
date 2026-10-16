import json,re,hashlib,datetime,subprocess
from pathlib import Path
C=Path(__file__).parent;R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception';commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def rd(p):return json.loads(p.read_text())
def wr(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
gpath=C/'wp30-compound-meaning.v1.json';graw=gpath.read_bytes();g=json.loads(graw);ident={};units=[];raws=[]
def source(k,path):
 raw=(R/path).read_bytes();assert raw==subprocess.check_output(['git','-C',str(R),'show',commit+':'+path]);ident[k]=dict(path=path,commit=commit,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),git_blob=subprocess.check_output(['git','-C',str(R),'rev-parse',commit+':'+path],text=True).strip(),actual_reader=reader,credit='Own actual complete named units; independent sourceFULL ledger separate.');return raw.decode('utf-8-sig').splitlines(keepends=True)
def met(k,ls,n,after=0):
 i=next(i for i,l in enumerate(ls) if i>=after and re.match(r'\s*def\s+'+re.escape(n)+r'(?=[\s(;]|$)',l));indent=re.match(r'\s*',ls[i]).group();j=i if re.search(r';\s*end\s*$',ls[i]) else next(j for j in range(i+1,len(ls)) if re.match(r'^'+re.escape(indent)+r'end\s*(?:#.*)?$',ls[j]));units.append(dict(id=k+':'+n,source_identity_key=k,range=[i+1,j+1],text=''.join(ls[i:j+1]),complete_definition=True))
ls=source('utility','Data/Scripts/019_Utilities/001_Utilities.rb')
for n in ['pbMoveTutorAnnotations','pbMoveTutorChoose','pbSet']:met('utility',ls,n)
ls=source('effects','Data/Scripts/013_Items/002_Item_Effects.rb');i=next(i for i,l in enumerate(ls) if l.startswith('ItemHandlers::UseFromBag.addIf(:move_machines'));j=next(j for j in range(i+1,len(ls)) if ls[j].strip()==')');units.append(dict(id='effects:BAG_MACHINES',source_identity_key='effects',range=[i+1,j+1],text=''.join(ls[i:j+1]),complete_registration=True))
ls=source('items','Data/Scripts/013_Items/001_Item_Utilities.rb')
for n in ['pbUseItem','pbUseItemOnPokemon','self.triggerUseFromBag']:met('items',ls,n)
ls=source('pokemon','Data/Scripts/014_Pokemon/001_Pokemon.rb')
for n in ['add_first_move','compatible_with_move?','able?','egg?']:met('pokemon',ls,n)
ls=source('party','Data/Scripts/016_UI/005_UI_Party.rb');met('party',ls,'pbChooseAblePokemon',1100)
for n in ['pbChoosePokemon','pbChooseNonEggPokemon','pbChooseAblePokemon']:
 i=next(i for i,l in enumerate(ls) if re.match(r'^def '+re.escape(n)+r'\(',l));j=next(j for j in range(i+1,len(ls)) if ls[j].strip()=='end' and not ls[j].startswith(' '));units.append(dict(id='event:'+n,source_identity_key='party',range=[i+1,j+1],text=''.join(ls[i:j+1]),complete_definition=True))
ls=source('itemdata','Data/Scripts/010_Data/002_PBS data/006_Item.rb')
for n in ['is_TR?','consumed_after_use?']:met('itemdata',ls,n)
for k,path,names in [('rawitems','PBS/items.txt',['TM57']),('rawbase','PBS/pokemon.txt',['MAGNEMITE','CATERPIE','MAGIKARP']),('rawmoves','PBS/moves.txt',['CHARGEBEAM','AMNESIA'])]:
 ls=source(k,path)
 for n in names:
  i=next(i for i,l in enumerate(ls) if l.strip()=='['+n+']');j=next((j for j in range(i+1,len(ls)) if ls[j].lstrip().startswith('[')),len(ls));raws.append(dict(id=k+':'+n,source_identity_key=k,range=[i+1,j],text=''.join(ls[i:j]),complete_raw_record=True))
records=[]
def add(label,assertions,ids):
 records.append(dict(id='WLC-'+label,premise='固定B8/R；完整WP30对应原文及具名普通非蛋非Shadow/有效default或指定fixture保留；前序data/UI/media/确认正常至所述点。没有执行游戏/目标代码/native或实际事件。',child_assertions=[dict(id=f'WLC-{label}-A{i:02}',meaning=s,complete_source_unit_ids=ids,status='MANUALLY_JOINED_BOUNDED_STATIC',whole_parent_acceptance=False) for i,s in enumerate(assertions,1)],normal_cancel_failure='前门与返回0/false、拒教学/选槽/退出分别保留；先Move学习与统计/first_moves再SceneEnd，再外层消费。后失败保实际前缀，不保证原子交易/回滚。',remaining=['非整体WP30/物品/队伍UI/事件调用全穷尽；sourcecredit保实际reader。'],accepted=False))
add('BAG_TR_ACTUAL_WRITER',[
'旧CGR-R014-A04的BagTR first_moves断言本身正确，但只给items:pbUseItem/OnPokemon不能定位实际append写入者；本包是其强制准确caller/sourceunit补件，旧对象原字节保留。',
'Bag pbUseItem对machine走triggerUseFromBag；move_machines addIf先machine条件，再pokemon_count/move/确认守卫，传bymachine=true及oneusemachine=item.is_TR?给pbMoveTutorChoose。',
'pbMoveTutorChoose逐成员拒蛋/Shadow/不兼容，pbLearnMove成功后才先moves_taught_by_item统计，再oneusemachine时add_first_move，之后ret真/结束Scene。',
'add_first_move只try_get有效身份且原first_moves不含才append，因此按身份去重；列表是原个体容器，没有从物种全egg_moves复制。',
'普通TM/HM的oneusemachine=false不append；TR=true才append，不由文件名TM数字推断类别。',
'pbUseItemOnPokemon机器分支直接pbLearnMove/可消费后true，没有pbMoveTutorChoose的TR append/统计写点；Party与Bag不同。'],['items:pbUseItem','items:self.triggerUseFromBag','effects:BAG_MACHINES','utility:pbMoveTutorChoose','pokemon:add_first_move','items:pbUseItemOnPokemon','itemdata:is_TR?'])
add('TM57_DEFAULT_RECEIVERS',[
'TM57完整原记录FieldUse=TR/Move=CHARGEBEAM，不因名字TM57当作普通TM；CHARGEBEAM原PP10。',
'MAGNEMITE原tutor含CHARGEBEAM，L<=5等级表没有它；合法L5仅TACKLE/first[TACKLE]/有空槽可教。',
'两入口正常都学新Move并消耗1；Bag的first[TACKLE,CHARGEBEAM]，Party保持[TACKLE]。',
'后遗忘CHARGEBEAM且额外重学开启，仅Bag留下记录可使其前置；不得把当前level无该招误推为两入口皆不可重学。'],['pokemon:compatible_with_move?','utility:pbMoveTutorChoose','pokemon:add_first_move','items:pbUseItem','items:pbUseItemOnPokemon'])
add('EMPTY_RELEARN_DEFAULTS',[
'BULBASAUR0 L5会TACKLE/GROWL/VINEWHIP且first空时，level候选空；物种EggMoves AMNESIA不能自动补入。',
'first[AMNESIA]×额外开/关和first空×开/关四组，只有first有且开时得AMNESIA，其余空。BULBASAUR完整raw沿stat-catalog67已有ownread记录，AMNESIA本包完整raw。',
'CATERPIE L1会TACKLE/STRINGSHOT、MAGIKARP L1会SPLASH且first空，分别level无未会候选。',
'这些是领域空结果，不保证安全UI；直接Relearn首次draw严格身份取nil失败早于输入与提醒统计，调用者预检则不进入。'],['pokemon:compatible_with_move?'])
add('EVENT_SELECTOR_PREDICATES',[
'top pbChooseAblePokemon传!egg?&&hp>0，非蛋与正HP同时要求；仅蛋队伍没有合格成员。',
'top pbChooseNonEggPokemon只传!egg?，因此非蛋濒死仍合格，不可与Able互换。',
'Screen逐成员预计算eligibility/ABLE注解；选不合格且allowIneligible=false只提示并继续，BACK负索引才结束。',
'top wrapper退出后pbSet选择变量，chosen<0时名称写空串；正常选择才取party.name。',
'pbSet对nil/负变量号早返，存在game_variables才赋值，存在game_map请求refresh；合法变量fixture正常写-1/空名。',
'没有证明demo事件接待实际调用/可达；纯domain选择能力与通用教学/重学蛋Shadow门各自保持。'],['party:pbChooseAblePokemon','event:pbChoosePokemon','event:pbChooseNonEggPokemon','event:pbChooseAblePokemon','utility:pbSet','pokemon:able?','pokemon:egg?'])
uids={u['id'] for u in units};assert all(x in uids for z in records for a in z['child_assertions'] for x in a['complete_source_unit_ids'])
formal='deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md';fr=(B/formal).read_bytes();out=dict(schema='gr8-crec-wp30-learning-consumers/v1',recorded_utc=utc,actual_reader=reader,formal=dict(path=formal,bytes=len(fr),sha256=hashlib.sha256(fr).hexdigest(),actual_whole_reread_chunks=['12f6a0','d0fc48']),source_identities=ident,complete_source_units=units,complete_raw_records=raws,mandatory_existing_relearner_packet=dict(path=gpath.name,bytes=len(graw),sha256=hashlib.sha256(graw).hexdigest(),required_complete_objects=['CGR-R014','CGR-R015'],required_whole_units=['relearn:pbGetRelearnableMoves','relearn:pbStartScreen','relearn:pbStartScene','relearn:pbDrawMoveList','items:pbLearnMove'],meaning='Original source-specific reader retained. This new packet corrects only missing actual BagTR caller/writer link; no oldclaim/newformalcase invented.'),mandatory_bulbasaur_raw_packet='stat-catalog67-meaning.v1.json /complete_raw_records base:BULBASAUR; complete original commonpremises preserved there.',records=records,manual_atoms=sum(len(x['child_assertions']) for x in records),existing_binding_correction=dict(old_id='CGR-R014-A04',old_complete_record=next(x for x in g['records'] if x['id']=='CGR-R014'),scope='Mandatory whenever adopting that exact BagTR assertion. CGR-R001/R006 CORE earlier limitedreception unaffected; no invented credit for its unreceivedR014.'),actual_current_source_reads=['61b52d','4aac91','0a918b','b1e955','6ba696','b0f4f2'],whole_PBS_credit=False,new_contexts=0,new_votes=0,denominator_frozen=False,whole_domain_acceptance=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
p=C/'wp30-learning-consumers-and-binding.v1.json';assert not p.exists();wr(p,out);rv=rd(C/'reverse-mapping.json');assert not any(x['id'].startswith('WLC-') for x in rv['records']);rv['records'].extend(records);rv['utc']=utc;wr(C/'reverse-mapping.json',rv);pr=rd(C/'progress.json');pr['updated_utc']=utc;pr['primary_clause_atoms']=sum(len(x.get('child_assertions',[])) for x in rv['records']);wr(C/'progress.json',pr);print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),groups=len(records),children=out['manual_atoms'],source_units=len(units),total_groups=len(rv['records']),total_children=pr['primary_clause_atoms'],utc=utc)))
