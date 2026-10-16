"""Serialize the completed bounded human review. No reference/recovered code execution."""
import collections
import json
import pathlib
from audit_inputs import OUT, TASK, REPO, RREPO, READSET, D, REC, CONTRACT, B8, R, TARGET, ident, put

DEC = json.loads((OUT / 'decisions.json').read_text())
BASE = D['source_groups'][0]['reference']['path']
ANIM = 'Data/Scripts/011_Battle/004_Scene/008_Battle_Scene_Animations.rb'
SCENE = 'Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb'
PIC = 'Data/Scripts/005_Sprites/010_PictureEx.rb'
WP67 = 'deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md'
WP16 = 'deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md'
WP15 = 'deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md'
WP74 = 'deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md'

# The reasons were written individually after all 106 assertions and complete definitions were read.
manual = []
typed = []
for o in D['primary_objects']:
    row = {'id': o['id'], 'population': o['population'], 'group': o['group'],
           'original_object_pointer': '/primary_objects/' + str(D['primary_objects'].index(o)),
           'origin_file': o['origin_file'], 'origin_pointer': o['origin_pointer'],
           'source_identity': o['source'], 'source_range': o['source_range'],
           'evidence_level': 'SOURCE_STATIC_NOT_EXECUTED',
           'formal': DEC['groups'][o['group']]['formal'],
           'formal_value_coverage': 'SUPPORTED_AGGREGATE' if o['group'] == 'EXTCP-F042' else 'PRECISION_AND_OWNERSHIP_ROOT_ADJUDICATION_OPEN'}
    qs = [q['id'] for q in DEC['qualifications'] if o['id'] in q['objects']]
    row['mandatory_qualifications'] = qs
    row['receipt'] = 'RECEIVED_WITH_MANDATORY_QUALIFICATION' if qs else 'RECEIVED_SOURCE_FACT'
    if o['population'] == 'manual':
        n = int(o['id'].split('.A')[1]) - 1
        reason = DEC['groups'][o['group']]['object_reasons'][n]
        row['original_assertion'] = o['meaning']['assertion']
        row['received_meaning'] = reason
        row['verification_reason'] = {'complete_definition': DEC['groups'][o['group']]['complete_source_range'],
                                      'specific_result': reason, 'consumer': DEC['groups'][o['group']]['consumer']}
        row['read_output'] = {'claims': '6fea78', 'source': {
            'EXTCP-F042':'63c846','EXTCP-F043':'63c846','EXTCP-F044':'63c846',
            'EXTCP-F045':'b900d2','EXTCP-F046':'b900d2','EXTCP-F047':'e5a6ae',
            'EXTCP-F048':'e5a6ae','EXTCP-F049':'9f7b76','EXTCP-F050':'9f7b76'}[o['group']]}
        manual.append(row)
    elif o['population'] == 'RGB_field':
        value = o['meaning']['rgb']
        row['ball'] = o['ball']
        row['received_meaning'] = {'rgb': value, 'alpha': '调用者另设，不能从该RGB记录推出alpha',
            'selection': '显式球种匹配' if o['ball'] != 'DEFAULT' else '未显式匹配的全部球种，包括普通/SPORT/Apricorn等'}
        row['consumer'] = {'path': ANIM, 'lines': [407,482,544,791],
            'meaning': '双方派出及失败爆出alpha255，收回先alpha0；出现/吸入helper再改变传入color的alpha。捕获吸入本身不调用普通变色吸入helper。'}
        row['verification_reason'] = '逐值读到RGB ' + str(value) + '，与源case/默认行完全匹配；不是球图资源ID或tone偏移，未知球图文件不随色表归一。'
        row['read_output'] = {'values':'cf6a06','source':'63c846','consumers':['f9e4a0','29bce5']}
        typed.append(row)
    else:
        m = o['meaning']
        field = m['field']
        idx = m['index']
        row.update(ball=o['ball'], field=field, index=idx, value=m['value'], scalar_leaves=m['scalar_leaves'])
        part, phase = field.split('.')
        if o['population'] == 'release_field':
            resources = {'upper_particle':432,'lower_particle':431,'upper_glare':367,'lower_glare':366}
            starts = {'ray':409,'upper_particle':436,'lower_particle':436,'upper_glare':371,'lower_glare':371}
            ends = {'ray':424,'upper_particle':449,'lower_particle':449,'upper_glare':375,'lower_glare':375}
            line = resources[part] if phase == 'resource' else starts[part] if phase == 'start_tone' else ends[part]
            gate = 'CHERISH射线专用色循环旁路本字段' if o['ball'] == 'CHERISHBALL' and part == 'ray' else '真实释放调用者到达；资源/正常更新为有限前提'
            if phase == 'resource':
                effect = '选择Graphics/Battle animations/ballBurst_后接本资源；粒子资源ring2会使对应初缩放减半，glare资源还选择对应缩放分支。'
            elif part == 'ray':
                effect = '非CHERISH初tone在0设置，末tone在该射线开始+8起5单位变化；CHERISH不访问这两个索引。'
            elif 'glare' in part:
                effect = '对应上下glare初tone在0设置，末tone从burst delay+11起4单位变化；DUSK下glare仍保持zoom0。'
            else:
                effect = '对应上下粒子初tone在0设置，末tone从每对错峰起点+7起4单位变化；同对上下共用半径及角。'
            row['read_output'] = {'values':'cf6a06','source_and_consumer':'b900d2'}
        else:
            resources = {'upper_glare':580,'middle_glare':579,'lower_glare':578,'upper_particle':626,'lower_particle':625}
            starts = {'upper_glare':584,'middle_glare':584,'lower_glare':584,'upper_particle':630,'lower_particle':630,'ring':714}
            ends = {'upper_glare':601,'middle_glare':601,'lower_glare':601,'upper_particle':684,'lower_particle':684,'ring':719}
            line = resources[part] if phase == 'resource' else starts[part] if phase == 'start_tone' else ends[part]
            gate = 'NEST下回转粒子仍构造/取值，delay处先显示再隐藏；不能授可见像素' if o['ball'] == 'NESTBALL' and part == 'lower_particle' else '真实捕获吸入调用者到达；不等同捕获成功'
            if phase == 'resource':
                effect = '选择对应ballBurst_资源；回转粒子的资源名继续决定前5单位缩放与+6起3单位缩小目标，MASTER/DIVE下粒子优先分支保留。'
            elif 'glare' in part:
                effect = '三glare按上/中/下各自使用本起终tone；初tone在0设置，10单位至末tone，+10隐藏。'
            elif part == 'ring':
                effect = '尾环初tone在0设置，+10起5单位至末tone；+8先缩放、+10显示、+15隐藏。'
            else:
                effect = '对应回转粒子初tone在0设置，+3起4单位至末tone；NEST隐藏仍会消费资源和tone，PREMIER旋转/DIVE上透明度门保持。'
            row['read_output'] = {'values':'721e76','source_and_consumer':'e5a6ae'}
        row['received_meaning'] = {'ball_identity':o['ball'],'component':part,'phase':phase,'exact_value':m['value'],
                                   'effect':effect,'gate':gate}
        row['consumer'] = {'path':BASE,'source_line':line,'complete_range':m['consumer_range']}
        row['verification_reason'] = '字段' + str(idx) + '的完整原值' + json.dumps(m['value'],ensure_ascii=False) + '与源行和实际索引接合一致；' + gate + '；' + effect
        typed.append(row)

rows = manual + typed
assert len(rows) == 618 and len({x['id'] for x in rows}) == 618
assert {x['id'] for x in rows} == {x['id'] for x in D['primary_objects']}
assert len(manual) == sum(len(g['object_reasons']) for g in DEC['groups'].values()) == 106
ledger = {'schema':'r8-cp02-reception/v1','status':DEC['status'],
          'contract_commit':CONTRACT,'source_target_commit':TARGET,'fixed_B8':B8,'fixed_R':R,
          'actual_reader':'独立委派02_ball_base_fields本会话；非原作者、非父接收者；平台opaque ID无回显',
          'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default normal','Fast':'off'},
          'actual':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','opaque_id']},
          'no_spawn':True,'existing_identity_reused':True,'new_votes':0,'root_final_credit':0,
          'denominator':dict(collections.Counter(x['population'] for x in rows)),
          'source_fact_receipts':618,'formal_value_coverage_is_not_618':True,
          'objects':rows,'qualifications':DEC['qualifications'],'remaining':DEC['remaining'],
          'classification':DEC['classification'],'UPDATE_NOT_STARTED':True}
put('reception-ledger.json',ledger)

# Each selected interface receives its own finite producer/consumer reasoning.
ir = {
 'EXTCP-IR002':('SUPPORTED','Base1–64 update完整；每条running先令finished假，再update；scene循环读取animDone。WP67-A256及WP16 311准确。',[BASE,SCENE,PIC]),
 'EXTCP-IR003':('SUPPORTED','Base临时集合只含自建精灵；成功捕获dispose把球移至captureBall并将临时槽置nil，正常尾部super只清其它临时精灵；借用成员未入集合。',[BASE,ANIM,SCENE]),
 'EXTCP-IR011':('SUPPORTED_WITH_OWNERSHIP_BOUNDARY','固定球直接排PictureEx；另一路pbCommonAnimation/pbBallBurstCommonAnimation查询作者数据库并构造PBAnimationPlayerX。后者入队，前者固定球调用等待；不能相互授完整参数覆盖。',[BASE,SCENE,'Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb','Data/Scripts/011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb']),
 'EXTCP-IR012':('ROOT_PRECISION_ADJUDICATION_OPEN','9.4失败与不转录条款完整读取；WP74§1/§2/§9/§10不提供固定球表/轨迹合同。最强NO_REQUIRED为高层scope明确；仍需主审选择保真边界，不能靠本字段表提出新必修。',[BASE,ANIM,SCENE]),
 'EXTCP-IR015':('SUPPORTED','PictureEx首次update建立timer_start；到期frame按elapsed*20取整。与PngAnimatedBitmap创建起钟或数据库播放器start起钟分开。',[PIC,BASE]),
 'EXTCP-IR016':('SUPPORTED','PictureEx按数组登记顺序逐项处理，初值当项首次执行时读取。NEST true后false、球角末端0均用此顺序，不当成同快照并发。',[PIC,BASE]),
 'EXTCP-IR017':('SUPPORTED_WITH_FINITE_PREMISES','线性动作首次处理捕获当前起点，相对动作再确定终点，lerp仍用原t0+delay；duration<=0即终值。回调在移除之前，异常可留已赋前缀。',[PIC,'Data/Scripts/001_Technical/002_RubyUtilities.rb',BASE]),
 'EXTCP-IR018':('SUPPORTED','每张PictureEx各自timer_start；Base完成观察在update开头，对显示帧率没有额外固定.05秒保证。多个对象构造/首次更新时刻可不同。',[PIC,BASE,SCENE]),
 'EXTCP-IR019':('SUPPORTED_WITH_ENTRY_BOUNDARY','球临时图经IconSprite→AnimatedBitmap→普通Gif包装，普通缓存加载异常可转32×32；直接cache非空无捕获；数字前缀PNG另校验且无同一rescue。未知球图不会自动取普通球图。',[BASE,'Data/Scripts/007_Objects and windows/007_BitmapSprite.rb','Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb','Data/Scripts/007_Objects and windows/001_RPG_Cache.rb']),
 'EXTCP-IR020':('SUPPORTED_REQUEST_ONLY','PictureEx到期SE交pbSEPlay；系统存在时检查音效资源并按选项缩放再交Audio。成员默认intro再调Pokemon/Species叫声；缺声可无请求，pitch/长度是请求估计，未观察实际声响。',[PIC,BASE,'Data/Scripts/008_Audio/002_Audio_Play.rb','Data/Scripts/004_Game classes/002_Game_System.rb','Data/Scripts/010_Data/002_PBS data/009_Species_files.rb'])
}
r019 = [
 ('EXTCP-R019.1','SUPPORTED','pbSendOutBattlers93–156同一loop推进fade与各球；对应球done后才推进自己的框；队列空且全部框done才离开。',[[93,156]]),
 ('EXTCP-R019.2','SUPPORTED','pbRecall161–179先等待完整recall并dispose，再构造并等待框消失。',[[161,179]]),
 ('EXTCP-R019.3','SUPPORTED','Show/Hide184–209各自循环等待；存在提示条先Hide再Show，USE_ABILITY_SPLASH门独立。',[[184,209]]),
 ('EXTCP-R019.4','SUPPORTED','pbFaint313–326共同推进faint与框；BattlerFaint613–657按高度裁切并叫声；三种cry分支不由高层条款直接恢复逐值。',[[313,326]]),
 ('EXTCP-R019.5','SUPPORTED','投球331–342等固定演出及队列空；成功dispose保留球；Hide356–371框和球淡出并行，球没有在此dispose。',[[331,342],[356,371]]),
 ('EXTCP-R019.6','SUPPORTED_NORMAL_RETURN_ONLY','pbSaveShadows390–405在yield前保存所有存在影子并隐藏，正常返回后恢复；pbAnimation包裹它、普通Common不包；无ensure。',[[390,405],[492,519]])
]
interfaces = {'schema':'r8-cp02-interfaces/v1','scope':'所给R019六子断言与10个selected IR；其余150/20全局分母不转入02',
 'reverse_group':D['reverse_current_contribution_objects'][0],
 'reverse_receipts':[{'id':i,'status':s,'producer_join':why,'scene_ranges':spans,'independent_current_read':True} for i,s,why,spans in r019],
 'selected_reverse_interfaces':[dict(original=x,status=ir[x['id']][0],producer_consumer_join=ir[x['id']][1],actual_read_paths=ir[x['id']][2],
                                  inherited_source_assertion_ids_are_locators_only=True) for x in D['selected_reverse_interfaces']],
 'source_assertion_binding_disposition':'保留完整原source_assertions ID集；只对本组618及本文件逐事实必要定义签收，不按数组扩签其它任务的主对象。',
 'provider_supplement':'full_battler_supplement八条原事实及后继限定全文读；RX-HANDLER/RX-ITEM/RX-ILLUSION更正不可丢。02没有从它们继承整个Battler/handler主责信用。',
 'candidate':DEC['candidate_assessment'],'remaining_necessary_units':[], 'execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
put('interfaces.json',interfaces)

spans = [
 (BASE,[[1,823]],'FULL_READ','63c846/b900d2/e5a6ae/9f7b76','九主组全部定义、表、消费者连续读，未以旧source-checked680授信用。'),
 (ANIM,[[1,849]],'FULL_READ_NECESSARY_CALLER_CONTEXT','5020f1/f9e4a0/29bce5','全部固定调用者上下文；不计130个03主对象正式接收。'),
 (PIC,[[1,548]],'FULL_READ','9f7b76/e74109','全部参数/默认/插值/应用接合；不执行参考代码。'),
 (SCENE,[[1,179],[184,209],[313,384],[390,405],[492,579]],'COMPLETE_NECESSARY_UNITS','30e132/58cc14/443c5d/57ed8e','派出/召回/提示条/倒下/投球/留球/影子包装/作者播放接点；区间外不签。'),
 ('Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb',[[79,149],[365,372]],'COMPLETE_NECESSARY_UNITS','443c5d/7e087c','scene graphics/input/frame/队列及正常结束清理；其余场景非本组。'),
 ('Data/Scripts/011_Battle/004_Scene/006_Battle_Scene_Objects.rb',[[511,607]],'COMPLETE_NECESSARY_UNITS','382e4d','BattlerSprite定义前部、个体身份、位图与默认intro完整；未将后续update前缀当完整方法。'),
 ('Data/Scripts/011_Battle/008_Other battle types/001_SafariBattle.rb',[[1,214]],'COMPLETE_NECESSARY_UNITS','9eca5f','FakeBattler/专框作为上下文及完整ThrowBait/ThrowRock，后续SafariScene/规则不签。'),
 ('Data/Scripts/007_Objects and windows/001_RPG_Cache.rb',[[1,144]],'FULL_READ','075cc8','直接缓存加载/普通异常传播与共享位图。'),
 ('Data/Scripts/007_Objects and windows/007_BitmapSprite.rb',[[1,243]],'FULL_READ','075cc8','IconSprite名字、先清旧位图、加载新资源、源区保留和update。'),
 ('Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb',[[1,228]],'FULL_READ','57ed8e','nil/数字前缀PNG/普通Gif的不同失败与时钟。'),
 ('Data/Scripts/001_Technical/002_RubyUtilities.rb',[[390,406]],'COMPLETE_NECESSARY_UNITS','9eca5f','nil_or_empty与lerp完整，零时长及起止clamp。'),
 ('Data/Scripts/010_Data/002_PBS data/009_Species_files.rb',[[183,246]],'COMPLETE_NECESSARY_UNITS','9eca5f','叫声选择/播放/时长完整。suffix选择无自动普通回退，长度helper可回退。'),
 ('Data/Scripts/014_Pokemon/001_Pokemon.rb',[[99,105]],'COMPLETE_NECESSARY_UNITS','57ed8e','个体和物种play_cry完整包装；不授个体全域信用。'),
 ('Data/Scripts/008_Audio/002_Audio_Play.rb',[[2,39],[202,219]],'COMPLETE_NECESSARY_UNITS','8888e9','字符串解析/音频记录/SE入口完整；不采用其余音频路由。'),
 ('Data/Scripts/004_Game classes/002_Game_System.rb',[[237,245]],'COMPLETE_NECESSARY_UNITS','8888e9','正常系统SE资源存在门与音量缩放。'),
 ('Data/Scripts/001_Technical/002_Files/001_FileTests.rb',[[109,115]],'COMPLETE_NECESSARY_UNITS','8888e9','audio SE资源解析完整；RTP内部作为既有共享解析前提，不授宿主输出。'),
 ('Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb',[[1,64]],'FULL_READ','aa6c72','动画数据库缓存与文件缺失入口；不执行load_data。'),
 ('Data/Scripts/011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb',[[474,589],[670,844]],'COMPLETE_NECESSARY_UNITS','183dac/7e087c','完整playTiming与PBAnimationPlayerX，区分作者帧流；未扩签其余作者数据格式。'),
 ('Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb',[[2,6],[247,277]],'COMPLETE_NECESSARY_UNITS','183dac/f0860e','abort异常与完整pbStartBattle入口；仅所调用领域初始化/核心作为有限前提，不授完整Battle域。')
]
formalspans = [
 (WP67,[[1,89],[232,270]],'8b3c1f/ca3b29','§1–3.6作为scope/配置/中止上下文；§9.1–9.4完整接合条款（不扩至另节9.4.1默认招式身份表）。'),
 (WP16,[[297,311]],'422b5b','§6.3完整且所有示例全文，聚合末轮边界。'),
 (WP15,[[98,190]],'422b5b','位图5.1/5.2及音频6.1–6.4.1完整必要条款。'),
 (WP74,[[1,32],[297,355]],'422b5b/ca3b29','范围、概念、音画时序与共享播放器10.2/10.2a完整；未接整作者域。'),
 ('deliverables/final-specification-set/scope-statement.md',[[1,155]],'8888e9/4fdac7','两次连续补读修复输出截断；历史资格不升级当前全局状态。'),
 ('deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',[[390,425]],'ffbdbe','K29/30/31/35/36/37/41/46/50等相关预期及局部上下文，不授整测试族主责。')
]
units = []
for path, ranges, status, tool, purpose in spans:
    units.append(dict(repo='R',commit=R,path=path,identity=ident(RREPO/path),read_ranges=ranges,status=status,platform_output=tool,purpose=purpose))
for path, ranges, tool, purpose in formalspans:
    units.append(dict(repo='B8',commit=B8,path=path,identity=ident(REPO/path),read_ranges=ranges,status='FULL_NECESSARY_CLAUSES',platform_output=tool,purpose=purpose))
seenpaths = {u['path']:u for u in units}
candidate_dispositions = []
for n,x in enumerate(D['all_dependency_identity_candidates']):
    candidate_dispositions.append({'index':n,'path':x['path'],'identity':'input-validation.json/reference_and_candidate_identities',
       'own_reading':seenpaths[x['path']]['read_ranges'] if x['path'] in seenpaths else [],
       'disposition':'NECESSARY_SPANS_READ_ONLY_NO_PRIOR_FULL_READ_INHERITANCE' if x['path'] in seenpaths else 'LOCATOR_ONLY_OTHER_CONTINUATION_OR_FOREIGN_PRIMARY_NOT_NEEDED_BY_02',
       'original_semantic_notes':'完整读为原作者声明与导航，不计本会话外域事实信用。'})
reading = {'schema':'r8-cp02-reading/v1','status':'BOUNDED_READING_COMPLETE','contract_commit':CONTRACT,
 'complete_contract_reading':{'prompt_zh':{'lines':[1,633],'outputs':['bbefce','3dfae1','d045cb']},
  'continuation_contracts':'所有schema/任务元数据全文呈现；1045个ID作为纯身份集合全结构解析及精确分区验证。',
  'readset_complete':'全部顶层键、618对象完整意义、9组、1反向组6子断言、10IR、原候选含撤回、8补充、61依赖声明及31身份记录全部按类型处理；重复身份/通用前提只读一次。',
  'AGENTS':'项目全文及prompt内相同副本；无额外适用祖先AGENTS。',
  'skill':'clean-document-revision全文已读；其description明确不用于评审/审计，故本审计保留纠错链，无正式文档修订。'},
 'input_identity_evidence':'input-validation.json',
 'object_displays':{'manual':{'count':106,'output':'6fea78'},'RGB_and_release':{'count':240,'output':'cf6a06'},'capture':{'count':272,'output':'721e76'}},
 'units':units,'dependency_candidates':candidate_dispositions,
 'readset_field_dispositions':{
  'schema/status/contract_commit/target_commit/target_checkout_tree/target_task_tree/fixed_B8/fixed_R/exclusive_write_set':'固定身份全结构解析，旧contract_commit40f45为前驱来源，不替代实际35d85派发身份。',
  'original_complete_readset':'完整恢复身份合同及31文件身份复用核对；1628507B集合完整，无重新下载原贡献。',
  'source_groups/primary_objects/object_count':'全部9/618语义逐值呈现并与完整源及必要消费者核验；exact-origin指针618匹配。',
  'reverse_current_contribution_objects/selected_reverse_interfaces':'R019六子断言和10IR逐事实处理，原完整ID集合保留；不扩成150/20全部。',
  'all_dependency_identity_candidates':'61身份逐一匹配；原阅读文字全文读为声明，实际信用仅units精确区间。',
  'necessary_unit_rule/qualified_existing_reader_result':'既有source-checked680与F042三条已接均不自动继承。',
  'original_proposal_full/required_or_policy_decision':'原完整候选、有限对照、失败/取消/前缀、撤回和保留范围已读；整体主审/ELR实际接收未造。',
  'full_battler_supplement':'八条全意义与强制更正全文读取，不从它们扩签本组以外领域。',
  'output_required/same_source_duplicate_rule/final_authority/UPDATE_NOT_STARTED':'执行限定输出、相同值不增加标量原子，最终权力保持主审。'},
 'old_payload_purposes':{'six_recovered_python_tools':'纯历史生成/身份工具，未执行；本组不依赖它们的算法产出作语义真值。',
  'atomic/field/forward/reverse/reading/coverage_json':'本组原始对象、接口及来源定位在完整readset或表完整原值中逐项读取；其它组载荷不在02分母。',
  'publication/validation/environment/checkpoint/progress':'复用身份/传输或原作者状态声明；不继承旧PASS，不重审无关行政记录。',
  'bounded_contributions/inputs_combat_review/ui_full':'外域与06接收主责；02用直接源定义自行接必要接口，不冒用66事实或整UI结果。',
  'review/interfaces/limits/proposals/validation_incidents':'实际完整读业务范围、候选/撤回、历史错误/后继与证据限制；0旧执行转入本次。'},
 'truncation_repairs':[{'output':'33cbc8/0a0f7d/9194c6/c08334','repair':'所有业务段拆开后在6fea78/cf6a06/721e76/a1aada全文呈现；身份数组结构解析。'},
  {'output':'ca3b29','repair':'WP16及WP74头部重取422b5b；当前WP67关键§9和WP74§9/10在尾部完整呈现。'},
  {'output':'8d9f4e','repair':'依赖31/32在a1aada补读，余每条完整显示。'},
  {'output':'8888e9','repair':'scope48–98在4fdac7补读、34–49在f0860e补读；首尾其它区间完整。'},
  {'output':'5020f1','repair':'仅rg locator中间截断无信用，source270起由f9e4a0衔接。'},
  {'output':'58cc14','repair':'Safari错误路径失败保留，9eca5f从真实R路径完整读取1–214；197–208补全提示条。'}],
 'tool_execution':'仅新写audit_inputs.py及本序列化工具，未运行任何恢复脚本、Ruby、游戏或行为模型。',
 'platform_IO_limit':'所列output为本次实际工具chunk_id；未把私有平台完整逐字流声称为已发布日志。报告保存精确源区间、身份、语义与新工具，旧作者早期I/O缺口保留。',
 'remaining_necessary_unread':[], 'UPDATE_NOT_STARTED':True}
put('reading-ledger.json', reading)
print(json.dumps({'objects':len(rows),'manual':len(manual),'typed':len(typed),'reverse':len(r019),'IR':len(ir),'units':len(units),'qualifications':len(DEC['qualifications'])},ensure_ascii=False))
