#!/usr/bin/env python3

# Historical author step: never overwrite later calibrated evidence.
import hashlib as _r3_hashlib, pathlib as _r3_pathlib
_r3_guard_manifest = _r3_pathlib.Path(__file__).resolve().parent.parent.parent / 'routing-manifest.json'
if _r3_hashlib.sha256(_r3_guard_manifest.read_bytes()).hexdigest() != '35175c7094b008e77af35cf6a7811c5fcd6f1a0dd20020b64d32b40d5670256e':
    raise SystemExit('Historical R3 author step refuses changed/final manifest; use fixed archive and recorded patch for audit.')
"""Prepare explicit R2-review dependency repairs; never writes the manifest."""
import json,pathlib,subprocess,hashlib,copy
R=pathlib.Path(__file__).resolve().parent;H=R.parent.parent;ROOT=H.parents[2];FINAL='5f87743293290de2e219ecdd6c19e88280f60c9a'; REVIEW='0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add'
m=json.loads((H/'routing-manifest.json').read_text());fs={int(f['feature_id'][3:]):f for f in m['features']};patch=json.loads((R/'source-refinement-patch.json').read_text());assert patch['status']=='PREPARED_NOT_YET_APPLIED';byid={x['feature_id']:x for x in patch['records']}
# Each row is a source judgment, not a keyword rule. remove/add IDs and purpose are explicit.
C=[
(61,[739],[], '物品C/I/R/P、Belch和奖金标记不消费招式/PP包装；740明确承担写穿/还原，4初始化和31正常终局继续保留。'),
(66,[739],[], '离场/濒死的HP、状态、形态及紧张感持物触发没有PP同步调用；740持物及正常终局/初始化交界保留。'),
(69,[739],[], '回合末四族是天气/HP/状态/阶级和取物；取物还原记录由740承接，不能借同WP20把PP同步加入本源。'),
(186,[32],[31], '登记预扣/复检退款及残留身份的正常终局消费者在WP42§6/6.0/31，外层§7治疗不承担退款。'),
(190,[32],[31], '主动药品HP请求/封顶沿145、登记退款沿11及31；伙伴/世界全队治疗不同于主动药品，不拿32替代。'),
(192,[40],[39], 'GuardSpec建立Mist=5并依侧期限递减，属WP45§6.2/39；§7/40交换/清屏障不是建立或期限责任。'),
(244,[263,265],[], 'GiftMaster、会话、Export及人工线上四层自有合同不走六类PBS编辑器；保留241礼物载体和243管理Receive调用，既有WP17输入直接引用保留。'),
(741,[421],[420], 'battle_money_gained/lost实际在WP06 stats§6/420，421只有商店/币/BP/煤灰；31正常终局和579→755奖金标记导航保留。'),
(348,[355],[364], '布局符号→图块编号/墙/自动邻接是三层地图数据，输出供364地图图块绘制；不是355音频播放，生成346/347和324地图交接保留。'),
(372,[355,358],[366], '元数据天气意图与固定渐变的实际消费者为WP16世界显示§5/366；战前特殊过渡358与音频355不承接天气，324/325转移生命周期保留。'),
(373,[33,355,358],[366], '九天气粒子/平铺/色调/白闪由366世界天气/屏幕效果消费，372应用管线保留；战斗异常33、音频355和战前过渡358均无该用途。'),
(487,[25,26],[29,208], 'Shadow经验/EV暂存与友好门交WP42成长29、WP30分配204/设置205/友好208；WP41换人失败/配置25/26不是成长合同，净化恢复748与持物578保留。'),
(608,[670],[665,666,667], '展示/区域/搜索/形态的真实UI在WP66-B的665/666/667；670是WP66-C背包过滤，不能从同WP66号转授图鉴职责；604–607和669保留。'),
(664,[157,158,159,160,161],[164,165,166,167], '盒子即时移动/释放/持物/标记和退出实际消费WP25容器164、仓库流165、入口守卫166和持久交界167；157–161全部是WP24伙伴/身份钱包/训练家装载配置，完整有效源不承本节。'),
(681,[25,26],[29,207], '经验/逐级显示、学招持久与战斗双提交由29/204/205/206/207/739共同承接；WP41失败/配置25/26不承担成长。735仅为写生复制与一般学习的明确排除性对照，不把其效果当学习执行。'),
(682,[157,158],[162,164], '捕获队列、命名、满队选择和送盒左移消费WP38的528–531及WP25容量162/接收164；伙伴参战/战后治疗157/158不承担接收UI，11/29/31保留。'),
(749,[157,158,172,667],[164,166,662,664], '净化室是同个体引用移动/替换与储存选择：WP25容器164、守卫166及WP66-B储存入口662/操作664，690净化室界面保持；伙伴、脚本交换改属主和图鉴Forms均非本操作。'),
(751,[355,358],[365,425], 'L95只负责摇草动画请求→列表写入→0.5秒等待，真正世界角色/临时格动画在365、计时在425；365可再交付其具名SE定时，不能由751直接把音频族或战前过渡当动画合同。'),
(754,[25],[29], '两成长持物族明确WP50§6/578和WP42/WP30成长29/204；换人失败25不是EXP/EV倍率消费者。'),
(755,[25],[29], 'EXP.SHARE/奖金世界输入交29/204成长、31终局、148个体物及153钱包，578持物处理保留；换人失败25无此作用。'),
(756,[650],[], 'Safari回起点为地图场景门/下车/转移，324/326已有转移和恢复导航；训练家卡650的独立只读开关场景无用途。'),
(757,[650],[645], '单调倒计时425、消息625/选择626与暂停循环微更新645是真实交界；训练家卡650不负责倒计时或微更新。'),
(759,[650],[643,645], '活动信息/专用退出/普通Quit/共享保存的主消费者是643保存退出和645暂停注册项；444/446持久保存与580/582会话不动，650训练家卡无此作用。'),
(764,[650],[], '中心/家失败回程设置地图转移/刷新交324/326，650训练家卡场景无此作用；其它未列字段与原责任保持。'),
(760,[355,358,643],[325,352,365], 'L70/L84–88是植物显示更新/资源/事件朝向及闪光：325地图显示生命周期、352图像身份解析和365角色显示交接；不含音频、战前过渡或保存退出。'),
(761,[186,650],[670], '施肥/种植/采摘是过滤背包670、容器177、领域结算590和确认626；不使用战斗预扣复检186或训练家卡650。'),
(762,[186],[183,670], 'Repel到0再次选择是普通道具使用183和按旗标过滤背包670，非战斗登记复检退款186；地图运动330、BGM355、消息625和确认626的具名调用保留。'),
(766,[699],[], 'Voltorb局部格翻面/效果/揭盘/收牌是本活动有序阶段，与Slot三轮停止滑移699完全不同；保留真实625确认/消息交界，不造逐动画阶段ID。')]
records=[]
def uni(a,b):return a+[x for x in b if x not in a]
def dep(i,reason):f=fs[i];return {'document':f['source']['document'],'anchor':f['source']['anchor'],'reason':reason}
for n,remove,add,why in C:
 f=fs[n];fid=f['feature_id'];old=copy.deepcopy(f['dependencies']);new=copy.deepcopy(old);new['feature_refs']=uni([x for x in old['feature_refs'] if int(x[3:]) not in remove],[fs[i]['feature_id'] for i in add]); assert all(fs[i]['feature_id'] in old['feature_refs'] for i in remove)
 if n in [186,190]:
  new['direct_refs']=[dep(31,'正常战斗对象终局§6/§6.0按残留物品身份退款；这是共同收尾，不能由外层世界治疗替代。') if x['document']==fs[31]['source']['document'] and x['anchor']==fs[32]['source']['anchor'] else x for x in new['direct_refs']]
 if n==192:
  new['direct_refs']=[dep(39,'GuardSpec的Mist建立5回合及阵营期限递减在§6.2；不把侧交换/清除当建立。') if x['document']==fs[39]['source']['document'] and x['anchor']==fs[40]['source']['anchor'] else x for x in new['direct_refs']]
 for i in add:
  d=dep(i,'R3依赖精准修复的真实用途：'+why)
  if not any(x['document']==d['document'] and x['anchor']==d['anchor'] for x in new['direct_refs']):new['direct_refs'].append(d)
 change=[]
 for key in ['feature_refs','direct_refs']:
  if new[key]!=old[key]:change.append({'pointer':'/dependencies/'+key,'before':old[key],'after':new[key]})
 x=byid.get(fid)
 if x is None:x={'feature_id':fid,'current_source_evidence':{'commit':FINAL,'document':f['source']['document'],**f['current_applicability']['locator']},'field_changes':[]};patch['records'].append(x);byid[fid]=x
 assert not any(c['pointer'].startswith('/dependencies/') for c in x['field_changes'])
 x['field_changes'].extend(change)
 difference='R3接收R2独立FAIL依赖整改：'+why+' 逐边证据：revisions/r3/dependency-repairs.json#'+fid+'；作者修正待独立复审。'
 prior=next((c for c in x['field_changes'] if c['pointer']=='/differences'),None)
 if prior:prior['after']=uni(prior['after'],[difference])
 else:x['field_changes'].append({'pointer':'/differences','before':f['differences'],'after':uni(f['differences'],[difference])})
 group='COMBAT-R2-DEP-001' if n in [61,66,69] else 'R2-CRE-DEP-001' if n in [186,190,192] else 'R2-CRE-DEP-002' if n in [244,741] else 'POK-WORLD-R2-DEP-001'
 records.append({'feature_id':fid,'finding_ref':group,'fixed_review_commit':REVIEW,'current_source_evidence':x['current_source_evidence'],'immutable_source':f['source'],'effective_scope':f['functional_scope'],'rationale':why,'removed_edges':[{'target_feature_id':fs[i]['feature_id'],'target_immutable_source':fs[i]['source'],'target_current_source':{'commit':FINAL,'document':fs[i]['source']['document'],**fs[i]['current_applicability']['locator']},'reason':why} for i in remove],'added_edges':[{'target_feature_id':fs[i]['feature_id'],'target_immutable_source':fs[i]['source'],'target_current_source':{'commit':FINAL,'document':fs[i]['source']['document'],**fs[i]['current_applicability']['locator']},'reason':why} for i in add],'retained_feature_refs':[v for v in old['feature_refs'] if int(v[3:]) not in remove],'field_changes':change,'status':'AUTHOR_FIXED_PENDING_INDEPENDENT_REVIEW','all_other_facets_preserved':True})
patch['dependency_repair_feature_ids']=[x['feature_id'] for x in records];patch['fixed_R2_FAIL_report_commit']=REVIEW;patch['input_manifest_sha256']=hashlib.sha256((H/'routing-manifest.json').read_bytes()).hexdigest();patch['patch_groups']={'source_responsibility_dependency_refinements':6,'direct_source_delta_annotations':51,'R2_review_dependency_repairs':28};(R/'source-refinement-patch.json').write_text(json.dumps(patch,ensure_ascii=False,indent=2)+'\n');(R/'dependency-repairs.json').write_text(json.dumps({'schema_version':'routing-r3-R2-dependency-repairs.v1','role':'AUTHOR_REPAIR_NOT_INDEPENDENT_REVIEW','fixed_report_commit':REVIEW,'status':'PREPARED_PENDING_APPLICATION','records':records,'same_root_additional_removed_edges':['751→355','760→355','664→159','664→160','664→161'],'retained_positive_controls':['68/71→739: actualPPgate/copy/DANCER/IMPOSTER','742→263/265: real shared trainer editor','744→650: source Hall-of-Fame contains trainer data card','735→207: explicit excluded global learning contrast','741→579→755: explicit parent child money-mark navigation']},ensure_ascii=False,indent=2)+'\n');print('prepared',len(records),'dependency rows,',len(patch['records']),'merged feature rows,',sum(len(x['field_changes']) for x in patch['records']),'explicit changes')
