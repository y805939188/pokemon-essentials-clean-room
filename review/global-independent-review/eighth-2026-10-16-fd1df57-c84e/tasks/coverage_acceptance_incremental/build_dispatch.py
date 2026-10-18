"""Freeze exact follow-up reception inputs, without dispatching any context."""
import datetime
import hashlib
import json
from pathlib import Path

B = Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e')
O = B/'tasks/coverage_acceptance_incremental'
D = O/'dispatch'; D.mkdir(exist_ok=True)
S = json.loads((B/'delegation/readsets/coverage-incremental-v2.json').read_text())['snapshot_entries']
C = json.loads((O/'file-coverage.json').read_text())
A = json.loads((O/'atomic-and-interface-denominator.json').read_text())
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def ident(path):
    raw=path.read_bytes()
    return {'path':str(path.relative_to(B)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}

def payload(index):
    return json.loads((B/S[index]['snapshot']).read_text())

common = '''先完整读取本prompt、本任务readset、inputs/eighth-global-review-prompt.md全部36653B（SHA63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b）、项目AGENTS及inputs/review-SKILL全文；摘要、脚本、locator、同blob或旧PASS不能代读。

固定项目/workspace/pokemon-essentials-clean-room，报告根review/global-independent-review/eighth-2026-10-16-fd1df57-c84e；B8 fd1df570cad987dc3852a3b958f03916e317f7fe/workspace tree751dfde81048c81390f89a65ca1d1a565ba8e1ca/formal treef292698cdd4a8e725525a9be6dc34b75faaf151e；R /workspace/pokemon-essentials，commit8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。输入snapshot固定于本地普通commitcab9deade98ff3038f4d8002531958fd74bd5fbd，workspace tree4bee3e4983fc90ee8ad40bc6557af6c5dbdd1188。root已报告完整远端回读，RRtree1c71c4e0c112c2e62cbc426c98b3775b03e37b7b，3692files345072665B、47gzip597667564原B，receipt publication/r8-world-decisions-audit-inputs-readback-11.json；不把root传输核验算本人语义阅读。

本任务是新的实际非原作者原子/消费者接收者。请求gpt-6.1-sol/ultra/default普速/Fast off；实际未回显字段逐一UNVERIFIED。仅root真实创建才增加context，计划/角色/续turn不增加独立性。无权自行spawn/install/commit/push，禁止修改R、formal、planning/audit、旧报告、原快照、其它任务或公共台账；不得运行目标/恢复程序。静态helper先全文读懂，只复制到自己新的隔离输出并保留命令、真实stdout/stderr、UTC、底层exit及失败；读取/解码/脚本union不授语义。

逐primary正式文件全文读完，再逐实际章节/段落/表格/脚注/附录/向量拆尽所有行为子断言与前提；heading/layout/行政逐精确用途处置，带规则字段不能仅因所在索引就豁免。旧locator只导航，不是原子单位。为每个新子断言给稳定子ID、准确sourcefact/源完整单元、producer/write/consumer/display/persist/reload链、正常/取消/异常/失败/部分提交、primary合同及实际接收者。源没有默认caller仍须审定义并给有限负证据，不能自动移出分母。每个有界受收事实须实际读取其完整内容和共同前提，绑定原实际reader；不把对方FULL_READ改成本人FULL_READ，不把同bytes路径关联当独立第二次实读或第二票。源码只能作审计证据，不复制进新规格，不按Ruby架构转译。

readset的R432/F131完整身份库只供精确定位和动态扩读，不要求为了元数据重复全部全文；primary及每个实际采用的sourcefact、完整clause和全部必要消费者必须亲自实读或按真实具名完整贡献接收并核其具体意义。input_artifacts明确原路径/capturedUTC/SHA/snapshot；读取固定snapshot，晚到delta须另冻结身份/完整接收，不倒填旧snapshot。consumer路径清单是开放发现集：不得凭现有列举声称所有动态/传递消费者穷尽。

报告每个旧locator的全部真实子断言已分解/未分解、事实支持/冲突、premise已核/未核、每个实际consumer的received/open；不要以一句“域未完成”替代精确未接收ID/路径/行/结构，也不要用源全文或方法清单签整篇formal。读全后仍有依赖未接收，就保留相应OPEN且交可直接继续的合同；可得未读/未审/未接收不叫hostlimit。独立反证仅对本人不是提出者的实际发现有效；若新发现需交完整原提案与独立审者，不自行最终required分类或全局PASS。保留root当前有限裁决与旧92/56/27的原输入范围，不能继承旧PASS免审，也不无证据重开旧账。

交review.md、progress.json、input-identities.json、reading-ledger.json、manual-atomic-clauses.json、sourcefact-consumer-receptions.json、old-locator-disposition.json、interfaces.json、coverage-gaps.json、next-dispatch.json以及真实I/O/执行账。所有primary路径、旧locator和采用sourcefact恰有明确处置；复合子断言及实际接口分母人工冻结/未冻结分列，禁止方法/行/分号填总数。每60秒向root报已实读路径/原子/consumer及真实pending。业务均NOT_EXECUTED，UPDATE_NOT_STARTED；仅当完整实际接收时可签自己的有限贡献，不能自签全局PASS。
'''

definitions=[
    ('kernel_atomic_reception','KERNEL全部原子与消费者独立接收',151,'clauses',153,'rows',
     [151,152,153,155,156,157,158,159,160,162,163,164,166,167,168,169,171,172,173,174,177,178,179,191,192,193,194,195,197,199,204,208,211,212,213,214],
     '''完整primary为旧矩阵中精确13个formal。源起点为kernel read-set.v1的77R定义与73PBS，追加consumer-census全部714词法候选（含注释/无关须逐具名处置）和实际动态/传递消费者。所有135原fact必须逐实义重收，135个相同generic premise不是支持；2219旧locator全部pending、771无local link，需人工拆子断言并逐个接完，不能把135fact或1504机械结构当最终分母。

重点包括WP02配置/默认备份/发现/注册/重载与实际运行消费，WP03身份/schema和复制/缓存，WP04导出嵌套参数及作者输入→输出→装载，WP05覆写/事件/插件/失败前缀，WP06全部设置/统计/时钟/随机/步数consumer，WP07文件/HTTP/弃用无默认caller，WP08全部message键/body和Intl消费者，WP09/10保存注册/删档前缀/空boot/17值校验/备份退出/迁移。KER-C0199/WP02:250不能用一个指针同时批准默认/备份发现与兼容边界；KER-F049不能从导出改写外推出缓存及后继消费者已接收。

PBS-world18、PBS-battle21、PBS设施7、CRE-B物品的字段/视图/raw/同bytes及各load前提按实际贡献接收，剩余物种/backup等源仍可得，不能把source0未读误写全部73已接。CORE/Move/AI/UI/WORLD/Developer真实采用者的每个相关输入、单位/时间/容量/身份/门/写点/失败prefix均具名，若当前17保留主任务未交，应直接读现存source/formal完成可判定部分并对未收精确范围OPEN；任务未启动不是材料缺失。'''),
    ('core_atomic_reception','COM-CORE全部复合条款与消费者独立接收',86,'rows',91,'facts',
     [86,87,88,89,90,91,29,30,31,33,34,35,36,37,38,40,41,43,44,46,47,48,49,51,52,55,56,57,59,60,61,62,63,64,65,66,68,70,71,72,73,74,75,77,78,79,80,85,105,106,107,108,109,110,111,113,114,115,118,119,123,128,160,162,163,164,166,167,168,169,215,216,218,219,221,222,223],
     '''完整primary为WP39/40/41/42/45及整篇对应catalog六formal；原16R5572行完整源贡献保留原实际reader，但本人须独立核事实/完整单元/实际消费者。全部63fact和994旧locator都纳入；994只是定位与2328分号候选，不是语义原子。165无fact link不能跳过，现有共同premise需要替换为各真实输入/分支/失败prefix。

特别先拆CORE-C0113/WP39:204的延迟攻击来源在/离场、蛋门、能力/物品/招式排除、关系清理与读取来源；C0117/:208的能力入口、raw字段、副本/持久写入；C0122/:216的濒死顺序、阵营/拥有者门、形态离场、能力/天气后继。全部目录向量逐完整输入、普通/边界/失败/取消/部分提交和源支持接收，catalog整篇读不等于逐vector PASS。

完整接入COM-BATTLER十源定义与全部状态/能力/物品/使用招式caller，Move父/实际子审事实与阶段114、Ability/Item80家族463配对、AI有限评价与实际执行差异、Facility各截获/恢复与普通终局、UI呈现/命令/返回、CRE个体写穿/成长/捕获存储/伙伴还原。源文件已由Move等全文不等于COM-BATTLER整个formal已验；后继primary仍独立。MagicRoom的pbPriority(true)是缓存查询而非自身重新算速度；入场按每成员先物品再能力、首真即停，不能错误两轮全扫描。新有界事实不能自动把994所有旧条款转PASS。

root已裁COM001以及拆出的COM002 ZERO_ABLE/COM003 MIXED_ORDER和CRE001的正确受限scope须保留；原报告早期required0只是当时状态。完整root限缩/非提出者反证另冻结实际读，不用早期报告推翻后继有限裁决；不重复同root立新mandatory。'''),
    ('creature_a_atomic_reception','CRE-A全部复合条款及实际消费者独立接收',129,'rows',123,'facts',
     [105,106,107,108,109,110,111,113,114,115,116,118,119,120,121,122,123,124,125,126,127,128,129,130,86,89,90,91,29,31,34,36,37,38,41,43,44,47,59,60,61,64,68,70,71,72,73,74,75,77,78,79,80,85,160,163,164,166,168,169,171,172,174,177,178,179,191,193,194,195,197,199,215,216,218,219,221,222,223,225,227,228,229,231,232,233],
     '''CRE-A唯一primary为原A子片7formal/11R（readset精确primary列表）；必须全文读primary、所有共享catalog完整上下文，并收全部102原fact。旧1430locator覆盖9个formal路径：7primary加旧已读WP23/共享pokemon catalog的局部定位；后两者为dependency整篇上下文阅读和精确locator接收，不转移CRE-C/D/E主责，不从少数locator签整个Shadow/其它域。

1430均PENDING_MANUAL_DECOMPOSITION/NOT_ACCEPTED_FROM_INDEXING，1307无local fact link；102fact有100个consumer空，逐一补真实消费者，或给“有限定义无默认caller”的精确负证据和不扩大范围理由。WP18:107只读标识/设置入口、:111 IV/EV容器、:112计算能力不变量必须拆成真实子断言。F060/F061复制容器与共享引用需追后续突变、重新计算、写穿、缓存和存档/重载，不能从copy一词推深复制。

覆盖个体/物种查询、身份/Owner、HP/PP/持物/状态、属性计算/派生/缓存、玩家/训练家/伙伴、队伍/盒子与图鉴，逐取得/捕获/赠送/交换→所有权/队伍盒子→图鉴/命名/UI→保存重载真实链。完整Party/Summary/Pokedex/Storage屏与场景、Battler写穿/离场/奖励、默认/备份species/forms/metrics/trainer/PBS、保存注册、event真实receiver全部具名。CRE-B/Move/AI/UI的有限收到事实只限完整精确ID与premise，不继承全域PASS。原9条CORE→CRE有限回执保留，CatchStore/Battler等未收到尾项不能改0。

GR8-CRE001有限受限255模板转普通EV工具与默认internalBattle=false阻断都保持；不扩到默认设施物品/Shadow/净化，不重复立案。C/D/E仍由parent17计划独立主责；如果读取其source作为A的必要消费者，按dependency记真范围，不冒那些整域独立完成。''')]

dispatch=[]
subshards=json.loads((B/'tasks/creature_review/subshards.json').read_text())
slice_a=next(x for x in subshards['slices'] if x['id']=='A')
for name,title,reverse_idx,reverse_key,fact_idx,fact_key,support_indices,specific in definitions:
    matrix_path=S[reverse_idx]['original_path']
    locators=[row for row in A['old_locator_rows'] if row['matrix']==matrix_path]
    formal_paths=sorted({row['path'] for row in locators})
    if name=='creature_a_atomic_reception':
        primary_formal=[row['path'] for row in slice_a['formal_primary']]
        primary_reference=[row['path'] for row in slice_a['reference_primary']]
    elif name=='kernel_atomic_reception':
        primary_formal=formal_paths
        primary_reference=[row['path'] for row in payload(155)['items'] if row['repo']=='/workspace/pokemon-essentials' and not row['path'].startswith('PBS/')]
    else:
        primary_formal=formal_paths
        primary_reference=sorted({row['path'] for row in payload(89)['full_read'] if row['repo']=='/workspace/pokemon-essentials'})
    facts=payload(fact_idx)[fact_key]
    readset={'schema':'gr8-exact-atomic-reception-followup/v1','frozen_utc':NOW,'task':name,
             'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default normal','Fast':'off'},'actual':'UNVERIFIED',
             'B8':'fd1df570cad987dc3852a3b958f03916e317f7fe','R':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
             'exclusive_write_set':'tasks/'+name+'/',
             'primary_formal_paths':primary_formal,'primary_reference_start_paths':primary_reference,
             'full_formal_context_paths_for_old_locators':formal_paths,
             'all_fixed_R432_F131_identity_library':[{k:v for k,v in row.items() if k in ('repo','path','bytes','sha256','git_blob','lines')} for row in C['files']],
             'all_old_locators_exact':locators,'old_locator_count':len(locators),
             'fact_count':len(facts),'full_original_source_fact_records':facts,
             'source_fact_snapshot_identity':S[fact_idx],
             'input_artifacts':[S[index] for index in sorted(set(support_indices))],
             'full_incremental_snapshot_master_identity':ident(B/'delegation/readsets/coverage-incremental-v2.json'),
             'support_policy':'Every actual adopted record/premise/consumer must be read in full meaningful context; broad corpus identity library and sourceFULL_READ claims do not grant ownread or acceptance.',
             'late_delta_policy':'Root-reported laterWRR/World/UI003/Ruby-zlibYARB/worldcatalog outputs not incorporated here; freeze exact identities and receive actual full relevant contents before use.',
             'not_started_by_generator':True,'update_started':False}
    rs=D/(name+'.readset.json');rs.write_text(json.dumps(readset,ensure_ascii=False,indent=2)+'\n')
    prompt='# '+title+'完整独立委派合同\n\n'+common+'\n## 本片全部精确范围\n\n'+specific+'\n\n本任务固定readset：`tasks/coverage_acceptance_incremental/dispatch/'+name+'.readset.json`。全部'+str(len(locators))+'旧locator及'+str(len(facts))+'完整原fact已经内嵌，原snapshot身份同时保留。唯一写集`tasks/'+name+'/`。这是新独立语义接收任务，不是原作者续turn；root必须实际创建后记录canonical入口与真实状态。\n'
    md=D/(name+'.md');md.write_text(prompt)
    dispatch.append({'id':name,'prompt':ident(md),'readset':ident(rs),'exclusive_write_set':'tasks/'+name+'/',
                     'primary_formal_files':len(primary_formal),'primary_reference_start_files':len(primary_reference),
                     'old_locator_scope_formal_paths':len(formal_paths),'old_locators':len(locators),'source_facts':len(facts),
                     'state':'READY_TO_ASSIGN_BY_ROOT_NOT_STARTED_BY_THIS_AUDITOR'})
nd=json.loads((O/'next-dispatch.json').read_text());nd['ready_atomic_reception_dispatch_contracts']=dispatch
(O/'next-dispatch.json').write_text(json.dumps(nd,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dispatch,ensure_ascii=False,indent=2))
