#!/usr/bin/env python3
"""Read-only recovery/identity tool. Rendering or checking grants no reading credit."""
import argparse
import hashlib
import json
import pathlib
import subprocess

CONTRACT = "30afe79aabc084e3baf9842cb87b90acbc5c6d0a"
ROOT = "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/receive_external_pbs_creature_backups"
READSET = ROOT + "/delegation/remaining-v1/gen8/readset.complete.json"


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def identity(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", default="/workspace/pokemon-essentials-clean-room")
    p.add_argument("--reference", default="/workspace/pokemon-essentials")
    p.add_argument("--record", help="Exact frozen record ID, e.g. P15:S0001")
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    d = json.loads(git(args.repo, "show", CONTRACT + ":" + READSET))
    records = {r["frozen"]["id"]: r for r in d["owned_records"]}
    primary = {r["id"]: r for r in d["owned_primary_files"]}
    raw = {}
    for key, obj in primary.items():
        data = git(args.reference, "show", obj["commit"] + ":" + obj["path"])
        assert identity(data) == {k: obj[k] for k in ("bytes", "sha256", "blob")}
        raw[key] = data

    def unit(r):
        f = r["frozen"]
        start, end = f["byte_offsets_half_open"]
        data = raw[f["identity_id"]][start:end]
        assert hashlib.sha256(data).hexdigest() == r["source_unit_sha256"]
        return data

    if args.check:
        fields = omissions = 0
        for r in records.values():
            unit(r)
            obj = r["complete_target_forward_object"]
            fields += len(obj["fields"])
            omissions += len(obj["omitted"])
            base = obj["base_section"]
            if base:
                assert records[base]["frozen"]["identity_id"] == "P14"
                unit(records[base])
        assert (len(records), fields, omissions) == (1237, 22953, 24088)
        print(json.dumps({"records": len(records), "fields": fields, "omissions": omissions,
                          "same_generation_base_links": 339, "identity_errors": 0,
                          "semantic_reading_credit": 0}))
    if args.record:
        r = records[args.record]
        print("CONTRACT", CONTRACT, "READSET", READSET)
        print("READING_CREDIT 0; receiver must actually read all content and check effective values")
        print(json.dumps(r, ensure_ascii=False, indent=2))
        print("BEGIN_EXACT_UTF8_UNIT", args.record)
        print(unit(r).decode("utf-8"), end="")
        print("END_EXACT_UTF8_UNIT", args.record)
        base = r["complete_target_forward_object"]["base_section"]
        if base:
            print("BEGIN_COMPLETE_SAME_GENERATION_BASE", base)
            print(json.dumps(records[base], ensure_ascii=False, indent=2))
            print(unit(records[base]).decode("utf-8"), end="")
            print("END_COMPLETE_SAME_GENERATION_BASE", base)
        f = next(f for f in d["original_target_inputs"] if f["relative_to_target_task"] == "field-contracts.json")
        contracts = json.loads(git(args.repo, "show", CONTRACT + ":" + f["parent_recovered_alias_path"]))
        ids = {v[2] for v in r["complete_target_forward_object"]["fields"]}
        ids.update(v[1] for v in r["complete_target_forward_object"]["omitted"])
        print("BEGIN_COMPLETE_FIELD_CONTRACTS")
        for obj in contracts["contracts"]:
            if obj["id"] in ids:
                print(json.dumps(obj, ensure_ascii=False, indent=2))
        print("END_COMPLETE_FIELD_CONTRACTS")
        print("A form's effective values still require applying the complete compiler contract to its base.")
    if not args.check and not args.record:
        p.error("Choose --check and/or --record; no implicit record sampling")


if __name__ == "__main__":
    main()
