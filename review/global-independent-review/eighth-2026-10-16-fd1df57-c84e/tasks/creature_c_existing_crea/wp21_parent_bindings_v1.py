import json,hashlib,datetime,re
from pathlib import Path
C=Path(__file__).parent;B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception'
names={'H':'wp21-handler-meaning-atoms.v1.json','M':'wp21-mechanism-spinda-display.v1.json','F':'form-data-receiver-supplement.v1.json','V':'form-mega-catalog69-meaning.v1.json','K':'display-item-catalog29-meaning.v1.json','D':'type-ribbon-data.v1.json','E':'wp31-wrappers-commit-meaning.v1.json','G':'wp30-compound-meaning.v1.json','W':'wp21-condition-source-bindings.v1.json'};packs={};bind={}
for k,n in names.items():
 raw=(C/n).read_bytes();d=json.loads(raw);packs[k]={x['id']:x for x in d['records']};bind[k]=dict(path=n,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader)
groups=[]
def refs(s):
 ret=[]
 for z in s.split('|'):
  k,id=z.split('@',1);assert id in packs[k],z;x=packs[k][id];ret.append(dict(package=names[k],complete_record_id=id,complete_existing_atom_ids=[a['id'] for a in x['child_assertions']]))
 return ret
def h(*ns):return '|'.join(f'H@C21-R{n:03}' for n in ns)
def group(id,lo,hi,status,rr,meaning):groups.append(dict(id='WP21-PG-'+id,range=[lo,hi],disposition=status,complete_existing_manual_records=refs(rr) if rr else [],manual_semantic_scope=meaning))
S='MANUALLY_JOINED_BOUNDED_STATIC'
group('01',1,11,'TYPED_PURPOSE_SCOPE_AND_RESPONSIBILITY',None,'完整标题/分类/目的范围非目标；当前所有注册族与提交/展示语义为审读范围，Mega/Shadow/战斗时序/专用UI/完整contest/资源/API其他主责不由本篇授PASS。')
group('02',15,20,S,'M@CFM-R001|M@CFM-R003|M@CFM-R004|M@CFM-R005|M@CFM-R012|M@CFM-R014','六术语逐义：整份物种mapping、不同hook分别定义、candidate和consumer提交分开、forced优先限合法数字（form与form_simple非nil/||对false差异仍保）、time整数、mark/ribbon/contest记录非完整玩法。')
group('03',26,27,S,'M@CFM-R001','register整份替换；query非Symbol且respond_to?id才取id，不对String统一to_sym；directmappingmiss后conditions插入序首通过，再nil；不是域验证/完整对象创建。')
group('04',28,32,S,'M@CFM-R002','copy在当时[]解析取同一handler对象，source重新register换binding不重绑target；原handler原地mutate共同可见；source无handler静默。全部9copy27target逐具名fullstatement已实际读，当前条件注册0但能力定义仍审。')
group('05',33,34,S,'M@CFM-R001|M@CFM-R002','hasFunction?返回实际hook/proc或nil而非booltrue；call传Pokemon及附加参数；49register+27唯一copytarget=76，每触发计数按全792源definition/inventory实际对应，未推运行注册成功。')
group('06',38,40,'TYPED_DIRECTORY_FORMAT',None,'目录条件取值说明是行为格式；环境角色来源3.3，不把标签名等于原生host/当前地图观察。')
group('07',44,58,S,h(14,15,16,18,20,21,24,25,26,30,32,40,42,48,49)+'|M@CFM-R003|W@WCS-R001|W@WCS-R002|W@WCS-R003','15读取注册及5copy全部逐species：宝珠或Distortion/Giratina、Shaymin早faint/freeze/night否则nil、多属性17+0或无abilitynil、season%4、knownSword、4drive、5/3日strict超时、gender、Rockruffstored>=2、RKS17、Milcery7+(PID%9)*7、区域firstcomponent1/2与stored>=2守卫；真实读者form仅normal非battle非storage且nonforced。')
group('08',60,73,S,h(1,11,12,23,27,31,33,38,39,41,45)+'|F@FDR-R003|W@WCS-R001|W@WCS-R002|W@WCS-R003','11create注册+5copy：Unown28、Burmy/Wormadam实际enum:None→2、SecretID%18、Pumpkin5/20/65阈值、Evening先于Night、Minior7..13、Toxel12nature、Sinistea10%、Alcremie63、Urshifu2；constructor末stored0/enabled/withMoves再初始化限定，不把candidate直接提交。')
group('09',75,84,S,h(13,19,24,25,37,46)+'|F@FDR-R001|F@FDR-R002|M@CFM-R004','六提交hook四改Moves两time；Rotom首形态move/targetfound/known次序、Kyurem内部compactskip、Furfrou/Hoopa>0stamp/0nil、Necro旧新<=2、Calyrex删与basislearnability不设currentlevel/末compact。Learn拒绝不回滚form或已删。')
group('10',86,92,S,h(19,28,33,43,44)+'|M@CFM-R011|F@FDR-R002','start三取值和两rawMove改写：Xerneas1、Zac/Zamheld→1/0并目标登记才IRONHEAD变；entryKyurem1/2+2、wildMinior>=7-7；normalPeer真实wild参数/全队起始/派出后调用，非所有裸model都触发。')
group('11',93,94,S,h(3,11,4,17,19,5,22,6,28,29,7,33,34,37,8,35,36,43,44)+'|M@CFM-R011','19leave族每条件完整源unit：Burmyend&&used、Darmanitan偶数元组、Kyurem>=3-2、Greninja2faint/end→1、Zygarde>=2faint/end-2、Minior<7+7、Necro>=3faint/end-2、Mimikyu/Eiscue/Morpeko端点门、Xerneas/Zac/Zamend门及其它固定0；终战专属招反向不检查IronHead注册，非end不改。')
group('12',96,102,S,h(47,2,9,10)+'|M@CFM-R009|M@CFM-R010|W@WCS-R003','其它3行：Rattata+17copiesegg当前region存在校验；Spinda个体位图有限host边界；Groudon/KyogreonlyPrimal注册/held条件归WP22，不从该表推整个Primal/孵化会话。')
group('13',106,117,S,h(16),'Arceus17编号1..8/10..18每编号plate或Z两值、无9、Fire10、无匹配0、无MULTITYPE nil；表六物理行各三列共17完整值与两个default控制精确接原4children和wholeproc，不合并为任意type排序。')
group('14',119,121,S,h(32,21),'Silvally17Memory同1..8,10..18且RKSSYSTEM守卫；Genesect依SHOCK/BURN/CHILL/DOUSE首匹配1..4，其它0。两个mapping族分别各wholeproc，未从中文名创造别名ID。')
group('15',123,125,S,h(38,40),'Toxel完整12nature集合内1/外0；Milcery7种sweet先后index0..6与PID%9*7确定值，无独立随机抽样。')
group('16',127,129,S,h(47)+'|M@CFM-R002|W@WCS-R003','Rattata蛋hook17全部copytarget原完整3行实际读（Sandshrew,Vulpix,Diglett,Meowth,Geodude,Grimer,Ponyta,Farfetchd,Corsola,Zigzagoon,Darumaka,Yamask,Stunfisk,Slowpoke,Articuno,Zapdos,Moltres）；regionform缺回base再比较拒，无强造form。核对要点分别接17/4/12/7/17数据原子，不当运行测试。')
group('17',133,142,S,'M@CFM-R006|M@CFM-R009','合法32bitPID/普通shiny缓存/validbitmap前提；八hexnibble右至左，四锚点顺序S1..4及各8x9/7x9/13x13/12x12，logic到actual*2；不新随机/不改model。')
group('18',144,151,S,'M@CFM-R007','四mask全部43source rows逐行解出闭区间，S3末5..7及S4下缘4..8不强补对称；范围外不标记。完整decodedrow vectors保在sourcepacket，不仅凭宽高。')
group('19',153,155,S,'M@CFM-R008','块只sample左上RGB/alpha，clamp后write2x2同色；normal(0,-115,-75)/shiny(-75,-10,-150)，未标记不动；重叠读取已写色重复处理。PID0/FFFFFFFF/0000F000锚点与200RGB单次/二次每分量独立固定算术，非运行像素。')
group('20',157,159,S,'M@CFM-R009|M@CFM-R010','个体nonEgg选有效species/form/gender/shiny/shadow/frontback后有效bitmapcopy、handler按chosenSpecies、each枚举bitmaps修饰；filename分帧PNG每独立frame自身原色，nativebitmap仅一次枚举不能推出内部1/all帧颜色或成败。')
group('21',161,163,S,'M@CFM-R009|M@CFM-R010','egg和directSpeciesparameter入口不经过相同PID修饰；copypixel不写resource/model，但取图前form/gender/shiny读副作用仍在；validdimension及全访问在内前提，无资源可nil/加载越界host/alpha显示未知、U03SP10静态非素材执行。')
group('22',169,175,S,'W@WCS-R001|W@WCS-R002|W@WCS-R003|M@CFM-R005','来源角色七行：env map→terrain/fishingfacing；season(mon-1)%4；night/eveningactualhour门nil/false替host；townposition三元首component；secretID高位；timefield；individual item/move/ability/gender/nature/PID/status。只接角色及精确定义，未观察当前host值或全地图。')
group('23',179,181,S,'M@CFM-R003|M@CFM-R005|W@WCS-R002|H@C21-R024|H@C21-R025','forced数字优先；fullform nonnil/简单||对false差异另保；writer仅当前literal定位Debug不宣称全事件不存在；catch有getForm才清forced。5/3日strict超window、onSet>0tstamp/0nil、空保护、hostclock回拨未知，不擅把秒解释游戏步数。')
group('24',183,183,S,'K@DIC-R4-IF01|K@DIC-R4-IF02|K@DIC-R4-IF03|K@DIC-R4-IF04|K@DIC-R4-IF05|K@DIC-R4-IF06|M@CFM-R003|M@CFM-R005','完整IF6具名432001/432000、normalfront/back/icon/Summarydynamic getter先提交0/cache/time/calc/conditionalDex再resource；forced1/battle/storage阻止，forced0只返回0不改stored1/time；显式低层形态参数不证明caller纯读，resource缺不回滚，EG动态合同保持。')
group('25',191,194,S,'M@CFM-R004|M@CFM-R003','四入口逐序：form= write/cache/handler/calc/conditionalDexgender+shiny；setForm yield夹在write/cache后；simple=仅write/calc；constructorstored0/enabled返回才form=及withMoves重做。callback/host/计算失败保prefix，不授全对象事务。')
group('26',196,196,S,'M@CFM-R004|F@FDR-R001|V@CFM-FM39','裸samevalue两setter不短路，dynamic仅different才submit，Catalog外层samefail；guard归实际caller不能倒补裸接口。')
group('27',200,204,S,'H@C21-R013|H@C21-R019|H@C21-R037|H@C21-R046|M@CFM-R004|G@CGR-R013','直接同Move id=保slot/ppup并clampcurrentpp非回满；learn新增/替换newMove初PP/ppup，fullpromptcancel/refuse不写这次learn但不undoform/前序deletion；删除压缩时机每species不同，不套machine keepPP变体。')
group('28',205,205,S,'H@C21-R019|H@C21-R046|V@CFM-FM23|V@CFM-FM24','Kyurem0 [Glaciate,IceBurn,FusionFlare]删除IceBurn即时compact导致迭代跳FusionFlare，留下两招；Calyrex删循环后compact不具此跳项。前提registry有效且existingtarget精确，不是普遍所有列表规格。')
group('29',206,208,S,'F@FDR-R001|F@FDR-R002|H@C21-R013|H@C21-R037|V@CFM-FM39|V@CFM-FM42','Rotom先targetexist再唯一slot保底后known取消、same1仅Overheat可删空且不补ThunderShock；Catalogsame早fail不动Moves；满无旧slotlearncancel不回滚form，双缺throw早于calc/dex；Necro旧或新>=3不改，0空learn被egg/shadow拒可空。')
group('30',209,211,S,'H@C21-R043|H@C21-R044|M@CFM-R004|G@CGR-R013','Zac/Zam两时点rawID保ppup/clampPP；提示yield→内部message→calc/dex，学习规则归WP30已whole审；本片只hook接口与真实调用，无native演出保证。')
group('31',213,224,S,'H@C21-R013|H@C21-R019|H@C21-R037|H@C21-R046|H@C21-R043|H@C21-R044|F@FDR-R001|F@FDR-R002','表F八完整行逐speciesform/sourceMove/targetexist/known过滤/0删除/1或2新增、Calyrex基础specieslearnability、Zac/Zam起始持物/终局不需持物均分别核；实际17source/defaultmove完整records已在FDR，未以名字或rowcount替原文。')
group('32',228,234,S,'F@FDR-R001|F@FDR-R002|V@CFM-FM40|V@CFM-FM41|V@CFM-FM42|V@CFM-FM43|G@CGR-R013','五失败row各异：Rotom缺目标试fallback再throw、Kyurem缺skip、Necro/Calyrex先registryparse错误早于egg/shadow、Zac持物/target未满足不改而形态可另变、还原IronHead缺在id=赋值失败保旧槽。Necro0[Tackle]→1追加SunsteelStrikePP5/ppup0validdefault静态，WP28整体道具另责。')
group('33',240,248,S,'M@CFM-R011|H@C21-R011|M@CFM-R004','五receiver完整源：BattleStart双方成员wild，Peerentrywild，Recall/Faint/Catch传battle/used/end，EndBattleparty0逐成员endtrue及catchendusedtrue/clearforced；Burmy依flags；calcHP副作用实际后续battleflush归动作，Mega/Primal另篇已有限接。')
group('34',254,258,S,'M@CFM-R012','markings初[]/nil格按0、sixslots/8positions/resourceheightvariant；Summaryclone draft+USE循环/Confirmwholearray/CancelBACKkeep，ACTIONnil>0失败；Storage无ACTION清零分支，方向/USE/BACK顺序保。原UI11/08完整facts真正接收，FULL源仍ui_wp66。')
group('35',259,260,S,'M@CFM-R013|E@CEC-R006','v20Integerbitmask→六bit数组在party/daycare/storage确转换而其它额外placements不被否定；clone保marks引用，Shedinja前space/ball→clone/newSpecies/name/marks[]/POKEBALL/itemnil/ribbonsclear/calc/heal→append/Dexseenowned→callerballremove；contest值保，不独立事务。')
group('36',264,268,S,'D@CTR-R004|D@CTR-R005','orderedribbons giveunknownignore/knowndedup；upgrade按arg匹配首可用next注册直接替可重复，不适用继续scan；全不适用首末有效末未持才give首/return；removeunknownnoop/registeredabsentindexnil传delete_at失败/clear。clone数组独立但mark数组不同。')
group('37',269,270,S,'M@CFM-R014|D@CTR-R003|D@CTR-R004|D@CTR-R005','Summary持列表顺12visible与scroll、iconpos仅crop非排序；80defaultRibbon完整records/schema/flags已读，净化固定Ribbon与Debug读者只接接口，PBS往返/完整资源仍依其主责。')
group('38',274,277,S,'M@CFM-R014|M@CFM-R013|E@CEC-R006','sixcontestvaluescreate0/valueclone，Beauty>=param及Feebas170完整authored边已有限实际接（169false/170true附其它门）；literal非Debugwriter未定位不等无功能，复制不清而marks/ribbons清，各独立。')
group('39',281,289,S,'M@CFM-R001|M@CFM-R002|M@CFM-R003|M@CFM-R004|M@CFM-R005|M@CFM-R011|M@CFM-R012|M@CFM-R013|M@CFM-R014|D@CTR-R004|D@CTR-R005','九不变量逐完整合同重接：只有实际hook注册才行为、正常dynamicdifferent、候选无统一域校验、三个setter差序、三Move路径、callerflags、forced/time/catch、三展示字段/特殊copy、条件0+copyshared。此复述不新增万能caller门或复用票。')
group('40',293,301,S,'M@CFM-R001|M@CFM-R002|M@CFM-R003|M@CFM-R004|M@CFM-R012|M@CFM-R014|D@CTR-R004|D@CTR-R005|F@FDR-R001','九失败分别接实际早写/后错：Rotom、nocopysource/String、形态任意整数记录不保证资源/显示、markoutofrange绘制min/editmod、SummarynilACTIONvsStorage无、ribbonduplicates/remove/回退、learningcancel不undoform、clock未知、contestwriter/U01U04未证。')
group('41',305,308,S,'M@CFM-R003|M@CFM-R004|M@CFM-R010|W@WCS-R001|W@WCS-R002','无hook创建不读dynamicquery但保stored；资源/目录决定UIvariants；season/night/env与配置真实调用；Kyurem跨周期规则齐但组合未运行不误标缺静态定义，完整host结果仍未知。')
group('42',312,314,'TYPED_COMPLETE_STATIC_VECTOR_REFERENCES','|'.join(f'V@CFM-FM{i:02}' for i in range(1,44))+'|'+'|'.join(f'K@DIC-U03-SP{i:02}' for i in range(1,11)),'FM43/SP10每完整原向量及所有共同前提/人工children已在独立完整包；这里只交叉目录，全部53完整recordID明确列出，261全目录人工映射另实际完成，全部NOT_EXECUTED。')
group('43',318,318,'TYPED_DEPENDENCY_RESPONSIBILITY',None,'个体/HP/PP/Mega/净化/进化/学习/寄养/战斗/资源/Trainer/Dex/迁移责任链完整解释，实际sourcecredit/具名完整贡献保原reader，不以主责名授其它whole域。')
group('44',322,327,'TYPED_EXPLICIT_UNVERIFIED',None,'六未证：非Debugforcedwriter、contestproduction、mark实际资源、demo/event可达、clock异常、conditional用途；定义能力可审但来源未观察不改成materiallimit，也无全局PASS。')
formal='deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md';raw=(B/formal).read_bytes();lines=raw.decode().splitlines();assert len(lines)==327;parents=[];unknown=[]
header_prefixes=('物种（含复制）','物种 |','时机 |','时机 | 注册','编号 |','---','次序／形状','形状 |','条件 |','入口 |','物种／时机','数据门／失败边界')
for i,l in enumerate(lines,1):
 if not l.strip():continue
 gs=[g for g in groups if g['range'][0]<=i<=g['range'][1]];structural=l.startswith('#') or (l.startswith('|') and l.lstrip('| ').startswith(header_prefixes))
 if not gs and not structural:unknown.append((i,l));continue
 assert len(gs)<=1
 parents.append(dict(id=f'WP21-L{i:03}',line=i,complete_raw=l,disposition='TYPED_STRUCTURE_OR_TABLE_HEADER' if structural else gs[0]['disposition'],semantic_group_ids=[g['id'] for g in gs],new_atoms=0,qualification='Actual complete source/formal and all named finite objects read. Exact existing complete manual record means all its child assertions/common premise/normal-failure/receiver references, not a body range or first/last assertion proxy. Original UI provider credit retained; no atomic/global denominator freeze.'))
assert not unknown,unknown
out=dict(schema='gr8-crec-wp21-physical-parent-dispositions/v1',recorded_utc=utc,actual_reader=reader,formal=dict(path=formal,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),lines=327,actual_current_reread='Two complete contiguous tool outputs1–165 and166–327; earlier whole ownread retained'),complete_manual_semantic_groups=groups,complete_nonempty_parent_records=parents,nonempty_parent_count=len(parents),manual_groups=len(groups),unassigned_parents=0,mandatory_complete_source_packet_bindings=bind,source_reader_boundary='Definitions and source/full files in this same actual context remain own; all selected complete UI originalunits and original sourceidentities are in wp21 mechanism selected_UI_reception with reader ui_wp66, actual finite reception not transfer of whole source FULL. Source hash/mechanicalcount doesnot substitute reading.',new_atoms=0,whole_domain_acceptance=False,denominator_frozen=False,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');p=C/'wp21-formal-parent-dispositions.v1.json';assert not p.exists();p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),parents=len(parents),manual_groups=len(groups),unassigned=0,utc=utc)))
