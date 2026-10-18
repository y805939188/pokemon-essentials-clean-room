import json,pathlib,datetime,hashlib,subprocess
p=pathlib.Path(__file__).parent
inv=json.loads((p.parent.parent/'delegation/readsets/ui_full.json').read_text());deps=json.loads((p/'dependency-identities.json').read_text())
by={x['path']:x for x in inv['reference']};by.update({x['path']:x for x in deps['records']})
def ref(i):return inv['reference'][i]['path']
phone='Data/Scripts/013_Items/004_Item_Phone.rb';system='Data/Scripts/004_Game classes/002_Game_System.rb'
units=[
('Pokégear列表构造与显示',ref(26),[1,129],[
'按钮绘制选择/未选择使用不同背景，图资源经INTL路径；女性变体先解析存在才选。','列表经MenuHandlers.each_available生成一次并保存commands，后续不是每轮重建条件。','总高按项目数×48计算后居中；初始选中0。','列表不足2项，UP/DOWN不移动也不播游标音。','关闭按正常fade/dispose/viewport尾部执行，没有通用异常回滚。']),
('Pokégear调度与三个默认入口',ref(26),[130,206],[
'主循环BACK>USE>UP>DOWN，全部trigger，只执行一个分支。','BACK正常返回-1；USE调用当前菜单项effect，truthy则break并销毁。','Map处理器打开非wallmap，得到非空目的地时先写fly_destination，关闭当前按钮画面并返回99999。','Phone默认入口无联系人条件，直接进入PhoneScreen。','Jukebox入口打开点唱机后返回false以继续按钮循环。','Map哨兵是结束按钮画面的局部协议，不证明后续飞行执行完成。']),
('地图底栏与初始定位',ref(27),[1,110],[
'底栏文字写区域名、左下地点、右下详情，setter值相同不刷新。','先分配viewport与sprites，再查当前位置与TownMap。','当前位置无定位时回退0左上，优先于显式region参数。','有定位且请求非负、异于当前且已登记，才选择请求区域左上。','其它请求按当前位置区域/坐标；严格get对实际最终ID未知可先失败。','区域尺寸只用正宽及形状串长度算ceil高度，不按字符过滤。','玩家坐标按实际地图宽高整数比例floor加子格偏移。','地图数据假值才显示友好缺失提示；不能把UnknownID改为该提示。']),
('地图图层/玩家/飞行图标初始化',ref(27),[111,157],[
'附加图先同区域再location_shown?，固定实际默认两条隐藏地点开关51/52。','地图附图480×320，相对地图左上按16像素格偏移。','有当前位置且显示同区域才创建玩家图标。','遍历0..29×0..19的治疗点，只有visitedMaps为真才建飞行图标。','飞行点初始visible仅mode1；创建后播放两帧动画。','cursor依当前逻辑格定位并play；help刷新后才fadein。','资源请求与sprite状态不证明实际宿主像素/图存在。']),
('地图点查询与编辑保存',ref(27),[159,246],[
'结束正常fadeout→dispose sprites→dispose viewport。','坐标到屏幕以格16、半格偏移和地图居中偏移计算。','wallmap附图直接取字段5；普通附图要求字段1正且开关打开。','保存先TownMap.save再Compiler.write_town_map，第二失败不回滚第一次。','地点/详情/治疗点各自顺序扫描第一条同格记录，隐藏或缺字段立即空、不继续下一条。','点字段7存在时，wallmap/非正号/关闭开关任一即隐藏。','地点/详情普通模式走消息哈希，编辑器返回原始键。','治疗点只有字段4/5/6都truthy才给三元组。','编辑只有editor且points存在；文字最大250，返回非nil即改首点或追加并置changed。','flyhelp在非直接fly且设置与资格通过才更新；改变point可见性并重置frame0。']),
('地图循环移动与按钮优先级',ref(27),[248,321],[
'每轮Graphics→Input→sprites后先推进既有横纵插值。','任一偏移未归零则next，整轮不处理新方向和按钮。','可输入轮dir8先更新逻辑坐标并夹0..29×0..19，再写地点/详情。','方向改变当轮建立0.1秒插值起点但继续处理按钮。','按钮BACK>(USE且mode1)>(USE且editor)>(ACTION且全部资格)。','editor changed BACK依次保存确认、退出确认；未改直接break。','mode1 USE先查治疗点和visited/debugCTRL；直接fly无确认return，浏览fly要确认。','不合资格mode1 USE仍挡后面的ACTION分支。','mode0非editor USE不独立挡ACTION。','ACTION切换还要求CAN_FLY、非wallmap、非直接fly及pbCanFly?。','退出正常播close并nil，直接返回治疗点分支绕过close尾部。']),
('地图屏幕和公开包装',ref(27),[326,356],[
'FlyScreen用editorfalse/flytrue，MapScreen用DEBUG作为editor。','正常屏幕先start→loop→end，无ensure。','pbShowMap fade包装，只有ret且非wallmap才写临时目的地。','取消返回nil不覆盖旧fly_destination；不能外推为包装主动清旧目的地。']),
('电话列表布局与数据刷新',ref(28),[1,138],[
'PhoneList只在视窗内画行；移动选中行红字，游标图片临时AnimatedBitmap。','场景开时根据rematches_enabled决定是否创建逐行再战图标。','信号图标按Call.can_make?选择，不检查联系人距离。','pbRefreshList仅采visible联系人，显示display_name并统计can_rematch?。','列表超高索引夹至末项，top_row按页大小调整。','再战图标逐行清旧后按可见联系人can_rematch?重设。','训练家头像走charset_filename，NPC格式phone%03d；取四向行走图首格。','地图ID>0才显示地图名；无选中联系人清头像和底栏。']),
('电话移动模式/普通输入',ref(28),[139,200],[
'pbActivateWindow每轮sprites更新列表后，先比较新旧索引。','移动时用可见列表index直接delete_at/insert完整contacts，再pbRefreshList。','此直接索引事实不能外推隐藏联系人变体正确。','随后index设为当前，新索引决定USE记录。','移动模式ACTION或USE先落定，优先于BACK。','移动BACK先把完整contacts当前索引元素移回switch_index，再恢复列表索引与刷新。','普通模式ACTION>BACK>USE，ACTION进入移动并记起始索引。','正常BACK返回nil并播关闭；USE返回当前可见记录。']),
('电话命令与删除排序消费者',ref(28),[205,271],[
'打开只检查是否有visible联系人，不检查has_pokegear。','零可见只pbMessage后return，不创建scene。','命令Call/Delete/Sort/Cancel，Delete仅can_hide?；少Delete时映射cmd补1。','Call将现有Contact记录直接给make_outgoing，绕过缺失类get路径。','Delete先确认，再visible=false，再sort，再refresh，再提示；任一后续失败不回滚先前状态。','删光提示无号码后break并正常endScene。','按原名/显示名sort!后再visible优先稳定partition。','特殊联系人排序先NPC再Trainer，之后同样visible优先。']),
('联系人状态初始化/查询/预检',phone,[1,58],[
'初始联系人空，rematch_variant0，enabled按设置，calltime0.0,lastrefresh0。','实例get只匹配visible，trainer布尔须等值。','训练家匹配规范type+name+start_version，NPC按name。','get_version先规范TrainerType，有联系人取version，否则0。','can_add?先has_pokegear门；NPC名称或训练家type/name/start_version可见同键阻止。','未知TrainerType在预检返回false。']),
('联系人直接写入及排序',phone,[59,144],[
'add自身不调用can_add?，所以没有持工具门。','两个训练家分支都先类型存在检查并规范id。','事件形态查重把args3版本数当查询start_version，实际构造用args3版本数/args4起始。','显式map/event形态查重同样args4版本数进start_version，构造args4/args5。','可见同键复用记录移尾，隐藏同键不命中而另建。','普通NPC按map/name/common_event构造。','成功push后sort_contacts并true，visible优先partition保相对顺序。','rematch未启用或同整秒不处理。','可见Trainer且flag<=0才计时，<=0重抽20...40整数分钟×60后当次减1。','减到0时先flag1再写事件Afalse/Btrue/refresh，后续异常不回滚flag。','reset_after_win规范类型查记录，increment后flag0/time0。']),
('电话公开包装与反馈失败前缀',phone,[148,210],[
'类级enabled/variant直接代理全局phone字段。','get_trainer调用实例get(true)；can_add?代理实例预检。','普通add先实例写入，成功后以原输入未规范TrainerType查询反馈联系人。','文本型type可先成功写入、随后feedback contactnil.display_name失败；无回滚。','add_silent只代理实例add，没有反馈查询。','公开variant/increment把type身份错送实例get的trainer布尔位，正常类型不匹配，0/无动作。','battle先实例get(true)，无联系人false，有则TrainerBattle.start下一version。','reset_after_win代理实例重置。']),
('联系人记录语义',phone,[215,313],[
'训练家版本数至少1，起始默认0，当前等起始；time0/flag0/common_event0。','NPC common_event默认0；所有联系人visibletrue。','visible同值早返，隐藏训练家先写visiblefalse再time0/flag0/Atrue/refresh。','can_hide?等trainer?，common_event_call?仅ID>0。','can_rematch?仅trainer且flag>=1，不额外检查全局enabled。','display_name训练家类型名+消息姓名，NPC_INTL。','variant=current−start；next=start+min(variant+1,globalcap,versions_count−1)。','increment仅Trainer写next。','set_ready_event只写Afalse/Btrue/refresh，不改flag/time。']),
('电话呼叫门与随机联系人',phone,[318,408],[
'can_make?只拒NoPhoneSignal；缺metadata默认有信号。','can_call先contact非空，再信号，再NPC直接true，再Trainer同图拒绝、两图定位同region门。','呼入候选须Trainer/visible/异图/地图名不同/元数据定位同region。','无当前位置nil，无候选sample为nil，选到不等同拨打成功。','make_incoming先信号，再sample，公共事件ID>0分派，否则训练家生成并play。','正ID助手false才显示缺事件提示。','make_outgoing接受现有记录；按标识路径调用缺失Phone.get，在can_call之前失败。','显式raise只在取得contact假值后；不能把缺失Phone.get直接改为该raise。']),
('电话播放与占位',phone,[410,443],[
'先start_message，再无条件取得一次TP、一次TE和地图名，即使无占位也抽。','合法训练家gender设置为真时男\\b/女\\r，其它不加。','dialogue按\\m分段；每段替换TN/TP/TE/TM，前若非末段加控制字符。','同通各段TP/TE共用已取得值。','逐段pbMessage后end_message，正常透传末消息结果；无额外稳定boolean。','任一前置抽样/消息失败不保证后续Click或外层恢复。']),
('电话消息生成',phone,[447,504],[
'validate记录后查当前type/name/version，无则start，无则default。','每组随机一条，nil组或空抽样为文字空串，再走PHONE_MESSAGES哈希。','先通用intro，再Morning5..9/Afternoon14..16/Evening17..19非空替换。','10..13与20..4不替换intro。','启用且flag1时取request后写flag2；flag2取remind，nil组才回退request。','无再战分支：body1/body2都truthy且(no body或rand100<75)取两段，否则body。','end只在普通主体分支且非空才追加。','函数不播放；flag1→2即使随后播放失败已提交。']),
('电话队伍与遭遇采样',phone,[506,538],[
'TP非Trainer为空；版本max(current,start)，无Trainer数据为空；合法非空队伍sample成员等概率。','空队伍在sample[:species]可失败，不承诺空串。','TE非Trainer为空；Encounter.get按版本，缺实际记录为空。','顺序Land/Cave/Water取首个非空表，前min(length,4)槽均匀，不按权重不去重。','非法物种查严格get可失败；第五槽不参与。','地图名直接命名服务，不叠加可见/信号/visited门。']),
('电话每帧倒计时挂钩',phone,[543,560],[
'须player存在且has_pokegear。','in_menu/in_battle/message_window/force_route/mapinterpreter任一暂停，两套倒计时均不更新。','先refresh_ready_trainers再处理呼入倒计时。','calltime<=0时抽20...40整数分钟×60.0，当帧减Graphics.delta。','减至<=0才make_incoming；没有信号时make_incoming早返但本帧已递减。']),
('旧电话18入口兼容',phone,[562,706],[
'所有旧入口先Deprecation.warn；警告成功不证明后续成功。','RegisterBattle预检起始0，拒绝false；确认后把0版本数/versions_count起始送普通add。','Register静默默认版本数1起始0；RegisterNPC按show_message选普通/静默。','DeleteContact对完整contacts索引赋visiblefalse；支持Ruby负索引，越界局部失败。','Find/Has/ReadyToBattle均调用缺失Phone.get，不能返回空/false。','Reset使用未定义trainer_type/name，参数求值先失败，后续false/true不可达。','BattleCount代理错误variant包装；Increment忽略传入versions_count、固定start0代理错误increment包装。','SetReadyToBattle仅调记录事件switch写入；RandomPhoneTrainer只选记录。','CallTrainer转按标识失败路径；GenerateCall仅生成。','PhoneCall播放并透传尾消息；EncounterSpecies/TrainerSpecies每次独立抽样；TrainerMapName只服务查询。']),
('点唱机画面及默认命令',ref(29),[1,83],[
'画面用一命令列表，BACK>USE，输入trigger但窗口更新先执行方向repeat。','USE返回当前index；BACK返回−1。','六默认项March/Lullaby/Oak/Custom/Stop/Exit按固定顺序。','pbSetCommands nil恢复原列表并按给定index定位。','正常fade/dispose尾部没有ensure。']),
('点唱机音乐/旗标/Custom前缀',ref(29),[84,149],[
'March请求RadioMarch后lowerfalse/highertrue；Lullaby相反；Oak两false。','旗标写仅PokemonMap存在时，BGM请求失败先于本地旗标写。','Custom先chdir Audio/BGM，再按wav/ogg/mp3/midi/mid/wma分别glob。','去扩展名去重后按downcase排序，子列表初始0。','子列表BACK保留原覆盖/旗标；USE每次setDefaultBGM选中后两旗标清。','空列表USE可送nil清覆盖；目录不可进在子列表前失败、覆盖/旗标保持。','离开Custom恢复主列表索引Custom。','Stop先setDefaultBGM(nil)，再请求当前地图bgm，再清旗标；步骤失败保留已提交前缀。','Exit/BACK不改覆盖/旗标，正常endScene。']),
('BGM覆盖接收与持久',system,[24,149],[
'GameSystem save对象包含defaultBGM状态，非单独UI临时变量。','bgm_play_internal先记playing_bgm请求，再视default覆盖决定宿主请求。','有default时各后续BGM请求都转覆盖身份，不会由电台请求自动清覆盖。','setDefaultBGM先清旧default，再尝试播放新曲，之后clone为新default。','nil/空新曲先清default，再bgm_play先前playing_bgm，不在这里清地图旗标。','宿主音量按PokemonSystem.bgmvolume缩放；内部只捕获ArgumentError后0位置重试。','文件存在检查/Audio请求不构成声音实际成功。']),
('TownMap与Phone/Encounter数据接收','Data/Scripts/010_Data/002_PBS data/002_TownMap.rb',[1,43],[
'TownMap id/名称键/filename/points/flags为登记字段，points/flags缺省空。','TownMap严格get来自数字IDmixin，未知实际ID抛UnknownID，exists?只测登记。','区域名经REGION_NAMES消息哈希；flags不区分大小写。','PhoneMessage.try_get校验type Symbol/String及name String，NPC niltype可先类型失败。','PhoneMessage作者节头join逗号不quote，不反推写出会改旧内存。','Encounter.get先指定map/version，有key即用，否则version0，无则nil。','电话数据默认三节Default/Jeff/Susie；默认地图两区域及points全读，事件可达仍未证。'])
]
f=json.loads((p/'forward-mapping.json').read_text());f['semantic_units']=[u for u in f['semantic_units'] if not u['id'].startswith('UI63-')]
for n,(name,path,rng,facts) in enumerate(units,1):
 src=dict(by[path]);src.update(reader='/root/ui_full',semantic_range=rng)
 f['semantic_units'].append({'id':f'UI63-U{n:03}','name':name,'sources':[src],'reader':'/root/ui_full','facts':[{'id':f'UI63-F{n:03}-{j:02}','assertion':x} for j,x in enumerate(facts,1)],'premise':'固定B8/R默认，无插件/并发写；具名合法输入与正常基础依赖，失败限定本地已提交前缀；SOURCE_STATIC，NOT_EXECUTED。','disposition':'OWN_READ_EXACT_SOURCE_UNITS; no whole consumer/runtime guarantee','execution':'NOT_EXECUTED'})
f['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();f['hand_authored_unit_count']=len(f['semantic_units']);f['fact_count']=sum(len(u['facts']) for u in f['semantic_units']);f['warning']='手工事实分解，非方法/行数统计；仍非全51R/18F最终原子分母。';(p/'forward-mapping.json').write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n')
print(f['hand_authored_unit_count'],f['fact_count'])
