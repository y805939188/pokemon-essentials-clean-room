#!/usr/bin/env python3
"""Render this reviewer's completed manual findings, never mutate candidate files."""
import collections, hashlib, json, pathlib
R=pathlib.Path('/workspace/pokemon-essentials-clean-room')
O=R/'review/r8-disposition-independent-d62b41f-20261017/agents'
B='planning/implementation-routing/r8-20261017/'
M=json.loads((R/(B+'routing-manifest.json')).read_text())
C=json.loads((R/(B+'section-coverage.json')).read_text())
E=json.loads((O/'kernel-full-mechanical-evidence.json').read_text())
FS=[(i,f) for i,f in enumerate(M['features']) if '/generic-kernel/' in f['source']['document']]
V=(R/(B+'views/generic-kernel.md')).read_text().splitlines()

def fid(n):return f'FR-{n:06}'
def case(n,ranges,claim):
 i,f=next((i,f) for i,f in FS if f['feature_id']==fid(n))
 return {'feature_id':fid(n),'source_document':f['source']['document'],'source_lines':ranges,
 'candidate_pointer':f'/features/{i}','candidate_fields':['future_plan','dependencies','decision_refs','current_applicability'],
 'view_line':next(i+1 for i,x in enumerate(V) if x.startswith('| '+fid(n)+' /')),
 'coverage_pointers':['/sections/'+str(i) for i,x in enumerate(C['sections']) if x['path']==f['source']['document'] and fid(n) in x['feature_refs'] and x['mapping_kind']=='behavior-unit'],
 'claim':claim}

findings=[
 {'id':'KF-001','severity':'P3','verdict':'FAIL','requirements':[1,3],
  'title':'纯未验证/责任索引被制造为独立实现功能',
  'cases':[case(392,[[246,256]],'表格只登记组合已知事实、待验证内容和处置责任，未新增一项可实现行为。'),
           case(398,[[313,359]],'L315明确“本表只指派责任，不展开语义”；全部是字段组到责任规格的索引。'),
           case(407,[[286,296]],'交界表将文本/编辑器/事件/资源/身份/候选材料转给各主规格；没有独立实现合同。')],
  'reason':'三行均登记为behavior-unit并分配“框架实现”、通用实现依据和未实现状态；元数据本身被计入66功能分母。待验证不消除该分类错误。',
  'required_action':'保留已登记FR ID的历史导航，按稳定ID合同登记归并/元数据后继关系；将原章节映射为section-metadata，关联真正的配置、schema、编译和领域消费者行。勿直接删号或重新seed。不要将正文附表一律视作治理：WP06统计目录确含初始化、更新和持久化行为，应保留其功能行。'},
 {'id':'KF-002','severity':'P2','verdict':'FAIL','requirements':[3,4,6],
  'title':'日志/控制流与宿主呈现、启动/恢复与持久状态的独立承载边界被合并',
  'cases':[case(435,[[119,139],[140,154]],'整节标MZ；其中异常格式化、日志追加、日志失败前缀、关键段0/1返回与脚本循环收尾是通用诊断/控制合同，窗口/复制/控制台/宿主重启是接入合同。'),
           case(439,[[36,43]],'语言候选/载入/直写存档与启动/载入菜单选择机会合为只含框架的单行；未说明菜单请求/确认和状态提交的双方职责。'),
           case(445,[[99,108],[114,119]],'同一行将持久值装载/选项保留与标题菜单、建地图容器、坐标设置、缺图选图/取消、进入/离开通知和地图恢复全序归给框架，partners仅框架。'),
           case(451,[[219,246]],'有效性/递归备份/保存与删除询问/拒绝退出、场景先置空及条件恢复、缺图选图/取消再次合为框架单行。')],
  'reason':'这些是正文中真实行为和独立验收面，不只是提到下游消费者。通用profile的“消费者按章节交界另列”没有在本行或机器依赖中兑现；错误呈现MZ覆盖也不能代替日志和脚本控制流责任。',
  'required_action':'仅在这些真实跨去向/验收边界处分组或关联既有功能：保留框架的设置、日志、装载与备份状态责任；为菜单、地图、输入取消、场景生命周期与宿主表现登记MZ接入责任和明确交接问题。可复用已有UI/世界功能而不重复制造功能，必要拆分追加新ID并从父line_ranges扣除。无需逐句拆分。'},
 {'id':'KF-003','severity':'P2','verdict':'FAIL','requirements':[3,5,6],
  'title':'随机服务父行吞入战斗记录/回放协作合同',
  'cases':[case(427,[[147,152]],'§5.3实际要求保存战斗初始状态、命令、随机数与换人记录，以及回放按序列消费而不重新随机。该行却仅框架，prototype_refs=[]、feature_refs=[]、WP依赖仅02/03。')],
  'reason':'同一候选已将WP58随机/换人序列FR-000135和回放FR-000136归为框架与Showdown协作；WP06这里既无协作边界也无对这些主功能的引用。来源明确区分普通随机、显式种子和录像序列，不能把三者揉成统一内核服务。没有原型可收尾，但必须留下具体问题。',
  'required_action':'将§5.3作为WP58协作功能的来源元数据/依赖，或按独立验收拆出协作候选；保留一般随机、地牢/彩票种子和有状态选择的框架粗标。补固定Showdown版本/格式、序列消费顺序、遗漏随机调用、回放版本、持久数据/命令和中止/清理责任问题；不要求本次运行业务原型。'},
 {'id':'KF-004','severity':'P3','verdict':'FAIL','requirements':[3,6],
  'title':'依赖字段沿旧WP计划复制，遗漏正文已有的必要调用/状态合同',
  'cases':[case(395,[[75,89],[112,116]],'编译缺失文件门依WP04，名称回退依WP08；实际wp_refs仅WP01。'),
           case(396,[[142,173],[200,242]],'schema类型转换/编译身份拒绝合同依WP04，实际wp_refs仅WP01。'),
           case(401,[[25,55]],'启动插件顺序及失败诊断需WP05/WP07合同，实际仅WP02/03。'),
           case(413,[[115,124]],'错误格式化/日志明确交给WP07，实际仅WP02/03。'),
           case(416,[[31,31]],'strength_push_count明确取WP59§5.3.1严格预检/等待门，实际仅WP02/03。'),
           case(420,[[77,86]],'战斗结果、经验、Mega、失败球事件到持久统计的生产/提交关系未关联战斗结果/捕获主功能，实际仅WP02/03。'),
           case(423,[[122,124]],'持久游戏时间/会话/最近保存时刻明确依保存/旧帧数迁移，实际无WP09/10。'),
           case(425,[[31,52],[60,80]],'游戏时间装载锚点和变量持久化依WP09；变量计时与WP13/WP59交界明确但字段只留WP02/03。'),
           case(426,[[88,95],[101,107]],'通知顺序和移动输入守卫依WP05/WP12及保存统计合同，实际仅WP02/03。'),
           case(428,[[168,171]],'保存/恢复与地牢待播种子直接依WP09/14，实际仅WP02/03。'),
           case(430,[[25,25],[37,38]],'告警文本通过WP08本地化，实际wp_refs仅WP01/03。'),
           case(436,[[161,167]],'编译、插件、紧急保存入口的失败合同来自WP04/05/09/10，实际仅WP01/03。'),
           case(448,[[158,160]],'备份/删除、转换写回转交WP10，实际仅WP03/06。'),
           case(449,[[36,38]],'迁移版本比较器明确依WP05，实际仅WP02/09。')],
  'reason':'66行feature_refs全空，wp_refs整篇恒定；routing.py L128–135只从WP索引继承依赖，L252直接复制。可读视图把这些值展示为“WP依赖”，并未限定它们只是历史规划最小前置。这里不要求列出一切提及的WP，而要求保留真正调用/状态资格与验收前提。',
  'required_action':'保留历史WP计划依赖作为可溯源输入，另对正文真实调用/状态边界登记准确的WP或稳定feature_refs；明确生产者/消费者方向。优先补上述可复现遗漏并重生成视图；勿把所有文本命中自动升级为依赖，也不因通用服务被某领域消费就强制重分类。'},
 {'id':'KF-005','severity':'P3','verdict':'FAIL','requirements':[4,6],
  'title':'旧格式支持范围未接上已有用户决策门',
  'cases':[case(449,[[40,48]],'旧数组到表、当前无17项适配和非空旧表转换是旧格式支持范围。'),
           case(450,[[78,109],[111,215]],'14项旧存档转换及64树果/4敷料旧身份映射为显式旧格式兼容内容。')],
  'reason':'两行target_scope均为待确认，decision_refs只含阶段/一般去向；DEC-SPECIAL-AND-HOST-SCOPE明确包含“XP工程迁移及旧格式支持范围”，却未绑定这些行，questions也没有要求用户决定是否纳入旧格式。阶段待定不能替代旧格式功能范围决定。',
  'required_action':'旧格式适配及其具体转换目录须设待决策并引用现有范围门，写清要决定支持哪些旧数据/版本。通用迁移编排或通用恢复若独立纳入，可保留框架候选但与旧格式支持验收区分；不得据此排除任何行。'},
 {'id':'KF-006','severity':'P3','verdict':'FAIL','requirements':[1,6,8],
  'title':'统计附表被填入不存在的“共享导航/无实现承诺”来源分类',
  'cases':[case(n,[[1,5],[7,143]],'原附表逐字段给初始化、更新规则、持久化及证据等级；没有该共享导航分类声明。') for n in range(415,425)],
  'reason':'/documents/61/source_classification及10行current_applicability/source_classification写成“共享导航、范围或测试设计；无独立实现承诺”。视图L62将其作为来源分类展示，但document_role却为behavior-or-data，下面又有10个实现功能。该值是routing.py L175在缺少“分类：”时采用的后备字串，不是源事实。',
  'required_action':'保留统计附表真实行为及10个章节粗标；将来源分类明确为“源文未单列分类（统计行为/数据附表）”或等价不伪造表述。不要把该文改为纯导航来迎合后备分类；重生成机器/视图并验证事实与计划一致。'}
]

pass_reasons={
388:'配置定义规模、世代基准与默认值作用域可作为框架配置能力粗标，未承诺运行兼容。',
389:'全部主/战斗设置表已读；本行只定位作者配置输入及默认值，领域效果另有主责，框架候选合理。',
390:'默认值派生、设置间联动与直接世代引用区分清楚，可保留章节粗标。',
391:'普通发现/显式路径、备份材料与语言配置的来源边界保留；框架作为配置/数据服务候选可保留，不能把材料存在当支持。',
393:'非法配置、调试设置、资源ID与发现失败未知没有被升级为目标已验证；框架候选合理。',
394:'默认身份、按类查询/回退/副作用和36类清单已读，框架登记/查询候选合理。',
397:'此父节含Nature顺序与14/10/10固定身份目录及未知引用拒绝，确有行为/数据合同，不能仅按“区分”标题降为元数据。',
399:'必选/可选数据装载与候选Shadow材料分开，未将来源可选性转成项目排除。',
400:'默认查询/参数验证/副作用与未知最终呈现保留，框架候选可以保留。',
402:'逐行解析/校验、通用/专用入口和内容依赖均属于作者内容服务，同去向粗标可保留。',
403:'父行已扣除地图事件和动画映射子节；保留写出/缓存/失败前缀的框架数据生命周期粗标合理。',
404:'地图/事件工程转换单列MZ并绑定待用户决策，没有自动排除XP迁移。',
405:'动画映射与播放资源接入单列MZ候选，保留零/有效条目的写入门。',
406:'编译入口的失败/部分状态是框架编排合同，关联子行为而不重复实现其宿主规则。',
408:'编译触发/配置变体的来源默认与目标待验证状态分开，可保留章节粗标。',
409:'完整通知/处理器表及异常部分状态已读；通用扩展合同归框架合理，具体业务消费者没有被重实现。',
410:'本节登记菜单扩展的注册/排序/过滤/分派数据机制，页面具体业务另归界面规格，框架候选合理。',
411:'插件元数据、依赖/冲突/循环、特殊版本比较与终止门可作为框架扩展兼容候选。',
412:'源发现/编译/产物消费三阶段及发布模式边界保留，未声称沿用Ruby架构或目标已支持。',
414:'插件基线/强制触发/真实组合未知未升级验证状态，框架候选可保留。',
424:'派生统计确有查询/副作用行为；不是因为不计入74就应删功能。来源分类错误另列KF-006。',
429:'时间/随机基线及未证组合只是本篇行为配置投影，章节粗标没有额外已验证承诺。',
431:'弃用别名校验、位置/关键字转发及未显式转发块的边界保留，框架兼容能力合理。',
432:'别名失败与兼容不变量均为真实行为约束，可保留粗标而不逐条拆分。',
433:'文件/归档状态、小端协议和资源路径解析是通用I/O合同；未承诺真实归档/宿主等价。',
434:'GET/POST分层及构造/写入异常边界属于框架网络服务候选，历史替身执行未升级为联网通过。',
437:'诊断配置/模式守卫与宿主未知保持事实边界；章节级框架候选可保留。',
438:'31域、规范键/地图共享桶及查找身份为真实文本服务合同，框架候选合理。',
440:'查找/空译/参数及指定图像“身份选择”属于语言服务；实际加载/像素已明确转交资源消费者，不必逐图拆功能。',
441:'完整收集/提取/导入/部分写入状态已读；作者文本数据服务可保留框架粗标，不把静态向量当已执行。',
442:'默认语言候选、加载与作者工作流支持状态分开，未把当前无候选当未来排除。',
443:'缺译/空译/格式化/截断失败合同保持独立，框架候选合理。',
444:'17持久单元、动态重复身份及变量/开关槽读取是框架持久状态合同；原宿主类型仅作来源标识。',
446:'正常保存前缀/校验/覆盖和三类直写路径分开，框架持久化候选合理；恢复UI责任由相关主行纠正。',
447:'设置/进度/版本与默认启动状态没有升级为已实现或已批准首版。',
452:'通用备份/紧急保存/单对象入口的默认与变体可作为框架候选；旧格式具体支持需由449/450范围门裁定。',
453:'备份同路径、转换失败前缀和旧对象缺陷是框架迁移边界，未把参考异常变为目标已批准政策。'
}
results=[]
for i,f in FS:
 refs=[x['id'] for x in findings if any(a['feature_id']==f['feature_id'] for a in x['cases'])]
 if refs:
  reason='；'.join(next(a['claim'] for a in x['cases'] if a['feature_id']==f['feature_id']) for x in findings if x['id'] in refs)
 else:reason=pass_reasons[int(f['feature_id'][3:])]
 results.append({'feature_id':f['feature_id'],'verdict':'FAIL' if refs else 'PASS','reason':reason,'finding_refs':refs,
 'manifest_pointer':f'/features/{i}','source_document':f['source']['document'],'source_heading':f['source']['heading'],
 'source_line_ranges':f['source']['line_ranges'],'fixed_identity_verdict':'PASS',
 'destination_verification':'待验证','implementation':'未实现','acceptance':'未验收'})

requirements=[
 {'number':1,'verdict':'FAIL','scope':'本域13文档/258有效标题机械无漏；纯元数据生成为实现行及统计分类事实错误需修。','finding_refs':['KF-001','KF-006']},
 {'number':2,'verdict':'PASS','scope':'本域66稳定ID唯一；文件、有效锚点、heading/unit SHA、行范围及父子不重叠全核。源/交付/候选/工作树字节一致。','finding_refs':[]},
 {'number':3,'verdict':'FAIL','scope':'同去向粗标一般保留；独立承载/验收边界、纯索引和具体依赖存在问题。','finding_refs':['KF-001','KF-002','KF-003','KF-004']},
 {'number':4,'verdict':'FAIL','scope':'本域无不纳入目标、无Showdown支持冒认；旧格式范围缺具体用户决策门。','finding_refs':['KF-005']},
 {'number':5,'verdict':'FAIL','scope':'四强制原型主功能在其他域，本域不重复裁定；本域录像序列接口遗漏协作与具体问题。','finding_refs':['KF-003']},
 {'number':6,'verdict':'FAIL','scope':'状态/阶段/事实与计划字段结构存在且全待验证/待定/未实现/未验收；来源分类、依赖和边界内容仍不充分。','finding_refs':['KF-002','KF-004','KF-005','KF-006']},
 {'number':7,'verdict':'PASS','scope':'仅文档写集级限定通过：U01/U02/U08/U09无漏绑，整批required_id过绑已明示保守口径；U07未见当前来源受影响证据。后继接受校准仍未做。','finding_refs':[]},
 {'number':8,'verdict':'待查','scope':'本域视图147行全文、66行展示与机器记录及validate/check-generated已核；完整schema/validator负例语义由父团队另审，本代理未完整阅读或执行self-test。来源分类展示错误见KF-006。','finding_refs':['KF-006']},
 {'number':9,'verdict':'PASS','scope':'交付→候选tracked diff全部仅新增routing目录；本代理只写kernel-full-*。不声称审计了所有远端/分支操作历史。','finding_refs':[]}
]
counts=dict(collections.Counter(x['verdict'] for x in results))
data={'schema':'independent-generic-kernel-full-review.v1','task':'/root/kernel_full_review',
 'candidate':E['candidate'],'formal_tree':E['formal_tree'],'source':E['source'],'delivery':E['delivery'],
 'configuration':{'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','Fast':'off','origin':'parent delegation / review-prompt natural-language request'},
 'authoritative_creation_echo':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','Fast':'UNVERIFIED','cloud_task_id':'UNVERIFIED'},
 'effective_execution_echo':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','Fast':'UNVERIFIED'},
 'qualification':'UNVERIFIED; inherited/requested configuration is not telemetry; no default-tier creation parameter was exposed in this subagent context.'},
 'independence':'Non-author full source reader; kernel_batch_check was a separate limited static index cross-check, not another full semantic reader.',
 'counts':{**E['counts'],'feature_verdicts':counts,'unread_source_documents':0,'unread_source_lines':0},
 'reading_ledger':E['reading_ledger'],'view_reading':E['view'],
 'instructions_read':['AGENTS.md',B+'README.md',B+'review-prompt.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/DELIVERY.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/cloud-eighth-update-handoff-prompt.md'],
 'index_reading':'batch-assignment U01/U02/U07/U08/U09 complete objects read; U07 initial output truncation supplemented. Formal README generic-kernel entries searched, fixed Git domain file set independently rebuilt. Full contracts/readsets and full formal README were not reread by this agent; batch obligations cross-checked by static helper indexes, no remediation semantic acceptance claimed.',
 'section_coverage':'258 records structurally parsed and complete per-heading identity/mapping fields read; 83 metadata/175 behavior-unit; full normalized domain records saved.',
 'requirements':requirements,'findings':findings,'features':results,
 'catalog_results':[{'document_id':x['document_id'],'path':x['path'],'verdict':'PASS','reason':'全文表格已读，静态案例保留SOURCE_STATIC/DERIVED_VECTOR/NOT_EXECUTED及历史限定；映射元数据，无新增实现功能。','headings':x['headings']} for x in E['reading_ledger'][11:]],
 'tools':{'mechanical_evidence':'kernel-full-mechanical-evidence.json','actual_io':'kernel-full-audit-tool-io.json','audit_exit':0,'stdout_tool_chunk':'8a28fb','audit_script':'kernel-full-audit.py','domain_snapshot':'kernel-full-domain-records.json','helper':'kernel-full-batch-check.json'},
 'remaining':['父团队完成完整schema/工具/负例语义审查。','修复本域6项finding后绑定新精确commit重核。','无权威执行echo的model/effort/tier/speed/Fast及云task ID继续UNVERIFIED。','Showdown版本/格式与实际原型仍待固定/运行，不以本审查补执行信用。','用户仍须决定旧格式及其他未决范围；上游29项整改和实际ACCEPTED后精确差分校准未执行。'],
 'conclusion':'FAIL_FIXED_CANDIDATE_DOMAIN; full reading complete, 6 actionable findings, no final R8 acceptance or compatibility certification.'}
(O/'kernel-full-results.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

lines=['# Generic Kernel 全文独立复审', '',
 f"固定候选 `{E['candidate']}`；正式子树 `{E['formal_tree']}`。本域结论 **FAIL（需返修）**：66功能行逐项裁定为{counts.get('PASS',0)} PASS、{counts.get('FAIL',0)} FAIL、0待查；这只是固定候选的打标审查，不是R8整改或兼容性最终验收。",'',
 '请求配置为gpt-6.1-sol / ultra / default / normal / Fast off；本子任务没有权威创建或执行echo，model、effort、tier、speed、Fast与真实云task ID逐字段UNVERIFIED。父任务请求、继承配置及角色名称均未当作有效遥测。此资格缺口不因完整阅读消失。','',
 '## 阅读、身份与分母','',
 '完整分块真实阅读11正文（2413行，261089B）及2静态测试目录（524行，89127B）；合计13文档、2937行、350216B，未读0。正文有效标题237，catalog标题21，共258；与section-coverage逐项相符（175 behavior-unit、83 section-metadata）。66行是功能分母，不等于258标题或静态向量数。','',
 'views/generic-kernel.md 1–147全文分三块读完。正文及表格不是只读标题或关键词；同去向子节保留章节粗标。概念父节内真实行为没有按标题盲删；WP03§6含固定身份目录、WP07附页目的/概念里的行为已由正文功能承接。WP06统计目录包含初始化/更新/持久化，保留其功能身份。','',
 '| 文件 | 完整阅读行区间 | 行数 | 标题数 | SHA256 |','| --- | --- | ---: | ---: | --- |']
for x in E['reading_ledger']:
 lines.append('| '+pathlib.Path(x['path']).name+' | '+','.join(f'{a}–{b}' for a,b in x['read_ranges'])+f" | {x['lines']} | {x['headings']} | `{x['sha256']}` |")
lines += ['', '全部13文件已比较固定source、delivery、candidate与当前工作树字节；66行源锚点/heading SHA/unit SHA/范围核对通过，父子选区无交叠。候选文件身份清单全部条目核对通过。可复现脚本、完整I/O及独立分母见kernel-full-audit.py、kernel-full-audit-tool-io.json、kernel-full-mechanical-evidence.json；原读取tool chunk与区间在JSON reading_ledger中。','',
 '已完整读根AGENTS、routing README/review-prompt、R8 DELIVERY、inputs/review-SKILL和中文handoff主入口。clean-document-revision只作为作者约束读取，没有声称它用于本审计报告写作。相关U01/U02/U07/U08/U09批次索引对象完整读，首次U07输出截断已补读。没有重审全部R8合同/历史readsets或原始参考；仅核当前打标与范围绑定，不裁定29项整改行为。','',
 '## 可复现问题','']
for f in findings:
 lines += [f"### {f['id']} / {f['severity']} — {f['title']}",'',f['reason'],'', '| 功能 | 源行（路径见逐功能表/JSON） | 候选JSON pointer | view行 | 证据 |','| --- | --- | --- | ---: | --- |']
 for x in f['cases']:
  lines.append(f"| {x['feature_id']} | "+','.join(f'{a}–{b}' for a,b in x['source_lines'])+f" | `{x['candidate_pointer']}` | {x['view_line']} | {x['claim']} |")
 lines += ['', '**必修动作：** '+f['required_action'],'']
lines += ['## 九项合同在本域的裁定','', '| 项 | 裁定 | 范围与依据 |','| --- | --- | --- |']
for x in requirements:lines.append(f"| {x['number']} | {x['verdict']} | {x['scope']} |")
lines += ['', 'U01绑定WP09/WP10和第二catalog；U02绑定WP04；U08绑定WP08；U09绑定WP03，均保持待整改后核对。WP03整批绑入MG-NAME-CANCEL、WP10整批绑入KER-002的过宽required_ids已由README明确为DOCUMENT_WRITE_SET_CONSERVATIVE，当前不另判缺陷；实际后继须按精确章节/finding差分。U07当前写历史overlay，未见本域源定位消费该overlay，不凭猜测补绑。助手产物kernel-full-batch-check.md/.json仅证明该限定索引核对；它没有替本审者读正文。','',
 '## 逐功能裁定','',
 'PASS表示本候选的对应章节粗标在本次范围内合理；不表示目标已实现、已验收、Showdown兼容或所有上游整改已关闭。FAIL按相关finding修复。每行固定源文件、章节、选区、JSON pointer及finding_refs均在kernel-full-results.json。','',
 '| 功能ID | 来源文件 / 章节 | 裁定 | 理由 / finding |','| --- | --- | --- | --- |']
for x in results:
 lines.append(f"| {x['feature_id']} | {pathlib.Path(x['source_document']).name} / {x['source_heading']} | {x['verdict']} | {x['reason']} "+(','.join(x['finding_refs']) if x['finding_refs'] else '')+' |')
lines += ['', '## 实际工具与限制','',
 '独立静态审计脚本exit 0；作者只读validate与check-generated均exit 0、errors=[]，真实argv/UTC/stdout/stderr/exit在工具I/O文件。机械通过没有抵销上述语义缺陷。未运行self-test（该命令会写作者负例工件），完整schema/验证器及负例人工审查留给父团队，合同8整体在本代理为待查。未运行Ruby、游戏、宿主、框架、业务向量或原型，未开发实现。','',
 '初期两次只读字段探索分别因documents.source使用path而非document/path位置假设抛KeyError（exit 1），随后按实际结构读取并补核；它们未产生PASS信用。首次宽范围文件名检索输出截断没有用于正文阅读结论；正文13文件均用上述无截断分块读完。一次批次总输出在U07被截断，已单独完整补读。','',
 '固定delivery→candidate tracked diff仅新增routing目录文件；本审者及限定助手只写kernel-full-*，没有改作者工件/正式规格/参考/分支或commit。本报告不证明所有远端操作历史。剩余为6项返修、新候选固定SHA重核、配置资格、用户范围决定、Showdown原型和上游实际ACCEPTED后的最终差分校准。']
(O/'kernel-full-report.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'features':len(results),'verdicts':counts,'findings':len(findings),'report':'kernel-full-report.md','results':'kernel-full-results.json'},ensure_ascii=False))
