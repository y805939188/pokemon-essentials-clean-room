#!/usr/bin/env python3
"""Render author repair evidence from frozen routing data; does not mutate routing data."""
import collections
import hashlib
import json
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parents[2]
ROOT=HERE.parents[2]
OUT=HERE/'revisions/r1'
REVIEW='a0352c7fba38391afc535525988245701d5ce202'
BASE='d62b41f4d620e50bb04c80a7505374bd284d8210'
SOURCE='fd1df570cad987dc3852a3b958f03916e317f7fe'
def read(p):return json.loads(p.read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def fid(n):return n if isinstance(n,str) else f'FR-{n:06}'
m=read(HERE/'routing-manifest.json')
res=read(OUT/'feature-resolution.json')
units=read(OUT/'new-and-retired-units.json')
review_root=Path('/tmp/r8-disposition-review-a0352c7')
findings=read(review_root/'findings.json')['findings']
active={x['feature_id']:x for x in m['features']}
retired={x['feature_id']:x for x in m['retired_features']}
old_manifest=json.loads(subprocess.check_output(['git','show',BASE+':planning/implementation-routing/r8-20261017/routing-manifest.json'],cwd=ROOT))
old_features={x['feature_id']:x for x in old_manifest['features']}
rows={x['feature_id']:x for x in res['rows']}
assert len(rows)==len(active)+len(retired)-len(units['new_rows'])
assert not res['unhandled_prior_nonpass']
assert all(x['source_identity_preserved'] for x in rows.values())
groups={
'CK-BATTLE-001':('保留147/148/153的领域父行，739/740/741单列PP、持物还原记录、战斗奖金/败款协作；列身份/顺序/异常和对应真实依赖。',[147,148,153],[739,740,741]),
'CK-META-001':('恢复WP27 §2.1定义缺省与§2.2逐槽数量显示，分别归框架与MZ消费；不以概念标题略过行为。',[],[722,723]),
'COMBAT-01':('FR10排除4.2.1，731覆盖退款残留身份、二次退款与下轮/失能直接清；绑定物品原型和背包/终局消费者。',[10,11],[731]),
'COMBAT-02':('FR4/61/66/68/69/71改为明确协作，分持久状态/还原记录与场上临时状态；735单拆模仿/写生两次提交。',[4,52,61,66,68,69,71],[735]),
'COMBAT-03':('音频请求/交付、目标选择、换人选择、设施多选、Arena裁判和回放残余输入有独立MZ子行；父当前范围排除子行。',[5,10,18,114,129,136],[732,733,734,736,737,738]),
'COMBAT-05':('补背包/主动物品、成长及个体/队伍、终局还原、存档/迁移与图鉴真实合同，保留旧WP索引并新增可定位直接引用。',[11,22,29,61,124,136],[]),
'COMBAT-06':('替补拒绝导致逃离和招式逃离分别改协作并绑定PROTO-ESCAPE；保留正常换人各自资格差异。',[20,58],[]),
'DS-001':('战斗测试和120项四层调试明列框架持久层/Showdown真实战斗状态/MZ白名单交互，绑定四类原型及用户工具范围门。',[257,261],[]),
'KF-002':('435日志格式/日志失败/0或1控制流由框架拥有，窗口控制台由MZ；439语言菜单、445启动/地图恢复、451存档备份/场景失败前缀分别列实际职责。',[435,439,445,451],[]),
'KF-003':('普通随机父行排除5.3，745单列记录初态/命令/随机/换人序列与回放消费协作，关联WP58并保留未运行边界。',[427],[745]),
'POK-S01':('补未知变化失败/伤害回退/PP不退及SHADOWSHED绑定边界，补彩票整数转换/低16位/五位匹配真实行为。',[],[724,725]),
'POK-S02':('484/485/487/488明确战斗派入/Call/捕获快照、持久招式不自动重建场上副本、经验EV暂存与战斗香登记复检/退款；绑定成长/物品/捕获原型。',[484,485,487,488],[748]),
'POK-S03':('519改协作，持久漫游个体跨战复用、PP/异常/对方持物与逃离/决定/终结记录分别列；补WP41与PROTO-ESCAPE。',[519],[]),
'POK-S04':('543/574/576/577明确持久异常/计数、C/I/R/P/Belch、LEPPA同下标强写、转物与负选择已耗；754/755单列成长目录族与世界/奖金输入。',[543,571,574,576,577,579],[754,755]),
'POK-S05':('按标记/缎带、净化室编成、交换重复收尾、雷达、Safari转移/捕虫计时判奖、暂停保存、树果显示和交互、野外宿主交接/调试、翻牌阶段拆MZ单元；608本身改明确MZ消费者。',[465,489,505,520,522,580,582,585,590,591,596,598,600,601,608,611],list(range(746,753))+list(range(756,767))),
'POK-S06':('492保留5.1动画/取消，743承接5.2–5.4统计/持物/额外个体/扣球/物种HP/图鉴/学招的框架提交。',[492],[743]),
'WU-01':('补战前包装§1、Duel§2、老虎机§1、挖矿§1和61候选主表；保留旧特殊注册/铁表身份，来源资格707归档。',[358,706,707],[726,727,728,729,730]),
'WU-02':('特殊活动矩阵/随机/资源账/形状摆放/削层/结算/排列角度/洗牌与不变量归框架；逐行列MZ采样/渲染/时间读回，767/768独立忙门。',[695,696,702,705,706,709,710,711,714,715,716,717,720,721],[767,768]),
'WU-03':('677–682及684成为明确三方协作消费者，精确关联已有领域规则与四类原型，MZ只拥有具体输入/呈现职责。',[677,678,679,680,681,682,684],[]),
'CAI-01':('对全部41个AI旧ID分策略常量/偏好、实时规则查询、共享准备字段与真实登记；75专门列items/ally_items和AI上下文缺索引整段失败，不假设Showdown自带该AI。',list(range(73,114)),[]),
'CAI-02':('AI责任/保留三节81/97/108归档为元数据，原完整行与immutable source保留，引用活跃策略/查询功能。',[81,97,108],[]),
'CAI-03':('补52A/B/C、真实状态/命令/换人/物品与20/27/28等评分读取边；预测值与实际执行合同分别验证。',[76,79,88,89,92,93,98,99,100,101,102,109,110,111,112,113],[]),
'CC-CATALOG-F01':('creature-rpg-wp35-36-57-64-68测试目录按明确Triad正文限定消费者；删除全部Duel误关联，保留Triad247–252。',[],[]),
'CK-DEP-001':('补PP/持物的WP42/50/64、伙伴WP39/41、储存迁移/捕获/净化室、道具Shadow/邮件/野外、成长战斗阶段和孵化命名/图鉴实际消费者。',[147,148,155,157,158,186,187,190,191,192,204,207,221],[]),
'CK-MIXED-001':('租借/交换两屏取消与最终队伍提交、Triad手选/随机及repeat/trigger仲裁分别列框架与MZ职责；特殊范围不自动纳入。',[235,236,249,250],[]),
'CK-MZ-001':('逐行给玩家外观/名字、守卫UI、获得/交换、背包PC/快捷、教学商店、成长/重学、寄养、信件和礼物下载的真实状态提交与输入/等待职责。',[152,166,171,172,178,179,183,196,197,205,206,213,239,240,242],[]),
'CK-TOOLS-001':('正常训练家装载留154，742拆新建作者工具；244礼物编辑/管理/导出列MZ/框架分工，二者接用户范围门。',[154,244],[742]),
'COMBAT-04':('46/47/56/57/63/122/131作为身份覆盖、责任或历史静态批准元数据归档；不使用不纳入目标规避。',[46,47,56,57,63,122,131],[]),
'DS-003':('266同文件归属和WP77的317–322配置/能力候选/一致性/缺口全部归元数据，关联实际消费者；不创建未经授权Demo复刻目标。',[266,317,318,319,320,321,322],[]),
'DS-004':('WP74六必需、WP75七必需、WP76具名必需/交界完整补入直接引用；WP77依赖通过metadata-dependencies及活跃消费者关联保留，区分源WP计划与正文责任。',list(range(277,323)),[]),
'KF-001':('392未验证组合、398字段责任目录、407编译交界转元数据，完整旧ID/旧行归档并关联已有功能。',[392,398,407],[]),
'KF-004':('身份/编译/诊断/插件、统计生产点、计时/计步、种子地牢、语言与持久化/迁移的遗漏合同按具体源锚点补齐；同时复核其它文档明列共同前置。',[395,396,401,413,416,420,423,425,426,428,430,436,448,449],[]),
'KF-005':('449/450旧数组/表格式和版本转换目录设待决策，引用DEC-SPECIAL-AND-HOST-SCOPE并询问具体旧版本支持范围。',[449,450],[]),
'KF-006':('DOC0062及415–424改为源文未单列分类的统计行为/数据附表，不再虚构共享导航/无实现承诺。',list(range(415,425)),[]),
'POK-S07':('八个来源/向量/覆盖/冻结依赖章节转元数据，完整历史行与稳定ID保留，关联实际主规则和验收消费者。',[478,480,482,500,539,553,573,618],[]),
'POK-S08':('537保留战斗开关与样本，753单列作者Type/Move缺省、Category×Power校验及本地化字段，由框架拥有并引用WP03/04/08。',[537],[753]),
'WORLD-CATALOG-F01':('世界WP60目录删除berry-plants、UI WP70目录删除Lottery误消费者；按子体系文档身份限定，保留实际Voltorb等具名交界。',[],[]),
'WORLD-CATALOG-F02':('四个具名标题追加碰撞后全局步进、退款/自然之恩、Safari捕获和重学真实消费者，并由消费者保留协作原型关系。',[596,187,11,31,49,554,555,577,581,206],[]),
'WU-04':('744单列名人堂克隆/容量裁剪/编号/PC门持久记录，691保留成员演出/浏览。',[691],[744]),
'WU-05':('684特殊模式/回放与690净化室消费者均设待决策并接同一特殊体系范围门，不由阶段待定替代用户范围决定。',[684,690],[]),
'WU-06':('326依WP09恢复门、384依捕获/战斗环境/结果、659依WP30学习重学及统计，均增加实际固定文档锚点。',[326,384,659],[]),
'WU-07':('345口径、704老虎机冻结依赖、707挖矿来源资格、713挖矿未决均归元数据并关联真正规则/表现单元。',[345,704,707,713],[])
}
root_tool=read(OUT/'tools/root-tool-resolution.json')
root_groups={x['id']:x for x in root_tool['findings']}
assert len(groups)==42 and len(root_groups)==2
out=[]
for g in findings:
    key=g['id']
    if key in root_groups:
        row=dict(root_groups[key]);row['author_disposition']='REVISED_PENDING_INDEPENDENT_REVIEW'
        row['evidence_owner']='/root';out.append(row);continue
    why,oldids,newids=groups[key]
    affected=set(map(fid,oldids))|set(g.get('feature_ids',[]))
    affected|={c['feature_id'] for c in g.get('cases',[]) if 'feature_id' in c}
    affected|={k for k,v in rows.items() if key in v['finding_refs']}
    metas=[x['metadata_id'] for x in m['metadata_records'] if set(x['retired_feature_ids']) & affected]
    out.append({'id':key,'prior_severity':g['severity'],'author_disposition':'REVISED_PENDING_INDEPENDENT_REVIEW',
        'specific_correction':why,'prior_feature_refs':sorted(affected),'new_feature_refs':list(map(fid,newids)),
        'metadata_refs':metas,'per_feature_evidence':[{'feature_id':x,'disposition':rows[x]['author_disposition'],
             'changes':rows[x]['changes']} for x in sorted(affected) if x in rows],
        'evidence':['routing-manifest.json','routing-policy.json','section-coverage.json','revisions/r1/feature-resolution.json'],
        'acceptance_boundary':'作者修正已保存；此项未由作者宣布PASS/CLOSED，需新的固定候选独立复审。'})
assert len(out)==len(findings)==44
write(OUT/'finding-resolution.json',{'schema_version':'routing-author-revision-findings.v1','original_candidate':BASE,
    'fixed_review_commit':REVIEW,'status':'AUTHOR_REVISED_AWAITING_INDEPENDENT_REVIEW','finding_count':len(out),
    'prior_nonpass_features':sum(x['prior_verdict']!='PASS' for x in rows.values()),'unhandled_prior_nonpass':[],
    'input_ledger':'tools/review-input-ledger.json','findings':out})

# Metadata carries source evidence/dependency navigation rather than future features.
wp77_targets=['wp04-pbs-lifecycle','wp02-rule-configuration-and-data-variants','wp11-map-topology-transfer',
 'wp12-terrain-movement-vehicles','wp13-map-events-npc-followers','wp14-random-dungeons','wp15-resource-matching-and-audio',
 'wp17-messages-windows-input','wp63-pokegear-map-music-and-phone','wp65-title-load-options-pause-and-pc',
 'wp66-a-party-and-summary-ui','wp66-b-storage-and-pokedex-ui','wp66-c-bag-item-storage-and-shop-ui',
 'wp67-a-battle-interaction-and-presentation','wp67-b-lifecycle-presentations-and-history','wp68-duel',
 'wp69-slot-machine','wp70-mining','wp71-tile-puzzles','wp36-wild-encounters-and-modifiers','wp57-factory-rentals-and-swaps',
 'wp64-mail-and-mystery-gift','wp27-bag-and-item-storage','wp53-safari-and-bug-catching-contest','wp60-berry-plants',
 'wp61-field-passive-effects-and-blackout','wp54-entry-eligibility-level-adjustment-and-clauses',
 'wp55-facility-session-and-restoration','wp56-palace-and-arena-variants','wp72-debug-contexts-and-controls',
 'wp73-a-content-editors','wp73-b-world-editors','wp74-battle-animation-authoring-and-exchange',
 'wp75-project-conversion-and-authoring-tools','wp76-facility-content-generation-and-simulation']
docs={Path(d['source']['path']).stem:d for d in m['documents']}
refs=[]
for target in wp77_targets:
    d=docs[target]
    refs.append({'document':d['source']['path'],'source_commit':SOURCE,
                 'type':'SOURCE_EVIDENCE_CONSUMER_NOT_NEW_DEMO_IMPLEMENTATION_PREREQUISITE',
                 'active_feature_refs':d['feature_ids'],
                 'reason':'WP77 §11.1具名来源合同；配置/入口候选/缺证关联这些既有消费者，不创建Demo实现任务。'})
wp77path=docs['wp77-demo-evidence-and-capability-coverage']['source']['path']
write(OUT/'metadata-dependencies.json',{'schema_version':'routing-metadata-dependency-navigation.v1',
    'source_commit':SOURCE,'source_document':wp77path,'source_section':'11.1 依赖（已净化交付件）',
    'metadata_refs':[x['metadata_id'] for x in m['metadata_records'] if x['source']['document']==wp77path],
    'dependencies':refs,'meaning':'来源依赖/证据消费关系；元数据没有实现阶段、去向验证或实现完成状态。'})

required={
'wp74-battle-animation-authoring-and-exchange':['wp15-resource-matching-and-audio','wp16-world-rendering-and-visual-transitions','wp67-a-battle-interaction-and-presentation','wp72-debug-contexts-and-controls','wp73-a-content-editors','wp04-pbs-lifecycle'],
'wp75-project-conversion-and-authoring-tools':['wp04-pbs-lifecycle','wp13-map-events-npc-followers','wp15-resource-matching-and-audio','wp17-messages-windows-input','wp08-localization','wp61-field-passive-effects-and-blackout','wp73-a-content-editors'],
'wp76-facility-content-generation-and-simulation':['wp54-entry-eligibility-level-adjustment-and-clauses','wp55-facility-session-and-restoration','wp57-factory-rentals-and-swaps','wp51-ai-action-selection-and-skill','wp52-a-generic-numerical-and-status-evaluation','wp52-b-field-damage-healing-and-target-evaluation','wp52-c-items-calling-and-control-evaluation','wp44-statuses-stat-stages-and-immunities','wp72-debug-contexts-and-controls','wp73-a-content-editors','wp75-project-conversion-and-authoring-tools','wp08-localization']}
write(OUT/'dependency-calibration.json',{'schema_version':'routing-author-dependency-calibration.v1',
    'old_wp_reference_type':'SOURCE_PLANNING_INDEX_REFERENCE; retained rather than claimed exhaustive',
    'document_wp_refs_type':'SOURCE_DOCUMENT_WP_MEMBERSHIP; not a complete dependency list',
    'direct_refs_type':'FIXED_FORMAL_CONTRACT_OR_NAMED_BOUNDARY_REFERENCE; reason defines usage, not all are mandatory implementation prerequisites',
    'explicit_dependency_source_ledger':'tools/source-dependency-excerpts.json',
    'required_and_named_shared_contracts':[{'source_document':docs[s]['source']['path'],
        'contracts':[docs[t]['source']['path'] for t in targets],
        'all_active_units_have_direct_refs':all(set(docs[t]['source']['path'] for t in targets)<=
           {r['document'] for r in f['dependencies']['direct_refs']} for f in active.values() if f['document_id']==docs[s]['document_id'])}
        for s,targets in required.items()],
    'metadata_dependency_navigation':'metadata-dependencies.json',
    'exclusionary_source_reading':[{'document':docs['wp68-duel']['source']['path'],
        'references':[docs['wp19-attributes-ability-and-stats']['source']['path'],docs['wp27-bag-and-item-storage']['source']['path']],
        'type':'SOURCE_BOUNDARY_COMPARISON',
        'meaning':'Duel源文为排除将生物数值/库存规则套入该活动而读这两份合同；引用不表示Duel伤害依赖生物能力，也不新增库存结算。'}],
    'limitations':['正文必需/同批共享/具名边界分层保留；未来实现的精确模块图仍须在用户范围和目标原型确定后评估。',
                    '目录标题/WP编号匹配不能证明语义依赖；不同子体系的相同WP编号已按实际文档身份修正。']})

prior_pass=[x for x in rows.values() if x['prior_verdict']=='PASS']
write(OUT/'retained-pass-propagation.json',{'schema_version':'routing-author-pass-propagation.v1',
    'fixed_review_commit':REVIEW,'prior_pass_count':len(prior_pass),
    'method':'保留独立复审中合理的章节去向；检查同根因元数据/混合界面/真实依赖并记录增补。旧PASS不是新候选自动PASS。',
    'rows':[{'feature_id':x['feature_id'],'prior_reason':x['prior_reason'],
        'prior_route':old_features[x['feature_id']]['future_plan']['destination'],
        'current_route':active[x['feature_id']]['future_plan']['destination'],
        'route_changed':active[x['feature_id']]['future_plan']['destination'] != old_features[x['feature_id']]['future_plan']['destination'],
        'source_preserved':x['source_identity_preserved'],'concrete_changes':x['changes'],
        'status':'RETAINED_SCOPED_ROUTE_WITH_EXPLICIT_PREREQUISITE_CALIBRATION_PENDING_REVIEW'} for x in prior_pass]})

source_units={}
for x in out:
    for key in x.get('prior_feature_refs',[])+x.get('new_feature_refs',[]):
        f=active.get(key,retired.get(key))
        if f:source_units[key]={'feature_id':key,'source':f['source'],
                 'current_functional_scope':f.get('functional_scope'),
                 'reading_claim':'SOURCE_LOCATOR_USED_FOR_AUTHOR_CORRECTION; not by itself a full-reading certificate'}
write(OUT/'source-reading-scope.json',{'schema_version':'routing-author-reading-scope.v1',
    'review_inputs':'tools/review-input-ledger.json','review_verdict_rows_consumed':len(rows),
    'formal_title_identity_inventory':'All indexed files/headings mechanically compared; this is separate from semantic reading.',
    'semantic_scope':'All domain reports and per-feature verdict/reason projections were consumed; fixed source reading targeted the reported clauses, mixed tables and explicit dependency sections.',
    'dependency_section_reading':'tools/source-dependency-excerpts.json; document dependency paragraphs read across domains; large-source display truncation does not confer a full-document reading claim.',
    'full_all_formal_clause_reading_claimed':False,
    'domain_source_reading':[
       {'domain':'creature-rpg','mode':'定向正文/表格读取；并非整域全文宣称',
        'feature_refs':list(map(fid,[147,148,152,153,154,155,166,171,172,178,179,183,196,197,205,206,213,221,235,236,239,240,242,244,249,250])),
        'specific_clauses':{'wp24':['3.2','3.3','4.4','5.3'],'wp25':['5'],'wp26':['3.3','4.2','4.3'],
          'wp27':['2.1','2.2','4.2','4.3','4.4','5'],'wp28':['3.2','3.4'],'wp29':['3.1','3.2','3.4','4'],
          'wp30':['5','6.2','6.3'],'wp33':['4'],'wp57':['3','4'],'wp64':['2.2','3','5','7'],'wp68-triple-triad':['4','5']}},
       {'domain':'pokemon-rules','mode':'问题源章/混合表格定向读取，不以定位清点冒充全文逐句审查',
        'feature_refs':list(map(fid,[465,484,485,487,488,489,492,505,519,520,522,537,543,571,574,576,577,579,580,582,585,590,591,596,598,600,601,608,611])),
        'topics':['Shadow战斗/净化/香及选择器','交换收尾和漫游持续个体','异常/PP/持物持久交接','Safari与捕虫计时/转移/保存','树果显示/等待','野外步进/回程/调试','图鉴搜索/查看写入与翻牌阶段']},
       {'domain':'combat-requirements','mode':'逐95战斗及41 AI裁定语义投影；战斗问题段和AI主动道具实际正文定向读取，八AI文档不冒称全字阅读',
        'feature_refs':list(map(fid,[4,5,10,11,18,20,22,29,52,58,61,66,68,69,71,75,114,121,124,126,128,129,130,136])),
        'topics':['退款残留/二次退款','换人交互与替补逃跑','持久能力/物品/写生','设施报名/裁判/恢复','回放残余输入','NPC业主资源和AI资格异常']},
       {'domain':'generic-kernel','mode':'统计/随机/诊断/本地化/启动/迁移的报告具名段与显式依赖定向读取',
        'feature_refs':list(map(fid,[392,395,396,398,401,407,413,415,416,420,423,425,426,427,428,430,435,436,439,445,448,449,450,451]))},
       {'domain':'engine-overworld','mode':'实际问题段/显式依赖读取，地牢/天气/场地/钓鱼和转移消费者重点',
        'feature_refs':list(map(fid,[326,345,346,348,349,358,372,373,374,381,384]))},
       {'domain':'user-interface','mode':'特殊活动完整相关章节、储存/图鉴/队伍/电话实际表格及生命周期问题段定向读取',
        'feature_refs':list(map(fid,[634,656,659,664,666,667,673,674,677,678,679,680,681,682,684,687,688,690,691,695,696,697,699,701,702,705,706,709,710,711,714,715,716,717,718,720,721]))},
       {'domain':'demo-dx','mode':'完整域报告/逐功能裁定；WP72问题入口/依赖、WP73归属及WP74/75/76/77全部显式依赖；WP77配置/一致性/缺口来源表定向读取',
        'feature_refs':list(map(fid,[257,261,266]+list(range(277,323)))),
        'limit':'不是97份派生机器证据或所有Demo正文的逐字独立复审；全输入消费类型见父任务ledger。'}],
    'selected_directly_inspected_source_ranges':[
       {'document':docs['wp51-ai-action-selection-and-skill']['source']['path'],'line_ranges':[[106,131]],'purpose':'业主资源、AI上下文、资格异常与登记'},
       {'document':docs['wp59-world-time-weather-field-moves']['source']['path'],'line_ranges':[[102,181],[189,282]],'purpose':'天气身份/概率/显示和十二族场地能力实际入口'},
       {'document':docs['wp60-fishing']['source']['path'],'line_ranges':[[24,108]],'purpose':'咬钩随机、真实输入窗口/取消及战斗消费'},
       {'document':docs['wp63-pokegear-map-music-and-phone']['source']['path'],'line_ranges':[[61,138]],'purpose':'实时联系人拖动与持久/呼叫入口区别'},
       {'document':docs['wp66-a-party-and-summary-ui']['source']['path'],'line_ranges':[[74,114]],'purpose':'奶招、物品/邮件先后与嵌套移位'},
       {'document':docs['wp66-b-storage-and-pokedex-ui']['source']['path'],'line_ranges':[[64,134],[153,258]],'purpose':'集合提交、取消、四层搜索和查看即写'},
       {'document':docs['wp07-diagnostics-files-http']['source']['path'],'line_ranges':[[117,154]],'purpose':'日志/控制流与宿主呈现分界'}],
    'correction_locators':list(source_units.values()),
    'executions':{'Ruby':0,'reference_game':0,'host_game':0,'business_vectors':0,'Showdown_prototypes':0,'framework_implementation':0},
    'target_compatibility_verified':0,'author_semantic_acceptance_claimed':False})

accepted=read(HERE/'accepted-source-updates.json').get('events',[])
regression_count=len(read(OUT/'tools/actual-results.json')['cases'])
upstream_sentence=(f'已登记{len(accepted)}个正式ACCEPTED接受事件，当前适用快照为`{m["current_snapshot"]["commit"]}`、正式树`{m["current_snapshot"]["formal_tree"]}`；17个相关活跃行已核对，实际文本变化仅FR-000403/588，191个已知批次绑定中其余174个待核对。固定历史source/retired原行不改。该接受不等于目标去向验证或上游全部关闭。'
    if accepted else '上游正式ACCEPTED回填由父任务唯一执行；本报告生成时事件表为空，current_snapshot仍为旧交付。不得由实际PASS或传入消息自行改成已校准。')
summary=['# R1作者返修交接','',
 f'固定旧候选 `{BASE}` 的独立复审 `{REVIEW}` 给出44组问题，原721行中448 PASS、227 FAIL、46待查。作者已逐组/逐旧行形成可复审修订，未自行宣布独立通过。','',
 f'当前索引观察为{len(m["documents"])}份正式文档，{len(m["features"])}个活跃功能、{len(m["retired_features"])}个完整退役旧行和{len(m["metadata_records"])}个元数据记录。新增47行，其中9个补漏、38个边界子行。历史ID全部保留；原source对象不变，当前有效区间由functional_scope表达。','',
 '- [44组逐问题映射](finding-resolution.json)、[全部721旧行处置](feature-resolution.json)、[合理PASS根因传播](retained-pass-propagation.json)。',
 '- [新增/退役单元](new-and-retired-units.json)、[来源定向阅读口径](source-reading-scope.json)、[依赖校准](dependency-calibration.json)、[元数据依赖导航](metadata-dependencies.json)。',
 f'- [97份固定复审输入台账](tools/review-input-ledger.json)、[工具实际I/O](tools/actual-command-io.json)、[{regression_count}项拒绝结果](tools/actual-results.json)、[ROOT两组工具映射](tools/root-tool-resolution.json)、[正式接受回填](tools/accepted-backfill-result.json)。','',
 '32个责任/来源/向量/冻结依赖章节归元数据；持久PP/物品/成长/逃跑/调试和AI策略查询按真实状态分责；缺失行为补回；特殊玩法的规则权威归框架、输入/表现归MZ。来源事实仍与未来计划分栏，所有去向待验证、阶段待定、实现/验收未完成。','',
 upstream_sentence+'Showdown四类原型未运行，用户首版/后续/特殊玩法和XP旧格式范围未全面批准。','',
 '下一步由父任务以新的40位候选SHA创建真正非作者gpt-6.1-sol ultra/default复审。语义分类、依赖必要性、元数据消费者和mixed边界仍由该独立任务裁定；结构检查不是此裁定。','']
(OUT/'README.md').write_text('\n'.join(summary))
print(json.dumps({'finding_groups':len(out),'prior_rows':len(rows),'unhandled_nonpass':res['unhandled_prior_nonpass'],
                  'active':len(active),'retired':len(retired),'new':len(units['new_rows'])},ensure_ascii=False))
