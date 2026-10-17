#!/usr/bin/env python3
"""Check explicit parent/child navigation in generated Markdown, without a browser."""
from pathlib import Path
import argparse
import copy
import datetime
import hashlib
import json
import re
import sys

INVENTORY = Path(__file__).resolve().parents[3]


def inspect(manifest, texts):
    rows = {}
    errors = []
    for path, text in texts.items():
        for number, line in enumerate(text.splitlines(), 1):
            match = re.match(r"\| (FR-\d{6}) / ", line)
            if match:
                fid = match.group(1)
                if fid in rows:
                    errors.append(f"duplicate view row: {fid}")
                rows[fid] = (path, number, line)
    checks = []
    active = {f['feature_id']: f for f in manifest['features']}
    for parent in manifest['features']:
        children = parent['functional_scope']['excluded_child_refs']
        if not children:
            continue
        pid = parent['feature_id']
        row = rows.get(pid)
        if not row:
            errors.append(f"missing parent row: {pid}")
            continue
        for child in children:
            expected_link = f'[{child}](#{child.lower()})'
            child_row = rows.get(child)
            anchor = f'<a id="{child.lower()}"></a>'
            if expected_link not in row[2]:
                errors.append(f"missing explicit child link: {pid} -> {child}")
            if not child_row:
                errors.append(f"missing child row: {child}")
            elif child_row[0] != row[0]:
                errors.append(f"child link crosses view without path: {pid} -> {child}")
            elif anchor not in child_row[2] or texts[row[0]].count(anchor) != 1:
                errors.append(f"missing or duplicate child anchor: {pid} -> {child}")
            if child not in active or active[child]['document_id'] != parent['document_id']:
                errors.append(f"child not active in same source document: {pid} -> {child}")
            checks.append({'parent': pid, 'child': child, 'view': row[0],
                           'parent_line': row[1], 'child_line': child_row[1] if child_row else None,
                           'link': expected_link, 'anchor': anchor})
    return errors, checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    manifest_path = INVENTORY / 'routing-manifest.json'
    manifest = json.loads(manifest_path.read_bytes())
    texts = {str(p.relative_to(INVENTORY)): p.read_text() for p in sorted((INVENTORY / 'views').glob('*.md'))}
    errors, checks = inspect(manifest, texts)
    if not checks:
        errors.append('no explicit parent/child boundary available for this regression')
    negative_cases = []
    if checks:
        first = checks[0]
        for name, token, expected in [
            ('parent omits explicit child ID link', first['link'], 'missing explicit child link'),
            ('child omits navigation anchor', first['anchor'], 'missing or duplicate child anchor'),
        ]:
            mutated = copy.copy(texts)
            mutated[first['view']] = mutated[first['view']].replace(token, '', 1)
            actual_errors, _ = inspect(manifest, mutated)
            negative_cases.append({'case': name, 'mutation': token, 'rejected': any(expected in e for e in actual_errors),
                                   'errors': actual_errors})
    result = {
        'schema_version': 'routing-view-navigation-check.v1',
        'scope': 'AUTHOR_STATIC_MARKDOWN_NAVIGATION_ONLY; no browser rendering, source semantics or independent acceptance',
        'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'manifest_sha256': hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        'view_sha256': {path: hashlib.sha256(text.encode()).hexdigest() for path, text in texts.items()},
        'parent_count': len({c['parent'] for c in checks}),
        'child_count': len({c['child'] for c in checks}),
        'edge_count': len(checks),
        'checks': checks, 'errors': errors, 'negative_cases': negative_cases,
        'all_negative_cases_rejected': len(negative_cases) == 2 and all(c['rejected'] for c in negative_cases),
    }
    result['result'] = 'PASS_STATIC_NAVIGATION' if not errors and result['all_negative_cases_rejected'] else 'FAIL'
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['checks', 'view_sha256']}, ensure_ascii=False, indent=2))
    return int(result['result'] == 'FAIL')


if __name__ == '__main__':
    sys.exit(main())
