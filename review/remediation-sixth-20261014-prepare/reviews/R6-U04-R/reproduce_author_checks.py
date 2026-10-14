"""Recompute the reviewed author's finite static checks at the frozen publication.

Only object-cache location and historical write-set observation are adapted.
This loads no Ruby and executes no reference definitions or behavior model.
"""
import hashlib, pathlib, subprocess
ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN = pathlib.Path(__file__).resolve().parent
AUTHOR = '22cc12e141ac2c2dd23c1dea218bf0873c5f86ca'
path = 'review/remediation-sixth-20261014-prepare/candidates/R6-U04/evidence/validate.py'
raw = subprocess.check_output(['git','-C',str(ROOT),'show',AUTHOR+':'+path])
assert raw == (ROOT/path).read_bytes()
code = raw.decode()
changes = {
    "RDB='/tmp/r6-u04-reference-objects'": 'RDB='+repr(str(OWN/'.scratch/reference.git')),
    "changed=git(ROOT,'diff','--name-only',BASE).decode().splitlines()": "changed=git(ROOT,'diff','--name-only',BASE,'"+AUTHOR+"').decode().splitlines()",
    "untracked=git(ROOT,'ls-files','--others','--exclude-standard').decode().splitlines()": "untracked=[]  # frozen committed author's snapshot, not the reviewer's working files",
}
for old, new in changes.items():
    assert code.count(old)==1, old
    code=code.replace(old,new)
# This is the fully inspected, hash-bound author's static checker, with the three
# exact adaptations above; it is not an untrusted serialized program or R code.
exec(compile(code, str(ROOT/path), 'exec'), {'__file__':str(ROOT/path), '__name__':'__main__'})
