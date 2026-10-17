#!/usr/bin/env python3
"""Review-output validation, preserving exact Git diff evidence whitespace."""
from pathlib import Path
import ast,hashlib,json,re,subprocess
O=Path(__file__).resolve().parent;R=O.parents[1];E=O/'evidence';prefix=O.relative_to(R).as_posix()+'/'
def sha(b):return hashlib.sha256(b).hexdigest()
jsons=[];scripts=[]
for p in sorted(O.rglob('*')):
 if not p.is_file():continue
 if p.suffix=='.json':json.loads(p.read_text());jsons.append(p.relative_to(O).as_posix())
 if p.suffix=='.py':ast.parse(p.read_text());scripts.append(p.relative_to(O).as_posix())
links=[]
for label,target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',(O/'REPORT.md').read_text()):
 assert (O/target).is_file(),target;links.append(target)
assert not subprocess.check_output(['git','diff','--name-only'],cwd=R)
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=R).decode().splitlines()
assert all(line.startswith('?? '+prefix)for line in status),status
exceptions=[]
manifest=json.loads((R/'planning/implementation-routing/r8-20261017/routing-manifest.json').read_text());features={x['feature_id']:x for x in manifest['features']}
for p in sorted(O.rglob('*')):
 if not p.is_file()or p.suffix in ['.gz']:continue
 b=p.read_bytes();text=b.decode();trailing=[i for i,line in enumerate(text.splitlines(),1)if line.rstrip()!=line];endblank=text.endswith('\n\n')
 if trailing or endblank:
  if p.name=='ev-effective-readset.txt':
   doc=None;checked=0
   for line in text.splitlines():
    if line.startswith('CURRENT '):doc=line.split(' ',2)[2]
    elif line.startswith('CONSUMER '):doc=features[line.split()[1]]['source']['document']
    elif line.startswith('CATALOG '):doc=line.split(' ',1)[1]
    elif re.match(r'^\d+: ',line):
     n,body=line.split(': ',1);raw=subprocess.check_output(['git','show','5f87743293290de2e219ecdd6c19e88280f60c9a:'+doc],cwd=R).decode().splitlines();assert raw[int(n)-1]==body;checked+=1
   for i in trailing:assert re.fullmatch(r'\d+: ',text.splitlines()[i-1])
   exceptions.append({'path':p.relative_to(O).as_posix(),'sha256':sha(b),'numbered_blank_source_lines':trailing,'all_numbered_source_lines_rechecked':checked,'treatment':'PRESERVE_NUMBERED_EMPTY_SOURCE_LINES; prefix colon-space is evidence formatting.'})
  else:
   assert p.suffix=='.diff', (str(p),trailing,endblank)
   # Complete raw patch evidence has whitespace-only context records by design.
   for i in trailing:assert text.splitlines()[i-1]==' ',(str(p),i)
   exceptions.append({'path':p.relative_to(O).as_posix(),'sha256':sha(b),'raw_patch_context_space_lines':trailing,'final_blank':endblank,'treatment':'PRESERVE_FIXED_GIT_DIFF_BYTES; these are context record markers, not document trailing spaces.'})
result={'json_parsed':jsons,'python_ast_parsed':scripts,'all_REPORT_links_exist':links,'all_untracked_paths_in_exclusive_review_prefix':True,'tracked_candidate_diff_empty':True,'raw_evidence_whitespace_exceptions':exceptions,'result':'PASS_OUTPUT_VALIDATION'}
(E/'output-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'json_files':len(jsons),'scripts':len(scripts),'report_links':len(links),'raw_patch_exceptions':len(exceptions),'result':'PASS'}))
