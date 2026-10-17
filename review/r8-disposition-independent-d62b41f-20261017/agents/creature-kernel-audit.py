#!/usr/bin/env python3
"""Independent document-only evidence collection; manual semantic verdicts below."""
import collections
import hashlib
import json
import pathlib
import re
import subprocess
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).resolve().parent
CANDIDATE = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
BASE = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
DELIVERY = '4575e80d041ab0c74a42e2e36399d05791dbaa5b'
PREFIX = 'planning/implementation-routing/r8-20261017/'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def sha(b):
    return hashlib.sha256(b).hexdigest()

def load(path):
    return json.loads(git('show', CANDIDATE + ':' + path))

def scan(b):
    """Parse ATX headers outside fenced code, preserving actual occurrences."""
    lines=b.decode().splitlines(keepends=True)
    headers=[]
    seen=collections.Counter()
    fence=None
    for no,line in enumerate(lines,1):
        stripped=line.lstrip(' ')
        if len(line)-len(stripped)<=3:
            match=re.match(r'(`{3,}|~{3,})(.*)',stripped)
            if match:
                ch=match[1][0]
                if fence is None:
                    fence=(ch,len(match[1]))
                elif ch==fence[0] and len(match[1])>=fence[1] and not match[2].strip():
                    fence=None
                continue
        if fence: continue
        match=re.match(r'^(#{1,6})[\t ]+(.+?)\s*$',line)
        if not match: continue
        title=re.sub(r'\s+#+\s*$','',match[2])
        raw=re.sub(r'<[^>]*>','',title)
        raw=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',raw).lower()
        raw=''.join(c for c in raw if c in ' -_' or unicodedata.category(c)[0] in 'LN')
        slug=raw.replace(' ','-')
        anchor=slug + ('-' + str(seen[slug]) if seen[slug] else '')
        seen[slug]+=1
        headers.append({'line_start':no,'level':len(match[1]),'title':title,'anchor':anchor,'heading_sha256':sha(line.encode())})
    for i,h in enumerate(headers):
        h['line_end']=next((n['line_start']-1 for n in headers[i+1:] if n['level']<=h['level']),len(lines))
    return lines,headers

# These explanations were written after the reviewer read every line of the
# corresponding source document in model-visible tool output. They are not
# inferred by this script from the document name or keywords.
REASONS = {
137:'物种/个体身份、内容字段责任与形态提交是框架领域合同；战斗只在此登记读取守卫。',
138:'创建、额外随机、缓存与NPC确定性覆盖属于持久个体生成；捕获/战斗消费者在表内明确引用其它主规格。',
139:'同身份复制、深浅共享及缓存保留由框架维护，未混入战斗执行。',
140:'Owner四字段、构造例外及变更入口是框架身份状态；宿主语言输入与UI语言已区分。',
141:'来源记录、外来查询、昵称与纯毫米辅助由框架承接；辅助的未知用途未被排除。',
142:'归纳身份、来源、形态提交与复制不变量，不需逐条再分功能。',
143:'个体字段/创建/复制的失败边界归框架，保持异常事实待政策决定。',
144:'创建来源与命名配置是领域配置，不把参数值当首版批准。',
145:'HP字段钳制、治疗/蛋守卫及调用者目录由框架持久个体负责；具体战斗施加未在此重定义。',
146:'状态字段与计数存储、守卫及写入者目录主要是持久层；战斗施加/计数递减明确归WP44。',
147:'FAIL：§5.5定义战斗包装/专门PP同步/变身不写回/战中学招同步，不只是消费者目录；框架独责掩盖双向状态交界。',
148:'FAIL：§6.4定义可更新还原记录、永久/临时移除、捕获入队/送箱和伙伴身份错配；应单列协作职责及原型问题。',
149:'持久不变量归框架合理；第8条战斗写穿应在修订后关联新协作子行，本条无需逐句编号。',
150:'字段失败及还原边界汇总可由框架维护；具体还原协作缺口归FR-000148。',
151:'治疗/重学/捕获配置的消费者索引可保留框架粗标。',
152:'FAIL：§3.2–3.3含玩家外观刷新、宿主用户名建议名和命名输入；仅框架且无MZ协作，未说明宿主边界。',
153:'FAIL：§4.4战斗内奖励/败北扣款、战斗守卫和两阶段统计/提示不属于单纯资源字段；需协作边界。',
154:'FAIL：§5.3调试交互新建、确认/成员录入及写回是独立作者工具范围，清单未关联特殊/工具待用户决策，也无UI职责。',
155:'音频逻辑请求及引子记忆交付宿主，MZ+框架方向合理；但依赖漏WP15/WP16等，见CK-DEP-001。',
156:'注册/注销的领域写入及野外消费者目录可由框架编排；参与和战后已拆到两个协作子行。',
157:'参与谓词与合并战斗队伍跨持久伙伴/战斗席位，协作粗标合理；依赖漏WP39。',
158:'战斗内成员与战后两分支治疗跨双方，协作粗标合理；不得理解成已验证。',
159:'领域/伙伴不变量汇总可由框架持有，具体协作执行已单列。',
160:'身份/资源/装载/注册失败汇总归框架；未知许可写入者保留待证。',
161:'资源及身份配置由框架维护，伙伴+特殊战斗组合仍待验证。',
162:'容量、寻址、地区容器与领域直写归框架；墙纸已拆。',
163:'墙纸显示读取可写背景，MZ+框架两方合理且不能当纯图片资源。',
164:'领域复制/移动/删除/接收是集合操作；UI4.2已排除出本行。',
165:'UI拿起/放下/交换/释放与PC菜单守卫需要MZ，标框架协作合理。',
166:'FAIL：§5表格横跨领域守卫和明确的UI入口/目标/持有条件，当前只框架，且未关联已拆UI行。',
167:'存入治疗/身份来源/持有物引用与迁移边界由框架集合层承接。',
168:'集合不变量归框架可接受；UI释放/交换归纳应沿FR-000165而非重新造行为。',
169:'领域与UI失败汇总以框架为主可接受，详细UI主行已存在。',
170:'集合配置/墙纸目录规模由框架提供、MZ消费，无新增独立行为。',
171:'FAIL：§3.3命名输入、消息等待地图更新/容量复检与静默入口混在同一框架行，未声明MZ协作或拆分。',
172:'FAIL：§4.2演出/图鉴/进化在最后替换前依次提交，§4.3选择器取消写事件变量，不能只按框架交换存储粗标。',
173:'消费者交界目录主要是指向WP38/WP53/WP64等的关系索引，框架编排合理；不是捕获判定本体。',
174:'获得/替换写入不变量归框架合理，UI主行缺口归171/172。',
175:'容量复检、外层返回与部分提交由框架编排；需保留等待时点而非承诺事务。',
176:'赠送/交换来源配置归框架；不证明实际事件可达。',
177:'背包查询/部分添加删除/预检/排序属于框架容器。',
178:'FAIL：§4.2–4.4包含数量输入、背包与PC提示先后、动态菜单、过滤选择及事件变量/刷新接入，当前只框架。',
179:'FAIL：§5含地图按键打开两列快捷菜单、确认/临时退出菜单/失败回菜单，不能由框架登记列表责任覆盖。',
180:'容器/登记不变量由框架维护合理；UI消费细分缺口归178/179。',
181:'容量/部分失败及接收包装差异由框架负责，明确false不等于回滚。',
182:'容器与初始PC配置由框架维护；显示规则缺口另见CK-META-001。',
183:'FAIL：父行剩余§3.2背包和§3.4队伍选择/数量/教学取消仍仅框架，战斗与野外已拆但场外UI未分工。',
184:'野外确认、地图操作与背包扣减是MZ+框架交界，方向合理。',
185:'探测仪事件搜索、方向/等待/消息与计数顺序属于MZ接入并有框架合作，方向合理。',
186:'登记扣物、复检/退款和球独立动作链跨双方；关联战斗道具原型正确。',
187:'退款残留身份与同轮终局/下轮命令/失能对照不是数值问题，协作+原型合理。',
188:'注册家族覆盖目录是规则能力目录；实际战斗/野外主行已另列，可框架承接。',
189:'剩余培养、机器/形态/融合持久效果由框架承接合理；嵌套UI重入应明示MZ责任。',
190:'场外与战斗治疗的资格和混乱/持久状态差异通过协作+原型保留，合理。',
191:'PP场外存活门差异与战斗同招/未变身写穿需要协作；原型合理。',
192:'战斗增益、侧状态、逃跑物品、笛/球和持久友好由双方协作，合理。',
193:'道具领域/入口不变量可框架承接，详细战斗行为已列协作子行。',
194:'失败/取消/扣减边界汇总可以框架编排，不代表战斗退款免原型。',
195:'道具配置由框架提供，战斗消费者依赖补全见CK-DEP-001。',
196:'FAIL：§3.1列表/窗口和数量/确认输入与交易提交混合，只有框架伙伴；应明示MZ交互责任。',
197:'FAIL：BP欢迎/告别/数量窗半价显示与交易提交混合，当前无MZ职责。',
198:'价格字段、覆盖映射、读取条件与会话清除由框架负责，合理。',
199:'物品/钱/统计的提交与回退是框架交易领域；不虚构事务。',
200:'交易不变量由框架负责，具体显示缺口见196/197。',
201:'资源/容量/列表复用失败汇总由框架负责，半价显示回指主UI行即可。',
202:'金钱/BP/价格/赠品配置由框架维护合理。',
203:'曲线、反向换算及表外异常是持久成长规则，框架可承接。',
204:'战斗EV/经验修正与逐级升级/学招循环跨双方；成长原型正确，仍需MZ暂停输入消费。',
205:'FAIL：等级/经验设置辅助含消息先于写入、场景刷新、能力差异窗与进化交互，当前仅框架未说明MZ职责。',
206:'FAIL：通用学习/遗忘/重学的确认/放弃/循环/空UI失败与领域候选混合，当前只框架；战斗6.1另拆不能覆盖场外UI。',
207:'战斗学招的替换/放弃暂停与场上同步合理标协作+成长原型。',
208:'友好/亲密存储、表值、正负修正和纯派生由框架承接；战斗效果引用其它主规则。',
209:'成长不变量汇总框架可接受；具体战中条款沿204/207联调。',
210:'成长字段/曲线/场外失败汇总归框架可接受；多级演出沿204/205。',
211:'成长配置由框架维护，未当作已批准首版。',
212:'寄养槽、同引用、寄存/取回/持久化由框架承接；不误当Showdown繁殖。',
213:'FAIL：槽位选择有双槽菜单/取消索引及事件变量写入、编译映射，当前只框架且无MZ接入责任。',
214:'兼容性、周期抽样、领取蛋副作用和静默成长均是框架领域，合理。',
215:'寄养状态/引用/费用报价不变量框架可接受，不补造真实扣费。',
216:'寄养前置失败与迁移历史保持框架粗标，未知事件接待没有被排除。',
217:'寄养配置/周期参数框架可接受。',
218:'蛋判据、来源与展示消费者目录可框架承接，详细输入演出在后续主行。',
219:'计步/动态加速扫描/顺序敏感提交由框架编排，宿主提供迈步输入。',
220:'框架+MZ及理由明确先领域提交后演出、分别验收；接受这一粗粒度混合行，不仅因含演出关键词就强拆。',
221:'命名/空输入/取消/淡出释放是MZ+框架，方向合理；字段已提交不回滚。',
222:'蛋持久状态和跨包调用关系由框架维护，合理。',
223:'蛋判据/提交/身份缓存不变量由框架负责合理。',
224:'直接重复提交、负字段、显示触发形态等失败边界框架编排，MZ消费沿220/221。',
225:'孵化数据与配置由框架提供，媒体仍待运行。',
226:'遭遇作者数据/快照/类型选择归框架领域；地图输入不等于整章MZ实现。',
227:'概率、驱虫剂、双打和开战前标记由框架规则/编排承接合理；宿主迈步输入要联调。',
228:'候选权重/等级抽样是框架野外规则，非战斗引擎自带功能。',
229:'野生个体生成/钩子/平衡等级框架负责，保留随机消费和自定义扩展边界。',
230:'本章只规定发起开战调用与临时字段生命周期，战斗启动另属WP39等；框架编排合理。',
231:'遭遇数据/触发不变量框架合理。',
232:'拒绝/版本/候选/累加边界由框架负责，不由未命中推不存在。',
233:'遭遇/能力修正配置由框架维护，不把世代参数当行为兼容证明。',
234:'特殊范围待用户决策，候选生成/规则校验归框架并列MZ合作，方向合理。',
235:'FAIL：租借界面选满/确认/取消第三只与会话提交混合，虽泛列MZ，理由未说明界面职责/独立验收，应分工或拆行。',
236:'FAIL：两屏交换取消/重选与无条件队伍提交是不同验收点，泛列MZ不能清楚承担其输入/提交关系。',
237:'临时集合与原队伍/规则人数/默认属主关系归框架；特殊范围待决策正确。',
238:'工厂候选池/区间/阈值数据归框架；特殊范围未自动排除。',
239:'FAIL：邮件模型与§2.2 250字输入/停止给予确认混合，只有框架伙伴，写信宿主职责缺失。',
240:'FAIL：§3.1–3.2阅读画面、PC信箱命令、取消和有序失败需MZ+框架；当前只框架。',
241:'礼物载体、ID队列/已领标记与解锁状态由框架承接合理。',
242:'FAIL：下载/候选过滤与§5接收掉落动画/消息后推队列混合，只有框架伙伴而无MZ职责。',
243:'领取的持久字段/背包/礼物队列提交由框架负责，条件图鉴展示应接MZ；主要去向可保留。',
244:'FAIL：整节是调试编辑/管理/导出作者工具，缺特殊工具范围待用户决定引用，且取消输入与共享对象提交未分工。',
245:'邮件/礼物持久不变量由框架维护；作者操作落盘范围不能改称已选首版。',
246:'邮件/礼物容量、解码和失败汇总归框架合理，具体UI主行需补分工。',
247:'卡面数值/价格为特殊玩法框架规则，MZ合作且待用户范围决定正确。',
248:'卡仓/赠卡/准入查询框架负责，库存不等于背包且未错误交Showdown。',
249:'FAIL：§4手选USE/BACK/预览与随机牌组构建混合，泛列MZ未给交互/随机规则独立责任，需细分。',
250:'FAIL：§5.1精确repeat/trigger仲裁/消息等待与棋盘翻转/对手评分混合，泛列MZ未给输入时序归属。',
251:'终局提示后卡仓转移、direct异常等框架规则合理，MZ协作/范围待决策保留。',
252:'MZ+框架且理由明确买卖查看交互与持有/资源主规则，接受粗标；不把展示报价当到账证明。',
}

FINDINGS = [
 {'id':'CK-META-001','severity':'P2','status':'FAIL','feature_ids':[], 'document_ids':['DOC-0030'], 'source_lines':[[45,72]],'title':'WP27两个可验收行为子节被概念父节吞成元数据', 'why':'§2.1默认/显式输入及§2.2 ShowQuantity/Consumable三态、图标遮数量、逐槽显示是具体数据/显示合同；section-metadata泛关联本篇六行不能给这些规则指定职责。标题覆盖通过不能替代语义功能覆盖。','required_fix':'保留既有ID，新增适当功能ID或将行为准确并入现有行且给来源范围/职责；分别表达框架数据规则与MZ显示消费，重建section/view。'},
 {'id':'CK-BATTLE-001','severity':'P2','status':'FAIL','feature_ids':['FR-000147','FR-000148','FR-000153'],'source_lines_by_feature':{'FR-000147':[[159,168]],'FR-000148':[[183,202]],'FR-000153':[[136,141]]},'title':'持久状态与战斗执行的明确交界仍只有框架职责','why':'WP20专门PP写穿/战中招式同步、可更新还原记录和伙伴捕获错配，以及WP24战斗奖金/败北结算是跨战斗会话与持久状态的行为；这些行无Showdown伙伴、具体协作问题或原型关系。','required_fix':'保留父ID；将有不同验收职责的子节单列协作候选或明确待原型决策，列双方状态/顺序/取消/异常/成员身份映射，并补WP42/WP50/WP39等依赖。不得只补一条泛泛待验证文字。'},
 {'id':'CK-MZ-001','severity':'P3','status':'FAIL','feature_ids':['FR-000152','FR-000166','FR-000171','FR-000172','FR-000178','FR-000179','FR-000183','FR-000196','FR-000197','FR-000205','FR-000206','FR-000213','FR-000239','FR-000240','FR-000242'],'source_lines_by_feature':{'FR-000152':[[56,79]],'FR-000166':[[139,151]],'FR-000171':[[84,89]],'FR-000172':[[105,118]],'FR-000178':[[115,157]],'FR-000179':[[159,165]],'FR-000183':[[69,77],[105,110]],'FR-000196':[[47,58],[72,80]],'FR-000197':[[88,104]],'FR-000205':[[126,148]],'FR-000206':[[159,180]],'FR-000213':[[79,97]],'FR-000239':[[40,42]],'FR-000240':[[52,71]],'FR-000242':[[94,97]]},'title':'多处真实UI/事件交界继承整篇框架模板而无宿主职责','why':'上述源区间包含输入/确认/取消循环、场景刷新、消息先于状态提交或事件变量刷新等独立可验收边界。相关行伙伴只有框架，理由统一声称消费者另列，但这些子节没有单列MZ行；WP25的4.2、WP28野外及WP35孵化则已有明确MZ责任，口径不一致。','required_fix':'按行为边界拆分或写明足够具体的框架/MZ责任和验收，不要求逐句ID；避免把数值/持久状态随UI一起扔给MZ。'},
 {'id':'CK-TOOLS-001','severity':'P3','status':'FAIL','feature_ids':['FR-000154','FR-000244'],'source_lines_by_feature':{'FR-000154':[[160,169]],'FR-000244':[[125,132]]},'title':'嵌在领域文档内的调试/作者工具未保留专门范围决定','why':'两行覆盖交互式新建NPC或礼物编辑/管理/导出，却仅有通用去向/阶段决策，target_scope待确认且没有DEC-SPECIAL-AND-HOST-SCOPE。README把调试/编辑工具保持待用户决定的规则未落实到这些嵌入行。','required_fix':'为相关工具子节保留明确用户范围待决策及引用，区分正常装载/领取与作者编辑取消/部分提交；不得自动排除或当作批准首版。'},
 {'id':'CK-MIXED-001','severity':'P3','status':'FAIL','feature_ids':['FR-000235','FR-000236','FR-000249','FR-000250'],'source_lines_by_feature':{'FR-000235':[[61,69]],'FR-000236':[[73,83]],'FR-000249':[[59,65]],'FR-000250':[[71,111]]},'title':'特殊玩法泛列MZ伙伴仍未说明交互/规则的不同验收点','why':'租借/交换的两屏取消与提交，Triad手选/随机和repeat/trigger仲裁与翻转/评分是分开的责任。当前各行仅复用special-framework泛理由；不是有伙伴名就已完成分工。','required_fix':'在保留特殊范围待决策的前提下，给具体MZ输入/场景与框架规则/状态责任，或按现有子节拆分；WP35 FR-000220及Triad FR-000252已作具体分工的粗行可作为一致口径。'},
 {'id':'CK-DEP-001','severity':'P3','status':'FAIL','feature_ids':['FR-000147','FR-000148','FR-000155','FR-000157','FR-000158','FR-000186','FR-000187','FR-000190','FR-000191','FR-000192','FR-000204','FR-000207','FR-000221'],'title':'重要新拆边界仍只继承旧WP计划依赖而漏正式直接合同','why':'例如音频FR-000155只有WP02/WP03/WP18，却直接依赖WP15/WP16/WP67-A；伙伴参与157/158没有WP39/WP42；战斗道具186/187只有WP20/27/30/31而漏WP40/WP42/WP67-A；成长204/207没有WP42；命名221没有WP17。feature_refs全部为空，未有其它机器引用弥补。','required_fix':'依据已读正式子节补必要直接依赖或清晰的类型化消费者/提供者引用，不把静态WP提取索引当完整规划依赖。可读视图同步显示。'},
]

def main():
    m=load(PREFIX+'routing-manifest.json')
    c=load(PREFIX+'section-coverage.json')
    batch=load('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batch-assignment.json')['batches']
    docs=[d for d in m['documents'] if '/creature-rpg/' in d['source']['path']]
    ids={d['document_id'] for d in docs}
    fs=[f for f in m['features'] if f['document_id'] in ids]
    assertions=[]
    ledger=[]
    expected_paths=git('ls-tree','-r','--name-only',BASE,'--','deliverables/final-specification-set/creature-rpg').decode().splitlines()
    assertions.append({'check':'independent_creature_tree_set','pass':sorted(expected_paths)==sorted(d['source']['path'] for d in docs)})
    sections=[]
    for d in docs:
        p=d['source']['path']; data=git('show',BASE+':'+p); lines,hs=scan(data)
        cs=[s for s in c['sections'] if s['document_id']==d['document_id']]
        identity_ok=sha(data)==d['source']['sha256'] and data==git('show',CANDIDATE+':'+p)==git('show',DELIVERY+':'+p)
        hkeys=lambda h:(h['level'],h['title'],h['anchor'],h['line_start'],h['line_end'],h['heading_sha256'])
        header_ok=[hkeys(x) for x in hs]==[hkeys(x) for x in cs]
        bindings=[b for b in batch if p in b['actual_target_write_set']]
        expected_batches=[b['id'] for b in bindings]; expected_required=sorted({x for b in bindings for x in b['required_ids']})
        binding_ok=d['upstream']['batches']==expected_batches and d['upstream']['required_ids']==expected_required
        features=[f for f in fs if f['document_id']==d['document_id']]
        used=[]; unit_ok=True
        for f in features:
            s=f['source']; selected=[h for h in hs if h['anchor']==s['anchor'] and h['heading_sha256']==s['heading_sha256']]
            unit=''.join(''.join(lines[a-1:b]) for a,b in s['line_ranges']).encode()
            unit_ok &= len(selected)==1 and sha(unit)==s['unit_sha256']
            for a,b in s['line_ranges']: used.extend(range(a,b+1))
            binding_ok &= f['upstream']['batches']==expected_batches and f['upstream']['required_ids']==expected_required
            binding_ok &= f['current_applicability']['status']==('待整改后核对' if expected_batches else '固定基线粗标')
        nooverlap=len(used)==len(set(used))
        assertions.extend([{'check':d['document_id']+'/'+k,'pass':bool(v)} for k,v in [('source_current_candidate_same_bytes',identity_ok),('independent_headings_and_positions',header_ok),('feature_locators_and_hashes',unit_ok),('nonoverlap',nooverlap),('r8_document_conservative_binding',binding_ok)]])
        ledger.append({'document_id':d['document_id'],'path':p,'read_ranges':[[1,len(lines)]],'reading':'FULL_MODEL_VISIBLE_TEXT','truncation_recovery':'长输出的中部省略区间已另次补读；见报告命令顺序。','line_count':len(lines),'bytes':len(data),'sha256':sha(data),'git_blob':git('rev-parse',BASE+':'+p).decode().strip(),'heading_count':len(hs),'feature_count':len(features),'metadata_heading_count':sum(s['mapping_kind']=='section-metadata' for s in cs),'r8_batches':expected_batches,'r8_required_ids':expected_required})
        for s in cs:
            sections.append({k:s[k] for k in ['document_id','path','level','title','anchor','line_start','line_end','mapping_kind','feature_refs']})
    # Check every generated row, without trusting only the view's row count.
    view=git('show',CANDIDATE+':'+PREFIX+'views/creature-rpg.md').decode()
    viewrows={}
    for i,line in enumerate(view.splitlines(),1):
        mm=re.match(r'^\| (FR-\d{6}) / ',line)
        if mm: viewrows[mm[1]]=(i,line)
    assertions.append({'check':'view_exact_feature_set','pass':set(viewrows)=={f['feature_id'] for f in fs}})
    texts=git('show',CANDIDATE+':'+PREFIX+'routing-manifest.json').decode().splitlines()
    positions={}
    for i,line in enumerate(texts,1):
        mm=re.match(r'\s*"feature_id": "(FR-\d{6})"',line)
        if mm: positions[mm[1]]=i
    results=[]
    for f in fs:
        fid=f['feature_id']; n=int(fid.split('-')[1]); reason=REASONS[n]
        related=[x['id'] for x in FINDINGS if fid in x['feature_ids']]
        _,v=viewrows[fid]
        needed=[f['future_plan']['rationale'],*f['future_plan']['questions'],f['future_plan']['destination'],f['destination_verification']['status'],f['future_plan']['stage'],f['implementation']['status'],f['implementation']['acceptance_status'],f['source']['anchor'],f['source']['commit'],*f['future_plan']['partners'],*f['dependencies']['wp_refs'],*f['decision_refs'],*f['future_plan']['prototype_refs'],*f['upstream']['batches']]
        needed.extend([f['source']['fact_excerpt'], f['current_applicability']['snapshot_commit'], f['current_applicability']['target_scope'],f['upstream']['status']])
        needed.extend('L'+str(a)+'-L'+str(b) for a,b in f['source']['line_ranges'])
        needed.append('https://github.com/y805939188/pokemon-essentials-clean-room/blob/'+f['source']['commit']+'/'+f['source']['document']+'#L'+str(f['source']['line_ranges'][0][0]))
        view_ok=all(x.replace('|','\\|').replace('\n',' ') in v for x in needed)
        assertions.append({'check':fid+'/view_key_fields_match','pass':view_ok})
        state_ok=f['destination_verification']=={'status':'待验证','evidence':[],'source_only_is_compatibility_evidence':False} and f['future_plan']['stage']=='待定' and f['future_plan']['stage_approval']=='未批准' and f['implementation']['status']=='未实现' and f['implementation']['acceptance_status']=='未验收'
        assertions.append({'check':fid+'/separate_honest_states','pass':state_ok})
        results.append({'feature_id':fid,'document_id':f['document_id'],'heading':f['source']['heading'],'source_document':f['source']['document'],'source_anchor':f['source']['anchor'],'source_line_ranges':f['source']['line_ranges'],'candidate_line':positions[fid],'view_line':viewrows[fid][0],'destination':f['future_plan']['destination'],'partners':f['future_plan']['partners'],'destination_semantics':'FAIL' if reason.startswith('FAIL') else 'PASS','overall_result':'FAIL' if related else 'PASS','reason':reason,'finding_refs':related,'locator_result':'PASS','state_result':'PASS' if state_ok else 'FAIL','view_fields_result':'PASS' if view_ok else 'FAIL','r8_binding_result':'PASS','prototype_result':'未运行/不要求原型才能接受粗标','catalog_semantic_result':'待查：对应catalog未在本子任务全文阅读'})
    unreviewed=[{'document_id':d['document_id'],'path':d['source']['path'],'status':'待查','reason':'交回父任务另启独立上下文完整复审；本审者未全文读。'} for d in m['documents'] if '/generic-kernel/' in d['source']['path'] or ('/test-catalog/' in d['source']['path'] and any('/'+x+'-' in d['source']['path'] for x in ['creature-rpg','generic-kernel']))]
    result={'schema_version':'independent-creature-review.v1','candidate':CANDIDATE,'source':BASE,'delivery':DELIVERY,'formal_tree':git('rev-parse',CANDIDATE+':deliverables/final-specification-set').decode().strip(),'task':'/root/creature_kernel_semantics','configuration':{'requested_model':'gpt-6.1-sol','requested_effort':'ultra','requested_tier':'default','actual_model':'UNVERIFIED','actual_effort':'UNVERIFIED','actual_tier':'UNVERIFIED','actual_fast':'UNVERIFIED','authority':'根委派要求；当前子任务无权威运行telemetry，不冒称已核实。'},'scope':'creature-rpg 15正文全部逐行语义阅读；116现有功能逐项；view全部行关键字段机械核对；section全部标题独立解析与人工metadata判断；相关R8写集逐文档/功能静态绑定。','conclusion':'FAIL_FIXED_COARSE_BASELINE','counts':{'documents':len(docs),'source_lines':sum(d['line_count'] for d in ledger),'bytes':sum(d['bytes'] for d in ledger),'headings':len(sections),'features':len(fs),'metadata_headings':sum(x['mapping_kind']=='section-metadata' for x in sections),'feature_results':dict(collections.Counter(r['overall_result'] for r in results)),'pending_upstream_features':sum(bool(f['upstream']['batches']) for f in fs)},'documents':ledger,'section_checks':sections,'features':results,'findings':FINDINGS,'mechanical_assertions':assertions,'mechanical_result':'PASS' if all(a['pass'] for a in assertions) else 'FAIL','unreviewed_reassigned':unreviewed,'limits':['未全文语义读generic-kernel及五catalog，不能把本报告当两域完整PASS。','未读取参考/Ruby/业务向量；未运行游戏、宿主、框架、原型或Showdown；没有兼容性已验证结论。','schema与验证器完整审查/全仓隔离/推送由父任务承担；本子任务只读过与locator/render/binding有关片段，未冒称完整工具审查。','固定基线粗标不等于R8整改完成；需新固定整改候选回填及独立再验收。']}
    for finding in FINDINGS:
        finding['candidate_locations']=[{'feature_id':fid,'path':PREFIX+'routing-manifest.json','line':positions[fid],'pointer':'/features/'+str(next(i for i,f in enumerate(m['features']) if f['feature_id']==fid))} for fid in finding['feature_ids']]
    for x in c['sections']:
        if x['document_id']=='DOC-0030' and x['line_start'] in [45,64]: FINDINGS[0].setdefault('coverage_records',[]).append(x)
    (OUT/'creature-kernel-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'mechanical_result':result['mechanical_result'],'counts':result['counts'],'unreviewed_reassigned':len(unreviewed)},ensure_ascii=False))

if __name__=='__main__': main()
