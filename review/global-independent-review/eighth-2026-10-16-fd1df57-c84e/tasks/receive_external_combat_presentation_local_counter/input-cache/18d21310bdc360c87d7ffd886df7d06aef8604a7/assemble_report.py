"""Audit bookkeeping only. No reference behavior is executed or reimplemented."""
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = Path('/workspace/pokemon-essentials-clean-room')
REF = Path('/workspace/pokemon-essentials')
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
INPUT = '30cfed0996003b6ebf4b5c51cc04f31ca9255440'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def write(name, obj):
    (HERE / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def run(args, cwd):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return {'argv': args, 'cwd': str(cwd), 'start_utc': start,
            'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'exit_code': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}

def identity(repo, commit, path):
    b = subprocess.check_output(['git', 'show', commit + ':' + path], cwd=repo)
    return {'repo': str(repo), 'commit': commit, 'path': path,
            'tree': subprocess.check_output(['git', 'rev-parse', commit + '^{tree}'], cwd=repo, text=True).strip(),
            'git_blob': subprocess.check_output(['git', 'rev-parse', commit + ':' + path], cwd=repo, text=True).strip(),
            'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(), 'lines': len(b.splitlines())}

ledger = json.loads((HERE / 'reading-ledger.json').read_text())

# Register completed reads, preserving partial-file truth for the other consumers.
name = 'Data/Scripts/016_UI/025_UI_TextEntry.rb'
f = next(x for x in ledger['dependency'] if x['path'] == name)
f.update(semantic_status='FULL_READ', read_intervals=[[1, f['lines']]],
         semantic_notes='全文786行；键盘min0 ESC空串/Return下限、光标四字符表13×5、空列跳过/控制行、删除与末字替换、自动小写、0.5秒切tab、命名mode2及正常资源清理；底层CharacterEntryHelper仍需UI依赖接收。')
f = next(x for x in ledger['dependency'] if x['path'].endswith('006_UI_Summary.rb'))
f['read_intervals'].append([814, 1025])
f['semantic_notes'] += ' 补读814-1025：详情/五页图标、成员前后跳转、完整pbMoveSelection：持久招式对象换序，Shadow拒换，战斗标记只挡选项菜单；缎带选择只前缀，未计完整。'
extra = [
    (REF, R, 'Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb', [[1,160]], 'HP恢复/扣减、正式失能、完整PP同步入口；PP通过原招式对象关联同步，不能从UI换序臆造错槽PP写入；形态方法仅前缀，未读余部。'),
    (REF, R, 'Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb', [[1,135]], '完整构造/工厂/原招式关联、total_pp与分类、多个默认谓词；余部未读。'),
    (SPEC, B8, 'deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md', None, '全文阅读；持久/战斗PP独立与原对象关联、HP/状态/持物及接收移位边界；仅相关接口对照，不替代该领域primary。')
]
for repo, com, path, intervals, note in extra:
    if any(x['path'] == path for x in ledger['dependency']):
        continue
    f = identity(repo, com, path)
    f.update(semantic_status='FULL_READ' if intervals is None else 'PARTIAL_READ_NECESSARY_METHODS',
             read_intervals=intervals or [[1, f['lines']]], semantic_notes=note,
             evidence_level='SOURCE_STATIC' if repo == REF else 'FORMAL_TEXT_READ',
             reviewer='external_combat_presentation / current actual context', reception='PENDING_MAIN_REVIEW')
    ledger['dependency'].append(f)
ledger['updated_utc'] = NOW
write('reading-ledger.json', ledger)

# Each row is a manually chosen source-structure -> formal/consumer link.
# It does not turn these structure groups into an exhaustive atomic assertion count.
links = [
 ['67:2,9.2','67:9.1,9.3','67:9.1','67:9.1','67:9.1','67:6.4,9.2','67:3.5,9.2,9.3'],
 ['67:3.2','67:3.2,9.2','67:3.2.1','67:3.2,9.3'],
 ['67:3.3,3.4','67:4.1','67:6.1,6.4','67:5.1,5.2','67:4.3','67:4.3','67:7.2,8.2'],
 ['67:3.2,9.3','67:9.3','67:9.3','67:7.1,9.2','67:7.1,8.1,9.3','67:9.4','67:9.4,9.4.1','67:9.4;74:10.2','67:9.4;74:10.2'],
 ['67:3.3,4.1','67:3.3','67:4.1','67:4.1','67:4.1','67:4.3'],
 ['67:9.2','67:9.2','67:9.2','67:9.2','67:7.1,9.2','67:9.3','67:9.2,9.3','67:9.3'],
 ['67:9.3;74:10.2','67:9.3','67:9.3','67:9.3','67:9.3','67:9.3','67:9.3','67:9.3','67:9.3'],
 ['67:3.2,9.3','67:3.2,9.3','67:9.3','67:9.3','67:9.3','67:9.3','67:9.3','67:8.1,9.3','67:8.1,9.3'],
 ['67:3.6','67:3.6','67:3.6'],
 ['67:8.2,8.3;38:6','67:8.2;38:5,6','67:8.1;38:2,5','38:3'],
 ['74:2,4.4,10.2','74:14','74:9','74:7.1,12','74:2,6.2','74:9,10.2a','74:10.2','74:10.1,10.2','74:10.2,10.2a'],
 ['38:4','38:4','38:4','38:4']
]
consumers = [
 ['Battle start/command/attack/end; Window_AdvancedTextPokemon; System.uptime; Input/Graphics'],
 ['Battle.pbStartBattle; trainer/species image factories; GameData::SpeciesMetrics'],
 ['Battle_CommandPhase; ActionSwitching; Party; Bag; Summary; TextEntry; Pokedex brief'],
 ['Battler_ChangeSelf; ExpAndMoveLearning; CatchAndStore; cached animation loader; PBAnimationPlayerX'],
 ['Scene_ChooseCommands; battler move display_*; menu bitmap/Window_CommandPokemon'],
 ['HP/EXP scene wrappers; SpeciesMetrics; PokemonSprite factories; System.uptime'],
 ['Scene_Animations; Safari bait/rock; PictureEx; bitmap/audio host'],
 ['Scene_PlayAnimations; CatchAndStore; PictureEx; BallAnimationMixin'],
 ['ChallengeGenerator real-battle branch; AI default command path'],
 ['Battle_Peers; storage; all ball handlers; scene; Battle_StartAndEnd; player Pokedex'],
 ['scene playback; animation editor preview/timing authoring; compiler; cache reload'],
 ['CatchAndStore calculation/success/failure; GameData Pokemon/Species; Settings']
]
facts = []
num = 0
for fi, f in enumerate(ledger['primary']):
    assert len(links[fi]) == len(f['units']), (fi, len(links[fi]), len(f['units']))
    for ui, u in enumerate(f['units']):
        num += 1
        granular_gap = fi == 6 and ui >= 1 or fi == 7 and ui in (0,1,3,4,5,6,7,8,9)
        facts.append({'id': f'EXTCP-F{num:03d}', 'reference': {k:f[k] for k in ('commit','path','git_blob','bytes','sha256')},
                      'source_range':u['range'], 'structure':u['structure'], 'read_fact_notes':u['semantic_notes'],
                      'formal_links':links[fi][ui].split(';'), 'necessary_consumers':consumers[fi],
                      'preconditions':'固定R、对应实际入口/正常数据/具名配置；依源码分支；资源与宿主请求成功不得作为实际观察。',
                      'status':'FORMAL_GRANULARITY_UNRESOLVED' if granular_gap else 'SOURCE_READ_FORMAL_LINKED',
                      'evidence_level':'SOURCE_STATIC', 'formal_scope':'所链条款的静态接口对照；不是整段内每个复合子断言已经独立验收。',
                      'reception':'PENDING_MAIN_REVIEW'})
write('forward-mapping.json', {'schema':'r8-forward/v2','structure_groups':79,'atomic_assertion_denominator':'NOT_CLOSED',
                              'facts':facts,'all_semantic_pass':False,
                              'granularity_gap':'球颜色/16行变体表/轨道/音色与精确时点虽全文读过，尚未为每个字段闭合到正式原子条款；可读内容映射缺口，不改标L02。'})

formal_paths = {k:next(x['path'] for x in ledger['dependency'] if Path(x['path']).name.startswith('wp'+k+'-'))
                for k in ['17','20','38','39','40','41','42','53','56','58','74']}
formal_paths['67'] = next(x['path'] for x in ledger['dependency'] if '/wp67-a-' in x['path'])
formal_paths['66a'] = next(x['path'] for x in ledger['dependency'] if '/wp66-a-' in x['path'])

# Manual compound-assertion groups, kept as lists so a broad PASS cannot erase an unverified child.
rows = [
 ('67','3.2',[37,44],['先对方后玩家的开场消息/派出','异色公共动画与动画开关分层','初始sprites与数据框等待'],['F008','F009','F011','F019','F051','F052','F055']),
 ('67','3.2.1',[45,59],['背景与消息时段独立解析','组合平台由base0决定共同前缀','无组合才独立base文件且不保证二次回退'],['F010']),
 ('67','3.3-3.4',[60,76],['网格/记忆/Cancel权限','SHADOW+训练家Call替代','SkyDrop拒非Fight','玩家回退/撤销/调试与控制权'],['F012','F013']),
 ('67','3.5',[77,83],['命令→攻击→回合末及决定截断','普通终局与显式abort不能合并','取消选择/退款/正常共同清理'],['F007']),
 ('67','3.6',[84,88],['Debug确认真/命令0/物品-1/遗忘0','Bag与剩余Call条件随机','move单数入口异常','真实生成分支使用AI绕过这些菜单'],['F060','F061','F062']),
 ('67','3.7',[89,105],['next/map/global/default音频选择','训练家按顺序最后非nil字段','空串与nil分开','引子备忘cue/current位置'],[]),
 ('67','4.1',[108,118],['招式槽/记忆/PP显示','Mega按钮切换继续选招','Shift登记与Mega撤销','call/auto先返回的非默认分层'],['F013','F030','F031','F032']),
 ('67','4.2',[119,122],['Call四结果分支','菜单资格与裸登记分开'],['F012']),
 ('67','4.3',[123,131],['文字nil/空名/有效名分开','目标光标跨侧和±2移动','NearAlly初选远位异常','确认不重查文字；执行邻近拒绝'],['F016','F017','F033']),
 ('67','5.1-5.2',[134,148],['内部战斗背包门','battle_use过滤','1/3自动选择拒绝后手选','2选招/4选敌/5无目标','各取消只退对应层','战斗与野外游标正常恢复'],['F015']),
 ('67','5.3-5.3.1',[149,163],['登记消费不等执行','1/2/3/5复检失败退款保留身份','4球独立消费者不退款','下一命令/正式失能直接清身份','正常终局再退及容量失败部分提交'],['F015']),
 ('67','6.1-6.4',[166,190],['三模式各菜单与取消层','SwitchIn可战斗+canSwitch/不可取消','显示idx反查真实idx','查询严格/宽松与登记正交','召回/派出消息与Illusion','Arena拒换和顺序替补'],['F014','F006']),
 ('67','7.1',[193,199],['暗影消息受showMessages门且无普通经验/升级循环','经验写入先于展示','单席玩家EXP1.75比例+满槽0.2','逐级重算/刷新/消息/两窗USE等待/学招'],['F022','F023','F034','F035','F038']),
 ('67','7.2',[200,208],['空槽持久先写、消息后场上追加','满槽两表写好后Ta-da','取消后放弃确认循环','HM正常拒绝调试豁免'],['F018']),
 ('67','8.1',[211,217],['投掷消息先于挡球','0-3失败与4成功','捕获移出/经验/结果/成功效果顺序','Critical压缩摇动仅展示','正常捕获ME3.5秒等待'],['F023','F058','F065','F066']),
 ('67','8.2-8.3',[218,233],['三门新图鉴页和owned写入','命名先于存储','满队策略/99取消/必须入队','旧成员先入盒再删除队伍','提示后左移记忆及还原记录','伙伴合并身份错配独立于普通路径'],['F063','F064']),
 ('67','9.1',[236,243],['普通全显后1秒','brief由后继补等待','paused3秒且battleEnd不自动','忙时快进/resume与确认不忙门','块只一次'],['F002','F003','F004','F005']),
 ('67','9.2',[244,253],['单席玩家显示数值HP/EXP','HP显示补间1秒','整数阈值/浮点HP颜色边界','条宽偶数像素量化','图标条件独立','数据框选择摆动与精灵摆动分开'],['F034','F035','F036','F037','F038','F040','F041']),
 ('67','9.3',[254,263],['多只派出框等自己的球','召回先球再框','特性条出现/隐去等待','倒下叫声与高度裁切','捕获 retained ball 与隐藏','影子保存正常恢复不保证异常ensure'],['F019','F020','F021','F023','F024','F042','F043','F044','F045','F046','F047','F048','F049','F050','F051','F052','F053','F054','F055','F056','F057','F058','F059']),
 ('67','9.4-9.4.1',[264,299],['精确move Opp优先与hitNum','18×6默认数据每格','类别两个偏移/默认无hitNum','无关联/库/同名返回层次','公共首精确名与影子包装差异','播放器20fps/正常恢复/例外不保证'],['F025','F026','F027']),
 ('67','10',[300,314],['Safari四命令/专用盒/预算','捕虫直投Sport/比较窗','Palace自动/无力','Arena图文逐项及通用消息更新','回放暂停降普通/abort'],[]),
 ('67','11-14',[315,348],['默认配置和具名变体','异常/资源/全宿主限制','测试目录只静态向量','依赖未接收不能推全系统完成'],[]),
 ('74','2,9,10.2,10.2a',[21,351],['27索引/25语义字段及常规60槽','五时序默认/文本一基帧','图形设置与纯色分支','先活动渐变后当帧事件','同层旧值共享和RGBA整组写','坐标符号差异','前景旧opacity是自身（581复读）','duration0只捕获不活动插值','20fps访问跳帧不补事件','锚点捕获与编辑偏移64'],['F067','F069','F071','F072','F073','F074','F075']),
 ('74','14-16',[403,447],['旧格式修正仅常规槽','宿主RPG转换无默认活动caller','Move/Opp映射及至少一有效写出','集合/关联不同缓存寿命','预览不保存'],['F068','F070','F071','F075']),
 ('38','capture/store',[1,146],['HP与球率/状态/UltraBeast前置','critical门与最多四次首失败停止','19球率+catcheffects','record/dex/nickname/store顺序','容量失败/队伍替换部分提交','normal终局身份错配'],['F063','F064','F065','F066','F076','F077','F078','F079']),
 ('20','5.4-5.5',[150,185],['包装PP独立字段','专门入口按原对象关联+同ID+非Transform写穿','UI换序不自动推出PP错槽','学招单独同步且不保证任意刷新'],[]),
 ('53','4,6',[49,186],['Safari四命令和预算回写','Bait/Rock概率与天气请求','Safari登记internal门','捕虫预算登记消费不动背包','比较窗确认后保留或拒绝','球尽与普通终局分开'],[]),
 ('56','Palace/Arena',[1,141],['Palace类别/部分资格/2A+D','Arena主动拒换/顺序替补','裁判心技体图文与通用消息','评判>=3且补位不重置','显示请求不证明实际素材'],[]),
 ('58','6.1-6.5',[138,164],['播放入口创建abortable场景','暂停降普通但非所有入口无交互','BACK中止只场景清理','正常终局与设施善后分开','实时依赖不由副本推隔离'],[]),
 ('66a','3,5,6.1,6.5',[31,194],['共享队伍初始0/网格/取消','Summary战斗标志只禁选项','持久招式换序与Shadow禁止','遗忘额外新招槽和BACK为-1','HM正常门/调试豁免','零招式初绘失败先于取消循环'],[]),
 ('17','message/state',[1,319],['战斗独立消息循环使用共享文本状态','busy/resume/skipAhead/linepause分层','通用消息与Arena判断图形更新','文本输入两模式取消差异'],[])
]
clauses=[]
for n,(key,section,rng,children,srcs) in enumerate(rows,1):
    p=formal_paths[key]
    clauses.append({'id':f'EXTCP-R{n:03d}','formal':identity(SPEC,B8,p),'section':section,'range':rng,
                    'subassertions':[{'id':f'EXTCP-R{n:03d}.{i+1}','assertion':v,'status':'STATIC_COMPARED_RECEPTION_PENDING'} for i,v in enumerate(children)],
                    'source_groups':['EXTCP-'+s for s in srcs],
                    'consumer_evidence':'reading-ledger.json dependency entries and interfaces.json; exact full/partial intervals retained',
                    'scope_limit':'仅这些列明子断言；范围中的其它条款不因一个组被标PASS。','reception':'PENDING_MAIN_REVIEW'})
write('reverse-mapping.json',{'schema':'r8-reverse/v2','primary_formal_files':0,'manual_clause_groups':len(clauses),
                             'manual_subassertions':sum(len(x['subassertions']) for x in clauses),'atomic_clause_denominator':'NOT_CLOSED',
                             'all_semantic_pass':False,'clauses':clauses})

# Exact inventory status: unread files are never reclassified as runtime limits.
universe={}
for dep in ['combat_review','ui_full']:
    obj=json.loads((HERE/'inputs'/f'{dep}.json').read_text())
    for side in ['reference','formal']:
        for f in obj[side]:
            k=(side,f['path'])
            universe.setdefault(k,{'side':side,'path':f['path'],'readsets':[]})['readsets'].append(dep)
for f in ledger['primary']+ledger['dependency']:
    side='reference' if f['repo']==str(REF) else 'formal'
    universe.setdefault((side,f['path']),{'side':side,'path':f['path'],'readsets':['scope_expansion']})
lookup={(('reference' if f['repo']==str(REF) else 'formal'),f['path']):f for f in ledger['primary']+ledger['dependency']}
denoms={}
for key,item in universe.items():
    f=lookup.get(key)
    item['read_status']=f['semantic_status'] if f else 'UNREAD_AVAILABLE'
    item['reception']='PENDING_MAIN_REVIEW'
    item['scope']='PRIMARY' if f in ledger['primary'] else 'DEPENDENCY_DISCOVERY_POOL'
    item['necessity_status']='ACTUALLY_READ' if f else 'NOT_FULLY_TRIAGED_REQUIRES_MAIN_SCOPE_RECEPTION'
    item['not_a_limit']=not bool(f)
for side in ['reference','formal']:
    vals=[x for x in universe.values() if x['side']==side]
    denoms[side]={'files':len(vals),'full_read':sum(x['read_status']=='FULL_READ' for x in vals),
                  'partial_read':sum(x['read_status'].startswith('PARTIAL') for x in vals),
                  'unread_available':sum(x['read_status']=='UNREAD_AVAILABLE' for x in vals),
                  'unreceived':len(vals)}
partial_gaps=[]
for f in ledger['dependency']:
    if f['semantic_status']=='FULL_READ':continue
    seen=set()
    for a,b in f['read_intervals']:seen.update(range(a,min(b,f['lines'])+1))
    spans=[];start=None
    for i in range(1,f['lines']+2):
        missing=i<=f['lines'] and i not in seen
        if missing and start is None:start=i
        if not missing and start is not None:spans.append([start,i-1]);start=None
    partial_gaps.append({'path':f['path'],'total_lines':f['lines'],'read_lines':len(seen),'unread_intervals':spans,
                         'disposition':'READABLE_NOT_FULLY_REVIEWED; exact relevant methods vs remaining context await main reception; not L02/L03'})
write('coverage-and-gaps.json',{'schema':'r8-external-denominators/v1','primary':{'files':12,'lines':6003,'bytes':233236,'full_read':12,'unread':0,'structure_groups':79,'unreceived_groups':79},
                              'discovery_pool':denoms,'files':list(universe.values()),'partial_file_gaps':partial_gaps,
                              'mapping_gaps':{'forward_granularity_groups':sum(x['status']=='FORMAL_GRANULARITY_UNRESOLVED' for x in facts),
                                              'atomic_source_fact_denominator':'NOT_CLOSED','atomic_formal_clause_denominator':'NOT_CLOSED'},
                              'global_administrative_read_gap':'Root-wide final bindings/history/public ledgers/other task receptions were not fully reread in this finite shard. R6 L01–L14 were fully read; other historical records remain unreceived, not inherited PASS.',
                              'claim':'This report cannot certify exhaustive closure or zero remaining findings.'})

interfaces=[
 ('IF01','Battle command → scene → command receiver','CommandPhase/SceneChooseCommands/ActionOther','grid modes, remembered cursor, return -1/-2/-3 and Call/Shift/Mega differ; consumer side controls registration/withdrawal','WP67-A 3–4; WP40 3/7'),
 ('IF02','Scene party → shared party/summary → switch validation','SceneChooseCommands141–191; Party475–714/746–1049; Summary1232–1379','display-to-actual inversion, mode/cancel layers; Summary can mutate persistent move order; PP relation follows original object','WP67-A 6/7; WP66-A 3/6; WP20 5.5'),
 ('IF03','Battle bag → item family → execute/refund','SceneChooseCommands193–325; Bag1–453; ActionUseItem; AttackPhase','filtered indices and per-pocket memory; consumption registration; family-specific recheck/refund retains choice; ordinary termination may refund again','WP67-A 5; WP40 4.2.1; WP42 6.0'),
 ('IF04','HP/EXP committed values → animation requests','BattlerChangeSelf1–124; ExpAndMoveLearning; ScenePlayAnimations216–385; SceneObjects','HP setter before blocking display; EXP segment commit before bar; numeric levels before windows; pending Ruby/host observations','WP67-A7/9.2; WP42 4'),
 ('IF05','Catch → effects → receipt queue → peer/storage/dex/name','CatchAndStore full; PokeBallEffects full; Battle_Peers full; Storage1–265; TextEntry full; Pokedex partial','rate/failure/success handlers, remove before EXP, queue; nickname before storage; data already committed before later display failure; partial contexts retained','WP38; WP67-A8; WP20 6.4'),
 ('IF06','Animation author/compile/reload → actual battle/editor player','MiscPBSData full; Compiler1274–1320; AnimEditorFunctions376–677; SceneElements451–511; primary player full','five timing types; file and cache identities distinct; 20fps visited-frame events; shared old snapshot; foreground captures own opacity','WP74 9/10/14–16; WP67-A9.4'),
 ('IF07','Picture process → sprites/planes/bitmap/audio host','PictureEx full; SpeciesMetrics full; Planes full; primary animation all','ordered process capture and 20fps requests; properties reach host; assets/native rendering/audio not executed; exact ball fields lack closed formal mapping','WP67-A9; WP74 10'),
 ('IF08','Variant override → common scene/message lifecycle','Safari/Bug/Palace/Arena/Recorded all full; Challenge_Battles full','Safari budget vs Bag, Bug compare pane; Palace no normal fight picker; Arena general message renderer; replay abortable and normal end differ','WP53/56/58; WP67-A10'),
 ('IF09','Background/music options → resource selection → scene','SceneInitialize full; BattleAudio full; Settings necessary ranges','next/map/global/fallback audio; background independent clock variants; metrics apply once when sprite positioned; host output unknown','WP67-A3.2.1/3.7')
]
write('interfaces.json',{'schema':'r8-interfaces/v2','interfaces':[{'id':a,'edge':b,'source':c,'contract':d,'formal':e,'evidence':'SOURCE_STATIC','reception':'PENDING_MAIN_REVIEW'} for a,b,c,d,e in interfaces],
                         'independent_receiver_receptions':0,'missing_receptions':['combat_review','ui_full','demo_dx/shared animation consumers','main reviewer independent counterreview/final scope reception'],
                         'no_fake_context_renaming':True})

write('proposals.json',{'schema':'r8-proposals/v2','classification':'PROPOSED_ONLY','required_updates':0,'submitted_candidates':0,
                        'independent_counterreview':'NOT_RECEIVED','records':[],
                        'retracted_hypotheses':[{'id':'GR8-EXTCP-H001','root_key':'foreground-opacity-snapshot-source','status':'RETRACTED_BY_PROPOSER',
                            'reference':identity(REF,R,'Data/Scripts/011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb'),
                            'formal':identity(SPEC,B8,formal_paths['74']),'source_lines':[572,583],'formal_lines':[338,350],
                            'finite_input':'正常有效图层：背景opacity20、前景100，f1前景opacity目标200/duration2；f0-f3均访问且无其它时序覆盖。',
                            'incorrect_hypothesis':'前景从背景20捕获导致中点110，误称与正文150有差异。',
                            'counterevidence':'固定R第581行取前景自身opacity，源静态中点150，与正文相同；实测/源码执行均未执行。',
                            'cancellation_failure_scope':'普通编辑取消不新增时序；错误假设与取消/异常无关；没有据此改源码或formal。',
                            'independence':'Same actual proposer reread; not an independent non-proposer reception.',
                            'historical_relation':'B20-C026仅用于定位现行条款；未继承其PASS；无新required根因。',
                            'minimal_revision':'NO_REVISION_SUPPORTED','next_action':'主审可复核撤回证据；不得把误读版本作为候选接受。'}],
                        'no_finding_is_not_global_pass':True})

checks=[]
for repo in [SPEC,REF]:
    for argv in [['git','rev-parse','--show-toplevel'],['git','remote','get-url','origin'],['git','rev-parse','HEAD','HEAD^{tree}'],
                 ['git','status','--porcelain=v1','--untracked-files=all'],['git','worktree','list','--porcelain']]:
        checks.append(run(argv,repo))
for argv in [['git','show-ref','--verify','refs/heads/main'],['git','show-ref','--verify','refs/remotes/origin/main'],
             ['git','ls-remote','origin','refs/heads/main','refs/tags/delivery/seventh-round-closed-final-20261016','refs/tags/delivery/seventh-round-closed-final-20261016^{}'],
             ['bash','-c','ruby --version']]:
    checks.append(run(argv,SPEC))
write('environment-checks.json',{'checks':checks,'commands_are_not_behavior_executions':True})
contracts=[]
for path in ['delegation/prompts/combat_presentation.md','delegation/readsets/combat_presentation.json','inputs/eighth-global-review-prompt.md','inputs/review-SKILL.md']:
    full='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/'+path
    contracts.append(identity(SPEC,INPUT,full))
contracts.append(identity(SPEC,INPUT,'AGENTS.md'))
write('identities.json',{'schema':'r8-identities/v2','readiness':'READY_WITH_LIMITS','fixed_input':INPUT,
                        'B8':{'commit':B8,'tree':'751dfde81048c81390f89a65ca1d1a565ba8e1ca','formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e','cloud_path':str(SPEC)},
                        'R':{'commit':R,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','cloud_path':str(REF),'requested_upstream':'Maruno17/pokemon-essentials','actual_origin':'y805939188/pokemon-essentials mirror; exact frozen commit/tree/bytes checked'},
                        'branch':'codex/r8-external-combat-presentation-20261016','base_commit':INPUT,'contracts':contracts,
                        'model_requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','fast':False},
                        'model_actual':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','fast':'UNVERIFIED'},
                        'actual_agent_session_id':'UNVERIFIED','source_thread_id':'01a13f49-a154-7054-9b04-ce31f924d01c',
                        'platform_log':'Tool conversation is the original log; earlier reads have no standalone start/end/stdout/stderr capture. New environment-checks contain actual subprocess provenance.',
                        'historical_mac_state':'Not mapped as locally present: 67835 untracked/478 ignored/7 other worktrees/35 branches/257 tags are historic Mac preparation, not verified current cloud counts.',
                        'source_separation':'Only own report directory written; no reference source copied into report/spec, no source translation/framework.',
                        'local_refs':'No local main or cached origin/main; live origin main/tag checked separately. No ref repair/reset.',
                        'limitations':['Ruby executable unavailable (exit127 probe)','No native RGSS/mkxp/audio/GPU/complete project observation','Other actual contexts/receptions unavailable in this task; user forbids spawn'],
                        'update_status':'UPDATE_NOT_STARTED'})

progress=json.loads((HERE/'progress.json').read_text())
progress.update(state='EVIDENCE_PACKAGE_PREPARED_WITH_GAPS',updated_utc=NOW,semantic_acceptance='NOT_RECEIVED',
                formal_clause_status='ATOMIC_DENOMINATOR_NOT_CLOSED',submitted_candidates=0,required_updates=0,
                content_review_complete=False,discovery_pool_denominators=denoms,dependency_read_files=len(ledger['dependency']),
                dependency_full_read_files=sum(x['semantic_status']=='FULL_READ' for x in ledger['dependency']),
                dependency_partial_read_files=sum(x['semantic_status']!='FULL_READ' for x in ledger['dependency']))
write('progress.json',progress)
print(json.dumps({'primary_groups':len(facts),'reverse_groups':len(clauses),'reverse_subassertions':sum(len(x['subassertions']) for x in clauses),
                  'dependency_files':len(ledger['dependency']),'pool':denoms,'mapping_granularity_gaps':sum(x['status']=='FORMAL_GRANULARITY_UNRESOLVED' for x in facts)},ensure_ascii=False))
