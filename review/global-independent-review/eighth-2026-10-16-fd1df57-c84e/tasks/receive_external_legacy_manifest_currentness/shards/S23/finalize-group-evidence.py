"""Serialize this context's explicit judgments and exact reading scopes; no automatic semantic review."""
from pathlib import Path
import collections, datetime, hashlib, json, os, subprocess

HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]
ROOT = TASK.parents[1]
REPO = ROOT.parents[2]
REF = Path('/workspace/pokemon-essentials')
INPUT = HERE / 'inputs/target-93d7df7f'
CAPTURE = datetime.datetime.now(datetime.timezone.utc).isoformat()
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CONTRACT = '2d44dafe215842de6355f46de7d4d273d8b4c264'
TARGET = '93d7df7f66adcaa25811fd6ff09352b754577af0'
ACTUAL = os.environ.get('CODEX_THREAD_ID', 'UNVERIFIED')

def load(name): return json.loads((INPUT/name).read_text())
def dump(directory, name, obj):
    (directory/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
def git(repo, *args): return subprocess.check_output(['git','-C',str(repo),*args])
def fixed(repo, commit, path, ranges, outputs, scope='FULL_READ_NAMED_RANGES'):
    data = git(repo,'show',commit+':'+path)
    lines = data.splitlines(keepends=True)
    mode, kind, blob = git(repo,'ls-tree',commit,'--',path).split(b'\t')[0].decode().split()
    assert kind=='blob' and all(1<=a<=b<=len(lines) for a,b in ranges)
    return {'repository':'Maruno17/pokemon-essentials' if repo==REF else 'y805939188/pokemon-essentials-clean-room',
        'commit':commit,'tree':git(repo,'rev-parse',commit+'^{tree}').decode().strip(),'path':path,
        'mode':mode,'blob':blob,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
        'physical_lines':len(lines),'read_scope':scope,'whole_file_read':ranges==[[1,len(lines)]],
        'ranges':[{'lines':[a,b],'byte_start':sum(map(len,lines[:a-1])),'bytes':len(b''.join(lines[a-1:b])),
                   'sha256':hashlib.sha256(b''.join(lines[a-1:b])).hexdigest()} for a,b in ranges],
        'actual_output_chunks':outputs,'reader':ACTUAL,'execution':'NOT_EXECUTED',
        'captured_utc':CAPTURE,'earlier_read_command_utc':'NOT_SEPARATELY_CAPTURED; platform tool outputs retain order'}

common = {'schema':'r8-lmc-group5-reception/v1','contract_commit':CONTRACT,
    'contract_tree':'b97efa207e6b131f1d099541b8dc7bbec92518fb',
    'target_commit':TARGET,'target_checkout_tree':'dd8105c747b6f66663d9f63254a686594791cae8',
    'target_task_tree':'e4e557611f94473568b69b7f1a6608896f700128',
    'B8':B8,'B8_tree':'751dfde81048c81390f89a65ca1d1a565ba8e1ca',
    'formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e',
    'R':R,'R_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0',
    'reader':ACTUAL,'original_author':'01a143c7-a558-738e-9580-11a8f12d903f',
    'parent_receiver':'01a1447a-0548-77cb-b3bc-af8857847031',
    'independence':'CODEX_THREAD_ID/CODEX_SESSION_ID equal actual reader and differ from both named contexts; no spawned child and no new vote from resumed turns.',
    'new_contexts_created_here':0,'upstream_context_creation_event':'UNVERIFIED_NOT_COUNTED',
    'requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','Fast':False},
    'actual_configuration':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast']},
    'branch':'codex/r8-legacy-reception-group-5-20261016','update_started':False,
    'business_execution':{'reference':0,'independent_model':0,'host_demo':0,'native_media':0,'real_save_replay':0,'vectors':'NOT_EXECUTED'},
    'shared_identity_cache':'../S23/identity-and-field-aliases.json',
    'input_recovery':'../S23/input-recovery.json',
    'capture_utc':CAPTURE,'exact_task_start_utc':'NOT_SEPARATELY_CAPTURED',
    'publication':'semantic core followed by ordinary push and incremental fresh remote byte verification; no self future hash'}
assert ACTUAL not in [common['original_author'],common['parent_receiver'],'UNVERIFIED']
shared_premises = {
    'dispatch':'split-contracts/dispatch.json completely read, no generated plan granted credit',
    'contracts':'S21/S22/S23 complete JSON all unique fields read; equal common fields and catalog read once; exact aliases validated',
    'prompts':'All three complete prompts read by exact equal attachment reuse; each distinct preamble read',
    'global_prompt':{'path':'inputs/eighth-global-review-prompt.md','bytes':36653,'sha256':'63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b','scope':'FULL_READ exact embedded text'},
    'skill':{'path':'inputs/review-SKILL.md','bytes':3598,'sha256':'ac3c8560f38192269b65b061673896a77f5eb794b90e90644e3c445b2c3be1f8','scope':'FULL_READ; excludes review/audit reports; no formal revision performed'},
    'AGENTS':'Root AGENTS FULL_READ; no additional applicable AGENTS under ancestor write paths',
    'parent_contract':'delegation/readsets/receive_external_legacy_manifest_currentness.complete.json all fields disposed by exact common aliases and unique schema/id/write_set',
    'original_contract':'delegation/prompts/legacy_manifest_currentness.md and readsets/legacy_manifest_currentness.json FULL_READ; latest user branch/publication authorization supersedes old no-push instruction',
    'authority':'Root canonical/final acceptance remains exclusive; no global B8 PASS or historical 27/56/92 reopening'}
dump(HERE,'context-and-premises.json',{**common,'shared_premises':shared_premises})

# Actual displayed source ranges, with complete boundaries for every adopted definition.
s21r = [
('Data/Scripts/003_Game processing/002_Scene_Map.rb',[[1,252]],['1d038f']),
('Data/Scripts/004_Game classes/008_Game_Player.rb',[[141,275],[416,616]],['2921dd']),
('Data/Scripts/004_Game classes/006_Game_Character.rb',[[362,400],[893,993]],['2921dd']),
('Data/Scripts/012_Overworld/001_Overworld.rb',[[69,218],[223,315]],['b789fb']),
('Data/Scripts/003_Game processing/003_Interpreter.rb',[[138,206]],['1d038f']),
('Data/Scripts/003_Game processing/004_Interpreter_Commands.rb',[[722,747]],['1d038f']),
('Data/Scripts/004_Game classes/010_Game_Follower.rb',[[1,215]],['b789fb']),
('Data/Scripts/004_Game classes/011_Game_FollowerFactory.rb',[[1,217],[285,296]],['b789fb']),
('Data/Scripts/003_Game processing/001_StartGame.rb',[[1,126]],['4a0ce1']),
('Data/Scripts/004_Game classes/005_Game_MapFactory.rb',[[1,154],[356,506]],['4a0ce1','f37628']),
('Data/Scripts/004_Game classes/004_Game_Map.rb',[[1,139]],['4a0ce1']),
('Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb',[[705,752]],['f37628']),
('Data/Scripts/005_Sprites/005_Sprite_SurfBase.rb',[[43,91]],['f37628'])]
s21f = [
('deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md',[[59,88],[166,190]],['593521']),
('deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md',[[52,89],[97,113],[182,198]],['593521']),
('deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md',[[94,109],[154,171]],['f55048']),
('deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md',[[82,97]],['f55048']),
('deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md',[[95,109]],['f55048']),
('deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md',[[243,247]],['f55048']),
('planning/review-manifest-2026-09-19.md',[[2849,2864]],['7c8d48'])]
s22r = [
('Data/Scripts/017_Minigames/007_Minigame_TilePuzzles.rb',[[1,608]],['23cfdd','9b0c60']),
('Data/Scripts/016_UI/007_UI_Bag.rb',[[351,704]],['9b0c60','87110b']),
('Data/Scripts/016_UI/017_UI_PokemonStorage.rb',[[679,714],[837,989],[1677,1691],[1705,1722],[1936,2022]],['106c61','6de0da','c384a5','87110b']),
('Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',[[1,264]],['6de0da']),
('Data/Scripts/016_UI/023_UI_PurifyChamber.rb',[[361,546],[1273,1308]],['87110b','6de0da']),
('Data/Scripts/016_UI/003_UI_Pokedex_Main.rb',[[82,377],[479,1302]],['106c61','0f867c','c384a5']),
('Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',[[139,301],[403,556]],['106c61','0f867c']),
('Data/Scripts/015_Trainers and player/001_Trainer.rb',[[57,79]],['a238be']),
('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',[[128,140]],['a238be']),
('Data/Scripts/001_Settings.rb',[[216,225]],['c384a5']),
('Data/Scripts/002_Save data/004_Game_SaveValues.rb',[[97,102]],['c384a5']),
('Data/Scripts/013_Items/001_Item_Utilities.rb',[[644,706],[755,776]],['b86045','322e06']),
('Data/Scripts/016_UI/001_UI_PauseMenu.rb',[[186,204]],['e2ef9c']),
('Data/Scripts/013_Items/002_Item_Effects.rb',[[43,47],[262,274]],['e2ef9c']),
('Data/Scripts/010_Data/002_PBS data/006_Item.rb',[[189,198]],['e2ef9c'])]
s22f = [
('deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md',[[1,210]],['8832e0','1c6c2e']),
('deliverables/final-specification-set/user-interface/wp71-tile-puzzles.md',[[1,178]],['9b68ee','ed5cfe']),
('deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md',[[31,44],[108,230],[299,313]],['61d7d8']),
('deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md',[[133,153]],['61d7d8']),
('deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md',[[199,201]],['61d7d8']),
('deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',[[278,332],[333,360],[532,568]],['61d7d8','a87d06','7c8d48']),
('README.md',[[1,22]],['2bbed9']),
('CURRENT-DELIVERY.md',[[1,13]],['2bbed9']),
('delivery/2026-10-16-seventh/README.md',[[1,14]],['2bbed9']),
('deliverables/final-specification-set/README.md',[[1,21]],['2bbed9']),
('deliverables/final-specification-set/scope-statement.md',[[1,21]],['2bbed9']),
('review/wp23-n01-review-2026-10-01/recheck-v3/report.md',[[1,76]],['2bbed9'])]
semantic = load('semantic-purpose-review.v2.json')
events = {u['id']:u for u in semantic['units']}
original_lines = git(REPO,'show',B8+':planning/review-manifest-2026-09-19.md').splitlines(keepends=True)
eight = [f'LM-E{n:03}' for n in [66,67,68,69,70,71,72,169]]
supplement = ['LM-E129','LM-E130','LM-E158','LM-E171']
mainlines = sorted({int(l[4:]) for e in eight for l in events[e]['primary_line_ids']})
supplylines = sorted({int(l[4:]) for e in supplement for l in events[e]['primary_line_ids']})
def runs(ns):
    out=[]
    for n in ns:
        if out and n==out[-1][1]+1:out[-1][1]=n
        else:out.append([n,n])
    return out
s22f.append(('planning/review-manifest-2026-09-19.md',runs(sorted(set(mainlines+supplylines)))+[[4115,4127]],['6da0db','b76934','7042b3','2c046f','36114c']))
s21reading = [fixed(REF,R,*x) for x in s21r]+[fixed(REPO,B8,*x) for x in s21f]
s22reading = [fixed(REF,R,*x) for x in s22r]+[fixed(REPO,B8,*x) for x in s22f]
world=load('world-interface-reception.v2.json')
worldrows=[r for p in world['fixed_contributions'] for r in p['records']]
factrows=[f for f in load('forward-mapping.json')['facts'] if f['id'].startswith('F-LMC-2849-')]
judgments = {
'VEHICLE': {'meaning':'正常201两个场景消费者显式传false；直接省参默认true；目的骑行许可独立；进入通知才另作骑行调整。同图与跨图/边缘入口分列。',
'normal':'非战斗、无已有转移/消息/转场阻塞，先前helper正常，201排队后在主/mini消费者保留surfing/diving。',
'counter':'仅换直接省参入口便清游泳；目的图可骑行时保骑行。无进入通知的同图传送不自动套force_cycling。',
'failure':'先清转移标记，再车辆/淡音/桥/地图/跟随；后继异常没有统一回滚。临时基点及ending_surf独立，实际合格步后通知才清。',
'providers':['WFS-005','WFS-028','WFS-032'],'source':['Scene_Map:72–101,121–134,165–230','Game_Player:575–616','Overworld:267–276','command201:722–747'],'formal':['WP11:64–76','WP12:184–196']},
'STEP': {'meaning':'开始写逻辑位置/距离/有条件离格；完成通知后才进入合格玩家的全局计步；强制路线/解释器分流不加全局步数。',
'normal':'移动门放行且通知/更新正常，开始后尚未完成时坐标/距离已变，全局步数尚未因完成增加。',
'counter':'通行许可不是必然位移；遭遇标记可跳本步；零位移碰撞正常完成仍可到步后入口。距离与全局步数不可互推。',
'failure':'一般完成通知可启动新运动、转移或失败；先前开始写入不由此回滚；31位回绕在玩家通知之前。',
'providers':['WFS-025','WFS-031','WI26'],'source':['Game_Player:141–193,416–555','Game_Character:376–400,893–993','Overworld:172–218'],'formal':['WP12:97–113','WP06:82–97']},
'FOLLOW': {'meaning':'实际location_passable与临时through独立于strict；同轴1/2格分支之外的非重合目标直接落位；显式转移同时写运行跟随与持久数据。',
'normal':'有效地图/角色、无覆写、helper正常；玩家→前跟随者链逐次移动并写回坐标/地图/朝向。',
'counter':'中间许可的两次一步尝试不保证第二次到达；(1,1)及同轴≥3直接定位；普通显式传送没有跟随数量守卫。',
'failure':'move_through正常返回才恢复旧through，没有ensure；传移中的早期写入不保证异常后恢复。',
'providers':['WI18','WI19','WI21','WI22','WI26'],'source':['Game_Follower:7–214','FollowerFactory:155–191','Game_Character:362–400','Scene_Map:72–101'],'formal':['WP13:154–168','WP12:52–89']},
'ERROR': {'meaning':'正常表达式返回原值；SystemExit及类名Reset原样重抛；其它异常包装事件上下文错误。',
'normal':'已到execute_script，有效错误/地图上下文且格式化正常；正常值不被误当布尔成功。',
'counter':'SystemExit/Reset不走普通EventScriptError；普通错误也不是成功结果。当前图查角色不等于绑定图或自动跟随实例。',
'failure':'错误文本构造本身也依赖helper；只确认正常格式化前提下的分层，不承诺全回滚或宿主最终显示。',
'providers':['WI04'],'source':['Interpreter:138–206'],'formal':['WP13:94–107']},
'MISSINGMAP': {'meaning':'显式转移没有读档ENOENT恢复；有播放BGM/BGS时淡音先读目标图而可早失败，无音频则可到替换地图集合后失败。',
'normal':'目标有效且前序helper正常时按正常转移链；继续读档仅在magic不符或safesave门触发重建。',
'counter':'仅切换音频状态即可改变缺图失败前缀；缺图调试选图/取消退出专属读档重建入口，不能套给显式传移。',
'failure':'读档非调试报缺图；当前图events=nil的损坏门与空集合不同；通过门不证明完整继续成功。',
'providers':['WFS-004','WFS-005'],'source':['Scene_Map:56–101','StartGame:63–104','MapFactory:17–27','Game_Map:45–74'],'formal':['WP11:64–66,171','WP09:95–109','WP10:243–247']}
}
s21facts=[]
for f in factrows:
    short=f['id'].rsplit('-',1)[1]
    s21facts.append({'id':f['id'],'original_object_pointer':'forward-mapping.json#/facts/'+str(load('forward-mapping.json')['facts'].index(f)),
        'original_fields_read':'ALL','judgment':judgments[short],'decision':'ACCEPT_FINITE_SOURCE_STATIC_MEANING',
        'not_adopted':'Provider facts unrelated to these five current chains remain contextual text, not whole-domain approval.',
        'runtime':'NOT_EXECUTED','root_final_acceptance':'PENDING_PARENT'})
precision=[
 {'id':'G5-EVIDENCE-01','classification':'EVIDENCE_RANGE_PRECISION','path':'evidence-catalog.json#/items/E-V2-WP11',
  'original':'physical_lines=190 but range166–194; byte slice silently stops at EOF','received':'actual166–190 complete; no fictitious191–194 reading','formal_required':False},
 {'id':'G5-EVIDENCE-02','classification':'BOUNDARY_SUPPLEMENT_COMPLETED','path':'E-V2-OVERWORLD ranges223–285 / WFS-032 range223–315',
  'original':'author range ends within darkness proc; location-window assertions extend to315','received':'223–315 fully displayed/read through both registration endings; cycling267–276 also complete','formal_required':False},
 {'id':'G5-EVIDENCE-03','classification':'BOUNDARY_SUPPLEMENT_COMPLETED','path':'E-V2-MAPFACTORY range1–88',
  'original':'getNewMap continuation89–91 omitted by that range','received':'1–154 actual read, including89–91; transfer setup17–27 separately complete','formal_required':False}]
s21=TASK/'shards/S21'
dump(s21,'frozen-denominator.json',{**common,'shard':'S21','facts':[f['id'] for f in factrows],'provider_records':[r['id'] for r in worldrows],
    'facts_count':5,'record_count':12,'object':'world-interface-reception.v2.json','scope':'Five finite2849 facts and every field of twelve selected records; no all-WORLD/source/global claim'})
dump(s21,'reading-ledger.json',{'reader':ACTUAL,'shared_premises':'../S23/context-and-premises.json','target_objects':[{'path':'world-interface-reception.v2.json','scope':'FULL_READ_ALL_FIELDS','chunk':'513586'},{'path':'forward-mapping.json','scope':'FULL_READ_ALL_FIELDS; only five WORLD facts independently adopted','chunk':'148584'},{'path':'reverse-mapping.json','scope':'FULL_READ_ALL_FIELDS; N01 clauses contextual only','chunk':'148584'},{'path':'interfaces.json','scope':'FULL_READ','chunk':'148584'}],
 'source_and_formal':s21reading,'boundary_precision':precision,'tool_results_are_not_semantic_credit':True})
dump(s21,'reception-ledger.json',{'shard':'S21','state':'READY_FOR_ROOT_SHARD_ACCEPTANCE','facts':s21facts,
 'provider_record_fields':[{ 'id':r['id'],'pointer':r['pointer'],'scope':'complete record text and all fields received; adopted meaning only where named by five fact joins','identity_alias':'../S23/identity-and-field-aliases.json#/world_record_exact_aliases'} for r in worldrows],
 'necessary_unread_in_five_fact_scope':[],'material_blockers':[],'parent_task_final':'ROOT_ONLY'})
dump(s21,'interfaces.json',{'shard':'S21','interfaces':[{'id':x['id'],'providers':x['judgment']['providers'],'source':x['judgment']['source'],'formal':x['judgment']['formal'],'state':'FINITE_CHAIN_RECEIVED_PENDING_ROOT'} for x in s21facts],
 'outside_scope_open':['All-WORLD/interpreter/resource/kernel full-domain atom reception','Real maps/host/native media/save/replay and unbounded plugin callers'],'business':'NOT_EXECUTED'})
dump(s21,'proposal-counters.json',{'new_required':0,'new_public_canonical_ids':0,'evidence_precision':precision,
 'decision':'五事实已有当前跨篇覆盖；没有从旧一致性标题生成新必修。不代替原作者或父接收者作全局裁决。','independent_counter_vote_added':0})
(s21/'report.md').write_text("""# S21 五条 WORLD 事实独立接收

状态：READY_FOR_ROOT_SHARD_ACCEPTANCE；UPDATE_NOT_STARTED。只完成本 shard 的五条有限静态链及两提供者十二条 record 全字段接收，父任务最终接收仍独占。

载具链确认201主/mini消费者保游泳、直接省参取消游泳、骑行目的地门与进入通知各自独立。计步链区分开始侧坐标/距离/离格与完成侧玩家全局步数，保留遭遇、强制路线及解释器门。跟随链确认实际通行与strict能力分开、同轴1/2格条件、其它非重合目标直接落位、传移运行值及持久记录写回。异常链区分正常返回、SystemExit/Reset重抛及普通包装错误。缺图链按音频前提和显式/读档入口分别保留失败前缀，events=nil不等于空集合。

每条的正常对照、最小边界、失败/部分提交、源/条款/提供者接合见 reception-ledger.json；实际完整源范围、原字节身份及工具输出块见 reading-ledger.json。未采用十二记录中无关事实的全域批准，没有借用原作者FULL_READ。

原证据的WP11范围166–194超过190行末尾，按实际166–190接收。原Overworld223–285截断通知块，本次补到315；MapFactory1–88后续89–91亦已补读。它们是本组证据精度/边界补充，未发现需改正式规格的新required。

五事实必要可读缺口0、材料阻塞0。更宽领域、宿主、真实地图/媒体/存档不在本有限接收中关闭；所有行为NOT_EXECUTED。共同固定身份、真实独立上下文、配置UNVERIFIED与一次共享身份验证见 ../S23/context-and-premises.json、../S23/input-recovery.json、../S23/identity-and-field-aliases.json。
""")

routes=load('current-primary-contribution-routes.v2.json')
event_notes={
'LM-E066':'完整保留12P2+2P3、N01单列、C/B/TP各修订与首稿错误；WP66-C三层返回/存入排序/给予门及TP尺寸反例已接有限消费者。',
'LM-E067':'11/14及余B两项/TP一项分开；37候选和37哨兵、四状态搜索、合法联动初态与S不变量对照已读，C回填不扩族。',
'LM-E068':'原14关闭及限定三包管理回填是历史输入阶段；N01未关闭不覆盖后来专项，B批独立通过不等于整合。',
'LM-E069':'18错误字段/原17正确记录分别保留；身份更正不授行为批准，后继130纠正46的计数，未逐个重造旧hash审计。',
'LM-E070':'v1空源→false不能套正常选择；后继外层成员门/Select及三消费点限定已保留，直接队伍路径不造正常UI可达。',
'LM-E071':'外层门与已有写入保留正确；统一Yes句仍须由72纠正；C01与CLOSURE-R01不是同一待办。',
'LM-E072':'事件自身仍是修订待审，旧v3独立报告才给具名关闭；两路Yes相反，129回填、158转写及B21资格分别接合。',
'LM-E169':'十七UI作者转写/401设计不是17当前域批准；129/130九输入资格和171作者完成由B21正面限定；三当前提供者的有限记录/开放边界分别收到。'}
openjoins=[
 {'id':'G5-CRE-C','provider':'CRE-C','fixed_carrier':'30cfed0996003b6ebf4b5c51cc04f31ca9255440',
  'objects':'coverage/root-active-snapshot-16/creature_c_existing_crea/{forward,reverse}-mapping.json',
  'actual':'both316B; records=[]; denominator_frozen=false; OPEN_SOURCE_AND_FORMAL_RECEPTION_RUNNING',
  'effect':'不能以此签WP21/22/23/30/31/32完整当前源/条款；N01本组有限源/条款核对不填满CRE-C全域',
  'kind':'FIXED_CARRIER_COMPLETED_CONTRIBUTION_ABSENT; source/formal still readable, not host limit'},
 {'id':'G5-CRE-D','provider':'CRE-D','fixed_carrier':'30cfed0996003b6ebf4b5c51cc04f31ca9255440',
  'actual':'route has exact creature_d readset only, no completed contribution bound',
  'effect':'取得/繁殖/遭遇/捕获及共享测试相关全量接收未完成',
  'kind':'ORIGINAL_ROUTE_EXPLICIT_OPEN; not new required specification defect'},
 {'id':'G5-DEVELOPER','provider':'DEVELOPER','fixed_carrier':'30cfed0996003b6ebf4b5c51cc04f31ca9255440',
  'objects':'coverage/root-active-snapshot-16/developer_full_cloud/{forward,reverse}-mapping.json',
  'actual':'both50B; entries=[]','effect':'WP72–77当前全量业务贡献不能由该路由签收',
  'kind':'FIXED_CARRIER_EMPTY_MAPPING; source/formal still readable, not host limit'},
 {'id':'G5-UI-TRANSITIVE','provider':'UI/UI66/MINIGAMES','actual':'UI interfaces all_interfaces_received=false; 17 records explicitly retain foreign/native/history/compiled/reward opens',
  'effect':'17接口全文与14个WP66选定记录、10个TP选定记录实际接收，不等于146/113/65源单元全部接收；169整批UI及8事件最终完整签收继续OPEN',
  'kind':'AVAILABLE_UNRECEIVED_FOREIGN_BUSINESS_SCOPE; no unread relabelled material limit'}]
s22=TASK/'shards/S22'
dump(s22,'frozen-denominator.json',{**common,'shard':'S22','formal_routes':131,'providers':20,'event_ids':eight,
 'event_content_paragraphs':sum(len(events[e]['content_paragraph_lines']) for e in eight),'event_physical_lines':len(mainlines),
 'event_bytes':sum(len(original_lines[n-1]) for n in mainlines),'necessary_successor_context':supplement,
 'new_primary_event_credit':0,'scope':'Route typed purposes and eight existing event joins; no all131 or whole UI/domain pass'})
dump(s22,'reading-ledger.json',{'reader':ACTUAL,'shared_premises':'../S23/context-and-premises.json',
 'target_route_all_fields':{'path':'current-primary-contribution-routes.v2.json','scope':'all131 route rows and20 providers typed identity/use/reception; unique qualifications read; identities verified separately','chunks':['f1b8a3','f161b5','a317a1','4f0753']},
 'event_all_fields':{'ids':eight,'chunks':['6da0db','b76934','7042b3','2c046f'],'shared_exact_values':'Exact aliases to already read first event; original raw compressed/detailed paragraphs all displayed, not summary substitutes'},
 'successor_all_fields':{'ids':supplement,'chunk':'36114c','new_credit':0},
 'peer_records':[{'object':'tasks/ui_full/interfaces.json','scope':'ALL17 complete records + top fields and closure-artifact identities','chunk':'ed5cfe'},
 {'object':'tasks/ui_wp66/forward-mapping.json','ids':['D06','D07','D09','D10','E05','B12','G01','G02','G03','G04','G05','I01','I02','I03'],'scope':'selected complete14 objects all fields','chunk':'bc06bd'},
 {'object':'tasks/ui_minigames/forward-mapping.json','ids':['MG-TP-%02d'%n for n in range(1,11)],'scope':'selected complete10 objects all fields','chunk':'bc06bd'},
 {'object':'CRE-C/DEVELOPER fixed empty forward/reverse + CRE-D exact route','scope':'all operative fields of empty artifacts / route; no manufactured business records','chunk':'a4de91'}],
 'source_and_formal':s22reading,
 'truncation_repair':'8832e0 mixed provider-index/C display truncated; C missing opening1–12 and remaining121–210 read in1c6c2e; minigames top-level fields separately read there; no full forward/reverse peer-file credit'})
dump(s22,'reception-ledger.json',{'shard':'S22','review_work':'COMPLETED_FINITE_GROUP_REVIEW','state':'INCOMPLETE',
 'routes':[{'id':x['id'],'path':x['path'],'primary_owner':x['primary_owner'],'provider_ids':x['provider_ids'],
   'field_disposition':{'id_path_owner_provider_ids':'read exact current route; not semantic approval','fixed_readset_current_formal_identity':'complete typed identity, all values verified in shared214-input proof','purpose_this_task_credit':'full common value read once; exact equality proved for all131'},
   'decision':'ACCEPT_ROUTING_ONLY','full_formal_or_provider_reception':False} for x in routes['formal_routes']],
 'providers':[{'id':x['id'],'field_disposition':'all route fields read; complete identity verified; use/reception limits binding','decision':'ROUTING_RECEIVED_NOT_FULL_BUSINESS'} for x in routes['providers']],
 'events':[{'id':e,'all_primary_fields_and_raw_text_read':True,'documentary_meaning':event_notes[e],
    'successors_checked':events[e]['actual_successor_events'],'decision':'FINITE_PURPOSE_JOIN_RECEIVED; EVENT_FINAL_NOT_SIGNED',
    'new_event_or_vote_credit':0} for e in eight],
 'accepted_successor_context':supplement,'open_necessary_interfaces':openjoins,'final_event_acceptance_count':0,
 'materials':'No absent readable source/formal file encountered; fixed-carrier empty/unbound contribution and available-unreceived foreign scope kept separate',
 'parent_root_task_final':'ROOT_ONLY'})
dump(s22,'interfaces.json',{'shard':'S22','finite_received':['131 exact B8 routes/20 typed provider routes','8 event original paragraphs and all purpose fields','129/130/158/171 complete successor context','WP66-C210L/WP71178L full current texts','UI17 complete interface records, WP66 selected14/TP selected10 complete records','bounded N01/Dex/Bag/TP real source/consumer/current-clause controls'],
 'not_received':openjoins,'cumulative_join_required':True,'business':'NOT_EXECUTED'})
dump(s22,'proposal-counters.json',{'new_required':0,'new_public_canonical_ids':0,'receipt_gaps':openjoins,
 'H001':'Parent finite NO_REQUIRED_BOUNDED_SCOPE report fully read. This shard does not add another full N01 counter vote or replace parent/root final decision.',
 'strongest_no_required':'B21 README/scope7 and manifest4121/4127 explicitly bind old pending and old approvals to original stages; current WP23/SH34 and historical v3 scope retain correct finite contract. No formal revision from old stage wording alone.',
 'route_caveat':'Shared test-catalog provider list is routing, not exhaustive transitive producer acceptance. Missing/empty current contribution is an acceptance dependency, not proof of a source/spec defect.',
 'independent_counter_vote_added':0})
(s22/'report.md').write_text("""# S22 当前路由及八事件接合

有限审查工作已做完；接收状态仍为INCOMPLETE，UPDATE_NOT_STARTED。131条formal_routes与20个provider已逐字段作身份/用途接收；八个既有事件全文、49内容段/77物理行/37,911字节及全部用途字段已独立读，后继129/130/158/171全文接合。没有重算新事件、新票或131份正式全文通过。

逐事件结论见 reception-ledger.json：66的14项修订、67的11/14与三余项、68的回填、69的18身份错误与原17正确记录、70/71/72的N01外层门/Select/取消前缀/相反确认语义、169的十七UI作者阶段均分别保留。129错误46+5由130明确改41状态+5导航=46，另6新增B链接；158是转写，171明确作者完成。B21与当前R7根导航给旧阶段的正面限定，旧待审或旧批准不转授B8。

补读当前WP66-C全部210行、WP71全部178行，接合Bag存入正常画面、即时排序与三层使用返回、Give生成门，以及TP末格漏扫/3×2端点/合法联动初态/完成截断。相关R定义和实际调用/消费、现行条款及目录完整范围见 reading-ledger.json。另全文接收UI17接口对象、14个WP66及10个TP完整选定record；未冒充整份146/113/65单元源贡献FULL_READ。

真实缺口：固定30cfed0载体的CRE-C两映射各316B、records为空且分母未冻结；Developer两映射各50B、entries为空；CRE-D只有readset。UI17接口仍明列原生控制桥、外域/历史/compiled/奖励等OPEN。它们不能通过文件存在/hash或本组有限事实清零。接收不足的范围与补足条件逐项具名于interfaces.json；可得源/正文未被称为宿主或材料限制。

因此八事件最终完整签收仍为0，父接收者须累计接合真实完整当前贡献或其有限补读证据后决定。新确认required为0；未整改、不重开第七轮27项。所有行为NOT_EXECUTED。固定身份与一次共享身份验证见../S23/context-and-premises.json及identity-and-field-aliases.json。
""")

s23names=json.loads((TASK/'split-contracts/S23.complete.json').read_text())['details']['mandatory_whole_objects']
direct = {
'build-evidence.py':('FULL_SOURCE_TEXT_READ_1_281','历史v1 writer与21组用途原因、五N01事实/提案/881未闭合声明完整读；旧错误不执行不覆盖v2。',['2c0334','a9c1ed']),
'complete-purpose-v2.py':('FULL_SOURCE_TEXT_READ_1_344','v2按手写TSV和冻结事件序列化，正则/标签仅分物理角色；生成路由/格式成功不构成语义审读。',['a9c1ed','8fd7d6','6b0296']),
'core-github-api.json':('FULL_TYPED_OBJECT_READ','75058727的commit/subtree/API对象，仅早core身份；unsigned不用于模型/审者认证。',['b33019']),
'core-readback-execution-attempt1.json':('FULL_READ','08:41 API代理Tunnel403，exit1、空stdout、完整stderr保留，未成功。',['c3535c']),
'core-readback-execution-attempt2.json':('FULL_READ','08:42借只读connector commit/tree后raw回读20文件/2195563B，exit0；不是后继33文件或业务通过。',['c3535c']),
'core-remote-readback.json':('EXACT_VALUE_ALIAS_FULLY_READ','与attempt2.stdout解析对象逐值完全相等；只一次传输信用，原始bytes不同。',['b33019']),
'current-primary-contribution-routes.v2.json':('EXACT_OBJECT_ALIAS_S22','S22全字段用途/身份接收；131业务全文未授。',['f161b5','a317a1','4f0753']),
'event-judgments.v2.tsv':('COMPLETE_FIELD_ROUTING_NOT_156_EVENT_SEMANTIC_READ','round/WP_topics/exact_later_events/current_purpose_judgment逐行绑定156事件；手写判断逐值等于semantic event及paragraph reasons。148事件语义仍归S01–S20、八事件归S22。',['8fd7d6','69b2b3']),
'evidence-catalog.json':('EXACT_VALUE_ALIAS_COMMON_CONTRACT','全部47项与三份complete共用catalog逐值相等；身份/范围/审读声称全文已读，不转授作者FULL_READ。',['77dede','716367','69b2b3']),
'frozen-primary-structure.json':('COMPLETE_TYPED_STRUCTURE_DISPOSITION','1413行identity/offset/hash/type及初始UNREAD/UNVERIFIED/UNDECOMPOSED；前态不能覆盖后态，亦不授新阅读。',['69b2b3','2bbed9']),
'identities.json':('FULL_READ','请求配置与实际UNVERIFIED、原Mac缺失、独占原分支及用户授权历史完整保留；来源线程不是实际执行ID。',['b33019']),
'progress.json':('FULL_READ','作者1413/156/881局部用途完成与root0分列；V2待推/平台退出未知为原时点。',['b33019']),
'protection-after-core-push.json':('FULL_READ','早core发布后main/tag/R保护的有限命令记录；不是Mac或全worktree字节审计。',['b33019']),
'protection-before-push.json':('FULL_READ','早core前HEAD/tree/status/remote记录，范围限云端；不重复制造当时保护凭证。',['b33019']),
'publication-operations.json':('FULL_READ','早core普通commit/push真实I/O/exit/UTC；没有用命令成功代业务成功。',['c3535c']),
'publication.json':('FULL_READ','旧semantic_conclusion INCOMPLETE/881和后继v2_state并存；v2 clarifier限定156用途，不以旧20文件回执认证33文件。',['c3535c']),
'purpose-dispositions.json':('COMPLETE_FIELD_ROUTING_AND_EXACT_ALIASES','units全21字段分别处理：六identity值与冻结逐值等；role/label/structure和共同资格全文；事件原因/后继/routes逐值别名；不以S23替S01–20读历史业务。',['69b2b3','2bbed9']),
'read-chunks.json':('FULL_TYPED_ARRAY_READ','全部34项? 以实际数组长度为准；导航/primary完整start/end/bytes仅作者输出计划，不能证实际读取。',['b33019']),
'reading-ledger.json':('FULL_READ','全部27主读、导航/补读/新17范围/精度修正/旧截断/全局未知均读；v1后继澄清不清全引擎分母，原range只证其范围。',['69b2b3']),
'remote-readback.py':('FULL_SOURCE_TEXT_READ_1_95','硬编码旧worktree/分支、ref断言、connector API证据备用、immutable raw并行逐文件比对；不执行恢复脚本。',['6b0296']),
'semantic-purpose-freeze.v2.json':('COMPLETE_TYPED_STRUCTURE_DISPOSITION','156事件物理边界/行ID/内容段绑定为用途人口，冻结在首次物理读完后，未倒填审前。',['69b2b3','2bbed9']),
'semantic-purpose-review.v2.json':('COMPLETE_FIELD_ROUTING_NOT_156_EVENT_SEMANTIC_READ','全部字段覆盖：共同四层资格全文一次；156手写reader_judgment和后继业务字段精确交各事件owner；本组八事件/四后继实际读，不替全156签。',['69b2b3','2bbed9']),
'validate-evidence.py':('FULL_SOURCE_TEXT_READ_1_58','JSON/集合/连续区间/hash/声明一致/保护机械检查；没有检验真实语义读取。旧still incomplete atomic inheritance字面不覆盖v2用途澄清。',['6b0296']),
'validation.json':('FULL_READ','15检查exit0仅TOOL_VALIDATION；作者状态一致不证明本轮语义全部接收。',['b33019']),
'world-interface-reception.v2.json':('EXACT_OBJECT_ALIAS_S21','S21十二完整记录及五有限链；不再给S23第二份事实/票信用。',['513586'])}
direct['read-chunks.json']=('FULL_TYPED_ARRAY_READ',f"全部{len(load('read-chunks.json'))}项role/start/end/bytes完整读；只证作者分片计划，不证明实际读取。",['b33019'])
fileids={r['relative_to_target_task']:r for r in json.loads((HERE/'input-recovery.json').read_text())['files']}
artifact=[]
for n in s23names:
    state,reason,chunks=direct[n]
    keys=list(load(n)) if n.endswith('.json') and isinstance(load(n),dict) else None
    artifact.append({'path':n,'raw_identity':{k:fileids[n][k] for k in ['mode','git_blob','bytes','sha256']},
      'complete_field_disposition':state,'meaning_and_qualification':reason,'top_level_keys_covered':keys,
      'actual_output_chunks':chunks,'full_business_semantics_accepted':False if n in ['event-judgments.v2.tsv','purpose-dispositions.json','semantic-purpose-review.v2.json','current-primary-contribution-routes.v2.json'] else 'Only described exact purpose, never global acceptance'})
dump(HERE,'frozen-denominator.json',{**common,'shard':'S23','objects':s23names,'object_count':25,'raw_bytes':sum(fileids[n]['bytes'] for n in s23names),
 'shared_alias_objects':['world-interface-reception.v2.json→S21','current-primary-contribution-routes.v2.json→S22'],
 'scripts':{'files':4,'lines':778,'executed':0},'no_automatic_all156_event_semantic_credit':True})
dump(HERE,'reading-ledger.json',{'reader':ACTUAL,'common':'context-and-premises.json','artifacts':artifact,
 'exact_alias_proof':'identity-and-field-aliases.json','old_failure_originals':'immutable target paths in input-recovery.json; local inert copy inputs/target-93d7df7f, not republished',
 'target_review_full_read':{'path':'review.md','chunk':'eeb8c1'},
 'parent_report_full_read':{'path':'../..//report.md','chunk':'7e029c'},
 'parent_counter_full_read':{'path':'../../counter-h001.md','chunk':'eeb8c1','adoption':'document qualification only; not another all-N01 source counter vote'},
 'truncations':['Initial six full connector responses exceeded output budget; complete prompt attachment and exact shared JSON fields subsequently displayed in bounded/deduplicated parts. No semantic credit for truncated output.',
 'Common catalog first oversized display had a missing middle; E-WP23 through E-COVERAGE-CONTRACT and E-R8-INPUTS/E-HISTORY-NAV later displayed completely.',
 '8832e0 mixed display repaired as recorded in S22; no sampled all-provider FULL_READ.'],
 'generation_and_verification_credit':0,'private_platform_complete_stream':'NOT_EXPORTED; no claim that this public ledger contains it'})
dump(HERE,'reception-ledger.json',{'shard':'S23','review_work':'COMPLETED_FINITE_FIELD_PURPOSE_REVIEW','state':'READY_FOR_ROOT_SHARD_TYPED_PURPOSE_ACCEPTANCE',
 'objects':artifact,'bulk_field_partition':{
 'frozen_primary_units':'id,line,byte_start,byte_end,bytes,sha256 pure identity verified; physical_type/read_state/purpose_state/semantic_assertions unique exact values read and retained as pre-read state',
 'purpose_units':'six identity fields as above; structure/read/purpose_status/current_behavior_reliance/root_reception/exemption/paragraph_role/paragraph_label/semantic_assertion_disposition/effective_qualification all values purpose-read; semantic_event/reason/successors/routes exact aliases to responsible events',
 'semantic_freeze_units':'id,round,line_ranges,primary_line_ids,content_paragraph_lines identity/structure; read and purpose_review are historical claims, not borrowed credit',
 'semantic_review_units':'freeze aliases plus WP_topics/reader_judgment/successors/routes delegated by exact event; common behavior/acceptance/identity/workflow/not_claimed qualifications read once',
 'tsv':'round and WP_topics typed structure; exact_later_events and current_purpose_judgment exact semantic-event aliases; 148 primary events remain S01–20, eight S22'},
 'necessary_unread_for_typed_purpose':[],'external_primary_semantic_reception':'148 events S01–S20 and remaining S22 joins stay root-unreceived here; no false whole25-business acceptance',
 'root_final':'ROOT_ONLY','material_blockers':[]})
dump(HERE,'interfaces.json',{'shard':'S23','S21':'world object exact alias; five independent static joins received there','S22':'route object exact alias; current business open objects retained',
 'S01_to_S20':'156 semantic event records minus eight existing =148 exact event and paragraph value aliases verified; owner/list in identity-and-field-aliases.json, no semantic read or acceptance credit from this proof',
 'history_tool':'attempt1/2 and v1 writer/qualification precede v2; preserve all failures and successor clarifier; no rerun',
 'publication':'old20-file core proof does not cover target33; own33 recovery/identity exact independently checked once','all_global_interfaces_closed':False})
dump(HERE,'proposal-counters.json',{'new_required':0,'new_canonical_ids':0,'new_counter_votes':0,
 'semantic_status_precision':'v1 incomplete atomic inheritance and v2 complete documentary purpose are different scopes; retain both, do not infer全引擎已完备',
 'old_failure':'attempt1 exit1 API proxy403; attempt2 exit0 core75058727 only; complete stderr/stdout available at immutable original paths',
 'inheritance':'All optional/Float/policy/limit/no-required remain original categories; no user policy chosen or old27 reopened'})
(HERE/'report.md').write_text("""# S23 工具、身份及旧失败资格接收

状态：READY_FOR_ROOT_SHARD_TYPED_PURPOSE_ACCEPTANCE；UPDATE_NOT_STARTED。25对象全部完成字段用途处置，四脚本778行实际完整阅读、执行0。这里的完成是本shard字段/资格接收，不能表述成156历史事件或25对象全部业务批准。

原始33载荷/3,736,917字节已在自有bare普通fetch固定93d7df7f后完整恢复，集合/mode/blob/bytes/SHA/checkout与任务tree均一致；本组早先从父固定缓存展示的对象逐文件与自有恢复逐字节相同。恢复原件留在忽略的惰性缓存；提交只发自身增量与精确恢复/身份索引，不重复发布既有3.7MB。214个唯一源/规格/readset/provider Git输入核身份，只计工具信用。

大JSON没有被笼统降为元资料：全部1413物理身份、角色/标签、旧读态和用途资格逐字段处置；156事件手写判断、后继、路由在TSV/event/paragraph间逐值别名证明，原始业务意义仍归S01–S20及S22。148事件在这里没有实际语义阅读或接收信用。world及131routes分别复用S21/S22，不重复加事实或票。具体字段分区见reception-ledger.json。

旧v1 writer完整保留881未闭合声明、五N01有限事实和H001最强反向材料。v2澄清的是156纪录用途，绝非全引擎原子完备。frozen文件的UNREAD是审前状态，后继作者FULL_READ不认证本接收者。reading-ledger与publication中的原时点/后继字段全部保留。

attempt1：API代理Tunnel403、exit1、stdout空，未成功。attempt2：只读connector提供早core身份，再raw回读20文件/2,195,563字节、exit0。core-remote-readback与attempt2.stdout解析值完全相同，只一次传输信用；这些是75058727早core，不是后继33文件或本组语义通过。恢复的原脚本均未执行。

本组身份复用、字段别名和作用范围已闭合；其它148事件语义、S22当前完整外域接合及根最终裁决仍保持各自OPEN。没有静态文件不可得阻塞，没有新required/政策选择/整改/运行。真实上下文与原作者、父接收者不同；实际模型/effort/tier/speed/Fast仍UNVERIFIED。公共完整私有平台流未导出，不倒填平台结束时刻。
""")
dump(HERE,'failures-and-qualifications.json',{'schema':'r8-group5-failures/v1','scope':'Actual visible tool failures; not an invented full private session log',
 'entries':[{'chunk':'695d6c','exit':128,'failure':'git status at /workspace before locating repo; corrected cwd'},
 {'chunk':'07090e','exit':1,'failure':'contract absent on initial B8 worktree; fetched exact frozen contract'},
 {'chunk':'0a7408','exit':1,'failure':"own verification helper assumed details.events; actual S01 has events_all_fields; corrected schema, rerun a4de91 passed214 identities"},
 {'chunks':['a238be','38560c'],'exit':2,'failure':'incorrect source path/cwd in locator searches; corrected actual reference paths; no absence inference'},
 {'kind':'OUTPUT_TRUNCATIONS','qualification':'Retained and supplemented as reading-ledger records; cannot claim initially truncated material read'},
 {'kind':'ORIGINAL_ATTEMPT1_2','qualification':'Complete original blobs preserved; no deletion/reclassification as business tests'}],
 'not_executed':'all recovered scripts and reference/game code; no automatic-review rejection occurred'})
print(json.dumps({'reader':ACTUAL,'shards':['S21','S22','S23'],'S21':'READY_FOR_ROOT_SHARD_ACCEPTANCE','S22':'INCOMPLETE explicit current-domain joins','S23':'READY_FOR_ROOT_SHARD_TYPED_PURPOSE_ACCEPTANCE','new_required':0,'own_business_runs':0}))
