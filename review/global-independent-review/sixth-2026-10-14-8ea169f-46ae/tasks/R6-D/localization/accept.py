"""Record manual semantic acceptance only after a displayed contiguous corpus read."""
import audit,json,sys
name=sys.argv[1];a=int(sys.argv[2]);b=int(sys.argv[3]);p=audit.OUT/f'records-{name}.json';rows=json.loads(p.read_text());b=min(b,len(rows)-1)
for i in range(a,b+1):
 rows[i]['semantic_status']='read_this_round';rows[i]['semantic_scope']='literal display identity/body and localization token meaning; not gameplay truth'
audit.write(p.name,rows)
audit.append('reading-ledger.jsonl',{'path':f'Text_english_core/{name}.txt','unit_range':[a,b],'review_extent':'manual_semantic_accepted','notes':'Actual displayed bodies read in current turn. Literal statement/help/label semantics and localization role reviewed; not used as substitute for gameplay implementation rules.'})
inv=json.loads((audit.OUT/'inventory.json').read_text());counts={}
for x in inv:
 d=x['path'].split('/')[-1][:-4];r=json.loads((audit.OUT/f'records-{d}.json').read_text());n=sum(v['semantic_status']=='read_this_round' for v in r);counts[d]=(n,len(r)-n);x['semantic_read']=n;x['semantic_unread']=len(r)-n;x['review_extent']='semantic_complete_for_localization_body' if n==len(r) else 'partial_semantic'
audit.write('inventory.json',inv)
f=json.loads((audit.OUT/'source-to-formal.json').read_text())
for r in f:
 d,i=r['unit'].rsplit(':',1)
 if d==name and a<=int(i)<=b:r['semantic_status']='read_this_round'
audit.write('source-to-formal.json',f)
m=json.loads((audit.OUT/'feature-matrix.json').read_text())
for x in m:
 n,u=counts[x['feature']];x['semantic_read']=n;x['semantic_unread']=u;x['disposition']='READ' if not u else 'IN_PROGRESS_READING_DEBT'
audit.write('feature-matrix.json',m)
s=json.loads((audit.OUT/'task-status.json').read_text());s['coverage']['semantic_read']=sum(x[0] for x in counts.values());s['coverage']['semantic_unread']=sum(x[1] for x in counts.values());s['coverage']['zero_unread_completion_gate_satisfied']=s['coverage']['semantic_unread']==0;s['status']='IN_PROGRESS';s['reason']='Continuing all remaining auditable text bodies; reading debt is not an external blocker.';audit.write('task-status.json',s)
audit.write('remaining-unread.json',[{'path':x['path'],'semantic_unread':x['semantic_unread'],'unit_ids':[i for i,r in enumerate(json.loads((audit.OUT/('records-'+x['path'].split('/')[-1][:-4]+'.json')).read_text())) if r['semantic_status']=='not_read']} for x in inv if x['semantic_unread']])
audit.event('manual_semantic_accept',domain=name,unit_range=[a,b],semantic_read=s['coverage']['semantic_read'],semantic_unread=s['coverage']['semantic_unread']);print(json.dumps(s['coverage']))
