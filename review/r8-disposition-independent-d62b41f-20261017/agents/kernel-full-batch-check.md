# Kernel batch binding cross-check
Candidate `d62b41f4d620e50bb04c80a7505374bd284d8210`; formal subtree `f292698cdd4a8e725525a9be6dc34b75faaf151e`.

Checked 11 body documents / 66 feature rows and 2 catalog documents by fixed-commit JSON/Git. Batch memberships match actual target write sets. No status elevation or accepted event found.

## Non-blocking conservative binding limitation

The manifest explicitly labels these bindings `DOCUMENT_WRITE_SET_CONSERVATIVE`. They correctly retain batch calibration obligations but do not identify exact finding impact:

- `DOC-0059`: `/documents/58/upstream/required_ids` at manifest line 3577; extra IDs versus individual full-contract required write sets: `GR8-CRE-MG-NAME-CANCEL-001`. All listed feature locations in JSON inherit this set.

- `DOC-0068`: `/documents/67/upstream/required_ids` at manifest line 4073; extra IDs versus individual full-contract required write sets: `GR8-KER-002`. All listed feature locations in JSON inherit this set.

WP03 needs GR8-PBS-EGGGROUP-DOMAIN-001, while GR8-CRE-MG-NAME-CANCEL-001 is scoped to WP64 and its Creature catalog; WP10 is in KER-001 write set but outside KER-002 write set. README authorizes conservative document binding and disclaims that every required finding changes each row. These are non-blocking scope limitations, not a FAIL. On the real successor candidate, require exact changed finding/section diff calibration.

U07: no evidence requiring generic formal-target binding. Required U07 write sets only create a history qualification overlay; current generic sources do not cite it.

Actual model/effort/tier/speed/Fast are all UNVERIFIED. No Ruby/game/framework execution. Full formal-body semantic review and whole readsets were not performed by this helper; parent owns body reread.

Machine result records all 13 document mappings, feature locations, fixed source identity, and limitations.
