C35 preparation is ready; no candidate freeze, staging, commit, push, or new target fetch has occurred.

Fresh preflight passed the nine fixed/reference/protected-ref checks and four extra guards. HEAD and the remote report branch are 81cc98eec7cc81706e51c8b274e9ff7042c0868b; the Git index is empty. R remains clean at 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b and its fixed tree. B8, main, delivery/seventh-round-closed-final-20261016 and the formal subtree retain their fixed identities. All current changed/tracked/untracked paths are under the report root. This is a live preflight snapshot, not a frozen C35 candidate list; root may continue writing.

Use this exact wrapper after a later authorized exact-candidate ordinary commit and successful ordinary push:

    python -B review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/publication/checkpoint-35-readback-wrapper.py EXACT_C35_COMMIT r8-ROOT_APPROVED_NAME-readback-35

The wrapper fixes the successful C34 baseline publication/r8-four-receivers-and-metadata-readback-34.json (27194524 bytes, SHA256 9c8576ad239dd37794f87530806d71b25cb2df3f1f570a87d444bc008f0a862c). Its remote-only seed is /workspace/scratch/r8-four-receivers-and-metadata-readback-34/remote.git; that seed has exactly one alternate, /workspace/scratch/checkpoint-34-flat-verified-c33/remote.git/objects. The flat backing cache has no alternates. The new C35 fresh bare cache will therefore have two alternate layers. The legacy deep C33 chain is unused. The wrapper requires a new unused name, exact pushed commit identity, and target absence in the C34 seed before fresh exact-SHA fetch.

The trusted publication/incremental-remote-readback.py remains unchanged (SHA256 c7993a3be2b3d0a4dfefd464e086a274c8bccc27f13dffa96a1647627c4d46ba). The new checkpoint-35-adapted-incremental-readback.py changes only init/tree command logging and provenance. Its exact derivation is checked by the wrapper; all original exact tree, report-only delta, new/changed blob bytes, reused baseline identity, and 116 gzip remote-container decode assertions remain. No worktree .git target is an independent source.

Dependencies and all original stdout/stderr/exit/UTC are in checkpoint-35-readback-readiness.json, checkpoint-35-preflight.json and checkpoint-35-io/. The actual verification call awaits root's explicit frozen candidate and successful ordinary push. Any readback proof is necessarily a postcommit successor and must not be described as included in that same commit.

This preparation grants zero source/FULL/semantic credit, zero new contexts, and zero votes. Business execution remains NOT_EXECUTED; UPDATE_NOT_STARTED. Actual model, effort, service tier, speed, Fast and UUID remain UNVERIFIED. Original final-current23 and original integration50 were not modified by this preparation.
