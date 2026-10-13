from pathlib import Path
import json,hashlib
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
REF=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B='9366d9d17aaeac3b4414236468affa650fb3dd27'
def read(n): return json.loads((OUT/n).read_text())
def write(n,d): (OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def identity(p,root,ver):
 b=p.read_bytes(); n=len(b.splitlines())
 return dict(path=str(p.relative_to(root)),version=ver,git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),sha256=hashlib.sha256(b).hexdigest(),line_count=n,material_availability='available_text')
def covered(path,ranges,semantic,kind='sources'):
 d=read('reading-coverage.json'); root=REF if kind=='sources' else ROOT; ver=R if kind=='sources' else B
 e=next((x for x in d[kind] if x['path']==path),None)
 if e is None: e=identity(root/path,root,ver); d[kind].append(e)
 e.setdefault('semantic_ranges',[]).extend(semantic)
 prior=e.get('read_ranges',[]); rr=prior+ranges; rr.sort(); merged=[]
 for a,z in rr:
  if merged and a<=merged[-1][1]+1: merged[-1][1]=max(z,merged[-1][1])
  else: merged.append([a,z])
 e['read_ranges']=merged; e['unreviewed_ranges']=[]; start=1
 for a,z in merged:
  if start<a: e['unreviewed_ranges'].append([start,a-1])
  start=max(start,z+1)
 if start<=e['line_count']: e['unreviewed_ranges'].append([start,e['line_count']])
 e['review_extent']='full' if not e['unreviewed_ranges'] else 'partial'
 e['evidence_level']='static_semantic_analysis'; write('reading-coverage.json',d)
def append(n,key,rows):
 d=read(n); d[key]+=rows; write(n,d)
def progress(next_range,summary):
 c=read('reading-coverage.json'); d=read('progress.json'); d.update(status='in_progress',complete=False,next_actual_range=next_range,latest_semantic_summary=summary,not_reviewed=[dict(path=x['path'],review_extent=x['review_extent'],unreviewed_ranges=x['unreviewed_ranges']) for x in c['sources'] if x['review_extent']!='full']); write('progress.json',d)
