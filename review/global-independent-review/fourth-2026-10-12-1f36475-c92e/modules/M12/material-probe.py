import json, hashlib, struct, subprocess
from pathlib import Path
r=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
tracked=subprocess.check_output(['git','-C',str(r),'ls-files','-z']).decode().split('\0')[:-1]
checks=['Graphics','Audio','Plugins','Animations','Game.ini','Game.rxproj','Data/MapInfos.rxdata','Data/System.rxdata','Data/Tilesets.rxdata','Data/CommonEvents.rxdata','Data/Animations.rxdata','Data/PkmnAnimations.rxdata','Data/move2anim.dat','Data/trainer_lists.dat','Graphics/UI/Town Map/mapRegion0.png','Data/Scripts.rxdata','Data/messages_core.dat','mkxp.json','animmaker.exe','extendtext.exe']
bitmaps=[]
for name in ['knownpoint.bmp','selpoint.bmp']:
 b=(r/name).read_bytes()
 bitmaps.append({'path':name,'tracked':name in tracked,'bytes':len(b),'signature':b[:2].decode(),'dimensions':list(struct.unpack_from('<ii',b,18)),'sha256':hashlib.sha256(b).hexdigest()})
print(json.dumps({'tracked_total_shared_identity_not_rehashed':len(tracked),'data_top_level':sorted(x.name for x in (r/'Data').iterdir()),'map_files':[str(x.relative_to(r)) for x in (r/'Data').glob('Map*.rxdata')],'availability':{name:(r/name).exists() for name in checks},'bitmaps':bitmaps,'inventory_counts':{'scripts':sum(x.startswith('Data/Scripts/') for x in tracked),'pbs':sum(x.startswith('PBS/') for x in tracked),'translation':sum(x.startswith('Text_english_core/') for x in tracked),'fonts':sum(x.startswith('Fonts/') for x in tracked)},'formal_files':len(list(Path('deliverables/final-specification-set').rglob('*.md'))),'scripts_same_except_entry_lines':(r/'scripts_extract.rb').read_bytes().splitlines()[:-2]==(r/'scripts_combine.rb').read_bytes().splitlines()[:-2]},ensure_ascii=False,indent=2))
