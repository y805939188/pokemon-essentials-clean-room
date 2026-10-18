import json,re,hashlib,datetime,subprocess,math
from pathlib import Path
C=Path(__file__).parent;A=C.parent/'creature_a_atomic_reception';R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception'
def rd(p):return json.loads(p.read_text())
def wr(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
names={'G':C/'wp30-compound-meaning.v1.json','W':C/'wp30-learning-consumers-and-binding.v1.json','HP':C/'wp30-happiness-initial-producer-binding.v1.json','ST':C/'stat-catalog67-meaning.v1.json','S':C/'wp21-mechanism-spinda-display.v1.json'};packs={};bindings={}
for k,p in names.items():
 raw=p.read_bytes();d=json.loads(raw);packs[k]={x['id']:x for x in d.get('whole_source_units',d.get('complete_source_units',[]))};bindings[k]=dict(path=p.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader)
ui_path=C.parent/'ui_full/creature-a-ui-package.v1.json';uid=rd(ui_path);allunits=uid.get('complete_units',uid.get('units',uid.get('semantic_units',[])))
if not allunits:
 for k,v in uid.items():
  if isinstance(v,list) and v and isinstance(v[0],dict) and any(x.get('id')=='S09' for x in v):allunits=v;break
selected=[x for x in allunits if x.get('id') in ['S09','S10','S13']];assert len(selected)==3
ballpath='Data/Scripts/011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb';raw=(R/ballpath).read_bytes();assert raw==subprocess.check_output(['git','-C',str(R),'show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+ballpath]);ls=raw.decode().splitlines(keepends=True);extra=[]
i=next(i for i,l in enumerate(ls) if l.startswith('  def self.onCatch('));j=next(j for j in range(i+1,len(ls)) if ls[j].startswith('  end'));extra.append(dict(id='ball:onCatch',range=[i+1,j+1],text=''.join(ls[i:j+1]),complete_definition=True))
i=next(i for i,l in enumerate(ls) if 'OnCatch.add(:FRIENDBALL' in l);j=next(j for j in range(i+1,len(ls)) if ls[j].startswith('})'));extra.append(dict(id='ball:FRIENDBALL',range=[i+1,j+1],text=''.join(ls[i:j+1]),complete_registration=True))
claims={};refs={}
def ref(s):
 k,n=s.split('@',1)
 if k=='X':assert n in [x['id'] for x in extra];return dict(package='SELF',unit_id=n,actual_reader=reader)
 if k=='UI':assert n in [x['id'] for x in selected];return dict(package='SELF',json_pointer='/complete_selected_UI_reception',unit_id=n,actual_source_reader='/root/ui_wp66',source_FULL_transferred=False)
 if n=='GROWTH_WHOLE':return dict(package=bindings['G']['path'],json_pointer='/complete_growth_registry_source',actual_reader=reader)
 assert n in packs[k],(k,n);return dict(package=bindings[k]['path'],unit_id=n,actual_reader=reader)
def Cc(v,rr,*ss):claims[v]=list(ss);refs[v]=[ref(x) for x in rr.split('|')]
gro='G@growth:self.max_level|G@growth:minimum_exp_for_level|G@growth:maximum_exp|G@growth:add_exp|G@growth:level_from_exp|G@GROWTH_WHOLE';exp='G@exp:pbGainExp|G@exp:pbGainExpOne';ev='G@exp:pbGainEVsOne';learn='G@items:pbLearnMove';relearn='G@relearn:pbGetRelearnableMoves|G@relearn:pbStartScreen|G@relearn:pbStartScene|G@relearn:pbDrawMoveList';happy='G@pokemon:changeHappiness'
Cc('GR-01',gro,'六曲线完整注册表内L50/L100分别125000/1000000、100000/800000、156250/1250000、117360/1059860、125000/600000、142500/1640000。','表内查表权威，L1特例和表外公式另分，已有600独立算术核对不冒目标运行。')
Cc('GR-02',gro,'Medium0经验首档L1，999999低于L100门得99。','>=1000000按max分支得100。')
Cc('GR-03',gro,'等级0返回ArgumentError对象而非raise。','经验-1在错误诊断插值引用未定义名称时先名称解析失败，不返回该对象。')
Cc('GR-04',gro,'add_exp先加999990+100，再夹最大1000000。','实际差1000000-999990=10；不是raw exp=的域保证。')
Cc('GR-05','G@pokemon:exp=','非Shadow原始exp=原样写负或超限。','随后level缓存nil，不保证后续读取/重算正常，也不自动夹限。')
Cc('GR-06',gro,'默认max100把101先夹100，再查表。')
Cc('GR-07',gro,'显式max101使L101超表，选各登记公式。','Erratic618474，Fluctuating20505而L100原1640000；不把非单调表外现状修参考或称设计建议。')
Cc('GR-08',exp,'a10×60=600；均分关单参与基础600。','scaled先整除5为120，同级因子1，再资格+1得121。')
Cc('GR-09',exp,'Owner同ID且语言0不触外来条件。','原121保持。')
Cc('GR-10',exp,'异ID、语言0只触1.5倍，不触1.7。','floor121×1.5=181。')
Cc('GR-11',exp,'ID相同但非零异语言仍触外来。','只取1.7，floor121×1.7=205，不连乘1.5。')
Cc('GR-12',exp,'两参与且均分关闭，各仍600基础。','各得121，不按人数暗除。')
Cc('GR-13',exp,'均分开两参与各600整除2=300。','整除5=60，同级因子1再+1=61。')
Cc('GR-14',exp,'兼任参与/共享且均分关优先参与全额。','不另加共享半额，仍121。')
Cc('GR-15',exp,'外层对方参与记录非空，但所记成员濒死使有效numPartic0。','均分关每个共享者得完整600，不论共享者1或2。','各121；从未有非空参与记录的对方不因本fixture绕外层门。')
Cc('GR-16',exp,'全队非参与非共享只半额300。','scaled整除5为60，同级因子1，不加参与/共享资格1。','只一个外层“其他”消息，个体消息被抑制。')
Cc('GR-17',exp,'EXPCHARM查Bag而非当前个体item。','121按3/2整数得181。')
Cc('GR-18',exp+'|G@held:self.triggerExpGainModifier|G@held:LUCKYEGG','当前合法物无经验handler回负，才回退initialItems。','初始LUCKYEGG完整handler对经验取3/2整数；合法无handler不阻止回退。')
Cc('GR-19',exp+'|G@exp:pbLearnMove','实际增长跨一级按逐级边界写exp/动画/等级，再calc、消息、新招。','仅当前在场成员调用levelup幸福，未上场成员不因拿经验同加。')
Cc('GR-20',exp+'|G@shadow:exp=','心阶段2且余量充足，实际121经Shadow exp=加saved_exp。','当前E保持、统计+121，提前返回不升级。')
Cc('GR-21',exp+'|G@shadow:exp=','最大经验夹限后实际10。','saved与统计仅各+10，当前E不变。')
Cc('GR-22',exp+'|G@shadow:exp=','Shadow心阶段4不进入获暂存exp分支。','无exp/统计增加，不按普通升级路径提交。')
Cc('GR-23',ev,'病毒阶段>=1含已治愈，产出1先倍2。','之后逐stat仍夹252单项及510总额，合法余量足写2。')
Cc('GR-24',ev,'现单项252使剩余空间0，evGain夹0。','总510同使剩余总额0，不能把facility255异常输入偷换为本合法边界。')
Cc('GR-25',learn+'|ST@moveall:WHOLE','满槽替换先建新Move，新total12。','machine且keepPP真才把当前PP设min旧5/新12=5。')
Cc('GR-26',learn+'|ST@moveall:WHOLE','非machine不进入保旧PP窄分支。','新对象current/total都按其初始总12，不继承旧5。')
Cc('GR-27',learn,'通用满槽按实际两次确认都放弃。','未到数组替换写点，返回false、招式集保持；不冒Battle/外重学整体false。')
Cc('GR-28',learn,'通用学习先拒蛋(非Debug)/Shadow并提示false。','没有新Move/slot写入；裸Battle学习没有同一前门。')
Cc('GR-29',relearn,'L20<=当前30且未会的等级招进入，首现去重。','配置开时first的合法未会A且不与等级候选重复才前置。','蛋/Shadow返回空，不等同空UI安全。')
Cc('GR-30',relearn,'非空且首次绘制正常，拒教招仅回列表循环。','未整流返回false或增提醒统计。')
Cc('GR-31',relearn+'|'+learn,'内层满槽放弃使pbLearnMove false。','原招式保持，重学继续列表而不退出。')
Cc('GR-32',relearn+'|'+learn,'之后另一招成功教学才提醒统计+1。','结束Scene正常后整体true；后SceneEnd失败可保学招/统计前缀。')
Cc('GR-33',relearn,'列表取消但不确认退出，继续循环。')
Cc('GR-34',relearn,'列表取消且确认退出，Scene结束后false。','提醒统计不增加。')
Cc('GR-35',happy,'h80的walking基础2，同取得地图+1，豪华球+1。','正增4乘铃1.5得6，软限关后h86。')
Cc('GR-36',happy,'以原行给定正增量2进入软限，h175剩余4，增2保持而得177。','h180>=179令正增量0。','不外推另加地图/球/铃的其它fixture仍177。')
Cc('GR-37',happy,'h250档2 faintbad为-10。','负值不受正修正/软限，夹后240。')
Cc('GR-38','G@items:pbUseEVRaisingItem|ST@effects:VITAMINS_AND_HPFEATHER|'+happy,'羽毛传no_ev_cap真，100+1合法到101。','实际EV增长才wing；h80无额外修正+3到83。')
Cc('GR-39','G@items:pbUseEVRaisingItem|ST@effects:VITAMINS_AND_HPFEATHER','单项252导致首次增量0，effect false。','不调用wing，h80保持；正常调用者不消耗。')
Cc('GR-40','G@items:pbUseEVRaisingItem|ST@effects:VITAMINS_AND_HPFEATHER','总额510把本次增量夹0，即使该项100。','不调用wing，h80保持。')
Cc('GR-41','X@ball:onCatch|X@ball:FRIENDBALL|S@catch:pbThrowPokeBall:0','捕获成功先经OnCatch dispatch指定FRIENDBALL handler。','软限开直接h150，关h200；不是LUXURYBALL正增+1。')
Cc('GR-42','G@pokemon:affection_level','h150/200/230/255阈值档分别2/3/4/5。','为派生值，非独立持久affection字段。')
Cc('GR-43','G@items:pbGainExpFromExpCandy|G@items:pbChangeExp','目标未满级且非Shadow，数量3先额外2次vitamin。','ChangeExp升分支再1次，共3，一次设置流/后跨级学习进化依实际升等。')
Cc('GR-44','G@items:pbChangeLevel','目标降到15走降级消息/负差异窗。','无幸福增量、新招或进化检查。')
Cc('GR-45',exp,'L2×base39=78，先floor78/5=15。','(14/15)^2.5约0.841573，floor12.6236=12再+1=13。','E27→40仍L3，统计13，前EV保；延迟整除错14，关scaled得11/E38。')
Cc('GR-46',exp,'a1两参与split各floor1/2=0，基础<=0早返早于Trainer/scaled+1。','EXP/统计保持，先EV不回滚。','a2各基础1非零，scaled floor1/5=0后仍资格+1得1。')
Cc('GR-47',exp,'a39两参与一共享且兼任split，分别floor39/4=9与floor39/2=19。','先各截断再和28，不先实数和29.25取29。','scaled同级floor28/5=5再+1=6；split关兼任只39。')
Cc('GR-48',exp+'|G@held:LUCKYEGG','11→Trainer floor16→非scaled floor/7=2→异语言floor3。','BagCharm floor4→LuckyEgg floor6→affection floor7。','E27→34/L3、统计7；关affection6，去Charm而LuckyEgg/affection保得4，不能合并倍率。')
Cc('GR-49',relearn+'|W@pokemon:compatible_with_move?','BULBASAUR该L5等级未会候选空；egg_moves含AMNESIA只证明兼容，非提醒候选自动来源。','first[AMNESIA]且额外开才[A]，其它三组空；完整raw沿ST与W两包绑定。')
Cc('GR-50',relearn,'CATERPIE/MAGIKARP给定默认招均已会而first空，领域候选空。','无预检直接UI首次strict nil身份失败早于BACK/USE，既无整体false保证也无学习/统计。','候选非空且首次绘制成功才适用GR30–34；调用方拦截不进入失败。')
Cc('GR-51','UI@S09|UI@S10|UI@S13|G@items:pbForgetMove|G@exp:pbLearnMove|'+learn,'两包装都单个体Summary4旧+1新，非HM槽1返回1。','BACK/第五新招返-1；非Debug旧HM槽0提示留循环，Debug可0。','Battle替换同步场上新PP；通用machine keepPP仅窄分支，UI相同不合并提交。')
Cc('GR-52',relearn,'合法不同M1/M2等级候选先首现去重。','first合法不同M3额外开得[M3,M1,M2]。','first[M1,M1]不前置重叠，得[M1,M2]；配置关不加M3，不能无条件2+1。')
Cc('GR-53','W@party:pbChooseAblePokemon|W@event:pbChoosePokemon|W@event:pbChooseAblePokemon|W@event:pbChooseNonEggPokemon|W@utility:pbSet','唯一蛋不满足!egg&&hp>0，注解不可选，选择继续。','BACK写变量-1/名称空；非蛋HP1可选，HP0拒。','NonEgg另一选择器允许HP0；事件实际调用未证，不造“唯一合格蛋”。')
for n,val,out in [(1,'256','256'),(2,'255','255'),(3,'omitted','70'),(4,'0','0')]:Cc(f'R6-U14-GR{n:02}','HP@species:self.schema|HP@parser:get_csv_record|HP@parser:cast_csv_value|HP@compiler:validate_compiled_pokemon|HP@compiler:validate_all_compiled_pokemon|HP@species:initialize|HP@pokemon:initialize',f'合法作者Happiness {val}，原CI完整前提全部保留。',f'成功创建前后物种/个体都{out}，观察在任何后续change之前，未被UI编辑器255域自动夹。')
Cc('R6-U14-GR05',happy,'合法h254属档2，walking基础1且无额外修正/软限。','正常完成h255；异常未到末端不保证夹限，不提前修正创建fixture。')
chg='G@items:pbChangeExp'
Cc('U03-EX01',chg,'Medium L3 E27请求28，提示先获1而此时E仍27。','返回后E28/vitamin一次h85/calc/refresh，同L3早退无窗学招进化；队伍与普通消息receiver不同而顺序相同。')
Cc('U03-EX02',chg,'E28请求27先失1消息，提示时E28。','随后E27/calc/refresh，同L3早退，h80不增，无窗学招进化。')
Cc('U03-EX03',chg,'目标先夹，27请求27或E0请求-1都同值。','未变化消息后早退，无重算刷新/h/窗/学招/进化，不按原-1报失1。')
Cc('U03-EX04',chg,'L100 E1000000请求1000001先夹1000000，同值早退。','E999999请求1000001目标1000000，先差1消息，再提交/vitamin/calc/refresh/L100窗学习/进化检查。','超限1不算入差量，不保证资格进化必发生。')
Cc('U03-EX05',chg,'E1请求-4先夹0，先失1而非5消息。','随后E0/calc/refresh同L1早退且h不变，无窗学习进化；提示/资源故障会话回滚未知。')
assert len(claims)==63
formal='deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md';fr=(B/formal).read_bytes();fl=fr.decode().splitlines();rows={}
for i,l in enumerate(fl,1):
 m=re.match(r'\| (GR-\d+|R6-U14-GR\d+|U03-EX\d+) \|',l)
 if m:rows[m[1]]=(i,l)
assert set(rows)==set(claims);records=[]
for v,ss in claims.items():
 line,row=rows[v];records.append(dict(id='GCV-'+v,vector=v,formal=dict(path=formal,line=line,complete_raw_row=row),premise='完整原行、GR08基准及各EX/CI共同前提全保；每行独立复位，raw/普通/Shadow、已到参与记录、合法数据与指定配置各自限定；source/场景/提示依赖正常至所述观察点。独立数学非target执行。',complete_source_unit_refs=refs[v],child_assertions=[dict(id=f'GCV-{v}-A{i:02}',meaning=s,complete_source_unit_refs=refs[v],status='MANUALLY_JOINED_BOUNDED_STATIC',whole_parent_acceptance=False) for i,s in enumerate(ss,1)],normal_failure_cancel='先EV再EXP、先消息再辅助提交、先slot替换再后消息/统计/SceneEnd/外层消费各依实际单位。取消只阻未到分支，不撤既有EXP/EV/h/学招/统计；合法前门失败与native后段未知分列。',persistence='Pokemon持久EXP/levelcache/EV/MovePP/happiness与first_moves，Battle临时同步和UIreceiver另由完整单位接合；Save17对象图仅有限已接静态合同，未执行dump/load。',remaining=['63完整有限向量均人工拆；其余BG/IU/SH/DC主责不借此批准，全域/历史/host结果未冻结。'],accepted=False))
ci_path='deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md';ci=(B/ci_path).read_text().splitlines();out=dict(schema='gr8-crec-growth-catalog63/v1',recorded_utc=utc,actual_reader=reader,formal_identity=dict(path=formal,bytes=len(fr),sha256=hashlib.sha256(fr).hexdigest(),current_read_chunks=['830d4c','c8161b']),complete_common_premises=[dict(line=i+1,text=l) for i,l in enumerate(fl) if l.startswith('共同前提：合法普通非蛋非 Shadow CATERPIE') or l.startswith('全部DERIVED_VECTOR／NOT_EXECUTED_THIS_UPDATE')],complete_CI_parent_common=dict(path=ci_path,line=322,text=ci[321],actual_read_chunk='af9f3a'),mandatory_complete_source_packet_bindings=bindings,extra_source_identity=dict(path=ballpath,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_reader=reader,credit='PARTIAL_COMPLETE_onCatch/FRIENDBALL only',actual_read_chunk='35768f'),complete_extra_source_units=extra,complete_selected_UI_reception=dict(parent_path=str(ui_path),parent_bytes=ui_path.stat().st_size,parent_sha256=hashlib.sha256(ui_path.read_bytes()).hexdigest(),original_reader='/root/ui_wp66',own_prior_full_A_finite_reception=True,complete_units=selected,source_FULL_transferred=False),records=records,manual_atoms=sum(len(x['child_assertions']) for x in records),pure_arithmetic_check=dict(GR45=math.floor((78//5)*((14/15)**2.5))+1,GR47=(39//4+39//2)//5+1,GR48=7,qualification='Independent arithmetic only, no Ruby/game/runtime simulation.'),new_contexts=0,new_votes=0,whole_domain_acceptance=False,denominator_frozen=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
p=C/'growth-catalog63-meaning.v1.json';assert not p.exists();wr(p,out);rv=rd(C/'reverse-mapping.json');assert not any(x['id'].startswith('GCV-') for x in rv['records']);rv['records'].extend(records);rv['utc']=utc;wr(C/'reverse-mapping.json',rv);pr=rd(C/'progress.json');pr['updated_utc']=utc;pr['primary_clause_atoms']=sum(len(x.get('child_assertions',[])) for x in rv['records']);wr(C/'progress.json',pr);print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),groups=63,children=out['manual_atoms'],total_groups=len(rv['records']),total_children=pr['primary_clause_atoms'],utc=utc)))
