# Independent arithmetic audit only. This does not import/evaluate/execute target Ruby.
from pathlib import Path
import re,json,hashlib,datetime
P=Path(__file__).parent;src=Path('/workspace/pokemon-essentials/Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb');raw=src.read_bytes();txt=raw.decode();out={}
def expected(k,n):
 if n==1:return 0
 if k=='Medium':return n**3
 if k=='Fast':return 4*n**3//5
 if k=='Slow':return 5*n**3//4
 if k=='Parabolic':return 6*n**3//5-15*n*n+100*n-140
 if k=='Erratic':
  if n<=50:return n**3*(100-n)//50
  if n<=68:return n**3*(150-n)//100
  if n<=98:return n**3*((1911-10*n)//3)//500
  return n**3*(160-n)//100
 if k=='Fluctuating':
  if n<=15:return n**3*(24+(n+1)//3)//50
  if n<=35:return n**3*(14+n)//50
  return n**3*(32+n//2)//50
 raise ValueError(k)
for match in re.finditer(r':id\s*=>\s*:(\w+),.*?:exp_values\s*=>\s*\[(.*?)\]',txt,re.S):
 k=match[1];values=list(map(int,re.findall(r'-?\d+',match[2])));assert len(values)==101,(k,len(values));diff=[dict(level=n,source=values[n],expected=expected(k,n)) for n in range(1,101) if values[n]!=expected(k,n)];out[k]=dict(checked_levels=[1,100],checked_values=100,index0=values[0],anchors=[values[1],values[50],values[100]],mismatches=diff)
assert set(out)=={'Medium','Erratic','Fluctuating','Parabolic','Fast','Slow'}
r=dict(schema='gr8-cre-c-growth-independent-arithmetic/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),reader='/root/creature_a_atomic_reception',source_sha256=hashlib.sha256(raw).hexdigest(),source_bytes=len(raw),source_semantic_credit='Sameactualcontext earlierfull188L source read; this parser freezes table numbers only',checked_table_values=600,curves=out,table_mismatches=sum(len(v['mismatches']) for v in out.values()),explicit_max101_registered_formula=dict(Erratic=(101**4+2000*101**3)//3500,Fluctuating=((101**3+101//2+32)*4)//201),business='NOT_EXECUTED',helper_execution='AUDIT_ONLY_PURE_ARITHMETIC',qualification='No target code execution, simulated session, native runtime or fullconsumer/global PASS; default max100 clamp separately defined by ownsource/static formal.')
(P/'curve-arithmetic-check.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False));assert r['table_mismatches']==0
