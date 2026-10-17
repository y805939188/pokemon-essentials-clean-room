#!/usr/bin/env python3
"""Independent all-row/explicit-scope-column Markdown navigation projection."""
from pathlib import Path
import collections,hashlib,json,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];SRC=ROOT/'planning/implementation-routing/r8-20261017'
m=json.loads((SRC/'routing-manifest.json').read_bytes());active={f['feature_id']:f for f in m['features']};rows={};texts={};checks=[]
for p in sorted((SRC/'views').glob('*.md')):
 text=p.read_text();texts[str(p)]=text
 for line_no,line in enumerate(text.splitlines(),1):
  mt=re.match(r'^\| (FR-\d{6}) / ',line)
  if not mt:continue
  fid=mt[1];assert fid not in rows
  cells=re.split(r'(?<!\\)\|',line)[1:-1];assert len(cells)==8,(fid,len(cells));rows[fid]=(p,line_no,line,cells)
assert set(rows)==set(active)and len(rows)==736
for fid,f in active.items():
 p,n,line,cells=rows[fid]
 assert f['future_plan']['destination']in cells[3]and f['destination_verification']['status']in cells[5]
 assert f['current_applicability']['snapshot_commit']in cells[2]
 assert f['future_plan']['stage']in cells[6]and f['implementation']['status']in cells[6]and f['implementation']['acceptance_status']in cells[6]
 for responsibility in f['future_plan']['responsibilities']:assert responsibility['scope'].replace('|','\\|')in cells[3],fid
 for child in f['functional_scope']['excluded_child_refs']:
  cp,cn,cline,ccells=rows[child];anchor=f'<a id="{child.lower()}"></a>';link=f'[{child}](#{child.lower()})'
  assert '排除的独立子功能'in cells[2]and link in cells[2]and cp==p
  assert anchor in ccells[0]and texts[str(p)].count(anchor)==1
  checks.append({'parent':fid,'child':child,'view':str(p.relative_to(ROOT)),'parent_line':n,'child_line':cn,'scope_column_link':link,'unique_child_anchor':anchor,'verdict':'PASS_STATIC_NAVIGATION'})
prior=json.loads((ROOT/'planning/implementation-routing/r8-20261017/revisions/r2/tools/root-tool-resolution.json').read_bytes())
old29=set(prior['findings'][0]['affected_parent_ids_in_review']);parents={x['parent']for x in checks};assert old29<=parents and any(x['parent']=='FR-000067'and x['child']=='FR-000769'for x in checks)
meta=(SRC/'views/metadata.md').read_text();found=re.findall(r'^\| (META-\d{6}) / ',meta,re.M);assert len(found)==33 and set(found)=={x['metadata_id']for x in m['metadata_records']}
result={'candidate':'a32873d2860b15d9f5e27727db8f131f4ec433b6','active_rows_checked':len(rows),'metadata_rows_checked':len(found),'all_original29_missing_parents_fixed':True,'parents':len(parents),'children':len({x['child']for x in checks}),'edges':len(checks),'checks':checks,'result':'PASS_STATIC_ALL_ROW_PROJECTION_AND_NAVIGATION','qualification':'No browser/screen/host execution. Byte reconstruction and author two navigation negatives are separately replayed; classification/consumer semantics are independently reviewed by domains.'}
(OUT/'evidence/independent-view-projection.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='checks'},ensure_ascii=False))
