"""Mechanical receipt checks only; never reference/game/model execution."""
import ast,hashlib,json,pathlib,subprocess,datetime,math
from fractions import Fraction
P=pathlib.Path(__file__).resolve().parent
R=pathlib.Path('/workspace/pokemon-essentials-clean-room')
C='35d85e4484b892ebc32542346861440638d2183c'
T=P.parents[1]
checks=[]
def check(name,condition,details=None):
 assert condition,(name,details)
 checks.append({'check':name,'result':'PASS_MECHANICAL_ONLY','details':details})
def read(n):return json.loads((P/n).read_text())
def git(*x,cwd=R):return subprocess.check_output(['git',*x],cwd=cwd,text=True).strip()
for f in sorted(P.iterdir()):
 if f.suffix=='.json':json.loads(f.read_text())
 elif f.suffix=='.jsonl':
  for x in f.read_text().splitlines():json.loads(x)
 elif f.suffix=='.py':ast.parse(f.read_text())
check('UTF8_JSON_JSONL_AST_valid',True)
a=json.loads((T/'continuation/06_qualifications_interfaces/readset.complete.json').read_text());d=read('reception-ledger.json');i=read('identity.json');b=read('battler-reception.json');v=read('reverse-reception.json');p=read('provider-reception.json');it=read('interfaces.json');l=read('reading-ledger.json')
check('exclusive_branch',git('branch','--show-current')=='codex/r8-cp-reception-06-20261016')
check('fixed_contract_and_embedded_binding_separate',i['contract_commit']==C and i['embedded_group_readset_contract_commit']==a['contract_commit'])
check('contract_tree',i['contract_tree']==git('rev-parse',C+'^{tree}'))
for name in ['continuation-contracts.json','continuation/06_qualifications_interfaces/prompt.zh.md','continuation/06_qualifications_interfaces/readset.complete.json']:
 f=T/name;rel=str(f.relative_to(R));frozen=subprocess.check_output(['git','show',C+':'+rel],cwd=R)
 check('fixed_input_exact:'+name,f.read_bytes()==frozen)
check('fixed_reference_tree',i['R_tree']=='7589c800b61ba13a13040ed0d686979b80a84fd0')
check('formal_tree_unchanged',git('rev-parse','HEAD:deliverables/final-specification-set')=='f292698cdd4a8e725525a9be6dc34b75faaf151e')
check('reference_tracked_clean',not git('status','--porcelain','--untracked-files=no',cwd=pathlib.Path('/workspace/pokemon-essentials')))
check('150_exact_reverse_IDs',{x['id'] for x in v['rows']}=={z['id'] for g in a['reverse_current_contribution_objects'] for z in g['subassertions']} and len(v['rows'])==150)
check('20_exact_interfaces',{x['id'] for x in it['selected']}=={x['id'] for x in a['selected_reverse_interfaces']} and len(it['selected'])==20)
check('66_exact_provider_IDs',{x['id'] for x in p['rows']}=={z['id'] for u in a['qualification_obligations']['six_provider_units_full']['payloads'] for z in u['assertions']} and len(p['rows'])==66)
check('8_corrected_Battler_and31_units',len(b['facts'])==8 and len(b['complete_units'])==31)
check('11_distinct_legacy_namespaced_edges',len(it['legacy_edges'])==11 and len({x['namespace'] for x in it['legacy_edges']})==11)
check('0_primary_credit',d['denominators']['primary_objects']==0 and d['denominators']['primary_source_assertions_credited_here']==0)
check('0_unread_necessary',d['unread_in_this_assigned_semantic_scope']==0 and read('history-and-limits.json')['readable_necessary_units_unread']==0)
check('31_payloads_count_bytes',len(l['operative_payloads'])==31 and sum(x['bytes'] for x in l['operative_payloads'])==1628507)
for x in l['operative_payloads']:
 f=R/x['reused_local_path'];q=f.read_bytes()
 check('input_identity:'+x['relative_to_target_task'],len(q)==x['bytes'] and hashlib.sha256(q).hexdigest()==x['sha256'] and hashlib.sha1(b'blob '+str(len(q)).encode()+b'\0'+q).hexdigest()==x['git_blob'])
by={x['identity']['path']:x for x in l['parent_readings']}
for x in v['rows']:
 check('evidence_resolves:'+x['id'],all(l['evidence_id_bindings'][z] in by for z in x['evidence_ids']))
for u in p['rows']:
 source='/workspace/pokemon-essentials/'+u['source']['path'];lo,hi=u['source']['lines'];covered=set()
 for x,y in by[source]['read_ranges_union']:covered.update(range(x,y+1))
 check('provider_complete_unit:'+u['id'],set(range(lo,hi+1))<=covered)
for x in l['parent_readings']:
 q=pathlib.Path(x['identity']['path']).read_bytes();check('parent_unchanged:'+x['identity']['path'],hashlib.sha256(q).hexdigest()==x['identity']['sha256'])
check('typed_and_semantic_unique_values',len(read('readset-typed-identity-values.json'))+len((P/'readset-semantic-strings.jsonl').read_text().splitlines())==read('view-generation.json')['unique_leaf_values'])
check('217_paths19_purpose_groups',sum(len(x['members']) for x in read('coverage-purpose-groups.json'))==217 and len(read('coverage-purpose-groups.json'))==19)
check('1769_script_literal_purpose_records',len(read('script-purpose-aliases.json'))==1769)
check('pure_hypothetical_arithmetic_controls',[math.ceil(Fraction(1)*20)+2, math.ceil(Fraction(1)/Fraction(3,4)*20)+2,10+2]==[22,29,12],{'scope':'rational arithmetic only, no producer/reference/model execution'})
check('source_fragment_views_removed',not any((P/n).exists() for n in ['battler-exact-input.json','battler-exact-units.txt','battler-unread-increment.txt']))
check('required_not_self_accepted',d['findings']['accepted_required']==0 and d['UPDATE_NOT_STARTED'] is True)
changed=set(git('diff','--name-only',C).splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
check('unique_write_set',all(x.startswith(str(P.relative_to(R))+'/') for x in changed if x),{'paths':len(changed),'base':C})
# No self-hash: validation is not in its own input manifest. Publication later binds immutable commit.
out={'schema':'r8-cp06-mechanical-validation/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_MECHANICAL_ONLY','checks':checks,'count':len(checks),'business_execution':0,'semantic_pass_from_checks':False,'UPDATE_NOT_STARTED':True}
(P/'validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'write_paths':len(changed),'business_execution':0}))
