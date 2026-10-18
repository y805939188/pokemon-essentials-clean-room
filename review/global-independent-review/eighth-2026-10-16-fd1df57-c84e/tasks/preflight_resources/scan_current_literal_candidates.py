"""Independent finite ASCII-run discovery, not a claim of complete program recovery."""
from pathlib import Path
import hashlib, json, re, subprocess
O=Path(__file__).resolve().parent
R=Path('/workspace/pokemon-essentials')
commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
known=json.loads((O/'current-programs-v2/inventory.json').read_text())
rules={
 'GLSL_MAIN':rb'\bvoid\s+main\s*\(',
 'GLSL_PRELUDE':rb'(?:#define\s+(?:FRAGMENT_SHADER|GLSLES|TEX_[A-Z_]+)|precision\s+(?:lowp|mediump|highp)\s+float)',
 'RUBY_DECLARATION':rb'(?m)^\s*(?:module|class|def)\s+[A-Za-z_:]',
 'C_GENERATOR':rb'(?:\bVALUE\b|\brb_[A-Za-z0-9_]+\s*\(|\bMJIT\b|#if\s)',
 'JAVASCRIPT_DECLARATION':rb'(?:\bfunction\s+[A-Za-z_][A-Za-z0-9_]*\s*\(|\bvar\s+[A-Za-z_][A-Za-z0-9_]*\s*=)'
}
rows=[]; summary=[]
for name in ['Game.exe','x64-msvcrt-ruby310.dll','zlib1.dll','animmaker.exe','extendtext.exe']:
 data=(R/name).read_bytes()
 frozen=subprocess.run(['git','-C',str(R),'show',commit+':'+name],check=True,capture_output=True).stdout
 assert data==frozen
 count=0; candidates=[]
 for m in re.finditer(rb'[\x09\x0a\x0d\x20-\x7e]{12,}',data):
  count+=1; raw=m.group(); kinds=[key for key,pat in rules.items()if re.search(pat,raw)]
  if not kinds:continue
  overlaps=[x['id']for x in known if Path(x['path']).name==name and x['start']<=m.start() and m.end()<=x['end_exclusive']]
  row=dict(id='ASCII-CAND-'+str(len(rows)+1).zfill(4),path=name,start=m.start(),end_exclusive=m.end(),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),rules=kinds,contained_in_known=overlaps,text=raw.decode('ascii'),semantic_status='KNOWN_READ_UNIT' if overlaps else 'UNREAD_DISCOVERY_CANDIDATE')
  rows.append(row);candidates.append(row)
 summary.append(dict(path=name,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),ascii_runs_min12=count,candidates=len(candidates),known_contained=sum(bool(x['contained_in_known'])for x in candidates),not_contained=sum(not x['contained_in_known']for x in candidates)))
qualification='All bytes scanned for these five exact ASCII-run rules. This does not find non-ASCII/UTF16/obfuscated/compressed/unmatched grammar programs, or establish full native CFG, construction, selection or execution. A marker hit is only a candidate, not proof of a coherent program.'
(O/'current-literal-discovery.json').write_text(json.dumps(dict(source_commit=commit,rules={k:v.decode()for k,v in rules.items()},qualification=qualification,summary=summary,rows=rows),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(summary=summary,qualification=qualification),ensure_ascii=False))
for x in rows:
 if not x['contained_in_known']:print(x['id'],x['path'],x['start'],x['end_exclusive'],x['rules'],repr(x['text']))
