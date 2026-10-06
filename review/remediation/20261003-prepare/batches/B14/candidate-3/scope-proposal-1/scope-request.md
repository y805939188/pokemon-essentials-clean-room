# B14 candidate-3 bounded scope proposal 1

**PHASE 1 ONLY — PROPOSED, NOT APPLIED.** This package is neither an applied candidate, scope authorization, PASS nor acceptance. No formal/spec/catalog or public-registry file is changed.

The frozen B09 affected review at `93b81d1e05b16b7f5c999e472620b8cc4d9c5d02` reviewed candidate `af39efbf32549be964cb083bd49bed6d1d5c0d2a` (tree `932ffac11a2701ddb432516e7bd07aa990fd326f`). Its one local observation is **B14-AFFECTED-B09-001, P3**, a retained cross-reference residue. Accepted B09-C remains `1e6b11a47370f1c7c4659a32443fc1afda597bac`; no B14 acceptance or actual integration follows.

The proposed scope is exactly three documents:

| Proposal | Formal path | Only proposed clauses | Complete patch |
| --- | --- | --- | --- |
| D01 | `specs/overworld/wp59-world-time-weather-field-moves.md` | §3.5 cross-reference suffix, base line91 | [original patch](01-original-WP59-3.5.patch) |
| D02 | `deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md` | §3.5 cross-reference suffix, base line68; §9 local WT navigation range, base line321 | [final patch](02-final-WP59-3.5-and-navigation.patch) |
| D03 | `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` | §I heading range, base line316; append WT41–WT44 after WT40, before §J | [catalog patch](03-engine-catalog-WT41-WT44.patch) |

The two suffixes separate map-scene/outdoor tint eligibility from battle time. Ordinary new-battle time checks map-metadata Cave first, even with disabled shading or a valid explicit non-Cave combat environment; otherwise enabled shading chooses night/evening/other 2/1/0 without an outdoor gate. Disabled shading on a non-Cave map retains new-battle default0. Correct WP59 §3.6 and accepted WP39 §7.3 retain their meaning and bytes. No other path/clause is necessary.

The four proposed WT designs supply full ordinary-entry, valid data/dependency, no debug skip/override/plugin/rewrite and stable clock premises. Tint operation and creation are checked separately: indoor20:00 gives neutral tint/time2; outdoor-only changes tint eligibility; non-Cave shading=false keeps default0; metadata Cave/shading=false with explicit Grass still gives2, reversing only metadata to Grass gives0; non-Cave shading=true at17:00/12:00 gives1/0 for both outdoor states. They are static designs, all unexecuted. No pixels, background-asset success, capture probability or runtime result is claimed.

**Exact fresh original synchronization amendment is pending.** Earlier `b37533ef1cfc7808ed41d64215647a78d165ada4` permission and candidate2 amendments do not authorize D01. Coordinator disposition must bind the exact three complete patch identities, including D01 and the two listed navigation-range clauses, before any application. This is a parent scope coordination handoff, not a human-permission request. The author stops here.

[scope-manifest.json](scope-manifest.json) gives each document/clause source ID and reason, before commit/blob/SHA256/bytes, intended-after blob/SHA256/bytes, complete patch hashes, owner/downstream impact and pending decision. [source-reading-log.json](source-reading-log.json) binds fixed source/control/report objects and reading limits. [static-designs.json](static-designs.json) records the fixtures; [validation.json](validation.json) records strict in-memory patch reconstruction and byte preservation.

All505 existing combined catalog IDs, order, multiplicity and row bytes remain; four proposed additions would give509. Every section outside WT and the entire second pokemon catalog remain byte-identical. FLY normal/throwing callback, common berry timestamp and splash reset/ordinary-update repairs are protected under their original observation IDs. WP16, berry, fishing, WP61, unrelated WP59 clauses, 24-hour/four-channel values, cache clocks and old evidence bytes are preserved. C007/shared003 are contextual links, not a new root/approved extension or another repaired original finding. Current qualified controls govern; no unconditional67-berry-table duty is added.

Requested authorship is gpt-6.1-sol / xhigh / service_tier=default (Standard); effective backend settings remain **UNVERIFIED** under approved Plan A. No configuration/quota/auth probes or changes, children, other sessions or messages occur. Only own Git/text/JSON/hash/patch bookkeeping is performed. No reference/Ruby/game/compiler/converter/generator/deserializer/simulator or historical verifier execution; runtime0, proven Demo0, vectors unexecuted. U01–U10/G01–G12/AX01–AX20 and all named unread/unverified limits remain in the manifest.

B14 keeps24 contributions/19 primary repairs. Accepted B01–B09 keep9/21 batches,170 contributions/142 touched/109 primary; minimum109 satisfied, strict100 satisfied/9 pending,229 OPEN/0 CLOSED. No counts or acceptance states change. All exact candidate and later exact-actual gates remain. B14/B10 formal serialization stays; after eventual B14-C all53 B10 reads/eight writes and dependency contract must be refrozen. No stage, commit, push, index/ref write or formal application is performed.
