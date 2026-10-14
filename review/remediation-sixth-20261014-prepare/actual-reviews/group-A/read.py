import json,sys,subprocess
from pathlib import Path
p=Path("review/remediation-sixth-20261014-prepare")
mode=sys.argv[1]
if mode=="contract":
 d=json.loads((p/"contracts"/f"R6-{sys.argv[2]}.json").read_text())
 obj=d if len(sys.argv)<4 or sys.argv[3]=="x" else d["scope_contracts"][int(sys.argv[3])]
 s=json.dumps(obj,ensure_ascii=False,indent=2).splitlines()
else:
 name=sys.argv[2]
 if mode=="source":
  raw=subprocess.check_output(["git","--git-dir=/tmp/r6-u01-r-reference.git","show","8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:"+name]);s=raw.decode().splitlines()
 else:s=Path(name).read_text().splitlines()
a=int(sys.argv[4] if mode=="contract" and len(sys.argv)>4 else sys.argv[3] if mode!="contract" and len(sys.argv)>3 else 1)
b=int(sys.argv[5] if mode=="contract" and len(sys.argv)>5 else sys.argv[4] if mode!="contract" and len(sys.argv)>4 else len(s))
print(f"INPUT {mode} {sys.argv[2]} TOTAL_LINES {len(s)} READ {a}-{min(b,len(s))}")
for i in range(a-1,min(b,len(s))): print(f"{i+1}: {s[i]}")
