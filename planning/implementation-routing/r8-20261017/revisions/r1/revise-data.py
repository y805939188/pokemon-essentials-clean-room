#!/usr/bin/env python3
"""Apply explicit source-unit author decisions to d62; never reseed existing IDs."""
import collections
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
from functools import lru_cache

HERE = Path(__file__).resolve().parents[2]
ROOT = HERE.parents[2]
BASE = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
REVIEW = 'a0352c7fba38391afc535525988245701d5ce202'
PREFIX = 'planning/implementation-routing/r8-20261017/'
FIXED = 'fd1df570cad987dc3852a3b958f03916e317f7fe'

# This script documents the explicit pre-backfill author migration. It must not
# overwrite the accepted current snapshot when inspected from a later candidate.
if json.loads((HERE/'accepted-source-updates.json').read_text()).get('events'):
    raise SystemExit('HISTORICAL_R1_MIGRATION_REFUSED_AFTER_ACCEPTED_BACKFILL; preserve current applicability and immutable history')

def show(path, commit=BASE):
    return subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)

def sha(data): return hashlib.sha256(data).hexdigest()
def write(path, obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

manifest = json.loads(show(PREFIX+'routing-manifest.json'))
coverage = json.loads(show(PREFIX+'section-coverage.json'))
policy = json.loads(show(PREFIX+'routing-policy.json'))
original = {f['feature_id']: copy.deepcopy(f) for f in manifest['features']}
active = {f['feature_id']: f for f in manifest['features']}
documents = {d['document_id']: d for d in manifest['documents']}
by_stem = {Path(d['source']['path']).stem: d for d in manifest['documents']}
review_root = Path('/tmp/r8-disposition-review-a0352c7')
reviews = {f['feature_id']: f for f in json.loads((review_root/'feature-results.json').read_text())['features']}
findings = json.loads((review_root/'findings.json').read_text())['findings']
changes, new_rows, retirements, section_changes = {}, [], [], []
source_reading = []
next_id = 722
manifest['schema_version'] = 'implementation-routing.v2'
manifest['retired_features'] = []
manifest['metadata_records'] = []

# Accepted old coarse judgments are retained; new fields make their current extent explicit.
for f in active.values():
    title=f['source']['heading']
    f['functional_scope']={'line_ranges':copy.deepcopy(f['source']['line_ranges']), 'excluded_child_refs':[],
        'reason':'本节原有独立行为/数据合同；当前有效范围与首次固定来源一致。'}
    f['dependencies']['direct_refs']=[]
    f['future_plan']['responsibilities']=[]
    for party in f['future_plan']['partners']:
        if party=='框架':
            scope=(f'维护“{title}”的持久输入、领域状态或作者数据；战斗/宿主消费者按直接引用交接。'
                   if f['future_plan']['destination']!='Showdown承担' else f'提供“{title}”明确需要的持久个体/配置输入，接收其规则结果；持久写入遵循被引用的领域合同。')
        elif party=='Showdown':scope=f'作为“{title}”所列战斗查询、临时状态及阶段执行的候选，固定版本/格式后逐项比对。'
        else:scope=f'承担“{title}”的输入采样、场景/资源和可观察呈现，领域提交由框架主合同提供。'
        f['future_plan']['responsibilities'].append({'party':party,'scope':scope})
for d in documents.values():d['retired_feature_ids']=[]
for c in coverage['sections']:
    c['metadata_refs']=[]
    c['retired_feature_refs']=[]

def fid(n): return n if isinstance(n,str) else f'FR-{n:06}'
def edit(n, destination=None, responsibilities=None, reason=None, questions=None, protos=(), scope=None, deps=(), refs=()):
    key=fid(n);f=active[key];p=f['future_plan']
    if destination:p['destination']=destination
    if responsibilities:
        p['responsibilities']=[{'party':k,'scope':v} for k,v in responsibilities]
        p['partners']=[k for k,v in responsibilities]
    if reason:p['rationale']=reason
    if questions is not None:p['questions']=questions
    p['prototype_refs']=sorted(set(p['prototype_refs']).union(protos))
    if scope:
        f['current_applicability']['target_scope']=scope
        if scope=='待决策' and 'DEC-SPECIAL-AND-HOST-SCOPE' not in f['decision_refs']:
            f['decision_refs'].append('DEC-SPECIAL-AND-HOST-SCOPE')
    if ('Showdown' in p['partners'] or protos) and 'DEC-SHOWDOWN-VERSION-FORMAT' not in f['decision_refs']:
        f['decision_refs'].append('DEC-SHOWDOWN-VERSION-FORMAT')
    f['dependencies']['wp_refs']=sorted(set(f['dependencies']['wp_refs']).union(deps))
    f['dependencies']['feature_refs']=sorted(set(f['dependencies']['feature_refs']).union(map(fid,refs)))
    changes.setdefault(key,[]).append({'action':'explicit-source-unit-revision','reason':reason or '补充正文直接消费者与验收前提','review_finding_refs':reviews.get(key,{}).get('finding_refs',[])})
    return f

@lru_cache(maxsize=None)
def locate(stem, section=None):
    d=by_stem[stem];path=d['source']['path']
    # Read only the shared, already provided heading parser; no source/reference execution.
    spec=importlib.util.spec_from_file_location('routing_data_parser',HERE/'routing.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    data=show(path,FIXED);hs,lines=module.headings(data)
    if section is None:h=hs[0]
    else:
        matches=[h for h in hs if h.get('section')==str(section)]
        if len(matches)!=1:raise ValueError((stem,section,'not unique'))
        h=matches[0]
    return d,h,lines,hs

def dep(n, stem, section, reason):
    f=active[fid(n)];d,h,lines,hs=locate(stem,section)
    item={'document':d['source']['path'],'anchor':h['anchor'],'reason':reason}
    if item not in f['dependencies']['direct_refs']:f['dependencies']['direct_refs'].append(item)
    f['dependencies']['wp_refs']=sorted(set(f['dependencies']['wp_refs']).union(d['wp_refs']))
    # Point only to active implementation units that own this exact source location.
    targets=[x['feature_id'] for x in active.values() if x['document_id']==d['document_id'] and
             any(a<=h['line_start']<=b for a,b in x['functional_scope']['line_ranges']) and x['feature_id']!=f['feature_id']]
    f['dependencies']['feature_refs']=sorted(set(f['dependencies']['feature_refs']).union(targets))
    changes.setdefault(f['feature_id'],[]).append({'action':'direct-dependency','reference':item})

def subtract(ranges, cuts):
    result=[]
    for start,end in ranges:
        cursor=start
        for a,b in sorted(cuts):
            if b<cursor or a>end:continue
            if cursor<a:result.append([cursor,a-1])
            cursor=max(cursor,b+1)
        if cursor<=end:result.append([cursor,end])
    return result

def add(stem, section, name, destination, responsibilities, reason, questions,
        parent=None, ranges=None, protos=(), scope=None, deps=(), refs=()):
    global next_id
    d,h,lines,hs=locate(stem,section)
    selected=ranges or [[h['line_start'],h['line_end']]]
    template=copy.deepcopy(active[fid(parent)] if parent else next((f for f in active.values() if f['document_id']==d['document_id']),original[d['feature_ids'][0]]))
    key=fid(next_id);next_id+=1
    template['feature_id']=key;template['name']=name;template['document_id']=d['document_id']
    s={'commit':FIXED,'document':d['source']['path'],'heading':h['title'],'anchor':h['anchor'],
        'heading_level':h['level'],'heading_sha256':h['heading_sha256'],'line_ranges':selected,
        'unit_sha256':sha(''.join(''.join(lines[a-1:b]) for a,b in selected).encode()),
        'file_sha256':d['source']['sha256'],'file_git_blob':d['source']['git_blob'],
        'fact_excerpt':next((l.strip()[:105] for a,b in selected for l in lines[a-1:b] if l.strip() and not l.startswith(('#','|','---'))),'有序数据表提供本单元的输入、权重、形状或规则；详固定来源。'),
        'evidence_type':'SOURCE_SPECIFICATION_ONLY'}
    template['source']=s
    template['current_applicability']=copy.deepcopy(original[next(iter(original))]['current_applicability'])
    template['current_applicability'].update(document=d['source']['path'],source_classification=d['source_classification'],
        status='待整改后核对' if d['upstream']['batches'] else '固定基线粗标',target_scope=scope or '待确认')
    template['functional_scope']={'line_ranges':copy.deepcopy(selected),'excluded_child_refs':[],'reason':reason}
    template['dependencies']={'wp_refs':[],'document_wp_refs':d['wp_refs'],'feature_refs':[],'direct_refs':[]}
    template['upstream']=copy.deepcopy(d['upstream'])
    template['future_plan'].update(prototype_refs=[],exclusion_decision=None,stage='待定',stage_approval='未批准')
    template['decision_refs']=['DEC-ROUTING-VERIFY','DEC-PHASE-SCOPE']
    active[key]=template
    edit(key,destination,responsibilities,reason,questions,protos,scope,deps,refs)
    if parent:
        pf=active[fid(parent)]
        pf['functional_scope']['excluded_child_refs'].append(key)
        pf['functional_scope']['line_ranges']=subtract(pf['functional_scope']['line_ranges'],selected)
        pf['functional_scope']['reason']='保留原固定来源定位；当前行为职责排除下列独立去向/验收子单元。'
        changes.setdefault(fid(parent),[]).append({'action':'extract-child-current-scope','new_feature_id':key,'ranges':selected})
    new_rows.append({'feature_id':key,'parent_feature_id':fid(parent) if parent else None,'source_document':s['document'],'source_ranges':selected,'reason':reason})
    return key

def retire(n, replacements, reason, groups):
    key=fid(n);old=copy.deepcopy(original[key]);mid=f'META-{len(manifest["metadata_records"])+1:06}'
    old['retirement']={'reason':reason,'review_finding_refs':groups,'metadata_record_id':mid,
        'replacement_feature_refs':[fid(x) for x in replacements]}
    manifest['retired_features'].append(old)
    manifest['metadata_records'].append({'metadata_id':mid,'document_id':old['document_id'],'source':copy.deepcopy(old['source']),
        'kind':'来源责任、证据或静态验收元数据','reason':reason,'feature_refs':[fid(x) for x in replacements],'retired_feature_ids':[key]})
    del active[key]
    retirements.append({'feature_id':key,'metadata_id':mid,'replacement_feature_refs':[fid(x) for x in replacements],'reason':reason,'review_finding_refs':groups})

D={}
for stem in by_stem:
    # Aliases only select an explicit document name; no classification is inferred from filenames.
    D[stem]=stem
def stem(prefix):
    if prefix in by_stem:return prefix
    matches=[s for s in by_stem if s.startswith(prefix+'-')]
    if len(matches)!=1:raise ValueError((prefix,matches))
    return matches[0]
F='框架实现';C='框架与Showdown协作';M='MZ接入与表现重建';S='Showdown承担'
def plan(n,route,why,fw=None,sd=None,mz=None,questions=None,protos=(),scope=None,refs=()):
    parties=[(k,v) for k,v in [('框架',fw),('Showdown',sd),('MZ',mz)] if v]
    return edit(n,route,parties,why,questions or ['验证上述各方在正常、取消和异常前缀下的具体职责及提交顺序。'],protos,scope,refs=refs)
def child(n,sec,name,route,why,fw=None,sd=None,mz=None,ranges=None,protos=(),scope=None,refs=()):
    parties=[(k,v) for k,v in [('框架',fw),('Showdown',sd),('MZ',mz)] if v]
    return add(Path(active[fid(n)]['source']['document']).stem,sec,name,route,parties,why,
        ['分别验证该独立单元的生产/消费、已提交状态、取消及异常后继；来源规则不构成目标兼容证据。'],
        parent=n,ranges=ranges,protos=protos,scope=scope,refs=refs)

# Missing behavior is restored from the exact source units, including behavior inside concept/purpose headings.
bag_defaults=add(stem('wp27'),'2.1','物品定义的缺省、显式值和有效消费属性',F,
    [('框架','拥有物品定义、缺省/显式false和有效消费属性的读取规则。')],
    '本节是可验收的数据输入合同，独立于背包容器及数量绘制。',
    ['验证省略、显式false和重要道具条件的有效值；显示层仅消费结果。'])
bag_quantity=add(stem('wp27'),'2.2','背包逐槽数量显示和图标遮挡',M,
    [('框架','提供ShowQuantity/Consumable的三态及逐槽数量。'),('MZ','按实际显示门绘制数量，处理图标遮挡和逐槽显示。')],
    '数量显示有独立表现验收边界，不能由容器功能或概念元数据替代。',
    ['验证三态、重要道具与图标遮数量的组合；不把总量查询当逐槽显示。'],refs=[bag_defaults,177])
unknown_effect=add(stem('wp43'),'2.1','未知效果身份、变化失败与伤害回退',S,
    [('框架','保留作者效果身份和实际绑定输入。'),('Showdown','调查变化效果失败、伤害回退及PP前缀的可观察行为。')],
    '未知效果的回退/失败是战斗执行合同；SHADOWSHED绑定与普通回退分列。',
    ['验证未知变化/伤害身份、外壳PP不退及真实SHADOWSHED绑定，不能靠同名数据推断。'])
lottery_match=add(stem('wp70-lottery'),'3','彩票低16位公开号与最低五位匹配',F,
    [('框架','执行输入整数转换、公开号低16位提取、最低五位最长连续匹配及并列结果规则。')],
    '匹配数学和输入域是独立领域行为，需供后续队伍/盒子检索消费。',
    ['验证负数/字符串转换、位宽和逐位匹配，保留来源异常；外部发奖不由本单元推断。'],refs=[615,616,617])
transition_wrapper=add(stem('wp16-pre-battle'),'1','战前包装的预置清理、音乐记忆与世界恢复',M,
    [('框架','提供战斗标记、四类预置及音乐备忘状态，按真实前缀清理。'),('MZ','包裹战前演出与战后地图/音频恢复，异常不保证恢复。')],
    '目的章实际定义包装行为，和特殊过渡注册表是不同验收单元。',
    ['验证设置战斗标记、保存音乐、四预置清理及正常返回恢复的先后，区分准入跳过与异常。'],refs=[5,32,355,358])
duel_entry=add(stem('wp68-duel'),'2','Duel临时生命、准入与结果合同',F,
    [('框架','拥有10/10临时生命、胜负/无平局和准入规则。'),('MZ','提供不可取消的动作选择入口与地图角色呈现。')],
    '本活动独立于常规宝可梦战斗，概念章中的生命/结果限制是实际会话合同。',
    ['验证无取消、无平局和玩家生命归零的终局优先级。'],scope='待决策',refs=[695,697,698])
slot_entry=add(stem('wp69-slot-machine'),'1','老虎机资源准入与难度输入',F,
    [('框架','检查币盒、余额/上限三个拒绝门并持有难度输入。'),('MZ','显示对应拒绝反馈并只在准入通过后建立场景。')],
    '准入与难度是会话规则，不能作为概念元数据省略。',
    ['验证三个拒绝入口与难度变化；拒绝不建立可下注场景。'],scope='待决策',refs=[699,700,701,702])
mine_entry=add(stem('wp70-mining'),'1','挖矿公开入口与会话建立',M,
    [('框架','提供玩法会话和库存接收，保留公开入口没有额外准入门的事实。'),('MZ','建立挖矿场景并处理进入/离开；不添加未有授权的币盒等准入限制。')],
    '目的章中的公开入口和无准入门是可验收行为。',
    ['验证直接入口、正常离开与异常前缀；是否纳入玩法由用户决定。'],scope='待决策',refs=[708,709,711])
mine_candidates=add(stem('wp70-mining-data'),None,'挖矿61项有序候选、权重与占格数据',F,
    [('框架','拥有61候选的有序条目、身份、权重、矩形/占格及去重语义。')],
    '主物品表是初始化抽样的权威行为数据；与铁障碍表和来源资格分开。',
    ['验证有序重复候选、权重累计与占格空洞；不能用48个身份替代61条候选。'],
    ranges=[[9,75]],scope='待决策',refs=[706,708,709])

# Independent battle/presentation/persistent boundaries; original source objects remain immutable.
refund_child=child(10,'4.2.1','退款残留消费身份与后续终局/命令清理',C,
    '该同级子标题仍属于背包退款整链，单独覆盖残留身份、二次退款与两种直接清理。',
    fw='拥有实时背包及退款容量，按实际已到达前缀提交库存。',
    sd='拥有已登记选择的物品身份，区分效果正常返回清身份、执行退款不清、终局撤销与下轮/失能直接清。',
    protos=['PROTO-BATTLE-ITEM'],refs=[11,31,177,186,187])
target_child=child(10,'4.3','登记期选靶光标、确认与资格消费',M,
    '目标光标/按钮/确认登记具有独立交互验收；资格判定仍由战斗规则提供。',
    fw='提供席位/拥有者身份映射和目标数据。',sd='提供目标许可与最终执行解析，保持NearAlly初选异常及执行拒绝。',
    mz='负责候选文字、高亮、按钮态、USE登记与取消回菜单；不自行修正引擎资格。',refs=[3,51,678])
audio_child=child(5,'7.5','战斗选曲请求与过渡/胜利/捕获音频交付',M,
    '逻辑选曲、音乐备忘与宿主播放消费是独立于战斗规则的表现接点。',
    fw='按玩家/训练家类型、地图和下一战预置形成逻辑音频请求及引子备忘。',
    mz='按入口交给战前过渡、胜利呈现或捕获ME，保留播放失败前已提交备忘与正常清理。',refs=[155,355,transition_wrapper,683])
switch_ui=child(18,'3.4','换人选择的许可、取消、摘要与登记交互',M,
    '界面许可、检查强度与是否登记正交，需独立于换入/换出查询验收。',
    fw='提供显示队伍与所有者/队伍下标映射。',sd='执行换入或组合资格以及二次登记检查。',
    mz='维护按钮、canCancel、摘要和返回命令小循环；不得把不登记推成宽松检查。',refs=[680,655])
sketch_child=child(52,'6.3','模仿临时槽与写生持久槽的有序提交',C,
    '复制槽位同时涉及战斗临时招式与持久学习，写生先持久后场上，失败不回滚。',
    fw='拥有持久招式列表、初始PP和写生后的个体/形态数据。',
    sd='执行模仿/写生前门与场上首槽替换，区分模仿不写持久、写生两次提交和后置形态异常。',
    protos=['PROTO-IN-BATTLE-GROWTH'],refs=[147,207])
entry_ui=child(114,'2.3','设施报名多选界面与已选成员接收',M,
    '成员资格/数量规则与实际多选焦点、取消、摘要和提交具有不同验收边界。',
    fw='提供规则数量、成员/组合资格及确认后的报名列表。',mz='处理选择顺序、按钮焦点、摘要、取消及确认后列表交付。',refs=[115,654,655])
arena_ui=child(129,'3.2','Arena逐项裁判画面与总结反馈',M,
    '心技体评分的计算/HP提交和裁判画面可独立验收。',
    fw='提供两侧心/技/体比较值、总分及胜负结果。',mz='按心→技→体顺序显示名字、VS、判定图标及总结文本。',
    ranges=[[102,104]],scope='待决策',refs=[684])
replay_ui=child(136,'6.4','回放消息、残余选靶与中止交互',M,
    '回放并非一律无交互；呈现/中止消费不同于记录恢复和正常终局。',
    fw='在中止结果0与正常终局之间分流，保留实时背包/图鉴的已提交前缀。',
    sd='按记录驱动命令并消费必要选靶，区分异常中止不执行正常终局。',
    mz='自动消息等待、必要目标选择、取消中止及场景结束。',refs=[135,677,678,683])
pp_child=child(147,'5.5','持久招式与战斗PP/学招同步',C,
    '持久列表、独立战斗PP、标识关联和变身例外形成明确双向状态边界。',
    fw='拥有持久招式列表、PP和新学习槽；只接受关联存在、标识相同且非变身的专门同步写入。',
    sd='拥有临时招式/PP，直接字段不自动写穿；升级后回读对应新槽，模仿/变身不保留。',
    protos=['PROTO-IN-BATTLE-GROWTH','PROTO-BATTLE-ITEM'],refs=[29,191,204,207])
held_child=child(148,'6.4','持有物写穿、可变还原记录与捕获成员身份',C,
    '持久当前物、按队伍索引的还原记录与伙伴捕获换位必须共同验证。',
    fw='拥有个体当前持物、队伍/盒子身份及接收后的集合移动。',
    sd='维护可更新还原记录及永久/暂时移除，正常终局按真实参与集合/索引写回。',
    protos=['PROTO-CAPTURE'],refs=[31,61,528,529,577])
money_child=child(153,'4.4','战斗奖金与败北损失的持久钱包提交',C,
    '内部战斗/金钱开关、两阶段奖金与扣款的实际增量/统计/提示跨战斗和钱包。',
    fw='拥有钱包夹限、实际变化统计及玩家/伙伴队伍边界。',sd='产生金钱资格、奖金/聚宝功标记和败北结算输入，并按终局顺序请求两阶段提交。',
    mz='显示实际变化大于0才产生的提示，保持消息失败前已提交状态。',refs=[31,579,421])
trainer_tool=child(154,'5.3','缺失训练家内容的调试新增交互',M,
    '正常装载失败与交互式新建训练家是不同目标范围。',fw='校验并提交训练家/队伍内容及落盘前缀。',
    mz='提供确认、字段/成员录入和取消；不把取消认成此前内容回滚。',scope='待决策',refs=[263,265])
evolution_domain=child(492,'5','进化成功后的领域提交、额外个体与图鉴/学招',F,
    '动画取消与成功领域提交分开：统计、耗物、物种/HP和额外个体均由框架拥有。',
    fw='按来源次序提交进化统计、物种/HP、消耗持物、Shedinja克隆入队/扣球、图鉴和学招；保留每步失败前缀。',
    mz='消费框架提交结果，提供图鉴条件页/消息和学习交互；不得自行重算或回滚领域写入。',
    ranges=[[165,192]],refs=[490,491,493,164,177,206,605,687])
hall_record=child(691,'7.1','名人堂历史克隆、编号和容量裁剪',F,
    '记录先于逐成员视觉演出，且没有另一本领域主规格可代替其持久职责。',
    fw='克隆队伍并追加历史、递增编号、按上限裁剪；上限0与PC可见/后续读取失败分别保留。',
    mz='在记录提交后逐成员演出；登记前BGM请求和失败前缀按实际顺序消费。',refs=[444,650])
record_rng=child(427,'5.3','录像随机序列与回放消费边界',C,
    '普通随机、显式种子和录像序列不可合并为同一种随机服务。',
    fw='保存初始条件、命令、随机数和换人序列及其版本。',sd='按真实调用域逐次消费已录序列，回放不重新随机；未录调用和顺序差异待验证。',
    refs=[132,133,134,135,136])

# Remaining explicit cross-state and persistent-write contracts.
plan(4,C,'参战者既有临时副本也有逐字段持久写回；建立、刷新与逐出必须共享个体身份。',
    fw='拥有真实个体的等级、形态、HP、异常/计数、持物及关联招式。',sd='建立席位临时能力/效果，按入口写穿特定字段并从个体回读；直接字段与专门入口严格区分。',
    questions=['验证直接持物id与持物入口、变身临时能力、PP关联及濒死/捕获清理的不同提交；保持真实成员/席位映射。'],refs=[145,146,pp_child,held_child,29,31])
for n,why,details in [
 (61,'物品操作写穿持久当前物并维护C/I/R/P/Belch，需独立于纯物品资格计算共同验收。','逐项区分临时/永久移除、取得/交换、野生记录更新、投掷后当前物重读及异常前缀'),
 (66,'离场、真正濒死和正常终局具有不同持久异常/HP/友好/图鉴提交。','自然回复/再生力结束标志、真正濒死的持久清理和形态离场，不将局部HP置0写穿'),
 (68,'每击能力顺序会引发即时物权转移和再次触发。','MAGICIAN/PICKPOCKET的当前物与还原记录、即刻自耗/递归及同击后续检查点'),
 (69,'回合末取物/回收/捡拾会更新持久物权及消费，属于战斗时序和个体状态交界。','BALLFETCH/HARVEST/PICKUP的资格、物品来源、还原记录和再次消费'),
 (71,'通用形态和共生接点写入个体/图鉴或转移当前物，不能只归临时战斗规则。','形态提交的缺HP保护、图鉴与场上回读，以及SYMBIOSIS不更新两份还原记录的差异')]:
    plan(n,C,why,fw='拥有个体当前持物、HP/异常/形态/友好/图鉴等持久记录，按实际成员身份接收明确写入。',
         sd='执行本章具名战斗资格/触发顺序及临时效果；'+details+'。',
         questions=['逐项验证'+details+'；保留先写后故障和无统一回滚的前缀。'],refs=[4,pp_child,held_child,31])
plan(20,C,'替补循环中的拒绝下一只会触发替补逃跑，成功写3后仍可能继续同次扫描。',
    fw='提供玩家/伙伴与真实后备成员，并消费最终原始结果及世界返回。',sd='执行逐席替补、替补专用逃跑资格、决定3后扫描/入场危害及外层检查点。',
    mz='提供下一只确认与替补选择，保留决定已写后仍出现的提示。',
    questions=['验证替补入口跳过的守卫、同次扫描后继、非致死换入及结果3的世界消费；不套普通逃跑统一资格。'],protos=['PROTO-ESCAPE'],refs=[22,31,32,switch_ui])
plan(58,C,'招式逃离、强制替补与不可取消选择是同一行动中的跨系统接点。',
    fw='拥有后备队伍与世界终局消费。',sd='执行招式专用可逃查询、决定3、接力保留与宽松/随机替补门。',
    mz='按入口处理玩家不可取消的中途替补等待和候选选择。',protos=['PROTO-ESCAPE'],refs=[20,22,23,31,switch_ui])
plan(121,F,'固定资格限制集合由赛前框架资格筛选消费，不是战斗执行状态。',fw='拥有固定资格名单和参数，供报名及成员/整队约束查询。',refs=[114,115,entry_ui])
plan(124,F,'设施会话、原队伍引用、暂停/继续和保存属于框架编排；单场战斗交给既有协作边界。',
    fw='拥有挑战ID、轮次/名单、报名/原队伍别名、暂停继续位置快照及保存返回/异常前缀。',
    mz='消费对手信息与传回起点请求；保存临时地图位置的正常恢复按会话顺序执行。',
    questions=['验证开始保存false仍进行中、暂停/继续临时位置正常恢复和传播异常跳过恢复；单场调整还原沿FR-000125。'],refs=[125,444,446,449,451,162,324])
plan(126,F,'会话/生成/保存的失败由框架保留前缀，单场战斗异常引用明确的协作主行。',
    fw='区分轮次已置位、名单不终止、零候选、保存false与传播异常及原队伍重置。',
    sd='在单场包装已调用后保留对局/经验还原失败的具体出口；不承担会话保存。',
    mz='提供已到达的反馈与地图刷新，不保证所有异常恢复。',refs=[124,125,116,446,451])
plan(128,C,'Palace以专用性格概率/压半和AI换人取代普通选招策略，需要规则调度接入。',
    fw='提供性格表、专用策略与AI平直随机域，保留2A+D实际门及零候选。',sd='接收自动登记，维护压半的在场生命周期、普通执行复检和换人；不调用普通逐招评分。',
    questions=['验证玩家/AI两入口前门、Mega早返、无力-2、压半换入清零与记录调用域，不能用普通AI或同一随机种子代替。'],scope='待决策',refs=[73,74,9,13,134,135])
plan(129,C,'Arena消费普通成功状态机并直接提交败者持久HP，评分/顺序补位与画面分开。',
    fw='保存两侧心技累计、首发HP基线和计数，接收直接HP0/濒死及终局结果。',sd='生产成功状态/本回合技槽，按至少3回合持续评判、取消持续招并顺序补位，正常补位不复位。',
    questions=['验证保护与状态2的技值、后续行动消费待结算状态、第3→4→5轮连续评判、直接HP写穿及回复期保留。'],scope='待决策',refs=[arena_ui,4,20,30,31])
plan(130,C,'差异矩阵是Palace/Arena与普通路径共同的行为配置/验收合同，具体承载沿两模式主行。',
    fw='提供专用策略和模式配置，保持矩阵中资格、概率、记录域差异。',sd='按模式接入自动选择、成功机、回合末与HP/顺序补位；不把差异仅当显示文案。',scope='待决策',refs=[128,129,134,135])

# Creature domain/UI contracts share a coarse row only where the concrete ownership is stated.
creature_ui={
152:('玩家标识/外观与命名输入分层。','拥有玩家类型/外观标识、宿主用户名建议和最终姓名。','刷新人物外观，采样初始命名/取消及显示建议；不改变字段验证。'),
166:('入口×目标×是否持有的领域/界面守卫须分别消费。','提供可存取/释放/交换等领域守卫。','按模式、持有对象及当前目标决定按钮/提示，调用领域入口而不替代守卫。'),
171:('获得工具的静默入队和带命名/消息等待入口分开。','拥有容量、来源/图鉴/入队或送盒提交；等待后按真实时点复检容量。','提供昵称输入、确认和消息中的地图更新，保留等待前已写状态。'),
172:('交换的演出/图鉴/进化发生在最终队伍替换之前。','拥有送出/收到个体及最终替换，消费选择器返回和事件变量。','提供选择、取消、交换演出、图鉴与进化交互；失败不宣称此前统计或演出提交回滚。'),
178:('物品/PC的领域资源转移与动态菜单、数量和事件变量是两端职责。','拥有背包/物品储存、部分添加删除和最终事件变量输出。','提供数量输入、选择过滤、给予/丢弃/存取提示与刷新，按实际提示前后提交点验收。'),
179:('快捷登记列表与地图两列菜单的控制状态不同。','保存登记列表及快捷物品使用结果/资源变化。','在地图按键打开两列菜单、确认执行及失败返回菜单，保留临时退出菜单状态。'),
183:('场外背包和队伍使用仍有数量、目标、教学确认及取消。','拥有物品资格、上限、处理器返回与成功后扣量/统计。','采样物品/个体/数量与教学确认，取消不提交尚未到达的效果，消息失败保留此前前缀。'),
196:('金钱买卖的窗口流程和交易提交由不同方验收。','拥有价格覆盖、容量、物品→统计→钱包的交易提交及免费购买夹限。','显示库存、数量/确认、反馈及连续操作，列表取消不提交交易。'),
197:('BP显示半价与实际扣减不同，须保留该显示/资源交界。','拥有BP余额、物品和消费统计，按真实价格执行扣减。','提供欢迎/告别、数量窗口与半价显示，明确展示值不代替到账/扣款。'),
205:('等级/经验设置中消息先于写入，后续还有能力窗与进化。','钳制并提交等级/经验、逐级能力与友好变化。','显示先行消息、刷新场景和能力差异窗，消费进化交互；消息异常保留实际到达前缀。'),
206:('场外学习/遗忘/重学具有领域候选与独立确认/放弃循环。','生成记录/等级候选并保持顺序/去重，拥有持久招式与统计写入。','提供满槽替换、放弃/重试、遗忘/重学选择和空列表失败入口；取消只影响对应阶段。'),
213:('寄养槽位选择与事件变量/作者输入映射需要宿主消费。','拥有寄养槽引用、费用报价及返回索引/事件变量提交。','提供两槽菜单、取消与选中反馈，正确区分取消哨兵与直接负索引。'),
239:('邮件模型与250字输入/停止给予的交互职责分开。','拥有邮件对象、附件快照及真实持物耦合。','采样写信文本/停止给予确认，处理显示和取消；不将文本界面取消当先前物权回滚。'),
240:('邮件阅读、PC命令与给予链包含可观察的有序部分提交。','拥有信箱列表、持物和邮件引用，执行先赋值再getter自清/失败的实际顺序。','展示邮件/PC命令并采样取下、给予和取消，保留已到达的引用变化。'),
242:('礼物下载/过滤与掉落动画后才推入队列是不同职责。','执行HTTP/解码、候选筛选、同ID及队列推入。','播放接收掉落动画和反馈，正常返回后才交付队列提交；不把下载成功当领取成功。'),
235:('租借选择/确认/取消第三只与会话队伍提交具有明确交接点。','拥有候选池、三只选择结果及租借队伍提交。','提供选满、摘要/确认与取消第三只返回的交互，不自行改候选生成。'),
236:('两屏交换的取消/重选和无条件队伍提交须分别验收。','拥有原队伍/租借成员及实际交换/最终写入。','维护两屏选择、取消与重选导航，在真实提交点交付选择。'),
249:('Triad手选/预览与随机牌组建立分责。','拥有规则配置、卡仓及随机牌组构建。','采样USE/BACK、手选/预览与确认，取消不冒充已建立有效牌组。'),
250:('Triad局部按键仲裁/消息等待不同于翻转和对手评分。','拥有棋盘、翻转/评分、对手决策和回合提交。','执行repeat/trigger仲裁、翻牌呈现和局部1.5秒消息等待，保持结果消息的独立出口。')}
for n,(why,fw,mz) in creature_ui.items():
    plan(n,M if n==179 else F,why,fw=fw,mz=mz,scope='待决策' if n in [235,236,249,250] else None)
plan(154,F,'正常训练家内容装载保留框架主责，交互调试新增已另列范围门。',fw='解析类型/版本、装载成员并建立NPC，未知内容按实际装载错误处理。',refs=[trainer_tool])
plan(244,M,'礼物调试编辑/管理/导出是作者工具，范围由用户另行决定。',fw='拥有礼物载体、共享对象编辑与导出/队列提交的实际前缀。',mz='提供类型/个体/名称等编辑、取消及管理菜单，取消不保证共享对象未变。',scope='待决策',refs=[241,243,263,265])
plan(153,F,'资源/许可字段由框架拥有，煤灰图块擦除与战斗金钱结算分别交付具体消费者。',fw='拥有钱包/币/BP/煤灰资源、初始直接赋值例外及徽章/标记。',mz='在通用迈步通知后清首个煤灰图块，消费资源实际增量后反馈；不把NPC擦图当采集。',refs=[money_child,330,596])

# AI strategy and data are distinguished from rule queries and true command/resource registration.
ai_semantics={
73:('技能值、Flags和控制顺序','框架提供训练家技能/野生档与策略次序；战斗侧提供控制权、Mega许可及实际登记。'),
74:('换人意愿、否决和后备估量','框架执行有序意愿/否决和后备评分；战斗侧提供换入换出资格及真实登记，保留集合空槽异常。'),
75:('NPC主动道具决策','框架拥有业主items/ally_items和AI估量/选择；战斗侧执行真实资格扫描与登记消费，玩家接管仍使用实时背包。'),
76:('招式/目标候选和权重抽取','框架合成WP52评分、构造候选并抽权重；战斗侧提供合法槽/目标与真实登记，预估重定向不替代执行解析。'),
77:('治疗道具估量','框架持有AI的HP估量表；SITRUSBERRY估量1等策略值与真实治疗效果分开。'),
78:('治疗/复活类别','框架提供有序身份类别供AI选择；类别表不授予真实使用资格。'),
79:('X道具偏好请求量','框架保留AI请求量；真正反向/单纯/封顶由WP44与WP28实际效果消费。'),
80:('普通换人处理器有序目录','框架持有意愿/否决的有序策略目录，条件与概率沿WP51主稿，不按身份另建架构。'),
82:('评估注册有界集合和默认查询','框架拥有F/T/S/G/P族的默认查询及有效规则目录；审计计数/历史归属只作元数据。'),
83:('F/T/S/G/P效果评估数据','框架维护效果身份、参数和分族评估表，实际效果执行仍由战斗主合同承担。'),
84:('通用评分修正和能力评级注册','框架持有通用评分/能力评级的数据与最终绑定，评分不是持久状态提交。'),
85:('基础能力评级','框架维护267身份基础偏好及未知0的策略数据，保留字面拼写差异。'),
86:('评估登记的已有/前向责任','框架保留跨族真实参数的消费关系；其中来源归属和历史状态不另产生执行能力。'),
87:('重复登记的最终查询绑定','框架提供重复键后继绑定、copy缺源不覆盖及默认查询行为，不要求沿用源模块结构。'),
88:('失败预测、逐目标合成和通用修正','框架拥有失败预测/友方反转/合成分数；战斗侧提供具名规则查询，准备字段副作用须按实际前缀核验。'),
89:('粗类型、速度、伤害和命中','框架计算粗略预估和AI随机会心/附效估量；战斗侧提供有效特性/物品/类型查询，近似不等于真实逐击。'),
90:('能力阶级偏好','框架按收益与可用招门计算偏好；战斗侧提供天然/封顶/真实可升降资格，评分不提交阶级。'),
91:('状态和持续计数偏好','框架计算状态、混乱/迷恋和保留意愿；战斗侧提供真实异常资格，预测不执行状态治疗。'),
92:('类型/能力改变偏好','框架拥有类型进攻覆盖与能力评级方向；战斗侧提供WP47-B实际操作前门/状态查询，保留GR8-AI-001待整改。'),
93:('Misc局部前门和评估边界','框架执行实际存在的Misc评估条件；战斗侧提供其具名查询，依赖/未决说明仅约束本评分而非新增业务。'),
94:('B族注册和缺源默认','框架持有出现→有效绑定的查询语义；计数不能证明目标策略覆盖。'),
95:('B族逐登记/最终绑定','框架保留族+身份、copy源和最终有效处理，正文数值合同才定义实际分数。'),
96:('场域收益匹配数据','框架拥有天气/场地有序匹配和组内一次计分数据，不建立真实天气。'),
98:('固定/条件基数与反击记录估量','框架计算代表估量/最近记录和反击分；战斗侧提供当前记录及规则查询，合成沿WP52-A。'),
99:('多击、蓄力及持续攻击预估','框架执行多击合并近似、两回合惩罚和候选估量；战斗侧提供真实资格，不能把合并预估当逐击反应链。'),
100:('治疗、吸取和牺牲偏好','框架计算预期恢复/牺牲分；战斗侧提供canHeal等具名资格，真实HP夹限和写入另属执行。'),
101:('天气/地形/危害和空间偏好','框架合成场域收益及技能门；战斗侧提供有效天气/实际期限等查询，评分不设置场域。'),
102:('墙、保护和命中控制评分','框架拥有保护/墙/反伤等偏好和copy缺源默认；战斗侧提供实际规则查询，合成由A消费。'),
103:('C族有效键和默认查询','框架持有直接键优先、条件首匹配和缺源默认；有界839键统计只作覆盖资料。'),
104:('C族逐登记最终绑定','框架保留167出现/165有效键及跨族copy失败的策略查询数据，不把空绑定自动回退。'),
105:('物品基础评级','框架拥有215项物品价值和未知/空身份0；价值不是实际伤害或恢复量。'),
106:('类型增幅和宝石条件映射','框架拥有39增幅物/18宝石的评级条件与机制世代门；消费当前可用伤害招查询。'),
107:('固定辅助集合和主规则引用','框架保留辅助偏好集合；黑名单等唯一执行合同直接引用WP47-A/B，不复制第二执行规则。'),
109:('持物V与即时效用E','框架计算物品价值/即时收益和熟成/拼写差异；战斗侧仅提供当前有效物/状态查询，评分不消费物品。'),
110:('物品操作预测','框架计算转移/查封/回收/强制食果/投掷偏好；战斗侧提供前门，评分不改C/I/R/P/Belch。'),
111:('调用/复制/目标混合评估','框架准备替代评估、黑名单和目标分；战斗侧提供实际调用资格，准备可写共享字段须验证异常后继，评分不扣PP。'),
112:('换人/逃离/行动与PP限制评分','框架计算换人、逃离、拘束、号令和PP限制偏好；战斗侧提供专门资格，评分不执行逃跑、换出或扣PP。'),
113:('浮空/变身/侧和位置交换预估','框架计算浮空、变身、重力和交换偏好；战斗侧提供WP45/47-B状态查询，实际写入另行执行。')}
ai_data={77,78,79,80,82,83,84,85,86,87,94,95,96,103,104,105,106,107}
for n,(topic,why) in ai_semantics.items():
    plan(n,F if n in ai_data else C,why,fw='拥有'+topic+'的策略、默认参数、候选/评分输出；不把预测值当真实效果。',
        sd=None if n in ai_data else '提供本节明确消费的实时规则/状态查询并接收实际登记；不默认目标引擎已有Essentials同款AI。',
        questions=['固定目标版本后验证'+topic+'的输入集合、近似/真实查询差异、共享准备字段与异常前缀。',
                   '确认用户期望保留该策略；策略数据、评分查询与真实行动的验证分别登记。'],
        protos=['PROTO-BATTLE-ITEM'] if n==75 else [])

# Diagnostics, state restoration and current source classification.
plan(435,F,'诊断的格式化、日志和控制流属于框架；窗口/控制台/重启由MZ接入。',
    fw='组装异常文本、追加日志并保留日志失败前缀，维护关键段0/1完成返回和调试主循环收尾。',
    mz='显示错误窗口/复制/控制台并消费宿主重启请求，保护消息等待不等于日志/控制流成功。',refs=[625,628,446,451])
plan(439,F,'语言配置/载入/直写保存和用户菜单的选择机会分开。',
    fw='拥有语言候选、当前语言、核心/游戏消息载入与按入口直写存档。',
    mz='在启动/载入菜单提供语言选择和确认，按各入口返回点交付选择，预览不自动持久化。',refs=[642,644,444,446])
plan(445,F,'启动/新游戏/继续由框架编排持久值，MZ消费标题和地图恢复。',
    fw='有序装载启动值/进度并保留选项；控制新游戏重置、地图记录重建或实例复用的条件。',
    mz='提供标题菜单、缺图选图/取消，建立地图显示/坐标及进入离开通知；按已到达前缀恢复。',refs=[642,324,326,451])
plan(451,F,'恢复链的备份/有效性状态与询问、场景和缺图处理分责。',
    fw='读取/校验存档、递归选择备份、删除/紧急保存并区分false和传播异常；保持部分文件状态。',
    mz='询问删除/拒绝退出、按真实顺序清场景及条件恢复，处理缺图选图/取消。',refs=[642,445,326,435])
for n in [449,450]:
    edit(n,scope='待决策')
    active[fid(n)]['future_plan']['questions'].append('由用户决定支持哪些旧存档版本、数组/表格式及旧身份；通用迁移编排与具体兼容表分别验收。')
stats=by_stem[stem('wp06-stats')]
stats['source_classification']='源文未单列分类（统计行为/数据附表）；本表给初始化、更新规则与持久化。'
for n in range(415,425):
    f=active[fid(n)];f['current_applicability']['source_classification']=stats['source_classification']
    edit(n,reason='本节统计字段的初始化、生产事件、更新规则与持久化由框架拥有；来源没有声明其为共享导航。')

# Pokémon domain writes and independently observable presentation consumers.
mark_ui=child(465,'5.1','标记编辑输入、确认取消与两个界面差异',M,
    '六格存储与编辑交互分开；摘要清零的缺值失败不推广到仓库界面。',
    fw='提供六格值和确认后的新值；取消不提交编辑值。',mz='处理8位置导航、确定递增、动作清零及确定/取消，按各界面实际能力绘制。',ranges=[[255,258]],refs=[654,655])
ribbon_ui=child(465,'5.2','缎带按持有顺序分页与图集裁切',M,
    '列表给予/升级/删除规则与12项分页、滚动和裁图分开验收。',
    fw='提供有序缎带身份及图标位置，不把图标位置当排序键。',mz='按持有顺序每页12项和滚动偏移绘制，按图标位置裁图。',ranges=[[269,269]],refs=[655])
plan(484,C,'心量表含战斗派入、Call和战后索引快照消费者，不能由持久规则单方承接。',
    fw='拥有持久G/H、存储性格下降量、步进和净化室；保留未随满队替换移动的战前心量表快照。',
    sd='在玩家所属派入/有效Hyper Call按阶段通知领域下降，场上类型与是否刷新招式按实际入口分别处理。',
    scope='待决策',refs=[5,13,31,485,489,529],questions=['验证派入/Call先后和捕获满队换出后的队伍索引错配；保留历史行为还是迁移修正需另决。'])
plan(485,C,'Shadow持久招式刷新和场上招式副本有明确不自动同步例外。',
    fw='维护前4 Shadow/后4原招记录、候选后缀、原对象PP保留和新槽满PP；捕获刷新并重记首招。',
    sd='保持战斗香不自动重建场上招式，捕获入口另按实际交接刷新；不能由持久变化推断副本已变。',
    scope='待决策',protos=['PROTO-BATTLE-ITEM','PROTO-CAPTURE'],refs=[147,488,529,739])
shadow_recovery_ui=child(487,'6.2','净化恢复中的窗口、命名及调用者失败',M,
    '暂存经验/EV与恢复提交保留父行；首窗口更新失败和遗迹石空回调是独立宿主验收边界。',
    fw='逐阶段提交Shadow/Hyper/缎带/招式/V/S/等级，只有等级工具正常返回才写精确经验及后续学习进化。',
    mz='提供心灵打开/恢复提示、能力变化窗口、更新回调和命名；净化室与遗迹石分别验收，异常不回滚已写值。',
    scope='待决策',refs=[205,206,492,690])
plan(487,C,'战斗收益进入Shadow暂存的阶段门与净化恢复分责，战中成长候选需单独验证。',
    fw='维护S/V、当前经验余量、阶段门、友好限制与非交互恢复算术，裸赋值不偷加战斗门。',
    sd='交付战斗实际经验/EV收益和时机；Shadow收益可能仅暂存而不触发战斗逐级学习。',
    scope='待决策',protos=['PROTO-IN-BATTLE-GROWTH'],refs=[25,26,204,205,578,shadow_recovery_ui])
plan(488,C,'香的登记/复检/退款、持久友好心量表和场上副本跨库存与战斗执行。',
    fw='拥有三种香/笛的作者旗标、库存扣退、持久友好和G，按野外/战斗/裸处理器的不同前门提交。',
    sd='执行登记与复检、清Hyper和返回成功消费身份；不重建场上招式，失败复检交回退款。',
    mz='承接选择器和消息，区分TIMEFLUTE被消费却未净化及取消前缀。',scope='待决策',
    protos=['PROTO-BATTLE-ITEM'],refs=[10,11,186,187,485])
chamber_editor=child(489,'8.1','净化室编成选择、暂持与存取交互',M,
    '编成数学/推进留父行；选择器返回、暂持/交换/取出及取消的即时提交形成独立交互边界。',
    fw='保存9组引用/朝向与可见标志，执行蛋/Shadow原始返回值门、先放后删、双满及盒满仍清源的实际前缀。',
    mz='实现取出模式盒选择及两种退出确认、无队伍面板、移动/组交换/暂持不能退出；空返回不撤回已完成储存操作。',
    scope='待决策',refs=[157,158,172,667,690])
plan(489,F,'组级亲和/流量、资格与顺序领取由框架持有，编成交互独立子行消费。',
    fw='维护NORMAL特殊边、T/F、每步推进及LUGIA九组资格；逐组调用净化后存放再清中心，不保证容量失败保留源。',
    mz='消费逐组提示、净化接点和继续询问；只在实际越过净化提交后进入接收呈现。',scope='待决策',refs=[487,shadow_recovery_ui,chamber_editor])
trade_dispose=child(505,'6','交换图鉴分支两次收尾与宿主释放',M,
    '交换领域条件和最终队伍替换留父行；双收尾/容器重复释放必须单独验证宿主生命周期。',
    fw='两次可到达检查均消费当时收到者物种，最终替换仅在画面调用正常返回后发生。',
    mz='提供交换/图鉴呈现和两处收尾，静态双调用不证明第二次实际抵达进化检查或释放安全。',ranges=[[106,106]],refs=[172,654,687])
plan(505,F,'交换条件与有序提交为领域合同，宿主双收尾另列且保持实际失败前缀。',
    fw='按收到者当前物种/持物与送出者不变之石门求交换进化，维护统计、拥有者、图鉴及最终槽替换。',
    mz='按画面前登记、不可取消演出/进化和正常返回接续；不能把条件命中当已入队。',refs=[172,743,trade_dispose])
plan(519,C,'持续漫游个体跨真实战斗复用，PP/异常/持物和总是逃跑均需引擎协作。',
    fw='持有漫游持续个体、终结/再次遇见/关联记录，按真实正常结果清理和通知，临时生成与真实参战者分开。',
    sd='执行强制单打/每回合逃跑，按真实招式门写PP及终局双方离场状态；对方持物不受玩家侧还原保证。',
    protos=['PROTO-ESCAPE'],refs=[22,23,31,32,147,148,529],questions=['逐结果验证持久HP/PP/异常/持物及通知前缀；总是逃跑策略不能由数值一致推定。'])
radar_fx=child(520,'6.2','雷达摇草动画、列表写入与半秒等待',M,
    '四环与稀有度抽样由框架拥有，动画请求后才写草列表/等待是独立表现前缀。',
    fw='提供四环有效格及稀有度，并在实际动画请求后写摇草列表。',mz='按配置请求普通/剧烈/闪光动画再等待0.5秒，素材和真实调度仍待验证。',ranges=[[95,95]],refs=[355,358])
roamer_debug=child(522,'8.4','漫游状态调试画面与按键门',M,
    '正常取消/事件/保存与开发者画面分开；调试不是默认用户流程。',
    fw='按USE/ACTION/CTRL+ACTION及开关/启用门修改条目、位置和再次遇见限制。',mz='呈现状态与全体命令，按真实按键门采样，不增加任意编辑能力。',scope='待决策',refs=[253,254])
type_author=child(537,'8','类型/招式作者缺省、校验与本地化输入',F,
    '作者原始记录缺省及类别×威力校验不由Showdown运行规则拥有。',
    fw='保留Type/Move省略与显式值、WP04校验及Name/Description各自语言域，向战斗提供有效记录。',ranges=[[163,163]],refs=[394,395,396,436,437])
plan(543,C,'持久异常与战斗计数/阶级分别归属，指定写入同步不能省略框架。',
    fw='保存真实异常与持久计数，按指定写入同步；不把COMATOSE查询或战斗阶级写为持久值。',
    sd='维护剧毒累计、混乱/迷恋/畏缩/阶级及中央提交守卫，指定状态和计数分别刷新并输出持久写回。',refs=[147,739,544,545])
held_growth_directory=child(571,'1','持物目录中的经验与EV两成长族',C,
    '注册目录需要按消费者分责；Exp/EV两族查询持久当前物及I回退，不能随其它族整交引擎。',
    fw='提供持久当前物品和I回退，拥有收益/上限及最终成长写入。',sd='在战斗收益阶段调用实际族并交付结果；目录不证明目标实际登记。',ranges=[[30,31]],protos=['PROTO-IN-BATTLE-GROWTH'],refs=[578,204,25])
plan(574,C,'C/I/R/P/Belch和持久成长查询跨战斗临时状态、持久写穿与终局还原。',
    fw='拥有持久当前持物/成长输入，接收C变化写穿并按实际玩家侧终局范围处理还原。',
    sd='维护C/I/R/P/序号/Belch/讲究锁/轻装、消费/颊囊/共生次序，逐helper重读状态且不统一回滚。',refs=[148,31,578,740],protos=['PROTO-IN-BATTLE-GROWTH'])
plan(576,C,'LEPPA持久槽先写再按同下标强写战斗槽是同步例外，主动背包与被动持物分开。',
    fw='持有持久招式PP及当前持物，按持物槽选择/限幅提交；主动使用另消费背包。',
    sd='执行持物资格与强制门，LEPPA不核对场上身份即按同下标写PP，再按C/I/R/P/Belch消费。',
    protos=['PROTO-BATTLE-ITEM'],refs=[147,186,187,574,739])
plan(577,C,'受击/退出的永久转物和消费前缀不能只由战斗层吞并。',
    fw='接收持久C/I转移、持物消费和异常前已写HP/PP；背包不随被动消费减少。',
    sd='逐击重读物品并执行共生、退出/替补和负选择已消费规则，保留自然之恩续击异常且不假定局部失败已正常还原。',
    refs=[148,20,31,574,576,740],protos=['PROTO-BATTLE-ITEM'])
held_world_inputs=child(579,'7','经验分享与奖金等世界持物直接消费者',C,
    '注册表外世界/成长持物输入具有独立持久消费者，不能统称Showdown处理器。',
    fw='提供EXP.SHARE、AMULETCOIN、LUCKINCENSE持久输入和成长/奖金写入，EXPALL仍是背包检查。',
    sd='在经验分配和奖金阶段消费当前持物/标记并给出阶段结果，按主规则与框架交接。',ranges=[[167,167]],
    protos=['PROTO-IN-BATTLE-GROWTH'],refs=[25,31,148,153,204,578])
safari_transfer=child(580,'3.4','Safari回起点场景门与转移表现',M,
    '预算/会话状态与只在地图场景回起点的宿主转移分开验收。',
    fw='提供已写会话决定及起点，回起点不清会话，缺起点按实际访问失败。',mz='地图场景才淡出/下车/按固定向下转移；非地图跳过，不能凭决定已写宣称转移。',scope='待决策',refs=[324,326,650])
contest_timer=child(582,'5.3','捕虫倒计时帧门、暂停微更新与定时器',M,
    '缩队/预算与计时显示及宿主微更新是不同验收边界。',
    fw='提供单调起点/限时、到期与24小时查询；0/负值的到期、显示门不同。',mz='仅三推迟门阻止到期；暂停循环可微更新，按非零限时建定时器并显示00:00边界。',scope='待决策',refs=[425,650,625,626])
contest_award=child(582,'5.4','捕虫判奖后的场景门与转移',M,
    '判分提交先于地图场景转移；缺判奖点可在已判后失败。',fw='先写决定/判分/名次，捕虫全灭先治疗再进入判奖。',
    mz='地图场景才淡出下车并按判奖点方向转移/刷新，同图也刷新；非地图跳过。',scope='待决策',refs=[583,600,324])
mode_pause=child(585,'8.3','Safari/捕虫暂停信息、退出保存与调试交互',M,
    '模式会话/持久归属保留父行，暂停UI和退出保存前缀单独验收。',
    fw='提供模式可见门、决定/判奖和保存逐项状态，保存失败只按WP09回退特定字段。',
    mz='绘制信息行、专用退出确认、普通Quit Game共享保存和调试编辑；拒绝保存仍退出，不替代模式结束。',scope='待决策',refs=[580,582,444,446,650])
berry_display=child(590,'5','树果常规显示调用门、图形与闪光',M,
    '时间结算算术留父行；常规显示是否请求结算、土壤/植物选图和闪光是独立表现边界。',
    fw='按机制提供结算结果/水分阶段，旧机制常规显示不自动结算。',mz='依调用门更新显示，阶段/水分选图、缺图回退、闪光及转向；不以显示更新证明规则已推进。',ranges=[[70,70],[84,88]],refs=[355,358,643])
berry_interaction=child(591,'6','树果询问、背包选择与采摘等待',M,
    '入口状态分派与交互过程分开；确认等待能微更新，提交前缀需跨双方验收。',
    fw='按施肥先写先扣、种植统计/状态/库存、采摘预检→统计→加入→开关→返回→外层reset提交，取消不回滚前缀。',
    mz='提供三选/过滤背包/确认文案及消息等待，区分按键退出前门和可到达地图微更新；提示前qty不因等待重取。',ranges=[[107,134]],refs=[177,186,626,650,590])
field_host=child(596,'3','移动完成、帧通知及Repel选择的宿主交接',M,
    '通知次序/全局计数留父行，碰撞完成、动画/自动移动、警告和选择器需宿主输入更新验收。',
    fw='提供真实通知次数/门和已写计数、煤烟及Repel状态，低电量先置警告后请求消息。',
    mz='完成碰撞计时/移动后派发通知、草丛/自动运动与冲浪收尾；处理警告消息及Repel确认/过滤选择，不能把无坐标变化推为无完成步。',
    ranges=[[27,36],[41,41],[45,45],[50,50],[55,55]],refs=[327,330,355,186,625,626])
poison_host=child(598,'5','野外毒伤批次反馈与全灭淡出交接',M,
    '逐成员毒伤保留父行；一次批次音效/闪烁和全灭消息淡出独立验收。',fw='提供首次实际处理标记与全队可战门，失败回程治疗后续成员状态。',
    mz='每批仅一次毒步音效/红闪；全灭消息和BGM/BGS淡出后调用回程，不把单成员濒死等同全灭。',ranges=[[85,85],[90,94]],refs=[600,355,626])
blackout_host=child(600,'7.2','失败回程目的地消费、清场与转移',M,
    '治疗/目的地状态与取消载具、伙伴清理和地图显示转移分开。',fw='先统计/治疗，再解析中心或家并写开关/转移参数；缺家图早返保留逃脱点，无家可走末尾。',
    mz='按消息/载具/伙伴清理/下车和地图场景门转移刷新；家缺资源与非地图分别验收，不保证每次换图。',ranges=[[141,146]],refs=[324,326,153,650])
field_debug=child(601,'8.2','野外状态调试、素材与作者证据入口',M,
    '运行时持久归属与开发者/资源/编译入口分开，调试范围保留用户决定。',fw='Repel数值及病毒三个动作沿各自正常门写状态；提供中心事件识别和资源存在查询，识别不等于构造。',
    mz='提供只读菌株/期限、动作菜单和Repel编辑；素材请求/宿主逐帧仍待验证。',scope='待决策',refs=[253,254,394,355])
plan(608,M,'本节本身是图鉴交互消费者，应明确框架记录与MZ筛选/选择/显示分工。',
    fw='提供区域/拥有见过/末次形态与排序持久状态；Start先写排序、形态首轮/移动写false异色，取消不自动回滚。',
    mz='提供区域/搜索/排序/形态菜单和Info图像请求；只请求普通外观，编号视图与摘要/简略差异分别验收。',refs=[604,605,606,607,669,670])
voltorb_input=child(611,'4.1','翻牌按键仲裁、局部动画和确认等待',M,
    '奖励余额提交留父行；局部阶段的按键拒绝和完成确认独立于数学结果验收。',fw='按局部正常返回点提交已揭/临时奖额，奖励先写余额/统计不因后续等待撤回。',
    mz='按UP>DOWN>LEFT>RIGHT>USE>ACTION>BACK采样，普通翻面/雷/揭盘/收牌分段等待，只在专门循环接受确认。',scope='待决策',refs=[699,625])

# Battle debug and UI are consumers of real domain contracts, not substitutes for them.
plan(257,C,'测试对象构造、普通开战/捕获/结算及双层状态调试跨三方，调试画面不拥有战斗真值。',
    fw='构造测试个体/队伍及持久副作用，按正常接收/资源规则提交调试触发结果。',
    sd='提供真实开战、阶段/捕获/终局与场上状态读写的目标引擎候选；不是只有UI赋值。',
    mz='提供战斗调试入口、菜单和显示，开发者范围由用户决定。',scope='待决策',
    protos=['PROTO-CAPTURE','PROTO-BATTLE-ITEM','PROTO-ESCAPE','PROTO-IN-BATTLE-GROWTH'],refs=[4,11,22,25,31,529])
plan(261,C,'120项四层状态必须保留字段层级、可编辑白名单和真实消费者，不能以显示值代表引擎支持。',
    fw='提供原个体及持久层的白名单读写，保留不同层之间不自动同步的门。',
    sd='调查场上/侧/位置/全场各字段的目标映射、读写许可和阶段消费，未知映射保持待验证。',
    mz='呈现按层分类的120项调试查询和允许的编辑操作，不暴露源中未有的任意编辑。',scope='待决策',
    protos=['PROTO-BATTLE-ITEM','PROTO-IN-BATTLE-GROWTH'],refs=[4,147,148,33,34,35,36])
ui_battle={
677:('命令/逃跑的屏幕控制与真实执行交接','持有队伍/拥有者和库存及退出包装状态。','执行尝试逃跑、登记/撤销、阶段与决定；正常结束和显式中止分别提交。','显示命令和逃跑反馈，采样输入，按已到达阶段结束场景。',['PROTO-ESCAPE'],[9,11,22,31,32]),
678:('战斗菜单的Mega、目标资格与输入登记','提供Mega持久身份、所需物与席位映射。','查询Mega资格、目标合法性及登记复检，动态目标由执行时解析。','处理Fight/Target导航、取消/USE和可见按钮态，不以高亮代替许可。',[],[9,10,51,472,732]),
679:('背包战斗用物的选择、扣除与退款残留','拥有实时背包容量/扣退及持久个体效果写入。','登记消费身份、执行前复检及退款残留、终局二次退款/下轮直接清理。','过滤/选择道具与对象、确认/取消并反馈，界面关闭不自动还款。',['PROTO-BATTLE-ITEM'],[10,11,31,177,186,187,731]),
680:('换人界面、资格及替补/逃跑消费者','提供显示队伍与队伍下标/拥有者的映射和持久对象。','查询换入/换出、组合与二次登记资格；终局替补/逃跑沿真实门。','负责可取消/摘要/按钮态及替补选择小循环，按具体入口不同许可。',['PROTO-ESCAPE'],[18,20,22,31,734]),
681:('战中成长窗口、持久槽与场上槽提交','拥有经验/等级/能力及持久学习，按每级和教学工具的具体顺序写入。','交付战中收益/暂停点，按同步门接收场上招式，写生两次提交不原子。','提供经验/能力变化、遗忘选择及取消学习；暂停不是事务回滚。',['PROTO-IN-BATTLE-GROWTH'],[25,26,147,204,205,206,735,739]),
682:('捕获演出、敌队移除和接收队列交接','拥有库存球、图鉴/队伍/盒子及满队换出后记忆数组回填。','执行投球判定、敌队移除与捕获队列；成功决定和真正接收为两个阶段。','表现球/捕获/新图鉴与命名/满队选择，确认失败保留实际提交前缀。',['PROTO-CAPTURE'],[11,29,31,157,158,528,529,530,531])}
for n,(why,fw,sd,mz,protos,refs) in ui_battle.items():
    plan(n,C,why,fw=fw,sd=sd,mz=mz,protos=protos,refs=refs)
plan(684,C,'Safari/捕虫/Palace/Arena/回放覆盖含真实规则和恢复，三方边界须按模式分别验收。',
    fw='持有模式会话、预算、报名/恢复与记录流，按各覆盖入口提交领域状态。',sd='调查特殊命令/捕获/成长/裁判/回放动作及决定，缺失目标机制保持未验证。',
    mz='提供模式专属菜单、Arena裁判显示和回放残余选靶/中止，不宣称单纯重画即覆盖。',scope='待决策',
    protos=['PROTO-CAPTURE','PROTO-BATTLE-ITEM','PROTO-ESCAPE','PROTO-IN-BATTLE-GROWTH'],refs=[128,129,134,135,136,580,581,582,583,737,738])
for n,fw,mz,refs in [
 (673,'按PC存取/丢弃的库存先后提交，保留部分添加/移除及已到达前缀。','提供数量/确认/取消和消息等待，消息失败不撤回库存。',[177,178,179,626]),
 (674,'按WP29执行买卖、库存过滤/回退、货币和数量提交。','提供商店列表/数量/确认、相机及消息，取消只停止未到达的提交。',[194,195,196,626]),
 (687,'负责物种/能力/HP/持物与额外个体/图鉴/学习等有序进化提交。','提供演出/取消/收尾，只有演出正常抵达后才续接对应领域提交。',[491,492,493,743]),
 (688,'在孵化显示前后按WP35提交蛋标志、首招/图鉴及昵称，命名拒绝不回滚孵化。','提供孵化动画、命名输入与消息/资源生命周期，异常只保留真实前缀。',[220,221,222,623]),
 (690,'持有净化室容器/引用及成长/净化/存放/清中心提交，容量和跨级失败不同。','提供组编辑/选择器和窗口更新；盒满/跨级窗口等失败不伪装成成功净化接收。',[487,489,shadow_recovery_ui,chamber_editor])]:
    plan(n,M,'来源本节为宿主消费者；逐项明确领域提交与输入/表现职责。',fw=fw,mz=mz,refs=refs,scope='待决策' if n==690 else None)

# Independent activities use framework session/rule authority; MZ samples and renders.
activity_rules={
695:('Duel固定16格损伤与一次特殊资格','提交双方矩阵损失、特殊资格及生命下限；与生物等级/命中/随机伤害无关。',None),
696:('Duel加权动作与台词随机次序','按特殊已用状态抽3/13等权重动作，再均匀选台词；包装两次身份随机另计。','先显示动作相关台词再询问玩家；台词确认不改变规则随机顺序。'),
697:('Duel会话状态与不可取消输入','持有10/10生命、先玩家零失败的终局优先级与特殊资格。','请求速度/朝向、肖像生命窗和动作表现；BACK继续选择，正常收尾恢复速度/朝向。'),
701:('老虎机场景账、下注/重玩与退出门','持有场景信用/下注/重玩及开转/取消规则，下注与支付先不写持久余额。','按DOWN优先于重玩及USE/BACK不同状态门采样，点亮线与等待3秒/.5秒/2秒后继续。'),
702:('老虎机支付、持久离场覆盖与净差统计','按待付/场景信用/上限逐次转移，正常离场写持久余额并仅记净差；不保证外部并发隔离。','支付循环最多每更新一枚或USE/满额清算；不把20枚/秒注释当实测节拍。'),
705:('老虎机22位置有序行为数据','拥有三轮各22项顺序及频次，结算读顶部及两循环前驱；不以频次推出最终中奖率。',None),
706:('挖矿13项铁形状行为数据','拥有有序13条等权/不去重形状和占用格，供摆放/阻挡规则消费。',None),
709:('挖矿初始化抽样、摆放及层厚算法','拥有候选累计权重、身份去重、矩形/占格、位置内层无上限与铁500次及130层厚抽样顺序。','显示实际埋藏数/初始光标与镐，不把图像位置当布局权威。'),
710:('挖矿削层、耐久和揭露规则','拥有镐/锤矩阵、中心铁门、耐久/调试豁免、全占格揭露与待领登记。','方向/切工具/敲击/放弃输入和工具忙门；只有闪光正常返回才通知已揭登记。'),
711:('挖矿终局优先级与逐件库存结算','坍塌先于全揭但不没收已揭物；按顺序逐件加包、允许整批部分成功，重复裸领取不幂等。','确认放弃/拒绝、坍塌/挖完提示及逐件反馈、正常关闭场景。'),
714:('拼图参数、权威状态与完成谓词','拥有模式/尺寸默认、排列/角度/暂持及前w×h完成谓词；表外模式不自造玩法。','按资源后缀切图、暂存列坐标和光标显示，不以屏幕状态替代排列权威。'),
715:('拼图七模式合法动作与完成规则','拥有互换/滑块/整行列移/旋转动作与各模式完成条件及旋转−1 mod4。','显示预渲染旋转图或整精灵旋转；媒体分支不改变规则。'),
716:('拼图动作前门和排列/角度提交','执行有界移动、合法动作和true/false返回，模式3–6按USE状态改变方向语义。','按trigger/repeat/press和本节独有优先序采样，越界拒绝也阻止低优先BACK。'),
717:('拼图洗牌、五步构造与尺寸限定可解性','拥有普通随机、模式3实际parity复检/末格漏扫及6/7五步构造，不承诺全尺寸可解/均匀或重播。',None),
718:('拼图完成/取消返回与动作提交时序','先判完成、未完成BACK返回false且不持久局面；按各动作正常返回点提交排列/角度。','处理隐藏光标/末块揭示、独立插值/淡入淡出及专门USE/BACK完成确认，动画内不接受正常动作。'),
720:('拼图权威状态、动作不变量与可达范围','持有排列权威/完成范围/模式尺寸限定保证及固定奇偶不变量，不将固定证明当求解器或运行覆盖。',None),
721:('拼图输入域、规则反例与宿主失败','保留表外模式、默认尺寸、非方形列端点、初始完成及空槽旋转的真实规则边界。','处理背景回退/主图音效失败和动画输入阻塞；宿主异常呈现仍待验证。')}
for n,(why,fw,mz) in activity_rules.items():
    plan(n,F,why,fw=fw,mz=mz,scope='待决策',refs=[duel_entry] if n in [695,696,697] else [slot_entry] if n in [701,702,705] else [mine_entry,mine_candidates] if n in [706,709,710,711] else [])
plan(699,M,'转轮时钟/停止消费有独立宿主时序，随机权威由框架提供。',
    fw='拥有三次初始索引抽样和每次停止滑移抽样/难度二次选择；重玩仍消费样本再强制零滑。',
    mz='按真实H/v/t更新区间，先停保留上次顶部或再提交顶部；重复USE重抽仍转最左轮，更新先于本轮输入。',scope='待决策',refs=[705,700,701])
mining_busy=child(710,'4.1','挖矿输入优先序、工具时钟及闪光忙门',M,
    '削层/耐久规则与11时间档忙门、清忙后终局检查形成不同验收边界。',
    fw='在损耗/挖层后交付动作与终局状态；闪光返回才登记待领。',mz='更新工具时钟与闪光alpha、拒忙期输入；清忙先判坍塌/全揭，再按方向>ACTION>USE>BACK采样。',scope='待决策',refs=[709,711])
tile_busy=child(718,'6.1','拼图动作阻塞、宿主读回与完成等待',M,
    '完成/取消规则与动画读回/时间段单独验收；动画更新Input不等于受理正常动作。',
    fw='按动画退出或中途已到点的位置提交离散角度/排列，异常不自动回滚。',mz='等待角度/坐标/alpha实际读回，行列淡入前排列已提交；专门确认后才返回true。',scope='待决策',refs=[716,717])

# Pure provenance/ownership/test-design sections are archived without altering their old source or ID.
metadata_decisions=[
 (46,list(range(48,55)),'效果身份到唯一主合同的责任索引，不新增执行规则。',['COMBAT-04']),
 (47,[33,34,35,36,48,49,50,51,52,53,54,542,550,558,574],'已有/域外责任登记，关联真正主规则。',['COMBAT-04']),
 (56,list(range(58,63)),'60身份的主合同覆盖索引，不另计效果实现。',['COMBAT-04']),
 (57,[33,34,35,36,48,49,50,51,52,53,54,58,59,60,61,62,574],'共享与域外归属元数据；保留范围限制。',['COMBAT-04']),
 (63,[58,59,60,61,62,9,13,20],'已确认观察/批准同步和静态设计登记；行为已由对应主规则承接。',['COMBAT-04']),
 (81,[73,74,75,76,77,78,79,80,88,89,90,91,92,93,109,110,111,112,113],'AI责任与未决范围，不是独立AI能力。',['CAI-02']),
 (97,[94,95,96,98,99,100,101,102,88,89,90,91,92,93],'B包保留责任/未关闭范围，关联实际策略与查询。',['CAI-02']),
 (108,[103,104,105,106,107,109,110,111,112,113],'C包责任和开放组合，不能当独立处理器。',['CAI-02']),
 (122,[114,115,116,117,118,119,120,121],'56来源身份及归属目录；主合同按报名/资格/调整/条款承载。',['COMBAT-04']),
 (131,[128,129,130,134,135,136,308,309,310,311,312,313,314,315,316],'设施模式保留项与审查限定，不新增模式实现。',['COMBAT-04']),
 (266,[267,268,269,270,271,272,273,274,275,276,286,287,294,301],'同文件WP73B/74/04/75归属声明，不另建实现功能。',['DS-003']),
 (317,[324,325,326,347,348,349,368,369,370,379,380,381,599,600,634],'Demo世界配置/入口候选及缺证；没有要求复刻具体Demo。',['DS-003']),
 (318,[150,154,224,225,226,227,228,229,230,231,232,233,234,634],'Demo遭遇/训练家/电话证据，既有消费者承载行为。',['DS-003']),
 (319,[114,124,128,129,235,236,580,581,582,583,609,695,699,708,714],'Demo特殊玩法/设施配置候选，不证明事件可达或用户纳入范围。',['DS-003']),
 (320,[117,118,119,253,262,267,277,294,308,634],'UI/作者链与平衡等级的证据索引，关联既有消费者。',['DS-003']),
 (321,[324,325,326,368,379,380,600,634],'C1–C8跨表一致性检查结果是来源审计证据。',['DS-003']),
 (322,[324,325,326,379,380,600,634,114,124,580,582],'G01–G12缺材料和不可证明的事件链是证据限制。',['DS-003']),
 (345,[338,339,340,341,342,343,344,327,328,329,330],'移动路线分派核对口径与通行责任引用，不新增运动。',['WU-07']),
 (392,[385,386,387,388,389,390,391,394,397,483,484,485,487,488,489],'未验证组合/责任表，关联配置及实际消费者；未验证不是功能。',['KF-001']),
 (398,[393,394,395,396,397,399,401,402,403,404,405,406,461,465,491,494,604,634],'字段责任目录只指派主责，不重复展开领域语义。',['KF-001']),
 (407,[399,400,401,402,403,404,405,406,436,277,294,355],'编译/作者/本地化交界的归属登记，不新增编译功能。',['KF-001']),
 (478,[470,471,472,473,474,475,476,477],'Mega/Primal静态来源数量及核对限制。',['POK-S07']),
 (480,[484,485,486,487,488,489],'Shadow成长/净化室固定算术和向量是已有主规则验收材料。',['POK-S07']),
 (482,[479,481,483,484,485,486,487,488,489],'Shadow来源字段与证据资格，不是新能力。',['POK-S07']),
 (500,[494,495,496,497,498,499,501,502,503,504,505,506],'进化固定算术/状态对照，主规则在WP32。',['POK-S07']),
 (539,[538,540,541,542,544,545,546,547,548,549],'阶级范围/清点方法与共享责任，关联行为表与主合同。',['POK-S07']),
 (553,[550,551,552,554,555,556,557],'伤害/恢复覆盖责任及域外引用，不是另一执行合同。',['POK-S07']),
 (573,[571,572,574,575,576,577,578,579],'持物目录覆盖/来源检索与开放范围，关联主消费者。',['POK-S07']),
 (618,[615,616,617,lottery_match],'彩票冻结依赖/旧批准/开放问题归交接元数据。',['POK-S07']),
 (704,[699,700,701,702,703,705,slot_entry],'老虎机固定依赖/配置/未决和事件缺证。',['WU-07']),
 (707,[706,mine_candidates,708,709,710,711,712],'挖矿48身份/口袋的来源资格不替代61候选行为表。',['WU-07']),
 (713,[706,mine_candidates,708,709,710,711,712],'挖矿冻结依赖/配置/不终止及宿主未知是验收元数据。',['WU-07'])]
for n,repls,why,groups in metadata_decisions:retire(n,repls,why,groups)

world_roles={
346:('地牢参数/种子与地图建立编排','拥有参数双键回退、种子三级选择/无条件清待播与全局重播及部分副作用；临时查询也按建立通知消费。','在实际地图建立改写尺寸/图块并接续事件实例，区分未驻留临时图与真实转移；不据查询返回恢复所有状态。',[324,325,426,427]),
348:('地牢符号图块化规则与宿主数据写入','拥有符号映射、每格随机、墙偏移及256等符号邻接变体映射，规则由框架提供。','把确定图块结果写入宿主三层地图数据并显示；图像可用性与通行另验。',[346,347,324,355]),
349:('地牢摆放候选、重试与坐标消费','拥有房间尺寸/占格间距、1000次单事件及100轮整体尝试，区分事件失败抛错与玩家失败正常保留旧暂存。','写数据事件位置和玩家传送暂存并按真实转移链消费；不自动检查最终地面/通行或修复旧矩形。',[346,347,324,327,333]),
372:('世界天气概率、意图及显示渐变分层','拥有地图概率/真实转移重掷、类型相同跳过与意图类型/强度/时长，不附加自动过期。','按意图类型差异启动固定渐变，连接后写duration20与显式重建0分开，正时长大小不决定名义渐变耗时。',[324,325,355,358]),
373:('天气身份/类别与Snow/Storm/Sun逐帧表现','提供天气身份、类别及战斗环境的逻辑映射；不把世界天气身份等同全部战斗规则。','实现Snow扰动、Storm闪屏、Sun逐帧更新和粒子/色调；素材与真实时间待验证。',[372,355,358,33]),
374:('场地招式资格、持久提交与演出交接','拥有十二族徽章/成员/地形资格及目的地/开关/使用统计的真实提交，按父子边界消费已列徽章和摇树算术。','显示选择/确认、动画并执行地图/载具/事件操作；取消和异常仅停止尚未到达阶段。',[327,328,329,330,368,369,370,655]),
381:('钓鱼随机咬钩门与输入时间窗','提供鱼竿/特性咬钩阈值及随机消费和遭遇请求，成功输入不保证遭遇实际开战。','建立等待/反应窗口、采样确认及钓鱼姿态/音效，遵守真实更新顺序且不将名义秒数当实测。',[379,380,382,383]),
634:('电话联系人生命周期与实时画面','拥有联系人、版本/再战上限和双倒计时、生成来电与全局状态；界面拖动不创造联系人。','提供电话列表/呼叫/实时拖动与消息显示，满足菜单/消息/路线门才消费计时通知。',[635,636,637,638,425,596]),
656:('队伍命令和物品/邮件/奶招提交','按奶招HP扣除、给予/取回/写信/移位及资格门拥有真实资源与字段写入；嵌套取回不回滚原已提交值。','处理命令/选择/消息和取消，保留移位发起时旧身份；表现失败不撤回先入袋/清物。',[183,186,187,188,239,240,241]),
664:('仓库集合操作和表现失败前缀','按WP25执行存取/拿起/交换/释放及治疗/最后可战门，不把完成一半操作统一回滚。','负责盒/队伍/暂持显示、动画/确认/摘要，退出保留已完成集合/标记/盒名墙纸写入。',[157,158,159,160,161,162,655]),
666:('图鉴搜索四层状态与持久排序','提供WP62记录及Start先写持久模式、结果态BACK归零；空结果不撤回模式，不替换已接受参数/列表。','维护焦点、本地子页/外层草稿、已接受会话参数和当前列表，按独有按键优先序及37档候选操作。',[604,605,606,607,608]),
667:('条目刷新和形态选择查看写入','WP62拥有末次性别/形态/异色记录及查看写入；普通图像刷新不写，形态首轮/移动三参写false且取消不回滚。','提供三页夹限/物种边界、Forms首末回绕及普通外观图像请求，摘要完整与获得简略编号分开。',[604,605,606,607,608])}
for n,(why,fw,mz,refs) in world_roles.items():plan(n,active[fid(n)]['future_plan']['destination'],why,fw=fw,mz=mz,refs=refs)
edit(358,reason='特殊注册表仅覆盖条件/优先级/演出注册；战前包装前缀与正常恢复已新增独立FR-000726，二者分别验收。',refs=[transition_wrapper])

# The following explicit document contracts were read from their fixed dependency
# sections (source-dependency-excerpts.json). These are shared authoring prerequisites,
# not claims that every dependent behavior is already supported by either target.
document_dependency_decisions={
'wp39':['wp20','wp24','wp25','wp11','wp02','wp59','wp36','wp12'],
'wp40':['wp39','wp19','wp20','wp27','wp28','wp24'],
'wp41':['wp40','wp27','wp39','wp20','wp21','wp24'],
'wp42':['wp41','wp30','wp25','wp44-statuses','wp45','wp19','wp20','wp24','wp39','wp40'],
'wp45':['wp40','wp11','wp59','wp39','wp41','wp43','wp44-statuses'],
'wp47-a-move':['wp40','wp43','wp44-statuses','wp45','wp46-damage-multihit'],
'wp47-b-switching':['wp41','wp44-statuses','wp45','wp20','wp21','wp27','wp40','wp42','wp49','wp48','wp46-damage-multihit','wp47-a-move'],
'wp49':['wp41','wp42','wp48','wp44-statuses','wp45'],
'wp51-ai-action':['wp40','wp41','wp28','wp43','wp24','wp50-held-item-triggers'],
'wp52-a-generic':['wp51-ai-action','wp50-held-item-triggers','wp40','wp41','wp43','wp44-statuses','wp48','wp46-damage-multihit','wp47-a-move','wp47-b-switching'],
'wp52-b-field':['wp51-ai-action','wp45','wp46-damage-multihit','wp49','wp50-held-item-triggers','wp52-a-generic','wp43','wp47-a-move','wp44-statuses','wp48'],
'wp52-c-items':['wp20','wp27','wp28','wp40','wp41','wp47-a-move','wp47-a-attributes','wp47-b-switching','wp47-b-control','wp49','wp50-held-item-triggers','wp51-ai-action','wp52-a-generic','wp52-b-field'],
'wp54-entry-eligibility':['wp25','wp30','wp39','wp44-statuses','wp40','wp42','wp43','wp46-damage-multihit','wp47-a-move','wp47-b-switching','wp50-held-item-triggers','wp54-entry-rules'],
'wp55':['wp54-entry-eligibility','wp54-entry-rules','wp42','wp50-held-item-triggers','wp09','wp10','wp20','wp24','wp30','wp25'],
'wp56':['wp55','wp54-entry-eligibility','wp54-entry-rules','wp51-ai-action','wp44-statuses','wp40','wp42','wp43'],
'wp58':['wp06-time','wp42','wp55','wp56','wp38','wp62','wp09'],
'wp18':['wp03','wp02','wp06-time'],
'wp20':['wp18','wp19','wp17-messages'],
'wp24':['wp18','wp02','wp03','wp12','wp13-map','wp39'],
'wp25':['wp20','wp24','wp18','wp10'],
'wp26':['wp25','wp08','wp18','wp20','wp21','wp24','wp17-messages','wp06-time','wp02'],
'wp27':['wp03','wp24','wp10','wp17-messages','wp20','wp02'],
'wp28':['wp20','wp27','wp30','wp31','wp18','wp19','wp21','wp24','wp06-time'],
'wp29':['wp24','wp27','wp18','wp06-time','wp03'],
'wp30':['wp19','wp20','wp24','wp06-time','wp18','wp02'],
'wp33':['wp25','wp27','wp30','wp06-time','wp20','wp18','wp24','wp09','wp21'],
'wp35':['wp34','wp12','wp25','wp26','wp33','wp09','wp06-time','wp15','wp17-messages','wp18','wp20','wp24','wp62'],
'wp36':['wp03','wp11','wp12','wp19','wp24','wp59','wp25','wp18','wp20','wp21'],
'wp57':['wp55','wp25','wp54-entry-eligibility','wp54-entry-rules','wp18','wp30','wp50-held-item-triggers'],
'wp64':['wp28','wp27','wp26','wp62','wp07-diagnostics','wp09','wp66-a','wp04','wp17-messages'],
'wp68-triple':['wp17-messages','wp19','wp24','wp27'],
'wp72':['wp10','wp24','wp27','wp39','wp51-ai-action'],
'wp73-a':['wp04','wp18','wp24','wp27','wp72','wp73-b'],
'wp73-b':['wp04','wp11','wp12','wp15','wp36','wp72','wp73-a'],
'wp74':['wp15','wp16-world','wp67-a','wp72','wp73-a','wp04'],
'wp75':['wp04','wp13-map','wp15','wp17-messages','wp08','wp61','wp73-a'],
'wp76':['wp54-entry-eligibility','wp55','wp57','wp51-ai-action','wp52-a-generic','wp52-b-field','wp52-c-items','wp44-statuses','wp72','wp73-a','wp75','wp08'],
'wp11':['wp05','wp09','wp12','wp13-map','wp15','wp59','wp03'],
'wp12':['wp11','wp06-time','wp36','wp59','wp13-map','wp15','wp03'],
'wp13-map':['wp11','wp12','wp05','wp15','wp09','wp39','wp72'],
'wp14':['wp11','wp03','wp06-time','wp09','wp13-map','wp04'],
'wp15':['wp03','wp07-diagnostics','wp06-time','wp11','wp12','wp13-map','wp21','wp65-title'],
'wp16-pre':['wp15','wp16-world','wp36','wp42','wp60-fishing','wp59','wp39','wp55','wp58','wp53'],
'wp16-world':['wp11','wp12','wp13-map','wp15','wp06-time','wp13-interpreter'],
'wp59':['wp06-time','wp11','wp12','wp20','wp24','wp09','wp13-map','wp36','wp60-berry','wp45','wp15'],
'wp60-fishing':['wp36','wp12','wp28','wp27','wp06-time','wp05','wp39','wp38','wp67-a'],
'wp02':['wp04','wp03','wp08','wp65-title'],
'wp03':['wp04','wp02'],
'wp04':['wp02','wp03','wp07-diagnostics','wp08','wp73-a','wp75','wp15'],
'wp05':['wp07-diagnostics','wp09','wp04','wp02'],
'wp06-time':['wp05','wp09','wp10','wp02','wp03','wp14','wp36','wp63','wp61','wp58'],
'wp07-deprecation':['wp07-diagnostics','wp08','wp03'],
'wp07-diagnostics':['wp04','wp05','wp09','wp10','wp07-deprecation'],
'wp08':['wp04','wp09','wp02'],
'wp09':['wp06-time','wp08','wp10','wp02','wp07-diagnostics'],
'wp10':['wp09','wp05','wp07-diagnostics','wp02'],
'wp19':['wp18','wp20','wp30','wp36','wp24','wp23-shadow-hyper','wp21','wp34','wp03'],
'wp21':['wp18','wp19','wp20','wp22-mega','wp23-shadow-hyper','wp31','wp30','wp33','wp34','wp39','wp42','wp15','wp24','wp62','wp10'],
'wp22-mega':['wp21','wp39','wp40','wp18','wp19','wp20','wp41','wp42','wp38','wp62'],
'wp23-shadow-hyper':['wp20','wp30','wp38','wp49','wp18','wp19','wp21','wp25','wp26','wp28','wp31','wp40','wp42','wp62'],
'wp31':['wp18','wp19','wp20','wp30','wp32-contextual','wp28','wp25','wp62','wp38','wp26','wp06-time'],
'wp32-contextual':['wp31','wp26','wp42','wp11','wp59','wp18','wp25','wp30','wp38','wp39','wp40','wp41','wp62','wp22-mega','wp23-shadow-hyper'],
'wp34':['wp33','wp19','wp20','wp21','wp18','wp24','wp27','wp35','wp61','wp26'],
'wp37':['wp36','wp42','wp06-time','wp41','wp09','wp10','wp05','wp11','wp12','wp15','wp19','wp20'],
'wp38':['wp20','wp25','wp27','wp30','wp39','wp42','wp47-b-switching','wp23-shadow-hyper','wp53','wp62'],
'wp43':['wp19','wp20','wp39','wp40','wp44-statuses','wp45','wp42','wp46-damage-multihit','wp47-a-move','wp47-b-switching','wp48','wp50-held-item-triggers'],
'wp44-statuses':['wp20','wp39','wp40','wp43','wp41','wp45','wp42','wp46-damage-multihit','wp47-a-move','wp47-b-switching','wp48','wp49','wp50-held-item-triggers'],
'wp46-damage-multihit':['wp43','wp44-statuses','wp44-effect','wp45','wp40','wp41','wp42','wp48','wp49','wp47-a-move','wp47-b-switching','wp50-held-item-triggers'],
'wp48':['wp43','wp44-statuses','wp44-effect','wp45','wp40'],
'wp50-held-item-triggers':['wp28','wp43','wp44-statuses','wp45','wp20','wp42','wp47-b-switching','wp48','wp49'],
'wp53':['wp36','wp38','wp42','wp59','wp37','wp05','wp06-time','wp09','wp10','wp11','wp12','wp15','wp17-messages','wp19','wp20','wp25','wp27','wp28','wp39','wp60-fishing','wp62'],
'wp60-berry':['wp27','wp59','wp09','wp06-time','wp15','wp13-map'],
'wp61':['wp59','wp30','wp42','wp36','wp33','wp34','wp35','wp23-shadow-hyper','wp37','wp53','wp05','wp06-time','wp09','wp10','wp11','wp12','wp15','wp17-messages','wp19','wp20','wp21','wp25','wp27','wp28','wp31'],
'wp62':['wp18','wp21','wp24','wp03','wp11','wp36','wp26','wp31','wp35','wp38','wp23-shadow-hyper'],
'wp69-voltorb-flip':['wp17-messages','wp24','wp27','wp06-time','wp06-stats'],
'wp70-lottery':['wp17-messages','wp25','wp27','wp06-time','wp06-stats'],
'wp17-draw':['wp17-messages','wp15'],
'wp17-messages':['wp08','wp15','wp13-map','wp02','wp06-time'],
'wp63':['wp24','wp11','wp59','wp36','wp06-time','wp17-messages','wp13-map','wp04','wp08','wp66-a'],
'wp65-controls':['wp17-messages','wp15','wp08','wp16-world'],
'wp65-title':['wp08','wp09','wp10','wp17-messages','wp24','wp13-map','wp15','wp27','wp28','wp59','wp63','wp64','wp66-a','wp66-b','wp66-c','wp23-shadow-hyper','wp25','wp62','wp53'],
'wp65-trainer':['wp24','wp62','wp06-time','wp09','wp15','wp08','wp17-messages'],
'wp66-a':['wp25','wp27','wp28','wp30','wp23-shadow-hyper','wp59','wp62','wp26','wp55','wp17-messages','wp66-b','wp66-c','wp63','wp64'],
'wp66-b':['wp25','wp62','wp17-messages','wp02','wp15'],
'wp66-c':['wp27','wp28','wp29','wp17-messages','wp24'],
'wp67-a':['wp38','wp42','wp40','wp16-world','wp17-messages','wp20','wp25','wp26','wp27','wp28','wp30','wp39','wp41','wp43','wp62','wp66-a','wp66-b','wp66-c','wp65-title','wp23-shadow-hyper','wp56','wp58','wp15'],
'wp67-b':['wp22-mega','wp23-shadow-hyper','wp31','wp32-contextual','wp35','wp26','wp16-world','wp17-messages','wp05','wp06-time','wp09','wp10','wp15','wp18','wp20','wp21','wp24','wp25','wp27','wp28','wp30','wp62','wp65-title','wp66-a','wp66-b','wp67-a'],
'wp68-duel':['wp17-messages','wp24','wp19','wp27'],
'wp69-slot-machine':['wp17-messages','wp24','wp27','wp06-time','wp06-stats','wp69-slot-reels'],
'wp70-mining':['wp17-messages','wp25','wp27','wp06-time','wp70-mining-data'],
'wp71':['wp17-messages','wp06-time','wp15']}
# Explicit main-contract links for data appendices with no dependency heading.
appendix_dependency_decisions={
'wp47-a-attributes':['wp47-a-move','wp43','wp44-statuses','wp45','wp46-damage-multihit'],
'wp47-b-control':['wp47-b-switching','wp40','wp41','wp20','wp42','wp50-held-item-triggers'],
'wp51-ai-decision':['wp51-ai-action','wp52-a-generic','wp52-b-field','wp52-c-items','wp28','wp44-statuses'],
'wp52-a-evaluation':['wp52-a-generic','wp51-ai-action','wp50-held-item-triggers','wp43','wp44-statuses'],
'wp52-b-effect':['wp52-b-field','wp52-a-generic','wp51-ai-action','wp46-damage-multihit','wp49','wp50-held-item-triggers'],
'wp52-c-item':['wp52-c-items','wp52-a-generic','wp52-b-field','wp20','wp27','wp28','wp40','wp41'],
'wp54-entry-rules':['wp54-entry-eligibility','wp25','wp30','wp39','wp44-statuses'],
'wp06-stats':['wp06-time','wp09'],
'wp22-transformation':['wp22-mega','wp21','wp19','wp20'],
'wp23-shadow-data':['wp23-shadow-hyper','wp20','wp30','wp38','wp28'],
'wp32-context-inputs':['wp32-contextual','wp31','wp42','wp38'],
'wp44-effect':['wp44-statuses','wp45','wp47-a-move','wp46-damage-multihit'],
'wp46-damage-healing':['wp46-damage-multihit','wp43','wp47-b-switching'],
'wp50-held-item-effect':['wp50-held-item-triggers','wp20','wp42','wp28'],
'wp69-voltorb-layouts':['wp69-voltorb-flip','wp06-time'],
'wp69-slot-reels':['wp69-slot-machine','wp06-time'],
'wp70-mining-data':['wp70-mining','wp27','wp03'],
'wp13-interpreter':['wp13-map','wp12','wp11','wp09','wp59','wp15'],
'wp13-move-route':['wp13-map','wp12']}
for prefix,targets in {**document_dependency_decisions,**appendix_dependency_decisions}.items():
    d=by_stem[stem(prefix)]
    for f in list(active.values()):
        if f['document_id']!=d['document_id']:continue
        for target in targets:
            dep(f['feature_id'],stem(target),None,
                f'本单元遵循本规范明列的共同前置/直接交界：{stem(target)}；该引用只限定输入、提交或消费者责任，不宣称目标已支持。')

# Feature-specific edges missed by the first candidate. The anchor is a real,
# immutable source heading; direct_refs remain independently auditable from WP names.
specific_dependencies={
11:[('wp27',None,'登记/复检失败/终局退款均写实时背包，必须保留容量与部分提交语义。'),('wp28',None,'消费资格和执行处理器来自主动道具主合同。')],
22:[('wp27',None,'逃离道具的登记扣除和执行失败退款依赖背包主合同。'),('wp42',None,'成功逃离的决定与正常终局/显式中止清理由终局主合同承接。')],
29:[('wp30',None,'每级经验提交后学习/友好度与同步门须使用成长主规则。'),('wp25',None,'参与者/队伍/捕获改变后的集合与索引关系。')],
61:[('wp42',None,'C/I变化在正常终局玩家侧还原，显式中止不保证还原。'),('wp38',None,'捕获满队换出会移动真实队伍并改变还原记录消费者。')],
124:[('wp09',None,'设施暂停/恢复记录随全局元数据保存，内存保留不等同落盘。'),('wp10',None,'会话恢复失败和旧格式迁移不由单场对局推断成功。')],
136:[('wp09',None,'全局记录随存档保存；外部录像文件产出者仍未证明。'),('wp38',None,'回放捕获/收服接收为具名边界，不因设施常规不可达而删除。'),('wp62',None,'捕获接收涉及图鉴记录及简略条目消费者。')],
147:[('wp42',None,'场上副本的HP/异常/PP同步及成长/终局按战斗阶段处理。'),('wp30',None,'持久学习/替换主规则与场上临时槽分开。')],
148:[('wp50-held-item-triggers',None,'持物消费/转移维护C/I/R/P/Belch与持久写穿。'),('wp64',None,'邮件与持物关系的真实给予/取回/信箱流程。')],
155:[('wp39',None,'伙伴登记不等于实际参战，战斗布局与参与者由上下文主合同判定。'),('wp41',None,'伙伴拥有者/队伍切换影响显示映射和换人。')],
157:[('wp10',None,'旧标记转换三个容器位置是迁移条件化消费者。')],
158:[('wp38',None,'捕获入队/满队换出/送盒的接收消费者与存入治疗。'),('wp23-shadow-hyper','8.1','净化室直接放置/删除和选择器可达性不等于正常仓库守卫。')],
186:[('wp38',None,'球类特殊执行与真实接收队列分开。'),('wp50-held-item-triggers',None,'主动恢复/消费背包和被动持物资格/记录严格分开。'),('wp61',None,'Repel再次使用与持久野外状态的消费者。'),('wp60-berry',None,'种植/施肥过滤与库存先后由树果主合同规定。')],
187:[('wp40',None,'战斗登记扣除/执行前复检与退款残留由命令主合同接续。'),('wp42',None,'正常终局退款/物品还原与显式中止不同。'),('wp50-held-item-triggers',None,'LEPPA/恢复资格与主动背包不得互相替代。')],
190:[('wp21',None,'进化/融合等指定入口会读取或改变持久形态和缓存。'),('wp23-shadow-hyper',None,'Shadow/Hyper普通个体用物门及香类旗标例外。')],
191:[('wp23-shadow-hyper','7','三种香的共用与专用许可、Hyper清除和TIMEFLUTE消费无净化。'),('wp40',None,'战斗用物登记与复检/退款沿命令主合同。')],
192:[('wp23-shadow-hyper',None,'Shadow教学/糖果/香与裸赋值不共享统一拒绝门。'),('wp64',None,'给予邮件及写信主合同，不能由普通持物改写推断。')],
204:[('wp42',None,'战斗收益/逐级写入时机和持物/Shadow分流由结果规格给定。'),('wp23-shadow-hyper','6','Shadow经验/EV暂存的阶段及普通分支，与净化恢复不同。')],
207:[('wp42',None,'战斗学习同步时机与升级暂停消费者。'),('wp47-a-move','6.3','模仿/写生的临时/持久槽与后置形态异常。')],
221:[('wp26',None,'蛋的事件接收/昵称/来源与获得主流程交界。'),('wp62',None,'孵化前后图鉴记录与简略条目的消费者。')],
395:[('wp04',None,'schema解析/校验与编译生命周期的实际读取。'),('wp08',None,'名称描述的语言域查询不由原始字段缺省保证。')],
396:[('wp04',None,'双基名与实际发现/编译解析分开。')],
401:[('wp05',None,'启动编译/插件时序与通知扩展共同限制。'),('wp07-diagnostics',None,'解析/编译异常的格式化、日志/控制台失败前缀。')],
413:[('wp07-diagnostics',None,'注册期插件错误打印并终止，依赖诊断输出而非UI正常返回。')],
416:[('wp59','5.3.1','场地统计生产点由场地招式实际成功/失败分支决定。')],
420:[('wp42',None,'战斗统计生产点、决定码与未实际开战分开。'),('wp38',None,'捕获计数在真实捕获/接收分层生产。')],
423:[('wp09',None,'保存/游戏用时字段的持久登记与写盘前缀。'),('wp10',None,'迁移中统计初始化/旧格式转换条件。')],
425:[('wp09',None,'游戏时间/计时字段登记及载入后运行时值边界。'),('wp13-map',None,'解释器等待/更新时间与消息微更新的消费者。'),('wp59',None,'墙钟/时段/世界天气读取的领域消费者。')],
426:[('wp05',None,'统计/计步生产由有序通知机制派发。'),('wp12',None,'零位移完成步/强制路线的实际通知入口。'),('wp09',None,'计步字段持久保存与普通载入。')],
428:[('wp09',None,'地牢区域/版本/待播种子是持久值但重播有全局运行时副作用。'),('wp14',None,'地图建立含临时查询的种子消费和失败前缀。')],
430:[('wp08',None,'弃用告警文本本地化，与输出通道分开。')],
436:[('wp04',None,'本地化提取/编译与PBS写回的触发和失败前缀。'),('wp05',None,'插件和启动加载影响消息集合，但不假设插件实例。'),('wp09',None,'语言选项与持久值/直写边界。'),('wp10',None,'载入/恢复条件下语言状态与失败处理。')],
448:[('wp10',None,'载入版本门与具体旧格式转换由迁移规格承接。')],
449:[('wp05',None,'迁移版本比较器是逐字符比较，不套语义版本习惯。')],
326:[('wp09',None,'地图恢复两分支以存档恢复门及缺图恢复条件为前提。')],
384:[('wp38',None,'钓鱼球倍率/捕获位置由捕获主合同消费。'),('wp39',None,'钓鱼战斗环境/公开开战交界不由鱼竿结果代表。'),('wp42',None,'开战返回布尔/决定码/清理阶段需战斗结果合同。')],
659:[('wp30',None,'完整学习/替换/重学资格及moves_taught_by_reminder统计属于成长主合同。')]}
for n,refs in specific_dependencies.items():
    if fid(n) not in active:continue
    for target,section,why in refs:dep(n,stem(target),section,why)

# Detailed AI edges separate a local scoring strategy from queried true behavior.
ai_edges={76:['wp52-a-generic','wp52-b-field','wp52-c-items'],79:['wp44-statuses'],
88:['wp47-a-move','wp50-held-item-triggers'],89:['wp50-held-item-triggers'],92:['wp47-b-switching'],
93:['wp40','wp41','wp46-damage-multihit','wp47-a-move','wp47-b-switching','wp50-held-item-triggers'],
98:['wp52-a-generic'],99:['wp52-a-generic'],100:['wp52-a-generic'],101:['wp52-a-generic'],102:['wp52-a-generic'],
109:['wp52-a-generic','wp20','wp27','wp28','wp40','wp41','wp52-b-field'],
110:['wp52-a-generic','wp20','wp27','wp28','wp40','wp41','wp52-b-field'],
111:['wp52-a-generic','wp20','wp27','wp28','wp40','wp41','wp52-b-field'],
112:['wp52-a-generic','wp20','wp27','wp28','wp40','wp41','wp52-b-field'],
113:['wp52-a-generic','wp20','wp27','wp28','wp40','wp41','wp52-b-field']}
for n,targets in ai_edges.items():
    for target in targets:dep(n,stem(target),None,'本行评分/失败预测直接读取该主合同的数值、资格或字段；仅作预测不等同执行真实效果，也不证明Showdown已登记同策略。')

plan(75,C,'NPC主动道具策略、业主资源和真实资格登记明确分责；AI上下文不能冒充真实战斗上下文。',
    fw='拥有items/ally_items业主资源及玩家AI控制时的背包消费者；执行本节独立偏好/近似排序，维护异常整段放弃而非略过单件。',
    sd='提供真实通用/CanUseInBattle查询与UseItem选择登记；按归属消费一次资源，效果和退款分别沿WP40/WP28，不能保证AI上下文完成需要选招/真实战斗的查询。',
    protos=['PROTO-BATTLE-ITEM'],refs=[11,177,186,187],
    questions=['验证POTION先入候选后ETHER缺选招索引使整段不登记/不消费的前缀，以及删ETHER才登记一次资源的对照。',
               '对NPC业主列表、ally_items、玩家受AI控制的实际资源身份逐项映射；区分策略评分、资格异常后的自动选招/Mega以及真实效果/退款。'])

# EXPLICIT_DECISIONS_INSERT_HERE

def finalize():
    manifest['features']=list(active.values())
    for d in documents.values():
        d['feature_ids']=[f['feature_id'] for f in manifest['features'] if f['document_id']==d['document_id']]
        d['retired_feature_ids']=[f['feature_id'] for f in manifest['retired_features'] if f['document_id']==d['document_id']]
    # Migrate old references, preserving their historical IDs in a separate field.
    replacement={r['feature_id']:r['replacement_feature_refs'] for r in retirements}
    for f in manifest['features']:
        resolved=[]
        for ref in f['dependencies']['feature_refs']:resolved.extend(replacement.get(ref,[ref]))
        f['dependencies']['feature_refs']=sorted(set(resolved)-{f['feature_id']})
    for meta in manifest['metadata_records']:
        meta['feature_refs']=sorted(set(ref for x in meta['feature_refs'] for ref in replacement.get(x,[x])))
    for c in coverage['sections']:
        oldrefs=c['feature_refs'];retired=[x for x in oldrefs if x in replacement]
        c['retired_feature_refs']=retired
        c['feature_refs']=sorted(set(ref for x in oldrefs for ref in replacement.get(x,[x])))
        owning=[f for f in manifest['features'] if f['source']['document']==c['path'] and
            any(a<=c['line_start']<=b for a,b in f['functional_scope']['line_ranges'])]
        if owning:
            chosen=min(owning,key=lambda f:sum(b-a+1 for a,b in f['functional_scope']['line_ranges']))
            c.update(mapping_kind='behavior-unit',feature_refs=[chosen['feature_id']],metadata_reason=None)
        else:
            c['mapping_kind']='section-metadata'
            c['metadata_refs']=[x['metadata_id'] for x in manifest['metadata_records'] if x['source']['document']==c['path'] and
                 any(a<=c['line_start']<=b for a,b in x['source']['line_ranges'])]
            if c['metadata_refs']:
                c['feature_refs']=sorted(set(ref for m in manifest['metadata_records'] if m['metadata_id'] in c['metadata_refs'] for ref in m['feature_refs']))
                c['metadata_reason']='来源责任、静态验收或证据元数据；旧稳定ID保留在归档中，当前不计独立实现功能。'
    apply_catalog_corrections()
    legacy_keys=['profiles','document_groups','metadata_heading_patterns','section_overrides']
    policy['legacy_initial_policy_snapshot']={'status':'HISTORICAL_D62_ONLY_NOT_A_REBUILD_OR_CLASSIFICATION_AUTHORITY',
        'commit':BASE, **{k:policy.pop(k) for k in legacy_keys}}
    policy['schema_version']='routing-policy.v2'
    policy['classification_method']='EXPLICIT_SOURCE_UNIT_DECISIONS; legacy seeding is not a classification authority'
    policy['revision_authority']={'base_commit':BASE,'review_commit':REVIEW,'decisions':'revisions/r1/revise-data.py'}
    policy['explicit_feature_revisions']=changes
    policy['retirements']=retirements
    policy['new_behavior_units']=new_rows
    write(HERE/'routing-manifest.json',manifest)
    write(HERE/'routing-policy.json',policy)
    write(HERE/'section-coverage.json',coverage)
    resolutions=[]
    retired_ids={x['feature_id'] for x in retirements}
    for key,review in reviews.items():
        resolutions.append({'feature_id':key,'prior_verdict':review['verdict'],'prior_reason':review['reason'],
            'finding_refs':review.get('finding_refs',[]),'author_disposition':
            'ARCHIVED_AS_SOURCE_METADATA' if key in retired_ids else 'REVISED_PENDING_INDEPENDENT_REVIEW' if key in changes else 'RETAINED_PRIOR_SCOPED_JUDGMENT',
            'changes':changes.get(key,[]),'source_identity_preserved':(original[key]['source']==(active[key] if key in active else next(f for f in manifest['retired_features'] if f['feature_id']==key))['source'])})
    unhandled=[x['feature_id'] for x in resolutions if x['prior_verdict']!='PASS' and x['author_disposition']=='RETAINED_PRIOR_SCOPED_JUDGMENT']
    write(HERE/'revisions/r1/feature-resolution.json',{'base_commit':BASE,'review_commit':REVIEW,'rows':resolutions,
        'prior_verdict_counts':dict(collections.Counter(x['prior_verdict'] for x in resolutions)),
        'unhandled_prior_nonpass':unhandled,'state':'AUTHOR_REVISED_NOT_INDEPENDENTLY_ACCEPTED'})
    write(HERE/'revisions/r1/new-and-retired-units.json',{'new_rows':new_rows,'retirements':retirements})
    print(json.dumps({'active_features':len(active),'retired_features':len(retirements),'new_features':len(new_rows),'unhandled_nonpass':unhandled},ensure_ascii=False,indent=2))

def apply_catalog_corrections():
    # Filled below with explicit source-document and named consumer qualifications.
    for c in coverage['sections']:
        path=c['path']
        forbidden=[]
        if path.endswith('/creature-rpg-wp35-36-57-64-68.md'):forbidden=['wp68-duel.md']
        elif path.endswith('/engine-overworld-wp11-15-59-60.md'):forbidden=['wp60-berry-plants.md']
        elif path.endswith('/user-interface-wp17-63-65-66-67-68-69-70-71.md'):forbidden=['wp70-lottery.md']
        if forbidden:
            c['feature_refs']=[x for x in c['feature_refs'] if Path(active[x]['source']['document']).name not in forbidden]
            c['metadata_reason']='静态验收来源，按本目录明确正文及具名后继限定消费者；同WP编号不构成跨子体系消费关系。'
        additions={
            ('engine-overworld-wp11-15-59-60.md',119):[596],
            ('user-interface-wp17-63-65-66-67-68-69-70-71.md',694):[187,11,31,49,554,555,577],
            ('user-interface-wp17-63-65-66-67-68-69-70-71.md',971):[581],
            ('user-interface-wp17-63-65-66-67-68-69-70-71.md',999):[206]}
        extra=additions.get((Path(path).name,c['line_start']),[])
        if extra:
            c['feature_refs']=sorted(set(c['feature_refs']).union(map(fid,extra)))
            c['metadata_reason']='本具名静态向量同时消费界面、规则及持久状态；关联已有主功能与其协作原型，均未执行。'
            section_changes.append({'path':path,'anchor':c['anchor'],'added_feature_refs':list(map(fid,extra))})

if __name__=='__main__':finalize()
