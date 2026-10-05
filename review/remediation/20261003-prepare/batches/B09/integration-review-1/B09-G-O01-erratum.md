# B09-G-O01 — append-only R-B09 erratum

The earlier R-B09 candidate report contains an error in my B013 narrative. This successor corrects that report for actual `dc64807c2d726171827017ec636c6a73efd8e4b5`, candidate `18873059e56314fcd48f6081d5a65a79301a52f6`. The three earlier report files remain byte-for-byte unchanged at `d6b1c1d7af3498321c779d38a8cc3edbabdefd77` and at the actual. Exact identities and locators are in [the erratum record](B09-G-O01-erratum.json).

Under the fixed fixture—default full player party A..F, A holds/restores X, B holds/restores Y, others and the catch hold nothing, and the partner **actually participates**—normal receiving boxes A at its current X, shifts player records, and leaves the old combined participant order intact. Storage retains the same creature identity. There is **one** normal-terminal player-side participant restoration traversal after receiving. Old index0 now reads shifted record Y, so **boxed A becomes Y**. Old index1 reads empty, so **live B becomes empty**. There is no later separate current-player pass to restore B to Y.

| Qualified design (not executed) | Boxed old member after restoration | Live shifted member |
| --- | --- | --- |
| Actual participating partner, A=X/B=Y, remaining/catch empty | A=Y | B=empty |
| No actual participation, including registered-only/excluded partner | A stays X | B=Y |
| Temporary loss with record X retained, no participation | A stays empty | Retained A instead restores X |
| Permanent consumption cleared A record, no participation | A stays empty | Retained A remains empty |
| Temporary/permanent old A loss with actual participation and B record Y | A can become Y | B follows old index1's shifted record |
| Middle D removed with actual participation and general old records | D=I_E | E=I_F, F=empty; earlier A/B/C unchanged |

The temporary-loss capture premise uses the qualified trainer Shadow/Snag Machine route. Wild-user Knock Off is rejected and a default partner AI attack does not prove that premise. The old positive/reverse paragraph already limited its temporary/permanent ordinary comparisons to no participation; those qualified comparisons and its E/F middle-member statement remain valid. The incorrect duplicated primary judgment and unqualified permanent-consumption row are the surfaces corrected here.

Fresh source evidence: normal party assembly `Overworld_BattleStarting155–207`; battle participant/record initialization `Battle95–168`; receiving/storage identity `CatchAndStore1–108,231–251`, `Battle_Peers1–59`, `PokemonStorage25–48,225–260`; normal-terminal order and sole restoration loop `Battle_StartAndEnd480–529`. All are at reference `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` and are bound in [the new source log](source-reading-log.json). No reference or vector was executed.

**Classification: report-only error.** Fixed qualified controls, the actual formal WP38/WP42 clauses, CP20–22/E14/CX40–42, and both WP20 §6.4 copies are correct. Current public registrations explicitly preserve the discrepancy and keep actual/parent acceptance pending. They do not turn the false report wording into an accepted formal rule. No formal-content or public acceptance-critical defect is found, so no reviewer correction to those files is required or made.

This erratum resolves O01 for this fresh R09 actual receipt. It does not change the old PASS label, edit a public O01 marker, accept the integration for parent C, substitute for B04/B05/B07/B08 actual reviews, or close canonical IDs.
