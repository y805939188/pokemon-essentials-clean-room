#!/usr/bin/env python3
"""Mechanical review entry list and separately indexed original stdout uses."""
import gzip
import importlib.util
import json
import pathlib
import re
import sys

sys.dont_write_bytecode = True
OUT = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("tagging_reading_build", OUT / "tagging-reading-build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


def load(name):
    path = OUT / name
    data = path.read_bytes() if path.exists() else gzip.decompress(pathlib.Path(str(path) + ".gz").read_bytes())
    return json.loads(data)


def main():
    docs = load("tagging-reading-documents.json")["documents"]
    report_tokens = {"report", "reports", "result", "results", "decision", "decisions"}
    receipt_tokens = {"qualification", "configuration", "config", "create", "creation", "created", "runtime"}
    entries, review, receipts, stdout_uses, scripts = [], [], [], [], []
    for doc in docs:
        path = doc["path"]
        role = "final_independent" if path.startswith("review/r8-r3-seven-line-independent-") else "prior_full_R3_independent" if path.startswith("review/r8-disposition-r3-independent-") else "candidate_source"
        basename_tokens = set(re.split(r"[^a-z0-9]+", pathlib.Path(path).name.lower()))
        entry = {key: doc[key] for key in ("path", "format", "stored_bytes", "stored_sha256", "decoded_bytes", "decoded_sha256", "unicode_characters", "line_count")}
        entry.update(role=role, source_artifact=build.ARTIFACT, read_complete_original="python3 " + str((OUT / "tagging-reading-read.py").relative_to(build.ROOT)) + " --document " + path + " --start 0 --chars N",
                     filename_report_result_decision_tokens=sorted(basename_tokens & report_tokens),
                     filename_qualification_config_creation_tokens=sorted(basename_tokens & receipt_tokens),
                     JSON_roots=[], actual_qualification_config_creation_pointers=[], original_stdout_pointers=[])
        if path.endswith((".json", ".json.gz", ".jsonl")):
            stored = build.raw(path)
            data = gzip.decompress(stored) if path.endswith(".gz") else stored
            text = data.decode("utf-8")
            parsed = [(name["document"], json.loads(text.splitlines()[name["jsonl_physical_line"] - 1]) if name["jsonl_physical_line"] else json.loads(text.lstrip("\ufeff"))) for name in doc["logical_documents"]]
            for name, root in parsed:
                entry["JSON_roots"].append({"document": name, "root_pointer": "", "root_type": build.typ(root),
                                             **({"ordered_top_keys": list(root)} if isinstance(root, dict) else {"root_array_length": len(root)} if isinstance(root, list) else {})})
                def scan(cur, pointer=""):
                    if isinstance(cur, dict):
                        for key, child in cur.items():
                            ptr = pointer + "/" + build.esc(key)
                            tokens = set(re.split(r"[^a-z0-9]+", key.lower()))
                            if tokens & receipt_tokens:
                                assert build.resolve(root, ptr) is child or build.resolve(root, ptr) == child
                                entry["actual_qualification_config_creation_pointers"].append({"document": name, "pointer": ptr, "exact_source_key": key, "type": build.typ(child)})
                            if "stdout" in tokens:
                                assert build.resolve(root, ptr) is child or build.resolve(root, ptr) == child
                                context_keys = ("command", "argv", "args", "cwd", "name", "label", "step", "tool", "exit_code", "returncode")
                                row = {"source_path": path, "document": name, "pointer": ptr, "exact_source_key": key,
                                       "type": build.typ(child), "classification_basis": "exact original property-name token stdout; no value-content analysis",
                                       "original_sibling_use_context_verbatim": {k: cur[k] for k in context_keys if k in cur},
                                       "complete_original_value_preserved_in_typed_pool": True}
                                if isinstance(child, str):
                                    row.update(value_unicode_characters=len(child), value_utf8_bytes=len(child.encode()), value_utf8_sha256=build.sha(child.encode()))
                                stdout_uses.append(row)
                                entry["original_stdout_pointers"].append({"document": name, "pointer": ptr, "exact_source_key": key})
                            scan(child, ptr)
                    elif isinstance(cur, list):
                        for i, child in enumerate(cur):
                            scan(child, pointer + "/" + str(i))
                scan(root)
        if role != "candidate_source" and entry["filename_report_result_decision_tokens"]:
            review.append(entry)
        if entry["actual_qualification_config_creation_pointers"] or entry["filename_qualification_config_creation_tokens"]:
            receipts.append(entry)
        if path.endswith((".py", ".py.gz", ".js")):
            scripts.append(entry)
        entries.append(entry)
    result = {"qualification": "MECHANICAL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT",
              "artifact": build.ARTIFACT, "all361_file_count": len(entries),
              "rules": {"review_entry": "Independent final/prior prefix AND exact basename token report,reports,result,results,decision,decisions.",
                        "receipt_entry": "Exact basename or recursively encountered JSON property-name token qualification,configuration,config,create,creation,created,runtime.",
                        "stdout_entry": "Exact original JSON property-name token stdout, with original path/pointer and original sibling command/argv/args/cwd/name/label/step/tool/exit_code/returncode when present.",
                        "tokens": "Lowercase then split by [^a-z0-9]+; no value-content or semantic classification."},
              "natural_text_preservation": "No source bytes or typed narrative are removed, cropped or summarized. All361 original sources remain pinned and the --document reader returns complete original decoded text by Unicode range. Every nonJSON full text is also an exact typed string; every JSON value, ordered structure and original byte/range/SHA locator remains in the lossless carriers. Stdout is separately indexed by original use, without deleting or filtering its values.",
              "all361_file_entries": entries,
              "independent_final_and_historical_report_result_decision_entries": review,
              "qualification_configuration_creation_receipt_entries": receipts,
              "original_stdout_uses_by_path_and_purpose": stdout_uses,
              "complete_script_source_entries": scripts,
              "counts": {"all_files": len(entries), "independent_report_result_decision_files": len(review),
                         "qualification_configuration_creation_files": len(receipts), "stdout_uses": len(stdout_uses), "script_files": len(scripts)},
              "semantic_reader": False, "full_reading_credit": False, "configuration_verdict": None, "semantic_verdict": None}
    print(build.encoded(build.write_json("review-entries.json", result)))
    print(build.encoded(result["counts"]))


if __name__ == "__main__":
    main()
