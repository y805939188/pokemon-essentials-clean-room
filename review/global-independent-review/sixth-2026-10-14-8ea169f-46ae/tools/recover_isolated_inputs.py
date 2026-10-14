"""Recover the six ignored audit inputs from fixed, local, read-only R objects."""
import hashlib,json,pathlib,subprocess
root=pathlib.Path(__file__).resolve().parents[1];base=root.parents[2]
ref=base/'reference/pokemon-essentials';dst=root/'tasks/R6-H/subtasks/supplement-inventory/resource-check/inputs'
inv=json.loads((root/'inventory/reference.json').read_text());dst.mkdir(parents=True,exist_ok=True)
for name in ['animmaker.exe','soundfont.sf2','zlib1.dll','x64-msvcrt-ruby310.dll','Game.exe','extendtext.exe']:
    row=next(x for x in inv if x['path']==name)
    b=subprocess.check_output(['git','-C',str(ref),'cat-file','blob',row['git_blob']])
    assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
    p=dst/name
    if p.exists():assert p.read_bytes()==b,'Preserve an unexpected existing file'
    else:p.write_bytes(b)
print('Six isolated audit inputs restored or verified; no reference execution.')
