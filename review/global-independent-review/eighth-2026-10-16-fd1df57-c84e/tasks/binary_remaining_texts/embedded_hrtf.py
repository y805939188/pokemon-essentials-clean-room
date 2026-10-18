"""Recover exact embedded MHRv3 byte structure, not audio rendering."""
import pathlib,json,struct,hashlib,gzip,statistics
ROOT=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();s=11394336;assert b[s:s+8]==b'MinPHR03';rate=struct.unpack_from('<I',b,s+8)[0];ch,ir,nf=b[s+12:s+15];assert ch in (0,1) and ir>0 and nf>0;p=s+15;fields=[];total=0
for i in range(nf):
 dist,ne=struct.unpack_from('<HB',b,p);start=p;p+=3;az=list(b[p:p+ne]);p+=ne;assert len(az)==ne and min(az)>0;fields.append({'field':i,'header_start':start,'header_end':p,'distance_millimeters':dist,'elevations':ne,'azimuth_counts':az,'ir_count':sum(az)});total+=sum(az)
channels=ch+1;sample_start=p;sample_end=p+total*channels*ir*3;delay_start=sample_end;end=delay_start+total*channels
samples=[int.from_bytes(b[z:z+3],'little',signed=True) for z in range(sample_start,sample_end,3)];delays=list(b[delay_start:end]);assert len(samples)==total*channels*ir and len(delays)==total*channels
# Native window3453611 loads exact start and end pointers into streambuffer pair.
native_end_va=0x140af2d01;assert native_end_va-5368709120-5632==end
raw=b[s:end];(ROOT/'embedded-default-44100.mhr').write_bytes(raw)
meta={'source':'Game.exe','start':s,'end':end,'bytes':end-s,'sha256':hashlib.sha256(raw).hexdigest(),'version':3,'sample_rate_hz':rate,'channel_type':ch,'channels':channels,'ir_size':ir,'fields':fields,'total_ir':total,'samples':{'start':sample_start,'end':sample_end,'coefficient_format':'signed24-little-endian','count':len(samples),'min':min(samples),'max':max(samples),'sha256':hashlib.sha256(b[sample_start:sample_end]).hexdigest()},'delays':{'start':delay_start,'end':end,'count':len(delays),'min':min(delays),'max':max(delays),'sha256':hashlib.sha256(b[delay_start:end]).hexdigest()},'native_start_instruction_offset':3453611,'native_end_pointer_va':hex(native_end_va),'native_evidence':'native-3447632.stdout:1326–1337 (only this local window read;whole15143bytefunctionUNREAD/nativeCFGlimit)','qualification':'Complete byte/field/coefficients/delay structure derived and exact native stream endpoints agree. No auditory/sample semantics or selectedbackend/filtersynthesisproved.'}
f=pathlib.Path('/usr/share/openal/hrtf/Default HRTF.mhr');d=f.read_bytes();meta['installed_comparator']={'path':str(f),'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'header_hex':d[:15].hex(),'equal':d==raw}
(ROOT/'embedded-hrtf-structure.json').write_text(json.dumps(meta,indent=2)+'\n')
rows=json.loads((ROOT/'game-after-ec-occurrences.json').read_text());done=[];left=[]
for r in rows:
 if s<=r['start'] and r['end_exclusive']<=end:done.append(dict(r,semantic_status='INVENTORY_ONLY_TYPED',type_evidence={'kind':'MHRV3_HEADER_COEFFICIENT_DELAY_SUBRUN','evidence':'embedded-hrtf-structure.json','start':s,'end':end,'reason':'Exact MHRv3 structured header, signed24coefficients andbyte delays; native stream begin/end match complete80353byteblob. Media meaning isseparate.'}))
 else:left.append(r)
(ROOT/'hrtf-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode(),mtime=0));(ROOT/'game-after-hrtf-occurrences.json').write_text(json.dumps(left,separators=(',',':'))+'\n');print(json.dumps({'metadata':meta,'typed_candidates':len(done),'remaining':len(left)}))
