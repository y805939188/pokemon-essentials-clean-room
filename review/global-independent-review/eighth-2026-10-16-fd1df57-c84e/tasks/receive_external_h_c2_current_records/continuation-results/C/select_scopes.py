"""Lossless field selection, with original pointer mapping; no acceptance inference."""
from pathlib import Path
import json,hashlib
T=Path(__file__).resolve().parent
W=T/'.work'
IDS=['GR7-H08-001','GR7-M13-003','GR7-M15-002','GR7-D06-001','GR7-M04-101','GR7-D07-001','GR7-J01-001','GR7-H14-001','GR7-POL-001','GR7-J16-001','GR7-J16-003']
bindings=[]
def select(label,keys,arraykey):
 path=W/'extra'/(label+'.json');d=json.loads(path.read_text());v={k:d[k] for k in keys if k in d}
 pointers={k:'/'+k for k in v}
 v[arraykey]=[]
 for i,r in enumerate(d[arraykey]):
  if r['id'] in IDS:
   pointers[arraykey+'/'+str(len(v[arraykey]))]='/'+arraykey+'/'+str(i);v[arraykey].append(r)
 out=W/(label+'-scoped.json');out.write_text(json.dumps(v,ensure_ascii=False))
 bindings.append({'source_label':label,'selected_path':str(out.relative_to(T)),'source_pointer_by_selected_pointer':pointers,'selection':'all11 matching canonical IDs, each entire object; present mandatory7 only in these three current closure arrays','source_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
select('b8ledger',['schema','utc','required_denominator','batch_denominator','phase','configuration_effective','counters','nonmandatory_adoption','final_closure_scope','finite_required_unmet_dependencies','retained_open_limits','final_closure_decision'],'issues')
select('b8decision',['schema','utc','decision_owner','scope_definition','acceptance_checkpoint_commit','dependency_audit','static_projection','counts','severities','finite_required_unmet_dependencies','retained_open_limits','old_global_closure_boundaries','nonmandatory_adoption','current_execution_policy','main_merge_prohibited'],'records')
select('b8dependencies',['schema','utc','audited_HEAD','B','final_functional_MI','FI','scoped_required_unmet_gates','all27_eligible_for_scoped_required_closure','closure_scope','retained_open_limits','history','reference_read_only_HEAD','CLOSED_granted_by_audit','qualification'],'records')
(T/'scope-bindings.json').write_text(json.dumps(bindings,ensure_ascii=False,indent=2)+'\n')
