import sys, json, pathlib, re, hashlib
from read_bookkeeping import get, ACT
D = pathlib.Path(__file__).parent
MAP = json.loads((D / "completion-audit-map.json").read_text())
cache = {}

def resolve(e):
    p = e["path"]
    if p not in cache:
        text = get(ACT, p).decode()
        cache[p] = json.loads(text) if p.endswith(".json") else (
            [json.loads(x) for x in text.splitlines() if x] if p.endswith(".jsonl")
            else text.splitlines(keepends=True))
    obj = cache[p]
    parts = e["pointer"].split("/")[1:]
    i = 0
    while i < len(parts):
        key = parts[i].replace("~1", "/").replace("~0", "~")
        if key in ["@lines", "@jsonl"]:
            i += 1
            continue
        if key == "@text_line":
            obj = obj.splitlines(keepends=True)
            i += 1
            continue
        if key == "@embedded_JSON":
            obj = json.loads(obj)
            i += 1
            continue
        obj = obj[int(key)] if isinstance(obj, list) else obj[key]
        i += 1
    return obj

def additional_metadata(e, value):
    # Pure diff envelope and identity/check-table values are metadata; their complete source bindings are verified separately.
    pointer = e["pointer"]
    if any(part in pointer.split("/") for part in ["name_status", "reproduction_arguments", "unfiltered_ordered_hunks", "diff_sections", "hunk_headers"]):
        return True
    if isinstance(value, str) and value.startswith(("diff --git ", "index ", "--- a/", "+++ b/", "@@ ", "new file mode ")):
        return True
    if e["path"].endswith("current-hashes.tsv"):
        return True
    if isinstance(value, str) and re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*:[0-9a-f]{6,64}", value):
        return True
    if isinstance(value, str) and value.startswith(("Unchanged exact copy ", "Source lineage ")):
        return True
    return False

if len(sys.argv) == 1:
    selected, metadata, files = [], [], []
    for entry in MAP["semantic_units"]:
        value = resolve(entry)
        if additional_metadata(entry, value):
            metadata.append(entry["n"])
            continue
        selected.append(entry)
        if entry["path"] not in files:
            files.append(entry["path"])
    pages = []
    start, chars = 0, 0
    for j, entry in enumerate(selected):
        size = len(json.dumps(resolve(entry), ensure_ascii=False)) + len(entry["pointer"]) + 30
        if chars + size > 10000 and j > start:
            pages.append([start, j])
            start, chars = j, 0
        chars += size
    if start < len(selected):
        pages.append([start, len(selected)])
    (D / "completion-business-page-index.json").write_text(json.dumps({
        "selected_original_unit_ids": [e["n"] for e in selected],
        "mechanical_metadata_unit_ids": metadata,
        "files": files, "pages": pages,
        "rule": "Exact values/types/source pointers retained; metadata is verified mechanically and business assertions are displayed."
    }, indent=2) + "\n")
    print("business values", len(selected), "pages", len(pages), "chars",
          sum(len(str(resolve(e))) for e in selected), "metadata", len(metadata))
else:
    index = json.loads((D / "completion-business-page-index.json").read_text())
    page = int(sys.argv[1])
    first, end = index["pages"][page]
    selected = [MAP["semantic_units"][i] for i in index["selected_original_unit_ids"][first:end]]
    files = {p: i for i, p in enumerate(index["files"])}
    for path in dict.fromkeys(e["path"] for e in selected):
        print("FILE P" + str(files[path]) + " " + path.split("/B14/")[1])
    for entry in selected:
        value = resolve(entry)
        key = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        assert hashlib.sha256(key.encode()).hexdigest() == entry["value_sha256"]
        print(str(entry["n"]) + " P" + str(files[entry["path"]]) + " " + entry["pointer"] +
              " [" + entry["type"] + "] " + json.dumps(value, ensure_ascii=False))
    with (D / "completion-display-receipts.jsonl").open("a") as receipt:
        receipt.write(json.dumps({"mode": "audit_business", "page": page,
                                 "selected_ordinals": [first, end], "literal_values": len(selected),
                                 "delivery": "DISPLAYED_BOUNDED; tool truncation requires supplement"}) + "\n")
