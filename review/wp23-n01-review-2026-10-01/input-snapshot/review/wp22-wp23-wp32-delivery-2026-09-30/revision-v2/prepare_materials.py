"""Own Markdown/JSON/source-identity maintenance for the bounded revision.
Reads reference as text/blobs only. Does not run old delivery writers or Ruby.
"""
from pathlib import Path
import json, re, hashlib, subprocess

ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'review/wp22-wp23-wp32-delivery-2026-09-30'
O=D/'revision-v2'
R=ROOT/'review/wp22-wp23-wp32-review-2026-09-30'
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def ident(p):
    b=p.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}

def save(p,j):p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')

# Preserve previous observation statements by identity/snapshot; current claims
# track the independent decisions and the actual bounded edits.
p=D/'new-observations.md';s=p.read_text()
s=s.replace('# 本批具名新观察（提取方，待独立审查）','# 本批具名观察与首审处理记录（提取方）',1)
s=s.replace('2026-09-30。本文件不重开既有关闭编号，不给旧包自行批准修订。新三包均ReviewPending；下列发现也没有独立通过结论。除授权状态／身份回填外，旧规格未改。新稿固定身份见各`wp*-fixed.json`和批摘要。',
'''2026-09-30首审后同步。WP22／WP32已获限定PASS_SCOPED并管理回填；WP23按R01～R03修订v2仍ReviewPending。本文件记录独立报告§3的判定与提取方实际处理，不自行批准修订。首稿观察文件 `6646dde258a08f030e0a91274dedeb94906e6a9706ceb321f1f0179138aeb1bf`（4,620字节）保存在本轮input-snapshot；旧声明留史，当前适用结论如下。''',1)
wp31=ident(ROOT/'specs/pokemon-rules/wp31-basic-evolution.md')
s=s.replace('- 最小建议：外审确认后，仅授权把WP31该摘要限定为“实际记录的要害次数（含WP32注明的目标范围）”；不改基础阈值、进化提交或旧关闭编号。本次未改WP31。',
f'- **CONFIRMED，已按授权实际同步**：只改WP31§3.4旧第114行目标范围摘要并加单点维护尾注，当前完整身份 `{wp31["sha256"]}`（{wp31["bytes"]:,}字节）。基础阈值、进化提交／取消及旧关闭编号不变；真正引用其完整身份的WP23／WP32及活动绑定已级联。上条旧完整身份与原句是同步前历史。',1)
s=s.replace('- 最小建议：保持WP32§6.3和W35的条件化结论，独立核对调用路径；运行／宿主重复释放语义留后续具名验证。不擅自宣称必然双进化或必然异常，不修参考。',
'- **CONFIRMED_STATIC／RETAIN_RUNTIME**：保持WP32§6.3和W35的条件化结论；第二次viewport释放能否继续仍为宿主未决。未改WP26，不宣称必然双进化、必然异常或运行确认。',1)
s=s.replace('最终净化领取双满拒绝后也清中心','最终净化领取在**确实到达存放**后双满拒绝仍清中心；跨级恢复可能按R01更早失败而保留中心',1)
s=s.replace('替换仅比较Shadow状态，没有普通放置的蛋／最后可战斗成员门','替换比较Shadow查询**原始返回值相等**（nil与false不相等），没有普通放置的蛋／最后可战斗成员门；蛋例要求原始返回值匹配',1)
s=s.replace('以上9项观察只有WP32-N01明确涉及旧摘要范围过窄；其余为新包内提取／交界扩展或宿主未决。统一送审材料由用户转交；没有向reviewer发送消息。',
'''独立判定：WP22-O01、WP23-O01／O02／O05／O06与WP32-N01为CONFIRMED；O03为CONFIRMED但保留到达前提；O04原为PARTIALLY_CONFIRMED，现按R02修为原始结果相等（修订仍待有限复审）；N02为CONFIRMED_STATIC／RETAIN_RUNTIME。R01新增净化室跨级失败、R03默认G0写标志／提示已同步主稿与场景；不是再增加旧观察编号或重开旧关闭项。统一有限复审材料由用户转交，未发送reviewer消息。''',1)
p.write_text(s)

# Source provenance extends the existing log; past readings are historical.
log=json.loads((D/'reading-log.json').read_text())
fresh=[
 ('Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb',[[17,58],[108,126],[196,222]],'R01净化顺序／遗迹石回调；R02清标志；R03进入Hyper'),
 ('Data/Scripts/016_UI/023_UI_PurifyChamber.rb',[[348,420],[474,628],[1072,1080]],'R01实际Screen接收者及缺回调；R02替换；O03到达前提；全Scripts查重开／兜底'),
 ('Data/Scripts/013_Items/001_Item_Utilities.rb',[[132,220]],'R01等级写入、首个窗口更新与后续学招的先后'),
 ('Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb',[[93,112]],'R02原始查询返回；R03有效Hyper屏蔽'),
 ('Data/Scripts/014_Pokemon/001_Pokemon.rb',[[186,208],[1159,1225]],'R01等级设经验下限；R02构造未设置shadow'),
 ('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',[[88,96]],'R03普通随机转交'),
 ('Data/Scripts/001_Technical/002_RubyUtilities.rb',[[366,387]],'R03单数值参数原样转交；不执行'),
 ('Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb',[[78,88]],'R01 Medium等级10/11/12固定表值'),
 ('PBS/pokemon.txt',[[469,479]],'R01 RATTATA默认Medium'),
 ('Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb',[[294,305]],'N01要害记录没有目标阵营门'),
 ('Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',[[669,677]],'N01逐目标调用者门')]
for path,ranges,purpose in fresh:
    full='reference/pokemon-essentials/'+path
    log.append({'package':'WP23 revision v2 / WP32-N01','path':full,**ident(ROOT/full),'ranges':ranges,'purpose':purpose})
log.append({'package':'WP23-R03','path':'specs/combat/wp55-facility-session-and-restoration.md',**ident(ROOT/'specs/combat/wp55-facility-session-and-restoration.md'),'ranges':[[65,87],[124,124]],'purpose':'已审数值0入口[0,1)浮点合同，仅引用，不重审'})
save(D/'reading-log.json',log)
source=json.loads((D/'source-identities.json').read_text());by={x['path']:x for x in source['sources']}
for path,ranges,purpose in fresh:
    full='reference/pokemon-essentials/'+path
    if full not in by:
        blob=subprocess.check_output(['git','-C',str(ROOT/'reference/pokemon-essentials'),'show',COMMIT+':'+path])
        current=ident(ROOT/full)
        by[full]={'path':full,**current,'readings':[],'matches_commit_blob':hashlib.sha256(blob).hexdigest()==current['sha256'] and len(blob)==current['bytes']}
    by[full]['readings'].append({'package':'revision v2','ranges':ranges,'purpose':purpose})
assert all(x['matches_commit_blob'] for x in by.values())
source['sources']=list(by.values());source['count']=len(by);source['revision_note']='首审修订补RubyUtilities与GrowthRate等具名段；保留首稿读取历史，不冒称所有文件全文复审'
save(D/'source-identities.json',source)

# Independent fixed arithmetic and static receiver/definition checks, not a
# translated/executed behavioral model.
ch=(ROOT/'reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb').read_text().splitlines()
ot=(ROOT/'reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb').read_text().splitlines()
screen_methods=re.findall(r'^  def (\w+)', '\n'.join(ch[347:628]),re.M)
relic_methods=re.findall(r'^  def (\w+)', '\n'.join(ot[107:128]),re.M)
checks=[{'id':'R01-arithmetic','method':'independent constant arithmetic; not UI/reference execution','input':{'old_exp':1000,'saved_exp':416},'expected':[332,1332,1331,1728],'actual':[416*4//5,1000+416*4//5,11**3,12**3]},
 {'id':'R01-receiver-methods','method':'literal declaration sets within named class ranges','expected':[False,True],'actual':['pbUpdate' in screen_methods,'pbUpdate' in relic_methods]},
 {'id':'R03-bounded-interval','method':'constant interval dominance; no random calls','expected':[1000,True],'actual':[4000//4,1<=4000//4]}]
assert all(c['expected']==c['actual'] for c in checks)
save(O/'targeted-checks.json',{'checks':checks,'semantic_manual_checks':[
 {'id':'WP23-R01','evidence':'Other17–58→Items132–220; Chamber582 passes Screen; no pbUpdate declaration or forwarding located','conclusion':'Chamber cross-level fails at first window; E1331 committed, exact1332/store/clear not reached; same-level and Relic separate','scenarios':['W24','W38','W39','W43','W44','W45']},
 {'id':'WP23-R02','evidence':'Shadow100–102; constructor1159–1225; Other20; Chamber502','pairs':[{'input':['nil','nil'],'gate':'pass'},{'input':['nil','false'],'gate':'reject'},{'input':['false','false'],'gate':'pass'}],'meaning':'raw result equality, manual static deduction; no runtime truth normalization','scenarios':['W33','W46']},
 {'id':'WP23-R03','evidence':'Battle93→RubyUtilities366–387; WP55§2.5; Other207–213; Shadow104–105','conclusion':'Default M4000/G0 float always meets threshold; stored flag true + display request; effective false; repeat possible','scenarios':['W12']},
 {'id':'WP32-N01','evidence':'MoveUsage294–304 and UseMove669–675','conclusion':'One old summary changed, no new target restriction or threshold rewrite'}],
 'status':'extractor self-check; WP23 revisions remain unreviewed; no reference execution'})

packages=[]
for n in [22,23,32]:
    p=D/f'wp{n}-fixed.json';j=json.loads(p.read_text());previous=json.loads((R/'input-snapshot'/p.relative_to(ROOT)).read_text())
    j['version']=2;j['status']='ReviewPending' if n==23 else 'Reviewed'
    j['status_scope']='R01–R03 revised v2 pending limited review' if n==23 else '2026-09-30 independent first-review PASS_SCOPED; administrative backfill, named static scope only'
    if n==22:j['scope']='A–F named static scope; independent first review PASS_SCOPED; current administrative backfill'
    j['review_history']=[{'version':1,'status':'ReviewPending','artifacts':previous['artifacts'],'note':'Fixed actual first-review objects retained in input-snapshot'},
      {'date':'2026-09-30','decision':'REQUEST_CHANGES' if n==23 else 'PASS_SCOPED','report':'review/wp22-wp23-wp32-review-2026-09-30/report.md'}]
    j['artifacts']=[{'path':a['path'],**ident(ROOT/a['path'])} for a in j['artifacts']]
    if n==23 and not any(b['package']=='WP55' for b in j['bindings']):
        j['bindings'].append({'package':'WP55','sender':'specs/combat/wp55-facility-session-and-restoration.md','receiver':j['artifacts'][0]['path']})
    for b in j['bindings']:
        b.update(ident(ROOT/b['sender']))
        b['status']='批内修订稿，尚未外审；仅引用已核实交界' if b['package']=='WP23' else 'Reviewed（既有具名静态范围；按实际当前维护版）'
    txt=(ROOT/j['artifacts'][0]['path']).read_text();j['scenarios']=re.findall(r'^\| (W\d{2}) \|',txt,re.M)
    if n==23:
        j['static_checks']+=checks
        j['manual_boundary_checks'][3]='Chamber raw nil/false equality; egg case requires matching raw results; capacity claims require reaching storage'
        j['manual_boundary_checks']+=['Cross-level Chamber Screen missing update callback; committed vs unreachable stages','G0 default flag write/display and effective false separately stated']
    save(p,j);packages.append(j)

boundary=json.loads((D/'boundary-checks.json').read_text());boundary['version']=2
boundary['bindings']=[b for p in packages for b in p['bindings']];boundary['binding_count']=len(boundary['bindings'])
for g in boundary['groups']:
    if g['id']=='B02':
        g['findings'][1]='净化80%经验／EV额度／零与nil分开；净化室跨级在首个能力窗口先失败，同等级和遗迹石不共享此缺方法点'
        g['findings'][-1]='替换按原始nil／false相等；蛋例有匹配前提；两种容量失败以实际到达存放为前提'
        g['findings'].append('普通默认Battle M4000／G0必写Hyper真并请求提示，有效Hyper假；正G公式与插件／回放范围分列')
        g['evidence']='WP23 §§5–8、W12/24/33/38/39/43–46；本轮三项回源与targeted-checks'
    if g['id']=='B04':
        g['findings'][1]='净化先清Shadow再恢复经验；可进入等级辅助，但净化室跨级在窗口先失败，不到后续学招／进化；遗迹石等有回调的路径另列'
        g['evidence']='WP22§4/6/7、WP23§5/6/8、WP32§4/5；WP22／WP32限定通过，WP23修订稿尚未外审'
    if g['id']=='B05':
        g['findings'][2]='WP32-N01已CONFIRMED，WP31第114行摘要及必要绑定已有限同步；N02宿主未决保持，未改WP26'
        g['findings'][3]='WP22／WP32按独立首审回填限定Reviewed；WP23仅R01–R03修订后ReviewPending，未自批通过'
        g['evidence']='本轮report§3/4、revision-response与revision-diffs；首稿历史保存在本轮input-snapshot'
    if g['id']=='B06':
        g['findings'][0]='六份被审v1身份留史；当前三主稿／三附表及必要依赖身份级联'
        g['findings'][1]='F06-08 WP22限定Reviewed＋WP23 ReviewPending；F09-04 WP32限定Reviewed，前向Inventoried保留'
        g['findings'][2]=f'{len(boundary["bindings"])}条规格绑定（新增WP55零参数随机合同依据）与磁盘一致，WP23明确未外审'
boundary['matrix']={'path':'planning/feature-matrix.md',**ident(ROOT/'planning/feature-matrix.md')}
boundary['new_observations']={'path':str((D/'new-observations.md').relative_to(ROOT)),**ident(D/'new-observations.md')}
boundary['remaining']=['WP23-R01/R02/R03修订稿待有限复审','WP32-N02宿主重复释放未决','U01–U10及WP78→WP79→WP80']
boundary['revision_history']=[{'version':1,**ident(R/'input-snapshot'/str((D/'boundary-checks.json').relative_to(ROOT))),'note':'首稿被审原件'}, {'version':2,'note':'首审修订/回填与46条当前绑定；未重审已接受行为'}]
save(D/'boundary-checks.json',boundary)

selfcheck=json.loads((D/'self-checks.json').read_text());selfcheck['version']=2
selfcheck['sequential_order']=['13/876 fixed preflight','WP23 R01–R03 source verification','WP31 N01 authorized one-point sync','WP22/WP32 scoped backfill','necessary identity cascade and limited re-review delivery']
selfcheck['packages']=packages;selfcheck['total_scenarios']=sum(len(p['scenarios']) for p in packages)
selfcheck['source_identity_file']={'path':str((D/'source-identities.json').relative_to(ROOT)),**ident(D/'source-identities.json')}
selfcheck['matrix']={'path':'planning/feature-matrix.md',**ident(ROOT/'planning/feature-matrix.md')}
selfcheck['seventeen_requirements']['examples_test_vectors']='WP22 W01–25; WP23 W01–46 (R01/R02/R03 and directly affected premises); WP32 W01–38'
selfcheck['reviewed_set']='WP01–WP22、WP24–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62；各包具名限定静态范围'
selfcheck['new_status']='WP22/WP32 scoped Reviewed after independent PASS_SCOPED; WP23 revised v2 ReviewPending. Main-line next batch not started.'
selfcheck['revision_checks']={'path':str((O/'targeted-checks.json').relative_to(ROOT)),**ident(O/'targeted-checks.json')}
selfcheck['review_history']=[{'version':1,**ident(R/'input-snapshot'/str((D/'self-checks.json').relative_to(ROOT))),'note':'105 cases / 45 bindings at first review; historical only'},{'version':2,'note':'109 cases / 46 bindings; no runtime validation or independent approval of WP23'}]
save(D/'self-checks.json',selfcheck)

summary='''# WP22／WP32限定回填与WP23三项修订 — 有限复审材料 v2

2026-09-30；规格提取方。独立首审结论：**WP22／WP32 PASS_SCOPED，WP23 REQUEST_CHANGES**。本次已回填两包限定Reviewed、回源修订WP23-R01～R03并按授权同步WP31的N01摘要。**WP23仍为ReviewPending（批内修订稿，尚未外审）**，N02宿主行为保留；不进入主线下一批。

## 1. 当前主稿／附表身份

| 包／文件 | 状态 | 完整SHA-256 | 字节 | 场景 |
| --- | --- | --- | ---: | ---: |
'''
for pkg in packages:
    for i,a in enumerate(pkg['artifacts']):
        summary+=f'| {pkg["package"]} [{Path(a["path"]).name}](../../{a["path"]}) | {pkg["status"]}（限定范围） | `{a["sha256"]}` | {a["bytes"]:,} | {len(pkg["scenarios"]) if i==0 else "—"} |\n'
summary+='''
六份被审v1完整身份保留在首审报告§1、各主附表尾注、wp*-fixed的review_history与本轮input-snapshot。当前字节不冒充被审对象。场景25／46／38，共109条，均为静态预期，不是运行测试。

## 2. 修订与确认范围

- R01：净化室跨级恢复的首个能力窗口缺更新回调；明确E1000／S416→目标1332，但失败时已写1331，未到学招／进化／昵称／存放／清中心。补同等级S0、遗迹石对照，并限定O03到达前提。
- R02：替换比较原始Shadow查询结果，nil／false不归一；补三组返回值对照，蛋替换例要求原始值匹配。
- R03：普通默认Battle M4000／G0写存储Hyper真并请求进入提示，有效查询仍假且同前提可重复；不扩到插件、小量表或回放。
- N01：已按独立确认有限同步WP31旧第114行摘要及完整身份引用；N02维持静态双调用／宿主未决，WP26未改。

WP62回填和WP38／C03同步已获本轮受理，本次不再修改它们；WP22／WP32只回填状态、N01同步状态和必要依赖身份，不改变其它已接受行为。

## 3. 核对与材料

'''
for name,label in [('self-checks.json','逐包自检与当前身份'),('boundary-checks.json','六组交界／46条完整绑定'),('new-observations.md','九项观察的独立判定与处理'),('source-identities.json',f'{source["count"]}条来源文件身份；仅具名段语义核对'),('revision-v2/preflight-checks.json','13项与876输入／快照及12轮历史预检'),('revision-v2/targeted-checks.json','固定算术与调用者／原始返回值／G0边界核对')]:
    i=ident(D/name);summary+=f'- [{name}]({name})：{label}；`{i["sha256"]}`，{i["bytes"]:,}字节。\n'
summary+='''
逐项回应及本轮差异见[revision-response](../wp22-wp23-wp32-review-2026-09-30/revision-response.md)与[revision-diffs](../wp22-wp23-wp32-review-2026-09-30/revision-diffs/)；本轮所有差异从**本轮首审input-snapshot**重建至当前目标，不复用更早闭合轮作为新差异基线。旧backfill-response／六份backfill-diff／diff-bindings为第六十三轮历史，保持原件，其目标由本轮快照核对。

当前最终只读登记／哈希／JSON／链接／差异／白名单结果见[validation-results.json](validation-results.json)。本轮仅运行审查过写入范围的自有文本／哈希／固定算术检查，没有运行旧交付生成／登记脚本或参考模型。

## 4. 登记与停止

现有manifest续**第六十四轮**、主TSV续**v39**，保留旧行与历史链；F06-08分别为WP22限定Reviewed、WP23 ReviewPending，F09-04为WP32限定Reviewed，前向范围保留。限定通过集合＝WP01–WP22、WP24–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62；仅各包具名静态范围，不是整个游戏运行通过。

备妥有限复审后停止，不启动主线下一批，不接管用户另行安排的独立工作；未创建任务／Agent、未发其它会话消息、未提交／推送。Demo、宿主、媒体、插件、U01–U10与WP78→WP79→WP80保留。

首稿摘要历史：`b2d16704d7ef0990eab88860c51ccb9c36a088663dd3e3e45604ec0e38808921`，5,299字节；原“三包ReviewPending／105场景”属于首次送审时点，不覆盖本轮状态。
'''
(D/'delivery-summary.md').write_text(summary)
print(json.dumps({'statuses':{p['package']:p['status'] for p in packages},'scenarios':selfcheck['total_scenarios'],'bindings':boundary['binding_count'],'sources':source['count']},ensure_ascii=False))
