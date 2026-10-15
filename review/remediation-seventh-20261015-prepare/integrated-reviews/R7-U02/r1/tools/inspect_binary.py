import hashlib
import json
import struct
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
exe = Path('/workspace/r7-ir-R7-U02/original/inputs/reference/Game.exe')
data = exe.read_bytes()
assert len(data) == 14732288
assert hashlib.sha256(data).hexdigest() == '5c75e92fcbb6ec50b9f8fc61913d751a8945d6a1fc69c3017c7b8686b532bf04'
pe = struct.unpack_from('<I', data, 0x3c)[0]
assert data[pe:pe+4] == b'PE\0\0'
count = struct.unpack_from('<H', data, pe+6)[0]
optional_size = struct.unpack_from('<H', data, pe+20)[0]
imagebase = struct.unpack_from('<Q', data, pe+24+24)[0]
sections = []
for i in range(count):
    at = pe+24+optional_size+40*i
    name = data[at:at+8].rstrip(b'\0').decode()
    virtualsize, rva, rawsize, offset = struct.unpack_from('<IIII', data, at+8)
    sections.append(dict(name=name,rva=rva,rawsize=rawsize,offset=offset))

def va_to_offset(va):
    rva = va-imagebase
    for s in sections:
        if s['rva'] <= rva < s['rva']+s['rawsize']:
            return s['offset']+rva-s['rva']
    raise ValueError(hex(va))

tables = []
for offset, names in [(11552288, 'a b x y back guide start leftstick rightstick leftshoulder rightshoulder dpup dpdown dpleft dpright'.split()),
                       (11552480, 'leftx lefty rightx righty lefttrigger righttrigger'.split())]:
    result = []
    for i, expected in enumerate(names):
        pointer = struct.unpack_from('<Q',data,offset+8*i)[0]
        at = va_to_offset(pointer)
        end = data.index(b'\0',at)
        value = data[at:end].decode('ascii')
        assert value == expected
        result.append(dict(name=value,va=hex(pointer),bytes_half_open=[at,end+1],sha256=hashlib.sha256(data[at:end+1]).hexdigest()))
    assert struct.unpack_from('<Q',data,offset+8*len(names))[0] == 0
    tables.append(result)
sample = data[9797195:9797501].decode('ascii')
assert sample.index('a:b0') < sample.index('misc1:b9') < sample.index('rightshoulder:b5')
assert hashlib.sha256(data[9797388:9797396]).hexdigest() == '36aac23c3495810ef967e0baed304c87fb28245744fcf1957f391f54aa4ddd39'
out = subprocess.check_output(['objdump','-d','--start-address=0x1403b2630','--stop-address=0x1403b2bb0',str(exe)])
scratch = Path('/workspace/r7-ir-R7-U02/native-field-parser.disassembly.txt')
scratch.write_bytes(out)
result = dict(imagebase=hex(imagebase),sections=sections,tables=tables,
              sample=dict(bytes_half_open=[9797195,9797501],fields=['a:b0','misc1:b9','rightshoulder:b5'],actual_order=True),
              error_string=data[11551200:11551232].split(b'\0')[0].decode(),
              disassembly=dict(path=str(scratch),bytes=len(out),sha256=hashlib.sha256(out).hexdigest(),va_half_open=['0x1403b2630','0x1403b2bb0']),
              execution='TOOL_VALIDATION_AND_STATIC_DISASSEMBLY_ONLY; PE_NOT_EXECUTED; no bridge or all-record semantics')
(root/'binary-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(buttons=[x['name'] for x in tables[0]],axes=[x['name'] for x in tables[1]],sample_order=True,disassembly_bytes=len(out)),ensure_ascii=False))
