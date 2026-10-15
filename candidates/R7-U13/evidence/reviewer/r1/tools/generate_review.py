"""Materialize this reviewer's independently determined documentary conclusions."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil

OUT=Path(__file__).resolve().parents[1]
TOOLS=OUT/'tools'
BOOT=Path('/workspace/r7-review-bootstrap/R7-U13-r1')
ORIGBOOT=Path('/workspace/r7-bootstrap/R7-U13-reviewer')
ORIG=Path('/workspace/r7-context/R7-U13-reviewer')
CAND=Path('/workspace/r7-review-input/R7-U13-r1-5635c73ea14adc278961da0e3917c2d00d580a25')
AUTHOR=CAND/'candidate/candidates/R7-U13/evidence/author'
B='e646432c644dec04d306842cc5a559a29c718fbc'
COMMIT='5635c73ea14adc278961da0e3917c2d00d580a25'
TREE='e2c261a77a7268a5eb07e7e364ac257d9fed3e31'
FREEZE='aa369555b0e8b6c8b077f964b54ed63d3b924f26'
DISPATCH='95c260d8f3fb4a171675dde877137fcd4c2f1c8d'

def load(path): return json.loads(path.read_bytes())
def save(path,value): path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def ident(data): return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

audit=load(TOOLS/'byte-audit.json')
author_audit=load(TOOLS/'author-evidence-audit.json')
thread=os.environ['CODEX_THREAD_ID']
assert thread=='01a13ff1-4e91-74b4-ac83-5838dbb59018'
context=dict(schema='r7-u13-reviewer-actual-context.v1',observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    role='R7-U13 independent candidate reviewer r1',actual_thread_id=thread,
    parent_source_thread_id='01a13f49-a154-7054-9b04-ce31f924d01c',
    actual_platform_task_id=os.environ.get('CODEX_TASK_ID','NOT_EXPOSED'),
    actual_separate_context_id=os.environ.get('CODEX_CONTEXT_ID','NOT_EXPOSED'),
    environment_id='ccarenv_b64_Y2NhcmVudl9kNmJhZDBkM2I0YzA4MTkxOTdhMWUzZjAxYTgxYmIxMw',
    public_evidence_process_pid=os.getpid(),public_evidence_parent_pid=os.getppid(),
    pid_qualification='Actual public evidence-generation process only; model process PID not exposed. No separate model CLI started.',
    author_actual_thread='01a13f80-5248-7789-ab67-26ce7270c019',
    author_environment_id='ccarenv_b64_Y2NhcmVudl9lNmFhYjBjMTlmYjA4MTkxYjVjMjkwN2JkMjRlYTQzNA',
    author_opaque_platform_task_and_context='Original author UNVERIFIED preserved; role labels are not identity evidence.',
    independence='Different actual CODEX_THREAD_ID and selected container; no author work performed in this context.',
    requested_configuration=dict(model='gpt-6.1-sol',reasoning_effort='ultra',service_tier='default',speed='ordinary',fast='forbidden'),
    effective_configuration=dict(model='UNVERIFIED',reasoning_effort='UNVERIFIED',service_tier='UNVERIFIED',speed='UNVERIFIED'),
    configuration_qualification='No valid runtime configuration response visible. Requests, tool exits, thread IDs and environment IDs do not attest model settings; no quota/authentication inspection.',
    subtasks_created=0,other_authors_or_reviewers_created=0,reference_model_or_host_launched=0)
save(TOOLS/'execution-context.json',context)

receipt_files=[]
for root,label in [(ORIG,'original'),(CAND,'candidate')]:
    for path in root.glob('recovery-receipt-*.json'):
        target=TOOLS/(label+'-'+path.name)
        shutil.copyfile(path,target)
        receipt_files.append(dict(role=label,path=target.name,**ident(target.read_bytes())))
for root,basename in [(ORIGBOOT,'original-restore'),(BOOT,'candidate-restore')]:
    for suffix in ['stdout','stderr']:
        shutil.copyfile(root/(basename+'.'+suffix),TOOLS/(basename+'.'+suffix))

counter=load(ORIG/'evidence/tasks/R7-C13/inputs/evidence/received-final-proposals/GR7-D07-001/counter-review.json')['findings'][0]
proposal=load(BOOT/'supplemental/tasks/R7-D07/findings.json')['findings'][0]
notes=[
 '固定R配置L64–66的用途/身份与候选§7、S01及矩阵一致；只认证已声明输入。',
 '固定R的播放解析与系统消费者在可命中、记录80/100、选项100、无默认覆盖的普通条件下形成80/100请求；正文§6和S01未把请求提升为库加载或声音。',
 '只在纸面改变库身份而保持脚本/轨道/请求前提；S01能表达声明输入差异，未从中推出实际静音、失败、后备或成功。',
 'FileTests L109–115、181–242、262–273确认专门SE四后缀加字面与广义六后缀加字面不同；原B04-R17原字节保留，未把后缀认证为格式支持。',
 'Audio_Play的通用nil与解析后空名守卫先于播放；声明没有取消事务，不推出库建立/释放/取消。',
 '主通道暂停位置12、有效记录B、选项正常且无默认覆盖；Game_System L62–82先登记B，L51–59请求12后仅对ArgumentError重试0。重试再普通失败会越出，L82 frame reset及L100–101恢复清理未达，paused及保存12保留；无统一回滚/SF2处理。',
 '无默认覆盖时，Game_System L65/L171的登记先于文件存在门；缺轨道不交付该轨道请求。正常WAV对照与静态MIDI声明分层，未推此前输出静音。',
 '正文§7和S01明确不选择未来SF2、FluidSynth、宿主API或旧兼容配置；GR6-POL-001仍独立。',
]
extra_notes=[notes[0],notes[1],
 '声明/轨道命中与未知SF2消费分层；L04/L09原生接受、guard、合成、声音均未知，旧资产结构/独立复算/配置审查事实保留。',
 notes[4],
 '第一次宿主BGM请求参数错误的重试只改变请求位置为0；没有把任意SF2错误纳入此处理，双失败前缀另按C11-V06。',
 notes[6]]
vectors=[]
for original,note in zip(counter['regression_vectors']+proposal['regression_vectors'],notes+extra_notes):
    vectors.append(dict(**original,documentary_review='PASS',reviewer_reason=note,behavior_result='NOT_EXECUTED',
                        evidence_level='SOURCE_STATIC + DERIVED_VECTOR',runtime_or_model_execution=0))
vectors.append(dict(id='GR7-D07-001-S01',documentary_review='PASS',
    reviewer_reason='候选目录L436–442的唯一新增声明向量明确普通80/100前提、纸面库身份变化和全部未知；原28行及统一NOT_EXECUTED限定未改。',
    execution='DERIVED_VECTOR / NOT_EXECUTED',behavior_result='NOT_EXECUTED',runtime_or_model_execution=0))
acceptance_notes=[
 '§7 L196给出独立MIDI用途/随附身份；与固定配置相符。',
 '§7 L196与§10 L215分开轨道查找、声明、原生选择/读取/接受、合成/发声。',
 'S01和正文没有缺库必败/静音、加载成功、格式保证或未来后端强制。',
 '§7及T-WP15-01明确保留L04/L09和已接SF2结构/复算/配置审查，不扩大为所有宿主设置缺口。',
 '四目标口径相同；来源固定commit和路径/行号明确；S01只有一个且不占用B04-R编号。',
 '原14向量字段逐项相同；B04-R01–28全行、§6、§11及F05-01保留；相关消费者重新静态推导，全部行为NOT_EXECUTED。',
 '本次实际不同thread独立核验当前冻结字节；此项仅完成候选非作者核验，R7-I正式接受和后继R7-IR仍待完成。',
]
acceptances=[dict(**original,reviewer_result='PASS_SCOPED_CANDIDATE',reviewer_reason=note) for original,note in zip(counter['acceptance'],acceptance_notes)]
shared=[
 dict(group='CG01',path='audit/source-traceability.md',contribution='Only three rows inside T-WP15-01 at candidate L322–324',
      reception='CLAUSE_RECEIVABLE_PENDING_R7_I',required_preservation='Keep U01/U02/U10/U11/U12 contributions and all prior approved-input/unknown fields; do not replace whole mirror.',
      actual_integration='NOT_PERFORMED'),
 dict(group='CG04',path='deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md',contribution='Separate GR7-D07-001-S01 block after B04-R28; original rows and order exact',
      reception='CLAUSE_RECEIVABLE_PENDING_R7_I',required_preservation='Keep U01 registry and U03 world-time contributions; preserve historical rows/status and unique IDs; integrate additions rather than overwrite shared catalog.',
      actual_integration='NOT_PERFORMED'),
 dict(group='CG07',path='planning/feature-matrix.md',contribution='Only F05-02 status and note at L174; Pending only',
      reception='CLAUSE_RECEIVABLE_PENDING_R7_I',required_preservation='Keep other feature rows and U01/U02/U10/U11/U12 current contributions. F05-01 and existing approval/media scope remain unchanged.',
      actual_integration='NOT_PERFORMED'),
]
dependencies=[
 dict(id='R7-I-clause-integration',status='OPEN',owner='R7-I',scope='CG01/CG04/CG07 actual shared reception and cumulative conflict/dependency ledger'),
 dict(id='fresh-R7-IR',status='OPEN',owner='new independent R7-IR',scope='Actual cumulative integrated commit/tree; this context must not review its own review output as R7-IR'),
 dict(id='formal-acceptance-and-closure',status='OPEN',owner='R7-I',scope='Formal acceptance only after actual gates; exact direct/transitive dependencies and regressions before closure'),
 dict(id='L04-L09-native-audio',status='OPEN',scope='Native configuration supply/selection/parser/dispatch, actual bank consumption/acceptance/guards/synthesis/sound; existing finite readable/SF2 evidence retained'),
 dict(id='old56-92-and-global-dedup',status='UNCHANGED_NOT_REATTESTED',scope='No historical closure or global deduplication credit from this candidate review'),
]
per=dict(schema='r7-u13-independent-candidate-review.v1',batch_id='R7-U13',review_round='r1',
    dispatch_commit=DISPATCH,freeze_commit=FREEZE,freeze_tree='08bd0f362c74ef7645b5bbd70b557489c122ae29',
    candidate_commit=COMMIT,candidate_tree=TREE,reviewer_thread=thread,author_thread=context['author_actual_thread'],
    records=[dict(id='GR7-D07-001',classification='required',priority='P3',verdict='PASS_SCOPED_CANDIDATE',
        minimum_contract='Record only the separate MIDI-purpose bank static declaration and supplied soundfont.sf2 identity; separate it from lookup/request/native outcomes and future policy.',
        candidate_identity_table='review-input-receipt.json#/candidate_files',
        acceptance_checks=acceptances,vectors=vectors,shared_reception=shared,
        normal_cancel_failure_partial={k:dict(result='PASS_DOCUMENTARY',reason=v) for k,v in {
            'normal':notes[1], 'cancel':notes[4], 'failure':extra_notes[2]+' '+extra_notes[4], 'partial_submission':notes[5]}.items()},
        conditional_sync=dict(additional_writes=[],WP15_section11='UNCHANGED',F05_01='UNCHANGED',optional_policy_navigation='NOT_ADOPTED'),
        manifest_assessment=dict(result='SUFFICIENT_FOR_THIS_FROZEN_DELIVERY',mirror_entries=4,unlisted_nonself_author_evidence=19,
            reason='Original author prompt requires per-mirror B/new identities. It does not require each evidence identity repeated in the author manifest. Four mirror identities match; final immutable commit/tree, root exhaustive 24-file table and this independent complete read bind the other evidence plus manifest. Do not claim author manifest listed all 24.'),
        unmet_dependencies=dependencies,L01_L14='RETAINED',old56_92='UNCHANGED',progress_denominator='27 items / 13 batches',
        semantic_scope='This exact isolated candidate only; no actual integration PASS, ACCEPTED or CLOSED')],
    requested_configuration=context['requested_configuration'],effective_configuration=context['effective_configuration'],
    execution=dict(SOURCE_STATIC='Fresh scoped source/configuration and documentary review',DERIVED_VECTOR='15 reviewed paper vectors; every behavior result NOT_EXECUTED',
                   TOOL_VALIDATION='Identity/scope/transport/documentary checks only',REFERENCE_OBSERVATION=0,independent_full_behavior_model=0,reference_Ruby=0,game_host=0,Demo=0,native_media=0,synthesis=0,sound=0,real_save_replay=0),
    integrated_PASS=False,ACCEPTED=False,CLOSED=False)
save(OUT/'per-id.json',per)

read_scopes=[
 dict(path='mkxp.json',repository='R',scope='Full L1–159; declaration L64–66'),
 dict(path='Data/Scripts/001_Technical/002_Files/001_FileTests.rb',repository='R',scope='L1–310, especially L109–115,181–242,262–273; remaining file identity only'),
 dict(path='Data/Scripts/004_Game classes/002_Game_System.rb',repository='R',scope='Full L1–287; request/registration/retry/resume/memory L44–249'),
 dict(path='Data/Scripts/008_Audio/002_Audio_Play.rb',repository='R',scope='Full L1–278; parse/routing/early-return/stop paths'),
 dict(path='Data/Scripts/008_Audio/001_Audio.rb',repository='R',scope='Full L1–154; duration only, no bank-consumption inference'),
 dict(path='Game.exe',repository='R',scope='Full byte identity only; original finite forward-map read independently; no new machine-code semantics claimed'),
 dict(path='deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md',repository='candidate',scope='Full L1–224 and complete comparison to B; all added strong assertions independently checked'),
 dict(path='deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md',repository='candidate',scope='Full L1–708 read; U13/audio/history clauses independently reviewed; unrelated rows checked for preservation and no new cross-scope claim, not a fresh certification of their source programs'),
 dict(path='audit/source-traceability.md',repository='candidate',scope='T-WP15-01 with neighboring headings L308–337; complete mirror comparison; other sections identity/preservation only'),
 dict(path='planning/feature-matrix.md',repository='candidate',scope='F05-01/F05-02 and neighbors L162–181; complete mirror comparison; other rows identity/preservation only'),
 dict(path='original-contract and prompts',repository='f622356f',scope='Full U13 seven groups and author/reviewer prompts; shared-path scopes of U01/U02/U03/U10/U11/U12, no semantic approval of those candidates'),
 dict(path='C13 inputs/delta-j16/findings.json',scope='/records/30 complete by structural comparison of duplicate proposal/counter payloads and reading remaining fields; other records not semantically reviewed'),
 dict(path='C13 late-author-payload-receptions.json',scope='/records/3; C11 received counter is not a D07 author mutation'),
 dict(path='C13 received-final-proposals/GR7-D07-001/counter-review.json',scope='Full independent C11 counter including all 7 acceptance and 8 regression entries'),
 dict(path='C17 limits-and-alias-reception.json',scope='Full L01–L14, overlays and provenance/alias qualifications'),
 dict(path='C13 identity-index/input-manifest/raw-binding-manifest',scope='All bytes/JSON validity and named input bindings only; no inheritance of semantic reads from listed files'),
 dict(path='supplemental tasks/R7-D07/findings.json',scope='Full original proposal including six exact regression vectors'),
 dict(path='supplemental tasks/R7-C11/challenges/native/forward-map.json',scope='Full original finite map and exact NATIVE-U01–U05 unknowns; no new native program execution'),
 dict(path='all 20 current author evidence files',scope='Full data reception/read, author scripts inspected as text, receipt/log fields programmatically checked; old first-push receipt not confused with final candidate'),
]
receipt=dict(schema='r7-u13-independent-review-input-receipt.v1',observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    dispatch_commit=DISPATCH,dispatch_tree=audit['dispatch_tree'],freeze_commit=FREEZE,freeze_tree=audit['freeze_tree'],
    candidate_commit=COMMIT,candidate_tree=TREE,fixed_B=B,base_repository_tree='84f79ec6e772aacbf3a464fde68cdc5a280e2950',base_formal_tree='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c',
    reference_commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',reference_tree='7589c800b61ba13a13040ed0d686979b80a84fd0',
    reviewer_context=context,frozen_control_identities=audit['frozen_controls'],candidate_files=audit['candidate_files'],
    candidate_files_received=24,candidate_bytes_received=862370,original_files_restored=21,original_bytes_restored=16814642,
    restoration_receipts=receipt_files,all_actual_current_bytes_sha256_blob_and_modes_match=True,
    candidate_complete_diff_only_authorized_scope=True,author_evidence_files=20,author_manifest_mirror_count=4,
    original_contract_manifest_requirement='Per mirror B/new identity; all other evidence bound by final commit/tree and complete actual readback',
    original_input_identity_table='tools/byte-audit.json#/restored',supplemental_inputs=[dict(logical_path=row['logical_path'],publication_commit=row['publication_commit'],transport_path=row['transport_path'],decoded=row['decoded']) for row in load(AUTHOR/'targeted-recovery.json')['files']],
    read_scopes=read_scopes,read_log_qualification='Early discovery/download and semantic reads have actual platform tool I/O but no separate local per-command UTC/stdout/stderr capture. No fabricated backfill. Local public logged verification begins in tools/commands.jsonl; restore tools separately supply their actual HTTP UTC/identity receipts and stdout/stderr. Publish/commit tail and final remote readback use actual detached platform output to avoid self-reference. Private model streams are excluded.',
    operational_notes=['Initial /workspace git-status attempt failed because repository is its child; corrected to actual repository.',
                       'Optional GitHub API tree lookup received proxy403; fixed Git objects and immutable raw URLs supplied all required inputs.',
                       'The initial branch fetch completed; a later attempted termination found no remaining fetch processes. No input conflict or evidence loss.',
                       'No .agents/skills at B or dispatch commit, and /workspace/.agents is an empty read-only mount. Project AGENTS.md read in full.'],
    snapshots='Selected immutable source snapshots, not full reference checkout or runtime certification',L01_L14='RETAINED',semantic_credit_from_transport=False)
save(OUT/'review-input-receipt.json',receipt)

report='''# R7-U13 r1 独立候选复审

GR7-D07-001：**PASS_SCOPED_CANDIDATE**。结论只绑定本次冻结的候选正文及证据，允许交 R7-I 按条款接收；实际整合 PASS、正式 ACCEPTED、CLOSED 均未宣告。

派发固定提交 `95c260d8f3fb4a171675dde877137fcd4c2f1c8d` / tree `577c350364bb4e2eb712325a9095d53d29eeeeb3`；其完整 reviewer-dispatch 已读。候选输入冻结 `aa369555b0e8b6c8b077f964b54ed63d3b924f26` / tree `08bd0f362c74ef7645b5bbd70b557489c122ae29`。本次实际审查 candidate `5635c73ea14adc278961da0e3917c2d00d580a25` / tree `e2c261a77a7268a5eb07e7e364ac257d9fed3e31`，没有用浮动作者分支替换。

实际审者 thread 为 `01a13ff1-4e91-74b4-ac83-5838dbb59018`，从本环境 `CODEX_THREAD_ID` 读取；作者为 `01a13f80-5248-7789-ab67-26ce7270c019`。二者 thread 及容器不同。作者未暴露的 opaque task/context 资格保留原样；公开工具 PID 不冒充模型进程 PID。请求 gpt-6.1-sol / ultra / default / 普速禁 Fast；实际 model、effort、tier、speed 分别 **UNVERIFIED**，没有用请求、角色名或退出0认证。合同禁止创建子任务，本审者创建0个。

本容器按已完整读取的固定恢复工具和清单，实际恢复原合同/源/反证21文件、16,814,642字节，再恢复当前候选24文件、862,370字节。另定向恢复固定C2的原D07提案及C11 native forward-map。全部bytes/SHA256/Git blob和普通100644模式独立重核；24文件均与实际candidate树相符；对B完整差异只有授权candidates/R7-U13/下24个新增文件。四份镜像逐字节与B比较，根mirror-diffs.patch及作者零上下文changes.patch均独立复算匹配。完整身份表和真实恢复回执见 [review-input-receipt.json](review-input-receipt.json) 与 [tools/byte-audit.json](tools/byte-audit.json)。

原作者manifest确实只逐项列4份镜像，19份其它非自身证据没有在其中重复身份。原f622356f作者入口要求的是“逐镜像固定B身份、新bytes/SHA/blob”；这4项均满足。最终固定commit/tree、根24文件完整表及本次独立全量读回共同绑定其余证据与manifest自身，因此本次交付可审查且满足该原要求；没有伪称作者manifest原来列全24项。20份作者证据全部接收审读，脚本只作为文本；旧首推23文件/825,028字节的回执保持旧版本资格，未冒充当前24文件。作者早期LF物化偏差、两次工具退出1及暂存空上下文检查退出2均保留；这些失败已由当前实际字节重新核清，未当语义PASS依据。

本次全文阅读原七组、原C11完整反证、D07原提案、L01–L14及当前WP15正文224行和共享目录708行。源新读范围、其它镜像定点范围及仅身份用途在receipt逐项分开；共享目录其它领域的原源程序没有因此获得重认证。C13根记录/records/30内提案与反证的重复嵌入均与已读原载荷相同，晚到/records/3明确C11不是D07作者变更。项目AGENTS.md全文已读；B、派发提交及实际工作区均未发现相关.agents/skills文件，workspace该挂载为空，没有虚构技能读取。

| 当前候选目标 | 实际变更及独立结论 |
| --- | --- |
| WP15 §7 L196 / §10 L215 | 固定R配置L64–66明确MIDI用途及soundfont.sf2身份；正文仅增加静态声明和依赖引用，分开查找、声明、原生消费/接受、合成及声音。PASS。 |
| 测试目录L436–442 | 单独新增GR7-D07-001-S01，具名80/100普通对照、纸面仅换absent-bank.sf2及全部未知；原B04-R01–28、顺序和资格保持。PASS。 |
| Feature Matrix F05-02 L174 | 只增加Pending和静态声明备注，原历史批准及Inventoried媒体范围保持。F05-01原字节未动。PASS。 |
| T-WP15-01 L322–324 | 只增加配置、定点脚本、既有有限原生证据及向量资格三行。精确R身份、路径、行号可追溯，无参考程序复制。PASS。 |

正常、取消、异常和部分提交的结论是本次重新审读得出。正常系统、可查到theme.mid、预解析记录80/100、选项100、无默认覆盖时，脚本层形成80/100请求；这不要求假定库已原生选择或可听。只在纸面更换库身份改变的是声明输入关系，没有执行配置变更，没有推出缺库必败、静音、后备或成功。普通WAV对照不抵消该独立角色。

通用nil/空名入口提前返回；静态声明没有取消事务，所以没有库初始化、释放或取消承诺。缺库、坏库、字段缺省/无效、原生guard、解析、后端及合成失败都保持未知。广义六后缀与专门SE四后缀加字面路径分别核对，B04-R17不变，后缀不能成为格式或可播放认证。

部分提交精确核对：主BGM暂停并保存位置12，恢复有效B，系统及选项正常、无默认覆盖；源先逻辑登记B，再请求位置12。首请求ArgumentError时只重试位置0；该重试再抛普通错误会传播，后继frame reset和恢复清理未到，paused与保存12保持。不存在统一回滚保证，也不能把位置0重试解释为SF2错误处理。缺轨道时BGM/BGS登记可先发生而不请求该轨道，原默认覆盖、暂停/记忆、时长和其它分入口规则保持。

| 原验收 | 本次结论 |
| --- | --- |
| C11-A01 | PASS：独立MIDI声明和随附身份已列。 |
| C11-A02 | PASS：轨道、声明、实际原生消费、接受与声音分层。 |
| C11-A03 | PASS：未增加运行故障/成功、未来SF2/FluidSynth或宿主API强制。 |
| C11-A04 | PASS：L04/L09及已接SF2结构、复算、配置审查事实保留。 |
| C11-A05 | PASS：四目标与独立S01口径一致，来源精确。 |
| C11-A06 | PASS：全部14个原向量字段精确保留，既有正文/目录/历史资格无回归。 |
| C11-A07 | PASS_SCOPED_CANDIDATE：本次不同实际context核验已完成；正式接受仍由R7-I后续决定。 |

C11-V01–V08、D07-SF-CFG-01–06以及S01的逐项输入、预期、本次判断及依据全部在 [per-id.json](per-id.json)。15项文档核验均PASS，**行为结果全部NOT_EXECUTED**。原14项input/expected/execution字段没有被改写。历史回归重点是B04-R17、RS09–19（含GR-007五组门）、B04-R01–12/22–26和M10-008；§6、§11、历史目录行和既有批准注记保持原字节。本结论不重签旧56/92，也不以历史PASS替代当前语义检查。

CG01/CG04/CG07本批贡献可按条款接收，实际整合仍OPEN。CG01只接T-WP15-01三行，保护U01/U02/U10/U11/U12其它来源贡献；CG04只追加独立S01，保护U01登记与U03世界时间及所有原目录条目；CG07只接F05-02待审备注，保护其它批次行。已读取原冲突组及这些批次具名共享路径scope，文件相交没有被当作他批已通过或已合入。R7-I须串行按条款整合，不能整份覆盖镜像。§11和F05-01无需条件同步且未动；没有采纳optional、导航facet、no-required或policy。

L01–L14保留，特别是L04原生配置供应/选择/分派和L09实际消费、接受/guard、合成/声音。Game.exe本次只核完整身份并独立读既有有限map及精确UNREAD依赖；没有重新解释整个原生程序或重审SF2算法。未来格式/后端/API和GR6-POL-001旧兼容政策未选择；不能因本条静态文档PASS关闭这些边界。进度分母仍27项/13批。

SOURCE_STATIC、DERIVED_VECTOR和TOOL_VALIDATION分开。参考/Ruby程序、独立完整行为模型、游戏宿主、Demo、native媒体、合成、发声、真实存档回放新增执行均0。历史H14/UTIL-03局部观察保持原资格，未倒填到本批。

工具证据见 [tools/commands.jsonl](tools/commands.jsonl)、两份原始恢复回执和 [tools/author-evidence-audit.json](tools/author-evidence-audit.json)。早期定位/下载及内容读取的真实I/O在平台工具记录，未单独落盘每条UTC/stdout/stderr；本报告如实保留此日志限制，没有重建历史时间。后继公开校验日志保存真实argv、UTC、工具PID、stdout、stderr和退出。提交/推送尾部与最终完整远端读回采用真实平台结果及分离回执绑定，避免自引用hash；私有模型流不发布。

唯一成果分支为codex/r7-u13-reviewer-20261015-r1，从固定B的独立干净checkout创建；只交本reviewer/r1证据，没有作者镜像、正式或公共文件变更。仍待R7-I按条款整合、共享接收及依赖/历史回归登记，随后新的独立R7-IR审真实累计整合字节，再由R7-I决定正式接受和满足条件后的关闭。当前没有输入/独立性阻塞。
'''
(OUT/'report.md').write_text(report)
print(json.dumps(dict(status='REVIEW_REPORT_MATERIALIZED',verdict='PASS_SCOPED_CANDIDATE',record='GR7-D07-001',vectors=15,behavior='NOT_EXECUTED',reviewer_thread=thread,reference_execution=0),ensure_ascii=False))
