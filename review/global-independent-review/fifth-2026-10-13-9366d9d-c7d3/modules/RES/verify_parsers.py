"""Inspection-tool checks only. No reference/framework/behavior-model execution."""
from audit_resources import *
from audit_binaries import PE, CLI, compressed
import subprocess

def main():
    checks=[]
    def check(name,ok,detail=None):
        require(ok,name);checks.append({'name':name,'passed':True,'detail':detail})
    raw=(ROOT/'soundfont.sf2').read_bytes();sf=soundfont(raw)
    old=json.loads((OUT.parent/'M12/soundfont-content-ledger.json').read_text())
    for kind,ht,bt,gt,mt in [('preset','phdr','pbag','pgen','pmod'),('instrument','inst','ibag','igen','imod')]:
        rs=old[kind+'_records'];check(kind+'_header_count',len(rs)==len(sf['tables'][ht])-1)
        gen_count=mod_count=zone_count=0
        for r in rs:
            h=sf['tables'][ht][r['index']];check_value=(h['values'][0]==r['name'])
            if kind=='preset':check_value=check_value and h['values'][1:3]==[r['program'],r['bank']]
            require(check_value,'header comparison')
            for z in r['zones']:
                bz=sf['tables'][bt][z['bag_index']];require(bz['global_zone']==z['global'],'global comparison');zone_count+=1
                for g,id_ in zip(z['generators'],bz['generator_ids'],strict=True):
                    nr=sf['tables'][gt][int(id_.split(':')[1])];require((g['op'],g['value'])==(nr['op'],nr['value']),'generator comparison');gen_count+=1
                for m,id_ in zip(z['modulators'],bz['modulator_ids'],strict=True):
                    nr=sf['tables'][mt][int(id_.split(':')[1])];require(nr['values']==[m['source']['raw'],m['destination'],m['amount'],m['amount_source']['raw'],m['transform']],'mod comparison');mod_count+=1
        check(kind+'_all_zones_generators_modulators_agree',True,{'zones':zone_count,'generators':gen_count,'modulators':mod_count})
    for s in old['sample_records']:
        nr=sf['tables']['shdr'][s['index']];v=nr['values']
        require(v==[s['name'],s['start'],s['end'],s['loop_start'],s['loop_end'],s['rate'],s['original_pitch'],s['pitch_correction'],s['link'],s['sample_type']],'sample fields comparison')
        require(nr['pcm']['sha256']==s['pcm_sha256'] and nr['pcm']['min']==s['amplitude_min'] and nr['pcm']['max']==s['amplitude_max'],'PCM comparison')
    check('all_505_sample_headers_PCM_hashes_and_extrema_agree',True)
    check('all_structural_voice_links_agree',len(old['preset_sample_links'])==len(sf['voice_links']) and all(
        [o['preset'],o['preset_zone'],o['instrument'],o['instrument_zone'],o['sample']]==[int(n[k].split(':')[1]) for k in ('preset','preset_zone','instrument','instrument_zone','sample')] and o['effective_addresses']==n['effective_addresses']
        for o,n in zip(old['preset_sample_links'],sf['voice_links'],strict=True)))
    pairs=[tuple(r['values'][1:3]) for r in sf['tables']['phdr'][:-1]]
    check('preset_bank_program_unique',len(pairs)==len(set(pairs)))
    check('bank0_all_128_programs',sorted(p for p,b in pairs if b==0)==list(range(128)))
    # Mutations remain in memory. Only the safe parser processes these inputs.
    cases=[]
    def mutation(label,offset,fmt,value):
        b=bytearray(raw);struct.pack_into(fmt,b,offset,value);cases.append((label,bytes(b)))
    mutation('RIFF_size',4,'<I',len(raw))
    mutation('nested_chunk_overrun',next(x['header_offset']+4 for x in sf['chunks'] if x['path']=='sdta/smpl'),'<I',0xffffffff)
    mutation('terminal_bag_index',sf['tables']['phdr'][-1]['offset']+24,'<H',65535)
    mutation('instrument_selector_oob',next(x['offset']+2 for x in sf['tables']['pgen'] if x.get('op')==41),'<H',65535)
    mutation('sample_end_oob',sf['tables']['shdr'][0]['offset']+24,'<I',0xffffffff)
    mutation('reversed_key_interval',next(x['offset']+2 for x in sf['tables']['igen'] if x.get('op')==43),'<H',0x007f)
    cases.append(('truncated_file',raw[:-1]))
    for label,b in cases:
        try:soundfont(b)
        except ValueError as e:check('reject_'+label,True,str(e))
        else:check('reject_'+label,False)
    for b,expected in [(b'\x7f',127),(b'\x80\x80',128),(b'\xbf\xff',16383),(b'\xc0\x00\x40\x00',16384)]:
        check('compressed_integer_'+str(expected),compressed(Reader(b),0)==(expected,len(b)))
    cli=CLI(PE((ROOT/'animmaker.exe').read_bytes()));ledger=cli.ledger()
    check('CLI_all_15_bodies_decoded',len(ledger['methods'])==15 and all(x['all_instruction_bytes_decoded'] and x['branches_valid'] for x in ledger['methods']),{'bytes':sum(x['code_size'] for x in ledger['methods']),'instructions':sum(x['instruction_count'] for x in ledger['methods'])})
    check('CLI_all_nonpadding_blobs_referenced',all(x['consumers'] or x['padding'] for x in ledger['all_blob_heap_records']))
    check('CLI_entry_is_Main',cli.label(cli.header['entry_token'])=='Program::Main')
    check('CLI_known_rectangle_signature',cli.signature(cli.tables[6][0]['Signature'])['args']==['string','i4','i4','i4','i4'])
    binary=[]
    for name in ('Game.exe','animmaker.exe','extendtext.exe','x64-msvcrt-ruby310.dll','zlib1.dll'):
        pe=PE((ROOT/name).read_bytes());im=pe.imports();ex=pe.exports()
        # Existing native objdump is an independent PE-container reader, never input execution.
        result=subprocess.run(['/usr/bin/objdump','-p',str(ROOT/name)],capture_output=True,text=True,check=True)
        dlls=re.findall(r'DLL Name: (\S+)',result.stdout)
        check(name+'_import_DLLs_match_objdump',dlls==[x['dll'] for x in im])
        binary.append({'path':name,'sha256':sha(pe.b),'imports':im,'exports':ex})
    for r in binary:
        for dep in r['imports']:
            target=next((v for v in binary if v['path'].lower()==dep['dll'].lower()),None)
            if target:
                names={v['name'] for v in target['exports']}
                check(r['path']+'_local_imports_resolve_'+dep['dll'],all(v.get('name') in names for v in dep['symbols']),{'symbols':len(dep['symbols']),'qualification':'static name match only, ABI/loading not proven'})
    save('parser-validation.json',{'validation_kind':'TOOL_VALIDATION_ONLY','checks':checks,'passed':True,
        'independence':'SF2 compared all nonterminal stored fields with existing independent M12 ledger; PE DLL inventory compared with native objdump; no second CLI decoder available, all 15 methods manually inspected against ECMA layout.',
        'limits':['Not a universal SF2/PE/CLI parser','No renderer/synthesizer/IL interpreter','Negative fixtures test parser bounds only','Comparison is not reference execution']})
    print(json.dumps({'checks':len(checks),'passed':True}))

if __name__=='__main__':main()
