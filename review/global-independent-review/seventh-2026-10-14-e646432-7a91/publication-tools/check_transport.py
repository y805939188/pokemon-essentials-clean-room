"""Finite transport checks over report-local synthetic bytes; no source runs."""
import argparse
import importlib.util
import json
from pathlib import Path
import uuid

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('r7_transport', HERE / 'transport.py')
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)
fixture = HERE.parent / 'temporary' / ('transport-check-' + uuid.uuid4().hex[:8])
fixture.mkdir(parents=True)
tool.ROOT = fixture
(fixture / 'normal.txt').write_bytes('完整字节核对\n'.encode())
(fixture / 'alias.txt').write_bytes((fixture / 'normal.txt').read_bytes())
(fixture / 'binary.dat').write_bytes(bytes(range(256)) * 32)
(fixture / 'binary.dat').chmod(0o600)
(fixture / 'normal.txt').chmod(0o640)
(fixture / 'events.jsonl').write_text('\n'.join(json.dumps(e) for e in [
    {'type': 'thread.started', 'thread_id': 'synthetic-check'},
    {'type': 'item.completed', 'item': {'type': 'reasoning', 'text': 'synthetic excluded private field'}},
    {'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'synthetic readonly command', 'exit_code': 2, 'aggregated_output': 'real-output-shaped synthetic fixture'}},
]) + '\n')
original = {p.name: p.read_bytes() for p in fixture.iterdir() if p.is_file()}
original_modes = {p.name: p.stat().st_mode & 0o777 for p in fixture.iterdir() if p.is_file()}
output = fixture / 'publication-transport' / 'package'
tool.pack(argparse.Namespace(output=str(output), workers=2))
tool.verify_or_restore(argparse.Namespace(package=str(output), destination=None))
destination = fixture / 'restored'
tool.verify_or_restore(argparse.Namespace(package=str(output), destination=str(destination)))
assert (destination / 'normal.txt').read_bytes() == original['normal.txt']
assert (destination / 'alias.txt').read_bytes() == original['alias.txt']
assert (destination / 'binary.dat').read_bytes() == original['binary.dat']
assert not (destination / 'events.jsonl').exists()
assert all((fixture / k).read_bytes() == v for k, v in original.items())
assert all((fixture / k).stat().st_mode & 0o777 == mode for k, mode in original_modes.items())
assert all((destination / k).stat().st_mode & 0o777 == original_modes[k] for k in ('normal.txt', 'alias.txt', 'binary.dat'))
index = json.loads((output / 'payload-index.json').read_text())
assert index['counts']['logical_files'] == 3
assert index['counts']['unique_objects'] == 2
projection = output / index['local_only_platform_streams'][0]['public_projection_path']
events = [json.loads(s) for s in projection.read_text().splitlines()]
assert len(events) == 2 and events[1]['item']['exit_code'] == 2
assert index['local_only_platform_streams'][0]['excluded_event_counts'] == {'reasoning': 1}
for path in ['/absolute', '../escape', 'nested/../escape']:
    try:
        tool.safe_relative(path)
    except ValueError:
        pass
    else:
        raise AssertionError('unsafe path accepted')
target = output / index['compressed_objects'][0]['transport_path']
target.write_bytes(target.read_bytes() + b'tamper')
try:
    tool.verify_or_restore(argparse.Namespace(package=str(output), destination=None))
except RuntimeError as e:
    assert 'compressed identity mismatch' in str(e)
else:
    raise AssertionError('tamper was accepted')
print(json.dumps({'qualification': 'SYNTHETIC_TRANSPORT_TOOL_VALIDATION_ONLY',
                  'fixture': str(fixture), 'checks': ['exact decoded bytes', 'duplicate identity', 'private-stream projection', 'source bytes and modes unchanged', 'restored600/640modes', 'path guards', 'tamper rejection'],
                  'business_or_reference_execution': 0}, ensure_ascii=False))
