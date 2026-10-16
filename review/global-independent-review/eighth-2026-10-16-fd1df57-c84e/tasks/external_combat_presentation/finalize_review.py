"""Serialize the final bounded review and its still-unreceived interfaces."""
import datetime
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=Path('/workspace/pokemon-essentials-clean-room')
REF=Path('/workspace/pokemon-essentials')
B='fd1df570cad987dc3852a3b958f03916e317f7fe'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
I='30cfed0996003b6ebf4b5c51cc04f31ca9255440'
ROOT='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def get(n): return json.loads((HERE/(n+'.json')).read_text())
def put(n,d): (HERE/(n+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def git(repo,*args):return subprocess.check_output(['git',*args],cwd=repo)
def identity(repo,commit,path):
    data=git(repo,'show',commit+':'+path)
    return dict(repo=str(repo),commit=commit,tree=git(repo,'rev-parse',commit+'^{tree}').decode().strip(),path=path,
                git_blob=git(repo,'rev-parse',commit+':'+path).decode().strip(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),lines=len(data.splitlines()))
def fixed(path):return json.loads(git(SPEC,'show',I+':'+ROOT+'tasks/'+path))

ledger=get('reading-ledger');fw=get('forward-mapping');atoms=get('atomic-assertions')
all_reads=ledger['primary']+ledger['dependency']
by_path={f['path']:f for f in all_reads}
formal67='deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md'
formal74='deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md'
formal15='deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md'
formal16='deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md'
anim='Data/Scripts/011_Battle/004_Scene/008_Battle_Scene_Animations.rb'
base='Data/Scripts/011_Battle/004_Scene/007_Battle_Scene_BaseAnimation.rb'
sceneplay='Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb'
cry='Data/Scripts/010_Data/002_PBS data/009_Species_files.rb'
picture='Data/Scripts/005_Sprites/010_PictureEx.rb'

# Read bounded provider payloads; never upgrade their source FULL_READ to ours.
provider_path=ROOT+'tasks/world_resources_rendering/forward-mapping.json'
provider=fixed('world_resources_rendering/forward-mapping.json')
extra=fixed('ui_full/wrr-extra-reception.json')
earlier=fixed('ui_full/wrr-bounded-reception.json')
selected=[*extra['received_objects'],*[x for x in earlier['received_units'] if x['unit_id'] in {'WRR-D07','WRR-D08','WRR-D09'}]]
for row in selected:
    assert row==next(x for x in provider['units'] if x['unit_id']==row['unit_id'])
provider_identity=identity(SPEC,I,provider_path)
assert provider_identity['bytes']==extra['binding']['bytes'] and provider_identity['sha256']==extra['binding']['sha256']
source_identities=[identity(REF,R,row['source']['path']) for row in selected]
put('bounded-contributions',dict(schema='r8-bounded-contributions/v1',recorded_utc=NOW,
    actual_receiver='this delegated context; platform actual ID UNVERIFIED',provider='/root/world_resources_rendering',
    exact_provider_artifact=provider_identity,selected_units=[x['unit_id'] for x in selected],assertions=sum(len(x['assertions']) for x in selected),
    payloads=selected,source_identities=source_identities,
    verification='All selected complete objects were read in ui_full receipt payloads, then exact-object equality to the frozen original provider artifact and source identities checked. Prior full artifact hash in the earlier receipt is historical; current object equality, not that stale whole-file hash, binds the selected three units.',
    original_receipts=[identity(SPEC,I,ROOT+'tasks/ui_full/wrr-extra-reception.json'),identity(SPEC,I,ROOT+'tasks/ui_full/wrr-bounded-reception.json')],
    scope='Six named units / 66 source-static assertions only. D05/D13 are provider meaning, not own source reading. D07/D08/D28 overlap own fully read primary; D09 overlaps own fully read dependency. Other provider units and whole domains not received.',
    main_reception='PENDING_MAIN_REVIEW',proposal_counterreview='NOT_RECEIVED',business='NOT_EXECUTED'))
assert sum(len(x['assertions']) for x in selected)==66

# The primary readset assigns no formal file. Do not fabricate a census of all
# clauses in other owners' primary documents. The exact necessary interfaces
# below have their own finite reverse denominator.
reverse=get('reverse-mapping')
reverse.update(schema='r8-reverse/v3',atomic_clause_denominator=0,
    primary_formal_denominator_explanation='Frozen combat_presentation.json formal=[]; full WP67-A belongs to ui_full. The 31 legacy groups/150 listed propositions are retained as scoped interface comparisons, not a census or acceptance of every clause in those full documents.',
    legacy_interface_propositions=150,all_semantic_pass=False)
interface_rows=[]
def interface(section,lines,claim,groups,path=formal67,qualification='SOURCE_STATIC; no actual media/host observation; reception pending'):
    interface_rows.append(dict(id=f'EXTCP-IR{len(interface_rows)+1:03}',formal=identity(SPEC,B,path),section=section,range=lines,
        assertion=claim,source_groups=[f'EXTCP-F{i:03}' for i in groups],
        source_assertions=[a['id'] for a in atoms['assertions'] if int(a['group'][-3:]) in groups],
        premise='Fixed B8/R; valid constructed objects; normal local processing unless the clause states an exception.',
        qualification=qualification,reception='PENDING_MAIN_REVIEW'))
interface('3.2',[37,44],'开场和异色公共动画具有不同等待及动画开关门。',[19,51,52,55])
interface('9.3',[256,256],'全部轨道结束后的下一次聚合更新开头才判完成。',[42])
interface('9.3',[256,256],'临时精灵正常结束后销毁，借用成员精灵不在临时销毁集合。',[42,49,50,58])
interface('9.3',[257,257],'训练家淡出、各个体球和数据框同轮推进，各框仅等自己的球。',[20,54,55])
interface('9.3',[258,258],'收回先球后数据框，倒下叫声与下落并行等待框。',[20,23,56,57])
interface('9.3',[259,259],'伤害闪烁和HP补间等待全部完成。',[22,38,56])
interface('9.3',[260,260],'投球阻塞并等待排列队列空。',[23,58])
interface('9.3',[260,260],'挡球单独阻塞。',[23,59])
interface('9.3',[260,260],'成功球保留后由隐藏入口与框退场并行淡出1秒。',[23,58])
interface('9.3',[260,260],'野生成功ME正常等待3.5秒。',[23,65])
interface('9.4',[267,270],'作者数据库的查找、播放器及球公共动画队列不同于固定BallAnimationMixin轨道。',[25,26,27,43,44,45,46,47,48,49,50])
interface('9.4 failure boundary',[269,269],'逐帧坐标/轨迹排除带WP74前向；该前向对固定过程轨道的责任归属需裁决。',sorted({43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59}),qualification='PROPOSED_SCOPE_GAP_GR8_EXTCP_002; not a claim that all coordinates must be specified')
interface('10.2',[321,337],'WP74的20fps、cel及timing合同消费作者动画数据库。',[67,69,71,72,73,74,75],formal74)
interface('10.2a',[338,351],'作者数据库播放器跳帧不补发事件，不能套用PictureEx同刻到期事件处理规则。',[72,75],formal74)
interface('6.3',[297,311],'PictureEx首次实际更新为t0，时间单位为1/20秒请求单位。',[42,43,44,46,48,49,50,51,52,54,55,56,57,58,59],formal16)
interface('6.3',[297,311],'同刻动作按登记顺序处理。',[44,48,54,56,57,58],formal16)
interface('6.3',[297,311],'插值起点由该动作实际处理时捕获，迟到按计划时点进度计算。',[44,46,48,49,50,54,55,56,57,58],formal16)
interface('6.3',[297,311],'轨道各自时钟独立，聚合多一次更新不保证实际固定多0.05秒。',[42,55,58],formal16)
interface('5.1',[110,130],'普通AnimatedBitmap与直接cache、前缀PNG的失败分支不同。',[6,43,45,47,55],formal15)
interface('6.1/6.4',[131,190],'共享SE/cry解析只能支持资源身份与音频请求，不能证明声音已经出现。',[44,49,53,56,57,58,59],formal15)
reverse['selected_interface_atomic_assertions']=len(interface_rows)
reverse['selected_interface_assertions']=interface_rows
reverse['forward_field_reverse_binding']=[dict(artifact=n,formal_section='WP67-A9.3 high-level support;9.4 forward scope/precision open',proposal='GR8-EXTCP-002') for n in atoms['table_artifacts']]
put('reverse-mapping',reverse)

proposal=dict(id='GR8-EXTCP-002',root_key='fixed-battle-picture-request-contract-owner',
    status='PROPOSED_ONLY_COUNTERREVIEW_AND_MAIN_DECISION_PENDING',proposed_priority='P3 coverage/ownership; final severity and required/optional/policy not decided here',
    title='固定战斗呈现静态请求的前向合同归属未闭合',
    source_identities=[identity(REF,R,p) for p in [base,anim,sceneplay,cry,picture]],
    formal_identities=[identity(SPEC,B,p) for p in [formal67,formal74,formal15,formal16]],
    source_ranges=[dict(path=anim,range=[610,657],meaning='完整倒下轨道'),dict(path=cry,range=[183,244],meaning='专用/普通叫声选择及长度除音高'),
                   dict(path=base,range=[65,823],meaning='固定球轨道、两张球种表及消费者'),dict(path=anim,range=[1,849],meaning='固定演出入口；F053已由高层接口另比，不自动新增根因')],
    formal_ranges=[dict(path=formal67,range=[254,270],meaning='9.3高层顺序/等待；9.4失败边界前向WP74'),
                   dict(path=formal74,range=[297,355],meaning='作者数据库timing和播放器，不是固定PictureEx球轨道'),
                   dict(path=formal16,range=[297,311],meaning='通用PictureEx调度，不定义各固定演出的资源/音高/轨迹参数'),
                   dict(path=formal15,range=[131,190],meaning='共享音频解析，不定义倒下75音高分支')],
    finite_premises=['固定B8与R，不引入插件覆盖；单个有效非蛋对手成员与其Scene立绘/影子/数据框已经正常构造。',
                    '展示个体的物种/形态已登记；无_faint专用资源，存在合法普通叫声；假定底层getPlayTime对该资源返回精确1.0秒。',
                    '调用正常倒下入口；无竞争属性写入；轨道得到足够更新；宿主SE/图形调用正常返回。',
                    '静态比较请求与等待算法；资源真实内容、实际播放时长/音质、像素和物理时序没有观察。'],
    minimal_counterexample=dict(input='一个正常倒下成员；只有普通叫声，长度返回1.0秒。',
        steps=['进入BattlerFaint.createProcesses。','专用_faint查询无结果后取普通叫声。','记录SE请求pitch和下落/裁切开始的请求时间。'],
        source_expected='普通叫声SE请求pitch=75；基础等待ceil((1/0.75)*20)=27，再加2，下落/隐藏影子/裁底从单位29开始。',
        current_formal='WP67-A9.3仅叫声＋下落＋框等待；WP74前向没有固定倒下的音高75及按音高调整长度等待规则。',
        difference='正文允许的高层实现不足以区分100音高/固定等待和该静态请求；这是覆盖精度/责任疑点，不是声称正文与R数值矛盾。'),
    normal_controls=[dict(input='同长度1.0秒的_faint专用资源存在',expected='优先专用；默认pitch，ceil(1*20)+2=22单位开始下落。'),
                     dict(input='专用和普通叫声均缺失',expected='不请求物种叫声，默认10+2=12单位开始下落。'),
                     dict(input='不调用倒下入口',expected='此轨道不请求该叫声或裁切。')],
    normal_cancel_failure_exception_partial_commit=dict(normal='轨道完成后成员隐藏且opacity复位255，数据框由独立轨道共同等待；源静态。',
        cancellation='轨道本身无用户取消返回；场景abort是外层清理，不能解释为回滚已提交战斗HP/状态。',
        failure='两种叫声缺失是具名正常分支；资源加载的placeholder/异常依实际类入口，不能一概宣称静默成功。',
        exception='构造/回调/宿主异常无本演出通用ensure恢复保证。正常返回的销毁/复位不覆盖中途异常。',
        partial_commit='倒下展示之前，领域HP与倒下流程可已写；本提案不新增事务或回滚，不保证后续队列/声音完成。'),
    negative_evidence_scope='本人完整读WP67-A/WP74/WP15/WP16及scope-statement；未在这些接合合同中找到固定倒下75音高/等待归属。两张固定球表496字段及16色另列确切源事实，不能据它们直接要求逐字段转录。全库其它正式文件未由本context全部读，不声称全文全局不存在，交主审结合ui_full等primary反证。',
    affected_consumer='Scene pbFaint→BattlerFaint→PictureEx/SE/cry length→scene共同等待；不同于PBAnimationPlayerX作者库。',
    impact='独立实现可能满足笼统叫声/下落叙述，却选100音高或错误等候；前向阅读WP74也无法恢复这个固定轨道分支。',
    minimal_revision_proposal='由主审确定固定轨道的正式归属和保真边界；若属于必需静态行为，在WP67-A9.3或明确接收文档补专用/普通75/缺声三分支及请求等待规则，并收窄9.4前向适用域。精确坐标、粒子tone及随机图形精度可另作明确scope政策，不要求整表逐行翻译。',
    retain_correct_scope='保留已正确的并行等待、聚合多一次更新、球生命周期、HP/EXP与作者播放器20fps/焦点/timing合同；不把素材/宿主未执行当静态源不可读。',
    reads_writes_sync=dict(reads=['展示个体species/form','叫声解析结果与长度','成员实际坐标/高度与canonical位置','PictureEx当前轨道时长'],
        writes=['源行为只登记SE/精灵属性/裁底/影子轨道；报告只写自身目录'],
        sync='数据框与倒下演出共同更新；原游戏数据提交不由本报告改动；跨域所有者最终接收待主审。'),
    acceptance_and_regressions=['静态独立复读固定R三个叫声分支，确认pitch和22/29/12三个请求单位；禁止把静态推导写成执行。',
        '复核getPlayTime=1.0秒是有限前提，非现存音频已测；不同音高长度按实际helper公式。',
        '对照已有9.3多轨共同等待和WP16首次实际处理语义，不能把请求单位保证成真实墙钟时刻。',
        '保留场景abort/资源缺失/中途异常的边界；不增加数据回滚承诺。',
        '独立检查其它正式文件/历史范围政策是否已经接收固定轨道；有明确排除则按scope政策反证此候选，不伪造required。'],
    historical_relation='未继承旧PASS；H001前景opacity误读已撤回且无关联。GR8-EXTCP-001不复用于新根因。早期16组粒度未决现由事实表和此有界候选接合。',
    actual_independent_nonproposer='NOT_RECEIVED',main_adjudication='NOT_RECEIVED',required_update=False,
    business_executions=0,evidence='SOURCE_STATIC / FORMAL_TEXT / FINITE_HYPOTHETICAL_REQUEST_VECTOR; NOT_EXECUTED')
proposals=get('proposals');proposals.update(schema='r8-proposals/v3',submitted_candidates=1,required_updates=0,records=[proposal])
proposals['reserved_ids']={'GR8-EXTCP-001':'Reserved by withdrawn opacity preparation; not reused.','GR8-EXTCP-H001':'Withdrawn same-proposer hypothesis; no independent reception.'}
put('proposals',proposals)

# Every discovery-pool row gets a responsibility reason. Unread stays unread.
coverage=get('coverage-and-gaps')
def owner_scope(path,side):
    if '/005_AI/' in path or '/006_AI MoveEffects/' in path or '/wp51-' in path or '/wp52-' in path:
        return 'com_ai','AI选择/评分正文；本域只消费已作出的选择，不审算法或训练家/PBS全体。'
    if '/003_Move/' in path or '/wp43-' in path or '/wp44-' in path or '/wp46-' in path or '/wp47-' in path:
        return 'com_move/creature domain','招式/伤害/效果内部语义；本域审展示调用/返回协议，具体资格/结果为具名前提，交对应primary接合。'
    if '/002_Battler/' in path or 'AbilityEffects' in path or 'ItemEffects' in path or '/wp48-' in path or '/wp49-' in path or '/wp50-' in path:
        return 'combat battler/ability/item owners','场上规则内部；必要HP/PP/显示对象/邻近receiver已作有限实读，其余不由Scene消费者授全域批准。'
    if '/018_Alternate battle modes/' in path or '/wp54-' in path or '/wp55-' in path:
        return 'com_facility','设施会话/生成/报名规则；本域已读实际替代Battle场景和模拟入口，不扩大到全部设施规则。'
    if '/007_Objects and windows/' in path or '/wp17-draw-text-tags' in path:
        return 'ui_full/world_resources_rendering','共享窗口/排版/资源；本域必要busy/resume、PictureEx、IconSprite/AnimatedBitmap/cache实读；其余呈现/字体/标签合同由primary接合。'
    if '/017_Minigames/' in path or '/wp68-' in path or '/wp69-' in path or '/wp70-' in path or '/wp71-' in path:
        return 'ui_minigames','其它游戏的规则及界面；固定战斗Scene未直接调用这些正文。'
    if '/016_UI/' in path or '/user-interface/' in path:
        return 'ui_full/ui_wp66','其它UI或共享界面全文；战斗直接进入的队伍/摘要/背包/命名/图鉴有限区间已读，剩余全文不在本域primary。'
    if '/test-catalog/' in path:
        return 'corresponding formal primary','其它域测试目录；本域UI/DX必要目录已整读，其余向量由各primary和主审接合，不授全局测试通过。'
    return 'combat_review','非呈现核心域全文；本域实际入口与必要协议已实读，剩余规则内部/全局接收留主审。'
for f in coverage['files']:
    read=by_path.get(f['path'])
    if read: f['read_status']=read['semantic_status']
    owner,reason=owner_scope(f['path'],f['side'])
    primary=any(x['path']==f['path'] for x in ledger['primary'])
    f.update(scope='PRIMARY' if primary else 'DISCOVERY_POOL_NOT_AUTOMATIC_PRIMARY',
             primary_owner='external_combat_presentation' if primary else owner,
             necessity_status='OWN_PRIMARY_FULL_READ' if primary else ('NECESSARY_READ_UNIT_SATISFIED_OR_ADDITIONAL_CONTEXT' if read else 'OTHER_PRIMARY_BODY_NOT_OWN_READING'),
             scope_reason='冻结primary全文逐结构审读。' if primary else reason,
             not_a_limit=True,reception='PENDING_MAIN_REVIEW')
counts={}
for side in ['reference','formal']:
    rows=[f for f in coverage['files'] if f['side']==side]
    statuses=Counter(f['read_status'] for f in rows)
    counts[side]=dict(files=len(rows),full_read=statuses['FULL_READ'],partial_read=statuses['PARTIAL_READ_NECESSARY_METHODS'],unread_available=statuses['UNREAD_AVAILABLE'],unreceived=len(rows))
def gaps(intervals,total):
    seen=set()
    for a,b in intervals:seen.update(range(a,b+1))
    missing=sorted(set(range(1,total+1))-seen)
    result=[]
    for n in missing:
        if result and result[-1][1]+1==n:result[-1][1]=n
        else:result.append([n,n])
    return result
partial=[dict(path=f['path'],commit=f['commit'],read_intervals=f['read_intervals'],unread_intervals=gaps(f['read_intervals'],f['lines']),
              reason='Exact complete necessary methods were read; the rest is available outside own finite body. No whole-file approval.',
              main_reception='PENDING_MAIN_REVIEW') for f in ledger['dependency'] if f['semantic_status'].startswith('PARTIAL')]
coverage.update(schema='r8-external-denominators/v2',discovery_pool=counts,partial_file_gaps=partial,
    mapping_gaps=[],primary_atomic_assertions=atoms['atomic_assertion_denominator'],
    primary_unmapped_assertions=0,primary_unreceived_assertions=atoms['atomic_assertion_denominator'],
    primary_formal_files=0,primary_formal_atomic_clauses=0,
    selected_reverse_interface_assertions=len(interface_rows),legacy_interface_groups=31,legacy_interface_propositions=150,
    reading_denominator_scope='Primary12 source files; dependencies are necessary units and additional read context. Discovery157R/60F retained for transparency, not auto-assigned whole-body work.',
    claim='Own source mapping complete within its declared finite proposition denominator. Candidate classification and cross-domain/final receptions pending; no global PASS.',
    continuation_additional_paths=[x['path'] for x in ledger['dependency'] if 'continuation_recorded_utc' in x],
    remaining_semantic_decisions=['GR8-EXTCP-002 independent counterreview and main scope/required/optional decision',
        'All own primary assertions and 20 selected formal interfaces await main reception',
        'Other primary bodies/history/admin/global synthesis not accepted by this context'],
    global_administrative_read_gap='Whole global history/admin not own delegated primary; prior full global prompt/skill/AGENTS read. Global owner must join current reports/history; no inherited approval.')
put('coverage-and-gaps',coverage)

interfaces=get('interfaces')
interfaces['bounded_provider_contributions']='bounded-contributions.json: six named units /66 assertions; no whole-source promotion'
interfaces['continuation_interfaces']=[dict(id='IF09',edge='Fixed PictureEx tracks → SE/cry duration/shared scheduler',
    source_groups=[f'EXTCP-F{i:03}' for i in [42,43,44,46,48,49,50,51,52,54,55,56,57,58,59]],
    read_units=['PictureEx whole548','Species_files183–244 complete cry methods','IconSprite/AnimatedBitmap/cache whole files',
                'WP15/16 whole formal files','WP67-A/WP74 whole formal files'],
    actual='Static resource/property/SE requests and shared interpolation semantics mapped; no media/host execution',
    gap='GR8-EXTCP-002 formal ownership/precision policy only; exact source data already read and recorded',reception='PENDING_MAIN_REVIEW'),
    dict(id='IF10',edge='Scene target/PP/HP → actual receiver',read_units=['Battle001 whole867 including nearBattlers553–577',
        'ActionAttacksPriority1–173, complete target receiver through132','Battler00195–220/680–724',
        'ChangeSelf1–160 including realMove PP association','Move0011–135'],
        actual='Battle.nearBattlers? does not normalize an object; Battler.near? does, but is not this caller. HP setter writes persistent HP before presentation; PP follows original move object.',
        receiver_rule_internals='Combat owner eligibility/target outcomes remain explicit input premises; no all-combat reception',reception='PENDING_MAIN_REVIEW')]
interfaces['independent_receiver_receptions']=[]
interfaces['missing_receptions']=['Main reception of own1045 source assertions and20 selected reverse interfaces',
    'Actual different nonproposer counterreview of GR8-EXTCP-002',
    'Global primary-domain/history/material/host joins beyond six received provider units']
put('interfaces',interfaces)

full=Counter('reference' if f['repo']==str(REF) else 'formal' for f in all_reads if f['semantic_status']=='FULL_READ')
part=Counter('reference' if f['repo']==str(REF) else 'formal' for f in all_reads if f['semantic_status'].startswith('PARTIAL'))
progress=get('progress')
progress.update(state='OWN_PRIMARY_CONTENT_REVIEW_COMPLETE_RECEPTIONS_PENDING',updated_utc=NOW,ended_utc=NOW,
    content_recording_end_utc=NOW,content_review_complete=True,submitted_candidates=1,required_updates=0,
    formal_clause_status='PRIMARY_FORMAL_ZERO;20_SELECTED_INTERFACE_ATOMS_AND150_LEGACY_PROPOSITIONS_RECEPTION_PENDING',
    primary_atomic_assertions=atoms['atomic_assertion_denominator'],primary_unmapped_assertions=0,
    discovery_pool_denominators=counts,dependency_read_files=len(ledger['dependency']),
    dependency_full_read_files=sum(x['semantic_status']=='FULL_READ' for x in ledger['dependency']),
    dependency_partial_read_files=sum(x['semantic_status'].startswith('PARTIAL') for x in ledger['dependency']),
    all_own_read_files=len(all_reads),own_full_read=full,own_partial_read=part,
    received_bounded_contributions=dict(units=6,assertions=66,source_full_read_credit=0),
    publication_status='CONTENT_READY_FOR_AUTHORIZED_SAME_BRANCH_PUSH_AND_FULL_REMOTE_READBACK',
    blockers=[],semantic_acceptance='NOT_RECEIVED',update_status='UPDATE_NOT_STARTED')
put('progress',progress)

incidents=get('validation-incidents')
incidents['continuation_corrections']=[
 dict(issue='Draft table-size formula was maintained with explicit logical fields and scalar leaves, not inferred semantic PASS.',resolution='16*14=224 and16*17=272 fields, plus16 RGB values; scalar leaves1200+48. Counts checked after complete table/consumer read.'),
 dict(issue='Local unpublished continuation draft incorrectly added opponent opening +10 to player sendout.',resolution='R player method reread381–460; player base=trajectory total+4+10order only. Opponent retains opening+10. Corrected before commit.'),
 dict(issue='Local unpublished draft named catch-click SE incorrectly and put jump-to-ball SE at absorption finish.',resolution='R base726–762 and animation658–813 reread; exact Battle catch click and absorption-start Battle jump to ball recorded.'),
 dict(issue='Initial continuation shorthand omitted integer division in trainer horizontal motion.',resolution='Recorded floor(W/32) before multiplying; did not impose an unobserved host rounding rule.')]
put('validation-incidents',incidents)

checkpoint=get('checkpoint')
checkpoint.update(state='SUPERSEDED_BY_COMPLETE_OWN_PRIMARY_MAPPING',updated_utc=NOW,
    primary_structures=79,primary_atomic_assertions=atoms['atomic_assertion_denominator'],
    unmapped_primary_assertions=0,content_complete=True,submitted_candidates=1,
    candidate_status='ONE_PROPOSED_CANDIDATE_GR8_EXTCP_002',
    remaining=['Independent nonproposer counterreview and main adjudication of GR8-EXTCP-002', 'Main reception of own primary facts and selected interfaces', 'Other primary/history/global joins; actual host/media execution not done'],
    current_evidence='atomic-assertions.json; ball-color-fields.json; release/capture-variance-fields.json; bounded-contributions.json',
    scope='Earlier publication remains history; current finite source mapping completed. No global or independent acceptance.')
put('checkpoint',checkpoint)

review=f'''# 第八轮 external_combat_presentation 独立审查

本域固定源读集与映射已完成：12/12 文件、6003 行、233236 bytes、79 个连续结构组；源未读0，具名断言未映射0。源事实分母为 **1045**：533条人工具名语义断言、496个球种差异逻辑字段、16个球色RGB字段。两类表另有1248个标量叶值，不和1045重复相加。逐字段事实、前提、消费者、正式接合及处置分别见 `atomic-assertions.json`、三份 `*-fields.json` 与 `forward-mapping.json`。数量本身不授语义PASS。

固定输入为委派提交 `{I}`，规格B8 `{B}`，参考R `{R}`。完整global prompt、skill和AGENTS已读；请求配置与实际配置分列。实际平台模型/effort/tier/Fast/会话ID均无可信回显，逐字段UNVERIFIED；源thread ID不是实际审者平台ID。当前正文使用指定最终态技能；审计撤回与修正历史保留。

16个曾粒度未决组已全部再次实读并映射，包括两个16球种表的每个资源/tone字段、训练家手位、释放/吸入/成功/收回、开场、排列、淡出、双方派出、伤害/倒下、捕获/挡球。CHERISH射线表值被专用色循环绕过、NEST下粒子显示同刻再隐藏、DUSK释放下glare未登记放大均具名登记。玩家派出没有对手专有的开场额外10单位；捕获吸入音在起点请求。这些均为源静态请求，不是像素或声音观察。

冻结primary正式文件分母为0（readset `formal=[]`）；不能把ui_full负责的WP67-A全篇原子分母转成本人主责。本人完整读相关正式文本，并保留31组/150个旧具名接口命题及新增20个精确反向接口断言。它们与源事实/字段互相绑定；这些数不冒充所有共享正文条款普查。主审应接合ui_full等primary的全篇贡献。

本人读集共{len(all_reads)}个文件身份：参考全文{full['reference']}、参考partial{part['reference']}、正式全文{full['formal']}；其中额外依赖{len(ledger['dependency'])}（全文{sum(x['semantic_status']=='FULL_READ' for x in ledger['dependency'])}、partial{len(partial)}）。每个partial可得未读区间保留在coverage文件，不改成limit。发现池仍157R/60F，其真实读/未读分布见 `coverage-and-gaps.json`，逐路径列明对应primary及本域边界；它不是自动新增全量主责。必要目标receiver、HP/PP对象关联、cry选择/长度、PictureEx、IconSprite/AnimatedBitmap/cache已作有限实读。另完整读取并核验资源primary的6个具名单元/66条有限事实贡献（`bounded-contributions.json`）；未把provider全文阅读计成本人已读。

提交疑似提案 **GR8-EXTCP-002** 一条：固定战斗过程轨道的正式归属及精度边界。最小有限例为无专用倒下叫声、普通叫声长度假定1秒：源请求75音高并在ceil(1/0.75*20)+2=29单位后开始下落；专用1秒为22，无两种叫声为12。WP67-A只写高层叫声/下落/等待，WP74前向承接作者库而非这些固定轨道。提案不要求逐帧或整表转录，由主审独立反证并裁定required/optional/scope政策。required已接收数0；独立非提案者反证未收到。此前H001前景opacity误读仍撤回，原值来自前景自身，未产生整改。

本人1045条源断言、79组和20条新增反向接口均尚未获主审最终接收；全局其它primary、历史及行政接合没有被本报告冒充接受。跨域规则内部以具名协议与有限前提接合，不由单个Scene消费者推全战斗通过。源材料可得未读与执行限制分开。

行为执行为0：参考/独立模型/全宿主/原生媒体/存档回放全部 **NOT_EXECUTED**。Ruby不可用的实际探测exit127保留；未安装软件。实际声音、像素、字体、墙钟、物理输入均UNVERIFIED。原先读取的平台stdout未全部落本地，其原始I/O完整性仍UNVERIFIED；现有工具输出不能补造早期日志。机械验证仅核身份、计数、映射/区间及写集，不能替代实读或行为测试。

唯一写集为本目录，唯一分支 `codex/r8-external-combat-presentation-20261016`。只提交和普通推送报告证据；main/tag/正式规格/R/公共台账/他人目录无改动。提交和完整远端回读结果由后继 `publication.json` 绑定实际语义核心commit，避免自哈希循环。**UPDATE_NOT_STARTED**；没有整改，没有自封最终全局PASS。
'''
(HERE/'review.md').write_text(review)
print(json.dumps(dict(own_files=len(all_reads),full=full,partial=part,primary_atoms=atoms['atomic_assertion_denominator'],reverse_interface_atoms=len(interface_rows),provider_assertions=66,discovery=counts),ensure_ascii=False))
