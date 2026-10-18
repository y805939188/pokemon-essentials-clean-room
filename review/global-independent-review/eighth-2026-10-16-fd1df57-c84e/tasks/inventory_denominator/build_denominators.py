#!/usr/bin/env python3
"""Build explicit navigation denominators. Never infer semantic completeness."""
import collections
import datetime
import hashlib
import json
from pathlib import Path
import re

OUT=Path(__file__).resolve().parent
B=Path('/workspace/pokemon-essentials-clean-room')
ROOT=OUT.parent.parent
wp=json.loads((OUT/'wp-map.json').read_text())
rows=wp['work_packages']
features=[]
in_original_feature_table=False
for number,line in enumerate((B/'planning/feature-matrix.md').read_text().splitlines(),1):
    if line.startswith('| Feature ID | Domain |'):
        in_original_feature_table=True
    elif in_original_feature_table and line.startswith('## '):
        in_original_feature_table=False
    if in_original_feature_table and re.match(r'^\| F\d\d-\d\d \|',line):
        cells=[x.strip() for x in line.split('|')[1:-1]]
        f=dict(zip(['feature_id','domain','name','description','classification','reference_locations','historical_status_text','confidence','notes'],cells))
        f['line']=number
        f['plan_work_packages']=[r['wp'] for r in rows if f['feature_id'] in re.findall(r'F\d\d-\d\d',r['scope'])]
        f['B8_formal_paths']=sorted({p for r in rows if r['wp'] in f['plan_work_packages'] for p in r['formal_payloads']+r['test_catalogs']+r.get('shared_formal_payloads',[])})
        f['semantic_read_qualification']='Feature navigation full text read; no inherited approval of B8 clauses or R source'
        features.append(f)

domains=[]
for number,line in enumerate((B/'planning/module-map.md').read_text().splitlines(),1):
    if re.match(r'^\| D\d\d ',line):
        cells=[x.strip() for x in line.split('|')[1:-1]]
        d=dict(zip(['domain','responsibility','subdomains','dependencies_text','pokemon_specific','host_coupling','spec_groups','evidence_navigation'],cells))
        d['line']=number;domains.append(d)

dep_edges=[]
for row in rows:
    for target in row['dependencies_expanded']:
        dep_edges.append({'dependent':row['wp'],'prerequisite':target,
                          'type':'DECLARED_COMPLETION_KNOWLEDGE_DEPENDENCY',
                          'source':'planning/extraction-plan.md','line':row['plan_line'],
                          'R8_actual_interface_acceptance':'UNREAD_UNRECEIVED'})

crosscut=[]
plan=(B/'planning/extraction-plan.md').read_text().splitlines()
for i,line in enumerate(plan,1):
    if 217<=i<=228 and line.startswith('| ') and not line.startswith(('| ---','| 横切')):
        cells=[x.strip() for x in line.split('|')[1:-1]]
        crosscut.append({'id':'DECL-X'+str(len(crosscut)+1).zfill(2),'name':cells[0],
                        'wp_text':cells[1],'required_question':cells[2],'line':i,
                        'acceptance':'UNREAD_UNRECEIVED'})
checkpoints=[{'id':'DECL-J01','name':'生物—队伍—储存','wps':['WP18','WP20','WP25','WP26','WP35','WP38','WP57','WP64'],'requirements':'identity/ownership, capacity, persistence and legal member moves; entry-specific failure prefixes','acceptance':'UNREAD_UNRECEIVED'},
 {'id':'DECL-J02','name':'战斗中成长—学习反馈','wps':['WP30','WP42','WP67-A'],'requirements':'growth primary rules, trigger/wait, ongoing battle ability/move changes, abandon choices and consistency','acceptance':'UNREAD_UNRECEIVED'},
 {'id':'DECL-J03','name':'捕获—战斗—图鉴','wps':['WP38','WP40','WP42','WP62','WP67-A'],'requirements':'unique capture formula, forced reception/cancel permissions, growth/registration/storage ordering','acceptance':'UNREAD_UNRECEIVED'}]

formal=json.loads((OUT/'formal-inventory.json').read_text())
source=json.loads((OUT/'reference-inventory.json').read_text())
# File units are a conservative first bound, explicitly awaiting actual semantic split.
source_rows=[{'repo':f['repo'],'commit':f['commit'],'tree':f['workspace_tree'],'path':f['path'],
              'sha256':f['sha256'],'blob':f['git_blob'],'unit_id':'FILE:'+f['path'],
              'unit_expansion':'PENDING_SEMANTIC_STRUCTURE_DECOMPOSITION',
              'facts':None,'consumers':None,'spec_clauses':None,
              'semantic_status':'UNREAD_UNRECEIVED_BY_INVENTORY_COORDINATOR'} for f in source]
formal_rows=[{'repo':f['repo'],'commit':f['commit'],'tree':f['workspace_tree'],'path':f['path'],
              'sha256':f['sha256'],'blob':f['git_blob'],'unit_id':'FILE:'+f['path'],
              'clause_expansion':'PENDING_ATOMIC_ASSERTION_AND_PREMISE_DECOMPOSITION',
              'source_facts':None,'premises':None,'consumers':None,
              'semantic_status':'UNREAD_UNRECEIVED_BY_INVENTORY_COORDINATOR'} for f in formal]

def write(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
write('feature-wp-formal-map.json',{'schema':'gr8-feature-routing/v1','features':features,'domains':domains,
      'feature_count':len(features),'domain_count':len(domains),'not_requirement_denominator':True,
      'features_missing_plan_wp':[f['feature_id'] for f in features if not f['plan_work_packages']]})
write('declared-interface-denominator.json',{'schema':'gr8-declared-interfaces/v1',
      'scope':'Only declared planning obligations; actual source interfaces remain open until source/receiver review',
      'knowledge_dependency_edges':dep_edges,'crosscut_obligations':crosscut,'junction_checkpoints':checkpoints,
      'actual_interface_denominator':'UNFROZEN_PENDING_DOMAIN_SOURCE_CONSUMER_REVIEW',
      'all_actual_interfaces_covered':False})
write('forward-matrix.file-denominator.json',{'schema':'gr8-forward-file-bound/v1','rows':source_rows,
      'file_denominator':len(source_rows),'semantic_unit_denominator':None,'fact_denominator':None,
      'qualification':'Inventory-only baseline; file count never substitutes for unit/fact coverage; domain ledgers must expand and receive'})
write('reverse-matrix.file-denominator.json',{'schema':'gr8-reverse-file-bound/v1','rows':formal_rows,
      'file_denominator':len(formal_rows),'formal_clause_denominator':None,
      'qualification':'Atomic clauses/subassertions and premises require named semantic expansion; not zero and not PASS'})

# Independently verify recovered historical bytes while retaining all version paths.
rec_path=ROOT/'tasks/history_current/recovery-manifest.json'
hist=[]
if rec_path.exists():
    for f in json.loads(rec_path.read_text())['files']:
        local=Path(f['local_path']);raw=local.read_bytes();identity=dict(f)
        identity.update(actual_mode=oct(local.stat().st_mode&0o777),
            independent_sha256=hashlib.sha256(raw).hexdigest(),independent_bytes=len(raw),
            identity_reverified=len(raw)==f['bytes'] and hashlib.sha256(raw).hexdigest()==f['sha256'],
            semantic_credit=False,purpose='Exact historical supplement recovery; present-day semantics separately reviewed by history_current')
        hist.append(identity)
write('historical-recovered-inventory.json',hist)
write('denominator-status.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'reference_files':432,'formal_files':131,'planning_files':5,'audit_files':1,
      'work_packages':87,'content_work_packages_including_WP01':84,'review_stages':3,
      'feature_groups':len(features),'domains':len(domains),'declared_dependency_edges':len(dep_edges),
      'declared_crosscut_obligations':len(crosscut),'declared_checkpoints':len(checkpoints),
      'actual_semantic_unit_denominator':'UNFROZEN','formal_atomic_clause_denominator':'UNFROZEN',
      'actual_interface_denominator':'UNFROZEN','supplement_currentness':'PENDING_HISTORY_CURRENT',
      'historical_restored_version_payloads':len(hist),'update_started':False,
      'completion':'INVENTORY_AND_ROUTING_COMPLETE_SEMANTIC_DENOMINATORS_NOT_COMPLETE'})
print(json.dumps({'features':len(features),'domains':len(domains),'deps':len(dep_edges),'crosscuts':len(crosscut),'historical_versions':len(hist)},ensure_ascii=False))
