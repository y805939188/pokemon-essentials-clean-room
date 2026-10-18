import datetime, hashlib, json, pathlib, subprocess
v=pathlib.Path(__file__).resolve().parent
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(n):return json.loads((v/n).read_text())
def save(n,o):(v/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def sha(b):return hashlib.sha256(b).hexdigest()
n=load('next-dispatch.json');f=load('forward-mapping.json');rev=load('reverse-mapping.json');by={a['id']:a for a in f['atoms']}
seeds=[x for x in n['unmet_formal_seed_structures'] if x['old_locator_id'].startswith('F08-')];assert len(seeds)==202
path=seeds[0]['path'];repo='/workspace/pokemon-essentials-clean-room';commit='fd1df570cad987dc3852a3b958f03916e317f7fe'
raw=subprocess.check_output(['git','-C',repo,'show',commit+':'+path]);lines=raw.decode().splitlines()
meaning={}
def series(prefix,values):
    for i,text in enumerate(values,1):meaning[f'{prefix}{i:02}']=text
series('BP',[
'种植阶段/时间/水分/统计/库存五个效果。','6h整点干燥与阶段3，惩罚0。','24h顶后一次重植再消费余时。','重植上限清零含覆盖物。','第7整点到负水分，后3整点罚3及3h对照。','DAMPMULCH整数15/2=7。','偶数14/2=7对照。','干燥1取整0不耗水不积罚。','CHERI覆盖物15整小时成熟、产量5；数据更新/查询不提交采摘统计，容量/确认门另属采摘。','旧浇水数0/1/4产量2/2/4–5。','新罚2产量3。','显式旧数据更新雨水门，普通精灵链不推进。','满包不采摘reset，等待更新另计。','终态列举与真实提交次序分开。','时间倒退早退无写。','施肥取消不写不耗。','施肥后拒种保留覆盖物且不退库存。','旧GROWTHMULCH时间/阶段/戳先于浇水，早退与上限对照分开。','浇水写入/反馈配置择一，不把新旧消息合播。','新阶段变动请求闪光的正反门，媒体未证。'])
series('FP',[
'普通完成通知→全局步→玩家周期→可转移→条件遭遇，选择不等于开战。','强制/解释器完成双一般通知并早退，转向与NPC分开。','127不触发、128/129同一步触发后归0。','随机0才生效，空可战集合也消耗周期。','默认无野外毒伤；两开关四组合分列。','可战快照/中毒门/免疫门及单次批反馈分开。','HP1不致死门清毒，不写faint友好。','逐成员毒伤与最后可战者回程，快照/治疗后门不合成后续保证。','零可战数检查不另要求队伍非空。','病毒菌株/期限/阶段编码与余数向量。','重复感染/合法菌株/治愈拒绝/重设期限/清期限/治疗边界。','日期不同只推进一次，包括回拨，空日期不初始化。','连续帧只首帧推进且更新时间。','首门含蛋，扣期仅感染非蛋，箱/寄养不纳入。','healingSpot/洞穴逃脱点/Teleport三状态与演出区别。','Dig/绳/Teleport各门与逃脱点清理。','失能回程统计→治疗→消息→载具/跟随/开关/转移/刷新→清点。','角色家优先与资源缺失早退、无家正常尾的分阶段差别。','非地图不执行实际转移，gameover与普通措辞分列。','捕虫最先特殊回程，普通blackout统计/治疗路径不执行；不追加扣款/重置。','非蛋完整治疗HP/异常/全部PP/待进化，蛋早退；病毒/物品/形态与专门heal_PP分开。','事件全部恢复按配置队伍或队伍+箱，个体治疗边界不扩。','跨日加载/新档空日期/调试入口各门，序列化不证明离线时间。','帧/任意步/玩家步/可转移/换图注册顺序与每个实际到达门；净化室独立于成员循环。','Repel冰面不减，耗尽提示与再用背包筛选，激活拒绝。','单次毒批音效/闪光与逐成员写入分开。','内部终局固定传播来源集，邻位阶段0目标/独立随机，新增感染不作新来源。','全蛋/全濒死/空队均零可战，检查入口同门。','治愈菌株重设期限回到感染期，字段0不动。','载入跨多日仍只下一帧推进一次。','入盒配置治疗先保存再恢复待进化，直接heal会清，关闭不治。','首煤烟层擦除与收集袋/容量/统计门分离。','合法强制完成可两次通知擦两层，玩家周期不进。','电量警告先写标志再提示，一会话一次及菜单等阻挡门。','感染蛋/非蛋/阶段0/2扣期集合与日期写入，对照仅蛋仍写日期。'])
series('R7-FP',[
'碰撞创建与正常完成分开：零距离也可消费全局/玩家周期。','前方通行增加位置/距离但完成计步相同。','未完成只创建前缀不消费周期。','事件触碰成功不创建本次碰撞链。','对角失败不新增碰撞链或周期。','强制仍真/WAIT后继时两一般通知但不进玩家周期。','一般消费者失败与首玩家消费者失败保留不同前缀。','无完成更新不保证最终计步/清理/回滚。'])
series('PD',[
'未知物种守卫族无效/假/0，与登记解引用失败分开。','普通登记展示形态P及无名归0。','无性别归雄档0。','首次末次记录保持，最近见到显式覆盖。','任一异色查询与形态计数仅0/1的限制。','区域访问需解锁与已见，全国另计。','捕获提示受已解锁区域包含门，全国解锁短路。','负/越界解锁作用全国位。','零区域时全国默认视图。','使用当前区域设置与地区越界全国映射。','空/缺区域成员返回nil，计数遍历可失败，编号/长度/主列表回退分列。','编译重复分节/物种报错，不产部分保存。','排序/搜索seen与owned资格门各异。','未拥有信息占位与战斗数=败+捕。','形态结构/名称/性别与显示全部门。','栖息地全版本枚举可混v0，单get版本优先独立。','赠送双满门与入队/交换登记/蛋构造副作用分开。','首次捕获计数→见过/拥有/提示/最近见到/页，重复不新物种提示。','浏览形态覆盖末次并随玩家字段存档请求保留。','UNOWN2精确已见真但计数0；只计0/1。','直接同基种键覆盖，同原形态不同键不归并/不刷新。','全国解锁先true，锁定未知false。','不刷新set_seen保持缓存；clear不清解锁表。','已构造对象两静默入队入口seen差异与owned同写。','摘要首个解锁即停，简略继续查编号。','ALCREMIE8普通登记展示7，最近见到按当前名归0。','当前有名/展示无名：普通归0而最近见到保留P。','搜索Start先持久模式写4，空结果取消保留；会话旧参数与重开初始化分开。','Cancel-before-Start无写；结果BACK清结果态/模式/参数并恢复游标。','区域菜单两计数与长度不作第三数，完成标记分开。','RATTATA具名形态两性只一项，显示全部仍不放宽结构门。','基础nil/空串标签、同图/异图、性别项数和标签条件分列。','One Form由结构多形态决定，空串不替代nil。','多项选择器首轮写末次且BACK不撤销，单项不进入。'])
for i,s in enumerate([
'内部实际出场给战斗玩家Dex写seen/形态/空末次，不改owned/两计数。','非空末次保持，重复登记幂等。','替换/伙伴/敌实际出场均需到共同登记，取消不达。','非内部实际出场门拒绝，不推广其它入口。','未出场后备不会仅在队中就登记。','登记前失败无写，刷新失败可留seen/形态/末次前缀。','静默入口原对照保持，地区门不无条件解锁。'],1):meaning[f'GR7-M14-002-C{i}']=s
for i,s in enumerate([
'摘要完整单条保存视图-1索引末地区编号001，与摘要/简略全国152不同。','视图0/1和空缺表编号0，场景成功仍需资源。','偏移按选定视图-1而非实际末表号。','当前区域开关决定选表，地图场景解析另行。','打开前调用方最近见到已写，BACK不回滚，取消-before-view无写。','场景/资源失败留已写最近见到，不保证关闭/清理/返回。','PD25/普通图像请求/主列表规则保持，无未来兼容或像素保证。'],1):meaning[f'GR7-M14-001-C{i}']=s
series('R6-PD',[
'首轮置普通记录，再UP回绕末项下一轮覆盖，BACK保留；后续读取形态1。','末项DOWN回绕首项下一轮覆盖，BACK保留；读取形态0。','普通前移后USE不撤销；只末次变，不改seen/owned/可访问缓存。'])
series('VF',[
'盒/余额入口门，零币免费与99999拒绝。','行和/雷数提示翻后不减。','乘法奖额1→2→2→6，未领不写余额。','标记非保护，普通仍翻。','已揭格可改标记不改分。','拒绝退出保原盘/奖。','领奖写余额/统计先于揭盘等待。','未揭退出不领。','所有倍率揭完即过关，不必翻1。','一级踩雷不领不扣、重开一级。','高等级倒置clamp失败边界，不假称正常重开。','八级过关支付后仍八级。','币上限只实际加1/统计1，提示仍6。','免费数等阈值拒绝，严格边界。','1000次失败返回末盘可违阈值。','倍率行有雷列无雷仍免费，计行列。','固定积24/3456不是预期收益。','领取后揭盘中断不撤余额，无关闭保证。'])
series('LT',[
'日期种子1037630不声称具体随机号码。','五位字符串填零。','同日期相同实现同号，跨日不调用变量不自动变。','00007匹配五位。','尾三位匹配后千位失配停。','个位失配0。','只最低五位比较。','非数字文本to_i0的合法限定。','蛋可胜且队伍先同分保留。','箱按顺序严格胜者，首同分不替换。','空队/空箱/全0结果空名0/0及变量读数。','首遍nil成员失败，三输出未写旧值可留。','同变量号最后匹配值覆盖。','5001生成跳写仍可刷新，检索跳项无刷新。','零长度盒忽略按实际容量走。','低16公开号匹配，与完整owner ID区分。'])
series('U05-HAB',[
'宽3/10000仅一亮点，ceil高度2与地图游标长度折算可指缺尾。','11111五亮点不补第六。','缺省/宽0单格回退仍受可见Point/隐藏/区域/遭遇资格门。','可见点并集与名称/详情/治疗首条查询不同，顺序互换对照。'])
series('R4-PD',[
'末次shiny真/假都普通预览，记录不清。','Info/Forms/图标/简略普通请求；摘要调用方最近见到另写。','任一异色资格通过但普通展示，不新增普通seen位。','只有异色素材不替代普通目录请求，资源/host失败未知。','多项首轮写false/BACK不撤，单项不进入，普通刷新保持true另门。'])
for c,s in zip('ABCDEFG',[
'MapSize字符2亮，非权重。','字符1亮对照。','字符0不亮。','字符x转换0不亮。','字符9仍一格不增亮度。','Point关闭/隐藏/区域/无物种各资格独立阻挡。','保原10000/11111/默认/可见并集与首条三查询控制，不执行生成器。']):meaning['U06-M11-001-'+c]=s
meaning['U06-M11-005-VF']='翻面/效果局部时段与已揭/分数提交分开，阶段中不收普通操作。'
meaning['U06-M11-005-VFEND']='雷/全盘揭示/等待/专门确认/收牌后续顺序；奖励不回撤，高等级失败前缀保持。'
series('R5-BP',[
'消息微更新可先跨生命周期重植，再拒摘不回滚成熟。','同秒快速拒摘先退出，不做该轮微更新/采摘reset。','先微更新再满包不采摘，重植保持且后消息可继续结算。','确认提交用旧qty3，统计后真返回才外层reset，异常和直工具分开。'])
series('C01F-014-',[
'仅[1]缺0，最终缺口失败不保存。','显式空[0]+[1]通过缺口/重复，不保证运行计数消费。','[0]/[2]缺1最终失败不自动补空。','全空可保存空集合，无头物种读取拒绝。'])

meta={3:('CATALOG_CONTRACT','ID/完整输入前提/推导预期三列，全部静态与独立算术非运行测试；WP53/SF为FAC，其他具名正文为外域主合同。'),5:('PROVENANCE','B18旧批准仅限旧字节/路径重映射；本轮新字节仍独立复核，旧链不授阅读或当前行为通过。'),119:('SHARED_PREMISE','R7碰撞完整公共夹具、独立替代与正常/异常不合并；原移动合同为primary。'),132:('SCOPE','R7不改变FP旧正常/强制通知/毒伤/注册/Repel门，实际到达条件保留。'),189:('SHARED_PREMISE','R6合法RATTATA双项、逐轮独立输入与普通写false前提，不作UI/runtime资格。'),197:('SCOPE','结构/性别/标签/单项不开保持；回绕归UI主合同。'),245:('SCOPE','合法01文本有限向量；原PD16全版本枚举保持，不扩大非01/native/任意坏输入。'),247:('SHARED_PREMISE','有效区域/版本/遭遇/元数据/地图位置/宽文本/Point及资源正常，无插件，各行独立。'),256:('ALGORITHM_REFERENCE','行优先已有字符占格映射、非零及可见并集门，缺尾不补；v0枚举与单get优先分开。'),260:('SHARED_PREMISE','合法默认已见拥有BULBASAUR/shiny末次，Forms外成对独立，资源差异条件而非像素证据。'),270:('SCOPE','异色维度/形态性别/通用资源服务与其它展示主合同保持，历史批准不替代新字节。'),274:('SHARED_PREMISE','U06只逻辑状态/请求/属性且依赖正常，输入服务快照不证物理键/Demo，媒体native未知。'),290:('QUALIFICATION','U06动画向量与UI同静态期望，未执行。'),299:('SHARED_PREMISE','R5独立条件、无额外写/正常步骤与异常实际前缀；无host/DemoPASS。'),310:('SHARED_PREMISE','C01编译向量独立合法数据/前序正常/无覆写；未执行编译/文件IO/native。')}
headers={54,79,121,136,191,201,224,249,262,278,292,301,312}
assert len(meta)+len(headers)==28
def primary(line):
    if line<=75:return 'WP60 Berry / foreign WORLD primary'
    if line<=132:return 'WP61 Field passive/blackout + movement / foreign WORLD, creature, KERNEL primaries'
    if line<=197:return 'WP62 Pokedex / foreign creature-D, PBS and UI primaries'
    if line<=220:return 'WP69 Voltorb / foreign UI primary'
    if line<=241:return 'WP70 Lottery / foreign WORLD/UI primary'
    if line<=286:return 'WP62 habitat/records with WP63/66 / foreign UI, WORLD, creature-D and PBS primaries'
    if line<=295:return 'WP69 animation / foreign UI primary'
    if line<=306:return 'WP60 message micro-update / foreign WORLD/UI primary'
    return 'Regional compiler / foreign PBS and KERNEL primary'
contact={
 'FP20':[2301,2302,2303,2304,2310], 'FP21':[1799,1800], 'FP24':[2290,2306,2307,2309,2327,2328,2329,2330,2331,2332,2333,2334],
 'FP27':[164], 'FP31':[2299,1799,1800], 'PD01':[2345,2346,2348], 'PD07':[2351], 'PD11':[2350,2351],
 'PD18':[1685,2294,2295,2296,2297,2345,2346,2348,2349,2350,2351], 'PD22':[2351], 'PD23':[2345,2350], 'PD26':[2349], 'PD27':[2349],
}
rows=[];seen=set()
for x in seeds:
    line=x['line'];text=lines[line-1]
    if line in headers:kind='TABLE_SCHEMA';focus='表头标记完整输入/前提、期望与执行状态角色；不增加源行为原子。';code=None
    elif line in meta:kind,focus=meta[line];code=None
    else:
        code=text.split('|')[1].strip();assert code in meaning,(line,code);seen.add(code);focus=meaning[code];kind='FOREIGN_PRIMARY_CASE_SCOPE'
    supports=[f'FAC-A{i:04}' for i in contact.get(code,[])];assert all(s in by for s in supports)
    rows.append({'id':x['old_locator_id'],'line':line,'formal_line_sha256':sha(text.encode()),'literal_case_id':code,'kind':kind,'complete_column_meaning_received':True,'manual_case_focus':focus,'complete_input_expected_text_reference':{'fixed_B8_path':path,'line':line,'sha256':sha(text.encode())},'primary_scope':primary(line) if line>5 else 'Global catalog scope/provenance','local_FAC_purpose':'Necessary FAC contact reconciled only to explicitly listed already-read source facts; all other full foreign behavior remains with named root primary.' if supports else 'Foreign primary case, shared premise, layout or provenance. Complete literal columns read; no new necessary FAC consumer value identified. No local full foreign behavior approval inferred.','support_fact_ids':supports,'status':'COMPLETE_LOCAL_FAC_SCOPE_AND_NECESSARY_CONTACT_DISPOSITION_FOREIGN_PRIMARY_NOT_INHERITED'})
assert len(seen)==174 and seen==set(meaning),(len(seen),set(meaning)-seen)
name='F08-all202-local-scope-and-necessary-contact-dispositions.v2.json'
packet={'schema':'FAC-F08-all202-foreign-primary-scope-meaning-reception/v2','utc':utc,'reader':'/root/facility_atomic_completion_cloud','formal_identity':{'repo':repo,'commit':commit,'path':path,'bytes':len(raw),'sha256':sha(raw)},'actual_read':'Initial whole F08 all317 lines actually read in this same context. Fresh all202 remaining structures delivered in three complete windows (through133,134–241,242–317), all full literal inputs/expected columns and shared premises visible without truncation.','scope':'This is the required local FAC purpose/necessary-contact reception for202 foreign catalog structures. It is not a local independent re-review or approval of all WP60/61/62/69/70 source behaviors, nor174 new FAC case atoms. Foreign primary acceptance belongs to root current primary contracts; root has required only necessary finite contacts here.','rows':rows,'counts':{'original_structures':202,'foreign_case_rows':174,'explicit_premise_layout_provenance_structures':28,'new_source_assertions':0},'mandatory_contact_packet':'external-catalog-necessary-contacts.v2.json plus actual SF40/terminal/capture/storage/FIP/bootstrap/micro-update receipts and all fact premises','contact_qualification':'FP27 ordinary internal-battle propagation itself is foreign primary; local support only names the already-proved facility internalBattle=false write, not a new propagation proof. FP21/31 use actual non-egg heal/egg early return and caught-storage ready_to_evolve preservation; no generic system expansion. PD/Dex contact writes and refresh/fallback failures retain exact original premises.','source_execution':'NOT_EXECUTED','new_required':0,'new_optional':0,'new_votes':0,'UPDATE_NOT_STARTED':True};save(name,packet)
added=0
for x in rows:
    for aid in x['support_fact_ids']:
        a=by[aid];rev['mappings'].append({'formal_clause':x['id'],'formal_child_id':f'FAC-F08-CONTACT-{x["literal_case_id"]}-{aid}','atomic_assertion':aid,'meaning_reference':name+'#'+x['id'],'source':a['source'],'source_unit':a['unit_locator'],'premise':a['premise'],'status':'FINITE_FAC_CONTACT_ONLY_FOREIGN_PRIMARY_SCOPE_RETAINED','pending_dependencies':[],'relation':'EXISTING_FACT_NECESSARY_CONTACT_NO_WHOLE_FOREIGN_INHERITANCE'});added+=1
save('reverse-mapping.json',rev)
n['unmet_formal_seed_structures']=[x for x in n['unmet_formal_seed_structures'] if not x['old_locator_id'].startswith('F08-')]
for x in seeds:n['closed_finite_formal_seed_structures'].append({**x,'status':'COMPLETE_LOCAL_FAC_PURPOSE_DISPOSITION_FOREIGN_PRIMARY_REMAINS_ROOT','receipt':name})
n['external202_current_disposition']='All202 complete local purpose/necessary contacts disposed; complete foreign primary behavior is not locally inherited or re-audited. Root current foreign primary signatures remain separate.';save('next-dispatch.json',n)
l=load('reading-ledger.json');l.setdefault('v2_exact_receptions',[]).append({'utc':utc,'packet':name,'actual_read':'Fresh complete202 full original structures in3 contiguous nontruncated windows;174case scopes+28metadata/premise/layout purposes manually distinguished.','qualification':'No foreign fullsource/statusinheritance; necessary local facts only. No source/businessmodel/Ruby/native execution.'});save('reading-ledger.json',l)
b=(v/name).read_bytes();print(json.dumps({'packet':name,'bytes':len(b),'sha256':sha(b),'rows':len(rows),'bindings_added':added,'remaining_seeds':len(n['unmet_formal_seed_structures'])}))
