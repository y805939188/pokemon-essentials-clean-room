"""Regenerate bounded handoff locations; reject ambiguous locators."""
from pathlib import Path
import argparse, datetime, difflib, hashlib, json, re, subprocess

ROOT = Path(__file__).resolve().parents[5]
EVIDENCE = Path(__file__).resolve().parent
AUTHOR_INPUT = '4575e80d041ab0c74a42e2e36399d05791dbaa5b'
REVIEWED_CANDIDATE = 'bce1659e01ca33ecafb91464ce1ada32c0499faf'
PREFIX = EVIDENCE.parent.relative_to(ROOT).as_posix()
OLD_LOCATOR = '| 启动读取 |'
BOOT_LOCATOR = '| 启动读取 | 先检查默认主档：'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def unique_line(lines, locator):
    matches = [n for n, line in enumerate(lines, 1) if locator in line]
    if len(matches) != 1:
        raise ValueError(f'locator must match exactly once: {locator!r}: {matches}')
    return matches[0]


def normalize(issue, location):
    result = dict(location)
    if (issue == 'GR8-KER-002'
            and result['target'].endswith('/wp09-save-startup-continue.md')
            and result['locator'] == OLD_LOCATOR):
        result['locator'] = BOOT_LOCATOR
    return result


def key(issue, location):
    return issue, location['candidate'], location['target'], location['locator']


def heading_anchor(lines, line_number):
    heading = next(line.lstrip('#').strip()
                   for line in reversed(lines[:line_number]) if line.startswith('#'))
    anchor = '#' + re.sub(r'[^\w\-\s]', '', heading.lower()).replace(' ', '-')
    return heading, anchor


def generate(record, tagging):
    derived = {}
    for issue in record['records']:
        for n, location in enumerate(issue['change_locations']):
            location = normalize(issue['id'], location)
            lines = (ROOT / location['candidate']).read_text().splitlines()
            location['line'] = unique_line(lines, location['locator'])
            issue['change_locations'][n] = location
            identity = key(issue['id'], location)
            if identity in derived:
                raise ValueError(f'duplicate location identity: {identity}')
            derived[identity] = location
    seen = set()
    for n, tag in enumerate(tagging['changes']):
        tag = normalize(tag['issue'], tag)
        identity = key(tag['issue'], tag)
        location = derived[identity]
        if identity in seen:
            raise ValueError(f'duplicate tagging identity: {identity}')
        seen.add(identity)
        tag.update(location)
        lines = (ROOT / location['candidate']).read_text().splitlines()
        tag['section'], tag['anchor'] = heading_anchor(lines, tag['line'])
        tagging['changes'][n] = tag
    if seen != set(derived):
        raise ValueError('record/tagging location populations differ')
    return record, tagging


def main():
    args = argparse.ArgumentParser()
    args.add_argument('--write', action='store_true')
    write = args.parse_args().write
    paths = [EVIDENCE / 'remediation-record.json', EVIDENCE / 'tagging-handoff.json']
    current = [json.loads(path.read_text()) for path in paths]
    generated = generate(*json.loads(json.dumps(current)))
    if write:
        for path, value in zip(paths, generated):
            path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
        current = list(generated)
    assert current == list(generated), 'stored locations differ from unique generated locations'

    rows = []
    for tag in current[1]['changes']:
        location = next(location for issue in current[0]['records'] if issue['id'] == tag['issue']
                        for location in issue['change_locations'] if key(issue['id'], location) == key(tag['issue'], tag))
        data = (ROOT / tag['candidate']).read_text()
        old = git('show', AUTHOR_INPUT + ':' + tag['target']).decode()
        changed = set()
        for operation, _, _, first, last in difflib.SequenceMatcher(
                a=old.splitlines(), b=data.splitlines(), autojunk=False).get_opcodes():
            if operation != 'equal':
                changed.update(range(first + 1, last + 1))
        number = unique_line(data.splitlines(), tag['locator'])
        section, anchor = heading_anchor(data.splitlines(), number)
        assert number == location['line'] == tag['line'] and number in changed
        assert (section, anchor) == (tag['section'], tag['anchor'])
        rows.append({**tag, 'unique_match': True, 'record_matches_tagging': True,
                     'line_is_in_actual_author_diff': True, 'heading_and_anchor_match': True})
    assert len(rows) == 8
    wp09 = ROOT / next(row['candidate'] for row in rows if row['locator'] == BOOT_LOCATOR)
    try:
        unique_line(wp09.read_text().splitlines(), OLD_LOCATOR)
    except ValueError as error:
        negative_control = str(error)
    else:
        raise AssertionError('original ambiguous locator was incorrectly accepted')
    assert next(row for row in rows if row['locator'] == BOOT_LOCATOR)['line'] == 102

    mirrors = []
    for entry in json.loads((EVIDENCE / 'candidate-manifest.json').read_text())['files']:
        data = (ROOT / entry['candidate']).read_bytes()
        prior = git('show', REVIEWED_CANDIDATE + ':' + entry['candidate'])
        assert data == prior and hashlib.sha256(data).hexdigest() == entry['sha256']
        mirrors.append({'path': entry['candidate'], 'bytes': len(data), 'sha256': entry['sha256'],
                        'identical_to_reviewed_candidate': True})
    result = {'schema': 'r8-u01-location-recheck/v1',
              'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'reviewed_candidate': REVIEWED_CANDIDATE, 'author_input': AUTHOR_INPUT,
              'level': 'TOOL_VALIDATION', 'business_execution': 'NOT_EXECUTED',
              'formal_review': 'NOT_PERFORMED_BY_AUTHOR; original independent reviewer recheck pending',
              'location_count': len(rows), 'locations': rows,
              'original_ambiguous_locator_rejected': negative_control,
              'mirror_count': len(mirrors), 'mirrors': mirrors}
    if write:
        (EVIDENCE / 'location-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'locations_verified': len(rows), 'mirrors_unchanged': len(mirrors),
                      'original_ambiguous_locator_rejected': True,
                      'business_execution': 'NOT_EXECUTED', 'formal_acceptance': 'NOT_CLAIMED'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
