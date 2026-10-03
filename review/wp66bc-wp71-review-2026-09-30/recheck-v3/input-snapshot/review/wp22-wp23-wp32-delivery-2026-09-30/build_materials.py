"""Assemble extractor-owned Markdown/JSON/hash/diff audit materials only.

No import, evaluation, compilation, or execution of reference source material.
"""
from pathlib import Path
import hashlib, json, difflib, subprocess, re

ROOT=Path(__file__).resolve().parents[2]
D=Path(__file__).resolve().parent
C=ROOT/'review/wp58-wp62-wp38-review-2026-09-30/closure-review'
REF=ROOT/'reference/pokemon-essentials'
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def identity(p):
    b=p.read_bytes()
    return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}

def save(name,obj):
    (D/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

packages=[json.loads((D/f'wp{n}-fixed.json').read_text()) for n in [22,23,32]]
for p in packages:
    for a in p['artifacts']:
        assert identity(ROOT/a['path'])=={k:a[k] for k in ['sha256','bytes']},a['path']
readings=json.loads((D/'reading-log.json').read_text())
sources={}
for row in readings:
    if not row['path'].startswith('reference/pokemon-essentials/'):
        continue
    rel=row['path'].removeprefix('reference/pokemon-essentials/')
    rec=sources.setdefault(rel,{'path':row['path'],**identity(ROOT/row['path']),'readings':[]})
    rec['readings'].append({k:row[k] for k in ['package','ranges','purpose']})
for rel,rec in sources.items():
    blob=subprocess.check_output(['git','-C',str(REF),'show',COMMIT+':'+rel])
    rec['matches_commit_blob']=hashlib.sha256(blob).hexdigest()==rec['sha256'] and len(blob)==rec['bytes']
    assert rec['matches_commit_blob'],rel
save('source-identities.json',{'reference_commit':COMMIT,'count':len(sources),'sources':list(sources.values()),
    'meaning':'File hashes and Git blob equality; semantic reading scope is the named ranges/literal-field searches, not whole-file rereview.'})

bindings=[b for p in packages for b in p['bindings']]
for b in bindings:
    assert identity(ROOT/b['sender'])=={k:b[k] for k in ['sha256','bytes']},b
groups=[
 {'id':'B01','scope':'WP22 × WP21/39/40/41/42/38',
  'findings':['个体资格／菜单许可／裸登记／执行器分别有门；所属训练家额度不是个体原Owner','普通换下无统一解除；濒死／捕获／世界／设施各自显式还原','个体提交两次与战斗完整回读、HP差值、图鉴全局写入已说明','Mega能力得失与Primal入场后能力检查不同；不共用次数或环规则'],
  'evidence':'WP22 §§3–6、W01–W24；WP21§4、WP39§5/6、WP40§7、WP41§4、WP42§6/7、WP38§5/6'},
 {'id':'B02','scope':'WP23 × WP20/30/38/40/42/49/62',
  'findings':['阶段≤3经验入暂存；EV高阶段落普通分支；当前经验余量不扣暂存','净化80%经验／EV额度／零与nil／学招取消分开','HP0清Hyper与一般治疗不清分开；旧战斗对象初始化清理不能当新成员统一清理','捕获Owner、抢夺、暗影拥有不重复定义；净化不清暗影拥有记录','净化室成员引用移动、替换蛋门例外及两种容量失败均具名'],
  'evidence':'WP23 §§3–8、W01–W41；WP30§4/5、WP42§4/5、WP38§5/6、WP62§3'},
 {'id':'B03','scope':'WP32 × WP31/26/42/11/59/38',
  'findings':['时钟、世界天气意图、当前地图在检查时读取，不用战斗开场快照','K逐击逐目标；D含替身与混乱；濒死清D不清K','接收先于世界进化；三表随删除左移，新捕获槽无成就','升级目标优先且取消不回查战后族；三表随后清理','事件准备、命中返回、成功提交分层；编号可重用','TradeSpecies按自身物种；双收尾调用保留宿主未决'],
  'evidence':'WP32 §§2–7、W01–W38；WP31§4/5/6、WP26§4、WP42§7'},
 {'id':'B04','scope':'三新包共享状态与次序',
  'findings':['Shadow入场副本类型可被随后Mega完整回读覆盖；没有新增互斥优先级','净化先清Shadow才恢复经验、调用等级辅助与可能进化；进化统一Shadow拒绝门仍由WP31定义','捕获解除变形、更新Shadow招、首招记录、图鉴与集合接收顺序继承WP38','心量表快照未随捕获三表移动，WP23-O05单列，不把所有队伍记录统称同步'],
  'evidence':'WP22§4/6/7，WP23§3/5/6，WP32§4/5；批内绑定明确尚未外审'},
 {'id':'B05','scope':'旧批准范围与新观察',
  'findings':['WP62被审v3 PASS_SCOPED与回填后字节分列；WP58／WP38已受理范围不重审','C03两项当前状态同步，revision_history保留历史ReviewPending','WP32-N01涉及WP31第114行过窄摘要，旧稿未改；其余8项新范围观察或宿主未决','新三包仅ReviewPending，不自行批准Reviewed'],
  'evidence':'backfill-response.md、new-observations.md、closure-review/report.md§§3–4'},
 {'id':'B06','scope':'身份与覆盖边界',
  'findings':['三主稿＋三附表按串行顺序固定；后级绑定与磁盘身份一致','矩阵仅F06-08两具名子范围及F09-04推进ReviewPending；保留前向Inventoried','45条规格绑定包含批内与已审状态，不把完整哈希当全域语义批准','Demo／宿主／媒体／插件、U01–U10与WP78→WP79→WP80保留'],
  'evidence':'wp22-fixed.json、wp23-fixed.json、wp32-fixed.json、最终矩阵与manifest／主TSV'}
]
save('boundary-checks.json',{'date':'2026-09-30','role':'extractor static boundary self-check; not independent review',
 'groups':groups,'bindings':bindings,'binding_count':len(bindings),
 'matrix':{'path':'planning/feature-matrix.md',**identity(ROOT/'planning/feature-matrix.md')},
 'new_observations':{'path':str((D/'new-observations.md').relative_to(ROOT)),**identity(D/'new-observations.md')},
 'remaining':['WP32-N01需要独立审查后才决定旧摘要维护','WP32-N02重复viewport释放属于宿主未决','全部新稿待独立外审','U01–U10及WP78→WP79→WP80']})

save('self-checks.json',{'date':'2026-09-30','role':'extractor; specification only; not independent reviewer',
 'reference_commit':COMMIT,'sequential_order':['WP62 administrative backfill','WP22','WP23','WP32'],
 'packages':packages,'total_scenarios':sum(len(p['scenarios']) for p in packages),
 'source_identity_file':{'path':str((D/'source-identities.json').relative_to(ROOT)),**identity(D/'source-identities.json')},
 'seventeen_requirements':{
  'purpose_user_behavior':'Each main spec §1', 'domain_inputs_outputs_preconditions':'WP22§§2–5; WP23§§2–8; WP32§§1–7',
  'state_rules_invariants_edges_failure':'Domain tables and named exceptions in all three main specs',
  'dependencies_configuration':'Bound identities plus data appendices', 'examples_test_vectors':'WP22 W01–25; WP23 W01–42; WP32 W01–38',
  'classification_open_questions_traceability':'Headers, final dependency/unknown/source sections'},
 'method_limits':['Static manual definition/caller/data/UI review','Independent fixed arithmetic and literal sets; not reference-equivalent execution',
 'No reference edits, Ruby execution, game, compiler, converter, generator, plugin, network, real save/map/input',
 'No framework implementation, agent/task, reviewer message, commit or push'],
 'matrix':{'path':'planning/feature-matrix.md',**identity(ROOT/'planning/feature-matrix.md')},
 'reviewed_set':'WP01–WP21、WP24–WP31、WP33–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62',
 'new_status':'WP22/WP23/WP32 remain ReviewPending; no fourth package started'})

changed=[
 'specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md',
 'specs/pokemon-rules/wp38-capture-and-receiving.md',
 'planning/feature-matrix.md',
 'review/wp58-wp62-wp38-delivery-2026-09-29/boundary-checks.json',
 'review/wp58-wp62-wp38-delivery-2026-09-29/self-checks.json',
 'review/wp58-wp62-wp38-delivery-2026-09-29/delivery-summary.md']
(D/'backfill-diffs').mkdir(exist_ok=True)
diffs=[]
for rel in changed:
    before=C/'input-snapshot'/rel;after=ROOT/rel
    diff=''.join(difflib.unified_diff(before.read_text().splitlines(True),after.read_text().splitlines(True),
        fromfile='closure-review/input-snapshot/'+rel,tofile=rel,n=3))
    name=Path(rel).stem+'.diff'
    dp=D/'backfill-diffs'/name;dp.write_text(diff)
    diffs.append({'path':str(dp.relative_to(ROOT)),**identity(dp),
                  'base':{'path':str(before.relative_to(ROOT)),**identity(before)},
                  'target':{'path':rel,**identity(after)},
                  'kind':'administrative backfill plus F06-08/F09-04 new batch status increments' if rel=='planning/feature-matrix.md' else 'administrative status/identity synchronization only'})
save('diff-bindings.json',{'base':'closure-review/input-snapshot','target':'final submitted files, not an intermediate matrix','diffs':diffs,
    'catalog_diffs':'manifest/TSV follow their existing append-history convention; no circular catalog diff hash'})
save('change-whitelist.json',{'existing_allowed':changed+['planning/review-manifest-2026-09-19.md','review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv'],
 'new_specs':[a['path'] for p in packages for a in p['artifacts']],
 'new_directory':str(D.relative_to(ROOT)), 'protected':'All other preexisting files in preexisting-files.tsv; includes all reviewer originals/history snapshots and all non-Git reference files'})

pre=json.loads((D/'preflight-checks.json').read_text())
response='''# WP62管理性回填、C03与身份链回应

2026-09-30；提取方。依据[独立闭合报告](../wp58-wp62-wp38-review-2026-09-30/closure-review/report.md)§4和[next-batch-prompt](../wp58-wp62-wp38-review-2026-09-30/closure-review/next-batch-prompt.md)。报告完整SHA-256 `867087b0b7f036b0b794250a9894d026b43f6fcdca1cf3df5ac16798b1d1d704`／10,212字节；执行提示 `46a97f4fa40ba6f7126febac66d2a4d93b3e8cce01f31dbc1a6f69e277d6a019`／13,536字节。原15项及C01-2／C02均已关闭，WP58／WP38回填受理；不重做首审。

## 1. 固定预检

全部9项逐字节匹配；828项当前输入、828项闭合快照、12份完成依赖及闭合轮原件匹配；此前11轮快照／列出原件无差异。reference HEAD正确且普通Git状态空；工作区根本身不是Git仓库。17,417个预存非Git文件基线留作修改白名单核对。详[preflight-checks.json](preflight-checks.json)。

| 对象 | 被审／受理基线SHA-256 | 字节 |
| --- | --- | ---: |
'''
for row in pre['report_section1_nine']:
    response+=f'| {row["object"]} | `{row["sha256"]}` | {row["bytes"]:,} |\n'
response+='''
## 2. 回填范围与C03

WP62头尾及F15-01回填Reviewed（限定静态范围，2026-09-30闭合短复审PASS_SCOPED；管理性回填）。范围按报告A～F：图鉴字段／持久接点及原键区别、写入门与接收者／次序、展示形态性别异色与计数、区域解锁可访问／nil与栖息地、已述展示筛选／摘要／存档与静态场景。不扩大到剧情、完整UI运行、Shadow全生命周期或整游戏。

WP38仅更新WP62的状态与实际完整引用，并把W07“未核准”历史化：本次闭合确认等级21、满血无状态x30／y43874；x90／y53910仍仅独立常数，旧v2错误前提不追认。捕获算法与20条场景未改。WP58本次字节不变，受理版仍为原30,501字节。

旧批boundary B05和self backfill_note两项C03简写同步；当前packages／artifacts／bindings与摘要一并同步；revision_history中的ReviewPending及旧哈希保留。两轮修订回应、既有差异、reviewer原件与历史快照全部未修改。

## 3. 最终目标身份与差异

以下为提交时目标，矩阵已包含随后三包增量；不是WP62回填中间版本。六份差异均相对指定闭合轮input-snapshot，并绑定此最终目标。矩阵中F15-01、F10-06为管理记法；F06-08的WP22／WP23与F09-04的WP32为新批ReviewPending增量，其余行不改。被审v3及原受理版身份见§1，新字节不冒充被审对象。

| 当前目标 | 完整SHA-256 | 字节 | 差异 |
| --- | --- | ---: | --- |
'''
for item in diffs:
    a=item['target'];link='backfill-diffs/'+Path(item['path']).name
    response+=f'| `{a["path"]}` | `{a["sha256"]}` | {a["bytes"]:,} | [diff]({link}) |\n'
response+='''
## 4. 登记与停止

现有主TSV续为v38，manifest续第六十三轮；§1更新当前身份，§2.1新增对应关系，§3保留被审／受理／回填／新交付链，§4追加本轮。闭合reviewer15件与新批产物补登，不建立平行总控。manifest不自哈希，主TSV不收自身或manifest；本目录自检不包含自身内容哈希，以最终只读复测确认登记值。

回填后按授权串行完成WP22→WP23→WP32，三主稿及三附表均ReviewPending；本回应不是外审批准。批末统一材料见[delivery-summary.md](delivery-summary.md)，完成后停止，不启动第四包。Demo／宿主／媒体／插件、U01–U10与WP78→WP79→WP80继续保留。
'''
(D/'backfill-response.md').write_text(response)

summary='''# WP22 → WP23 → WP32 统一送审材料

2026-09-30；规格提取方，非独立reviewer。先完成WP62限定Reviewed管理回填与C03，再按顺序回源、写稿、自检、固定和矩阵增量。**新三包全部ReviewPending（批内固定版本，尚未外审）**；没有实现新框架。105条静态场景不是运行测试。

## 1. 主稿与附表（最终固定身份）

| 包／文件 | 完整SHA-256 | 字节 | 主稿场景 |
| --- | --- | ---: | ---: |
'''
for pkg in packages:
    for i,a in enumerate(pkg['artifacts']):
        summary+=f'| {pkg["package"]} [{Path(a["path"]).name}](../../{a["path"]}) | `{a["sha256"]}` | {a["bytes"]:,} | {len(pkg["scenarios"]) if i==0 else "—"} |\n'
summary+='''
- WP22 A～F：Mega个体／战斗分层、所有者与资源、登记取消执行、状态传播、Primal独立规则、换下／濒死／捕获／终局／设施还原；48个默认Mega目标／47石／1招式型，含METAGROSS实际HP差异。
- WP23 A～G：建立、心阶段、Hyper、经验／EV暂存与恢复、招式、各净化入口、9组净化室的成员流转／节奏与流量／领取及失败；25性格数据、可选131配置／18招／4物品／1类型与默认未启用边界。
- WP32 A～F：实时地图／时钟／天气输入、L0／K／D与R、逐击记录和濒死清理、战后条件与取消、捕获队伍移位、交换／事件提交；35个情境身份及57条默认数据。

## 2. 回填与新观察

WP62被审v3 `e38812c8057fd3348c10319c29240ef6e21e72f37c769601f6e1d86bb0d56639`／32,378字节获独立PASS_SCOPED；本次回填后身份与六份最终差异见[backfill-response.md](backfill-response.md)。WP58／WP38原受理范围继承，WP38仅状态／身份／W07历史记法同步；旧报告、两轮回应与所有快照不改。

[new-observations.md](new-observations.md)列9项待审观察。WP32-N01指出WP31第114行“对对方”的要害摘要过窄，旧稿未改；WP32-N02公开交换双收尾及宿主重复释放未决。其余7项是新包范围内的数据或生命周期边界，不是重开旧关闭编号。

## 3. 自检、交界与审计材料

'''
for name,meaning in [('self-checks.json','逐包静态检查与17项标准映射'),('boundary-checks.json','六组交界及45条完整绑定'),('source-identities.json','实际来源文件身份、读取范围与固定commit blob核对'),('diff-bindings.json','六份差异的基线与最终目标绑定'),('preflight-checks.json','9项／828输入／历史快照固定预检'),('backfill-response.md','管理回填回应与身份链')]:
    a=identity(D/name);summary+=f'- [{name}]({name})：{meaning}；`{a["sha256"]}`，{a["bytes"]:,}字节。\n'
summary+='''
全量登记、JSON／链接、差异重建、固定输入白名单、历史原件／快照及reference只读状态的最终只读检查见[validation-results.json](validation-results.json)。自有检查只做文本、哈希、集合、JSON、差异与固定算术；没有执行或转译参考模型。

## 4. 登记范围与停止点

现有[manifest](../../planning/review-manifest-2026-09-19.md)续第六十三轮、[主TSV](../wp18-wp20-delivery-2026-09-26/current-hashes.tsv)续v38；保留全部历史身份与旧ReviewPending。F06-08分别登记WP22／WP23，F09-04登记WP32，均ReviewPending＋前向Inventoried。批内WP22→WP23／WP32、WP23→WP32引用明确未外审。

既有限定通过集合：WP01–WP21、WP24–WP31、WP33–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62。新三包不加入Reviewed集合。不是整个游戏运行通过，也不是全Feature完成。

本批完成后停止；未启动第四包、未创建Agent／新任务、未发reviewer消息、未提交／推送。Demo、宿主、媒体、插件、U01–U10及WP78→WP79→WP80出口保留；新观察与所有新稿等待用户转交独立审查。
'''
(D/'delivery-summary.md').write_text(summary)
print(json.dumps({'packages':len(packages),'scenarios':sum(len(p['scenarios']) for p in packages),
                  'bindings':len(bindings),'source_files':len(sources),'diffs':len(diffs)},ensure_ascii=False))
