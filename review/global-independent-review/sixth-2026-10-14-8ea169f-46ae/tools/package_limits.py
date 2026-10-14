"""Explicit refreshed material/host boundaries; historical identities remain separate."""
import hashlib,json,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]; REPO=ROOT.parents[2]
def put(p,x):(ROOT/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
old='f49d870c6fd616ab6736754a218a4553b5acac7f'
prefix='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/'
payloads={}
for name in ['unresolved-decisions.json','limits-and-missing-materials.md']:
    path=prefix+name
    data=subprocess.check_output(['git','show',old+':'+path],cwd=REPO)
    out=ROOT/'evidence'/('historical-'+name);out.write_bytes(data)
    payloads[name]={'repo':str(REPO),'commit':old,'path':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                   'git_blob':subprocess.check_output(['git','rev-parse',old+':'+path],cwd=REPO).decode().strip(),
                   'purpose':'historical recovery index, not new game PASS','r6_snapshot':str(out.relative_to(ROOT))}
pol=json.loads((ROOT/'evidence/historical-unresolved-decisions.json').read_text())
for d in pol['decisions']:
    d['r6_status']='POLICY_NOT_SELECTED_NOT_REQUIRED_UPDATE'
    d['r6_fresh_read_basis']=['tasks/R6-K/reading-ledger.jsonl','tasks/R6-K/forward-source-matrix.jsonl','tasks/R6-H/subtasks/history-r4-r5/']
    d['old_contract_versions_remain_historical']=True
    d['r6_reference_identities']='inventory/reference.json'
    d['r6_current_contract_identities']='inventory/formal131.json'
profile_policy={'id':'GR6-POL-001','classification':'independent_policy','title':'旧宿主数据库剖面的兼容范围',
 'aliases':['R6-B-COMP-SELECT (material/selection boundary, not a mandatory defect ID)'],
 'r6_status':'POLICY_NOT_SELECTED_NOT_REQUIRED_UPDATE','proposer':'R6-I','severity':'not applicable: compatibility scope choice',
 'source':'Game.exe in inventory/reference.json; exact recovered BIN-0079/0080/0081 identities and offsets in evidence/bin-readable/',
 'evidence':['tasks/R6-B/compat-unit-forward.json','tasks/R6-B/compat-field-index.json','tasks/R6-B/semantic-notes.md','tasks/R6-B/report.md'],
 'fact':'三份可读兼容定义本轮完整静态新审，344类/方法与988访问器字段有具名定位；部分地图/事件/音频/动画字段有活动散文件consumer，另外旧数据库定义没有因此变成当前活动游戏合同。实际native选择与动态提供者未知。',
 'inputs_and_controls':'选择一个准确已恢复定义剖面，按其具体字段/构造默认/方法结果分析；三个同名剖面不能拼合成一个默认系统。构造默认与反序列化对象值、散文件覆写与原嵌入定义分开。',
 'decision_required':'未来是否承诺当前可用活动consumer之外的旧宿主数据库/脚本数据兼容剖面，以及支持哪一份有限输入域。',
 'if_preserved':'先选择具名剖面和输入/输出/失败域，按已审事实写架构中立能力或数据合同；不复制RPG类层级、继承或同名API。',
 'if_not_preserved':'明确排除额外旧数据库作者兼容域，保留其定义确实存在和当前活动consumer的必要行为；不得据无默认caller删除源事实。',
 'current_correct_scope':'现行Engine/资源/Compiler/Interpreter/音频/动画的活动consumer合同继续有效；原生实际选择仍为L04/L05，不把三个剖面都说成已运行。',
 'negative_evidence_boundary':'B完整三程序、当前散文件consumer及本轮O/K接合；native全CFG、外部覆写/插件未知，不宣称默认缺名在所有宿主一定报错。',
 'minimum_revision':'本轮报告已展开事实并登记独立兼容政策；不纳入56必修，不要求现在修改formal。',
 'acceptance':'政策日后选择后，逐所选定义事实/消费者及失败前提建立兼容合同与有限向量，宿主选择另作实际观察；不靠类型名/PASS授运行等价。',
 'dependencies':'不阻塞14必修候选批次；仅阻塞未来扩展旧剖面兼容声明。',
 'non_proposer_basis':'原源领域事实由R6-B独立新读；全局政策范围由R6-O独立核对另存policy-profile-counter。',
 'execution_status':'SOURCE_STATIC; original embedded program/native selector NOT_EXECUTED',
 'required_in_update':False,'user_input_needed_now':False,'historical_relation':'R6 new finite legacy profile policy; original six BAG/UTIL policies retain exact IDs and original denominator'}
put('findings/policy-records.json',{'schema':'r6.policy.v1','count':7,'historical_policies':6,'new_policies':1,'records':pol['decisions']+[profile_policy],
 'general_compatibility_boundary':pol['general_compatibility_boundary'],
 'new_required_documentary_facts_do_not_select_defect_compatibility':True,'update_started':False,
 'source_payload_identity':payloads['unresolved-decisions.json']})
rows=[
('L01','地图和完整工程','所有具名地图/解释器/编译/设施/作者脚本及PBS当前新读；源能力和实际事件接线分别登记。','R仍无完整地图、CommonEvents、System、Tilesets、Game.ini/Game.rxproj及完整项目资源；真实NPC/道馆/发奖/完整Demo可达未观察。','取得有来源/commit/bytes身份的完整工程，并准备隔离兼容宿主和所需资源。',['tasks/R6-O/report.md','tasks/R6-DX/report.md','tasks/R6-F/report.md']),
('L02','图形和音频','两BMP均8×8×24bit，各64像素，共128；字体/SF2及全部可得资源选择/坐标/尺寸请求已新查。','无完整Graphics/Audio；实际资源加载、动画帧、量化坐标、混音/叫声/听感未知。历史“64像素”不得理解为两文件合计64。','提供准确资源及目标图形/音频宿主；源请求与宿主观察分别记。',['tasks/R6-D/report.md','tasks/R6-O/report.md']),
('L03','原生执行','本机Ruby2.6.10、Python3.14、Node22.21.1及静态工具重核；只用现有工具与受控替身，无安装或安全配置变化。','兼容Windows/RGSS/mkxp和.NET宿主本轮未建立；Mac隔离Ruby不证明随附Ruby3.1游戏运行。','可用授权宿主、资源、受控输入/输出和隔离方案。',['evidence/commands','tasks/R6-O/execution-log.json']),
('L04','Game和运行库','五PE结构、接口/资源、Game可读程序及controller1666记录790模式、原生字符串分类均有新类型/结构和具名语义证据；非aux COFF字段与可读程序/其它字串分别处置。','全机器码CFG与原生版本/后端/分派选择未建立；导入导出/定义名字不证明实际功能。非程序原生元串的inventory_only范围不冒称游戏语义审读。','具名有限机器码/版本问题需目标宿主或可安全恢复证据；无需无界逆向全部机器码。',['tasks/R6-B/report.md','tasks/R6-B/residual-candidate-dispositions.json','evidence/tool-evidence-qualifiers.json']),
('L05','可读内嵌程序','55shader逐全文/函数/字段新审；3兼容脚本完整事实与caller；四孤立旧提取副本以逐字身份别名处置。','GPU编译、采样、精度、实际接线和像素颜色未知；不要求未来复用宿主/GPU/Ruby类层级。','目标GPU/宿主、完整素材和已绑定程序选择链。',['evidence/shader-reading.json','tasks/R6-B/report.md']),
('L06','animmaker','15可读IL方法、743指令/1670bytes/11EH全部有限结构和控制/失败前缀新审；外部依赖分界明确。','图像/XML库空矩形/编码/错误格式化/文件失败及实际输出未运行；≤96文档不是验证门，扩展名不保证PNG，失败不保证回滚。','可用.NET兼容宿主及准确依赖库、受控输入/输出目录。',['tasks/R6-B/animmaker-method-forward.json','tasks/R6-B/animmaker-interface-structure.json']),
('L07','extendtext','1740bytes有限工作循环、17导入、四窗口/子控件请求、互斥量及150ms请求新审。','Windows API真实返回、实际尺寸、精确周期、目标进程所有权、自动启动和运行库启动余部未知。','Windows兼容隔离目标窗口与真实API观察；不将未检查返回当成功。',['tasks/R6-B/extendtext-forward.json','tasks/R6-B/extendtext-PE.json']),
('L08','字体','8字体104表/2326glyph、全部字符映射、度量、轮廓/60954简单点结构、消费者档位与回退新查。','Font.exist/字宽/hinting、字节码执行和真实UI视觉未知；资源轮廓解析不替渲染。','准确目标字体宿主、显示输入和字形/尺寸观察。',['tasks/R6-D/fonts/report.md','tasks/R6-D/report.md']),
('L09','soundfont','完整RIFF/hydra九表25786记录含sentinel；236预设240乐器505样本、1524链接2000710采样点，106空选择/42标称范围观察/2非零ignored terminal及配置选择新核且独立复算。','原生接受/异常guard处理、合成及声音未知；不把结构完整解析称格式全部合规或采样器等价。','目标音频宿主和受控SF2加载/合成/观察。',['evidence/resource-parser/soundfont-full-audit.json','tasks/R6-H/subtasks/supplement-inventory/resource-countercheck.json']),
('L10','序列化','安全惰性解码唯一Main49行、两根183行脚本中181行同字节prelude与方向差异、49Main关联；messages全部10697key/body与文本结构新比。','解码不执行对象、不启动原生载入；本轮不审全部翻译语言质量。','原生隔离loader及准确语言材料；质量审校为另一具体范围。',['tasks/R6-D/localization/report.md','tasks/R6-B/loader-identity.json','tasks/R6-B/script-identity.json']),
('L11','动态扩展和配置','固定入口、注册/覆写/消费者、默认及Gen5–8备选PBS与无默认caller定义有本轮具名有限合同。','任意插件/表达式/外部覆写、无界输入、配置全部笛卡尔组合及调度未穷尽。','新增具名插件/配置/事件材料与输入域可恢复相应有限范围。',['tasks/R6-D/report.md','tasks/R6-K/report.md','tasks/R6-CA/report.md']),
('L12','外部状态和服务','文件/网络/档案/保存可读分支、取消异常和部分提交静态新读；有限隔离源执行各保真。','真实网络/生产账号/外部服务、真实用户保存往返和打包档案未验证；exit0或空串不能证明业务成功。','明确授权的隔离替代服务/存档/档案及真实输入输出；不使用生产状态。',['tasks/R6-K/report.md','tasks/R6-F/validation-notes.md','tasks/R6-O/execution-boundary-counter/']),
('L13','纯元资料','432/131/38093完整身份与用途处置；116补充路径中111superseded secondary、5独立保留按用途；发布6和activation6完整读，历史资格投影及生成结构分开。','许可不作法律或游戏规则结论；历史hash/PASS和生成导航不授当前行为批准；非当前语义的inventory_only有精确理由。','若新增材料被指定为当前primary，重新纳入明确读集；不靠旧scope扩大game分母。',['tasks/R6-H/report.md','tasks/R6-H/subtasks/supplement-inventory/effective-supplement116.json']),
('L14','执行与工具元数据缺口','确有早期原源/替身输出、后续反证与新阅读；缺字段原样保留，不补造起止或Ruby真实exit。部分root工具/行政读取最初只在平台工具回显中保存，关键最终校验另用capture保留真实完整分离输出。','K早期bag/owner通过tee得到的0不等于底层Rubyexit；部分Fishing早期UTC、初始读取单独日志未捕获；部分root工具早先的独立stdout/stderr/UTC记录没有本地另存，不能把后继capture校验充当原命令记录。后续新读不重写历史metadata。','若需相同范围新执行，理解对象/依赖后受控重跑并保存完整UTC/stdout/stderr/底层exit；新执行另计，原缺口仍在。',['tasks/R6-K/report.md','tasks/R6-O/execution-log.json','tasks/R6-O/execution-boundary-counter/','evidence/commands/'])]
records=[{'id':id,'classification':'limit','title':title,'r6_available_and_reviewed':have,
 'unknown_scope':unknown,'recovery_conditions':recovery,'evidence':evidence,'required_update':False,
 'historical_relation':'new execution provenance limit' if id=='L14' else 'same historical L01–L13 ID, evidence refreshed; not inherited reading PASS',
 'state':'FINITE_STATIC_SCOPE_REVIEWED_RUNTIME_OR_METADATA_UNKNOWN','new_reference_execution_implied':False} for id,title,have,unknown,recovery,evidence in rows]
put('findings/limit-records.json',{'schema':'r6.limits.v1','count':len(records),'records':records,'historical_payload':payloads['limits-and-missing-materials.md'],
 'procedural_incident_separate':'control/write-boundary-incident.json','limits_are_not_unread_dispositions':True,'update_started':False})
text=['# 第六轮材料、运行和元数据边界','', 'L01–L13沿历史恢复索引重新核材料，L14新增早期元数据限制。可得文本/有限可读程序的阅读不能被这些运行限制豁免。', '']
for d in records:
 text+=['## '+d['id']+' '+d['title'],'',d['r6_available_and_reviewed'],'',d['unknown_scope'],'','恢复条件：'+d['recovery_conditions'],'']
text+=['## 实际写边界事件','', 'INC-R6-001：UI/Party子任务遗漏cwd，曾在仓库根瞬时创建两个新untracked审计文件，后移入自己的任务目录。当前原位置不存在；未发现正式/R/旧报告/原62变化。这是实际流程违规，不能宣称全队始终守住仅写审查根。原日志、移动与纠正完整保留；不构成新游戏整改ID。','', '所有完整宿主/Demo、真实画面/音频/物理输入、真实保存/生产网络及完整独立玩法模型执行均未开始。有限源隔离、算术工具和旧R4/R5执行分期另列。UPDATE_NOT_STARTED。','']
(ROOT/'limits-and-missing-materials.md').write_text('\n'.join(text))
print(json.dumps({'limits':14,'policies':7,'historical_policy_count':6,'new_policy_count':1,'incident_separate':1}))
