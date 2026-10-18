"""New identity/ledger assembler. No reference, recovered helper, or game execution.

All semantic judgments below were authored after the cited actual tool reads.
The tool checks identities, exact populations and serialization, not semantic truth.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess

OUT = Path(__file__).resolve().parent
REPO = next(p for p in OUT.parents if (p / '.git').is_dir())
PARENT = OUT.parent.parent
R = Path('/workspace/pokemon-essentials')
CONTRACT = '35d85e4484b892ebc32542346861440638d2183c'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
TARGET = '18d21310bdc360c87d7ffd886df7d06aef8604a7'
READSET = PARENT / 'continuation/05_capture_debug/readset.complete.json'
data = json.loads(READSET.read_text())
original = PARENT / 'recovered' / TARGET
utc = datetime.datetime.now(datetime.timezone.utc).isoformat()


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def identity(path, repo, commit):
    rel = path.relative_to(repo).as_posix()
    entry = git(repo, 'ls-tree', commit, '--', rel).decode().strip()
    mode, typ, rest = entry.split(' ', 2)
    blob, got_path = rest.split('\t', 1)
    assert typ == 'blob' and got_path == rel
    content = path.read_bytes()
    assert content == git(repo, 'cat-file', 'blob', blob), rel
    return dict(repo=str(repo), commit=commit, path=rel, mode=mode,
                git_blob=blob, bytes=len(content), sha256=hashlib.sha256(content).hexdigest())


def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


# Reuse immutable material already recovered in the supplied contract checkout.
# All 31 bytes/modes/blobs are verified; no duplicate recovery or old script run.
input_proofs = []
for f in data['original_complete_readset']['files']:
    path = original / f['relative_to_target_task']
    actual = identity(path, REPO, CONTRACT)
    assert all(actual[k] == f[k] for k in ('mode', 'git_blob', 'bytes', 'sha256'))
    input_proofs.append(dict(relative_to_target_task=f['relative_to_target_task'],
                             remote_path_at_target_commit=f['remote_path_at_target_commit'],
                             verified_cache_identity=actual,
                             target_commit=TARGET,
                             credit='IDENTITY_ONLY_UNLESS_SEPARATELY_LISTED'))
assert len(input_proofs) == 31
assert sum(x['verified_cache_identity']['bytes'] for x in input_proofs) == 1628507
assert git(R, 'rev-parse', 'HEAD').decode().strip() == RC
assert git(REPO, 'rev-parse', B8 + ':deliverables/final-specification-set').decode().strip() == 'f292698cdd4a8e725525a9be6dc34b75faaf151e'
assert git(REPO, 'rev-parse', CONTRACT + ':deliverables/final-specification-set') == git(REPO, 'rev-parse', B8 + ':deliverables/final-specification-set')
contracts = json.loads((PARENT / 'continuation-contracts.json').read_text())
job = next(x for x in contracts['jobs'] if x['id'] == '05_capture_debug')
for key in ('prompt', 'readset'):
    actual = identity(PARENT / job[key], REPO, CONTRACT)
    assert all(actual[k] == job[key + '_identity'][k] for k in ('mode', 'bytes', 'sha256', 'git_blob'))
groups = {x['id']: x for x in data['source_groups']}
atoms = json.loads((original / 'atomic-assertions.json').read_text())['assertions']
for obj in data['primary_objects']:
    assert obj['meaning'] == atoms[int(obj['origin_pointer'].split('/')[-1])]
    assert obj['source'] == groups[obj['group']]['reference']
    actual = identity(R / obj['source']['path'], R, RC)
    assert all(actual[k] == obj['source'][k] for k in ('bytes', 'sha256', 'git_blob'))
assert sorted(job['ids']) == sorted(x['id'] for x in data['primary_objects'])

session = os.environ.get('CODEX_THREAD_ID', 'UNVERIFIED')
assert session not in ('01a143b2-8ba3-76f5-a39d-7904a2dd1000', '01a14479-e75c-7131-85ed-aec1de217031')
save('bindings.json', dict(schema='r8-cp05-bindings/v1', utc=utc,
    contract_commit=CONTRACT, contract_tree=git(REPO, 'rev-parse', CONTRACT+'^{tree}').decode().strip(),
    readset_embedded_contract_commit=data['contract_commit'], embedded_commit_purpose='Earlier parent contract provenance; actual dispatch binds 35d85e4, not moving HEAD.',
    target_commit=TARGET, target_checkout_tree=data['target_checkout_tree'], target_task_tree=data['target_task_tree'],
    B8=B8, R=RC, reference_tree=git(R, 'rev-parse', 'HEAD^{tree}').decode().strip(),
    branch='codex/r8-cp-reception-05-20261016', actual_context=session,
    original_author='01a143b2-8ba3-76f5-a39d-7904a2dd1000', prior_receiver='01a14479-e75c-7131-85ed-aec1de217031',
    independence='Different actual environment thread echo from both named contexts. No self-spawn; one bounded receiver, no extra votes.',
    requested=dict(model='gpt-6.1-sol', effort='ultra', tier='default normal', Fast='off'),
    actual_config={k:'UNVERIFIED' for k in ('model','effort','tier','speed','Fast')},
    input_proofs=input_proofs, originals_read_only=True, UPDATE_NOT_STARTED=True))

# Each entry names exact presented spans and platform output IDs. Extra visible
# prefixes of unrelated functions are intentionally not given complete-unit credit.
reads = []


def read(label, repo, path, spans, outputs, purpose):
    commit = RC if repo == R else CONTRACT
    ident = identity(repo / path, repo, commit)
    lines = (repo / path).read_bytes().splitlines(keepends=True)
    ranges = []
    for lo, hi in spans:
        assert 1 <= lo <= hi <= len(lines), (path,lo,hi,len(lines))
        content = b''.join(lines[lo-1:hi])
        ranges.append(dict(first=lo,last=hi,sha256=hashlib.sha256(content).hexdigest()))
    reads.append(dict(id=label,identity=ident,actual_read_ranges=ranges,platform_output_ids=outputs,
                      purpose=purpose,level='SOURCE_STATIC' if repo == R else 'FORMAL_TEXT_OR_CONTRACT',
                      full_file=spans == [(1,len(lines))], no_whole_foreign_domain_credit=True))


read('R-DEBUG',R,'Data/Scripts/011_Battle/004_Scene/009_Battle_DebugScene.rb',[(1,106)],['a892b4'],'F060–062：完整类、全部空操作和返回值、缺失move读取、50次与候选/让渡')
read('R-CATCH',R,'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb',[(1,271)],['a892b4'],'F063–066：完整接收、队列、投球、数学和混入')
read('R-BALL',R,'Data/Scripts/011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb',[(1,198)],['0feb63'],'F076–079：所有四表/1+19+2+0注册和完整处理器')
read('R-PEER',R,'Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb',[(1,77)],['0feb63'],'默认Peer的同身份存放、缺失消息边界、形态生命周期；NullPeer不冒默认替换')
read('R-SETTINGS',R,'Data/Scripts/002_BattleSettings.rb',[(1,140)],['0feb63'],'新式球率、软上限、暴击、捕获经验和替换默认，完整配置文件')
read('R-BATTLE',R,'Data/Scripts/011_Battle/001_Battle/001_Battle.rb',[(1,287),(300,348),(348,480),(483,490),(500,542),(547,551),(582,602),(642,645),(658,675),(820,840)],['ad6a7e','eefec0','e75067','a99655','0c0097','8a0721'],'构造/身份/侧/队伍段、所有必要存活枚举/目标顺序、移出、图鉴门和UI包装；非整文件信用')
read('R-END',R,'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb',[(1,6),(247,351),(405,512)],['eefec0','e75067'],'起战正常/显式abort、主循环、完整正常终局/接收/退款/初始物品恢复')
read('R-EXP',R,'Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',[(1,90)],['bb2dde'],'完整pbGainExp与EV接收，仅捕获标记/参与者时点；不接收全部成长域')
read('R-COMMAND',R,'Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb',[(1,265)],['f8d4de','a9bfcb'],'完整命令/撤销/菜单许可/登记/AI分支，非AI全部策略信用')
read('R-SWITCH',R,'Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',[(113,136)],['8a0721'],'调试换人候选的真实调用者校验及AI替补入口')
read('R-AI',R,'Data/Scripts/011_Battle/005_AI/001_Battle_AI.rb',[(1,163)],['f8d4de'],'AI命令/替补直接入口与定义；仅旁路场景辅助的有限事实')
read('R-SIM',R,'Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb',[(377,438)],['f8d4de','4254d2'],'完整pbRuledBattle：1%真实分支/三个控制旗标、正常治疗/持物恢复；异常不保证')
read('R-ITEM',R,'Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb',[(1,149)],['8a7c9f'],'球专路、先登记扣减、无复检退款、正常返回清身份')
read('R-ATTACK-ITEM',R,'Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb',[(68,91)],['a99655'],'完整物品攻击阶段：useType4→专用球，结果正值早返')
read('R-ITEM-HANDLERS',R,'Data/Scripts/013_Items/001_Item_Utilities.rb',[(1,116)],['42dd13','a99655'],'处理器集合、CanUse缺失默认true与UseInBattle通知入口；非全部物品域')
read('R-ITEM-BALL-REG',R,'Data/Scripts/013_Items/003_Item_BattleEffects.rb',[(28,65),(322,327)],['a9bfcb'],'完整球条件许可与执行注册；失败无消耗仅在登记前前提下')
read('R-HANDLER',R,'Data/Scripts/003_Game processing/005_Event_Handlers.rb',[(148,203),(286,298)],['4ea9db'],'RX-HANDLER更正：raw add、查找/trigger id规范化、copy即时共享、空子类；不移植API')
read('R-STORAGE',R,'Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',[(1,265)],['4ea9db'],'完整Box/Storage：容量、同身份插入、先当前盒后扫描、治疗及ready标记保留')
read('R-DEX',R,'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',[(1,361)],['a84fa3'],'完整实际图鉴接收定义；全国拥有计数、基础种/显示形态/刷新/已解锁门')
read('R-TRAINER',R,'Data/Scripts/015_Trainers and player/001_Trainer.rb',[(65,88)],['a84fa3'],'实际party_count/party_full和可战斗计数')
read('R-PLAYER',R,'Data/Scripts/015_Trainers and player/004_Player.rb',[(112,123)],['a84fa3'],'owned?到图鉴接收者桥')
read('R-POKEMON',R,'Data/Scripts/014_Pokemon/001_Pokemon.rb',[(113,115),(147,184),(252,307),(877,906),(1066,1071)],['4ea9db','cd097a','42dd13'],'species_data使用form_simple；form写入/图鉴前缀、非蛋heal含PP与ready清、空名归默认、当前形态重量/基础速度')
read('R-SPECIES',R,'Data/Scripts/010_Data/002_PBS data/008_Species.rb',[(243,328),(365,375)],['a84fa3','cd097a'],'旗标、前代递归与完整家族演化枚举/月石道具谓词，不要求当前可立即进化')
read('R-ITEM-ID',R,'Data/Scripts/010_Data/002_PBS data/006_Item.rb',[(176,178)],['a84fa3'],'PokeBall/SnagBall旗标与机器的实际资格')
read('R-BATTLER',R,'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',[(1,13),(105,112),(277,289),(309,330),(344,357),(421,429),(694,699),(747,777)],['ad6a7e','39aa53','0c0097','8a0721'],'HP/失能、属性、重量有效性门、异侧/存活同伴与直接对位；无整个Battler信用')
read('R-RESET',R,'Data/Scripts/011_Battle/002_Battler/002_Battler_Initialize.rb',[(305,316)],['cd097a'],'完整捕获后场上对象reset；pbInitEffects委托不冒全效果重新审查')
read('R-SLEEP',R,'Data/Scripts/011_Battle/002_Battler/004_Battler_Statuses.rb',[(1,16),(276,278)],['4ea9db','ad6a7e'],'实际状态与视为睡眠区分')
read('R-ABILITY',R,'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',[(68,72),(80,82),(92,94),(351,362),(414,419)],['39aa53','42dd13'],'完整必要分派、Heavy/LightMetal及COMATOSE；不接收八伴件其余主域')
read('R-ITEM-WEIGHT',R,'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb',[(53,56),(64,66),(253,257)],['39aa53','42dd13'],'nil-only默认与FloatStone整数除二')
read('R-SETUP',R,'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',[(171,304),(306,329),(375,409)],['f4b9a6'],'完整必要编组、参数注入、时段与野生核心及正常外层善后；同个体/不同参与数组')
read('R-DEFAULTS',R,'Data/Scripts/001_Settings.rb',[(1,17),(216,227),(294,325)],['f4b9a6'],'世代8、容量6/40、存盒治疗关、图鉴设置')
read('R-OPTIONS',R,'Data/Scripts/016_UI/015_UI_Options.rb',[(1,36)],['cd097a'],'普通选项手动送盒/命名Give默认')
read('R-SCENE-MENUS',R,'Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb',[(141,324),(460,474)],['8a7c9f','8a0721','eedf86'],'mode1/2、真实队伍下标反查、99取消调用者、球目标接合、命名和图鉴桥')
read('R-SCENE-COMMAND',R,'Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb',[(267,308)],['8a7c9f'],'确认与命令：初始0、BACK返回默认值，忙时恢复并继续')
read('R-SCENE-CAPTURE',R,'Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb',[(331,385)],['f8d4de'],'完整投球/成功ME/收球/挡球入口；正常等待3.5秒、异常无统一ensure')
read('R-CAPTURE-ANIM',R,'Data/Scripts/011_Battle/004_Scene/008_Battle_Scene_Animations.rb',[(661,849)],['4254d2','bb2dde'],'成功依原摇数≥4；critical只压展示，成功球保留；非本组参数表签收')
read('R-ANIM-BASE',R,'Data/Scripts/011_Battle/004_Scene/007_Battle_Scene_BaseAnimation.rb',[(1,64)],['bb2dde'],'正常聚合等待/临时精灵dispose，无全局回滚')
read('R-AUDIO',R,'Data/Scripts/019_Utilities/003_Utilities_BattleAudio.rb',[(40,58)],['cd097a','eedf86'],'完整捕获ME选择定义；请求不等实际发声')
read('R-TEXT',R,'Data/Scripts/016_UI/025_UI_TextEntry.rb',[(180,255),(666,786)],['42dd13','f4b9a6'],'实际命名结果/空串、screen正常返回与mode2桥；不冒完整文字输入域')
read('R-PARTY-UI',R,'Data/Scripts/016_UI/005_UI_Party.rb',[(705,713),(746,800),(917,924)],['42dd13'],'summary桥、完整选择循环和screen包装；取消先于存盒')
read('R-DEX-UI',R,'Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',[(71,139),(556,571),(613,619)],['63e325','42dd13'],'brief建立/输入循环/关闭及screen桥；绘制细节不授本组信用')
read('R-PBS-BALLS',R,'PBS/items.txt',[(3803,4036)],['63e325','a99655'],'全部26球完整记录；包含描述但仅旗标/battleuse和登记比较作为事实证据')

F='deliverables/final-specification-set/'
read('F-38',REPO,F+'pokemon-rules/wp38-capture-and-receiving.md',[(1,146)],['f9231c'],'唯一捕获主规格全文；全部公式、枚举、失败和历史范围，不外推runtime')
read('F-67',REPO,F+'user-interface/wp67-a-battle-interaction-and-presentation.md',[(84,88),(209,233),(254,270)],['b78dd5','6fa48c'],'完整3.6、8、9.3–9.4有关条款；不是全篇UI primary审查')
read('F-CP',REPO,F+'test-catalog/pokemon-rules-wp31-32-37-38.md',[(138,165)],['6fa48c'],'CP01–24完整捕获向量；只有限推导不当reference执行')
read('F-U10',REPO,F+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',[(951,970)],['6fa48c'],'完整U10-CP01–09及共同前提/暂停消息前缀')
read('F-39',REPO,F+'combat-requirements/wp39-battle-context-and-participants.md',[(116,133)],['485f58'],'伙伴实际参与资格/共享成员身份与构造默认')
read('F-42',REPO,F+'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md',[(35,58),(166,192)],['0a685b','485f58'],'捕获决定/正常终局/伙伴错配及原兼容裁决范围')
read('F-62',REPO,F+'pokemon-rules/wp62-pokedex-records-regions-and-content.md',[(11,47),(108,119)],['0a685b'],'记录字段、包装有门/直接无门、全国拥有与区域解锁接合')
read('F-76',REPO,F+'demo-dx/wp76-facility-content-generation-and-simulation.md',[(158,170)],['0a685b'],'真实模拟与直接辅助、1%分支、正常治疗而非战前快照')

save('reading-ledger.json',dict(schema='r8-cp05-reading/v1',actual_reader=session,utc=utc,reads=reads,
    contract_reading=dict(continuation_contracts='FULL 1–1297; b4586d/ecf864/f64acd',
        prompt='FULL 1–633; 775318/2c951c/9df001, including embedded whole global prompt/AGENTS/skill',
        readset='ALL fields through exact JSON projections: f64acd,6a589a,a46261,10f67c,e81c50,c75812; repeated source identity/premise values read once with exact equality checked',
        skill='review-SKILL.md full 9df001; excludes audit reports by its description',
        original_review_limits_incidents='Full original review.md/limits.json/validation-incidents.json at 7a1617; author claims remain claims'),
    truncations=dict(first_combined_contract_read='Truncated; no full credit; repaired bounded reads',
        dependency_projection='e81c50 truncated middle; indices22–36 fully repaired c75812',
        formal_navigation='b78dd5 truncated; required9.3–9.4/CP/U10 repaired6fa48c; navigation-only unneeded hits not credited',
        source_navigation='4254d2 declaration/header repaired bb2dde; all needed capture class body actually visible; rg hits are locator only'),
    failed_lookup_attempts='Wrong guessed paths produced exit2; subsequently resolved with rg --files and exact reads. No input modified.',
    original_readers_not_inherited=True,business_execution='NOT_EXECUTED',UPDATE_NOT_STARTED=True))

# Handwritten received meanings in ID order: no generated generic PASS assertions.
meaning = {
60:[
'初始化只记战斗引用、四槽命令/招式记忆与日志开关，不构造视觉对象；不承诺支持完整Scene协议。',
'初始化与pbStartBattle均重置lastCmd/lastMove为四个0；后者另写传入battle。',
'1–76所列阶段、图形、HP/EXP、结束等入口为空操作；消息/随机辅助及显式返回方法分别保留，不能概括所有方法皆空。',
'Blitz忽略keys，返回0..29随机整数；不是按键读取或玩家交互证据。'],
61:[
'普通/暂停/确认/选择消息只有log_messages真才请求日志；不构造文字/输入等待。',
'确认可选记录消息后恒true，不依据玩家输入。',
'命令列表可选记录消息后恒0，不解释传入commands/defaultValue。',
'物品菜单恒−1，与正常Bag返回/登记链分开。',
'遗忘辅助恒0，即选首槽；不是放弃/正常摘要操作。'],
62:[
'主命令先抽0..14，命中0返回Bag1；未命中才继续下一抽。',
'仅未选Bag时抽0..9，命中0返回Call4；总概率7/75，其余Fight0；非两个独立总体概率。',
'出招辅助至多50次让渡的循环表达式先读取缺失单数move；标准Battler只有moves，无补充入口时首读失败，早于rand和yield；不推出真实模拟必败。',
'目标候选=对方存活场上位置，不按target_data类别；空集−1，否则sample。',
'同训练家队伍段中不在活跃场上者先入候选，不先保证非蛋/存活/可换；空集nil，非空至多50次随机让渡(idx,self)，由caller判断；耗尽不等于找到合法替补。'],
63:[
'非暗影且givenicknames0并确认Yes才调用命名，所得字符串经name=写入（空/默认种名归未命名）；命名在去向选择及存储之前。',
'仅队满且sendToBoxes0/2进入询问；2删送盒项并修正后续下标；摘要/查看队伍正常返回后重显，构造默认1与实际选项默认0分开。',
'命令初始游标0；BACK值99在询问档结束循环走常规存放，在强制档重显；选人取消是另一层，回去向菜单。',
'选定旧成员先离场、毒计数清、解除Mega/Primal，再Peer存同一对象；只有存放正常返回才删除玩家队伍，再查盒名/暂停；容量兜底错误早于删除。',
'送盒暂停正常返回后才左移initialItems与等级/会心/承伤四类记录并清尾；消息内失败保已存盒/已删除前缀，无后继重排或统一回滚保证。',
'常规Peer返回负值时新个体已入队；入队暂停消息正常返回后才填新槽initialItems；非负走盒名与送盒提示，不统一回填。'],
64:[
'每个体先pbSetCaught再pbSetSeen，两包装受internalBattle门；未owned时直接set_owned无该门；别把三者写成统一开关或自动全部成功。',
'新增消息/最近见到/图鉴页仅原先未拥有且全局player持图鉴且其解锁查询真；owned查询/写入接收者为battle.pbPlayer；正常主流程两者同一，不能外推任意副本。',
'暗影个体直接向battle.pbPlayer图鉴写shadow_owned，在命名/存储之前；不受上述包装门。',
'队列按个体完整登记→命名/存放后才下一只，整个each正常结束才clear；多只为人工队列前提，不假定普通野生投球自然生成。',
'图鉴、名字、治疗、存盒/删队/记忆等按实际到达前缀保留；无通用事务，异常可使已处理个体仍在未清队列，不推定自动重试或永久丢失。'],
65:[
'参数属敌侧则直接取该位置，属己侧则用其直接对位查询；若倒下改取首个存活同伴（非自身），不等于任意后备。',
'合法球前提下无存活同伴得到nil，后续fainted?先失败，达不到无目标提示；直接调用不自带背包消耗，已登记路径的消耗须另有前提。',
'目标有效时先brief投掷消息，训练家战非Snag+Shadow才挡球/提示/早返；挡球不进捕获计算、失败统计或first-ball更新。',
'0–3各自结果消息正常返回后才调用onFailCatch；其先统计+1再通知失败handler；场景throw或结果消息异常可阻止这些后继写入。',
'4时先Gotcha/成功旋律，再移除参与队伍（保空位/重排显示秩），捕获经验开才captured=true→GainExp→false；后者异常不保证撤标记。',
'经验正常返回后reset场上引用；无可战者决定训练家1/野生4；Snag改owner→onCatch→球种→解除/暗影招/首招/强制形态→Peer离场→藏球→入待接收。藏球实参仍是最初入口idxBattler，重选目标后未换为新index；不许默认为一定隐藏新目标框。',
'只有非4且流程到达末尾才设置首次失败球（此前poke_ball_failed假时）并标失败；成功不更新，阻挡/前段异常也不自动更新。'],
66:[
'独立于battle.debug，只有全局$DEBUG且CTRL按住才直接4；上游投球已重置criticalCapture=false，绕过率/随机。',
'正常物种基础率或显式输入率；UltraBeast且非BEAST球跳过全部球倍率，先除10；整数输入截断，显式浮点输入依其数值类型，不把/10写成通用实数乘0.1。',
'HP式先转浮点，真实SLEEP/FROZEN×2.5、其它非NONE×1.5，然后唯一floor、下限1；视为睡眠只影响Dream球，最大HP须为合法正值。',
'x≥255先短路，或无条件处理器真时直接4；均不进入critical/普通随机；MASTER仍在HP计算之后检查。',
'y=floor(65536/(255/x)^0.1875)，普通依次至多4次[0,65535]比较<y，首失败停止；不是始终耗四次随机。',
'开关真时全局player全国owned数按严格>600/450/300/150/30取5..1否则0，护符翻倍，整数c=x*d/12；c>0才抽256，命中后仅一次65536成功4/失败0并置critical=true；否则转普通。',
'文件末将完整CatchAndStoreMixin纳入Battle；Safari另有专用覆盖，不据混入断言所有模式同一许可/接收。'],
76:[
'无条件、基础率、成功、失败四个独立ItemHandlerHash；实际注册符号键，子类没有额外GameData解析覆盖。',
'isUnconditional只有nil回false，modify只有nil回原rate，false/0不被当nil；OnCatch/OnFail通知不自动保证成功或消费。',
'onFail入口先failed_poke_ball_count+1再trigger；默认无失败注册，扩展回调抛错亦不回滚该统计。'],
77:[
'MASTER仅无条件表真，不另改基础率；UltraBeast非BEAST前置仍先除10但随后必捕。',
'GREAT/SAFARI×1.5、ULTRA×2，无该处理器局部255钳制。',
'NET在当前战斗类型含BUG/WATER时×新3.5/旧3；REPEAT在battle.pbPlayer已owned目标物种时同倍率；未命中各保持。',
'DIVE仅environment为Underwater×3.5；不是所有水面/冲浪/钓鱼。',
'NEST仅等级≤30乘max((41-level)/10.0,1)，30级1.1、31级不变；浮点除法。',
'TIMER乘min(1+0.3*turnCount,4)；合法非负轮数前提，10起封顶4。',
'DUSK仅time==2乘新3/旧3.5；洞穴/夜晚由prepare_battle赋值，默认世代8新档。',
'QUICK仅turnCount==0×5，不泛称首次投掷；后续轮数不变。'],
78:[
'FAST取pokemon当前形态baseStats的SPEED≥100才×4，再与255取小；不是战斗加减速后的speed。',
'LEVEL查询无实参的allSameSideBattlers，默认为侧0存活场上（含实际伙伴，不含后备），最高等级依≥4倍/≥2倍/>分别×8/4/2，再上限255。',
'LURE需encounter_type非空且登记类别fishing，新5/旧3，再上限255；不是仅凭环境水域。',
'HEAVY先有效战斗重量（0.1kg），新≥3000+30/≥2000+20/<1000−20、中档不变；旧≥4096+40/≥3072+30/≥2048+20/其余−20。',
'HEAVY输入率0立刻0；非零依重量加减后钳[1,255]。重量先当前形态+变化下限1，再有效能力（模式破坏者可抑制）/道具，最终下限1。',
'LOVE同LEVEL的侧0存活集合，存在同物种且两者非无性别并异性别才×8一次，之后255取小。',
'MOON须已登记MOONSTONE，检查基础幼体起整家族演化中使用物品的方式及参数；命中×4再上限255，不要求该个体当前可进化。',
'“上限255”只限FAST/LEVEL/LURE/HEAVY/LOVE/MOON六个处理器的具名出口，HEAVY另有0早返/下限1；其它倍率球不统一钳255，不能原样作全族断言。'],
79:[
'SPORT×1.5，无其它模式资格由本handler暗加，也无局部255钳。',
'DREAM调用asleep?→pbHasStatus，真实睡眠或合格KOMALA/COMATOSE皆可×4；和捕获公式真实状态倍率分开。',
'BEAST对UltraBeast×5，否则除10；物种整数率45变4，不是4.5；若显式浮点率则保其除法类型；与非BEAST异兽前置互斥。',
'HEAL成功handler调用个体heal：非蛋回HP/清状态及计数/全PP，并清ready_to_evolve；不是只治HP，蛋早返。',
'FRIEND成功设happiness为软上限开150、关200；固定默认AFFECTION_EFFECTS=false→软上限关200。',
'固定全部脚本注册搜索只见四表中的1/19/2项，OnFailCatch为0；无默认失败附效不能补成官方系列规则；不推出无界插件也为空。']}

deps = {60:['R-SIM','R-AI','R-COMMAND','F-76'],61:['R-SIM','R-AI','R-COMMAND','F-76'],62:['R-BATTLE','R-BATTLER','R-SWITCH','R-COMMAND','R-AI','R-SIM','F-76'],
63:['R-PEER','R-STORAGE','R-SCENE-MENUS','R-SCENE-COMMAND','R-SETUP','R-DEFAULTS','R-OPTIONS','R-POKEMON','R-PARTY-UI','R-TEXT','F-U10','F-39','F-42'],
64:['R-BATTLE','R-DEX','R-PLAYER','R-SCENE-MENUS','R-DEX-UI','R-END','F-62'],
65:['R-BATTLE','R-BATTLER','R-ITEM','R-ITEM-HANDLERS','R-ITEM-BALL-REG','R-ATTACK-ITEM','R-RESET','R-EXP','R-SCENE-CAPTURE','R-CAPTURE-ANIM','R-AUDIO','R-END','F-42'],
66:['R-SETTINGS','R-DEX','R-BATTLE','R-BALL','R-SLEEP','R-ABILITY','R-COMMAND'],
76:['R-HANDLER','R-CATCH','R-PBS-BALLS'],77:['R-CATCH','R-SETTINGS','R-SETUP','R-BATTLER','R-PLAYER','R-DEX'],
78:['R-CATCH','R-SETTINGS','R-SPECIES','R-BATTLER','R-ABILITY','R-ITEM-WEIGHT','R-POKEMON','R-BATTLE'],
79:['R-CATCH','R-SLEEP','R-ABILITY','R-POKEMON','R-SETTINGS','R-PBS-BALLS']}
group_reason={
60:'WP67-A3.6与WP76§7.2给直接辅助和真实AI模拟分流；无视觉定义不等于完整宿主等价。',
61:'恒值返回与日志直接见完整Debug类；正式3.6和WP76列相同结果，不以这些值替代玩家UI。',
62:'缺失move负证据与实际moves访问器/AI caller并读；正常模拟旁路，目标/换人有限随机辅助须caller校验，现文已写。',
63:'WP38§6、WP67-A§8.2/8.3与U10-CP01–09逐阶段吻合；正常、去向取消、选人取消、消息异常、存盒失败前缀不同。',
64:'WP38§6与WP62§3.1保持包装门/直接写入、三条件页面、逐只清队列和失败前缀；不要求事务或自动重试。',
65:'WP38§2/5与WP67-A§8.1保留消息/阻挡/捕获/经验/接收次序；原断言过简处按received_meaning限定，静态调用/已登记扣减/最终UI分列。',
66:'WP38§3全文及CP01–14/24对照公式、floor、严格比较和随机消耗；无静态差异证据，不继承旧PASS。',
76:'WP38§4四族与实际原生handler定义吻合；nil-only回退、通知和失败统计先写需保持，不把工具结构变未来API。',
77:'WP38§4逐球表和CP07–12对照全部新旧值/开关/receiver；无统一255钳制；默认值由固定世代8设置核对。',
78:'WP38§4逐球输入集合/有效重量单位/家族与CP09–11/23已覆盖；A08必须限具名六族，属证据限定而非新正式必修。',
79:'WP38§3/4/8区分真实状态与视为睡眠、整数率、成功heal/友好与空失败族；其它生命周期交相应primary不重审全域。'}
primary = {'60':'R-DEBUG','61':'R-DEBUG','62':'R-DEBUG','63':'R-CATCH','64':'R-CATCH','65':'R-CATCH','66':'R-CATCH','76':'R-BALL','77':'R-BALL','78':'R-BALL','79':'R-BALL'}
receipts=[]
for obj in data['primary_objects']:
    number=int(obj['group'].split('F')[-1]); i=int(obj['id'].split('.A')[-1])-1
    receipts.append(dict(id=obj['id'],original_complete_object=obj,
        received_meaning=meaning[number][i],actual_reader=session,
        source_read=primary[str(number)],necessary_units=deps[number],
        formal_read=['F-67'] if number in (60,61,62) else ['F-38','F-CP']+(['F-67'] if number in (63,64,65) else []),
        comparison_reason=group_reason[number],status='RECEIVED_FINITE_WITH_EXPLICIT_MEANING',
        required_formal_revision_supported=False,open_necessary_units=[],evidence='SOURCE_STATIC / FORMAL_TEXT; NOT_EXECUTED'))
assert len(receipts)==64 and len(set(x['id'] for x in receipts))==64
assert sum(len(x) for x in meaning.values())==64
save('reception-ledger.json',dict(schema='r8-cp05-reception/v1',status='READY_FOR_PARENT_RECEPTION',
    denominator=64,received=64,unread_primary=0,necessary_unreceived=0,records=receipts,
    semantic_credit_not_from_assembler=True,original_payloads=input_proofs,
    GR8_EXTCP_002='OPEN; original proposal read completely; no independent counterreview/root adjudication adopted by this bounded job.',
    UPDATE_NOT_STARTED=True))

reverse_reasons = {
'EXTCP-R005':['R-DEBUG→F-67§3.6：确认/命令/物品/遗忘各恒值，日志门独立。','R-DEBUG：先Bag1/15，再剩余Call1/10，普通对照Fight。','R-DEBUG/R-BATTLER：单数move缺定义；读取失败在rand/yield之前。','R-SIM/R-COMMAND/R-AI/F-76：controlPlayer真旁路辅助，不能据辅助异常推整个模拟失败。'],
'EXTCP-R015':['R-CATCH：brief投掷消息先于训练家阻挡，已注册合法球/目标前提。','R-CATCH/R-BALL：0–3失败消息后统计与回调；4成功；早返不混入失败球。','R-CATCH/R-BATTLE/R-EXP/R-RESET：移出→临时captured经验→复位/结果→球与离场→队列，后继失败保前缀。','R-CAPTURE-ANIM完整构造：success先取numShakes≥4，之后crit正摇数压成1，仅展示。','R-SCENE-CAPTURE/R-AUDIO：对手训练家存在即早返；野生ME正常请求、按uptime等≥3.5后停，不是媒体时长实测。'],
'EXTCP-R016':['R-CATCH/R-DEX/R-BATTLE/F-62：未拥有/持图鉴/已解锁三门；拥有写入不受展示门。','R-CATCH/R-POKEMON/R-SCENE-MENUS：命名值先提交；空名归默认后再去向/存储。','R-CATCH/R-SCENE-COMMAND/R-SCENE-MENUS：0初始游标与99取消返回分列；2移送盒项/禁止取消。','R-CATCH/R-PEER/R-STORAGE：同一旧对象存盒成功先于删除；满盒失败早于删除。','R-CATCH/F-U10：暂停消息后才四记忆左移；新入队消息后回填；终局按现记录恢复。','R-SETUP/R-BATTLE/R-END/F-39/F-42：实际伙伴才新建参与集合并共享成员，后来玩家删除/追加不改变旧集合；按旧索引读移位记录可错配。'],
'EXTCP-R025':['R-CATCH/R-BALL/R-SLEEP/R-ABILITY：HP/真实状态、球率和异兽先除十顺序，Dream另用视为睡眠。','R-CATCH/R-DEX/R-SETTINGS：critical严格档与护符，c>0门；普通首次失败停止，不必耗尽四次。','R-BALL/R-PBS-BALLS：全部19率+1无条件+2成功+0失败登记，26球与4无登记逐项核实。','R-CATCH/R-BATTLE/R-DEX/R-SCENE-MENUS：逐个体计数/已见/拥有/暗影→命名→存储→最终clear。','R-PEER/R-STORAGE/R-CATCH/F-U10：菜单双满预检与直接兜底分开；缺失Peer消息入口错误先于正常返回/删队。','R-SETUP/R-END/F-42：实际伙伴的旧合并身份与移位记录导致CP21/22错配；无伙伴同步集合为普通对照。']}
reverse=[]
for group in data['reverse_current_contribution_objects']:
    checks=[]
    for atom, reason in zip(group['subassertions'],reverse_reasons[group['id']],strict=True):
        checks.append(dict(original=atom,received_meaning_and_join=reason,status='RECEIVED_FINITE',execution='NOT_EXECUTED'))
    reverse.append(dict(original_complete_group=group,checks=checks,full_foreign_formal_credit=False))
save('interfaces.json',dict(schema='r8-cp05-interfaces/v1',actual_reader=session,
    old_reverse_groups=4,old_reverse_subassertions=21,received_subassertions=21,
    reverse=reverse,
    selected_reverse_interfaces=[dict(original=data['selected_reverse_interfaces'][0],
        received_meaning='成功投球4→pbThrowSuccess；battle.opponent真即return，野生清brief/请求捕获ME/uptime等待至少3.5秒/stop。回调异常不保证停声，无真实音频或墙钟观察。',
        definitions=['R-CATCH','R-SCENE-CAPTURE','R-AUDIO'],formal=['F-67'],status='RECEIVED_FINITE')],
    supplementary_mandatory_facts=dict(full_text_read=True,
        adopted={'RX-HANDLER':'Directly verified R-HANDLER; rawadd and empty subclasses corrections required.'},
        not_adopted=['RX-ABILITY-DISPATCH','RX-ITEM-DISPATCH','RX-MOVE-BASE','RX-MOVE-USAGE','RX-SCENE-REFRESH','RX-SCENE-HP','RX-SCENE-ILLUSION'],
        disposition='Other seven whole receipts not needed for this bounded job and remain job06/primary responsibility. Necessary Weight/COMATOSE definitions directly read here; no whole Battler/provider credit.'),
    broader_31_150_20_66_population='Not accepted in this job; only the exact4/21+1 selected objects above. Parent/job06 owns cumulative reception.',
    open_necessary_units=[],global_task_final='OPEN_ROOT_ONLY',UPDATE_NOT_STARTED=True))

save('evidence/identity-validation.json',dict(schema='r8-cp05-validation/v1',utc=utc,
    checks=dict(contract_prompt_readset=True,all31_recovered_identities=True,all64_origin_pointer_equal=True,
                all64_source_identities=True,exact64_contract_ids=True,formal_tree_equals_B8=True,
                distinct_actual_context=True),
    counts=dict(primary_groups=11,primary_objects=64,old_reverse_groups=4,old_reverse_subassertions=21,selected_interfaces=1),
    semantics_credit=0,reference_model_host_executions=0,UPDATE_NOT_STARTED=True))
print(json.dumps(dict(status='ASSEMBLED_IDENTITY_CHECKS_OK',receipts=len(receipts),reading_entries=len(reads),context=session),ensure_ascii=False))
