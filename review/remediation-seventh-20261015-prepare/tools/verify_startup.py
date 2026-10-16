"""Read-only fixed-input byte checks for the cloud R7 remediation preparation."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess

PROJECT = Path(__file__).resolve().parents[3]
ROOT = PROJECT / 'review/global-independent-review/seventh-2026-10-14-e646432-7a91'
OUT = Path(__file__).resolve().parents[1] / 'startup'
REFERENCE = Path('/workspace/r7-reference')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'


def git(*args, cwd=PROJECT):
    return subprocess.check_output(['git', '-C', str(cwd), *args])


def identity_stream(stream, size):
    sha = hashlib.sha256()
    blob = hashlib.sha1(f'blob {size}\0'.encode())
    count = 0
    for block in iter(lambda: stream.read(1024 * 1024), b''):
        count += len(block)
        sha.update(block)
        blob.update(block)
    return {'bytes': count, 'sha256': sha.hexdigest(), 'git_blob': blob.hexdigest()}


def check_working(row, base):
    with (base / row['path']).open('rb') as stream:
        actual = identity_stream(stream, row['bytes'])
    expected = {k: row[k] for k in actual}
    assert actual == expected, (row['path'], expected, actual)
    return {'path': row['path'], **actual, 'match': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='identity-v1.json')
    args = parser.parse_args()
    assert git('rev-parse', 'HEAD').decode().strip() == C2
    assert git('rev-parse', B + '^{tree}').decode().strip() == '84f79ec6e772aacbf3a464fde68cdc5a280e2950'
    assert git('rev-parse', C2 + '^{tree}').decode().strip() == '1f4375e2a51801ed62bc143c1d51f70296fa52f3'
    assert git('rev-parse', C2 + ':' + str(ROOT.relative_to(PROJECT))).decode().strip() == 'a011f74704047f11ee47c9a631914337558cb81b'
    assert git('rev-parse', 'HEAD', cwd=REFERENCE).decode().strip() == '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
    assert git('rev-parse', 'HEAD^{tree}', cwd=REFERENCE).decode().strip() == '7589c800b61ba13a13040ed0d686979b80a84fd0'
    rows = {}
    for name, base in [('source', REFERENCE), ('formal', PROJECT), ('supplements', PROJECT)]:
        records = json.loads((ROOT / f'inventory/{name}.final.json').read_bytes())
        rows[name] = [check_working(row, base) for row in records]
    historical = []
    for record in json.loads((ROOT / 'history/recovery-identity-verification.json').read_bytes()):
        declared = record['declared']
        proc = subprocess.Popen(['git', '-C', str(PROJECT), 'show', declared['commit'] + ':' + declared['path']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        actual = identity_stream(proc.stdout, declared['bytes'])
        stderr = proc.stderr.read().decode()
        code = proc.wait()
        expected = {k: declared[k] for k in actual}
        historical.append({'declared': declared, 'actual': actual, 'exit_code': code, 'stderr': stderr, 'match': code == 0 and actual == expected})
    status_before_preparation = '## work\n'  # Captured by the first tool read before any mutation.
    result = {
        'schema': 'r7.cloud-startup-identity.v1',
        'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'classification': 'TOOL_VALIDATION_IDENTITY_ONLY',
        'status': 'READY_WITH_LIMITS' if all(x['match'] for x in historical) else 'HISTORICAL_OBJECT_FETCH_REQUIRED',
        'project': str(PROJECT), 'reference': str(REFERENCE),
        'original_paths_are_provenance_only': True,
        'path_map': {
            '/Users/dingshinn/Desktop/pokemon-framework-reference': str(PROJECT),
            '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials': str(REFERENCE),
            '/private/tmp': '/tmp',
            'old_readiness_directory': 'HISTORICAL_METADATA_ONLY_NOT_ACCESSED',
        },
        'initial_status_captured': status_before_preparation,
        'preparation_branch': git('branch', '--show-current').decode().strip(),
        'fixed_B': B, 'publication_C2': C2,
        'remote_main': git('ls-remote', 'origin', 'refs/heads/main').decode().strip(),
        'delivery_tag': git('ls-remote', 'origin', 'refs/tags/delivery/sixth-round-closed-final-20261014').decode().strip(),
        'worktrees': git('worktree', 'list', '--porcelain').decode(),
        'reference_working_status': git('status', '--porcelain=v1', cwd=REFERENCE).decode(),
        'instructions': {'AGENTS.md': check_working({'path': 'AGENTS.md', 'bytes': 6328, 'sha256': '41cea9c6aa439dc70eaca2c26ce1f7967a887538c1aef25b9297c07b0437ff40', 'git_blob': '07b3655388c7405ec32aeb12e143db10a5e28c81'}, PROJECT), 'additional_applicable_skills': 'NONE_PRESENT_IN_CHECKOUT_OR_WORKSPACE_AGENTS'},
        'full_byte_checks': rows, 'historical_checks': historical,
        'counts': {k: len(v) for k, v in rows.items()} | {'historical': len(historical), 'historical_missing_or_mismatching': sum(not x['match'] for x in historical)},
        'limitations': 'L01-L14 retained. No new source semantic acceptance, model equivalence, game host, Demo, native media, real save/replay execution. Active sessions outside this environment are UNVERIFIED; this environment has one worktree and a clean starting checkout.',
        'requested_author': {'model': 'gpt-6.1-sol', 'effort': 'xhigh', 'service_tier': 'default', 'speed': 'normal; Fast forbidden'},
        'requested_reviewer': {'model': 'gpt-6.1-sol', 'effort': 'ultra', 'service_tier': 'default', 'speed': 'normal; Fast forbidden'},
        'effective_configuration': 'UNVERIFIED',
    }
    assert Path(args.output).name == args.output
    target = OUT / args.output
    with target.open('x') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(json.dumps({'status': result['status'], 'counts': result['counts'], 'missing': [x['declared'] for x in historical if not x['match']]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
