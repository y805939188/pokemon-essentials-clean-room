#!/usr/bin/env python3
"""Read-only workspace protection checks; optional result file is explicit."""
from pathlib import Path
import subprocess,json,hashlib,datetime,argparse
O=Path(__file__).resolve().parents[1];W=O.parents[2];P=Path('/Users/dingshinn/Desktop/pokemon-framework-reference');R=P/'reference/pokemon-essentials';B='9366d9d17aaeac3b4414236468affa650fb3dd27';RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';pre=str(O.relative_to(W))
def git(root,*args):return subprocess.check_output(['git',*args],cwd=root)
def wtparse(raw):
 out={}
 for block in raw.strip().split('\n\n'):
  if not block:continue
  lines=block.splitlines();path=lines[0].split(' ',1)[1];out[path]=lines[1:]
 return out
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
before=wtparse((O/'evidence/worktrees.before.txt').read_text());after=wtparse(git(P,'worktree','list','--porcelain').decode())
worktree_changes=[]
for path,state in before.items():
 if path==str(W):continue
 if after.get(path)!=state:worktree_changes.append({'path':path,'before':state,'after':after.get(path)})
root_status=git(P,'status','--porcelain=v1','--untracked-files=all').decode();ref_status=git(R,'status','--porcelain=v1','--untracked-files=all').decode();stash=git(P,'stash','list').decode()
corpus=json.loads((O/'corpus-inventory.json').read_text());extra_checks=[]
for q in corpus['local_extras']:
 if q.get('corpus')!='workspace_untracked':continue
 path=P/q['path'];actual=hashlib.sha256(path.read_bytes()).hexdigest()if path.is_file()else None
 extra_checks.append({'path':q['path'],'expected_sha256':q['sha256'],'actual_sha256':actual,'match':actual==q['sha256']})
changed=[x for x in git(W,'diff','--name-only','-z',B,'--').decode().split('\0')if x];staged=[x for x in git(W,'diff','--cached','--name-only','-z','--').decode().split('\0')if x];untracked=[x for x in git(W,'ls-files','--others','--exclude-standard','-z').decode().split('\0')if x]
outside=[p for p in set(changed+staged+untracked)if not p.startswith(pre+'/')]
ident={'original_HEAD':git(P,'rev-parse','HEAD').decode().strip(),'main':git(P,'rev-parse','main').decode().strip(),'origin_main_local':git(P,'rev-parse','origin/main').decode().strip(),'delivery_tag':git(P,'rev-parse','delivery/fourth-round-clean-final-20261012^{commit}').decode().strip(),'formal_tree':git(P,'rev-parse','HEAD:deliverables/final-specification-set').decode().strip(),'reference_HEAD':git(R,'rev-parse','HEAD').decode().strip(),'reference_tree':git(R,'rev-parse','HEAD^{tree}').decode().strip(),'review_branch':git(W,'branch','--show-current').decode().strip(),'review_HEAD':git(W,'rev-parse','HEAD').decode().strip()}
checks={'original_status_exact_before':root_status==(O/'evidence/root_status.before.txt').read_text(),'reference_status_exact_before':ref_status==(O/'evidence/reference_status.before.txt').read_text(),'stash_exact_before':stash==(O/'evidence/stashes.before.txt').read_text(),'original62_byte_identities':len(extra_checks)==62 and all(x['match']for x in extra_checks),'other_worktree_registration_HEADs_unchanged':not worktree_changes,'all_changes_only_report_root':not outside,'B5_protected_refs':all(ident[k]==B for k in ['original_HEAD','main','origin_main_local','delivery_tag']),'formal_subtree_unchanged':ident['formal_tree']=='d5a462b4c6f8b78c3264a25d6b5495230fa265e2','reference_identity_unchanged':ident['reference_HEAD']==RC and ident['reference_tree']=='7589c800b61ba13a13040ed0d686979b80a84fd0','report_branch_expected':ident['review_branch']=='codex/review-fifth-2026-10-13-9366d9d-c7d3'}
d={'schema_version':'gr5.protection.v1','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'passed':all(checks.values()),'identities':ident,'changed_or_staged_paths':len(set(changed+staged)),'report_untracked_paths':len(untracked),'outside_report_changes':outside,'original_extra_files':extra_checks,'other_worktree_changes':worktree_changes,'boundary':'Read-only checks. Other worktree registration/HEAD compare plus no operations there; does not claim every ignored byte in every unrelated checkout was semantically re-audited.'}
Path(args.output).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'passed':d['passed'],'checks':checks,'outside':outside},ensure_ascii=False));raise SystemExit(0 if d['passed']else 1)
