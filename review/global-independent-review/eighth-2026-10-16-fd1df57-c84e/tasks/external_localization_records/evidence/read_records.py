from pathlib import Path
import sys, json, datetime
name=sys.argv[1]; start=int(sys.argv[2]) if len(sys.argv)>2 else 1; end=int(sys.argv[3]) if len(sys.argv)>3 else 100000
p=Path('/workspace/pokemon-essentials/Text_english_core')/(name+'.txt')
lines=p.read_text(encoding='utf-8-sig').splitlines()
out=[f'FILE {p.name} full physical lines={len(lines)}; requested records {start}-{end}. Every following JSON string is one complete record with key=translation, in order beginning at requested start. Record i maps to physical lines 2*i+3 and 2*i+4. Differing pairs have both full fields and explicit index. No record omitted. Header shown in full.']
for n,line in enumerate(lines[:4],1): out.append(f'L{n} '+json.dumps(line,ensure_ascii=False))
assert (len(lines)-4)%2==0
for index in range(start,min(end,(len(lines)-4)//2)+1):
 n=4+2*(index-1);a,b=lines[n:n+2]
 if a==b: out.append(json.dumps(a,ensure_ascii=False))
 else: out.append(f'R{index} L{n+1} key='+json.dumps(a,ensure_ascii=False)+f' L{n+2} translation='+json.dumps(b,ensure_ascii=False))
s='\n'.join(out)+'\n'
print(s,end='')
root=Path(__file__).parent/'reads';root.mkdir(exist_ok=True)
(root/(name+'-'+str(start)+'-'+str(end)+'.txt')).write_text(s)
with (Path(__file__).parent/'read-invocations.jsonl').open('a') as f:f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':sys.argv,'file':str(p),'record_range':[start,min(end,(len(lines)-4)//2)],'note':'Rendering only; semantic reading requires actual reviewer receipt; exit status on platform.'})+'\n')
