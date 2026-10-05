# B09 exact candidate freeze envelope

The review target is the exact final envelope SHA delivered by the ordinary
push and independent remote readback handoff. Its parent payload is
`d15259042aa6665b3fa75786a4d3650d702cab5c`, tree
`72c8f35f1c6a9407624a615f43995aea0f53110d`, based on accepted predecessor
`407536adb682a04161d3e9c82f153a62b1becd97` through the immutable scope checkpoint
`de11c8a712b3fbce5c1e11756919536c4739e2a5`.

[payload-manifest.json](payload-manifest.json) freezes every baseline-to-payload
changed path with before/after blob, SHA256 and byte identities, all twenty
contribution dispositions, all sixty-two input/current-refreeze bindings, the
seven final/five approved original identities, and required independent gates.
[full-predecessor-to-payload.patch](full-predecessor-to-payload.patch) is the
complete unfiltered binary Git diff, including all evidence and scope history.
It is distinct from the twelve-path normative patch.

This envelope adds exactly this README, the manifest, and that full patch. The
normative documents, qualifications, payload evidence and fixed histories do not
change after the payload commit. Review the complete payload diff together with
`git diff --binary d15259042aa6665b3fa75786a4d3650d702cab5c <FINAL_SHA>` and
`git diff --binary 407536adb682a04161d3e9c82f153a62b1becd97 <FINAL_SHA>` with no
path filter. The final Git tree and handoff receipt bind the envelope's own
identities without attempting to embed its SHA in its own contents.

The [candidate handoff](../candidate-1/README.md) names the full scope, evidence,
limits and gates. Independent R-B09 and separate affected R-B04/R-B07/R-B08
candidate/actual reviews remain required. The exact WP20 original/final reader
proposal remains unapplied and requires parent scope disposition. B14 formal
serialization remains blocked until accepted B09-C and the required refreeze.
No public registry edit, canonical closure, behavioral execution or independent
approval is asserted by this author envelope. Effective configuration remains
UNVERIFIED under approved Plan A; no quota/authentication/configuration probes.
