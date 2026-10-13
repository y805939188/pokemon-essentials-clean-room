#!/usr/bin/env python3
"""Rebuild documentation mirrors, shared proposals and a review patch from B5.

No source/game execution. Writes only this author directory and --projection-root.
"""
import argparse, difflib, hashlib, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=next(p for p in ROOT.parents if (p/'.git').exists())
FREEZE='22fba7786b0090a1955ce6211315b0036cddfbcd'
B5='9366d9d17aaeac3b4414236468affa650fb3dd27'
CONTRACT='review/remediation-fifth-20261013-prepare/contracts/R5-U02/contract.json'
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def identity(data):
 return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
def write(path,data):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
def dump(path,data):write(path,(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode())
def main():
 p=argparse.ArgumentParser();p.add_argument('--projection-root',default='/tmp/r5-u02-projection');args=p.parse_args()
 scratch=Path(args.projection_root).resolve()
 if not str(scratch).startswith(('/tmp/','/workspace/')) or scratch==REPO or REPO in scratch.parents:raise SystemExit('Projection must be an authorized scratch directory outside repository.')
 c=json.loads(git('show',FREEZE+':'+CONTRACT));d=json.loads((ROOT/'edits.json').read_text());assert d['baseline']==B5
 groups={}
 for op in d['operations']:
  assert op['target'] in c['batch']['allowed_formal_files']
  for finding in op['finding_ids']:assert op['target'] in c['per_finding_formal_permissions'][finding]
  groups.setdefault(op['target'],[]).append(op)
 patch=[];fragments=[];projections=[]
 for target,ops in sorted(groups.items()):
  baseline=git('show',B5+':'+target);original=baseline.decode();updated=original
  for op in ops:
   assert updated.count(op['before'])==1,(op['id'],'exact anchor conflict')
   updated=updated.replace(op['before'],op['after'],1)
  output=updated.encode();write(scratch/target,output)
  patch.extend(difflib.unified_diff(original.splitlines(keepends=True),updated.splitlines(keepends=True),fromfile='a/'+target,tofile='b/'+target))
  mode='direct-mirror' if target in c['candidate_direct_mirrors'] else 'shared-proposal'
  projections.append(dict(target=target,mode=mode,baseline=identity(baseline),projected=identity(output),operations=[o['id'] for o in ops],finding_ids=sorted({f for o in ops for f in o['finding_ids']})))
  if mode=='direct-mirror':write(REPO/c['candidate_direct_mirrors'][target],output)
  else:
   dest=REPO/c['shared_fragment_outputs'][target]
   text='# R5-U02共享候选片段\n\n实际写者：R5-I。B5 '+B5+'；目标 `'+target+'`。整合接受门R5-U01仍WAIT；独立候选复审未签。按edits.json顺序应用精确锚点，不覆盖其它批次贡献。\n'
   for op in ops:
    start=original.index(op['before']);line=original[:start].count('\n')+1
    text+='\n## '+op['id']+'\n\n所属：'+', '.join(op['finding_ids'])+'。操作：替换B5精确锚点，起始行'+str(line)+'；锚点SHA256 '+hashlib.sha256(op['before'].encode()).hexdigest()+'。\n\n原正确行为：'+op['preserved']+'\n\n<!-- BEGIN '+op['id']+' -->\n'+op['after']+'\n<!-- END '+op['id']+' -->\n'
    fragments.append(dict(fragment_id=op['id'],target=target,payload_path=str(dest.relative_to(REPO)),payload_marker=op['id'],operation='replace_exact_anchor',baseline_commit=B5,baseline_file=identity(baseline),baseline_start_line=line,before=op['before'],anchor_sha256=hashlib.sha256(op['before'].encode()).hexdigest(),replacement_sha256=hashlib.sha256(op['after'].encode()).hexdigest(),replacement_bytes=len(op['after'].encode()),finding_ids=op['finding_ids'],dependencies=[dict(batch='R5-U01',status='WAIT')],preserved=op['preserved'],conflict_policy='If B5 anchor changed by another accepted contribution, R5-I must resolve overlap with owners and independently review resulting actual bytes; never apply a whole-file replacement.'))
   write(dest,text.encode())
 write(ROOT/'formal-diff.patch',''.join(patch).encode())
 dump(ROOT/'fragment-manifest.json',dict(schema='r5-u02.shared-fragment-manifest.v1',actual_writer='R5-I',baseline_commit=B5,fragments=fragments,projection_files=projections))
 print(json.dumps(dict(documentation_files=len(groups),direct_mirrors=sum(x['mode']=='direct-mirror' for x in projections),shared_targets=sum(x['mode']=='shared-proposal' for x in projections),fragments=len(fragments),evidence_level='TOOL_VALIDATION',new_behavior_execution=0)))
if __name__=='__main__':main()
