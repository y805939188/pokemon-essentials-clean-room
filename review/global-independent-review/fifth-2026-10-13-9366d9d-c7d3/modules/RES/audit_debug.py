"""Read existing DWARF interface metadata with a bounded system-tool invocation."""
from audit_resources import ROOT, save, sha
import collections
import re
import subprocess

def main():
    path=ROOT/'x64-msvcrt-ruby310.dll'
    result=subprocess.run(['/usr/bin/dwarfdump','--debug-info',str(path)],text=True,capture_output=True,check=True,timeout=30)
    records=[];current=None
    for line in result.stdout.splitlines():
        match=re.match(r'(0x[0-9a-f]+):\s+(DW_TAG_\w+)',line)
        if match:
            current={'offset':match[1],'tag':match[2],'attributes':{}};records.append(current)
        elif current:
            match=re.search(r'(DW_AT_\w+)\s+\((.*)',line)
            if match and match[1] in ['DW_AT_name','DW_AT_linkage_name','DW_AT_producer','DW_AT_language','DW_AT_low_pc','DW_AT_high_pc','DW_AT_type','DW_AT_external','DW_AT_declaration','DW_AT_byte_size']:
                current['attributes'][match[1]]=match[2].rstrip(')')
    units=[v for v in records if v['tag']=='DW_TAG_compile_unit']
    kinds=['DW_TAG_subprogram','DW_TAG_formal_parameter','DW_TAG_base_type','DW_TAG_typedef','DW_TAG_structure_type','DW_TAG_union_type','DW_TAG_enumeration_type']
    save('native-debug-metadata.json',{'path':path.name,'sha256':sha(path.read_bytes()),'tool':'/usr/bin/dwarfdump',
        'debug_info_exit':result.returncode,'debug_info_output_sha256':sha(result.stdout.encode()),'debug_info_stderr':result.stderr,
        'tag_counts':dict(collections.Counter(x['tag'] for x in records)),'compile_units':units,
        'readable_interface_records':[v for v in records if v['tag'] in kinds],
        'verify_status':'INTERRUPTED_NO_RESULT','verify_reason':'An optional --verify invocation did not return during continued work and was interrupted via tool stdin control-C. It is not counted as passed. --debug-info completed normally.',
        'review_extent':'All debug_info records scanned; compile-unit provenance and declaration/type/interface attributes decoded. Native function semantics and debugger location expressions not interpreted or executed.'})
    print('compile units',len(units),'tags',dict(collections.Counter(x['tag'] for x in records)))
    for row in units:print(row['attributes'].get('DW_AT_name'))

if __name__=='__main__':main()
