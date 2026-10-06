"""New read-only diff/document bookkeeping; no historical/reference execution."""
import subprocess,json,pathlib,hashlib,re,sys,importlib.util,functools
sys.dont_write_bytecode=True
D=pathlib.Path(__file__).parent
spec=importlib.util.spec_from_file_location('reader',D/'read_documents.py')
reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
docs=json.loads((D/'reading-documents.json').read_text())
values=json.loads((D/'reading-values.json').read_text())
value_ids={(v['type'],v['sha256']):v['id'] for v in values}
doc_paths={q['path']:i for i,q in enumerate(docs) if q['commit']==reader.A}
def typed_string(s):
    h=hashlib.sha256(json.dumps(s,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
    return value_ids.get(('str',h))
@functools.lru_cache(maxsize=None)
def blob(s,p):return subprocess.check_output(['git','show',s+':'+p])
out=[];missing=[]
for capture in json.loads((D/'stream-capture.json').read_text()):
    raw=subprocess.check_output(['git','diff']+capture['parameters'])
    assert len(raw)==capture['bytes'] and hashlib.sha256(raw).hexdigest()==capture['sha256']
    inv=json.loads((D/(capture['name']+'-inventory.json')).read_text())
    lines=raw.splitlines(keepends=True);checks=[]
    for g in inv['groups']:
        p=g['header'].split(' b/',1)[1];group=lines[g['start_line']-1:g['end_line']]
        added=any(l.startswith(b'new file mode') for l in group)
        before=[] if added else blob(capture['base'],p).splitlines(keepends=True)
        rebuilt=[];cursor=0;j=0;hunks=[]
        while j<len(group):
            m=re.match(rb'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',group[j])
            if not m:j+=1;continue
            oldstart=int(m[1]);oldcount=int(m[2] or b'1');newcount=int(m[4] or b'1')
            start=oldstart-1 if oldcount else oldstart
            rebuilt.extend(before[cursor:start]);cursor=start;j+=1;oc=nc=0
            oldmap=[]
            while oc<oldcount or nc<newcount:
                l=group[j];j+=1;prefix=l[:1];body=l[1:]
                if j<len(group) and group[j].startswith(b'\\ No newline at end of file'):
                    body=body.rstrip(b'\n');j+=1
                assert prefix in [b' ',b'+',b'-']
                if prefix in [b' ',b'-']:
                    assert before[cursor]==body,(p,cursor)
                    cursor+=1;oc+=1
                    s=body.decode().rstrip('\r\n');vi=typed_string(s)
                    oldmap.append({'old_line':cursor,'prefix':prefix.decode(),'value_id':vi,'body_sha256':hashlib.sha256(body).hexdigest()})
                    if vi is None and prefix==b'-':missing.append({'stream':capture['name'],'path':p,'line':cursor,'body':s})
                if prefix in [b' ',b'+']:rebuilt.append(body);nc+=1
            assert oc==oldcount and nc==newcount
            hunks.append({'old_start':oldstart,'old_count':oldcount,'new_start':int(m[3]),'new_count':newcount,'old_context_and_removal_map':oldmap})
        rebuilt.extend(before[cursor:]);actual=blob(reader.A,p)
        assert b''.join(rebuilt)==actual,p
        checks.append({'path':p,'stream_start_line':g['start_line'],'stream_end_line':g['end_line'],'group_sha256':hashlib.sha256(b''.join(group)).hexdigest(),'actual_document_index':doc_paths[p],'actual_blob_sha256':hashlib.sha256(actual).hexdigest(),'complete_reconstruction':True,'hunks':hunks})
    out.append({'stream':capture,'groups':checks,'complete_reconstruction':True})
(D/'stream-reading-map.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n')
# Missing text is navigation for a supplemental semantic read, never an omission waiver.
(D/'stream-removal-supplements.json').write_text(json.dumps(missing,ensure_ascii=False,indent=2)+'\n')
print('Both full streams reconstructed exactly; groups',*[len(q['groups']) for q in out],'unmatched removed line scalars',len(missing))
for q in missing:print(json.dumps(q,ensure_ascii=False))
