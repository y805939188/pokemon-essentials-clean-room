import pathlib,json,subprocess,hashlib,datetime,collections
V=pathlib.Path(__file__).resolve().parent;RR=V.parents[2];P=RR/'tasks/pbs_creature_facility/subreviews/trait_eligibility';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def sha(b):return hashlib.sha256(b).hexdigest()
raw=(P/'species-field-classes.json').read_bytes();assert len(raw)==1563838 and sha(raw)=='62c392f85a00187ccc1d5bd5c89c2a08d73c63211f770d73967478ccbce86a7a';classes=json.loads(raw)
paths=sorted({o['file'] for c in classes for o in c['occurrences']});files=[];texts={}
for i,p in enumerate(paths):
 b=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',R+':'+p]);texts[p]=b.decode('utf-8-sig').splitlines();files.append({'code':i,'repo':'/workspace/pokemon-essentials','commit':R,'path':p,'bytes':len(b),'sha256':sha(b),'blob':subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse',R+':'+p]).decode().strip()})
fcode={p:i for i,p in enumerate(paths)};keymap={'Evolutions':'Evolution'};allowed={'Abilities','BaseStats','Evolution','Flags','Height','HiddenAbilities','Incense','Weight'}
compact=[];checks=[]
for c in classes:
 occ=[]
 for o in c['occurrences']:
  t=texts[o['file']];header=t[o['start']-1].split('#',1)[0].strip();assert header=='['+c['species']+']'
  actual={};loc={}
  for line in range(o['start']+1,o['end']+1):
   x=t[line-1].split('#',1)[0].strip()
   if '=' not in x:continue
   k,val=(y.strip() for y in x.split('=',1));k=keymap.get(k,k)
   if k in allowed:actual.setdefault(k,[]).append(val);loc.setdefault(k,[]).append(line)
  assert actual==c['fields'] and loc==o['field_lines'],(c['id'],o['file'])
  occ.append({'f':fcode[o['file']],'s':o['start'],'e':o['end'],'direct':o['direct_template_species'],'dataset':o['dataset'],'offsets':{k:[n-o['start'] for n in ns] for k,ns in o['field_lines'].items()}})
 groups=[]
 for o in occ:
  rest={k:v for k,v in o.items() if k not in ['f','dataset']};j=next((i for i,g in enumerate(groups) if g['body']==rest),None)
  if j is None:groups.append({'files':[o['f']],'datasets':[o['dataset']],'body':rest})
  else:groups[j]['files'].append(o['f']);groups[j]['datasets'].append(o['dataset'])
 # Grouping can reorder noncontiguous aliases. Keep occurrence order as explicit group/index references.
 order=[]
 for o in occ:
  gi=next(i for i,g in enumerate(groups) if o['f'] in g['files'] and g['body']=={k:v for k,v in o.items() if k not in ['f','dataset']});order.append([gi,groups[gi]['files'].index(o['f'])])
 reconstructed=[]
 for gi,oi in order:
  g=groups[gi];x=g['body'];reconstructed.append({'dataset':g['datasets'][oi],'file':paths[g['files'][oi]],'start':x['s'],'end':x['e'],'direct_template_species':x['direct'],'field_lines':{k:[x['s']+n for n in ns] for k,ns in x['offsets'].items()}})
 assert reconstructed==c['occurrences']
 compact.append({'id':c['id'],'species':c['species'],'fields':c['fields'],'occurrence_groups':groups,'order':order})
 checks.append({'id':c['id'],'actual_fixedR_field_lines_values_header_exact':True,'lossless_occurrence_inverse_exact':True,'occurrence_count':len(occ)})
out={'schema':'FAC-new-necessary-trait-primary-literal-extraction/v2','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'original':{'path':str((P/'species-field-classes.json').relative_to(RR)),'bytes':len(raw),'sha256':sha(raw)},'files':files,'records':compact,'checks':checks,'scope':'Literal primaryheader/fieldvalue/fieldline equality and lossless metadata factoring only. Doesnot run compiler/constructor/eligibility predicates/traitmath/graph model or target. Actualhuman/manual reception of every field/occurrence is separate; this extraction doesnot grant reading or semantic proof.','business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
(V/'trait-primary-649-literal-factored.v2.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
fieldrows=['Complete raw eight-field projection of each649class; absentkey isabsentliteral, notdefault/inheritance. Allvalues are exactstringlists; notderivedtraitflags.']
occrows=['All2732sourceoccurrences. f=filecode inidentity. s/e=inclusiveprimaryrange; direct=directtemplateSpeciesflag fromoldmetadata; offsets are exactline minus s. Groups alias only identicalbody; order=[group,index] reconstructs everyoriginal occurrence inoriginalorder. No businessmodel execution.']
fieldrows.extend(json.dumps({'id':c['id'],'species':c['species'],'fields':c['fields']},ensure_ascii=False,separators=(',',':')) for c in compact)
occrows.extend(json.dumps({'id':c['id'],'groups':c['occurrence_groups'],'order':c['order']},ensure_ascii=False,separators=(',',':')) for c in compact)
(V/'trait-649-primary-fields.view.jsonl').write_text('\n'.join(fieldrows)+'\n');(V/'trait-2732-primary-occurrences.view.jsonl').write_text('\n'.join(occrows)+'\n')
print('classes',len(classes),'occurrences',sum(len(c['occurrences']) for c in classes),'files',len(files),'metadata_checks',len(checks))
for n in ['trait-primary-649-literal-factored.v2.json','trait-649-primary-fields.view.jsonl','trait-2732-primary-occurrences.view.jsonl']:
 b=(V/n).read_bytes();print(n,len(b),sha(b),len(b.splitlines()))
