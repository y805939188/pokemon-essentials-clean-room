"""Assemble explicit human reception decisions; validate identities, never infer semantic PASS.

New review tool. Reads fixed inputs and the hand-authored 130-row decision table.
Writes only this script's directory. Does not execute reference or recovered programs.
"""
import csv
import hashlib
import json
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
REPO = next(p for p in OUT.parents if (p / 'AGENTS.md').is_file())
BASE = REPO / 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
TASK = BASE / 'tasks/receive_external_combat_presentation'
R = Path('/workspace/pokemon-essentials')
CONTRACT = '35d85e4484b892ebc32542346861440638d2183c'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
TARGET = '18d21310bdc360c87d7ffd886df7d06aef8604a7'
READSET_PATH = TASK / 'continuation/03_fixed_choreography/readset.complete.json'
D = json.loads(READSET_PATH.read_text())
UTC = datetime.now(timezone.utc).isoformat()


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args])


def digest(data):
    return hashlib.sha256(data).hexdigest()


def identity(root, commit, path):
    data = (root / path).read_bytes()
    fixed = git(root, 'show', f'{commit}:{path}')
    assert data == fixed, ('working-input-differs', path)
    mode, typ, blob, _ = git(root, 'ls-tree', commit, '--', path).decode().strip().split(None, 3)
    assert typ == 'blob'
    return dict(repo=str(root), commit=commit, path=path, mode=mode,
                git_blob=blob, bytes=len(data), sha256=digest(data), lines=len(data.splitlines()))


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


# Units below are explicit actual readings, not the original author's FULL_READ claims.
# [a,b] means all lines inclusive; unrelated prefixes seen in a view receive no complete-unit credit.
scene = 'Data/Scripts/011_Battle/004_Scene/'
battle = 'Data/Scripts/011_Battle/001_Battle/'
units = []


def unit(key, root, commit, path, intervals, output_ids, meaning):
    ident = identity(root, commit, path)
    lines = (root / path).read_bytes().splitlines(keepends=True)
    spans = []
    for a, b in intervals:
        assert 1 <= a <= b <= len(lines)
        raw = b''.join(lines[a-1:b])
        spans.append(dict(lines=[a, b], bytes=len(raw), sha256=digest(raw)))
    units.append(dict(id=key, identity=ident, actual_read_intervals=intervals,
                      exact_recoverable_views=spans, actual_platform_output_chunk_ids=output_ids,
                      semantic_credit='FINITE_COMPLETE_UNITS_ONLY', meaning=meaning,
                      replay='git -C <repo> show <commit>:<path> | sed -n <a>,<b>p; verify identity before reading'))


unit('S-PLAY', R, RC, scene+'004_Scene_PlayAnimations.rb', [[1,406]], ['50c473','69712d'],
     '全部本组场景入口完整：Intro/lineup/opponent/sendout/recall/splash/HP/damage/EXP/level/faint/capture/hide/deflect/shadows；407以后动画库查找不授完整阅读。')
unit('S-FIXED', R, RC, scene+'008_Battle_Scene_Animations.rb', [[1,849]], ['69712d','ab7742','844cc8'],
     '完整固定演出文件及构造、排期、全部结束条件；逐ID分母以130表为准。')
unit('S-BASE', R, RC, scene+'007_Battle_Scene_BaseAnimation.rb', [[1,253],[349,456],[569,823]], ['0ce191','95e4ab','bb2516'],
     '完整公共驱动、RGB选择/手位/轨迹/滚球/开闭/出现吸入、release/capture burst、成功星/recall；两张差异表字段主责留02，不授496字段额外接收。')
unit('S-PICTURE', R, RC, 'Data/Scripts/005_Sprites/010_PictureEx.rb', [[1,548]], ['0ce191','95e4ab','bb2516'],
     '完整排期、属性、首次更新起钟、当前起点捕获、同刻顺序、回调、音频交付、sprite量化与裁底；无实际像素观察。')
unit('S-SCENE', R, RC, scene+'001_Battle_Scene.rb', [[1,150],[375,419]], ['e98170'],
     '完整坐标、队列更新/清理、输入abort、frame更新、refresh/换图；151后窗口片段不计，给定普通更新/资源前提。')
unit('S-INIT', R, RC, scene+'002_Scene_Initialize.rb', [[1,94]], ['e98170','7b5f16'],
     '初始化、start和pbInitSprites完整；野生位图来自真实party，后续sendout才另选Illusion；95后背景定义不计。')
unit('S-CRY', R, RC, 'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb', [[183,246]], ['e98170'],
     '完整叫声候选/播放/长度；suffix文件选择不自动去suffix，长度helper可回标准；正pitch除以pitch/100。')
unit('S-LERP', R, RC, 'Data/Scripts/001_Technical/002_RubyUtilities.rb', [[390,406]], ['e98170'], '完整nil_or_empty与线性插值，端点/非正时长归一。')
unit('S-HP-FAINT', R, RC, 'Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb', [[1,98]], ['9e9fc'],
     'HP扣减/恢复、drain、effect和正式faint完整；HP先写、显示后才记录部分标志；faint领域清理在演出后。')
unit('S-BATTLER', R, RC, 'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb', [[105,112],[177,205]], ['9e9fc','661887'],
     '完整HP setter/fainted?及display属性/shiny/super/owned有限getter；不继承Battler整文件或动态Pokemon纯度信用。')
unit('S-OWNERS', R, RC, battle+'001_Battle.rb', [[215,257],[303,319],[820,867]], ['9e9fc','62ff91'],
     '完整玩家/属主分段/party路由/显示包装/动画门/特性条延时；不审整个战斗对象。')
unit('S-SWITCH', R, RC, battle+'005_Battle_ActionSwitching.rb', [[220,299]], ['9e9fc'],
     '完整recall-replace、消息、替换和sendOut；场景正常返回后才复位命令下标/seen/used。')
unit('S-START', R, RC, battle+'002_Battle_StartAndEnd.rb', [[1,6],[170,317]], ['661887','c94fe6'],
     '完整abort、开场消息及对方先玩家后sendout、start捕获中止和core；317结束行补读，不给参与者/主循环外域信用。')
unit('S-EXP', R, RC, battle+'003_Battle_ExpAndMoveLearning.rb', [[1,271]], ['1f9776','f1b9b6'],
     '完整EXP/EV/gainOne/learnMove，必要显示的写入/刷新/两窗/学招与Shadow消息门；不等于全成长领域审查。')
unit('S-CAPTURE', R, RC, 'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb', [[112,271]], ['f1b9b6','b89452'],
     '完整pbThrowPokeBall/pbCaptureCalc及mixin接入：producer产0..4，critical判定与动画压缩分离；只消费112以后，不授战后存放定义。')
unit('S-BOX', R, RC, scene+'006_Battle_Scene_Objects.rb', [[1,77],[158,204],[301,412],[548,607]], ['661887','1f9776','f1b9b6'],
     '完整框配置/HP/EXP查询与启动、补间更新/位置/主update；成员坐标/setBitmap/intro callback；未读的绘字/其余update不计。')
unit('S-TOP-WINDOW', R, RC, 'Data/Scripts/013_Items/001_Item_Utilities.rb', [[206,221]], ['1f9776'], '两次升级窗的完整共享消费者，只USE退出、正常dispose，没有BACK取消或异常ensure。')
unit('S-ICON', R, RC, 'Data/Scripts/007_Objects and windows/007_BitmapSprite.rb', [[1,243]], ['6d8a8e'], '完整IconSprite、BitmapSprite等文件，名称换图前清旧图及AnimatedBitmap委托；不承诺加载失败回滚。')
unit('S-BITMAP', R, RC, 'Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb', [[1,228]], ['a7595a'], '普通GifBitmap捕获缓存普通加载异常并32×32占位；nil入口、前缀PNG校验/失败分支不同。')
unit('S-CACHE', R, RC, 'Data/Scripts/007_Objects and windows/001_RPG_Cache.rb', [[1,144]], ['a7595a'], '完整直接cache与引用行为，无非空文件通用rescue；宿主Bitmap未执行。')
unit('S-AUDIO', R, RC, 'Data/Scripts/008_Audio/002_Audio_Play.rb', [[1,39],[102,141],[202,233]], ['a7595a'], '完整参数解析/ME播放停止/SE播放停止必要定义；系统/RPG/native后备路由和异常边界分列。')
unit('S-AUDIO-SYSTEM', R, RC, 'Data/Scripts/004_Game classes/002_Game_System.rb', [[153,166],[237,249]], ['62ff91'], '系统ME与SE完整：文件门、选项音量缩放、真实Audio请求；ME有帧重置，SE没有对应尾部请求。')
unit('S-AUDIO-RESOLVE', R, RC, 'Data/Scripts/001_Technical/002_Files/001_FileTests.rb', [[109,115]], ['62ff91'], '完整专用SE解析；nil早返、候选扩展名及RTP委托；不证明物理素材存在。')
unit('S-CAPTURE-ME', R, RC, 'Data/Scripts/019_Utilities/003_Utilities_BattleAudio.rb', [[40,58]], ['62ff91'], '完整捕获ME：预置clone优先，再地图/全局/默认，回退名加相对ME路径；消费时仍须播放入口正常。')
unit('S-SETTINGS', R, RC, 'Data/Scripts/001_Settings.rb', [[1,17],[128,140],[215,223],[432,441]], ['7b5f16','62ff91'], '世代8、super shiny门、队伍6、默认512×384；其它Settings未授全文信用。')
unit('S-BATTLE-SETTINGS', R, RC, 'Data/Scripts/002_BattleSettings.rb', [[1,140]], ['b89452'], '完整设置文本阅读；这里只接critical默认开及capture经验默认开的配置，不扩大规则验证。')
unit('S-PLAYTIME', R, RC, 'Data/Scripts/008_Audio/001_Audio.rb', [[70,81]], ['b89452'], '完整公开getPlayTime：字面路径及wav/mp3/ogg和负值夹0；内部格式解析未授信用，三分支1秒只是给定helper返回前提。')
fp = 'deliverables/final-specification-set/'
unit('F-67', REPO, B8, fp+'user-interface/wp67-a-battle-interaction-and-presentation.md', [[1,49],[190,218],[236,271]], ['3c799e','95193d','c94fe6'],
     '完整相关目的/范围/概念、3.2开场、7.1/7.2显示、8.1捕获、9.1至9.4等待/失败/正常恢复条款；不是348行全文或UI全域主责。')
unit('F-74', REPO, B8, fp+'demo-dx/wp74-battle-animation-authoring-and-exchange.md', [[1,35],[297,355]], ['95193d'],
     '目的/范围/非目标及完整相关作者timing/共享播放器条款；WP74前向不能自动支持固定PictureEx所有坐标。其余作者工具外域不重审。')
unit('F-16', REPO, B8, fp+'engine-overworld/wp16-world-rendering-and-visual-transitions.md', [[1,27],[291,316]], ['95193d'], '范围及完整6.3排期/首次起钟/相对动作/聚合额外更新；不授世界全域批准。')
unit('F-15', REPO, B8, fp+'engine-overworld/wp15-resource-matching-and-audio.md', [[1,29],[104,190]], ['f66535','7b5f16'], '目的/范围及完整5.1失败表、5.2、6.1至6.4相关条款；未读6.4.1全表不授音频格式解析信用。')
unit('F-38', REPO, B8, fp+'pokemon-rules/wp38-capture-and-receiving.md', [[31,46],[81,103]], ['c94fe6'], '完整捕获数学段和成功提交表，只接摇数/critical与表现提交交界，不复审全部球效果/接收。')
unit('F-SCOPE', REPO, B8, fp+'scope-statement.md', [[1,42],[88,128]], ['62ff91','50e02b'], '历史状态按原时点保留，范围/媒体/素材/执行未知分列；不是数值轨道已经获得排除政策的凭据。')
unit('F-TEST', REPO, B8, fp+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md', [[360,403]], ['50e02b'], '实际读该连续范围；只核K22/23/29/30/31/35和R7-U08-HP01..04本组相关显示/提交预期，其余上下文不授领域PASS。')

decisions = list(csv.DictReader((OUT/'semantic-decisions.tsv').open(), delimiter='\t'))
assert len(decisions) == 130
by_id = {r['id']: r for r in decisions}
assert len(by_id) == len(decisions)
assert set(by_id) == {o['id'] for o in D['primary_objects']}
allowed = {'SOURCE_CONFIRMED','SOURCE_CORRECTED','SOURCE_QUALIFIED'}
assert all(r['decision'] in allowed and r['independent_meaning_and_reason'] for r in decisions)

# Reuse the fixed, inert recovery. This is an identity check, not new semantic credit.
rawroot = TASK/'recovered'/TARGET
reused = []
for item in D['original_complete_readset']['files']:
    p = rawroot/item['relative_to_target_task']
    raw = p.read_bytes()
    assert len(raw) == item['bytes'] and digest(raw) == item['sha256'], p
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == item['git_blob'], p
    reused.append(dict(item, actual_reused_path=str(p.relative_to(REPO)),
                       verification='MATCHED_ALL_LISTED_BYTES_SHA256_BLOB; prior remote provenance reused'))
assert sum(x['bytes'] for x in reused) == 1628507 and len(reused) == 31

atom = json.loads((rawroot/'atomic-assertions.json').read_text())
forward = json.loads((rawroot/'forward-mapping.json').read_text())
reverse = json.loads((rawroot/'reverse-mapping.json').read_text())
assert all(atom['assertions'][int(o['origin_pointer'].rsplit('/',1)[1])] == o['meaning'] for o in D['primary_objects'])
for selected, original in [(D['source_groups'], forward['facts']),
                           (D['reverse_current_contribution_objects'], reverse['clauses']),
                           (D['selected_reverse_interfaces'], reverse['selected_interface_assertions'])]:
    original_by_id = {x['id']: x for x in original}
    assert all(original_by_id[x['id']] == x for x in selected)
assert json.loads((rawroot/'proposals.json').read_text()) == D['original_proposal_full']

core_inputs = [
    'AGENTS.md', str((BASE/'inputs/eighth-global-review-prompt.md').relative_to(REPO)),
    str((BASE/'inputs/review-SKILL.md').relative_to(REPO)),
    str((TASK/'continuation-contracts.json').relative_to(REPO)),
    str((TASK/'continuation/03_fixed_choreography/prompt.zh.md').relative_to(REPO)),
    str(READSET_PATH.relative_to(REPO)),
]
input_ids = [identity(REPO, CONTRACT, x) for x in core_inputs]
prompt = (TASK/'continuation/03_fixed_choreography/prompt.zh.md').read_text()
for leaf in ['eighth-global-review-prompt.md', 'review-SKILL.md']:
    assert (BASE/'inputs'/leaf).read_text().strip() in prompt

reception = []
for obj in D['primary_objects']:
    row = by_id[obj['id']]
    n = int(obj['group'].split('F')[-1])
    group_detail = n >= 51
    reception.append(dict(id=obj['id'], original_complete_object=obj,
                          independent_decision=row['decision'],
                          current_effective_meaning=row['independent_meaning_and_reason'],
                          actual_source_units=['S-PLAY' if n < 51 else 'S-FIXED'],
                          necessary_joint_units=['S-BASE','S-PICTURE','S-SCENE'],
                          current_formal_units=['F-67','F-16'] + (['F-74','F-15'] if group_detail else []),
                          formal_credit=('SOURCE_DETAIL_RETAINED_HIGH_LEVEL_JOIN_ONLY; exact numeric retention is not adjudicated by this receipt'
                                         if group_detail else 'FINITE_INTERFACE_SUPPORTED; see each independent qualification and precise source unit'),
                          formal_locator_preserved=obj['meaning']['formal_links'],
                          final_canonical_credit=0, execution='SOURCE_STATIC_NOT_EXECUTED'))

joins = {
 'EXTCP-IR001': ('SUPPORTED_FINITE', ['S-PLAY','S-FIXED','S-INIT','S-START','S-BATTLER','S-SETTINGS','S-OWNERS'],
                 '基础Intro阻塞；训练家full排列异步；野生框/Intro2等队列；shiny与super门独立，野生初图和sendout Illusion分开。'),
 'EXTCP-IR003': ('SUPPORTED_NORMAL_ONLY', ['S-BASE','S-FIXED','S-ICON'],
                 'addSprite借用不进入tempSprites；addNewSprite才进入；成功球先移出临时表，普通dispose只销毁余项。异常不保证走dispose。'),
 'EXTCP-IR004': ('SUPPORTED_FINITE', ['S-PLAY','S-FIXED','S-SCENE'],
                 'fade/各球同轮，框等自己的球；退出谓词只查框及队列，不额外等fade标志。'),
 'EXTCP-IR005': ('SUPPORTED_FINITE', ['S-PLAY','S-FIXED','S-CRY','S-BASE'],
                 'recall先球后框；faint与框共同推进。75音高与crop细节是补充源事实，不能扩大该高层条款覆盖。'),
 'EXTCP-IR006': ('SUPPORTED_FINITE', ['S-PLAY','S-FIXED','S-BOX','S-HP-FAINT'],
                 '先HP提交，所有目标HP条和闪烁均结束才正常返回；动画门不关闭HP等待，显示异常保已有提交。'),
 'EXTCP-IR007': ('SUPPORTED_FINITE', ['S-PLAY','S-FIXED','S-SCENE'], 'pbThrow显式同时检查自身animDone与inPartyAnimation为空；队列由pbUpdate推进。'),
 'EXTCP-IR008': ('SUPPORTED_FINITE', ['S-PLAY','S-FIXED','S-CAPTURE'], '领域先投掷brief，再挡球阻塞，再阻挡消息返回；挡球不吸入或捕获。'),
 'EXTCP-IR009': ('SUPPORTED_NORMAL_ONLY', ['S-PLAY','S-FIXED','S-BASE','S-LERP','S-CAPTURE'],
                 '成功dispose保留球供隐藏入口；球1秒淡出与框退场共同等，隐藏入口不销毁球；缺球早返，异常无共同回滚。'),
 'EXTCP-IR010': ('SUPPORTED_FINITE', ['S-PLAY','S-CAPTURE','S-CAPTURE-ME','S-AUDIO','S-AUDIO-SYSTEM'],
                 '仅无opponent请求选曲ME、按运行钟等待>=3.5再停；不是声音已发出的观察。'),
 'EXTCP-IR012': ('PENDING_ROOT_SCOPE_DECISION', ['S-FIXED','S-BASE','S-CRY','F-67','F-74','F-16','F-15'],
                 '9.4在招式/公共动画失败段明确不转录逐帧坐标/轨迹/作者格式；74说明共享作者库合同。不能从该前向证明固定轨道每个参数已覆盖，也不能从未转录证明每个参数必修。GR8-EXTCP-002范围/音频75保真边界仍原canonical待主审。'),
 'EXTCP-IR015': ('SUPPORTED_FINITE', ['S-PICTURE','S-BASE','S-LERP'], '每轨首次实际update才建t0，20单位每秒是请求时基；构造后延迟启动不快进。'),
 'EXTCP-IR016': ('SUPPORTED_FINITE', ['S-PICTURE','S-FIXED'], '各图process按登记顺序；同刻先隐藏再opacity恢复，不重新可见。'),
 'EXTCP-IR017': ('SUPPORTED_FINITE', ['S-PICTURE','S-LERP','S-FIXED'], '首次实际处理在该顺序处捕获起值、DELTA据此定终点，迟到进度仍用计划时点；floor增量不改写为最终位置。'),
 'EXTCP-IR018': ('SUPPORTED_FINITE', ['S-PICTURE','S-BASE','S-PLAY'], '各PictureEx独立t0；聚合在某次开头无running项才完成，不推固定多0.05秒或全域额外帧。'),
 'EXTCP-IR019': ('SUPPORTED_FINITE', ['S-ICON','S-BITMAP','S-CACHE'], '普通GifBitmap捕获普通加载异常；nil明确失败，前缀PNG/直接cache另有边界；不能把所有资源缺失写成静默空白。'),
 'EXTCP-IR020': ('SUPPORTED_REQUEST_BOUNDARY', ['S-CRY','S-AUDIO','S-AUDIO-SYSTEM','S-AUDIO-RESOLVE','S-PICTURE'], 'SE登记/参数解析/系统文件门/缩放/宿主请求分开，cry_length除音高是估计规则；不签音频已播放、像素或实际时长。'),
}
assert set(joins) == {x['id'] for x in D['selected_reverse_interfaces']}
interfaces = []
for obj in D['selected_reverse_interfaces']:
    status, keys, reason = joins[obj['id']]
    interfaces.append(dict(id=obj['id'], original_complete_interface=obj,
                           independent_status=status, actual_complete_units=keys,
                           independent_join=reason, whole_source_group_credit=False,
                           execution='NOT_EXECUTED'))

subnotes = {
 'EXTCP-R001.1':'S-START170–242对方先/玩家消息最后；野生不做对手sendOut，F-67 3.2支持。',
 'EXTCP-R001.2':'S-PLAY及S-OWNERS双层门；Illusion shiny与自身super分列，F-67 3.2/2支持。',
 'EXTCP-R001.3':'S-INIT完整建框/野生初图、S-PLAY等待，F-67 3.2支持。',
 'EXTCP-R013.1':'S-EXP pbGainExpOne受showMessages，全部Shadow跳普通循环；普通pbGainExp给Shadow false，不能称所有自然路径均有经验消息。',
 'EXTCP-R013.2':'S-EXP190后先写pkmn.exp再pbEXPBar；F-67 7.1写入时点支持。',
 'EXTCP-R013.3':'S-BOX初建玩家单席门、1.75比例及.2闪光完整；F-67 7.1/9.2支持正常初建前提。',
 'EXTCP-R013.4':'S-EXP/PLAY/TOP-WINDOW完整支持逐级重算刷新/消息/两窗仅USE/学招；共享窗未传scene参数。',
 'EXTCP-R015.1':'S-CAPTURE投掷brief在训练家挡球之前，F-67 8.1支持正常有效目标路径。',
 'EXTCP-R015.2':'S-CAPTURE完整producer普通0..4、critical0/4，consumer仅4成功；F-38 3/F-67 8.1支持，不外推任意直接numShakes>=4。',
 'EXTCP-R015.3':'S-CAPTURE正常成功后顺序与F-38 5/F-67 8.1一致，演出/经验失败保此前缀，不由本组证明深层回调结果。',
 'EXTCP-R015.4':'critical展示压1由S-FIXED构造独立证明；F-38规定判定0/4，F-67 8.1本段未明确写展示压1。只接源接口补充，不把它计成该formal clause已逐字段覆盖。',
 'EXTCP-R015.5':'S-PLAY投掷成功与ME选择/播放完整，F-67 8.1/9.3支持野生3.5秒请求等待；无音乐/声音运行证明。',
 'EXTCP-R019.1':'S-PLAY各框等自己球且队列空，F-67 9.3支持。',
 'EXTCP-R019.2':'S-PLAY收回完整先球再框，F-67 9.3支持。',
 'EXTCP-R019.3':'S-PLAY特性条门及各自阻塞，F-67 9.2/9.3支持，不由showAnims统一关闭。',
 'EXTCP-R019.4':'S-FIXED610–657支持高度裁切与叫声三分支；F-67 9.3只写叫声/下落/框，未写高度裁切参数。作为源补充接收，收窄反向文字覆盖信用。',
 'EXTCP-R019.5':'S-FIXED正常dispose与S-PLAY隐藏入口接合，F-67 9.3正常球生命周期支持。',
 'EXTCP-R019.6':'S-PLAY pbSaveShadows正常恢复、无ensure；正式支持位置应补F-67 9.4第267/271行，不能仅以9.3范围冒充此条正文。',
}
reverse_receipts=[]
for group in D['reverse_current_contribution_objects']:
    for a in group['subassertions']:
        key=a['id']
        state=('SOURCE_SUPPLEMENT_NOT_LITERAL_FORMAL_COVERAGE' if key in ['EXTCP-R015.4','EXTCP-R019.4']
               else 'SUPPORTED_WITH_FORMAL_LOCATOR_CORRECTION' if key=='EXTCP-R019.6' else 'SUPPORTED_FINITE')
        reverse_receipts.append(dict(id=key, original_subassertion=a, original_parent=group['id'],
                                     formal=group['formal'], original_range=group['range'],
                                     independent_status=state, independent_reason=subnotes[key]))
assert len(reverse_receipts)==18 and set(subnotes)=={x['id'] for x in reverse_receipts}

independence=dict(role='03_fixed_choreography delegated actual receiver; no self-spawn',
                  source_parent_thread='01a13f49-a154-7054-9b04-ce31f924d01c',
                  original_author_context='01a143b2-8ba3-76f5-a39d-7904a2dd1000',
                  parent_receiver_context='Not asserted as this receiver; fixed contract read as input only',
                  actual_opaque_context_id='UNVERIFIED; source_thread_id is parent provenance, not invented receiver UUID',
                  independent_basis='Separate delegated execution environment and current review turn; no author/parent assertions inherited as votes',
                  git_author='Existing Shin Ding / y805939188@gmail.com reused',
                  requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default normal',Fast='off'),
                  actual=dict(model='UNVERIFIED',effort='UNVERIFIED',tier='UNVERIFIED',speed='UNVERIFIED',Fast='UNVERIFIED'),
                  self_spawn_count=0, invented_votes=0)
incidents=[
 dict(chunk='d4bec7',result='New identity/assembly tool first runexit1: declared capture range ended274 but fileEOF271; actual reading had already reached EOF271. Corrected ledger range to112–271, no source or specification mutation, no behaviour execution.'),
 dict(chunk='e2b11c',result='Initial broad rg file inventory truncated; no whole-file credit; replaced by exact fixed readset'),
 dict(chunk='c9ad46',result='git invoked at /workspace outside repository; exit128; corrected cwd'),
 dict(chunk='3bb501',result='Initial combined contract/prompt/readset output truncated; no credit for omitted text; repaired by structured complete sections and consecutive semantic object views'),
 dict(chunk='138b3d/659ba6',result='Broad navigation output truncated or pre-fetch paths missing; exact fixed files subsequently read'),
 dict(chunk='b931d9/9a84b3/b878a5/c3b54e',result='Large metadata views truncated; primary130 meanings, original31 identities, candidates61, 16interfaces and six-job ID partition re-presented without relying on omitted output; Cartesian 02 aliases structurally shown in50e02b'),
 dict(chunk='25c389',result='Wrong guessed 016_Battle_CatchAndStore.rb path absent; actual005_Battle_CatchAndStoreMixin.rb located and necessary definitions completely read'),
 dict(chunk='b89452',result='Wrong guessed006_RTP.rb absent, overall commandexit2 despite earlier read output; no RTP full credit claimed; necessary SE resolver read at exact path; parser internals not claimed'),
 dict(chunk='7b5f16/cee725',result='Search output truncated; search is navigation/negative-evidence locator only, exact relevant clauses read separately'),
 dict(chunk='c94fe6',result='pbStartBattleCore end317 repaired; earlier170–316 alone not counted as complete core'),
]
counts=dict(source_groups=15,primary_objects=130,source_decisions=dict(Counter(r['decision'] for r in decisions)),
            exact_source_objects_unread=0,necessary_units_unreceived=0,reverse_groups=4,
            reverse_subassertions=18,reverse_statuses=dict(Counter(r['independent_status'] for r in reverse_receipts)),
            selected_interfaces=16,interfaces_fact_joined=15,interfaces_pending_scope_decision=1,
            other_jobs_primary_credit=0,whole_formal_file_credit=0,
            new_required=0,new_optional=0,new_canonical_findings=0,
            existing_candidate_pending=['GR8-EXTCP-002'],all_business_executions=0)

dump('reading-ledger.json', dict(schema='r8-cp03-reading-ledger/v1',utc=UTC,contract=CONTRACT,
     contract_tree=git(REPO,'rev-parse',CONTRACT+'^{tree}').decode().strip(), B8=B8,R=RC,target=TARGET,
     status='FINITE_READING_COMPLETE',independence=independence,counts=counts,input_identities=input_ids,
     reading_method='Full prompt embeds exact global prompt and skill (byte text containment checked); readset completely structurally parsed, shared repeated metadata factored, every130 meaning and all18+16 selected claims actually presented/read; source methods read continuously to end. Tool parses/digests are identity only.',
     units=units,reused_recovery=dict(files=reused,files_count=31,bytes=1628507,new_downloads=0,
          semantic_credit='Only scoped primary objects and explicit relevant wrapper/qualifier content; not31 whole semantic files'),
     original_dependency_candidates=D['all_dependency_identity_candidates'],
     candidate_disposition='All61 locator identities read; only necessary complete units listed above source-checked; others explicitly outside03, not marked limits or PASS.',
     supplement=D['full_battler_supplement'], supplement_disposition='Complete companion text read. HP/Illusion/refresh directness used only where independently joined above. Handler/ability/item/move facts not adopted as new source evidence or counted; their mandatory corrections preserved for06/parent.',
     incidents=incidents,io_limit='Actual source read tool outputs available via listed platform chunk IDs; their full private streams are not claimed published. Fixed path/blob/ranges/view hashes allow exact reconstruction; reconstructed views are not fabricated historical stdout.',UPDATE_NOT_STARTED=True))
dump('reception-ledger.json', dict(schema='r8-cp03-reception/v1',utc=UTC,status='READY_FOR_PARENT_RECEPTION',
     scope='03 only; complete source semantics with explicit corrections, not root task-final or all exact-detail retention policy acceptance',
     counts=counts,records=reception,reverse_current_contribution_objects=D['reverse_current_contribution_objects'],
     reverse_receipts=reverse_receipts,original_proposal_full=D['original_proposal_full'],
     proposal_disposition='Received complete proposal including withdrawn H001; three cry branches independently source checked, root scope/canonical decision remains OPEN. Existing ELR dispatch is not a receipt. No new mandatory root or all-ball-field requirement.',
     UPDATE_NOT_STARTED=True))
dump('interfaces.json', dict(schema='r8-cp03-interfaces/v1',utc=UTC,status='FINITE_FACT_JOINS_COMPLETE_WITH_ONE_SCOPE_DECISION_PENDING',
     records=interfaces,unique_primary_credit=130,shared_group_credit=0,
     exclusions=['No all150 reverse assertions credit','No all20 new interfaces credit','No66 provider facts credit','No all1045 source objects credit','No wholeWP67-A primary credit'],
     UPDATE_NOT_STARTED=True))

report='''# 第八轮固定战斗呈现有限接收 03

本组已完成实质阅读与独立静态接合，状态 **READY_FOR_PARENT_RECEPTION**。固定合同35d85e4484b892ebc32542346861440638d2183c；只写本目录，专用分支codex/r8-cp-reception-03-20261016。B8为fd1df570cad987dc3852a3b958f03916e317f7fe、正式tree f292698cdd4a8e725525a9be6dc34b75faaf151e；R为8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。固定原贡献18d21310bdc360c87d7ffd886df7d06aef8604a7的31份恢复载荷1,628,507B已复用并逐项核对bytes/SHA256/blob；身份不授语义信用。

## 覆盖与可接收范围

15源组、130个精确对象全部实际呈现和逐条核源：127条源事实确认、2条必要澄清、1条源断言更正。不是把130条原文原样全部PASS。连续读完场景本组1–406行、固定轨道1–849行，补齐公共驱动/球helper、完整PictureEx、必要HP/EXP/开场/捕获生产者和消费者、图像失败与音频请求定义。逐对象原始完整意义、原JSON指针、独立具体判断、来源和formal映射保存在reception-ledger.json及手写semantic-decisions.tsv；完整单位、固定身份、读片hash和实际工具输出chunk保存在reading-ledger.json。每条支持均限普通构造、合法数据、无竞争覆写及具名资源/宿主正常返回前提。

本组4旧反向组的18子断言全部核收：15条有限支持、2条作为源补充而不冒充formal逐字覆盖、1条纠正formal定位。16个被选接口已逐事实接合；其中15个支持当前有限请求/正常生命周期，IR012的范围政策仍待主审裁定。重复接口和外组helper没有再增加130主对象信用；没有替父审全部31组/150子断言、全部20接口、66 provider facts、1045对象或131正式文件。61个依赖候选是定位人口，必要完整单位已读，其余明确属其他组，并非“材料不可得”。本组必要可得未读/未接收均0。

## 发现与强制限定

1. **CP03-EVIDENCE-001，原报告源事实错误**：F052.A03把对方排列条写成“基准(0,114)再扣位图宽”。固定R的008_Battle_Scene_Animations.rb 104–109实际先用248再减位图宽，正确为(248−width,114)，球为(174,84)。给定width248时，正确条X0；错误字面会得−248。保留原记录，接收采用更正意义，不改参考或正式规格，也不另造必修canonical。
2. **CP03-EVIDENCE-002，起点/增量澄清**：F051.A03的floor(W/2)是初始相对动作，floor(−W/2)是后续移动增量，不是最终偏移。完整makeSlideSprite→PictureEx相对动作捕获链支持：W513、原X0时先256、最终−1；偶宽512对照最终0。均是静态推导，未执行。不得把第二值直接当终点。
3. **CP03-EVIDENCE-003，训练家身份澄清**：F058.A02捕获演出的trainer来自pbPlayer即player[0]，对应player_1手位，不能泛化成目标或任意席位owner。普通派出则按席位owner取idxTrainer；这两条路径不同。
4. **反向信用收窄**：R015.4的critical展示压1、R019.4的高度裁切有完整源证据，但WP67-A指定8.1/9.3段没有逐字段写这些细节。两条接为源补充，不计formal精度已经覆盖。R019.6正常影子恢复/无ensure的formal支持应接9.4（267/271），不能只标9.3。该修正不等于判正文矛盾，也不自动要求补写全部数值。

## GR8-EXTCP-002 与实际缺口

完整原提案及H001撤回记录均已读并原样保留。当前接收者独立于原CP作者，已核完整BattlerFaint、cry选择/长度、PictureEx/SE与场景共同等待。给定非蛋正常个体、已构造精灵/影子/框、相应资源选择正常且helper文件时长返回精确1秒：专用_faint先选且默认pitch100，开始下落请求ceil(1×20)+2=22；无专用、普通存在时pitch75，ceil((1/.75)×20)+2=29；两者都无结果时10+2=12。无声分支仍请求通用Pkmn faint。声音或框后续异常无共同回滚；HP与其它领域前缀可已提交，正式faint的后续清理发生在场景正常返回之后。

最强反方是WP67-A目的侧重用户阶段/等待，9.4明确不转录逐帧坐标/轨迹/作者格式，WP74只接作者数据库共享播放器，WP15/16接通用音频与图片排期。这足以反对“全部坐标/RGB必须逐项搬入正式正文”的扩张；但这些有限条款也没有把固定倒下75音高选择明确写成已接受的可替代范围政策。范围声明的素材/宿主未知只限制实际输出，不能豁免可读静态请求。故本组核实源事实与有限前向精度疑点，**保留既有GR8-EXTCP-002的主审政策/归属裁决OPEN**，不自授required、optional或全局no-required，不将既有ELR派发当成收到反证。负证据限实际读的WP67-A目的/3.2/7.1/8.1/9.2–9.4、WP74目的与9/10、WP15相关入口、WP16 6.3及scope相关段；不声称全131份中绝对不存在。

若主审选择保留该音频请求行为，最小内容是三分支优先/75音高/按pitch折算的请求等待及无ensure边界，接入唯一既有canonical；不顺带转录496球字段、引入未来Ruby/PictureEx API或修改无关作者库规则。若已有独立有效范围政策排除这些精度，按其准确身份关闭这一有限疑点即可。建议验收仍为上述22/29/12前提、专用/普通/均缺三对照、原位图/影子和多轨共同等待、迟到/首次起钟、正常结束及中止部分提交。所有这些向量NOT_EXECUTED。

## 边界、历史与独立性

没有新正式必修、optional或canonical；1个既有候选待主审，不新增多层行政审查。H001前景opacity误读已撤回，不能复活；原先保留的Float/optional/policy/limits不因本组接收采用、关闭或改号。八项Battler强制澄清全文已读：HP/Illusion/刷新在必要交界独立核对；Handler/add、空子类、Exp/EV等更正保留给原外域接收，不冒本组已核所有handler。R6/R7历史PASS和旧关闭不授本轮批准。

当前为独立委派执行，父source_thread_id为01a13f49-a154-7054-9b04-ce31f924d01c，原CP作者01a143b2-8ba3-76f5-a39d-7904a2dd1000不是本接收签字。没有把父thread ID伪装成本接收者UUID。实际opaque ID/model/effort/tier/speed/Fast无可信回显均UNVERIFIED；请求gpt-6.1-sol/ultra/default普通速度/Fast off。沿用已有Git身份，没有自行spawn或伪造新票。

参考/独立模型/游戏/原生媒体/真实保存回放执行全部0、NOT_EXECUTED。L01/02/03/08/09/10/11/12/14只在实际素材、宿主、插件、时间、输入、音频/像素与I/O范围保留；本组可得定义未读不归入limit。原作者早期stdout缺口、Ruby探测127保留为历史，不能转作本组执行。新机械工具只核输入身份、130-ID精确集合、原始对象等值和报告一致性；未运行恢复旧脚本。初期错误cwd、路径猜错、输出截断及317末行补读均在账内保留，遗漏片段已补，检索命中不授全文信用。

本组交付供父接收与主审汇总；根canonical/task-final仍独占。普通commit/push和本次自身增量的逐文件远端回读由publication.json绑定实际core身份，不递归生成self-hash。**UPDATE_NOT_STARTED**。
'''
(OUT/'report.md').write_text(report)
dump('validation.json', dict(schema='r8-cp03-validation/v1',utc=UTC,kind='TOOL_VALIDATION_IDENTITY_AND_STRUCTURE_ONLY',
     counts=counts,all_primary_origin_objects_match_fixed_raw=True,
     reused_fixed_recovery_all31_match=True,prompt_embeds_exact_global_and_skill=True,
     expected_id_set_equals_hand_authored_decisions=True,source_and_formal_working_bytes_equal_frozen=True,
     input_identities=input_ids,behaviour_executions=0,
     additional_views_are_not_historical_stdout=True,
     finite_status='READY_FOR_PARENT_RECEPTION_WITH_EXISTING_SCOPE_DECISION_OPEN',UPDATE_NOT_STARTED=True))
print(json.dumps(dict(output=str(OUT.relative_to(REPO)),counts=counts,verified_recovery_files=len(reused),
                      report_bytes=(OUT/'report.md').stat().st_size),ensure_ascii=False))
