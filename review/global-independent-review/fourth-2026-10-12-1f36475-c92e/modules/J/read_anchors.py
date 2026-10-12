"""Review-only bounded source/spec reader; stores paths/ranges, never source text."""
import sys,json,pathlib,datetime
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[4]
SRC=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
LOG=HERE/'read-log.json'
records=json.loads(LOG.read_text()) if LOG.exists() else []
for req in json.loads(sys.stdin.read()):
    root=SRC if req['kind']=='source' else ROOT
    matches=list(root.glob(req['path']))
    if len(matches)!=1: raise RuntimeError((req,len(matches)))
    p=matches[0]; lines=p.read_text().splitlines()
    print('\n### '+req['kind']+' '+str(p.relative_to(root)))
    for a,b in req['ranges']:
        for i in range(a-1,min(b,len(lines))): print(f'{i+1}: {lines[i]}')
    records.append({'kind':req['kind'],'path':str(p.relative_to(root)),'ranges':req['ranges']})
LOG.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
