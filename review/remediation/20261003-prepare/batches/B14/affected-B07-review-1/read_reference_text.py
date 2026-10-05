import sys,pathlib,subprocess,json,hashlib
r=pathlib.Path('/workspace/reference-pokemon-essentials-B07'); c='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
assert subprocess.check_output(['git','-C',str(r),'rev-parse','HEAD'],text=True).strip()==c
p=sys.argv[1];b=(r/p).read_bytes();ls=b.decode().splitlines();ranges=[]
for q in sys.argv[2:]:
 a,z=map(int,q.split(':'));z=min(z,len(ls));assert 1<=a<=z;ranges.append([a,z]);print('\n'+p+':'+str(a)+'-'+str(z));print('\n'.join(f'{i}: {ls[i-1]}' for i in range(a,z+1)))
with open('/tmp/b14_r07_static_read_log.jsonl','a') as f:f.write(json.dumps({'commit':c,'path':p,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'lines':len(ls),'ranges':ranges},ensure_ascii=False)+'\n')
