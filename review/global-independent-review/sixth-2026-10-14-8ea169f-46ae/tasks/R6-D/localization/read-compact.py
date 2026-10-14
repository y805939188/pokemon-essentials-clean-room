"""Display contiguous corpus records with identity-copy deduplication only."""
import audit,sys,json
name=sys.argv[1];p=audit.REF/'Text_english_core'/f'{name}.txt'
lines=p.read_text(encoding='utf-8-sig').splitlines();records=json.loads((audit.OUT/f'records-{name}.json').read_text())
a=int(sys.argv[2]);b=min(int(sys.argv[3]),len(records)-1)
for start in range(a,b+1,8):
 out=[]
 for n in range(start,min(start+8,b+1)):
  k,v=lines[4+2*n:6+2*n]
  out.append(str(n)+':'+k+(' => '+v if k!=v else ''))
 print(' | '.join(out))
audit.append('reading-ledger.jsonl',{'path':str(p.relative_to(audit.REF)),'unit_range':[a,b],'line_range':[5+2*a,6+2*b],'sha256':audit.sha(p.read_bytes()),'review_extent':'semantic_display','method':'contiguous displayed keys and bodies; identity copies deduplicated; eight independently numbered records per output line'})
audit.event('read_compact_corpus',domain=name,unit_range=[a,b])
