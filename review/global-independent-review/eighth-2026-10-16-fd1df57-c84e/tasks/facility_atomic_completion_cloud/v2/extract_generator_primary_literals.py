import subprocess,json,pathlib,re,hashlib
v=pathlib.Path(__file__).resolve().parent;R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
keys=['ORANBERRY','SITRUSBERRY','ADAMANTORB','BABIRIBERRY','BLACKSLUDGE','BRIGHTPOWDER','CHESTOBERRY','CHOICEBAND','CHOICESCARF','CHOICESPECS','CHOPLEBERRY','DAMPROCK','DEEPSEATOOTH','EXPERTBELT','FLAMEORB','FOCUSSASH','FOCUSBAND','HEATROCK','LEFTOVERS','LIFEORB','LIGHTBALL','LIGHTCLAY','LUMBERRY','OCCABERRY','PETAYABERRY','SALACBERRY','SCOPELENS','SHEDSHELL','SHELLBELL','SHUCABERRY','LIECHIBERRY','SILKSCARF','THICKCLUB','TOXICORB','WIDELENS','YACHEBERRY','HABANBERRY','SOULDEW','PASSHOBERRY','QUICKCLAW','WHITEHERB']
def records(p):
 b=subprocess.check_output(['git','show',R+':'+p],cwd='/workspace/pokemon-essentials');ss=b.decode('utf-8-sig').splitlines(keepends=True);ix=[i for i,s in enumerate(ss) if re.fullmatch(r'\[.+\]\s*',s)];rr=[]
 for n,i in enumerate(ix):
  z=ix[n+1] if n+1<len(ix) else len(ss);rr.append({'id':ss[i].strip()[1:-1],'ordinal':n+1,'range':[i+1,z],'raw':''.join(ss[i:z])})
 return {'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','rev-parse',R+':'+p],cwd='/workspace/pokemon-essentials',text=True).strip()},rr
out={'schema':'facility-literal-selected-input-records/v2','fixedR':R,'actual_reader':'/root/facility_atomic_completion_cloud','reading_status':'EXTRACTED_FOR_EXPLICIT_FULL_READING_NOT_YET_FULL41','scope':'Literal section extraction only, notypedparser/businessmodel/eligibilityexecution; candidateindexorderretained. Noallitems/Pokemon/MoveFULL.','groups':[]}
view=[]
for p,want in [('PBS/items.txt',keys),('PBS/pokemon.txt',['SMEARGLE']),('PBS/moves.txt',['SKETCH','AERIALACE','SWIFT'])]:
 ident,rr=records(p);rd={x['id']:x for x in rr};chosen=[]
 for n,k in enumerate(want):
  x=rd[k].copy();x['selected_ordinal']=n+1;chosen.append(x);view.append(f'FILE {p} SELECTED {n+1} SOURCEORD {x["ordinal"]} L{x["range"][0]}–{x["range"][1]}\n'+x['raw'])
 out['groups'].append({'identity':ident,'complete_selected_records':chosen})
(v/'generator-selected41items-and-Sketch-primary.raw.v2.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');(v/'generator-selected41items-and-Sketch-primary.view.txt').write_text('\n'.join(view))
p=v/'generator-selected41items-and-Sketch-primary.view.txt';b=p.read_bytes();print('view',len(b),len(b.splitlines()),hashlib.sha256(b).hexdigest())
