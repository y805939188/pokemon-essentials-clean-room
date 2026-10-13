"""Complete literal per-record/per-field generation comparison; no gameplay/model.
Different payloads are retained as authored profiles, not patched or 'corrected'."""
import re
from collections import defaultdict,Counter
import review_state as s
families=['abilities','berry_plants','encounters','items','moves','pokemon','pokemon_forms','pokemon_metrics','types']
def ledger(path):return s.read('pbs-records-'+path[4:].replace('/','--').replace(' ','_')+'.json')
def seq(rec):return [(p['key'],p['value_sha256']) for p in rec['properties']]+[('raw_row',p['sha256']) for p in rec['raw_rows']]
summary=[]
for profile in ['Gen 5 backup','Gen 6 backup','Gen 7 backup','Gen 8 backup']:
 for fam in families:
  path='PBS/'+profile+'/'+fam+'.txt';a=ledger(path);b=ledger('PBS/'+fam+'.txt');ar={x['record_key']:x for x in a['records']};br={x['record_key']:x for x in b['records']};rows=[];allfields=Counter()
  for rec in a['records']:
   key=rec['record_key'];target=br.get(key)
   if not target:rows.append({'record_key':key,'source_lines':rec['lines'],'status':'not_in_current_profile'});continue
   ap=defaultdict(list);bp=defaultdict(list)
   for p in rec['properties']:ap[p['key']].append({'line':p['line'],'sha256':p['value_sha256'],'value':p.get('data_value')})
   for p in target['properties']:bp[p['key']].append({'line':p['line'],'sha256':p['value_sha256'],'value':p.get('data_value')})
   changed=[]
   for k in sorted(ap.keys()|bp.keys()):
    if [p['sha256'] for p in ap[k]]!=[p['sha256'] for p in bp[k]]:
     changed.append({'field':k,'profile_values':ap[k],'current_values':bp[k]});allfields[k]+=1
   if [x['sha256'] for x in rec['raw_rows']]!=[x['sha256'] for x in target['raw_rows']]:
    changed.append({'field':'ordered_raw_rows','profile_values':rec['raw_rows'],'current_values':target['raw_rows']});allfields['ordered_raw_rows']+=1
   rows.append({'record_key':key,'source_lines':rec['lines'],'current_lines':target['lines'],'all_ordered_field_payloads_equal':seq(rec)==seq(target),'differences':changed,'semantic_context':'Each retainedfielduses its own schema andlinkedconsumer. A generationfolderlabel doesnot enablethosemechanics, nor iseveryprofileequivalenttoofficialgames.'})
  out={'schema_version':'gr5.review.v1','path':path,'version':s.R,'git_blob':a['git_blob'],'current_path':b['path'],'current_git_blob':b['git_blob'],'exact_blob_equal':a['git_blob']==b['git_blob'],'records':rows,'current_only_identities':[x['record_key'] for x in b['records'] if x['record_key'] not in ar],'profile_only_identities':[x['record_key'] for x in a['records'] if x['record_key'] not in br],'field_change_counts':dict(allfields),'review_boundary':'Complete per-record literal comparisons; data interpretation comes from schema-field-contracts and consumer source reviews. No mechanics execution and no canonical data correction.'}
  name='pbs-profile-'+profile.replace(' ','_')+'--'+fam+'.json';s.write(name,out)
  summary.append({k:v for k,v in out.items() if k not in ['records','current_only_identities','profile_only_identities']});summary[-1].update(profile_records=len(ar),current_records=len(br),profile_only_count=len(out['profile_only_identities']),current_only_count=len(out['current_only_identities']),changed_common_records=sum(bool(x.get('differences')) for x in rows),artifact=name)
s.write('pbs-profile-comparison.json',{'schema_version':'gr5.review.v1','source_baseline':s.R,'profiles':summary,'scope':'All36 generation-backup paths with everyordered record/property; exactblob reuse separately recorded; source data changes distinctfrom rules/settings changes.'})
for x in summary:print(x['path'],'profile/current',x['profile_records'],x['current_records'],'changed-common',x['changed_common_records'],'profile-only',x['profile_only_count'],'field-kinds',','.join(x['field_change_counts']))
# Inspect derived references without upgrading ordinary optional data to hardconstraints.
checks=[]
for profile in ['current','Gen 5 backup','Gen 6 backup','Gen 7 backup','Gen 8 backup']:
 prefix='PBS/' if profile=='current' else 'PBS/'+profile+'/'
 base=ledger(prefix+'pokemon.txt');forms=ledger(prefix+'pokemon_forms.txt');ids={r['record_key'] for r in forms['records']}
 for r in base['records']+forms['records']:
  for p in r['properties']:
   if p['key']=='PokedexForm':checks.append({'profile':profile,'record':r['record_key'],'field':'PokedexForm','target':p['data_value'],'explicit_target_exists':r['record_key'].split(',')[0]+','+p['data_value'] in ids,'source_line':p['line']})
   if p['key']=='Flags':
    for flag in p['data_value'].split(','):
     m=re.fullmatch('DefaultForm_(\\d+)',flag,re.I)
     if m:checks.append({'profile':profile,'record':r['record_key'],'field':'DefaultForm flag','target':m[1],'explicit_target_exists':m[1]=='0' or r['record_key'].split(',')[0]+','+m[1] in ids,'source_line':p['line'],'boundary':'Not a compiler form-reference constraint; runtime form lookup can usebasefallback.'})
s.write('species-display-form-relations.json',{'schema_version':'gr5.review.v1','source_baseline':s.R,'checks':checks})
print('Display/defaultform relations without explicit target',[(x['profile'],x['record'],x['field'],x['target']) for x in checks if not x['explicit_target_exists']])
