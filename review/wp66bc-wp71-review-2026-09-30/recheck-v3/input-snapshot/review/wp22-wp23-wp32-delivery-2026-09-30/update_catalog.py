"""Continue existing manifest and main TSV, preserving their frozen prior history."""
from pathlib import Path
import re, hashlib, json

ROOT=Path(__file__).resolve().parents[2]
D=Path(__file__).resolve().parent
C=ROOT/'review/wp58-wp62-wp38-review-2026-09-30/closure-review'
M='planning/review-manifest-2026-09-19.md'
T='review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv'

def identity(p):
    b=p.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}

old=(C/'input-snapshot'/M).read_text()
old_tsv=(C/'input-snapshot'/T).read_text()
pat=re.compile(r'^\| `([^`]+)`(.*?)\| `([a-f0-9]{8})` \| `([a-f0-9]{64})` \| ([\d,]+) \|$',re.M)
head,tail=old.split('## 2.',1)
old_paths={m[0] for m in pat.findall(head)}
new_files=sorted(p for p in C.iterdir() if p.is_file())
new_files+=sorted(p for p in D.rglob('*') if p.is_file())
packages=[json.loads((D/f'wp{n}-fixed.json').read_text()) for n in [22,23,32]]
new_files+=[ROOT/a['path'] for p in packages for a in p['artifacts']]
new_paths=sorted(set(str(p.relative_to(ROOT)) for p in new_files)-old_paths)
assert len(list(C.glob('*')))>0

descriptions={
 'planning/feature-matrix.md':'F15-01 WP62管理回填Reviewed；F06-08 WP22／WP23与F09-04 WP32具名ReviewPending；保留前向范围',
 'specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md':'WP62闭合PASS_SCOPED后限定Reviewed管理回填；被审v3留史',
 'specs/pokemon-rules/wp38-capture-and-receiving.md':'WP38已受理限定Reviewed；WP62回填后引用及W07历史记法管理同步',
 'review/wp58-wp62-wp38-delivery-2026-09-29/delivery-summary.md':'活动摘要v4；WP62／C03管理同步，旧修订历史保留',
 'review/wp58-wp62-wp38-delivery-2026-09-29/self-checks.json':'活动self v4；当前身份同步，历史ReviewPending保留',
 'review/wp58-wp62-wp38-delivery-2026-09-29/boundary-checks.json':'活动boundary v4；C03及WP62限定通过绑定同步'}

tsv_rows=[]
for line in old_tsv.splitlines():
    if not line or line.startswith('#'):continue
    sha,size,path=line.split('\t');tsv_rows.append(path)
for path in new_paths:
    if path not in tsv_rows and path not in [M,T]:tsv_rows.append(path)
ttext='# WP18–WP62及WP22／23／32交付文件哈希（2026-09-30测量；v38；第六十三轮；三列：hash<TAB>bytes<TAB>path）\n# manifest 与 TSV 自身不自哈希；保留原v37全部730条，新增闭合reviewer原件与本批材料\n'
for path in tsv_rows:
    x=identity(ROOT/path);ttext+=f'{x["sha256"]}\t{x["bytes"]}\t{path}\n'
(ROOT/T).write_text(ttext)
descriptions[T]=f'v38；{len(tsv_rows)}条；原730条保留'

def row(path,note=''):
    x=identity(ROOT/path);a=f'（{note}）' if note else ''
    return f'| `{path}`{a} | `{x["sha256"][:8]}` | `{x["sha256"]}` | {x["bytes"]:,} |'

def replace(m):
    path=m[1]
    if path in descriptions:return row(path,descriptions[path])
    x=identity(ROOT/path)
    return f'| `{path}`{m[2]}| `{x["sha256"][:8]}` | `{x["sha256"]}` | {x["bytes"]:,} |'

head=pat.sub(replace,head)
head=re.sub(r'^## 1\..*$', '## 1. 当前有效版本（2026-09-30 WP62管理回填与WP22→WP23→WP32统一交付；第六十三轮）',head,flags=re.M)
head=head.rstrip()+'\n'
for path in new_paths:
    if path.startswith(str(C.relative_to(ROOT))):note='独立闭合轮原件；本次仅补登、未修改'
    elif path.startswith('specs/'):note='新批首稿v1；ReviewPending，批内固定版本，尚未外审'
    else:note='WP22／23／32提取侧交付及自有静态审计材料；非独立review'
    head+=row(path,note)+'\n'
head+='\n'

pre=json.loads((D/'preflight-checks.json').read_text())
oldids={r['path']:{k:r[k] for k in ['sha256','bytes']} for r in pre['report_section1_nine']}
newids={a['path']:a for p in packages for a in p['artifacts']}
wp62=identity(ROOT/'specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md')
wp38=identity(ROOT/'specs/pokemon-rules/wp38-capture-and-receiving.md')
tsv=identity(ROOT/T)
correspondence=f'''\n- 2026-09-30第六十三轮：依据闭合短复审报告 `867087b0b7f036b0b794250a9894d026b43f6fcdca1cf3df5ac16798b1d1d704`（10,212字节）及执行提示 `46a97f4fa40ba6f7126febac66d2a4d93b3e8cce01f31dbc1a6f69e277d6a019`（13,536字节），原15项与C01-2／C02全部关闭、WP58／WP38回填受理。全部9项固定身份及828项输入／快照、12份依赖与旧11轮快照／原件复测一致；无额外磁盘变化。WP62被审v3 `e38812c8057fd3348c10319c29240ef6e21e72f37c769601f6e1d86bb0d56639`（32,378字节）获PASS_SCOPED，本次管理回填为 `{wp62['sha256']}`（{wp62['bytes']:,}字节）；WP38引用／状态维护后 `{wp38['sha256']}`（{wp38['bytes']:,}字节），不重写捕获算法，WP58字节不变。旧批活动v4与C03同步、历史ReviewPending保留。串行WP22→WP23→WP32固定三主稿＋三附表（25／42／38场景，均ReviewPending），45条依赖绑定、9项新观察（WP32-N01旧摘要过窄单列、不默改）。六份差异相对闭合快照绑定最终目标；矩阵同时含管理回填与新批具名子范围。当前主TSV v38 `{tsv['sha256']}`（{tsv['bytes']:,}字节，{len(tsv_rows)}条）；本轮材料见 `review/wp22-wp23-wp32-delivery-2026-09-30/`。不自批新包Reviewed；不启动第四包。\n\n'''
body='## 2.'+tail
body=body.replace('## 3. 历史条目（已被替代，仅供追溯）',correspondence+'## 3. 历史条目（已被替代，仅供追溯）',1)
history='\n<!-- 第六十三轮追加身份链；此前原文与勘误不覆盖 -->\n\n'
for path in json.loads((D/'change-whitelist.json').read_text())['existing_allowed']:
    previous=identity(C/'input-snapshot'/path)
    if path==M:
        after='第六十三轮继续登记；本文件不自哈希，最终完整身份在交付后由磁盘复测'
    else:
        now=identity(ROOT/path);after=f'被 `{now["sha256"]}` 替代（{now["bytes"]:,}字节，本轮当前；新字节不冒充旧被审对象）'
    history+=f'| `{path}` | `{previous["sha256"][:8]}` | 2026-09-30第六十三轮管理／交付续记 | 旧完整身份 `{previous["sha256"]}`（{previous["bytes"]:,}字节，闭合轮输入）保留；{after} |\n'
for path,a in newids.items():
    history+=f'| `{path}` | 无历史被审版 | 第六十三轮首稿v1 | 固定 `{a["sha256"]}`（{a["bytes"]:,}字节）；ReviewPending，批内固定版本，尚未外审 |\n'
history+='\n'
body=body.replace('## 4. 2026-09-19 修订与交付摘要（按轮次）',history+'## 4. 2026-09-19 修订与交付摘要（按轮次）',1)
body+='''\n**第六十三轮（WP62管理回填／C03→WP22→WP23→WP32；2026-09-30）**：\n\n'''
body+=f'- **固定／回填**：9项与828输入／快照一致；旧11轮快照／reviewer原件及两轮提取回应／差异保护。WP62按闭合报告A～F限定Reviewed管理回填；WP38仅必要状态／身份／W07历史记法同步，WP58不变。C03两条活动简写关闭；旧revision_history不全局替换。\n'
for pkg in packages:
    text='；'.join(f'`{a["path"]}` `{a["sha256"]}`／{a["bytes"]:,}字节' for a in pkg['artifacts'])
    body+=f'- **{pkg["package"]}**：{text}；{len(pkg["scenarios"])}条静态场景；ReviewPending（首稿v1，批内固定，尚未外审）。\n'
body+=f'- **登记／检查**：新增{len(new_paths)}条，manifest当前{len(old_paths)+len(new_paths)}条可核身份（原826条保留）；主TSV v38 {len(tsv_rows)}条（原730条保留），`{tsv["sha256"]}`／{tsv["bytes"]:,}字节。新增闭合reviewer15件、三主稿三附表与自有回填／摘要／self／boundary／来源身份／差异及检查材料。六份差异绑定最终目标，矩阵增量已纳入；45条完整依赖绑定。最终全量只读结果见本批validation-results.json；哈希、JSON／链接、差异重建与语义场景分别计量，不把计数当行为正确性证明。\n'
body+='- **新观察／停止**：WP32-N01关于WP31第114行计数目标范围单列待审，旧稿未改；另外8项本包观察／宿主未决保持。既有限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62；新三包不加Reviewed。Demo／宿主／媒体／插件、U01–U10、WP78→WP79→WP80保留。统一送审材料备妥后停止，不启动第四包、不创建任务／Agent、不发reviewer消息、不提交推送。\n'
(ROOT/M).write_text(head+body)
print(json.dumps({'manifest':identity(ROOT/M),'manifest_rows':len(old_paths)+len(new_paths),
 'TSV':tsv,'TSV_rows':len(tsv_rows),'added_rows':len(new_paths),'new_paths':new_paths},ensure_ascii=False,indent=2))
