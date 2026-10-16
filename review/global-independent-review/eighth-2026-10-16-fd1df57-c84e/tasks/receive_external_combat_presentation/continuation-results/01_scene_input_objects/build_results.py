"""Serialize explicit reviewer notes. Does not execute restored code or the game."""
import collections
import datetime
import json
from check_inputs import REPO, REF, ROOT, TASK, OUT, CONTRACT, git, identity

D = json.loads((TASK/'continuation/01_scene_input_objects/readset.complete.json').read_text())
NOTES = json.loads((OUT/'assessment-notes.json').read_text())
STAMP = datetime.datetime.now(datetime.timezone.utc).isoformat()

def save(name, obj):
    (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

units = []
def unit(repo, path, intervals, purpose, chunks='platform current turn'):
    commit = D['fixed_R'] if repo == REF else D['fixed_B8']
    raw = git(repo, 'show', commit+':'+path)
    assert (repo/path).read_bytes() == raw
    n = len(raw.splitlines())
    assert all(1 <= a <= b <= n for a,b in intervals), (path,n,intervals)
    units.append(dict(id='READ-%02d' % (len(units)+1), repo=str(repo), commit=commit,
                      path=path, **identity(raw), line_count=n, read_intervals=intervals,
                      purpose=purpose, output_locator=chunks, whole_file=intervals == [[1,n]],
                      complete_credit='Only listed complete units; incidental prefixes excluded.'))

scene = 'Data/Scripts/011_Battle/004_Scene/'
battle = 'Data/Scripts/011_Battle/001_Battle/'
battler = 'Data/Scripts/011_Battle/002_Battler/'
ui = 'Data/Scripts/016_UI/'
obj = 'Data/Scripts/007_Objects and windows/'
data = 'Data/Scripts/010_Data/002_PBS data/'
formal = 'deliverables/final-specification-set/'
unit(REF,scene+'001_Battle_Scene.rb',[[1,419]],'F001–F007全部定义','009cf2')
unit(REF,scene+'002_Scene_Initialize.rb',[[1,191]],'F008–F011全部定义','2b1bca')
unit(REF,scene+'003_Scene_ChooseCommands.rb',[[1,474]],'F012–F018全部定义','2b1bca,967a1a')
unit(REF,scene+'005_Battle_Scene_Menus.rb',[[1,551]],'F028–F033全部定义','9e1825,ee2da3')
unit(REF,scene+'006_Battle_Scene_Objects.rb',[[1,698]],'F034–F041全部定义','ee2da3,2b4082,98e9db')
unit(REPO,formal+'user-interface/wp67-a-battle-interaction-and-presentation.md',[[1,348]],'接点全文；只接受本组具名子断言','98e9db,21f45f,24a42e,a9915a')
unit(REF,battle+'009_Battle_CommandPhase.rb',[[1,265]],'接受/回退/自动选择/物品族消费者','016273')
unit(REF,battle+'004_Battle_ActionAttacksPriority.rb',[[1,132]],'选招、自动登记、登记目标与可目标查询','016273')
unit(REF,battle+'001_Battle.rb',[[200,577],[816,867]],'侧尺寸/属主/队伍映射/枚举/对面序/近邻/消息包装','8f769f,4dbd12,e05f63')
unit(REF,battle+'002_Battle_StartAndEnd.rb',[[1,6],[170,347],[405,512]],'开场、中止、主循环、正常清理','f62859')
unit(REF,battle+'005_Battle_ActionSwitching.rb',[[1,311]],'完整换入换出、选择包装、替补/消息/重排/派出','7fd3d1,515b03')
unit(REF,battle+'006_Battle_ActionUseItem.rb',[[1,149]],'登记消费、四执行族、退款和身份残留','7fd3d1')
unit(REF,battle+'008_Battle_ActionOther.rb',[[1,201]],'Call/Shift/Mega资格与消费','515b03')
unit(REF,battle+'010_Battle_AttackPhase.rb',[[1,202]],'固定执行次序与决定截断','515b03')
unit(REF,battle+'003_Battle_ExpAndMoveLearning.rb',[[1,271]],'经验caller门、逐级写入/展示、学招/取消','958f40,e01190')
unit(REF,battler+'003_Battler_ChangeSelf.rb',[[1,124]],'HP writer、正式失能、PP关联','958f40')
unit(REF,battler+'001_Battle_Battler.rb',[[98,216],[695,760]],'写穿HP/status、显示属性、归一化与盟友枚举','958f40,4dbd12,37aa54')
unit(REF,battler+'008_Battler_UseMoveTargeting.rb',[[36,91],[173,191]],'执行目标解析、添加与盟友重选','23a434')
unit(REF,'Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb',[[1,201]],'完整基类PP/realMove/显示query','23a434')
target_path = 'Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb'
unit(REF,target_path,[[1,len((REF/target_path).read_bytes().splitlines())]],'全部Target数据/default与RandomNearFoe=1','0f2303')
unit(REF,scene+'004_Scene_PlayAnimations.rb',[[1,156],[184,308]],'intro/sendOut/提示条/HP/EXP全部必要包装','93f25d')
unit(REF,scene+'007_Battle_Scene_BaseAnimation.rb',[[1,64]],'聚合完成器、临时精灵销毁','93f25d')
unit(REF,scene+'008_Battle_Scene_Animations.rb',[[1,79],[183,252],[577,608]],'Intro/框/提示条/伤害闪烁必要完整轨道','2d4397')
unit(REF,'Data/Scripts/005_Sprites/010_PictureEx.rb',[[123,181],[362,478],[546,548]],'完整运行/回调/时钟调度及适配委托','79035f,19b72c,f63548')
unit(REF,'Data/Scripts/001_Technical/002_RubyUtilities.rb',[[390,406]],'nil_or_empty和lerp','cdcf93')
unit(REF,obj+'005_SpriteWindow_text.rb',[[114,619]],'高级文字组件全文，四态、resume与skipAhead分开')
unit(REF,ui+'005_UI_Party.rb',[[475,714],[746,853],[917,988],[1013,1034]],'启动、列表/子菜单、摘要、选择/映射接点、选招')
unit(REF,ui+'006_UI_Summary.rb',[[184,215],[814,844],[929,992],[1232,1380]],'遗忘初绘、空首招边界、换序、HM门和返回')
unit(REF,ui+'007_UI_Bag.rb',[[1,453]],'背包窗口/场景全文，过滤映射和取消层','2bf7ae')
unit(REF,ui+'004_UI_Pokedex_Entry.rb',[[71,152],[557,580],[614,619]],'brief图鉴入口/初绘/输入/返回')
unit(REF,ui+'025_UI_TextEntry.rb',[[738,778]],'命名包装、mode2与画面返回，不接收全部输入编辑域')
unit(REF,ui+'018_UI_ItemStorage.rb',[[341,376]],'背包子命令真实UIHelper，BACK=-1与局部ensure','6104e3')
unit(REF,'Data/Scripts/013_Items/001_Item_Utilities.rb',[[206,221]],'右上数值窗口仅USE关闭')
unit(REF,data+'010_SpeciesMetrics.rb',[[1,101]],'全部指标、惰性生成、影子门、偏移','0f2303')
unit(REF,data+'009_Species_files.rb',[[1,246]],'全部图像/影子/叫声选择和请求；无媒体观察','063dd7,25ef05')
unit(REF,data+'008_Species.rb',[[267,276]],'物种指标和影子门完整委托','bed503,e05f63')
unit(REF,data+'014_TrainerType.rb',[[52,90]],'训练家前背图与玩家服装候选','6104e3')
unit(REF,data+'005_Move.rb',[[106,204]],'完整display_type，注释的类型表未作运行逻辑','6104e3,e05f63')
unit(REF,'Data/Scripts/014_Pokemon/004_Pokemon_Move.rb',[[1,77]],'持久Move PP和显示查询完整定义','6104e3')
unit(REF,'Data/Scripts/014_Pokemon/001_Pokemon.rb',[[94,105],[113,179]],'命名/招式上限、叫声、species_data/form副作用边界')
unit(REF,'Data/Scripts/001_Settings.rb',[[11,17],[134,137],[217,225]],'世代8、超级异色门、队伍上限6')
unit(REF,obj+'001_RPG_Cache.rb',[[1,144]],'cache直接加载、共享引用与普通异常','d8858e')
unit(REF,obj+'007_BitmapSprite.rb',[[1,243]],'全部BitmapSprite/AnimatedSprite/IconSprite/ChangelingSprite','d8858e,23a434')
unit(REF,obj+'008_AnimatedBitmap.rb',[[1,228]],'全部普通/前缀PNG包装与更新','d8858e')
unit(REF,obj+'009_Planes.rb',[[1,76]],'全部平面资源清除/加载','d8858e')
unit(REF,'Data/Scripts/011_Battle/008_Other battle types/004_BattleArenaBattle.rb',[[1,200]],'Arena仅换入/顺序替补和相关完整方法；余部绘制不接收','e01190')
unit(REF,'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb',[[1,107]],'满队模式1/2、负索引返回消费者、图鉴/命名桥','bba3d7')
unit(REPO,formal+'engine-overworld/wp15-resource-matching-and-audio.md',[[102,130]],'完整§5.1/5.2失败与时相合同','cdcf93')
unit(REPO,formal+'user-interface/wp17-messages-windows-input.md',[[59,85]],'完整§3.3四态','cdcf93')
unit(REPO,formal+'user-interface/wp66-a-party-and-summary-ui.md',[[31,65],[166,208]],'列表返回、摘要换序/遗忘/HM/学习','cdcf93')
unit(REPO,formal+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',[[360,426]],'BT59及HP01–04完整段；其余模式只上下文，不授全域信用','25ef05')
unit(REPO,formal+'combat-requirements/wp40-commands-obedience-and-action-order.md',[[45,76],[97,120]],'命令、退款与NearAlly的主合同','4dbd12,f63548')
unit(REPO,formal+'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md',[[183,192]],'正常终局退款及失败前缀','f63548')
unit(REPO,formal+'creature-rpg/wp20-hp-status-moves-helditem.md',[[124,157]],'招式表/零招式与PP规则','f63548')
unit(REPO,formal+'combat-requirements/wp39-battle-context-and-participants.md',[[138,157]],'全部布局对面序和近邻表','bba3d7')

records = []
for g in D['source_groups']:
    xs = [x for x in D['primary_objects'] if x['group'] == g['id']]
    assert len(xs) == len(NOTES[g['id']])
    for x,note in zip(xs,NOTES[g['id']]):
        records.append(dict(id=x['id'], original_complete_object=x,
                            current_complete_meaning_and_reason=note,
                            disposition='RECEIVED_WITH_MANDATORY_QUALIFICATION' if note.startswith('Q:') else 'RECEIVED_FINITE_SOURCE_FACT',
                            formal_locator=x['meaning']['formal_links'],
                            source_read_unit=next(u['id'] for u in units if u['path']==x['source']['path']),
                            consumer_joins='interfaces.json: reverse record and joined provider paths',
                            evidence='SOURCE_STATIC / FORMAL_TEXT; NOT_EXECUTED',
                            precise_parameter_adoption='Source exact values retained; formal link does not automatically mandate every internal parameter.',
                            necessary_unread=[], root_task_final_credit=0))
assert [x['id'] for x in records] == [x['id'] for x in D['primary_objects']]
save('reception-ledger.json',dict(schema='r8-cp01-reception/v1',utc=STAMP,
    status='READY_FOR_PARENT_RECEPTION',contract_commit=CONTRACT,target_commit=D['target_commit'],
    fixed_B8=D['fixed_B8'],fixed_R=D['fixed_R'],source_groups=D['source_groups'],
    denominator=166,received_facts=166,original_wording_qualified=sum(x['disposition'].endswith('QUALIFICATION') for x in records),
    records=records,necessary_unread=[],unavailable_required_material=[],
    new_required_findings=0,new_candidates_pending_parent_adjudication=1,
    findings='findings.json',root_task_final='OPEN_PARENT_AUTHORITY',UPDATE_NOT_STARTED=True))

save('reading-ledger.json',dict(schema='r8-cp01-reading/v1',utc=STAMP,contract_commit=CONTRACT,
    effective_contract='35d85e user dispatch; embedded 40f45d retained only as provenance',
    fixed_B8=D['fixed_B8'],fixed_R=D['fixed_R'],target_commit=D['target_commit'],
    primary=dict(files=5,lines=2333,bytes=80222,groups=32,objects=166,unread=0),
    units=units,identity_receipt='input-identities.json',
    contract_reading=dict(complete_prompt=True,AGENTS='Root AGENTS.md and embedded exact copy read; no applicable descendant AGENTS.',
        skill='inputs/review-SKILL.md fully read; clean-document-revision explicitly excludes review/audit reports, so no document revision performed.',
        readset_field_dispositions={
            'primary_objects':'All166 current assertions individually presented and compared; notes are explicit per object.',
            'source_groups':'All32 notes/consumer/formal links/premises read. Shared identity values mechanically verified.',
            'reverse_current_contribution_objects':'All14 groups/59 assertions read; per-fact dispositions in interfaces.json.',
            'selected_reverse_interfaces':'Both complete current claims read and joined; no takeover of other tasks source population.',
            'all_dependency_identity_candidates':'All61 metadata/purpose/semantic_notes read as prior-author claims. Actual new-reader spans above alone receive semantic credit.',
            'original_complete_readset':'Entire schema/availability/provenance and31 file identities processed; cache equals exact target Git objects.',
            'original_proposal_full':'All CP002 and withdrawn H001 content read; classification not changed. No independent ruling on out-of-group fixed tracks.',
            'full_battler_supplement':'Both complete companions read; scene REFRESH/HP/ILLUSION joined directly; five unrelated core facts not adopted as own verification.',
            'continuation-contracts':'All six jobs parsed; exact object/group sets and identities handled as administrative partition. No dispatch/spawn/new votes.',
            'remaining_scalar_fields':'Fixed identities, necessary-unit rule, old680/received3 qualification, output list, duplicate rule and root authority read.'}),
    incidents=[
      'Initial whole-file listings and raw concatenations were truncated. No whole semantic credit from them. Prompt completed by continuous sed ranges; group/assertion values repaired in compact deduplicated displays; reverse claims repaired without repeated formal identities; dependency notes32–60 repaired.',
      'Mistaken source paths for Target/Pokemon_Move/CatchAndStore returned missing-file errors; rg located actual paths and complete necessary units were read.',
      'A draft build_results tool invocation had JavaScript SyntaxError before execution; it produced no file or semantic credit. Replaced with this bounded serializer.',
      'gh auth status reported invalid GH_TOKEN; ordinary git fetch succeeded. No credential changed; publication uses authorized ordinary git push.'
    ],
    provenance=dict(reader='Current delegated /root context, logical task01_scene_input_objects',
        author_context='01a143b2-8ba3-76f5-a39d-7904a2dd1000',
        parent_source_thread='01a13f49-a154-7054-9b04-ce31f924d01c',
        source_thread_is_not_reader_uuid=True,
        independence='This task did not author the target contribution or parent reception. No role renaming used as evidence of an extra reviewer.',
        actual_platform_uuid='UNVERIFIED',requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default normal',Fast='off'),
        actual={k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast']},
        spawned_agents=0,new_votes=0),
    execution=dict(reference=0,independent_behavior_model=0,host_demo=0,native_media=0,status='NOT_EXECUTED',
        tools='Python/Git for identity, JSON serialization and report consistency only; no restored scripts executed.'),
    necessary_unread=[],UPDATE_NOT_STARTED=True))

print(json.dumps(dict(primary_records=len(records),qualified=sum(n.startswith('Q:') for a in NOTES.values() for n in a),read_units=len(units))))
