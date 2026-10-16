"""Read fixed static ranges into ignored views; this does not execute target code."""
import hashlib,json,pathlib,subprocess,sys
P=pathlib.Path(__file__).resolve().parent
spec=json.loads((P/'private'/sys.argv[1]).read_text());lines=[];identities=[]
for z in spec:
 repo='/workspace/pokemon-essentials' if z['repo']=='R' else '/workspace/pokemon-essentials-clean-room'
 commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' if z['repo']=='R' else 'fd1df570cad987dc3852a3b958f03916e317f7fe'
 data=subprocess.check_output(['git','-C',repo,'show',commit+':'+z['path']]);txt=data.decode().splitlines();identity={**z,'commit':commit,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),'linecount':len(txt),'execution':'NOT_EXECUTED','ranges_generated_not_automatically_read':True};identities.append(identity)
 for a,b in z['ranges']:
  if b is None:b=len(txt)
  assert 1<=a<=b<=len(txt),(z,a,b,len(txt))
  lines.append('FILE '+z['repo']+' '+z['path']+' '+str([a,b]))
  lines.extend(str(n)+':'+txt[n-1] for n in range(a,b+1))
frames=[];buf=''
for line in lines:
 if len(buf)+len(line)>12500 and buf:frames.append(buf);buf=''
 buf+=line+'\n'
if buf:frames.append(buf)
stem=sys.argv[1].replace('.json','')
for i,buf in enumerate(frames):(P/'views'/f'{stem}-{i:03}.txt').write_text(buf)
(P/'private'/f'{stem}-identities.json').write_text(json.dumps(identities,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'stem':stem,'frames':len(frames),'lines':len(lines),'chars':sum(map(len,frames))}))
