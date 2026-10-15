"""Bounded identity/data audit. Does not run any reference or model code."""
import datetime
import hashlib
import json
from pathlib import Path
import struct


ROOT = Path(__file__).resolve().parent
CONTEXT = Path('/workspace/r7-context/R7-U02-author')


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def main():
    plan = json.loads(Path('/workspace/r7-bootstrap/R7-U02-author/recovery/batches/R7-U02.json').read_bytes())
    rows = []
    for row in plan['artifacts'] + plan['evidence'] + plan['fixed_read_inputs']:
        actual = identity((CONTEXT / row['local_path']).read_bytes())
        assert all(actual[k] == row[k] for k in actual)
        rows.append({'local_path': row['local_path'], **actual})
    contract = json.loads((CONTEXT / 'dispatch/delegation/contracts/R7-U02.json').read_bytes())
    raw = CONTEXT / 'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'
    bindings = []

    def walk(value):
        if isinstance(value, dict):
            if all(k in value for k in ('input_sha256', 'raw_member_byte_offsets', 'raw_member_sha256')):
                source = (raw / (value['input_sha256'] + '.raw')).read_bytes()
                start, end = value['raw_member_byte_offsets']
                member = source[start:end]
                assert len(member) == value['raw_member_bytes']
                assert hashlib.sha256(member).hexdigest() == value['raw_member_sha256']
                parsed = json.loads(source)
                for token in value['json_pointer'].split('/')[1:]:
                    token = token.replace('~1', '/').replace('~0', '~')
                    parsed = parsed[int(token)] if isinstance(parsed, list) else parsed[token]
                assert json.loads(member) == parsed
                canonical = json.dumps(parsed, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
                assert hashlib.sha256(canonical).hexdigest() == value['canonical_sha256']
                bindings.append({**value, 'byte_and_pointer_match': True})
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(contract)
    result = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'qualification': 'TOOL_VALIDATION only; not semantic acceptance or reference execution.',
              'restored_file_count': len(rows), 'restored_bytes': sum(x['bytes'] for x in rows),
              'files': rows, 'contract_member_binding_checks': bindings}
    (ROOT / 'fixed-input-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')

    executable = CONTEXT / 'inputs/reference/Game.exe'
    data = executable.read_bytes()
    pe = struct.unpack_from('<I', data, 0x3c)[0]
    sections_n = struct.unpack_from('<H', data, pe + 6)[0]
    optional = pe + 24
    optional_size = struct.unpack_from('<H', data, pe + 20)[0]
    image_base = struct.unpack_from('<Q', data, optional + 24)[0]
    sections = []
    for i in range(sections_n):
        offset = optional + optional_size + i * 40
        name = data[offset:offset + 8].split(b'\0')[0].decode()
        vsize, rva, raw_size, raw_start = struct.unpack_from('<IIII', data, offset + 8)
        sections.append({'name': name, 'rva': rva, 'vsize': vsize,
                         'raw_size': raw_size, 'raw_start': raw_start})

    def to_raw(va):
        for section in sections:
            start = image_base + section['rva']
            if start <= va < start + section['raw_size']:
                return section['raw_start'] + va - start
        raise ValueError(hex(va))

    def to_va(raw_offset):
        for section in sections:
            start = section['raw_start']
            if section['raw_size'] and start <= raw_offset < start + section['raw_size']:
                return image_base + section['rva'] + raw_offset - start
        raise ValueError(raw_offset)

    vocabularies = {}
    expected = {
        'buttons': 'a b x y back guide start leftstick rightstick leftshoulder rightshoulder dpup dpdown dpleft dpright'.split(),
        'axes': 'leftx lefty rightx righty lefttrigger righttrigger'.split()
    }
    for name, start, end in [('buttons', 11552288, 11552416), ('axes', 11552480, 11552536)]:
        names = []
        for offset in range(start, end, 8):
            va = struct.unpack_from('<Q', data, offset)[0]
            if va == 0:
                assert offset == end - 8
                continue
            raw_start = to_raw(va)
            raw_end = data.index(0, raw_start) + 1
            names.append({'name': data[raw_start:raw_end-1].decode('ascii'),
                          'pointer_bytes': [offset, offset + 8], 'name_va': hex(va),
                          'name_bytes': [raw_start, raw_end], **identity(data[raw_start:raw_end])})
        assert [x['name'] for x in names] == expected[name]
        vocabularies[name] = names
    fields = data[9797195:9797501].decode().strip().split(',')[2:]
    assert fields[0] == 'a:b0'
    pos = fields.index('misc1:b9')
    assert fields[pos + 1] == 'rightshoulder:b5'
    ranges = []
    for start, end in [(9797195, 9797501), (9797388, 9797396),
                       (11552288, 11552416), (11552480, 11552536),
                       (3873328, 3874736), (11551200, 11551232)]:
        ranges.append({'byte_range_half_open': [start, end],
                       'va_range_half_open': [hex(to_va(start)), hex(to_va(end - 1) + 1)],
                       **identity(data[start:end])})
    binary = {'qualification': 'BINARY_DATA_STATIC + TOOL_VALIDATION; no native execution, device, registry, or host claim.',
              'file': 'R:Game.exe', 'fixed_commit': '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
              **identity(data), 'ranges': ranges, 'vocabularies': vocabularies,
              'sample': {'record': 'DB-0087', 'ordinary': fields[0], 'unknown': fields[pos],
                         'next_recognized': fields[pos+1], 'actual_load': 'NOT_EXECUTED'},
              'bounded_disassembly_read': {'tool': 'objdump -d -M intel',
                  'va_half_open': ['0x1403b2630', '0x1403b2bb0'],
                  'unknown_error_request': '0x1403b278e', 'append_path': '0x1403b28f9',
                  'allocation_failure_count_reset': '0x1403b2979',
                  'outer_call': '0x1403b2a79',
                  'observation': 'Unknown name reaches error request without append. Outer loop clears field buffers and continues. Allocation failure is a different count-reset path.',
                  'raw_source_or_machine_code_published': False},
              'remaining': ['CC04 registration/host-query bridge NOT_READ',
                  'Actual device/backend NOT_EXECUTED', 'Full record semantics/76 fields in 48 records/registration priority NOT_SIGNED']}
    (ROOT / 'binary-static.json').write_text(json.dumps(binary, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'files_exact': len(rows), 'restored_bytes': result['restored_bytes'],
                      'raw_member_pointer_checks': len(bindings), 'buttons': len(vocabularies['buttons']),
                      'axes': len(vocabularies['axes']), 'sample': binary['sample'],
                      'execution_credit': 0, 'semantic_acceptance': False}, ensure_ascii=False))


if __name__ == '__main__':
    main()
