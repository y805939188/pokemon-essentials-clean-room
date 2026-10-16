"""Copy exact immutable Git ranges for direct reading; never execute evidence."""
from pathlib import Path
import subprocess,json,hashlib
P=Path(__file__).resolve().parent
R='/workspace/pokemon-essentials'; B='/workspace/pokemon-essentials-clean-room'
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';BC='fd1df570cad987dc3852a3b958f03916e317f7fe'
plan=[
 ('SC-source',R,RC,'Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb',[(979,1133)]),
 ('SC-receiver',B,BC,'deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md',[(212,251)]),
 ('U03-data',R,RC,'Data/Scripts/010_Data/002_PBS data/006_Item.rb',[(119,202)]),
 ('U03-consumers',R,RC,'Data/Scripts/013_Items/001_Item_Utilities.rb',[(644,752)]),
 ('U03-receiver',B,BC,'deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md',[(115,152),(222,265)]),
 ('U03-vectors',B,BC,'deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md',[(274,300)]),
 ('form-producer',R,RC,'Data/Scripts/014_Pokemon/001_Pokemon.rb',[(147,184)]),
 ('form-time',R,RC,'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',[(422,432),(475,485)]),
 ('form-request',R,RC,'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb',[(92,125)]),
 ('form-sprites',R,RC,'Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb',[(49,60),(124,140)]),
 ('summary-consumer',R,RC,'Data/Scripts/016_UI/006_UI_Summary.rb',[(117,138),(303,310)]),
 ('party-refresh',R,RC,'Data/Scripts/016_UI/005_UI_Party.rb',[(162,232),(269,275),(855,898),(966,976),(1380,1405)]),
 ('bottle-effect',R,RC,'Data/Scripts/013_Items/002_Item_Effects.rb',[(1216,1230)]),
 ('summary-receiver',B,BC,'deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md',[(214,234)]),
 ('form-receiver',B,BC,'deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md',[(173,202)]),
 ('bottle-receiver',B,BC,'deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md',[(298,342)]),
 ('EV-handlers',R,RC,'Data/Scripts/013_Items/002_Item_Effects.rb',[(762,832)]),
 ('EV-helper',R,RC,'Data/Scripts/013_Items/001_Item_Utilities.rb',[(401,444)]),
 ('form-stat-context',R,RC,'Data/Scripts/014_Pokemon/001_Pokemon.rb',[(104,120)]),
 ('form-registration',R,RC,'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',[(189,219)]),
]
out=P/'consumer-reads';out.mkdir(exist_ok=True);rows=[]
for name,repo,commit,path,ranges in plan:
 b=subprocess.check_output(['git','show',commit+':'+path],cwd=repo);lines=b.splitlines(keepends=True)
 identity={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
 mode=subprocess.check_output(['git','ls-tree',commit,'--',path],cwd=repo,text=True).split()[0]
 payload=f'{repo} {commit}\n{path}\n'+json.dumps(identity)+'\n'
 for start,end in ranges:
  assert 1<=start<=end<=len(lines)
  payload+=f'EXACT LINES {start}–{end}\n'+b''.join(lines[start-1:end]).decode()+'\n'
 (out/(name+'.txt')).write_text(payload)
 rows.append({'name':name,'repo':repo,'commit':commit,'path':path,'mode':mode,**identity,'ranges':ranges,'purpose':'SOURCE_STATIC/SPEC_STATIC necessary qualification consumer; no behavior execution','semantic_status':'UNREAD'})
(out/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ranges':len(rows),'lines':sum(e-s+1 for *_,rs in plan for s,e in rs)}))
