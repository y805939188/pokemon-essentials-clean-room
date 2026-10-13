"""Read-only bounded SoundFont resource audit; no synthesis, game or framework code."""
import struct,json,hashlib,collections,pathlib,sys,math
R=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
O=pathlib.Path(__file__).resolve().parents[1]
b=(R/'soundfont.sf2').read_bytes(); chunks={}
def walk(a,z,parent=''):
 while a<z:
  typ=b[a:a+4].decode('ascii');n=struct.unpack_from('<I',b,a+4)[0];s=a+8;e=s+n
  assert e<=z,(typ,e,z)
  if typ=='LIST':walk(s+4,e,b[s:s+4].decode('ascii'))
  else:chunks[parent+'/'+typ]=(s,e)
  a=e+(n%2)
 assert a==z
assert b[:4]==b'RIFF' and b[8:12]==b'sfbk'
walk(12,len(b))
def rows(name,fmt):
 s,e=chunks['pdta/'+name];n=struct.calcsize(fmt);assert (e-s)%n==0
 return list(struct.iter_unpack(fmt,b[s:e]))
def name(v):return v.partition(b'\0')[0].decode('ascii','replace')
ph=rows('phdr','<20sHHHIII');pb=rows('pbag','<HH');pg=rows('pgen','<HH');pm=rows('pmod','<HHhHH')
ih=rows('inst','<20sH');ib=rows('ibag','<HH');ig=rows('igen','<HH');im=rows('imod','<HHhHH');sh=rows('shdr','<20sIIIIIBbHH')
# Source document sections 7/8; numeric identities/field widths are format facts.
gnames='startAddrsOffset endAddrsOffset startloopAddrsOffset endloopAddrsOffset startAddrsCoarseOffset modLfoToPitch vibLfoToPitch modEnvToPitch initialFilterFc initialFilterQ modLfoToFilterFc modEnvToFilterFc endAddrsCoarseOffset modLfoToVolume unused1 chorusEffectsSend reverbEffectsSend pan unused2 unused3 unused4 delayModLFO freqModLFO delayVibLFO freqVibLFO delayModEnv attackModEnv holdModEnv decayModEnv sustainModEnv releaseModEnv keynumToModEnvHold keynumToModEnvDecay delayVolEnv attackVolEnv holdVolEnv decayVolEnv sustainVolEnv releaseVolEnv keynumToVolEnvHold keynumToVolEnvDecay instrument reserved1 keyRange velRange startloopAddrsCoarseOffset keynum velocity initialAttenuation reserved2 endloopAddrsCoarseOffset coarseTune fineTune sampleID sampleModes reserved3 scaleTuning exclusiveClass overridingRootKey unused5 endOper'.split()
reserved={14,18,19,20,42,49,55,59,60}
issues=[]
def gen(x):
 op,raw=x;v=raw if raw<32768 else raw-65536
 return {'op':op,'field':gnames[op] if op<len(gnames) else 'unknown','value':([raw&255,raw>>8] if op in [43,44] else raw if op in [41,53,54] else v)}
def source(x):return {'raw':x,'index':x&127,'cc':bool(x&128),'negative':bool(x&256),'bipolar':bool(x&512),'curve':x>>10}
def mod(x):return {'source':source(x[0]),'destination':x[1],'amount':x[2],'amount_source':source(x[3]),'transform':x[4]}
def audit(h,bag,gens,mods,kind,indexop,targetsize):
 assert h[-1][3 if kind=='preset' else 1]==len(bag)-1
 assert bag[-1]==(len(gens)-1,len(mods)-1)
 assert all(a[0]<=z[0] and a[1]<=z[1] for a,z in zip(bag,bag[1:]))
 output=[]
 for hi,row in enumerate(h[:-1]):
  start=row[3 if kind=='preset' else 1];end=h[hi+1][3 if kind=='preset' else 1];assert start<=end
  zones=[]
  for zi in range(start,end):
   a,c=bag[zi];z,d=bag[zi+1];g=[gen(x) for x in gens[a:z]];m=[mod(x) for x in mods[c:d]];ops=[x['op'] for x in g]
   glob=not g or ops[-1]!=indexop
   if glob and zi!=start:issues.append([kind,hi,zi,'nonglobal zone missing final selector'])
   if len(ops)!=len(set(ops)):issues.append([kind,hi,zi,'duplicate generators'])
   for j,x in enumerate(g):
    op=x['op'];v=x['value']
    if op in reserved or op>60:issues.append([kind,hi,zi,'reserved generator',op])
    if op==indexop and not 0<=v<targetsize:issues.append([kind,hi,zi,'selector bounds',v])
    if op==indexop and j!=len(g)-1:issues.append([kind,hi,zi,'selector not final'])
    if op in [43,44] and not 0<=v[0]<=v[1]<=127:issues.append([kind,hi,zi,'key/velocity range bounds',v])
    if op==43 and j!=0:issues.append([kind,hi,zi,'key range ordering'])
    if op==44 and any(q not in [43] for q in ops[:j]):issues.append([kind,hi,zi,'velocity range ordering'])
   if len({(x[0],x[1],x[3]) for x in mods[c:d]})!=d-c:issues.append([kind,hi,zi,'duplicate modulators'])
   for j,x in enumerate(m):
    if x['transform']!=0:issues.append([kind,hi,zi,'nonlinear/undefined transform',x['transform']])
    for f in ['source','amount_source']:
     q=x[f];ix=q['index']
     if q['curve']>3 or (not q['cc'] and ix not in [0,2,3,10,13,14,16]) or (q['cc'] and ix in [0,6,32,38,98,99,100,101,*range(120,128)]):issues.append([kind,hi,zi,'source domain',q])
   zones.append({'bag_index':zi,'global':glob,'generator_span':[a,z],'modulator_span':[c,d],'generators':g,'modulators':m})
  obj={'index':hi,'name':name(row[0]),'zones':zones}
  if kind=='preset':obj.update(program=row[1],bank=row[2],reserved_library_genre_morphology=list(row[4:]))
  output.append(obj)
 return output
presets=audit(ph,pb,pg,pm,'preset',41,len(ih)-1);instruments=audit(ih,ib,ig,im,'instrument',53,len(sh)-1)
ss,se=chunks['sdta/smpl'];pcm=memoryview(b)[ss:se];n=(se-ss)//2
samples=[]
for ix,x in enumerate(sh[:-1]):
 title,start,end,loopstart,loopend,rate,pitch,correction,link,stype=x
 assert 0<=start<=end<=n,(ix,start,end,n)
 vals=[y[0] for y in struct.iter_unpack('<h',pcm[start*2:end*2])]
 row={'index':ix,'name':name(title),'start':start,'end':end,'loop_start':loopstart,'loop_end':loopend,'rate':rate,'original_pitch':pitch,'pitch_correction':correction,'link':link,'sample_type':stype,'sample_points':len(vals),'amplitude_min':min(vals,default=None),'amplitude_max':max(vals,default=None),'mean_square':sum(y*y for y in vals)/len(vals) if vals else None,'pcm_sha256':hashlib.sha256(pcm[start*2:end*2]).hexdigest(),'following_46_zero':end+46<=n and not any(pcm[end*2:(end+46)*2])}
 if not (start<=loopstart<=loopend<=end):issues.append(['sample',ix,'loop bounds'])
 if rate==0 or pitch in range(128,255):issues.append(['sample',ix,'rate or pitch domain'])
 if stype!=1:issues.append(['sample',ix,'sample type requires additional stereo/rom handling',stype,link])
 samples.append(row)
# Resolve the stored zone links and effective sample-address offsets; all sample points above inspected.
links=[]
for p in presets:
 for pz in p['zones']:
  if pz['global']:continue
  ii=pz['generators'][-1]['value'];ins=instruments[ii];globalvals={}
  for iz in ins['zones']:
   vals={g['op']:g['value'] for g in iz['generators']}
   if iz['global']:globalvals=vals;continue
   vals={**globalvals,**vals};si=vals[53];s=samples[si]
   addr=[s['start']+vals.get(0,0)+32768*vals.get(4,0),s['end']+vals.get(1,0)+32768*vals.get(12,0),s['loop_start']+vals.get(2,0)+32768*vals.get(45,0),s['loop_end']+vals.get(3,0)+32768*vals.get(50,0)]
   valid=0<=addr[0]<addr[1]<=n and (vals.get(54,0)&3 not in [1,3] or addr[0]<=addr[2]<addr[3]<=addr[1])
   if not valid:issues.append(['effective_sample_bounds',p['index'],ii,iz['bag_index'],addr])
   links.append({'preset':p['index'],'preset_zone':pz['bag_index'],'instrument':ii,'instrument_zone':iz['bag_index'],'sample':si,'sample_modes':vals.get(54,0),'effective_addresses':addr,'bounds_valid':valid})
usage=collections.Counter()
for kind,rs in [('preset',pg[:-1]),('instrument',ig[:-1])]:
 for op,raw in rs:usage[(kind,op)]+=1
summary={'schema_version':'gr5.resource-content.v1','path':'soundfont.sf2','source_baseline':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','source_sha256':hashlib.sha256(b).hexdigest(),'format_version':struct.unpack('<HH',b[slice(*chunks['INFO/ifil'])]),'format_source':{'title':'E-mu SoundFont 2.01 Technical Specification','url':'https://www.synthfont.com/SFSPEC21.PDF','sha256':hashlib.sha256(pathlib.Path('/tmp/pokemon-gr5-c7d3/sfspec21.pdf').read_bytes()).hexdigest(),'inspected_sections':['7.2–7.10','8.1–8.3','9.4–9.5']},'evidence_level':['TOOL_VALIDATION','SOURCE_STATIC'],'execution_status':'NOT_SYNTHESIZED_NOT_PLAYED_NOT_HOST_EXECUTED','counts':{'presets':len(presets),'instruments':len(instruments),'samples':len(samples),'preset_zones':len(pb)-1,'instrument_zones':len(ib)-1,'preset_generators':len(pg)-1,'instrument_generators':len(ig)-1,'preset_modulators':len(pm)-1,'instrument_modulators':len(im)-1,'sample_points_container':n,'resolved_preset_sample_links':len(links)},'banks':dict(collections.Counter(p['bank'] for p in presets)),'sample_rates':dict(collections.Counter(s['rate'] for s in samples)),'generator_usage':[{'level':k[0],'op':k[1],'field':gnames[k[1]] if k[1]<len(gnames) else 'unknown','count':v} for k,v in sorted(usage.items())],'issues':issues,'inspection_extent':'Every hydra row decoded with semantic field identities and cross-links; every declared sample PCM point read for amplitude/energy/bounds. Stored coefficients and selectors available; no synthesis or perceptual/audio equivalence proof.','not_claimed':['native host soundfont loader acceptance','actual audible timbre or quality','full MIDI/controller/synthesis dynamic behavior','new framework API or mandated renderer']}
(O/'soundfont-content-inspection.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
(O/'soundfont-content-ledger.json').write_text(json.dumps({'schema_version':'gr5.resource-content-ledger.v1','preset_records':presets,'instrument_records':instruments,'sample_records':samples,'preset_sample_links':links},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
