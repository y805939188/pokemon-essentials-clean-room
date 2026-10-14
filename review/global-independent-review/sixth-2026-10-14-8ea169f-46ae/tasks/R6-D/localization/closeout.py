"""Final current-state validation and sanitized audit report. Never executes reference code."""
import audit,json,subprocess
from collections import Counter
OUT=audit.OUT
inventory=json.loads((OUT/'inventory.json').read_text())
assert len(inventory)==18
assert sum(x['records'] for x in inventory)==10697
assert all(x['semantic_read']==x['records'] and x['semantic_unread']==0 for x in inventory)
forward=json.loads((OUT/'source-to-formal.json').read_text());reverse=json.loads((OUT/'formal-to-source.json').read_text());findings=json.loads((OUT/'findings.json').read_text())
assert len(forward)==10697 and len({x['unit'] for x in forward})==10697
assert all(x['semantic_status']=='read_this_round' for x in forward)
assert all(x['status']=='PROPOSAL_NOT_ADJUDICATED' for x in findings)
L='Data/Scripts/001_Technical/003_Intl_Messages.rb'
additional=[
 {'formal':{'path':'deliverables/final-specification-set/user-interface/wp65-controls-help-appendix.md','lines':[21,28],'clause':'3 page content'},'source':[{'path':'Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb','lines':[13,35]},{'path':L,'lines':[600,610]}],'prerequisites':'Screen reached; key diagram selected-language identity lookup precedes image creation; backdrop fixed.','disposition':'STATIC_CONSUMER_READ; PROPOSAL_GAP_R6-D-LZ-002'},
 {'formal':{'path':'deliverables/final-specification-set/user-interface/wp65-controls-help-appendix.md','lines':[50,50],'clause':'6 dependencies'},'source':[{'path':'Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb','lines':[19,52]}],'prerequisites':'Both explanation labels and designated key diagrams call the language service; image resolution stays resource responsibility.','disposition':'STATIC_CONSUMER_READ; PROPOSAL_GAP_R6-D-LZ-002'},
 {'formal':{'path':'deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md','lines':[29,56],'clause':'3.1–3.2 controls used by supplied corpus'},'source':[{'path':'Data/Scripts/007_Objects and windows/011_Messages.rb','lines':[419,505]},{'path':'Data/Scripts/007_Objects and windows/011_Messages.rb','lines':[584,629]}],'prerequisites':'Translated script return string handed to normal message consumer, relevant player/window dependencies valid; lookup-stage escapes and numbered placeholders are distinct from these controls.','disposition':'STATIC_RULE_MATCH; NOT_EXECUTED_THIS_ROUND'},
 {'formal':{'path':'deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md','lines':[59,82],'clause':'3–4 draw tags used by supplied corpus'},'source':[{'path':'Data/Scripts/007_Objects and windows/010_DrawText.rb','lines':[75,101]},{'path':'Data/Scripts/007_Objects and windows/010_DrawText.rb','lines':[345,393]},{'path':'Data/Scripts/007_Objects and windows/010_DrawText.rb','lines':[498,548]}],'prerequisites':'Recognized tag and rendering loop reach its position; typed bracket escape markers and ordinary angle-bracket prose are not all controls. Pixel layout/resource existence outside local claim.','disposition':'STATIC_RULE_MATCH; NOT_EXECUTED_THIS_ROUND'}]
old={(x['formal']['path'],tuple(x['formal']['lines']),x['formal'].get('clause')) for x in reverse}
for x in additional:
 k=(x['formal']['path'],tuple(x['formal']['lines']),x['formal'].get('clause'))
 if k not in old:reverse.append(x)
audit.write('formal-to-source.json',reverse)
# Current source bytes compared to the pinned objects; reading coverage remains a separate ledger.
paths={'AGENTS.md'}
for x in inventory:paths.add('reference/pokemon-essentials/'+x['path'])
paths.update(['reference/pokemon-essentials/Data/messages_core.dat','reference/pokemon-essentials/Data/Scripts.rxdata'])
for logfile in [OUT/'reading-ledger.jsonl',OUT/'pokedex/reading-ledger.jsonl']:
 for line in logfile.read_text().splitlines():
  x=json.loads(line);p=x.get('path','')
  if p.startswith(('Data/','Text_english_core/')):p='reference/pokemon-essentials/'+p
  if p.startswith(('reference/pokemon-essentials/','deliverables/final-specification-set/')):paths.add(p)
identity=[]
for p in sorted(paths):
 if p.startswith('reference/pokemon-essentials/'):
  repo=audit.REF;revision='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';relative=p[len('reference/pokemon-essentials/'):]
 else:repo=audit.ROOT;revision='8ea169fbd0f33f378b5d732fd6bea59e854e04a6';relative=p
 r=subprocess.run(['git','show',revision+':'+relative],cwd=repo,capture_output=True)
 assert r.returncode==0,(p,r.stderr)
 current=(audit.ROOT/p).read_bytes();same=current==r.stdout
 identity.append({'path':p,'revision':revision,'sha256':audit.sha(current),'pinned_equal':same})
assert all(x['pinned_equal'] for x in identity)
audit.write('pinned-content-validation.json',identity)
issues=[];cache={}
def walk(x):
 if isinstance(x,dict):
  if 'path' in x and 'lines' in x:
   p=audit.ROOT/x['path']
   if not p.exists():p=audit.REF/x['path']
   if not p.exists():issues.append(['missing_path',x['path']])
   else:
    if p not in cache:cache[p]=len(p.read_text(encoding='utf-8-sig').splitlines())
    a,b=x['lines']
    if not isinstance(a,int) or not isinstance(b,int) or not 1<=a<=b<=cache[p]:issues.append(['bad_line',x])
  for y in x.values():walk(y)
 elif isinstance(x,list):
  for y in x:walk(y)
for name in ['source-to-formal.json','formal-to-source.json','facts.json','findings.json','localized-image-matrix.json']:
 walk(json.loads((OUT/name).read_text()))
json_files=list(OUT.glob('*.json'))
for p in json_files:json.loads(p.read_text())
assert not issues,issues
# Header prose is exactly the same in all 18 domains, with each domain heading explicitly inventoried.
headers=json.loads((OUT/'headers.json').read_text());assert len({x['first_three_lines_sha256'] for x in headers})==1
buckets=json.loads((OUT/'event-buckets.json').read_text());bc=Counter(x['type'] for x in buckets)
status=json.loads((OUT/'task-status.json').read_text());status['coverage']['formal_reverse_rows']=len(reverse);status['coverage']['pinned_files_compared']=len(identity);status['coverage']['pinned_content_mismatches']=0;status['coverage']['remaining_source_consumer_debt_in_owned_scope']=0;status['coverage']['header_prose_identity_deduplicated_files']=18;status['status']='COMPLETE';status['reason']='All owned auditable units read this round, all 10697 semantic bodies closed, necessary local consumers/configuration and related formal clauses reviewed; proposals retained for parent adjudication.'
status['scope_exclusions']=['Game/shader/compatibility/Ruby-wide execution analysis','Pixel appearance, actual media existence and engine/demo runtime','Gameplay truth inferred solely from help or Pokédex prose','WP11 detailed map-name alias state scenarios beyond the locally read localization boundary']
status['finding_proposals']=len(findings);audit.write('task-status.json',status)
validation={'result':'PASS','scope':'Artifact identities, exact source/spec line locations, pinned bytes and coverage arithmetic only; not a runtime behavior test','json_files_parsed':len(json_files),'record_identities':10697,'semantic_read':10697,'semantic_unread':0,'pinned_files_equal':len(identity),'related_vector_rows':35,'formal_reverse_rows':len(reverse),'issues':issues,'adjudication':'NOT_PERFORMED','initial_check_correction':'One malformed formal-line endpoint in initial draft found by artifact validator, corrected and final check rerun.'}
audit.write('artifact-validation.json',validation)
md=['# R6-D 本地化独立复核：范围读取完成','',
'固定 main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`、main tree `6ab3429170d2762607fbc2237014c3a160449fa1`、formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`（131文件）；参考 HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。AGENTS.md 先全文读取。仅写本目录，无参考/formal修改、分支切换、提交、安装或外部服务。',
'',f'18份文本的 **10697条唯一键/正文全部本轮语义读取，可审未读0**。身份相同的译文副本去重显示；5对键正文不相同均显式读取。14个名称/类别等域先读全，随后连续逐批读完 SCRIPT_TEXTS 3305、ITEM_DESCRIPTIONS 665、MOVE_DESCRIPTIONS 725；POKEDEX_ENTRIES 1028由本任务并行子代理本轮逐批读取。合并前独立核对它的每条键/值/文件SHA、行号及0–1027连续人工接受范围；详情在 `pokedex/`。结构成功从未计为语义完成，初期欠读检查点由后续真实读取闭合。',
'', '每条身份、源行、SHA、键/正文分别的placeholder/转义/控制候选、消费者、采集接线、规则与formal行/clause，见 `records-*.json`、`source-to-formal.json`、`feature-matrix.json`。编号是审计偏移，不是物种/招式/物品ID。逐批显示和人工接受分列于 `reading-ledger.jsonl`，命令另见 `command-log.jsonl`；子代理保留自己的账本。18份相同三行头部说明按身份去重，域头分别核对。',
'', '默认消息采用独立primitive白名单解码，文件字节全部消费；无Marshal.load、对象钩子、Ruby/游戏代码执行。18域10697条文本与二进制键/值逐条一致，缺失、不同及二进制额外键为0。31域外层、空域及事件域76桶全部检查：'+str(bc.get('dict',0))+'个实际桶均为空哈希，'+str(bc.get('NoneType',0))+'个位置缺席，无未读事件正文。此事实不替代默认game、地图或Demo可达性。5对非身份值只在空格/换行处不同，保持“键规范化不改译文值”的边界。',
'', '脚本归档安全解析为恰一条Main记录，压缩字符串解压后49行全部读取；没有本地化输入标记，因此该记录不贡献可采集文本，而恰一节的外部Data/Scripts采集数量门成立。解压没有被当作执行。旧解析工具只在全文理解后独立适配，旧审查结果和旧隔离回执均未当本轮通过。',
'', '本地化服务823行连续全文读取；必要配置、启动、语言选择、选项直写存档、作者提取/编译菜单、分节、目录枚举、数据获取、采集setter调用者及消息/绘制标记消费者均按实际范围读取。WP08正文214行及LZ01–35全部重读，reverse矩阵'+str(len(reverse))+'行给出精确源位置与前提；WP17及WP65/资源局部交界亦具名。地图名局部消费者已读，WP11更深别名状态情景保持其他任务范围，不伪称在此重审。',
'', 'SCRIPT_TEXTS还包含48个语言可选图像身份（46完整逻辑名、2个basename），63个实际加载/绘制调用点已读并见 `localized-image-matrix.json`。因此不能把每条SCRIPT_TEXTS都理解成可见散文。消息色板/等待/音乐/金钱控制、格式占位、绘制对齐/换行/icon、作者文本编码处于不同阶段；词法候选并不自动等于有效控制。普通角括号描述也有实际非标记消费者。',
'', '**两项均仅为待终裁提案，未自行终裁：** R6-D-LZ-001记录已存在的采集解码次序在实际消费者上的键错配：三条固定条目的采集键换行处为U+005C+U+000A，普通运行输入对应为U+005C+U+006E；只在采集键提供译文时可能普通回原文，随后窗口才处理换行。最小例采用不含额外拼接的物品成功提示。R6-D-LZ-002提议补足“指定UI图像也可由当前语言选择”的能力及对照向量。每项在 `findings.json` 保留源/spec定位、前提、普通对照、最小反例、取消/异常/部分提交、负搜索、必要消费者、级别提议、最小修订、保留范围、同步文件、验收与依赖。',
'', '名称、物品帮助和图鉴叙述作为显示/查找材料审查；其中攻击、进化、概率或绝对能力描述不能单独充当玩法充分证据。没有运行宿主/Demo、多语言切换、完整作者往返或像素渲染；现有未知和兼容政策保留。',
'',f'最终审计材料校验通过：{len(identity)}个已读相关文件与固定Git对象逐字节相同；所有定位、记录身份、35条相关向量及覆盖算术有效，见 `artifact-validation.json`、`pinned-content-validation.json`。这是材料校验，不是行为测试通过。实际model、effort、tier、speed、运行UUID均无回显，维持UNVERIFIED。']
(OUT/'report.md').write_text('\n'.join(md)+'\n')
table=['# 本地化语义读取矩阵','','| 域 | 条目 | 结构已读 | 语义已读 | 未读 |','|---|---:|---:|---:|---:|']
for x in inventory:table.append('| '+x['path'].split('/')[-1][:-4]+f" | {x['records']} | {x['records']} | {x['semantic_read']} | 0 |")
table.extend(['','总计10697，未读0。每条消费者、采集接线和精确formal定位在JSON矩阵；图像身份交界另见localized-image-matrix.json。两项提案等待父任务终裁。'])
(OUT/'coverage-matrix.md').write_text('\n'.join(table)+'\n')
audit.event('final_scope_closeout',status='COMPLETE',semantic_read=10697,semantic_unread=0,proposals=len(findings),pinned_files_equal=len(identity),artifact_validation='PASS',adjudication='NOT_PERFORMED')
print(json.dumps(validation,ensure_ascii=False,indent=2))
