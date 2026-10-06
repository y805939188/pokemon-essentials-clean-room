import json,pathlib,re,sys
D=pathlib.Path(__file__).parent;vs=json.loads((D/'reduced-values.json').read_text());q=[]
for i,x in enumerate(vs):
 z=x['value']
 pure=not isinstance(z,str) or bool(re.fullmatch(r'[\x21-\x7e]+',z)) or bool(re.fullmatch(r'(?:review|deliverables|specs|planning|audit|root|agents|Data|PBS)/[A-Za-z0-9_ ./()@:+\-]+\.(?:md|json|tsv|csv|rb|txt|dat|pdf|png|rxdata|jsonl)',z))
 code='.py/text/' in x['first']
 if x['seed_read'] or (pure and not code):continue
 q.append(i)
(D/'semantic-queue.json').write_text(json.dumps(q)+'\n')
reuse={x['queue_index'] for x in json.loads((D/'exact-framed-reuse.json').read_text())}
structural={x['queue_index'] for x in json.loads((D/'structural-queue-indices.json').read_text())}
a=int(sys.argv[1]);used=0;budget=11000
progress=json.loads((D/'progress.json').read_text());progress['audit_queue_consumed']=[0,a];progress['audit_next']=a;(D/'progress.json').write_text(json.dumps(progress,indent=2)+'\n')
for k in range(a,len(q)):
 i=q[k];x=vs[i]
 if k in reuse or k in structural:continue
 loc=x['first'].replace('review/remediation/20261003-prepare/batches/B14/','')
 line=f'{k} V{i} {loc} {json.dumps(x["value"],ensure_ascii=False)}\n'
 if used and used+len(line)>budget:break
 print(line,end='');used+=len(line)
else:k=len(q)
print('NEXT_QUEUE',k,'TOTAL',len(q))
logfile=D/'audit-display-log.json';log=json.loads(logfile.read_text()) if logfile.exists() else [];log.append({'start':a,'end_exclusive':k,'queue_total':len(q),'output_complete_claim':False,'note':'Delivery range; acknowledged only by next start in progress.json'});logfile.write_text(json.dumps(log,indent=2)+'\n')
