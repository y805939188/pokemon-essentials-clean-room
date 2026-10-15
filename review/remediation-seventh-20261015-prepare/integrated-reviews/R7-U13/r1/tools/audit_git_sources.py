"""Compare restored evidence with actual immutable Git objects, not only plans."""
from pathlib import Path
import subprocess,json,datetime
from run_logged import identity
W=Path('/workspace/r7-ir-R7-U13');T=Path(__file__).parent;MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
def git(*a):return subprocess.check_output(['git','-C',str(W/'checkout'),*a])
P=json.loads((W/'actual-plans/R7-U13.json').read_bytes());J=json.loads((W/'actual-input/integration/applied-clauses.json').read_bytes())
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'restored_git_object_checks':[],'tree_checks':[],'additional_reads':[]}
for r in P['artifacts']:
    d=git('show',r['commit']+':'+r['path']);assert d==(W/'actual-input'/r['local_path']).read_bytes()
    mode=git('ls-tree',r['commit'],'--',r['path']).decode().split()[0];assert mode=='100644'
    out['restored_git_object_checks'].append({'commit':r['commit'],'path':r['path'],'local_path':r['local_path'],'identity':identity(d),'mode':mode,'exact':True})
for s in J['source_bindings']:
    for ck,tk in [('candidate_commit','candidate_tree'),('candidate_review_commit','candidate_review_tree')]:
        actual=git('rev-parse',s[ck]+'^{tree}').decode().strip();assert actual==s[tk]
        out['tree_checks'].append({'batch':s['id'],'commit':s[ck],'tree':actual,'exact':True})
for path in ['deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md','deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md','review/remediation-sixth-20261014-prepare/inputs/limit-records.json','review/remediation-sixth-20261014-prepare/inputs/policy-records.json']:
    d=git('show',MI+':'+path);dest=W/'supplemental/actual'/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(d)
    out['additional_reads'].append({'commit':MI,'path':path,'local_path':str(dest),'identity':identity(d)})
(T/'git-source-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'restored_exact_Git_blobs':len(out['restored_git_object_checks']),'candidate_and_review_trees':len(out['tree_checks']),'additional_restored':len(out['additional_reads'])}))
