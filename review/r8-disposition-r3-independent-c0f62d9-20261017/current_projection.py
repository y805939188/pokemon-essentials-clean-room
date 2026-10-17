#!/usr/bin/env python3
"""Independent exact21 new-heading identities and current-readable count projection."""
from pathlib import Path
from collections import Counter
import ast,hashlib,json,subprocess,re,unicodedata
O=Path(__file__).resolve().parent;R=O.parents[1];S=R/'planning/implementation-routing/r8-20261017';E=O/'evidence';C='c0f62d973180679134f2eb1a488c1dc359c8658f';CUR='5f87743293290de2e219ecdd6c19e88280f60c9a'
def sha(b):return hashlib.sha256(b).hexdigest()
# Compile only this review's previously inspected standalone Markdown parser.
tree=ast.parse((O/'static_audit.py').read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='parse');exec(compile(ast.Module(body=[fn],type_ignores=[]),'<independent-heading-parser>','exec'))
def blob(p):return subprocess.check_output(['git','show',CUR+':'+p],cwd=R)
m=json.loads((S/'routing-manifest.json').read_text());cov=json.loads((S/'current-section-coverage.json').read_text());hist=json.loads((S/'section-coverage.json').read_text());mapping=json.loads((S/'revisions/r3/new-heading-mappings.json').read_text());features={f['feature_id']:f for f in m['features']};docs={d['source']['path']:d for d in m['documents']};oldkeys={(s['path'],s['anchor'])for s in hist['sections']};new={(s['path'],s['anchor']):s for s in cov['sections']if(s['path'],s['anchor'])not in oldkeys};results=[]
assert mapping['source_identity_heading_sha256_convention']=='SHA256_UTF8_TITLE_ONLY'
for item in mapping['accepted_mappings']:
 p=item['document'];b=blob(p);hs,ls=parse(b);h=next(x for x in hs if x['anchor']==item['anchor']);s=new[(p,h['anchor'])]
 expected={'commit':CUR,'document':p,'anchor':h['anchor'],'heading':h['title'],'heading_level':h['level'],'heading_sha256':sha(h['title'].encode()),'raw_markdown_heading_sha256':h['heading_sha256'],'line_ranges':[[h['line_start'],h['line_end']]],'unit_sha256':sha(''.join(ls[h['line_start']-1:h['line_end']]).encode()),'file_sha256':sha(b),'file_git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'file_bytes':len(b)}
 assert item['source_identity']==expected
 assert s['feature_refs']==item['feature_refs']and s['metadata_refs']==item['metadata_refs']
 for source in item['consumer_fixed_sources']:
  actual=features[source['feature_id']]['source'];assert all(source['source'][k]==actual[k]for k in ['commit','document','anchor','line_ranges'])
 results.append({'path':p,'anchor':h['anchor'],'identity':expected,'feature_refs':s['feature_refs'],'metadata_refs':s['metadata_refs'],'mechanical_verdict':'PASS_EXACT_GIT_AND_PROJECTION','semantic_review':'Attributed domain/source ledgers; identity does not prove consumer relevance.'})
assert len(results)==21 and {(x['path'],x['anchor'])for x in results}==set(new)
text=(S/'current-coverage.md').read_text();assert CUR in text;rows={}
for line in text.splitlines():
 if line.startswith('| deliverables/final-specification-set/'):
  cells=[x.strip()for x in line.split('|')[1:-1]];assert len(cells)==5;assert cells[0]not in rows;rows[cells[0]]=cells
hc=Counter(x['path']for x in hist['sections']);cc=Counter(x['path']for x in cov['sections']);nc=Counter(x['path']for x in results)
assert set(rows)==set(docs)
for p,cells in rows.items():
 assert list(map(int,cells[1:4]))==[hc[p],cc[p],nc[p]]
 events=docs[p]['upstream']['accepted_events'];assert all(e in cells[4]for e in events)
 if not events:assert '源字节未变' in cells[4]
result={'candidate':C,'current':CUR,'all21_new_heading_identity_checks':results,'all131_current_readable_summary_rows_exact':True,'current_heading_count':sum(cc.values()),'historical_heading_count':sum(hc.values()),'new_heading_count':sum(nc.values()),'semantic_qualification':'No semanticPASS inferred from metadata counts or matching identity; independent domain review separate.'}
(E/'independent-current-projection.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'headings':sum(cc.values()),'new':len(results),'current_readable_rows':len(rows),'result':'PASS_STATIC_PROJECTION_ONLY'}))
