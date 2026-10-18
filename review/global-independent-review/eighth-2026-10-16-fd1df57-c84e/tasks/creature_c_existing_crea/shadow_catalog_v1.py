import json,re,hashlib,datetime,subprocess
from pathlib import Path
P=Path(__file__).parent;R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception';rc='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
paths={'shadow':'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb','other':'Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb','chamber':'Data/Scripts/016_UI/023_UI_PurifyChamber.rb','exp':'Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb','itemutils':'Data/Scripts/013_Items/001_Item_Utilities.rb','obtain':'Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb','storageui':'Data/Scripts/016_UI/017_UI_PokemonStorage.rb'};ids={};ts={};us=[]
for k,path in paths.items():
 raw=(R/path).read_bytes();assert raw==subprocess.check_output(['git','-C',str(R),'show',rc+':'+path]);ts[k]=raw.decode('utf-8-sig').replace('\r\n','\n');ids[k]=dict(path=path,commit=rc,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),git_blob=subprocess.check_output(['git','-C',str(R),'rev-parse',rc+':'+path],text=True).strip(),lines=len(raw.splitlines()),actual_reader=reader,credit='OWN_COMPLETE_NAMED_UNITS_ONLY' if k=='storageui' else 'OWN_PREVIOUS_FULL_ACTUAL_READ_REUSED_NO_NEW_CREDIT')
def unit(k,name,nth=0):
 s=ts[k];ms=list(re.finditer(r'^( *)def '+re.escape(name)+r'(?=[( ;\n])[^\n]*\n',s,re.M));assert len(ms)>nth,(k,name,nth);m=ms[nth];z=m.end() if '; end' in m.group(0) else m.end()+re.search(r'^'+m.group(1)+r'end\s*$',s[m.end():],re.M).end();us.append(dict(id=k+':'+name+':'+str(nth),source_identity_key=k,range=[s.count('\n',0,m.start())+1,s.count('\n',0,z-1)+1],text=s[m.start():z],complete_definition=True))
for k in ['shadow','other']:us.append(dict(id=k+':WHOLE',source_identity_key=k,range=[1,len(ts[k].splitlines())],text=ts[k],complete_source_file=True))
for k,names in [('chamber',['partialSum','flow','tempo','insertAfter','insertAt','self.isSuperEffective','self.maximumTempo','chamberFlow','isPurifiableIgnoreRegular?','isPurifiable?','update','pbPlace','pbPlacePokemon','pbOpenSetDetail','pbDoPurify','pbStartPurify']),('itemutils',['pbTopRightWindow','pbChangeLevel','pbChangeExp']),('obtain',['pbBoxesFull?','pbStorePokemon']),('storageui',['pbChoosePokemon','pbSelectBoxInternal','pbSelectBox']),('exp',['pbGainExpOne'])]:
 for n in names:unit(k,n)
for k,name in [('other','pbUpdate'),('chamber','pbChoosePokemon')]:
 unit(k,name,0)
unit('other','pbUpdate',1)
copies=[]
for n in ['shadow-data-vectors.v1.json','wp23-shadow-lifecycle-meaning-atoms.v1.json','battle-consumer-delta.v1.json','form-data-receiver-supplement.v1.json','default-transformation-records.v1.json']:
 raw=(P/n).read_bytes();copies.append(dict(path=n,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader,scope='Complete source/finite raw/data/common premises already personally read; new packet does not borrow any foreign sourceFULL.'))
cs={}
def C(v,*s):cs[v]=list(s)
C('SH01','默认无可用Shadow moves且ShadowRush未登记时makeShadow仍置shadow真、saved_exp0、六saved_ev0、G默认4000。','没有Shadow moves时不进入原招备份/替换分支，原moves保留。','不能把可选PBS存在当默认已加载。')
C('SH02','重复makeShadow重置旧saved_exp与saved_ev。','G重满并重置Hyper/步数。','当前moves重新作为原招来源，不能保证恢复第一次建立前招式。')
C('SH03','stage为ceil(min(G,M)/(M/5.0))，M4000时G0/1/800/801/2400/2401/4000分别0/1/1/2/3/4/5。','G0而shadow标志真仍满足shadowPokemon?。')
C('SH04','直接G=-1使shadowPokemon?false。','adjustHeart对合法Shadow把G夹到0..M，G1减100得到0而仍Shadow。')
C('SH05','玩家拥有入场触发battle心量表下降，HARDY4000减110为3890。','敌方/伙伴不共享玩家心量表下降门。','SHADOW Type已登记时三种阵营进入副本均可改临时类型。')
C('SH06','HARDY G2500的起始stage4使友好变更先被拒。','随后香倍率1下降90到2410，stage仍4。','h80保持，不在降G后追补本次友好。')
C('SH07','able_party步数255加1到256才做walking下降。','跨stage会更新Shadow moves，G0则准备通知。','该次后计数归0，盒中/fainted成员不在able_party队伍循环。')
C('SH08','一Shadow招时stage5只S。','stage4/3补原B，stage2补B/C，stage1/0补B/C/D。','净化后才恢复完整原A/B/C/D。','replace_moves保现有候选，再按新候选补，结果不必候选排序。')
C('SH09','现[B,S]都在候选时不会删除。','保旧B Move对象和其PP。','不按候选[S,B]重排或回满。')
C('SH10','两个Shadow招使原招恢复从偏移MAX_MOVES+2开始。','H0只能补C/D，不提前补A/B。')
C('SH11','正整数G4000均匀rand范围0..3999，<=1000命中。','r1000进而1001不进，概率1001/4000。')
C('SH12','G1001正整数的全部0..1000都满足门。','G0默认Battle.pbRandom调用Kernel rand(0)得到浮点[0,1)，仍满足<=1000。','此时写存储Hyper真并提示，但effective getter因G0返回false。','后继同样调用可重复进入该写/提示。')
C('SH13','内部玩家有效Hyper且原招非Shadow时直接全局rand(100)<20通过服从门，不经Battle.pbRandom。','19通过而20失败。','非internalBattle由外层不调用此门。')
C('SH14','招式行动后Hyper反伤按总HP整数除24，23/48先得到0/2但最少1处理使1/2。','其反伤早于后继10%平静检查。','Call选择不是该招式行动反伤caller。')
C('SH15','G>0存活Hyper的普通heal不清存储Hyper。','hp=0经Shadow写入清Hyper。','G0有效Hyper假不等同存储Hyper必已清。')
C('SH16','Shadow pbInitPokemon前置仅旧@pokemonIndex>0且旧副本有效Hyper时清旧个体Hyper。','旧index0不满足该索引门。','普通离场先把副本视为fainted，使其有效Hyper假而跳该清理。')
C('SH17','Shadow exp=截留实际差121到S，当前E保持。','收益统计在Battle调用者按实际差增加121。','净化4/5整数折算得到96，不是全121。')
C('SH18','每次gained EXP先按当前真实E的最大余量10夹限。','当前E仍未变使两次均截留10而S20。','净化请求16再按真实余量夹为10。')
C('SH19','S0在Ruby中truthy所以仍进入净化经验段并清S。','已最大E不增加而同等级分支仍calc_stats。')
C('SH20','战斗EV消费者仅Shadow stage<=3且V存在时写暂存V。','stage4/5按普通EV字段写入。','V额度含当前EV与已暂存值。')
C('SH21','当前250/总508加V1后，单项252和总510均只余1。','请求3只再暂存1。')
C('SH22','净化add_evs按main顺序逐项单项252/总510夹限。','251/509请求5只恢复1。','V随后置nil，剩4不保留。','S nil时没有经验段保证calc_stats。')
C('SH23','人工V存在/Snil仍会先加EV并清V。','Snil跳过整个经验和其calc分支。','不能把常规makeShadow必给S0当成这个人工输入禁止条件。')
C('SH24','Relic Stone pbUpdate定义允许跨级窗口走其正常更新调用。','在后来学招/演化/昵称取消前，Shadow/缎带/EV/S消费已经到达。','这些取消不回滚净化。','Chamber跨级先在Screen receiver更新缺方法失败，不能套同一后继取消。')
C('SH25','TimeFlute只拒非Shadow、G0、Lugia。','给定G100合格后调用pbPurify，该工具因G不0立即return。','handler仍true使正常外层消费笛，G与Shadow不变。')
C('SH26','TimeFlute对G0先拒。','对Lugia先拒。','对非Shadow先拒，正常外层不消费。')
C('SH27','可选香raw没有Scent旗标。','Hyper普通个体前门要求Scent有效数据，因此菜单链拒。','直接handler能清Hyper不证明菜单链可达。')
C('SH28','RelicStone外层hasPurifiable只Lugia时false。','另有可净化非Lugia使选择器可打开。','选择器只有Shadow/G0门，给定存活Lugia也能进pbPurify。','取消选择不提交净化。')
C('SH29','四NORMAL外圈的4条有向优势加partialSum4=10得到T14。','没有中心使flow0。','NORMAL中心多1优势和length/2=2得到F7。','无中心优势则F6，其它组不会加速普通中心。')
C('SH30','isSuperEffective只要求至少一个攻击类型/防守类型组合超效。','FIRE对GRASS/WATER可由Grass弱点命中，不计算复合乘积抵消。')
C('SH31','一NORMAL外圈T=partialSum1+自环优势1=2。','NORMAL中心优势使F2。','每实际步G3减2到1，再到0只准备通知而不pbPurify。')
C('SH32','Lugia的净化资格另要求九组均maximumTempo14。','任一T13使其失败。','中心可空与外圈T14是不同条件，G>0仍未ready。')
C('SH33','普通pbPlace先拒egg。','REPLACE走原始shadowPokemon?相等而无同样egg门。','nil==nil和false==false可过，nil==false拒，不归一化真假。')
C('SH34','Chamber Scene选择器启动Storage command1。','该command的pbSelectBox直接用box selector，Party按钮返回[-2,-1]并按盒映射取值。','映射空则继续循环；映射有X先成员菜单，Select才返回原位置。','直接pbPlacePokemon对合法party位置成功后pbDelete可压缩party，没有最后可战斗门。','选人期间currentBox变化或已完成取拿不因后来BACK/No撤销；本次retval仍nil。')
C('SH35','[A,B,C] facing1删除A后index1指C。','在A后insertAfter X时facing1>index0使facing加1到2，仍指B。','flow可随新有向邻接变化。')
C('SH36','暂持Pokemon是编辑循环的heldpkmn引用。','切组不自动送回原位。','held存在时BACK提示持有而不退出。')
C('SH37','pbBoxesFull?要求party和boxes同时满。','boxes满但party空位时不拒WITHDRAW。','实际调用pbStoreCaught只找boxes并可return-1。','caller不检查返回值仍清held/原槽，容器保有性不能保证。')
C('SH38','S0同级正常净化已经清Shadow/返EV/S后才到pbStorePokemon。','队伍和盒都满使通用存放拒绝。','caller仍setShadow nil，中心被清。','若先触发跨级更新异常则未到此store和清中心。')
C('SH39','先计算purifiable组索引集合。','第一只S0同级正常领取后先清该center。','拒绝切下一组只阻止后组，不恢复第一只。')
C('SH40','开始heart快照按旧party索引记录。','捕获替换移动levels/K/D但不移动该快照。','现index0 G0对应旧快照0使本提示循环跳过。')
C('SH41','Pokemon基础clone浅复制saved_ev引用。','Shadow clone逐键写ret.saved_ev但没有新建Hash，所以仍共享。','改副本V数值影响原表。','将副本saved_ev=nil只换该字段，不清原表。','shadow_moves另clone为独立数组。')
C('SH42','Shadow入场可先把副本types设SHADOW。','Mega完整pbUpdate(true)再从持久个体回读types。','没有Shadow永久最后覆盖优先级。')
C('SH43','Rattata当前E1000/S416返还整数332，newexp1332对应L11。','pbChangeLevel先设11最低E1331并重算/升级happiness。','首个能力窗口调用scene参数实际是PurifyChamberScreen self；该类无pbUpdate。','Scene类另有pbUpdate，不能误称Scene也缺该方法。','窗口缺方法时尚未写精确1332、学招/演化/昵称/store/清中心。','更早Shadow/Hyper/缎带/招式/V恢复及清V/S已到，中心仍引用此同对象。')
C('SH44','同一只改S0使newexp1000同等级。','直接exp=1000及calc_stats不进跨级窗口。','后续正常可到命名/store容量分支。')
C('SH45','RelicStone传其有pbUpdate的Screen receiver。','不会在Chamber相同缺方法处失败。','正常ChangeLevel返回后再写精确newexp1332，后续仍各按实际前门。')
C('SH46','两普通未设shadow原始nil/nil比较真。','未设nil与purified false比较假。','false/false比较真，普通place仍单独有egg门。')
C('SH47','G0有效Hyper假，即使存储Hyper真也不能以已清effective Hyper取得rettrue。','h255且G0使共同工具无友好/心量收益，正常野外handlerfalse不消费。','战斗专门CanUse也拒绝；H0不是H5。')
C('SH48','只h254可得普通友好+1到255，G仍0。','共同工具true使正常野外消费一份。','Shadow G0未净化不统一阻止香效果。')
C('SH49','Lonely起始stage4先拒友好。','随后按存储Lonely香下降130到2370/stage3。','跨stage后不追补本次h。')
C('SH50','有效安装可选records/moves/type才使用此fixture。','Growlithe默认Shadow data G4000、有序ShadowBlitz/ShadowWave。','Snorunt G2500、有序ShadowWave/ShadowShed。','两者H5，不能据raw存在声称默认已加载或运行。')
C('SH51','注册先扣库存。','执行前变G0/h255使当前CanUseInBattlefalse。','不调用效果handler，正常退款分支恢复未用物品。','handler本身true不替代复检结果。')
C('SH52','心量表方法查存储@nature，不读nature_for_stats覆盖。','HARDY存储即使计算覆盖Lonely仍下降90到2410。','起始stage4门使h80保持。')
assert set(cs)=={f'SH{i:02}' for i in range(1,53)}
formal='deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md';fr=(B/formal).read_bytes();rows=[]
for v,ss in cs.items():
 loc=[(i+1,l) for i,l in enumerate(fr.decode().splitlines()) if l.startswith('| '+v+' |')];assert len(loc)==1;line,text=loc[0];refs=['shadow:WHOLE','other:WHOLE']
 if int(v[2:]) in list(range(29,40))+[43,44,45,46]:refs +=['chamber:pbDoPurify:0','chamber:pbOpenSetDetail:0','itemutils:pbChangeLevel:0','itemutils:pbTopRightWindow:0']
 if v=='SH34':refs+=['storageui:pbChoosePokemon:0','storageui:pbSelectBox:0','storageui:pbSelectBoxInternal:0']
 if v in ['SH17','SH18','SH19','SH20','SH21']:refs+=['exp:pbGainExpOne:0']
 if v=='SH37':refs+=['obtain:pbBoxesFull?:0']
 if v=='SH38':refs+=['obtain:pbStorePokemon:0']
 if v=='SH45':refs+=['other:pbUpdate:1']
 rows.append(dict(id='SHV-'+v,vector=v,formal=dict(path=formal,line=line,complete_raw_row=text),premise='完整原行以及目录固定/默认/可选/人工/正常前序条件全保留。每行独立重置；合法数据与资源/host/先前消息正常至观察点，不假装已执行可选安装、生成、动画、Marshal或真实保存。',child_assertions=[dict(id=f'SHV-{v}-A{i:02}',meaning=x,complete_source_unit_ids=refs,mandatory_source_packets=[x['path'] for x in copies],status='MANUALLY_JOINED_BOUNDED_STATIC',whole_parent_acceptance=False) for i,x in enumerate(ss,1)],normal_cancel_failure='正常取消、资格拒绝、局部异常和已到model/缓存/EV/EXP/moves/Container/Bag前缀分列；不存在统一回滚或finally。屏幕/场景类型按真实receiver，不由命名代调用；无host恢复或像素保证。',remaining='未列其它组合、原始默认运行可达、宿主、demo、插件、保存重载及其它primary继续具名OPEN。',accepted=False))
out=dict(schema='gr8-cre-c-shadow-catalog52/v1',recorded_utc=utc,actual_reader=reader,formal_identity=dict(path=formal,bytes=len(fr),sha256=hashlib.sha256(fr).hexdigest(),complete_read_chunks=['b81e99','dff095','7d3377','bb295d']),source_identities=ids,complete_source_units=us,mandatory_complete_source_packet_bindings=copies,records=rows,manual_atoms=sum(len(x['child_assertions']) for x in rows),chamber_minimal_receiver_qualification='Root accepted prior exact Screen self/Scene pbUpdate clarification in root-chamber-receiver-reception.json; no new formal defect or vote. Full current source independently reread as necessary here.',actual_current_source_rereads=dict(shadow='7e930a',other_and_scene='9d9ba6',Screen='707c79',window='8cf0d6',storage_choose=['5fbb44','e82254']),source_FULL_transferred=False,new_votes=0,denominator_frozen=False,whole_domain_acceptance=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
f=P/'shadow-catalog52-meaning.v1.json';assert not f.exists();f.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');rv=json.loads((P/'reverse-mapping.json').read_text());assert not ({x['id'] for x in rows}&{x['id'] for x in rv['records']});rv['records']+=rows;rv['utc']=utc;(P/'reverse-mapping.json').write_text(json.dumps(rv,ensure_ascii=False,indent=2)+'\n');pr=json.loads((P/'progress.json').read_text());pr.update(updated_utc=utc,primary_clause_atoms=sum(len(x.get('child_assertions',[])) for x in rv['records']));(P/'progress.json').write_text(json.dumps(pr,ensure_ascii=False,indent=2)+'\n');raw=f.read_bytes();print(json.dumps(dict(utc=utc,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),groups=len(rows),atoms=out['manual_atoms'],source_units=len(us),current_groups=len(rv['records']),current_atoms=pr['primary_clause_atoms'])))
