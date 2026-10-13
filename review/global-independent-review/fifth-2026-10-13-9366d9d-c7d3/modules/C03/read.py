import sys,json,pathlib,hashlib,subprocess
O=pathlib.Path(__file__).parent
R=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B='9366d9d17aaeac3b4414236468affa650fb3dd27'
t,p,*ranges=sys.argv[1:]
b=(R/p).read_bytes() if t=='R' else subprocess.check_output(['git','show',B+':'+p])
lines=b.decode().splitlines(); rs=[list(map(int,x.split(':'))) for x in ranges] if ranges else [[1,len(lines)]]
print(t,p,'total',len(lines))
for a,z in rs:
 for i in range(a,min(z,len(lines))+1): print(f'{i}: {lines[i-1]}')
with (O/'direct-read-log.jsonl').open('a') as f:f.write(json.dumps({'root':'R' if t=='R' else 'B5','path':p,'sha256':hashlib.sha256(b).hexdigest(),'ranges':rs,'line_count':len(lines)},ensure_ascii=False)+'\n')
