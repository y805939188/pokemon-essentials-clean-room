import json,hashlib,datetime,re
from pathlib import Path
C=Path(__file__).parent;B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception'
names={'D':'default-transformation-records.v1.json','B':'battle-consumer-delta.v1.json','M':'mega-menu-entry-consumers.v1.json','V':'form-mega-catalog69-meaning.v1.json','W':'wp22-flags-ai-bug-consumers.v1.json','O':'wp22-item-removal-config-bindings.v1.json'};packs={};bind={}
for k,n in names.items():
 raw=(C/n).read_bytes();d=json.loads(raw);packs[k]={x['id']:x for x in d['records']};bind[k]=dict(path=n,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader)
groups=[]
def refs(s):
 ret=[]
 for z in s.split('|'):
  k,id=z.split('@',1);assert id in packs[k],z;x=packs[k][id];ret.append(dict(package=names[k],complete_record_id=id,complete_existing_atom_ids=[a['id'] for a in x['child_assertions']]))
 return ret
def group(id,file,lo,hi,status,rr,meaning):groups.append(dict(id='WP22-PG-'+id,file=file,range=[lo,hi],disposition=status,complete_existing_manual_records=refs(rr) if rr else [],manual_semantic_scope=meaning))
S='MANUALLY_JOINED_BOUNDED_STATIC'
group('01','main',1,3,'TYPED_PURPOSE_AND_STATIC_SCOPE',None,'标题、所属领域、静态证据与无运行确认；不当运行结果或全域验收。')
group('02','main',7,7,S,'M@CME-R002|M@CME-R003|M@CME-R004|M@CME-R005|B@CBC-R012|B@CBC-R013','菜单→登记→招式目标→普通攻击执行与Primal入场尝试区分；取消待执行不消费、成功形态/owner已用/当前个体身份三个不同状态。')
group('03','main',9,9,'TYPED_DEPENDENCY_AND_TERM_BOUNDARY',None,'动作、业主、换人引用真正责任；一般进化/动态形态/能力族/捕获算法非本篇重审。Primal Reversion进入与解除术语已分。')
group('04','main',15,15,S,'D@CTF-R001|D@CTF-R004|B@CBC-R012','同基础物种、简化形态、数据要求、执行前重读目标；无匹配0而不是所有坏输入均0。')
group('05','main',16,16,S,'D@CTF-R001|D@CTF-R006|W@WMB-R002','持久item与已知招ID资格，不用战斗临时招式，不需PP/不消费各资源；owner ring实时资源是另一读者。')
group('06','main',17,17,S,'B@CBC-R011|M@CME-R001|M@CME-R004','战斗seat/side/currentowner/wild/Transform/SkyDrop先后门，不把个人OwnerID当战斗业主。')
group('07','main',18,18,S,'W@WMB-R001|W@WMB-R002|O@WMR-R003','禁止开关index34非当前值；构造目录快照vs许可时liveBag/owneritems；唯一currentraw环与registry成功load前提明列。')
group('08','main',19,19,S,'B@CBC-R011|B@CBC-R012|M@CME-R002|M@CME-R003','每侧每训练家-1/seat/-2；初始化、写pending、matching撤销、完成才used；非持久个体字段。')
group('09','main',20,20,S,'D@CTF-R006|D@CTF-R007|B@CBC-R013','Primal每次读handler/held/stored，身份随物变化，无Mega共享次数；不把当前forced简化form当stored。')
group('10','main',21,23,S,'D@CTF-R001|D@CTF-R004|D@CTF-R006|B@CBC-R012|B@CBC-R013|O@WMR-R002','持久→战斗数值类型能力→scene→条件globalDex接合；实际itemActive过滤与裸个体持物分层，MagicRoom/Embargo/Klutz不直接删item；蛋/faint门各caller，不能补到裸接口。')
group('11','main',27,27,S,'D@CTF-R001|D@CTF-R002|V@CFM-ME02|V@CFM-ME03|V@CFM-ME04|V@CFM-ME05','数据顺序首匹配：基础species及unmega==form_simple先过滤，石或招为OR，target>0且不同才has；48/46/47+1、Slowbro目标2/来源0精确默认输入。')
group('12','main',29,29,S,'D@CTF-R003|V@CFM-ME06','当前数据stone或move定义Mega身份，不需当前还持有/会招；非Mega还原-1，makeMega>0/makeUnmega>=0只提交，不具备ring/quota/stat/scene同步。')
group('13','main',31,31,S,'D@CTF-R002|D@CTF-R005|D@CTF-R008|V@CFM-ME26','Banette0无forced有效数据+BANETTITE→1/has，none或wrong→0；有效物品身份和战斗许可不混，48表与Meta原HP95保。')
group('14','main',33,33,S,'D@CTF-R001|D@CTF-R004','查询目标不直接写形态；form_simple forced||stored与完整form getter不同；fallbackbase/unknownnil解引用分开；变形不清forced，所以正常模型存储提交可被锁掩盖。')
group('15','main',35,35,S,'O@WMR-R003|W@WMB-R001|W@WMB-R002|D@CTF-R001','generation8/afterMega>=7true/index34而非当前开关；个体许可无>=6统一门；47stoneflag非target必要条件；whole当前trainers20记录无这50ID只支持样本检索，不给demo不可获得结论。')
group('16','main',43,44,S,'B@CBC-R011|W@WMB-R002|V@CFM-ME08|V@CFM-ME09|V@CFM-ME25','Battler先Transform拒绝，正常CanMega先禁止/has/wild后DebugCtrl直通，再SkyDrop/ring/owner==-1；无额外Shadow门，Debug不能越前段。')
group('17','main',45,46,S,'M@CME-R001|M@CME-R002|M@CME-R003','正常commands/fight/Encore/无move/PalaceAuto门与按钮参数有限；裸register/toggle仅owner索引写/撤，不重查permission、不护重复/非法输入。')
group('18','main',47,48,S,'M@CME-R004|B@CBC-R012','普通攻击非wild/nonfaint/UseMove/exactownerpending；Pursuit可在switch提前；executor只exists/pokemon/currenttarget/notmega，不能补全部菜单门。')
group('19','main',50,50,S,'B@CBC-R011|W@WMB-R002|V@CFM-ME07','当前战斗owner0Bag、partner/foe各items/quota，原Owner外来不决定；同owner共一次/同侧不同owner各一次。')
group('20','main',54,54,S,'M@CME-R002|M@CME-R003|M@CME-R006|V@CFM-ME11|V@CFM-ME12|V@CFM-ME13','pending正常toggle/wholecancel/Shift/nextphase清，-2不清；matching撤销不refund；invalidmove/targetretry不清，wholeexit才外层清；执行资格丢失不used，普通换下再入仍Mega且quota已用。')
group('21','main',58,58,S,'B@CBC-R012|D@CTF-R003|W@WMB-R002','playerowned先stat再oldability/Illusion/messages、数据message1或普通ring响应；fallbackringname只显示非授权；formname优先/缺省Mega+species，非硬编码Ray消息分派。')
group('22','main',60,60,S,'B@CBC-R012|V@CFM-ME15|V@CFM-ME16','persistentcommit→Battlerform→Update(true)→scene→used，Gengar已Mega清Telekinesis，失旧/得新ability及optionalpriority随后；早退无这些写，中途故障保统计/形态prefix。')
group('23','main',62,62,S,'D@CTF-R004|B@CBC-R012|B@CBC-R013|V@CFM-ME16','form=清ability值不清index、onSet/calc/conditionalDex；model后Battler同值再提交，Update又calc；无专门move重置/PP回满/清全stages effects，图鉴登记不由包装internal统一拦。')
group('24','main',64,64,S,'D@CTF-R008|M@CME-R007|V@CFM-ME14','Meta80→95独立50Lv IVEV0 total140→155 current70→85→70，低HP5解除floor1；lossHP差不是比例。Faintundo只persistent不整Battlerrefresh；默认HP不增与自定义分开。')
group('25','main',68,68,S,'D@CTF-R006|D@CTF-R007|V@CFM-ME19|V@CFM-ME21','handler返回非nil即presence；defaultorbs→1，identityreturned==stored；移orb使identityfalse但stored1可留，区别Mega按当前数据身份。false/0变体不是默认数据。')
group('26','main',70,72,S,'B@CBC-R013|M@CME-R005|V@CFM-ME19|V@CFM-ME20','速度entry位置heal/伤害/FaintEXPJudge后CheckForm→Primal→continualability/switchinability；无ring/switch/wild/quota/stat门；model→battle→fullupdate/scene/两anim/msg重复提交，executor无Megaability/sort不等于entry无ability天气。')
group('27','main',74,74,S,'D@CTF-R007|O@WMR-R001','专用undo非nil优先，否则当前primal才0；whole792未注册专用undo两default进入；noorbidentityfalse所以bareundo不0；普通unlosable经真实species/Transform门区别直接remove，0变体非nilcapability不伪装默认。')
group('28','main',80,81,S,'M@CME-R006|M@CME-R007|D@CTF-R008','普通withdrawability→Peerclamp→localHP0/faintedweather无persistentHP0/unmega；真正Faint按各门清状态/Peer→unmega→unprimal→choices/achievement，persistent变化而副本未fullupdate，不靠默认HP解除复活。')
group('29','main',82,83,S,'V@CFM-ME22','捕获成功本体队列前Owner/ball/解除/Shadowmoves/first/Peer；既有旧成员满队选中才Peer→poisonCount→两undo→store/partyshift，不靠世界当前party后续；取消不先写，真实wholeCatch/Store完整单位已在该record绑定。')
group('30','main',84,86,S,'B@CBC-R005|B@CBC-R006|V@CFM-ME23|V@CFM-ME24','裸EndBattle捕获/scene/cancel/ability/party0Peer+initialitems无统一undo；world当前player/partner/canLose2or5再end通知，decision0正常可到；organized双方levelrestore→逐heal/undo→olditems→record/stat；Play不调用organizedwrapper。')
group('31','main',87,89,S,'W@WMB-R004|M@CME-R006|D@CTF-R007','BugContest函数实际逐只heal→unmega→unprimal再Judging，完整会话/失败dispatcher非本片；Peer被调不等普通形态，显式undo无资源消耗/历史dex/stat/quota返还。')
group('32','main',93,96,S,'D@CTF-R001|D@CTF-R004|D@CTF-R007|B@CBC-R011|B@CBC-R012|B@CBC-R013|M@CME-R003','四不变量逐义：firstreturn不绕第二、Transformbattle/Shadow无统一门、成功ownerquota不refund而裸register/debug可绕普通、qualification与commit中途无事务rollback。自定义坏数据与默认不混。')
group('33','main',97,97,S,'W@WMB-R003|V@CFM-ME24','AI switch/item/auto先截，permission真才register再score，差招成功换人unregister；完整AI/prediction与recordMega缺口不代真实执行合同。')
group('34','main',101,101,'TYPED_COMPLETE_STATIC_VECTOR_REFERENCE','V@CFM-ME01|V@CFM-ME02|V@CFM-ME03|V@CFM-ME04|V@CFM-ME05|V@CFM-ME06|V@CFM-ME07|V@CFM-ME08|V@CFM-ME09|V@CFM-ME10|V@CFM-ME11|V@CFM-ME12|V@CFM-ME13|V@CFM-ME14|V@CFM-ME15|V@CFM-ME16|V@CFM-ME17|V@CFM-ME18|V@CFM-ME19|V@CFM-ME20|V@CFM-ME21|V@CFM-ME22|V@CFM-ME23|V@CFM-ME24|V@CFM-ME25|V@CFM-ME26','ME01–26全部原完整行/共同前提及人工子断言已实际逐条包；本目录引用不增加执行测试/票或全篇自动PASS。')
group('35','main',105,107,'TYPED_DEPENDENCY_FORWARD_SCOPE',None,'形态/动作/owner主规则及其它具名领域真实依赖；前向UI/模式/demo/调试/host/plugin/media与U01–10保留，不决定API/schema/修数据，不转移他人wholeformal接受。')
group('36','main',111,114,'TYPED_EXPLICIT_UNVERIFIED',None,'运行插件/坏数据媒体、demo获得、返回0/forced运行组合、recordMega影响分别保留；本上下文静态已读不冒运行验证。')
group('D01','data',1,3,'TYPED_CURRENT_DATA_STATIC_SCOPE',None,'固定top-level/backup分开、文本枚举及固定算术、成功compile/菜单/媒体非本表证。')
group('D02','data',7,7,S,'D@CTF-R002|D@CTF-R004','48targets46bases47stone1move/Unmega缺省0/Raymessage1其余0；表顺HPAtkDefSpeedSpAtkSpDef不当公式、abilityinherit和所有slots不由单名字推。')
group('D03','data',11,58,S,'D@CTF-R002|D@CTF-R005|D@CTF-R008','完整48表行各target/石或招identity/六个值均和原完整formrecord逐字段对照；每行sourcepointer另保。Slowbro2、Meta95与Salamence同六值仍各独立作者输入；不作官方校正。')
group('D04','data',64,65,S,'D@CTF-R006','Kyogre1 WATER/PrimordialSea/100和Groudon1 GROUND,FIRE/DesolateLand/100，baseHP各100，orb处理器而非Mega字段。')
group('D05','data',67,67,S,'D@CTF-R005|D@CTF-R006|W@WMB-R001|W@WMB-R002','Red/Blue无Flags且无MegaStone；完整693Flags列唯一ring与47stone逐ID对应48表47石；stone/orb个体held与ringowner资源不同，无消耗步骤。')
group('D06','data',71,73,S,'D@CTF-R008','48base/targetHP独立对照只Meta变化，固定数据非修复建议；50Lv0IVEV普通calc total140/155 current70/85回70，目标HP5undo最低1，loss差非比例。')
group('D07','data',77,77,'TYPED_SOURCE_AND_UNVERIFIED_SCOPE','D@CTF-R002|D@CTF-R005|D@CTF-R006|D@CTF-R008|W@WMB-R001','已读50forms/48base/50items/DragonAscent全record与defs仅有限来源；其它20PBS未whole不隐去，文本与固定算术不证明compile/菜单/媒体。')
formal={'main':'deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md','data':'deliverables/final-specification-set/pokemon-rules/wp22-transformation-data.md'};parents=[];fids={};unknown=[];transform=json.loads((C/names['D']).read_text());rawrecords=transform['raw_complete_records']
for file,path in formal.items():
 raw=(B/path).read_bytes();lines=raw.decode().splitlines();assert len(lines)==(114 if file=='main' else 77);fids[file]=dict(path=path,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),lines=len(lines),actual_whole_rereads=['968efb','a3ddd7','current numbered whole114+77'])
 for i,l in enumerate(lines,1):
  if not l.strip():continue
  gs=[g for g in groups if g['file']==file and g['range'][0]<=i<=g['range'][1]]
  structural=l.startswith('#') or bool(re.match(r'^\|\s*(?:---|状态／输入 \||层 \||入口 \||基础物种 \||物种 \|)',l))
  if not gs and not structural:unknown.append((file,i,l));continue
  assert len(gs)<=1
  p=dict(id=f'WP22-{file}-L{i:03}',file=file,line=i,complete_raw=l,disposition='TYPED_STRUCTURE_OR_TABLE_HEADER' if structural else gs[0]['disposition'],semantic_group_ids=[g['id'] for g in gs],new_atoms=0,qualification='Complete raw physical parent actually read and manually interpreted; reference binds all existing child assertions with full common premises/complete source receivers, not auto acceptance by range/hash/semicolon or prior PASS.')
  if file=='data' and 11<=i<=58:
   cols=[z.strip() for z in l.strip('|').split('|')];header=cols[0]+','+cols[1];matches=[(n,x) for n,x in enumerate(rawrecords) if x['source_identity_key']=='forms' and x['header']==header];assert len(matches)==1;idx,x=matches[0];fields={z['key']:z['raw_value'] for z in x['ordered_raw_fields']};rawstats=fields['BaseStats'].replace(',','／');requirement=fields.get('MegaStone',fields.get('MegaMove'));assert rawstats==cols[3] and requirement==cols[2].split()[-1]
   p['complete_authored_row_source_binding']=dict(package=names['D'],pointer=f'/raw_complete_records/{idx}',complete_header=header,raw_source_range=x['range'],requirement_field='MegaStone' if 'MegaStone'in fields else 'MegaMove',exact_requirement=requirement,complete_six_value_vector=rawstats,meaning='Six authored data values in stated table order and exact requirement, not calculated stats/complete runtime ability slots. Whole record and defaults/consumer premises were separately actually read.')
  parents.append(p)
assert not unknown,unknown
out=dict(schema='gr8-crec-wp22-complete-physical-parent-dispositions/v1',recorded_utc=utc,actual_reader=reader,formal_identities=fids,complete_manual_semantic_groups=groups,complete_nonempty_parent_records=parents,nonempty_parent_count=len(parents),manual_groups=len(groups),unassigned_parents=0,mandatory_complete_source_packet_bindings=bind,qualification='Two complete formal papers actually read, all semantic parents manually joined to exact complete prior meanings and whole source units/default records. This is a parent disposition artifact, not additional atom denominator/domainPASS. All normal/failure prefixes and host/plugin/forward boundaries remain. No new independent reviewer/context/vote.',new_atoms=0,denominator_frozen=False,whole_domain_acceptance=False,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');p=C/'wp22-formal-parent-dispositions.v1.json';assert not p.exists();p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),parents=len(parents),manual_groups=len(groups),unassigned=0,utc=utc)))
