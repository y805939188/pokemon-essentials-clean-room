from pathlib import Path
import hashlib,json,struct
ROOT=Path('/workspace/pokemon-essentials')
OUT=Path(__file__).resolve().parent
PIN={'R_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'}
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,v):
 assert Path(n).name==n
 (OUT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def require(x,m):
 if not x:raise ValueError(m)
class Reader:
 def __init__(self,b):self.b=b
 def span(self,s,n):
  require(0<=s<=len(self.b) and 0<=n<=len(self.b)-s,'out of bounds')
  return self.b[s:s+n]
 def unpack(self,f,p):return struct.unpack(f,self.span(p,struct.calcsize(f)))
