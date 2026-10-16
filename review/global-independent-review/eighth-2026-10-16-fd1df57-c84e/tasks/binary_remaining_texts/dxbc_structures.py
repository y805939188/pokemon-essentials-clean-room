"""DXBC container boundaries and readable chunk metadata only, no shader execution."""
import pathlib,struct,json,hashlib,gzip,re
ROOT=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();out=ROOT/'compiled-shader-objects';out.mkdir(exist_ok=True);good=[];bad=[]
def sha(x):return hashlib.sha256(x).hexdigest()
for match in re.finditer(b'DXBC',b):
 s=match.start()
 try:
  version,size,count=struct.unpack_from('<III',b,s+20);assert version==1 and 32<=size<=1048576 and s+size<=len(b) and 0<count<=64 and 32+4*count<=size
  chunks=[]
  for i in range(count):
   rel=struct.unpack_from('<I',b,s+32+4*i)[0];assert 32+4*count<=rel<=size-8;p=s+rel;tag=b[p:p+4].decode('ascii');n=struct.unpack_from('<I',b,p+4)[0];assert p+8+n<=s+size;raw=b[p+8:p+8+n];texts=[]
   for m in re.finditer(rb'[\x20-\x7e]{4,}',raw):texts.append({'offset':p+8+m.start(),'end':p+8+m.end(),'text':m.group().decode()})
   row={'tag':tag,'start':p,'payload_start':p+8,'end':p+8+n,'payload_bytes':n,'payload_sha256':sha(raw),'printable_metadata_candidates':texts}
   if tag in ('SHDR','SHEX'):
    v,tokens=struct.unpack_from('<II',raw);row.update(shader_version_word=hex(v),declared_token_count=tokens,actual_dwords=n//4,token_length_matches=tokens*4==n)
   chunks.append(row)
  spans=sorted((r['start'],r['end']) for r in chunks);assert all(a[1]<=z[0] for a,z in zip(spans,spans[1:]));raw=b[s:s+size];path=out/(str(s)+'.dxbc');path.write_bytes(raw);good.append({'start':s,'end':s+size,'bytes':size,'sha256':sha(raw),'header_version':version,'header_checksum_hex':b[s+4:s+20].hex(),'checksum_algorithm_not_verified':True,'chunk_count':count,'chunks':chunks,'path':str(path.relative_to(ROOT))})
 except (AssertionError,ValueError,struct.error,UnicodeDecodeError) as e:bad.append({'start':s,'reason':'signature candidate failed container bounds/tag parse','error_type':type(e).__name__})
ev={'containers':good,'rejected_signature_candidates':bad,'qualification':'Compiled GPUprogram objects structurally bounded only. Printablemetadata separately read. Tokenizedbytecode/opcode/controlflow, target selection/compilation/rendering remains unreceived L05/nativeboundary; not counted among55priorGLSLmainsor5preludes.'}
(ROOT/'compiled-shader-container-structures.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n');rows=json.loads((ROOT/'game-after-float-occurrences.json').read_text());done=[];left=[]
for row in rows:
 hits=[g for g in good if g['start']<=row['start'] and row['end_exclusive']<=g['end']]
 if hits:done.append(dict(row,semantic_status='STRUCTURE_PARSED_COMPILED_PROGRAM_METADATA',type_evidence={'kind':'DXBC_CONTAINER_SUBRUN','evidence':'compiled-shader-container-structures.json','container_start':hits[0]['start'],'container_end':hits[0]['end'],'reason':'Exact DXBC header/chunk bounds; candidate insidecompiledshadercontainer. Readablemetadata reception separate, shaderbehaviorNOT_REVIEWED; notopaque-exemptionofothertext.'}))
 else:left.append(row)
(ROOT/'dxbc-structure-dispositions.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode(),mtime=0));(ROOT/'game-after-dxbc-occurrences.json').write_text(json.dumps(left,separators=(',',':'))+'\n');print(json.dumps({'containers':[{k:r[k] for k in ('start','end','bytes','sha256','chunk_count')} for r in good],'rejected':bad,'candidate_intersections':len(done)},ensure_ascii=False))
