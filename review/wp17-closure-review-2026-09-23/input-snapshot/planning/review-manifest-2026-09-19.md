# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-23 WP17 回归复审修订后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md` | `5aecfd39` | `5aecfd3979c85a572d1256c04802a7263930eefbe088295e6d289ab9772e571e` | 35,698 |
| `planning/extraction-plan.md` | `c1735877` | `c173587708c9fcaaaaa1a4079bdedaa14d02405871b3fe3cd2ed6d16caeffd78` | 46,915 |
| `specs/demo/wp01-baseline-and-evidence-scope.md`（WP01 修订稿 v4） | `2a52e94e` | `2a52e94e615d0f1f45d55b0d14317b79e58bc6f988b76095e044f770ca41b407` | 16,543 |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md`（WP02 修订稿 v4） | `82b47151` | `82b471510ff563e6964697cb28e77ae816e190062dfafc9e328f44a81c2131fa` | 37,817 |
| `specs/kernel/wp02-settings-inventory-appendix.md`（WP02 附表 v2） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `specs/kernel/wp03-content-identity-and-schema.md`（WP03 修订稿 v5） | `de331460` | `de331460e013bfc07533d0f368967fe729bcf0720d98e7d990a16a0614e9c27d` | 30,708 |
| `specs/kernel/wp04-pbs-lifecycle.md`（WP04 修订稿 v4） | `b5d33db1` | `b5d33db1ac4172c216715df713bda414f7358fa69dcf5c21b5a8a0409d48da59` | 23,172 |
| `specs/kernel/wp05-events-extensions-plugins.md`（WP05 修订稿 v4） | `d65b6d14` | `d65b6d14bf95f47d59166f7bcef74984d92b243e465f8c035daa95b9521a24f7` | 18,497 |
| `specs/kernel/wp06-time-random-steps-stats.md`（WP06 修订稿 v5） | `c01140cb` | `c01140cb60d76f8f13de454a7a52f5fae544ac0fe415eaf81d877df0e24c9d7d` | 21,359 |
| `specs/kernel/wp06-stats-directory.md`（WP06 统计目录附表 v2） | `15b75cea` | `15b75cea1698c8978f4cc33380089f3c501cfec0ab8894f3991a6a6513e2d04a` | 14,954 |
| `specs/kernel/wp07-diagnostics-files-http.md`（WP07 修订稿 v4） | `2cd5408a` | `2cd5408ae9dbb1d96281057829c6bff125fdf471b2afc0e96020d105801cdbd2` | 17,398 |
| `specs/kernel/wp08-localization.md`（WP08 修订稿 v4，状态回填） | `4aa7c989` | `4aa7c989d3874e63cfc9772f0e04c1c71b4f511c022a3d632a7df6e62dc4b331` | 18,258 |
| `specs/kernel/wp09-save-startup-continue.md`（WP09 修订稿 v3） | `76450356` | `76450356b03f11abc59808e84c7c07e0f69c3f6543aaafc9b1856b3cdf2de4e6` | 18,087 |
| `specs/kernel/wp10-migration-failure-recovery.md`（WP10 修订稿 v4，状态回填+C04） | `b01a9fc7` | `b01a9fc7315bcef7fd5e9a246c147d0dcf5597f134abcc42ce33d9dc8c2df17b` | 22,733 |
| `specs/overworld/wp11-map-topology-transfer.md`（WP11 Reviewed，状态回填） | `84ca24a5` | `84ca24a5919f05a280e67b0470436cdaf5557800ced19a0fccb218fbf3f38275` | 19,944 |
| `specs/overworld/wp12-terrain-movement-vehicles.md`（WP12 Reviewed，状态回填+WP12-C01） | `8187e7de` | `8187e7deb59950301a12a6518a3c81a1e2a3aebabc347f7fa388e02364e8b280` | 32,153 |
| `specs/overworld/wp13-map-events-npc-followers.md`（WP13 Reviewed，状态回填） | `0b9bbd02` | `0b9bbd02e9b6032690967549f62d0f5024c0a8bf6ad541e0f7b94b7a09d242d8` | 28,571 |
| `specs/overworld/wp13-interpreter-command-matrix.md`（WP13 命令兼容矩阵附表 v3） | `ab69bc87` | `ab69bc87c97b805f1a2f0848a35e9b86aa8b582f8128553038f2487b85245de5` | 17,561 |
| `specs/overworld/wp13-move-route-matrix.md`（WP13 移动路线附表 v2） | `f637f1c3` | `f637f1c32db9fd59e93b0b3c81f33637f22e715dfeaaabb74f5fad6a71db12c7` | 8,315 |
| `analysis/inventory/wp02_settings_common.py` | `ba01d4d2` | `ba01d4d23f6f2eef42b123befc6809d09bfac282a7dd9f928aa6ac31427a868d` | 8,231 |
| `analysis/inventory/wp02_settings_inventory.py` | `dfa38c40` | `dfa38c407258607da467e6c609e0b75c78485dc974e85f387aa9cd12969c0ca3` | 1,491 |
| `analysis/inventory/wp02_build_appendix.py` | `7c965c9d` | `7c965c9d36a7eccb039a703312aa10a6c418fc120db769b888666c03d73c03d6` | 12,192 |
| `analysis/inventory/wp02-regen-check-2026-09-19.md` | `8ce853cc` | `8ce853cc28577ca3567407fe4b92d97e2f319835508834e5ae7cbd4151bdd05e` | 3,323 |
| `analysis/inventory/out/wp02-settings-inventory-appendix.md`（临时输出） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `review/joint-review-2026-09-19.md` | `f0e0029d` | `f0e0029db9a1e17a9c650a5a936a4ed1dd700e580e78efd305b02d020adf9494` | 12,253 |
| `review/wp01-review-2026-09-19.md` | `e044597c` | `e044597c5d3933d9376c42207da68351063806a285041785b383b877b5afe74b` | 11,708 |
| `review/wp02-review-2026-09-19.md` | `b3923043` | `b39230435fe4a6f1aaa83f68979c9c8a529cc6f176729801c2f1d3eb41e61151` | 18,146 |
| `review/wp02-recheck-2026-09-19.md` | `858adc69` | `858adc69f6d525ac7e4107d9466d02d9e8143e1342dea1ec65652662eed3981a` | 14,343 |
| `review/wp02-closure-review-2026-09-19.md` | `5f963011` | `5f9630118e9fbdda6578106b3ebb96b9db6777519650485d7569d5fb28c49d7d` | 10,820 |
| `review/wp03-review-2026-09-19/report.md` | `6f5bd583` | `6f5bd583ee53b017828f3f3060682b31cf99eb82b5f6a82c6bc74a7eadd88846` | 18,612 |
| `review/wp03-recheck-2026-09-19/report.md` | `799f7c0d` | `799f7c0dfb8fe49add0c3a43659901b55821694d91338cfb6ce70a5ec906296d` | 14,947 |
| `review/wp03-recheck-v3-2026-09-19/report.md` | `3f2d9661` | `3f2d9661cda4d3b96deef7b1bb88b0b30d3274131f8c0837352d5ae8623d3a3a` | 7,776 |
| `review/wp03-closure-review-2026-09-19/report.md` | `1544a179` | `1544a1794074681b2f0df0e0995479ba76d42998e6e0c189d7600d43d11e9167` | 7,778 |
| `review/wp03-closure-review-2026-09-19/next-batch-prompt.md` | `a8fa4858` | `a8fa4858089357ffe3a6003a1b82793879c84f654877fbdf85a00b09c97e617e` | 10,093 |
| `review/wp04-wp07-review-2026-09-19/report.md` | 见原件 | 见 `review/wp04-wp07-review-2026-09-19/` 目录 | 25,625 |
| `review/wp04-wp07-recheck-2026-09-19/report.md` | 见原件 | 见 `review/wp04-wp07-recheck-2026-09-19/` 目录 | 16,743 |
| `review/wp04-wp07-recheck-v3-2026-09-19/report.md` | `4c208ff8` | `4c208ff8713bda3ea26a857422d420f04fd3f20b188f2c3bbeb0bc2559a33ed2` | 10,897 |
| `review/wp04-wp07-recheck-v3-2026-09-19/revision-prompt.md` | `4b247519` | `4b247519f52a70b1439a70b61fe470058f1ab8e2d3863e2f33145e8e92fa2215` | 3,983 |
| `review/wp04-wp07-closure-review-2026-09-19/report.md` | `1cc5e453` | `1cc5e453a023fea7d0b7225e35895fc946637e04528d84172e0cb5ce3df3b9ce` | 7,457 |
| `review/wp04-wp07-closure-review-2026-09-19/next-batch-prompt.md` | `a416fcc2` | `a416fcc2dae05a5e1e24e4d6280c89f0b551247222af3efa3073208264f290c4` | 10,313 |
| `review/wp08-wp10-review-2026-09-19/report.md` | `4e455ffc` | `4e455ffc6295c470477653dc2aa6b3a24968e527904c3f9af154d0c3a254635b` | 21,222 |
| `review/wp08-wp10-review-2026-09-19/revision-prompt.md` | `ebfc287b` | `ebfc287b9a61659b9a77da301c96bae21b65c8904fe1125f3435b9afb60fcd09` | 7,637 |
| `review/wp08-wp10-recheck-2026-09-19/report.md` | `03ac20b4` | `03ac20b4a64bdd868affe6ada45822f6580b2c23eaef108492701e4299251e62` | 10,903 |
| `review/wp08-wp10-recheck-2026-09-19/revision-prompt.md` | `facc4d4c` | `facc4d4c9b17864b11ce2331e818eb9f75c5dea7202fcdcc1c1d1a0429f02b4c` | 4,040 |
| `review/wp08-wp10-closure-review-2026-09-19/report.md` | `f414b7ff` | `f414b7ff4232d6df892b8c90cc9c7ea0e43e2955546a01349b4bd24fda9c6150` | 7,335 |
| `review/wp08-wp10-closure-review-2026-09-19/next-batch-prompt.md` | `22fe65a9` | `22fe65a9602b7a9d15cdfe0d52cc7d25c8f21d5a7060690371f1805bb22bec99` | 10,818 |
| `review/wp11-wp13-review-2026-09-19/report.md` | `490e02ac` | `490e02ac1030e11c869699bad9c8f402dcd9322a4d65d9df5ae71e39df40692d` | 21,538 |
| `review/wp11-wp13-review-2026-09-19/revision-prompt.md` | `bc6c9624` | `bc6c9624c2fc941756080f0c2698d5b313688d66de4cae1ec227996c57c038f7` | 9,769 |
| `review/wp11-wp13-review-2026-09-19/revision-response.md` | `048cf40b` | `048cf40b059647e3feed3a184ddeee4b46aa4334ec50f6a1dad4b910098f545d` | 12,906 |
| `review/wp11-wp13-review-2026-09-19/revision-diffs/wp11-map-topology-transfer.diff` | `031308f7` | `031308f7ef3059cd02afd2b673cbea0e73ccc2c8d39e23a1bd4cbacc23f902a8` | 23,168 |
| `review/wp11-wp13-review-2026-09-19/revision-diffs/wp12-terrain-movement-vehicles.diff` | `5dd8b477` | `5dd8b477ab85d0b013b757c40ac60ce84799f70c96cf0e3d73cce55e75419195` | 31,633 |
| `review/wp11-wp13-review-2026-09-19/revision-diffs/wp13-map-events-npc-followers.diff` | `a5dc6d8f` | `a5dc6d8f53a14ce0872e4a1c6cdabfbd7e893bb021efaf90521cb5cec3178681` | 28,599 |
| `review/wp11-wp13-review-2026-09-19/revision-diffs/wp13-interpreter-command-matrix.diff` | `367d0e0c` | `367d0e0c4f6e159d993e1147a6139bd05e44795bc53fcb8912b68e5411a4559c` | 23,105 |
| `review/wp11-wp13-recheck-2026-09-20/report.md` | `80d829f3` | `80d829f306e2aba9d19b25dfd89acb4ebe602b422bb2ce9e8ef8ea0f38ca5854` | 20,746 |
| `review/wp11-wp13-recheck-2026-09-20/revision-prompt.md` | `5cf2dd7e` | `5cf2dd7eda388586a035a8cc5f0c6e901597f3af723b356f3c3ba763fd686354` | 8,784 |
| `review/wp11-wp13-recheck-2026-09-20/revision-response.md` | `afeca04a` | `afeca04a52f7b0a447fb68c51e876144e29a4e3abdb8a8c42a8828aa7bc2833a` | 9,382 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp11-map-topology-transfer.diff` | `d82215d7` | `d82215d749cc1ab8b6215f174eb539c5730d6d688c174c94ba28b0b5a44f3af1` | 8,713 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp12-terrain-movement-vehicles.diff` | `407f47a7` | `407f47a7679e58a99fa76a9c30880825de41aea0a14d7cde1f03fe22c659bf8a` | 18,060 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp13-map-events-npc-followers.diff` | `995070d2` | `995070d2cbe6ad4ad6e3bbb767b59e269eed77f2c29c6bde919d4e9d5ed981c2` | 17,398 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp13-interpreter-command-matrix.diff` | `393b8c0c` | `393b8c0cd21db2bf97b4e96d3e3fbab6dc92c85f48d444ed3f63613b46bff6d3` | 1,621 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp13-move-route-matrix.diff` | `355c9260` | `355c9260e88b31af17e815cdce8074df32a67032e1bb292556c7b4fb15efcd47` | 5,313 |
| `review/wp11-wp13-recheck-v3-2026-09-22/report.md` | `0d605917` | `0d605917577f59aeb0667ba89b457346872912ab3e3d1e7c667a7c615ecf23ea` | 10,497 |
| `review/wp11-wp13-recheck-v3-2026-09-22/revision-prompt.md` | `932a4386` | `932a4386ff352acc8e0f8fddd664db86981089df950155e4f92273dd3c41444c` | 3,261 |
| `review/wp11-wp13-recheck-v3-2026-09-22/revision-response.md` | `ded1f087` | `ded1f0874f0e0fc1b5e4d499e35bafcff357759dc9fd0a5ac277e1df9e0e4830` | 3,860 |
| `review/wp11-wp13-recheck-v3-2026-09-22/revision-diffs/wp11-map-topology-transfer.diff` | `a73e1873` | `a73e1873d392c06904be0bdad742d8c6d522dcea212da3463c157b92c9f0ae67` | 2,594 |
| `review/wp11-wp13-recheck-v3-2026-09-22/revision-diffs/wp12-terrain-movement-vehicles.diff` | `573cc212` | `573cc2122d2b210e44ce30dd892c8a7883f474adfa8be2fbb92a084bed73feda` | 3,592 |
| `review/wp11-wp13-recheck-v3-2026-09-22/revision-diffs/wp13-map-events-npc-followers.diff` | `42c134f5` | `42c134f5d10759859ed5d535cc81b01d087ef8984dd659395cd85121e7ae0376` | 7,887 |
| `review/wp11-wp13-recheck-v3-2026-09-22/revision-diffs/feature-matrix.diff` | `3807b326` | `3807b3268baba972c7137414929ad9622aee8247e181636d22baac736969d853` | 7,594 |
| `review/wp11-wp13-closure-review-2026-09-23/report.md` | `e84f45ea` | `e84f45eaac4db2fa3d970ece6b794b60fe87b0a4b751bddf00674161a69ff0d4` | 6,153 |
| `review/wp11-wp13-closure-review-2026-09-23/next-batch-prompt.md` | `8f22bbe0` | `8f22bbe0636f03eb6764cd3ca79482787a0534a56c161257711be106b98cd8f5` | 3,645 |
| `review/wp14-wp16-review-2026-09-23/report.md` | `bd48bcb3` | `bd48bcb3bf8515910d2fd6e904c8607fe6aeebec7a8d7d8f62af7eb776994152` | 7,978 |
| `review/wp14-wp16-review-2026-09-23/revision-prompt.md` | `7e1e709b` | `7e1e709bcb1321b0c3088dd5e7a9a7a8a8e6a7da214e66a38b406d6cbe8aea23` | 3,470 |
| `review/wp14-wp16-review-2026-09-23/revision-response.md` | `bc317dc4` | `bc317dc4c244b6117503cc995278520c4c94cd31f5a37e0013bce45f30b3120c` | 5,080 |
| `review/wp14-wp16-review-2026-09-23/revision-diffs/wp14-random-dungeons.diff` | `7d5a33d0` | `7d5a33d041d37e4177fae892ff6f37990ba911899e18c85eb9fd7d598af8d917` | 7,302 |
| `review/wp14-wp16-review-2026-09-23/revision-diffs/wp15-resource-matching-and-audio.diff` | `36ecbfc2` | `36ecbfc2e847cc663b1ca816873b7215edccf03235183f6338c6b954fd436594` | 6,286 |
| `review/wp14-wp16-review-2026-09-23/revision-diffs/wp16-world-rendering-and-visual-transitions.diff` | `fe718118` | `fe718118533d22e77875157572a649ed7090208915cecde3aeaf18e44d74cf39` | 7,626 |
| `review/wp14-wp16-recheck-2026-09-23/report.md` | `9d6bc101` | `9d6bc1018da9de6000f28db140f6e2fb3a25e71eb5e55020e4d1b574402eac25` | 11,764 |
| `review/wp14-wp16-recheck-2026-09-23/revision-prompt.md` | `8c0f54f3` | `8c0f54f3c3f2de8f15e0622223f9bcd632ef0dd415433b03463a388f2ff3cd61` | 4,909 |
| `review/wp14-wp16-recheck-2026-09-23/revision-response.md` | `92ebec7d` | `92ebec7d281e86e497ae8ce63d0f32a8be23430de0b2ba284bbb3661a8691b45` | 5,016 |
| `review/wp14-wp16-recheck-2026-09-23/revision-diffs/wp14-random-dungeons.diff` | `860dec6a` | `860dec6af0e8fa105a0692556195c3b875ff2f1c8e26cc4265c336fdb096c51d` | 6,798 |
| `review/wp14-wp16-recheck-2026-09-23/revision-diffs/wp15-resource-matching-and-audio.diff` | `2a06fde4` | `2a06fde4a331ecd14e46a703f7976cf8cc2b4a53999cf2c1f7a8aa91b6ef21fd` | 8,800 |
| `review/wp14-wp16-recheck-2026-09-23/revision-diffs/wp16-world-rendering-and-visual-transitions.diff` | `4905328e` | `4905328e34986a9682a24317983c4577bc86ccac7713846568a1ed60f2b9f7b4` | 9,450 |
| `review/wp14-wp16-closure-review-2026-09-23/report.md` | `a2839f92` | `a2839f929fce00e3b039952c609a9943402a3d377a0628b41c0bae57155dcb07` | 7,423 |
| `review/wp14-wp16-closure-review-2026-09-23/next-batch-prompt.md` | `313a9434` | `313a9434a91c8000b6493df31ad37cc25364ec5451b953318aefd2ad7e1d47a4` | 6,917 |
| `review/wp17-review-2026-09-23/report.md` | `a94e8448` | `a94e8448b8389781f8d89bb0407fd5061963b365d498e1f232f80700d7e51cc2` | 14,508 |
| `review/wp17-review-2026-09-23/revision-prompt.md` | `f117f89c` | `f117f89cd379902d86707e8f7268ac83223b3af938ec0b975190ee90d799599a` | 5,917 |
| `review/wp17-review-2026-09-23/revision-response.md` | `852993f7` | `852993f729e827dd38e120b4e7ac7a76db6bb424260ec66649652b13e0470fbf` | 5,856 |
| `review/wp17-review-2026-09-23/revision-diffs/wp17-messages-windows-input.diff` | `89db47ca` | `89db47cab238234ca9358220255b74efd6de0067ed138e5b2c99dace9e4c27bb` | 38,511 |
| `review/wp17-recheck-2026-09-23/report.md` | `0c6bb45f` | `0c6bb45fa6282e66e4d9f0a70d5490643da3dd6fbe8b5d67b14312a587fb85ef` | 9,033 |
| `review/wp17-recheck-2026-09-23/revision-prompt.md` | `d6159d83` | `d6159d83b8999b3d9953f933ec611d05facfb441e1142e0e40f78afd79ce571e` | 3,387 |
| `review/wp17-recheck-2026-09-23/revision-response.md` | `01632506` | `01632506f5fc23773fab5db7a522b5503d5e24e8c299bec2756aa0f29964b418` | 3,229 |
| `review/wp17-recheck-2026-09-23/revision-diffs/wp17-messages-windows-input.diff` | `7f3ab739` | `7f3ab7390ed02c8edfddffb55e513c961414f4bb06f5d5ad4778e43d897d180d` | 7,289 |
| `review/wp17-recheck-2026-09-23/revision-diffs/wp17-draw-text-tags.diff` | `1ae1d131` | `1ae1d131b4e2c78f3cfa69fd8eaee448da03603c00def96ef19b288940a44d84` | 6,304 |
| `specs/ui/wp17-messages-windows-input.md`（WP17 修订稿 v3） | `6010f40b` | `6010f40b2f00feb1643b7da215ea4ccac1be3e0af429de57a9efaf400c16c4c9` | 29,193 |
| `specs/ui/wp17-draw-text-tags.md`（WP17 绘制标记附表 v2） | `e01466ef` | `e01466ef9f45f661c57f2bb7e53adaa7504d4bafa7e25308f3cb41950a9a24d0` | 7,129 |
| `specs/overworld/wp14-random-dungeons.md`（WP14 Reviewed，状态回填） | `cb4edd9c` | `cb4edd9caac4109baa392b1792c4a52f6c00afb210e63afbf7aa019276ee96f7` | 24,017 |
| `specs/overworld/wp15-resource-matching-and-audio.md`（WP15 Reviewed，状态回填+WP15-C01） | `cb184c3d` | `cb184c3d58a51fa86bc4bc89b5708dc61fa77ad33578709804846494fa7c6143` | 21,219 |
| `specs/overworld/wp16-world-rendering-and-visual-transitions.md`（WP16 Reviewed，状态回填） | `d7aad4aa` | `d7aad4aa649cf7e07cebdda593b7f8b454a712f9fb05ae673cc8cc0a4dca347a` | 21,399 |

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 各轮 review 实测哈希均与当时本地文件一致，对应关系见第 3 节历史。
- 2026-09-19 WP08–WP10 闭合复审实测三包 v3（WP08 `65a79ab5`、WP09 `76450356`、WP10 `d50edf92`）与当时 manifest 的 39 项哈希及字节数全部匹配；本地独立重算结果一致。本轮回填与批次交付后，WP08/WP10 的当前哈希已变为 `4aa7c989` / `b01a9fc7`，矩阵已变为 `c0aaaf1e`；闭合复审实际审查的是回填前版本，新哈希为管理性状态变更，不伪称为复审对象。
- 结论：各轮 review 的审查对象均能与本地文件对应；本轮修订前的被审版本即第 3 节所列历史版本。
- 2026-09-19 WP11–WP13 批次复审修订前，实测四份被审文件与 manifest（`c14b62d1`，17,435 字节）的 SHA-256 及字节数与复审 report.md 第 1 节固定版本全部一致，修订意见适用；修订后三包与命令矩阵新哈希为 `ac090bc1` / `92dba89d` / `a1288287` / `6da4a23e`，新增移动路线附表 `77cbdb3d`；被审哈希保留于第 3 节历史，复审实际审查的是修订前版本，新哈希不伪称为复审对象。
- 2026-09-22 WP11–WP13 v2 复审修订前，实测五份规格/附表、manifest（`fd03ca37`，22,721 字节）与 feature-matrix（`033e48b7`）的 SHA-256 及字节数与 v2 复审 report.md 第 1 节固定版本全部一致，修订意见适用；修订后三包、两附表新哈希为 `df39a9e5` / `7f1979bd` / `1ec410b6` / `ab69bc87` / `f637f1c3`；v2 被审哈希保留于第 3 节历史，v2 复审实际审查的是 v2 版本，v3 新哈希不伪称为复审对象。
- 2026-09-22 WP13-R05 剩余分支修订与 WP11/WP12 状态回填前，实测五份规格/附表、manifest（`9c493983`，27,523 字节）与 feature-matrix（`55352c01`）的 SHA-256 及字节数与 v3 复审 report.md 第 1 节固定版本全部一致。WP11/WP12 经 v3 复审 PASS_SCOPED（被审哈希 `df39a9e5` / `7f1979bd`，保留于第 3 节历史），本轮回填 Reviewed 及 WP12-C01 同步为管理性变更，新哈希 `84ca24a5` / `8187e7de` 不伪称为复审对象；WP13 经 WP13-R05 剩余分支修订为 `b9b809e4`（v4），feature-matrix 为 `3861c4b1`。
- 2026-09-23 WP11–WP13 批次闭合复审：WP13-R05 最后分支闭合，三包均 PASS_SCOPED 且未发现回归；复审实测 manifest 68 条记录全部匹配。WP13 回填 Reviewed（被审哈希 `b9b809e4` 保留于第 3 节历史），回填后新哈希 `0b9bbd02` 不伪称为复审对象；feature-matrix 经 F04-04/F04-05 回填为 `eb27d0bc`。至此 WP01–WP13 全部限定 Reviewed。
- 2026-09-23 WP14–WP16 首轮复审修订前，实测三份规格（`4703c27d`/`1aa30467`/`4e55e3b1`）、manifest（`2a2627bd`，36,361 字节）与 feature-matrix（`667881b8`）的 SHA-256 及字节数与复审 report.md 第 1 节固定版本全部一致，修订意见适用；修订后三包新哈希为 `349b938d` / `30f2544e` / `f93ec3b0`；被审哈希保留于第 3 节历史，复审实际审查的是首版，v2 新哈希不伪称为复审对象。
- 2026-09-23 WP14–WP16 回归复审修订前，实测三份规格（`349b938d`/`30f2544e`/`f93ec3b0`）、manifest（`2e7a84eb`，40,011 字节）与 feature-matrix（`1cce4b65`）的 SHA-256 及字节数与回归复审 report.md 第 1 节固定版本全部一致，修订意见适用；修订后三包新哈希为 `5ca2c044` / `8e44c387` / `ccb7bb9a`；v2 被审哈希保留于第 3 节历史，回归复审实际审查的是 v2，v3 新哈希不伪称为复审对象。
- 2026-09-23 WP14–WP16 闭合复审：三包均 PASS_SCOPED、四个原问题全部闭合、未发现回归；复审实测 manifest 85 条记录全部匹配。三包回填 Reviewed（被审哈希 `5ca2c044`/`8e44c387`/`ccb7bb9a` 保留于第 3 节历史），回填后新哈希 `cb4edd9c`/`cb184c3d`/`d7aad4aa` 不伪称为复审对象；feature-matrix 经六个 Feature 回填为 `315643e3`。回填含 WP15-C01（旧"全缺失"例收紧为"通用候选也缺失则 nil"）。至此 WP01–WP16 全部限定 Reviewed。
- 2026-09-23 WP17 首轮复审修订前，实测 WP17 首版（`e46cd496`）、manifest（`59ae2a99`，47,152 字节）与 feature-matrix（`2609ef9f`）的 SHA-256 及字节数与复审 report.md 第 1 节固定版本全部一致，修订意见适用；修订后 WP17 新哈希为 `e0d54372`，新增绘制标记附表 `9b76c393`；被审哈希保留于第 3 节历史，复审实际审查的是首版，v2 新哈希不伪称为复审对象。
- 2026-09-23 WP17 回归复审修订前，实测 WP17 v2（`e0d54372`）、附表（`9b76c393`）、manifest（`26539aa3`，50,227 字节）与 feature-matrix（`a9d84326`）的 SHA-256 及字节数与回归复审 report.md 第 1 节固定版本全部一致，修订意见适用；修订后 WP17 新哈希为 `6010f40b`，附表新哈希 `e01466ef`；v2 被审哈希保留于第 3 节历史，回归复审实际审查的是 v2，v3 新哈希不伪称为复审对象。

### 2.2 历史版本关系（据本地记录重建，证据受限）

- 2026-09-19 14:18:53 四份总控文档定稿；约 14:38 首次计算哈希并写入清单（历史条目见第 3 节）。
- 2026-09-19 14:39:03，overview 与 module-map 在本地被进一步修订（内容增大、行数不变），送审附件为 14:39 版，清单未同步，造成联合 review 实测值与清单记录不一致（联合 review R01）。
- **证据限制**：14:39 的修改时刻来自本地文件 mtime；变更范围（补核 E04 训练家引用、E11 HTTP 工具、E21 参战/布局，细化总览 §3 与 module-map D01/D11 行）是本地模型比对当前版本与此前阅读记录后重建的说明。**没有该次修改的操作日志或旧版全文**；14:39 之前的两版内容（`0421575b` / `0e22b7f2`）在本地已被覆盖、无留存副本，无法提供逐行 diff。不补造旧版本或历史日志。

## 3. 历史条目（已被替代，仅供追溯）

| 文件 | 旧 SHA-256（前 8 位） | 记录时点 | 替代关系 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `0421575b` | 2026-09-19 约 14:38 | 被 14:39 修订版 `1ca34f44` 替代 |
| `planning/module-map.md` | `0e22b7f2` | 2026-09-19 约 14:38 | 被 14:39 修订版 `32eab70d` 替代 |
| `planning/feature-matrix.md` | `2f4e3e31` → … → `a9d84326` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联、WP03 回填+WP04–WP07 追踪、批次复审关联、三包回填、WP06 回填+WP08–WP10 追踪、批次复审关联、WP09 回填修订、WP08/WP10 回填与 WP11–WP13 追踪修订、WP11–WP13 复审修订（v2 状态与移动路线附表登记）、v2 复审修订（v3 状态与关闭项登记）、WP11/WP12 Reviewed 回填与 WP13 v4 状态同步、WP13 Reviewed 回填、WP14–WP16 批次追踪修订、WP14–WP16 首轮复审修订（v2 状态登记）、WP14–WP16 回归复审修订（v3 状态与 WP16-R02 关闭登记）、WP14–WP16 Reviewed 回填、WP17 批次追踪修订、WP17 首轮复审修订（v2 状态与绘制附表登记）；2026-09-23 经 WP17 回归复审修订（v3 状态与 R02～R05/C01 关闭登记）被 `5aecfd39` 替代 |
| `planning/extraction-plan.md` | `aef0d7ab` → `d441c68b` | 2026-09-19 | 依次经 R02/R03、C02 修订为 `c1735877`（当前有效） |
| `specs/demo/wp01-baseline-and-evidence-scope.md` | `403e814c` → … → `c952847d` | 2026-09-19 | 依次经 WP01-R01/R02/R03、C02、状态回填、尾部状态同步（C03）修订为 `2a52e94e`（当前有效） |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md` | `d322cf95` → … → `272b0291` | 2026-09-19 | 依次经 WP02-R01～R06、F1/F2/C1、状态回填、尾部状态同步（C03）修订为 `82b47151`（当前有效） |
| `specs/kernel/wp02-settings-inventory-appendix.md` | `6fba2cdd` | 2026-09-19 附表首版 | 经 F1/F2 修订被 `f165b1cb` 替代（当前有效） |
| `specs/kernel/wp03-content-identity-and-schema.md` | `d61233f0` → … → `7a9c85da` | 2026-09-19 | 首版经 WP03-R01～R05、复检、枚举存在条件收紧修订为 `7a9c85da`（闭合通过版）；经状态回填被 `de331460` 替代（当前有效） |
| `specs/kernel/wp04-pbs-lifecycle.md` | `e2bc7e6b` → … → `0df88787` | 2026-09-19 | 首版经 WP04-R01～R03、复检 R02 修订为 `0df88787`（v3 通过版）；经状态回填被 `b5d33db1` 替代（当前有效） |
| `specs/kernel/wp05-events-extensions-plugins.md` | `a8412720` → … → `aae49934` | 2026-09-19 | 首版经 WP05-R01～R03、复检 R02/R03 修订为 `aae49934`（v3 通过版）；经状态回填被 `d65b6d14` 替代（当前有效） |
| `specs/kernel/wp06-time-random-steps-stats.md` | `c18eae6a` → … → `3cdfc081` | 2026-09-19 | 首版经 WP06-R01～R03、复检 R03、附表定点修订为 `3cdfc081`（闭合通过版）；经状态回填与 BATCH-C03 维护被 `c01140cb` 替代（当前有效） |
| `specs/kernel/wp06-stats-directory.md` | `0ea55ff1` | 2026-09-19 附表首版 | 经附表事实定点修订被 `15b75cea` 替代（当前有效） |
| `specs/kernel/wp07-diagnostics-files-http.md` | `0225f652` → … → `101577ef` | 2026-09-19 | 首版经 WP07-R01～R03、复检 R01/R03 修订为 `101577ef`（v3 通过版）；经状态回填被 `2cd5408a` 替代（当前有效） |
| `specs/kernel/wp08-localization.md` | `1f2fd3a6` → … → `65a79ab5` | 2026-09-19 | 首版经 WP08-R01～R03、R01 旧总结清理修订为 `65a79ab5`（闭合通过版）；本轮经状态回填被 `4aa7c989` 替代 |
| `specs/kernel/wp09-save-startup-continue.md` | `359eb1c1` → … → `76450356` | 2026-09-19 | 首版经 WP09-R01～R03、状态回填与 BATCH-C02 限定修订为 `76450356`（v2 通过版，当前有效） |
| `specs/kernel/wp10-migration-failure-recovery.md` | `12018885` → … → `d50edf92` | 2026-09-19 | 首版经 WP10-R01～R05、三处条件收紧与 BATCH-C03 修订为 `d50edf92`（闭合通过版）；本轮经状态回填与 BATCH-C04 维护被 `b01a9fc7` 替代 |
| `analysis/inventory/wp02_settings_inventory.py` | `46f1ba84` | 2026-09-19 | 重构为共享模块后被 `dfa38c40` 替代（当前有效） |
| `analysis/inventory/wp02_build_appendix.py` | `898134d0` | 2026-09-19 | 重构为共享模块后被 `7c965c9d` 替代（当前有效） |
| `specs/ui/wp17-messages-windows-input.md` | `e46cd496` → `e0d54372` | 2026-09-23 首版送审 | 首版经 WP17-R01～R05/C01 修订为 `e0d54372`（v2）；经回归复审 WP17-R01 剩余两处与 C02 维护修订被 `6010f40b` 替代（当前有效） |
| `specs/ui/wp17-draw-text-tags.md` | `9b76c393` | 2026-09-23 附表首版送审 | 经回归复审 WP17-R01 剩余两处修订被 `e01466ef` 替代（当前有效） |
| `specs/overworld/wp14-random-dungeons.md` | `4703c27d` → … → `5ca2c044` | 2026-09-23 首版送审 | 首版经 WP14-R01 修订为 `349b938d`（v2）；经回归复审 WP14-R01 剩余范围修订为 `5ca2c044`（v3，闭合通过版）；经 Reviewed 状态回填被 `cb4edd9c` 替代（当前有效，管理性变更） |
| `specs/overworld/wp15-resource-matching-and-audio.md` | `1aa30467` → … → `8e44c387` | 2026-09-23 首版送审 | 首版经 WP15-R01 修订为 `30f2544e`（v2）；经回归复审 WP15-R01 剩余范围修订为 `8e44c387`（v3，闭合通过版）；经 Reviewed 状态回填与 WP15-C01 同步被 `cb184c3d` 替代（当前有效，管理性变更） |
| `specs/overworld/wp16-world-rendering-and-visual-transitions.md` | `4e55e3b1` → … → `ccb7bb9a` | 2026-09-23 首版送审 | 首版经 WP16-R01/R02 修订为 `f93ec3b0`（v2）；经回归复审 WP16-R01 剩余范围修订为 `ccb7bb9a`（v3，闭合通过版）；经 Reviewed 状态回填被 `d7aad4aa` 替代（当前有效，管理性变更） |
| `specs/overworld/wp11-map-topology-transfer.md` | `7f1274c2` → … → `df39a9e5` | 2026-09-19 首版送审 | 首版经 WP11-R01/R02/C01 修订为 `ac090bc1`（v2）；经 v2 复审 WP11-R02 剩余范围修订为 `df39a9e5`（v3，PASS_SCOPED 通过版）；2026-09-22 经 Reviewed 状态回填被 `84ca24a5` 替代（当前有效，管理性变更） |
| `specs/overworld/wp12-terrain-movement-vehicles.md` | `9bc37359` → … → `7f1979bd` | 2026-09-19 首版送审 | 首版经 WP12-R01/R02/R03 修订为 `92dba89d`（v2）；经 v2 复审剩余范围修订为 `7f1979bd`（v3，PASS_SCOPED 通过版）；2026-09-22 经 Reviewed 状态回填与 WP12-C01 同步被 `8187e7de` 替代（当前有效，管理性变更） |
| `specs/overworld/wp13-map-events-npc-followers.md` | `86d96672` → … → `b9b809e4` | 2026-09-19 首版送审 | 首版经 WP13-R01–R05 修订为 `a1288287`（v2）；经 v2 复审剩余范围修订为 `1ec410b6`（v3）；经 v3 复审 WP13-R05 剩余分支修订为 `b9b809e4`（v4，闭合通过版）；2026-09-23 经 Reviewed 状态回填被 `0b9bbd02` 替代（当前有效，管理性变更） |
| `specs/overworld/wp13-interpreter-command-matrix.md` | `1ff42842` → `6da4a23e` | 2026-09-19 首版送审 | 首版经 WP13-R01/R02 修订为 `6da4a23e`（v2）；2026-09-22 经 v2 复审 WP13-R02 剩余范围修订被 `ab69bc87` 替代（当前有效） |
| `specs/overworld/wp13-move-route-matrix.md` | `77cbdb3d` | 2026-09-19 附表首版 | 2026-09-22 经 v2 复审 WP13-R01 剩余范围修订被 `f637f1c3` 替代（当前有效） |

## 4. 2026-09-19 修订与交付摘要（按轮次）

**第一轮至第十四轮**：联合 review 处理与 WP01；WP01 复审处理与 WP02 首版；WP02 复审处理（R01～R06）；WP02 复检处理（F1/F2/C1）；WP02 闭合状态回填与 WP03 首版；WP03 复审处理（R01–R05）；WP03 复检处理（四组剩余项）；WP03 v3 复检处理（枚举存在条件收紧）；WP03 闭合状态回填与 WP04–WP07 批次首版；WP04–WP07 批次复审修订；WP04–WP07 复检六项修订；三包状态回填与 WP06 定点修订；WP06 闭合登记与 WP08–WP10 批次首版；WP08–WP10 批次复审修订；WP09 回填与 WP08/WP10 剩余项修订。

**第十五轮（WP08/WP10 闭合登记 + WP11–WP13 批次，本轮）**：

- **WP08/WP10 状态回填**：WP08 → Reviewed（文本域与已述身份形态、默认/当前语言消息分层、主动/延迟载入、查找/空译/异常边界、占位格式化、提取/编译/直写工作流及适用静态场景范围）；WP10 → Reviewed（固定默认转换登记、版本筛选/顺序、旧格式入口边界、备份与写回路径、已述恢复/紧急保存/地图失败分支、转换目录及已记录参考快照反例范围）；矩阵 F02-05、F03-02、F03-04 同步；被审哈希保留于历史。
- **BATCH-C04 维护**：WP10 树果转换行改为"构造新对象→条件填充→正常到达末尾时替换条目"（非符号输入跳过条件填充仍可到达末尾替换；填充抛错时尚未执行末尾替换）。
- **WP11（地图拓扑与转移）**：地图身份与加载（setup/valid?/validLax?）；连接配置与坐标/偏移规则（边字母换算 N/W→0、E→宽、S→高、显式坐标、双向索引、两端尺寸为 0 忽略）；边缘跨图（连接换算、on_leave_map/on_enter_map、天气重置）；显式传送（取消载具、setup 重建、moveto/转身、跟随者转移、精灵集重建）；生命周期（邻图加载/显示偏移/连接与范围修剪、地图索引错误处理）；地图恢复分支（WP09/WP10 引用）。`7f1274c2`
- **WP12（地形/运动/载具）**：18 个地形标签能力表；通行判定链（通行位/事件阻挡/玩家阻挡/水约束/冰/岩架/桥/冲浪/骑行/严格通行/调试穿透/跨图）；移动入口与结果（move_generic 移动/岩架跳下/下瀑/碰撞）；运动状态机（步行 3/跑步 4/骑行 5/冲浪 4/潜水 3/冰滑 4/瀑布 2 及停止态）；载具函数（上下车、目的地清理、BGM）；瀑布下/上瀑；许可与领域边界（跑鞋/强制路线/徽章交界）。`9bc37359`
- **WP13（地图事件/NPC/跟随）**：事件页选择（从后向前、条件满足、nil 页不可见可穿透）；触发方式（动作键/玩家接触/事件接触/自动运行/并行处理/感知 sight-trainer/counter）；解释器更新循环（冻结防护/失联终止/子解释器/消息/移动/上岸/计时/菜单等待/深度 100 限制）；命令兼容矩阵（48 有实现/18 空操作 command_dummy/2 标记/else 回退）；NPC 移动与感知；跟随者生命周期（FollowerData、实例化、移动/转向/更新、转移限制 followers=0 守卫、持久化与弃用格式）。`86d96672`、`1ff42842`
- **跨包核对**：WP11 转移与 WP12 移动结果一致（跨图通行引用）；WP12 移动与 WP13 触发/等待/跟随一致（步后触发与 over_trigger 联动）；WP13 解释器与 WP05 通知一致（事件通知引用）；WP11 地图恢复与 WP09/WP10 分支一致（引用不重复）；WP13 命令与 WP04 编译转换一致（简写转换与运行时解释器）。未发现规则重复定义或冲突。
- **矩阵增量**：F04-01 → ReviewPending（WP11）＋Inventoried（元数据语义与可达）；F04-02、F04-03 → ReviewPending（WP12）＋Inventoried（真实地图流程/场地招式媒体）；F04-04、F04-05 → ReviewPending（WP13）＋Inventoried（Demo 事件/完整跟随系统）。
- 三包状态均为 **ReviewPending**，统一送外部 review；未自行升级 Reviewed；未执行 WP14。

**第十六轮（WP11–WP13 批次复审修订，本轮）**：

- **复审处理**：外部复审 REQUEST_CHANGES（WP11-R01/R02/C01、WP12-R01/R02/R03、WP13-R01–R05）。修订前实测四份被审文件与 manifest 哈希/字节数与复审固定版本一致；逐项核实→修订→新哈希→清单更新，修复回应见 `review/wp11-wp13-review-2026-09-19/revision-response.md`（`048cf40b`），逐项差异见同目录 `revision-diffs/`。
- **WP11 v2（`ac090bc1`）**：连接端点改为二维锚点定义（N/S 配置值为锚点 x、边值为 y；E/W 反之；显式坐标直用）；修正两个坐标场景（(xA−6, 0)、人工 wB=20 得 (19,2) 及反向例）；显示偏移按子像素单位（REAL_RES=128/格）；四入口转移对照（边缘/同图/跨图 setup/读档恢复）补 moving 守卫、普通移动出界检查、moveto 取模、索引回退、通知时机与玩家位置、缺图入口差异；生命周期补实例复用/重建与临时/持久自开关分层；5.1 表头补证据列。
- **WP12 v2（`92dba89d`）**：通行判定重构为五层（地图层/玩家专用层/角色层/玩家覆写/跟随者严格入口），水/冰限制归非玩家分支；can_run? 补 diving 例外与 must_walk/must_walk_or_run 区分；速度表加非强制路线与 bumping 前提及等级/时间换算；岩架失败不转碰撞；increase_steps 实际行为与计步层次（全局计步引用 WP06）；pbEndSurf 仅结束冲浪、上水另一入口；瀑布清理两分支与调用链；pbCancelVehicles 参数语义与重复上车不计数。
- **WP13 v2（`a1288287`、`6da4a23e`、新增 `77cbdb3d`）**：命令矩阵 10 项误报改空操作（126/133/301/311–313/315–318），统计改 28 dummy + 2 标记 + 66 其他入口（96 分派）并加口径；补 401/655 续行消费；控制结果列逐行区分启动效果/等待/推进（209 vs 210、203、205–207/223–225/232–236/242/246、233、105 双推进、111/122/314/204/353/355 实际语义）；失联改"event_id 归 0、列表继续"并与命令结束/显式退出分列；触发按调用者分入口（over_trigger? 非 through 别名、感知两种检查、更新机会与菜单差别）；跟随补全（去重/移除/领队链/相连与不相连/即时定位/转移后隐藏恢复/互动/守卫适用入口）；新增移动路线命令矩阵附表。
- **交叉检查**：WP11×WP12 载具清理调用点一致；WP12×WP06 计步引用不重复定义；WP13×WP11/12 跟随与路线通行引用一致；WP13×WP07 脚本异常分层一致；WP11×WP09/10 缺图入口差异一致。
- 三包状态保持 **ReviewPending**，v2 再送外部复审；未自行升级 Reviewed；未执行 WP14；未修改 reference/；未提交/推送。

**第十七轮（WP11–WP13 v2 复审修订，本轮，2026-09-22）**：

- **复审处理**：v2 独立复审结论为 WP11/WP12/WP13 分别 REQUEST_CHANGES（剩余 1/3/4 项），WP11-R01、WP11-C01、WP13-R03 关闭。修订前实测五份规格/附表、manifest 与 feature-matrix 哈希/字节数与复审固定版本全部一致；逐项核实→修订→新哈希→清单更新，修复回应见 `review/wp11-wp13-recheck-2026-09-20/revision-response.md`（`afeca04a`），逐项差异见同目录 `revision-diffs/`。
- **WP11 v3（`df39a9e5`）**：显式传送缺图失败按音频前提分两阶段（有 BGM/BGS 时 autofade 先于清桥/setup 读取目标图即失败；无音频时到达 setup 后失败），不再统一"失败时集合已清空"。
- **WP12 v3（`7f1979bd`）**：优先级 0 图块事件的提前许可明确为"结束本次地图层判定"（角色层碰撞仍执行）；层 5 区分跟随者实际入口（location_passable?/move_through）与全向 strict 能力（未检索到默认调用链）；计步层次改为运动开始/完成两观察点（统计与条件性离格通知在开始侧，全局计步仍引用 WP06）；上水状态提交（前跳前提交、失败无回滚）；surf_jump 清理分层守卫；新增 on_enter_map 的 force_cycling 消费者（强制骑行图上车/禁骑图下车/边缘切图亦触发/同图传送无通知）。
- **WP13 v3（`1ec410b6`、`ab69bc87`、`f637f1c3`）**：路线附表推进规则按运动状态（玩家 bump 置计时也算运动状态）并重写、补空强制路线边界；主文档移动等待补"已置等待标记（210）"前提并删除相反场景括注；矩阵 101 行消费范围纠正（相邻 101 不消费、401/102/103 区分）；触发表按实际调用者重写（玩家失败→玩家侧 [1,2]、NPC 失败→事件侧 trigger 2、步完成同位 here 要求 over_trigger 真、counter 仅移动完成后）；跟随位移改条件分支（同轴一格/两格四种许可组合/非同轴直接定位）。
- **交叉检查**：WP12 层 5 × WP13-R05 共用一处通行定义；force_cycling × WP11 通知时机一致；移动等待 × 强制路线术语一致；全局计步仍归 WP06。
- 三包状态保持 **ReviewPending**，v3 再送外部复审；未自行升级 Reviewed；未执行 WP14；未修改 reference/；未提交/推送。

**第十八轮（WP13-R05 闭合修订 + WP11/WP12 状态回填，本轮，2026-09-22）**：

- **复审结论**：v3 独立复审 WP11 PASS_SCOPED、WP12 PASS_SCOPED、WP13 REQUEST_CHANGES（仅剩 WP13-R05 一个条件分支）；其余 7 个剩余项全部关闭，累计 WP11-R01/R02/C01、WP12-R01/R02/R03、WP13-R01/R02/R03/R04 关闭。修订前实测被审文件哈希/字节数与复审固定版本全部一致。
- **WP13 v4（`b9b809e4`）**：跟随位移末分支补"其他非重合目标均直接定位"（同轴超过两格与非同轴均覆盖，非逐格追赶或停留）；新增同轴三格静态场景（(5,5)→目标 (8,5) 直接定位）；一格/两格许可分支与 (1,1) 例保留；两份矩阵未改动。
- **WP11/WP12 状态回填**：按复审 §1 范围分别登记 **Reviewed**（管理性变更；被审哈希 `df39a9e5` / `7f1979bd` 保留历史，回填后新哈希 `84ca24a5` / `8187e7de` 不伪称为复审对象）；WP12-C01 同步收窄（上水运动状态交界已覆盖，仅资格/动画/媒体保留前向范围）；WP13 前置依赖行同步。
- **矩阵同步**：F04-01 → Reviewed（WP11 范围）＋Inventoried（元数据语义与可达）；F04-02、F04-03 → Reviewed（WP12 范围）＋Inventoried（各自前向范围）；F04-04、F04-05 保持 ReviewPending（WP13 v4 范围）。
- 修复回应见 `review/wp11-wp13-recheck-v3-2026-09-22/revision-response.md`（`ded1f087`），差异见同目录 `revision-diffs/`。
- WP13 保持 **ReviewPending**（v4 再送复审）；WP11/WP12 限定通过不等于 F04-01～F04-03 全量通过；未执行 WP14；未修改 reference/；未提交/推送。

**第十九轮（WP13 状态回填与 WP11–WP13 批次闭合，本轮，2026-09-23）**：

- **闭合复审结论**：WP13-R05 最后分支闭合（同轴三格及以上直接定位与源码一致），WP11/WP12/WP13 均 PASS_SCOPED、未发现回归；复审实测 manifest 68 条记录全部匹配，参考 HEAD 不变。
- **WP13 回填**：状态 Reviewed（管理性变更；被审哈希 `b9b809e4` 保留历史，回填后 `0b9bbd02` 不伪称为复审对象）；Feature Matrix F04-04、F04-05 → Reviewed（WP13 范围）＋Inventoried（各自前向范围）。至此 WP01–WP13 全部限定 Reviewed。
- **下一批授权**：按复审建议执行 WP14 → WP15 → WP16（WP16 使用 WP15 固定自检输出）；WP17 留待后续。

**第二十轮（WP14–WP16 批次首版，本轮，2026-09-23）**：

- **WP14 随机地牢（`4703c27d`）**：生成触发（on_game_map_setup + random_dungeon 元数据门控）；输入域（参数集双键回退/图块集首条回退/区域版本/三级种子/屏幕尺寸/地图事件）；参数域全表（含默认值与 cave/forest 样本）；尺寸推导（节点制与 ≥20 直读、缓冲区、大网格奇偶）；迷宫生成（9 类图样、深度优先、额外连接、房间派生、退化整区房间）；连通性泛洪与无上限重绘；墙体推断/34-136 修复/防御性抛错；装饰与图块化（随机选取/变体）；事件与玩家摆放（贴墙拒绝、互距 ≥2、多格支持、100 轮失败抛异常）；种子消费点与重播全局序列、待播种子无条件清空（WP06 引用）。
- **WP15 资源匹配/访问/声音（`1aa30467`）**：路径解析（图像 .png/.gif、音频六扩展名、RTP/加密包、失败归 nil）；物种图像通用降格（闪光→暗影→性别→形态→物种/000）与蛋/脚印/影子回退；训练家（套装后缀回退）与道具图标（000 兜底/机器类型降格/邮件）；缓存（路径+色相键、引用计数、空名 32×32、retain）；音频四类播放（存在才发声、BGM/BGS 状态登记与缺失边界、音量选项缩放、默认 BGM 覆盖）、停止/淡出/暂停/恢复/记忆、pbCueBGM 延迟提示、地图自动播放与夜间变体、传送淡出、叫声回退与系统音效。
- **WP16 世界绘制与视觉过渡（`4e55e3b1`）**：图块精灵网格（循环移位滚动 + 亚格偏移、邻图拼接、无连接全量重绘）、图块来源与优先级/桥/反射分层、自动图块动画（帧时长与 [N] 后缀、uptime 同步）；视口分层（−100 全景/0 地图/200 图片/500 闪烁）；角色精灵（图块图/4×4 图形、灌木深度、图案帧、日夜着色）；反射（静水/普通、摆动、TIME_SHADING 互斥）、冲浪基点、动态阴影；天气（9 类型注册、强度→粒子上限、分阶段淡入淡出、跨图偏移跟随）；雾/全景/色调/闪烁/震动；精灵集生命周期与转场（显式传送重建、边缘切图连续）。
- **批内顺序**：WP14/WP15 分别推进后，WP16 使用 WP15 固定自检输出（`1aa30467`，批内引用注明尚未外审）；WP15 交付前自检发现并修复一处表格未转义竖线，哈希以修正后为准。
- **矩阵增量**：F04-06 → ReviewPending（WP14）＋Inventoried（可达性/种子复现）；F02-04、F05-01、F05-02 → ReviewPending（WP15 对应范围）＋Inventoried（媒体实际存在等）；F05-03、F05-04 → ReviewPending（WP16 对应范围）＋Inventoried（实际视觉结果等）。
- 三包状态均为 **ReviewPending**，统一送外部 review；未自行升级 Reviewed；未执行 WP17；未修改 reference/；未提交/推送。

**第二十一轮（WP14–WP16 首轮复审修订，本轮，2026-09-23）**：

- **复审处理**：首轮复审三包均 REQUEST_CHANGES（WP14-R01、WP15-R01、WP16-R01、WP16-R02）。修订前实测三份规格、manifest 与 feature-matrix 哈希/字节数与复审固定版本全部一致；逐项核实→修订→新哈希→清单更新，修复回应见 `review/wp14-wp16-review-2026-09-23/revision-response.md`（`bc317dc4`），逐项差异见同目录 `revision-diffs/`。
- **WP14 v2（`349b938d`）**：摆放失败按事件/玩家拆分——事件失败置标记、至多 100 轮、抛异常；玩家失败不置标记（参考快照行为），循环静默结束、事件位置保留、玩家暂存坐标保留旧值；异常保证收窄至事件失败路径。
- **WP15 v2（`30f2544e`）**：形态数据前提按入口拆分——前/后图/图标无 get_species_form 前置（候选穷尽才 nil）；蛋/脚印/影子/叫声有形态查询（蛋回退 000 固定兜底，其余 nil）；通用降格与固定蛋/道具回退保留。
- **WP16 v2（`f93ec3b0`）**：天气 duration 语义改为"正值启用固定阶段淡入、零值立即切换"（非实际时长）；补实际调用者前提——全局精灵集仅在类型变化时调用 fade_in，同类型强度变化不保证粒子上限刷新（Rain(1)→Rain(5) 场景登记）。
- **传播检查**：WP16 对 WP15 的资源路径/缓存/帧重置引用不受 WP15-R01 影响，无需修改。
- 三包状态保持 **ReviewPending**，送直接回归复审；未自行升级 Reviewed；**WP17 未启动**；未修改 reference/；未提交/推送。

**第二十二轮（WP14–WP16 回归复审修订，本轮，2026-09-23）**：

- **复审处理**：回归复审三包均 REQUEST_CHANGES（WP16-R02 关闭；WP14-R01、WP15-R01、WP16-R01 保留剩余范围）。修订前实测三份规格、manifest 与 feature-matrix 哈希/字节数与回归复审固定版本全部一致；逐项核实→修订→新哈希→清单更新，修复回应见 `review/wp14-wp16-recheck-2026-09-23/revision-response.md`（`92ebec7d`），逐项差异见同目录 `revision-diffs/`。
- **WP14 v3（`5ca2c044`）**：负可绘制区按事件集合分流（空事件集合不置标记不抛异常、玩家暂存坐标保留；含事件则事件失败置标记可抛）；补明每轮重置失败标记、最终由最后一轮决定。
- **WP15 v3（`8e44c387`）**：区分"形态键未命中但基础物种存在（get_species_form 回退基础记录，专门入口可命中基础资源）/查询整体 nil（脚印/影子/叫声守卫 nil，蛋类走 000 候选）/文件候选全未命中（含蛋 000 也可 nil）"三个条件；三例验收向量替换；前轮"固定蛋兜底"不准确措辞未保留。
- **WP16 v3（`ccb7bb9a`）**：恢复 fade_in 的"正在淡入则返回"守卫链（调用到达→不在淡入→无变化守卫→才判断 duration）；旧粒子基础阶段校准为 1–3 并注 Graphics.delta 累积、time_shift 与完成守卫；场景补"无在途淡入"前提与有在途过渡时零 duration 被守卫拒绝的对照；WP16-R02 保持关闭。
- **传播检查**：WP16 不使用 WP15 的形态查询路径；WP16 头部与 traceability 登记管理性备注（未改子范围自 `1aa30467` 继承、形态范围按 WP15 新版本另审）。
- 三包状态保持 **ReviewPending**，送回归复审；未自行升级 Reviewed；**WP17 未启动**；未修改 reference/；未提交/推送。

**第二十三轮（WP14–WP16 状态回填与 WP17 批次开始，本轮，2026-09-23）**：

- **闭合复审结论**：WP14/WP15/WP16 均 PASS_SCOPED，WP14-R01、WP15-R01、WP16-R01/R02 全部关闭，未发现回归；复审实测 manifest 85 条记录全部匹配。
- **三包回填**：按闭合报告 §3 范围分别登记 **Reviewed**（管理性变更；被审哈希 `5ca2c044`/`8e44c387`/`ccb7bb9a` 保留历史，回填后 `cb4edd9c`/`cb184c3d`/`d7aad4aa` 不伪称为复审对象）；WP15-C01 同步（旧"全缺失"例收紧为"通用候选也缺失则 nil"）；WP16 的 WP15 依赖状态同步为限定 Reviewed。Feature Matrix F04-06、F02-04、F05-01～F05-04 → Reviewed（对应范围）＋Inventoried（各自前向范围）。至此 WP01–WP16 全部限定 Reviewed。
- **下一批授权**：执行 WP17（消息、窗口与输入；F05-05、F05-06），不附带 WP18。
- **WP17 首版（`e46cd496`，`specs/ui/`）**：消息文本进入与替换（顺序敏感、变量递归、性别色、换肤）；控制标记目录（f/ff/g/cn/pt/op/cl/wu/wm/wd/ts/\./\|/wt/wtnp/^/!/se/me/ch 逐项）；逐字显示/快进/暂停/自动继续（busy/resume/waitcount/uptime）；选项（索引编码、cmdIfCancel 正/负/零三种取消策略、内嵌 \ch、确认包装）；数量输入（范围/位数/负号/初值夹限/取消值/越界蜂鸣）；按键层（参考层别名 vs 宿主提供、F8、鼠标窗口内前提）；文字输入（键盘场景 ESCAPE 仅限 minlength=0、光标场景四字符集/自动切小写/无独立取消、自由文本 ESCAPE 返原文、字符计数按字符）；状态交界（消息标记/Input.update 防残留/text_input 进出）；绘制标记目录（c/c2/c3/o/b/i/u/s/outln/fs/fn/ar/al/ac/icon/img/br/r）。
- **矩阵增量**：F05-05、F05-06 → ReviewPending（WP17 对应范围）＋Inventoried（真实交互观察/宿主输入面）。
- WP17 状态 **ReviewPending**，送外部 review；未自行升级 Reviewed；未执行 WP18；未修改 reference/；未提交/推送。

**第二十四轮（WP17 首轮复审修订，本轮，2026-09-23）**：

- **复审处理**：首轮复审 WP17 REQUEST_CHANGES（WP17-R01～R05、非阻塞 C01）。修订前实测 WP17 首版、manifest 与 feature-matrix 哈希/字节数与复审固定版本全部一致；逐项核实→修订→新哈希→清单更新，修复回应见 `review/wp17-review-2026-09-23/revision-response.md`（`852993f7`），逐项差异见同目录 `revision-diffs/`。
- **WP17 v2（`e0d54372`）+ 绘制标记附表（`9b76c393`）**：`\1` 正名为暂停控制符（WP08 占位符 `{1}`）；8 位十六进制为 c2 正文/阴影两半色（各 15 位 RGB）；`\w[]` 置 nil 非恢复默认；`\f`/`\ff` 查找路径与四列切取修正；`\ch` 两字段解析规则（变量号接受 0、取消字段可负/0/非数字转 0）；新增附表（识别 21/处理 19、pg/pog 识别但无动作）。resume 四态区分（忙非暂停不推进字符）；选项 nil/[] 对照、显式取消值不夹限、setter 顺序、边缘回绕 trigger+整除条件；文字上限按三入口模式（键盘拒绝/光标先删再插/自由文本拒绝、初值不截短、自动切小写按模式与光标位置、OK 不足先播 SE 无蜂鸣）；等待/地图更新/清理按入口（局部 message_waiting vs 全局显示标记、自由文本无内建更新、清理仅正常出口）；鼠标 catch_anywhere 参数。
- 矩阵 F05-05、F05-06 → ReviewPending（v2 范围登记）＋Inventoried（前向范围）。
- WP17 状态保持 **ReviewPending**，再送外部复审；未自行升级 Reviewed；未执行 WP18；未修改 reference/；未提交/推送。

**第二十五轮（WP17 回归复审修订，本轮，2026-09-23）**：

- **复审结论**：回归复审 WP17 仅剩 R01 附表两处，R02～R05/C01 全部关闭。修订前实测 WP17 v2、附表、manifest 与 feature-matrix 哈希/字节数与回归复审固定版本全部一致；修复回应见 `review/wp17-recheck-2026-09-23/revision-response.md`（`01632506`），逐项差异见同目录 `revision-diffs/`。
- **附表 v2（`e01466ef`）**：`<c>` 修正为"正文色改变并清除当前阴影色（空阴影压栈），`</c>` 弹栈恢复外层组合"（嵌套例覆盖）；新增图像标记文尾消费边界（单独标记→空绘制项目列表、`A<img=...>` 文尾不生成、含后续字符才产生图像项；注明直接格式化入口边界，不扩大为所有消息文尾图像无效）；场景同步。
- **主文档 v3（`6010f40b`，C02 维护）**：空数组场景改命名参数（commands=[]、defaultCmd=0）；选项确认/空命令场景命名条件化；setter 顺序场景补范围 [1,9]；6.1 通用更新顺序收紧为"按入口不同（7.2）"。已接受范围未重写。
- 矩阵 F05-05、F05-06 → ReviewPending（v3 范围与关闭项登记）＋Inventoried（前向范围）。
- WP17 状态保持 **ReviewPending**，送直接回归复审；未自行升级 Reviewed；未执行 WP18；未修改 reference/；未提交/推送。
