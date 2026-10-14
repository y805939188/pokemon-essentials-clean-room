import json, hashlib, datetime, subprocess
from pathlib import Path

OUT = Path(__file__).resolve().parent
PREP = OUT.parents[1]
CONTRACT = json.loads((PREP / 'contracts/R6-U06.json').read_text())
VERIFY = json.loads((OUT / 'verification.json').read_text())
AUTHOR = json.loads((PREP / 'candidates/R6-U06/evidence/author-findings.json').read_text())
GROUPS = ['identity_and_verdict', 'bidirectional_evidence', 'premises_and_counterexample',
          'minimum_revision_contract', 'acceptance_and_regression', 'independent_adjudication',
          'dependencies_and_receivers']
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
COMMON_HISTORY = [
    'R1仅原WP资格；R2为229控制/21批/341精确贡献；R3为23/76，M09 optional、U08历史未启动、M02 NO_REQUIRED保留。',
    'R4当前17/76与B5 16/75及Summary具名残余区分；未把当前修订扩大为旧领域总资格。',
    'R5唯一activation只选13fddb…的92 proposed原精确内容，92 CLOSED/OPEN0、51 P2/41 P3；7 optional、7 no-required、原6 policy、原13 limits分列。262原贡献=259显式+3镜像，6行政transfer与3纠正不当作新语义。',
    'R4/B5固定9366…三正式载荷、R5原任务包22fba…、所选关闭13fddb…、唯一activation12df95…均恢复固定对象并比对相关完整语义字段。旧G03/G09 FAIL、U03旧FAIL/修复、两advisory MISMATCH和SC-U07-001体内LF旧错误及其纠正保留。',
    '233旧测试ID顺序及重复次数保持，53个B17/B19/B20/U07旧行逐字节保持；所有非本批修改的旧表行逐字节相同。旧PASS没有代替本次回源审查。'
]
DEPENDENCIES = {
    'primary_batch': 'R6-U06', 'author_entry': 'R6-U06-A', 'reviewer_entry': 'R6-U06-R',
    'blocking_author_dependencies': [], 'unique_actual_receiver_writer': 'R6-I',
    'file_receivers': {
        'demo-dx/wp73-a-content-editors.md': ['R6-U06'],
        'demo-dx/wp75-project-conversion-and-authoring-tools.md': ['R6-U06', 'R6-U09'],
        'test-catalog/demo-dx-wp72-73-74-75-76-77.md': ['R6-U06', 'R6-U07', 'R6-U08', 'R6-U09']},
    'pending': ['唯一写者实际接收', '共享整合后全文非作者复审', '直接及传递接口验收', '实际整合版精确历史回归', '正式接受', 'CLOSED登记'],
    'administrative_sync': 'Feature Matrix/traceability/audit/planning/public acceptance仅R6-I在相应授权及整合验收后写入，本审者不写。',
    'identity_scope': '固定入口指定/root、source_thread_id 01a10d94-84b9-759e-aa1d-edb0d9b6d0e2；作者记录另含其指定整合线程01a13a93-d1da-71e4-a488-63b8524f503d。保留两记录时点；本审者没有取得实际R6-I平台UUID或正式接收回执，不能代为裁定或冒称已接收。'
}
DETAILS = {
'R6-B-001': {
 'evidence': [
  'R/MapsAndEvents完整1–1751新读。348–364：表/优先级对象访问到达局部救援，且map.tileset_id本身可读时，构造的说明仅tileset ID和map ID。正常返回nil不是该异常救援的同义输入。',
  '366–400通行/柜台查询：合法已载地图、合法坐标及Table读取先满足；非空tile在通行表无条目才有map/x/y/一基层号，最高层为3。空tile先false；优先级或Table其它故障不统一成此说明。',
  '生产—消费：MapData缓存/查询→活动check_counters1625–1678→驱动1683–1751（1725调用）；Debug_MenuExtraCode668–725在逐格前685取表。likely_passage?919–934定义可读，但唯一命中1256处于1232–1397停用块，不能充作活动consumer。',
  '外层Compiler.main1101–1115及Errors完整1–94打印/再抛不证明给局部说明补坐标，也不证明窗口/日志实际成功。反向定位候选WP75§10:290、§15.1:393及CV-M24:188，三处一致。'
 ],
 'counter': [
  '独立反证两B记录及debug/Compiler对应完整结果支持P3收窄，不支持原提案把一切缺表/nil或其它异常都概括为两ID。',
  '最小夹具：地图5、tileset7，地图已载且tileset_id可读，对象/属性访问在局部保护内失败→构造两ID说明；不要虚构坐标/层。',
  '另独立合法Table、坐标(2,3)、最高层非空tile999、通行表无该项→map5/(2,3)/层3；普通合法tile和空tile各保持原查询结果。',
  '正常取表返回nil时，后继首次使用的故障另判；从本次源范围不推所有异常全局统一错误。此前已成功写出的文件不回滚，个别地图保存失败仍按已有局部保护。'
 ],
 'revision': ['候选准确分开对象/属性取表异常、正常nil返回与无效tile条目；§10、§15.1和CV-M24同步。', '未改变异常传播、已写前缀、单图保存容错、地图/媒体/宿主未知。最小必要追加修订：无。'],
 'acceptance': ['独立人工核B001-01…05五个静态案例，正常、缺对象、无条目、nil和写出前缀均与固定源相符；NOT_EXECUTED。', 'WP13地图/Table前提、WP04编译异常/部分写出、WP03导出边界均已新读对应完整相关单元。']
},
'R6-B-002': {
 'evidence': [
  'MapsAndEvents139–181构建器按追加顺序产命令；1192–1223售货展开：免费容量门→生成提示→接收脚本；收费金额门、容量门→扣价→生成提示→接收脚本。生成提示是转换器生成文本，并非给注释任意自由文案参数。',
  '有序解释器update84–136在命令返回后推进；command101162–209同步等待，预读文字不提前执行后面的355；125656–661扣款、3551168–1179直到抵达才求值。execute_script138–181异常包装没有自动退款。',
  'pbReceiveItem706–736自身先获得消息，后730添加，再成功入包消息；接收入口抵达不等于立即入包。WP27§7:156–191明确既有内层顺序；WP17§7.1及异常边界、WP13主文/命令矩阵均接合。WP29普通商店自身先add后扣价为另一入口，不重写它。',
  '反向候选WP75§8.3:241–242及CV-M11:175明确外层顺序、观察点、合法前提和异常前缀。旧文本转换阶段/ASCII/大小写/首行/非负价门保持。'
 ],
 'counter': [
  '原“＋”可以是动作集合；缺的是有序合同，不裁为明确字面反序。两份独立B反证/Compiler反证的限定已采纳。',
  '最小有效页只含售货首行注释及结束；已注册POTION、有效背包/余额、普通同步单行生成文本、转换不另重排、无并行/插件/回入或其它相关写入。',
  '免费money1000/POTION0在生成提示时仍1000/0；收费200在该时点800/0。继续正常到接收内部获得消息时仍qty0，再成功添加才qty1。',
  '容量拒绝、钱不足不扣/不接收；收费生成提示处失败，已扣800/qty0前缀不撤销，接收未达。本链没有退款或整体回滚步骤，不扩大为全局永久不能补偿或游戏必能继续。'
 ],
 'revision': ['候选最小补外层免费“生成提示→接收”、收费“扣款→生成提示→接收”，接收内层引用正确WP27。', '未引入事务/退款，未改变WP29普通商店合同及旧处理门。最小必要追加修订：无。'],
 'acceptance': ['独立人工核B002-01…06六个静态案例，免费、收费、两拒绝门、消息故障与接收内层前缀均成立；NOT_EXECUTED。', '正常同步返回前提与失败只到已达前缀均明确；没有把缺宿主当作此有限静态顺序不可裁定。']
},
'R6-DX-E001': {
 'evidence': [
  'Species.editor_properties113–147实际Types绑定118是一般GameDataPoolProperty(:Type,false)，默认不自动排序且不允许重复，不调用双槽TypesProperty496–523。专门pbChooseTypeList151–155排除pseudo；实际一般池经通用目录116–129，Type完整1–141接受已注册pseudo。',
  '字段全表逐个回源：Types/蛋群/两特性池不重复且不自动排序；TutorMoves/EggMoves不重复且自动排序（入口标识排序、刷新名称排序）；Offspring一般Species目录可重复、不自动排序并不强制只0形态；三档野生持物一般Item池可重复、不自动排序。',
  '一般池1040–1155：不重复池入口对共享旧集合原地去重；新工作表、添加已有只定位、改成其它已有删当前项、选择器取消不新增、手动换序门及Apply Yes/No/Cancel分开。父pbPropertyList1624–1706自身Yes/No/Cancel门与子赋槽分开。',
  'EditorScreens926–987从PBS属性投影生成父工作槽→父Yes→species validator292–330仅Types去重去空→注册976→档案977→基础PBS978。Species初始化175–221/PBS投影392–453、Writer174–223、CSV742–842不截两项。此链只写基础物种PBS，不冒称额外forms writer。',
  'Pokemon.types313–315返回完整副本、hasType331–334可命中第三项；WP19§3.1原本正确，未扩大为完整三类型战斗证明。反向候选WP73-A§3.3/3.4限定及§4.4:140–151绑定表、CE-M15:62、CE-M19:66、六CE-TYPES行75–80都一致。'
 ],
 'counter': [
  '完整原DX-E001提案/非提出者editor反证支持实际字段绑定遗漏，不能把独立双槽控件或单引用pseudo过滤移植到Types池。',
  '合法非空Types初始[NORMAL]；已注册FIRE/WATER及pseudo P；正常父保存链全部前门/写出成功，无插件改写。添加FIRE/WATER并Apply/父Yes→工作表、登记/档案/基础PBS均保留[NORMAL,FIRE,WATER]顺序；完整个体查询/第三成员判断成立。',
  'P在一般Types池可选、专门单引用选择器不可选；添加已有不新增、改为其它已有删本项、选择器取消保持、新表ApplyNo或父No不提交，Cancel各留相应页。',
  '原共享[NORMAL,FIRE,NORMAL]仅打开后ApplyNo/父No仍被入口去重成[NORMAL,FIRE]，但未新增档案/PBS写入。取消新表不是内存总回滚。登记后档案失败或档案后PBS失败只证实已完成前缀。'
 ],
 'revision': ['候选增加所有实际一般池字段绑定与Types三类型/pseudo案例，保留双槽本身、单引用过滤、共享规范化/取消和原物种保存链。', '已有进化复数编辑投影空表、单数导出数字参数、训练家IV/EV默认/取消、B17/B19/B20与单选择器规则保持。最小必要追加修订：无。'],
 'acceptance': ['独立人工核E001-01…06六个静态案例并对应CE-TYPES-01…06，正常、pseudo、重复、两级No/Cancel、共享入口去重和后段写出失败成立；NOT_EXECUTED。', '新读Type producer、GameData目录、validator/registry/PBS writer、直接Pokemon消费者及WP19对应单元，未用作者自检代替。']
},
'R6-DX-E002': {
 'evidence': [
  'WritePBS291–351完整metrics writer先从非零形态收后缀建路径，再按该后缀逐记录；只有非零形态才在五组均与当前基础相等时省节。基础记录不经过该相等省略门。',
  'Metrics完整1–101解释现有/惰性副本、五组及默认空suffix；SpritePositioning1–111的正常No档案重载、pbSave103–106档案→PBS前缀保持，没有新增广播/后缀统一。',
  '正文WP73-B§7.5及B19-C016本已正确，全文新读并不修改。反向只改候选WE-M20:107，明确路径仍由非零形态决定、同后缀基础输出、相等非零只省节。'
 ],
 'counter': [
  '原提案可能被“所有行必须不同”宽读；完整非提出者E002反证/root裁级仅支持P3独立测试行主语修复。',
  '仅基础记录，无非零→无路径。基础B/非零D同suffix且五组不同→该路径两节；同suffix五组相等→仍有该路径、基础一节。',
  '基础suffix s、非零suffix t不同→路径只由t选，该路径只写非零；基础不写是suffix不匹配，不是基础相等被省略。不存在/不能正常取当前基础等前提不补推。',
  '惰性副本默认suffix为空而非沿用非空suffix；正常退出No重载及保存档案/PBS失败已达前缀保持，不声称各文件原子。'
 ],
 'revision': ['唯一必要改动已在WE-M20落实；WP73-B正文、B19-C016详细矩阵和部分失败/NOT_EXECUTED资格逐字节保持。最小必要追加修订：无。'],
 'acceptance': ['独立人工核E002-01…05五个静态案例，四个规定布局及退出/前缀对照成立；NOT_EXECUTED。惰性副本另由完整Metrics源静态核对。', '不将读writer或人工布局当作实际目录创建/PBS写出、编辑器UI或宿主验收。']
}}

records = []
for scope, author in zip(CONTRACT['scope_contracts'], AUTHOR['records']):
    id_ = scope['id']; d = DETAILS[id_]
    assert author['id'] == id_
    record = {
      'id': id_,
      'identity_and_verdict': {'classification': scope['identity_and_verdict']['classification'],
        'severity': scope['identity_and_verdict']['severity'], 'title': scope['identity_and_verdict']['title'],
        'root_cause_key': scope['identity_and_verdict']['root_cause_key'], 'aggregation_aliases': scope['aggregation_aliases'],
        'verdict': 'PASS', 'state': 'CANDIDATE_PASS',
        'scope': '仅冻结4d92cda…的三份镜像有限静态语义；原OPEN_NOT_UPDATED历史不覆写。'},
      'bidirectional_evidence': {'result': 'PASS', 'evidence_level': 'SOURCE_STATIC', 'complete_chain': d['evidence']},
      'premises_and_counterexample': {'result': 'PASS', 'counterevidence_and_boundaries': d['counter'], 'execution': 'NOT_EXECUTED'},
      'minimum_revision_contract': {'result': 'PASS', 'assessment': d['revision'], 'required_additional_revisions': []},
      'acceptance_and_regression': {'result': 'PASS', 'new_static_acceptance': d['acceptance'], 'precise_history': COMMON_HISTORY,
         'author_vector_assessment': author['acceptance_and_regression'], 'author_vector_limit': '原记录完整保留作定位；每条人工回源核对，不继承作者PASS为观察。所有22向量未执行。'},
      'independent_adjudication': {'result': 'PASS', 'reviewer': 'R6-U06-R /root direct non-author',
         'requested': {'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'default'},
         'effective': {'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','platform_uuid':'UNVERIFIED'},
         'independence': '本任务未参与作者候选或正式稿撰写，未改候选；本人直接审读，无新增CLI或子审者代审。',
         'candidate_files': VERIFY['candidate_files'], 'support': d['evidence'], 'opposition': [],
         'remaining_unknowns': ['有效平台配置无回显','原生宿主/媒体/完整地图/实际UI与PBS写出未运行','实际整合版本尚未审查'],
         'reading_evidence': ['readings.jsonl','json-readings.jsonl','reading-attestation.json'],
         'minimal_required_revision': 'NONE'},
      'dependencies_and_receivers': dict(DEPENDENCIES, nonblocking_domain_dependencies=CONTRACT['nonblocking_domain_dependencies'][id_])
    }
    assert all(k in record for k in GROUPS)
    records.append(record)
report = {
 'schema': 'R6.U06.independent-review.v1', 'utc': NOW, 'logical_id':'R6-U06-R',
 'decision':'PASS', 'decision_state':'CANDIDATE_PASS', 'candidate_commit':VERIFY['candidate_commit'],
 'candidate_tree':VERIFY['candidate_tree'], 'candidate_directory_tree':'7a2817af930dc0afa6ce0011b4c29d4be32bc9d0',
 'preparation_commit':'469a268b92daed7b4d28d7fd0da75520cbb7228f',
 'reference_commit':CONTRACT['frozen_reference'], 'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0',
 'formal_commit':CONTRACT['frozen_main'], 'formal_tree':'1046fbb657882e84b3dfc6d017943a9edf7782e5',
 'contract_identity':{'bytes':111186,'sha256':'38ff31ade36e0ff6b7e9cd3b70f904e221ba0bb3dfb85d0c7d1047a7db62cef6','git_blob':'5ae84a18e246a813e8c9b6023b81d12a6b3aee11'},
 'prompt_identity':{'bytes':224129,'sha256':'b67e8aab419ca64d07c4cd60638aecd154e341ec2e79bf25a31b93a4bb7fd4bf','git_blob':'416519b53a66af56a68593d0bce30f2c360ba9b3'},
 'records':records, 'required_additional_revisions':[], 'candidate_semantic_blockers':[],
 'tool_validation':{'independent_checks':26,'author_checks':30,'author_checks_level':'DOCUMENT/TOOL_ONLY','author_full_remote_payload_readback':46},
 'manual_vectors':{'B001':5,'B002':6,'DXE001':6,'DXE002':5,'total':22,'executed':0},
 'execution_counts':json.loads((OUT/'execution.json').read_text())['execution_counts'],
 'limits': ['L01完整地图/工程','L02图形音频','L03原生宿主','L04游戏/运行库','L05–L09具名内嵌/字体/soundfont限制',
            'L10序列化解码不等于执行','L11任意扩展/配置组合','L12外部状态/服务','L13纯元资料','L14有效配置/工具元数据'],
 'scope_not_granted':['INTEGRATED_PASS','formal_acceptance','CLOSED','full host/Demo','real save','production success','permanent compatibility profile'],
 'publication_rule':'有限core C后有限publication P；自身identity由外部最终响应及实际远端读回绑定，不递归自哈希。'
}
(OUT/'review-findings.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

VECTOR_NOTES = {
 'B001-01':'MapsAndEvents348–355在合法map.tileset_id下的局部救援发生早于后继逐层读取。',
 'B001-02':'357–364独立优先级访问保护，只构造两ID，不能补坐标。',
 'B001-03':'366–400合法两表/非空tile进入无条目支；i=2对应一基层3。',
 'B001-04':'合法普通查表不触此错误；passable?缺map/越界的false与counter?前提分别核。',
 'B001-05':'nil正常返回未触取表救援；驱动逐图写出和外层异常无总回滚/日志成功保证。',
 'B002-01':'1192–1223免费生成顺序、101同步等待、355晚达与ReceiveItem706–736先消息后add相接。',
 'B002-02':'收费125先抵达、1000减200为800；其它链同免费；qty只在后继正常add变1。',
 'B002-03':'收费金额比较和免费/收费容量前门失败均不达扣款/接收。',
 'B002-04':'101返回前错误使后继355未达；已执行125不自动补偿，只裁已达前缀。',
 'B002-05':'ReceiveItem内层消息先add；捕获到add false/后段异常不根据早期can_add推完成。',
 'B002-06':'MapsAndEvents售货regex/登记/价格门与候选CV-M11旧识别门及文本转换阶段保持。',
 'E001-01':'实际Types一般池→父槽→validator→register/archive/base PBS→Pokemon.types完整序列链不截两项。',
 'E001-02':'Type producer及通用catalog完整each；专门单引用chooser自己的pseudo filter不移植。',
 'E001-03':'一般池允许重复false的ADD已有/SET撞其它已有和selector cancel分支分别核。',
 'E001-04':'池No返回oldvalue、父No不register、两级Cancel继续各自循环，未接收新增序列。',
 'E001-05':'oldvalue入口uniq!且共享PBS Types投影，不因No恢复；登记/写出门仍未达。',
 'E001-06':'EditorScreens976→977→978顺序，故障只裁已完成登记/档案及PBS部分前缀。',
 'E002-01':'write_pokemon_metrics选paths仅看非零form；不存在非零即无PBS路径。',
 'E002-02':'路径s已选；基础不进省略比较、非零不同五组不省，两节。',
 'E002-03':'路径先选再省非零相等节；基础继续写，不取消路径。',
 'E002-04':'只t由非零选路径；基础s不匹配过滤，非零D写出。',
 'E002-05':'SpritePositioning91–106正常No重载、Yes archive后PBS；Metrics现有布局不新增广播。'
}
vectors=[]
for author in AUTHOR['records']:
    for vector in author['premises_and_counterexample']['author_vectors']:
        vectors.append({'canonical_id':author['id'],'id':vector['id'],'input':vector['input'],
          'expected':vector['expected'],'independent_source_reason':VECTOR_NOTES[vector['id']],
          'result':'SUPPORTED_STATIC','evidence_level':'DERIVED_VECTOR','execution':'NOT_EXECUTED',
          'candidate_commit':VERIFY['candidate_commit']})
assert len(vectors)==22 and len(VECTOR_NOTES)==22
(OUT/'derived-vector-review.json').write_text(json.dumps({'schema':'R6.U06.independent-manual-vectors.v1',
 'utc':NOW,'vector_count':22,'execution_count':0,'rows':vectors,
 'limit':'本人逐案人工回源推导；没有向量执行、参考程序执行、独立模型或宿主观察。'},ensure_ascii=False,indent=2)+'\n')

readings=[json.loads(x) for x in (OUT/'readings.jsonl').read_text().splitlines()]
jreadings=[json.loads(x) for x in (OUT/'json-readings.jsonl').read_text().splitlines()]
attestation = {
 'schema':'R6.U06.reviewer-reading-attestation.v1','utc':NOW,
 'method':'本人语义审读；完整字节/身份、lossless JSON选定子树、连续编号正文范围分开记录。工具成功、hash、搜索命中不自动算语义PASS。',
 'AGENTS':'先完整读仓库AGENTS.md；适用祖先无其它AGENTS，报告路径无嵌套指令。clean-room仅行为/证据，不提供框架源码，不写R。',
 'prompt':'完整读固定审者提示词：手动合同、原合同七组及四个完整原提案、footers、115条恢复映射均覆盖；embedded JSON逐字节等于完整contracts/R6-U06.json。重复身份对象lossless dictionary复用，不是摘要。早期超限截断不计完整，后继定段/完整子树补读。',
 'formal_fulltext':'三镜像全部225/439/340行按连续小段完整语义新读。固定main三正式稿完整bytes逐段比较：所有equal span等于已读候选全文，全部旧差异行完整输出新读，见baseline-comparison.json及reviewer-verification-02.stdout。不是只看候选差异摘要。WP73-B全部217行新读。',
 'source':'MapsAndEvents全部1751行新读；Types/Metrics完整对象、通用目录/池/父属性/validator/writer/CSV/个体消费者、解释器/接收及活动/停用caller、外层错误与Debug入口按具名完整相关单元新读，逐载荷/行段见readings.jsonl。未声称全部R432或所有其它源物理行本次全文。',
 'proposals_counterevidence':'四原提案完整七组在合同中读取；B001/B002两独立反证全文、DX两editor完整记录、debug/Compiler的两B完整结果读取。B反证阅读ledger全部records/元数据及相关直接caller/block搜索新读。十四具名counter载荷逐字节身份全部核；巨大机械coverage、55 shader或其它领域记录仅身份/导航，不冒称其本次全部语义新读或审查通过。',
 'author':'作者完整报告、四完整七组、22向量及30检查、执行/阅读元数据、106行验证器和读回/读取/命令脚本、原失败/成功日志完整读。46新增载荷本次独立远端全部bytes读回。作者自检不代替本次裁决。',
 'history':'固定原对象恢复并核完整相关7语义记录、7selected关闭记录、唯一activation精确scope；R4/B5三固定原载荷及受影响行/消费者覆盖；历史限定、aliases/tombstones、state、14limits和7policy完整相关对象读取。只具名历史接口范围，不宣称全扫R1–R5全部文件。',
 'dependencies':'当前dependency/file-conflict完整相关R6-U06边/接收表、非阻塞域依赖与7closure门读取；只有R6-I实际写，U09/07/08共享接合尚待实际整合复审。',
 'read_events':len(readings),'json_subtree_events':len(jreadings),
 'ledger_paths':['readings.jsonl','json-readings.jsonl'], 'all_payload_emission_is_not_execution':True,
 'unexecuted_layers':['reference definition','conversion/editor','22 manual vectors','independent behavior model','host','Demo','save','production service']
}
(OUT/'reading-attestation.json').write_text(json.dumps(attestation,ensure_ascii=False,indent=2)+'\n')
execution=json.loads((OUT/'execution.json').read_text())
execution['semantic_review_completed_utc']=NOW
execution['attempt_accounting']=[
 '独立validator第一次exit1：reviewer脚本把绝对报告目录用于git show路径，未执行R；原stderr/exit保留。修正相对路径后第二次26项exit0。',
 '本次后期尝试读取不存在derived-vectors.json发生FileNotFoundError；向量实际已在author-findings.json完整读取，随后rg定位确认。该次stdout/stderr在工具会话保存，独立argv/UTC/exit未另捕获，NOT_CAPTURED，不倒补。',
 '作者旧验证首轮计入新表头、错误origin fetch、core API403及其普通成功后继原日志均保留/读，不能改写成首次全成功。',
 '初期读取/fetch元数据未另捕获保持NOT_CAPTURED，读集ledger从真实捕获开始。请求配置不是实际配置证明。'
]
(OUT/'execution.json').write_text(json.dumps(execution,ensure_ascii=False,indent=2)+'\n')

lines=['# R6-U06-R 独立非作者候选复审', '',
 '**裁决：PASS / CANDIDATE_PASS。四个 required ID 全部支持，最小必要追加修订为无。**', '',
 '本结论只绑定作者冻结提交 `4d92cda068cd7ce027630ab24f05873a50389c93`、workspace tree `58157870fd6e5e277a4afd29816253b980c58cf5`、候选目录 tree `7a2817af930dc0afa6ce0011b4c29d4be32bc9d0`。不等于实际整合后 PASS、正式接受或 CLOSED。', '',
 '本人是直接独立非作者审者 R6-U06-R，未撰写或修改该候选/正式稿。请求 gpt-6.1-sol / ultra / default tier及普速；平台没有有效model/effort/tier/speed/UUID回显，全部 **UNVERIFIED**。用户禁止额外CLI验配置，本任务没有启动CLI或其它审者代审。实际cwd、分支、UTC和真实捕获命令见[execution.json](execution.json)及命令记录；早期未捕获字段不倒补。', '',
 '固定准备基准469a268…的审者提示词完整224129 bytes/SHA b67e8aab…/blob416519b…，合同完整111186 bytes/SHA38ff31ad…/blob5ae84a18…。精确值及三候选身份见[review-findings.json](review-findings.json)。R固定8c5911e…/tree7589c800…；正式基准8ea169fb…/formal tree1046fbb6…保持原字节。', '',
 '| 镜像 | bytes | SHA256 | Git blob |', '| --- | ---: | --- | --- |']
for f in VERIFY['candidate_files']:
    lines.append(f"| {Path(f['formal_path']).name} | {f['bytes']} | `{f['sha256']}` | `{f['git_blob']}` |")
lines += ['', '## 本人实读与证据层', '',
 '先完整读适用AGENTS。完整提示词/合同/四原提案、反证的四项相关完整记录、三镜像全文、固定主稿的完整相同文本与全部旧差异行、WP73-B全文、MapsAndEvents全部1751行及其它必要源/消费者完整单元、历史精确资格与政策/限制已新读。具体方法与边界见[reading-attestation.json](reading-attestation.json)、[readings.jsonl](readings.jsonl)、[json-readings.jsonl](json-readings.jsonl)和[baseline-comparison.json](baseline-comparison.json)。早期截断输出未充作全文，后继补读。14个counter载荷全字节身份通过；巨大机械覆盖、其它领域/shader材料仅身份/导航，不冒称其本次全部语义复审。', '',
 '独立26项文档/身份检查通过，见[verification.json](verification.json)。首次审者路径检查错误exit1与修正后exit0分别保留。作者30项检查是TOOL_VALIDATION；22个案例是人工静态推导，本人逐案回源核验，执行数仍0。作者冻结46新增载荷、620718 bytes均本次独立完整远端读回，见[author-independent-readback.json](author-independent-readback.json)；这证明发布身份而非运行行为。', '']
labels={'identity_and_verdict':'1 身份与裁决','bidirectional_evidence':'2 双向证据','premises_and_counterexample':'3 前提与反证','minimum_revision_contract':'4 最小修订','acceptance_and_regression':'5 验收与回归','independent_adjudication':'6 独立裁定','dependencies_and_receivers':'7 依赖与接收'}
for rec in records:
    id_=rec['id'];d=DETAILS[id_];identity=rec['identity_and_verdict']
    lines += [f"## {id_} · {identity['severity']} · PASS", '', f"**{labels[GROUPS[0]]}。** required；根因 `{id_}`，不新增聚合/consumer facet。完整原提案与root限定共同裁定，支持该冻结候选。", '', f"**{labels[GROUPS[1]]}。**"]
    lines += [''] + ['- '+x for x in d['evidence']] + ['', f"**{labels[GROUPS[2]]}。**", ''] + ['- '+x for x in d['counter']]
    lines += ['',f"**{labels[GROUPS[3]]}。** "+' '.join(d['revision']), '',f"**{labels[GROUPS[4]]}。** "+' '.join(d['acceptance'])+' 精确历史限定及实际受影响行的回归见下节和JSON对应七组；旧PASS不代替本次审读。', '',
      f"**{labels[GROUPS[5]]}。** 本人逐条原提案、反证、固定源和候选核验，支持上述有限范围，无反对或未能裁定的候选语义事项。实际配置UNVERIFIED、未运行层未知；22人工案例不升级为SOURCE_EXECUTION。", '',
      f"**{labels[GROUPS[6]]}。** 主批唯一R6-U06；作者准备无跨批阻塞。必要域接口："+'；'.join(CONTRACT['nonblocking_domain_dependencies'][id_])+'。实际正式接收者/写者仅R6-I；公共同步与整合后门均尚待完成。', '']
lines += ['## 精确历史与共享接合', ''] + ['- '+x for x in COMMON_HISTORY] + ['',
 'WP73-A接收U06；WP75接收U06/U09；本测试目录接收U06/U07/U08/U09。相关冲突边均要求隔离镜像、唯一实际写者和整合后全文非作者复验。不得整文件最后覆盖胜出。实际接收、共享全文PASS、直接/传递接口、实际整合版历史回归、正式接受、CLOSED登记六后继门均为PENDING。Feature Matrix/traceability/audit/planning同步属R6-I，本报告不写公共台账。', '',
 '固定入口记录/root来源线程01a10d94…；作者证据另记指定整合线程01a13a93…。二者作为各自记录保留，本审者没有实际R6-I UUID/接收回执；不替父线程登记整合身份或把记录名称当已运行平台任务。', '',
 '## 运行限制与发布', '',
 '本任务新增R源定义执行、转换器/编辑器执行、向量执行、独立完整行为模型、宿主、Demo、真实save、生产服务均 **0**。Python仅读取/比较/解析文档与Git对象、保存证据、发布读回；没有执行作者/R脚本、未知EXE/DLL/序列化程序或操作Mac。L01–L14具名材料/未知/恢复条件及7独立policy维持；缺完整地图、媒体和宿主不阻塞本次有限静态验收，也不构成UI/像素/音频/持久化或任意插件组合通过。没有新增optional/policy或未来永久缺陷兼容选择。', '',
 '普通提交/推送到审者分支；只写本独立报告目录。有限语义core C先冻结，其后publication P包含C的实际发布与完整载荷读回回执。manifest明确排除自身及尚未知的未来载荷，最终P及其新增载荷读回由外部最终响应绑定，避免递归自哈希。具体C/P/tree由[publication-receipt.json](publication-receipt.json)和最终响应绑定。未合并main、force、删除、移动tag或改作者/正式文件。', '']
(OUT/'review-report.md').write_text('\n'.join(lines))
print(json.dumps({'result':'REPORTS_WRITTEN','records':len(records),'decision':'PASS','utc':NOW},ensure_ascii=False))
