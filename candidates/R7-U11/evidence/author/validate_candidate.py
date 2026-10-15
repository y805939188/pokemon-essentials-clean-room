"""Check containment, exact B preservation and bounded clause contributions; not a behavior model."""
from pathlib import Path
import difflib,hashlib,json,re,subprocess
B='e646432c644dec04d306842cc5a559a29c718fbc'; ROOT=Path('candidates/R7-U11');E=ROOT/'evidence/author'
recipe=json.loads((E/'edits.json').read_bytes()); results=[]
def section(t,start,end):return t[t.index(start):t.index(end)]
for row in recipe['mirrors']:
 p=row['formal_path']; old=subprocess.check_output(['git','show',B+':'+p]);new=Path(row['path']).read_bytes();ot=old.decode();nt=new.decode()
 assert Path(p).read_bytes()==old,('formal changed',p)
 assert len(new)==row['new']['bytes'] and hashlib.sha256(new).hexdigest()==row['new']['sha256']
 if '/demo-dx/' in p:
  rebuilt=ot
  for c in recipe['changes']:
   if c['scope'].startswith(('§1 ','§3.2','§14 ','§16-6','§17 ')):
    assert rebuilt.count(c['old'])==1;rebuilt=rebuilt.replace(c['old'],c['new'],1)
  assert rebuilt==nt,'WP75 edit recipe mismatch'
  assert section(ot,'### 12.4','## 13.')==section(nt,'### 12.4','## 13.')
  assert ot[ot.index('## 18.'):]==nt[nt.index('## 18.'):]
  assert '装载器脚本（可静态解码读取但不执行' not in section(nt,'6. 停用/不可达：','7. 训练家检查副作用：')
  results.append('WP75: exact approved edits only; §12.4/§18 byte-preserved')
 elif '/test-catalog/' in p:
  assert new.startswith(old)
  a=[x for x in ot.splitlines() if x.startswith('| CV-M29 |')];assert a==[x for x in nt.splitlines() if x.startswith('| CV-M29 |')]
  ids=re.findall(r'^\| (R7-U11-EXT-\d\d) \|',nt,re.M);assert ids==[f'R7-U11-EXT-{i:02}' for i in range(1,13)]
  results.append('Catalog: all B bytes preserved as prefix; 12 derived NOT_EXECUTED cases appended')
 elif p.startswith('audit/'):
  c=next(c for c in recipe['changes'] if c['scope'].startswith('T-WP75'))
  assert ot.replace(c['old'],c['new'],1)==nt
  assert section(ot,'### T-WP75-01','\n### T-WP76-01') in section(nt,'### T-WP75-01','\n### T-WP76-01')
  results.append('Audit: original T-WP75-01 table unchanged; one separate evidence paragraph appended')
 else:
  olds=ot.splitlines(True);news=nt.splitlines(True);assert len(olds)==len(news)
  changed=[i+1 for i,(a,b) in enumerate(zip(olds,news)) if a!=b];assert changed==[259]
  assert olds[258].split('|')[1:-2]==news[258].split('|')[1:-2]
  results.append('Matrix: only F18-04 line259 note changes; historical status cells preserved')
 diff=''.join(difflib.unified_diff(ot.splitlines(True),nt.splitlines(True),fromfile='B/'+p,tofile=row['path'],n=0))
 (E/(p.replace('/','__')+'.diff')).write_text(diff)
# Whole tracked working tree is still B. New paths must all be in this batch.
assert subprocess.check_output(['git','diff',B,'--name-only']).strip()==b''
untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard','-z']).decode().split('\0')
assert all(not p or p.startswith('candidates/R7-U11/') for p in untracked)
assert not (ROOT/'specs').exists()
# Table cells must not be silently split by an extra pipe.
for row in recipe['mirrors']:
 for line in Path(row['path']).read_text().splitlines():
  if line.startswith('| R7-U11-EXT-'):assert line.count('|')==4
out={'schema':'r7.u11.author-validation.v1','stage':'TOOL_VALIDATION','result':'AUTHOR_CONTAINMENT_AND_PRESERVATION_CHECKS_OK','checks':results,'formal_tracked_diff_from_B':[],'conditional_mirror':'NOT_CREATED','source_execution':0,'native_API_execution':0,'host_Demo_replay':0,'independent_candidate_review':'PENDING_R7_I_FROZEN_INPUT','acceptance':'NOT_ASSERTED'}
(E/'validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2))
