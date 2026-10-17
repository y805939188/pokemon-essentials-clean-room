#!/usr/bin/env python3
"""Validate document identity, scope and preservation; no Ruby/game/model execution."""
from pathlib import Path
import json,hashlib,subprocess,re,collections,datetime,difflib,posixpath
root=Path(__file__).resolve().parents[5];e=Path(__file__).resolve().parent;c=e.parent;prefix=c.relative_to(root).as_posix()+'/'
fixed='4575e80d041ab0c74a42e2e36399d05791dbaa5b';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';RR='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
def git(*args,repo=root):return subprocess.check_output(['git','-C',str(repo),*args])
def source(rev,path,repo=root):return git('show',rev+':'+path,repo=repo)
def sha(b):return hashlib.sha256(b).hexdigest()
a=next(x for x in json.loads((root/RR/'handoff/batch-assignment.json').read_text())['batches'] if x['id']=='R8-U04'); targets=a['actual_target_write_set'];candidates=a['candidate_write_set']
assert git('branch','--show-current').decode().strip()=='revise/r8-u04-20261017'
assert git('merge-base',fixed,'HEAD').decode().strip()==fixed
assert git('rev-parse','HEAD',repo=Path('/workspace/pokemon-essentials')).decode().strip()==R
assert not git('status','--porcelain',repo=Path('/workspace/pokemon-essentials'))
# Include tracked and untracked paths. All author work must be inside this batch.
changed=set(git('diff','--name-only',fixed).decode().splitlines())|set(git('ls-files','--others','--exclude-standard').decode().splitlines())
assert all(p.startswith(prefix) for p in changed), sorted(changed)
actual={p.relative_to(root).as_posix() for p in (c/'mirror').rglob('*') if p.is_file()};assert actual==set(candidates),(actual,candidates)
for target in targets:
 assert (root/target).read_bytes()==source(fixed,target)==source('fd1df570cad987dc3852a3b958f03916e317f7fe',target),target
units=json.loads((e/'input-identities.json').read_text())
for u in units:
 b=source(u['commit'],u['path'],Path(u['repo']));assert len(b)==u['bytes'] and sha(b)==u['sha256'];assert git('rev-parse',u['commit']+':'+u['path'],repo=Path(u['repo'])).decode().strip()==u['blob']
assert len(units)==40
ci=json.loads((e/'contract-input-identities.json').read_text())
for u in ci['inputs']:
 b=source(fixed,u['path']);assert len(b)==u['bytes'] and sha(b)==u['sha256']
ld=json.loads((e/'reading-ledger.json').read_text());assert len(ld['source_spec_units'])==40 and all(u['complete_contiguous_source_or_formal_read'] for u in ld['source_spec_units'])
# Preserve all original catalogue rows exactly except the required MP13 correction.
cat=next(t for t in targets if '/test-catalog/' in t);old=source(fixed,cat).decode();new=(c/'mirror'/cat).read_text();oldlines=old.splitlines();newlines=new.splitlines()
changed_old=[l for l in oldlines if l not in newlines];assert len(changed_old)==1 and changed_old[0].startswith('| MP13 |'),changed_old
oldrows=[l for l in oldlines if l.startswith('|') and not l.startswith('| MP13 |')];newrows=collections.Counter(l for l in newlines if l.startswith('|'));assert all(newrows[l]>=n for l,n in collections.Counter(oldrows).items())
new_ids=re.findall(r'^\| (R8-[A-Z]+\d+) \|',new,re.M);expected=['R8-PBS01']+['R8-NP%02d'%i for i in range(1,6)]+['R8-RP%02d'%i for i in range(1,9)]+['R8-JT%02d'%i for i in range(1,7)]+['R8-CE%02d'%i for i in range(1,6)]+['R8-LB%02d'%i for i in range(1,6)];assert new_ids==expected and len(new_ids)==len(set(new_ids))==30
matrix=next(t for t in targets if 'interpreter-command-matrix' in t);mold=source(fixed,matrix).decode();mnew=(c/'mirror'/matrix).read_text();oldcmd={int(m.group(1)):l for l in mold.splitlines() if (m:=re.match(r'^\| (\d+) \|',l))};newcmd={int(m.group(1)):l for l in mnew.splitlines() if (m:=re.match(r'^\| (\d+) \|',l))};assert set(oldcmd)==set(newcmd) and len(oldcmd)==96
assert {k for k in oldcmd if oldcmd[k]!=newcmd[k]}=={117,119}
assert all(l in mnew for l in mold.splitlines() if l.startswith('| 空操作 |') or l.startswith('| 标记 |') or l.startswith('| 其他实现入口 |') or l.startswith('| 合计分派命令 |'))
# Markdown links resolve in the virtual integrated tree: this batch's mirror over fixed input.
newlinks=[];anchors=[]
for t in targets:
 text=(c/'mirror'/t).read_text();original=source(fixed,t).decode();ids=re.findall(r'<a id="([^"]+)"',text);assert len(ids)==len(set(ids)),t
 anchors.extend({'target':t,'anchor':i} for i in ids if i.startswith('r8-'))
 for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
  if href in re.findall(r'\[[^\]]*\]\(([^)]+)\)',original) or '://' in href:continue
  path,sep,anchor=href.partition('#');dest=posixpath.normpath(posixpath.join(posixpath.dirname(t),path)) if path else t
  b=(c/'mirror'/dest).read_bytes() if dest in targets else source(fixed,dest)
  if anchor:assert f'id="{anchor}"' in b.decode(),(t,href)
  newlinks.append({'from':t,'href':href,'virtual_target':dest})
 # no-index diff uses exit1 for different files; whitespace diagnostics must be empty
 p=subprocess.run(['git','diff','--no-index','--check',str(root/t),str(c/'mirror'/t)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 assert p.returncode in (0,1) and not p.stdout and not p.stderr,(t,p.returncode,p.stdout,p.stderr)
# Verify composed whole-file reading has a contiguous partition of all final lines.
composition=json.loads((e/'final-composition.json').read_text())
for f in composition['files']:
 old=source(fixed,f['target']).decode().splitlines(True);new=(root/f['candidate']).read_text().splitlines(True);cursor=1
 for s in f['segments']:
  assert s['final_line_start']==cursor;s1=s['original_line_start']-1;s2=s['original_line_end_exclusive']-1;t1=s['final_line_start']-1;t2=s['final_line_end_exclusive']-1
  if s['kind']=='equal':assert old[s1:s2]==new[t1:t2]
  cursor=s['final_line_end_exclusive']
 assert cursor==len(new)+1==f['final_lines']+1
issues=json.loads((e/'issue-dispositions.json').read_text())['records'];assert {x['id'] for x in issues}==set(a['required_ids'])
for x in issues:
 for v in x['vectors']:assert v in new_ids
 for ref in x['references']:
  u=next(u for u in units if u['evidence_id']==ref['evidence_id']);n=len(source(u['commit'],u['path'],Path(u['repo'])).splitlines());assert 1<=ref['lines_inclusive'][0]<=ref['lines_inclusive'][1]<=n
for p in e.rglob('*.json'):json.loads(p.read_text())
for p in e.rglob('*.jsonl'):
 for line in p.read_text().splitlines():json.loads(line)
manifest=[]
for t in targets:
 p=c/'mirror'/t;b=p.read_bytes();base=source(fixed,t);manifest.append({'candidate':p.relative_to(root).as_posix(),'target':t,'mode':'100644','bytes':len(b),'sha256':sha(b),'blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'base_bytes':len(base),'base_sha256':sha(base),'base_blob':git('rev-parse',fixed+':'+t).decode().strip()})
(e/'candidate-manifest.json').write_text(json.dumps({'schema':'r8-u04-six-file-candidate-manifest/v1','base':fixed,'branch':'revise/r8-u04-20261017','files':manifest,'meaning':'只绑定六镜像内容，所在commit由外部完整SHA绑定，不写自身未来hash。','business_execution':'NOT_EXECUTED'},ensure_ascii=False,indent=2)+'\n')
report={'schema':'r8-u04-static-document-validation/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'PASS_TOOL_VALIDATION_ONLY','base_commit':fixed,'branch':git('branch','--show-current').decode().strip(),'source_units_verified':40,'contract_inputs_verified':len(ci['inputs']),'mirror_files':6,'formal_targets_equal_fixed_B8':6,'old_catalog_all_rows_preserved_except_required_MP13':True,'new_static_vector_count':30,'old_command_id_set_preserved':96,'changed_command_rows':[117,119],'old_classification':'96 = 28 + 2 + 66 unchanged','new_relative_links':newlinks,'new_anchors':anchors,'whole_final_composed_coverage':6,'required_disposition_count':6,'write_boundary':'exclusive R8-U04 mirror/evidence only','reference_fixed_and_clean':True,'checks_not_proving':'不证明游戏行为、静态预期执行、宿主、编译/保存/载入成功或任何独立验收。','business_execution':'NOT_EXECUTED','candidate_independent_PASS':'PENDING_NONAUTHOR'}
(e/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
