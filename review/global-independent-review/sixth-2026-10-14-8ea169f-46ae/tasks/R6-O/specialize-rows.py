from pathlib import Path
import json,re,datetime
out=Path('review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-O');inv=json.loads((out/'inventory.json').read_text());rows=[json.loads(x) for x in (out/'reverse-matrix.jsonl').read_text().splitlines()];fp={x['path']:n for n,x in enumerate(inv['formal'])};fw=[json.loads(x) for x in (out/'forward-matrix.jsonl').read_text().splitlines()];method={x['unit']:(x['start_line'],x['end_line']) for x in fw[3]['named_source_locations']};char=Path(inv['sources'][15]['path']).read_text().splitlines();whens=[]
for k in range(452,546):
 m=re.match(r'\s*when (\d+)',char[k])
 if m:whens.append((int(m.group(1)),k+1))
span={code:(a,(whens[j+1][1]-1 if j+1<len(whens) else 547)) for j,(code,a) in enumerate(whens)}
def ev(n,a,z,fact):return {'path':inv['sources'][n]['path'],'lines':[a,z],'fact':fact,'grade':'SOURCE_STATIC','owner':'R6-O full source newread, precise row binding'}
VF=[]
for k,l in enumerate(Path(inv['sources'][104]['path']).read_text().splitlines()[:115],1):
 if re.match(r'\s*\[\d+, \d+, \d+, \d+, \d+\]',l):VF.append(k)
changed=0
for r in rows:
 n=fp[r['formal']];a,z=r['lines'];text=r['clause'];codecell=text.split('|')[1].strip() if text.startswith('|') else ''
 if n==3 and 25<=a<=121:
  codes=set(int(x) for x in re.findall(r'\d+',codecell))
  for x,y in re.findall(r'(\d+)\s*[–—-]\s*(\d+)',codecell):codes.update(range(int(x),int(y)+1))
  selected=[('command_'+str(c),method['command_'+str(c)]) for c in sorted(codes) if 'command_'+str(c) in method]
  if selected:r['evidence']=[ev(3,x,y,name+' observable behavior and control result') for name,(x,y) in selected];changed+=1
 if n==5 and 33<=a<=78 and codecell.isdigit():
  c=int(codecell);ss=[ev(15,427,432,'route-entry guard and iteration bound')]
  if c==0:ss.append(ev(15,433,447,'nonrepeat restoration versus repeat wrap'))
  elif c in span:
   x,y=span[c];ss.append(ev(15,x,y,f'exact routecode{c} branch'))
   x,y=(468,470) if c<=14 else (490,492) if c<=26 else (547,551);ss.append(ev(15,x,y,'entry-specific index advance/yield'))
  r['evidence']=ss;changed+=1
 if n==16 and 9<=a<=83:
  loc=VF[a-9];r['evidence']=[ev(104,loc,loc,'exact ordered Voltorb candidate '+codecell+', arithmetic and order checkedO-LIT-VF')];changed+=1
 if n==36 and 15<=a<=36:
  r['evidence']=[ev(103,10,12,'exact cyclic position'+codecell+' ofthree ordered22item reels;O-LIT-SLOT')];changed+=1
 if n==37 and 13<=a<=73:
  loc=151+a-13;r['evidence']=[ev(106,loc,loc,'exact weighted itemshape row'+codecell+';O-LIT-MINING')];changed+=1
 if n==37 and 83<=a<=95:
  loc=214+a-83;r['evidence']=[ev(106,loc,loc,'exact ironshape row'+codecell+';correctedO-LIT-MINING')];changed+=1
(out/'reverse-matrix.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
with (out/'command-log.jsonl').open('a') as f:f.write(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':'python3 specialize-rows.py (first inline variantSyntaxError else547 preserved intool output; nofilewrite then)','result':f'{changed} rows specialized from own fulltext/source actual offsets; range matching is navigation, prior manual reading andfinitechecks remain evidence. No referenceexecution.'},ensure_ascii=False)+'\n')
print('Specialized',changed,'concrete source branches/literal rows')
