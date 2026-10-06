"""New B14-G document/identity bookkeeping only. Never executes reference or historical tools."""
import json, pathlib, subprocess, hashlib, sys, re
G=pathlib.Path('review/remediation/20261003-prepare/batches/B14/integration-stage-1')
B=json.loads((G/'boundary-and-bindings.json').read_text())
A=B['accepted_predecessor'];C=B['candidate'];PLAN=B['fixed_PLAN'];REPORT=B['fixed_originalREPORT']
CONTRACT='review/remediation/20261003-prepare/batches/B09/acceptance-stage-1/B14-downstream-contract.json'
def git(commit,path):return subprocess.check_output(['git','show',commit+':'+path])
def obj(commit,path):return json.loads(git(commit,path))
def identity(data,path,binding,commit=None):
 d=dict(path=path,git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),binding=binding)
 if commit:d['commit']=commit
 return d
def save(name,value):(G/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def control_inputs():
 con=obj(A,CONTRACT);ids={c['id'] for c in con['contribution_controls']};out=[]
 for k in ['fixed_original_findings','fixed_approved_acceptance']:
  meta=con[k];o=obj(meta['commit'],meta['path'])
  if isinstance(o,list):
   for i,v in enumerate(o):
    if v['id'] in ids:out.append((meta['commit'],meta['path'],'/'+str(i),v))
  else:
   for i,v in o.items():
    if i in ids:out.append((meta['commit'],meta['path'],'/'+i,v))
 for path in [CONTRACT]+['review/remediation/20261003-prepare/batches/B09/acceptance-stage-1/'+s for s in ['acceptance-manifest.json','completion-statistics-successor.json','readiness-and-conflicts.json','report-corrections-successor.json','downstream-handshake.json']]:out.append((A,path,'',obj(A,path)))
 return out
def reading_values(inputs):
 seen={};entries=[];structures=[];aliases=[]
 def visit(v,source,p):
  if isinstance(v,(dict,list)):
   children=list(v) if isinstance(v,dict) else list(range(len(v)))
   structures.append(dict(source=source,selector=p,kind=type(v).__name__,children=children))
   for k in children:visit(v[k],source,p+'/'+str(k).replace('~','~0').replace('/','~1'))
  else:
   key=json.dumps(v,ensure_ascii=False,separators=(',',':'));loc=dict(source=source,selector=p)
   if key not in seen:
    seen[key]=len(entries);entries.append((loc,v))
   aliases.append(dict(**loc,value_index=seen[key]))
 for commit,path,p,v in inputs:visit(v,dict(commit=commit,path=path),p)
 return entries,structures,aliases
if __name__=='__main__':
 mode=sys.argv[1]
 if mode=='control-read':
  entries,structures,aliases=reading_values(control_inputs());lines=[]
  for n,(loc,v) in enumerate(entries):lines.append(str(n)+' '+loc['source']['path'].split('/')[-1]+'#'+loc['selector']+' = '+json.dumps(v,ensure_ascii=False))
  start=int(sys.argv[2]);end=int(sys.argv[3]);print('\n'.join(lines[start:end]));print('READ_RANGE',start,end,'TOTAL',len(lines))
  if start==0:save('control-reading-map.json',dict(method='Independent frozen-object scalar reading with lossless complete original container structure and exact selector aliases; repeated values reuse first exact scalar, never summary paraphrases.',inputs=[dict(commit=c,path=p,selector=s) for c,p,s,v in control_inputs()],structures=structures,scalar_source_selectors=[loc for loc,v in entries],aliases=aliases,unread_scalar_ranges=list(range(end,len(lines))),semantic_read_claim='Only emitted, nontruncated ranges count; final log supersedes initial pending ranges.'))
def evidence_inputs():
 out=[]
 for p in B['evidence_paths']+[p for r in B['report_bindings'] for p in r['paths']]:
  commit=C if p in B['evidence_paths'] else next(r['report_commit'] for r in B['report_bindings'] if p in r['paths'])
  data=git(commit,p)
  if p.endswith('.json'):out.append((commit,p,'',json.loads(data)))
  elif p.endswith('.jsonl'):
   for n,l in enumerate(data.decode().splitlines()):out.append((commit,p,'/'+str(n),json.loads(l)))
 return out
def semantic_units(inputs,seen=None):
 seen=seen or set();units=[];reuse=[]
 def walk(v,src,p):
  if isinstance(v,dict):
   for k,w in v.items():walk(w,src,p+'/'+k)
  elif isinstance(v,list):
   for i,w in enumerate(v):walk(w,src,p+'/'+str(i))
  else:
   key=json.dumps(v,ensure_ascii=False,separators=(',',':'))
   if key in seen:return
   seen.add(key)
   if not isinstance(v,str):return
   if re.fullmatch(r'[0-9a-f]{40,64}',v):return
   if v.startswith(('review/','deliverables/','specs/','Data/','PBS/','https://','/','@','git ')):return
   if not (re.search('[\u3400-\u9fff]',v) or (' ' in v and len(v)>30)):return
   if v.startswith(('{','[')):
    try:walk(json.loads(v),src,p+'/JSON_string_content');return
    except json.JSONDecodeError:pass
   units.append((dict(commit=src[0],path=src[1],selector=p),v))
 for c,path,p,v in inputs:walk(v,(c,path),p)
 return units
if __name__=='__main__' and sys.argv[1]=='evidence-read':
 base=set(json.dumps(v,ensure_ascii=False,separators=(',',':')) for _,v in reading_values(control_inputs())[0])
 units=semantic_units(evidence_inputs(),base);start=int(sys.argv[2]);end=int(sys.argv[3])
 for n,(loc,v) in enumerate(units[start:end],start):print(n,loc['path'].split('/')[-1]+'#'+'/'.join(loc['selector'].split('/')[-3:]),'=',json.dumps(v,ensure_ascii=False))
 print('UNITS',len(units),'READ',start,end)
 if start==0:save('evidence-reading-map.json',dict(method='Exact scalar reuse of complete independently read controls; report value maps retain their own immutable structures/identities. Unique narrative values are emitted for reading. Paths, pointers, hashes and numeric identity fields are bookkeeping, not behavior proof.',files=[identity(git(c,p),p,'EXACT_STATIC_INPUT',c) for c,p,s,v in evidence_inputs() if not s],narrative_selectors=[loc for loc,v in units],unread_narrative_range=[end,len(units)],reference_execution=0,historical_program_execution=0))

if __name__=='__main__' and sys.argv[1]=='literal-read':
    paths=B['evidence_paths']+[p for r in B['report_bindings'] for p in r['paths']]
    seen=set();units=[];mapping=[]
    # Main report bodies were read literally in this task; retain exact per-line reuse.
    for r in B['report_bindings']:
        for line in git(r['report_commit'],r['directory']+'report.md').decode().splitlines(keepends=True):seen.add(line)
    for p in paths:
        if p.endswith('.md') and not p.endswith('/report.md'):
            commit=C if p in B['evidence_paths'] else next(r['report_commit'] for r in B['report_bindings'] if p in r['paths'])
            for n,line in enumerate(git(commit,p).decode().splitlines(keepends=True),1):
                if line not in seen:
                    seen.add(line);units.append((dict(commit=commit,path=p,line=n),line))
                mapping.append(dict(commit=commit,path=p,line=n,sha256=hashlib.sha256(line.encode()).hexdigest()))
    start=int(sys.argv[2]);end=int(sys.argv[3])
    for n,(loc,v) in enumerate(units[start:end],start):print(str(n)+' '+loc['path'].split('B14/')[-1]+':'+str(loc['line'])+' '+v.rstrip('\n'))
    print('LITERAL_UNITS',len(units),'READ',start,end)
    if start==0:save('literal-reading-map.json',dict(method='Exact literal line reuse only; main eight report bodies separately read completely. Every other Markdown line retained with full frozen path/line/hash identity; no source/body normalization.',selectors=[loc for loc,v in units],all_lines=mapping,unread_unique_range=[end,len(units)]))


# Current G document metadata resolver. This never judges behavioral quality.
DOCUMENT_LABELS = {
    'WP59': ('specs/overworld/wp59-world-time-weather-field-moves.md', 'deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md'),
    'Fishing': ('specs/overworld/wp60-fishing.md', 'deliverables/final-specification-set/engine-overworld/wp60-fishing.md'),
    'Berry': ('specs/pokemon-rules/wp60-berry-plants.md', 'deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md'),
    'WP61': ('specs/pokemon-rules/wp61-field-passive-effects-and-blackout.md', 'deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md'),
    'WP16': ('specs/overworld/wp16-world-rendering-and-visual-transitions.md', 'deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md'),
}
def exact_heading_index(data):
    result={}
    for n,line in enumerate(data.decode().splitlines(keepends=True),1):
        m=re.fullmatch(r'(#{2,6})\s+(\d+(?:\.\d+)*)\.?\s+.+',line.rstrip('\r\n'))
        if m:
            number=m.group(2)
            if number in result:raise ValueError('Duplicate exact section number '+number)
            result[number]=dict(line=n,heading=line.rstrip('\r\n'),heading_sha256=hashlib.sha256(line.encode()).hexdigest())
    return result

def expand_named_sections(selector,index):
    out=[]
    for term in selector.split('/'):
        m=re.fullmatch(r'§(\d+(?:\.\d+)*)(?:–(\d+(?:\.\d+)*))?',term)
        if not m:raise ValueError('Unrecognized explicit selector '+selector)
        a=m.group(1);z=m.group(2)
        if z:
            at=tuple(map(int,a.split('.')));zt=tuple(map(int,z.split('.')))
            if len(at)!=len(zt) or at[:-1]!=zt[:-1] or at>zt:raise ValueError('Non-sibling named range '+term)
            numbers=['.'.join(map(str,at[:-1]+(v,))) for v in range(at[-1],zt[-1]+1)]
        else:numbers=[a]
        for number in numbers:
            if number not in index:raise ValueError('Missing exact named section '+number)
            if number not in out:out.append(number)
    return out

def bind_current_document(path,designs):
    labels=[label for label,paths in DOCUMENT_LABELS.items() if path in paths]
    if len(labels)!=1:raise ValueError('Unrecognized explicit document '+path)
    label=labels[0];data=pathlib.Path(path).read_bytes();index=exact_heading_index(data)
    doc=dict(path=path,document_label=label,document_role='ORIGINAL_SPEC' if path.startswith('specs/') else 'FINAL_SPEC',identity=identity(data,path,'CURRENT_G_EQUAL_EXACT_C3',C),clauses=[],clause_bindings=[],current_heading_locators=[],quality_interpretation='PENDING_EIGHT_EXACT_ACT_ULTRA_GATES')
    for design in designs:
        if design['document_label']!=label:raise ValueError('Foreign document label for '+path)
        selector=design['selector'];sections=expand_named_sections(selector,index);clause=label+selector+' '+design['description']
        doc['clauses'].append(clause)
        doc['clause_bindings'].append(dict(**design,expanded_sections=sections))
        for number in sections:
            loc=dict(clause=clause,document_label=label,selector=selector,section_number=number,**index[number],scope_role=design['scope_role'],scope='Exact named section navigation only; no whole-document or behavioral approval')
            if design.get('selection_kind')=='SINGLE_AUTHORIZED_SPLASH_SENTENCE':
                if number!='5.1.1':raise ValueError('Splash belongs to exact subsection5.1.1')
                rawlines=data.splitlines(keepends=True);selected=185 if path.startswith('specs/') else 162
                body=rawlines[selected-1];end=body.index(b'Snow');part=body[:end]
                if not part.decode().startswith('Rain类别') or not part.decode().rstrip().endswith('。'):raise ValueError('Wrong exact splash sentence')
                loc.update(selection_kind=design['selection_kind'],selected_line=selected,line_sha256=hashlib.sha256(body).hexdigest(),utf8_byte_start=0,utf8_byte_end_exclusive=end,selected_sentence_sha256=hashlib.sha256(part).hexdigest(),selected_sentence_bytes=len(part),ancestors_for_context_only=['5','5.1'],scope='Only the approved splash sentence before the untouched Snow tail; parent5.1 is context, not a second match')
            doc['current_heading_locators'].append(loc)
    return doc
