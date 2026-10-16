import json,sys,pathlib,hashlib
base=pathlib.Path(__file__).resolve().parents[2]
hist=base/'evidence/external-recovered/receive_external_h_c2_current_records/ac8cae2652f02ddb7aa6e820c29be4c50522a799'
identity={'sha256','blob','git_blob','bytes','mode','repo','repository_id','tree','fixed_commit','commit','B8','R','fixed_B8','fixed_R','fixed_formal_tree','fixed_R_tree','formal_tree','R_tree','utc','created_utc','actual_reader','reading_events','exact_value_sha256','original_payload','fixed_git_bytes_match'}
def strip(x,trail=''):
 if isinstance(x,list):return [strip(v,trail) for v in x]
 if isinstance(x,dict):
  out={}
  for k,v in x.items():
   if k in identity:continue
   if k in ('complete_frozen_required_source_ranges','current_formal_locators','fixed_reading_indices'):
    out[k]={'disposition':'typed exact locator list only; no body credit','count':len(v)};continue
   if k in ('content','text') and ('source' in trail.lower() or (k=='content' and ('formal_context' in trail or 'formal_assertion' in trail or 'complete_inputs' in trail)) or str(x.get('path','')).endswith('.rb')):
    out[k]='[embedded source bytes TYPED_ONLY; no source reading credit]';continue
   out[k]=strip(v,trail+'/'+k)
  return out
 return x
def factor(x,seen=None,path='#'):
 if seen is None:seen={}
 if isinstance(x,str) and len(x)>65:
  if x in seen:return {'exact_same_value_as':seen[x]}
  seen[x]=path;return x
 if isinstance(x,list):return [factor(v,seen,path+'/'+str(i)) for i,v in enumerate(x)]
 if isinstance(x,dict):return {k:factor(v,seen,path+'/'+k) for k,v in x.items()}
 return x
mode=sys.argv[1]
if mode=='current':
 d=json.load(open(base/'adjudication/root-decisions.partial.json'))
 for i in range(int(sys.argv[2]),int(sys.argv[3])):
  r=d['records'][i];print('CURRENT',i,r['id'],r['classification'],r['severity']);print('ROOT_REASON',r['root_reason']);print(json.dumps(strip(r['complete_semantic_contract_received']),ensure_ascii=False,separators=(',',':')))
elif mode in 'ABC' and len(mode)==1:
 d=json.load(open(hist/'partition-receptions'/mode/'accepted-contribution.json'))
 for i in range(int(sys.argv[2]),int(sys.argv[3])):
  r=d['records'][i];print('HIST',mode,i,r['id']);print(json.dumps(factor(strip({k:v for k,v in r.items() if k in ['contribution_judgment','contribution_interface','contribution_counter','accepted_scope','parent_interface_reception']})),ensure_ascii=False,separators=(',',':')))
elif mode=='D':
 d=json.load(open(hist/'partition-receptions/D/accepted-contribution.json'))
 for i in range(int(sys.argv[2]),int(sys.argv[3])):
  print('LEGACY',i);print(json.dumps(strip(d['complete_legacy_contribution'][i]),ensure_ascii=False,separators=(',',':')))
else:raise ValueError(mode)
