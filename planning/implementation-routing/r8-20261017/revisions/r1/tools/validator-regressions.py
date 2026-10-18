#!/usr/bin/env python3
"""Author regression checks for reported static holes; no game/reference execution."""
from pathlib import Path
import argparse
import copy
import datetime
import importlib.util
import json
import subprocess
import sys

sys.dont_write_bytecode = True
INVENTORY = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("routing_r1_static_checks", INVENTORY / "routing.py")
routing = importlib.util.module_from_spec(spec)
spec.loader.exec_module(routing)


def load_inputs(fixture):
    if not fixture:
        return routing.read_json(INVENTORY / "routing-manifest.json"), routing.read_json(INVENTORY / "section-coverage.json")
    # Shape-only migration in memory isolates the validator from unfinished author edits.
    prefix = str(INVENTORY.relative_to(routing.ROOT)) + "/"
    def old(name):
        return json.loads(routing.blob(routing.INITIAL_CANDIDATE, prefix + name))
    m, c = old("routing-manifest.json"), old("section-coverage.json")
    m.update(schema_version="implementation-routing.v2", retired_features=[], metadata_records=[])
    for d in m["documents"]:
        d["retired_feature_ids"] = []
    for f in m["features"]:
        f["functional_scope"] = {"line_ranges": copy.deepcopy(f["source"]["line_ranges"]),
            "excluded_child_refs": [], "reason": "TOOL_FIXTURE_ONLY; not a revised routing proposal"}
        f["future_plan"]["responsibilities"] = [{"party": p, "scope": "TOOL_FIXTURE_ONLY"} for p in f["future_plan"]["partners"]]
        f["dependencies"]["direct_refs"] = []
        f['current_applicability']['locator'] = {k:copy.deepcopy(f['source'][k]) for k in ['heading','anchor','heading_level','heading_sha256','line_ranges','unit_sha256','file_sha256','file_git_blob']}
    for s in c["sections"]:
        s.update(metadata_refs=[], retired_feature_refs=[])
    return m, c


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--legacy-fixture", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    manifest, coverage = load_inputs(args.legacy_fixture)
    accepted_registry = {'events': []} if args.legacy_fixture else None
    baseline_errors = routing.errors(manifest, coverage, accepted_registry)
    if baseline_errors:
        print(json.dumps({"result": "INVALID_BASELINE", "errors": baseline_errors}, ensure_ascii=False))
        return 1
    cases = []
    def check(name, mutate, expected):
        m, c = copy.deepcopy(manifest), copy.deepcopy(coverage)
        mutate(m, c)
        errors = routing.errors(m, c, accepted_registry)
        passed = bool(errors) and any(expected in e for e in errors)
        cases.append({"case": name, "required_error_contains": expected, "rejected": bool(errors),
            "expected_check_passed": passed, "errors": errors})
    check("missing feature name", lambda m,c: m["features"][0].pop("name"), "schema:")
    check("invalid feature current commit/path", lambda m,c: m["features"][0]["current_applicability"].update(snapshot_commit="0"*40, document="missing.md"), "current feature snapshot/path")
    check("false current locator unit hash", lambda m,c: m['features'][0]['current_applicability']['locator'].update(unit_sha256='0'*64), 'current feature locator identity')
    check("false current locator anchor", lambda m,c: m['features'][0]['current_applicability']['locator'].update(anchor='missing'), 'current feature locator heading')
    check("false current locator ranges", lambda m,c: m['features'][0]['current_applicability']['locator'].update(line_ranges=[[999999,999999]]), 'current feature locator range')
    check("false source formal tree", lambda m,c: m["source_baseline"].update(formal_tree="0"*40), "formal tree mismatch")
    check("false current formal tree", lambda m,c: m["current_snapshot"].update(formal_tree="0"*40), "formal tree mismatch")
    check("false source file Git blob", lambda m,c: m["features"][0]["source"].update(file_git_blob="0"*40), "immutable source")
    check("false document bytes", lambda m,c: m["documents"][0]["source"].update(bytes=1), "complete Git identity")
    check("false document source blob", lambda m,c: m["documents"][0]["source"].update(git_blob="0"*40), "complete Git identity")
    check("false current document bytes", lambda m,c: m["documents"][0]["current_applicability"]["identity"].update(bytes=1), "complete identity")
    check("false current document blob", lambda m,c: m["documents"][0]["current_applicability"]["identity"].update(git_blob="0"*40), "complete identity")
    check("false current identity path", lambda m,c: m["documents"][0]["current_applicability"]["identity"].update(path="missing.md"), "identity path mismatch")
    check("false source baseline index identity", lambda m,c: m["source_baseline"]["index"].update(bytes=1), "authority/identity mismatch")
    check("stale heading title/level/end", lambda m,c: c["sections"][60].update(title="wrong",level=6,line_end=999999), "complete heading coverage fields")
    check("missing heading", lambda m,c: c["sections"].pop(), "heading coverage")
    check("empty collaborators", lambda m,c: m["features"][0]["future_plan"].update(partners=[]), "schema:")
    check("responsibility party differs from collaborator", lambda m,c: m["features"][0]["future_plan"].update(responsibilities=[{"party":"MZ","scope":"invalid binding"}]), "responsibilities must agree")
    check("removed known R8 binding", lambda m,c: m["features"][0]["upstream"].update(batches=[],required_ids=[]), "known conservative batch binding mismatch")
    check("invalid WP dependency", lambda m,c: m["features"][0]["dependencies"].update(wp_refs=["WP999"]), "unknown dependency WP")
    check("invented accepted event", lambda m,c: (m["features"][0]["upstream"].update(accepted_events=["invented"],status="已校准"),m["features"][0]["current_applicability"].update(status="已校准")), "accepted event")
    check("unknown direct source consumer", lambda m,c: m["features"][0]["dependencies"].update(direct_refs=[{"document":"missing.md","anchor":"missing","reason":"mutation"}]), "unresolved direct source dependency")
    check("unknown metadata link", lambda m,c: c["sections"][0].update(metadata_refs=["META-999999"]), "unresolved metadata/retired coverage reference")
    check("functional scope outside source", lambda m,c: m["features"][0]["functional_scope"].update(line_ranges=[[999999,999999]]), "invalid current functional scope")
    check("duplicate stable ID", lambda m,c: m["features"][1].update(feature_id=m["features"][0]["feature_id"]), "duplicate feature IDs")
    if manifest["retired_features"]:
        check("retired historical row changed", lambda m,c: m["retired_features"][0]["future_plan"].update(rationale="rewritten history"), "preserve complete original row")
    registry_errors = routing.errors(manifest, coverage, {"events": ["not-an-event"]})
    cases.append({"case":"malformed accepted event registry","rejected":bool(registry_errors),
        "expected_check_passed":any("malformed event" in e for e in registry_errors),"errors":registry_errors})
    result = {"scope":"AUTHOR_TOOL_VALIDATION_ONLY; not independent acceptance or routing semantic review",
        "input_mode":"in-memory legacy shape fixture" if args.legacy_fixture else "actual revised candidate files",
        "started_utc":started,"ended_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "reported_findings":["ROOT-TOOL-01","ROOT-TOOL-02"],"baseline_valid":True,
        "cases":cases,"all_checks_passed":all(c["expected_check_passed"] for c in cases),
        "manual_gates":["candidate classification and dependency semantics","authenticity/sufficiency of user scope decisions, target evidence and acceptance receipts"]}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"all_checks_passed":result["all_checks_passed"],"cases":len(cases),"failed":[c for c in cases if not c["expected_check_passed"]]},ensure_ascii=False))
    return 0 if result["all_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
