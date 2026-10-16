"""Serialize individually written reverse/interface assessments; no behavior execution."""
import json
from check_inputs import TASK, OUT

d = json.loads((TASK/'continuation/01_scene_input_objects/readset.complete.json').read_text())
reads = json.loads((OUT/'reading-ledger.json').read_text())['units']

# Each value is a distinct current-reader reason, in frozen subassertion order.
notes = {
'EXTCP-R001': [
'StartAndEnd170–347先组织对方开场/派出再玩家；SceneInitialize初建野生实际Pokemon图，ScenePlay1–156承接派出。不是把所有球轨道重新收为本组。',
'ScenePlay普通shiny?门可受Illusion；Super分支另读自己super_shiny?及Settings门。showAnims控制公共异色动画，不关闭初始布局和派出等待。',
'SceneInitialize24–191建初始精灵/数据框；ScenePlay开场和派出包装等待相关完成器。实际bitmap、声音成功与宿主帧未观察。'],
'EXTCP-R002': [
'SceneInitialize79–156分别决定战斗背景时段与消息框时段；一个资源候选不替另一个候选作存在证明。',
'base0组合候选存在与否决定双方共用的组合前缀，再分别请求base0/base1；不单独探测base1决定前缀。',
'没有组合平台时用独立base候选；初次存在检查后的加载仍可能失败，不能从文件名分流推出第二层业务回退保证。普通Gif加载的空图兜底另列IR019。'],
'EXTCP-R003': [
'SceneChoose1–84的左右/上下网格与lastCmd记忆分开；BACK只有给定可取消门才返回。CommandPhase根据是否首行动等决定回退权限。',
'SHADOW机制且训练家战的mode替换Run为Call；菜单显示条件与ActionOther呼唤执行四分支是不同层。',
'CommandPhase对SkyDrop携带中的位置只允许Fight，非Fight结果先拒绝再回循环；负值调试/取消控制不当作普通命令。',
'CommandPhase回退可撤先前登记，F9负返回交调试入口；玩家控制/AI控制先分流。场景只返回选择，未独自登记领域行动。'],
'EXTCP-R004': [
'AttackPhase全文显示Call→Switch→Item→Mega→招式固定相序；StartAndEnd主循环在阶段后依据decision截断，不能许诺每轮全部走完。',
'Scene pbAbort关闭场景并抛BattleAbortedException；主开始链捕获置decision0。普通pbEndOfBattle的逐choice退款/peer复位不在同一条异常中止链。',
'正常终局先scene EndBattle再逐choice取消退款、特性退场和成员复位。某次退款/回调异常可保留此前提交，不保证余项继续；两胜利入口设置标记，失败不设置。'],
'EXTCP-R007': [
'Fight菜单保持实际move槽和lastMove，PP/类型取显示query；totalPP0图形分支不画PP、文本分支写---。realMove关联不是按以后摘要槽号重找。',
'SceneFight返回-2切换Mega登记并继续同一选招循环；按钮条件、领域资格、实际Mega执行分层。',
'-3登记Shift，CommandPhase并撤该位置Mega选择；ActionOther执行Shift另有合法布局/属主/端点条件，菜单图标不等于执行成功。',
'Fight包装先调用autoFightMenu，再走autoChooseMove等门，然后普通手选。Palace覆写的全部概率/执行规则归原责任；本组仅接受入口优先级与旁路可能。'],
'EXTCP-R008': [
'ActionOther1–57：Hyper暗影先降心，非暗影睡眠治愈，非暗影可升命中则升，否则nothing happened；非Hyper暗影不走后两种收益。',
'SceneCommand门决定是否给Call按钮；裸登记Call只写choice，不自证同样场景资格。执行者仍按真实battler状态分支。'],
'EXTCP-R009': [
'SceneChoose333–356把无/不合类位置记nil，存在而失能记空名，活位记名；TargetMenu对已有位置可画中性按钮，nil文字不等于零图形。',
'选择循环按左右跨侧、上下同侧±2及可用文本跳过规则移动；目标数0整体模式与目标数1单选分开，RandomNearFoe确为1。',
'NearAlly初选把Battler对象传给不归一化的Battle.nearBattlers?，可能初选同侧远位；文本生成另用正常位置索引近邻门。不能把Battler.near?的归一化借给此caller。',
'USE对非负初选直接交付，不重新看文本；实际pbAddTarget拒自己/不邻近后，NearAlly可随机重选有效盟友。选择身份与执行最终目标不相等。'],
'EXTCP-R010': [
'CommandPhase仅内部战斗的普通Bag通路进入场景背包；其它模式的独立预算/物品来源不在此签收。',
'Bag过滤battle_use可用物品，显示过滤索引再映射原口袋索引；光标、道具身份与数量是不同数据。',
'类型1/3只有一个候选时先自动提交；回调拒绝不会立刻退出，而转成员选择循环，再取消才退背包。',
'类型2开选招；类型4唯一对手可自动，否则开Foe选择；类型5无成员选择但回调仍携带idxBattler。无目标窗口不能概括成没有身份参数。',
'成员/招式子取消回对应上层；类型4由战斗目标画面返回后背包需重新显现；最终取消才退出整次Bag调用。未登记不会消费。',
'正常返回保存战斗口袋光标并恢复野外原光标/可见性；没有覆盖全部异常的ensure，加载/回调失败不保证同样恢复。'],
'EXTCP-R011': [
'登记先写choice并consume，AttackPhase随后才按类别执行。成功选中不等于效果已运行；取消未执行choice有独立退款。',
'类型1/2/3/5执行复检拒绝可先refund但保留choice道具身份；不能凭已退款自动清身份。正常效果回调返回后清身份，即使效果返回false。',
'类型4走独立球执行者，本组只核外层选择/交付和该消费者分路，不接管捕获率/球handler全集；不能套普通类型的失败退款。',
'下一命令阶段初始化及正式Faint直接清choice身份，不走refund；故复检拒绝后是否终局/失能/下轮会改变后续退款次数。',
'正常终局可再次按残留身份退款；容量拒绝时已有扣减/效果/第一次退款仍保留，不保证继续清理。WP67§5.3.1与WP40/WP42定位一致。'],
'EXTCP-R012': [
'mode0换入、mode1Send to Boxes、mode2摘要；成员子命令取消回列表，列表取消才检查canCancel。Scene本身无统一-1返回保证。',
'Switch In可见门是mode0且able且(canSwitch或不可取消)，不可取消时绕过canSwitch显示门；实际提交仍交领域校验。',
'正常完整partyOrder与显示队伍互逆，场景按partyStart反查真实下标。若破坏映射，Scene177–182仍yield -1：shouldRegister包装拒负数留列表，mode1 callback真会先关子屏，再由CatchAndStore34退外层。WP67 line170“映射不到则忽略继续循环”不得签成统一场景守卫；仅正常映射下接受，异常表述留父审。',
'checkLaxOnly仅pbCanSwitchIn?，严格再查重复选择和可换出；shouldRegister另决定登记。负查询哨兵与有效候选登记不可混为一体。',
'切换先召回消息/动画、实际替换、派出消息/图；发送取Illusion或传入Pokemon，普通wild初图却取真实party个体。已在场摘要重排持久move不重构整个battler。',
'Arena覆写拒手动换出，即使菜单可见也不保证成功；自动按序替补取下一party位置，无普通玩家选人屏。本组不签Arena剩余绘制/评分全集。'],
'EXTCP-R013': [
'pbGainExpOne暗影分支只在showMessages真时显示获得；普通分配caller对暗影可传false。暗影不进入普通EXP条/逐级循环，不能由helper门推出默认必有消息。',
'每段经验先写持久Pokemon exp，再请求Scene条动画；逐级重算先于升级提示，呈现失败可保实际经验/能力变化而停止后续。',
'DataBox初建仅玩家单席开EXP门；动画duration=1.75×段比例，满槽追加0.2闪光。无EXP门立即完成；重初始化不复位旧true的内部边界已在F034限定。',
'升级先calc_stats、refresh，再消息与两次数值窗USE关闭，之后学招。BACK不关闭这两窗；未运行原生字体/输入/计时。'],
'EXTCP-R014': [
'未满槽先追加持久招式，learned消息正常返回后才追加在场战斗招式；显示异常可留下仅前一份提交。',
'满槽替换在Ta-da消息之前写持久与在场两份；PP与realMove保持对象关联，不凭slot变化推错误扣PP。',
'遗忘返回负值后询问放弃，拒绝放弃重开循环；放弃与选定遗忘槽不共用提交前缀。',
'遗忘界面拒绝HM/hidden move，debug门可豁免；空招式表直接进入遗忘详情会先读取失败，普通空槽学习另走前一分支。'],
'EXTCP-R017': [
'普通消息全部显示后才设1秒计时；输入快进与计时到期分开，block只在首次全显时触发。',
'brief留下窗口，下个消息pbWaitMessage另等1秒；部分动画直接清brief而不消费这段等待，不能把后继消息当唯一清除者。',
'paused全显后在battleEnd=false时3秒自关；true时需输入。Source仅两胜利方法置true。WP67§9.1“胜负BGM设置后”与§3.5及源码不一致，候选CP01-C01交父审，不能签成失败亦无自动关闭。',
'高级文字skipAhead和resume不同：普通消息可快进；列表忙时仅resume，等待/字符节拍未满足不强制全显。列表不忙后USE/BACK才能提交；abortable BACK另抛中止。',
'yielded本地门确保每次消息调用block最多一次；block异常没有统一回滚，不承诺其后窗口关闭。'],
'EXTCP-R018': [
'数字/EXP首次构建只给玩家单席，其它布局窄框；同一对象重初始化没有关闭旧门，故这里只签正常新建前提。',
'animate_hp用旧/新HP设1秒System.uptime插值，Scene等待animating_hp结束；显示HP是独立于已经提交实际HP的数值。',
'h浮点比较T/4、T/2的整数阈值；T101的50.5绿→50黄、25.25黄→25红；数字to_i不反向改变条色。',
'源码条宽先比例、正值至少1、再就近偶数像素量化；WP67§9.2没有写完整公式。已有HP04测试目录明确保留“比例条宽/偶数舍入”，修正反向locator，不把全部内部常数自动升级新required。',
'owned须opponent且owned?，owned?又有wild/显示species门；闪光、状态、性别、Mega/原始各自查询与图标条件不互相替代。',
'DataBox selected1/2的0.6秒摆动与成员selected1摆动/selected2的0.3秒闪烁分别更新；目标结束逐位reset，不推宿主精确像素。']}

joins = {
'EXTCP-R001':[3,4,10,21,23,40,41], 'EXTCP-R002':[2,44,45],
'EXTCP-R003':[1,3,7,13,52], 'EXTCP-R004':[1,10,12,14,53],
'EXTCP-R007':[3,4,7,8,13,19,39], 'EXTCP-R008':[3,7,13],
'EXTCP-R009':[3,4,8,9,17,18,20,52,55],
'EXTCP-R010':[3,7,27,29,32], 'EXTCP-R011':[3,7,10,12,14,16,52,53],
'EXTCP-R012':[1,3,9,11,19,21,27,28,46,47,50,54],
'EXTCP-R013':[5,15,21,33], 'EXTCP-R014':[3,15,19,28,39,50,54],
'EXTCP-R017':[1,2,21,24,26,49], 'EXTCP-R018':[5,16,17,21,25,34,36,40,51]}
qualified = {'EXTCP-R012.3','EXTCP-R017.3','EXTCP-R018.4'}
reverse=[]
for g in d['reverse_current_contribution_objects']:
    assert len(notes[g['id']]) == len(g['subassertions'])
    for fact, note in zip(g['subassertions'], notes[g['id']]):
        reverse.append(dict(id=fact['id'], original_complete_assertion=fact,
                            original_reverse_group=g,
                            actual_complete_meaning_and_reason=note,
                            read_units=['READ-%02d'%n for n in [6,*joins[g['id']]]],
                            disposition='QUALIFIED_FINITE_RECEPTION' if fact['id'] in qualified else 'FINITE_RECEPTION_UNDER_STATED_PREMISES',
                            evidence='SOURCE_STATIC / FORMAL_TEXT; NOT_EXECUTED',necessary_unread=[],root_task_final_credit=0))
assert len(reverse)==59

selected=[]
for x in d['selected_reverse_interfaces']:
    damage=x['id']=='EXTCP-IR006'
    selected.append(dict(id=x['id'],original_complete_interface=x,
        actual_complete_meaning_and_reason=(
          'ScenePlay221–278将所有所请求伤害动画与相应HP条加入本地处理，聚合等待各自done。BaseAnimation完成与BattlerDamage577–608完成器、DataBox HP标志相接。只接此等待合取，不接收F056其它轨道常数或把开启条件改成永远请求。' if damage else
          'Scene pbAddSprite有局部rescue，pbAddPlane没有同层rescue；IconSprite先清旧图，AnimatedBitmap普通Gif加载异常返回32×32空图，前缀PNG检查/加载不共用兜底，直接RPG::Cache.load_bitmap也不走普通Gif rescue。只签这些加载/失败接点，不授其它所有资源/轨道对象全量信用。'),
        read_units=['READ-%02d'%n for n in ([5,6,16,21,22,23] if damage else [1,2,42,43,44,45,48])],
        disposition='FINITE_INTERFACE_RECEIVED',necessary_unread=[],root_task_final_credit=0))

old=json.loads((TASK/'recovered'/d['target_commit']/'interfaces.json').read_text())
facets=[
('interfaces[0]',old['interfaces'][0],[1,3,7,8,13,52], '命令→返回→登记/撤销/执行的本组全部菜单和消费者；F9、Mega、Shift、Call身份分列。'),
('interfaces[1]',old['interfaces'][1],[3,9,11,19,27,28,39,50,54], '队伍映射、取消层、摘要重排和realMove关联；异常映射限定见R012.3。'),
('interfaces[2]',old['interfaces'][2],[3,7,10,12,14,16,29,32,52,53], '全部本组物品选择/消费/执行复检/退款前缀；捕获率和球handler不属本组。'),
('interfaces[3]',old['interfaces'][3],[5,15,16,17,21,33], '实际HP/EXP写入→通知→条动画→后置记录；显示失败不撤销已写值；仅ScenePlay所列完整包装，不声称216–385全读。'),
('interfaces[4]:party/dex/name facets only',old['interfaces'][4],[3,27,28,30,31,47], '仅捕获满队mode1/2的party负值返回消费者、图鉴brief和命名桥；不接球/peer/storage全域或捕获事务。'),
('interfaces[8]:background/metrics facets only',old['interfaces'][8],[2,5,34,35,36,37,40,41,44,45], '仅场景背景/时段/平台、物种指标×2及影子门/定位；音乐选择优先级归后续声音组，不偷签。'),
('continuation_interfaces[1]',old['continuation_interfaces'][1],[3,5,8,9,16,17,18,19,28], 'NearAlly对象/索引差异、HP写穿、PP随realMove；领域资格与未来API均不由此内部事实替代。')]
facets=[dict(original_exact_locator=loc,original_complete_interface=x,
             joined_complete_facts=note,read_units=['READ-%02d'%n for n in ns],
             disposition='ONLY_NAMED_FINITE_FACETS_RECEIVED',necessary_unread=[])
        for loc,x,ns,note in facets]

payload=dict(schema='r8-cp01-interfaces/v1',status='READY_FOR_PARENT_RECEPTION',
    contract_commit=d['contract_commit'],effective_dispatch_contract='35d85e4484b892ebc32542346861440638d2183c',
    target_commit=d['target_commit'],reverse_groups=14,reverse_assertions=59,
    reverse_qualified=sorted(qualified),reverse_records=reverse,
    selected_reverse_interfaces=selected,bounded_original_interface_facets=facets,
    foreign_remainder='Other frozen jobs own F019–027/F042–059,496 variants and16 RGB objects. Their absence from this receipt is explicit allocation, not this group necessary unread.',
    original_id_collision='Original interfaces[8] IF09(background/music) and continuation_interfaces[0] IF09(fixed tracks) retain distinct exact locators; never merged by display id.',
    supplement='Full eight-fact companion read. RX-SCENE-REFRESH/HP/ILLUSION directly rejoined with required qualifiers; five foreign core facts remain context only.',
    proposal='Original CP002 remains PROPOSED_ONLY/root decision pending; H001 withdrawn. Fixed pitch/track precision and RGB policy are not independently adjudicated here.',
    necessary_unread=[],unavailable_required_material=[],new_required_findings=0,
    new_candidates_pending_parent_adjudication=1,execution='NOT_EXECUTED',UPDATE_NOT_STARTED=True)
valid={x['id'] for x in reads}
for x in [*reverse,*selected,*facets]:
    assert set(x['read_units']) <= valid
(OUT/'interfaces.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(reverse=len(reverse),selected=len(selected),facets=len(facets))))
