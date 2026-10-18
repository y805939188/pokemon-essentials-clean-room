"""Navigation-only continuation; removes only separately evidenced types and read table."""
import pathlib,json,gzip,hashlib
ROOT=pathlib.Path(__file__).resolve().parent;readset=json.loads((ROOT/'game-pending-readset.json').read_text());typed={}
for n in ['numeric-typed-dispositions.jsonl.gz','ec-typed-dispositions.jsonl.gz']:
 for l in gzip.decompress((ROOT/n).read_bytes()).splitlines():
  r=json.loads(l);assert r['candidate_id'] not in typed;typed[r['candidate_id']]=r
table=json.loads((ROOT/'builtin-controller-readset.json').read_text());tablecover={}
for t in readset:
 for r in t['refs']:
  hits=[v for v in table['records'] if v['start']<=r['start'] and r['end_exclusive']<=v['end']]
  if hits:tablecover[r['candidate_id']]=hits[0]['record']
rows=[];covered=[]
for i,t in enumerate(readset,1):
 if i<=10450:continue
 refs=[r for r in t['refs'] if r['candidate_id'] not in typed and r['candidate_id'] not in tablecover]
 if refs:rows.append(dict(t,refs=refs,original_view_line=i))
 else:covered.append({'original_view_line':i,'read_id':t['read_id'],'covered_candidate_ids':[r['candidate_id'] for r in t['refs']]})
(ROOT/'game-continuation-readset.json').write_text(json.dumps(rows,ensure_ascii=False,separators=(',',':'))+'\n')
(ROOT/'game-continuation-view.txt').write_text('\n'.join(str(i)+' orig='+str(t['original_view_line'])+' '+t['read_id']+' '+t['text'].replace('\r','\\r').replace('\n','\\n') for i,t in enumerate(rows,1))+'\n')
proof={'qualification':'Rows removed only where all occurrence refs are exact separately typed numeric records or complete independently read257recordcontroller table. No vocabulary-basedclassification or semanticcreditfromscript.','continuation_rows':len(rows),'original_view_total':len(readset),'original_first_read_lines':10450,'table_candidate_coverage':tablecover,'covered_rows':covered}
(ROOT/'continuation-partition.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps({'continuation_rows':len(rows),'covered_rows':len(covered),'builtin_candidates':len(tablecover)}))
