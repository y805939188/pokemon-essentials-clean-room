"""Fixed-input, read-only static resource audit. Standard library only.

This is an inspection tool, not a renderer, synthesizer or framework. It never
loads reference code as code. All writes are confined to this file's directory.
External format names/numbers are data-layout facts. No reference source copied.
"""
from pathlib import Path
import array
import collections
import hashlib
import json
import math
import re
import struct
import sys

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-H/subtasks/supplement-inventory/resource-check/inputs')
OUT = Path(__file__).resolve().parent
PIN = {
    'main': '8ea169fbd0f33f378b5d732fd6bea59e854e04a6',
    'formal_root': 'deliverables/final-specification-set/',
    'R_root': str(ROOT),
    'R_commit': '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
    'R_tree': '7589c800b61ba13a13040ed0d686979b80a84fd0',
    'runtime_request_verbatim': '请求 gpt-6.1-sol / reasoning_effort=ultra / service_tier=default，禁Fast。',
    'actual_runtime': 'UNVERIFIED',
    'execution': {'reference': 0, 'model': 0, 'host_or_demo': 0},
}

def sha(b):
    return hashlib.sha256(b).hexdigest()

def save(name, payload):
    if Path(name).name != name:
        raise ValueError('output must be a basename')
    (OUT / name).write_text(json.dumps({'identity': PIN, **payload}, ensure_ascii=False, indent=2) + '\n')

def require(ok, why):
    if not ok:
        raise ValueError(why)

class Reader:
    def __init__(self, b):
        self.b = b
    def span(self, start, size):
        require(0 <= start <= len(self.b) and 0 <= size <= len(self.b)-start, 'out of bounds')
        return self.b[start:start+size]
    def unpack(self, fmt, at):
        return struct.unpack(fmt, self.span(at, struct.calcsize(fmt)))

GEN_NAMES = ('startAddrsOffset endAddrsOffset startloopAddrsOffset endloopAddrsOffset '
    'startAddrsCoarseOffset modLfoToPitch vibLfoToPitch modEnvToPitch initialFilterFc '
    'initialFilterQ modLfoToFilterFc modEnvToFilterFc endAddrsCoarseOffset modLfoToVolume '
    'unused1 chorusEffectsSend reverbEffectsSend pan unused2 unused3 unused4 delayModLFO '
    'freqModLFO delayVibLFO freqVibLFO delayModEnv attackModEnv holdModEnv decayModEnv '
    'sustainModEnv releaseModEnv keynumToModEnvHold keynumToModEnvDecay delayVolEnv '
    'attackVolEnv holdVolEnv decayVolEnv sustainVolEnv releaseVolEnv keynumToVolEnvHold '
    'keynumToVolEnvDecay instrument reserved1 keyRange velRange startloopAddrsCoarseOffset '
    'keynum velocity initialAttenuation reserved2 endloopAddrsCoarseOffset coarseTune '
    'fineTune sampleID sampleModes reserved3 scaleTuning exclusiveClass overridingRootKey '
    'unused5 endOper').split()
RESERVED = {14,18,19,20,42,49,55,59,60}
INSTRUMENT_ONLY = {0,1,2,3,4,12,45,46,47,50,54,57,58}
DEFAULTS = {i:0 for i in range(59) if i not in RESERVED | {41,53}}
DEFAULTS.update({8:13500, 43:[0,127], 44:[0,127], 46:-1,47:-1,56:100,58:-1})
for _i in (21,23,25,26,27,28,30,33,34,35,36,38):
    DEFAULTS[_i] = -12000
RANGES = {i:(-12000,12000) for i in (5,6,7,10,11)}
RANGES.update({8:(1500,13500),9:(0,960),13:(-960,960),15:(0,1000),16:(0,1000),17:(-500,500),
    22:(-16000,4500),24:(-16000,4500),29:(0,1000),37:(0,1440),48:(0,1440),
    51:(-120,120),52:(-99,99),56:(0,1200),57:(0,127),46:(0,127),47:(1,127),58:(0,127)})
for _i in (21,23,25,27,33,35): RANGES[_i] = (-12000,5000)
for _i in (26,28,30,34,36,38): RANGES[_i] = (-12000,8000)
for _i in (31,32,39,40): RANGES[_i] = (-1200,1200)

def unit(op):
    if op in (0,1,2,3): return 'sample_points'
    if op in (4,12,45,50): return '32768_sample_points'
    if op in (5,6,7,10,11,52): return 'relative_cents'
    if op in (8,22,24): return 'absolute_cents'
    if op in (9,13,37,48): return 'centibels'
    if op in (15,16,17,29): return '0.1_percent'
    if op in (21,23,25,26,27,28,30,33,34,35,36,38): return 'timecents'
    if op in (31,32,39,40): return 'timecents_per_key'
    return {41:'instrument_index',43:'inclusive_key_interval',44:'inclusive_velocity_interval',
        46:'MIDI_key',47:'MIDI_velocity',51:'semitones',53:'sample_index',54:'loop_flags',
        56:'cents_per_key',57:'exclusive_group',58:'MIDI_root_key'}.get(op,'reserved')

def mod_source(raw):
    ix,cc=raw & 127,bool(raw & 128)
    names={0:'constant_one',2:'note_on_velocity',3:'note_key',10:'poly_pressure',13:'channel_pressure',14:'pitch_wheel',16:'pitch_wheel_sensitivity'}
    return {'raw':raw,'index':ix,'cc':cc,'source':f'MIDI_CC_{ix}' if cc else names.get(ix,'reserved'),
        'direction':'decreasing' if raw & 256 else 'increasing',
        'polarity':'bipolar' if raw & 512 else 'unipolar',
        'curve':{0:'linear',1:'concave',2:'convex',3:'switch'}.get(raw >> 10,'reserved')}

# Format-defined defaults, explicitly NOT rows discovered in R.
# SF2.01 section 8.4.2 is internally inconsistent: printed 0x502 versus
# type=3,D=1,CC=0,index=2 (0x0d02). This projection uses the bitfield description
# conditionally; alternatives below prevent treating this as known host policy.
DEFAULT_MODS = [(0x0502,48,960,0,0),(0x0102,8,-2400,0x0d02,0),
    (13,6,50,0,0),(0x81,6,50,0,0),(0x0587,48,960,0,0),(0x028a,17,1000,0,0),
    (0x058b,48,960,0,0),(0xdb,16,200,0,0),(0xdd,15,200,0,0),(0x020e,'initial_pitch_cents',12700,16,0)]

def soundfont(data):
    rd=Reader(data); require(rd.span(0,4)==b'RIFF' and rd.span(8,4)==b'sfbk','not SF2')
    require(rd.unpack('<I',4)[0]+8==len(data),'RIFF size mismatch')
    chunks=[]; bypath={}
    def walk(a,z,parent,depth):
        require(depth<=3,'excessive nesting')
        while a<z:
            require(z-a>=8,'partial chunk')
            cid=rd.span(a,4).decode('ascii'); n=rd.unpack('<I',a+4)[0]; s=a+8; e=s+n
            require(e<=z and e+(n&1)<=z,'chunk overrun')
            path=parent+'/'+cid; row={'path':path,'header_offset':a,'payload_offset':s,'size':n,'padding':n&1}
            chunks.append(row)
            if cid=='LIST':
                require(n>=4,'short LIST'); kind=rd.span(s,4).decode('ascii'); row['list_type']=kind
                walk(s+4,e,kind,depth+1)
            else:
                require(path not in bypath,'duplicate chunk'); bypath[path]=(s,n)
            a=e+(n&1)
        require(a==z,'chunk alignment')
    walk(12,len(data),'',0)
    require([x.get('list_type') for x in chunks if x['path']=='/LIST']==['INFO','sdta','pdta'],'LIST order')
    require([x['path'] for x in chunks if x['path'].startswith('pdta/')]==['pdta/'+n for n in ('phdr','pbag','pmod','pgen','inst','ibag','imod','igen','shdr')],'hydra order')
    formats={'phdr':'20sHHHIII','pbag':'HH','pmod':'HHhHH','pgen':'HH','inst':'20sH','ibag':'HH','imod':'HHhHH','igen':'HH','shdr':'20sIIIIIBbHH'}
    tables={}; observations=[]
    def note(kind,**kwargs): observations.append({'kind':kind,**kwargs})
    for table,fmt in formats.items():
        a,n=bypath['pdta/'+table]; width=struct.calcsize('<'+fmt)
        require(n%width==0 and n>=width,'table width/count')
        tables[table]=[]
        for ix,vals in enumerate(struct.iter_unpack('<'+fmt,rd.span(a,n))):
            values=[v.split(b'\0')[0].decode('ascii','replace') if isinstance(v,bytes) else v for v in vals]
            r={'id':f'{table}:{ix}','index':ix,'offset':a+ix*width,'values':values,'consumers':[], 'terminal':(ix+1)*width==n}
            if isinstance(vals[0],bytes):
                rawname=vals[0]; r['name_padding_zero']=b'\0' not in rawname or not any(rawname[rawname.index(0):])
                if not r['name_padding_zero']: note('nonzero_name_padding',record=r['id'])
            if table in ('pgen','igen'):
                op,raw=vals; value=[raw&255,raw>>8] if op in (43,44) else raw if op in (41,53,54,57) else struct.unpack('<h',struct.pack('<H',raw))[0]
                r.update(op=op,field=GEN_NAMES[op] if op<len(GEN_NAMES) else 'unknown',value=value,unit=unit(op))
                if not r['terminal']:
                    if op in RESERVED or op>=len(GEN_NAMES): note('reserved_generator',record=r['id'])
                    if op in RANGES and not RANGES[op][0]<=value<=RANGES[op][1]:
                        # The immediate-zero-time sentinel is allowed for applicable envelope stages.
                        if not (value==-32768 and unit(op)=='timecents'):
                            note('nominal_parameter_range',record=r['id'],field=r['field'],value=value,nominal=RANGES[op])
                    if table=='pgen' and op in INSTRUMENT_ONLY|{53}:note('illegal_preset_generator',record=r['id'])
                    if table=='igen' and op==41:note('illegal_instrument_generator',record=r['id'])
            if table in ('pmod','imod'):
                src,dst,amount,amt_src,transform=vals
                r.update(source=mod_source(src),destination=GEN_NAMES[dst] if dst<len(GEN_NAMES) else 'unknown',amount=amount,amount_source=mod_source(amt_src),transform=transform)
                if not r['terminal']:
                    for v in (r['source'],r['amount_source']):
                        if v['source']=='reserved' or v['curve']=='reserved':note('reserved_mod_source',record=r['id'])
                    if transform!=0 or dst in RESERVED|{41,43,44,46,47,53,54,56,57,58} or dst>=60:note('invalid_mod_destination_or_transform',record=r['id'])
            tables[table].append(r)
    # Explicit terminal rows retained; no terminal treated as a playable record.
    for h,expected in [('phdr','EOP'),('inst','EOI'),('shdr','EOS')]:
        if tables[h][-1]['values'][0]!=expected:note('terminal_name',table=h,value=tables[h][-1]['values'][0])
    for t in ('pmod','imod','pgen','igen'):
        if any(tables[t][-1]['values']):note('nonzero_ignored_terminal',table=t,values=tables[t][-1]['values'])
    zones={}; headers={}
    for h,b,g,m,sel,target,idxfield in [('phdr','pbag','pgen','pmod',41,'inst',3),('inst','ibag','igen','imod',53,'shdr',1)]:
        hr,br,gr,mr=(tables[x] for x in (h,b,g,m))
        require(hr[0]['values'][idxfield]==0 and br[0]['values']==[0,0],'unowned leading records')
        require(hr[-1]['values'][idxfield]==len(br)-1,'header terminal index')
        require(br[-1]['values']==[len(gr)-1,len(mr)-1],'bag terminal index')
        require(all(x['values'][idxfield]<=y['values'][idxfield] for x,y in zip(hr,hr[1:])),'header monotonicity')
        require(all(all(i<=j for i,j in zip(x['values'],y['values'])) for x,y in zip(br,br[1:])),'bag monotonicity')
        headers[h]=[]
        for x,y in zip(hr,hr[1:]):
            owned=[]; start,end=x['values'][idxfield],y['values'][idxfield]
            require(start<end,'empty owner')
            for bi in range(start,end):
                row=br[bi]; ga,ma=row['values']; gz,mz=br[bi+1]['values']; gs=gr[ga:gz]; ms=mr[ma:mz]
                ops=[v['op'] for v in gs]; glob=sel not in ops
                require(not glob or bi==start,'global zone must be first')
                require(glob or ops[-1]==sel,'selector final')
                require(len(ops)==len(set(ops)),'duplicate op')
                for j,op in enumerate(ops):
                    require(op!=43 or j==0,'key order')
                    require(op!=44 or all(v==43 for v in ops[:j]),'velocity order')
                for grr in gs:
                    grr['consumers'].append(row['id'])
                    if grr['op'] in (43,44):require(0<=grr['value'][0]<=grr['value'][1]<=127,'range')
                for mrr in ms:mrr['consumers'].append(row['id'])
                require(len({tuple(v['values'][i] for i in (0,1,3)) for v in ms})==len(ms),'duplicate modulators')
                row['consumers'].append(x['id']); row.update(global_zone=glob,generator_ids=[v['id'] for v in gs],modulator_ids=[v['id'] for v in ms])
                if not glob:
                    ti=gs[-1]['value'];require(0<=ti<len(tables[target])-1,'target index')
                    row['target']=f'{target}:{ti}';tables[target][ti]['consumers'].append(row['id'])
                zones[row['id']]=row;owned.append(row['id'])
            x['zones']=owned;headers[h].append(x)
    a,n=bypath['sdta/smpl'];require(n%2==0,'odd PCM bytes');pcm=array.array('h',rd.span(a,n))
    if sys.byteorder!='little':pcm.byteswap()
    total=len(pcm)
    def pcm_summary(lo,hi):
        vals=pcm[lo:hi]
        return {'points':len(vals),'sha256':sha(rd.span(a+2*lo,2*(hi-lo))),
            'min':min(vals,default=None),'max':max(vals,default=None),
            'sum':sum(vals),'sum_of_squares':sum(v*v for v in vals),
            'zero_points':vals.count(0),'clipped_extreme_points':vals.count(-32768)+vals.count(32767)}
    for r in tables['shdr'][:-1]:
        nm,s,e,ls,le,rate,pitch,corr,link,typ=r['values'];require(0<=s<e<=total,'sample bounds')
        require(s<=ls<le<=e,'sample loop bounds')
        require(typ==1,'this fixed audit expects mono samples; do not silently skip stereo/ROM')
        require(400<=rate<=50000 and (pitch<=127 or pitch==255),'sample pitch/rate')
        r.update(pcm=pcm_summary(s,e),bounds={'start':s,'end_exclusive':e,'loop_start':ls,'loop_end_exclusive':le},rate_hz=rate,
            root_key=pitch,pitch_correction_cents=corr,link_semantics='ignored_for_mono',sample_type='mono',
            duration_at_original_rate_seconds=(e-s)/rate,
            portability={'min_48_points':e-s>=48,'loop_min_32_points':le-ls>=32,'loop_pre_8':ls-s>=8,'loop_post_8':e-le>=8,
                'matching_8_point_loop_neighborhood':pcm[ls-4:ls+4]==pcm[le-4:le+4],
                'following_46_zero':e+46<=total and all(v==0 for v in pcm[e:e+46]),
                'following_46_available':min(46,total-e),'following_46_nonzero':sum(v!=0 for v in pcm[e:e+46])})
    require('sdta/sm24' not in bypath,'unexpected 24-bit extension')
    def zone_values(z):return {tables[z['id'][:1]+'gen'][int(k.split(':')[1])]['op']:tables[z['id'][:1]+'gen'][int(k.split(':')[1])]['value'] for k in z['generator_ids']}
    def effective_zone(h,z):
        first=zones[h['zones'][0]]; inherited=zone_values(first) if first['global_zone'] else {}
        return {**inherited,**zone_values(z)}
    def mod_identity(v):return tuple(v[i] for i in (0,1,3))
    defaults=[{'id':'format_default:'+str(i),'values':list(x),'source':mod_source(x[0]),'destination':GEN_NAMES[x[1]] if isinstance(x[1],int) else x[1],'amount_source':mod_source(x[3])} for i,x in enumerate(DEFAULT_MODS)]
    links=[]
    for p in headers['phdr']:
        for zid in p['zones']:
            pz=zones[zid]
            if pz['global_zone']:continue
            pv=effective_zone(p,pz);i=tables['inst'][pv[41]]
            for izid in i['zones']:
                iz=zones[izid]
                if iz['global_zone']:continue
                iv=effective_zone(i,iz); s=tables['shdr'][iv[53]];values={**DEFAULTS,**iv}
                for op,v in pv.items():
                    if op in (41,43,44):continue
                    if op not in INSTRUMENT_ONLY:values[op]=values.get(op,0)+v
                kr=[max(pv.get(43,[0,127])[0],iv.get(43,[0,127])[0]),min(pv.get(43,[0,127])[1],iv.get(43,[0,127])[1])]
                vr=[max(pv.get(44,[0,127])[0],iv.get(44,[0,127])[0]),min(pv.get(44,[0,127])[1],iv.get(44,[0,127])[1])]
                values[43]=kr;values[44]=vr
                _,ss,se,ls,le,*_=s['values']
                addr=[ss+values[0]+32768*values[4],se+values[1]+32768*values[12],ls+values[2]+32768*values[45],le+values[3]+32768*values[50]]
                looping=values[54]&3
                require(looping in (0,1,3) and values[54] in (0,1,3),'sample mode reserved bits')
                require(0<=addr[0]<addr[1]<=total,'effective sample bounds')
                require(not looping or addr[0]<=addr[2]<addr[3]<=addr[1],'effective loop bounds')
                mods={mod_identity(x['values']):{'base':x['id'],'values':x['values']} for x in defaults}
                # Local zone overrides global by identity; instrument overrides format default.
                for zz in ([zones[i['zones'][0]]] if zones[i['zones'][0]]['global_zone'] else [])+[iz]:
                    for mid in zz['modulator_ids']:
                        mr=tables['imod'][int(mid.split(':')[1])];mods[mod_identity(mr['values'])]={'base':mid,'values':mr['values']}
                pmods={}
                for zz in ([zones[p['zones'][0]]] if zones[p['zones'][0]]['global_zone'] else [])+[pz]:
                    for mid in zz['modulator_ids']:
                        mr=tables['pmod'][int(mid.split(':')[1])];pmods[mod_identity(mr['values'])]=mr
                for ident,mr in pmods.items():
                    if ident in mods:
                        mods[ident]['preset_addition']=mr['id']; vv=list(mods[ident]['values']);vv[2]+=mr['values'][2];mods[ident]['values']=vv
                    else:mods[ident]={'base':mr['id'],'values':mr['values']}
                effective={GEN_NAMES[k]:v for k,v in sorted(values.items()) if k!=53}
                root=values[58] if values[58]>=0 else s['root_key'] if s['root_key']<=127 else 60
                row={'id':f'voice:{len(links)}','preset':p['id'],'bank':p['values'][2],'program':p['values'][1],
                    'preset_zone':zid,'instrument':i['id'],'instrument_zone':izid,'sample':s['id'],
                    'key_range':kr,'velocity_range':vr,'nonempty_selection':kr[0]<=kr[1] and vr[0]<=vr[1],
                    'effective_generators_before_modulation_or_host_clamping':effective,
                    'effective_modulators':list(mods.values()),
                    'modulator_projection_basis':'conditional_SF201_bitfield_description; not_verified_host_defaults',
                    'default_filter_alternatives':{
                        'SF201_bitfields':{'amount_source':3330,'resolved_base':mods[(258,8,3330)]['base'],'resolved_amount':mods[(258,8,3330)]['values'][2]},
                        'SF201_printed_hex':{'amount_source':1282,'default_amount':-2400,'stored_imod_with_3330_is_distinct':True},
                        'SF204_printed_default':{'amount_source':0,'default_amount':-2400,'stored_imod_with_3330_is_distinct':True}},
                    'effective_addresses':addr,
                    'root_key':root,'sample_rate_hz':s['rate_hz'],'pitch_correction_cents':s['pitch_correction_cents'],
                    'loop_behavior':{0:'one_shot',1:'loops_through_release',3:'loops_until_release_then_tail'}[looping],
                    'consumer_contract':'RES-AUDIO-SF2','audible_result':'UNKNOWN_NOT_SYNTHESIZED'}
                links.append(row);s.setdefault('resolved_voice_consumers',[]).append(row['id'])
    # Every sample point, including gaps/guards, receives statistics without saving media.
    merged=[]
    for s,e in sorted((r['values'][1],r['values'][2]) for r in tables['shdr'][:-1]):
        if merged and s<=merged[-1][1]:merged[-1][1]=max(merged[-1][1],e)
        else:merged.append([s,e])
    gaps=[];cursor=0
    for s,e in merged:
        if s>cursor:gaps.append({'start':cursor,'end_exclusive':s,**pcm_summary(cursor,s)})
        cursor=e
    if cursor<total:gaps.append({'start':cursor,'end_exclusive':total,**pcm_summary(cursor,total)})
    info={}
    for k,(s,n) in bypath.items():
        if k.startswith('INFO/'):
            info[k]=list(rd.unpack('<HH',s)) if k.endswith(('/ifil','/iver')) else rd.span(s,n).rstrip(b'\0').decode('latin1')
    for p in tables['phdr'][:-1]:p['consumers']=['mkxp.json:66 via MIDI bank/program selection; actual MIDI files absent']
    for t,rs in tables.items():
        for r in rs:
            if r['terminal']:r['consumers']=['structural_sentinel_only']
            elif not r['consumers']:note('unreferenced_record',record=r['id'])
    summary={'sha256':sha(data),'bytes':len(data),'record_counts_including_terminals':{k:len(v) for k,v in tables.items()},
        'voice_links':len(links),'empty_voice_selections':sum(not x['nonempty_selection'] for x in links),
        'sample_points':total,'banks':dict(collections.Counter(x['values'][2] for x in tables['phdr'][:-1])),
        'sample_rates':dict(collections.Counter(x['rate_hz'] for x in tables['shdr'][:-1])),
        'loop_modes':dict(collections.Counter(x['loop_behavior'] for x in links)),
        'sample_portability_failures':{k:sum(not x['portability'][k] for x in tables['shdr'][:-1]) for k in ('min_48_points','loop_min_32_points','loop_pre_8','loop_post_8','matching_8_point_loop_neighborhood','following_46_zero')},
        'observation_counts':dict(collections.Counter(x['kind'] for x in observations)),
        'all_raw_table_records_owned_or_explicitly_unreferenced':True,'unscanned_sample_bytes':0,
        'format_conformance_claim':False,'host_acceptance':'UNKNOWN'}
    return {'summary':summary,'chunks':chunks,'info':info,'tables':tables,'observations':observations,
        'default_filter_document_ambiguity':{'SF201_url':'https://www.synthfont.com/SFSPEC21.PDF','SF204_url':'https://www.synthfont.com/sfspec24.pdf','section':'8.4.2',
            'SF201_printed_amount_source':1282,'SF201_bitfield_description_encoded':3330,'SF204_printed_amount_source':0,
            'review':'File rows are unambiguous; external format editions/text disagree. Effective-modulator list is conditional on SF201 bitfields; per-voice alternatives retain uncertainty. No external synth implementation or host run selected a policy.'},
        'format_defaults_not_R_records':defaults,'generator_defaults_not_R_records':{GEN_NAMES[k]:v for k,v in DEFAULTS.items()},
        'voice_links':links,'pcm_all_points':pcm_summary(0,total),'pcm_gaps':gaps}

def main():
    result=soundfont((ROOT/'soundfont.sf2').read_bytes())
    save('soundfont-full-audit.json',result)
    print(json.dumps(result['summary'],ensure_ascii=False))

if __name__=='__main__': main()
