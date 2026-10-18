#!/usr/bin/env python3
"""Static JSON logical-object reader, with exact original identity and IO capture."""
from pathlib import Path
import sys, json, hashlib, datetime
base = Path(__file__).resolve().parent
tag, filename, *selectors = sys.argv[1:]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
stdout = stderr = ""
code = 0
identity = None
try:
    path = Path(filename)
    raw = path.read_bytes()
    data = json.loads(raw)
    identity = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
    selected = []
    for selector in selectors:
        value = data
        for component in selector.strip('/').split('/') if selector.strip('/') else []:
            component = component.replace('~1', '/').replace('~0', '~')
            value = value[int(component)] if isinstance(value, list) else value[component]
        selected.append({"selector": selector, "complete_selected_object": value})
    stdout = json.dumps({"path": str(path), "identity": identity, "selected": selected}, ensure_ascii=False, indent=2) + '\n'
except Exception as exc:
    stderr = f'{type(exc).__name__}: {exc}\n'
    code = 1
end = datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {"operation": "STATIC_JSON_OBJECT_READ_NOT_BUSINESS_EXECUTION", "argv": sys.argv,
          "actual_reader": "/root/com_ai", "actual_new_contexts": 0,
          "start_utc": start, "end_utc": end, "identity": identity,
          "stdout": stdout, "stderr": stderr, "exit_code": code,
          "semantic_credit": "ONLY_AFTER_ACTUAL_COMPLETE_SELECTED_OBJECT_READING"}
(base / 'io' / (tag + '.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
sys.stdout.write(stdout)
sys.stderr.write(stderr)
sys.exit(code)
