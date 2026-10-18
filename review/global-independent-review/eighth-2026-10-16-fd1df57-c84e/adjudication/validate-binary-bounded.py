"""Read inert PE/ELF bytes and validate exact bounded evidence; execute no target."""
from pathlib import Path
import datetime
import hashlib
import json
import struct
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REF = Path('/workspace/pokemon-essentials')
PRIOR = ROOT / 'tasks/binary_controller_strings_review'
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
run_id = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
OUT = ROOT / 'evidence/root-binary-counterreview' / ('run-' + run_id)
OUT.mkdir(parents=True, exist_ok=False)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

game = (REF / 'Game.exe').read_bytes()
ruby = (REF / 'x64-msvcrt-ruby310.dll').read_bytes()
units = json.loads((PRIOR / 'new-program-inventory.json').read_text())
for unit in units:
    source = game if unit['path'] == 'Game.exe' else ruby
    raw = source[unit['start']:unit['end_exclusive']]
    assert len(raw) == unit['bytes'] and sha(raw) == unit['sha256']
    assert raw == (PRIOR / unit['extracted']).read_bytes()

# ELF64 little-endian object, never linked, loaded, or executed.
obj = (PRIOR / 'brotli-dictionary.object').read_bytes()
assert obj[:6] == b'\x7fELF\x02\x01'
shoff = struct.unpack_from('<Q', obj, 40)[0]
entsize, count, names_index = struct.unpack_from('<HHH', obj, 58)
assert entsize == 64
sections = [struct.unpack_from('<IIQQQQIIQQ', obj, shoff + i * entsize) for i in range(count)]
names = sections[names_index]
names_data = obj[names[4]:names[4] + names[5]]

def cstr(raw, offset):
    end = raw.index(0, offset)
    return raw[offset:end].decode('ascii')

symbol_matches = []
for sec in sections:
    if sec[1] != 2:  # SHT_SYMTAB
        continue
    strings = sections[sec[6]]
    strings_data = obj[strings[4]:strings[4] + strings[5]]
    for pos in range(sec[4], sec[4] + sec[5], sec[9]):
        name, info, other, index, value, size = struct.unpack_from('<IBBHQQ', obj, pos)
        if cstr(strings_data, name) != 'kBrotliDictionaryData':
            continue
        target = sections[index]
        section_name = cstr(names_data, target[0])
        data = obj[target[4] + value:target[4] + value + size]
        assert section_name == '.rodata' and size == 122784
        assert data == game[12051776:12174560]
        symbol_matches.append(dict(symbol='kBrotliDictionaryData', section=section_name,
                                   value=value, bytes=size, sha256=sha(data)))
assert len(symbol_matches) == 1

# Independently decode two bounded request windows with installed GNU objdump.
pe = struct.unpack_from('<I', game, 0x3c)[0]
assert game[pe:pe + 4] == b'PE\0\0'
section_count = struct.unpack_from('<H', game, pe + 6)[0]
optional_size = struct.unpack_from('<H', game, pe + 20)[0]
optional = pe + 24
assert struct.unpack_from('<H', game, optional)[0] == 0x20b
image_base = struct.unpack_from('<Q', game, optional + 24)[0]
section_rows = []
for i in range(section_count):
    p = optional + optional_size + i * 40
    virtual_size, rva, raw_size, raw_pointer = struct.unpack_from('<IIII', game, p + 8)
    section_rows.append((rva, raw_pointer, raw_size))

def va(raw_offset):
    for rva, pointer, size in section_rows:
        if pointer <= raw_offset < pointer + size:
            return image_base + rva + raw_offset - pointer
    raise AssertionError(raw_offset)

def raw_at_rva(value):
    for rva, pointer, size in section_rows:
        if rva <= value < rva + size:
            return pointer + value - rva
    raise AssertionError(value)

export_rva = struct.unpack_from('<I', game, optional + 112)[0]
ex = struct.unpack_from('<IIHHIIIIIII', game, raw_at_rva(export_rva))
export_names = {'SDL_RWFromConstMem': 0x3a61c0,
                'SDL_GameControllerAddMappingsFromRW': 0x3a6f20,
                'SDL_JoystickUpdate': 0x3a5880, 'SDL_NumJoysticks': 0x3a5760}
received_exports = []
for i in range(ex[7]):
    name_rva = struct.unpack_from('<I', game, raw_at_rva(ex[9]) + i * 4)[0]
    name = cstr(game, raw_at_rva(name_rva))
    if name not in export_names:
        continue
    ordinal_index = struct.unpack_from('<H', game, raw_at_rva(ex[10]) + i * 2)[0]
    target = struct.unpack_from('<I', game, raw_at_rva(ex[8]) + ordinal_index * 4)[0]
    assert target == export_names[name]
    received_exports.append(dict(name=name, rva=hex(target)))
assert len(received_exports) == 4
assert struct.unpack_from('<I', game, 9774880)[0] == 442647
assert sha(game[9774912:10217559]) == '8883f85acfad455feedca7a95203e18629d5c60fc3933d7f511eebd731089cfe'

import_rva = struct.unpack_from('<I', game, optional + 120)[0]
cursor = raw_at_rva(import_rva)
received_import = []
while True:
    lookup, timestamp, chain, dll_name, first_thunk = struct.unpack_from('<IIIII', game, cursor)
    if not any((lookup, timestamp, chain, dll_name, first_thunk)):
        break
    dll = cstr(game, raw_at_rva(dll_name))
    thunk_cursor = raw_at_rva(lookup or first_thunk)
    i = 0
    while True:
        value = struct.unpack_from('<Q', game, thunk_cursor + i * 8)[0]
        if not value:
            break
        if first_thunk + i * 8 == 0xea8de0:
            assert not value >> 63
            symbol = cstr(game, raw_at_rva(value) + 2)
            assert dll == 'x64-msvcrt-ruby310.dll' and symbol == 'rb_eval_string_protect'
            received_import.append(dict(dll=dll, symbol=symbol, iat_rva='0xea8de0'))
        i += 1
    cursor += 20
assert len(received_import) == 1

operations = []
for label, left, right in [('controller', 58961, 59072), ('zlib', 535423, 535452),
                            ('numeric', 8094388, 8094433)]:
    cmd = ['objdump', '-d', '--start-address=' + hex(va(left)),
           '--stop-address=' + hex(va(right)), str(REF / 'Game.exe')]
    began = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run(cmd, capture_output=True, check=False)
    ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
    (OUT / (label + '.stdout')).write_bytes(result.stdout)
    (OUT / (label + '.stderr')).write_bytes(result.stderr)
    assert result.returncode == 0
    operations.append(dict(command=cmd, start_utc=began, end_utc=ended,
                           exit_code=result.returncode, stdout=label + '.stdout',
                           stderr=label + '.stderr', stdout_sha256=sha(result.stdout)))
    print(result.stdout.decode(), end='')

result = dict(start_utc=start, end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              execution_kind='TOOL_VALIDATION_ONLY; inert source bytes and disassembly',
              new_behavior_runs=0, target_programs_executed=0, short_units_bound=len(units),
              whole_dictionary_symbol=symbol_matches, operations=operations,
              exact_selected_exports=received_exports, exact_selected_import=received_import,
              semantic_limit='No entire native CFG, final dispatcher, codec success, device or game execution certified.',
              UPDATE_NOT_STARTED=True)
(OUT / 'validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(short_units_bound=len(units), dictionary_exact=True,
                      static_decode_processes=len(operations), new_behavior_runs=0)))
