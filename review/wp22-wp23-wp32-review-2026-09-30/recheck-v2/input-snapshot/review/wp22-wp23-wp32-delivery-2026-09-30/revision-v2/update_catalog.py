"""Append round 64 / main TSV v39 from its frozen round-63 baseline.
Refuses to overwrite an independently changed current catalog. No reference execution.
"""
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'review/wp22-wp23-wp32-delivery-2026-09-30';O=D/'revision-v2'
R=ROOT/'review/wp22-wp23-wp32-review-2026-09-30'
M='planning/review-manifest-2026-09-19.md';T='review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv'
STATE=Path('/tmp/wp23-revision-catalog-state.json')

def ident(p):
    b=p.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}

expected=json.loads(STATE.read_text()) if STATE.exists() else {p:ident(R/'input-snapshot'/p) for p in [M,T]}
for p in [M,T]:assert ident(ROOT/p)==expected[p],f'Catalog independently changed: {p}; preserve and inspect before updating'
old=(R/'input-snapshot'/M).read_text();oldtsv=(R/'input-snapshot'/T).read_text()
head,tail=old.split('## 2.',1)
pat=re.compile(r'^\| `([^`]+)`(.*?)\| `([a-f0-9]{8})` \| `([a-f0-9]{64})` \| ([\d,]+) \|$',re.M)
oldpaths={x[0] for x in pat.findall(head)}
final=json.loads((R/'final-checks.json').read_text())
reviewers=[ROOT/x['path'] for x in final['artifacts']]+[R/'final-checks.json']
newfiles=reviewers+[R/'revision-response.md']+sorted((R/'revision-diffs').glob('*.diff'))+sorted(p for p in O.rglob('*') if p.is_file())
newpaths=sorted({str(p.relative_to(ROOT)) for p in newfiles}-oldpaths)
tsvpaths=[line.split('\t')[2] for line in oldtsv.splitlines() if line and not line.startswith('#')]
for p in newpaths:
    if p not in tsvpaths and p not in [M,T]:tsvpaths.append(p)
t='# 主交付文件哈希（2026-09-30测量；v39；第六十四轮WP23三项修订＋WP22／WP32回填＋N01同步；三列：hash<TAB>bytes<TAB>path）\n# manifest 与 TSV 自身不自哈希；保留v38原778条；历史原件与被审身份留存\n'
for p in tsvpaths:
    i=ident(ROOT/p);t+=f'{i["sha256"]}\t{i["bytes"]}\t{p}\n'
(ROOT/T).write_text(t);tsv=ident(ROOT/T)

changed=json.loads((O/'change-whitelist.json').read_text())['existing_allowed']
notes={p:'第六十四轮首审有限修订／回填及当前身份维护；被审v1留史' for p in changed if p not in [M,T]}
notes['planning/feature-matrix.md']='F06-08 WP22限定Reviewed＋WP23 R01–R03修订v2 ReviewPending；F09-04 WP32限定Reviewed；前向保留'
notes['specs/pokemon-rules/wp31-basic-evolution.md']='WP32-N01独立CONFIRMED后的批准单点摘要同步；继承原限定Reviewed'
notes[T]=f'v39；{len(tsvpaths)}条；原778条保留'
def row(p,note=''):
    i=ident(ROOT/p);a=f'（{note}）' if note else ''
    return f'| `{p}`{a} | `{i["sha256"][:8]}` | `{i["sha256"]}` | {i["bytes"]:,} |'
def replacement(m):
    p=m[1]
    if p in notes:return row(p,notes[p])
    i=ident(ROOT/p);return f'| `{p}`{m[2]}| `{i["sha256"][:8]}` | `{i["sha256"]}` | {i["bytes"]:,} |'
head=pat.sub(replacement,head)
head=re.sub(r'^## 1\..*$', '## 1. 当前有效版本（2026-09-30 WP23三项修订、WP22／WP32限定回填与WP32-N01批准的WP31摘要同步；第六十四轮）',head,flags=re.M)
head=head.rstrip()+'\n'
reviewerpaths={str(p.relative_to(ROOT)) for p in reviewers}
for p in newpaths:
    note='本轮独立首审reviewer原件；未修改' if p in reviewerpaths else '提取侧有限修订回应／差异／自有静态检查；非独立review'
    head+=row(p,note)+'\n'
head+='\n'
body='## 2.'+tail
wp31=ident(ROOT/'specs/pokemon-rules/wp31-basic-evolution.md')
packages=[json.loads((D/f'wp{n}-fixed.json').read_text()) for n in [22,23,32]]
correspondence=f'''\n- 2026-09-30第六十四轮：独立首审报告 `e97d0e677d71e3e6179e483d84e215b835fc46243cb1ed1a6b3e33bcaddc919c`（15,276字节）、修订提示 `84bbaff63954ce96269440aee9c6124dab18b6bf259664c05c9342a11d4d30b7`（9,071字节）：WP22／WP32各PASS_SCOPED、WP23仅R01～R03必修；WP62／WP38与C03受理，N01确认、N02保留宿主未决。13项与876输入／快照及旧12轮快照／原件逐字节匹配，无额外变化。WP23按净化室跨级首次失败／原始nil-false替换门／默认G0写标志与提示修订v2，仍ReviewPending；WP22／WP32主附表按报告§4回填限定Reviewed，被审v1完整身份留史。WP31仅按N01授权同步旧第114行摘要与维护尾注，现 `{wp31['sha256']}`／{wp31['bytes']:,}字节，继承旧限定通过；依赖表实际完整身份级联，不全局替换历史。当前场景25／46／38、46条绑定、66条来源身份；17份新diff相对本轮input-snapshot重建最终目标，旧6份diff只核到首稿快照。主TSV v39 `{tsv['sha256']}`／{tsv['bytes']:,}字节、{len(tsvpaths)}条，新增{len(newpaths)}条，原874／778行保留。统一有限复审材料见本轮revision-response；不进入主线下一批，不接管独立并行工作。\n\n'''
body=body.replace('## 3. 历史条目（已被替代，仅供追溯）',correspondence+'## 3. 历史条目（已被替代，仅供追溯）',1)
history='\n<!-- 第六十四轮追加身份替代链；旧历史不覆盖 -->\n\n'
for p in changed:
    oldid=ident(R/'input-snapshot'/p)
    if p==M:after='续第六十四轮；本清单不自哈希，最终身份从磁盘测量'
    else:
        now=ident(ROOT/p);after=f'被 `{now["sha256"]}` 替代（{now["bytes"]:,}字节，本轮当前；新字节不冒充本轮被审对象）'
    history+=f'| `{p}` | `{oldid["sha256"][:8]}` | 第六十四轮有限修订／回填 | 固定输入 `{oldid["sha256"]}`（{oldid["bytes"]:,}字节）留史；{after} |\n'
history+='\n'
body=body.replace('## 4. 2026-09-19 修订与交付摘要（按轮次）',history+'## 4. 2026-09-19 修订与交付摘要（按轮次）',1)
body+='\n**第六十四轮（WP23三项修订＋WP22／WP32限定回填＋N01同步；2026-09-30）**：\n\n'
body+='- **预检与保护**：13项完整身份／字节、876项输入与快照、本轮原件及旧828／806／782／755／734／707／677／644／613／589／548／521快照均匹配；18,342个预存文件基线核对，reference固定且普通Git清洁；旧reviewer／回应／差异与全部快照不覆盖。\n'
body+='- **WP23 R01–R03**：跨级净化室先缺窗口更新回调（E1000／S416，目标1332但失败时已写1331且中心保留），同等级与遗迹石分列；替换比较原始nil／false而非布尔归一，蛋例补匹配前提；普通默认M4000／G0写存储Hyper真与提示而有效假，可重复。主体／附表／W12、W24、W33、W38／W39及W43–46、self／boundary／O03／O04同步，仍ReviewPending，未自批关闭。\n'
for pkg in packages:
    fixed='；'.join(f'`{a["path"]}` `{a["sha256"]}`／{a["bytes"]:,}字节' for a in pkg['artifacts'])
    body+=f'- **{pkg["package"]}当前身份**：{fixed}；{pkg["status"]}（具名范围），{len(pkg["scenarios"])}场景；被审v1主附表身份留史。\n'
body+=f'- **N01／登记**：WP31单点批准同步 `{wp31["sha256"]}`／{wp31["bytes"]:,}字节；N02只确认静态双调用，宿主重复释放保留，未改WP26。新增{len(newpaths)}行＝本轮reviewer16件＋回应1＋diff17＋本轮审计材料；manifest当前{len(oldpaths)+len(newpaths)}条可核身份、主TSV v39 {len(tsvpaths)}条 `{tsv["sha256"]}`／{tsv["bytes"]:,}字节；原874／778行与旧替代链保留。最终全量身份／JSON／链接／绑定／差异／876白名单与保护范围结果见活动validation-results.json；不制造自哈希循环。\n'
body+='- **通过与停止**：本主线限定通过集合为WP01–WP22、WP24–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62；WP23修订稿待有限复审，不把F06-08整行算完成。Demo／宿主／媒体／插件、U01–U10及WP78→WP79→WP80保持。完成有限修订送审后停止，不启动下一批，不接管另行安排的独立任务，不创建Agent／任务、不发送其它会话消息、不提交推送。\n'
(ROOT/M).write_text(head+body)
state={p:ident(ROOT/p) for p in [M,T]};STATE.write_text(json.dumps(state))
print(json.dumps({'manifest':state[M],'TSV':state[T],'manifest_rows':len(oldpaths)+len(newpaths),'TSV_rows':len(tsvpaths),'added':len(newpaths),'reviewer_originals':len(reviewers)},ensure_ascii=False,indent=2))
