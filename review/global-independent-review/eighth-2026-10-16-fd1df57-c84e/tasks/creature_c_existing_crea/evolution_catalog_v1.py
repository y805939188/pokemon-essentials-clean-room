import json,re,hashlib,datetime,subprocess
from pathlib import Path
P=Path(__file__).parent;R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception';rc='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';bc='fd1df570cad987dc3852a3b958f03916e317f7fe'
fpath='deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md';raw=(B/fpath).read_bytes();assert raw==subprocess.check_output(['git','-C',str(B),'show',bc+':'+fpath]);ft=raw.decode();table={}
for i,line in enumerate(ft.splitlines(),1):
 m=re.match(r'^\| ((BE|CX|RM|CP)\d+) \|',line)
 if m:table[m.group(1)]=dict(line=i,complete_raw_row=line)
assert len(table)==140
packnames=['wp31-registry-meaning-atoms.v1.json','wp31-wrappers-commit-meaning.v1.json','wp32-context-meaning.v1.json','battle-consumer-delta.v1.json'];packets={n:json.loads((P/n).read_text()) for n in packnames};bindings=[]
for n in packnames:
 r=(P/n).read_bytes();bindings.append(dict(path=n,bytes=len(r),sha256=hashlib.sha256(r).hexdigest(),actual_reader=reader,credit='OWN_PREVIOUS_COMPLETE_DEFINITIONS_AND_MANUAL_MEANINGS_REUSED_NO_NEW_REVIEWER'))
identities={};units=[]
select={
 'wp31-registry-meaning-atoms.v1.json':{'C31-REG-Level','C31-REG-Silcoon','C31-REG-Cascoon','C31-REG-AttackGreater','C31-REG-AtkDefEqual','C31-REG-Item','C31-REG-HoldItem','C31-REG-TradeItem','C31-REG-TradeSpecies','C31-REG-Event','C31-REG-EventAfterDamageTaken','C31-REG-BattleDealCriticalHit','C31-REG-Shedinja'},
 'wp31-wrappers-commit-meaning.v1.json':{'pokemon:check_evolution_internal','pokemon:check_evolution_on_level_up','pokemon:species=','pokemon:action_after_evolution','pokemon:trigger_event_evolution','pokemon:clone','species:get_evolutions','ui:self.pbDuplicatePokemon','ui:pbStartScreen','ui:set_up_animation','ui:pbEvolution','ui:pbFlashInOut','ui:pbEvolutionSuccess','ui:pbEvolutionMethodAfterEvolution','ui:pbEndScreen','utilities:pbLearnMove','utilities:pbChangeLevel','utilities:pbChangeExp','utilities:pbUseItem','utilities:pbUseItemOnPokemon','effects:RareCandyMaximum','effects:RareCandy','effects:EvolutionStones'},
 'wp32-context-meaning.v1.json':{'time:pbGetTimeNow:0','time:self.isDay?:0','time:self.isNight?:0','time:self.isMorning?:0','time:self.isAfternoon?:0','time:self.isEvening?:0','screen:weather:0','metadata:has_flag?:0','trade:pbStartTrade:0','trade:pbStartScreen:0','trade:pbTrade:0','trade:pbEndScreen:0','pokemon:hp=:0','pokemon:heal:0','evolution:pbEvolutionEvent:0','catch:pbStorePokemon:0','catch:pbRecordAndStoreCaughtPokemon:0','sprite:pbDisposeSpriteHash:0','sprite:pbDisposeSprite:0','sprite:pbDisposed?:0','message:pbDisposeMessageWindow:0','trainer:pokemon_party:0','trainer:able_party:0','party:pbChooseTradablePokemon:0','party:pbChooseTradablePokemon:1','party:pbChoosePokemonForTrade:0','world:set_weather'},
 'battle-consumer-delta.v1.json':{'world:after_battle','world:pbEvolutionCheck','world:set_up_player_trainers','world:partner_can_participate?','world:event:record_party_status','world:event:evolve_and_black_out','startend:pbEndOfBattle','change:pbFaint','usage:pbRecordDamageLost','usage:pbReduceDamage','usemove:pbConfusionDamage','usemove:pbProcessMoveHit'}}
for n,d in packets.items():
 arr=d.get('whole_source_units',d.get('complete_source_units',d.get('source_units',[])));known={x['id'] for x in arr};assert select[n]<=known,(n,select[n]-known)
 for u in arr:
  if u['id'] not in select[n]:continue
  v=dict(u);v['id']=n+'/'+u['id'];v['original_packet']=n
  if 'source_identity_key' in u:
   key=n+'/'+u['source_identity_key'];v['source_identity_key']=key;identities[key]=d['source_identities'][u['source_identity_key']]
  else:
   v['source_identity_boundary']='Evolution registry source identity and full actual source read retained inside original packet source_units; no transferred provider FULL.'
  units.append(v)
def fresh(k,path,names=None,whole=False):
 r=(R/path).read_bytes();assert r==subprocess.check_output(['git','-C',str(R),'show',rc+':'+path]);s=r.decode('utf-8-sig').replace('\r\n','\n');identities[k]=dict(path=path,bytes=len(r),sha256=hashlib.sha256(r).hexdigest(),git_blob=subprocess.check_output(['git','-C',str(R),'rev-parse',rc+':'+path],text=True).strip(),lines=len(r.splitlines()),actual_reader=reader,credit='OWN_FULL_ACTUAL_READ' if whole else 'OWN_COMPLETE_NAMED_UNITS_REUSED_FROM_OWN_FULL_FILE' if k in ['storage','pokemon'] else 'OWN_COMPLETE_NAMED_UNIT_ONLY')
 if whole:units.append(dict(id=k+':WHOLE',source_identity_key=k,range=[1,len(r.splitlines())],text=s,complete_source_file=True))
 for name in names or []:
  m=re.search(r'^( *)def '+re.escape(name)+r'(?=[( ;\n])[^\n]*\n',s,re.M);assert m,(k,name);z=m.end() if '; end' in m.group(0) else m.end()+re.search(r'^'+m.group(1)+r'end\s*$',s[m.end():],re.M).end();units.append(dict(id=k+':'+name,source_identity_key=k,range=[s.count('\n',0,m.start())+1,s.count('\n',0,z-1)+1],text=s[m.start():z],complete_definition=True))
 return s
fresh('picture','Data/Scripts/005_Sprites/010_PictureEx.rb',whole=True);fresh('ruby','Data/Scripts/001_Technical/002_RubyUtilities.rb',['lerp']);fresh('storage','Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',['pbCopy','pbMoveCaughtToBox','pbStoreCaught']);fresh('pokemon','Data/Scripts/014_Pokemon/001_Pokemon.rb',['gender','singleGendered?','getMoveList'])
raw_records=[]
for key,path,headers in [('pbs_species','PBS/pokemon.txt',['IVYSAUR','VENUSAUR']),('pbs_move','PBS/moves.txt',['PETALBLIZZARD'])]:
 s=fresh(key,path)
 for header in headers:
  m=re.search(r'^\['+header+r'\][^\n]*\n',s,re.M);assert m;n=re.search(r'^\[',s[m.end():],re.M);z=m.end()+n.start() if n else len(s);raw_records.append(dict(id=key+':'+header,source_identity_key=key,range=[s.count('\n',0,m.start())+1,s.count('\n',0,z-1)+1],text=s[m.start():z],complete_raw_record=True,actual_reader=reader))
claims={}
def C(i,*v):claims[i]=list(v)
C('BE01','达到L16使Level16的谓词真。','首目标正常演化成功后才改变species。')
C('BE02','L15不满足Level16。','无其它命中条目时返回nil且不调用提交。')
C('BE03','仅PID的高16位值对10余数小于5时Silcoon可命中。','10000指该高16位数值的样本而非把整个PID10000直接代入。')
C('BE04','高16位值10005的余数5使命中Cascoon分支。','与Silcoon的余数小于5条件互斥。')
C('BE05','攻60大于防40命中AttackGreater。','攻防相等命中AtkDefEqual而不命中AttackGreater。')
C('BE06','使用物WATERSTONE与Item参数相等使该道具家族命中。','道具wrapper不调用Location等level_up家族谓词。')
C('BE07','egg?在共同第一守卫返回nil。')
C('BE08','Shadow在共同第一守卫返回nil。','实际石头/糖果handler还各自给Shadow拒绝消息。')
C('BE09','Everstone共同守卫早于道具族回调。','handler没有目标返回false所以正常外层不扣石。')
C('BE10','BattleBond能力共同守卫早于所有族扫描。')
C('BE11','允许取消的动画BACK分支累计取消计数。','成功提交未调用而species保持。','取消保留先前caller等级和学习写入。')
C('BE12','石头和交换调用Evolution(false)。','BACK不能在该演化动画中设置canceled真。','本行的只能完成提交以其余依赖正常返回为前提，不保证异常后仍完成。')
C('BE13','满级候选存在且配置允许时默认演化仍可取消。','演出正常返回后handler为true。','普通consumed-after-use糖果由外层扣除，即使取消也不退。')
C('BE14','满级没有level-family目标时handler显示no-effect。','该分支返回false阻止外层扣除。')
C('BE15','Happiness谓词自身只有友好阈值而无刚升级历史门。','满级糖果直接调用level-family可得到其目标。')
C('BE16','成功计数早于成功消息。','消息早于进化后动作。','后动作早于species写入。','species写入早于Dex登记。','Dex登记早于进化学习。')
C('BE17','IVYSAUR完整Moves字段没有0,PETALBLIZZARD。','VENUSAUR完整Moves首项是0,PETALBLIZZARD。','成功物种变更后getMoveList读目标记录，level0项可学习，已知则静默跳过。')
C('BE18','满槽遗忘/放弃发生在species和Dex提交后。','拒绝这次学习不恢复进化前species或已完成的Dex。')
C('BE19','真实base species变化且目标无default/nonzero form时保留stored form。','真实变化清forced_form。')
C('BE20','真实species变化到单性别/无性别目标清gender缓存。','后继gender读取按目标gender_ratio派生。')
C('BE21','取消分支不调用pbEvolutionSuccess。','因此成功统计未增。','因此成功音效消息未运行。','因此持物/复制后动作未运行。','ready标记不由本取消分支清除。')
C('BE22','Ninjask是level目标，Shedinja是旧Nincada后动作条目。','party5在默认容量6下通过space门。','有POKEBALL才追加清昵称/标记/持物/缎带、普通球且满血的clone。','先append和Dex再扣球，正常后原个体继续提交Ninjask。')
C('BE23','默认party6使Shedinja回调第一门返回false。','原Ninjask提交继续。')
C('BE24','有space但无球使第二门返回false。','不追加、不消费球。')
C('BE25','HoldItem after-action要求真实target相等。','仍持required item才清持有。','不匹配返回false继续扫描。')
C('BE26','默认允许fainted成员进入战后检查。','Success记录原fainted后在species=之后再次hp=0。')
C('BE27','默认CHECK_EVOLUTION_AFTER_ALL_BATTLES允许决定2败北。','关闭时只对决定2或5早退，不能推广所有非胜局皆跳过。')
C('BE28','队伍逐个成员各建演化演出。','一次正常取消不终止后续成员循环。')
C('BE29','D>=49的战后EventAfterDamageTaken只设R并返回false。','后续正确编号且R真才返回事件目标。','成功提交清R。')
C('BE30','全队事件入口able_party排除蛋。','able_party排除当前fainted。')
C('BE31','每个合格成员独立触发同一number。','未维护全局已消费number集合。')
C('BE32','正常取消未改species/R时可以重试相同number。')
C('BE33','number不同于parameter使事件谓词false。','number没有在失败时被消费。')
C('BE34','None由get_evolutions(true)过滤。','没有其它命中条目时不产生目标。')
C('BE35','TradeItem清正在演化的收到者item。','对等方不是该消费的receiver。','目标不匹配不消费。')
C('BE36','StartScreen target最初visible=false。','PictureEx首轮启动delay0 visible=true/white alpha255/zoom0。','delay40按每秒20单位等于约2秒时开始目标放大。','第一段zoom12单位约0.6秒，约2.6秒出现大轮廓。','成功flash选择target并把zoom归1、white alpha归0。','所有结论依赖有效非透明资源和正常host时间推进，不冒像素观察。')
C('BE37','看到目标白轮廓后接受BACK仍可恢复旧sprite并隐藏target。','恢复不抹除此前已经呈现的白轮廓属性序列。','成功model未运行而取消统计增加。','更早取消可以不抵达首个目标放大。')
C('CX01','9时morning与day同时真。','10时只有day。','14时afternoon与day同时真。','17时evening与day同时真。','20时night真。')
C('CX02','未提供Time参数时检查读取当时Time.now而非开场快照。','已经选定目标后Success不重跑时段条件。')
C('CX03','LevelRain读$game_screen.weather_type类别，并显式接受Fog。','战斗Rain不替代世界None。')
C('CX04','Screen nil时天气族门短路不命中。','非None未知weather类别lookup可以失败。','NoWeather只做None身份比较。')
C('CX05','028完整map记录MossRock满足map metadata flag门。','谓词没有坐标或交互要求。','地图真实可达仍非本静态记录证明。')
C('CX06','当前map元数据缺时flag/region可返回false。','当前$game_map缺时读取map_id可失败。')
C('CX07','Region取当前map TownMapPosition[0]。','不读取当前图鉴观看区域或解锁状态。')
C('CX08','pokemon_party排除蛋而保留fainted成员。','伙伴的独立队伍不加入该玩家类型扫描。')
C('CX09','开始通知L0映射实际玩家队伍levels。','K/D按同一玩家队伍长度填0。','伙伴不是这些初始表成员。')
C('CX10','有效每击calcDamage>0且critical时增加攻击者K。','pbHitEffectivenessMessages的critical记录不以substitute为拒绝门。','画皮哨兵路径没有实际critical真则不增加。')
C('CX11','K记录按玩家拥有攻击者而无对立目标门。','因此满足前提的友方要害也增加K。')
C('CX12','pbRecordDamageLost把本击hpLost加到玩家目标D。','该hpLost可来自替身。','30+19等于49而本体HP可以不变。')
C('CX13','confusion自伤也调用damage记录入口。','目标为玩家自身和友方来源不取消D记录。','毒残余没有这次招式记录调用。')
C('CX14','普通计划损失先截HP并应用撑住。','HP20留1使hpLost19进入D，不是100。','真faint路径再清D。')
C('CX15','真faint把D槽归0。','真faint不清K。','hp=0清ready标记。')
C('CX16','正常治疗没有从D扣恢复量。','普通换出没有清成就D表。','30+19仍49，只要之间未真faint。')
C('CX17','每场开始重建D零表。','两场48与1不能跨场相加。','既有R与当前D不同字段。')
C('CX18','默认配置下普通世界after-battle通知不按1/2/3/4/5/0全排除扫描。','决定0需要实际世界返回并触发通知；准入跳过不是同一前提。')
C('CX19','配置关闭时2与5提前跳进化。','3/4/0仍到达检查。','正常通知后清L0/K/D。')
C('CX20','世界可输败局治疗先于进化通知。','检查读取此时fainted，治疗后的成员不因入战前濒死被拒。')
C('CX21','先升级族命中使战后族不再查询。','取消已经选定的升级演化不会回退重选战后族。','正常后续仍清K/D。')
C('CX22','显式容量3使[A,B,C]确实满而进入替换。','送走A使当前party成为[B,C,X]。','L0/K/D各左移对应B/C，X尾槽为nil。','B保其旧K3/D49，不能按新索引错误归A。')
C('CX23','先送盒的旧成员不在后续玩家party扫描。','R尚false不因该次D49自动在盒中变真。','存盒保存恢复R不保存临时D表。')
C('CX24','不替换旧party时不左移三表。','捕获者送盒不进入当前party进化扫描。')
C('CX25','低D分支没有清旧R真。','Everstone统一守卫使未准备者连战后置R回调都到不了。')
C('CX26','Yamask1事件param2不匹配number1。','R真且number2命中目标。','正常取消保持R和旧species，可以重试2。')
C('CX27','trigger_event_evolution的true表示找到目标并正常返回演出。','取消时true也不表示species已经提交。')
C('CX28','事件全队遍历预选able_party。','第一成员正常取消不消费编号或阻断第二成员。')
C('CX29','全队事件入口排除蛋/fainted。','裸单成员trigger没有额外alive门，但仍受共同egg/Shadow/石/能力门。')
C('CX30','收到Poliwhirl的KINGSROCK满足TradeItem。','Success旧条目after-action先清收到者持物。','外层最后才用收到者替换party槽。')
C('CX31','实际TradeSpecies比较收到者自身species与其参数。','默认Karrablast/Shelmet参数是对方species，两个比较均false。','普通交换接收与此进化失败是不同结果。')
C('CX32','自定义参数等于收到者自身时第一比较通过。','只要旧送出者没有Everstone即可，不再要求其species。')
C('CX33','收到者自己的Everstone由共同门先拒。','交换最后接收该对象仍可继续。')
C('CX34','选择器取消写负下标/空名，由事件caller决定不调用交易。','启动交易没有交互取消分支。','其交换演化显式false不可动画取消。')
C('CX35','Dex页条件成立时pbTrade可先调用EndScreen(false)。','外层固定再调用EndScreen。','viewport第二次dispose发生在第二次进化检查前。','宿主重复dispose是否正常未知，不能保证双进化。')
C('CX36','特定存盒路径heal前存R、heal后恢复同值。','普通Pokemon.heal清R。','这些操作与D战斗表保存没有等价关系。')
C('CX37','Shedinja副本在当前party末尾追加。','后续HasInParty读取已经变化的party。','新副本没有开始L0/K/D槽，不继承原成就。')
C('CX38','正常取消使world通知继续到三表清理。','异常没有正常返回就不保证后段清理。','没有在此finally或回滚已进化成员。')
C('CX39','默认容量6时3成员party不满。','捕获X直接append而不进入替换。','旧三槽不移，新索引3缺失。')
C('CX40','实际partner参与时setup创建新merged数组而保留旧Pokemon引用。','捕获替换仅改实际玩家party和其initialItems记录，不改旧merged身份序。','A送盒仍同对象，normal ending按旧merged索引把新记录Y写给盒A。','留队B在旧merged索引1读到空记录而被清持物。','后续进化持物谓词读当前实际item，不能读原X/Y快照。')
C('CX41','无partner共同使用玩家party数组。','delete/append也改变终局遍历身份。','送盒A已离开该循环而保持X。','留队B与左移Y记录对应。')
C('CX42','送中间C时merged仍旧A/B/C/D/E/F。','玩家记录左移使旧C索引2变W，旧D索引3变空。','同对象盒C被写W、留队D被写空。','A/B索引未变，仍X/Y。')
assert set(claims)=={f'BE{i:02}' for i in range(1,38)}|{f'CX{i:02}' for i in range(1,43)}
rows=[]
for ordinal,(vector,cs) in enumerate(claims.items(),1):
 source_packages=['wp31-registry-meaning-atoms.v1.json','wp31-wrappers-commit-meaning.v1.json'] if vector.startswith('BE') else ['wp32-context-meaning.v1.json','battle-consumer-delta.v1.json']
 if vector in ['BE26','BE27','BE28','BE29']:source_packages+=['battle-consumer-delta.v1.json']
 if vector in ['BE35','CX25','CX26','CX27','CX29','CX30','CX31','CX32','CX33','CX37']:source_packages+=['wp31-registry-meaning-atoms.v1.json','wp31-wrappers-commit-meaning.v1.json']
 rows.append(dict(id='CEV-'+vector,vector=vector,formal=dict(path=fpath,**table[vector]),premise='完整原行前提全部保留；共同固定R与合法当前对象、默认/人工/可选数据各按原行，不偷换来源。前序资源/数据/消息/host步骤须正常至声明观察点，无额外callback改写。',child_assertions=[dict(id=f'CEV-{vector}-A{i:02}',meaning=c,source_complete_packages=source_packages,source_unit_receiver='完整selected_source_units及各原包中具名完整定义，按本向量具体producer/caller/receiver组合；不是仅按命中range赋PASS。',status='MANUALLY_DERIVED_BOUNDED_STATIC',whole_parent_acceptance=False) for i,c in enumerate(cs,1)],normal_cancel_failure='保原行的正常/取消/失败输入差异。只到达的写入保留；异常不保证后来模型/Dex/消息/容器/清理，取消只阻止未进入的提交段。实际例不承诺资源/宿主/随机/保存成功。',remaining='完整事件demo调用/host像素/回放/保存重载和所有非本行组合仍OPEN。',accepted=False))
neighbors=[dict(vector=k,formal=dict(path=fpath,**v),disposition='COMPLETE_CATALOG_CONTEXT_READ_NEIGHBOR_PRIMARY_NOT_TRANSFERRED',C_credit='Only explicit actual C producer/receiver meanings in existing bounded packages; no RM/CP whole PASS.',open='RM完整漫游/雷达及CP完整捕获数值/球handlers/caller仍由相应primary实际审读；本次不拿wholecatalog读取代其完整sourcefacts/consumer或既有root资格。') for k,v in table.items() if k.startswith(('RM','CP'))]
out=dict(schema='gr8-cre-c-evolution-catalog79/v1',recorded_utc=utc,actual_reader=reader,formal_identity=dict(path=fpath,commit=bc,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),actual_full_read_chunks=['5c3e1a','aa0d5b']),bindings=bindings,source_identities=identities,selected_source_units=units,complete_raw_records=raw_records,records=rows,manual_atoms=sum(len(r['child_assertions']) for r in rows),catalog_neighbor_dispositions=neighbors,new_source_full_read=dict(picture=dict(path='Data/Scripts/005_Sprites/010_PictureEx.rb',lines=548,actual_full_chunks=['55920f','3bee34','4795a7'])),actual_raw_chunks=['46ca6a','6d740e'],actual_storage_reread=['79cc0e','9f5194'],denominator_frozen=False,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
f=P/'evolution-catalog79-meaning.v1.json';assert not f.exists();f.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');rv=json.loads((P/'reverse-mapping.json').read_text());assert not any(r['id'].startswith('CEV-') for r in rv['records']);rv['records']+=rows;rv['utc']=utc;(P/'reverse-mapping.json').write_text(json.dumps(rv,ensure_ascii=False,indent=2)+'\n');pr=json.loads((P/'progress.json').read_text());pr.update(updated_utc=utc,primary_clause_atoms=sum(len(r.get('child_assertions',[])) for r in rv['records']));(P/'progress.json').write_text(json.dumps(pr,ensure_ascii=False,indent=2)+'\n');ld=json.loads((P/'reading-ledger.json').read_text());ld['discovered_dependencies'].append(dict(**identities['picture'],current_status='FULL_READ_CURRENT_SCOPE',recorded_utc=utc,actual_full_chunks=['55920f','3bee34','4795a7'],new_votes=0));(P/'reading-ledger.json').write_text(json.dumps(ld,ensure_ascii=False,indent=2)+'\n');r=f.read_bytes();print(json.dumps(dict(utc=utc,bytes=len(r),sha256=hashlib.sha256(r).hexdigest(),manual_groups=len(rows),manual_atoms=out['manual_atoms'],complete_source_units=len(units),raw_records=len(raw_records),neighbor_vectors=len(neighbors),current_manual_total=pr['primary_clause_atoms'])))
