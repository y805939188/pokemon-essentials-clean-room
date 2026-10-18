"""Build audit indexes from explicit readings; generation never grants acceptance."""
from pathlib import Path
import datetime
import hashlib
import json
import os

T = Path(__file__).resolve().parent
P = T / 'evidence/recovered-target'
CONTRACT = '40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'
C = '90b9e27ef03feb2c018bb2f258b5e0d5aaed012b'
B = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CONTEXT = os.environ.get('CODEX_THREAD_ID', 'UNVERIFIED')
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def read(path):
    return json.loads((P / path).read_text())

def write(path, obj):
    (T / path).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def ident(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(T)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

original = read('reading-ledger.json')
forward = read('forward-mapping.json')
reverse = read('reverse-mapping.json')
images = read('evidence/continuation/image-unit-inventory.json')
source_ranges = read('evidence/continuation/all-dependency-personal-ranges.json')
pbs = json.loads((T / 'evidence/pbs-current/elr-pbs-field-finite-input.json').read_text())
selected = {'TYPE_NAMES', 'TRAINER_TYPE_NAMES', 'ITEM_PORTION_NAMES',
            'ITEM_PORTION_NAME_PLURALS', 'RIBBON_NAMES', 'RIBBON_DESCRIPTIONS'}
partial = {'ITEM_DESCRIPTIONS': {253}, 'SCRIPT_TEXTS': set(range(2145, 2154)) | {1991, 2043, 2061, 2202}}
primary = []
data_read = []
for i, unit in enumerate(original['units']):
    domain = Path(unit['identity'][2:]).stem
    record = unit.get('record')
    actually_read = (record is not None and (domain in selected or record in partial.get(domain, set())))
    header_read = record is None and domain in selected
    primary.append({'id': unit['id'], 'source': unit['identity'], 'lines': unit['lines'],
                    'original_object': f'evidence/recovered-target/reading-ledger.json#/units/{i}',
                    'kind': 'record' if record is not None else 'header',
                    'literal_read_here': actually_read or header_read,
                    'full_chain_reception': 'OPEN',
                    'reason': '当前字段实读不转授生产/PBS/展示/历史全部接收；未显示的字段保持未读。'})
    if actually_read:
        raw = (T / 'evidence/primary-reference' / (domain + '.txt')).read_text(encoding='utf-8-sig').splitlines()
        data_read.append({'id': unit['id'], 'domain': domain, 'record': record,
                          'raw_key': raw[2 * record + 2], 'raw_value': raw[2 * record + 3],
                          'lines': unit['lines'], 'source_commit': R,
                          'evidence': 'dbee78 (six complete views); 6d685f (SCRIPT2145–2153); 9b02af (five unequal pairs)',
                          'disposition': 'COMPLETE_LITERAL_FIELDS_READ_CHAIN_PARTIAL',
                          'meaning': '独立文本键/译文值；仅键归一化，值不按键算法变换；此文字不证明玩法执行。'})
assert len(data_read) == 433
assert len([x for x in primary if x['kind'] == 'record']) == 10697

frozen = {
    'schema': 'gr8-elr-independent-frozen-denominator/v1', 'utc': NOW,
    'contract_commit': CONTRACT, 'target_commit': C,
    'target_checkout_tree': '3d2d7f5723f99ad92367bc9618df882802e300cf',
    'target_task_tree': '6c7b90ecf4c32914f053b3de2db489d05ad4063f',
    'B8': B, 'R': R,
    'qualification': '精确对象冻结是机械索引；任何未实际呈现的业务值均未因生成获得阅读信用。',
    'transport': {'files': 213, 'bytes': 18637972, 'complete_identities': 'evidence/target-recovery.json'},
    'primary_objects': primary,
    'fact_groups': [{'id': x['id'], 'domain': x['domain'], 'origin': f'evidence/recovered-target/forward-mapping.json#/fact_groups/{i}', 'status': 'PARTIAL_READ' if x['domain'] in selected else 'NOT_RECEIVED'} for i,x in enumerate(forward['fact_groups'])],
    'image_methods': [{**x, 'original_status_only': x['status'], 'our_status': 'COMPLETE_CALLER_METHOD_READ', 'our_credit_boundary': '实际全部方法体与结束行；不授整文件/完整UI或全媒体批准。'} for x in images],
    'seven_interfaces': [{'id': x['id'], 'origin': f'evidence/recovered-target/interfaces.json#/interfaces/{i}'} for i,x in enumerate(read('interfaces.json')['interfaces'])],
    'pbs35': pbs['all35_exact_owner_field_identities'],
    'pbs_value_bundle': {'identity': ident(T/'evidence/pbs-current/localization-field-contribution.v1.json'), 'status': 'NOT_FULLY_READ_NOT_RECEIVED', 'full_payload_available': True, 'six_plus_two_vs_27': '六个current原路径+两个既有完整有限贡献；其余27原owner不因口述或同blob获得接收。'},
    'author_dependency_ranges54': source_ranges,
    'reverse125': [{'id': x['id'], 'lines': x['lines'], 'subassertion_count': len(x['subassertions']), 'origin': f'evidence/recovered-target/reverse-mapping.json#/wp08_clause_records/{i}', 'status': 'SOURCE_LINKAGE_NOT_RECEIVED'} for i,x in enumerate(reverse['wp08_clause_records'])],
    'tests41': [{'id': f'LZ{i:02d}', 'status': 'FULL_FORMAL_VECTOR_READ_NOT_EXECUTED'} for i in range(1,42)],
    'separate_populations': {'primary_files':18,'primary_records':10697,'primary_headers':18,'primary_fields':21394,'image_methods':36,'image_calls':63,'pbs_paths':35,'interfaces':7,'author_dependencies':54,'author_dependency_whole':12,'author_dependency_partial':42,'reverse_clause_objects':125,'reverse_subassertions':398,'tests':41},
    'no_combined_pass_denominator': True
}
write('frozen-denominator.json', frozen)

whole_source_reads = {
 'R-003_Intl_Messages.rb': (823, ['1c6b03','d76e4e','cb095d']),
 'R-003_Minigame_SlotMachine.rb': (456, ['ce8f44','ec4d9f']),
 'R-008_AnimatedBitmap.rb': (228, ['4fe8f5']),
 'R-007_BitmapSprite.rb': (243, ['4fe8f5']),
 'R-001_RPG_Cache.rb': (144, ['4fe8f5']),
 'R-001_MKXP_Compatibility.rb': (48, ['a37808']),
 'R-003_Type.rb': (141, ['3e6f47']),
 'R-012_Ribbon.rb': (48, ['3e6f47']),
 'R-014_TrainerType.rb': (134, ['3e6f47']),
 'R-006_Item.rb': (270, ['78d9e0','977fe1']),
 'F-wp08-localization.md': (231, ['1b7924']),
 'F-wp15-resource-matching-and-audio.md': (224, ['9930fd','a37808']),
 'F-wp69-slot-machine.md': (110, ['4d333e']),
 'F-wp69-slot-reels.md': (49, ['4d333e'])}
whole = [{'identity': ident(T/'evidence/necessary-source'/name), 'actual_lines': [1,n], 'output_chunks': chunks, 'reading': 'WHOLE_ACTUALLY_READ', 'qualification': '全文读取不等于整个对应领域已接受；只用于本任务有限接合。'} for name,(n,chunks) in whole_source_reads.items()]
file_reads = {
 'review.md':'b1a078', 'continuation-review.md':'b1a078', 'proposals.json':'2881eb',
 'interfaces.json':'76bc59', 'evidence/continuation/peer-reception.json':'76bc59',
 'evidence/continuation/image-unit-inventory.json':'f6771e reversible full field view',
 'evidence/continuation/received/media-messages.json':'88453d',
 'evidence/continuation/received/media-encoding.json':'88453d',
 'evidence/continuation/received/media-data-getters.json':'24dd95',
 'evidence/continuation/limit-records.json':'977fe1',
 'evidence/contracts/localization_records.md':'a8be7b',
 'evidence/contracts/eighth-global-review-prompt.md':'eccd76 + 935786, exact same bytes as fixed contract copy',
 'evidence/contracts/AGENTS.md':'d631ee, exact same bytes as root AGENTS',
 'evidence/contracts/review-SKILL.md':'935786, exact same bytes as fixed contract copy',
 'evidence/continuation/received/resource_media_serialized_cloud--static-recovery-001--current-serialized--Main.rb':'2a2330, inert derived representation only',
 'evidence/continuation/own-source-views/bed7d014ac8ab7aa.txt':'2a2330, complete contained97–131 only; trailing wait partial',
 'evidence/continuation/own-source-views/f686ebc920605139.txt':'24dd95',
 'evidence/continuation/own-source-views/3c82753dd6b41458.txt':'24dd95',
}
for domain in selected:
    file_reads[f'evidence/reads/{domain}-1-100000.txt'] = 'dbee78'
for x in images:
    num=int(x['id'].split('-')[-1])
    file_reads[x['view']] = ('d793d5' if num==1 else 'ce8f44 + ec4d9f exact full source alias' if num<=5 else 'c5c420' if num<=17 else '672031' if num<=26 else '4a90fc')
manifest = json.loads((T/'evidence/target-recovery.json').read_text())
files=[]
for row in manifest['files']:
    name=row['relative_to_target_task']
    if name in file_reads:
        state='READ_WITH_EXPLICIT_SCOPE'
    elif any(f'/own-source-views/{key}' in name for key in ['26ca8927492122a7','18ff84e29a4e1bae','aff3277720abd61c','d6cde40c60a038cf','2edec0fcdf163685','d6cde40c60a038cf']):
        state='IDENTICAL_SOURCE_ALIAS_ONLY'
    else:
        state='RECOVERED_NOT_FULLY_READ_PURPOSE_AND_SEMANTICS_OPEN'
    files.append({'path':name,'bytes':row['bytes'],'sha256':row['sha256'],'mode':row['mode'],'git_blob':row['git_blob'],'identity_exact':True,'reading':state,'evidence':file_reads.get(name),'reception': 'NO_WHOLE_FILE_ACCEPTANCE_FROM_TRANSPORT'})
reading = {
 'schema':'gr8-elr-independent-reading-ledger/v1','utc':NOW,'reviewer_context':CONTEXT,
 'original_author_context':'01a143ad-a413-739d-b640-d4896e2e5029',
 'independence': {'different': CONTEXT not in ['UNVERIFIED','01a143ad-a413-739d-b640-d4896e2e5029'],'evidence':'11613e exact CODEX_THREAD_ID/CODEX_SESSION_ID allowlist output','self_spawn':0,'new_contexts_created_by_this_task':0,'global_context_count_delta':'UNVERIFIED_PARENT_REGISTRY_ONLY'},
 'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default normal','speed':'normal','Fast':'off'},
 'actual':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','agent_id']},
 'actual_context':CONTEXT,'contract_full_read':{'prompt':'c23233','readset':'55f18a + 003862 + 48a959 lossless factoring, all213 rows/all fields','global':'eccd76 + 935786','skill':'935786','AGENTS':'d631ee','recovery_helper':'8375fa'},
 'full_source_or_formal_reads':whole,'target_file_states':files,'literal_record_reads':data_read,
 'caller_methods36':[{ 'id':x['id'],'source':x['path'],'range':x['range'],'presentation':'evidence/recovered-target/'+x['view'],'proof':file_reads[x['view']],'status':'COMPLETE_METHOD_ACTUALLY_READ','whole_file_credit':False} for x in images],
 'complete_counter_packet':{'source':'evidence/root-packets/coverage/root-active-snapshot-19/counter_slot_localization_existing_kernel/counterreview.json','actual_full_sections':['1','2','3','4','5','6','7','8'],'proof':['64c6cc','e7f271','fd62c0'],'mandatory_clarifier':'ca063a','all_root_bounded_adjudication_packets':'78c643'},
 'extra_clarifiers':{'glob':'evidence/pbs-current/root-active-snapshot-*/pbs_creature_current_cloud/mandatory-*.json','proof':'dfb53e','count':7,'acceptance':'完整阅读更正文字，原提供者阅读资格不改写成本人源全文。'},
 'counts':{'literal_primary_records_read':433,'literal_primary_records_unread':10264,'literal_fields_read':866,'literal_fields_unread':20528,'primary_files_literal_full':6,'primary_files_literal_partial':2,'primary_files_literal_unread':10,'headers_read':6,'headers_not_read':12,'complete_primary_chains_accepted':0,'complete_callers':36,'located_calls_bound_to_complete_callers':63,'reverse_mapping_objects_not_received':125},
 'failures_and_truncations':[
  {'proof':'504e15/c7b353/25c659/a64728','kind':'contract object initially absent; ordinary exact fetch repaired; no semantic credit for failed reads'},
  {'proof':'e97a83','kind':'raw213-file readset output truncated; replaced by full reversible105/78/79-line views; original JSON preserved'},
  {'proof':'c9b8e0','kind':'wrong section-key assumption printed wholecounter/truncated; full sections and IO ledger re-read at64c6cc/e7f271/fd62c0'},
  {'proof':'9930fd','kind':'combined output truncated WP15 front; wholemissingfront1–90 re-read a37808, tail visible in original9930fd'},
  {'proof':'4466a5','kind':'PBS60874+530487B output truncated; NOT_READ/NOT_RECEIVED retained for complete value packet; never treated as material limit'},
  {'proof':'0952d3','kind':'metadata iteration KeyError view on last row; no claim last row received'},
  {'proof':'115199','kind':'FileTests ranges include partialneighbor canonicalize/pbGetFileString; no whole-method credit to these partial tails'}],
 'original_IO_boundary':'Tool chunk IDs identify actual public output in this execution. Source bytes/views retained separately; exact per-readUTC/stdout-stderr private event export is UNVERIFIED and not reconstructed.',
 'business_execution':{'reference':0,'model':0,'game_host':0,'media':0,'save_reload':0,'status':'NOT_EXECUTED'},
 'UPDATE_NOT_STARTED':True}
write('reading-ledger.json',reading)

zh = [
 '翻牌只翻译bg/memo基名，再加固定目录；tiles/cursor不变，前序部件可已建立。',
 '每个转轮独立查符号图完整身份；先创建/抽初始索引，后取图；图高随后参与边界时间。',
 '按获奖/重玩/未中分支循环查win/bonus/lose，bonus有独立门；音效与内部支付显示可能在图失败前已发生。',
 '场景按序创建背景和三轮后才查insert；失败无整体回滚保证。',
 '运行查stop，等待查insert，已下注查press；未下注BACK仍走正常币额/净统计尾提交。',
 '卡背noback只控制固定背面；type非空才查类型图，然后严格类型查询；出错不保证清理。',
 'owner0直接卡背；其余选固定玩家/敌方背面，类型图独立翻译，物种图与数字图独立。',
 'Safari先查databox身份，再用返回位图尺寸创建内容；不能推真实载入成功。',
 '单人/多人各先查玩家和敌方两个身份再按奇偶取值；旧包装先释放，坐标与标志按原分支。',
 '等级图身份翻译和数值等级绘制分开。',
 'NONE提前返回；猛毒取最后状态行，其余用严格状态图标位；负位不画。',
 '图形命令模式翻译按钮光标，背景固定；文本模式另建命令窗口。',
 '图形招式模式依序查fight/type/Mega/shift，位图尺寸用于按钮布局；文本模式独立。',
 '命名先建页签/对象/背景和多分支，再查controls；对象分支不令全部命名资源可翻译。',
 '命名模式图翻译后传绘图列表，裁片由模式乘60决定；目的位置另算。',
 '重学先逐候选取名再创建场景/类型图，随后首绘；空列表不自动成为安全取消。',
 '重学可见项分别取名/类型/PP；选中项严格读取发生在前序绘图资料后，描述最后消费。',
 '背包重要物品已登记/可登记分支查register不同图行；有登记图时抑制数量，关闭项不走物品。',
 '仓储手持对象优先，无对象提前返回；非蛋才有等级/能力/物品/类型图，名字独立。',
 'Summary保留队伍引用，先查类型图再首绘；marking、背景和箭头固定。',
 '遗忘场景先查类型图，选中第一招后首绘；无招式不保证到输入阶段。',
 'Summary蛋提前改画；濒死/状态/病毒决定statuses图行；持有物名称独立查。',
 '招式页只为存在招式请求翻译类型图，display_type与PP档/缺招占位独立。',
 '招式选择页四项或四加新项各查类型图，固定详情背景不变，个体类型图另用已建图。',
 '训练家卡先解析翻译女性卡存在性，再受女性门选择；普通卡亦翻译，背景另查固定身份。',
 '点唱机先查背景完整身份，再建标题与命令窗口；不证明音频播放。',
 '图鉴菜单查bg_menu，SEEN/OBTAINED标签和命令内容分别处理。',
 '队伍面板形状固定；三种HP背景经Changeling消费译名，statuses独立；球和HP条固定。',
 '队伍蛋抑制等级图；图身份与数字等级分开。',
 '完整图鉴首场景先类型图，城镇地图/区域额外资料按独立门；后续首绘需前序正常。',
 '简短图鉴独立构造全国/区域编号，再建类型图与第一页；不从类型图反推登记。',
 '图鉴info背景总查，brief才overlay；已拥有门控制分类/正文/脚印/类型，未拥有占位，US单位独立。',
 '区域页翻译bg_area；遭遇格/地图高亮来自独立数据，区域和物种文本在末部消费。',
 '形态页翻译bg_forms，形态标签取已存在性别/形态元组，物种名独立。',
 '图鉴主场景只查types/hw/searchslider三图，其他滑条/形状/背景固定；先准备后刷新。',
 '控制帮助七图各查完整身份，标签与固定背景分开；addImage存picture.name，屏号控制显示；PictureSprite后继未读。']
assert len(zh)==36
received_images=[{'id':x['id'],'current_complete_meaning':meaning,'R':{'commit':R,'path':x['path'],'range':x['range'],'sha256':x['sha256'],'blob':x['blob']},'presentation':'evidence/recovered-target/'+x['view'],'consumer_join':'Translation/_INTL→当前方法→AnimatedBitmap/IconSprite/Changeling/绘图列表/事件图片，按该方法实际分支；具名后继不足不签全接口。','disposition':'FINITE_CALLER_CONTRIBUTION_RECEIVED','unresolved':'完整I05 UI贡献、控制帮助PictureSprite后继及非本任务全域合同未接受。' if i==35 else '相应UI整域/正式跨篇累计与真实媒体执行未接受。'} for i,(x,meaning) in enumerate(zip(images,zh))]
reception={
 'schema':'gr8-elr-independent-reception-ledger/v1','utc':NOW,'status':'INCOMPLETE','receiver_context':CONTEXT,
 'literal_primary_fields':data_read,'image_callers':received_images,
 'complete_finite_packets':[
  {'id':'GR8-ELR-001','meaning':'七角色在原状态门先查当前game→core→原身份，再交现有入口；四组指定集合缺Slot。完整最强no-required解释不克服明确指定调用者边界。','decision':'SUPPORT_EXISTING_ROOT_REQUIRED_P3_BOUNDED','evidence':'proposal-counters.json','unresolved':'完整历史canonical/alias及必要跨域最终接收OPEN；不新增必修根或独立票。'},
  {'id':'ELR-I04-ENC01–04','meaning':'31桶、18非空hash；21216字符串E=true且UTF8合法，178字符串键链接；Scripts594B有561B非UTF8压缩串，E标注不授编码合法或运行；解码Main49只静态。','evidence':'media-messages/media-encoding完整包88453d，原读者保持media，root有限接收78c643。','disposition':'FINITE_CONTAINER_AND_ENCODING_CONTRIBUTION_RECEIVED','unresolved':'未逐值接收剩余10264文本及178链接全目标内容；不签全I04/全语料。'},
  {'id':'L01–L14-current-copy','meaning':'完整现行14条limit的范围、恢复条件、失败元数据与历史资格已读；这不是取得原R5/R6/R7原合同。','evidence':'977fe1','disposition':'QUALIFICATION_PACKET_RECEIVED','unresolved':'历史原限载荷/56/37及optional/Float/policy/no-required原记录仍未接受。'},
  {'id':'PBS-mandatory-clarifiers','meaning':'Pokemon真实EOF1227；form方法448–485；trap类末345及UsageEOF515；FieldUse/BattleUse为枚举；Player123/Start126；消耗谓词consumed_after_use?；取得失败可有Bag前缀；57边/52父项/35方法。','evidence':'dfb53e七份完整更正包','disposition':'CORRECTION_TEXT_RECEIVED_ONLY','unresolved':'不扩大为未读PBS字段值、战斗方法或Bag实现全文批准。'}],
 'complete_primary_chain_count':0,'full_task_final_ready':False,
 'remaining_exact_objects':{'primary_records':'frozen-denominator.json#/primary_objects where kind=record and literal_read_here=false (10264)','primary_headers':'same index where kind=header and literal_read_here=false (12)','pbs35':'frozen-denominator.json#/pbs35, every necessary_localization_field_scope remains full-value NOT_RECEIVED','pbs530487':'evidence/pbs-current/localization-field-contribution.v1.json (NOT_FULLY_READ)','interfaces':'interfaces.json (all7 not final accepted)','reverse_objects':'frozen-denominator.json#/reverse125 (125 source-linkage objects)','target_files':'reading-ledger.json#/target_file_states, every RECOVERED_NOT_FULLY_READ row remains OPEN; no typed-purpose exemption yet'},
 'capacity_boundary':'本次单接收上下文尚未完成全部可得业务值。剩余材料远超本次可继续呈现并逐对象判断的容量；这是交付容量与实际缺读，不是文件缺失、权限、宿主或原始材料限制。保持INCOMPLETE并给同一非作者context可续接的精确对象索引。',
 'UPDATE_NOT_STARTED':True}
write('reception-ledger.json',reception)

statuses=[
 ('ELR-I01','PARTIAL','完整Intl823/WP08全文及LZ41向量已读；game/core/空命中/键值分离成立。','KER-F102–112原完整贡献和Compiler.pbEachSection完整依赖未接，不签125反向source-linkage。'),
 ('ELR-I02','NOT_RECEIVED','作者ELR-C02完整声称已读，属于待验事实。','15生产者+额外TrainerType及3共同合同原完整贡献未实读，不能据概要关闭。'),
 ('ELR-I03','PARTIAL','六域419记录及四个完整数据定义、六事实组已读；份量nil回名称，空串不等于nil。','35PBS逐字段值、530487B包与Gen备选上下文未全接；不签任何完整PBS正文。'),
 ('ELR-I04','PARTIAL','完整媒体container/encoding有限包及五个差异字段、惰性Main已读。','剩余10264语料值与178链接全内容/相关必要消费者尚未全接；messages_game缺席是固定R事实，原生未执行另列。'),
 ('ELR-I05','PARTIAL','63调用对应36完整方法读完，原始R范围逐一核对；包装/绘图/部分事件桥已读。','UI36、Dex7与四图像家族原完整贡献未接；PictureSprite后继未读；不冒全部UI接收。'),
 ('ELR-I06','NOT_RECEIVED','作者ELR-C06的地图名/保存/物品先后声称及PBS后继前缀更正文字已读。','原SaveData/Value/SaveValues/StartGame、地图名可变值、物品取得及UI提示原完整贡献未接；后继更正须与原源一起采用。'),
 ('ELR-I07','PARTIAL','当前L01–L14及root有限ELR001历史保留全文已读。','原历史资格报告、R6有效56/R7原37、optional/Float/policy/no-required及canonical/alias去重未全接；不重开27。')]
write('interfaces.json',{'schema':'gr8-elr-independent-interface-reception/v1','utc':NOW,'target_commit':C,'interfaces':[{'id':i,'status':s,'actually_received':a,'necessary_unreceived':u,'full_final_acceptance':False} for i,s,a,u in statuses],'complete':0,'partial':5,'not_received':2,'not_a_host_limit':True,'root_task_final_exclusive':True,'UPDATE_NOT_STARTED':True})
write('proposal-counters.json',{
 'schema':'gr8-elr-independent-proposal-counter-reception/v1','utc':NOW,'id':'GR8-ELR-001','proposer_context':'01a143ad-a413-739d-b640-d4896e2e5029','existing_counter_context':'/root/kernel_atomic_reception','receiver_context':CONTEXT,'actual_receiver_differs_from_author':CONTEXT!='01a143ad-a413-739d-b640-d4896e2e5029','complete_current_proposal':ident(P/'proposals.json'),'counter_source':'evidence/root-packets/coverage/root-active-snapshot-19/counter_slot_localization_existing_kernel/counterreview.json','mandatory_clarifier':'evidence/root-packets/coverage/root-active-snapshot-20/counter_slot_localization_existing_kernel/reel-table-extent-clarifier.v1.json','all8_sections_and_IO_ledger_received':True,
 'ordinary':'有效当前语言两层无A时交A；core有C/game无A时交C；gameB与coreC共存交B。',
 'minimal_counterexample':'合法当前game域24的A→同布局非空B，core无A，A仍可用，默认定义及正常有币盒/正币/非满入口；每转轮实际交B。仅按四组指定集合固定SlotA会丢失该条件行为。',
 'strongest_no_required':'任意字符串通用查找可复用，若四组只是例示或更高当前合同已覆盖Slot，补项可仅为导航/alias/no-required。',
 'resolution':'完整WP08明确只覆盖指定调用者，WP15重复四组，WP69主文及49L附表无Slot语言接点；查找算法不能自行确定实际调用者。支持已有root有限requiredP3，保留更高合同/完整历史反证权。',
 'seven_roles':['转轮符号','中奖','大奖','未中','投入','停止','按键提示'],
 'failure_cancel_partial':'无盒/零币/满币拒于初始化前；BACK门与财务尾提交保留。非空普通包装只捕获cache加载，后续仍可失败；前缀条带独立校验。Icon空串先清图，转轮直接空串在Gif前失败；不回试A。初始化随机/场景及支付显示前缀不保证回滚，正常先币额后统计。',
 'minimal_final_rule':'WP08补七自然角色与game→core→原身份；WP69说明状态门依赖；WP15同步有限导航。测试保留LZ39–41并加有限Slot对照即可，不强制新ID。',
 'preserve':'22位置有序转轮、H时间/滑移/随机/有效线/奖励/重玩/净币统计、原四组及固定资源、各种空译/失败分层、不新增语言选择或存档写入。',
 'root_existing_decision':'CLASSIFIED_BOUNDED_SCOPE_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION required/P3',
 'receiver_decision':'SUPPORT_EXISTING_BOUNDED_DECISION; not root task-final acceptance',
 'history':'OPEN: canonical/alias/扩展由主审完整历史接收后裁决；标题未命中无负证资格。',
 'counts':{'target_proposals':1,'existing_bounded_required_supported':1,'new_required_roots':0,'new_optional':0,'new_policy':0,'new_no_required':0,'new_votes':0,'self_spawn_contexts':0},
 'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})
print(json.dumps({'status':'INCOMPLETE','literal_records_read':len(data_read),'literal_records_unread':10697-len(data_read),'complete_caller_methods':len(images),'full_primary_chains_accepted':0,'target_files_recovered':len(files)},ensure_ascii=False))
