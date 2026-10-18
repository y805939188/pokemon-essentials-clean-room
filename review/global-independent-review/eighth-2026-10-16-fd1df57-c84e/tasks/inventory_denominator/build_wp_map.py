#!/usr/bin/env python3
"""Mechanical projection of the completely read extraction plan and path inventory.

This produces routing and denominator records, never semantic coverage approval.
"""
import collections
import datetime
import json
from pathlib import Path
import re

OUT=Path(__file__).resolve().parent
B=Path('/workspace/pokemon-essentials-clean-room')
formal=json.loads((OUT/'formal-inventory.json').read_text())
rows=[]
for line_no, line in enumerate((B/'planning/extraction-plan.md').read_text().splitlines(),1):
    if re.match(r'^\| WP\d\d(?:-[A-C])? \|',line):
        cells=[x.strip() for x in line.split('|')[1:-1]]
        rows.append(dict(zip(['wp','scope','goal','inputs','expected_outputs','dependencies_text','questions','completion_criteria'],cells),plan_line=line_no))
families=collections.defaultdict(list)
for row in rows:
    families[row['wp'].split('-')[0]].append(row['wp'])

catalogs={
 'combat-requirements-wp39-40-41-42-45.md':['39','40','41','42','45'],
 'combat-requirements-wp47-ab.md':['47-A','47-B'],
 'combat-requirements-wp49-51-52.md':['49','51','52-A','52-B','52-C'],
 'combat-requirements-wp54-55-56-58.md':['54','55','56','58'],
 'creature-rpg-wp18-20-24-25-26.md':['18','20','24','25','26'],
 'creature-rpg-wp27-28-29-30-33.md':['27','28','29','30','33'],
 'creature-rpg-wp35-36-57-64-68.md':['35','36','57','64','68'],
 'demo-dx-wp72-73-74-75-76-77.md':['72','73-A','73-B','74','75','76','77'],
 'engine-overworld-wp11-15-59-60.md':['11','12','13','14','15','59','60'],
 'engine-overworld-wp16.md':['16'],
 'generic-kernel-wp02-03-04.md':['02','03','04'],
 'generic-kernel-wp05-06-07-08-09-10.md':['05','06','07','08','09','10'],
 'pokemon-rules-wp19-21-22-23-34.md':['19','21','22','23','34'],
 'pokemon-rules-wp31-32-37-38.md':['31','32','37','38'],
 'pokemon-rules-wp43-44-46-48-50.md':['43','44','46','48','50'],
 'pokemon-rules-wp53-60-61-62-69-70.md':['53','60','61','62','69','70'],
 'user-interface-wp17-63-65-66-67-68-69-70-71.md':['17','63','65','66-A','66-B','66-C','67-A','67-B','68','69','70','71']}
def family_expand(wp):
    return families.get(wp,[wp])
def dependencies(text):
    deps=[]
    ranges=[]
    for match in re.finditer(r'WP(\d\d)[–—-]WP(\d\d)',text):
        ranges.append(match.span())
        for n in range(int(match[1]),int(match[2])+1):
            deps.extend(family_expand('WP'+str(n).zfill(2)))
    for match in re.finditer(r'WP\d\d(?:-[A-C])?',text):
        if not any(a<=match.start()<b for a,b in ranges):
            deps.extend(family_expand(match[0]))
    return list(dict.fromkeys(deps))

domains={}
for row in rows:
    wp=row['wp']; stem=wp.lower()
    payloads=[]
    for f in formal:
        if '/test-catalog/' in f['path']:
            continue
        if Path(f['path']).name.startswith(stem+'-'):
            payloads.append(f['path'])
    row['formal_payloads']=payloads
    row['domains']=sorted({p.split('/')[2] for p in payloads})
    row['test_catalogs']=['deliverables/final-specification-set/test-catalog/'+name for name, wps in catalogs.items() if wp[2:] in wps]
    row['dependencies_expanded']=dependencies(row['dependencies_text'])
    row['data_coverage_appendix_payloads']=[p for p in payloads if re.search(r'(?:data|coverage|appendix|defaults|matrix|reels|layouts|directory|scenarios|stats-directory)\.md$',p)]
    row['body_payloads']=[p for p in payloads if p not in row['data_coverage_appendix_payloads']]
    row['primary_contract_status']='ROUTING_ONLY_RULE_LEVEL_PRIMARY_REQUIRES_SEMANTIC_REVIEW'
    row['semantic_status']='UNREAD_BY_THIS_TASK'
    if not payloads:
        row['disposition']='WP01: scope/baseline navigation; WP78/79/80: consistency, coverage and sanitized-package stages; no same-number formal body'
        row['shared_formal_payloads']=['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md']
    for d in row['domains']:
        domains.setdefault(d,[]).append(wp)

def write(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
write('wp-map.json',{'schema':'gr8-wp-routing/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'plan_rows':87,'content_rows_including_WP01':84,'review_stages':['WP78','WP79','WP80'],
      'families_not_additional_tasks':{k:v for k,v in families.items() if len(v)>1},'work_packages':rows,
      'purpose':'routing and denominator; formal clauses not yet reviewed by this task'})

shards={
 'kernel_review':['generic-kernel'],
 'creature_review':['creature-rpg'],
 'combat_review':['combat-requirements','pokemon-rules'],
 'root_engine':['engine-overworld'],
 'root_ui':['user-interface'],
 'root_demo':['demo-dx'],
 'root_shared':['shared']}
seen=[]
for owner,ds in shards.items():
    ps=[f['path'] for f in formal if (f['path'].split('/')[2] in ds or (any(Path(f['path']).name.startswith(d+'-') for d in ds) and '/test-catalog/' in f['path']))]
    if owner=='root_shared':
        ps=['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md']
    seen.extend(ps)
    write('formal-shard-'+owner+'.json',{'owner':owner,'paths':ps,'count':len(ps),
          'semantic_status':'UNREAD_UNTIL_RECEIVED_FROM_NAMED_REVIEWER','shared_dependencies':'root_shared plus all cross-domain WP references and consumer receipts'})
    (OUT/('formal-shard-'+owner+'.txt')).write_text(''.join(p+'\n' for p in ps))
summary={'formal_denominator':131,'assigned':len(seen),'unique_assigned':len(set(seen)),
         'unassigned':sorted(set(f['path'] for f in formal)-set(seen)),
         'duplicate_assignments':[p for p,n in collections.Counter(seen).items() if n>1],
         'wp_rows':len(rows),'domains':domains,
         'cross_domain_wps':{r['wp']:r['domains'] for r in rows if len(r['domains'])>1}}
write('routing-summary.json',summary)
print(json.dumps(summary,ensure_ascii=False))
