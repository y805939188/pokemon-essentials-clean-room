"""Integrate seventy manually authored finite dispositions; no domain PASS inference."""
import collections
import csv
import datetime
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
START = datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(raw): return hashlib.sha256(raw).hexdigest()
def dump(path, value): path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
manual_path = BASE / "sourcefact-70-specific-receptions.manual.tsv"
fact_path = BASE / "sourcefact-consumer-receptions.json"
manual_raw = manual_path.read_bytes()
rows = list(csv.DictReader(manual_raw.decode().splitlines(), delimiter="\t"))
assert len(rows) == len({r["fact_id"] for r in rows}) == 70
assert all(None not in r and all(v for v in r.values()) for r in rows)
facts = json.loads(fact_path.read_text())
original_digest = digest(json.dumps([r["original_record"] for r in facts["records"]], ensure_ascii=False, sort_keys=True).encode())
old_ids = {r["fact_id"] for r in facts["records"] if r["status"] == "FULL_RECORD_READ_SOURCE_AND_CONSUMER_RECEPTION_OPEN"}
already = {r["fact_id"] for r in facts["records"] if r.get("specific_manual_reception", {}).get("manual_file") == manual_path.name}
assert {r["fact_id"] for r in rows} == old_ids | already
ledger = json.loads((BASE / "reading-ledger.json").read_text())
full = {r["path"] for r in ledger["records"] if r.get("repo") == "R" and r.get("status") == "FULL_READ"}
lookup = {r["fact_id"]: r for r in facts["records"]}
for index, row in enumerate(rows, 2):
    record = lookup[row["fact_id"]]
    assert record["record_full_fields_read"] is True
    source_paths = [source["path"] for source in record["original_record"]["sources"]]
    assert set(source_paths) <= full, (row["fact_id"], set(source_paths)-full)
    record["specific_manual_reception"] = {
        "manual_file": manual_path.name,
        "manual_file_sha256": digest(manual_raw),
        "manual_row": index,
        "actual_reviewer": "/root/kernel_atomic_reception",
        "recorded_utc": START,
        "recorded_utc_is_not_backfilled_read_time": True,
        "source_claim_disposition": row["claim_disposition"],
        "complete_source_units_and_explicit_supplements": row["exact_source_units"],
        "accepted_exact_meaning_or_audit_purpose": row["precise_accepted_meaning"],
        "actual_named_consumers_or_receipts": row["actual_consumers_received"],
        "remaining_named_scope": row["remaining_named_scope"],
        "formal_atom_navigation": row["formal_atom_navigation"],
        "source_read_credit": "Own actual complete original-source paths verified against reading ledger; provider finite receipts retain original reader. No new source FULL from this integration.",
        "legacy_manual_atom_links": "Navigation retained; broad pre-existing arrays do not establish exact semantic correspondence by themselves.",
        "execution": "NOT_EXECUTED",
        "whole_domain_received": False,
    }
    record["status"] = "SPECIFIC_SOURCE_OR_PURPOSE_DISPOSITION_RECORDED_FULL_DOMAIN_OPEN"
    record["pending_exact_consumer_records"] = row["remaining_named_scope"] + " Exact remaining lexical records are in consumer-candidate-dispositions.json; dynamic/transitive denominator not frozen."
assert original_digest == digest(json.dumps([r["original_record"] for r in facts["records"]], ensure_ascii=False, sort_keys=True).encode())
facts["specific70_manual_reception"] = {
    "path": manual_path.name, "bytes": len(manual_raw), "sha256": digest(manual_raw),
    "count": 70, "original_records_preserved_sha256_normalized": original_digest,
    "source_full_credit_added": 0, "whole_domain_approvals_added": 0,
    "specific_statuses": dict(collections.Counter(r["claim_disposition"] for r in rows)),
    "scope": "Seventy former generic OPEN facts now have individually authored positive/negative support, supplements, purposes and named remaining boundaries. This does not close all135 facts, all consumers or final semantic denominator.",
}
facts["updated_utc"] = START
dump(fact_path, facts)
outcome = {
    "utc": START, "manual_count": len(rows), "original_records_unchanged": True,
    "original135_normalized_sha256": original_digest,
    "fact_status_counts": dict(collections.Counter(r["status"] for r in facts["records"])),
    "new_source_full_credit": 0, "new_required_or_votes": 0,
    "manual_file": str(manual_path), "manual_bytes": len(manual_raw), "manual_sha256": digest(manual_raw),
}
stdout = json.dumps(outcome, ensure_ascii=False) + "\n"
end = datetime.datetime.now(datetime.timezone.utc).isoformat()
io = BASE / "io"
(io / "sourcefact-specific70-integration.stdout.txt").write_text(stdout)
(io / "sourcefact-specific70-integration.stderr.txt").write_text("")
dump(io / "sourcefact-specific70-integration.json", {
    "id": "sourcefact-specific70-integration", "started_utc": START, "ended_utc": end,
    "command": "python integrate-sourcefact-specific70.py", "underlying_exit_code": 0,
    "reads": [str(manual_path), str(BASE / "reading-ledger.json"), str(fact_path)],
    "writes": [str(fact_path)], "stdout_path": str(io / "sourcefact-specific70-integration.stdout.txt"),
    "stderr_path": str(io / "sourcefact-specific70-integration.stderr.txt"),
    "business_execution": "NOT_EXECUTED", "reading_credit": "Integration of already actually read originals and manually authored finite claims; no new read credit.",
})
print(stdout, end="")
