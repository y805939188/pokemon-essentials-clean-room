"""Read exact text ranges, without importing or executing inspected files."""
from pathlib import Path
import sys

roots = {
    'R': Path('/workspace/r7-context/R7-U10-reviewer/inputs/reference'),
    'B': Path('/workspace/r7-context/R7-U10-reviewer/inputs/project'),
    'C': Path('/workspace/r7-review-input/R7-U10-r2-583330fb69935ff6b2eb32ca11ede6c23bde5ecd/candidate/candidates/R7-U10'),
    'S': Path('/workspace/r7-context/R7-U10-reviewer/supplement'),
}
for argument in sys.argv[1:]:
    root, path, first, last = argument.split('|')
    lines = (roots[root] / path).read_text().splitlines()
    first, last = int(first), min(int(last), len(lines))
    print(f'READ {root}/{path} L{first}-{last}; total {len(lines)} lines')
    for index in range(first - 1, last):
        print(f'{index + 1:5} {lines[index]}')
