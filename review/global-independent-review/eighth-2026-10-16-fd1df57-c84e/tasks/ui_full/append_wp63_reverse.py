import json,pathlib,datetime
p=pathlib.Path(__file__).parent;s=json.loads((p/'reverse-mapping.json').read_text());s['records']=[x for x in s['records'] if not x['id'].startswith('UI63-')]
items=[]
def add(clause,units,claims,status='SUPPORTED_LOCAL_SOURCE_STATIC'):
 for claim in claims:items.append((clause,units,claim,status))
add('§2.1入口',[2,7],[
'暂停菜单Pokégear由持机门控制。','暂停TownMap要求无机且有TOWNMAP，互斥。','地图助手wallmap不写飞行目的地。','非wallmap得到ret才写飞行目的地。','入口飞行执行是WP59接点，不能将写目的地称为转移成功。'])
add('§2.2按钮',[1,2],[
'默认Map/Phone/Jukebox三项；第三方插件不穷尽。','列表由菜单集合按排序与condition构造。','按钮纵列居中。','UP/DOWN循环，至少两项才播游标音。','BACK返回−1。','USE执行当前项effect。','effect假值留在画面循环。','Map非空ret先写目的地。','Map选定销毁按钮画面并以哨兵结束。','Phone不查有无联系人。','Phone空本只提示，未建画面。','女性变体有可解析资源才选。','主按钮BACK>USE>UP>DOWN，全trigger。','Map焦点同轮DOWN+USE只确认原Map。'])
add('§2.3 FLY跨域',[7],[
'Party确认FLY后打开直接fly地图。','选中治疗点返回三元组由caller写目的地。','BACK不写新目的地。','Party取消重建丢BoxLink许可且焦点0是Caller独立事实。','无FLY成员执行失败及清目的地归WP59。'],'REQUIRES_NAMED_CALLER_RECEIPT')
add('§3.1初始定位',[3,24],[
'无当前位置定位时优先区域0左上。','有定位且显式region非负、不同当前并exists时取显式区域左上。','显式region未知则回当前区域。','严格查询只针对最终选中区域。','最终ID未知先UnknownID，非友好提示。','友好缺地图提示只在取得数据假值时。','玩家图标要求有定位并显示其当前区域。','子格h=ceil(shape.length/w)，仅w>0参与。','横偏移floor(playerx*w/mapwidth)，仅w>1。','纵偏移floor(playery*h/mapheight)，仅h>1。','形状只取长度，不过滤0/1。','示例w3/S10000/19,19落在15,13。','合法地图实际尺寸与坐标是推导前提。'])
add('§3.2显示',[4,5,24],[
'底栏区域名来自消息本地化。','底栏地点/详情普通本地化、editor原键。','附图普通按正开关，wallmap直接字段5。','默认附图恰两项。','飞行图标只建visitedMaps治疗点。','图标初始只mode1可见。','名称只同坐标第一条。','详情只同坐标第一条。','治疗点只同坐标第一条。','首条隐藏立即空，不搜下一条。','首条缺详情空串，不搜下一条。','首条缺治疗字段nil，不搜下一条。','点带switch且wallmap一律隐藏。','点switch<=0隐藏。','普通点switch关隐藏。','调试CTRL不绕首条和字段/隐藏门。','visitedMaps写入是地图进入生产者接点。'])
add('§3.3浏览与编辑',[5,6],[
'方向dir8每轴±1。','逻辑坐标夹0..29×0..19。','先逻辑移动再地点/详情刷新。','当轮建立0.1秒显示插值。','移动发起当轮仍处理按钮。','后续未到点next全部输入。','读回两轴到点同轮恢复新方向和按钮。','普通BACK nil。','editor未改BACK直接退出。','editor已改BACK先问保存。','保存确认先save.dat再write PBS，无事务回滚。','保存后继续问退出。','editor USE文本上限250。','新点追加，旧点改首条。','editor文本返回非nil即changedtrue。','名义时长不证明宿主精确到点。','按钮BACK>mode1USE>editorUSE>合格ACTION。','mode1不合格USE挡ACTION。','mode0非editorUSE不挡合格ACTION。','CTRL为press，其余按钮trigger。'])
add('§3.4飞行',[6,7],[
'直接fly打开即mode1。','浏览ACTION切0/1要求CAN_FLY true。','ACTION还要求非wallmap。','ACTION还要求非直接fly。','ACTION还要求pbCanFly?通过。','mode1USE要求治疗点。','还要求visited或DEBUG+CTRL。','直接fly返回无确认。','浏览转fly需确认后返回。','返回是地图ID/x/y三元组。','BACK不写新的目的地。','临时目的地的实际飞行消费需WP59完整接点。'])
add('§4.1画面',[8,9,10],[
'无可见联系人只提示不开画面。','仅可见联系人形成显示列表。','信号图标仅NoPhoneSignal门。','注册数为可见命令数。','待再战数按can_rematch?。','再战行图标仅场景开时enabled才创建。','训练家头像为类型charset。','NPC头像为phoneNNN图。','所在地图名只map_id>0时查。','USE打开当前记录命令。','普通BACK关闭。','ACTION进入移动模式。','列表先repeat更新再比较索引。','移动实时写完整contacts数组。','移动ACTION/USE优先BACK落定。','移动BACK先逆移动再恢复起始index。','普通ACTION>BACK>USE。','全可见三条DOWN+USE+BACK以USE落定。','隐藏联系人索引变体未证明。'])
add('§4.2数据',[11,14,24],[
'联系人在PokemonGlobal.phone内保存。','训练家字段含map/event/type/name/版本数/起始/当前/time/flag/common_event。','NPC含map/name/common_event。','全联系人visible默认true。','rematch_variant默认0。','rematches_enabled默认设置false。','display_name训练家类型名+消息名。','NPC display_name为INTL名。','界面语言与训练家语言来源不混。'])
add('§4.3注册删除排序',[11,12,13,14,10],[
'can_add?先查has_pokegear。','can_add?训练家类型必须登记。','can_add?仅可见同键阻止。','直接add不调用预检。','直接add两个训练家形态仍查类型存在。','未知类型在新增前false。','NPC直写无持机门。','可见查重记录复用并移尾。','隐藏同键另建，不恢复旧记录。','构造版本数至少1。','构造current=start。','构造time/flag为0。','新增后visible优先稳定partition。','普通反馈附带注册音消息请求。','静默入口跳过反馈。','训练家按事件add查重把versions_count放start_version查询。','正常type字符串可先新增再反馈原输入查询失败。','静默字符串type可成功。','规范type普通反馈成功。','UI Delete只can_hide?即Trainer。','Delete确认后visiblefalse。','隐藏Trainer清time。','隐藏Trainer清flag。','隐藏Trainer写Atrue并请求refresh。','之后sort/refresh/message正常尾部。','删光提示空并关。','排序名、display_name、NPC先三式。','每式后再visible优先稳定partition。','BACK逆移动恢复仅在已证全可见索引前提。'])
add('§4.4再战',[12,14],[
'每秒判断last_refresh_time。','只有enabled更新。','只可见Trainer。','flag>0跳过。','time<=0先抽20..39分钟整数。','当次仍减1。','从20分首轮变1199秒。','减到0写flag1。','随后Afalse/Btrue及刷新。','flag1后不再抽倒计时。','next=start+min(relative+1,globalcap,count−1)。','relative=current−start。','battle入口用next_version。','reset_after_win先increment再清flag/time。','默认cap0，常规start0不向上推进。'])
add('§4.5缺陷公开形态',[13,15,20],[
'记录级输入可进入正确next/increment/reset路径。','按标识make_outgoing调用缺失Phone.get。','缺失在信号/距离门前。','不是返回空。','公开variant把type作布尔Trainer门。','正常type不等true，query0。','同错位increment不动作。','旧包装转发不保证可用。','生成事件使用公开版本query的接点另由compiler/interpreter接收。'])
# Every legacy row decomposed separately; references exact source wrapper unit20 and local provider.
legacy=[
('RegisterBattle',['先v22警告。','预检固定start0。','拒绝预检或确认false。','确认调用0版本数/传入count作start。','count0提升1且current=传入count。']),
('Register',['先v22警告。','静默无强制持机预检。','默认count1/start0。','类型未知false。']),
('RegisterNPC',['map/name/common_event参数重排。','show_message选择普通/静默。','正常true。','common_event0不是注册拒绝。']),
('DeleteContact',['完整持久数组索引。','赋visiblefalse的结果false。','负索引从末端。','越界局部失败。','Trainer隐藏前缀仍有效。']),
('FindPhoneTrainer',['先警告。','缺Phone.get未定义方法。','不返回空。']),
('HasPhoneTrainer',['缺查询在真假比较前失败。','不返回false。']),
('ReadyToBattle',['缺查询先失败。','不到can_rematch?。']),
('Reset',['实参名tr_type/tr_name未被使用。','未定义trainer_type/name求值先失败。','后续false/true不可达。','警告旧名误字不改变失败。']),
('BattleCount',['错误布尔槽恒0。','不读取真实对象进度。']),
('Increment',['忽略versions_count。','固定start0。','错误布尔槽不动作。','正常返回空。']),
('SetReady',['Trainer事件Afalse/Btrue/refresh。','正常尾true。','NPC无动作空。','不写flag/time。']),
('RandomPhoneTrainer',['同region可见Trainer异图且异地图名。','无候选/无当前位置nil。','不查信号。','选中不等已拨。']),
('CallTrainer',['转按标识make_outgoing。','缺查询先于信号距离。']),
('GenerateCall',['只生成文本。','flag1可能推进2。','不播放。','不抽TP/TE。']),
('PhoneCall',['播放分段。','每通TP/TE各一次。','尾Click。','透传末消息结果，无稳定布尔。','数据消息失败保持本地前缀。']),
('EncounterSpecies',['单次TE采样。','前三表顺序、前四槽均匀。','非Trainer/无表空串。','缺请求版本退0。','非法物种不保证空串。']),
('TrainerSpecies',['单次合法队伍成员均匀。','非Trainer/无数据空串。','空队伍不保证空串。','每次独立重抽。']),
('TrainerMapName',['按map_id命名服务。','不查信号。','不查可见/已访问。','不增强未知数据保护。'])]
for name,claims in legacy:add('§4.6 '+name,[20,11,13,14,15,16,17,18],claims)
add('§5.1呼出',[15,17,24],[
'无信号先拒绝。','Trainer同图先拒。','Trainer两图定位缺一或region异拒超范围。','NPC过信号门即允许。','公共事件只ID>0。','NPC默认ID0走训练家生成。','nil TrainerType在PhoneMessage.try_get validate先失败。','联系人不因生成失败自动删除。','正ID缺事件助手false后提示。','事件内容实际执行保持保留。'])
add('§5.2呼入',[19,15],[
'持机才能帧更新。','菜单、战斗、消息、强制路线、解释器运行暂停。','暂停时两个倒计时都不更新。','呼入<=0抽整数20..39分钟。','乘60.0成为浮点秒。','当帧减Graphics.delta。','到0发起一次。','候选同region异图异地图名可见Trainer。','有公共事件ID分派，缺事件提示。','无则生成并播放。','无信号时make_incoming早退，不反推暂停倒计时。'])
add('§5.2编译重写接点',[24],[
'作者节头join逗号没有quote。','写出不改变旧内存身份。','姓名带逗号重新编译语义须保留WP04已证token条件。','真实电话播放和坏输出后状态未执行。'],'BOUNDED_COMPILER_RECEIPT_REQUIRED')
add('§5.3生成/播放',[16,17,18,24],[
'消息先当前version，再start，再default。','intro随机一条。','Morning05:00..09:59替换非空。','Afternoon14:00..16:59替换非空。','Evening17:00..19:59替换非空。','10..13及夜间保留通用。','enabled且flag1取request并就地flag2。','flag2取remind，nil组退request。','普通body1/body2都存在且无body或75%时取两段。','否则body。','普通end非空才追加。','TN联系人name。','TP用max(current,start)队伍成员。','TE前Land/Cave/Water首非空表前至多4槽均匀。','TP/TE每通开始各一次，无占位也抽。','全部段落共用这两个值。','队伍重复物种保留成员次数。','TE不按权重不去重。','第五槽不参与。','无Trainer数据TP空串。','空队伍不保证保护。','Encounter缺指定version退0。','三表空或无记录TE空串。','非法参数/物种可失败。','性别着色门保持。','start省略号→各消息→endClick同通路径。','时段谓词来自PBDayNight，本人1..180精确读取。'])
add('§6点唱机',[21,22,23],[
'六项顺序固定。','March请求电台后lowerfalse/highertrue。','Lullaby lowertrue/higherfalse。','Oak两false。','有Custom覆盖时电台命令仍播放覆盖请求。','电台不清default。','Custom先进入BGM目录。','枚举wav/ogg/mp3/midi/mid/wma。','去扩展名去重。','按小写排序。','USE写默认覆盖。','Custom USE后两旗标false。','Custom BACK回主列表且保留覆盖。','Stop先清覆盖。','Stop再请求地图BGM。','Stop后两旗标清。','Exit/BACK不写覆盖旗标。','跨图进入生产者清当前地图旗标。','default覆盖独立于当前地图清理。','不保证具体曲目资源存在或宿主播放。','目录缺失在子列表前失败。','目录存在空文件列表与目录缺失分开。','空子列表USE可清覆盖与旗标。','空子列表BACK保留覆盖。'])
add('§7–11不变量/失败/配置/保留',[2,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],[
'工具入口持机门与直写注册门不混。','浏览nil与飞行三元组分层。','wallmap不写目的地。','联系人操作改变全局phone状态。','对话生成唯一局部写flag1→2。','点唱机不写TownMap数据。','无信号显示图标并拒呼出。','无信号呼入倒计时照减，到发起点才拒。','无治疗点/未visited的mode1USE无动作。','版本count1/cap0以常规合法状态不推进。','47P+18PL是目录设计编号，不是业务执行。','配置CAN_FLY true。','rematches_enabled默认false。','gendercolour默认true。','默认extras两条。','BADGE_FLY/MECHANICS_GENERATION是独立配置接点。','TownMap/phone输入与编译产物不等媒体存在。','全局phone/visited/持机随存档。','fly_destination临时会话字段。','PartyFLY取消丢许可/焦点0保持跨域限定。','NPC公共事件内容、demo授予/注册/解锁可达未证。','第三方菜单组合不穷尽。','媒体存在/宿主像素与音频未证。','弃用转发不是成功保证。'])
start=0
for clause,units,claim,status in items:
 start+=1;s['records'].append({'id':f'UI63-C{start:03}','formal':{'file':'wp63-pokegear-map-music-and-phone.md','clause':clause},'assertion':claim,'source_units':[f'UI63-U{x:03}' for x in units],'premise':'固定默认B8/R，无插件并发；合法具名数据与基础依赖，源静态请求不证明宿主执行，跨域链未冒闭合。','status':status,'execution':'NOT_EXECUTED'})
s['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();s['manually_authored_assertion_count']=len(s['records']);s['scope']='WP17两正文304子断言+WP63全文手工拆分；不是其它11F或全catalog全部向量的最终分母';s['formal_all_ui_atomic_denominator']='NOT_FINAL';(p/'reverse-mapping.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n');print('WP63',start,'total',len(s['records']))
