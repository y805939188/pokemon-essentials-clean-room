"""Data-only complete explicit Marshal link reception view; no loading classes/code."""
import datetime, hashlib, json
from pathlib import Path
OUT = Path(__file__).resolve().parent
parsed = json.loads((OUT/'static-recovery-001/current-serialized/messages_core.dat.json').read_text())
source = Path('/workspace/pokemon-essentials/Data/messages_core.dat').read_bytes()
assert len(source)==963270 and hashlib.sha256(source).hexdigest()=='ba73f82b8d55e0d2c008cf649c2b2197c242da187bfbbed70d18bd956cc1c359'
objects, links = {}, []
def walk(node, path):
    if not isinstance(node, dict) or 'type' not in node:
        return
    if node['type']=='@':
        links.append((node, path))
    elif 'object_index' in node:
        index=node['object_index']
        assert index not in objects
        objects[index]=(node,path)
    if 'wrapped' in node:
        walk(node['wrapped'],path+'.wrapped')
    for index, child in enumerate(node.get('items', [])):
        walk(child,path+'['+str(index)+']')
    for index, pair in enumerate(node.get('pairs', [])):
        walk(pair[0],path+'.pair'+str(index)+'.key')
        walk(pair[1],path+'.pair'+str(index)+'.value')
    for index, pair in enumerate(node.get('ivars', [])):
        walk(pair[0],path+'.ivar'+str(index)+'.key')
        walk(pair[1],path+'.ivar'+str(index)+'.value')
    if 'default' in node:
        walk(node['default'],path+'.default')
walk(parsed['root'],'root')
assert len(objects)==21303 and len(links)==178
rows=[]
for index,(node,path) in enumerate(links):
    start,end=node['start'],node['end_exclusive']
    raw=source[start:end]
    assert raw[0]==64
    c=int.from_bytes(raw[1:2],'little',signed=True)
    decoded=(0 if c==0 else c-5 if c>4 else c+5 if c < -4 else int.from_bytes(raw[2:],'little',signed=c<0))
    assert decoded==node['object_index']
    target,target_path=objects[decoded]
    assert target['start'] < start and target['type']=='"'
    text=bytes.fromhex(target['bytes_hex']).decode('utf8')
    assert text==target['text_utf8']
    rows.append({'link':index,'source_path':path,'source_span':[start,end],
                 'original_hex':raw.hex(),'target_object':decoded,'target_path':target_path,
                 'target_span':[target['start'],target['end_exclusive']],
                 'target_type':target['type'],'entire_target_text':text})
artifact={'schema':'gr8-complete-current-objectlinks/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'source':parsed['source'],'objects':len(objects),'links':rows,'link_count':len(rows),
          'generation_reading_credit':0,'target_execution':False}
(OUT/'messages-current-views/objectlinks.json').write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+'\n')
lines=[]
for r in rows:
    lines.append(str(r['link'])+' '+r['source_path']+' '+str(r['source_span'])+' '+r['original_hex']+' -> #'+str(r['target_object'])+' '+r['target_path']+' '+str(r['target_span'])+' '+json.dumps(r['entire_target_text'],ensure_ascii=False))
(OUT/'messages-current-views/objectlinks.txt').write_text('\n'.join(lines)+'\n')
print(json.dumps({'links':len(rows),'target_types':['string'],'all_original_link_tags_indices_and_target_text_validated':True,'semantic_reading_credit':0}))
