"""Lossless per-program action spelling; roles/numerical geometry remain separately addressable."""
from pathlib import Path
import json,collections,re
R=Path(__file__).resolve().parent
ps=json.loads((R/'static-push-roles.json').read_text())['glyphs']
syms={'SVTCA0':'Y','SVTCA1':'X','MIAP1':'m','MDAP1':'a','MDAP0':'A','SRP0':'p','SRP1':'r','SRP2':'s','IUP1':'U','IUP0':'V','RTG':'t','RTHG':'q','SHC0':'c','SHC1':'C','SHP0{1}':'j','SHP1{1}':'h','IP{1}':'i'}
def token(a):
 if a in syms:return syms[a]
 if a.startswith('MDRP'):return 'd'+a[4:]+';'
 if a.startswith('DELTAP'):return 'D'+a[6:]
 if a.startswith('SLOOP'):return 'L'+a[6:]+';'
 if a.startswith('SDS='):return 'S'+a[4:]+';'
 if a.startswith('SDB='):return 'B'+a[4:]+';'
 if a.startswith('SMD='):return 'M'+a[4:]+';'
 return '['+a+']'
def compress(tokens):
 # Only immediate repeated lexical sequences in one complete unit, no cross-program reuse.
 out=[];i=0
 while i<len(tokens):
  best=None
  for n in range(1,9):
   unit=tokens[i:i+n]
   if len(unit)!=n:continue
   count=1
   while tokens[i+count*n:i+(count+1)*n]==unit:count+=1
   gain=n*count-n-2
   if count>1 and (best is None or gain>best[0]):best=(gain,n,count,unit)
  if best and best[0]>0:
   _,n,count,unit=best;out.append('('+''.join(unit)+')*'+str(count)+';');i+=n*count
  else:out.append(tokens[i]);i+=1
 return ''.join(out)
(R/'glyph-spelling-glossary.json').write_text(json.dumps({'symbols':syms,'other':'[verbatim full action]; dN=MDRP decimal flag N; Dn{k}=DELTAPn with k pairs; Lk=SLOOP k; Sk=SDS k; Bk=SDB k; Mk=SMD k; (sequence)*n is immediate sequence repeated n times in this glyph only; F arguments are bottom-to-top stack schema; all nonpush actions retained. Every push instruction, byte/word encoding, literal value, source PC and consumer PC is retained in decoded-programs.json/static-push-roles.json. Geometry and CVT addresses have full-range typed disposition; all control values were actually read, including the separately expanded packed DELTA selectors.'},indent=2)+'\n')
(R/'glyphs.read.txt').write_text('\n'.join(p['unit']+':'+compress([token(a) for a in p['actions']]) for p in ps)+'\n')
print((R/'glyphs.read.txt').stat().st_size)
