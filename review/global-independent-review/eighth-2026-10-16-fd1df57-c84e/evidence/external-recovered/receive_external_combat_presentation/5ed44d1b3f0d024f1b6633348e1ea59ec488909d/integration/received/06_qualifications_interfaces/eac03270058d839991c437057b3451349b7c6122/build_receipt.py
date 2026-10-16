"""Serialize this reviewer's explicit decisions; no reference behavior executed."""
from pathlib import Path
import json, hashlib, subprocess, collections, datetime, re
O=Path(__file__).resolve().parent
T=O.parents[1]
REPO=Path('/workspace/pokemon-essentials-clean-room')
REF=Path('/workspace/pokemon-essentials')
ROOT=T.parents[1]
A=json.loads((T/'continuation/06_qualifications_interfaces/readset.complete.json').read_text())
RAW=T/'recovered'/A['target_commit']
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(name,x): (O/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ident(p):
 b=p.read_bytes()
 return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'lines':len(b.decode('utf-8').splitlines())}
def sh(*args,cwd=REPO): return subprocess.check_output(args,cwd=cwd,text=True).strip()
identity={'schema':'r8-cp06-actual-identity/v1','utc':UTC,'role':'bounded independent receiver 06_qualifications_interfaces','branch':sh('git','branch','--show-current'),'contract_commit':'35d85e4484b892ebc32542346861440638d2183c','embedded_group_readset_contract_commit':A['contract_commit'],'embedded_binding_qualification':'Preserved readset field40f45 is historical metadata; this reception is frozen at user-specified35d85.','contract_tree':sh('git','rev-parse','35d85e4484b892ebc32542346861440638d2183c^{tree}'),'B8':A['fixed_B8'],'B8_tree':sh('git','rev-parse',A['fixed_B8']+'^{tree}'),'formal_tree':sh('git','rev-parse',A['fixed_B8']+':deliverables/final-specification-set'),'R':A['fixed_R'],'R_tree':sh('git','rev-parse','HEAD^{tree}',cwd=REF),'target_commit':A['target_commit'],'target_checkout_tree':A['target_checkout_tree'],'target_task_tree':A['target_task_tree'],'git_identity':{'name':sh('git','config','user.name'),'email':sh('git','config','user.email')},'requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal/default','Fast':False},'actual_configuration':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast']},'actual_platform_context_uuid':'UNVERIFIED; no authoritative platform echo supplied','original_author_context':'01a143b2-8ba3-76f5-a39d-7904a2dd1000','previous_parent_receiver_context':'01a14479-e75c-7131-85ed-aec1de217031','delegation_source_thread':'01a13f49-a154-7054-9b04-ce31f924d01c; not asserted to be this receiver UUID','independence':'This delegated task is separate from author and prior receiver in the supplied task context; no alias/role renaming or fabricated platform UUID is used. No subagents spawned.','exclusive_write_set':str(O.relative_to(REPO))+'/','UPDATE_NOT_STARTED':True}
dump('identity.json',identity)
# Manual reception reasoning, one complete decision for each declared reverse group.
reasons={
1:'入口先对方开场再玩家派出；Scene先建图后Intro。普通intro/派出等待与受showAnims门的Shiny公共动画分开，未据请求授声音或像素成功。',
2:'prepare_battle提供背景/平台/时间输入；Scene对背景与消息各查时段资源，base0决定双方组合前缀。组合失败才独立平台，独立平台不另补第二次回退。',
3:'四格方向/记忆/USE及mode1的BACK由Scene决定；SHADOW类型存在且训练家战才把Run改Call，SkyDrop先行阻止该席选择。后继命令取消会回退前席并撤销登记。',
4:'命令、攻击、回合末和正decision退出点分开；普通pbEndOfBattle才进行还原/退款等后段，Scene abort只清场景，不授正常终局义务。',
5:'Debug固定确认真、命令0、物品-1、遗忘0。随机Bag1/15及剩余Call1/10具有条件门，且单数move读取可先失败。生成器真实战斗分支controlPlayer使AI路径可绕过Debug输入。',
6:'音频入口依next/map/global/default优先级；训练家序列最后非nil配置生效，空串不等nil。intro cue和选曲记忆只证明请求，不证明设备播放。',
7:'招式槽、PP文字/色阶及本席记忆和Mega/Shift独立；回调接受才退出，Shift取消Mega登记。自动/挣扎/不可选择分支不经过同一菜单。',
8:'Call的超模式清除/心量、睡眠治疗、可升命中及无事发生按分支。裸登记Call与UI SHADOW门不是同一资格检查；本组不把注册当执行。',
9:'nil、空串、姓名分别影响按钮/导航/文字。NearAlly初选传Battler对象给不规范化的nearBattlers?，三打可错误放行远端；确认不重查texts，执行pbFindTargets/pbMoveCanTarget?仍可拒远端。',
10:'战斗背包internalBattle门及battle_use过滤独立；1/3自动拒后手选、2再选招、4敌席、5无成员。蛋拒绝、取消层级、正常返回恢复野外游标均沿真实消费者。',
11:'登记扣物后攻击时重核；1/2/3/5失败退款保留choice，4球不如此退款。下一命令/倒下清理与普通终局再退款有独立时点；背包容量只保证实际已插入前缀。',
12:'canCancel由主动/强制/捕获入口决定；显示排序反查实际party下标。换入/换出限制、lax与严格模式分开，召回Illusion与Arena不准主动换人按调用者，未扩展全部换人规则。',
13:'普通经验循环和Shadow保存经验分开；收益消息先于分段经验提交，提交先于经验条请求；等级/能力值已写才开增量和新值窗。1.75比例及满槽0.2秒属于请求计时。',
14:'空招槽先持久个体写入再提示、场上副本后同步；满招替换两者在TaDa前更新。取消后放弃确认可重选，HM门正常开启、DEBUG豁免。',
15:'投掷消息早于挡球；0..3失败与4成功分开。成功先移除场上目标再经验/后段处理，critical只是展示压缩；野生ME等待3.5秒不授实际声长。',
16:'图鉴三门和owned写入分开；命名先写名后接收。满队99取消与强制入队独立；旧成员先入盒再删、消息后移四类记忆。伙伴合并队伍与玩家实际队伍身份不保证一致。',
17:'普通1秒/brief后继1秒/暂停非战末3秒分别计时。busy时快进和resume有别，消息块至多一次；BattleEnd取消自动关闭。原生墙钟与实际输入未执行。',
18:'仅玩家单席HP数字/EXP门；HP固定1秒、数字单独to_i、色阶用浮点h对整数T阈值、宽度偶数量化。图标及框/成员选择摆动独立。',
19:'多只派出共同循环，各框仅等自球；召回球后框。特性条阻塞、伤害并行、倒下叫声等待后裁底下落并与框轨道共同推进；成功球脱离临时销毁，影子仅正常返回恢复。',
20:'精确OppMove/Move与hitNum，默认18x6身份及两独立偏移/回退不加原hitNum。Common首名与招式影子包装不同；20fps作者播放器及正常恢复边界已接合。',
21:'Safari预算和菜单、Bug比较替换、Palace自动招式/Arena裁判、Replay预录回放分别由覆写进入，不能把共用Scene当所有变体规则已验收。',
22:'默认开关来自Battle初始化与局部设置；variant/Debug差异明确，R6/R7限制和静态未执行保留。有限接口完成不替代其余五组或全局历史接收。',
23:'作者库27索引/25语义字段/60常规槽及五timing数据独立于固定轨道；先渐变后事件、共享旧值、整组RGBA、坐标符号、前景自身opacity、duration0捕获、20fps访问跳帧不补事件和64编辑偏移均得到player与正式必要节支持。',
24:'旧格式仅常规槽转换；RPG转换只有定义和注释编译调用，限定散文件搜索无默认活动caller。Move/Opp命名有效身份使changed并写出，缓存各自寿命；canvas.play无保存，正常编辑退出保存是独立分支。',
25:'HP/rate/status/UltraBeast修正、四次首失败停止、critical及19球种handler沿捕获核心。记录/图鉴/命名/存储按前缀，容量/伙伴错配已由WP38明确；旧peer失败返回笔记按CP06-Q001更正。',
26:'战斗招式副本PP与持久realMove对象引用分开；非Transform写realMove.pp，概要换序移动同一对象，不能把原槽下标当当前持久招槽。学招路径明确同步对象。',
27:'Safari四命令/球预算写回、饵/石概率和天气；Safari内部图鉴门独立。Bug球预算不等Bag，比较后替换及异常前缀不保证回滚，BallEnd会话与战斗结局分开。',
28:'Palace类别分布只部分可选检查，2A+D；Arena主动换人禁、轮数>=3裁定且换人不重置，裁判图形更新借通用消息。请求不证明素材实际显示。',
29:'回放Scene可中止且部分普通选择交互仍存在；预录选择/随机/换人通道与普通终局分层。facility包装ensure清理不等Scene abort通用恢复，队伍clone不等全局隔离。',
30:'共享Party初选0/网格/取消，Summary inbattle只禁options；持久招换序及Shadow拒绝、额外新招/BACK-1、HM/DEBUG及空首招首次绘制失败均对照当前WP66-A。',
31:'Battle有独立消息循环，使用共享busy/pausing/resume/skipAhead。行满插暂停与滚动继续的组件路径已读；Arena通用消息每轮更新裁判图形，键盘ESC空串和光标BACK删除不是同一取消。'
}
# Evidence IDs refer to exact source parents below; only listed intervals carry reading credit.
names={
'SC':'011_Battle/004_Scene/001_Battle_Scene.rb','INIT':'011_Battle/004_Scene/002_Scene_Initialize.rb','CHOOSE':'011_Battle/004_Scene/003_Scene_ChooseCommands.rb','PLAY':'011_Battle/004_Scene/004_Scene_PlayAnimations.rb','MENUS':'011_Battle/004_Scene/005_Battle_Scene_Menus.rb','BOX':'011_Battle/004_Scene/006_Battle_Scene_Objects.rb','BASEANIM':'011_Battle/004_Scene/007_Battle_Scene_BaseAnimation.rb','ANIM':'011_Battle/004_Scene/008_Battle_Scene_Animations.rb','PLAYER':'011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb','COMMAND':'011_Battle/001_Battle/009_Battle_CommandPhase.rb','ATTACK':'011_Battle/001_Battle/010_Battle_AttackPhase.rb','OTHER':'011_Battle/001_Battle/008_Battle_ActionOther.rb','ITEM':'011_Battle/001_Battle/006_Battle_ActionUseItem.rb','SWITCH':'011_Battle/001_Battle/005_Battle_ActionSwitching.rb','END':'011_Battle/001_Battle/002_Battle_StartAndEnd.rb','EXP':'011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb','BATTLE':'011_Battle/001_Battle/001_Battle.rb','HP':'011_Battle/002_Battler/003_Battler_ChangeSelf.rb','BATTLER':'011_Battle/002_Battler/001_Battle_Battler.rb','PRIORITY':'011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb','TARGET':'011_Battle/002_Battler/008_Battler_UseMoveTargeting.rb','CATCH':'011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb','BALL':'011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb','PEER':'011_Battle/007_Other battle code/004_Battle_Peers.rb','DEBUG':'011_Battle/004_Scene/009_Battle_DebugScene.rb','AUDIO':'012_Overworld/002_Battle triggering/003_Utilities_BattleAudio.rb','SAFARI':'011_Battle/008_Other battle types/001_SafariBattle.rb','BUG':'011_Battle/008_Other battle types/002_BugContestBattle.rb','PALACE':'011_Battle/008_Other battle types/003_BattlePalaceBattle.rb','ARENA':'011_Battle/008_Other battle types/004_BattleArenaBattle.rb','RECORD':'011_Battle/008_Other battle types/005_RecordedBattle.rb','PARTY':'016_UI/005_UI_Party.rb','SUMMARY':'016_UI/006_UI_Summary.rb','BAG':'016_UI/007_UI_Bag.rb','TEXT':'016_UI/025_UI_TextEntry.rb','MESSAGE':'007_Objects and windows/011_Messages.rb','TEXTWIN':'007_Objects and windows/005_SpriteWindow_text.rb','PICTURE':'007_Objects and windows/010_PictureEx.rb','MOVE':'011_Battle/003_Move/001_Battle_Move.rb','CRY':'010_Data/002_PBS data/009_Species_files.rb','PREPARE':'012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb'}
names.update({'GENERATOR':'018_Alternate battle modes/004_BattleChallenge/004_ChallengeGenerator_BattleSim.rb','STORAGE':'014_Pokemon/004_PokemonStorage.rb','FACILITY':'018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb','CACHE':'010_Data/002_PBS data/001_MiscPBSData.rb','COMPILER':'021_Compiler/002_Compiler_CompilePBS.rb','CONVERT':'020_Debug/002_Animation editor/004_AnimEditor_ExportImport.rb','EDITMAIN':'020_Debug/002_Animation editor/005_AnimEditor_Functions.rb','PREVIEW':'020_Debug/002_Animation editor/001_AnimEditor_SceneElements.rb'})
# Resolve only filenames that are unique; incorrect guessed prefixes confer no evidence.
allrefs=list((REF/'Data/Scripts').rglob('*.rb'))
for k,v in list(names.items()):
 p=REF/'Data/Scripts'/v
 if not p.exists():
  hits=[x for x in allrefs if x.name==Path(v).name]
  if len(hits)!=1:
   # Explicit actual alternate basenames, not a silent fuzzy substitute.
   alt={'PICTURE':'009_PictureEx.rb','DEBUG':'010_Battle_SceneDebug.rb','TARGET':'004_Battler_UseMoveTargeting.rb'}
   if k in alt:hits=[x for x in allrefs if x.name==alt[k]]
  assert len(hits)==1,(k,v,[str(x) for x in hits])
  p=hits[0]
 names[k]=str(p)
group_ev={1:['INIT','PLAY','END'],2:['PREPARE','INIT'],3:['COMMAND','CHOOSE'],4:['END','COMMAND','ATTACK'],5:['DEBUG','COMMAND'],6:['AUDIO'],7:['CHOOSE','COMMAND','MENUS','PRIORITY'],8:['OTHER','COMMAND'],9:['CHOOSE','BATTLE','TARGET'],10:['CHOOSE','BAG','ITEM'],11:['COMMAND','ATTACK','ITEM','END'],12:['CHOOSE','SWITCH','ARENA','PARTY'],13:['EXP','PLAY','BOX'],14:['EXP','SUMMARY'],15:['CATCH','PLAY','ANIM'],16:['CATCH','PEER','END'],17:['SC','TEXTWIN'],18:['BOX','MENUS'],19:['PLAY','BASEANIM','ANIM'],20:['PLAY','PLAYER'],21:['SAFARI','BUG','PALACE','ARENA','RECORD'],22:['BATTLE','SC','DEBUG'],23:['PLAYER'],24:['PLAYER'],25:['CATCH','BALL','PEER'],26:['HP','MOVE','SUMMARY','EXP'],27:['SAFARI','BUG'],28:['PALACE','ARENA'],29:['RECORD','END','SC'],30:['PARTY','SUMMARY'],31:['SC','MESSAGE','TEXTWIN','TEXT','ARENA']}
group_ev[5].append('GENERATOR')
group_ev[16].append('STORAGE')
group_ev[24].extend(['CACHE','COMPILER','CONVERT','EDITMAIN','PREVIEW'])
group_ev[29].append('FACILITY')
rev=[]
for g in A['reverse_current_contribution_objects']:
 n=int(g['id'][-3:]);assert n in reasons
 for sub in g['subassertions']:
  row={'id':sub['id'],'group':g['id'],'original_assertion':sub['assertion'],'formal':g['formal'],'formal_section':g['section'],'formal_locator_range':g['range'],'decision':'RECEIVED_STATIC_BOUNDED','independent_reason':reasons[n],'evidence_ids':group_ev[n],'evidence_level':'SOURCE_STATIC + CURRENT_FORMAL_STATIC; NOT_EXECUTED','scope':'Only this named proposition; adjacent clauses and entire parent/domain are not upgraded.'}
  if sub['id']=='EXTCP-R013.2':row.update(decision='RECEIVED_WITH_EXPLICIT_QUALIFICATION',qualification='提交先于经验条请求；收益消息可能更早。不得解释为所有显示均在经验写入之后。')
  if sub['id']=='EXTCP-R025.6':row['qualification']='任何失败返回主张均受CP06-Q001限制：默认Peer满仓路径可先在消息调用失败。'
  rev.append(row)
dump('reverse-reception.json',{'schema':'r8-cp06-reverse-assertions/v1','count':len(rev),'groups':31,'rows':rev,'not_primary_source_denominator':True})
ir_reason=[
'初始Intro阻塞与Shiny经Battle.showAnims门分开；队列等待完整。',
'Animation.update在本轮开始见running即保留unfinished；全轨结束后下一次开头才done。',
'addNewSprite进入tempSprites；addSprite借用sprites不进入临时销毁。capture成功在dispose前移出其球。',
'pbSendOut把trainer fade、多球、各自框共同update；框由对应球done开门，结束仍等全部框/队列。',
'原并行措辞必须限定：倒下轨道内部先等所选叫声长度，再下落/裁底；只有此轨道整体与数据框退场共同推进。召回仍先球后框。',
'闪烁Animation数组和animatingHP标志全部清除才返回。',
'capture animation done与inPartyAnimation?共同退出；不是球done即返回。',
'deflect独立Animation等待；不进入捕获吸入/保留球路径。',
'成功球从temp移到captureBall；hide同时驱动数据框退场和1秒opacity补间。',
'仅野生pbWildBattleSuccess请求ME，等待3.5秒并stop；实际媒体/墙钟未证。',
'PBAnimationPlayerX读取作者数据库，固定Animation/BallAnimationMixin注册PictureEx；名称/调度/生命周期分开。',
'WP67-A9.4逐帧坐标/轨迹排除可解释视觉参数；未明确排除固定倒下75音高/音高折算等待。CP002有限缺漏候选保留，不能把496表全转录绑定为同项。',
'作者player固定20fps，cel与timing来自PBAnimation，speed元数据未消费。',
'作者player只处理实际新frame，跳帧不回放漏过timing；PictureEx按到期process逐项处理。',
'PictureEx首次update设置timer_start；名义单位1/20秒，首次实际处理点独立。',
'processes按插入遍历，同一到期时刻的set/move/callback保持登记顺序。',
'动作首次实际处理捕获当时属性；progress相对于计划delay，可因迟到先跳进度，非预先冻结所有起点。',
'Picture时钟与作者player/HP/EXP各自独立；聚合额外一次update不等固定真实0.05秒。',
'AnimatedBitmap nil/前缀PNG验证与普通Gif救援、直接cache路径、IconSprite清旧后建新均分开，失败不承诺恢复。',
'cry选择/长度及SE调用仅证明身份、pitch/volume和请求；缺资源/宿主/设备实际声音未知。']
irs=[]
for x,reason in zip(A['selected_reverse_interfaces'],ir_reason,strict=True):
 y=dict(x);y['original_reception']=y.pop('reception',None);y['independent_decision']='RECEIVED_WITH_QUALIFICATION' if x['id'] in ['EXTCP-IR005','EXTCP-IR012'] else 'RECEIVED_STATIC_BOUNDED';y['independent_reason']=reason;y['execution']='NOT_EXECUTED';irs.append(y)
# All old edges, including the duplicated IF09 namespace, receive independent scope decisions.
legacy=A['qualification_obligations']['interfaces_all'];oldedges=[]
for collection in ['interfaces','continuation_interfaces']:
 for x in legacy.get(collection,[]):
  y=dict(x);y['namespace']=collection+'/'+x['id'];y['original_reception']=y.pop('reception',None);y['independent_reception']='RECEIVED_STATIC_BOUNDED_WITH_REMAINING_GLOBAL_RECEPTIONS';y['qualification']='The cited full-source list is author provenance, not this receiver whole-file credit; actual intervals are in reading-ledger. IF05 applies CP06-Q001; fixed-track edge retains CP002. No domain-wide acceptance.';oldedges.append(y)
dump('interfaces.json',{'schema':'r8-cp06-complete-interface-reception/v1','selected_count':20,'selected':irs,'legacy_edge_count':len(oldedges),'legacy_edges':oldedges,'namespace_rule':'interfaces/IF09 is background/audio; continuation_interfaces/IF09 is fixed-track SE. They are distinct objects.','provider_units':6,'provider_assertions':66,'independence':identity['independence'],'final_authority':'Parent and root retain canonical/task-final decisions; no new administrative review layer required.','UPDATE_NOT_STARTED':True})
# Provider assertions: full selected units, no credit for provider's unselected text.
provider=A['qualification_obligations']['six_provider_units_full'];provider_rows=[]
for u in provider['payloads']:
 for z in u['assertions']:
  provider_rows.append({'id':z['id'],'original_claim':z['claim'],'unit':u['unit_id'],'source':u['source'],'formal_references':u['spec'],'decision':'RECEIVED_STATIC_BOUNDED','basis':'This receiver independently read the complete selected source interval and its actual presentation/resource consumer; exact per-parent intervals in reading-ledger. The written claim is accepted under the stated premise, without native output or whole-provider credit.','premises':u['premises'],'execution':'NOT_EXECUTED'})
dump('provider-reception.json',{'schema':'r8-cp06-provider-reception/v1','fixed_provider_artifact':provider['exact_provider_artifact'],'units':6,'assertions':66,'rows':provider_rows,'whole_provider_credit':False})
# All eight mandatory corrections retained verbatim; adopt only the qualified fact.
bat=A['full_battler_supplement']['adjudication/root-battler-eight-consumer-facts-reception.v1.json'];unitinput=ROOT/'adjudication/root-battler-eight-facts-exact-inputs.v1.json';bu=json.loads(unitinput.read_text());unitmeta=[]
for i,u in enumerate(bu['complete_necessary_units'],1):
 d=bu['identities'][u['source_identity']];p=Path(d['repo'])/d['path'];b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==d['sha256']
 assert ''.join(b.decode().splitlines(keepends=True)[u['range'][0]-1:u['range'][1]])==u['text']
 unitmeta.append({'unit':i,'source_identity':u['source_identity'],'identity':ident(p),'complete_range':u['range'],'decision':'ACTUALLY_READ_COMPLETE_NECESSARY_UNIT','actual_read_basis':'Earlier direct-source/full-parent reading plus full battler-unread-increment.txt 1–1590. Exact source-text equality checked; ephemeral source-copy views removed before publication.','whole_parent_credit':False})
batrecords=[]
for x in bat['sections']['3_complete_eight_receipts']:
 y=dict(x);y['this_receiver_decision']='RECEIVED_QUALIFIED_FACT_ONLY';y['this_receiver_reason']='Independent complete 31-unit reading confirms the mandatory correction. Original fact is preserved as history and is not adopted unchanged. No 810 assertions or complete foreign domain credited.';batrecords.append(y)
dump('battler-reception.json',{'schema':'r8-cp06-eight-qualified-battler-facts/v1','exact_input_identity':ident(unitinput),'complete_units':unitmeta,'facts':batrecords,'units_count':31,'facts_count':8,'execution':'NOT_EXECUTED','source_fragment_republication':False})
# Reading ledger: presentation is not automatic credit. Explicit notes repair truncation/early direct-cat provenance.
events=[json.loads(x) for x in (O/'presentation-events.jsonl').read_text().splitlines()]
by=collections.OrderedDict()
for e in events:
 p=e['path']
 if p.startswith(str(O)+'/'):continue
 by.setdefault(p,{'identity':{k:e[k] for k in ['path','bytes','sha256','git_blob','total_lines']},'presented_ranges':[],'reading_qualification':'Actual literal review with bounded semantic decisions in reverse/interfaces/provider/battler files; no behavior execution.'})['presented_ranges'].append(e['shown_lines'])
for p,ran in [(REF/'Data/Scripts/011_Battle/004_Scene/002_Scene_Initialize.rb',[1,191]),(REF/'Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb',[1,134]),(REF/'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',[209,304])]:
 k=str(p);by.setdefault(k,{'identity':ident(p),'presented_ranges':[],'reading_qualification':'Direct full text originally read in tool output 4cd4f7; later overlap retained, not double counted.'})['presented_ranges'].append(ran)
for u in unitmeta:
 p=u['identity']['path'];by.setdefault(p,{'identity':u['identity'],'presented_ranges':[],'reading_qualification':'Full exact necessary Battler unit read through equality-checked incremental literal view.'})['presented_ranges'].append(u['complete_range'])
for p,v in by.items():
 n=v['identity'].get('total_lines',v['identity'].get('lines'));covered=set()
 for lo,hi in v['presented_ranges']:covered.update(range(lo,hi+1))
 merged=[]
 for z in sorted(covered):
  if merged and z==merged[-1][1]+1:merged[-1][1]=z
  else:merged.append([z,z])
 v['read_ranges_union']=merged;v['whole_parent_literal_read']=len(covered)==n;v['remaining_parent_lines']=n-len(covered);v['remaining_scope']='Outside declared necessary units unless separately listed; not a material limit, not adopted as whole-parent semantics.'
# Record already repaired output incidents explicitly, without falsely granting failed calls credit.
incidents=[{'kind':'OUTPUT_TRUNCATION_REPAIRED','scope':'WP15 203–224; scope-statement 1–55; readset semantic strings 241–279; ActionOther 1–44 and later38–62','disposition':'Only union of actually visible repaired ranges used. Truncated attempts give no independent full credit.'},{'kind':'BAD_RANGE_OR_PATH_REPAIRED','scope':'AnimatedBitmap 1–228; PokeBallEffects1–198; delivery/eighth-review-inputs1640–1781; compiler1274–1321; ExportImport89–147; ActionOther actual basename','disposition':'Failed assertions/FileNotFound calls read no semantic content; corrected calls completed the necessary units.'},{'kind':'READ_VIEW_FILTER_REPAIRED','scope':'Slash-bearing prose was overclassified as locator in temporary payload/history display filters','disposition':'All newly recovered 142 payload and139 historical values were fully reread from explicit repair views. Exact aliases retained. No excluded prose receives credit merely from a pathname test.'}]
# All 31 current operative objects purpose-classified, not blanket transport exemption.
payload=[]
ids=json.loads((O/'input-identities.json').read_text())
for f in ids['files']:
 n=f['relative_to_target_task'];row=dict(f)
 if n.endswith('.py'):
  row.update(purpose='AUTHOR_GENERATOR_OR_VALIDATOR_CURRENT_CLAIMS',actual_scope='All meaning-bearing literals extracted statically with AST; exact aliases to readset/payload values, remaining literal reading views, and control purpose reviewed. Recovered code never executed. Its PASS/commit/readback claims are historical assertions, not this receiver execution proof.',decision='RECEIVED_AS_QUALIFIED_AUTHOR_PROVENANCE')
 elif n in ['atomic-assertions.json','forward-mapping.json','ball-color-fields.json','release-variance-fields.json','capture-variance-fields.json']:
  row.update(purpose='QUALIFICATIONS_AND_DENOMINATOR_WITH_FOREIGN_PRIMARY_FACTS',actual_scope='Current scope/status/count/limitations and operative provenance fully purpose-read through exact scalar aliases and remaining views. Underlying 1045 source assertions are assigned to groups01–05; this group adds0 primary acceptance and does not repeat them.',decision='QUALIFICATIONS_RECEIVED_PRIMARY_ACCEPTANCE_DEFERRED_TO_ASSIGNED_GROUPS')
 elif n in ['publication.json','publication.first-receipt.json','environment-checks.json','validation.json','validation-incidents.json','checkpoint.json','progress.json','identities.json']:
  row.update(purpose='OPERATIVE_IDENTITY_STATE_VALIDATION_PUBLICATION',actual_scope='All operative statement values purpose-read via exact aliases and complete remaining/repair views; identity/count relations mechanically checked. Past subprocess/original platform reading timestamps and old remote claims are retained as historical evidence, not reexecuted or invented.',decision='RECEIVED_WITH_HISTORICAL_EXECUTION_PROVENANCE_LIMIT')
 else:
  row.update(purpose='OPERATIVE_CONTRACT_INTERFACE_QUALIFICATION_OR_PROPOSAL',actual_scope='All group06 business assertions, qualifiers, dependency notes,31reverse groups/150atoms,20interfaces,6provider/66facts,proposal/tombstone and copied contract provenance read through lossless exact-value factoring. Current B8/R necessary units independently compared.',decision='RECEIVED_WITH_EXPLICIT_QUALIFICATIONS')
 payload.append(row)
reading={'schema':'r8-cp06-reading-ledger/v1','utc':UTC,'identity':'identity.json','fixed_group_readset':ident(T/'continuation/06_qualifications_interfaces/readset.complete.json'),'full_contract_inputs':{'contract':ident(T/'continuation-contracts.json'),'group_prompt':ident(T/'continuation/06_qualifications_interfaces/prompt.zh.md'),'global_prompt':ident(ROOT/'inputs/eighth-global-review-prompt.md'),'AGENTS':ident(REPO/'AGENTS.md'),'review_SKILL':ident(ROOT/'inputs/review-SKILL.md')},'full_read_method':'Readset and contract JSON were parsed in full, all unique meaning-bearing strings actually read with explicit exact-value aliases. Structural numbers,IDs,hashes and pure locators kept as typed metadata, not automatically semantic PASS. Script literals/operative payload statements separately purpose-read; all filter/truncation repairs recorded. Required semantic decisions are explicit per ID.','readset_views':json.loads((O/'view-generation.json').read_text()),'evidence_id_bindings':names,'parent_readings':list(by.values()),'battler_units':'battler-reception.json complete31','provider_units':'provider-reception.json complete6/66','operative_payloads':payload,'incidents':incidents,'old_reading_log_limit':'Original author/previous receiver tool transcripts were not supplied in full. Author claims of actual reading/time/old execution remain provenance-qualified; this receiver uses its own literal readings and static checks.','first_persisted_literal_event_utc':events[0]['utc'],'earlier_actual_reads':'Contract/prompt/AGENTS/skill/readset and direct provider outputs occurred before read_unit logging; original platform tool outputs remain their actual evidence; no invented start/end metadata.','semantic_credit_from_hash_or_count':0,'reference_or_recovered_code_executed':False,'native_or_independent_behavior_vectors':0,'UPDATE_NOT_STARTED':True}
dump('reading-ledger.json',reading)
# Audit correction and bounded independent counterreview of the existing canonical candidate.
correction={'id':'CP06-Q001','kind':'RECEPTION_EVIDENCE_CORRECTION','global_required_finding':False,'old_statement':'存储先入队，满队可治疗再存盒，失败返回旧当前盒','old_locator':'readset.all_dependency_identity_candidates[24].semantic_notes / target reading-ledger.json Peer dependency','actual_source':'Battle_Peers.rb 5–24: storage negative result reaches an unqualified pbDisplayPaused before the old-box return. Default Peer has no such method; no Peer-specific override found in fixed R script search.','bounded_counterexample':'Default Battle::Peer, full player party, destination storage rejects insertion, ordinary no-plugin object. After any earlier normalization/heal/storage attempt, missing message method may fail before the return; do not promise the old box number.','formal_current':'WP38 §6, line114 already records this local failure.','decision':'Correct reception evidence only; no specification remediation supported. Prefix effects and outer exception handling remain separate.','source_evidence':['PEER','CATCH'],'execution':'SOURCE_STATIC; NOT_EXECUTED'}
proposal={'id':'GR8-EXTCP-002','original_full_proposal':A['original_proposal_full'],'this_independent_receiver':'identity.json','independent_scope':'Finite faint cry selection, pitch-adjusted wait and current formal ownership. No496-field transcription demand and no whole131 negative-coverage claim.','static_source_result':{'dedicated_cry':'Prefer _faint resource; default pitch, nominal ceil(1.0*20)+2=22 units for hypothetical1-second length.','ordinary_cry':'Fallback ordinary resource requested at pitch75; duration divides by0.75, ceil((1.0/0.75)*20)+2=29 units.','both_missing':'Base10 plus2=12 units, no species cry request.','downstream':'Faint track cry wait precedes lower/crop/hide; Scene updates databox exit alongside it and blocks until both finish. PictureEx nominal units are not host wall-clock guarantees.'},'strongest_counterargument':'WP67-A9.4 explicitly does not transcribe per-frame coordinates/trajectories/author format and forwards WP74. This can support excluding purely visual particle/coordinate fidelity. It does not expressly exclude named faint audio priority, pitch75 or pitch-adjusted ordering; WP74 is an author database/editor contract and cannot silently supply the fixed track. WP15 shared audio parsing and WP16 generic scheduling likewise do not assign this producer-specific choice.','independent_recommendation':'REQUIRED_PROPOSED_P3_FOR_FINITE_AUDIO_REQUEST_OMISSION_OR_EXPLICIT_SCOPE_DECISION','reason':'The written scope includes faint observable phases and timing; current high-level cry+fall permits a100-pitch/fixed-wait variant with different observable request/ordering under the same legal input. No explicit current exclusion was found in the fully read WP67-A or the complete relevant WP74/WP15/WP16/scope clauses. This is a bounded coverage issue, not a demonstrated contradictory numeric promise.','minimum_revision_if_adopted':'WP67-A9.3 or one explicit owner: dedicated/default-pitch, ordinary75 with pitch-adjusted length, both-missing branches; all plus2 nominal units, within actual first-processing scheduler semantics. Scope may deliberately exclude exact particle/coordinate tables separately.','normal_cancel_missing_exception_prefix':'No local input cancellation; Scene abort/normal end distinct. Missing cry is a normal branch. Other resource/host/callback exceptions need not roll back HP/faint state committed earlier; no universal ensure/pixel/audio success.','retain_correct':'All current concurrent databox/faint waiting, normal temp disposal, HP/EXP ordering, author player20fps and H001 withdrawal.','static_acceptance':['Independently compare all3cry branches and1.0-second hypothetical22/29/12 controls.','Check ordinary75 length division and requested sound identity/form, not merely supplied29.','Use complete selected producer/consumer and shared PictureEx units; no native media execution credit.','Root may resolve explicit product scope or canonical alias; this receiver does not mark ACCEPTED/CLOSED.'],'preexisting_ELR_counterreview':'The fixed contract contains a dispatch prompt, not an actual ELR returned reception. This is this group06 receiver independent analysis and does not impersonate that context.','final_adjudication':'PENDING_PARENT_ROOT; not a reading gap in this group','UPDATE_NOT_STARTED':True}
dump('findings-and-counterreview.json',{'schema':'r8-cp06-findings/v1','evidence_corrections':[correction],'existing_candidate_counterreview':proposal,'retracted_H001':'Independently confirmed foreground own-opacity snapshot;100→200 midpoint150, not110. NO_REVISION_SUPPORTED; original proposal/tombstone retained.','new_canonical_required_findings':0,'existing_required_candidates_recommended':1,'accepted_required':0,'UPDATE_NOT_STARTED':True})
# Historical limits and categories remain distinct. No past PASS inherited.
limits=json.loads((RAW/'limits.json').read_text());hist={
'schema':'r8-cp06-history-and-limits/v1','R6_limit_original':ident(REPO/'review/remediation-sixth-20261014-prepare/inputs/limit-records.json'),'R6_limits_full_read':True,'R6_limit_original_current_byte_relation':'Fixed original9aa72bc99a4cf52c8fb9cad8a637a963341388b0 toB8 diff for limit-records is empty; not a semantic PASS from identical bytes.','R6_limit_count':14,'target_limit_dispositions':limits,'current_successor':{'identity':ident(REPO/'delivery/2026-10-16-seventh/eighth-review-inputs.json'),'actual_read_range':[1640,1781],'operative_range':[1722,1781],'result':'L01–L14 retained OPEN; model/effort/tier/speed unverified, all new behavior vectors not executed, broader native/device/SF2/geometry and future compatibility remain open; nonmandatory adoption NONE.'},'target_applicable_optional_records':['R6-UI-PARTY-003','GR6-F-003','R6-D-FONT-C01','R6-D-PBS-C08','R6-C-P02'],'optional_receipt':'Complete exact selected records retained in historical-selected-exact.json and all337 unique semantic strings including slash-prose repairs actually read. These remain optional; source facts are not promoted to native pixel observations.','FLOAT_facet':'R6-DX-AN-007::FLOAT_RECURRENCE remains a separate optionalP3 facet; not a bit-exact/global floating endpoint guarantee.','policy_ids':['BAG-04','UTIL-03','UTIL-05','UTIL-11','UTIL-12','UTIL-13','GR6-POL-001'],'policy_receipt':'All7 existing records and general compatibility boundary preserved/read as historical policy; no policy selected and no broader Bag/utility/native review claimed.','no_required':['R6-UI-PARTY-004'],'no_required_receipt':'Retain original erroneous stale Entry premise AND independent counterevidence: Ruby loop-local command does not retain prior Entry0 in the cited path. Current classification no_required_revision governs; do not resurrect original full proposal as a proved failure. This receiver does not claim a new Ruby execution.','non_applicable_R6_optional':['R6-CM-FB-01','UI-ST-002','GR6-F-G001'],'non_applicable_scope':'Unknown effect binding, held storage cross-page preview and facility template corpus are not adopted as group06 propositions. Keep original categories; no rerun of complete R7/history.','real_unclosed_limits':['Actual platform UUID/model configuration authoritative echo absent.','Original author early read stdout/stderr/time not fully supplied; preserve L14.','Native graphics/audio/font/physical input/wall-clock/save/replay/whole-model behavior not executed.','Parent/root global final receptions and CP002 scope/classification remain pending.'],'readable_necessary_units_unread':0,'UPDATE_NOT_STARTED':True}
dump('history-and-limits.json',hist)
# Coverage-purpose groups already preserve every one of the217discoveredpaths without promoting them to primary.
coverage=json.loads((O/'coverage-purpose-groups.json').read_text());assert sum(len(x['members']) for x in coverage)==217
atomic=json.loads((RAW/'atomic-assertions.json').read_text());forward=json.loads((RAW/'forward-mapping.json').read_text())
assert atomic['atomic_assertion_denominator']==1045 and forward['structure_groups']==79
assert len(rev)==150 and len(irs)==20 and len(provider_rows)==66 and len(batrecords)==8 and len(unitmeta)==31 and len(payload)==31
reception={'schema':'r8-cp06-completed-bounded-reception/v1','utc':UTC,'status':'BOUNDED_WORK_COMPLETE_READY_FOR_PARENT_RECEPTION','identity':'identity.json','denominators':{'primary_objects':0,'primary_source_assertions_credited_here':0,'reverse_groups':31,'reverse_assertions':150,'selected_reverse_interfaces':20,'legacy_interface_edges_including_distinct_IF09':len(oldedges),'provider_units':6,'provider_assertions':66,'mandatory_Battler_corrected_facts':8,'mandatory_Battler_complete_necessary_units':31,'operative_target_payloads':31,'discovered_path_qualifications':217,'discovered_paths_scope_groups':len(coverage),'R6_limits':14},'completed_semantic_outputs':['reverse-reception.json','interfaces.json','provider-reception.json','battler-reception.json','history-and-limits.json','findings-and-counterreview.json'],'qualifications':{'EXTCP-IR005':'Internal cry-before-fall; faint track parallel to databox, not cry/fall mutually parallel.','EXTCP-R013.2':'EXP committed before bar, gain message can precede commit.','CP06-Q001':'Old Peer failed-storage return shorthand corrected; current WP38 already correct.','IF09':'Preserve interfaces/IF09 and continuation_interfaces/IF09 as different namespace identities.','RX-HANDLER_and_RX-ITEM-DISPATCH':'Only mandatory corrected facts adopted; raw add key/no registry subclass, Exp-1/EVregistration exceptions retained.','H001':'Withdrawal independently supported; no revived candidate.'},'findings':{'new_global_required_roots':0,'evidence_correction':1,'existing_CP002_counterreview':'Supported finite coverage candidate; recommend P3 required or explicit scope decision. Parent/root final disposition pending.','accepted_required':0,'remediation_started':False},'unread_in_this_assigned_semantic_scope':0,'remaining_blockers_to_global_completion':['Root CP002 final canonical/scope decision and any separately dispatched ELR actual result.','Other groups01–05 own1045primary acceptance; not counted here.','Existing native/media/runtime/configuration/old-log limitations retained, not reclassified as unread.'],'not_blocking_this_finite_delivery':['No missing readable necessary unit for the declared group06 propositions.','Parent/root can consume this completed finite receipt directly; no additional nested administrative reviewer requested.'],'claim_boundaries':['Not full current WP67-A primary acceptance, not whole217path domain acceptance.','No actual source/Ruby/reference/independent model/host/native/game vectors executed.','Hashes/counts/AST/JSON checks are mechanical evidence only.','No recovered script executed; no formal/source/main merge edits.'],'UPDATE_NOT_STARTED':True}
dump('reception-ledger.json',reception)
print(json.dumps({'written':['identity.json','reading-ledger.json','reception-ledger.json','reverse-reception.json','interfaces.json','provider-reception.json','battler-reception.json','findings-and-counterreview.json','history-and-limits.json'],'reverse':len(rev),'interfaces':len(irs),'provider':len(provider_rows),'battler':len(batrecords),'necessary_units':len(unitmeta),'payloads':len(payload)},ensure_ascii=False))
