import pathlib
import re
import sys

path = pathlib.Path(sys.argv[1])
pattern = re.compile(sys.argv[2])
lines = path.read_text().splitlines()
starts = [i for i, line in enumerate(lines) if re.match(r"^  def\s", line)]
for start in starts:
    if re.search(r";\s*end\s*$", lines[start]):
        end = start
    else:
        end = next(i for i in range(start + 1, len(lines)) if lines[i] == "  end")
    if any(pattern.search(line) for line in lines[start:end + 1]):
        print(str(path) + ":" + str(start + 1) + "-" + str(end + 1))
        for i in range(start, end + 1):
            print(str(i + 1) + ": " + lines[i])
