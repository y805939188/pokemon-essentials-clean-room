from pathlib import Path
import json,hashlib,urllib.request,urllib.parse,datetime,subprocess
P=Path('review/remediation-sixth-20261014-prepare');E=P/'candidates/R6-U01/evidence';S=Path('/tmp/r6-u01-context');S.mkdir(exist_ok=True)
ident=lambda b:{'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
f=json.loads((P/'inputs/frozen-inputs.json').read_text());c=json.loads((P/'contracts/R6-U01.json').read_text());extra=['Data/Scripts/010_Data/002_PBS data/008_Species.rb','PBS/pokemon_forms.txt'];rows=[next(x for x in f['source_materials'] if x['path']==n) for n in extra]
(E/'additional-readset-registration.json').write_text(json.dumps({'registered_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'author_role':'R6-U01-A','purpose':'Necessary K003 data producer: default base-form, no earlier pre-evolution selection and Shellos form1; read-only fixed bytes; no write-set enlargement','root_mapping':'/tmp/r6-u01-frozen/Maruno17/pokemon-essentials/'+f['reference_commit'],'additional_source_materials':rows,'planned_semantic_ranges':{'Data/Scripts/010_Data/002_PBS data/008_Species.rb':[[1,584]],'PBS/pokemon_forms.txt':[[1119,1130]]}},ensure_ascii=False,indent=2)+'\n')
for r in rows:
 url='https://raw.githubusercontent.com/Maruno17/pokemon-essentials/'+f['reference_commit']+'/'+urllib.parse.quote(r['path'],safe='/')
 b=urllib.request.urlopen(url,timeout=30).read();assert all(ident(b)[k]==r[k] for k in ident(b));p=Path('/tmp/r6-u01-frozen/Maruno17/pokemon-essentials')/f['reference_commit']/r['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);print(json.dumps({'extra_read_only_input':r,'local':str(p),'identity_validated':True},ensure_ascii=False))
# Validate only U01 source/formal and U01 independent evidence, not other batches.
text=(P/'prompts/R6-U01-A.md').read_text();s=text.index('```json',text.index('## 精确共同证据'));z=text.index('\n```',s+8);ev=json.loads(text[s+8:z]);names=['findings/independent-K-%03d.json'%i for i in range(1,4)]+['tasks/R6-O/counter-K-%03d.json'%i for i in range(1,4)]
evs=[]
for n in names:
 r=next(x for x in ev.values() if x['path']==n);p=P/'inputs/evidence'/n;b=p.read_bytes();assert all(ident(b)[k]==r[k] for k in ident(b));evs.append({'local_path':str(p),'frozen_identity':r,'verified':True})
(E/'input-evidence-identities.json').write_text(json.dumps(evs,ensure_ascii=False,indent=2)+'\n')
g=json.loads((P/'inputs/file-conflict-graph.json').read_text());d=json.loads((P/'inputs/dependency-graph.json').read_text());paths=set(c['candidate_formal_paths']);
ctx={'file_conflicts':{'schema':g['schema'],'edges':[x for x in g['edges'] if x.get('from')=='R6-U01' or x.get('to')=='R6-U01'],'file_receivers':{k:v for k,v in g['file_receivers'].items() if k in paths},'sole_writer':'thread01a13a93-d1da-71e4-a488-63b8524f503d / R6-I'},'dependency_graph':{'schema':d['schema'],'edges':[x for x in d['edges'] if 'R6-U01' in json.dumps(x) or any(k in json.dumps(x) for k in c['required_ids'])],'author_blocking_interbatch_edges':d['author_blocking_interbatch_edges'],'reason':d['reason']}}
for name in ['aliases-tombstones-and-accepted-negative-hypotheses.json','execution-phases.json']:
 j=json.loads((P/'inputs'/name).read_text());
 if name=='execution-phases.json':j={k:v for k,v in j.items() if k!='families'}|{'families':[x for x in j['families'] if x['id'] in ['R6-K','R6-O']]}
 ctx[name]=j
(S/'u01-context.json').write_text(json.dumps(ctx,ensure_ascii=False,indent=2)+'\n');print('u01-context saved')
# Precise historical projections retain complete relevant records, not truncated summaries.
H=Path('review/remediation-fifth-20261013-prepare');reg=json.loads((H/'contracts/R5-U03/regression-readset.json').read_text());sel=[x for x in reg if x['finding_id'] in ['GR5-M01-006','GR5-M04-002']];print('selected history',[(x['finding_id'],len(json.dumps(x))) for x in sel]);
(S/'historical-u03-projections.json').write_text(json.dumps(sel,ensure_ascii=False,indent=2)+'\n')
a=json.loads((H/'registration/successors/20261014-final-activation/activation-receipt.json').read_text());print('activation accepted type',type(a['accepted_actual']).__name__); print('activation scope',json.dumps({k:a[k] for k in ['closing_candidate','status','unique_activation_key','closure_scope','preserved_exclusions','history_preserved','execution']},ensure_ascii=False))
(E/'context-input-identities.json').write_text(json.dumps([{'path':str(p),**ident(p.read_bytes())} for p in [P/'inputs/file-conflict-graph.json',P/'inputs/dependency-graph.json',H/'contracts/R5-U03/regression-readset.json',H/'registration/successors/20261014-final-activation/activation-receipt.json']],ensure_ascii=False,indent=2)+'\n')
