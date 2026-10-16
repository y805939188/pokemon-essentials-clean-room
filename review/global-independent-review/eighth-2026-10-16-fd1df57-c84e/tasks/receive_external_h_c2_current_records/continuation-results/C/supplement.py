"""Restore selected immutable evidence as inert bytes, with both physical identities."""
import gzip,json,subprocess,hashlib
from pathlib import Path
T=Path(__file__).resolve().parent
W=T/'.work'; C2='4580645dfbfec4a3c7ccbad56ae293cc619b0d25'; B='fd1df570cad987dc3852a3b958f03916e317f7fe'
ROOT='review/global-independent-review/seventh-2026-10-14-e646432-7a91/'
def git(*a):return subprocess.check_output(['git','--git-dir='+str(W/'remote.git'),*a])
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def restore(label,commit,path):
 try:raw=git('show',commit+':'+path);data=raw;physical=path
 except subprocess.CalledProcessError:
  assert commit==C2
  index=ROOT+'publication-transport/core/payload-index.json'
  idx=json.loads(git('show',commit+':'+index));r=next(x for x in idx['logical_files'] if x['logical_path']==path.removeprefix(ROOT))
  physical=ROOT+'publication-transport/core/'+r['transport_path'];raw=git('show',commit+':'+physical);data=gzip.decompress(raw)
  assert ident(data)=={'bytes':r['bytes'],'sha256':r['sha256'],'git_blob':r['git_blob_content_id']}
 q=W/'extra'/(label+'.json' if label!='utilstdout' else label);q.parent.mkdir(exist_ok=True);q.write_bytes(data)
 f=T/'supplemental-bindings.json';d=json.loads(f.read_text()) if f.exists() else []
 d.append({'label':label,'commit':commit,'logical_path':path,'physical_path':physical,'physical_tree_entry':git('ls-tree',commit,physical).decode().strip(),'encoded':ident(raw),'decoded':ident(data),'reading_credit':'IDENTITY_ONLY_UNTIL_EXACT_DISPLAY_ACK'});f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');return q
if __name__=='__main__':
 for label,path in [('j01counter','evidence/received-final-proposals/GR7-J01-001/counter-review.json'),('c14counter','tasks/R7-C14/counter-review.json'),('utilreceipt','execution/local-ruby-util03-reference-observation.json'),('utilstdout','execution/util03-ruby.stdout'),('m04facts','tasks/R7-M04/forward-map.json')]:restore(label,C2,ROOT+path)
 restore('utilpolicy','9aa72bc99a4cf52c8fb9cad8a637a963341388b0','review/remediation-sixth-20261014-prepare/inputs/policy-records.json')
 for label,path in [('b8ledger','ledger.json'),('b8decision','closure/final/decision.json'),('b8dependencies','closure/final/dependency-and-history-reception.json')]:restore(label,B,'review/remediation-seventh-20261015-prepare/'+path)
