# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-29 WP55／WP56／WP57首审REQUEST_CHANGES修订、C01记法与继承C02剩余后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md`（F12-08四包具名Reviewed；F13-04/F13-05首审REQUEST_CHANGES，按原编号修订后再送） | `b97ed883` | `b97ed8836dd510b8f0c2ca8f0485cf03a01737d2fb515b6d4f0e65a3a56684cc` | 51,500 |
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
| `review/wp17-closure-review-2026-09-23/report.md` | `8a36381b` | `8a36381baa4b3640409052fcead16676d573a2762aaa6b0b965c504f82576f11` | 10,720 |
| `review/wp17-closure-review-2026-09-23/next-batch-prompt.md` | `da7a0ed3` | `da7a0ed331c72e9f85b1b616895171a6d9f74383c4cff1e76ac831c7f48a10b2` | 10,593 |
| `specs/ui/wp17-messages-windows-input.md`（WP17 Reviewed，状态回填） | `bb61f967` | `bb61f967a91423de675a32f71f2a1efd91efc822a6e5d5a08be63d3af246fc12` | 30,047 |
| `specs/ui/wp17-draw-text-tags.md`（WP17 绘制标记附表 v2） | `e01466ef` | `e01466ef9f45f661c57f2bb7e53adaa7504d4bafa7e25308f3cb41950a9a24d0` | 7,129 |
| `specs/overworld/wp14-random-dungeons.md`（WP14 Reviewed，状态回填） | `cb4edd9c` | `cb4edd9caac4109baa392b1792c4a52f6c00afb210e63afbf7aa019276ee96f7` | 24,017 |
| `specs/overworld/wp15-resource-matching-and-audio.md`（WP15 Reviewed，状态回填+WP15-C01） | `cb184c3d` | `cb184c3d58a51fa86bc4bc89b5708dc61fa77ad33578709804846494fa7c6143` | 21,219 |
| `specs/overworld/wp16-world-rendering-and-visual-transitions.md`（WP16 Reviewed，状态回填） | `d7aad4aa` | `d7aad4aa649cf7e07cebdda593b7f8b454a712f9fb05ae673cc8cc0a4dca347a` | 21,399 |
| `specs/creature-rpg/wp18-creature-identity-species-ownership.md`（WP18 **Reviewed（限定范围）**；WP26/WP30/WP28 依赖行同步后，管理性；被审 `4428049b` 保留历史） | `55fb5004` | `55fb5004ecf99272f2f88332d20bb076cce6ca5075f6ed546eb24e83df579791` | 37,448 |
| `specs/pokemon-rules/wp19-attributes-ability-and-stats.md`（WP19 **Reviewed（限定范围）**；WP30/WP28 依赖行同步后，管理性；被审 `6c669fcf` 保留历史） | `cd3dcf4b` | `cd3dcf4bf8e7dbea0a45d4abb30540fe2c28406a614590ac1a198a622930055f` | 36,492 |
| `specs/creature-rpg/wp20-hp-status-moves-helditem.md`（WP20 Reviewed（限定范围），上游引用同步后（含 WP28 依赖行同步）；行为通过版 `d595b1b2` 保留历史） | `05a59789` | `05a59789554a4824121a852f05bf643f799b6e52af6837eb966c19cbec678d3c` | 35,076 |
| `specs/pokemon-rules/wp21-dynamic-forms-and-display.md`（WP21 **Reviewed（限定范围）**，闭合复审 PASS_SCOPED 回填后；被审 `4e475505` 保留历史） | `b5eeb48e` | `b5eeb48e958d58eed9c3bf2048b507e969a81d854e5a24151f63cf718bbd3945` | 42,498 |
| `specs/creature-rpg/wp24-player-trainers-partners.md`（WP24 **Reviewed（限定范围）**，定点复审 PASS_SCOPED 回填后；被审 `8b06ddc4` 保留历史） | `32594094` | `325940946f7b120c4e484695dd35c5804c2baf9411798d95c22af2f944a2e7e5` | 29,668 |
| `specs/creature-rpg/wp25-party-and-storage.md`（WP25 **Reviewed（限定范围）**；闭合轮 WP21 引用同步与 WP26 依赖行同步后，管理性；被审 `98b52717` 保留历史） | `f505afd5` | `f505afd5d1dcbea666effadb5b304c7f384db07a9480637ac064d2a7b6334d17` | 27,107 |
| `review/wp18-wp20-delivery-2026-09-26/delivery-summary.md`（v4 注记后） | `5118e628` | `5118e628da49cec0917ad7bab48f135d91e78104fb108f785d28d7d54ffcca67` | 12,099 |
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv`（v33；636条；原609条保留） | `0f811306` | `0f8113065947f4b94c3ed8cf8d0ea9db8ef53160b7d1728fce7abe56028c2333` | 87,544 |
| `review/wp21-wp25-delivery-2026-09-26/delivery-summary.md`（v4 同步） | `8d8b7e5d` | `8d8b7e5d06234285efc16707af254991881d25d871c6589c07620f09ade13bb2` | 13,976 |
| `review/wp21-wp25-review-2026-09-26/report.md` | `a6354444` | `a6354444fc83f38724d1112cb236ac4c3f14e09fb1fe3ed16025870b43a44577` | 18,772 |
| `review/wp21-wp25-review-2026-09-26/revision-prompt.md` | `2e8f5a67` | `2e8f5a67f8da408f969d129d71db7b6b79c8dc31824d428c93ac839b42dacf58` | 8,164 |
| `review/wp21-wp25-review-2026-09-26/revision-response.md` | `34a3fb5e` | `34a3fb5ecb6ab9f59620610f18f30d4b82741fde39216c13a443aa72b781ebe9` | 9,585 |
| `review/wp21-wp25-review-2026-09-26/revision-diffs/wp21-dynamic-forms-and-display.diff` | `7b8eb22a` | `7b8eb22aee4785902ab76cb2b40c504ab30415697e859e4904278a73c1dd8d42` | 41,319 |
| `review/wp21-wp25-review-2026-09-26/revision-diffs/wp24-player-trainers-partners.diff` | `cf748fc8` | `cf748fc86b35fe1d0105ef5dc36ff354f1b0894c8984d92178f3871831650e56` | 21,841 |
| `review/wp21-wp25-review-2026-09-26/revision-diffs/wp25-party-and-storage.diff` | `3b15e838` | `3b15e838c3219c0e8fe976485c541172f5de3a850d43777eaaf68382355e1cb3` | 27,331 |
| `review/wp21-wp25-review-2026-09-26/revision-diffs/wp19-attributes-ability-and-stats.diff` | `68debf8b` | `68debf8bf0df649833444d30f1e0c4c11f4e175d53eb592464fd14591e870539` | 3,427 |
| `review/wp21-wp25-review-2026-09-26/revision-diffs/feature-matrix.diff` | `991e2b8f` | `991e2b8f0b04a27e83ba97e7dbdc52abdeb14ba00ef758ed5f115a632d9cce08` | 7,882 |
| `review/wp21-wp25-review-2026-09-26/revision-diffs/delivery-summary.diff` | `0f822f78` | `0f822f78b4b6233f7b0383e29f42929c18d9dcdee9874721137deb7ae3ee3f74` | 8,922 |
| `review/wp21-wp25-delivery-2026-09-26/wp18-backfill.diff` | `278faeda` | `278faedafc01d8e5da5a026675f105cf7669866da909b5032e0f0b58aca70591` | 3,153 |
| `review/wp21-wp25-delivery-2026-09-26/wp19-backfill.diff` | `5b760f9c` | `5b760f9c9de0d200acea6ccfc0dc345de1c03c61e6857b73b0f85d36de3ab071` | 3,356 |
| `review/wp21-wp25-delivery-2026-09-26/wp20-refsync.diff` | `98cb92a4` | `98cb92a4b05c25b31eb3bc8fb04a3ed34830047e13def14561a3bffea5550187` | 3,374 |
| `review/wp18-wp20-delivery-2026-09-26/wp17-backfill.diff` | `7d04f964` | `7d04f96424cd7e8427eb819ce2e83b9fbacc674258ccd9ddefe3be0aeab91fda` | 3,301 |
| `review/wp18-wp20-delivery-2026-09-26/feature-matrix-diff-from-review.diff` | `bcd3d0e4` | `bcd3d0e4e86cb07911790daa8b9773893c4ee47f880944f6433fcb49ddd57707` | 11,774 |
| `review/wp18-wp20-review-2026-09-26/report.md` | `2f8b22e3` | `2f8b22e308e33e2ce3c332b21e3a6f735dc78e53b766bf105afdc48deafe4c16` | 19,173 |
| `review/wp18-wp20-review-2026-09-26/revision-prompt.md` | `44cccbca` | `44cccbcae8d0cfcff015103388136d599cd5e8ec4fb7d5521a39835f1ab991a1` | 8,697 |
| `review/wp18-wp20-review-2026-09-26/revision-response.md` | `aea5c122` | `aea5c122fe64e145d471a80cfcb5e0a871b69154dd804b2f3e4e0c378b13c374` | 12,269 |
| `review/wp18-wp20-review-2026-09-26/revision-diffs/wp18-creature-identity-species-ownership.diff` | `a5f7283d` | `a5f7283d9309c38c14429af8b7f771f4c9eb8ef3cd5b1c281e28c5be020acc15` | 12,875 |
| `review/wp18-wp20-review-2026-09-26/revision-diffs/wp19-attributes-ability-and-stats.diff` | `fe6c4de9` | `fe6c4de94c90122a9569febcc3acd300321d918533e331e85a9b02c88fa6dbaa` | 23,608 |
| `review/wp18-wp20-review-2026-09-26/revision-diffs/wp20-hp-status-moves-helditem.diff` | `e8ba1b68` | `e8ba1b68d442f7c32054200f5187c94c076e8c9dd389b44c5a6b75d7cb67e002` | 30,733 |
| `review/wp18-wp20-review-2026-09-26/revision-diffs/feature-matrix.diff` | `09014951` | `090149517a9fe65bece87232471200c52307f3e1c11189edd6a11fd365b45d70` | 12,426 |
| `review/wp18-wp20-review-2026-09-26/revision-diffs/delivery-summary.diff` | `26aa5906` | `26aa590645a3dd3dc914c9492ad14683dc73aa81728fb1a194139b528ab6b823` | 9,447 |
| `review/wp18-wp20-recheck-2026-09-26/report.md` | `18356917` | `1835691740ada23333e8d5ea7b05463de46671f2352085c28c3597400b328542` | 11,643 |
| `review/wp18-wp20-recheck-2026-09-26/revision-prompt.md` | `e67680a7` | `e67680a74859913ee072114d4c255d9eced34d400490138e59bd22e09b1f3de4` | 4,890 |
| `review/wp18-wp20-recheck-2026-09-26/revision-response.md` | `07a481ab` | `07a481ab7774d9b5ad5ccb0c0f2a90fd083fa29739bee3ba5bafa5d46deec97a` | 6,501 |
| `review/wp18-wp20-recheck-2026-09-26/revision-diffs/wp18-creature-identity-species-ownership.diff` | `709c73f9` | `709c73f91f81925f541a0076b3b7cfa2cc57d33a7a6ddc6c329e8d1003c34d9b` | 7,475 |
| `review/wp18-wp20-recheck-2026-09-26/revision-diffs/wp19-attributes-ability-and-stats.diff` | `d299a14b` | `d299a14bedc75bc036ddc75ee25877bb1ab4b11d0ce0e6119796429859dc0e7e` | 8,249 |
| `review/wp18-wp20-recheck-2026-09-26/revision-diffs/wp20-hp-status-moves-helditem.diff` | `5aa23ca0` | `5aa23ca038c30084d023ba5b9e742897ef3d1d67e8ba3d7c2afe273142797ae0` | 7,947 |
| `review/wp18-wp20-recheck-2026-09-26/revision-diffs/feature-matrix.diff` | `113a1fbe` | `113a1fbeed89a43443dca3b8f0743bc7c6f308405cea73fd198753ead9155774` | 12,689 |
| `review/wp18-wp20-recheck-2026-09-26/revision-diffs/delivery-summary.diff` | `8c15d66d` | `8c15d66d32329f83cb312a11e05ad4a9ba37e37883715b28fb2491fa2b8d7a2c` | 11,664 |
| `review/wp18-wp20-closure-review-2026-09-26/report.md` | `93f1de1c` | `93f1de1c669e3410304511b1e18c695278779a9943eea4b5e70c50d736d634ef` | 8,748 |
| `review/wp18-wp20-closure-review-2026-09-26/next-batch-prompt.md` | `cd213c33` | `cd213c33479a77842faec025f68eeecd6a665018af9b95f975a088be6a1a9453` | 10,450 |
| `review/wp21-wp25-recheck-2026-09-26/report.md` | `f2dc78d2` | `f2dc78d21de9982c71677f80e8a0b109a27870c2602a0b728de7b85aa43ea6fa` | 11,521 |
| `review/wp21-wp25-recheck-2026-09-26/revision-prompt.md` | `6e6fc526` | `6e6fc526fde90d964c56ea31222cdb81acee3db9f2ab17466c4c9080d343faa7` | 4,550 |
| `review/wp21-wp25-recheck-2026-09-26/revision-response.md` | `7b5d3775` | `7b5d3775390c200cde13ded556be5eb6f7d99b4f0941186de37bb3522a46f4cc` | 6,023 |
| `review/wp21-wp25-recheck-2026-09-26/revision-diffs/wp21-dynamic-forms-and-display.diff` | `d812eabe` | `d812eabe2ef3c51c414617da8bd83d356ea08169ebb45b529cd4c6cde7a3e8f3` | 12,874 |
| `review/wp21-wp25-recheck-2026-09-26/revision-diffs/wp24-player-trainers-partners.diff` | `91b61274` | `91b61274a48ded0385644e0a3f390a6e91a18d48c490f69fd007c19df9231992` | 6,861 |
| `review/wp21-wp25-recheck-2026-09-26/revision-diffs/wp25-party-and-storage.diff` | `96c2046a` | `96c2046a01cfa93a17c88029bcfcea9052cb6463e192fab44bd2b344bc1c7650` | 9,168 |
| `review/wp21-wp25-recheck-2026-09-26/revision-diffs/feature-matrix.diff` | `a82406ba` | `a82406ba28c683a74bbc7db834512f42e382908df57399010896d3603669c9ae` | 8,017 |
| `review/wp21-wp25-recheck-2026-09-26/revision-diffs/delivery-summary.diff` | `30f62f8b` | `30f62f8b33ae8258fcdd65b72f719ee6161f1c1ec32fe47125ddb45b2fd050eb` | 13,797 |
| `review/wp21-wp25-closure-review-2026-09-26/report.md` | `12e283ae` | `12e283ae0cfb665452c3a89fc73ecc21e26fbdff29a73d3613974f99a5d141f0` | 8,339 |
| `review/wp21-wp25-closure-review-2026-09-26/next-batch-prompt.md` | `f09c5a8a` | `f09c5a8a4cdab1c1f059386513fab4191d32502c8e3e9f4f11a244bd91867bd4` | 10,380 |
| `review/wp21-wp25-closure-review-2026-09-26/revision-response.md` | `90961bb0` | `90961bb019ee40f8ae023476594d4f2ceeef9ce237dfa55de6e8935eb8e09123` | 3,590 |
| `review/wp21-wp25-closure-review-2026-09-26/revision-diffs/wp21-dynamic-forms-and-display.diff` | `a4926019` | `a492601961e08a8fb2d6c8dc0128ed75ab9f0896e7ed64163cf94cde9595243b` | 3,516 |
| `review/wp21-wp25-closure-review-2026-09-26/revision-diffs/wp18-creature-identity-species-ownership.diff` | `4f754254` | `4f7542547b81da9e7725019c67bde4f9779430c71ec17eb51698cb8a0b064e65` | 1,458 |
| `review/wp21-wp25-closure-review-2026-09-26/revision-diffs/wp19-attributes-ability-and-stats.diff` | `7958529b` | `7958529bf3c2740b08c2da3fb1d078042ddd094e7c4990d95a286f602d74634d` | 1,073 |
| `review/wp21-wp25-closure-review-2026-09-26/revision-diffs/wp25-party-and-storage.diff` | `1369e8b9` | `1369e8b96d216e7f38cf9c5d5140f36eadc3f0f81dabf9b5b4a5e310f66b2b38` | 913 |
| `review/wp21-wp25-closure-review-2026-09-26/revision-diffs/feature-matrix.diff` | `118a8d31` | `118a8d314c5870684e900624be3ac6affde0028e3d77d60308dda748dc936820` | 4,133 |
| `review/wp21-wp25-closure-review-2026-09-26/revision-diffs/delivery-summary.diff` | `b5aa766b` | `b5aa766b55156f1cdf2d8dc1799a1e976c08e4451d90817dc4b1d714e3637734` | 14,888 |
| `specs/creature-rpg/wp26-acquisition-gifts-and-script-trade.md`（WP26 **Reviewed（限定静态范围）**，2026-09-26 闭合复审 PASS_SCOPED 回填后；被审 v3 `afc7214a` 保留历史） | `c87101ad` | `c87101adc78d2bf5d6c51fd6bb2f608fec0b2536da19d855f12cdaca79520f18` | 35,738 |
| `specs/creature-rpg/wp27-bag-and-item-storage.md`（WP27 **Reviewed（限定静态范围）**，2026-09-26 闭合复审 PASS_SCOPED 回填后；WP28/WP29 依赖行同步（2026-09-27，管理性）；被审 v3 `969cb37c` 保留历史） | `6ac234e4` | `6ac234e466918123fe0382cef95829d20456522b4e17d377df31e079649a908d` | 27,602 |
| `specs/creature-rpg/wp30-growth-learning-and-friendship.md`（WP30 **Reviewed（限定静态范围）**，2026-09-26 闭合复审 PASS_SCOPED 回填后；WP28 依赖行同步（2026-09-27，管理性）；被审 v3 `41e71624` 保留历史） | `b9f58991` | `b9f58991b095f780b6dd9fbfe6f460224433f1b608cc575767c59278f5a4cf21` | 37,019 |
| `review/wp26-wp27-wp30-delivery-2026-09-26/delivery-summary.md`（v4 回填注记后） | `bdd353fd` | `bdd353fdf5ab24efe6014c01f707e653998d61c60c9d39b1950bdd1b14bf93de` | 13,366 |
| `review/wp26-wp27-wp30-delivery-2026-09-26/feature-matrix-diff-from-closure.diff` | `c8b70094` | `c8b700944e511a503ddab985933e074e7ad86663a971b6c9e3e55381a4cd29a3` | 12,628 |
| `review/wp26-wp27-wp30-review-2026-09-26/report.md` | `78a9ba42` | `78a9ba42675f16cc8900dc434f97a6eaacb5c819c42b072aa38f538b0d7e9e23` | 25,241 |
| `review/wp26-wp27-wp30-review-2026-09-26/revision-prompt.md` | `5f48b43b` | `5f48b43b17fd233cb3e9321208c4ba48e7a185b95747a84f5c274d4b96bf24a8` | 9,590 |
| `review/wp26-wp27-wp30-review-2026-09-26/revision-response.md` | `2765129f` | `2765129f9a94c5cc94e7ce731c9c84655943ccb5e5058728ac509aa4d16f5258` | 9,462 |
| `review/wp26-wp27-wp30-review-2026-09-26/revision-diffs/wp26-acquisition-gifts-and-script-trade.diff` | `a7855f91` | `a7855f91355185fc9d79d4bf87cc932d870a25720f1f863ab0a4ed8ed6d742d8` | 29,067 |
| `review/wp26-wp27-wp30-review-2026-09-26/revision-diffs/wp27-bag-and-item-storage.diff` | `0a329ee2` | `0a329ee2030a7c5168a573ab2cfcc67e8d4d54b47b7f9225ea3b19b62b711f93` | 21,706 |
| `review/wp26-wp27-wp30-review-2026-09-26/revision-diffs/wp30-growth-learning-and-friendship.diff` | `4e89689c` | `4e89689cda3c04534651800ed859ca605a36a6904c38b68d7e2a2fd1d1c33364` | 28,948 |
| `review/wp26-wp27-wp30-review-2026-09-26/revision-diffs/feature-matrix.diff` | `edf6b1fb` | `edf6b1fb6c163c60b70fbcdbe034dc105653aeff0e4bf994dfdb53efc6982a6f` | 10,401 |
| `review/wp26-wp27-wp30-review-2026-09-26/revision-diffs/delivery-summary.diff` | `097b56e4` | `097b56e4023111695c7c21ae10bc5b694622fbd9d8505cca3234cbf2b1121454` | 11,638 |
| `review/wp26-wp27-wp30-recheck-2026-09-26/report.md` | `8c23dfa1` | `8c23dfa132760a3e90be87924e341d72c36fb263fdf8e42fe84df1aa645f80d7` | 16,221 |
| `review/wp26-wp27-wp30-recheck-2026-09-26/revision-prompt.md` | `4306637f` | `4306637fc1a988c1859f06d147d43c8a563810583ea8fd6e31167ef980b6d006` | 7,592 |
| `review/wp26-wp27-wp30-recheck-2026-09-26/revision-response.md` | `8a4ee716` | `8a4ee7163c00da5f1a41de1a71de129f707ae49b6888496c1dd33f25840ea26b` | 6,393 |
| `review/wp26-wp27-wp30-recheck-2026-09-26/revision-diffs/wp26-acquisition-gifts-and-script-trade.diff` | `237ae5f3` | `237ae5f3380840f6c518ecc027043c4cef1892ae6c869de191724cc70aede927` | 17,067 |
| `review/wp26-wp27-wp30-recheck-2026-09-26/revision-diffs/wp27-bag-and-item-storage.diff` | `5add2f96` | `5add2f96a33b1ed6a7419dd4942c111d3ef90226a60b58470f111191a7d13409` | 15,481 |
| `review/wp26-wp27-wp30-recheck-2026-09-26/revision-diffs/wp30-growth-learning-and-friendship.diff` | `c684dcb1` | `c684dcb193f6ef9cf562ec555413f5ee241fe0d8759eb9dce251e56114493804` | 11,877 |
| `review/wp26-wp27-wp30-recheck-2026-09-26/revision-diffs/feature-matrix.diff` | `e3c3e241` | `e3c3e2418cbbf3e8f7ea2f413e29477a056d9ae91ddfa0c4561be9b87a65a4fa` | 10,789 |
| `review/wp26-wp27-wp30-recheck-2026-09-26/revision-diffs/delivery-summary.diff` | `fb5a69fd` | `fb5a69fda6d214080ad9b1cbb5d373b4057182c3312edb2e1d89711f39f698e7` | 13,619 |
| `specs/pokemon-rules/wp31-basic-evolution.md`（WP31 **Reviewed（限定静态范围）**，2026-09-27 有限复审 PASS_SCOPED 回填后；WP28/WP29 依赖行同步（2026-09-27，管理性）；被审 v2 `e541c650` 保留历史） | `0b40917c` | `0b40917c3a0c9b942f004dd5fb6bc75addf749d154e162e75e06a2f001806d91` | 39,554 |
| `specs/creature-rpg/wp28-item-use-and-training.md`（WP28 **Reviewed（限定静态范围）**，2026-09-27 闭合复审 PASS_SCOPED 回填后；被审 v3 `7e10cb25` 保留历史） | `a4ccb383` | `a4ccb38365521eeb130b30d9e04a281812cd03ccc76ca5443393f5fbc352d95a` | 44,159 |
| `specs/creature-rpg/wp29-shops-and-exchanges.md`（WP29 **Reviewed（限定静态范围）**，2026-09-27 闭合复审 PASS_SCOPED 回填后；被审 v3 `1ed4b957` 保留历史） | `f7788c7d` | `f7788c7d600c7e9c266f3c8178c81a587b4807f5218b66286a3f3d3a4e5ef31f` | 26,053 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/report.md`（闭合复审报告） | `21712a5c` | `21712a5c8715b793e18f2426868685f6e83caccf4e3f59eee083daef7e6d6e29` | 11,449 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/next-batch-prompt.md`（回填＋下一批执行提示） | `8091fed2` | `8091fed24599616048b6b2ac83b25fba4bebc0070b96eed18e1c79d319e58fda` | 12,982 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/input-manifest.json` | `a7c30375` | `a7c303750debf8adb2c2f36f5d05516b3ce07c6bbd3adb623ac0942f608a9eb0` | 113,632 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/current-hashes.tsv` | `b2d4dc7f` | `b2d4dc7fcad71a76b3b95a113abb7388df61b7b9890367bfb919028f5beeefd5` | 24,945 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/changes-from-v2.diff` | `23ad4a7c` | `23ad4a7cc7b21b32454fb71666093eefd97f66b636382df913c6b32b16a7298e` | 99,411 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/diff-checks.json` | `0eb2cd90` | `0eb2cd90438e26190d6756c95ea226ae62a8b5f904261fb7891fcb6bbc9ce391` | 1,674 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/source-checks.json` | `5edade54` | `5edade54951848612ae8ac1cf3f2d42f9cfd91c7e1ea729e362ef0e6c281c7ed` | 8,661 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/static-checks.json` | `155addb3` | `155addb33407eca3c3c1fc156339c9ef8bc50882cdfec19c489febaef381debe` | 1,937 |
| `review/wp26-wp27-wp30-closure-review-2026-09-26/final-checks.json` | `dfcfad8a` | `dfcfad8acfaa9eb433bc8c84e16695a2c89b9e3bd77730e844927eac6beb3ecd` | 2,354 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-response.md`（回填回应） | `fd800ef2` | `fd800ef2534491eeaae1a8a7023f59fe185eb605a78d65849c2bd52cc56a7e56` | 6,306 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/delivery-summary.md`（本批交付摘要 v4，闭合回填注记后） | `990f30b4` | `990f30b417e4d561a67530992df3428ea5fdae78c9f038f90a0c046e6cfa2109` | 14,649 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/self-checks.json`（逐包自检） | `f22d8fdc` | `f22d8fdcf5c39c96d5507c66a49c373a7b8be768485898109b298f6dbeb702f6` | 7,388 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/boundary-checks.json`（批末交界） | `63fb993b` | `63fb993be6c6a2c5f697a6324d24429b6a8caa3fd49391a96004729948d6a59b` | 3,359 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/wp26-backfill.diff` | `1f290388` | `1f290388f1e1616baac1be3dea65e4278cd99e3c9a160f8614b3866d75dc909d` | 3,567 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/wp27-backfill.diff` | `f2131aec` | `f2131aec5dfaaf55d359a73e1b7b5986d9a7227d9712d15035446a5e4a77ada5` | 3,083 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/wp30-backfill.diff` | `c6025a2d` | `c6025a2d6bb1db8315a6f7562b8d2309cb3ba7728c9fa6a69ea667ddf757a12c` | 7,784 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/feature-matrix.diff`（含回填与新批次增量） | `1204fc1b` | `1204fc1b792f39a0a74981974c639d6900ed4ce1f6ca566c84c72511b4c50da9` | 12,806 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/wp18-refsync.diff` | `7cda993c` | `7cda993cf38a4f52fa072d69c1a19241bcd5b179799f7fdbdeb5d6cf5ca3f516` | 1,705 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/wp19-refsync.diff` | `c0d9b873` | `c0d9b8738e2c25759ba498dcd33b7efad2fa8e0a80ac48b6f89974e758571380` | 1,272 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/wp20-refsync.diff` | `9514fa6e` | `9514fa6e43a60a982a2d1bd1f6c43eec0f9922fd2d3b86ba2752a05e66a93983` | 1,206 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/wp21-refsync.diff` | `7905061c` | `7905061cb71ebaaacd77e790db2cfe719b03441705edc1d1932efc77d41d2896` | 1,417 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/wp25-refsync.diff` | `5725a497` | `5725a497f03edec25d77c61cd625edd165f8fec4d569f6af9a227440d4dbaeeb` | 1,175 |
| `review/wp31-wp28-wp29-delivery-2026-09-26/backfill-diffs/delivery-summary.diff` | `99700a02` | `99700a02325b517e6e3c73051f81a7f35c486f01d2ea5e37ec6e1b0fc535b6ab` | 4,208 |
| `review/wp31-wp28-wp29-review-2026-09-26/report.md`（首审报告：REQUEST_CHANGES，10 项必修＋C01/C02） | `5e34d822` | `5e34d822a9ef350dc4944ca5d505a749651cea6a807fc868e22ee860fbc0ed59` | 21,709 |
| `review/wp31-wp28-wp29-review-2026-09-26/revision-prompt.md`（有限修订提示） | `13d32a4b` | `13d32a4b2fca619b0419f3cc3a49bd3f7b3d9836b39565dd75167346cfaab646` | 10,673 |
| `review/wp31-wp28-wp29-review-2026-09-26/input-manifest.json` | `b2967d6e` | `b2967d6e046928df485a0f53c2c4aefb30f2967de7fc689a0bae000a025dbf0e` | 131,803 |
| `review/wp31-wp28-wp29-review-2026-09-26/current-hashes.tsv` | `fd2b2230` | `fd2b2230f2d472d2140e1ddc38bf4d717f4c3c5463d9ccafde26df477ac5191d` | 27,618 |
| `review/wp31-wp28-wp29-review-2026-09-26/changes-from-previous.diff` | `1b8225b0` | `1b8225b06f0644668f4155e7a039b7512602ad27486c410356325789e24f9611` | 87,466 |
| `review/wp31-wp28-wp29-review-2026-09-26/diff-checks.json` | `c2cde3fe` | `c2cde3fe996c130e60a2aa2f6973fb0030e0c55604e37dd62fe8d5f6349c6691` | 3,756 |
| `review/wp31-wp28-wp29-review-2026-09-26/source-checks.json` | `43324492` | `433244929486aa477b8aae9c130218eec4ec338af8da3dfe4b33c1ba4f2a9c28` | 7,270 |
| `review/wp31-wp28-wp29-review-2026-09-26/set-checks.json` | `efd7ea17` | `efd7ea17a01f784ee6e59a103d06d8e14eb7cd9fb599107aee6f04c9fc1639f5` | 3,019 |
| `review/wp31-wp28-wp29-review-2026-09-26/arithmetic-checks.json` | `8993e8eb` | `8993e8eb0035f3fbd9a5b62167fb8d716102fe2221ab1e26a9ec9b81f8fbdc84` | 1,927 |
| `review/wp31-wp28-wp29-review-2026-09-26/static-checks.json` | `395e757a` | `395e757a630d6fb456a2703e995cdd1a7777cf1a28b5d2443abc656081bcf6b3` | 820 |
| `review/wp31-wp28-wp29-review-2026-09-26/final-checks.json` | `55727086` | `557270868915ff0d4e82bf8eb8578a2b2c3a21d6cd7b77a6b2e2ce4572d04637` | 2,515 |
| `review/wp31-wp28-wp29-review-2026-09-26/revision-response.md`（逐项修订回应） | `e516ca69` | `e516ca699c06d41cf2414e5e3b5e897e3d6ba5c0c9b78084d940d6cf5e69fe2f` | 10,646 |
| `review/wp31-wp28-wp29-review-2026-09-26/revision-diffs/wp31-basic-evolution.diff` | `1353e3c2` | `1353e3c2a7b1c2262ee2321f55b37b0d90f9694734acb1a934910ce0558e68aa` | 22,066 |
| `review/wp31-wp28-wp29-review-2026-09-26/revision-diffs/wp28-item-use-and-training.diff` | `30f91d9a` | `30f91d9a37425778eec919b62fdd1977efc8de7bc183cc1d0cb6e95be5e43fbe` | 40,003 |
| `review/wp31-wp28-wp29-review-2026-09-26/revision-diffs/wp29-shops-and-exchanges.diff` | `b5b287d9` | `b5b287d9e5cc8d3218d9aedb276c06c9aaa0ec5107090d886d881fb9ad4c4769` | 19,541 |
| `review/wp31-wp28-wp29-review-2026-09-26/revision-diffs/feature-matrix.diff` | `ce3183ac` | `ce3183aceb80a7f3ffb62ea439581d85273774ace7ab34e38637b9d614a754e1` | 7,711 |
| `review/wp31-wp28-wp29-review-2026-09-26/revision-diffs/delivery-summary.diff` | `0db55cfc` | `0db55cfc59424490dc5052c969b96638b298998923e654cc5cf7800e8ee8420c` | 4,402 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/report.md`（有限复审报告：WP31 PASS_SCOPED；WP28/WP29 剩三项） | `f6f2c705` | `f6f2c70579b133446bd52ff1dc330e347b85ff0ec961a9d559f1b05d817dd220` | 12,842 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/revision-prompt.md`（WP31 回填＋三点收尾提示） | `bcef7f46` | `bcef7f4617d533b14dd43c724801894d03b52f1b4a8201ac37c68a8b6008c787` | 7,465 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/input-manifest.json` | `bf75dd05` | `bf75dd051c96c655659cc5fb3b018783838dbd266ba457f1241a9ce42e4c323f` | 141,309 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/current-hashes.tsv` | `a4722cce` | `a4722cce0fd64a1b016401ac433737f848f1b6ab1821b5d62442c6447f7401c3` | 29,782 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/changes-from-v1.diff` | `4000ff37` | `4000ff3757dc7a3d6d779926b58dda665be9a2593f55d6ed3bf5afbf9693b59c` | 129,275 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/diff-checks.json` | `01e51ade` | `01e51ade9ecb3896a4d9acb9be0cbe3f28e404fb3b990c7ac81d50b6efbc9b44` | 1,784 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/source-checks.json` | `dd61fed9` | `dd61fed947114faf1017d6ce92abf57dcb2bb08eb32aefab8aa55a280fce124f` | 6,669 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/static-checks.json` | `3cd7f2e0` | `3cd7f2e0f23e1875bea7cfc7628b543c5f51e77f2bb464748c7dc25830f5e6f9` | 791 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/static-vectors.json` | `6928addb` | `6928addb42c2e7ab674248dfd13574dcd4e664eea12d46bfdbfa07ef588584b9` | 2,067 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/final-checks.json` | `46edc95f` | `46edc95f184c450e299d9f065366bbc59114373d356fa861b2f6edb992498200` | 2,460 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/revision-response.md`（WP31 回填＋三点收尾回应） | `73c9cab3` | `73c9cab38496f5d60269bf479ce8a90f2a1e02b3a16b320ab7e4e05a8d08a851` | 7,260 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/revision-diffs/wp31-basic-evolution.diff` | `4d5e843d` | `4d5e843dec5eae3765a2ad69e03ea441cc459a32380283a2de1fdfc0e22f02b7` | 3,707 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/revision-diffs/wp28-item-use-and-training.diff` | `85df9c4c` | `85df9c4cda371d6a528b851f32c10824fe82e2fd0b9e6aba37b833e72e0be9a7` | 19,382 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/revision-diffs/wp29-shops-and-exchanges.diff` | `f9930cb9` | `f9930cb9191ef73c9bc1948b07e9fe77e12ff025f1a6df7bfb8be433739186d9` | 5,613 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/revision-diffs/feature-matrix.diff` | `2688d197` | `2688d19727cbd579966f291efcabdaf0d1c9bea6a0670ba608521acf1da04082` | 7,962 |
| `review/wp31-wp28-wp29-recheck-2026-09-27/revision-diffs/delivery-summary.diff` | `08809ecd` | `08809ecdfa5afcd1147cd67e1ff2cf8a39baa792aad1424328519ee824dc6e3d` | 4,762 |
| `review/wp31-wp28-wp29-closure-review-2026-09-27/report.md`（闭合复审报告：WP28/WP29 PASS_SCOPED；WP31 回填接受） | `8d56d23e` | `8d56d23e3271907e3522557cbed6315c85f01f4503ccdeae824abf5cfc76c6e3` | 8,920 |
| `review/wp31-wp28-wp29-closure-review-2026-09-27/next-batch-prompt.md`（回填＋WP33→WP35 提示） | `a9e31d54` | `a9e31d54a7b096bc7849d8fd14f0f01063fdb98bd1815aeb166dca4cf41deb0e` | 12,960 |
| `review/wp31-wp28-wp29-closure-review-2026-09-27/input-manifest.json` | `95d28936` | `95d2893698e5d7685690ed7713a8298d60b9af1fbf61f957fa0fcfde5e2dbe0c` | 152,200 |
| `review/wp31-wp28-wp29-closure-review-2026-09-27/current-hashes.tsv` | `a2c2b170` | `a2c2b170c8dcc45920e26e69f9371ba2d67c6076d72d34a3a4149c2f273d0fff` | 31,972 |
| `review/wp31-wp28-wp29-closure-review-2026-09-27/changes-from-v2.diff` | `e24903fa` | `e24903fa5dc7d52067e4d2631286f0545f104189070acc69f33ed1776d9f7b05` | 78,281 |
| `review/wp31-wp28-wp29-closure-review-2026-09-27/diff-checks.json` | `f9d53111` | `f9d53111da584aff6b80fdbe549ed915100ab122585019891e8e911dc607f585` | 1,785 |
| `review/wp31-wp28-wp29-closure-review-2026-09-27/source-checks.json` | `1a106d37` | `1a106d3738f333838a7a7c27b7b811233540785d44e05347dfd610024caa9f8f` | 6,844 |
| `review/wp31-wp28-wp29-closure-review-2026-09-27/static-checks.json` | `a34d677d` | `a34d677dbe5b4501e1f3fb6a31a1e7d254341c3d3dd33c2dadc3e48739083d3d` | 1,213 |
| `review/wp31-wp28-wp29-closure-review-2026-09-27/final-checks.json` | `0b7928e4` | `0b7928e4211f181fbfb9d0033945d3e108df9e4bb7a1a509c5497314e3c4f1e5` | 2,284 |
| `specs/creature-rpg/wp33-daycare-and-breeding-session.md`（WP33 v2 复审回填 Reviewed（限定静态范围，管理性）；被审 v2 `6cb65468` 保留历史） | `8c678e33` | `8c678e337d26354583bca17ffc7bdca8246f0d9ef8547de22102d0b99159cc89` | 25,144 |
| `specs/pokemon-rules/wp34-inheritance-and-offspring.md`（WP34 闭合复审回填 Reviewed（限定静态范围，管理性）；被审 v3 `d0113d76` 保留历史；WP39 轮 WP33 依赖行同步） | `46acc90f` | `46acc90ff175919b2e30ed2c990b3c604316c7c1493c37eef1ff594cd242e6fb` | 30,716 |
| `specs/creature-rpg/wp35-eggs-and-hatching.md`（WP35 v2 复审回填 Reviewed（限定静态范围，管理性）；被审 v2 `0abe2622` 保留历史；引用 WP34 回填后哈希（WP39 轮同步）；WP59 轮 BATCH-C02 头部引用同步） | `34f1a5df` | `34f1a5df24de90bd823f112a8e9b9f7d54e10aba9986e0747ac26c597bd50716` | 24,610 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-response.md`（WP28/WP29 回填回应） | `64a8884e` | `64a8884ec9338f527d2eab58e5e38aef118c6f9342c22193517e2c559a1fce55` | 4,445 |
| `review/wp33-wp35-delivery-2026-09-27/delivery-summary.md`（本批交付摘要；v4 注记后） | `6b1d9a1a` | `6b1d9a1abf0d97193065ddb479a0a19a280ec4d7bfd5094ff0ea12354fef522b` | 9,924 |
| `review/wp33-wp35-delivery-2026-09-27/self-checks.json`（逐包自检） | `581b530f` | `581b530ff7cc1ddf248dc0218efcc85c0f30f93ac00224c36a5256f60fabc5b7` | 6,876 |
| `review/wp33-wp35-delivery-2026-09-27/boundary-checks.json`（批末交界；JSON 引号修复后；修复前 `7bf8c59e`/2,875） | `80dcc8aa` | `80dcc8aa76f9a96962ef401fba5a16a852ba9987a4388dc765af2b1efa0adeda` | 2,877 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/wp28-backfill.diff` | `6d91006f` | `6d91006fe1df046e6ff80449d6f5ceda801ad1411ab2c0b3ed4460e8864ef0c0` | 3,950 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/wp29-backfill.diff` | `31d7a17f` | `31d7a17f86e46b6f182eb857fadd47206584d58f615e28f3544964a845dcb0ed` | 3,213 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/feature-matrix.diff` | `e934aaf7` | `e934aaf7bd6dab6a352f62ffe36e81715f723dbf42336bcb44867bccf19d50dd` | 9,482 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/delivery-summary.diff` | `7c181906` | `7c1819067a1781e49847553f031780e7f140dd78146792795f8a017547ad81e1` | 2,336 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/wp18-refsync.diff` | `a087b982` | `a087b982530a191ee0398d83bc168f30be45fe9c9b86da045d4fc6de2bf15bef` | 1,373 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/wp19-refsync.diff` | `5d643010` | `5d6430108358565fe7747079f11e231f93fcfcd861c0779a464480f599f7a8f3` | 1,278 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/wp20-refsync.diff` | `56327851` | `56327851b276aec966494faa3634bf89cda8d4b9fce7aa052ff90908133340bf` | 1,320 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/wp27-refsync.diff` | `12fcd499` | `12fcd499ad39288b6f00efe275a7d624b908358282edd96e4f3d2bc5a81383c5` | 1,265 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/wp30-refsync.diff` | `0e8df139` | `0e8df13967069ad899ab9618734abfaae4a9f0a8d42b50dd81b76bf34b09fc11` | 1,249 |
| `review/wp33-wp35-delivery-2026-09-27/backfill-diffs/wp31-refsync.diff` | `bc5c732d` | `bc5c732d1bddc1b84ce0353b791015736cc2b164ed27d2e23c94454f5aaa8d98` | 2,175 |
| `review/wp33-wp35-review-2026-09-27/report.md` | `7f61f821` | `7f61f821d8c40fad05ea37b6a3417cf5df7fffd8b04c7acc3c6041024def611f` | 19,379 |
| `review/wp33-wp35-review-2026-09-27/revision-prompt.md` | `2ad9d012` | `2ad9d0128a2c2101f7ae9c3fa75faaa438bbad6755eb91d5af8a8c3ae8bac57f` | 11,396 |
| `review/wp33-wp35-review-2026-09-27/input-manifest.json` | `6b6eb0c7` | `6b6eb0c70ec89efa67366c90bad03c357d075392d5233b73329ebcfc8b9581a6` | 171,550 |
| `review/wp33-wp35-review-2026-09-27/current-hashes.tsv` | `9c185e24` | `9c185e248b7bc586459b0e5548523d7d20f68963a26e9096de2724b9e455e94d` | 35,486 |
| `review/wp33-wp35-review-2026-09-27/changes-from-previous.diff` | `dffcb2a4` | `dffcb2a40efb7145e594c1338315e06520b040cc6b99c9f8cb9770941485354d` | 85,787 |
| `review/wp33-wp35-review-2026-09-27/diff-checks.json` | `000a6b4e` | `000a6b4e9dfd8cc61f135f9716a26834535795a23ef894bb11977b437b7c0123` | 3,369 |
| `review/wp33-wp35-review-2026-09-27/source-checks.json` | `2a668d92` | `2a668d92dd1b9b98e03db1651c75f705d4c84ae7bf943a34bf51f1672babc968` | 4,678 |
| `review/wp33-wp35-review-2026-09-27/text-checks.json` | `e8fb1241` | `e8fb124101fffecdaf32e588ab3e29ee0385eb5f1dfa8afe8a83d750dc2185d2` | 4,696 |
| `review/wp33-wp35-review-2026-09-27/static-vectors.json` | `10462140` | `1046214003fbdcded3702ccc4e06509f41a03fecf5004eedff86cd4fb7f727f4` | 3,852 |
| `review/wp33-wp35-review-2026-09-27/static-checks.json` | `7ea3dafe` | `7ea3dafe952dd9dd05edf26f82a3ba05cfd9e9e9497fd7edb173ec4f23834f24` | 1,453 |
| `review/wp33-wp35-review-2026-09-27/final-checks.json` | `53059859` | `5305985967a6dfc1674579a9a1b4e6546e798db2906a60fcf7f935616ee15373` | 2,624 |
| `review/wp33-wp35-review-2026-09-27/revision-response.md`（提取侧回应） | `74a9a812` | `74a9a812e95feba7ed44b1f9f1101bddc59a1a95c8fd3ea971bf132226894051` | 13,495 |
| `review/wp33-wp35-review-2026-09-27/revision-diffs/wp33-daycare-and-breeding-session.diff` | `cb3f73bc` | `cb3f73bcb3c36dae57ac1d10891873f7e604296ddff20b25a9a3792fbd4dd7d3` | 18,932 |
| `review/wp33-wp35-review-2026-09-27/revision-diffs/wp34-inheritance-and-offspring.diff` | `58ea7025` | `58ea702518eb0b3af65c32e8fdb70e9b0efc91f6dc4e9375d5adc902f69b407c` | 28,831 |
| `review/wp33-wp35-review-2026-09-27/revision-diffs/wp35-eggs-and-hatching.diff` | `ab745492` | `ab7454924fd93407508db566562108a76deb5771fd55d4314915317206662417` | 22,452 |
| `review/wp33-wp35-review-2026-09-27/revision-diffs/feature-matrix.diff` | `d134a2e5` | `d134a2e5508ee2073f1f4a385f76c42cfa0af8aac13e066d8e707020e6de56c6` | 4,771 |
| `review/wp33-wp35-review-2026-09-27/revision-diffs/delivery-summary.diff` | `c0531217` | `c05312176b0a1d3521722862340f8b3e64406f23fc344a10be94aca2d3b60480` | 7,350 |
| `review/wp33-wp35-review-2026-09-27/revision-diffs/boundary-checks-fix.diff` | `a81c596f` | `a81c596f6628cc711417bfa41a33895159757c7c0c1e6ee108983b2dcf47ef8e` | 1,414 |
| `review/wp33-wp35-recheck-2026-09-27/report.md` | `6314bd64` | `6314bd648edacaa8f898f1522dd33f8ef782df7586e09b136ac4d97b7a4380f0` | 13,517 |
| `review/wp33-wp35-recheck-2026-09-27/revision-prompt.md` | `d8379990` | `d83799909f9c0f98876ac41f60785ac72a4013f8c5df4a134da5c51d64a8ab90` | 8,009 |
| `review/wp33-wp35-recheck-2026-09-27/input-manifest.json` | `50bb62ce` | `50bb62ce8767cb31364b751deea29d0b801943678812c62bb278e7d4bb95d6ce` | 225,008 |
| `review/wp33-wp35-recheck-2026-09-27/current-hashes.tsv` | `4b679142` | `4b679142675b26c8d4efad93333e6eb196f2723f2aab4327cf46d1512b6d0ea2` | 37,903 |
| `review/wp33-wp35-recheck-2026-09-27/changes-from-v1.diff` | `8bc81194` | `8bc81194f7950ebe421ea55e2863bdbd9db8de2a87d3d1fc80b06d4aa69fee45` | 124,136 |
| `review/wp33-wp35-recheck-2026-09-27/diff-checks.json` | `26d7ae23` | `26d7ae2325a810cde5227518a683f8a3b81105d27c37360981099a17428d5fb1` | 2,801 |
| `review/wp33-wp35-recheck-2026-09-27/source-checks.json` | `ae655643` | `ae6556431f3913690e0772e3acf9dec02d18a36711d06ed090aadb541a698a80` | 6,634 |
| `review/wp33-wp35-recheck-2026-09-27/text-checks.json` | `1ec44429` | `1ec44429770bed4942359792160213dff34e05b9bd3c8565b4734bb4d0d62c38` | 4,351 |
| `review/wp33-wp35-recheck-2026-09-27/static-vectors.json` | `fb2acc6e` | `fb2acc6e9e894f20dcc29091f2903db79915a54a62475363bcee0c7c9c06bff2` | 3,086 |
| `review/wp33-wp35-recheck-2026-09-27/static-checks.json` | `9f26a12f` | `9f26a12f51c4b1119fc665b05dbdfb128e5b9bab58eca0a387c0ae13daff8ee0` | 1,075 |
| `review/wp33-wp35-recheck-2026-09-27/final-checks.json` | `f2087c59` | `f2087c592018d2758228325f40047f77dd595474ab26ef3c49e77fd873ab8cd0` | 2,640 |
| `review/wp33-wp35-recheck-2026-09-27/revision-response.md`（提取侧回应 v3） | `0188ef21` | `0188ef210477b3b864725dac9fb7d9fd2d663adcfb8d5c66571f5e3761533335` | 7,329 |
| `review/wp33-wp35-recheck-2026-09-27/revision-diffs/wp33-daycare-and-breeding-session.diff` | `7c957def` | `7c957defc3da5c8edbc345a5b4e835432fff6c52653baf39f5ad6f562d4002ca` | 7,713 |
| `review/wp33-wp35-recheck-2026-09-27/revision-diffs/wp34-inheritance-and-offspring.diff` | `422f4446` | `422f444696523f35cb7c5e493105fe66b2eb95ccf4fe271f3d34fe3d1f843b8c` | 12,137 |
| `review/wp33-wp35-recheck-2026-09-27/revision-diffs/wp35-eggs-and-hatching.diff` | `6b739e7f` | `6b739e7f39bb814f747acc1ee472e8dd94cbdfad421dc074cab1c7cb82c58cc4` | 5,481 |
| `review/wp33-wp35-recheck-2026-09-27/revision-diffs/feature-matrix.diff` | `46131c4f` | `46131c4f46a605c99ad81261f84d3c418fc03f9fd9ffc4ed7ebe39873aae4ba4` | 4,878 |
| `review/wp33-wp35-recheck-2026-09-27/revision-diffs/delivery-summary.diff` | `82e5042e` | `82e5042e94aba8a34554af2bbb82cf271633a885272ab96dd1ce114ee8d56ba4` | 9,027 |
| `review/wp33-wp35-closure-review-2026-09-27/report.md` | `90c20faf` | `90c20faf02009ead5893c052bb64d9d260eb6562ec3d805a653032929fb06b5e` | 10,068 |
| `review/wp33-wp35-closure-review-2026-09-27/next-batch-prompt.md` | `f791c8c2` | `f791c8c24800bdd12b43b9a8395a0a24ac399fdbc0c339a911e6fb6d00238f26` | 15,325 |
| `review/wp33-wp35-closure-review-2026-09-27/input-manifest.json` | `3237361a` | `3237361aff6e4ecda14d29eaeeb9d65e0823c0f08ad91671312705c4da38958e` | 240,408 |
| `review/wp33-wp35-closure-review-2026-09-27/current-hashes.tsv` | `1927c42f` | `1927c42f72e3cf86544b49bc98c45a92149d26be09f850cf9d4d4aef24cc471f` | 40,152 |
| `review/wp33-wp35-closure-review-2026-09-27/changes-from-v2.diff` | `3055c640` | `3055c6402be783edc4c25d029c91bff93cef464d06cd4717270a4dbdb5155d22` | 80,015 |
| `review/wp33-wp35-closure-review-2026-09-27/diff-checks.json` | `e3234e44` | `e3234e443edae9d20ecff77d042daa34aa7db8d2fa257d3c3a37181df27e888a` | 1,914 |
| `review/wp33-wp35-closure-review-2026-09-27/source-checks.json` | `3e3e2d3a` | `3e3e2d3abffa798be7c443e6303965bd65430d0f6044ea5efb279139464a101b` | 4,734 |
| `review/wp33-wp35-closure-review-2026-09-27/text-checks.json` | `625f9f0d` | `625f9f0d10fc43e4ecbc50df3a65d15ccfb1beaebfa1528d24a25e9fa00140f2` | 3,657 |
| `review/wp33-wp35-closure-review-2026-09-27/static-checks.json` | `1bc05662` | `1bc056620baba8926c147a37de8a728b54c1185af5ff64cc39c2bad5990fd9fb` | 1,129 |
| `review/wp33-wp35-closure-review-2026-09-27/final-checks.json` | `f324cb58` | `f324cb58f8296edb8efa3ba90b5d0805bfadeeb3ddbed16928b329af56650a12` | 3,030 |
| `specs/overworld/wp59-world-time-weather-field-moves.md`（WP59 闭合回填 Reviewed（限定静态范围，管理性）；被审 v3 `9a41d185` 保留历史；含 C04 记法） | `46e80106` | `46e8010658029a4338a1abc23dd9191ae0cb91f9f05dd0f3815eb0c4318b4094` | 42,401 |
| `specs/creature-rpg/wp36-wild-encounters-and-modifiers.md`（WP36 闭合回填 Reviewed（限定静态范围，管理性）；被审 v3 `d21edcc7` 保留历史；引用 WP59 回填后哈希；含 C04 拆分） | `5a05aad7` | `5a05aad72cec624397912038f3fb2f7df920eac220b2e55cbe9ee583c161ac33` | 34,305 |
| `specs/pokemon-rules/wp60-berry-plants.md`（WP60 树果闭合回填 Reviewed（限定静态范围，管理性）；被审 v3 `114c432b` 保留历史；引用 WP59/WP36 回填后哈希） | `1d588f0a` | `1d588f0aabd538f711cf47fa5ce66197da59f1a1a72e036b8a8c314c764516e1` | 25,082 |
| `specs/overworld/wp60-fishing.md`（WP60 钓鱼闭合回填 Reviewed（限定静态范围，管理性）；被审 v3 `5f274a2c` 保留历史；引用 WP59/WP36 回填后哈希） | `e5d94e05` | `e5d94e0512c481f1d10d222d148ddd6bdac6097b9eef0aaa847f4bf0734a0e3e` | 20,950 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/backfill-response.md` | `8ab43cb9` | `8ab43cb90b0ea042e5d62b0d2dd89a0758d132ec39b507cb61299c3fe6ebe1d5` | 3,778 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/delivery-summary.md`（本批交付摘要 v4；闭合回填轮） | `6d74f799` | `6d74f7995b19673ebb9d3d32ad441d5411810a3e9630e54b50a220022fc75b0d` | 12,913 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/self-checks.json`（逐包自检 v3；v2 复审收尾轮同步） | `3bad9fd6` | `3bad9fd6130ed99da468700a889097969c10c49f0ad23175a9e8515a30068afe` | 12,955 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/boundary-checks.json`（批末交界 v3；v2 复审收尾轮同步） | `db51d641` | `db51d64120200af5674c4f49f6dbb5b289f1d8afa06c606f59b2758730ad4f21` | 6,903 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/backfill-diffs/wp34-backfill.diff` | `bd3147f3` | `bd3147f3ca45d3c5163d0cbb4a4f31c3244e2b830f4a873c6f3b04c1ff93841e` | 4,100 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/backfill-diffs/wp35-refsync.diff` | `256ee71b` | `256ee71b6dbfa92c0e95cf75ee1c4a71c1f887c834e2d677b166ba808d4f2e06` | 3,974 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/backfill-diffs/feature-matrix.diff`（含回填与新批两段） | `705f7b12` | `705f7b12854f857cd163163cd3ea9eb71780aa5957ecdbdaf12567f5a2c31973` | 8,676 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/backfill-diffs/delivery-summary.diff`（旧批 v3→v4） | `233b9a82` | `233b9a82e3c22090055d05f8789df76ab8763968c362d548fc2e2f3413641fd6` | 4,835 |
| `review/wp59-wp36-wp60-review-2026-09-27/report.md`（本批首审报告） | `e9750d3b` | `e9750d3bee8738210506b5bcb12d559fdb33bbcfb0493773d4f71645667ebcdd` | 26,473 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-prompt.md`（首审有限修订提示） | `53a04e9a` | `53a04e9ae417221a90f1de163485d6367d924525f3b9a0f7b6412ffc4b58fd35` | 15,388 |
| `review/wp59-wp36-wp60-review-2026-09-27/input-manifest.json`（首审固定输入清单） | `107344a3` | `107344a3dbe83b8cafb9760572e1ccc4bb5cbc4e63545149671cff401187a199` | 261,860 |
| `review/wp59-wp36-wp60-review-2026-09-27/current-hashes.tsv`（首审固定哈希表） | `9b5cf066` | `9b5cf066ceb146a0cb68adaf9c006014384f08273daa2bad6254375e67c97d38` | 43,062 |
| `review/wp59-wp36-wp60-review-2026-09-27/changes-from-previous.diff` | `5f49b5f0` | `5f49b5f0e866f2841e52f0abe4297723b92406282656883ca010cd042dd7914e` | 65,557 |
| `review/wp59-wp36-wp60-review-2026-09-27/diff-checks.json` | `98382725` | `98382725908e1a86c4d46dbcd7d73cff2c1dbafb8a1cb98014ae74618dd1ca04` | 1,518 |
| `review/wp59-wp36-wp60-review-2026-09-27/source-checks.json` | `8e8768a5` | `8e8768a5546865a89967ea0e7db8710b3a3a9272e817ac56aa2088d08224ed52` | 10,604 |
| `review/wp59-wp36-wp60-review-2026-09-27/text-checks.json` | `c7b94931` | `c7b94931b50544c3d263abc748f5546c7c8f67342f0218530c598b70603b8f74` | 5,260 |
| `review/wp59-wp36-wp60-review-2026-09-27/static-checks.json` | `e3856769` | `e385676973231eced3d194c42420e44d77e9d1899afd0a1145ad37b12845131d` | 4,006 |
| `review/wp59-wp36-wp60-review-2026-09-27/static-vectors.json` | `95a14015` | `95a140151f713d6f14d34c7364011a5b7fec991b77ccfc76b0ecf8c1b9b039b7` | 2,694 |
| `review/wp59-wp36-wp60-review-2026-09-27/final-checks.json` | `0fd44a56` | `0fd44a56ef241ecbde9610bfd1f94aaca62eefe48d718c87ab888abe323bde9d` | 2,812 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-response.md`（提取侧修订回应，13 项＋C01/C02） | `97c5be51` | `97c5be51c60e931914b70fb6a52013dbe0a4099013f9a0d25cc7ad0d705d3ac4` | 19,116 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-diffs/wp59-revision.diff` | `a7c2a109` | `a7c2a109b786ea5d2e4854107f28eb10aea0dd4f048b8ba3defe4875526e3e57` | 40,349 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-diffs/wp36-revision.diff` | `1f9a2df4` | `1f9a2df4fb40625ae32130d3346889079f7b09e3a51494bd59c583b65dc11a74` | 32,313 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-diffs/wp60-berry-revision.diff` | `4a34f1c6` | `4a34f1c646f4c9d710c0acf0173c7a2947c37aa39183d911aa8d09e76503cabe` | 22,668 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-diffs/wp60-fishing-revision.diff` | `0c8f94ce` | `0c8f94cebcd32c53040ecb00ec2d4cd7d056a07adae89f53214bea183f68e0ef` | 22,709 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-diffs/wp35-refsync.diff` | `5b0aeac7` | `5b0aeac75af503b2d04a7534fce50ee8b57c85c2a5acdc11491209150ad0e88b` | 2,798 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-diffs/feature-matrix.diff` | `ffc170bd` | `ffc170bd05e06376d47779ed1aebee7167813e0dd174eb6b4be077ff30fb5889` | 8,999 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-diffs/delivery-summary.diff` | `5ec19ea2` | `5ec19ea2759401313e6d44efa74d0e0f5b3e37f48660d27dd47ff6353e58ec67` | 14,173 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-diffs/self-checks.diff` | `9214e3df` | `9214e3df5b3d84474f817f0edfcc252f7391f5c06582f2a2e15d681c9cd7bf1a` | 15,242 |
| `review/wp59-wp36-wp60-review-2026-09-27/revision-diffs/boundary-checks.diff` | `3f7e50a9` | `3f7e50a93199d25402c0fc2ceae9efcb7d30c5ced4dabd2405929766fcc75e57` | 9,692 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/report.md`（v2 复审报告） | `173ac1dc` | `173ac1dc5e5ff3db1297f3d302d7ab8de570c0db8b256b1cc7731439c86b78a9` | 16,199 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-prompt.md`（定点收尾提示） | `16953dad` | `16953dad7b46279b4ca38c9194ea635b69ddaf69daf07a89e8d6ebc8d32ed7d5` | 9,341 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/input-manifest.json`（v2 复审固定输入清单） | `10caf81c` | `10caf81cefb37b43bc69b4dd0083d1804b9fe643bd90a0a657a03ed3259b6bbe` | 303,602 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/current-hashes.tsv`（v2 复审固定哈希表） | `b6e90fa6` | `b6e90fa619476504d2ac70dbc299523ad63790def5af97b5ead0986b7af7fa48` | 45,927 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/changes-from-v1.diff` | `65424c5f` | `65424c5f13748406566e20b03eda6c0650d7bca179ad59ae24f944fc2cbbc8ab` | 219,064 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/diff-checks.json` | `e88a2e14` | `e88a2e14773e6de4900bb5cc0dcaacaff91677a4bae5d205e064c4413a336452` | 3,030 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/source-checks.json` | `033969e2` | `033969e265aecae9b0a6a4f60c767343d65c9456227ef2f626e401f76ac36f40` | 13,983 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/text-checks.json` | `24a1cca8` | `24a1cca850fb85c1cc06a2064d6d81f59ddd42f75b3defd9b7cec7c39b8dae5b` | 16,139 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/static-checks.json` | `fdeb230e` | `fdeb230ea0065b065939876a9fd1c1e5d3b9820d9606e3cea79d087054898e97` | 1,234 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/static-vectors.json` | `a66ea406` | `a66ea40677efeb080d0167ffaea53fe9f8288561d57eba37a46d37c77fc39b7b` | 2,292 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/final-checks.json` | `d3984c28` | `d3984c28ccb6309e73fdb299c917cae6cdd9b1e0ca3db6029bd3f89e42a9bbad` | 2,947 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-response.md`（提取侧收尾回应，四编号＋C01/C03） | `233fd124` | `233fd124879bb3c421b81eec64e85e73e7dc4bf8934181e819ac9f759324b10f` | 13,082 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-diffs/wp59-revision.diff` | `8c772de5` | `8c772de51269dfc6aa9a5b6221afe01977d71a8e3e3f15f87515e84a2861520d` | 12,913 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-diffs/wp36-revision.diff` | `9a109faa` | `9a109faae06be87de045d7b875893582937753f98fd300ca0e179d6b4bd33031` | 6,904 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-diffs/wp60-berry-revision.diff` | `783880a4` | `783880a4f664a3dcc7201fd4e41579c6aa8f9bc67b14c1242fcf07cfab751c0c` | 6,114 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-diffs/wp60-fishing-revision.diff` | `faded8c8` | `faded8c87a2801aafb550a1fcd2f39e9bee891fd97ac48f4b0cf8d7e7a59cc09` | 6,420 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-diffs/feature-matrix.diff` | `8810fb3e` | `8810fb3e4fe80f544368bb2b28a499519ba4dd5f8396b8ab57f5b045b0fee1fd` | 9,355 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-diffs/delivery-summary.diff` | `8fe7889c` | `8fe7889cfac974601ad507919df6eef8ca49b5e4127cbc9327a4b6176c3916a4` | 12,704 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-diffs/self-checks.diff` | `ae9e21ca` | `ae9e21ca572c78cd01c7dbbf34525caee6ea5a4607112382373f182bf0b857be` | 8,396 |
| `review/wp59-wp36-wp60-recheck-2026-09-27/revision-diffs/boundary-checks.diff` | `f35089b1` | `f35089b131b55d0510231f314402a57ab3f060aeca4ca4687f8bfa120dd62d03` | 8,751 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/report.md`（闭合复审报告） | `25835002` | `258350026084def02d36649c67709414307774600a94b88f8d28b0e5ac5779d1` | 12,741 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/next-batch-prompt.md`（回填与下一批提示） | `11123b46` | `11123b4610037689461527b439e0719b50057e6236f4daf31f82c0864a3cb1a2` | 17,658 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/input-manifest.json`（固定输入清单） | `c5adfb3a` | `c5adfb3aa3682abb40e7a4a7fb3c3a0350258a3efabd1b46b198eff3c71e84b3` | 322,718 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/current-hashes.tsv`（固定哈希表） | `dbcf5d35` | `dbcf5d350ba893ecd810c98aa9c18cada1188561fcb23bcd7e03ae4cf7ddb252` | 48,668 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/changes-from-v2.diff` | `440026e6` | `440026e623aa557fe4f98523921737e8b46bcab6bada7034514fc8d6ddc08fb6` | 127,829 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/diff-checks.json` | `ac7af1c5` | `ac7af1c57c876381505037876dabef2eabd34fa9663c3823bdd8d8e073680a14` | 2,827 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/source-checks.json` | `c6a3464e` | `c6a3464ecedb420f069c41561ac0d57060c68b7599b2bb733fa2d80c251cb8b8` | 11,481 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/text-checks.json` | `fba7812f` | `fba7812f6c566a19e4a5baa87dae5b191c4dbd4d71423c93ec9a3842538ffe39` | 16,606 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/static-checks.json` | `a419ceee` | `a419ceeead3b5d79ac0afdf804f8c3a388f35e679c0d73c0e430ed15951b3db6` | 2,585 |
| `review/wp59-wp36-wp60-closure-review-2026-09-27/final-checks.json` | `663d7d07` | `663d7d0749b13912693a742a8c5f0acdfc29b610a969b147c5abeca6307229bd` | 3,032 |
| `specs/combat/wp39-battle-context-and-participants.md`（WP39已限定通过，管理性回填后；被审v3留史） | `9a3a796f` | `9a3a796f08335bc7d4886c7e2b11f3b273c955e24ba9d6fe966c60103df5719b` | 42,697 |
| `specs/combat/wp40-commands-obedience-and-action-order.md`（限定Reviewed；本轮独立批准三摘要更正后） | `8c80e5f3` | `8c80e5f3f4c3d6ad151bfa65c8a4fce5691adafb318b14565f89f929b24acbe8` | 43,769 |
| `specs/combat/wp41-switching-positioning-and-escape.md`（限定Reviewed；本轮独立批准三摘要更正后） | `a5232a1e` | `a5232a1ed18dc24257748c34b2ec83eca9730e2c8ef077c7be638ff3b4d38036` | 33,281 |
| `review/wp39-wp41-delivery-2026-09-27/backfill-response.md`（闭合回填回应） | `57e53a70` | `57e53a706c9d3a111d154c3dbd280dd9c25806c4c31327b33ebeea70a062123c` | 5,577 |
| `review/wp39-wp41-delivery-2026-09-27/delivery-summary.md`（旧批摘要v4，闭合回填） | `a1df7ee3` | `a1df7ee38a71874e5ab14586a7dc4551e8bfdbfda7a0182a8ba4467a1ed16b20` | 12,006 |
| `review/wp39-wp41-delivery-2026-09-27/self-checks.json`（逐包自检 v3；三项收尾＋C03 同步） | `6d16628f` | `6d16628fb0c8b2819c6a83aa792785849ce839d8ce95a695121ffd2d18b6a8ea` | 23,048 |
| `review/wp39-wp41-delivery-2026-09-27/boundary-checks.json`（批末交界 v3；三项收尾＋C03 同步） | `46a58b20` | `46a58b20347ce9089cec89497d046a2270fc28eb9599f052b66ed4f03bd949d0` | 6,926 |
| `review/wp39-wp41-delivery-2026-09-27/backfill-diffs/wp59-backfill.diff` | `c4fc5304` | `c4fc5304602b0d51d6151fd2bddf214efc47ec713700923f28936afc667b6e7c` | 7,757 |
| `review/wp39-wp41-delivery-2026-09-27/backfill-diffs/wp36-backfill.diff` | `f05b2142` | `f05b2142e465e86a5e725b2fc2f0c4f443d2f7a26bfba6f9abb95c281c100610` | 8,195 |
| `review/wp39-wp41-delivery-2026-09-27/backfill-diffs/wp60-berry-refsync.diff` | `7ba1fe2b` | `7ba1fe2b4c08f46f2ae4eb9a295e424de50438ffd1a3b9db0b17997ae07045d9` | 5,273 |
| `review/wp39-wp41-delivery-2026-09-27/backfill-diffs/wp60-fishing-refsync.diff` | `3686a0df` | `3686a0dfe5eee850b86c580cfd44bb4b5e51320e2265d5313ce2520c473fe63f` | 5,133 |
| `review/wp39-wp41-delivery-2026-09-27/backfill-diffs/feature-matrix.diff`（含回填与 WP39–WP41 两段） | `db2edf64` | `db2edf641ee572098520f9e5d8e8e2b2ce6f12a16f634f01588bea9c852b37e3` | 13,983 |
| `review/wp39-wp41-delivery-2026-09-27/backfill-diffs/wp34-refsync.diff` | `44d578ae` | `44d578aeb4dc9c6e10888cd4637965259832135d68bab20d99ec68add26a74e3` | 3,042 |
| `review/wp39-wp41-delivery-2026-09-27/backfill-diffs/wp35-refsync.diff` | `a82eab1f` | `a82eab1fa990e45873d1245578997175324081597d0ed8752fa59983d98d6083` | 4,925 |
| `review/wp39-wp41-delivery-2026-09-27/backfill-diffs/delivery-summary.diff`（旧批 v3→v4） | `21e5baf6` | `21e5baf66510ff97f02fa9f019da72c8762e4683095c834ed2738f6837e2a7ac` | 2,356 |
| `review/wp39-wp41-review-2026-09-27/report.md`（首审报告） | `a539db6c` | `a539db6cd901b92fa4f0c723ba612d44a1c7e5349a26c28e9632713e38a95d79` | 23,770 |
| `review/wp39-wp41-review-2026-09-27/revision-prompt.md`（有限修订提示） | `543b6f14` | `543b6f147330689aba6b72a8d6e2e5cbbf6c8d32de2f59e80dcd57856d65dfba` | 14,362 |
| `review/wp39-wp41-review-2026-09-27/input-manifest.json`（固定输入清单） | `1097ecef` | `1097ecefcb0415ef1526893cbc4c1e5ecab7ff63c22313c7dae648fc1fdb03cc` | 347,393 |
| `review/wp39-wp41-review-2026-09-27/current-hashes.tsv`（固定哈希表） | `a28ff15c` | `a28ff15c8780c6f2f3597694bcf5f06ebe1a8b1862853d570d431dc28b8025c2` | 52,075 |
| `review/wp39-wp41-review-2026-09-27/changes-from-previous.diff` | `8586d6c9` | `8586d6c97ebf76925c927f63b5e5edd6899997ada9d15e025d55704b429f28d5` | 108,594 |
| `review/wp39-wp41-review-2026-09-27/diff-checks.json` | `af74fd80` | `af74fd8064fd8c539ffb4324c3d16b43cc41d6a144b8654dfa31f118a78f0039` | 2,688 |
| `review/wp39-wp41-review-2026-09-27/source-checks.json` | `68b10ddf` | `68b10ddf07e23dee3276a720a7a7c5011f5fce5b46728a390020be8b71a007cb` | 8,619 |
| `review/wp39-wp41-review-2026-09-27/text-checks.json` | `573923fc` | `573923fc5953244bef26ce32b730a3953b233e6f84e36189f223ed56f12f1442` | 13,835 |
| `review/wp39-wp41-review-2026-09-27/static-checks.json` | `70112c38` | `70112c3857f4ebc4e6acf3631ad41ee56161ebbddbbe6f75166489991da5bbf0` | 764 |
| `review/wp39-wp41-review-2026-09-27/static-vectors.json` | `172925ac` | `172925acc7cae93ac0026b9db6fe4ec125c491806d7ffc74483628870d38a93b` | 3,197 |
| `review/wp39-wp41-review-2026-09-27/final-checks.json` | `bedab5f5` | `bedab5f5528550c05950952f8dd869bf250d433208106d595c130224c1cda5a2` | 2,834 |
| `review/wp39-wp41-review-2026-09-27/revision-response.md`（提取侧首审回应，12 项＋C01/C02） | `eec9fbc2` | `eec9fbc27c020eeed8c5e3cbbeca15f03554fb22d313f3ead3b7cca618babcad` | 17,055 |
| `review/wp39-wp41-review-2026-09-27/revision-diffs/wp39-revision.diff` | `dd473ba2` | `dd473ba253c4126466bc487c4bafb7e23bff6350c1b71b929fa48a5aa3bcd554` | 22,717 |
| `review/wp39-wp41-review-2026-09-27/revision-diffs/wp40-revision.diff` | `ae4631a4` | `ae4631a47d014ef574308b7528e785624f419ef92d5c83f5aad2352cae60db6a` | 24,903 |
| `review/wp39-wp41-review-2026-09-27/revision-diffs/wp41-revision.diff` | `7667dd09` | `7667dd09f4e07483fdb73cd808a202d50c12bf2b2881d4e88a2afc9fa50f3164` | 25,070 |
| `review/wp39-wp41-review-2026-09-27/revision-diffs/feature-matrix.diff` | `18eaa1ee` | `18eaa1eef5bc2a9e58030cb0c62bd66e4bdf6b79d33578b1cfe32aeab4fe4b4a` | 6,758 |
| `review/wp39-wp41-review-2026-09-27/revision-diffs/delivery-summary.diff` | `89f79943` | `89f79943cad7772e1cc67057b50b65f618b2291a3541577ecd4355b515042850` | 12,478 |
| `review/wp39-wp41-review-2026-09-27/revision-diffs/self-checks.diff` | `d3da9737` | `d3da973761193cfc2ba654758f4d7265077e4e980aaea9525655abd0c0feb8ca` | 15,697 |
| `review/wp39-wp41-review-2026-09-27/revision-diffs/boundary-checks.diff` | `7071b5d6` | `7071b5d6317a403464abef4b57536198d19b18b983f7e8e8b31c5f02914ed004` | 8,580 |
| `review/wp39-wp41-recheck-2026-09-27/changes-from-v1.diff` | `65714e4d` | `65714e4d32c22c2e926dffb5bbf6e6e523b1f616a31cdc40e38fcd68c216a635` | 160,079 |
| `review/wp39-wp41-recheck-2026-09-27/current-hashes.tsv`（reviewer 固定哈希表，原件保留） | `2aef1ad5` | `2aef1ad5f62c765ee473e60c6435266a96504a77e941b61a73ff67d9a7aa6d55` | 54,542 |
| `review/wp39-wp41-recheck-2026-09-27/diff-checks.json` | `dce9f40f` | `dce9f40f8a2c8acb1cd3574d01e0e5c91ef1f9a9eb78fe29983394c01f62dad3` | 2,429 |
| `review/wp39-wp41-recheck-2026-09-27/final-checks.json` | `c40d3918` | `c40d3918cbf66202f2f775bd81be85dbca7b79e4bc0187fd0c54e526de281b70` | 2,781 |
| `review/wp39-wp41-recheck-2026-09-27/input-manifest.json`（复审固定 408 项输入清单） | `43c25bb7` | `43c25bb7ec7f2c62387e3ab22bc683e387358ab1f9fafa4acd5be3e54036ae79` | 365,827 |
| `review/wp39-wp41-recheck-2026-09-27/report.md`（v2 有限复审报告；REQUEST_CHANGES，9/12 关闭） | `50a485f2` | `50a485f2eac388d188704b1b6e1aa7d63c8a4883e0c07b6067fa9ff880a75467` | 15,110 |
| `review/wp39-wp41-recheck-2026-09-27/revision-prompt.md`（三个剩余编号＋C03 的权威有限修订提示） | `dbcae65a` | `dbcae65a951fd598fb2dea1f15f79363b9bd05bf6dc510602de22e4d667b2d68` | 9,575 |
| `review/wp39-wp41-recheck-2026-09-27/source-checks.json` | `36212055` | `36212055e2a5c42bd4c5f1082d135e4019405354fdfca99a36398e6301095787` | 9,077 |
| `review/wp39-wp41-recheck-2026-09-27/static-checks.json` | `9f0f5655` | `9f0f56554e582d0916659c8b3e67ee68b1335777439ee3b475683917aacc79e0` | 3,515 |
| `review/wp39-wp41-recheck-2026-09-27/static-vectors.json` | `0b056dcc` | `0b056dcc8d92272edf80f405c8aa3eeb787426956544c5f65bcf0b5490598984` | 6,808 |
| `review/wp39-wp41-recheck-2026-09-27/text-checks.json` | `842fd221` | `842fd221124f58e3c4905ad4f58a0178bf464d4f45e9a53f4a1733fd368f4867` | 1,887 |
| `review/wp39-wp41-recheck-2026-09-27/revision-response.md`（提取侧 v3 收尾回应，三项＋C03＋直接传播） | `7fea838c` | `7fea838c46413d20afde7b2485bbe7855b6bc779e95a18b30fa4f49a46ade36a` | 15,187 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/wp39-revision.diff` | `23a5fb57` | `23a5fb57d6f7f43d2fa3fe087e479d0185e9bdf1f4f5f146cda3b1c648bcf445` | 20,031 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/wp40-revision.diff` | `56cf484f` | `56cf484f1a68b95a394b02c5614bbfbb57c1afd60fbf9644221781e29b7e1745` | 18,173 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/wp41-revision.diff` | `d92fe8e1` | `d92fe8e1360cff1003c8a9cfcef22472866a393b50ec389409339beee3c4e685` | 11,805 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/feature-matrix.diff` | `24113271` | `24113271408ca25006c18a3b4b2fd7e615847d33169b96499bd13f93c9999e83` | 7,059 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/self-checks.diff` | `b2f0c904` | `b2f0c90446ddae528d2ed4c8f5e129a4e75460509d349d184ff20555d0f843fc` | 21,014 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/boundary-checks.diff` | `e8b470e9` | `e8b470e999c710daae54092a8e952cb6a819a253747421ac6c7ed9213b0e20ea` | 10,364 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/delivery-summary.diff` | `c2e32a5f` | `c2e32a5fce83c85243af6b605a9bc051194493baf59a188145e904fe7e77090b` | 14,927 |
| `review/wp39-wp41-closure-review-2026-09-27/changes-from-v2.diff` | `7aa21498` | `7aa214983211a8306ca9857809ac46872b49d6dfbf8a0775ef84e583fde92b76` | 151,990 |
| `review/wp39-wp41-closure-review-2026-09-27/current-hashes.tsv`（闭合轮reviewer固定表，原件） | `7c29c823` | `7c29c8233381fb93cc7bfd4fbe8c1e45553d791b776cc5b202846f7a06d3fcf4` | 57,028 |
| `review/wp39-wp41-closure-review-2026-09-27/diff-checks.json` | `8d00e2d7` | `8d00e2d78ada908824aea60da06efcb67681f4cffe636dc6a91f34c5f060fe13` | 2,436 |
| `review/wp39-wp41-closure-review-2026-09-27/final-checks.json` | `72bfa0e0` | `72bfa0e07172880eb590e3859c063ea0bc42898277a603d70246c34e6ae15f5b` | 3,016 |
| `review/wp39-wp41-closure-review-2026-09-27/input-manifest.json`（闭合轮固定427项输入） | `fecd22b8` | `fecd22b8331094e3334b4cff6b4f57e36cc3a016b628b3a964d267db72892a5e` | 386,953 |
| `review/wp39-wp41-closure-review-2026-09-27/next-batch-prompt.md`（回填＋WP43→WP44→WP45执行提示） | `a712c0fb` | `a712c0fb9c3311bfbade32305cfb000827864d5bb985d07567022c1763f9ed35` | 16,208 |
| `review/wp39-wp41-closure-review-2026-09-27/report.md`（独立闭合报告；三包PASS_SCOPED、原12项及C03闭合） | `c88d91cf` | `c88d91cf0202e083294870896283fc10264860f608b8bad69ba46b9c622b7f07` | 11,892 |
| `review/wp39-wp41-closure-review-2026-09-27/source-checks.json` | `5f299ddf` | `5f299ddff993b5fefbef400a5be14767946a4163e3c9b26e9e0197df63be91ca` | 5,713 |
| `review/wp39-wp41-closure-review-2026-09-27/static-checks.json` | `2a0d7458` | `2a0d745888fa65b43df032b47da4761d8ee628ca9c5ede9868cfaca3d4e1807e` | 812 |
| `review/wp39-wp41-closure-review-2026-09-27/static-vectors.json` | `f13e2b6b` | `f13e2b6b55c9d3cd64c8fb47b3628373271034b201392f065ded656c95efc5ea` | 5,595 |
| `review/wp39-wp41-closure-review-2026-09-27/text-checks.json` | `677efc75` | `677efc753ab2a5cbeb971e4013e43d50c5d9a9bd37d573506863b3408a1e3994` | 7,518 |
| `specs/pokemon-rules/wp43-types-accuracy-and-damage.md`（限定通过后的身份级联；原行为保留） | `d8ba547b` | `d8ba547b3c1f8338f9f00fdac67c146ecd147942c94d576f77d27e4375cb905b` | 30,921 |
| `specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md`（限定通过后的身份级联；原行为保留） | `3d4d9c40` | `3d4d9c40d83746459df0c89353a046abd8d4ca32e82e2de76e0ab44499273d1e` | 50,426 |
| `specs/pokemon-rules/wp44-effect-coverage.md`（限定Reviewed；本轮关闭状态／完整身份维护） | `c226232d` | `c226232d523b899197590800b8e6f75230de103363eebf6c12a16111a24cb2ad` | 27,346 |
| `specs/combat/wp45-weather-terrain-side-and-position-effects.md`（限定通过后的身份级联；原行为保留） | `046e8bf0` | `046e8bf04fc663e41a6e48c3f9aaa193022d141fea39752eeb2db87a306bd597` | 36,525 |
| `review/wp43-wp45-delivery-2026-09-27/backfill-diffs/feature-matrix.diff` | `1617019c` | `1617019c19041bfe3ff09551871093ea5f30563560254fe3bffd88d716ddcf4a` | 9,702 |
| `review/wp43-wp45-delivery-2026-09-27/backfill-diffs/previous-delivery-summary.diff` | `83297d81` | `83297d8191544eed153f4a29567d49fa98851ee95c8224a96cafe98f838ffcdd` | 11,601 |
| `review/wp43-wp45-delivery-2026-09-27/backfill-diffs/wp39-backfill.diff` | `77966eba` | `77966eba98c81e8c8d0f00cf505cefcbdde69bfd02057436862e41d368e5f60d` | 5,818 |
| `review/wp43-wp45-delivery-2026-09-27/backfill-diffs/wp40-backfill.diff` | `f8e88efa` | `f8e88efaeb26180262d108e1a4f8bb0f6dc415653ff62c52aacaec732c402373` | 6,623 |
| `review/wp43-wp45-delivery-2026-09-27/backfill-diffs/wp41-backfill.diff` | `5ed55ae0` | `5ed55ae0a5e04f0650ce688c29968bd55f7308b9e38fa49eedc2037a05ff3b97` | 5,065 |
| `review/wp43-wp45-delivery-2026-09-27/backfill-response.md`（提取侧回填回应，六项＋TSV补检） | `3d9f3385` | `3d9f33857088e6000cc0a588b74897aeb000e91e0338ba12e50c7edf48d0978c` | 5,830 |
| `review/wp43-wp45-delivery-2026-09-27/boundary-checks.json`（v2；五组交界与十条受影响完整哈希绑定） | `21abfe14` | `21abfe14138ed5e2fcd5ba3d3f0b499d192326e970c4495a905fcafa0098ac4e` | 6,629 |
| `review/wp43-wp45-delivery-2026-09-27/delivery-summary.md`（v3；闭合后管理维护） | `4cc8e434` | `4cc8e434e1a7d1feca37dce2290626055fd41fbc8d3dc8215ddc1ef43960e35d` | 10,636 |
| `review/wp43-wp45-delivery-2026-09-27/self-checks.json`（v2；当前结论／向量更新，旧声明留史） | `307d1ff0` | `307d1ff0d54d9c1ddbcf8ee10f6161e6eff044cb5d486352b3acab643313004d` | 56,423 |
| `review/wp43-wp45-review-2026-09-27/changes-from-previous.diff` | `a52a7c5d` | `a52a7c5dff6900f7736beb3871711c6264c8104c39e4546ae9e312ed736bc2f5` | 92,005 |
| `review/wp43-wp45-review-2026-09-27/coverage-checks.json`（reviewer集合／内容覆盖检查） | `514dd2f6` | `514dd2f6e25081d6620473b0da2c032fa27fe4146d8cc89c5ad55dfcc38bcc3f` | 1,595 |
| `review/wp43-wp45-review-2026-09-27/current-hashes.tsv`（reviewer本轮固定哈希表，原件） | `1e719451` | `1e719451a324c430404aaf00674cc90e6ba5fb42bf3883e1e3ff8aff68d360f6` | 60,214 |
| `review/wp43-wp45-review-2026-09-27/diff-checks.json` | `b0f5b097` | `b0f5b0974db6d9498c9bb957fd0b52a7c178837c2c39842ed26849e3d60c4a74` | 1,776 |
| `review/wp43-wp45-review-2026-09-27/final-checks.json` | `cf138116` | `cf1381163898467a29621f9c5826df38ffbf1f698a41dbe6f105c5fe0b0dc1ed` | 3,188 |
| `review/wp43-wp45-review-2026-09-27/input-manifest.json`（固定451项输入清单） | `0a0cbb55` | `0a0cbb55accf032cc1bbabe1cad8a07b6584758228a9b2d6572776f02c16d436` | 409,730 |
| `review/wp43-wp45-review-2026-09-27/report.md`（首审报告；WP43 PASS_SCOPED，批次REQUEST_CHANGES） | `308acc64` | `308acc6467f730722d8cf59eec0b18173c91b9257d55da311ffab09432bf6ea1` | 15,538 |
| `review/wp43-wp45-review-2026-09-27/revision-prompt.md`（三项必修、N01、C01与WP43回填授权） | `adab1c0e` | `adab1c0e054f89988bf6069cd6bfdf5f25367568d52b9b0a04a8895065bf5148` | 11,454 |
| `review/wp43-wp45-review-2026-09-27/source-checks.json` | `a297eac2` | `a297eac27279acd076ae51d7a6537ac784be6f5e49aa2e0126cfc5f46231c496` | 16,001 |
| `review/wp43-wp45-review-2026-09-27/static-checks.json` | `8ab1329e` | `8ab1329e6f281209a9140a2a37496e805278253894b1e65baa70d26f5aec0e23` | 595 |
| `review/wp43-wp45-review-2026-09-27/static-vectors.json` | `a39f4efd` | `a39f4efd576eff2013b3bcd102bdbf40f4f1b6877ccc7e811846cec3223f650f` | 6,116 |
| `review/wp43-wp45-review-2026-09-27/text-checks.json` | `a3e71a5f` | `a3e71a5f9bd44930633877feca4114b728f9af290172cae17dd8b163dae2fc57` | 2,315 |
| `review/wp43-wp45-review-2026-09-27/revision-response.md`（提取侧有限修订回应；实际差异待复审） | `a114fc00` | `a114fc008cecdb26a1b3832662e2e3283ce38edffc81d058f6ceb1e3d545e173` | 16,324 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp40-n01.diff` | `8c01d8b9` | `8c01d8b98251ac7e85fcf48e9a354b7129855e94355a65df2df920385dcfec6f` | 7,407 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp41-reference-sync.diff` | `f231032c` | `f231032c94a6ddd90ffdd2c76e3c406b94da536d3ab6d38b723b379be2211dac` | 2,806 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp43-reviewed-backfill.diff` | `888681b4` | `888681b4087f9f4cebc75c71fc6b737b144f354c9e221ca82acc7e9e31dc6132` | 7,853 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp44-revision.diff` | `c01fc160` | `c01fc160de111374358d1b8aac71dcfcd178410da14f2192bb3fed7e984c55b2` | 30,434 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp44-effect-coverage.diff` | `634ac62a` | `634ac62a326307724db91374afafdd589da47e85fbdc5cd84d2590d6602d69ab` | 20,722 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/wp45-revision.diff` | `c7bfed74` | `c7bfed7488b3a3dfdadc8a59bc71cdf266f8a99d781c9fec5d09a0ae7d0978a9` | 14,233 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/feature-matrix.diff` | `c1dfb980` | `c1dfb980e895a9a883b4ae138121fad873edd217f795460cfd3207a3a1c0072e` | 5,015 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/self-checks.diff` | `8376bae0` | `8376bae01dde0c2c92e7dfaa31266164b9168d3fe1d81607b0b84cce9ef16bbf` | 29,928 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/boundary-checks.diff` | `b85e7836` | `b85e7836549f856b9301dc6da136cda92cba25cc2d546254a08bd51e1aa164c7` | 8,872 |
| `review/wp43-wp45-review-2026-09-27/revision-diffs/delivery-summary.diff` | `6aeb2ec6` | `6aeb2ec62d3fc62ecfba2055d48d05926363dbaea983dfb81e1252de237f4940` | 18,490 |

| `review/wp43-wp45-recheck-2026-09-27/changes-from-v1.diff`（本轮独立复审原件） | `0eeb78cd` | `0eeb78cd9c54a902080a060a3a208cb8a898fe1342eb5703e134a6024b926c51` | 207,622 |
| `review/wp43-wp45-recheck-2026-09-27/coverage-checks.json`（本轮独立复审原件） | `50d73923` | `50d73923df56b1ec9d52f228e22df8aaaca24714d527b955600cbce0585618f5` | 2,083 |
| `review/wp43-wp45-recheck-2026-09-27/current-hashes.tsv`（本轮独立复审原件） | `051ca1d1` | `051ca1d19baf7736469fa5142b527810d9a7bcd99f864c62c9f6ef0a6f0fefdc` | 63,249 |
| `review/wp43-wp45-recheck-2026-09-27/diff-checks.json`（本轮独立复审原件） | `2d674afd` | `2d674afdd076a1526d1f4346331751ed4e4811f4f14960f0a2cebc1057dc14b4` | 3,382 |
| `review/wp43-wp45-recheck-2026-09-27/final-checks.json`（本轮独立复审原件） | `a0527d63` | `a0527d639305894bdd478b39ddc1165848890b66c62773b9d447dfe9bde51664` | 3,330 |
| `review/wp43-wp45-recheck-2026-09-27/input-manifest.json`（本轮独立复审原件） | `58b5f76d` | `58b5f76d52a834121d63cd4426a12e0b1d373fb34ad3be6e1529b75fe227beb6` | 433,945 |
| `review/wp43-wp45-recheck-2026-09-27/next-batch-prompt.md`（本轮独立复审原件） | `a4dcb34f` | `a4dcb34ff159d1cf81d98f40f4c1f42d8edec44d851919b2a5e38c576566cfee` | 16,972 |
| `review/wp43-wp45-recheck-2026-09-27/report.md`（本轮独立复审原件） | `c88366bc` | `c88366bcb68beb81f40667ef46ec0b1016476763347491d3e6c693ce2961ccae` | 12,828 |
| `review/wp43-wp45-recheck-2026-09-27/source-checks.json`（本轮独立复审原件） | `a930e9ff` | `a930e9ff46b5a42f701ada57529ed0e95d5e643fb013ea32b1186d6a61533d2f` | 7,071 |
| `review/wp43-wp45-recheck-2026-09-27/static-checks.json`（本轮独立复审原件） | `992229b2` | `992229b28bb9a1e99a848dec684e761cbd76500bf1ebcd5dcf8b5d8d6cda487a` | 604 |
| `review/wp43-wp45-recheck-2026-09-27/static-vectors.json`（本轮独立复审原件） | `eb34d975` | `eb34d9750c68a4554ceebf19223682698d2090401fc9928e6d1d2d26042874fa` | 3,428 |
| `review/wp43-wp45-recheck-2026-09-27/text-checks.json`（本轮独立复审原件） | `1f4ceb0c` | `1f4ceb0c17996cda6e0d6169d84c24a39b4bb4cbcb5479395668e68bca4d4ef9` | 9,100 |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md`（限定通过后的身份级联；原行为保留） | `126e2612` | `126e2612e2776c41557475a98cd97b8ef40a0a7f02fd95f16c434de49855a3eb` | 41,759 |
| `specs/pokemon-rules/wp48-ability-calculation-modifiers.md`（限定通过后的身份级联；原行为保留） | `1c701d50` | `1c701d507747d95ba456f3df8a2697b0a1e409d1508dd2d8651b7d50d102403c` | 35,320 |
| `specs/combat/wp49-ability-phase-triggers.md`（限定通过后的身份级联；原行为保留） | `e41ca96d` | `e41ca96da9f15bc88526f31337aefe3ba767b9b19776ceba0a6472df1061253c` | 53,127 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-diffs/delivery-summary-prior.diff`（提取侧本轮交付） | `209eb9a8` | `209eb9a8b00b1a5ef4c5c6aa3f67f4abaedbe1ad40cfa1471787e9d21933a5f1` | 11,662 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-diffs/feature-matrix.diff`（提取侧本轮交付） | `4db120fb` | `4db120fb3fcf525efc95a2d8053fd0482b9d07900b53990834f8ed6becc9451c` | 8,564 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-diffs/wp40-commands-obedience-and-action-order.diff`（提取侧本轮交付） | `ff003ffd` | `ff003ffd07a87805f894fc9165ac117e3b5a4722d1b81199c79e79092430ba37` | 5,783 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-diffs/wp41-switching-positioning-and-escape.diff`（提取侧本轮交付） | `06ac72cf` | `06ac72cfe57304884a5b23b08f6dbee7f26bda6b9d9170e680a56bfcf7c4bb65` | 2,893 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-diffs/wp43-types-accuracy-and-damage.diff`（提取侧本轮交付） | `a290d3e4` | `a290d3e43147201497b54e1d9bb11c0c3251cc03a7f0a68a5258c815759926eb` | 8,260 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-diffs/wp44-effect-coverage.diff`（提取侧本轮交付） | `c2ffc95a` | `c2ffc95a020c19b2175474763be4f11d024291407f615a7cd1fb6bc6fc297db8` | 1,365 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-diffs/wp44-statuses-stat-stages-and-immunities.diff`（提取侧本轮交付） | `8ea98691` | `8ea9869114c9772a5ca9f7d282ff6c436c52d05976917aabd3af4a45bd0898ad` | 5,884 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-diffs/wp45-weather-terrain-side-and-position-effects.diff`（提取侧本轮交付） | `235a4c66` | `235a4c669420248df8388a5634a78874df5e81a8d1f7b2bef9190e835066edc0` | 7,438 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-response.md`（提取侧本轮交付） | `7b99bc61` | `7b99bc61584becf3e9850a1d16bad684add81899be06c44f94a6d268b976a7e2` | 4,642 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/boundary-checks.json`（v2；有限修订传播，首稿留史） | `9509999c` | `9509999c8dadeba83dfeceb39fd4d45d7d0b1494e1837abed8f01163792a309b` | 14,399 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md`（v3；闭合后管理维护，旧声明留史） | `498dde56` | `498dde568f7c77c30c35d28e2ab492622b7c985c0243977683b54d184111f695` | 9,388 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/self-checks.json`（v2；有限修订传播，首稿留史） | `939f7e36` | `939f7e366b0c75feb45275e5ee340647715499cde96144b22bb78273925864e3` | 102,908 |

| `review/wp42-wp48-wp49-review-2026-09-27/changes-from-previous.diff`（本轮独立首审原件） | `1364e6a8` | `1364e6a81fc2f573bcb16e3a9933670a0e0dc601a1bcf8738663fbd5ebe7a703` | 122,485 |
| `review/wp42-wp48-wp49-review-2026-09-27/coverage-checks.json`（本轮独立首审原件） | `76173387` | `76173387f2bd979e5b2f51cb2221d3c51a387e6004dee8e5e84135f59e8bdd56` | 515 |
| `review/wp42-wp48-wp49-review-2026-09-27/current-hashes.tsv`（本轮独立首审原件） | `c40010c7` | `c40010c71e7a16b1ca412d5769765d8109fca6b92aecfdb1bd573d30c152254d` | 66,968 |
| `review/wp42-wp48-wp49-review-2026-09-27/diff-checks.json`（本轮独立首审原件） | `0ba13765` | `0ba13765007c4821829d14ba4c53fd67c5576a46937573f205d4e99662621a40` | 2,920 |
| `review/wp42-wp48-wp49-review-2026-09-27/final-checks.json`（本轮独立首审原件） | `ceb9ea41` | `ceb9ea41727d38830ab1bdd2379198eb9e81b754fd6ad65b95fca58b520c9ca4` | 3,017 |
| `review/wp42-wp48-wp49-review-2026-09-27/input-manifest.json`（本轮独立首审原件） | `c2129a10` | `c2129a10279afb20799eddba23fd236e935d74fd3535b1bd721b7fe471199620` | 460,058 |
| `review/wp42-wp48-wp49-review-2026-09-27/report.md`（本轮独立首审原件） | `2068681a` | `2068681add50704d439c98133d42ce4ce665da58deffef9011ead37bb148af60` | 11,466 |
| `review/wp42-wp48-wp49-review-2026-09-27/revision-prompt.md`（本轮独立首审原件） | `29862926` | `29862926457c505f1d3061dffcffd5b0b78d681393f51511eccfa5add8cb22bd` | 8,895 |
| `review/wp42-wp48-wp49-review-2026-09-27/source-checks.json`（本轮独立首审原件） | `dfaadcae` | `dfaadcae489778cbe2c173f4fd472e01ff14dc3fee9a0e0618a854d6756fe6f5` | 12,363 |
| `review/wp42-wp48-wp49-review-2026-09-27/static-checks.json`（本轮独立首审原件） | `45458215` | `4545821579499b7b3c6a3d1b788b5e072fa43bfe40dc1e8010c7c9aef431f1a0` | 444 |
| `review/wp42-wp48-wp49-review-2026-09-27/static-vectors.json`（本轮独立首审原件） | `ec5f04ca` | `ec5f04ca9c5499b648ee820873e906fda2b1ab45cf61e0962659bd499c151f96` | 5,275 |
| `review/wp42-wp48-wp49-review-2026-09-27/text-checks.json`（本轮独立首审原件） | `b1672766` | `b167276659dc4dda7a774a51d76f2eb8a20c024d90e8df7c6bbb7d6e36c48139` | 2,201 |
| `review/wp42-wp48-wp49-review-2026-09-27/revision-response.md`（提取側有限修订材料） | `5d20434a` | `5d20434afff2e59ef9b1286272bdf95ef8aed62694ee4684bdddfd25dd6a40d2` | 8,707 |
| `review/wp42-wp48-wp49-review-2026-09-27/revision-diffs/wp42-growth-end-of-round-and-battle-outcomes.diff`（提取側有限修订材料） | `77403aec` | `77403aecc72babff4be1514d99ffbfa697124008b2d31f0f8ded0af6409d0fb6` | 9,174 |
| `review/wp42-wp48-wp49-review-2026-09-27/revision-diffs/wp48-ability-calculation-modifiers.diff`（提取側有限修订材料） | `7d668a58` | `7d668a58cdb13f05787935d10ed242985b51c17018636527814c24f44e0a8a47` | 5,691 |
| `review/wp42-wp48-wp49-review-2026-09-27/revision-diffs/wp49-ability-phase-triggers.diff`（提取側有限修订材料） | `72add46d` | `72add46da6667cbd7444fc2b85bcedc057e71b80709abc73afa9e46b66c238c9` | 13,600 |
| `review/wp42-wp48-wp49-review-2026-09-27/revision-diffs/feature-matrix.diff`（提取側有限修订材料） | `6fecb4c2` | `6fecb4c29cf622d62c50f0a5507983af1df883d4187c3a25c801286bdbf5b1d5` | 8,018 |
| `review/wp42-wp48-wp49-review-2026-09-27/revision-diffs/delivery-summary.diff`（提取側有限修订材料） | `128ab037` | `128ab03757370657355cd85b7159b3fdffe0ac9b5fab3959af1cae541419d3e3` | 11,546 |
| `review/wp42-wp48-wp49-review-2026-09-27/revision-diffs/self-checks.diff`（提取側有限修订材料） | `126ba702` | `126ba702a8d7839bfec4f2765bcd3772b62cbe5c9eaad2022bcacee138f8a78b` | 26,199 |
| `review/wp42-wp48-wp49-review-2026-09-27/revision-diffs/boundary-checks.diff`（提取側有限修订材料） | `d5e226aa` | `d5e226aa6258870d8693eda77701c1f194e46bce564a3ae70f665908469a4768` | 7,922 |

| `review/wp42-wp48-wp49-recheck-2026-09-27/changes-from-v1.diff`（本轮独立闭合原件） | `360904f5` | `360904f50dbaf390ab8a444faaf9b5ab24a6d7784fbc39b22b6471a25867b76a` | 133,835 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/coverage-checks.json`（本轮独立闭合原件） | `14807ce7` | `14807ce78181c95e83254bc7d66eeab38a7957c3ea7716fcaeb3a0f7238eb136` | 1,478 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/current-hashes.tsv`（本轮独立闭合原件） | `56b644e0` | `56b644e0b3c41d3c941048b1c2a2a77e736003b28cb53dd06330b7ba561440be` | 69,735 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/diff-checks.json`（本轮独立闭合原件） | `066213fb` | `066213fb93607dc24aa629acfcd5d9e8098ac96b987ee92bcde153eb8d0fc9ff` | 2,103 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/final-checks.json`（本轮独立闭合原件） | `5f837cef` | `5f837cef78f6d8b625c7f74584585edf50ae22f85af0149c869c7fb34c6821da` | 3,312 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/input-manifest.json`（本轮独立闭合原件） | `5f6a356c` | `5f6a356c30e1f4e70799c619e496a287e82cab458b8df158ede42aab1c8038a1` | 479,610 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/next-batch-prompt.md`（本轮独立闭合原件） | `8a2ba73c` | `8a2ba73c38a80dcd8483a824e305e3f26e00a74abbe141c8872eb18ef0bd08c3` | 15,482 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/report.md`（本轮独立闭合原件） | `f0e26622` | `f0e266220cf76a0aa4f490c61b547bc705453d3729012629a563c4c727ac926b` | 10,972 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/source-checks.json`（本轮独立闭合原件） | `79504545` | `79504545574bfde4dae8a1a70a067ee81a9fef9c746a2fd8b0c6f2028bcbdb8c` | 12,309 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/static-checks.json`（本轮独立闭合原件） | `52b14ad7` | `52b14ad7063630cb72a15e8e16be08fbc97398b4ed5229f85e2b4429d7128c0b` | 2,237 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/static-vectors.json`（本轮独立闭合原件） | `f26cb864` | `f26cb864a5745b36ee473d88abf9030f9d03e227d61416cc9975c0ea7be91f3e` | 3,675 |
| `review/wp42-wp48-wp49-recheck-2026-09-27/text-checks.json`（本轮独立闭合原件） | `3c701924` | `3c701924d079fb7ee11f4e7e4a5ecb9503000bb97119e10971c8b24e7d65e541` | 10,736 |
| `specs/pokemon-rules/wp46-damage-multihit-and-healing.md`（首审PASS_SCOPED后限定Reviewed回填及C01维护；N01定点同步） | `0f7c9b4b` | `0f7c9b4b21ec45c2084876de08218812aab7a615b6fb2d53ff1c0de603d3b662` | 48,872 |
| `specs/pokemon-rules/wp46-damage-healing-coverage.md`（首审PASS_SCOPED后限定Reviewed回填及C01维护） | `549cd587` | `549cd587095df207bf359c34fd66f14f2dda0c93ce1dcaec6bf4f63fc4d084c1` | 36,824 |
| `specs/combat/wp47-a-move-attributes-targeting-and-calling.md`（首审PASS_SCOPED后限定Reviewed回填及C01维护；必要身份级联） | `e4934943` | `e49349438e19be9bbd09bcc192e69f4d839a8e715c46cf09291f0f8c5c390f96` | 34,014 |
| `specs/combat/wp47-a-attributes-targeting-calling-data.md`（首审PASS_SCOPED后限定Reviewed回填及C01维护） | `49e34300` | `49e343003be7c22653cad121f3c037b915212da18b6240cda12e653d07c91a17` | 19,340 |
| `specs/combat/wp47-b-switching-control-and-item-changes.md`（首审PASS_SCOPED后限定Reviewed回填及C01维护；必要身份级联） | `00769901` | `007699019544203b9b5f4c42f18db8eb91711d2d96f6fa8afdf047d44b16e778` | 39,000 |
| `specs/combat/wp47-b-control-items-coverage-data.md`（首审PASS_SCOPED后限定Reviewed回填及C01维护） | `0736044d` | `0736044d556367392e2a0204a4a934a903d3472c9cb28435b4765798d915d13a` | 17,922 |
| `review/wp46-wp47-delivery-2026-09-27/backfill-diffs/delivery-summary-prior.diff`（本轮提取侧交付） | `48fa708a` | `48fa708a9567fb9f5c806f4a4a579d5e9b16196ba4dff1e9cda414780bdeb860` | 12,257 |
| `review/wp46-wp47-delivery-2026-09-27/backfill-diffs/feature-matrix.diff`（本轮提取侧交付） | `ea5c019c` | `ea5c019ceb63b121e4003b5fd29eebff26f010b987649169cbdc2a94c8f5b910` | 10,422 |
| `review/wp46-wp47-delivery-2026-09-27/backfill-diffs/wp42-growth-end-of-round-and-battle-outcomes.diff`（本轮提取侧交付） | `52bc6bfb` | `52bc6bfb72e861523ec2b58cbbbcc599a33045537ce20124e98a05e257dd0fff` | 2,551 |
| `review/wp46-wp47-delivery-2026-09-27/backfill-diffs/wp48-ability-calculation-modifiers.diff`（本轮提取侧交付） | `5a93408b` | `5a93408b37b3937ba7b85db2e2028b1845622a950864d2b996fc75ab74f28f5d` | 2,443 |
| `review/wp46-wp47-delivery-2026-09-27/backfill-diffs/wp49-ability-phase-triggers.diff`（本轮提取侧交付） | `2e79d8a4` | `2e79d8a4fad138932b951a07a4c06d2c09f5c23cafb15478b5e479406aec907d` | 5,109 |
| `review/wp46-wp47-delivery-2026-09-27/backfill-response.md`（本轮提取侧交付） | `7adff526` | `7adff526730ce22e211d33b11849e0914ac035d7699b74f12105d37a26f4bb69` | 4,454 |
| `review/wp46-wp47-delivery-2026-09-27/boundary-checks.json`（v2；旧批限定回填／获批同步；v1留史） | `2cb48235` | `2cb48235c7794e4167128a399f04c9cb3465e299c9096da1ecde6e49f9d6dae0` | 23,256 |
| `review/wp46-wp47-delivery-2026-09-27/delivery-summary.md`（v2；旧批限定回填／获批同步；v1留史） | `73226fe5` | `73226fe59a5b6036bdabb913f121d5cadd76e23ad2f62c9a54dc686d173697c6` | 6,036 |
| `review/wp46-wp47-delivery-2026-09-27/self-checks.json`（v2；旧批限定回填／获批同步；v1留史） | `eda9101a` | `eda9101ab5b563f5c3b53e53b029a6d0c82ec8e96a7358c3e4e0c6c7be2318c9` | 209,456 |

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。
| `review/wp46-wp47-review-2026-09-27/changes-from-previous.diff`（独立首审原件；未修改） | `da770931` | `da7709316ec69a78b74d75bd4a3149046997053950545a0a52a299ece94b1bb4` | 93,811 |
| `review/wp46-wp47-review-2026-09-27/coverage-checks.json`（独立首审原件；未修改） | `61d462d7` | `61d462d71d953d64e479458fe4398b13f7d6d36d82ae264a7f9fc76d4fa69e5d` | 5,975 |
| `review/wp46-wp47-review-2026-09-27/current-hashes.tsv`（独立首审原件；未修改） | `ee1bc61b` | `ee1bc61bf87a2377191b9b73bc84d2c1c14ee4c1bd39dc0ac7afec4cfa6ace90` | 73,352 |
| `review/wp46-wp47-review-2026-09-27/diff-checks.json`（独立首审原件；未修改） | `bef28462` | `bef284624c90e6161e30b5a7c8d2312f08f1bd6a2b7d16a8325800ee500e9081` | 1,511 |
| `review/wp46-wp47-review-2026-09-27/final-checks.json`（独立首审原件；未修改） | `d85e1050` | `d85e105055b2f2a22517dc4ca02745659a970f6680f5d2dde71e8d334ba479d3` | 4,046 |
| `review/wp46-wp47-review-2026-09-27/input-manifest.json`（独立首审原件；未修改） | `6b1c9487` | `6b1c94877af430ad88055561a607b22b775d14865b480eb0aff2675c5336f98c` | 505,418 |
| `review/wp46-wp47-review-2026-09-27/next-batch-prompt.md`（独立首审原件；未修改） | `559ed0a2` | `559ed0a2ae12138742ad9d2d111f3d7801b9438e374e6091095457e1f81c932c` | 18,465 |
| `review/wp46-wp47-review-2026-09-27/report.md`（独立首审原件；未修改） | `1bd018f5` | `1bd018f519db064d3a9ff9d2b9582e692cd6bf0c129a56f1dd7bab0ee5730541` | 16,289 |
| `review/wp46-wp47-review-2026-09-27/review-notes.json`（独立首审原件；未修改） | `261f8bf1` | `261f8bf11e49c3ce709ff9c482a019e3eb9db25653cb839e8c8bf9c7ff0dba9d` | 2,562 |
| `review/wp46-wp47-review-2026-09-27/source-checks.json`（独立首审原件；未修改） | `922d47bb` | `922d47bb4e56435e28d7ccae63753f5d0efee88bd91bcebf4c6d0c4b29def932` | 14,000 |
| `review/wp46-wp47-review-2026-09-27/static-checks.json`（独立首审原件；未修改） | `99c59a4d` | `99c59a4df8a5c2f7677eb6b350efe2560fd88eec6ea6776e39e73d874d6454a6` | 1,347 |
| `review/wp46-wp47-review-2026-09-27/static-vectors.json`（独立首审原件；未修改） | `b37b9765` | `b37b9765b0dc5b5ef18cb8827ee7f9b4e9efcac924c0cef3e3cc06ea3b9bdd8e` | 4,562 |
| `review/wp46-wp47-review-2026-09-27/text-checks.json`（独立首审原件；未修改） | `6df7f69b` | `6df7f69ba5d54d6c7416b1b536d928e4d159a4a34f9c476dfb75cfa3e0439eec` | 21,478 |
| `specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md`（2026-09-28有限复审PASS_SCOPED后限定Reviewed管理回填；必要身份级联） | `f0b6b147` | `f0b6b1472ed1eceb7679c0bf50d836076a0a52a593ce011132ee90c1e01e6f72` | 32,490 |
| `specs/pokemon-rules/wp50-held-item-effect-coverage.md`（2026-09-28有限复审PASS_SCOPED后限定Reviewed管理回填） | `f62603f2` | `f62603f26e7570e32949ebce97c531ef0af59ba6da4f083bff9d85775de2fc69` | 14,418 |
| `specs/combat/wp51-ai-action-selection-and-skill.md`（已审WP51仅上游身份/状态与表格连接维护；本轮必要身份级联） | `2b0847b5` | `2b0847b5d52d9907804c62703871a9a6557a6b9940a8fd0a93c702329808a025` | 27,645 |
| `specs/combat/wp51-ai-decision-defaults.md`（2026-09-28首审PASS_SCOPED后限定Reviewed；C01维护/管理回填） | `5069a369` | `5069a3690c6886204ebe9877ff0165e77c4c437fb8273032ac9d6f52bf89c2d0` | 5,472 |
| `specs/combat/wp52-a-generic-numerical-and-status-evaluation.md`（2026-09-28有限复审PASS_SCOPED后限定Reviewed管理回填；BATCH-C01与本轮回填同步） | `388b5fce` | `388b5fce672b8d88cb08e309827154c35e44f68cbe4fd07b62c2f66e3701f26b` | 50,104 |
| `specs/combat/wp52-a-evaluation-coverage-and-data.md`（2026-09-28有限复审PASS_SCOPED后限定Reviewed管理回填；BATCH-C01与本轮回填同步） | `91ab040d` | `91ab040d63013316881f7fafb52657407fb5b17158a64c6522059b86ec58bed8` | 61,156 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/boundary-checks-prior.diff`（本批提取侧材料） | `5dd48b0b` | `5dd48b0bca2b3ee71c4cb73ff7fdb3d5a59c35d7d581b1ec8ef756979ee08eb7` | 25,210 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/delivery-summary-prior.diff`（本批提取侧材料） | `99cf7b25` | `99cf7b250e388f32b2c8e0f8a319812d3cbfea60ca2295167cefb034d23a8c4e` | 12,944 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/feature-matrix.diff`（本批提取侧材料） | `77ae4a02` | `77ae4a023f211d6eef165676226ecbbfaadb6bc4b47a871fa2a098c2c6461126` | 10,969 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/self-checks-prior.diff`（本批提取侧材料） | `b5e4ad9b` | `b5e4ad9b9827e480e859c978f87528de0d005061a758ceaf7e883a6eadf54062` | 13,468 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp40-commands-obedience-and-action-order.diff`（本批提取侧材料） | `e489cb3f` | `e489cb3fcdc31a815a21d4b4d5ac5b96b420aa7cb786087ed0e2231d8e7f2010` | 4,675 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp41-switching-positioning-and-escape.diff`（本批提取侧材料） | `5744cf8c` | `5744cf8c77c9731a968f109f3f87c44728b2d7e56f86e4a0fae35556037c0446` | 9,451 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp42-growth-end-of-round-and-battle-outcomes.diff`（本批提取侧材料） | `5de4430e` | `5de4430ee2353976c6d1b35672240885c001660ec0dc9d686bc0241c65a79599` | 2,285 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp43-types-accuracy-and-damage.diff`（本批提取侧材料） | `bb3cfb5d` | `bb3cfb5d03c8fc330d8c07ce2976bd3345fc2a891d150794b6c35135bbfa9387` | 1,123 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp44-statuses-stat-stages-and-immunities.diff`（本批提取侧材料） | `f58b85a2` | `f58b85a22de2a0484ec4183d1576bd80332f5ca65ca4dac2a2458863f2a3ffea` | 1,464 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp45-weather-terrain-side-and-position-effects.diff`（本批提取侧材料） | `a83345b3` | `a83345b392e2dca42246c7fd8feb73328bd443df48384dbe8e80d16fb9576434` | 2,354 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp46-damage-healing-coverage.diff`（本批提取侧材料） | `0878cb2f` | `0878cb2f58d6cc4c7960a8340e632a0069e7e2a778baa6b52f5ffa1d4aa83f8e` | 3,043 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp46-damage-multihit-and-healing.diff`（本批提取侧材料） | `a26cff0f` | `a26cff0fdd79ae4328c7df6301aa95a8f0c205c75fe8439d274eb4d9641a7bf4` | 8,099 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp47-a-attributes-targeting-calling-data.diff`（本批提取侧材料） | `21fa7985` | `21fa7985757534ca7e399da8ab37eb91b55d3f0c63fe156921725c082a67d010` | 1,968 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp47-a-move-attributes-targeting-and-calling.diff`（本批提取侧材料） | `a56a0523` | `a56a0523dc124c8e53aacad082d05dc896e10bb7e6626915054033b1f00f9b7e` | 8,333 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp47-b-control-items-coverage-data.diff`（本批提取侧材料） | `d9b9029c` | `d9b9029c5fa781330c006dce65843418e1f7857b4e517232cfc0dd274d6fd51b` | 2,300 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp47-b-switching-control-and-item-changes.diff`（本批提取侧材料） | `75f8f9a6` | `75f8f9a66ba3b0aabffc760d680a68b0d6ba42b5eef3507fdc4368a1da464ce0` | 14,375 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp48-ability-calculation-modifiers.diff`（本批提取侧材料） | `89efff71` | `89efff71aedf15943cdc0bf9398ad8b30e6d7543aeca6f580613d04ce496cf8e` | 2,206 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-diffs/wp49-ability-phase-triggers.diff`（本批提取侧材料） | `88053ace` | `88053acea420736f58b1dd09818e8e28e8d5216ead88b12ed4abd319f3690c6e` | 3,483 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-response.md`（本批提取侧材料） | `860bc758` | `860bc758987f3ca772ef445fa3051e939aaddd23f76afa6b06275ae85d8f8e05` | 7,731 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/boundary-checks.json`（v3；闭合后管理维护，v2被审身份留史） | `26acad41` | `26acad41c8a5f49468d0aeeffd5e9584770c8f74947dd64066da5cffc323d256` | 49,349 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/delivery-summary.md`（v3；闭合后管理维护，v2被审身份留史） | `20a61b73` | `20a61b73befceb5a88bb4db76c5c4dd0a453fc0f7b6639ac3d3f79987a5d7848` | 4,833 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/self-checks.json`（v3；闭合后管理维护，v2被审身份留史） | `6e832558` | `6e83255802631e198518cd5178f75ec4204498ae2a0d2b92592e6b69b87f13bc` | 464,719 |
| `review/wp50-wp51-wp52a-review-2026-09-28/backfill-changed-lines.json`（本轮独立首审原件；未修改） | `59181cb3` | `59181cb3655d29261b8b719a6e3da40b8b77a5cfa8cf2cbf6d24b5cc1b1a4cb3` | 92,675 |
| `review/wp50-wp51-wp52a-review-2026-09-28/changes-from-previous.diff`（本轮独立首审原件；未修改） | `98176658` | `98176658e2390da786d9eae1bad0c4356cf59962f5e8ed2293cb7f6073c612ef` | 235,965 |
| `review/wp50-wp51-wp52a-review-2026-09-28/coverage-checks.json`（本轮独立首审原件；未修改） | `53afc2dd` | `53afc2ddf3903404c5c363209597e5c0f546f05bb684e220d27a9727fc08304e` | 2,387 |
| `review/wp50-wp51-wp52a-review-2026-09-28/current-hashes.tsv`（本轮独立首审原件；未修改） | `8954aa14` | `8954aa14a03c4b961c3b69d59557b5c56c8d26c4b8c52784bfdce5f471c8943e` | 79,263 |
| `review/wp50-wp51-wp52a-review-2026-09-28/diff-checks.json`（本轮独立首审原件；未修改） | `5c92074f` | `5c92074f49b3dc15c55ebf42bd64509acf2179de4c28bd42aa76e32164df822d` | 5,060 |
| `review/wp50-wp51-wp52a-review-2026-09-28/final-checks.json`（本轮独立首审原件；未修改） | `a71fe74d` | `a71fe74db83b1773e9c685c69f300e021654e6f92fdba425c06df10b9ca8faa7` | 3,999 |
| `review/wp50-wp51-wp52a-review-2026-09-28/input-manifest.json`（本轮独立首审原件；未修改） | `0b702890` | `0b70289035edaeeb85296e9ea2f47ef56838a8fd7e3c02984ea5d100ed993af1` | 551,568 |
| `review/wp50-wp51-wp52a-review-2026-09-28/report.md`（本轮独立首审原件；未修改） | `39e5a7e8` | `39e5a7e85cfafbcfeb49eb31c667a81a80fbc425d36b843013e45e5cee8e3c85` | 12,797 |
| `review/wp50-wp51-wp52a-review-2026-09-28/review-notes.json`（本轮独立首审原件；未修改） | `60156fe8` | `60156fe8029e58cd4589f3dc5ed02ae2b9b105e3820f086a6acddfb9154bf116` | 4,319 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-prompt.md`（本轮独立首审原件；未修改） | `c58476b8` | `c58476b85724c916e2a47f3613a9fd936bbabcfb3ced0df774c5d94e26d7f869` | 10,691 |
| `review/wp50-wp51-wp52a-review-2026-09-28/source-checks.json`（本轮独立首审原件；未修改） | `f15c0351` | `f15c0351cf73f91c3aaee999417633d4c220bd5b8c25020a6bb75cc56a2c2429` | 15,794 |
| `review/wp50-wp51-wp52a-review-2026-09-28/static-checks.json`（本轮独立首审原件；未修改） | `6cdafb08` | `6cdafb0865f9185c1453f66da4b807de615f20a9165c35cfb96751aafb9e5cd4` | 936 |
| `review/wp50-wp51-wp52a-review-2026-09-28/static-vectors.json`（本轮独立首审原件；未修改） | `a43dddb6` | `a43dddb6e7c861dff0fff26c067dbb00192a8511d31261097b47ceb53bf61f26` | 5,183 |
| `review/wp50-wp51-wp52a-review-2026-09-28/text-checks.json`（本轮独立首审原件；未修改） | `a98d18fb` | `a98d18fb0993500930c3e89c6636c7a629b112195f452f06541b2dec9c7ebaa3` | 22,082 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-response.md`（提取侧本轮有限修订材料） | `47dfc20d` | `47dfc20d1d1fe50fc582856b9a6ad83ec9fb3e39dc6f74bcaf7cfdb6b88e95eb` | 7,997 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-diffs/boundary-checks.diff`（提取侧本轮有限修订材料） | `de39b9d8` | `de39b9d8ee70532a7fec30a59f51544a6eb674fa9cf65e6836be8ae09385c616` | 22,751 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-diffs/delivery-summary.diff`（提取侧本轮有限修订材料） | `dd9da37e` | `dd9da37e7e32cd03e4814d7a3adca81c2524b50f68aef7ad23ae4f6702003a0e` | 13,964 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-diffs/feature-matrix.diff`（提取侧本轮有限修订材料） | `4abfc7b8` | `4abfc7b817c9950062da2c720e67977e0f570ebd0a5bae58b7ee265e2e245740` | 8,959 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-diffs/self-checks.diff`（提取侧本轮有限修订材料） | `e5f6cb57` | `e5f6cb57958a72153dd955dfcb8e225a2431970538656474fdf12119fbb2015e` | 87,393 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-diffs/wp50-held-item-triggers-and-consumption.diff`（提取侧本轮有限修订材料） | `24d57151` | `24d57151b658da71be7b8f86067699b1d3529fc79f9a0227aca5982c67943b06` | 9,685 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-diffs/wp51-ai-action-selection-and-skill.diff`（提取侧本轮有限修订材料） | `8568c8d3` | `8568c8d321b1756a99dde8113b889d16f385d3e8e9b1ff44b3047ae4e707d9cc` | 11,198 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-diffs/wp51-ai-decision-defaults.diff`（提取侧本轮有限修订材料） | `8f9dd720` | `8f9dd720b780ceae56882b19542203a21bd231437e5033e3a4ddf2bb4d77f816` | 1,936 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-diffs/wp52-a-evaluation-coverage-and-data.diff`（提取侧本轮有限修订材料） | `ec2d4854` | `ec2d48546c42d9fcfdb92e5df00323c622900d7ea987cec1bf7552b315b93272` | 4,096 |
| `review/wp50-wp51-wp52a-review-2026-09-28/revision-diffs/wp52-a-generic-numerical-and-status-evaluation.diff`（提取侧本轮有限修订材料） | `05fb6f9a` | `05fb6f9a3b9350c68331a46ebb51ea5865decb32913e04bd6580d16dd1d20c6d` | 10,964 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/changes-from-v1.diff`（本轮独立有限复审原件） | `8b812777` | `8b8127779a01a31c7697f449b8e3373f48a516de3318f8bbfb7f971265f433be` | 233,309 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/coverage-checks.json`（本轮独立有限复审原件） | `93c7fb55` | `93c7fb55609aaaabfa8f71d1b04aa75f04043166044403f922ac88a728daba8e` | 1,820 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/current-hashes.tsv`（本轮独立有限复审原件） | `b792683f` | `b792683f886b120573e2e977d0bd6692f6d4a27b222fad1bf527d33cdca80376` | 82,658 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/diff-checks.json`（本轮独立有限复审原件） | `29c69a43` | `29c69a43e98e5336acd17b96c77fe06b0b6858b6e01b5fd8475a4d892c1426a3` | 2,973 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/final-checks.json`（本轮独立有限复审原件） | `d6b899c7` | `d6b899c774e130f5b5975c7d7b9ff31d625a1113955553f9abebadbe1eba2d6c` | 3,614 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/input-manifest.json`（本轮独立有限复审原件） | `85c57512` | `85c57512e868a05a7802db64341ef614291c059e1931a0f15d1bdbedec50b95e` | 572,468 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/next-batch-prompt.md`（本轮独立有限复审原件） | `5868bfcd` | `5868bfcd92f142ab88bea00c8edf420618ecf295c71782b01dcc0bf0b72d0077` | 17,404 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/report.md`（本轮独立有限复审原件） | `6537ac37` | `6537ac37528a3e21f9f809d4ea72fd309c132a07539ca2d312d34b889ef0ca4a` | 10,814 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/source-checks.json`（本轮独立有限复审原件） | `bd0f0c5c` | `bd0f0c5c7c78a67ff77f0c25ab59cbf4cbb0f0f6d9a61ffa37a3d7f2ce585c6f` | 13,879 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/static-checks.json`（本轮独立有限复审原件） | `f79e4224` | `f79e4224fab0578159bf362c386c40b6c8714d70ed28dae22417c021503bea97` | 1,000 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/static-vectors.json`（本轮独立有限复审原件） | `ecf6bd35` | `ecf6bd35f29e4eb2e991210eba2261bd2b80bcff5e98d30ef77955e715e40a56` | 2,185 |
| `review/wp50-wp51-wp52a-recheck-2026-09-28/text-checks.json`（本轮独立有限复审原件） | `68893499` | `68893499f8816ad7ec63e3a4b5687df11714ae135f2b21cce61df74692148355` | 22,713 |
| `specs/combat/wp52-b-field-damage-healing-and-target-evaluation.md`（限定Reviewed回填；2026-09-28有限复审PASS_SCOPED；R01 CLOSED） | `73fa6ffa` | `73fa6ffa2096cea14354faca92e63439c9db7698541536212901050f65baf759` | 45,342 |
| `specs/combat/wp52-b-effect-coverage.md`（限定Reviewed回填；2026-09-28有限复审PASS_SCOPED） | `723838f2` | `723838f295a6041a8f14b55a8f3abcab909f3431f8fef6050a22306975a6d3b5` | 57,979 |
| `specs/combat/wp52-c-items-calling-and-control-evaluation.md`（2026-09-28独立首审PASS_SCOPED；限定Reviewed回填；B/A引用本轮回填重固定） | `658b40bc` | `658b40bca3e9567203dea4fc1d9c417adddbca4f1c9f7e1535e6b30ed0e32c2b` | 40,722 |
| `specs/combat/wp52-c-item-control-coverage-and-data.md`（2026-09-28独立首审PASS_SCOPED；限定Reviewed回填） | `f83205ee` | `f83205eebd3889354a4fb8afe9847c9e489d0eec9d84b876e06b6da3c0f09088` | 38,390 |
| `specs/combat/wp54-entry-eligibility-level-adjustment-and-clauses.md`（2026-09-28独立首审PASS_SCOPED；限定Reviewed回填；N01同步） | `2a1518c3` | `2a1518c3351ed9fa3dfaf839010dcc0f4c56df862353c39a227151aa83d06dfb` | 33,809 |
| `specs/combat/wp54-entry-rules-and-cup-data.md`（2026-09-28独立首审PASS_SCOPED；限定Reviewed回填） | `0ec50236` | `0ec502366b743770f95d7971cf3f087a153694bc6ff4395b8852642fd422a18d` | 12,381 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-diffs/boundary-checks-prior.diff`（本轮提取侧交付材料） | `abdd7984` | `abdd798422981b3ad7a14e484496f1e69194c0db126535c2a8dce9e815e4df44` | 23,570 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-diffs/delivery-summary-prior.diff`（本轮提取侧交付材料） | `a16ef26f` | `a16ef26f465731961f6dfdfa8d4aa449b83e572c468a640f5ae27c4e2b95a53a` | 14,521 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-diffs/feature-matrix.diff`（本轮提取侧交付材料） | `20f07473` | `20f0747397161bf4bc67d171b5207e8ea5b63449c5ce6f98f7c23ac3ed2de0de` | 9,452 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-diffs/self-checks-prior.diff`（本轮提取侧交付材料） | `5e7d285d` | `5e7d285d5414b1e2e7b2df9a27a7c8b051bf67368a793ac18398ffea191e5de9` | 56,889 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-diffs/wp50-held-item-effect-coverage.diff`（本轮提取侧交付材料） | `fcd89a05` | `fcd89a05ed498d5cffda92330a4baf66dfb73a972d3a2823ba7f500279384d4b` | 2,243 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-diffs/wp50-held-item-triggers-and-consumption.diff`（本轮提取侧交付材料） | `f696f577` | `f696f5771ec14534ac4181259a77c2091467f14a7575b405e574073a835374aa` | 6,284 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-diffs/wp51-ai-action-selection-and-skill.diff`（本轮提取侧交付材料） | `5725bb71` | `5725bb71c785e452a0aa045d33047facfccd31b92b55aeb8dd6a5c2d4cbe17ae` | 4,187 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-diffs/wp52-a-evaluation-coverage-and-data.diff`（本轮提取侧交付材料） | `c1e4653d` | `c1e4653d0ff9a54e56e6f5b72051bcaa38d5bdfbe36a230b08b62268d4c5e5e5` | 2,720 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-diffs/wp52-a-generic-numerical-and-status-evaluation.diff`（本轮提取侧交付材料） | `a3766364` | `a376636420885f9f12f2582611e186d3d949c38eb8436f22bbf0f51473d4212a` | 8,410 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-response.md`（本轮提取侧交付材料） | `1331835f` | `1331835f952041f5396ec2ee12ece709fe768c7b133fcb6aee14edf408930a8d` | 4,511 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/boundary-checks.json`（v3；PASS_SCOPED后B回填与C02） | `9e693b2c` | `9e693b2cfd18dba605bfa43e6d2825661529ed811189edd161c13a7e9d52014a` | 20,318 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/delivery-summary.md`（v4；继承C02剩余维护） | `4ba4ed58` | `4ba4ed58f9672c9dce98638afde52b3d32a2e71cf5b9f4630e84f0055cb5f1af` | 9,587 |
| `review/wp52b-wp52c-wp54-delivery-2026-09-28/self-checks.json`（v4；继承C02剩余） | `b776328d` | `b776328d56003326f0b4d5eb02023a549d8472330e335a4846012aa52b0f2ecc` | 1,070,038 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/binding-checks.json`（本轮独立首审原件；未修改） | `c5e22f44` | `c5e22f4443908f8040e3d5ba5f3d0f4ab2fc423fee7d24d910ff7d40fa4da572` | 11,302 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/changes-from-previous.diff`（本轮独立首审原件；未修改） | `20b151ae` | `20b151ae8315da0c7591bc9ecf32d3ad1003a5391d1c8305808195a593d71343` | 204,190 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/check_constants.py`（本轮独立首审原件；未修改） | `e254c38d` | `e254c38d6064b67653fb2537cff154ebc53d7a9225c738714f48978932e556bf` | 2,225 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/check_text_and_identity.py`（本轮独立首审原件；未修改） | `088ae6c6` | `088ae6c639883afd95821df1cfdf2ffc85b19020f7abda92a6d7443e51ee3c02` | 13,154 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/constant-checks.json`（本轮独立首审原件；未修改） | `0610a592` | `0610a592712ec86a5dfc999ac56154f70f0edfc72bc42ec48e51c45be34c8077` | 3,964 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/coverage-checks.json`（本轮独立首审原件；未修改） | `2b7f6c48` | `2b7f6c4811f54619e61bd373b43d7af1841b6c15f7e50088ea0e3b16b6294323` | 2,394 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/current-hashes.tsv`（本轮独立首审原件；未修改） | `86c0511a` | `86c0511ac8aee95f549a7fd4c1b414a554d1f163a792cb3a7cbe816b7cba2dab` | 87,007 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/diff-checks.json`（本轮独立首审原件；未修改） | `de826bcd` | `de826bcdd41d3d77b21f6b708d013c8d2be15e36232dd6f80cbe08724030b9d5` | 4,102 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/final-checks.json`（本轮独立首审原件；未修改） | `c69b99a5` | `c69b99a59038f3b85002c160f0d0344418c28b6f9c430e255fd6b8bb6c7441cc` | 4,466 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/identity-checks.json`（本轮独立首审原件；未修改） | `3ba604c6` | `3ba604c6fe72ad41755ad20a898de96cde1377e0274ee8f07d86e61f2675b6f1` | 1,105 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/input-manifest.json`（本轮独立首审原件；未修改） | `3cdca6c4` | `3cdca6c433912063b50f30ff37ddd6d05dece6367d1e8140654fb9c8fded4774` | 603,528 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/report.md`（本轮独立首审原件；未修改） | `b7e5e47b` | `b7e5e47bc99da6a3965ca2885b80f5e654cefc79d4ff641fb3586c7d18284ddd` | 14,417 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/review-notes.json`（本轮独立首审原件；未修改） | `6dbcd0f7` | `6dbcd0f7ef2850dc73e4d87fe731e5099f9ceddfb0fedde39b708441b3e7066a` | 5,692 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-prompt.md`（本轮独立首审原件；未修改） | `da43a392` | `da43a392e29207dcffca089ff1a6587d76ff3881eb02285cea27aa2003383c9a` | 10,379 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/scenario-index.json`（本轮独立首审原件；未修改） | `b053f816` | `b053f8161ba12bd15b0ae0426dad590c0e9067ecc8289aee04342af06cec6329` | 3,301 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/source-checks.json`（本轮独立首审原件；未修改） | `c78f41f4` | `c78f41f4627ec1daa007f50a5a15327de431d9ccafc705dc3f36b5d70d89f7f5` | 13,579 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-response.md`（提取侧本轮有限修订材料） | `0b179892` | `0b179892f81a02bd592885de20de6cf96882a7e736ba0dd6e63d28a081b5e4e1` | 12,855 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/boundary-checks.diff`（提取侧本轮有限修订材料） | `20a85334` | `20a85334fb2f5913570ea8be09cff2f205e99a7afb194a1e8b803f4973bffe63` | 17,378 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/delivery-summary.diff`（提取侧本轮有限修订材料） | `39f3417f` | `39f3417f7f4172f72977f239af01e5c62344a6ed82b43daea67cabedbcb439f7` | 14,164 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/feature-matrix.diff`（提取侧本轮有限修订材料） | `557254a0` | `557254a028ae4e66188d283d447c5d2d63b1fc335df18e18c240443b75eed661` | 5,806 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/self-checks.diff`（提取侧本轮有限修订材料） | `7e4cea13` | `7e4cea135762bef9ee730ff6430ecabc98012e32b86205d43c8fbdc7f9066a51` | 12,883 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp46-damage-multihit-and-healing.diff`（提取侧本轮有限修订材料） | `5a5416db` | `5a5416db2d48734890e278455ddec6f4bc16d2c8fb53fc96894c6821da85e6db` | 6,140 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp47-a-move-attributes-targeting-and-calling.diff`（提取侧本轮有限修订材料） | `358f2f58` | `358f2f583ddb4cf8a8da65d78d79f82d57a214381a4bd54e678d8b659bf1189e` | 3,789 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp47-b-switching-control-and-item-changes.diff`（提取侧本轮有限修订材料） | `1628b8ab` | `1628b8ab869432d26c4fa9627ea6c7aa340d8dacc3ddb2dca8dc7140c211226b` | 3,531 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp50-held-item-triggers-and-consumption.diff`（提取侧本轮有限修订材料） | `96f2acb2` | `96f2acb29d168572430bf32ae2d66c6b587ec9e451e688dc823cb01f2b40bcb8` | 2,939 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp51-ai-action-selection-and-skill.diff`（提取侧本轮有限修订材料） | `94ea965e` | `94ea965e243df99fb3366171c5404255bb6d7169e8f6cf9e20af82572d75c9ee` | 3,216 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp52-a-evaluation-coverage-and-data.diff`（提取侧本轮有限修订材料） | `531d146e` | `531d146e9d17c441dc2f476adefc358c1040238ab8e96e16ebd8876587da087f` | 39,625 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp52-a-generic-numerical-and-status-evaluation.diff`（提取侧本轮有限修订材料） | `13711fe3` | `13711fe36662b5b110d5eb5f3bee8b6ec5fa9a4c2acd42d3f63ba8ea8cca04e0` | 7,902 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp52-b-field-damage-healing-and-target-evaluation.diff`（提取侧本轮有限修订材料） | `1c8b4366` | `1c8b4366566636d9e20f324b16b3bfecdaf69192a10784650580b4a1d2a63c3b` | 9,682 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp52-c-item-control-coverage-and-data.diff`（提取侧本轮有限修订材料） | `62fd6a93` | `62fd6a93fdcd1020821e79431d09e8fcf0c1077f6dc01d796dd66670dc14ef75` | 2,336 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp52-c-items-calling-and-control-evaluation.diff`（提取侧本轮有限修订材料） | `7a6368f2` | `7a6368f25292ffdac9c94706fee45445258f97fc021a97df9d9b7eb5d63ebed5` | 9,917 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp54-entry-eligibility-level-adjustment-and-clauses.diff`（提取侧本轮有限修订材料） | `70c7ba9a` | `70c7ba9a934756fb918d4c6aa1b28bd30b86781ae3c26445c013c75b575bc9e0` | 11,276 |
| `review/wp52b-wp52c-wp54-review-2026-09-28/revision-diffs/wp54-entry-rules-and-cup-data.diff`（提取侧本轮有限修订材料） | `a9d8742a` | `a9d8742a1f649ed328ee1eaf7d43dc02a1f599f41436fe5a5643dd0be33d5e1e` | 2,219 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/changes-from-v1.diff`（本轮独立有限复审原件；未修改） | `f2df6c21` | `f2df6c21067dc655e732fe3f649be7b1020dd4f2d5b9d03dc0bfb27dd563011d` | 234,633 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/check_revision.py`（本轮独立有限复审原件；未修改） | `40d0ca02` | `40d0ca020c31fc121951edacbb46ff7b19491f342d3f2a0997ba08376578ce3c` | 10,906 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/coverage-checks.json`（本轮独立有限复审原件；未修改） | `f794e552` | `f794e5522fe61e3afbeb73f0f032b3ef3b4cab9bf38c85e011279996a8bdd66b` | 845 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/current-hashes.tsv`（本轮独立有限复审原件；未修改） | `74c83cd1` | `74c83cd156da3c5c78393b113a30260136de4ef59e12bed73a7cbd015b5361fe` | 91,935 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/diff-checks.json`（本轮独立有限复审原件；未修改） | `547bcf58` | `547bcf58fabf235a2b1c88bccf2c19bcf637dd22147bef28da7a2d09b1cab3ea` | 7,334 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/embedded-record-checks.json`（本轮独立有限复审原件；未修改） | `b8ea5615` | `b8ea5615c1c8a1a553cc829486108124942619f0ed86442c53b13d612162c128` | 10,547 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/final-checks.json`（本轮独立有限复审原件；未修改） | `3b42aa20` | `3b42aa205e6af7323dee635c034f2cbf09e411d85086fe86f64cb6fb89ce6c7f` | 4,381 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/identity-checks.json`（本轮独立有限复审原件；未修改） | `d05d040d` | `d05d040d84b5e04942a79dbef5ffb5a70afd7b4b446c2bb7790b9785a0669d4a` | 7,027 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/input-manifest.json`（本轮独立有限复审原件；未修改） | `b2549f25` | `b2549f25d16024c38b0e79a75bbe289c2b597949c1a3c9a3f91e7a8c4b79dcf6` | 639,950 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/next-batch-prompt.md`（本轮独立有限复审原件；未修改） | `0e49b872` | `0e49b872ba414cb321152d449a70610a51da0ad83ca99ec0c5cd31890e7fbf74` | 15,809 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/propagation-checks.json`（本轮独立有限复审原件；未修改） | `1047a3b8` | `1047a3b8fcfdba22be61321a8a41cbe7d386e32ade1bed30a8fa64c8c04c081f` | 34,011 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/report.md`（本轮独立有限复审原件；未修改） | `35d382cd` | `35d382cd11f7f5334317ee10a88fdf53f3bfe2c0d05453ae39f3079ab583b5ec` | 12,290 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/source-checks.json`（本轮独立有限复审原件；未修改） | `0e9b0449` | `0e9b044952700853377af458a9d5c8edc9e159be6296be00cbb8cc5e7ddb7124` | 19,063 |
| `review/wp52b-wp52c-wp54-recheck-2026-09-28/static-checks.json`（本轮独立有限复审原件；未修改） | `89ab62c5` | `89ab62c5b3c58f460415191ba008b0d7cf90c141295e6765112abf635cc9f6bf` | 2,968 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-response.md`（提取侧回填材料；2026-09-29维护版） | `835459a7` | `835459a74ae189af5c9f64235fa7286012d3ab9ef4dc999ec434f7ceada43b29` | 6,661 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-diffs/boundary-checks.diff`（提取侧本轮回填材料） | `acf18df7` | `acf18df7fb2ae940748a4c39bf06721bb5bb386113509bac0ef4d5ca1ab1904e` | 8,981 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-diffs/delivery-summary.diff`（提取侧本轮回填材料） | `97c76509` | `97c765098feeb6a062a572871ad47e7c35e08465afd871c963768ff4e209fad4` | 11,388 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-diffs/feature-matrix.diff`（提取侧本轮回填材料） | `d8652baf` | `d8652baf27251f038476800566c53abd49374c6531b885ce5e88f816449b5924` | 7,623 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-diffs/self-checks.diff`（提取侧本轮回填材料） | `032740a1` | `032740a1d486469764e1d8f61dc144aef619191fbba9e6dc6894e94bac799622` | 8,907 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-diffs/wp52-a-evaluation-coverage-and-data.diff`（提取侧本轮回填材料） | `82f191cd` | `82f191cde1fd9cab6b2a95416ce6102708f91307157e89ee629f8e9b0a193b0b` | 4,337 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-diffs/wp52-a-generic-numerical-and-status-evaluation.diff`（提取侧本轮回填材料） | `7547ce3c` | `7547ce3cc645a0c93453d94c5cf95a4c8dba09ec9f57d0a69903c759797ccb3f` | 4,907 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-diffs/wp52-b-effect-coverage.diff`（提取侧本轮回填材料） | `111fa0b0` | `111fa0b00f50ea851e63408994e864e4d2fbc66cfecea9448934ace5169001a4` | 1,933 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-diffs/wp52-b-field-damage-healing-and-target-evaluation.diff`（提取侧本轮回填材料） | `eb9534be` | `eb9534be5e21363540e6507d1fa745b57d4620d9e6063222a5e772bd11ac6587` | 9,856 |
| `review/wp55-wp57-delivery-2026-09-28/backfill-diffs/wp52-c-items-calling-and-control-evaluation.diff`（提取侧本轮回填材料） | `bcabd536` | `bcabd536ab900a4f1ae224ac659abfd8df98f6defa94f18d8fb7d2cb7c6bada9` | 5,102 |
| `specs/combat/wp55-facility-session-and-restoration.md`（2026-09-29修订v2；ReviewPending） | `0bcff15b` | `0bcff15b2e5683a3b9b96c621ba650b55220131dddf34957d75c39caf83557c7` | 27,698 |
| `specs/combat/wp56-palace-and-arena-variants.md`（2026-09-29修订v2；ReviewPending） | `8ed7940b` | `8ed7940bdd732e8d960a7c5292e1baeacc27489c34dc67f15ffe0501fb4966b0` | 21,274 |
| `specs/creature-rpg/wp57-factory-rentals-and-swaps.md`（2026-09-29修订v2；ReviewPending） | `7e69ccdc` | `7e69ccdccb422d1b04799990041a3745d747ebab3a765b8f7d686ad4f270ef8b` | 14,776 |
| `review/wp55-wp57-delivery-2026-09-28/delivery-summary.md`（本批提取侧交付材料 v2） | `0fcab05d` | `0fcab05d9f13dd9109bf70c699b7c6159dcca43e766524e5529855bc54909ac8` | 6,514 |
| `review/wp55-wp57-delivery-2026-09-28/self-checks.json`（本批提取侧交付材料 v2） | `36704503` | `36704503193cadbd3120ceabf3e2b38cd26274f90ad29f9dd18e7367aa026cb3` | 20,320 |
| `review/wp55-wp57-delivery-2026-09-28/boundary-checks.json`（本批提取侧交付材料 v2） | `8c2033a7` | `8c2033a751f405376cf2375c033c5d6d691e61ff9f296995c71594c9cc49c64c` | 8,670 |
| `review/wp55-wp57-review-2026-09-28/backfill-checks.json`（本轮独立首审原件；未修改） | `6aea56fd` | `6aea56fd1a554b28479c9f61fe0ddf5acf80eb1a5b87368d5b043f56eec2dd22` | 1,765 |
| `review/wp55-wp57-review-2026-09-28/changes-from-previous.diff`（本轮独立首审原件；未修改） | `8fafd983` | `8fafd983b46f1379fb1d9c602ca1554fdd310a57add7957ff14c775974056ce7` | 145,047 |
| `review/wp55-wp57-review-2026-09-28/check_review.py`（本轮独立首审原件；未修改） | `4ca4e9a6` | `4ca4e9a61241ff41635463c024e71b34dbc0ed1b5ce7e1037c1710de3e964d43` | 9,658 |
| `review/wp55-wp57-review-2026-09-28/constant-checks.json`（本轮独立首审原件；未修改） | `277925c1` | `277925c1ac6a5f82f4cdd40966a908e209ac1e770e4d39de750266c0f9d5d9dd` | 3,592 |
| `review/wp55-wp57-review-2026-09-28/coverage-checks.json`（本轮独立首审原件；未修改） | `c4f04dd9` | `c4f04dd9cf4a5c5fb990829a1e049a491c3c5036865474efe23cdfc48a151d8a` | 710 |
| `review/wp55-wp57-review-2026-09-28/current-hashes.tsv`（本轮独立首审原件；未修改） | `b48e6e8f` | `b48e6e8fda1a76b1b2d4e4875a28cf5c969efccfc8604af9fd46a7ccd5c35da3` | 96,071 |
| `review/wp55-wp57-review-2026-09-28/diff-checks.json`（本轮独立首审原件；未修改） | `91ebb22f` | `91ebb22f3a2bfc32bae911879d84b8120a61bd26b261c8c7da99a6a764213366` | 4,039 |
| `review/wp55-wp57-review-2026-09-28/final-checks.json`（本轮独立首审原件；未修改） | `34cde17b` | `34cde17b04ff1e461fafacdbf1e007ac2aed90c2ed27cfd6ecc84d8b5d7a6ee7` | 4,894 |
| `review/wp55-wp57-review-2026-09-28/findings.json`（本轮独立首审原件；未修改） | `65c801fe` | `65c801fe0d637a24e2e897fac75ebe59f6b0b6e31bc0562f63ca449ef6c84a36` | 5,086 |
| `review/wp55-wp57-review-2026-09-28/identity-checks.json`（本轮独立首审原件；未修改） | `83a936ec` | `83a936ecbe0c512fc71113672536b58c093f717dc83c1f84c9821794616ea853` | 1,226 |
| `review/wp55-wp57-review-2026-09-28/input-manifest.json`（本轮独立首审原件；未修改） | `106ba916` | `106ba91621f192d5c67eec0db8058ca6faf83da4b863d0af9fc1960842fb1f4c` | 667,273 |
| `review/wp55-wp57-review-2026-09-28/integrity-checks.json`（本轮独立首审原件；未修改） | `ef07ab70` | `ef07ab7088b890bda12438fed9de8e0bc5a238aca53862c5d899da80b586ff5c` | 4,652 |
| `review/wp55-wp57-review-2026-09-28/report.md`（本轮独立首审原件；未修改） | `1e3d4314` | `1e3d4314e0d4d2d6b6d8b3a83cd3b4d2ed80540b0bc5072268a6a7a5a5ad4531` | 20,977 |
| `review/wp55-wp57-review-2026-09-28/review-notes.json`（本轮独立首审原件；未修改） | `1c56cd76` | `1c56cd76944471a74d244f01c7c6cbc5c2d6248a2c09cdd22ccfec7831680f59` | 6,709 |
| `review/wp55-wp57-review-2026-09-28/revision-prompt.md`（本轮独立首审原件；未修改） | `e5f787e4` | `e5f787e4944979843d860259e15b9988d7739f283a055be2ec33df04abcc9244` | 11,926 |
| `review/wp55-wp57-review-2026-09-28/source-checks.json`（本轮独立首审原件；未修改） | `88ac4840` | `88ac4840156085c64dcd6dfc70b0ff3c86f2d4b5d251b0bc4b59c43277141f2d` | 8,698 |
| `review/wp55-wp57-review-2026-09-28/revision-response.md`（提取侧本轮修订回应） | `0da546c0` | `0da546c0a7451250bbe08963f937b95e4d405a0ebcac783ea764e142c97d7f93` | 21,627 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/feature-matrix.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `e12e4973` | `e12e497324089b153dd1d940339d8b68dc22cbb5b25c36136355a106ad39d042` | 4,533 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/wp52batch-delivery-summary.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `3aefcc03` | `3aefcc03e3d639711d6be624065dc4f84d5919fef5802f025e7d03f484e691b7` | 6,306 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/wp52batch-self-checks.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `febc9b20` | `febc9b202bef4b82f2fa0d5bdd32c321119fdb12bc41e43a6fca9884ca75a09b` | 5,524 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/wp55-facility-session-and-restoration.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `1f83970b` | `1f83970bf529cbf82bf2a9233494fd6f4c5c8eb99cf8973694f1abe5bbc69da2` | 32,656 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/wp55batch-backfill-response.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `6ebde6c1` | `6ebde6c105fd8faf6f49cb7b3fc70ee13531070d178bc21a348148ac04425a4c` | 3,678 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/wp55batch-boundary-checks.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `005ca7f4` | `005ca7f49b2838429527619422056a57bc64b563b8536d72614bb4160cf9264d` | 7,265 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/wp55batch-delivery-summary.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `70cae3ff` | `70cae3ff72ae0fdcbac9622aa368ccb17951ef2a8980b7f94ea511fab194f7f7` | 11,123 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/wp55batch-self-checks.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `a64bbadc` | `a64bbadc6906fca7456d39133c87fdc6be23d5c6387f9f82aae52acca8447848` | 10,973 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/wp56-palace-and-arena-variants.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `4056a317` | `4056a317823845c98f871ede78ddce571d5f8e38f4dd110e5c17db3e02a957dd` | 26,038 |
| `review/wp55-wp57-review-2026-09-28/revision-diffs/wp57-factory-rentals-and-swaps.diff`（提取侧本轮修订差异，相对本轮input-snapshot） | `bc9a93be` | `bc9a93be1eb7828861534d967d94255a6611060cdc590db232767c8e8cda377d` | 17,497 |

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
- 2026-09-26 WP17 闭合复审与状态回填：外部闭合复审 PASS_SCOPED（R01 最后两处与 C02 关闭、R02～R05/C01 继承关闭、未发现回归）；复审实测 manifest（`d3bef580`，53,195 字节）98 条记录全部匹配，被审 WP17 v3 `6010f40b`、附表 v2 `e01466ef` 与本工作区回填前实测一致。按闭合报告 §5 范围将主文档回填 **Reviewed**（管理性变更；被审哈希 `6010f40b` 保留于第 3 节历史，回填后 `bb61f967`、30,047 字节不伪称为复审对象）；附表未加状态注记、字节不变（`e01466ef` 继续有效）。feature-matrix F05-05/F05-06 同步各自 WP17 子范围为 Reviewed、保留前向 Inventoried，矩阵由 `5aecfd39` 变为 `fb109386`（35,656 字节）。闭合报告（`8a36381b`）与执行提示（`da7a0ed3`）原件登记于第 1 节。
- 2026-09-26 WP18–WP20 批次交付（首次送审，批内固定未外审）：三包首版固定为 WP18 `7ab818e2`（34,100 字节）、WP19 `3cba4bcd`（30,963 字节）、WP20 `84c29af6`（29,018 字节）；WP19 引用 WP18、WP20 引用 WP18/WP19 的批内哈希已同步一致。feature-matrix 经八个 Feature 增量（F06-01/02/03/04/05/06、F07-01、F08-05，均 ReviewPending＋前向 Inventoried）由 `fb109386` 变为 `c7c09d7b`（38,071 字节）。管理与批次差异、完整哈希与字节数见 `review/wp18-wp20-delivery-2026-09-26/`（`52da6bbf`/`57025ecc`/`7d04f964`/`bcd3d0e4`）。本批不自行升级 Reviewed；WP21 未启动。
- 2026-09-26 WP18–WP20 首轮独立复审与 v2 修订：复审报告（`2f8b22e3`）结论三包均 REQUEST_CHANGES（9 项必修、2 项非阻塞维护；WP17 回填接受；107 条 manifest 记录与固定输入匹配）。修订前实测三包 v1、矩阵与 manifest 与复审 report.md 第 1 节固定版本全部一致，意见适用。11 项**全部核实认可**并修订：WP18-R01/R02；WP19-R01～R04（含 WP19-R04 传播至 WP18）；WP20-R01～R03（含 C01 引用维护）；BATCH-C01/C02。修订后 v2：WP18 `3d30f3f1`（35,885 字节）、WP19 `252649f7`（35,222 字节）、WP20 `d595b1b2`（33,864 字节）；批内互引全部同步（WP19→WP18、WP20→WP18/WP19）。矩阵经状态措辞与还原记录措辞同步为 `3129eacc`（38,176 字节）。逐项回应 `aea5c122`、差异 5 份（`a5f7283d`/`fe6c4de9`/`e8ba1b68`/`09014951`/`26aa5906`）；交付摘要 v2 `ddf85f73`、TSV v2 `cdb89a96`。v1 被审哈希保留于第 3 节历史；三包保持 **ReviewPending**，未自批 Reviewed。
- 2026-09-26 WP18–WP20 定点复审与 v3 修订／WP20 回填：复审报告（`18356917`）结论 **WP20 PASS_SCOPED、WP18/WP19 仅剩 WP18-R01 两处**（其余 8 项必修与 C01/C02 CLOSED）；修订前实测五项被审对象与 report.md 第 1 节固定版本全部一致。按报告 §3 修订为 v3：WP18 `4428049b`（36,889 字节）、WP19 `6c669fcf`（35,935 字节）；按 §5 将 WP20 回填 **Reviewed（限定范围）**（管理性变更；被审哈希 `d595b1b2` 保留于第 3 节历史，回填后 `f8272acf`、35,018 字节不伪称为复审对象；含 §4 允许的 C03 简写同步与批内引用同步至 v3）。矩阵 F06-05/F06-06/F08-05 → Reviewed（WP20 子范围）＋前向 Inventoried，F06-01/02/07-01、F06-03/04 更新为"v2 已送定点复审、剩 WP18-R01（及传播）"，矩阵 `3129eacc` → `5fc73d82`（38,333 字节）。逐项回应 `07a481ab`、差异 5 份（`709c73f9`/`d299a14b`/`5aa23ca0`/`113a1fbe`/`8c15d66d`）；交付摘要 v3 `f014b114`、TSV v3 `ef231e80`。WP18/WP19 保持 **ReviewPending**；WP20 回填为管理性变更、无需另等外审。
- 2026-09-26 WP18–WP20 闭合复审与 WP18/WP19 回填：外部闭合复审（报告 `93f1de1c`）结论 **WP18/WP19 PASS_SCOPED**（WP18-R01 最后两处关闭、其余继承关闭、未发现回归）、**WP20 回填接受**；复审实测 123 条 manifest 记录与 27 条交付哈希全部匹配，五项固定对象与本地实测一致。按报告 §4 将 WP18/WP19 回填 **Reviewed（限定范围）**（管理性变更；被审哈希 `4428049b`/`6c669fcf` 保留于第 3 节历史，回填后 `85368fe3`/`489984f7` 不伪称为复审对象）；WP20 上游引用同步为 `f2f904e5`（管理性）。矩阵 F06-01/F06-02/F07-01、F06-03/F06-04 → Reviewed（对应子范围）＋前向 Inventoried，矩阵 `5fc73d82` → `528f38aa`（38,158 字节）。**至此 WP01–WP20 全部限定 Reviewed**；下一批授权：WP21→WP24→WP25。
- 2026-09-26 WP21–WP25 批次交付（首次送审，批内固定未外审）：三包首版固定为 WP21 `5a5ef9ca`（30,245 字节）、WP24 `45370acd`（24,659 字节）、WP25 `920b0943`（21,310 字节）；WP25 引用 WP24 的批内哈希（注明尚未外审）。feature-matrix 经五个 Feature 增量（F06-07、F07-02/F07-03、F07-04/F07-05，均 ReviewPending＋前向 Inventoried）由 `528f38aa` 变为 `5379d879`（39,456 字节）。管理与批次差异、完整哈希与字节数见 `review/wp21-wp25-delivery-2026-09-26/`（`d29d177a` 摘要；回填差异 3 份 `278faeda`/`5b760f9c`/`98cb92a4`）与 v4 TSV `a5a2ded7`。本批不自行升级 Reviewed；WP22/WP23/WP26 未启动。
- 2026-09-26 WP21–WP25 首轮独立复审与 v2 修订：复审报告（`a6354444`）结论三包均 REQUEST_CHANGES（12 项必修＋BATCH-C01 一组；WP18/WP19 回填与 WP20 引用同步接受；132 条 manifest 记录与交付哈希匹配）。修订前实测三包 v1、矩阵、manifest 与 report.md 第 1 节固定版本完全一致。12 项**全部核实认可**并修订：WP21-R01～R06（注册机制改用真实底层；目录校数与取值数据六表；招式三类路径与跳项例；标记双界面差异；缎带升级/移除边界；Beauty 消费者与复制接收路径）；WP24-R01～R03（编号三层语义；伙伴分阶段/再读取/谓词/收尾双分支；金钱守卫与分阶段统计）；WP25-R01～R03（容量与 clear/直写；地区代理差异分列；界面守卫条件化）；BATCH-C01（WP19 引用文字、WP25 同批措辞、DARMANITAN 简写、笔误与责任包号）。修订后 v2：WP21 `55a47313`（40,922 字节）、WP24 `8b06ddc4`（28,865 字节）、WP25 `98b52717`（26,359 字节）；WP25 引用 WP24 同步；矩阵 `5379d879` → `bb037cea`（39,516 字节）；WP19 管理性同步 `489984f7` → `03167162`（36,381 字节）。逐项回应 `34a3fb5e`、差异 6 份（`7b8eb22a`/`cf748fc8`/`3b15e838`/`68debf8b`/`991e2b8f`/`0f822f78`）；交付摘要 v2 `c88e1e5b`、TSV v5 `7db3b12b`。v1 被审哈希保留于第 3 节历史；三包保持 ReviewPending。
- 2026-09-26 WP21–WP25 定点复审（recheck）与 WP21-R03 修订／WP24、WP25 回填：复审报告（`f2dc78d2`，11,521 字节）结论 **WP24/WP25 PASS_SCOPED、WP21 仅剩 WP21-R03**（原 12 项中 11 项与 BATCH-C01 CLOSED；BATCH-C02 非阻塞、随本轮同步）；复审实测 141 条 manifest 记录匹配、收尾输入未变。修订前实测五项固定对象（WP21 `55a47313`/40,922、WP24 `8b06ddc4`/28,865、WP25 `98b52717`/26,359、矩阵 `bb037cea`/39,516、manifest `a3b5b28f`/86,871）与报告 §1 及 `input-snapshot/` 完全一致。按报告 §3 修订 WP21（v3 `4e475505`，42,037 字节：直接换招标识保留槽位/PP 提升计数、当前 PP 按新招式总 PP 钳制；15→5、3→3 对照）并同步 BATCH-C02 三包简写；按 §5 将 WP24（`32594094`，29,668 字节）、WP25（`46bd905d`，27,081 字节）回填 **Reviewed（限定范围）**（含 C02 同步与 WP25→WP24 引用同步；被审 `8b06ddc4`/`98b52717` 保留于第 3 节历史，回填后新哈希不伪称为复审对象）；WP21 保持 **ReviewPending**。矩阵 `bb037cea` → `e0762970`（39,590 字节；F07-02～F07-05 → Reviewed＋前向 Inventoried，F06-07 措辞更新）。逐项回应 `7b5d3775`、差异 5 份（`d812eabe`/`91b61274`/`96c2046a`/`a82406ba`/`30f62f8b`）；交付摘要 v3 `62d8a2c8`、TSV v6 `4c66bcb4`。复审报告与提示原件登记于第 1 节。
- 2026-09-26 WP21–WP25 闭合复审与 WP21 回填：闭合复审（报告 `12e283ae`，8,339 字节）结论 **WP21 PASS_SCOPED**（WP21-R03 最后剩余与 BATCH-C02 CLOSED、未发现直接回归），**WP24/WP25 继承 PASS_SCOPED、回填接受**；复审实测 149 条 manifest 记录与 53 条交付哈希全部匹配、固定 158 项输入。回填前复算六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。按报告 §4 将 WP21 回填 **Reviewed（限定范围）**（管理性变更；被审 v3 `4e475505` 保留于第 3 节历史，回填后 `19a36297`/42,449 字节不伪称为复审对象）；同步 WP18（`85368fe3` → `0464ca07`，37,313 字节）、WP19（`03167162` → `c7fb40fa`，36,406 字节）、WP25（`46bd905d` → `edc275c5`，27,058 字节）对 WP21 状态的引用。矩阵 F06-07 → Reviewed（WP21 子范围）＋前向 Inventoried，矩阵 `e0762970` → `8b83d668`（39,577 字节）。回填回应 `90961bb0`、差异 6 份（`a4926019`/`4f754254`/`7958529b`/`1369e8b9`/`118a8d31`/`b5aa766b`）；交付摘要 v4 `8d8b7e5d`、TSV v7 `679338ea`。**至此 WP01–WP21、WP24、WP25 限定 Reviewed**（WP22/WP23 未完成，不得概括为全部通过）。
- 2026-09-26 WP26–WP30 批次交付（首次送审，批内固定未外审）：三包首发固定为 WP26 `793473a0`（27,898 字节）、WP27 `fe14af5d`（21,719 字节）、WP30 `5972e119`（28,244 字节）；三包均为新文件（无前版替代关系）、无批内互引，上游引用均为已限定通过包。feature-matrix 经六个 Feature 增量（F07-06、F10-05、F08-01、F08-02、F09-01、F09-02，均 ReviewPending＋各自范围）由 `8b83d668` 变为 `af8328ee`（40,955 字节）。交付材料见 `review/wp26-wp27-wp30-delivery-2026-09-26/`（摘要 `9c713161`；矩阵合并差异 `c8b70094`）与 v8 TSV `08ced51b`。本批不自行升级 Reviewed；WP22/WP23/WP28/WP29/WP31 未启动。
- 2026-09-26 WP26–WP30 首审与 v2 修订：首审报告（`78a9ba42`，25,241 字节）结论 **REQUEST_CHANGES**（WP26 4 项、WP27 3 项、WP30 6 项必修＋2 项非阻塞维护；WP21 管理性回填接受、既有限定通过保留）。修订前实测六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。**13 项与 2 项维护全部核实认可并修订**：WP26-R01（入口/返回值/选择结果分列）、R02（昵称保留与外来参数语义）、R03（入盒治疗继承；对等方对象按常规战斗接入、不称联机）、R04（容量复检条件可达与条件反例）；WP27-R01（接收/拾取/奖品直接添加分列）、R02（登记三层守卫）、R03（过滤游标恢复）；WP30-R01（非法经验失败阶段与原始 setter 分列）、R02（表外公式与 L101 边界向量）、R03（席位归属/外来二选一/背包护符/回退条件）、R04（Shadow 暂存实际写入）、R05（wing 调用链与友友球）、R06（重学三层取消）；BATCH-C01/C02。修订后 v2：WP26 `67056812`（33,910 字节）、WP27 `0a6a28f7`（25,961 字节）、WP30 `114038f3`（34,957 字节）；矩阵 `af8328ee` → `c4505715`（41,308 字节；六行版本说明）；交付摘要 v2 `dd06a4bd`（9,731 字节）。逐项回应 `2765129f`、差异 5 份（`a7855f91`/`0a329ee2`/`4e89689c`/`edf6b1fb`/`097b56e4`）；TSV v9 `ec86e13d`。三包保持 **ReviewPending**，送原编号与直接回归复审；被审 v1 哈希保留于第 3 节历史。
- 2026-09-26 WP26–WP30 v2 复审与 v3 收尾：复审报告（`8c23dfa1`，16,221 字节）结论仍 REQUEST_CHANGES：**8 项必修与 BATCH-C01/C02 CLOSED，仅剩 WP26-R02/R04、WP27-R01/R02、WP30-R05**。修订前实测六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。**五项与 C03 维护全部核实认可并修订**：WP26-R02（管道名单删除外来赠送）、WP26-R04（"仅队伍"限定初始检查；内层复检无值返回、外层仍 true；§7 拆入口初检/内层复检）、WP27-R01（预检/添加场景分列）、WP27-R02（菜单"已登记 -> 取消"优先分支）、WP30-R05（羽毛只绕 100 点阈值、仍受 252/510；三向量）；C03（治疗条件检查对象、"配对预检仅…"限定、过滤"打开前重置"限带谓词、均分两份额按资格、"同上"锚定、通用版标签、setter 引用章节）。修订后 v3：WP26 `afc7214a`（35,387 字节）、WP27 `969cb37c`（27,166 字节）、WP30 `41e71624`（36,040 字节）；矩阵 `c4505715` → `6b49c40b`（41,342 字节；六行"仅剩具名项"）；交付摘要 v3 `df4926ae`（11,682 字节）。逐项回应 `8a4ee716`、差异 5 份（`237ae5f3`/`5add2f96`/`c684dcb1`/`e3c3e241`/`fb5a69fd`）；TSV v10 `35cd3605`。三包保持 **ReviewPending**，送五项及直接回归短复审；被审 v2 哈希保留于第 3 节历史；首轮回应 R05 简写已在本轮纠正（旧回应保留历史）。

- 2026-09-26 WP26–WP30 闭合回填与 WP31→WP28→WP29 批次（本轮）：闭合复审报告 `21712a5c`（11,449 字节）与提示 `8091fed2`（12,982 字节）——**WP26/WP27/WP30 均 PASS_SCOPED**、最后五项关闭、未发现直接回归、C03 随回填；回填前实测六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。按 §4 回填三包 **Reviewed（限定静态范围）**（被审 v3 `afc7214a`/`969cb37c`/`41e71624` 保留历史；回填后 `c87101ad`/35,738、`8064f172`/27,516、`6fbc5a20`/36,970 不伪称为复审对象）；C03 三项同步（WP30 §12.2 锚定与 Shadow 前提承接、`008_PokemonBag.rb` 笔误更正、"整批 8 项关闭"历史语境）；必要状态引用同步（管理性：WP18 `54b54743`/37,399、WP19 `1c4325f5`/36,443、WP20 `9a2ad1ab`/35,027、WP21 `b5eeb48e`/42,498、WP25 `f505afd5`/27,107）。同会话执行 **WP31→WP28→WP29**：三包批内固定为 WP31 `b5966bbf`/35,629、WP28 `f9cd5fe3`/32,848、WP29 `3705047f`/21,918（均 ReviewPending、尚未外审；WP28 引用 WP31 批内哈希并随级联同步）；批末四项交界通过（含 WP31 对 WP18 引用由 §4.1 修正为 §3.4 及级联重固定）。矩阵六行回填与四行增量后为 `cbf671a8`/42,243；交付材料见 `review/wp31-wp28-wp29-delivery-2026-09-26/`（回应 `fd800ef2`、自检 `f22d8fdc`、交界 `63fb993b`、摘要 `3f832427`、回填与引用同步差异 10 份）；WP26–WP30 交付摘要 v4 `bdd353fd`/13,366；TSV v11 与第三十六轮登记见 §1/§3/§4。

- 2026-09-27 WP31／WP28／WP29 首审修订（v2，本轮）：首审报告 `5e34d822`（21,709 字节）与提示 `13d32a4b`（10,673 字节）——**REQUEST_CHANGES**（WP31×2、WP28×6、WP29×2 必修＋BATCH-C01/C02；205 条 manifest 与 109 条 TSV 匹配）；WP26–WP30 回填与五份上游同步获接受。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致；**10 项与两组维护全部核实认可并修订**（WP31-R01 事件编号非一次性、R02 形态/性别例外；WP28-R01 分流返回、R02 集合/返回/库存、R03 数量/应用/扣除分列、R04 战斗退回分支、R05 具体效果、R06 形态/融合使用表；WP29-R01 库存原地过滤、R02 价格层级/旧覆盖保留）。修订后 v2：WP31 `e541c650`/39,138、WP28 `f2f7618c`/42,586（级联 WP31 引用）、WP29 `d5c847f1`/25,211；矩阵 `cbf671a8` → `a05c39f4`/42,454（四行"首审已送审：REQUEST_CHANGES，修订后再送"）；交付摘要 v2 `023c090e`/10,914。逐项回应 `e516ca69`、差异 5 份（`1353e3c2`/`30f91d9a`/`b5b287d9`/`ce3183ac`/`0db55cfc`）；被审首版哈希保留历史；TSV v12；本轮送审材料（报告/提示/检查/清单）登记于第 1 节。三包保持 ReviewPending（首审修订后再送）；未自批 Reviewed。

- 2026-09-27 WP31 回填与 WP28／WP29 三点收尾（本轮）：有限复审报告 `f6f2c705`（12,842 字节）与提示 `bcef7f46`（7,465 字节）——**WP31 PASS_SCOPED（已回填 Reviewed（限定静态范围））**；WP28/WP29 仍 REQUEST_CHANGES，原 10 项关闭 7 项，仅剩 **WP28-R03/R06、WP29-R02**；222 条 manifest 与 126 条 TSV 匹配。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致；三项与 C03 记法全部核实认可并修订——WP28-R03（删"羽毛无多量"、恢复数量上限三层；羽毛多量/WING 别名向量）、WP28-R06（§6.8 删全局"物品种类不变"，具名替换随 §5.6/§3.3）、WP29-R02（合法 `setPrice(D,-1)`/`setSellPrice(D,-1)` 保留例子；BP 拆"通过/拒绝/复查前提"）；C03（两层命名、检查通过后、最后路径速记、MAXHONEY）。修订后：WP31 回填 `ee47f124`/39,499（被审 v2 `e541c650` 保留历史、不伪称）；WP28 `7e10cb25`/43,917（级联 WP31 回填后引用；被审 v2 `f2f7618c` 保留历史）、WP29 `1ed4b957`/25,793（被审 v2 `d5c847f1` 保留历史）；矩阵 `a05c39f4` → `909080cb`/42,493（F09-03 → Reviewed（WP31 子范围）＋前向 Inventoried；余量行"仅剩三点已修订"）；交付摘要 v3 `6b22ac03`/13,286。逐项回应 `73c9cab3`、差异 5 份（`4d5e843d`/`85df9c4c`/`f9930cb9`/`2688d197`/`08809ecd`）；TSV v13；本轮送审材料（报告/提示/检查/向量）登记于第 1 节。WP28/WP29 保持 ReviewPending；不得写成 WP01–WP31 连续全部完成。

- 2026-09-27 WP28／WP29 回填与 WP33→WP34→WP35 批次（本轮）：闭合复审报告 `8d56d23e`（8,920 字节）与提示 `a9e31d54`（12,960 字节）——**WP28/WP29 均 PASS_SCOPED、WP31 继承 PASS_SCOPED 且回填接受**；最后三项（WP28-R03/R06、WP29-R02）与 C03 全部关闭、未发现直接回归（238 条 manifest 与 142 条 TSV 匹配、固定 240 项输入）。回填前实测六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。按报告 §4 回填两包 **Reviewed（限定静态范围）**：被审 v3 `7e10cb25`/43,917、`1ed4b957`/25,793 保留历史，回填后 `a4ccb383`/44,159、`f7788c7d`/26,053 不伪称为复审对象；矩阵 F08-03/F08-04、F08-06 → Reviewed（对应子范围）＋前向 Inventoried（`909080cb` → `77c3bff0`/43,092）。必要状态引用同步（管理性，6 文件）：WP18 `55fb5004`/37,448、WP19 `cd3dcf4b`/36,492、WP20 `05a59789`/35,076、WP27 `6ac234e4`/27,602、WP30 `b9f58991`/37,019、WP31 `0b40917c`/39,554。**自此限定通过集合＝WP01–WP21、WP24–WP31**（WP22/WP23 未完成，不得写成连续全部通过）。同会话按提示串行执行 **WP33→WP34→WP35**：三包批内固定为 WP33 `4e17c679`/21,180、WP34 `bb950920`/24,359、WP35 `61a6bdb9`/19,715（均 ReviewPending、批内固定、尚未外审；WP34 引用 WP33、WP35 引用 WP34 的批内哈希）；批末四项交界通过（WP33×WP25/27/30/06/24、WP34×WP18/19/20/21/33、WP35×WP34/12/25/26/06/09、追踪一致性）。矩阵经 F09-05/F09-06/F09-07 增量（ReviewPending（各自范围）＋前向 Inventoried）为 `77c3bff0`/43,092；交付材料见 `review/wp33-wp35-delivery-2026-09-27/`（回应 `64a8884e`、自检 `581b530f`、交界 `7bf8c59e`、摘要 `8c420fa7`、回填与引用同步差异 10 份）；旧批摘要 v4 `990f30b4`/14,649；TSV v14 `7368bba6`/23,314（168 行）；闭合报告与提示原件登记于第 1 节。WP33–WP35 未自批 Reviewed。

- 2026-09-27 WP33／WP34／WP35 首审修订（v2，本轮）：首审报告 `7f61f821`（19,379 字节）与提示 `2ad9d012`（11,396 字节）——**REQUEST_CHANGES**（WP33×2、WP34×3、WP35×3 必修＋BATCH-C01/C02；264 条 manifest 与 168 条 TSV 匹配、固定 266 项输入；WP28/WP29 回填与六份状态引用同步获接受）。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致；**8 项与两组维护全部核实认可并修订**（WP33-R01 入口门控与副作用分层、R02 共享招式方向/接受表/首项；WP34-R01 单次交换与 Ditto 招式矩阵、R02 熏香样本、R03 创建随机/派生缓存/重掷；WP35-R01 归零与防重属迈步调用者、R02 HatchSteps 三层与摘要四段、R03 拥有者重写后异色；C01 迁移反例/经验前提/加速扫描时点；C02 JSON 引号修复、WP34 链接、取证范围、措辞）。修订后 v2：WP33 `6cb65468`/24,789、WP34 `7ba35a9d`/29,265（级联 WP33 修订稿引用）、WP35 `0abe2622`/24,219（级联 WP34）；矩阵 `77c3bff0` → `243df4e4`/43,258（F09 三行"首审已送审：REQUEST_CHANGES（已修订（v2），待复审）"）；交付摘要 v2 `462ee890`/8,745；boundary-checks JSON 修复为 `80dcc8aa`/2,877（修复前 `7bf8c59e`/2,875）；修订材料：回应 `74a9a812`/13,495、差异 6 份（`cb3f73bc`/`58ea7025`/`ab745492`/`d134a2e5`/`c0531217`/`a81c596f`）；TSV v15 `44da94e7`/25,692（186 行）；首审报告/提示/检查 11 份登记于第 1 节。被审首版哈希保留历史；三包保持 ReviewPending（首审修订后再送）；未自批 Reviewed。

- 2026-09-27 WP33／WP35 回填与 WP34-R03 收尾（v3，本轮）：v2 复审报告 `6314bd64`（13,517 字节）与提示 `d8379990`（8,009 字节）——**WP33／WP35 均 PASS_SCOPED（管理性回填）、仅剩 WP34-R03 末次普通异色缓存时点**；原八项中七项关闭、R03 的 Nature/随机输入部分与 C01/C02 保留关闭；282 条 manifest 与 186 条 TSV 匹配、固定 284 项输入。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。**WP34-R03 收尾**：§8.2 步 2/3/4 改为"轮首读取→命中停止；未命中清缓存并换号→下一轮或退出"、用尽次数退出时普通异色缓存为空（收尾不补读）、零次不读取/不清；§9.9 与 §13.2 同步（新增 N=2 用尽时点对照与 PID0/N0 对照行）。**回填（管理性）**：WP33 `8c678e33`/25,144、WP35 `315e74f6`/24,540 登记 **Reviewed（限定静态范围）**（被审 v2 `6cb65468`/`0abe2622` 保留历史）；WP34 `d0113d76`/30,617（v3，级联 WP33 回填后哈希；待短复审）。矩阵 F09-05/F09-07 → Reviewed（对应子范围）、F09-06 保持（"仅剩 R03 末次缓存（v3 已修订、待短复审）"），矩阵 `243df4e4` → `17fa287c`/43,198。级联：WP35 引用 WP34 v3 `d0113d76`。C03 记法同步（事件层责任表述、领取引用 §5.3、濒死非蛋成员仍可提供加速）。交付摘要 v3 `28cbc965`/9,383；收尾材料：回应 `0188ef21`/7,329、差异 5 份（`7c957def`/`422f4446`/`6b739e7f`/`46131c4f`/`82e5042e`）；TSV v16 `a756e2ee`/27,947（203 行）；v2 复审材料 11 份登记于第 1 节。**限定通过集合增加 WP33、WP35**（原 WP01–WP21、WP24–WP31 保留；WP22/WP23/WP32/WP34 未完成，不得写成连续全部通过）。

- 2026-09-27 WP34 回填与 WP59→WP36→WP60 批次（本轮）：闭合复审报告 `90c20faf`（10,068 字节）与提示 `f791c8c2`（15,325 字节）——**WP34 v3 PASS_SCOPED、无剩余必修**；WP33／WP35 回填与 C03 获接受；299 条 manifest 与 203 条 TSV 匹配、固定 301 项输入。回填前实测六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。**WP34 回填（管理性）**：头部/§16 登记 **Reviewed（限定静态范围，2026-09-27 闭合复审 PASS_SCOPED）**；被审 v3 `d0113d76`/30,617 保留历史，回填后 `8e3511d3`/30,758 不伪称为复审对象；矩阵 F09-06 → Reviewed（WP34 子范围）＋前向 Inventoried；WP35 引用同步 `34e83236`/24,583；旧批摘要 v4 `6b1d9a1a`/9,924。**自此限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP35**（WP22/WP23/WP32 未完成）。同会话执行 **WP59→WP36→WP60**：四份产物批内固定为 WP59 `971b0807`/34,153、WP36 `b8a5bc26`/27,307、WP60 树果 `227bb696`/20,545、WP60 钓鱼 `b7de3ff4`/16,866（均 ReviewPending、批内固定、尚未外审；WP36 引用 WP59、WP60 双产物引用 WP59/WP36 批内哈希）；批末五组交界通过（WP59×WP06/11/12/20/24、WP36×WP59/03/19/24、WP60 树果×WP59/27、WP60 钓鱼×WP36/59/12/14、追踪一致性）。矩阵六 Feature 增量（F10-01/02、F14-01～04 → ReviewPending（各自范围）＋前向 Inventoried）后为 `64d297de`/44,540；交付材料见 `review/wp59-wp36-wp60-delivery-2026-09-27/`（回填回应 `8ab43cb9`、摘要 `407c61a5`、自检 `86348342`、交界 `cef81335`、回填差异 4 份）；TSV v17 `aec34bd2`/30,842（225 行）；闭合轮材料 10 份登记于第 1 节。三新包未自批 Reviewed。

- 2026-09-27 WP59／WP36／WP60 首审修订（v2，本轮）：首审报告 `e9750d3b`（26,473 字节）与提示 `53a04e9a`（15,388 字节）——**REQUEST_CHANGES**（WP59×4、WP36×4、WP60×5 必修＋BATCH-C01/C02；321 条 manifest 与 225 条 TSV 匹配、固定 323 项输入；WP34 回填与 WP35 必要引用同步获接受、既有限定通过保留）。修订前实测七项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。**13 项与两组维护全部核实认可并修订**（WP59-R01 天气 duration/强度分层与编辑器 nil、R02 入口×检查×确认×效果矩阵、R03 返回与异常分阶段、R04 月相/星座完整规则与 tone 缓存；WP36-R01 整数折算/宽限分母取整/重置入口、R02 入口禁用与早退清理、R03 版本枚举反例、R04 迷人身躯三分支与首非蛋口径；WP60-R01 精灵链不推进与 6h/10h 向量、R02 施肥取消不回滚与采摘次序、R03 Yield 缺省三层；WP60-R04 资格标志/公共事件前提、R05 等待段＋1/抖动八槽/阈值 68%；C01 26 类型/IV 重算/雨粒子左下与每秒/24×24 中间量/机制标记与设置分离；C02 WP35 头部与钓鱼 §1 引用同步）。修订后 v2：WP59 `440a67b1`/40,114、WP36 `3120d1e1`/32,592（级联 WP59 v2）、树果 `e468c3bf`/24,593（级联）、钓鱼 `f280e9a7`/20,304（级联＋C02）；矩阵 `64d297de` → `b580eb92`/44,780（六行"首审 REQUEST_CHANGES，已修订为 v2、待复审"）；交付摘要 v2 `835334ef`/10,390（短标签笔误 835334ee 于第四十四轮更正）；self-checks v2 `4f9c02d8`/11,965、boundary-checks v2 `b12ebefd`/6,271；WP35 头部引用同步 `1fbfd98e`/24,610（管理性）。修订材料：回应 `97c5be51`/19,116、差异 9 份（`a7c2a109`/`1f9a2df4`/`4a34f1c6`/`0c8f94ce`/`5b0aeac7`/`ffc170bd`/`5ec19ea2`/`9214e3df`/`3f7e50a9`）；TSV v18 `a8eb500f`/33,716（246 行）；首审报告/提示/检查 11 份登记于第 1 节。被审 v1 哈希保留历史；四产物保持 ReviewPending（各自具名范围，首审修订后再送）；未自批 Reviewed。

- 2026-09-27 WP59／WP36／WP60 v2 复审收尾（v3，本轮）：v2 复审报告 `173ac1dc`（16,199 字节）与收尾提示 `16953dad`（9,341 字节）——**REQUEST_CHANGES**：原 13 项中 9 项关闭，仅剩 **WP59-R02、WP59-R04、WP36-R02（含钓鱼直接传播）、WP60-R01**（342 条 manifest 与 246 条 TSV 匹配、固定 344 项输入；C02 关闭、WP35 管理性同步接受、既有限定通过保留）；C01 只剩 IV 重算简写未同步、另列 C03 登记／场景维护。修订前实测七项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。**四项与 C01 剩余、C03 全部核实认可并收尾修订**（WP59-R02 FLY CanUse 列与 DEBUG 总括；WP59-R04 完整整数日数学／2299160 精确门／星座全 12 行表／旧零色调不变量删除；WP36-R02 终态按入口分列与钓鱼 §7 传播；WP60-R01 范围行与 6h→阶段3/水分10/惩罚0 场景、雨浇水 update 前提；C01 IV 至多 4 轮、环后统一重算一次；C03 短标签 835334ef、旧回应段标题更正、3 秒向量起始条件、钓鱼概率分列与仅潜水前提、树果终态标注）。修订后 v3：WP59 `9a41d185`/42,041、WP36 `d21edcc7`/33,424、树果 `114c432b`/24,912、钓鱼 `5f274a2c`/20,759；矩阵 `b580eb92` → `1de3852f`/44,896（六行"9/13 关闭＋四项已收尾修订为 v3、待复审"）；交付摘要 v3 `809e0fa0`/12,097；self-checks v3 `3bad9fd6`/12,955、boundary-checks v3 `db51d641`/6,903。收尾材料：回应 `233fd124`/13,082、差异 8 份（`8c772de5`/`9a109faa`/`783880a4`/`faded8c8`/`8810fb3e`/`8fe7889c`/`ae9e21ca`/`f35089b1`）；TSV v19 `d2e72991`/36,452（266 行）；v2 复审材料 11 份登记于第 1 节。被审 v2 哈希保留历史；四产物保持 ReviewPending（各自具名范围，复审后再送）；未自批 Reviewed。

- 2026-09-27 WP59／WP36／WP60 闭合回填与 WP39→WP40→WP41 批次（本轮）：闭合复审报告 `25835002`（12,741 字节）与回填提示 `11123b46`（17,658 字节）——**PASS_SCOPED**：原 13 项全部关闭、C01/C02/C03 接受；362 条 manifest 与 266 条 TSV 匹配、固定 364 项输入。回填前实测七项固定对象与报告 §1 及 `input-snapshot/` 完全一致。**四产物管理性回填 Reviewed（限定静态范围）**（被审 v3 `9a41d185`/`d21edcc7`/`114c432b`/`5f274a2c` 保留历史；回填后 `46e80106`/42,401、`5a05aad7`/34,305、`1d588f0a`/25,082、`e5d94e05`/20,950，不伪称为复审对象）；**C04 两处记法**（WP59 年调整括注方向、WP36 终态场景按入口拆分＋临时标记注释）；矩阵六行 → Reviewed（对应子范围）＋前向 Inventoried；必要状态引用同步（管理性）：WP34 §11 与导入语、WP35 对 WP34 回填后哈希 `46acc90f`/30,716。**回填后限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP59–WP60**。同会话执行 **WP39→WP40→WP41**：三包批内固定为 WP39 `26c72739`/34,016、WP40 `3ced6de7`/33,115（引用 WP39）、WP41 `75746653`/23,900（引用 WP40），均 ReviewPending、尚未外审；批末五组交界通过（WP39×WP20/24/25/11/02 及 WP36/59、WP40×WP39/19/20/27/28、WP41×WP39/40/27、持久与临时状态、追踪一致性）。矩阵 F11-01～F11-05 增量后为 `0d6a0c9c`/45,993；交付材料见 `review/wp39-wp41-delivery-2026-09-27/`（回填回应 `57e53a70`、摘要 `f23ddcb0`、自检 `469c9b30`、交界 `4d942a4e`、回填差异 8 份）；旧批摘要 v4 `6d74f799`/12,913；TSV v20 `e4054253`/39,875（291 行）；闭合轮材料 10 份登记于第 1 节。三新包未自批 Reviewed。

- 2026-09-27 WP39／WP40／WP41 首审修订（v2，本轮）：首审报告 `a539db6c`（23,770 字节）与有限修订提示 `543b6f14`（14,362 字节）——**REQUEST_CHANGES**（WP39×3、WP40×5、WP41×4 必修＋C01/C02；387 条 manifest 与 291 条 TSV 匹配、固定 389 项输入；旧批回填接受、既有限定通过保留）。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。**12 项与两组维护全部核实认可并修订**（WP39-R01 单次构造与时间线、R02 九布局全表/全局索引/缩减前提、R03 写入方向分层；WP40-R01 登记保留与 Mega 状态、R02 命令期逃跑、R03 特殊/PP 分层、R04 道具家族、R05 抢夺最小标记；WP41-R01 三入口守卫与 94/64、R02 检查分层、R03 形态清理分列、R04 强制换出两族；C01 术语/有限目录/场景前提、C02 批内哈希绑定与错引更正）。修订后 v2：WP39 `1fdfb8bc`/38,555、WP40 `555282ba`/38,012（级联 WP39 v2）、WP41 `237ac575`/28,916（级联 WP40 v2＋WP39 v2）；矩阵 `0d6a0c9c` → `0fe9fe2f`/46,193（五行"首审已修订为 v2、待复审"）；交付摘要 v2 `f9209703`/8,855；self-checks v2 `9633f336`/12,444、boundary-checks v2 `0db06e68`/5,323。修订材料：回应 `eec9fbc2`/17,055、差异 7 份（`dd473ba2`/`ae4631a4`/`7667dd09`/`18eaa1ee`/`89f79943`/`d3da9737`/`7071b5d6`）；TSV v21 `1a5a56e8`/42,331（310 行）；首审材料 11 份登记于第 1 节。被审 v1 哈希保留历史；三包保持 ReviewPending（各自具名范围，首审修订后再送）；未自批 Reviewed。

- 2026-09-27 WP39／WP40／WP41 v2 复审收尾（v3，第四十七轮）：独立复审报告 `50a485f2`（15,110 字节）与提示 `dbcae65a`（9,575 字节）结论 **REQUEST_CHANGES，9/12 关闭，仅剩 WP39-R01、WP40-R03、WP41-R02**；C01/C02 已接受，C03 有界维护。修订前六件必检与 self／boundary／主 TSV 三件补检全部与本轮快照逐字节匹配。关闭集合 WP39-R02/R03、WP40-R01/R02/R04/R05、WP41-R01/R03/R04 及三个编号已接受部分保留。仅收尾待战对象复用／输入／钩子／返回、PP 与服从旧摘要、严格非登记 UI 组合检查与 WP40 直接传播，完成 C03，未重开九项。当前 v3：WP39 `864dec26`/42,165、WP40 `716a2442`/40,100、WP41 `463cab3c`/31,502；完整哈希绑定 WP40→WP39、WP41→WP40／WP39 同步；矩阵 `2402cf42`/46,283（五行 9/12 关闭、剩对应编号 v3 待复审）；摘要 `8360aec4`/11,292、self `6d16628f`/23,048、boundary `46a58b20`/6,926。新增回应 `7fea838c`/15,187 与快照差异 7 份；复审原件 11 份补登。主 TSV v22 `4bf6bcf4`/44,821（329 条）；manifest §1 共 425 条。v1／被审 v2／当前 v3 身份分开；三包继续 ReviewPending（自身具名范围，复审收尾后再送）＋前向 Inventoried；没有整体 PASS_SCOPED 或 Reviewed 回填。既有限定通过集合 WP01–WP21、WP24–WP31、WP33–WP36、WP59–WP60 保留。

- 2026-09-27 WP39／WP40／WP41闭合回填与WP43→WP44→WP45批次（第四十八轮）：独立闭合报告 `c88d91cf`（11,892字节）与执行提示 `a712c0fb`（16,208字节）给三包PASS_SCOPED（限定静态范围），原12项及C03全部闭合。回填前六项固定对象与主TSV补检均与闭合快照逐字节匹配。头尾与互相状态引用管理回填，完整哈希按WP39→WP40→WP41级联；当前 WP39 `9a3a796f`/42,697、WP40 `07789951`/40,547、WP41 `e6b835af`/31,897；被审v3完整身份保留§3，不冒称回填字节被审。矩阵F11五行Reviewed＋前向Inventoried，F12三行增量ReviewPending＋前向Inventoried，当前 `bf77403c`/47,030。新批四产物（3包＋WP44附表）wp43-types-accuracy-and-damage `6021d835`/29,511、wp44-statuses-stat-stages-and-immunities `b7eae260`/35,014、wp44-effect-coverage `ea5237d3`/24,809、wp45-weather-terrain-side-and-position-effects `2fbe3b65`/34,109，均尚未外审；79个具名前提场景／向量、44源数据文件身份与固定commit匹配、五份管理差异内存重建。N01新增证据：WP40无防守概括过宽，WP43给模式破坏＋目标无防守的q70/r70反例；仅具名登记，不静默重写旧行为。交付回应 `3d9f3385`，摘要 `96b9abf4`，self `3c1259dd`，boundary `c20c3cbc`；reviewer原件11份补登。主TSV v23 `f9650af5`/48,017（353条），manifest当前表449条。限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP59–WP60；新三包未自批Reviewed。

- 2026-09-27 WP43管理回填、N01同步与WP44／WP45有限修订（第四十九轮）：首审报告 `308acc64`（15,538字节）／权威提示 `adab1c0e`（11,454字节）给批次REQUEST_CHANGES；WP43 A～F本体PASS_SCOPED，WP44-R01/R02及WP45-R01必修，N01新证据CONFIRMED，C01两处维护。七项必检与五项补检共十二件匹配本轮快照；本轮先WP40 N01实际校准及WP41必要身份传播，再WP43管理回填，再WP44主稿／附表与WP45 v2修订。22条精确参数合同连接16泛化项、破壳与五集合族；多项招式镜甲预检不带模式破坏者门；快速／广域免抽签后仍有最后行动门；C01剧毒限定与EOF781同步。当前 wp40-commands-obedience-and-action-order `ad471872`/42,476、wp41-switching-positioning-and-escape `42878fac`/31,939、wp43-types-accuracy-and-damage `0cd9958c`/30,543、wp44-statuses-stat-stages-and-immunities `85e17c6c`/49,950、wp44-effect-coverage `47bd80e2`/27,133、wp45-weather-terrain-side-and-position-effects `f92b0f3c`/35,823；矩阵 `b230d1d7`/47,092仅改F12三行。WP43被审首版留史，不冒充回填字节被审；WP44/45保持ReviewPending。回应 `a114fc00`/16,324，差异10份可从本轮快照精确重建；摘要v2 `39275cb4`/9,790、self `307d1ff0`/56,423、boundary `21abfe14`/6,629。补登reviewer12件，主TSV v24 `95415831`/51,044（376条），manifest当前表472条；仅送三个必修、N01、C01及直接传播，不启动下一批。限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43、WP59–WP60。

- 2026-09-27 WP44／WP45闭合回填、N01收尾与WP42→WP48→WP49批次（第五十轮）：独立复审报告 `c88366bcb68beb81f40667ef46ec0b1016476763347491d3e6c693ce2961ccae`（12,828字节）及提示 `a4dcb34ff159d1cf81d98f40f4c1f42d8edec44d851919b2a5e38c576566cfee`（16,972字节）给PASS_SCOPED，三个必修及N01/C01均CLOSED、WP43回填接受。八必检＋两补检匹配快照；旧六规格只作状态／引用维护，WP44/45限定Reviewed。新三包串行固定：wp42-growth-end-of-round-and-battle-outcomes `9bde1314`/37,859、wp48-ability-calculation-modifiers `480016af`/34,233、wp49-ability-phase-triggers `92869008`/50,601，均ReviewPending（具名静态范围，未外审）；83场景、48族／263登记语句／267展开身份的文本集合与16项独立算术已自检。八份回填diff，新三包及四份交付文档，补登reviewer12件；保留旧472／376行，各新增27行，manifest499条／主TSV v25 403条 `cddd2914bd41389cc786de8970771e43e84fe87029d48e8f02733cc024103283`（54,775字节）。只送三新包及五组直接交界后停止；通过集合为WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43–WP45、WP59–WP60，运行与出口保留。

- 2026-09-27 WP42／WP48／WP49首审有限修订v2（第五十一轮）：独立报告 `2068681add50704d439c98133d42ce4ce665da58deffef9011ead37bb148af60`（11,466字节）及权威提示 `29862926457c505f1d3061dffcffd5b0b78d681393f51511eccfa5add8cb22bd`（8,895字节）给REQUEST_CHANGES，WP42-R01／WP48-R01／WP49-R01三必修、BATCH-C01两处维护；旧WP44/45回填和N01关闭接受。六必检＋三补检匹配；按WP42→WP48→WP49逐包固定：wp42-growth-end-of-round-and-battle-outcomes `6644c777`/41,329、wp48-ability-calculation-modifiers `87e39127`/35,021、wp49-ability-phase-triggers `7a4ecf93`/52,573。默认拾取18／11有序表与重复位置、命中整数商96及r95真／96与97假、野生敌方当前同侧存活场上人数门、合法MOODY输入与ICEFACE回调标志已修订；新稿仍ReviewPending，待有限复审。新增回应和七差异，补登reviewer12件；manifest519行／TSV v26 423行 `e16fc33168b07694e0791ac96fc81cf367bdd37d9ab70cb6e9a8c9d4f1e9a4b5`（57,528字节），旧499／403行保留。只送三原编号、C01及直接传播后停止，既有限定通过集合不扩大。

- 2026-09-27 WP42／48／49限定回填与WP46→WP47-A→WP47-B首稿（第五十二轮）：独立报告 `f0e266220cf76a0aa4f490c61b547bc705453d3729012629a563c4c727ac926b`（10,972字节）与提示 `8a2ba73c38a80dcd8483a824e305e3f26e00a74abbe141c8872eb18ef0bd08c3`（15,482字节）给PASS_SCOPED，三原编号及C01全CLOSED。六必检＋三补检匹配快照；三旧稿仅头尾／身份维护，WP49级联两个上游。新批串行固定：wp46-damage-multihit-and-healing `0e5a676e`/47,352、wp47-a-move-attributes-targeting-and-calling `ad6a6d6c`/33,207、wp47-b-switching-control-and-item-changes `24185ce4`/37,934及各包附表，均ReviewPending（具名范围）；139/55/60主身份、102场景、26项常数检查。八效果文件314＋内建挣扎1，254本批＋61已有主规则，无本有界集合无名留白；全局WP79未启动。新观察WP47-B-N01/N02及BATCH-N03只登记新材料，旧WP40/41未改，待独立review定点判断。补登reviewer12件，新增总27行，manifest546／主TSV v27 450行 `db333a8d31fa22d91cbd52e74d3072d0e0c5584d6764fc758293dc2002255648`（61,152字节），原519／423行保留。限定通过集合WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP45、WP48–WP49、WP59–WP60；批末只送新三包和直接交界后停止。

- 2026-09-27批、2026-09-28收尾：WP46/47限定回填及WP50→WP51→WP52-A首稿（第五十三轮）。独立报告 `1bd018f519db064d3a9ff9d2b9582e692cd6bf0c129a56f1dd7bab0ee5730541`（16,289字节）与提示 `559ed0a2ae12138742ad9d2d111f3d7801b9438e374e6091095457e1f81c932c`（18,465字节）给旧三包PASS_SCOPED并批准WP47-B-N01/N02、BATCH-N03三摘要同步；现实际完成CLOSED，C01三点及六件限定Reviewed回填完成。14必检/补检＋7级联补检匹配。新稿wp50-held-item-triggers-and-consumption `937551e0`/29,336、wp51-ai-action-selection-and-skill `1174d485`/25,064、wp52-a-generic-numerical-and-status-evaluation `f7f400c6`/46,332及三附表均ReviewPending；28/23/50共101场景、21常数检查。WP50 32族196身份；WP51 15换人处理器；WP52-A 164效果身份，334登记出现，267能力评级；后续B/C未启动。18份差异相对本轮快照，旧self/boundary/摘要v2留v1历史。补登reviewer13件，新增41行；manifest587／主TSV v28 491行 `986477f175f2dc3db9303b456ba0379c0de81a1b95ae5bb37d4388812fe415f8`（67,071字节），原546/450行不丢。限定通过集合WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP49（WP47为A/B）、WP59–WP60；本批只送新三包及五组直接交界后停止。

- 2026-09-28 WP50/52-A首审有限修订与WP51限定回填（第五十四轮）：独立报告 `39e5a7e85cfafbcfeb49eb31c667a81a80fbc425d36b843013e45e5cee8e3c85`（12,797字节）及提示 `c58476b85724c916e2a47f3613a9fd936bbabcfb3ced0df774c5d94e26d7f869`（10,691字节）REQUEST_CHANGES仅WP50-R01、WP52-A-R01；WP51 A～E PASS_SCOPED，前批三观察/C01/回填接受。本次12件预检匹配。R01修false取消贪吃要求、半血仍有效及五果世代门；另一R01修三墙按当前同侧存活场上人数，固定名义双席25/19对照。WP50/52-A v2继续ReviewPending；WP51 C01存在性/天气抑制名与主附表具名Reviewed回填，原六首稿身份留史。111场景（33/25/53）、28常数；覆盖数据/其它已支持规则不重开。9份修订diff相对本轮快照，旧18份原件保留。补登reviewer14件，新增24行；manifest611／TSV v29 515条 `e0f2a3f0d99828355d10ca7a9e385ed707c5d9a2ef6d9a26d0b637ba866b7a55`（70,456字节），原587/491保留。只送两原编号、C01/WP51回填及直接传播有限复审后停止，不启动下一批。

- 2026-09-28 WP50/52-A限定回填与WP52-B→WP52-C→WP54首稿（第五十五轮）：独立报告 `6537ac37528a3e21f9f809d4ea72fd309c132a07539ca2d312d34b889ef0ca4a`（10,814字节）与提示 `5868bfcd92f142ab88bea00c8edf420618ecf295c71782b01dcc0bf0b72d0077`（17,404字节）PASS_SCOPED，两R/C01全CLOSED、WP51回填接受。12件预检匹配，旧111场景输入期望不变，5规格/矩阵/旧摘要self/boundary共9份管理diff。本轮新稿wp52-b-field-damage-healing-and-target-evaluation `b41c2773`/42,914、wp52-c-items-calling-and-control-evaluation `542e7b01`/39,343、wp54-entry-eligibility-level-adjustment-and-clauses `3ef7ae5a`/32,322及各附表只ReviewPending；60/55/42共157场景、31常数。B/C按真实数值责任转23条登记；B270/C167/A334/WP51已有15直接/复制出现，另C条件组57物品。全直接/复制782有效键＋条件57＝839具名可定位入口，非运行/全局外审通过。WP54十工厂/五样本/三模式与56来源身份/14条款键；新观察WP54-N01独立登记待审，不改旧WP46。reviewer12＋新6＋交付4＋diff9共新增31行；manifest642／TSV v30 546条 `7e8467f5d58101757ff7c29c6ec8d9a2ca2f1381a8135b498b677930f7df7963`（74,801字节），原611/515保留。批末只送新三包与直接交界后停止，不启动WP55。
- 2026-09-28 WP52-B-R01有限修订、WP54-N01同步、BATCH-C01维护与C／WP54限定回填（第五十六轮）：独立报告 `b7e5e47bc99da6a3965ca2885b80f5e654cefc79d4ff641fb3586c7d18284ddd`（14,417字节）与提示 `da43a392e29207dcffca089ff1a6587d76ff3881eb02285cea27aa2003383c9a`（10,379字节）给WP52-B REQUEST_CHANGES（仅R01）、C／WP54各PASS_SCOPED、N01 CONFIRMED、C01非阻塞。15项预检逐字节匹配。R01将压榨PP改为分入口（普通候选跳过／触达处理器PP0缺失查询先失败／PP1、2、−1保留），B 60→62场景，`b41c2773`/42,914→`8036a674`/44,557，除R01外未发现其它阻塞、继续ReviewPending。N01确认后WP46 §4分入口同步，`aa9a7f1e`/47,646→`0f7c9b4b`/48,872。C01把A主附表B247/C190与“未启动”改为A阶段历史定位，`5cdc3edf`/48,733→`9c74d50c`/49,622、`fa760fac`/59,366→`7bce736d`/60,674。C主附表限定Reviewed回填（`542e7b01`/39,343→`290bee81`/40,332；`9e8d3030`/37,701→`f83205ee`/38,390），WP54主附表同理（`3ef7ae5a`/32,322→`2a1518c3`/33,809；`b45c976e`/11,746→`0ec50236`/12,381）；C对B引用=R01修订稿待复审。必要身份级联WP47-A `e4934943`/34,014、WP47-B `00769901`/39,000、WP50 `f0b6b147`/32,490、WP51 `2b0847b5`/27,645；矩阵`abacb775`/50,610。16份修订diff相对本轮快照；回应1份。reviewer16＋回应1＋diff16共新增33行；manifest675／主TSV v31 579条 `e91e849cbd56f88fcb0792521e17eb9382669fa5911a9a2066e511df9e37f64f`（79,741字节），原642/546行保留。只送R01、N01同步、C01、C／WP54回填及直接传播有限复审后停止，不启动WP55。
- 2026-09-28 WP52-B限定Reviewed回填、BATCH-C02维护与WP55→WP56→WP57首稿（第五十七轮）：独立有限复审报告 `35d382cd11f7f5334317ee10a88fdf53f3bfe2c0d05453ae39f3079ab583b5ec`（12,290字节）与提示 `0e49b872ba414cb321152d449a70610a51da0ad83ca99ec0c5cd31890e7fbf74`（15,809字节）给PASS_SCOPED，R01／N01实际同步／C01全CLOSED、C／WP54回填接受；先行完成B限定Reviewed回填（B主 `8036a674`/44,557→`73fa6ffa`/45,342；B附表 `d2ccf48f`/57,193→`723838f2`/57,979）与C02（旧self/boundary/summary升v3 `3a05f9e0`/1,069,184、`9e693b2c`/20,318、`6ec4fe6f`/9,057；artifacts六项重固定、Q41尾句同步），9份backfill-diff相对本轮快照重建9/9。新三包串行固定：wp55-facility-session-and-restoration `d5ee5ba7`/21,873（25场景）、wp56-palace-and-arena-variants `fde119ea`/16,917（22场景）、wp57-factory-rentals-and-swaps `e510f840`/11,933（15场景），均ReviewPending（具名范围，批内互引注明未外审）。矩阵F13-04/F13-05标ReviewPending子范围、F12-08四包具名Reviewed；reviewer14件＋回填回应1＋9diff＋三包3＋批材料3共新增30行；manifest705／主TSV v32 609条 `edcc4b54979e635f95a70324d5b501a03a03bc865441acab120878c2ad26274f`（83,890字节），原675/579行保留。只送三新包、回填/C02与直接交界统一外审后停止，不启动WP58。
- 2026-09-29 WP55／WP56／WP57首审REQUEST_CHANGES修订、C01记法与继承C02剩余（第五十八轮）：独立首审报告 `1e3d4314e0d4d2d6b6d8b3a83cd3b4d2ed80540b0bc5072268a6a7a5a5ad4531`（20,977字节）与修订提示 `e5f787e4944979843d860259e15b9988d7739f283a055be2ec33df04abcc9244`（11,926字节）给REQUEST_CHANGES：WP55×5、WP56×5、WP57×3共13项必修；WP52-B限定Reviewed回填接受、C02仅剩packages两条非阻塞。9项固定对象与707项输入逐字节匹配、旧快照与reviewer原件保护。**13项全部核实认可并修订**（WP55-R01会话决定/单场返回分层与保存门、R02空报名与未开始结束、R03保存返回假与异常分层、R04 data查询先失败、R05零长度抽样与短名单；WP56-R01实际门A与2A＋D并重算61/129、22/64、90/185、R02压半生命周期、R03换人早返标记、R04技分覆盖与时点、R05评判2／0与三具名心分；WP57-R01 Factory默认拥有者、R02取消仍提交、R03含端点越界），并同步WP55§2.5属主概括。修订后：WP55 `d5ee5ba7`/21,873→`0bcff15b`/27,698（34场景）、WP56 `fde119ea`/16,917→`8ed7940b`/21,274（27场景）、WP57 `e510f840`/11,933→`7e69ccdc`/14,776（17场景），均仍ReviewPending；矩阵F13-04/F13-05标“首审REQUEST_CHANGES，按原编号修订后再送”（`0a726a5f`/51,444→`b97ed883`/51,500）。C01三处记法与继承C02剩余闭合（旧self v3→v4 `3a05f9e0`/1,069,184→`b776328d`/1,070,038；旧摘要v4 `4ba4ed58`/9,587；回填回应维护版 `835459a7`/6,661；批boundary v2 `8c2033a7`/8,670；批self v2 `36704503`/20,320；批摘要v2 `0fcab05d`/6,514）。新增27行（reviewer16／回应1／diff10）：manifest §1共732条、主TSV v33 636条 `0f8113065947f4b94c3ed8cf8d0ea9db8ef53160b7d1728fce7abe56028c2333`（87,544字节），原705/609行保留。只送原13编号、C01／继承C02及直接传播作有限复审后停止，不启动WP58或其它包。

### 2.2 历史版本关系（据本地记录重建，证据受限）

- 2026-09-19 14:18:53 四份总控文档定稿；约 14:38 首次计算哈希并写入清单（历史条目见第 3 节）。
- 2026-09-19 14:39:03，overview 与 module-map 在本地被进一步修订（内容增大、行数不变），送审附件为 14:39 版，清单未同步，造成联合 review 实测值与清单记录不一致（联合 review R01）。
- **证据限制**：14:39 的修改时刻来自本地文件 mtime；变更范围（补核 E04 训练家引用、E11 HTTP 工具、E21 参战/布局，细化总览 §3 与 module-map D01/D11 行）是本地模型比对当前版本与此前阅读记录后重建的说明。**没有该次修改的操作日志或旧版全文**；14:39 之前的两版内容（`0421575b` / `0e22b7f2`）在本地已被覆盖、无留存副本，无法提供逐行 diff。不补造旧版本或历史日志。

## 3. 历史条目（已被替代，仅供追溯）

| 文件 | 旧 SHA-256（前 8 位） | 记录时点 | 替代关系 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `0421575b` | 2026-09-19 约 14:38 | 被 14:39 修订版 `1ca34f44` 替代 |
| `planning/module-map.md` | `0e22b7f2` | 2026-09-19 约 14:38 | 被 14:39 修订版 `32eab70d` 替代 |
| `planning/feature-matrix.md` | `2f4e3e31` → … → `6b49c40b` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联、WP03 回填+WP04–WP07 追踪、批次复审关联、三包回填、WP06 回填+WP08–WP10 追踪、批次复审关联、WP09 回填修订、WP08/WP10 回填与 WP11–WP13 追踪修订、WP11–WP13 复审修订（v2 状态与移动路线附表登记）、v2 复审修订（v3 状态与关闭项登记）、WP11/WP12 Reviewed 回填与 WP13 v4 状态同步、WP13 Reviewed 回填、WP14–WP16 批次追踪修订、WP14–WP16 首轮复审修订（v2 状态登记）、WP14–WP16 回归复审修订（v3 状态与 WP16-R02 关闭登记）、WP14–WP16 Reviewed 回填、WP17 批次追踪修订、WP17 首轮复审修订（v2 状态与绘制附表登记）、WP17 回归复审修订（v3 状态与 R02～R05/C01 关闭登记）、WP17 Reviewed 回填（F05-05/F05-06）、WP18–WP20 批次追踪增量（八个 Feature）、WP18–WP20 首轮复审修订（八行状态措辞与还原记录措辞同步）、WP18–WP20 定点复审回填（F06-05/F06-06/F08-05 → Reviewed；WP18/WP19 行更新）、WP18/WP19 回填（F06-01/F06-02/F07-01、F06-03/F06-04 → Reviewed）、WP21–WP25 批次追踪增量（五个 Feature）、WP21–WP25 首轮复审修订（五行状态措辞）；2026-09-26 经定点复审回填（F07-02～F07-05 → Reviewed＋前向 Inventoried；F06-07 措辞更新）被 `e0762970` 替代；2026-09-26 再经闭合回填（F06-07 → Reviewed（WP21 子范围）＋前向 Inventoried）被 `8b83d668` 替代；2026-09-26 再经批次增量（六个 Feature → ReviewPending＋各自范围）被 `af8328ee` 替代；2026-09-26 再经首审修订（六行版本说明）被 `c4505715` 替代；2026-09-26 再经 v2 复审收尾（六行"仅剩具名项"）被 `6b49c40b` 替代；2026-09-26 再经 WP26–WP30 闭合回填（六行 → Reviewed（对应子范围））与 WP31→WP28→WP29 批次增量（F09-03、F08-03/F08-04、F08-06 → ReviewPending（批内固定、尚未外审））被 `cbf671a8` 替代；2026-09-27 再经首审修订（四行 → "首审已送审：REQUEST_CHANGES，修订后再送"）被 `a05c39f4` 替代；2026-09-27 再经有限复审回填与余量行同步（F09-03 → Reviewed（WP31 子范围）＋前向 Inventoried；余量行"仅剩三点已修订"）被 `909080cb` 替代；2026-09-27 再经 WP28／WP29 回填（F08-03/F08-04、F08-06 → Reviewed（对应子范围）＋前向 Inventoried）与 WP33→WP34→WP35 批次增量（F09-05/F09-06/F09-07 → ReviewPending（批内固定、尚未外审）＋前向 Inventoried）被 `77c3bff0` 替代；2026-09-27 再经 WP33／WP34／WP35 首审修订（F09-05/F09-06/F09-07 → "首审已送审：REQUEST_CHANGES（已修订（v2），待复审）"）被 `243df4e4` 替代；2026-09-27 再经 WP33／WP35 回填与 WP34-R03 收尾（F09-05/F09-07 → Reviewed（对应子范围）＋前向 Inventoried；F09-06 → "v2 复审仅剩 WP34-R03 末次缓存（v3 已修订、待短复审）"）被 `17fa287c` 替代；2026-09-27 再经 WP34 回填（F09-06 → Reviewed（对应子范围））与 WP59→WP36→WP60 批次增量（F10-01/F10-02、F14-01～F14-04 → ReviewPending（各自范围，批内固定、尚未外审）＋前向 Inventoried）被 `64d297de` 替代；2026-09-27 再经首审修订（WP59／WP36／WP60 六行 → "首审 REQUEST_CHANGES，已修订为 v2、待复审"）被 `b580eb92` 替代；2026-09-27 再经 v2 复审收尾（六行 → "9/13 关闭＋四项已收尾修订为 v3、待复审"）被 `1de3852f` 替代；2026-09-27 再经闭合回填（六行 → Reviewed（对应子范围）＋前向 Inventoried）与 WP39–WP41 批次增量（F11-01～F11-05 → ReviewPending（各自具名范围）＋前向 Inventoried）被 `0d6a0c9c` 替代；2026-09-27 再经首审修订（F11-01～F11-05 → "首审 REQUEST_CHANGES，已修订为 v2、待复审"）被 `0fe9fe2f` 替代（历史）；经 F11-01～05 五行复审状态同步（9/12 关闭；剩对应编号 v3 待复审），修订前完整身份 `0fe9fe2fce11fd3db104f752361115a164bc5442be54be613a1baebb43922683`（46,193 字节，被审 v2）被 `2402cf4281b1aefb0770545d0ff147e56252f5b1ff9f36ceeb97777ac0691c8f` 替代（46,283 字节，当前有效；v3）；经2026-09-27 闭合回填及新批具名状态／摘要维护，修订前 `2402cf4281b1aefb0770545d0ff147e56252f5b1ff9f36ceeb97777ac0691c8f`（46,283字节，被审v3）留史，当前被 `bf77403c9b402f55830a0db482006465d9b74e0e798ab758c80f204e33ab1661` 替代（47,030字节，当前有效）；2026-09-27经WP43回填与三项有限修订、N01/C01的追踪／交付同步v2，修订前完整身份 `bf77403c9b402f55830a0db482006465d9b74e0e798ab758c80f204e33ab1661`（47,030字节）留史，被 `b230d1d7840b31923c741d439c2344990c18e00108a45801fdc45b6fd5078cc7` 替代（47,092字节，当前有效）；2026-09-27经本轮管理回填与新三包增量维护，修订前完整身份 `b230d1d7840b31923c741d439c2344990c18e00108a45801fdc45b6fd5078cc7`（47,092字节，历史被审／登记版）留史，被 `4234c91e8b2c3a8153e607709425b7ba89900462d069694e962f21206aa0bed2` 替代（48,137字节，当前有效；新字节不冒充原被审对象）；2026-09-27经WP42／WP48／WP49首审有限修订v2及直接传播；被审／修订前完整身份 `4234c91e8b2c3a8153e607709425b7ba89900462d069694e962f21206aa0bed2`（48,137字节，v1／此前登记版）留史，被 `6d9a28754bd2cfb3622a8a6dbf6b624600fd8c45aa34db570dc111f57c455a20` 替代（48,271字节，当前有效；v2未外审，非Reviewed）；2026-09-27经本轮管理状态与新批交付增量维护；修订前完整身份 `6d9a28754bd2cfb3622a8a6dbf6b624600fd8c45aa34db570dc111f57c455a20`（48,271字节，被审v2／前轮登记版）保留，被 `9b0ac4a232ec2df4855f8ad31b32d9ef2d9511185d4384647f57c515b434efc8` 替代（48,848字节，当前有效；新管理字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）本批管理状态、配套材料与新交付增量维护；旧完整身份 `9b0ac4a232ec2df4855f8ad31b32d9ef2d9511185d4384647f57c515b434efc8`（48,848字节，被审首稿／前轮登记版）保留，被 `35935419cb9648d4bfd60665d7a7719a9d79230b9d7585bf852a9120ef87ab30` 替代（49,556字节，当前有效；新字节不冒充旧被审对象）；2026-09-28经有限修订的矩阵/当前配套同步，首稿旧断言留明确历史；旧完整身份 `35935419cb9648d4bfd60665d7a7719a9d79230b9d7585bf852a9120ef87ab30`（49,556字节，被审首稿v1／前轮登记版）保留，被 `f2c1a5810dd6fcba6fc7f37f0c0fd5666062f81e8628b70471993cc62d9a1001` 替代（49,715字节，当前有效；当前新字节不冒充本轮被审对象）；2026-09-28经旧批活动状态/身份与新批交付登记维护；旧完整身份 `f2c1a5810dd6fcba6fc7f37f0c0fd5666062f81e8628b70471993cc62d9a1001`（49,715字节，被审v2或WP50附表v1／前轮登记版）保留，被 `529569423b895c73026c47d6eef6745dfb387b09d37859f1527cb47f8cd9276d` 替代（50,343字节，前轮登记版）留史，再被 `0a726a5f3b57e81652fe87c888925a632fbcb0b61a6cf551ceab0abdd2dc90f4` 替代（51,444字节，前轮登记版）留史；2026-09-29经WP55／WP56／WP57首审REQUEST_CHANGES后的F13-04/F13-05行状态同步（“首审REQUEST_CHANGES，按原编号修订后再送”），由 `b97ed8836dd510b8f0c2ca8f0485cf03a01737d2fb515b6d4f0e65a3a56684cc` 替代（51,500字节，当前管理字节，不冒充被审对象） |
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
| `specs/ui/wp17-messages-windows-input.md` | `e46cd496` → `e0d54372` → `6010f40b` | 2026-09-23 首版送审 | 首版经 WP17-R01～R05/C01 修订为 `e0d54372`（v2）；经回归复审 WP17-R01 剩余两处与 C02 维护修订为 `6010f40b`（v3，闭合通过版）；经 Reviewed 状态回填被 `bb61f967` 替代（当前有效，管理性变更） |
| `specs/ui/wp17-draw-text-tags.md` | `9b76c393` | 2026-09-23 附表首版送审 | 经回归复审 WP17-R01 剩余两处修订被 `e01466ef` 替代（当前有效） |
| `specs/overworld/wp14-random-dungeons.md` | `4703c27d` → … → `5ca2c044` | 2026-09-23 首版送审 | 首版经 WP14-R01 修订为 `349b938d`（v2）；经回归复审 WP14-R01 剩余范围修订为 `5ca2c044`（v3，闭合通过版）；经 Reviewed 状态回填被 `cb4edd9c` 替代（当前有效，管理性变更） |
| `specs/overworld/wp15-resource-matching-and-audio.md` | `1aa30467` → … → `8e44c387` | 2026-09-23 首版送审 | 首版经 WP15-R01 修订为 `30f2544e`（v2）；经回归复审 WP15-R01 剩余范围修订为 `8e44c387`（v3，闭合通过版）；经 Reviewed 状态回填与 WP15-C01 同步被 `cb184c3d` 替代（当前有效，管理性变更） |
| `specs/overworld/wp16-world-rendering-and-visual-transitions.md` | `4e55e3b1` → … → `ccb7bb9a` | 2026-09-23 首版送审 | 首版经 WP16-R01/R02 修订为 `f93ec3b0`（v2）；经回归复审 WP16-R01 剩余范围修订为 `ccb7bb9a`（v3，闭合通过版）；经 Reviewed 状态回填被 `d7aad4aa` 替代（当前有效，管理性变更） |
| `specs/overworld/wp11-map-topology-transfer.md` | `7f1274c2` → … → `df39a9e5` | 2026-09-19 首版送审 | 首版经 WP11-R01/R02/C01 修订为 `ac090bc1`（v2）；经 v2 复审 WP11-R02 剩余范围修订为 `df39a9e5`（v3，PASS_SCOPED 通过版）；2026-09-22 经 Reviewed 状态回填被 `84ca24a5` 替代（当前有效，管理性变更） |
| `specs/overworld/wp12-terrain-movement-vehicles.md` | `9bc37359` → … → `7f1979bd` | 2026-09-19 首版送审 | 首版经 WP12-R01/R02/R03 修订为 `92dba89d`（v2）；经 v2 复审剩余范围修订为 `7f1979bd`（v3，PASS_SCOPED 通过版）；2026-09-22 经 Reviewed 状态回填与 WP12-C01 同步被 `8187e7de` 替代（当前有效，管理性变更） |
| `specs/overworld/wp13-map-events-npc-followers.md` | `86d96672` → … → `b9b809e4` | 2026-09-19 首版送审 | 首版经 WP13-R01–R05 修订为 `a1288287`（v2）；经 v2 复审剩余范围修订为 `1ec410b6`（v3）；经 v3 复审 WP13-R05 剩余分支修订为 `b9b809e4`（v4，闭合通过版）；2026-09-23 经 Reviewed 状态回填被 `0b9bbd02` 替代（当前有效，管理性变更） |
| `specs/overworld/wp13-interpreter-command-matrix.md` | `1ff42842` → `6da4a23e` | 2026-09-19 首版送审 | 首版经 WP13-R01/R02 修订为 `6da4a23e`（v2）；2026-09-22 经 v2 复审 WP13-R02 剩余范围修订被 `ab69bc87` 替代（当前有效） |
| `specs/overworld/wp13-move-route-matrix.md` | `77cbdb3d` | 2026-09-19 附表首版 | 2026-09-22 经 v2 复审 WP13-R01 剩余范围修订被 `f637f1c3` 替代（当前有效） |
| `specs/creature-rpg/wp18-creature-identity-species-ownership.md` | `f3c33277` → `f36f7b8a` | 2026-09-26 首版自检期 | 自检期内两次重固定（形态继承精确化；批末交叉引用同步）被 `7ab818e2` 替代（v1，首版送审）；经首轮复审 WP18-R01/R02 修订被 `3d30f3f1` 替代（v2）；经定点复审 WP18-R01 剩余两处（登记读取路径、hasNature? 传播）修订被 `4428049b` 替代（v3，闭合通过版）；经 Reviewed 状态回填被 `85368fe3` 替代；经 WP21 依赖行同步（闭合回填轮，管理性）被 `0464ca07` 替代；经 WP26/WP30 依赖行同步（回填轮，管理性）被 `54b54743` 替代；经 WP28/WP29 依赖行同步（回填轮，管理性）被 `55fb5004` 替代（当前有效） |
| `specs/pokemon-rules/wp19-attributes-ability-and-stats.md` | `695fcdef` | 2026-09-26 首版自检期 | 批末同步 WP18 引用后重固定被 `3cba4bcd` 替代（v1，首版送审）；经首轮复审 WP19-R01～R04 及传播修订被 `252649f7` 替代（v2）；经定点复审 WP18-R01 传播修订被 `6c669fcf` 替代（v3，闭合通过版）；经 Reviewed 状态回填被 `489984f7` 替代（v3 管理性）；经 C01 上游引用文字同步被 `03167162` 替代；经 WP21 依赖行同步（闭合回填轮，管理性）被 `c7fb40fa` 替代；经 WP30 依赖行同步（回填轮，管理性）被 `1c4325f5` 替代；经 WP28/WP29 依赖行同步（回填轮，管理性）被 `cd3dcf4b` 替代（当前有效） |
| `specs/creature-rpg/wp20-hp-status-moves-helditem.md` | 无中间版本 | 2026-09-26 首版 | 自检期描述修正直接落于 v1 `84c29af6`（首版送审）；经首轮复审 WP20-R01～R03 修订被 `d595b1b2` 替代（v2，定点复审 PASS_SCOPED 通过版）；经 Reviewed 状态回填（含 C03 简写与引用同步）被 `f8272acf` 替代（v2 管理性回填）；经上游引用同步被 `f2f904e5` 替代；经 WP30 依赖行同步（回填轮，管理性）被 `9a2ad1ab` 替代；经 WP28/WP29 依赖行同步（回填轮，管理性）被 `05a59789` 替代（当前有效） |
| `specs/pokemon-rules/wp21-dynamic-forms-and-display.md` | 无中间版本 | 2026-09-26 首版 | 自查修正三处示例/表述直接落于 v1（`5a5ef9ca`，首版送审）；经首轮复审 WP21-R01～R06 修订被 `55a47313` 替代（v2）；经定点复审 WP21-R03（当前 PP 钳制）与 BATCH-C02 球字段简写修订被 `4e475505` 替代（v3）；经闭合复审 PASS_SCOPED 后回填被 `19a36297` 替代；经 WP30 依赖行同步（回填轮，管理性）被 `b5eeb48e` 替代（当前有效，管理性回填；被审 `4e475505` 保留历史） |
| `specs/creature-rpg/wp24-player-trainers-partners.md` | 无中间版本 | 2026-09-26 首版 | 自查修正两处笔误与一处未证实概括后落于 v1（`45370acd`，首版送审）；经首轮复审 WP24-R01～R03 修订被 `8b06ddc4` 替代（v2）；经定点复审 PASS_SCOPED 后按 BATCH-C02 同步回填被 `32594094` 替代（当前有效，管理性回填；被审 `8b06ddc4` 保留历史） |
| `specs/creature-rpg/wp25-party-and-storage.md` | 无中间版本 | 2026-09-26 首版 | 自查修正屏幕/场景分层并同步 WP24 引用后落于 v1（`920b0943`，首版送审）；经首轮复审 WP25-R01～R03 修订与 WP24 引用同步被 `98b52717` 替代（v2）；经定点复审 PASS_SCOPED 后按 BATCH-C02 场景同步、回填与 WP24 引用同步被 `46bd905d` 替代（v3 管理性回填）；经闭合轮 WP21 引用同步（管理性）被 `edc275c5` 替代；经 WP26 依赖行同步（回填轮，管理性）被 `f505afd5` 替代（当前有效；被审 `98b52717` 保留历史） |
| `specs/creature-rpg/wp26-acquisition-gifts-and-script-trade.md` | 无中间版本 | 2026-09-26 首版 | WP26–WP30 批次首发固定为 `793473a0`（27,898 字节，被审）；经首审 WP26-R01～R04 修订被 `67056812` 替代（v2）；经 v2 复审 WP26-R02/R04 与 C03 收尾修订被 `afc7214a` 替代（v3，被审版）；经 2026-09-26 闭合复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `c87101ad` 替代（当前有效，管理性回填；被审 v3 `afc7214a` 保留历史） |
| `specs/creature-rpg/wp27-bag-and-item-storage.md` | 无中间版本 | 2026-09-26 首版 | WP26–WP30 批次首发固定为 `fe14af5d`（21,719 字节，被审）；经首审 WP27-R01～R03 与 BATCH-C02 修订被 `0a6a28f7` 替代（v2）；经 v2 复审 WP27-R01/R02 与 C03 收尾修订被 `969cb37c` 替代（v3，被审版）；经 2026-09-26 闭合复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `8064f172` 替代（管理性回填；被审 v3 `969cb37c` 保留历史）；经 WP28/WP29 依赖行同步（回填轮，管理性）被 `6ac234e4` 替代（当前有效） |
| `specs/creature-rpg/wp30-growth-learning-and-friendship.md` | 无中间版本 | 2026-09-26 首版 | WP26–WP30 批次首发固定为 `5972e119`（28,244 字节，被审）；经首审 WP30-R01～R06 与 BATCH-C01 修订被 `114038f3` 替代（v2）；经 v2 复审 WP30-R05 与 C03 收尾修订被 `41e71624` 替代（v3，被审版）；经 2026-09-26 闭合复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `6fbc5a20` 替代（管理性回填；被审 v3 `41e71624` 保留历史）；经 WP28/WP29 依赖行同步（回填轮，管理性）被 `b9f58991` 替代（当前有效） |
| `review/wp18-wp20-delivery-2026-09-26/delivery-summary.md` | `52da6bbf` | 2026-09-26 首次送审 | 经首轮复审 v2 同步（C02 及反向一致性）被 `ddf85f73` 替代（v2）；经定点复审 v3 同步被 `f014b114` 替代（v3）；经闭合回填 v4 注记被 `5118e628` 替代（当前有效，v4） |
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` | `57025ecc` | 2026-09-26 首次送审 | 经 v2 重测被 `cdb89a96` 替代（v2）；经 v3 重测被 `ef231e80` 替代（v3）；经 v4 初测被 `1c515390` 替代；同轮二次重测（WP24/WP25 修正后）被 `a5a2ded7` 替代（v4）；经 v5 重测（WP21–WP25 修订材料后）被 `7db3b12b` 替代（v5）；经 v6 重测（定点复审修订与回填材料后）被 `4c66bcb4` 替代（v6）；经 v7 重测（闭合回填材料后）被 `679338ea` 替代（v7）；经 v8 重测（WP26–WP30 批次材料后）被 `08ced51b` 替代（v8）；经 v9 重测（首审修订（v2）材料后）被 `ec86e13d` 替代（v9）；经 v10 重测（v2 复审收尾（v3）材料后）被 `35cd3605` 替代（v10）；经 v11 重测（闭合回填与 WP31→WP28→WP29 批次材料后）被 `a7149e31` 替代（v11）；经 v12 重测（WP31／WP28／WP29 首审修订（v2）材料后）被 `0c811f2d` 替代（v12）；经 v13 重测（WP31 回填与 WP28／WP29 三点收尾材料后）被 `ef046028` 替代（v13）；经 v14 重测（WP28／WP29 回填与 WP33→WP34→WP35 批次材料后）被 `7368bba6` 替代（v14）；经 v15 重测（WP33／WP34／WP35 首审修订（v2）材料后）被 `44da94e7` 替代（v15）；经 v16 重测（WP33／WP35 回填与 WP34-R03 收尾（v3）材料后）被 `a756e2ee` 替代（v16）；经 v17 重测（WP34 回填与 WP59→WP36→WP60 批次材料后）被 `aec34bd2` 替代（v17）；经 v18 重测（WP59／WP36／WP60 首审修订（v2）材料后）被 `a8eb500f` 替代（v18）；经 v19 重测（WP59／WP36／WP60 v2 复审收尾（v3）材料后）被 `d2e72991` 替代（v19）；经 v20 重测（闭合回填与 WP39–WP41 批次材料后）被 `e4054253` 替代（v20）；经 v21 重测（WP39／WP40／WP41 首审修订（v2）材料后）被 `1a5a56e8` 替代（v21）；经 v22 重测（复审收尾材料；原 310 条保留、追加 19 条），修订前完整身份 `1a5a56e8521544f38c5aa3b1a588d9dfc270219fa3b3a63504f930fab49ea7a8`（42,331 字节，v21）被 `4bf6bcf4947aebeae1e46f10ba9ced94c4ed227c2d69435253c5802f56929a97` 替代（44,821 字节，当前有效；v22）；经2026-09-27 v23更新，保留329条并追加24条，修订前 `4bf6bcf4947aebeae1e46f10ba9ced94c4ed227c2d69435253c5802f56929a97`（44,821字节，v22）留史，当前被 `f9650af5cc4b9d450006844b96436592211721e49a0dba1036df6e8d6e4175f7` 替代（48,017字节，当前有效）；2026-09-27经v24更新；保留353条，新增23条，修订前完整身份 `f9650af5cc4b9d450006844b96436592211721e49a0dba1036df6e8d6e4175f7`（48,017字节）留史，被 `95415831e570e765210686c637f3552e6e9cf5a7595e2cca23eae462186720d7` 替代（51,044字节，当前有效）；2026-09-27经v25登记与本批新增27项，修订前完整身份 `95415831e570e765210686c637f3552e6e9cf5a7595e2cca23eae462186720d7`（51,044字节，历史被审／登记版）留史，被 `cddd2914bd41389cc786de8970771e43e84fe87029d48e8f02733cc024103283` 替代（54,775字节，当前有效；新字节不冒充原被审对象）；2026-09-27经v26有限修订交付登记（保留403条，追加20条）；被审／修订前完整身份 `cddd2914bd41389cc786de8970771e43e84fe87029d48e8f02733cc024103283`（54,775字节，v1／此前登记版）留史，被 `e16fc33168b07694e0791ac96fc81cf367bdd37d9ab70cb6e9a8c9d4f1e9a4b5` 替代（57,528字节，当前有效；v2未外审，非Reviewed）；2026-09-27经v27登记，保留450条中的原423条并新增27条；修订前完整身份 `e16fc33168b07694e0791ac96fc81cf367bdd37d9ab70cb6e9a8c9d4f1e9a4b5`（57,528字节，被审v2／前轮登记版）保留，被 `db333a8d31fa22d91cbd52e74d3072d0e0c5584d6764fc758293dc2002255648` 替代（61,152字节，当前有效；新管理字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）主TSV v28就地维护与41行新增，原450行保留；旧完整身份 `db333a8d31fa22d91cbd52e74d3072d0e0c5584d6764fc758293dc2002255648`（61,152字节，被审首稿／前轮登记版）保留，被 `986477f175f2dc3db9303b456ba0379c0de81a1b95ae5bb37d4388812fe415f8` 替代（67,071字节，当前有效；新字节不冒充旧被审对象）；2026-09-28经v29就地更新与24行新增，原491行保留；旧完整身份 `986477f175f2dc3db9303b456ba0379c0de81a1b95ae5bb37d4388812fe415f8`（67,071字节，被审首稿v1／前轮登记版）保留，被 `e0f2a3f0d99828355d10ca7a9e385ed707c5d9a2ef6d9a26d0b637ba866b7a55` 替代（70,456字节，当前有效；当前新字节不冒充本轮被审对象）；2026-09-28经TSV v30就地更新/保留原515及新增31行；旧完整身份 `e0f2a3f0d99828355d10ca7a9e385ed707c5d9a2ef6d9a26d0b637ba866b7a55`（70,456字节，被审v2或WP50附表v1／前轮登记版）保留，被 `7e8467f5d58101757ff7c29c6ec8d9a2ca2f1381a8135b498b677930f7df7963` 替代（74,801字节，前轮登记版）留史，再被 `e91e849cbd56f88fcb0792521e17eb9382669fa5911a9a2066e511df9e37f64f` 替代（79,741字节，前轮登记版）留史，再被 `b280196e76c3a04478c2a349c0391e723c4b9f33f0476796c82dea4ef47997b0` 替代（83,890字节，当前管理字节不冒充被审对象） |
| `review/wp21-wp25-delivery-2026-09-26/delivery-summary.md` | `a046f5f5` | 2026-09-26 首版 | 同轮随 WP24/WP25 修正重测被 `d29d177a` 替代（v1 定稿）；经首轮复审 v2 同步被 `c88e1e5b` 替代（v2）；经定点复审 v3 同步（回填＋R03）被 `62d8a2c8` 替代（v3）；经闭合回填 v4 同步被 `8d8b7e5d` 替代（当前有效，v4） |
| `review/wp26-wp27-wp30-delivery-2026-09-26/delivery-summary.md` | `9c713161` | 2026-09-26 首版 | WP26–WP30 批次首发固定（v1 首版，被审）；经首审 v2 同步被 `dd06a4bd` 替代（v2，被审）；经 v2 复审 v3 收尾同步被 `df4926ae` 替代（v3）；经闭合回填 v4 注记被 `bdd353fd` 替代（当前有效，v4） |
| `specs/pokemon-rules/wp31-basic-evolution.md` | 无中间版本 | 2026-09-26 首版 | WP31→WP28→WP29 批次首发固定为 `e5658f31`（35,631 字节）；批末交界核对修正对 WP18 的引用（§4.1→§3.4）后重固定为 `b5966bbf`（35,629 字节，被审首版）；经首审 REQUEST_CHANGES（WP31-R01/R02＋BATCH-C01）修订被 `e541c650` 替代（v2，被审版）；经 2026-09-27 有限复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `ee47f124` 替代（管理性回填；被审 v2 `e541c650` 保留历史）；经 WP28/WP29 回填后引用同步（管理性）被 `0b40917c` 替代（当前有效） |
| `specs/creature-rpg/wp28-item-use-and-training.md` | 无中间版本 | 2026-09-26 首版 | 批次内自检修正后固定为 `4abaf6f9`（32,848 字节）；批末交界级联重固定为 `f9cd5fe3`（32,848 字节，被审首版）；经首审 REQUEST_CHANGES（WP28-R01～R06＋BATCH-C02）修订与 WP31 引用级联被 `f2f7618c` 替代（v2，被审版）；经有限复审（7 项关闭、剩 R03/R06）收尾修订与 WP31 回填后引用同步被 `7e10cb25` 替代（v3；被审 v2 `f2f7618c` 保留历史）；经 2026-09-27 闭合复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `a4ccb383` 替代（当前有效，管理性回填；被审 v3 `7e10cb25` 保留历史） |
| `specs/creature-rpg/wp29-shops-and-exchanges.md` | 无中间版本 | 2026-09-26 首版 | 批次首发固定为 `3705047f`（21,918 字节，被审首版；含自检修正后的当前值）；经首审 REQUEST_CHANGES（WP29-R01/R02＋BATCH-C02）修订被 `d5c847f1` 替代（v2，被审版）；经有限复审（7 项关闭、剩 R02）收尾修订被 `1ed4b957` 替代（v3；被审 v2 `d5c847f1` 保留历史）；经 2026-09-27 闭合复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `f7788c7d` 替代（当前有效，管理性回填；被审 v3 `1ed4b957` 保留历史） |
| `review/wp31-wp28-wp29-delivery-2026-09-26/delivery-summary.md` | `3f832427` | 2026-09-26 首版 | 批次首发固定为 `3f832427`（8,403 字节）；经首审修订注记（v2）被 `023c090e` 替代（v2）；经有限复审注记（v3）被 `6b22ac03` 替代（v3）；经闭合回填 v4 注记被 `990f30b4` 替代（当前有效，v4） |
| `specs/creature-rpg/wp33-daycare-and-breeding-session.md` | 无中间版本 | 2026-09-27 首版 | WP33→WP34→WP35 批次首发固定为 `4e17c679`（21,180 字节，被审首版、保留历史）；经 2026-09-27 首审 REQUEST_CHANGES（WP33-R01/R02＋BATCH-C01/C02）修订被 `6cb65468` 替代（v2 修订稿，被审版）；经 2026-09-27 v2 复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `8c678e33` 替代（当前有效，管理性回填；被审 v2 `6cb65468` 保留历史） |
| `specs/pokemon-rules/wp34-inheritance-and-offspring.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `bb950920`（24,359 字节，被审首版、保留历史）；经首审 REQUEST_CHANGES（WP34-R01～R03）修订被 `7ba35a9d` 替代（v2 修订稿，被审版）；经 2026-09-27 v2 复审 R03 收尾（末次普通异色缓存时点）修订被 `d0113d76` 替代（v3；引用 WP33 回填后哈希 `8c678e33`）；经 2026-09-27 闭合复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `8e3511d3` 替代（管理性回填；被审 v3 `d0113d76` 保留历史）；经 WP39 轮 WP33 依赖行与导入语同步（管理性）被 `46acc90f` 替代（30,716 字节，当前有效） |
| `specs/creature-rpg/wp35-eggs-and-hatching.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `61a6bdb9`（19,715 字节，被审首版、保留历史）；经首审 REQUEST_CHANGES（WP35-R01～R03）修订被 `0abe2622` 替代（v2 修订稿，被审版）；经 2026-09-27 v2 复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `315e74f6` 替代（管理性回填；被审 v2 `0abe2622` 保留历史）；经 WP34 回填后引用同步（管理性）被 `34e83236` 替代；经 WP59 轮 BATCH-C02 头部引用同步（管理性）被 `1fbfd98e` 替代；经 WP39 轮 WP34 回填后哈希引用同步（管理性）被 `34f1a5df` 替代（24,610 字节，当前有效） |
| `review/wp33-wp35-delivery-2026-09-27/delivery-summary.md` | `8c420fa7` | 2026-09-27 首版 | 批次首发固定为 `8c420fa7`（7,573 字节）；经首审修订注记（v2）被 `462ee890` 替代（v2）；经 v2 复审收尾注记（v3）被 `28cbc965` 替代（v3）；经闭合复审收尾注记（v4）被 `6b1d9a1a` 替代（当前有效，v4） |
| `specs/overworld/wp59-world-time-weather-field-moves.md` | 无中间版本 | 2026-09-27 首版 | WP59→WP36→WP60 批次首发固定为 `971b0807`（34,153 字节，批内固定、尚未外审；被审 v1）；经首审 REQUEST_CHANGES（WP59-R01～R04）修订被 `440a67b1` 替代（v2 修订稿，被审版）；经 v2 复审收尾（R02/R04＋C03）修订被 `9a41d185` 替代（42,041 字节，v3 收尾稿，被审版）；经闭合回填（C04＋状态）修订被 `46e80106` 替代（42,401 字节，当前有效，管理性回填；被审 v3 `9a41d185` 保留历史） |
| `specs/creature-rpg/wp36-wild-encounters-and-modifiers.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `b8a5bc26`（27,307 字节；引用 WP59 批内哈希 `971b0807`、尚未外审；被审 v1）；经首审 REQUEST_CHANGES（WP36-R01～R04）修订与 WP59 v2 级联被 `3120d1e1` 替代（32,592 字节，v2 修订稿，被审版）；经 v2 复审收尾（R02＋C01 剩余一条）与 WP59 v3 级联被 `d21edcc7` 替代（33,424 字节，v3 收尾稿，被审版）；经闭合回填（C04＋状态）与 WP59 回填后级联被 `5a05aad7` 替代（34,305 字节，当前有效，管理性回填；被审 v3 `d21edcc7` 保留历史） |
| `specs/pokemon-rules/wp60-berry-plants.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `227bb696`（20,545 字节；引用 WP59/WP36 批内哈希、尚未外审；被审 v1）；经首审 REQUEST_CHANGES（WP60-R01～R03）修订与上游级联被 `e468c3bf` 替代（24,593 字节，v2 修订稿，被审版）；经 v2 复审收尾（R01＋C03.4）与上游 v3 级联被 `114c432b` 替代（24,912 字节，v3 收尾稿，被审版）；经闭合回填（状态＋上游级联）被 `1d588f0a` 替代（25,082 字节，当前有效，管理性回填；被审 v3 `114c432b` 保留历史） |
| `specs/overworld/wp60-fishing.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `b7de3ff4`（16,866 字节；引用 WP59/WP36 批内哈希、尚未外审；被审 v1）；经首审 REQUEST_CHANGES（WP60-R04/R05）修订、上游级联与 C02 引用同步（§1 WP27→WP28）被 `f280e9a7` 替代（20,304 字节，v2 修订稿，被审版）；经 v2 复审收尾（WP36-R02 传播＋C03.3）与上游 v3 级联被 `5f274a2c` 替代（20,759 字节，v3 收尾稿，被审版）；经闭合回填（状态＋上游级联）被 `e5d94e05` 替代（20,950 字节，当前有效，管理性回填；被审 v3 `5f274a2c` 保留历史） |
| `review/wp59-wp36-wp60-delivery-2026-09-27/delivery-summary.md` | `407c61a5` | 2026-09-27 首版 | 批次首发固定为 `407c61a5`（7,191 字节，被审 v1）；经首审修订注记（v2，首批哈希与修订材料入表）被 `835334ef` 替代（10,390 字节，v2 注记；短标签笔误于第四十四轮更正）；经 v2 复审收尾注记（v3）被 `809e0fa0` 替代（v3）；经闭合回填 v4 注记被 `6d74f799` 替代（12,913 字节，当前有效，v4） |
| `review/wp59-wp36-wp60-delivery-2026-09-27/self-checks.json` | `86348342` | 2026-09-27 首版 | 批次首发固定为 `86348342`（6,866 字节，被审 v1）；经首审修订同步（受影响结论更正、旧结论留史）被 `4f9c02d8` 替代（11,965 字节，v2）；经 v2 复审收尾同步（入口分列、向量分列）被 `3bad9fd6` 替代（12,955 字节，当前有效，v3） |
| `review/wp59-wp36-wp60-delivery-2026-09-27/boundary-checks.json` | `cef81335` | 2026-09-27 首版 | 批次首发固定为 `cef81335`（4,074 字节，被审 v1）；经首审修订同步（组 2/3/4/5 更正）被 `b12ebefd` 替代（6,271 字节，v2）；经 v2 复审收尾同步（组 2/4/5）被 `db51d641` 替代（6,903 字节，当前有效，v3） |
| `specs/combat/wp39-battle-context-and-participants.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `26c72739`（34,016 字节，被审 v1）；经首审 REQUEST_CHANGES（WP39-R01～R03＋C01/C02）修订被 `1fdfb8bc` 替代（38,555 字节，v2 修订稿，被审版）；经 v2 复审三项收尾、C03 与必要级联（v3；尚未外审），修订前完整身份 `1fdfb8bc8c12ab33bde658f4569849a097f9a0fea0bcd058b6ee02dd5479e197`（38,555 字节，被审 v2）被 `864dec262b0d7e3f9bdc4944bab07f2c2bcefd459fee2f6a46af9323bf0122f5` 替代（42,165 字节，当前有效；v3）；经2026-09-27 闭合复审PASS_SCOPED后的管理性回填及必要完整哈希级联，修订前 `864dec262b0d7e3f9bdc4944bab07f2c2bcefd459fee2f6a46af9323bf0122f5`（42,165字节，被审v3）留史，当前被 `9a3a796f08335bc7d4886c7e2b11f3b273c955e24ba9d6fe966c60103df5719b` 替代（42,697字节，回填后版本，已限定通过） |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `3ced6de7`（33,115 字节，被审 v1；引用 WP39 批内哈希）；经首审 REQUEST_CHANGES（WP40-R01～R05＋C01/C02）修订与 WP39 v2 级联被 `555282ba` 替代（38,012 字节，v2 修订稿，被审版）；经 v2 复审三项收尾、C03 与必要级联（v3；尚未外审），修订前完整身份 `555282ba37ae92ae1fb75b2fbfebc5a989efe4a7f73e956dae714c6d097f7cde`（38,012 字节，被审 v2）被 `716a244244248bc25d626ed487fc4b47b65cd942942a3d9647821cbfde84ef7d` 替代（40,100 字节，当前有效；v3）；经2026-09-27 闭合复审PASS_SCOPED后的管理性回填及必要完整哈希级联，修订前 `716a244244248bc25d626ed487fc4b47b65cd942942a3d9647821cbfde84ef7d`（40,100字节，被审v3）留史，当前被 `07789951f9aaaa7cac82508218a3f58c76caa735e18e4fad9f9a2dcd123a80d3` 替代（40,547字节，回填后版本，已限定通过）；2026-09-27经N01新证据确认后的局部行为简写校准；既有限定Reviewed保留，实际修订待复核，修订前完整身份 `07789951f9aaaa7cac82508218a3f58c76caa735e18e4fad9f9a2dcd123a80d3`（40,547字节）留史，被 `ad4718722897ef448623fb2bdcd7e9e8ca9a51538a5015edc331fcae50516654` 替代（42,476字节，当前有效）；2026-09-27经本轮有限复审PASS_SCOPED后状态／引用管理回填，修订前完整身份 `ad4718722897ef448623fb2bdcd7e9e8ca9a51538a5015edc331fcae50516654`（42,476字节，历史被审／登记版）留史，被 `13ac33470f375f2a3c5f0af7acddb6b038b98ba058e73397f39babf592d32b42` 替代（42,751字节，当前有效；新字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）独立批准三摘要定点同步，原限定Reviewed保留；旧完整身份 `13ac33470f375f2a3c5f0af7acddb6b038b98ba058e73397f39babf592d32b42`（42,751字节，被审首稿／前轮登记版）保留，被 `8c80e5f3f4c3d6ad151bfa65c8a4fce5691adafb318b14565f89f929b24acbe8` 替代（43,769字节，当前有效；新字节不冒充旧被审对象） |
| `specs/combat/wp41-switching-positioning-and-escape.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `75746653`（23,900 字节，被审 v1；引用 WP40 批内哈希）；经首审 REQUEST_CHANGES（WP41-R01～R04＋C01/C02）修订与 WP40 v2／WP39 v2 级联被 `237ac575` 替代（28,916 字节，v2 修订稿，被审版）；经 v2 复审三项收尾、C03 与必要级联（v3；尚未外审），修订前完整身份 `237ac575dc1da67e4e9776d6f28a24a7bbefb239cbccc9e9d9a40897f3d93033`（28,916 字节，被审 v2）被 `463cab3c062a366a7b142f66248ea9e5bb5bacb9a12ff8748f930aefd498a2ec` 替代（31,502 字节，当前有效；v3）；经2026-09-27 闭合复审PASS_SCOPED后的管理性回填及必要完整哈希级联，修订前 `463cab3c062a366a7b142f66248ea9e5bb5bacb9a12ff8748f930aefd498a2ec`（31,502字节，被审v3）留史，当前被 `e6b835af5db676a28b80e7fb1513cf379267b2cdab427c7e9cc916e8e8a4c234` 替代（31,897字节，回填后版本，已限定通过）；2026-09-27经WP40 N01后完整哈希引用管理性级联，行为不变，修订前完整身份 `e6b835af5db676a28b80e7fb1513cf379267b2cdab427c7e9cc916e8e8a4c234`（31,897字节）留史，被 `42878fac04b7ba5e195663f183fb484489200bab8ef5dc17333b0c0525b14085` 替代（31,939字节，当前有效）；2026-09-27经本轮有限复审PASS_SCOPED后状态／引用管理回填，修订前完整身份 `42878fac04b7ba5e195663f183fb484489200bab8ef5dc17333b0c0525b14085`（31,939字节，历史被审／登记版）留史，被 `1b7e395b98727e3aa7272ad73d3873c77f4581d0acd18ac71cc6703736a77ccb` 替代（31,948字节，当前有效；新字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）独立批准三摘要定点同步，原限定Reviewed保留；旧完整身份 `1b7e395b98727e3aa7272ad73d3873c77f4581d0acd18ac71cc6703736a77ccb`（31,948字节，被审首稿／前轮登记版）保留，被 `a5232a1ed18dc24257748c34b2ec83eca9730e2c8ef077c7be638ff3b4d38036` 替代（33,281字节，当前有效；新字节不冒充旧被审对象） |
| `review/wp39-wp41-delivery-2026-09-27/delivery-summary.md` | `f23ddcb0` | 2026-09-27 首版 | 批次首发固定为 `f23ddcb0`（6,286 字节，被审 v1）；经首审修订注记（v2）被 `f9209703` 替代（8,855 字节，v2）；经 v2 复审三项收尾、C03 与必要级联（v3；尚未外审），修订前完整身份 `f9209703a127a2165d3c821d5e42487e5cd4e61bb2993e66ade0bb51c40b948e`（8,855 字节，被审 v2）被 `8360aec47b2bff8d03287fb07e23a96a7dc229cdf305ba071f7a79794d19e841` 替代（11,292 字节，当前有效；v3）；经2026-09-27 闭合回填及新批具名状态／摘要维护，修订前 `8360aec47b2bff8d03287fb07e23a96a7dc229cdf305ba071f7a79794d19e841`（11,292字节，被审v3）留史，当前被 `a1df7ee38a71874e5ab14586a7dc4551e8bfdbfda7a0182a8ba4467a1ed16b20` 替代（12,006字节，当前有效） |
| `review/wp39-wp41-delivery-2026-09-27/self-checks.json` | `469c9b30` | 2026-09-27 首版 | 批次首发固定为 `469c9b30`（8,486 字节，被审 v1）；经首审修订同步被 `9633f336` 替代（12,444 字节，v2）；经 v2 复审三项收尾、C03 与必要级联（v3；尚未外审），修订前完整身份 `9633f336394ae2577c5784d5e1f3e736e310c147a614d6901478b239a94adbd7`（12,444 字节，被审 v2）被 `6d16628fb0c8b2819c6a83aa792785849ce839d8ce95a695121ffd2d18b6a8ea` 替代（23,048 字节，当前有效；v3） |
| `review/wp39-wp41-delivery-2026-09-27/boundary-checks.json` | `4d942a4e` | 2026-09-27 首版 | 批次首发固定为 `4d942a4e`（3,985 字节，被审 v1）；经首审修订同步被 `0db06e68` 替代（5,323 字节，v2）；经 v2 复审三项收尾、C03 与必要级联（v3；尚未外审），修订前完整身份 `0db06e6834764314a7b1247fd808bef4f67fbddacbe6fd5c60e3a29bebc21a4a`（5,323 字节，被审 v2）被 `46a58b20347ce9089cec89497d046a2270fc28eb9599f052b66ed4f03bd949d0` 替代（6,926 字节，当前有效；v3） |



| `specs/pokemon-rules/wp43-types-accuracy-and-damage.md` | `6021d835` | 2026-09-27被审首版v1 | 2026-09-27经首审PASS_SCOPED后Reviewed管理回填、N01记录与上游身份同步；基础计算不重写，修订前完整身份 `6021d835ebd2b62eac63062c5475e53501b5e6d46ff94873f2284799cf11ef0e`（29,511字节）留史，被 `0cd9958c256ef2caf7d6f9933127f35e5644131a3a97ed79d46998c6bcc15688` 替代（30,543字节，当前有效）；2026-09-27经本轮有限复审PASS_SCOPED后状态／引用管理回填，修订前完整身份 `0cd9958c256ef2caf7d6f9933127f35e5644131a3a97ed79d46998c6bcc15688`（30,543字节，历史被审／登记版）留史，被 `b5ac8946316fae5cac765db52d2344767bca2f9e5abed52ebfc331a216040ed7` 替代（30,921字节，当前有效；新字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `b5ac8946316fae5cac765db52d2344767bca2f9e5abed52ebfc331a216040ed7`（30,921字节，被审首稿／前轮登记版）保留，被 `d8ba547b3c1f8338f9f00fdac67c146ecd147942c94d576f77d27e4375cb905b` 替代（30,921字节，当前有效；新字节不冒充旧被审对象） |
| `specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md` | `b7eae260` | 2026-09-27被审首版v1 | 2026-09-27经首审指定编号及C01有限修订为v2，ReviewPending，尚未通过复审，修订前完整身份 `b7eae260636adef8e1e301737765c5ab396216f481086aecaab0c42857a1cf67`（35,014字节）留史，被 `85e17c6c15225040eb5dd5f38503bbcac6c8fd96916f40270e3c989e86559311` 替代（49,950字节，当前有效）；2026-09-27经本轮有限复审PASS_SCOPED后状态／引用管理回填，修订前完整身份 `85e17c6c15225040eb5dd5f38503bbcac6c8fd96916f40270e3c989e86559311`（49,950字节，历史被审／登记版）留史，被 `a4e82ddf09d9d9db4e4d610e8dc074d5ef093136b74290dd83b84f764a6bdf9c` 替代（50,426字节，当前有效；新字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `a4e82ddf09d9d9db4e4d610e8dc074d5ef093136b74290dd83b84f764a6bdf9c`（50,426字节，被审首稿／前轮登记版）保留，被 `3d4d9c40d83746459df0c89353a046abd8d4ca32e82e2de76e0ab44499273d1e` 替代（50,426字节，当前有效；新字节不冒充旧被审对象） |
| `specs/pokemon-rules/wp44-effect-coverage.md` | `ea5237d3` | 2026-09-27被审首版v1 | 2026-09-27经首审指定编号及C01有限修订为v2，ReviewPending，尚未通过复审，修订前完整身份 `ea5237d3257e1326876d3aae8d36c9bac003eb9682ad7402b05bc02797b45e39`（24,809字节）留史，被 `47bd80e20c877e612bb99e6929cf46b2efe7d87d94862760e9871234eecac3ef` 替代（27,133字节，当前有效）；2026-09-27经本轮有限复审PASS_SCOPED后状态／引用管理回填，修订前完整身份 `47bd80e20c877e612bb99e6929cf46b2efe7d87d94862760e9871234eecac3ef`（27,133字节，历史被审／登记版）留史，被 `c226232d523b899197590800b8e6f75230de103363eebf6c12a16111a24cb2ad` 替代（27,346字节，当前有效；新字节不冒充原被审对象） |
| `specs/combat/wp45-weather-terrain-side-and-position-effects.md` | `2fbe3b65` | 2026-09-27被审首版v1 | 2026-09-27经首审指定编号及C01有限修订为v2，ReviewPending，尚未通过复审，修订前完整身份 `2fbe3b6586b41214f02a8e1ec59257dad5dd740f5ce882279497e388f7a8afab`（34,109字节）留史，被 `f92b0f3cfa807d0c9a069fb586cde3673f878d4762dbede3425b08b86f06f35b` 替代（35,823字节，当前有效）；2026-09-27经本轮有限复审PASS_SCOPED后状态／引用管理回填，修订前完整身份 `f92b0f3cfa807d0c9a069fb586cde3673f878d4762dbede3425b08b86f06f35b`（35,823字节，历史被审／登记版）留史，被 `7ddb026aa71e8576d54ab2f98df5e78e84066e28eccbada4f551ca5ae58e5d95` 替代（36,525字节，当前有效；新字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `7ddb026aa71e8576d54ab2f98df5e78e84066e28eccbada4f551ca5ae58e5d95`（36,525字节，被审首稿／前轮登记版）保留，被 `046e8bf04fc663e41a6e48c3f9aaa193022d141fea39752eeb2db87a306bd597` 替代（36,525字节，当前有效；新字节不冒充旧被审对象） |
| `review/wp43-wp45-delivery-2026-09-27/self-checks.json` | `3c1259dd` | 2026-09-27被审首版v1 | 2026-09-27经WP43回填与三项有限修订、N01/C01的追踪／交付同步v2，修订前完整身份 `3c1259dd3f8966282b7880de4bee02b8c7a5bcd8640ed6dae8e729dc6b841113`（40,415字节）留史，被 `307d1ff0d54d9c1ddbcf8ee10f6161e6eff044cb5d486352b3acab643313004d` 替代（56,423字节，当前有效） |
| `review/wp43-wp45-delivery-2026-09-27/boundary-checks.json` | `c20c3cbc` | 2026-09-27被审首版v1 | 2026-09-27经WP43回填与三项有限修订、N01/C01的追踪／交付同步v2，修订前完整身份 `c20c3cbcf1e0488f899ab8ff389635543efc49a5499f58741456ad481200687a`（4,122字节）留史，被 `21abfe14138ed5e2fcd5ba3d3f0b499d192326e970c4495a905fcafa0098ac4e` 替代（6,629字节，当前有效） |
| `review/wp43-wp45-delivery-2026-09-27/delivery-summary.md` | `96b9abf4` | 2026-09-27被审首版v1 | 2026-09-27经WP43回填与三项有限修订、N01/C01的追踪／交付同步v2，修订前完整身份 `96b9abf484d4eafa958b81f41c4755ff250e19c240804577a74236eed3027619`（8,597字节）留史，被 `39275cb4291ba561557e2ee014cb5c1d5236836bcd615d981b8a31878d8b2d7d` 替代（9,790字节，当前有效）；2026-09-27经本轮管理回填与新三包增量维护，修订前完整身份 `39275cb4291ba561557e2ee014cb5c1d5236836bcd615d981b8a31878d8b2d7d`（9,790字节，历史被审／登记版）留史，被 `4cc8e434e1a7d1feca37dce2290626055fd41fbc8d3dc8215ddc1ef43960e35d` 替代（10,636字节，当前有效；新字节不冒充原被审对象） |


| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | 无历史被审版 | 2026-09-27首稿v1 | 当前首发 `9bde1314b9b96f36fa243abfd0ca965775dd651c7861e0f20f475d5f83d97161`（37,859字节），批内固定、ReviewPending；没有独立审查通过历史；2026-09-27经WP42／WP48／WP49首审有限修订v2及直接传播；被审／修订前完整身份 `9bde1314b9b96f36fa243abfd0ca965775dd651c7861e0f20f475d5f83d97161`（37,859字节，v1／此前登记版）留史，被 `6644c77775b1e02481674079c847652dbbf2c566214d3969f1f333f741c22f7d` 替代（41,329字节，当前有效；v2未外审，非Reviewed）；2026-09-27经v2有限复审PASS_SCOPED后的管理回填／必要身份级联；修订前完整身份 `6644c77775b1e02481674079c847652dbbf2c566214d3969f1f333f741c22f7d`（41,329字节，被审v2／前轮登记版）保留，被 `8b8149c3b1f6ee7d130802a4fe1638404a5ac76e7927ee4ce77c85ee5127620f` 替代（41,759字节，当前有效；新管理字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `8b8149c3b1f6ee7d130802a4fe1638404a5ac76e7927ee4ce77c85ee5127620f`（41,759字节，被审首稿／前轮登记版）保留，被 `126e2612e2776c41557475a98cd97b8ef40a0a7f02fd95f16c434de49855a3eb` 替代（41,759字节，当前有效；新字节不冒充旧被审对象） |

| `specs/pokemon-rules/wp48-ability-calculation-modifiers.md` | 无历史被审版 | 2026-09-27首稿v1 | 当前首发 `480016af9731a97607300ae84851b6b6286ae624b1452a0193b849295f2b3728`（34,233字节），批内固定、ReviewPending；没有独立审查通过历史；2026-09-27经WP42／WP48／WP49首审有限修订v2及直接传播；被审／修订前完整身份 `480016af9731a97607300ae84851b6b6286ae624b1452a0193b849295f2b3728`（34,233字节，v1／此前登记版）留史，被 `87e39127e14eddd10f6e0d10e6d63999e0cb9ff70fa0e2505dc97a195f3b3bb8` 替代（35,021字节，当前有效；v2未外审，非Reviewed）；2026-09-27经v2有限复审PASS_SCOPED后的管理回填／必要身份级联；修订前完整身份 `87e39127e14eddd10f6e0d10e6d63999e0cb9ff70fa0e2505dc97a195f3b3bb8`（35,021字节，被审v2／前轮登记版）保留，被 `457a47b0438a5664fa75e1988251e5aefea2620efec0c006c4f78f7c12a00611` 替代（35,320字节，当前有效；新管理字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `457a47b0438a5664fa75e1988251e5aefea2620efec0c006c4f78f7c12a00611`（35,320字节，被审首稿／前轮登记版）保留，被 `1c701d507747d95ba456f3df8a2697b0a1e409d1508dd2d8651b7d50d102403c` 替代（35,320字节，当前有效；新字节不冒充旧被审对象） |

| `specs/combat/wp49-ability-phase-triggers.md` | 无历史被审版 | 2026-09-27首稿v1 | 当前首发 `9286900834514d363d0e15b50aeefdd581c0b86b930c9cfe006421dcc470ca6d`（50,601字节），批内固定、ReviewPending；没有独立审查通过历史；2026-09-27经WP42／WP48／WP49首审有限修订v2及直接传播；被审／修订前完整身份 `9286900834514d363d0e15b50aeefdd581c0b86b930c9cfe006421dcc470ca6d`（50,601字节，v1／此前登记版）留史，被 `7a4ecf931a65931cd8c6255d09b2697f83a5b538da907a016e5712efa32a67d7` 替代（52,573字节，当前有效；v2未外审，非Reviewed）；2026-09-27经v2有限复审PASS_SCOPED后的管理回填／必要身份级联；修订前完整身份 `7a4ecf931a65931cd8c6255d09b2697f83a5b538da907a016e5712efa32a67d7`（52,573字节，被审v2／前轮登记版）保留，被 `b5c083209e218dc17d7490cc2f171a653502d05e58ec66b83b403ea6d96b4e25` 替代（53,127字节，当前有效；新管理字节不冒充原被审对象）；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `b5c083209e218dc17d7490cc2f171a653502d05e58ec66b83b403ea6d96b4e25`（53,127字节，被审首稿／前轮登记版）保留，被 `e41ca96da9f15bc88526f31337aefe3ba767b9b19776ceba0a6472df1061253c` 替代（53,127字节，当前有效；新字节不冒充旧被审对象） |


| `review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md` | `c688fc9d` | 2026-09-27被审首稿v1 | 2026-09-27经WP42／WP48／WP49首审有限修订v2及直接传播；被审／修订前完整身份 `c688fc9d509fa605b69dd4a29bc69e990f98668ed15ae83dd52f913844406f1a`（5,577字节，v1／此前登记版）留史，被 `e41b85316b620dede8ce1b8c30f61cbbdabee155a069ae34bbce19c5258a1e58` 替代（8,520字节，当前有效；v2未外审，非Reviewed）；2026-09-27经本轮管理状态与新批交付增量维护；修订前完整身份 `e41b85316b620dede8ce1b8c30f61cbbdabee155a069ae34bbce19c5258a1e58`（8,520字节，被审v2／前轮登记版）保留，被 `498dde568f7c77c30c35d28e2ab492622b7c985c0243977683b54d184111f695` 替代（9,388字节，当前有效；新管理字节不冒充原被审对象） |

| `review/wp42-wp48-wp49-delivery-2026-09-27/self-checks.json` | `d7ffb5cd` | 2026-09-27被审首稿v1 | 2026-09-27经WP42／WP48／WP49首审有限修订v2及直接传播；被审／修订前完整身份 `d7ffb5cdad8253c7f2b52f7419ece41786febe8984bf621179956bbdfbcf80c7`（87,252字节，v1／此前登记版）留史，被 `939f7e366b0c75feb45275e5ee340647715499cde96144b22bb78273925864e3` 替代（102,908字节，当前有效；v2未外审，非Reviewed） |

| `review/wp42-wp48-wp49-delivery-2026-09-27/boundary-checks.json` | `d0eef5f4` | 2026-09-27被审首稿v1 | 2026-09-27经WP42／WP48／WP49首审有限修订v2及直接传播；被审／修订前完整身份 `d0eef5f44519273d94662ab9f8b1b334804ba8bdf97039af916dcee99c6eae34`（9,704字节，v1／此前登记版）留史，被 `9509999c8dadeba83dfeceb39fd4d45d7d0b1494e1837abed8f01163792a309b` 替代（14,399字节，当前有效；v2未外审，非Reviewed） |


| `specs/pokemon-rules/wp46-damage-multihit-and-healing.md` | 无历史被审版 | 2026-09-27本批首稿v1 | 首发固定 `0e5a676e234a71a949602d93a2a6aeb4c26cf09acc894e47eee66eb3c1e8a323`（47,352字节），ReviewPending；自检不代替外审，批内引用尚未外审；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `0e5a676e234a71a949602d93a2a6aeb4c26cf09acc894e47eee66eb3c1e8a323`（47,352字节，被审首稿／前轮登记版）保留，被 `aa9a7f1e206275ce934a1bc3cf860813bafac852795a5d939316c6f5d9e8bf4c` 替代（47,646字节，前轮登记版）留史，再被 `0f7c9b4b21ec45c2084876de08218812aab7a615b6fb2d53ff1c0de603d3b662` 替代（48,872字节，当前有效；N01定点同步，新字节不冒充旧被审对象） |

| `specs/pokemon-rules/wp46-damage-healing-coverage.md` | 无历史被审版 | 2026-09-27本批首稿v1 | 首发固定 `170e063faaea4b66b5e8a7fc0b9bba907ff7aba7b4c15d8f435ff50d51f7ce88`（36,408字节），ReviewPending；自检不代替外审，批内引用尚未外审；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `170e063faaea4b66b5e8a7fc0b9bba907ff7aba7b4c15d8f435ff50d51f7ce88`（36,408字节，被审首稿／前轮登记版）保留，被 `549cd587095df207bf359c34fd66f14f2dda0c93ce1dcaec6bf4f63fc4d084c1` 替代（36,824字节，当前有效；新字节不冒充旧被审对象） |

| `specs/combat/wp47-a-move-attributes-targeting-and-calling.md` | 无历史被审版 | 2026-09-27本批首稿v1 | 首发固定 `ad6a6d6c4d5c90dbf32f5cd0c843a84dad605319ee4a99c1d5d3d04f8f57b49c`（33,207字节），ReviewPending；自检不代替外审，批内引用尚未外审；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `ad6a6d6c4d5c90dbf32f5cd0c843a84dad605319ee4a99c1d5d3d04f8f57b49c`（33,207字节，被审首稿／前轮登记版）保留，被 `1b1dea7cee12b38d867f81122718e328857bc8f17096632e9178bf07b5ff6675` 替代（33,611字节，前轮登记版）留史，再被 `e49349438e19be9bbd09bcc192e69f4d839a8e715c46cf09291f0f8c5c390f96` 替代（34,014字节，当前有效；必要身份级联，新字节不冒充旧被审对象） |

| `specs/combat/wp47-a-attributes-targeting-calling-data.md` | 无历史被审版 | 2026-09-27本批首稿v1 | 首发固定 `1c164a68ed2d35c1dceaa9314038a9fe0f6a011c845a9adf512f740a466a898c`（18,920字节），ReviewPending；自检不代替外审，批内引用尚未外审；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `1c164a68ed2d35c1dceaa9314038a9fe0f6a011c845a9adf512f740a466a898c`（18,920字节，被审首稿／前轮登记版）保留，被 `49e343003be7c22653cad121f3c037b915212da18b6240cda12e653d07c91a17` 替代（19,340字节，当前有效；新字节不冒充旧被审对象） |

| `specs/combat/wp47-b-switching-control-and-item-changes.md` | 无历史被审版 | 2026-09-27本批首稿v1 | 首发固定 `24185ce4179387c900b11e3505d9309f1869ba8587aa2bd263609f1eec25c0bd`（37,934字节），ReviewPending；自检不代替外审，批内引用尚未外审；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `24185ce4179387c900b11e3505d9309f1869ba8587aa2bd263609f1eec25c0bd`（37,934字节，被审首稿／前轮登记版）保留，被 `0287e0b2ea569d24330933ae06498e61237eb0dc9d4116efa9783cc72f739317` 替代（38,558字节，前轮登记版）留史，再被 `007699019544203b9b5f4c42f18db8eb91711d2d96f6fa8afdf047d44b16e778` 替代（39,000字节，当前有效；必要身份级联，新字节不冒充旧被审对象） |

| `specs/combat/wp47-b-control-items-coverage-data.md` | 无历史被审版 | 2026-09-27本批首稿v1 | 首发固定 `3a092b6653b0d283a47e45aa4ed9b06b04ca62683a14b17b42048829bf00d83c`（17,454字节），ReviewPending；自检不代替外审，批内引用尚未外审；2026-09-27批（2026-09-28收尾）首审PASS_SCOPED后限定Reviewed回填／C01维护／必要身份级联；旧完整身份 `3a092b6653b0d283a47e45aa4ed9b06b04ca62683a14b17b42048829bf00d83c`（17,454字节，被审首稿／前轮登记版）保留，被 `0736044d556367392e2a0204a4a934a903d3472c9cb28435b4765798d915d13a` 替代（17,922字节，当前有效；新字节不冒充旧被审对象） |


| `review/wp46-wp47-delivery-2026-09-27/self-checks.json` | 被审v1原件在本轮input-snapshot | v2管理维护 | 2026-09-27批（2026-09-28收尾）本批管理状态、配套材料与新交付增量维护；旧完整身份 `da4c44a0fbd29ce8d656e98a102d331b8a13c0acd6de4b8c62b511b13c59d57b`（203,805字节，被审首稿／前轮登记版）保留，被 `eda9101ab5b563f5c3b53e53b029a6d0c82ec8e96a7358c3e4e0c6c7be2318c9` 替代（209,456字节，当前有效；新字节不冒充旧被审对象） |

| `review/wp46-wp47-delivery-2026-09-27/boundary-checks.json` | 被审v1原件在本轮input-snapshot | v2管理维护 | 2026-09-27批（2026-09-28收尾）本批管理状态、配套材料与新交付增量维护；旧完整身份 `b39ff17c64ab09e136b031968ed44d3cfbaf826d81517103bbbb7b27f215503b`（10,413字节，被审首稿／前轮登记版）保留，被 `2cb48235c7794e4167128a399f04c9cb3465e299c9096da1ecde6e49f9d6dae0` 替代（23,256字节，当前有效；新字节不冒充旧被审对象） |

| `review/wp46-wp47-delivery-2026-09-27/delivery-summary.md` | 被审v1原件在本轮input-snapshot | v2管理维护 | 2026-09-27批（2026-09-28收尾）本批管理状态、配套材料与新交付增量维护；旧完整身份 `85f4df02f5592cca3d91fbbb46aec7d86ea5378f83012661455f04910beb0554`（6,945字节，被审首稿／前轮登记版）保留，被 `73226fe59a5b6036bdabb913f121d5cadd76e23ad2f62c9a54dc686d173697c6` 替代（6,036字节，当前有效；新字节不冒充旧被审对象） |

| `specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md` | 无历史被审版 | 本批首稿v1 | 固定 `937551e00ec61a8a807bfa197ece1e2f91b6b5f91f620375e6c14ea900e9027a`（29,336字节），ReviewPending；批内固定尚未外审，运行保留；2026-09-28经两项有限修订与WP51状态/上游身份直接传播，继续ReviewPending；旧完整身份 `937551e00ec61a8a807bfa197ece1e2f91b6b5f91f620375e6c14ea900e9027a`（29,336字节，被审首稿v1／前轮登记版）保留，被 `fcbbca67dafbb1aaa1cfd2560983a6f34830c31c11feccb7688f08b372a395b1` 替代（31,648字节，当前有效；当前新字节不冒充本轮被审对象）；2026-09-28经独立有限复审后的限定Reviewed回填/必要身份与表格维护；旧完整身份 `fcbbca67dafbb1aaa1cfd2560983a6f34830c31c11feccb7688f08b372a395b1`（31,648字节，被审v2或WP50附表v1／前轮登记版）保留，被 `6c97afebe925f9cbe4aedfb1deb815b1d3277bd952ceae04e532887a16cd9627` 替代（32,132字节，前轮登记版）留史，再被 `f0b6b1472ed1eceb7679c0bf50d836076a0a52a593ce011132ee90c1e01e6f72` 替代（32,490字节，当前管理字节不冒充被审对象） |

| `specs/pokemon-rules/wp50-held-item-effect-coverage.md` | 无历史被审版 | 本批首稿v1 | 固定 `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686`（13,855字节），ReviewPending；批内固定尚未外审，运行保留；2026-09-28经独立有限复审后的限定Reviewed回填/必要身份与表格维护；旧完整身份 `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686`（13,855字节，被审v2或WP50附表v1／前轮登记版）保留，被 `f62603f26e7570e32949ebce97c531ef0af59ba6da4f083bff9d85775de2fc69` 替代（14,418字节，当前管理字节不冒充被审对象） |

| `specs/combat/wp51-ai-action-selection-and-skill.md` | 无历史被审版 | 本批首稿v1 | 固定 `1174d485f2648682cbd98a446044dfd487bab694d7afdb94e309f3d3fe4a6972`（25,064字节），ReviewPending；批内固定尚未外审，运行保留；2026-09-28经WP51首审PASS_SCOPED后C01非阻塞维护与限定Reviewed回填；旧完整身份 `1174d485f2648682cbd98a446044dfd487bab694d7afdb94e309f3d3fe4a6972`（25,064字节，被审首稿v1／前轮登记版）保留，被 `baebd58a7f4eed635f685f583fa7b4d21785a9ac13a0a1ee4c2ccd6ec7b6bac5` 替代（26,784字节，当前有效；当前新字节不冒充本轮被审对象）；2026-09-28经独立有限复审后的限定Reviewed回填/必要身份与表格维护；旧完整身份 `baebd58a7f4eed635f685f583fa7b4d21785a9ac13a0a1ee4c2ccd6ec7b6bac5`（26,784字节，被审v2或WP50附表v1／前轮登记版）保留，被 `8deea695576b9786d5026dd9a66ce7ea3c4dc7d3332b88891d23a8998c6b87a0` 替代（27,283字节，前轮登记版）留史，再被 `2b0847b5d52d9907804c62703871a9a6557a6b9940a8fd0a93c702329808a025` 替代（27,645字节，当前管理字节不冒充被审对象） |

| `specs/combat/wp51-ai-decision-defaults.md` | 无历史被审版 | 本批首稿v1 | 固定 `f3837410a9c41617495d2691e69f2e7baa11e7e5c3d7521f618a0f1472ad6c09`（4,811字节），ReviewPending；批内固定尚未外审，运行保留；2026-09-28经WP51首审PASS_SCOPED后C01非阻塞维护与限定Reviewed回填；旧完整身份 `f3837410a9c41617495d2691e69f2e7baa11e7e5c3d7521f618a0f1472ad6c09`（4,811字节，被审首稿v1／前轮登记版）保留，被 `5069a3690c6886204ebe9877ff0165e77c4c437fb8273032ac9d6f52bf89c2d0` 替代（5,472字节，当前有效；当前新字节不冒充本轮被审对象） |

| `specs/combat/wp52-a-generic-numerical-and-status-evaluation.md` | 无历史被审版 | 本批首稿v1 | 固定 `f7f400c642d77f29c5411ac156fe0e49716848b87ed232b02b8d418e1c67126a`（46,332字节），ReviewPending；批内固定尚未外审，运行保留；2026-09-28经两项有限修订与WP51状态/上游身份直接传播，继续ReviewPending；旧完整身份 `f7f400c642d77f29c5411ac156fe0e49716848b87ed232b02b8d418e1c67126a`（46,332字节，被审首稿v1／前轮登记版）保留，被 `6c0534fea6d4a18284c1e54a38e413ad010d38291088b0df45d8ac087ca44c9c` 替代（48,127字节，当前有效；当前新字节不冒充本轮被审对象）；2026-09-28经独立有限复审后的限定Reviewed回填/必要身份与表格维护；旧完整身份 `6c0534fea6d4a18284c1e54a38e413ad010d38291088b0df45d8ac087ca44c9c`（48,127字节，被审v2或WP50附表v1／前轮登记版）保留，被 `5cdc3edf5c14428166215d2b5b214eee95e751cd58902fe6047cd47eb4489c5e` 替代（48,733字节，前轮登记版）留史，再被 `9c74d50cd8d886707c9d6addd1b6f5be162beec6333daca924d7b4d7ddc3df70` 替代（49,622字节，前轮登记版）留史，再被 `7e6000fd3ab3f5829335ef4bcbd46247a13ed2a9d7a3cb61f579766332d6f46d` 替代（50,038字节，前轮登记版）留史，再被 `388b5fce672b8d88cb08e309827154c35e44f68cbe4fd07b62c2f66e3701f26b` 替代（50,104字节，当前管理字节不冒充被审对象） |

| `specs/combat/wp52-a-evaluation-coverage-and-data.md` | 无历史被审版 | 本批首稿v1 | 固定 `b620a868091aff4e1bb519f18e89698688eef279dbb020f828e2a0dfa25739c6`（58,177字节），ReviewPending；批内固定尚未外审，运行保留；2026-09-28经两项有限修订与WP51状态/上游身份直接传播，继续ReviewPending；旧完整身份 `b620a868091aff4e1bb519f18e89698688eef279dbb020f828e2a0dfa25739c6`（58,177字节，被审首稿v1／前轮登记版）保留，被 `a5a13acaf8572fa621b91911430b2286b23340618c72d4b5d2e1522aaf4ec5f9` 替代（58,772字节，当前有效；当前新字节不冒充本轮被审对象）；2026-09-28经独立有限复审后的限定Reviewed回填/必要身份与表格维护；旧完整身份 `a5a13acaf8572fa621b91911430b2286b23340618c72d4b5d2e1522aaf4ec5f9`（58,772字节，被审v2或WP50附表v1／前轮登记版）保留，被 `fa760facb18685586550f4a831c30616e4503942e2e170eaf605afa517ed868b` 替代（59,366字节，前轮登记版）留史，再被 `7bce736d31418d5e02e441956806c218cf9e8f97e9f24051c54398fc0239f80f` 替代（60,674字节，前轮登记版）留史，再被 `91ab040d63013316881f7fafb52657407fb5b17158a64c6522059b86ec58bed8` 替代（61,156字节，当前管理字节不冒充被审对象） |


| `review/wp50-wp51-wp52a-delivery-2026-09-27/self-checks.json` | 首稿v1原件在本轮input-snapshot | v2有限修订维护 | 2026-09-28经有限修订的矩阵/当前配套同步，首稿旧断言留明确历史；旧完整身份 `5faccf42e26c67da07e0d844cc03a0d4c9120246e6823f7bab438691361279fc`（364,926字节，被审首稿v1／前轮登记版）保留，被 `0960427cb4ce0f2044604a15b1754dc310f47162d1e16ad67999dd753ad4111d` 替代（416,764字节，当前有效；当前新字节不冒充本轮被审对象）；2026-09-28经旧批活动状态/身份与新批交付登记维护；旧完整身份 `0960427cb4ce0f2044604a15b1754dc310f47162d1e16ad67999dd753ad4111d`（416,764字节，被审v2或WP50附表v1／前轮登记版）保留，被 `6e83255802631e198518cd5178f75ec4204498ae2a0d2b92592e6b69b87f13bc` 替代（464,719字节，当前管理字节不冒充被审对象） |

| `review/wp50-wp51-wp52a-delivery-2026-09-27/boundary-checks.json` | 首稿v1原件在本轮input-snapshot | v2有限修订维护 | 2026-09-28经有限修订的矩阵/当前配套同步，首稿旧断言留明确历史；旧完整身份 `f5eb0aca474da0ba48adb816b8289b3b4a8e4e5966fe4dbcd18b8a3e69fc914d`（14,164字节，被审首稿v1／前轮登记版）保留，被 `82c7c95c75abd44d48213cc470b16ca62c21123eb332d09b36905aeae6b1be90` 替代（31,428字节，当前有效；当前新字节不冒充本轮被审对象）；2026-09-28经旧批活动状态/身份与新批交付登记维护；旧完整身份 `82c7c95c75abd44d48213cc470b16ca62c21123eb332d09b36905aeae6b1be90`（31,428字节，被审v2或WP50附表v1／前轮登记版）保留，被 `26acad41c8a5f49468d0aeeffd5e9584770c8f74947dd64066da5cffc323d256` 替代（49,349字节，当前管理字节不冒充被审对象） |

| `review/wp50-wp51-wp52a-delivery-2026-09-27/delivery-summary.md` | 首稿v1原件在本轮input-snapshot | v2有限修订维护 | 2026-09-28经有限修订的矩阵/当前配套同步，首稿旧断言留明确历史；旧完整身份 `0df9331d437df132728bc58cb36af53d16d09c4f787e99445db3de56c483029b`（6,554字节，被审首稿v1／前轮登记版）保留，被 `7f2207b4267758a9483bd7042554116192c669061663a07c5178c3ec63c66748` 替代（9,407字节，当前有效；当前新字节不冒充本轮被审对象）；2026-09-28经旧批活动状态/身份与新批交付登记维护；旧完整身份 `7f2207b4267758a9483bd7042554116192c669061663a07c5178c3ec63c66748`（9,407字节，被审v2或WP50附表v1／前轮登记版）保留，被 `20a61b73befceb5a88bb4db76c5c4dd0a453fc0f7b6639ac3d3f79987a5d7848` 替代（4,833字节，当前管理字节不冒充被审对象） |


| `specs/combat/wp52-b-field-damage-healing-and-target-evaluation.md` | 无历史被审版 | 2026-09-28首稿v1 | 固定 `b41c2773e3b00f8654767e597dfad20b34587fcb7d8d73bab11dbf784e13569d`（42,914字节），ReviewPending；批内固定尚未外审；2026-09-28经WP52-B-R01有限修订v2、R01待有限复审；旧完整身份 `b41c2773e3b00f8654767e597dfad20b34587fcb7d8d73bab11dbf784e13569d`（42,914字节，被审首稿v1／前轮登记版）保留，被 `8036a674606d1455cd77f35b335e90a34b694afde08e8add950ac89931a12d00` 替代（44,557字节，被审v2／前轮登记版）留史，再被 `08939beed65fdde42d1aee86af482dc0346d10046ac6c4447b149cdf49fb804a` 替代（45,326字节，前轮登记版）留史，再被 `73fa6ffa2096cea14354faca92e63439c9db7698541536212901050f65baf759` 替代（45,342字节，当前有效；新字节不冒充被审对象） |

| `specs/combat/wp52-b-effect-coverage.md` | 无历史被审版 | 2026-09-28首稿v1 | 固定 `d2ccf48fbd64cc786bcd7bf060631a007523ea48afff6d38a00391c7ac8b47fe`（57,193字节），ReviewPending；批内固定尚未外审；2026-09-28有限复审PASS_SCOPED后限定Reviewed回填；旧完整身份 `d2ccf48fbd64cc786bcd7bf060631a007523ea48afff6d38a00391c7ac8b47fe`（57,193字节，被审v1／前轮登记版）保留，被 `723838f295a6041a8f14b55a8f3abcab909f3431f8fef6050a22306975a6d3b5` 替代（57,979字节，当前管理字节不冒充被审对象） |

| `specs/combat/wp52-c-items-calling-and-control-evaluation.md` | 无历史被审版 | 2026-09-28首稿v1 | 固定 `542e7b01546ce812dd94bc8505f636224573fa4d89e7d450126d23deeb85c84c`（39,343字节），ReviewPending；批内固定尚未外审；2026-09-28独立首审PASS_SCOPED后限定Reviewed管理回填；旧完整身份 `542e7b01546ce812dd94bc8505f636224573fa4d89e7d450126d23deeb85c84c`（39,343字节，被审首稿v1／前轮登记版）保留，被 `290bee81e83140473c30aa9fd74d8debad25d80e1de4aae440b0b20f5371934f` 替代（40,332字节，前轮登记版）留史，再被 `6a42aa649f446402dba953c0414053327fa8f784b62ac5caeb7174c08c3c973d` 替代（40,706字节，前轮登记版）留史，再被 `39c2c15994fe1369325b1b7b1624010583574ddbf7d2f4e6d813af26fbae7024` 替代（40,722字节，前轮登记版）留史，再被 `658b40bca3e9567203dea4fc1d9c417adddbca4f1c9f7e1535e6b30ed0e32c2b` 替代（40,722字节，当前管理字节不冒充被审对象） |

| `specs/combat/wp52-c-item-control-coverage-and-data.md` | 无历史被审版 | 2026-09-28首稿v1 | 固定 `9e8d3030b462c2bef28cf0793aea5b6802e87c6db1d7c80b04fb63f0fc766261`（37,701字节），ReviewPending；批内固定尚未外审；2026-09-28独立首审PASS_SCOPED后限定Reviewed管理回填；旧完整身份 `9e8d3030b462c2bef28cf0793aea5b6802e87c6db1d7c80b04fb63f0fc766261`（37,701字节，被审首稿v1／前轮登记版）保留，被 `f83205eebd3889354a4fb8afe9847c9e489d0eec9d84b876e06b6da3c0f09088` 替代（38,390字节，当前管理字节不冒充被审对象） |

| `specs/combat/wp54-entry-eligibility-level-adjustment-and-clauses.md` | 无历史被审版 | 2026-09-28首稿v1 | 固定 `3ef7ae5a64face7f5fabc70ee295ee6615be54ebbd8351e103104166c0a8a968`（32,322字节），ReviewPending；批内固定尚未外审；2026-09-28独立首审PASS_SCOPED后限定Reviewed管理回填与N01语境同步；旧完整身份 `3ef7ae5a64face7f5fabc70ee295ee6615be54ebbd8351e103104166c0a8a968`（32,322字节，被审首稿v1／前轮登记版）保留，被 `2a1518c3351ed9fa3dfaf839010dcc0f4c56df862353c39a227151aa83d06dfb` 替代（33,809字节，当前管理字节不冒充被审对象） |

| `specs/combat/wp54-entry-rules-and-cup-data.md` | 无历史被审版 | 2026-09-28首稿v1 | 固定 `b45c976e01251aedc4b445a93efee7bb645c35cdd374bef6e741ab40375a4815`（11,746字节），ReviewPending；批内固定尚未外审；2026-09-28独立首审PASS_SCOPED后限定Reviewed管理回填；旧完整身份 `b45c976e01251aedc4b445a93efee7bb645c35cdd374bef6e741ab40375a4815`（11,746字节，被审首稿v1／前轮登记版）保留，被 `0ec502366b743770f95d7971cf3f087a153694bc6ff4395b8852642fd422a18d` 替代（12,381字节，当前管理字节不冒充被审对象） |

| `specs/combat/wp55-facility-session-and-restoration.md` | 无历史被审版 | 2026-09-28首稿v1 | 固定 `d5ee5ba7b3f48fc14c7552248d865d560b64a626624e96e6cbf64d1f9916b1dc`（21,873字节），ReviewPending；批内固定尚未外审；25场景、会话/对手/恢复接点；2026-09-29经首审REQUEST_CHANGES修订v2（R01～R05＋属主概括同步；34场景；仍ReviewPending）：旧完整身份 `d5ee5ba7b3f48fc14c7552248d865d560b64a626624e96e6cbf64d1f9916b1dc`（21,873字节，被审v1）保留，被 `0bcff15b2e5683a3b9b96c621ba650b55220131dddf34957d75c39caf83557c7`（27,698字节，当前修订稿；新字节不冒充被审对象）替代 |

| `specs/combat/wp56-palace-and-arena-variants.md` | 无历史被审版 | 2026-09-28首稿v1 | 固定 `fde119eaca1bd3543571b76343972a26903da905b02e30ebe55ed3c7cf50145b`（16,917字节），ReviewPending；批内固定尚未外审；22场景、性格概率表/三回合评判；2026-09-29经首审REQUEST_CHANGES修订v2（R01～R05；27场景；WP55引用重固定为批内修订稿）：旧完整身份 `fde119eaca1bd3543571b76343972a26903da905b02e30ebe55ed3c7cf50145b`（16,917字节，被审v1）保留，被 `8ed7940bdd732e8d960a7c5292e1baeacc27489c34dc67f15ffe0501fb4966b0`（21,274字节，当前修订稿；新字节不冒充被审对象）替代 |

| `specs/creature-rpg/wp57-factory-rentals-and-swaps.md` | 无历史被审版 | 2026-09-28首稿v1 | 固定 `e510f8402a2d253ac78cf97bb6eeb5d2bd04b196f9ec5da5437567d0c33f0858`（11,933字节），ReviewPending；批内固定尚未外审；15场景、候选/租借/交换与恢复接点；2026-09-29经首审REQUEST_CHANGES修订v2（R01～R03；17场景；WP55引用重固定为批内修订稿）：旧完整身份 `e510f8402a2d253ac78cf97bb6eeb5d2bd04b196f9ec5da5437567d0c33f0858`（11,933字节，被审v1）保留，被 `7e69ccdccb422d1b04799990041a3745d747ebab3a765b8f7d686ad4f270ef8b`（14,776字节，当前修订稿；新字节不冒充被审对象）替代 |

| `review/wp52b-wp52c-wp54-delivery-2026-09-28/delivery-summary.md` | 首稿v1原件在本轮input-snapshot | v2修订维护 | `23724461c38c7270cd12cbef4e5aada25f8463f466cd437bfa0c76aa267dc1c4`（5,982字节，v1登记版）留史，被 `c173bc0062de20ad14be16efd17cb7ddae7aa944532e85161b35453f1b45d4c9` 替代（7,973字节，v2登记版）留史，再被 `7a668589111858f0749c2f95f853c86f2b2b3f1d4ad858f1d5df4f66365e3103` 替代（9,057字节，v3首登记版）留史，再被 `85431e92ed74cc2478d7de3cf1f0923b05fc81ef29c9e69f708fd13810d89640` 替代（9,057字节，前轮登记版）留史，再被 `f48729efbb9be72a28d048a424ba319f437309d6d199bdfdba346e13d0003898` 替代（9,057字节，前轮登记版）留史，再被 `6ec4fe6fd143489bdc8384449864fe9bc78348bc55d84ec3badfe38c2943ab80` 替代（9,057字节，前轮登记版）留史；2026-09-29经继承C02剩余引用同步升v4：由 `4ba4ed58f9672c9dce98638afde52b3d32a2e71cf5b9f4630e84f0055cb5f1af` 替代（9,587字节，当前；新字节不冒充） |

| `review/wp52b-wp52c-wp54-delivery-2026-09-28/self-checks.json` | 首稿v1原件在本轮input-snapshot | v2修订维护 | `3ab93186bc086874fd5de406876ef815364f86d4e150704953d2c5f809484c26`（1,063,788字节，v1登记版）留史，被 `7f77e8c250ea6999daa149bf006c79d75ca7e794cc5f8756e9e9599f9e027602` 替代（1,068,195字节，v2登记版）留史，再被 `53882278565b80dbc439eeffdcbe6205e97dc8da6ff3302c36372c3739f0e0db` 替代（1,069,184字节，v3首登记版）留史，再被 `713d0db147ff96d8f064cbc627db84a2fbe05a5460d21c77dc6a0124e277b135` 替代（1,069,184字节，前轮登记版）留史，再被 `ebf7aaa0fbfe3b41c21861b98ac0f11c15c43879ef91be4ec0a7cf21c2f365b9` 替代（1,069,184字节，前轮登记版）留史，再被 `3a05f9e0cfcc9fc54820a1c0ab6c93c745d1d23787bba91a03facef43062fb11` 替代（1,069,184字节，前轮登记版）留史；2026-09-29经继承C02剩余闭合升v4：由 `b776328d56003326f0b4d5eb02023a549d8472330e335a4846012aa52b0f2ecc` 替代（1,070,038字节，当前；新字节不冒充） |

| `review/wp52b-wp52c-wp54-delivery-2026-09-28/boundary-checks.json` | 首稿v1原件在本轮input-snapshot | v2修订维护 | `c48ef0c0a365dd13897c15d5ca40eacf15720c687655273e8b94fe59423e5794`（16,020字节，v1登记版）留史，被 `2193fbf8748049d4bf49c7ab1b3e2ff6f68e99675725bc1c7cd451ebd289ce6f` 替代（19,470字节，v2登记版）留史，再被 `a52a051f183ed45e5e23383726ac4f3b0f31d51e2ac673d8151bff4e70509764` 替代（20,318字节，v3首登记版）留史，再被 `32e6255ef1234b753672e63de10a5648886680374ea4db205773a7bb0114adfe` 替代（20,318字节，前轮登记版）留史，再| `review/wp55-wp57-delivery-2026-09-28/delivery-summary.md` | 首稿v1原件在本轮input-snapshot | v2修订维护 | `6217eeb05793b2b0a6620a1bb06b30ad5d51cc24e59d74c6f43c0e1b18568bad`（4,970字节，v1登记版）留史，被 `0fcab05d9f13dd9109bf70c699b7c6159dcca43e766524e5529855bc54909ac8`（6,514字节，当前v2；新字节不冒充）替代 |

| `review/wp55-wp57-delivery-2026-09-28/self-checks.json` | 首稿v1原件在本轮input-snapshot | v2修订维护 | `72396ffb1676cce44cb43dab3ec9f0ec8a8c36cd939febde402e08ca834d3d30`（17,131字节，v1登记版）留史，被 `36704503193cadbd3120ceabf3e2b38cd26274f90ad29f9dd18e7367aa026cb3`（20,320字节，当前v2；新字节不冒充）替代 |

| `review/wp55-wp57-delivery-2026-09-28/boundary-checks.json` | 首稿v1原件在本轮input-snapshot | v2修订维护 | `5839c099ef7fe3ee675f9b880a853c6fb043e52acb8b4baaa07c0186b07ebcd8`（7,571字节，v1登记版）留史，被 `8c2033a751f405376cf2375c033c5d6d691e61ff9f296995c71594c9cc49c64c`（8,670字节，当前v2；新字节不冒充）替代 |

| `review/wp55-wp57-delivery-2026-09-28/backfill-response.md` | 首稿v1原件在本轮input-snapshot | v2修订维护 | `2aa102f2c42004b00f64d54974c50fc639e276e5c23d43cf8eeffca1f13309ca`（6,006字节，v1登记版）留史，被 `835459a74ae189af5c9f64235fa7286012d3ab9ef4dc999ec434f7ceada43b29`（6,661字节，当前维护版；新字节不冒充）替代 |

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

**第二十六轮（WP17 状态回填与 WP18–WP20 批次，本轮，2026-09-26）**：

- **闭合复审结论**：WP17 PASS_SCOPED（R01 最后两处与 C02 关闭、R02～R05/C01 继承关闭、未发现回归）；复审实测 manifest `d3bef580`（53,195 字节）98 条记录全部匹配，被审 v3 `6010f40b`、附表 v2 `e01466ef` 与本地实测一致；闭合报告 `8a36381b`、下一批提示 `da7a0ed3` 归档于 `review/wp17-closure-review-2026-09-23/`。
- **WP17 回填**：主文档头部/§13 登记 **Reviewed**（限定静态范围：消息进入/替换/已述控制与绘制标记；逐字显示与确认状态；选项/数量及取消编码；按键与文字入口的已述编辑边界；解释器等待/地图更新机会/正常与异常出口的已述交界；管理性变更；被审哈希 `6010f40b` 保留历史，回填后 `bb61f967`、30,047 字节不伪称为复审对象）；附表未改、字节不变（`e01466ef` 继续有效）。feature-matrix F05-05/F05-06 → Reviewed（WP17 子范围）＋Inventoried（前向范围），矩阵 `5aecfd39` → `fb109386`。至此 WP01–WP17 全部限定 Reviewed。
- **WP18 首版（v1 `7ab818e2`，`specs/creature-rpg/wp18-creature-identity-species-ownership.md`，34,100 字节；自检期内经"形态继承精确化"与"批末交叉引用同步"两次重固定，中间版本 `f3c33277`/`f36f7b8a` 不再有效）**：物种内容/个体信息分层（物种查找身份与形态回退、字段责任目录、个体字段目录）；物种与形态变更影响（`species=` 形态优先级/缓存清理，三形态入口副作用差异表）；个体生成（创建参数、初始化清单、随机派生指针、六类生成上下文）；复制（深/浅复制清单与身份保持）；来源与拥有者（Owner 结构、六个变更入口、来源方式域 `{0,1,2,4}` 与孵化时间戳边界、外来判定只用 id+名字、命名清除规则）；静态场景 14 项；前向引用 17 项。自检完成；批内固定、尚未外审。
- **WP19 首版（v1 `3cba4bcd`，`specs/pokemon-rules/wp19-attributes-ability-and-stats.md`，30,963 字节；批末同步 WP18 引用后重固定，中间版本 `695fcdef` 不再有效）**：数值四分层（固定/覆盖/派生/随机）；类型/性别/异色（含超级异色）/特性选择/Nature 的派生与缓存规则；等级↔经验接口；IV/EV 域与上限模式；能力公式（取整顺序、HP 特例、禁用变体）；重算触发目录与当前 HP 写回规则（含濒死复活推论）；五组共 36 行数值向量（自有算术核对：HP/能力/写回/派生/PP）；前向引用 10 项。自检完成；批内固定、尚未外审（头部与依赖表引用 WP18 `7ab818e2`）。
- **WP20 首版（v1 `84c29af6`，`specs/creature-rpg/wp20-hp-status-moves-helditem.md`，29,018 字节）**：HP 赋值/濒死/治疗五入口逐项核对（保留字段与拒绝行为）；异常值域与关联计数（睡眠/中毒语义、收尾归零）；招式槽/静默学习/初始化/删除与顺序规则；最初招式记录与调用点；重学/兼容判定接口；招式对象与 PP 派生（含提升计数极端值边界）；PP 恢复与写穿边界；持有物字段规则（邮件耦合、快照还原、捕获入队/送箱分流）；静态场景 25 项；前向引用 12 项。自检完成；批内固定、尚未外审（头部与依赖表引用 WP18 `7ab818e2`、WP19 `3cba4bcd`）。
- **批内交界核对**：术语（个体/形态/派生/缓存）、所有权与复制、重算与 HP 写回、招式/PP 与持有状态四处交界检查通过；发现并修复三处章节交叉引用不一致（WP18→WP20 §5.1、WP18→WP19 §4.6、WP19→WP20 §5.4），并级联同步批内哈希引用。
- **矩阵增量**：F06-01、F06-02、F07-01 → ReviewPending（WP18 各自范围）＋Inventoried（动态形态/完整接收流程/服从等前向范围）；F06-03、F06-04 → ReviewPending（WP19 范围）＋Inventoried（派生消费/Hyper 入口与成长流程）；F06-05、F06-06、F08-05 → ReviewPending（WP20 各自范围）＋Inventoried（战斗内机制/学习交互/触发生效范围）。矩阵 `fb109386` → `c7c09d7b`（38,071 字节）。
- **批末交付**：`review/wp18-wp20-delivery-2026-09-26/`——`delivery-summary.md`（`52da6bbf`）、`current-hashes.tsv`（`57025ecc`）、`wp17-backfill.diff`（`7d04f964`）、`feature-matrix-diff-from-review.diff`（`bcd3d0e4`）；全部登记于第 1 节。三包状态 **ReviewPending（各自具名范围）**，批末统一送审；未自行升级 Reviewed。
- **停止点**：本批至此停止，不启动 WP21 或其他包；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未提交/推送（工作区非 git 仓库）；manifest 自身不自哈希，最终实测值由交付消息报告。

**第二十七轮（WP18–WP20 首轮复审修订，本轮，2026-09-26）**：

- **复审处理**：首轮独立复审（报告 `2f8b22e3`）结论 WP18/WP19/WP20 均 REQUEST_CHANGES（9 项必修、2 项非阻塞维护；WP17 回填接受；WP01–WP17 限定 Reviewed 不变）。修订前实测三包 v1、矩阵、manifest 与 report.md 第 1 节固定版本全部一致，意见适用；**11 项全部核实认可、无保留分歧项**。逐项回应 `aea5c122`，差异 5 份 `a5f7283d`/`fe6c4de9`/`e8ba1b68`/`09014951`/`26aa5906`（均相对本轮 `input-snapshot/`）。
- **WP18 v2（`3d30f3f1`，35,885 字节）**：R01 创建返回状态与中途赋空分开（Nature 返回前已被重算求值缓存、等级缓存说明、形态复检的 `withMoves` 条件；新增 2 场景）；R02 外来赠送包装默认性别 0、来源方式原样保留（新增 3 场景）；WP19-R04 传播（类型"1–2"表述改为内容约定）。
- **WP19 v2（`252649f7`，35,222 字节）**：R01 普通/超级异色分别求值、分别缓存（设置/失效表述与 3 个对照场景）；R02 非法等级（返回错误对象）与非法经验（诊断文本求值阶段失败）分列；R03 维生素默认配置（世代 8 不受 100 限制）、删去无据双倍表述、Shadow 暂存额度含已暂存值（3 个对照）；R04 类型列表无两项硬上限（1 个对照）；C01（写回行旧上限前提、WP20 交叉引用修正）；C02（薄荷入口已定位、流程待 WP28；其余未决不随之关闭）。
- **WP20 v2（`d595b1b2`，33,864 字节）**：R01"快照还原"改为可更新的还原记录（初始化/更新/结束读届时记录；永久消耗不返还、暂时打落还原、永久取得更新记录三对照；个体/战斗入口未知道具差异）；R02 PP 三层区分（直接字段/同步入口/替换复制招式）与首次失败时序（设置调用内失败、计数已改、PP 保留）；R03 HP0 清理的蛋前提与复活分量（REVIVE 半血、完全复活回满；新增蛋保留场景）。
- **传播检查**：批内互引全部同步（WP19→WP18 `3d30f3f1`；WP20→WP18 `3d30f3f1`＋WP19 `252649f7`）；三包旧表述检索清空；矩阵八行状态措辞与 F06-05/F08-05 还原记录措辞同步（`c7c09d7b` → `3129eacc`，38,176 字节）；交付摘要 v2 同步（`52da6bbf` → `ddf85f73`）、TSV v2 重测（`57025ecc` → `cdb89a96`）。
- **保留**：WP19 核心公式与已核对向量不变；既定边界（WP21 处理器、WP28 道具流程、WP38/WP42/WP50 效果族、WP23/WP44 等）不提前展开。
- 三包保持 **ReviewPending（各自具名范围）**，修订后统一送复审；未自批 Reviewed；WP21 未启动；未修改 `reference/`；未提交/推送。

**第二十八轮（WP18–WP20 定点复审修订与 WP20 回填，本轮，2026-09-26）**：

- **复审处理**：定点复审报告 `18356917`（11,643 字节）——**WP20 PASS_SCOPED**；WP18/WP19 仅剩 WP18-R01 两处缓存边界（其余 8 项必修与 C01/C02 CLOSED；115 条 manifest 记录匹配）。修订前实测五项被审对象与 report.md 第 1 节固定版本全部一致。两处剩余项**均核实认可并修订**；逐项回应 `07a481ab`，差异 5 份 `709c73f9`/`d299a14b`/`5aa23ca0`/`113a1fbe`/`8c15d66d`（相对本轮 `input-snapshot/`）。
- **WP18 v3（`4428049b`，36,889 字节）**：§4.1"返回时仍未缓存"收窄为"初始化赋空 + 最终状态取决于后续读取"；形态三入口表补登记读取性别/普通异色的缓存填充；创建复检条目补登记副作用；新增"复检+登记（返回前缓存）/关闭复检（保持未缓存）"两对照。
- **WP19 v3（`6c669fcf`，35,935 字节）**：§3.5 `hasNature?` 改为"只看当前缓存（不记录是否曾求值）"；§6 同步；新增"覆盖存在时清空表现 Nature→假→读取后真、重算不填回"序列。
- **WP20 回填**：**Reviewed（限定静态范围**：HP/非蛋濒死与治疗入口、蛋例外、状态设置与计数交界；招式槽/初始化/静默学习/记录与重学接口；PP 数学、赋值与失败阶段、同步入口；个体/战斗持有物入口、邮件失配读取、可更新还原记录及已述捕获边界）。管理性变更（含报告 §4 允许的 C03 三处简写同步与批内引用同步至 v3）；被审哈希 `d595b1b2` 保留于第 3 节历史，回填后 `f8272acf`、35,018 字节不伪称为复审对象。
- **矩阵同步**：F06-05/F06-06/F08-05 → Reviewed（WP20 子范围）＋前向 Inventoried；F06-01/02/07-01、F06-03/04 更新为"v2 已送定点复审，仅剩 WP18-R01（及传播）修订后再送"；矩阵 `3129eacc` → `5fc73d82`（38,333 字节）。
- **传播检查**：批内互引同步至 v3（WP19→WP18 `4428049b`；WP20→WP18 `4428049b`＋WP19 `6c669fcf`）；三包旧表述（"返回时仍未缓存/从未求值/濒死含蛋/恒在区间"）检索清空；交付摘要 v3 同步（`ddf85f73` → `f014b114`）、TSV v3 重测（`cdb89a96` → `ef231e80`）。
- **停止点**：送 WP18-R01 两处及直接回归短复审后停止；WP18/WP19 保持 ReviewPending；未启动 WP21 或其他提取包；未修改 `reference/`；未运行游戏/参考脚本/网络；未提交/推送。

**第二十九轮（WP18/WP19 回填与 WP21–WP25 批次，本轮，2026-09-26）**：

- **闭合复审结论**：WP18/WP19 PASS_SCOPED（WP18-R01 最后两处关闭、其余继承关闭、未发现回归）；WP20 回填接受、C03 CLOSED；复审实测 123 条 manifest 记录与 27 条交付哈希全部匹配，五项固定对象与本地实测一致；闭合报告 `93f1de1c`、执行提示 `cd213c33` 归档于 `review/wp18-wp20-closure-review-2026-09-26/`。
- **WP18/WP19 回填**：按报告 §4 登记 **Reviewed（限定范围）**（管理性变更；被审哈希 `4428049b`/`6c669fcf` 保留于第 3 节历史，回填后 `85368fe3`/`489984f7` 不伪称为复审对象）；WP20 上游引用同步为 `f2f904e5`（管理性）。矩阵 F06-01/F06-02/F07-01、F06-03/F06-04 → Reviewed（对应子范围）＋前向 Inventoried，矩阵 `5fc73d82` → `528f38aa`（38,158 字节）。**至此 WP01–WP20 全部限定 Reviewed。**
- **WP21 首版（`5a5ef9ca`，`specs/pokemon-rules/wp21-dynamic-forms-and-display.md`，30,245 字节）**：形态注册机制（双键查找/条件注册零用例/复制共享）与 49 条注册/9 条复制的触发族目录（读取 15、创建 11、提交 6、战斗离场 19、入场 2、开始 3、蛋创建 1、位图 1、Primal 2）；提交副作用链（缓存/重算/招式/图鉴登记顺序）；锁定与限时形态；标记/缎带/华丽大赛属性（U04 保留）；静态场景 19 项；前向引用 10 项。自检完成；批内固定、尚未外审。
- **WP24 首版（`45370acd`，`specs/creature-rpg/wp24-player-trainers-partners.md`，24,659 字节）**：训练家/玩家身份与标识；玩家内容与初始命名；四类资源域与写入者目录；徽章与七项功能标记（读取侧定位、写入侧 U 类）；训练家装载/版本/缺失反馈/调试新增路径；伙伴注册/资格/战后清理；静态场景 14 项；前向引用 8 项。自检完成；批内固定、尚未外审。
- **WP25 首版（`920b0943`，`specs/creature-rpg/wp25-party-and-storage.md`，21,310 字节）**：队伍/盒子容量与伪位置；容器操作与界面流转（屏幕/场景分层）；限制分层（领域 vs 界面）；存入治疗（默认关）与持久交界；静态场景 19 项；前向引用 6 项。自检完成；批内固定、尚未外审（引用 WP24 `45370acd`）。
- **批末交界核对**：四项核对通过（形态提交↔WP18/19/20 缓存/重算/状态、WP24↔WP18 拥有者、WP25↔WP18/20/24 集合与状态保留、追踪一致性）；未发现规则冲突；"生物—队伍—储存"检查点本包部分完成（WP26/WP38 后续复核，不替代 WP78）。
- **矩阵增量**：F06-07、F07-02/F07-03、F07-04/F07-05 → ReviewPending＋前向 Inventoried；矩阵 `528f38aa` → `5379d879`（39,456 字节）。
- **批末交付**：`review/wp21-wp25-delivery-2026-09-26/`——`delivery-summary.md`（`d29d177a`）、回填差异 3 份（`278faeda`/`5b760f9c`/`98cb92a4`）；旧交付摘要 v4（`5118e628`）与 v4 TSV（`a5a2ded7`）。三包保持 ReviewPending，批末统一送审。
- **停止点**：本批至此停止，不启动 WP22/WP23/WP26 或其他包；未修改 `reference/`；未运行游戏/参考脚本/网络；未提交/推送。

**第三十轮（WP21–WP25 首轮复审修订，本轮，2026-09-26）**：

- **复审处理**：首轮独立复审（报告 `a6354444`）结论 WP21/WP24/WP25 均 REQUEST_CHANGES（12 项必修＋BATCH-C01 一组；WP18/WP19 回填与 WP20 引用同步接受；132 条 manifest 记录与交付哈希匹配）。修订前实测三包 v1、矩阵、manifest 与 report.md 第 1 节完全一致；**12 项全部核实认可**。逐项回应 `34a3fb5e`，差异 6 份 `7b8eb22a`/`cf748fc8`/`3b15e838`/`68debf8b`/`991e2b8f`/`0f822f78`（相对本轮 `input-snapshot/`）。
- **WP21 v2（`55a47313`，40,922 字节）**：R01 注册机制改用真实底层（单键整映射替换/复制时绑定/无字符串归一/真值判断）；R02 读取/创建族复制目标校正（各 5）、HOOPA 归读取族、新增取值数据六表（ARCEUS/SILVALLY 17 项无 9、GENESECT 四驱动、TOXEL 12 性格、MILCERY 糖果顺序、区域蛋 17 目标）；R03 招式三类路径与 KYUREM 跳项例/ROTOM 抛错边界；R04 标记编辑双界面差异；R05 缎带升级不去重与移除失败路径；R06 Beauty 消费者与复制接收路径。
- **WP24 v2（`8b06ddc4`，28,865 字节）**：R01 玩家编号三层语义（记录 1 回退）；R02 伙伴注册分阶段/身份 ID 当版本/参与谓词顺序/战后双分支；R03 金钱守卫与两阶段统计（封顶不提示不统计）。
- **WP25 v2（`98b52717`，26,359 字节）**：R01 容量=当前长度与 clear/直写语义；R02 地区代理（pbMove 只复制、删除/墙纸失败、无消费者）分列；R03 界面守卫按目标/持有条件化；同步 WP24 引用。
- **BATCH-C01**：WP19 三处旧引用文字同步（管理性 `489984f7` → `03167162`，36,381 字节）；WP25 同批措辞；DARMANITAN 简写（偶数形态映射）；笔误与责任包号（BP→WP29、导航器→WP63）。
- **传播检查**：矩阵五行状态措辞（`5379d879` → `bb037cea`，39,516 字节）；交付摘要 v2 `c88e1e5b`、TSV v5 `7db3b12b`；三包旧表述检索清空。
- **停止点**：送原编号与直接回归复审后停止；三包保持 ReviewPending（未自批）；未启动 WP22/WP23/WP26；未修改 `reference/`；未运行游戏/参考脚本/网络；未提交/推送。

**第三十一轮（WP21–WP25 定点复审修订与 WP24/WP25 回填，本轮，2026-09-26）**：

- **复审结论**：定点复审报告 `f2dc78d2`（11,521 字节）结论 **WP24/WP25 PASS_SCOPED、WP21 仅剩 WP21-R03**（原 12 项中 11 项与 BATCH-C01 CLOSED；BATCH-C02 非阻塞、随本轮同步）；复审实测五项固定对象与报告 §1 一致、141 条 manifest 记录匹配、收尾输入未变。
- **WP21 v3（`4e475505`，42,037 字节）**：R03——直接换招标识改为"保留槽位与 PP 提升计数、当前 PP 按新招式总 PP 钳制"（§4.2 路径①与战斗专属招改写、§6 不变量 5、§10.2 两对照场景共四处）；BATCH-C02 球字段改为"重置为普通球（POKEBALL）"；§9 两行触发条件同步；保持 **ReviewPending**（送短复审）。
- **WP24 回填（`32594094`，29,668 字节）**：按 §5 登记 **Reviewed（限定范围）**；BATCH-C02 三项（查询键未命中语义、回退记录 1 后仍缺失、刷新三态）同步；被审 `8b06ddc4` 保留于第 3 节历史，回填后新哈希不伪称为复审对象。
- **WP25 回填（`46bd905d`，27,081 字节）**：登记 **Reviewed（限定范围）**；BATCH-C02 两项（不可存放对照分写、墙纸工具分列）同步；WP25→WP24 引用同步；被审 `98b52717` 保留历史。
- **矩阵与交付**：矩阵 `bb037cea` → `e0762970`（39,590 字节；F07-02～F07-05 → Reviewed＋前向 Inventoried，F06-07 措辞更新）；交付摘要 v3 `62d8a2c8`（12,088 字节）、TSV v6 `4c66bcb4`（7,346 字节）；逐项回应 `7b5d3775`（6,023 字节）、差异 5 份（`d812eabe`/`91b61274`/`96c2046a`/`a82406ba`/`30f62f8b`）。
- **停止点**：送 WP21-R03 及直接传播短复审后停止；WP21 保持 ReviewPending（未自批）；未启动 WP22/WP23/WP26；未修改 `reference/`；未运行游戏/参考脚本/网络；未提交/推送。

**第三十二轮（WP21–WP25 闭合复审与 WP21 回填，本轮，2026-09-26）**：

- **复审结论**：闭合复审报告 `12e283ae`（8,339 字节）结论 **WP21 PASS_SCOPED**（WP21-R03 最后剩余与 BATCH-C02 CLOSED、未发现直接回归）、**WP24/WP25 继承 PASS_SCOPED 且回填接受**；复审实测 149 条 manifest 记录与 53 条交付哈希全部匹配、固定 158 项输入；WP01–WP20 既有批准范围保持；WP22/WP23 未完成（不得概括为全部通过）。
- **WP21 回填（`19a36297`，42,449 字节）**：按报告 §4 登记 **Reviewed（限定范围）**；头部/§13 更新；矩阵 F06-07 → Reviewed（WP21 子范围）＋前向 Inventoried；被审 v3 `4e475505` 保留于第 3 节历史，回填后新哈希不伪称为复审对象。
- **状态引用同步（管理性）**：WP18 `85368fe3` → `0464ca07`（37,313 字节）、WP19 `03167162` → `c7fb40fa`（36,406 字节）、WP25 `46bd905d` → `edc275c5`（27,058 字节）。
- **矩阵与交付**：矩阵 `e0762970` → `8b83d668`（39,577 字节）；交付摘要 v4 `8d8b7e5d`（13,976 字节）、TSV v7 `679338ea`（8,688 字节）；回填回应 `90961bb0`（3,590 字节）、差异 6 份（`a4926019`/`4f754254`/`7958529b`/`1369e8b9`/`118a8d31`/`b5aa766b`）；闭合报告与执行提示登记于第 1 节。
- **下一批**：按提示执行 **WP26→WP27→WP30**（逐包自检、批末统一送审），由本侧另行记录交付。
- **停止点**：本轮回填后不启动其他包；未修改 `reference/`；未运行游戏/参考脚本/网络；未提交/推送。

**第三十三轮（WP26–WP30 批次，本轮，2026-09-26）**：

- **批次授权与顺序**：按闭合复审提示执行 **WP26→WP27→WP30**（串行自检、批内固定、批末统一送审）；不启动其他包。
- **WP26（`793473a0`，27,898 字节）**：六入口对照（普通/静默、仅入队/可送箱、外来赠送、蛋入口）＋脚本交换；守卫与写入顺序、命名/存储管道、交换替换与无回滚、交易进化交界；自检修正两处（静默缺省等级失败路径、交换图鉴写入无 see_form 参数）。
- **WP27（`fe14af5d`，21,719 字节）**：口袋/槽位/容量与"预检纯、执行可部分"语义；PC 储存 999×999 与懒创建播种；存取/丢弃数量流与重要物品边界；快捷登记与过滤；存档迁移交界；自检修正两条场景。
- **WP30（`5972e119`，28,244 字节）**：六曲线（L50/L100 锚点）与反向换算边界；战斗经验/EV 完整修正次序与升级循环；等级/经验辅助流；两版学习入口与满槽替换/放弃/重学；友好度方法表与软上限、亲密派生。
- **矩阵与交付**：矩阵 `8b83d668` → `af8328ee`（40,955 字节；六个 Feature → ReviewPending（各自范围）＋前向 Inventoried）；交付摘要 v1 `9c713161`（7,448 字节）、矩阵合并差异 `c8b70094`（12,628 字节）、TSV v8 `08ced51b`（9,346 字节）。
- **批末交界核对**：WP26×WP18/WP20/WP21/WP25、WP27 容器不变量与实际调用者、WP30 重算/HP/招式状态×WP19/WP20 三项通过；矩阵/未决/前向引用一致（见交付摘要 §4）。
- **停止点**：三包保持 **ReviewPending（各自具名范围）**，批内固定统一送外审；未自批 Reviewed；未启动 WP22/WP23/WP28/WP29/WP31 或其他包；未修改 `reference/`；未运行游戏/参考脚本/网络；未提交/推送。

**第三十四轮（WP26–WP30 首审修订（v2），本轮，2026-09-26）**：

- **复审结论**：首审报告 `78a9ba42`（25,241 字节）结论 **REQUEST_CHANGES**（WP26 4 项、WP27 3 项、WP30 6 项必修＋2 项非阻塞维护；WP21 管理性回填接受、既有限定通过保留）。修订前实测六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。
- **修订（13 项＋2 维护全部核实认可）**：WP26（R01 入口/返回值/选择结果分列；R02 昵称保留与外来参数语义；R03 入盒治疗继承＋对等方对象按常规战斗接入；R04 容量复检条件可达与条件反例）；WP27（R01 接收/拾取/奖品直接添加分列；R02 登记三层守卫；R03 过滤游标恢复；BATCH-C02 前提注记与 POTION 文本样本）；WP30（R01 非法经验失败阶段与原始 setter 分列；R02 表外公式与 L101 边界向量 618,474/20,505；R03 席位归属/外来 1.5-1.7 二选一/背包护符/回退条件；R04 Shadow 暂存实际写入输出；R05 wing 调用链与友友球；R06 重学三层取消；BATCH-C01 头部名称与时态）。
- **修订后 v2**：WP26 `67056812`（33,910 字节）、WP27 `0a6a28f7`（25,961 字节）、WP30 `114038f3`（34,957 字节）；矩阵 `af8328ee` → `c4505715`（41,308 字节；六行版本说明）；交付摘要 v2 `dd06a4bd`（9,731 字节）。逐项回应 `2765129f`（9,462 字节）、差异 5 份（`a7855f91`/`0a329ee2`/`4e89689c`/`edf6b1fb`/`097b56e4`）；TSV v9 `ec86e13d`（10,524 字节）；首审报告与提示登记于第 1 节。
- **保留**：被审 v1 哈希全部保留于第 3 节历史；三包保持 **ReviewPending**；未自批 Reviewed。
- **停止点**：送 WP26-R01～R04、WP27-R01～R03、WP30-R01～R06 及直接回归复审后停止；未启动 WP22/WP23/WP28/WP29/WP31 或其他包；未修改 `reference/`；未运行游戏/参考脚本/网络；未提交/推送。

**第三十五轮（WP26–WP30 v2 复审与 v3 收尾，本轮，2026-09-26）**：

- **复审结论**：v2 复审报告 `8c23dfa1`（16,221 字节）仍 REQUEST_CHANGES：**8 项必修与 BATCH-C01/C02 CLOSED，仅剩 WP26-R02/R04、WP27-R01/R02、WP30-R05**；既有通过范围保留。修订前实测六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。
- **修订（五项＋C03 全部核实认可）**：WP26-R02（§3.3 管道名单删除外来赠送）；WP26-R04（"仅队伍"限定为初始检查；内层复检无值返回、外层仍 true；§7 拆入口初检/内层复检两行）；WP27-R01（§10.2 拆"预检·纯"与"添加·执行并写入"）；WP27-R02（菜单"已登记 -> 取消（不要求处理器）；未登记且资格通过 -> 登记"）；WP30-R05（羽毛只绕 100 点阈值、仍受 252/510；§12.2 三向量）；C03（治疗条件检查对象、配预检限定、过滤重置限带谓词、均分两份额按资格、"同上"锚定、通用版标签、setter 引用章节）。
- **修订后 v3**：WP26 `afc7214a`（35,387 字节）、WP27 `969cb37c`（27,166 字节）、WP30 `41e71624`（36,040 字节）；矩阵 `c4505715` → `6b49c40b`（41,342 字节；六行"仅剩具名项"）；交付摘要 v3 `df4926ae`（11,682 字节）。逐项回应 `8a4ee716`（6,393 字节）、差异 5 份（`237ae5f3`/`5add2f96`/`c684dcb1`/`e3c3e241`/`fb5a69fd`）；TSV v10 `35cd3605`（11,707 字节）；复审报告与提示登记于第 1 节。
- **保留**：被审 v2 哈希保留于第 3 节历史；三包保持 **ReviewPending**；未自批 Reviewed；首轮回应 R05 简写已纠正（旧回应保留历史）。
- **停止点**：送五项（WP26-R02/R04、WP27-R01/R02、WP30-R05）及直接回归短复审后停止；未启动 WP22/WP23/WP28/WP29/WP31 或其他包；未修改 `reference/`；未运行游戏/参考脚本/网络；未提交/推送。

**第三十六轮（WP26–WP30 闭合回填与 WP31→WP28→WP29 批次，本轮，2026-09-26）**：

- **复审结论**：闭合复审报告 `21712a5c`（11,449 字节）结论 **WP26/WP27/WP30 均 PASS_SCOPED**（最后五项关闭、未发现直接回归；C03 记法维护随回填；179 条 manifest 与 83 条交付 TSV 匹配、189 项固定输入）。回填前实测六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。
- **回填（管理性）**：三包登记 **Reviewed（限定静态范围）**——WP26 `c87101ad`（35,738 字节）、WP27 `8064f172`（27,516 字节）、WP30 `6fbc5a20`（36,970 字节）；被审 v3 `afc7214a`/`969cb37c`/`41e71624` 保留历史、不伪称为复审对象。C03 三项同步（WP30 §12.2 锚定与 Shadow 前提承接；`008_PokemonBag.rb` 笔误更正、旧回应保留；"整批 8 项关闭"历史语境）。
- **必要状态引用同步（管理性）**：WP18 `54b54743`（37,399）、WP19 `1c4325f5`（36,443）、WP20 `9a2ad1ab`（35,027）、WP21 `b5eeb48e`（42,498）、WP25 `f505afd5`（27,107）。
- **WP31 基础进化（`b5966bbf`，35,629 字节）**：条件族目录（升级/道具/交换/战后/事件全族）；五入口统一守卫与首目标选择；提交顺序（统计→消息→进化后动作→物种变更→濒死保持→重算→标记→图鉴→进化时招式→收尾）、取消与复制（队伍/球前提）；入口对照（升级/道具重点，交换/战后/事件完整触发前向 WP32）；自检修正对 WP18 的引用（§4.1→§3.4）并级联。
- **WP28 主动道具与培养/教学（`f9cd5fe3`，32,848 字节）**：四类上下文分流（背包/野外/个体/战斗）；十个注册家族与覆盖目录（条件注册/复制/未命中归属）；治疗/复活/PP、EV 与培养（100 点阈值仅世代 ≤7、252/510 恒限）、经验糖果、机器/教学、进化道具（引用 WP31 批内固定 `b5966bbf`，尚未外审）、主要特殊道具；消耗时机（入口层返回真后扣减；战斗登记即扣减、失败退回；部分成功按份消耗）。
- **WP29 买卖与 BP 商店（`3705047f`，21,918 字节）**：金钱商店买/卖、BP 商店购买；库存预过滤（重要物品已持有）；价格来源/覆盖（买覆盖 >0、卖覆盖 ≥0 且参数×2、BP 商店共享买槽）与取整；数量上限（资源÷价、零价→每槽上限、钳 999）；写入顺序（买=先物可回退后钱；卖=先钱后物且移除不检查）；资源 setter 钳制与交易层两判分列；纪念球赠品；独立核对商店调用链（不套用 WP27 结论）。
- **批末交界核对**：四项通过（WP31×WP18/19/20/21/25/26/30、WP28×WP20/27/30/31、WP29×WP24/27、追踪一致性）；含 WP31 引用修正级联（WP31 `e5658f31`→`b5966bbf`、WP28 同步重固定）。
- **矩阵与交付**：矩阵 `6b49c40b` →（回填六行中间 `347dfff0`/41,242）→ `cbf671a8`（42,243 字节；六行 Reviewed＋四行 ReviewPending 增量）；交付材料 `review/wp31-wp28-wp29-delivery-2026-09-26/`（回应 `fd800ef2`、自检 `f22d8fdc`、交界 `63fb993b`、摘要 `3f832427`、差异 10 份）；WP26–WP30 交付摘要 v4 `bdd353fd`/13,366；闭合报告与提示登记于第 1 节；TSV v11（见第 1 节）。
- **停止点**：批末统一送审后停止；不启动 WP22/WP23/WP32/WP33 或其它包；三新包保持 ReviewPending（未自批）；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第三十七轮（WP31／WP28／WP29 首审修订（v2），本轮，2026-09-27）**：

- **复审结论**：首审报告 `5e34d822`（21,709 字节）结论 **REQUEST_CHANGES**（WP31×2、WP28×6、WP29×2 必修＋BATCH-C01/C02；205 条 manifest 与 109 条 TSV 匹配、208 项固定输入）；WP26–WP30 回填与五份上游同步**获接受**。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。
- **修订（10 项＋两组维护全部核实认可并修订）**：WP31-R01（事件编号无一次性消费状态；复用/取消后重试/不匹配三对照）、WP31-R02（物种设置形态/性别例外，按 WP18 §3.4；提交表/保留表/不变量/依赖同步）；WP28-R01（背包回退 UseInField、野外 1/0/−1 与快捷收集/确认分层）、R02（无个体检查只看队伍非蛋、循环返回=最后路径、直接工具库存边界）、R03（界面上限/效果应用/外层扣除分列；树果 EV5/h90 与糖果一次设置两向量）、R04（战斗退回按资格复检/目标分支，效果返回不控制退款、投球独立）、R05（REVIVALHERB 回满、XATTACK 分档、MAXMUSHROOMS 五项、GUARDSPEC=白雾、HONEY 返回语义）、R06（§5.6 形态/融合道具有界使用表；融合工具替换背包标识、拆分容量；修正"物品种类不变"与责任归属）；WP29-R01（库存原地过滤与列表复用边界）、R02（价格输入层级、PBS 仅非负整数格式、旧覆盖保留）。BATCH-C01/C02 同步（取消不进入成功序列、目标 VENUSAUR 0 级样本、TradeItem 对象、复制个体号静态闭合、缓存措辞、"语句数"口径、场景前提）。
- **修订后 v2**：WP31 `e541c650`（39,138 字节）、WP28 `f2f7618c`（42,586 字节；级联 WP31 修订稿引用）、WP29 `d5c847f1`（25,211 字节）；矩阵 `cbf671a8` → `a05c39f4`（42,454 字节；四行"首审已送审：REQUEST_CHANGES，修订后再送"）；交付摘要 v2 `023c090e`（10,914 字节）。逐项回应 `e516ca69`（10,646 字节）、差异 5 份（`1353e3c2`/`30f91d9a`/`b5b287d9`/`ce3183ac`/`0db55cfc`，相对本轮 `input-snapshot/`）；被审首版哈希保留历史；首审材料登记于第 1 节；TSV v12。
- **保留**：三包保持 **ReviewPending（首审修订后再送）**、不自批 Reviewed；矩阵前向 Inventoried 保留；未启动其它包。
- **停止点**：送原编号（WP31-R01～R02、WP28-R01～R06、WP29-R01～R02）及直接回归复审后停止；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第三十八轮（WP31 回填与 WP28／WP29 三点收尾，本轮，2026-09-27）**：

- **复审结论**：有限复审报告 `f6f2c705`（12,842 字节）结论 **WP31 PASS_SCOPED；WP28/WP29 仍 REQUEST_CHANGES**（原 10 项关闭 7 项，仅剩 WP28-R03/R06、WP29-R02；222 条 manifest 与 126 条 TSV 匹配、224 项固定输入）。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。
- **WP31 回填（管理性）**：登记 **Reviewed（限定静态范围，2026-09-27 有限复审 PASS_SCOPED）**——头部/§14；矩阵 F09-03 → Reviewed（WP31 子范围）＋前向 Inventoried；被审 v2 `e541c650` 保留历史，回填后 `ee47f124`（39,499 字节）不伪称为复审对象；WP28 引用同步为本轮限定通过（回填后版本）。**至此 WP01–WP21、WP24–WP27、WP30–WP31 限定通过**（WP22/WP23/WP28/WP29 未完成，不得写成连续全部完成）。
- **三点收尾（全部核实认可并修订）**：WP28-R03（删除两处"羽毛无多量"错误、恢复羽毛数量上限家族与三层结构；新增羽毛多量与 WING 别名向量）；WP28-R06（§6.8 删除"使用不改变物品种类"全局保证，改为具名效果与 §5.6 的标识替换）；WP29-R02（旧值保留例子改合法 `setPrice(D,-1)`/`setSellPrice(D,-1)`；BP 拆为"单价20/BP50→首查通过、最多2、选2花40余10"＋"单价60/BP50→首查拒绝"＋"复查失败另列前提"）；C03 记法（两层命名、检查通过后、最后路径速记、MAXHONEY）。
- **修订后 v3**：WP31 `ee47f124`（39,499 字节，回填后）、WP28 `7e10cb25`（43,917 字节；被审 v2 `f2f7618c` 保留历史）、WP29 `1ed4b957`（25,793 字节；被审 v2 `d5c847f1` 保留历史）；矩阵 `a05c39f4` → `909080cb`（42,493 字节）；交付摘要 v3 `6b22ac03`（13,286 字节）。逐项回应 `73c9cab3`（7,260 字节）、差异 5 份（`4d5e843d`/`85df9c4c`/`f9930cb9`/`2688d197`/`08809ecd`，相对本轮 `input-snapshot/`）；有限复审材料登记于第 1 节；TSV v13。
- **保留**：WP28/WP29 保持 ReviewPending（送三项及直接回归短复审）；不启动其它包。
- **停止点**：送 WP28-R03/R06、WP29-R02 及直接回归短复审后停止；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第三十九轮（WP28／WP29 回填与 WP33→WP34→WP35 批次，本轮，2026-09-27）**：

- **复审结论**：闭合复审报告 `8d56d23e`（8,920 字节）与提示 `a9e31d54`（12,960 字节）结论 **WP28/WP29 均 PASS_SCOPED、WP31 继承 PASS_SCOPED 且回填接受**；最后三项（WP28-R03/R06、WP29-R02）与 C03 全部关闭、未发现直接回归；238 条 manifest 与 142 条 TSV 匹配、固定 240 项输入；WP01–WP21、WP24–WP31 为可登记限定通过集合（WP22/WP23 未完成，不得称连续全部通过）。回填前实测六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。
- **WP28/WP29 回填（管理性）**：登记 **Reviewed（限定静态范围，2026-09-27 闭合复审 PASS_SCOPED）**——WP28 头部/§13、WP29 头部/§14；矩阵三行回填；被审 v3 `7e10cb25`/`1ed4b957` 保留历史，回填后 `a4ccb383`（44,159 字节）/`f7788c7d`（26,053 字节）不伪称为复审对象。
- **必要状态引用同步（管理性，6 文件）**：WP18 `55fb5004`（37,448）、WP19 `cd3dcf4b`（36,492）、WP20 `05a59789`（35,076）、WP27 `6ac234e4`（27,602）、WP30 `b9f58991`（37,019）、WP31 `0b40917c`（39,554）。
- **WP33 寄养会话与兼容性（`4e17c679`，21,180 字节）**：寄养槽位/寄存/取回、兼容评分与概率、256 步周期与走步经验（静默学招）、费用报价与事件责任、迁移与统计写入点；逐行核对与独立算术自检。
- **WP34 遗传与后代生成（`bb950920`，24,359 字节）**：归一/交换单次与 Ditto 边界；物种（熏香门/后代采样/地区钩子）、形态/Nature/特性/招式/IV/球/异色/病毒逐项与随机候选顺序；引用 WP33 批内固定版本（尚未外审）。
- **WP35 蛋与孵化（`61a6bdb9`，19,715 字节）**：孵化演出全通道逐行；每步次序与加速、多蛋顺序、提交 8 步写入、命名三出口、持久化边界；引用 WP34 批内固定版本（尚未外审）。
- **批末交界核对**：四项通过（WP33×WP25/27/30/06/24、WP34×WP18/19/20/21/33、WP35×WP34/12/25/26/06/09、追踪一致性）；详见交付目录 `boundary-checks.json`。
- **矩阵与交付**：矩阵 `909080cb` → `77c3bff0`（43,092 字节；F08-03/F08-04、F08-06 → Reviewed（对应子范围）＋前向 Inventoried，F09-05/F09-06/F09-07 → ReviewPending（批内固定、尚未外审）＋前向 Inventoried）；交付材料 `review/wp33-wp35-delivery-2026-09-27/`（回应 `64a8884e`、自检 `581b530f`、交界 `7bf8c59e`、摘要 `8c420fa7`、回填与引用同步差异 10 份）；旧批摘要 v4 `990f30b4`/14,649；TSV v14 `7368bba6`（23,314 字节，168 行）；闭合报告与提示登记于第 1 节。
- **停止点**：批末统一送审后停止；不启动 WP22/WP23/WP32/WP36 或任何其它包；三新包保持 **ReviewPending（未自批）**；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第四十轮（WP33／WP34／WP35 首审修订（v2），本轮，2026-09-27）**：

- **复审结论**：首审报告 `7f61f821`（19,379 字节）与提示 `2ad9d012`（11,396 字节）结论 **REQUEST_CHANGES**（WP33×2、WP34×3、WP35×3 必修＋BATCH-C01/C02；264 条 manifest 与 168 条 TSV 匹配、固定 266 项输入）；WP28/WP29 回填及六份必要状态引用同步**获接受**；既有 WP01–WP21、WP24–WP31 限定通过保留。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。
- **修订（8 项＋两组维护全部核实认可）**：WP33-R01（生成/领取工具守卫分层：仅"占用槽数=2"；兼容性/标记属周期与事件层；治疗蛋例外；生成副作用与重试重新生成）、R02（供方→学员两方向、学员空位、供方槽序、学员接受表、首项；get_egg_moves 与原始 egg_moves 分用）；WP34-R01（单次交换不复查；Ditto 四槽序矩阵；语言读双方拥有者）、R02（PICHU 无熏香、SEAINCENSE 在 AZURILL；样本三处替换）、R03（真正抽样/确定性派生/缓存三分；Nature 创建末尾已缓存；重掷只清 shiny 缓存）；WP35-R01（归零与防重属迈步调用者；pbHatch 不查蛋态/不写计数；负值/缺失不兜底）、R02（HatchSteps 三层次；摘要四段＋三组边界）、R03（拥有者重写不清缓存；未求值首次读取按新拥有者）；C01（迁移反例引用 WP10 §4、经验关闭前提、加速扫描时点）、C02（boundary-checks JSON 引号修复、WP34 链接、取证范围 11–255、措辞）。
- **修订后 v2**：WP33 `6cb65468`（24,789 字节；被审首版 `4e17c679` 保留历史）、WP34 `7ba35a9d`（29,265 字节；级联 WP33 修订稿引用；被审首版 `bb950920` 保留历史）、WP35 `0abe2622`（24,219 字节；级联 WP34；被审首版 `61a6bdb9` 保留历史）；矩阵 `77c3bff0` → `243df4e4`（43,258 字节）；交付摘要 v2 `462ee890`（8,745 字节）；boundary-checks 修复 `80dcc8aa`（2,877 字节；修复前 `7bf8c59e`/2,875）。
- **修订材料与交付**：`review/wp33-wp35-review-2026-09-27/` 回应 `74a9a812`（13,495 字节）、差异 6 份（`cb3f73bc`/`58ea7025`/`ab745492`/`d134a2e5`/`c0531217`/`a81c596f`，基准本轮 `input-snapshot/`）；首审报告/提示/检查 11 份登记于第 1 节；TSV v15 `44da94e7`/25,692（186 行）；manifest 本轮登记见 §1/§2.1/§3。
- **停止点**：批末统一送原八个编号（WP33-R01/R02、WP34-R01～R03、WP35-R01～R03）及直接回归复审后停止；不启动 WP22/WP23/WP32/WP36 或其它包；三包保持 **ReviewPending（未自批）**；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第四十一轮（WP33／WP35 回填与 WP34-R03 收尾（v3），本轮，2026-09-27）**：

- **复审结论**：v2 复审报告 `6314bd64`（13,517 字节）与提示 `d8379990`（8,009 字节）结论 **REQUEST_CHANGES**：**WP33/WP35 PASS_SCOPED（管理性回填）**、仅剩 **WP34-R03 一处**（末次普通异色缓存时点）；原八项中七项关闭、R03 的 Nature/随机输入部分与 C01/C02 保留关闭；282 条 manifest 与 186 条 TSV 匹配、固定 284 项输入。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。
- **WP34-R03 收尾（v3）**：§8.2 判定时点改写（**轮首读取**→命中停止；未命中清普通异色缓存并换号→下一轮或退出；用尽次数退出时**缓存为空**、收尾不补读；零次不读取/不清）、§9.9 与 §13.2 同步（新增 N=2 用尽时点对照与 PID0/N0 对照行）；未添加返回前补判定；被审 v2 `7ba35a9d` 保留历史。
- **WP33／WP35 回填（管理性）**：登记 **Reviewed（限定静态范围，2026-09-27 v2 复审 PASS_SCOPED）**——头部/§13、头部/§15；被审 v2 `6cb65468`/`0abe2622` 保留历史，回填后 `8c678e33`（25,144 字节）/`315e74f6`（24,540 字节）不伪称为复审对象；级联引用（WP34→WP33 `8c678e33`；WP35→WP34 v3 `d0113d76`，尚未外审）；C03 记法同步（事件层责任表述、领取引用 §5.3、濒死非蛋成员仍可提供加速）。
- **矩阵与交付**：矩阵 `243df4e4` → `17fa287c`（43,198 字节；F09-05/F09-07 → Reviewed（对应子范围）＋前向 Inventoried；F09-06 保持"仅剩 R03 末次缓存（v3 已修订、待短复审）"）；交付摘要 v3 `28cbc965`（9,383 字节）；收尾材料 `review/wp33-wp35-recheck-2026-09-27/`（回应 `0188ef21`、差异 5 份 `7c957def`/`422f4446`/`6b739e7f`/`46131c4f`/`82e5042e`）；v2 复审材料 11 份登记于第 1 节；TSV v16 `a756e2ee`/27,947（203 行）。
- **停止点**：批末统一送 **WP34-R03 剩余点及直接回归**（连同 WP33/WP35 回填与 C03 差异）短复审后停止；不启动 WP22/WP23/WP32/WP36 或其它包；WP34 保持 **ReviewPending（未自批）**；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第四十二轮（WP34 回填与 WP59→WP36→WP60 批次，本轮，2026-09-27）**：

- **复审结论**：闭合复审报告 `90c20faf`（10,068 字节）与提示 `f791c8c2`（15,325 字节）结论 **WP34 v3 PASS_SCOPED、无剩余必修**；WP33／WP35 回填与 C03 获接受；299 条 manifest 与 203 条 TSV 匹配、固定 301 项输入。回填前六项固定对象与报告 §1 及 `input-snapshot/` 完全一致。
- **WP34 回填（管理性）**：头部/§16 登记 **Reviewed（限定静态范围，2026-09-27 闭合复审 PASS_SCOPED）**；被审 v3 `d0113d76`（30,617）保留历史，回填后 `8e3511d3`（30,758）不伪称为复审对象；矩阵 F09-06 → Reviewed（WP34 子范围）＋前向 Inventoried；WP35 引用同步（`34e83236`/24,583）；旧批摘要 v4（`6b1d9a1a`/9,924）。**限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP35**。
- **WP59 世界时间/天气与场地能力（`971b0807`，34,153 字节）**：时钟/时段/季节/明暗与消费者目录；天气 9 种/类别/地图概率管线/事件命令 236/显示渐入；12 族场地能力（入口三层、徽章统一门、各族许可→效果→返回、直接工具与处理器链差异、摇树概率向量）。
- **WP36 普通遭遇与修正（`b8a5bc26`，27,307 字节）**：地图×版本表与编译器约束；类型目录 25 项；类型选择与时段细分回退；概率链（宽限放大掷/累加器/修正顺序）；选择（偏好过滤/多次掷/等级）与生成（持有物/闪光分档/性别性格/病毒/钩子）；开战交接与状态生命周期。
- **WP60 树果（`227bb696`，20,545 字节）与钓鱼（`b7de3ff4`，16,866 字节）**：植物状态机/重植循环/水分与两机制产量/交互次序；三竿入口/等待-咬钩-收竿/三分支与状态恢复/遭遇请求与战斗侧消费。
- **批末交界核对**：五组通过（WP59×WP06/11/12/20/24、WP36×WP59/03/19/24、WP60 树果×WP59/27、WP60 钓鱼×WP36/59/12/14、追踪一致性）；详见交付目录 `boundary-checks.json`。
- **矩阵与交付**：矩阵 `17fa287c` → `64d297de`（44,540 字节）；交付材料 `review/wp59-wp36-wp60-delivery-2026-09-27/`（回填回应 `8ab43cb9`、摘要 `407c61a5`、自检 `86348342`、交界 `cef81335`、回填差异 4 份）；TSV v17 `aec34bd2`/30,842（225 行）；闭合轮材料 10 份登记于第 1 节。
- **停止点**：批末统一送 WP59／WP36／WP60（两产物）首审后停止；不启动 WP22/WP23/WP32/WP37/WP61 或其它包；三新包保持 **ReviewPending（未自批）**；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第四十三轮（WP59／WP36／WP60 首审修订（v2），本轮，2026-09-27）**：

- **复审结论**：首审报告 `e9750d3b`（26,473 字节）与提示 `53a04e9a`（15,388 字节）结论 **REQUEST_CHANGES**（WP59×4、WP36×4、WP60×5 必修＋BATCH-C01/C02；321 条 manifest 与 225 条 TSV 匹配、固定 323 项输入、14 条链接与 24 个 JSON 有效）；WP34 回填与 WP35 必要引用同步获接受，既有 WP01–WP21、WP24–WP31、WP33–WP35 限定通过保留。修订前实测七项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。
- **修订（13 项＋两组维护全部核实认可）**：WP59-R01（duration 仅 0/正数两义、同类型强度不刷新、编辑器 None/取消→nil 与保存才提交；删“2→2 秒”）、R02（入口×实际检查×确认×效果矩阵；确认处理器仅 DIG/TELEPORT；直接 CUT/DIVE/SURF 边界）、R03（返回五分级；HEADBUTT 坐标处异常、FLY 内部 false 外层 true）、R04（月相 8 阈值含等号/负回绕/日内项快照；星座 7/20→3、7/21–7/22→0、7/23→4；tone 缓存分层）；WP36-R01（累加折算 A=21/189/210→21/21/22 整数除；宽限分母取整；reset 与装图保留规则；次序＝累加→自行车→地图级→道具/特性）、R02（禁用仅触发检查；候选空早退保留；开战调用正常返回后清理；强制移动分流）、R03（each_of_version 0 版数组键反例；四种对照）、R04（迷人身躯 2/3 异性＋1/3 同性、无性别不赋值；首非蛋口径）；WP60-R01（精灵链不推进旧机制；6h→阶段 3/水分 10/惩罚 0、10h→4/−5/3；重植按剩余小时）、R02（施肥先写后扣、取消不回滚；采摘次序与外层 reset）、R03（Yield 校验/对调/缺省 3/15/2,5/缺记录报错）；WP60-R04（surfing 标志资格；公共事件返回真前提与整体绕过）、R05（等待段＋1、每段 0.4s；抖动八槽 1.6s；67.5 阈值=68% 有效）；C01（26 类型、IV 重掷重算、雨粒子左下/每秒、24×24 中间量、机制标记与设置分离、浇水双写）、C02（WP35 头部残句清除；钓鱼 §1 与主规则引用 WP28、容器 WP27；WP14 不虚构交界）。
- **修订后 v2**：WP59 `440a67b1`（40,114 字节；被审 v1 `971b0807` 保留历史）、WP36 `3120d1e1`（32,592 字节；级联 WP59 v2；被审 v1 `b8a5bc26` 保留历史）、树果 `e468c3bf`（24,593 字节；级联；被审 v1 `227bb696` 保留历史）、钓鱼 `f280e9a7`（20,304 字节；级联＋C02；被审 v1 `b7de3ff4` 保留历史）；矩阵 `64d297de` → `b580eb92`（44,780 字节；六行 → “首审 REQUEST_CHANGES，已修订为 v2、待复审”）；交付摘要 v2 `835334ef`（10,390 字节；短标签笔误 835334ee 于第四十四轮更正）；self-checks v2 `4f9c02d8`（11,965 字节）、boundary-checks v2 `b12ebefd`（6,271 字节）；WP35 头部引用同步 `1fbfd98e`（24,610 字节，管理性）。
- **修订材料与交付**：`review/wp59-wp36-wp60-review-2026-09-27/` 回应 `97c5be51`（19,116 字节）、差异 9 份（`a7c2a109`/`1f9a2df4`/`4a34f1c6`/`0c8f94ce`/`5b0aeac7`/`ffc170bd`/`5ec19ea2`/`9214e3df`/`3f7e50a9`，基准本轮 `input-snapshot/`）；首审报告/提示/检查 11 份登记于第 1 节；TSV v18 `a8eb500f`/33,716（246 行）；manifest 本轮登记见 §1/§2.1/§3。
- **停止点**：批末送原 13 个编号（WP59-R01～R04、WP36-R01～R04、WP60-R01～R05）及直接回归复审后停止；不启动 WP22/WP23/WP32/WP37/WP61 或其它包；四产物保持 **ReviewPending（各自具名范围，首审修订后再送）**；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第四十四轮（WP59／WP36／WP60 v2 复审收尾（v3），本轮，2026-09-27）**：

- **复审结论**：v2 复审报告 `173ac1dc`（16,199 字节）与收尾提示 `16953dad`（9,341 字节）结论 **REQUEST_CHANGES**：原 13 项中 9 项关闭，仅剩 WP59-R02、WP59-R04、WP36-R02（含钓鱼直接传播）、WP60-R01；342 条 manifest 与 246 条 TSV 匹配、固定 344 项输入；C02 关闭、WP35 管理性同步接受、既有限定通过保留；C01 只剩 IV 重算简写、另列 C03 登记／场景维护。修订前实测七项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。
- **收尾修订（四项＋C01 剩余、C03 全部核实认可）**：WP59-R02（FLY CanUse 列与包装同函数、显式个体不重查招式；DEBUG 只绕被检查函数内部门、不绕快捷收集）；WP59-R04（完整整数日数学含 2,299,160 精确世纪门；星座全 12 行表与匹配规则；旧零色调不变量删除改缓存分层；三秒向量补起始条件）；WP36-R02（终态按入口分列：pbEncounter 候选空 false/保留、开战返回 true/清；步进 allow 拒绝末尾 force_single=false、开战返回清+triggered+false 不套 true；钓鱼 §7 传播同步）；WP60-R01（范围行与 6h→阶段 3/水分 10/惩罚 0、雨浇水显式 update 前提；采摘终态标注）；C01（IV 至多 4 轮、环后仅实际重掷才统一重算一次）；C03（短标签 835334ef 更正、旧回应段标题更正 FLY :471–512／SWEETSCENT :791–832、钓鱼概率分列 45/70/95→68/100/100、仅潜水前提、树果终态记法）。
- **修订后 v3**：WP59 `9a41d185`（42,041 字节；被审 v2 `440a67b1` 保留历史）、WP36 `d21edcc7`（33,424 字节；级联 WP59 v3；被审 v2 `3120d1e1` 保留历史）、树果 `114c432b`（24,912 字节；级联；被审 v2 `e468c3bf` 保留历史）、钓鱼 `5f274a2c`（20,759 字节；级联＋传播；被审 v2 `f280e9a7` 保留历史）；矩阵 `b580eb92` → `1de3852f`（44,896 字节；六行 → “9/13 关闭＋四项已收尾修订为 v3、待复审”）；交付摘要 v3 `809e0fa0`（12,097 字节）；self-checks v3 `3bad9fd6`（12,955 字节）、boundary-checks v3 `db51d641`（6,903 字节）。
- **收尾材料与交付**：`review/wp59-wp36-wp60-recheck-2026-09-27/` 回应 `233fd124`（13,082 字节）、差异 8 份（`8c772de5`/`9a109faa`/`783880a4`/`faded8c8`/`8810fb3e`/`8fe7889c`/`ae9e21ca`/`f35089b1`，基准本轮 `input-snapshot/`）；v2 复审材料 11 份登记于第 1 节；TSV v19 `d2e72991`/36,452（266 行）；manifest 本轮登记见 §1/§2.1/§3。
- **停止点**：批末送四个剩余编号及直接传播复审后停止；不启动 WP22/WP23/WP32/WP37/WP61 或其它包；四产物保持 **ReviewPending（各自具名范围，复审后再送）**；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第四十五轮（WP59／WP36／WP60 闭合回填与 WP39→WP40→WP41 批次，本轮，2026-09-27）**：

- **复审结论**：闭合复审报告 `25835002`（12,741 字节）与回填提示 `11123b46`（17,658 字节）结论 **PASS_SCOPED**（原 13 项全部关闭、C01/C02/C03 接受；362 条 manifest 与 266 条 TSV 匹配、固定 364 项输入）；回填前七项固定对象与报告 §1 及 `input-snapshot/` 完全一致。
- **回填（管理性）**：四产物登记 **Reviewed（限定静态范围，2026-09-27 闭合复审 PASS_SCOPED；管理性回填）**（被审 v3 `9a41d185`/`d21edcc7`/`114c432b`/`5f274a2c` 保留历史；回填后 `46e80106`/42,401、`5a05aad7`/34,305、`1d588f0a`/25,082、`e5d94e05`/20,950 不伪称为复审对象）；C04 两处记法（WP59 年调整括注方向、WP36 终态场景按入口拆分＋临时标记注释）；矩阵六行 → Reviewed（对应子范围）＋前向 Inventoried；必要状态引用同步（管理性）：WP34 `46acc90f`/30,716、WP35 `34f1a5df`/24,610。**回填后限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP59–WP60**。
- **WP39 战斗上下文与参与者（`26c72739`，34,016 字节）**：入口/规则/跳过/跳过清点；布局 9 种与对面取序、缩减与拒绝；所有者/队伍段/席位映射与伙伴编队；参战者初始化职责；环境/天气/时间输入与钩子时间线；对视合并与覆写钩子。
- **WP40 命令、服从性与行动顺序（`3ced6de7`，33,115 字节；引用 WP39 批内版本）**：命令目录与控制权/撤销重选；选择期原因族与物品两层、目标合法性；攻击阶段次序与使用招式完整检查序；服从整数门与不服从三分支；优先级/子优先级/空间/平局与重算时点；Mega/Primal 分列、Call 四分支、Shift 选择语义。
- **WP41 换人、位置移动与逃跑（`75746653`，23,900 字节；引用 WP40 批内版本）**：换入五拒绝/换出双阶段；出入场次序与入场通知；回合末替补与页面提示边界；Shift 重映射与代价；逃跑资格聚合与整数判定；拖出/接力/换出招式有界族。
- **批末交界核对**：五组通过（WP39×WP20/24/25/11/02 及 WP36/59、WP40×WP39/19/20/27/28、WP41×WP39/40/27、持久与临时状态、追踪一致性）；详见交付目录 `boundary-checks.json`。
- **矩阵与交付**：矩阵 F11-01～F11-05 增量后为 `0d6a0c9c`/45,993；交付材料 `review/wp39-wp41-delivery-2026-09-27/`（回填回应 `57e53a70`、摘要 `f23ddcb0`、自检 `469c9b30`、交界 `4d942a4e`、回填差异 8 份）；旧批摘要 v4 `6d74f799`/12,913；TSV v20 `e4054253`/39,875（291 行）；闭合轮材料 10 份登记于第 1 节。
- **停止点**：批末统一送 WP39／WP40／WP41 首审后停止；不启动 WP22/WP23/WP32/WP37/WP38/WP42/WP61 或其它提取包；三新包保持 **ReviewPending（未自批）**；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第四十六轮（WP39／WP40／WP41 首审修订（v2），本轮，2026-09-27）**：

- **复审结论**：首审报告 `a539db6c`（23,770 字节）与有限修订提示 `543b6f14`（14,362 字节）结论 **REQUEST_CHANGES**（WP39×3、WP40×5、WP41×4 必修＋C01/C02；387 条 manifest 与 291 条 TSV 匹配、固定 389 项输入；旧批回填接受、既有限定通过保留）。修订前实测六项固定对象与报告 §1 及本轮 `input-snapshot/` 完全一致。
- **修订（12 项＋两组维护全部核实认可）**：WP39-R01（单次构造/引用身份/入口时间线/校验位置分开）、R02（九布局对面取序全表＋邻近规则；全局索引÷2 业主映射；缩减前提 1v1/1v2）、R03（写入方向分层：能力副本/item 持久/字段级入口/回读）；WP40-R01（成功登记保留与取消点；Mega 复位只清非负，[-1,2,-2]→[-1,-1,-2]）、R02（玩家逃跑命令阶段当场判定；敌侧登记与 alwaysflee 分列）、R03（specialUsage 与 skipAccuracyCheck 分开＋四类调用表；前置通过先扣 PP、后段失败已扣；安可检查新招；Stance Change）、R04（道具按 battle_use 家族复检/退款；球直接执行）、R05（抢夺按最小正标记 2/4→2）；WP41-R01（查询/普通/替补三入口守卫分层；计数时点；Battler.speed 当前值；94/64）、R02（仅换入/组合/UI/登记/执行分层；执行不复查）、R03（普通换下不解除 Mega/Primal；显式解除仅在濒死/战后；副本 HP 置 0≠持久归零）、R04（强制换出变化/伤害两族分列；伤害族野生终局无吸盘/扎根门；打落不属该族）；C01（术语/有界十项重映射/均匀仅 random=true/场景前提/statusCount/伙伴 id 引用）、C02（批内完整哈希绑定与条款文件错引更正）。
- **修订后 v2**：WP39 `1fdfb8bc`（38,555 字节；被审 v1 `26c72739` 保留历史）、WP40 `555282ba`（38,012 字节；级联 WP39 v2；被审 v1 `3ced6de7` 保留历史）、WP41 `237ac575`（28,916 字节；级联 WP40 v2＋WP39 v2；被审 v1 `75746653` 保留历史）；矩阵 `0d6a0c9c` → `0fe9fe2f`（46,193 字节；五行 → "首审已修订为 v2、待复审"）；交付摘要 v2 `f9209703`（8,855 字节）；self-checks v2 `9633f336`（12,444 字节）、boundary-checks v2 `0db06e68`（5,323 字节）。
- **修订材料与交付**：`review/wp39-wp41-review-2026-09-27/` 回应 `eec9fbc2`（17,055 字节）、差异 7 份（`dd473ba2`/`ae4631a4`/`7667dd09`/`18eaa1ee`/`89f79943`/`d3da9737`/`7071b5d6`，基准本轮 `input-snapshot/`）；首审材料 11 份登记于第 1 节；TSV v21 `1a5a56e8`/42,331（310 行）；manifest 本轮登记见 §1/§2.1/§3。
- **停止点**：批末送原 12 个编号（WP39-R01～R03、WP40-R01～R05、WP41-R01～R04）及直接回归复审后停止；不启动 WP22/WP23/WP32/WP37/WP38/WP42/WP61 或其它提取包；三包保持 **ReviewPending（各自具名范围，首审修订后再送）**；未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。

**第四十七轮（WP39／WP40／WP41 v2 复审收尾（v3），本轮，2026-09-27）**：

- **复审与预检**：报告 `50a485f2eac388d188704b1b6e1aa7d63c8a4883e0c07b6067fa9ff880a75467`（15,110 字节）／提示 `dbcae65a951fd598fb2dea1f15f79363b9bd05bf6dc510602de22e4d667b2d68`（9,575 字节）结论 REQUEST_CHANGES、9/12 关闭，剩 WP39-R01、WP40-R03、WP41-R02。六件必检与三件补检全部匹配快照；保留关闭九项与已接受部分。被审 manifest `5bf42d0d98ca4a2a39cfc3d06815ac9fd8747be8dbc49631993dca8101fa84b1`（218,662 字节，406 条）与主 TSV v21 `1a5a56e8521544f38c5aa3b1a588d9dfc270219fa3b3a63504f930fab49ea7a8`（42,331 字节，310 条）留史。
- **三项收尾**：WP39-R01——合并成功复用已保存 A，第二核心只装载 B 数据；未保存探测另分支；数组创建／已有对象复用、具名钩子时间线与野生／训练家返回 3／5 对照；WP40-R03——删除无目标免耗和特殊动作统括服从豁免摘要，保留两标志与四类调用，普通后段失败 PP 5→4；WP41-R02——完整组合查询、严格／宽松队伍 UI、登记与执行分层，不登记也可组合检查；WP40 概念表同步分族合同，boundary 组 3 去除相反保证。
- **C03 维护**：WP39 参与者校验用可战斗野生计数；WP40 返回上一席位只撤销上一席位、Mega 环先于业主槽；WP41 伤害族末段门限非野生拖出，逃跑摘要按三入口、调试取消决定不变但停止命令期余席；交付摘要首审回应／diff 目录与 v1→v2→v3 历史修正。只定点读取 13 个源文件并核对固定 commit，未执行参考过程。
- **当前固定**：WP39 `864dec26`/42,165、WP40 `716a2442`/40,100、WP41 `463cab3c`/31,502；矩阵 `2402cf42`/46,283；摘要 `8360aec4`/11,292；self `6d16628f`/23,048；boundary `46a58b20`/6,926。三条完整哈希绑定同步，v1／被审 v2 留史，当前 v3 尚未外审。
- **材料与登记**：`review/wp39-wp41-recheck-2026-09-27/revision-response.md`（`7fea838c46413d20afde7b2485bbe7855b6bc779e95a18b30fa4f49a46ade36a`, 15,187 字节）与七份 `revision-diffs/`（基准同轮 input-snapshot，内存重建 7/7）；reviewer 原件 11 份均保留并补登。主 TSV v22 `4bf6bcf4947aebeae1e46f10ba9ced94c4ed227c2d69435253c5802f56929a97`（44,821 字节，329 条）；manifest §1 425 条，§2.1／§3 同步。清单不自哈希，最终全量实测由交付消息报告。
- **停止点**：仅送 WP39-R01、WP40-R03、WP41-R02、C03 差异及直接传播短复审并停止；三包和 F11-01～05 保持 ReviewPending（各自具名范围）＋前向 Inventoried；不自批 Reviewed。未启动其它包、未发消息、未创建任务／并行 Agent、未提交／推送；reference 只读，未运行游戏、参考 Ruby／表达式、解释器／事件脚本、生成器、编译器、转换器、插件或真实网络，未操作真实地图／存档／输入。Demo、宿主、媒体、插件、U01–U10 与 WP78→WP79→WP80 仍保留。

**第四十八轮（WP39／WP40／WP41闭合回填＋WP43→WP44→WP45批次，本轮，2026-09-27）**：

- **独立结论与预检**：报告 `c88d91cf0202e083294870896283fc10264860f608b8bad69ba46b9c622b7f07`（11,892字节）、执行提示 `a712c0fb9c3311bfbade32305cfb000827864d5bb985d07567022c1763f9ed35`（16,208字节）；原12项及C03全部闭合、三包PASS_SCOPED（限定静态范围）。六项固定输入＋主TSV七项MATCH。被审manifest `029ace88ec69272796cd6be016d605be5d4e0ebb18b31948a9c52008265ca30d`（228,722字节，425条）与TSV v22 `4bf6bcf4947aebeae1e46f10ba9ced94c4ed227c2d69435253c5802f56929a97`（44,821字节，329条）保留历史。
- **管理性回填**：WP39 `9a3a796f`/42,697、WP40 `07789951`/40,547、WP41 `e6b835af`/31,897；三包头尾、WP39/40互相状态、WP40→WP39与WP41→WP40／WP39完整哈希级联，不改已接受行为；被审v3 `864dec26`/42,165、`716a2442`/40,100、`463cab3c`/31,502与回填后身份分开。旧批摘要v4 `a1df7ee3`/12,006；五份差异以闭合快照为基准，均可内存重建。
- **WP43**：普通类型／相性与命中资格分层；阶级阈值／会心门／伤害四类倍率及舍入，计算伤害与计划／实际HP分开；已读固定伤害、混乱、吸收等有界接口。21个固定抽取值／数值向量；完整处理器前向WP48/50。新增N01：上游无防守简写的具名反例，待外审处置，未静默修改WP40。
- **WP44**：五持久异常、混乱／着迷／畏缩／瞌睡及计数；普通／同步／自施／直接提交分开；七阶级资格、反转／倍增／镜甲、部分成功与直接重写；114个阶级文件标识、31状态标识及23域外标识的覆盖附表。29个状态／阶级向量，自己的期限消费者已定位，完整总序仍WP42。
- **WP45**：世界默认／战斗临时／压制／清除分开；9天气／5场地名录；13全场＋22侧＋9位置记录；自然恢复、直接清除、火海双递减、危害／侧交换／位置延迟与Shift差异。29个场景，完整招式／特性／道具家族留相应前向。
- **当前新产物**：wp43-types-accuracy-and-damage `6021d835`/29,511、wp44-statuses-stat-stages-and-immunities `b7eae260`/35,014、wp44-effect-coverage `ea5237d3`/24,809、wp45-weather-terrain-side-and-position-effects `2fbe3b65`/34,109；均ReviewPending（自身范围）。WP44绑定WP43，WP45绑定WP44主稿／附表及WP43实际完整哈希。矩阵仅8行管理＋新批变更，`bf77403c9b402f55830a0db482006465d9b74e0e798ab758c80f204e33ab1661`（47,030字节），F11-06/07未动。
- **交付与登记**：`review/wp43-wp45-delivery-2026-09-27/` 回填回应 `3d9f33857088e6000cc0a588b74897aeb000e91e0338ba12e50c7edf48d0978c`/5,830；摘要 `96b9abf484d4eafa958b81f41c4755ff250e19c240804577a74236eed3027619`/8,597；self `3c1259dd3f8966282b7880de4bee02b8c7a5bcd8640ed6dae8e729dc6b841113`/40,415；boundary `c20c3cbcf1e0488f899ab8ff389635543efc49a5499f58741456ad481200687a`/4,122；5份回填差异。闭合轮reviewer原件11件完整登记。主TSV v23 `f9650af5cc4b9d450006844b96436592211721e49a0dba1036df6e8d6e4175f7`（48,017字节，353条），manifest当前表449条；清单自身不自哈希，最终全量终值由交付消息实测报告。
- **批末出口**：回填→WP43→WP44→WP45→五组交界与材料已按授权执行，仅将这三包／附表及N01交本批独立首审并停止。限定通过集合仍为WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP59–WP60。未自批新三包Reviewed，未启动WP22／23／32／37／38／42／46或第四新包；未发reviewer消息、未创建任务／并行Agent、未提交／推送。reference只读；未运行参考过程／游戏／真实网络，Demo、宿主、媒体、插件、U01–U10及WP78→79→80出口保留。

**第四十九轮（WP43管理回填、N01同步与WP44／WP45有限修订，本轮，2026-09-27）**：

- **独立结论与预检**：报告 `308acc6467f730722d8cf59eec0b18173c91b9257d55da311ffab09432bf6ea1`（15,538字节）、提示 `adab1c0e054f89988bf6069cd6bfdf5f25367568d52b9b0a04a8895065bf5148`（11,454字节）：WP43本体PASS_SCOPED；批次REQUEST_CHANGES，WP44-R01/R02、WP45-R01三项必修；N01新证据CONFIRMED，需实际上游同步；C01两处维护。十二项实测与input-snapshot相同。修订前manifest `022a35f6d57ca87d33d2dc6d8475db73afa04200b2a94ace85c2990023ebdc14`（240,319字节，449条）及主TSV v23 `f9650af5cc4b9d450006844b96436592211721e49a0dba1036df6e8d6e4175f7`（48,017字节，353条）留史。
- **N01与回填**：WP40 §5.3按新证据分开解除半无敌阻挡／实际普通命中处理器，保留r69／r70及模式破坏关对照；这是行为简写校准，不叫纯状态回填。WP41只同步上游一行。WP43 A～F管理回填Reviewed，旧首版 `6021d835ebd2b62eac63062c5475e53501b5e6d46ff94873f2284799cf11ef0e`（29,511字节）为独立被审对象；公式与原数值保持，N01改确认记录。旧WP40范围与旧12项关闭保留，N01实际修订待有限复核。
- **三个必修与C01**：WP44-R01补K01–K22对象／量／序／前门／部分成功／UserSide，附表精确锚点代替泛化回指；重力81→121先截断、青草61→31先四舍五入且无额外接地；破壳五项与五集合族具名。WP44-R02区分中央反射与无模式破坏门的多项预检，M01/M02/M03对照。WP45-R01免连续保护抽签后仍检查其它未动UseMove／Shift，失败计数9→1、不建侧标记，成功9→27。C01普通毒不增Toxic，仅剧毒计数正递增；取证尾数781。13源文件定点回读／固定commit匹配，无参考执行。
- **当前身份与传播**：wp40-commands-obedience-and-action-order `ad471872`/42,476、wp41-switching-positioning-and-escape `42878fac`/31,939、wp43-types-accuracy-and-damage `0cd9958c`/30,543、wp44-statuses-stat-stages-and-immunities `85e17c6c`/49,950、wp44-effect-coverage `47bd80e2`/27,133、wp45-weather-terrain-side-and-position-effects `f92b0f3c`/35,823；十条受影响完整哈希绑定匹配；矩阵 `b230d1d7840b31923c741d439c2344990c18e00108a45801fdc45b6fd5078cc7`（47,092字节），仅F12三行：WP43子范围Reviewed＋前向Inventoried，WP44/45修订v2仍ReviewPending＋前向Inventoried。114／31／23审计身份及起始行、67普通参数不变；22合同锚点明确。WP43原公式段／前20条数值向量与WP45已支持主要生命周期段字节回归匹配。
- **交付与清单**：新增`review/wp43-wp45-review-2026-09-27/revision-response.md`（`a114fc008cecdb26a1b3832662e2e3283ce38edffc81d058f6ceb1e3d545e173`, 16,324字节）及10份revision-diffs（均对本轮快照，可内存重建），不覆盖reviewer原件。摘要v2 `39275cb4291ba561557e2ee014cb5c1d5236836bcd615d981b8a31878d8b2d7d`/9,790；self v2 `307d1ff0d54d9c1ddbcf8ee10f6161e6eff044cb5d486352b3acab643313004d`/56,423；boundary v2 `21abfe14138ed5e2fcd5ba3d3f0b499d192326e970c4495a905fcafa0098ac4e`/6,629；旧声明／旧backfill差异置历史语境。reviewer12件补登；主TSV v24 `95415831e570e765210686c637f3552e6e9cf5a7595e2cca23eae462186720d7`（51,044字节，376条），当前表472条。清单不自哈希，完整终值由交付消息实测报告。
- **范围与停止**：仅送WP44-R01/R02、WP45-R01、BATCH-N01、C01和直接传播有限复审后停止。限定通过集合WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43、WP59–WP60；WP44主稿／附表与WP45不自批Reviewed。不启动任何新包，不创建任务／并行Agent、不发reviewer消息、不提交／推送；reference只读，不执行游戏、参考过程或真实网络。Demo、宿主、媒体、插件、U01–U10及WP78→WP79→WP80保留。

**第五十轮（WP44／WP45闭合管理回填、N01收尾及WP42→WP48→WP49首稿，本轮，2026-09-27）**：

- **授权与预检**：独立有限复审PASS_SCOPED；WP44-R01/R02、WP45-R01、BATCH-N01/C01全闭合，WP43回填接受。八必检加WP41／主TSV补检逐字节匹配。原manifest `8ea63286474328dcb2ca45aa6af3aac385bf7f33ec01bff4e3deda721dc340fe`（253,979字节、472条），原TSV v24 `95415831e570e765210686c637f3552e6e9cf5a7595e2cca23eae462186720d7`（51,044字节、376条）保留历史。
- **管理维护**：WP40 N01 CLOSED→WP41必要身份→WP43关闭说明→WP44主稿／附表Reviewed→WP45 Reviewed。已审行为不重写；矩阵F12-01/02/03相应子范围维护，旧摘要v3明确当前／历史语境，旧checks和reviewer原件／快照不倒写。
- **新批**：wp42-growth-end-of-round-and-battle-outcomes `9bde1314`/37,859、wp48-ability-calculation-modifiers `480016af`/34,233、wp49-ability-phase-triggers `92869008`/50,601。WP42 A～E主阶段／成长／终局，WP48 A～E计算／免疫27族，WP49 A～F阶段21族及直接生命周期，三包仅ReviewPending。WP49完整绑定WP42／48批内未外审身份；矩阵F11-06/07、F12-06两个子范围登记，未自批整行。
- **自检与交界**：29／23／31共83静态场景，16项独立常数算术；26份源身份与固定commit blob一致，实际阅读范围各稿具名。48族239直接＋24复制语句，267展开身份，无主归属交叉；每身份有行为参数正文。五组交界覆盖成长／写回／总序、计算与免疫、阶段与退出／连锁、登记接缝及追踪。气体结束重触发、吐导弹读后写、舞者失败恢复和场地重复通知按源保留，未改reference。
- **材料**：`review/wp42-wp48-wp49-delivery-2026-09-27/backfill-response.md` `7b99bc61584becf3e9850a1d16bad684add81899be06c44f94a6d268b976a7e2`（4,642字节）。
- **材料**：`review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md` `c688fc9d509fa605b69dd4a29bc69e990f98668ed15ae83dd52f913844406f1a`（5,577字节）。
- **材料**：`review/wp42-wp48-wp49-delivery-2026-09-27/self-checks.json` `d7ffb5cdad8253c7f2b52f7419ece41786febe8984bf621179956bbdfbcf80c7`（87,252字节）。
- **材料**：`review/wp42-wp48-wp49-delivery-2026-09-27/boundary-checks.json` `d0eef5f44519273d94662ab9f8b1b334804ba8bdf97039af916dcee99c6eae34`（9,704字节）。
- **登记与停止**：8份backfill-diffs相对闭合快照；reviewer12件补登。manifest499行／主TSV v25 403行 `cddd2914bd41389cc786de8970771e43e84fe87029d48e8f02733cc024103283`（54,775字节）。全量最终重测值由交付消息报告，不自哈希。批末只送WP42／48／49及直接交界后停止；不启动第四包，不创建任务／Agent、不发消息、不提交／推送。限定通过集合保留WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43–WP45、WP59–WP60；运行／Demo／U01–U10及WP78→79→80出口保留。

**第五十一轮（WP42／WP48／WP49首审三项及BATCH-C01有限修订v2，本轮，2026-09-27）**：

- **审查与预检**：本轮REQUEST_CHANGES三必修＋C01。六件必检与self／boundary／主TSV三补检均匹配当前审查快照。旧manifest `a74f4d0ca2d7259dc5fe21630034cf03a0ea02c1a65c193f69b05a27f951eff6`（267,338字节，499条）与主TSV v25 `cddd2914bd41389cc786de8970771e43e84fe87029d48e8f02733cc024103283`（54,775字节，403条）保留；reviewer12件和501项快照不倒写。旧管理回填接受，N01关闭不重开。
- **WP42-R01**：§7.2补普通18／稀有11有序默认表及9＋2窗口权重／区间，过滤保序保重复，DESTINYKNOT第7／9／11位保留；新增E12/E13：等级1／91、第二抽98／99四具体输出，原资格、长度门、首抽、采蜜不改。
- **WP48-R01**：C06及§4.2／self改整数入口，ma121/100、命中121、闪避100、80×121整除100=96；r95命中，96／97失败；旧小数阈值声明仅历史留存，不改WP43正确主规则。
- **WP49-R01与C01**：§5.1／H03按野生敌方当前同侧存活场上计数，双席布局两活拒、一活且其它门过则决定3／真；玩家侧不加人数门。E03以攻击0其它四项＋6形成合法候选，升攻后剩四项固定选防；ICEFACE入场回调不要求switch_in真，L02与IMPOSTER对照。完整级联两上游v2身份。
- **当前固定**：wp42-growth-end-of-round-and-battle-outcomes `6644c777`/41,329、wp48-ability-calculation-modifiers `87e39127`/35,021、wp49-ability-phase-triggers `7a4ecf93`/52,573；矩阵仅F11-06/07、F12-06具名修订为v2待复审；三包与对应子范围ReviewPending＋前向Inventoried。被审v1完整身份见§3。
- **直接自检**：85条场景（31／23／31）；原WP42 29条、WP48未改22条、WP49未改28条向量保持，主要未涉及正文块字节回归保持。263条能力审计行、48族267身份集合不变。17项当前算术记录区分继承与新复核，本轮8源／数据路径定点读取／检索并匹配固定commit；不运行参考计算。
- **材料**：`review/wp42-wp48-wp49-review-2026-09-27/revision-response.md` `5d20434afff2e59ef9b1286272bdf95ef8aed62694ee4684bdddfd25dd6a40d2`（8,707字节）。
- **材料**：`review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md` `e41b85316b620dede8ce1b8c30f61cbbdabee155a069ae34bbce19c5258a1e58`（8,520字节）。
- **材料**：`review/wp42-wp48-wp49-delivery-2026-09-27/self-checks.json` `939f7e366b0c75feb45275e5ee340647715499cde96144b22bb78273925864e3`（102,908字节）。
- **材料**：`review/wp42-wp48-wp49-delivery-2026-09-27/boundary-checks.json` `9509999c8dadeba83dfeceb39fd4d45d7d0b1494e1837abed8f01163792a309b`（14,399字节）。
- **登记与停止**：七份revision-diffs相对本轮快照；旧backfill回应／差异只留首稿历史，旧reviewer不修改。本轮新增20行，manifest519／主TSV v26 423行 `e16fc33168b07694e0791ac96fc81cf367bdd37d9ab70cb6e9a8c9d4f1e9a4b5`（57,528字节）；最终全量身份、链接、JSON、快照保护由交付消息实测报告，清单不自哈希。仅送WP42-R01、WP48-R01、WP49-R01、BATCH-C01及直接传播有限复审后停止；不启动新包、不自批Reviewed、不发消息、不创建Agent、不提交／推送。限定通过集合保留WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43–WP45、WP59–WP60；运行／Demo／U01–U10和WP78→79→80出口保留。

**第五十二轮（WP42／48／49限定Reviewed管理回填与WP46→WP47-A→WP47-B首稿，本轮，2026-09-27）**：

- **独立授权与预检**：三原编号及C01全CLOSED，PASS_SCOPED范围见本轮报告。九件预检逐字节匹配；原manifest `6dfa15eadfa3b40a125741b90192a80b17ae0925e993b7f95a62b8a476ec4631`（279,090字节，519条）、主TSV v26 `e16fc33168b07694e0791ac96fc81cf367bdd37d9ab70cb6e9a8c9d4f1e9a4b5`（57,528字节，423条）留史。reviewer原件和521项输入快照不覆盖。
- **回填**：WP42 A～E成长／主阶段／终局与世界数据，WP48 27族148身份，WP49 21族119身份及直接生命周期，只头尾限定Reviewed及必要完整哈希引用更新。旧已接受主体文字不变；旧摘要v3，旧checks／回应／差异历史保留。矩阵F11-06/07、F12-06具名回填；F12-02/03仅WP42引用语境。
- **新稿**：wp46-damage-multihit-and-healing `0e5a676e`/47,352、wp47-a-move-attributes-targeting-and-calling `ad6a6d6c`/33,207、wp47-b-switching-control-and-item-changes `24185ce4`/37,934；每包附表均独立固定。WP46 A～F139主身份／38场景，WP47-A A～E55／29，WP47-B A～F60／35；新包及F12-04/05只ReviewPending＋前向Inventoried，未增加任务号／第四包。
- **覆盖与默认数据**：8效果文件314身份＋内建挣扎1，本批254主合同、引用旧主规则61（WP43 1／WP44 29／WP45 31），主归属无重叠，非全局全部招式完成。七调用／复制排除并集63、自然之恩67条、三持物类型映射17/17/4；号令排除32、安可6＋6、投掷578项默认威力完整给表。32源／数据文件实测匹配固定commit，实际读取区间与仅数据检索分别记录。26项独立常数运算，没有参考执行／转译模型。
- **交界与新观察**：五组交界包含整招／每击与反应中止、目标／PP／递归记录、C/I/R/P/Belch与换人／能力后置、目录接缝和身份追踪。WP47-B-N01反射撤退射击外层零击数门、N02号令真实槽普通标志，以及BATCH-N03野生拖出读当前替身耐久，全部具名来源／输入／影响，待新批独立review判断，旧WP40／41行为未改，不自动重开旧审批。
- **材料**：`review/wp46-wp47-delivery-2026-09-27/backfill-response.md` `7adff526730ce22e211d33b11849e0914ac035d7699b74f12105d37a26f4bb69`（4,454字节）。
- **材料**：`review/wp46-wp47-delivery-2026-09-27/delivery-summary.md` `85f4df02f5592cca3d91fbbb46aec7d86ea5378f83012661455f04910beb0554`（6,945字节）。
- **材料**：`review/wp46-wp47-delivery-2026-09-27/self-checks.json` `da4c44a0fbd29ce8d656e98a102d331b8a13c0acd6de4b8c62b511b13c59d57b`（203,805字节）。
- **材料**：`review/wp46-wp47-delivery-2026-09-27/boundary-checks.json` `b39ff17c64ab09e136b031968ed44d3cfbaf826d81517103bbbb7b27f215503b`（10,413字节）。
- **登记与停止**：五份backfill-diffs相对本轮快照；reviewer12件补登，新增共27行，当前manifest546条／TSV v27 450条 `db333a8d31fa22d91cbd52e74d3072d0e0c5584d6764fc758293dc2002255648`（61,152字节）。登记后全量哈希／字节／短标签／集合、链接／JSON、快照原件及reference检查由交付消息实测报告，清单不自哈希。只统一送WP46／47-A／47-B及附表与直接交界（含三新观察）后停止；没有新包Reviewed授权。限定通过集合WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP45、WP48–WP49、WP59–WP60，运行／Demo／U01–U10及WP78→79→80保留；未启动WP50或其它第四包，不发消息、不创建任务／Agent、不提交／推送。

**第五十三轮（WP46/47限定Reviewed回填、三观察同步与WP50→WP51→WP52-A首稿；2026-09-27批，2026-09-28收尾）**：

- **授权及输入**：旧三包首审PASS_SCOPED，前批回填接受；独立13件原件不改。14预检＋7级联规格逐字节匹配，旧manifest `bfa66f471e698aa5cffc2690d273c0efca05b8cae6798ced88600b312844d889`（293,017字节，546条）与TSV v27 `db333a8d31fa22d91cbd52e74d3072d0e0c5584d6764fc758293dc2002255648`（61,152字节，450条）留史。548本轮输入快照及既有521项快照受保护。
- **获批语义同步**：N01反射撤退射击外层0击拒换人；N02号令真实槽、specialUsage=false、普通前置通过后扣PP；N03野生伤害拖出读主要效果时当前替身耐久0或绕过，非野生仍拒本击吸收。按报告§3实际写入WP40/41并具名CLOSED；没有扩改其它旧行为。
- **C01／回填**：WP46区间拆开、鸟嘴加热HP提交后每击反应、神秘守护WP45建立期限与WP44免疫查询；139/55/60主身份及旧61分布1/29/31保持。旧三主三附表限定Reviewed，原被审六件身份留史。14实际改动旧规格＋矩阵＋旧摘要/self/boundary共18份diff；配套v2保留v1上下文。
- **新三包**：wp50-held-item-triggers-and-consumption `937551e0`/29,336、wp51-ai-action-selection-and-skill `1174d485`/25,064、wp52-a-generic-numerical-and-status-evaluation `f7f400c6`/46,332，每包一附表；WP50 A～F持物计算触发与消费32族196身份、28场景；WP51 A～E决策/技能/资源/权重、23场景；WP52-A A～F通用失败/数值/状态阶级与类型能力评估、50场景。101场景、21独立常数算术均非参考执行；新包只ReviewPending。
- **覆盖与边界**：全Scripts AI字面注册784语句、786出现／783键，A334、WP51已有15、B247、C190；3重复键明列后续B/C责任，未强行报0重复。267能力评级完整默认表。38源身份与commit blob实测一致、阅读／索引范围分列；完整B/C未启动。真实整数命中96与阈值失败保留，负会心级／同速反序／负请求／评级方向等只作新AI快照差异，不回写真规则。
- **交界**：五组覆盖物品有效性/消费/持久状态、物品计算及能力时序、AI控制与选择资源、AI预测与真实合同和B/C接缝、版本历史状态追踪；26条新主稿上游完整绑定。F08-05分旧Reviewed与新WP50；F12-07 WP51、F12-08仅WP52-A ReviewPending，前向Inventoried。
- **材料**：`review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-response.md` `860bc758987f3ca772ef445fa3051e939aaddd23f76afa6b06275ae85d8f8e05`（7,731字节）。
- **材料**：`review/wp50-wp51-wp52a-delivery-2026-09-27/delivery-summary.md` `0df9331d437df132728bc58cb36af53d16d09c4f787e99445db3de56c483029b`（6,554字节）。
- **材料**：`review/wp50-wp51-wp52a-delivery-2026-09-27/self-checks.json` `5faccf42e26c67da07e0d844cc03a0d4c9120246e6823f7bab438691361279fc`（364,926字节）。
- **材料**：`review/wp50-wp51-wp52a-delivery-2026-09-27/boundary-checks.json` `f5eb0aca474da0ba48adb816b8289b3b4a8e4e5966fe4dbcd18b8a3e69fc914d`（14,164字节）。
- **登记与停止**：新增41行＝reviewer13＋新稿附表6＋交付顶层4＋diff18；manifest587／TSV v28 491条 `986477f175f2dc3db9303b456ba0379c0de81a1b95ae5bb37d4388812fe415f8`（67,071字节）。登记后全量哈希/字节/短标签/集合、链接/JSON、18diff重建、快照与原件保护、reference只读状态实测由交付消息报告；不自哈希。只送WP50/WP51/WP52-A及五组直接交界后停止；WP52-B/C、其它第四包、WP22/23/32/37/38及Demo/宿主/媒体/插件/U01–U10、WP78→79→80不启动，不创建任务/Agent、不发reviewer消息、不提交/推送。

**第五十四轮（WP50-R01／WP52-A-R01有限修订、BATCH-C01及WP51限定Reviewed回填；2026-09-28）**：

- **独立范围／预检**：REQUEST_CHANGES仅两必修，WP51 A～E PASS_SCOPED；旧三观察/C01/WP46/47回填接受，不重开。九必检＋三配套共12件逐字节匹配。被审manifest `34308ae1293a9ac7a272b8e93ef7e82999e7aa3a15b53a2d50ab7b6b6404de50`（315,913字节，587条）、TSV v28 `986477f175f2dc3db9303b456ba0379c0de81a1b95ae5bb37d4388812fe415f8`（67,071字节，491条）留史；本轮589项输入及旧548/521快照、reviewer14件均保护。
- **WP50-R01**：低HP参数false使半血不要求有效贪吃，true才要求；可食果/普通有效性/各消费者资格保留。ORAN26→36、50→60、51不触发；SITRUS半血→75；混乱果世代6半血→62，世代8无贪吃拒/有效贪吃→83。§4/V05替换旧相反句、V29–V33新增；恢复量/RIPEN/Nature/forced/消费链、WP28/51主动入口不改。
- **WP52-A-R01**：三墙按目标当前同侧存活场上人数，排倒下/空位/后备、不按名义布局；N09–N11固定双席、中等、无会心/其它倍率、普通单目标、墙前37，人数2得25/人数1得19。保留绕墙/类别/极光幕优先，WP43/49及负会心/整数96等已支持内容不改。
- **C01／WP51回填**：后备可伤为存在后备/招/至少一对手未被吸收的组合；天气到期重估明确CLOUDNINE/AIRLOCK并另列UTILITYUMBRELLA。S06/S07局部对照；WP51主稿/附表与F12-07限定Reviewed，C01维护与管理状态分列；主动道具数值和默认数据不改。WP50/52-A及其子范围继续ReviewPending，WP52-B/C仍Inventoried未启动。
- **当前规格**：`specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md` `fcbbca67dafbb1aaa1cfd2560983a6f34830c31c11feccb7688f08b372a395b1`（31,648字节）；有限修订v2，待复审。
- **当前规格**：`specs/combat/wp51-ai-decision-defaults.md` `5069a3690c6886204ebe9877ff0165e77c4c437fb8273032ac9d6f52bf89c2d0`（5,472字节）；WP51限定Reviewed回填后字节。
- **当前规格**：`specs/combat/wp51-ai-action-selection-and-skill.md` `baebd58a7f4eed635f685f583fa7b4d21785a9ac13a0a1ee4c2ccd6ec7b6bac5`（26,784字节）；WP51限定Reviewed回填后字节。
- **当前规格**：`specs/combat/wp52-a-evaluation-coverage-and-data.md` `a5a13acaf8572fa621b91911430b2286b23340618c72d4b5d2e1522aaf4ec5f9`（58,772字节）；有限修订v2，待复审。
- **当前规格**：`specs/combat/wp52-a-generic-numerical-and-status-evaluation.md` `6c0534fea6d4a18284c1e54a38e413ad010d38291088b0df45d8ac087ca44c9c`（48,127字节）；有限修订v2，待复审。
- **继承／验收**：WP50覆盖附表v1字节未变，32族196身份不变；AI注册A334/B247/C190/已有WP51 15、三前向重复键与267能力评级不变。原101场景仅V05改错，新增10条，当前33/25/53共111；独立常数21＋7＝28。self/boundary/摘要v2保留历史上下文；26条活动上游绑定按实际身份级联。
- **材料**：`review/wp50-wp51-wp52a-review-2026-09-28/revision-response.md` `47dfc20d1d1fe50fc582856b9a6ad83ec9fb3e39dc6f74bcaf7cfdb6b88e95eb`（7,997字节）。
- **材料**：`review/wp50-wp51-wp52a-delivery-2026-09-27/delivery-summary.md` `7f2207b4267758a9483bd7042554116192c669061663a07c5178c3ec63c66748`（9,407字节）。
- **材料**：`review/wp50-wp51-wp52a-delivery-2026-09-27/self-checks.json` `0960427cb4ce0f2044604a15b1754dc310f47162d1e16ad67999dd753ad4111d`（416,764字节）。
- **材料**：`review/wp50-wp51-wp52a-delivery-2026-09-27/boundary-checks.json` `82c7c95c75abd44d48213cc470b16ca62c21123eb332d09b36905aeae6b1be90`（31,428字节）。
- **登记／停止**：9份修订diff＝5规格＋矩阵＋摘要/self/boundary，相对本轮input-snapshot；原18份回填diff保留并仅校验到被审v1快照。reviewer14＋回应1＋diff9新增24行，manifest611／主TSV v29 515条 `e0f2a3f0d99828355d10ca7a9e385ed707c5d9a2ef6d9a26d0b637ba866b7a55`（70,456字节），旧行/历史链保留。登记后全量身份/字节/短标签/缺失重复/集合、链接/JSON/绑定、diff重建、快照原件与reference只读状态实测由交付消息报告；manifest不自哈希、TSV不收自身。仅两原编号及C01/WP51管理回填和直接传播送有限复审后停止；不启动WP52-B/C或下一批、不创建任务/Agent、不发reviewer消息、不提交推送。限定通过集合在原WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP49（WP47为A/B）、WP59–WP60上仅加WP51；运行/Demo/宿主/U01–U10和WP78→79→80继续保留。

**第五十五轮（WP50/52-A限定Reviewed回填与WP52-B→WP52-C→WP54首稿；2026-09-28）**：

- **授权／固定**：两R和C01独立CLOSED，WP51回填接受。12件预检逐字节匹配；旧manifest `a1e818788aa7a55dbceb832271b622e836aa768769de67198dc5ebb31fdded13`（331,077字节，611条）及TSV v29 `e0f2a3f0d99828355d10ca7a9e385ed707c5d9a2ef6d9a26d0b637ba866b7a55`（70,456字节，515条）留史，613当前输入及旧589/548/521快照和reviewer原件保护。
- **回填**：WP50 A～F32族196身份与核心接点、WP52-A A～F164效果334登记/22共用修正与具名数据主附表限定Reviewed；WP51原范围不扩。只头尾状态/完整身份及V29–V33/S06–S07表格连接，旧111场景输入期望不变，既有果实/三墙/两C01行为不重写。旧摘要/self/boundary v3保留v2被审语境；9份diff相对本轮快照，旧修订材料不覆盖。
- **新三包**：wp52-b-field-damage-healing-and-target-evaluation `b41c2773`/42,914、wp52-c-items-calling-and-control-evaluation `542e7b01`/39,343、wp54-entry-eligibility-level-adjustment-and-clauses `3ef7ae5a`/32,322及各自附表，均ReviewPending。B具体基数/多击/跨回合/恢复自损/场域保护/多目标；C物品V/E/操作调用/拘束原命令/PP/浮空变身；WP54四资格层/默认组合/等级经验还原/条款。60/55/42共157静态场景、31常数；不等于动态执行。
- **目录／数据**：B由247加23数值/恢复/誓约出现得270，C190减23为167，A334与WP51 15不变。784 add/copy语句展开786出现/783不同键，静态解析782有效直接键；另2个addIf组57物品身份合839有效可定位入口。三重复键中连续切割真覆盖、解除保护/撤退射击copy缺本族源保留旧行为；写生另一个缺源copy未建新整体键。C基础物品评级215；WP54十活动工厂/五直接样本/三模式、56审计身份与14条款键；禁用注释样例不计默认。42源/数据路径与commit blob实测一致，实际正文/仅定位范围分列。
- **新观察／交界**：WP54-N01指出条款重开OHKO后冰子类可能复用父级保存的目标门，旧拒冰摘要与AI预测存在直接交界差异；稳定来源/具名输入/最小建议单列待独立判断，旧WP46未改。五组交界覆盖B预测与真数值阶段、C价值/资源/写入原行动、A/B/C/51注册条件组、WP54资格/调整/条款与调用者、状态历史与未决。35条新主稿上游绑定；C对B尚未外审。
- **材料**：`review/wp52b-wp52c-wp54-delivery-2026-09-28/backfill-response.md` `1331835f952041f5396ec2ee12ece709fe768c7b133fcb6aee14edf408930a8d`（4,511字节）。
- **材料**：`review/wp52b-wp52c-wp54-delivery-2026-09-28/delivery-summary.md` `23724461c38c7270cd12cbef4e5aada25f8463f466cd437bfa0c76aa267dc1c4`（5,982字节）。
- **材料**：`review/wp52b-wp52c-wp54-delivery-2026-09-28/self-checks.json` `3ab93186bc086874fd5de406876ef815364f86d4e150704953d2c5f809484c26`（1,063,788字节）。
- **材料**：`review/wp52b-wp52c-wp54-delivery-2026-09-28/boundary-checks.json` `c48ef0c0a365dd13897c15d5ca40eacf15720c687655273e8b94fe59423e5794`（16,020字节）。
- **登记／停止**：新增31行（reviewer12/新稿附表6/顶层4/diff9），manifest642／主TSV v30 546条 `7e8467f5d58101757ff7c29c6ec8d9a2ca2f1381a8135b498b677930f7df7963`（74,801字节），原行和历史链保留，manifest不自哈希/TSV不收自身。登记后全量身份/字节/短标签/集合/缺失重复、链接/JSON/绑定、diff重建、快照原件/reference实测由交付消息报告。只送WP52-B/C/WP54及直接交界含N01后停止；不启动WP55或第四包，不创建任务/Agent、不发reviewer消息、不提交推送。限定通过集合WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP51（WP47为A/B）、WP52-A、WP59–WP60；运行/Demo/宿主/媒体/插件/U01–U10与WP78→79→80保留。

**第五十六轮（WP52-B-R01有限修订、WP54-N01同步、BATCH-C01维护与C／WP54限定回填；2026-09-28）**：

- **授权／预检**：独立报告 `b7e5e47bc99da6a3965ca2885b80f5e654cefc79d4ff641fb3586c7d18284ddd`（14,417字节）与执行提示 `da43a392e29207dcffca089ff1a6587d76ff3881eb02285cea27aa2003383c9a`（10,379字节）；WP52-B REQUEST_CHANGES仅R01，C／WP54各PASS_SCOPED，N01 CONFIRMED，C01非阻塞。15项关键对象预检逐字节匹配；644项输入、旧613／589／548／521快照与reviewer原件保护。
- **R01**：B主稿§2压榨PP行与§8 B04族分入口（普通候选跳过／触达处理器PP0缺失查询先失败／PP1、2、−1保留）；60→62场景；`b41c2773`/42,914 → `8036a674`/44,557；B附表未改；继续ReviewPending。
- **N01**：WP46 §4 OHKOIce分“原定义／条款加载后”入口并补来源；`aa9a7f1e`/47,646 → `0f7c9b4b`/48,872；AI拒冰门与WP43公式保留；WP54 §6／Q41、附表尾注、矩阵同步。
- **C01**：A主稿与附表前向定位历史化（B247／C190、未启动→A阶段定位）；`5cdc3edf`/48,733→`9c74d50c`/49,622、`fa760fac`/59,366→`7bce736d`/60,674；行为与场景未改。
- **回填**：C主附表限定Reviewed（`542e7b01`/39,343→`290bee81`/40,332；`9e8d3030`/37,701→`f83205ee`/38,390）；WP54主附表同理（`3ef7ae5a`/32,322→`2a1518c3`/33,809；`b45c976e`/11,746→`0ec50236`/12,381）；C对B引用=R01修订稿待复审；矩阵F12-08/F13-03回填为C/54具名Reviewed、B仅R01待复审。
- **级联／材料**：WP47-A `e4934943`/34,014、WP47-B `00769901`/39,000、WP50 `f0b6b147`/32,490、WP51 `2b0847b5`/27,645仅更新引用；`revision-response.md` `0b179892`（12,855字节）；revision-diffs 16份；旧backfill-response与9份backfill-diffs、旧摘要v1留史。
- **登记／停止**：新增33行（reviewer16／回应1／diff16）；manifest675／主TSV v31 579条 `e91e849cbd56f88fcb0792521e17eb9382669fa5911a9a2066e511df9e37f64f`（79,741字节），原642/546行保留；限定通过集合新增WP52-C、WP54，WP52-B未通过不写连续完成；只送有限短复审后停止，不启动WP55。

**第五十七轮（WP52-B限定Reviewed回填、BATCH-C02与WP55→WP56→WP57首稿；2026-09-28）**：

- **授权／预检**：独立有限复审报告 `35d382cd11f7f5334317ee10a88fdf53f3bfe2c0d05453ae39f3079ab583b5ec`（12,290字节）与执行提示 `0e49b872ba414cb321152d449a70610a51da0ad83ca99ec0c5cd31890e7fbf74`（15,809字节）：PASS_SCOPED，R01／N01实际同步／C01全CLOSED、C／WP54回填接受；677项固定输入与旧快照/reviewer原件保护。
- **回填**：WP52-B主/附表头尾限定Reviewed（B主 `8036a674`/44,557→`73fa6ffa`/45,342；B附表 `d2ccf48f`/57,193→`723838f2`/57,979）；A主 `388b5fce`/50,104、A附表 `91ab040d`/61,156、C主 `658b40bc`/40,722随B状态同步与引用重固定；矩阵F12-08四包具名Reviewed。
- **C02**：旧self `3a05f9e0`/1,069,184、boundary `9e693b2c`/20,318、summary `6ec4fe6f`/9,057；artifacts六项按磁盘重固定、Q41尾句同步；9份backfill-diff相对本轮快照重建9/9。
- **新三包**：wp55-facility-session-and-restoration `d5ee5ba7`/21,873（挑战身份/会话状态机/对手抽取表/内容表和个体创建/保存点/异常边界，25场景）；wp56-palace-and-arena-variants `fde119ea`/16,917（Palace两表与自动选招、AI换人；Arena成功机/心技体/三回合评判/顺序补位，22场景）；wp57-factory-rentals-and-swaps `e510f840`/11,933（候选生成/租借/交换/隔离与容量，15场景）。均ReviewPending；批内互引注明“批内固定版本，尚未外审”。
- **交界／矩阵**：五组交界与13条绑定见 `review/wp55-wp57-delivery-2026-09-28/boundary-checks.json`；F13-04/F13-05标ReviewPending子范围，F13-03已审范围未扩为整个设施通过。
- **材料**：`review/wp55-wp57-delivery-2026-09-28/`backfill-response.md` `2aa102f2c42004b00f64d54974c50fc639e276e5c23d43cf8eeffca1f13309ca`（6,006字节）；本批摘要 `6217eeb05793b2b0a6620a1bb06b30ad5d51cc24e59d74c6f43c0e1b18568bad`（4,970字节）；self `72396ffb1676cce44cb43dab3ec9f0ec8a8c36cd939febde402e08ca834d3d30`（17,131字节）；boundary `5839c099ef7fe3ee675f9b880a853c6fb043e52acb8b4baaa07c0186b07ebcd8`（7,571字节）。
- **登记／停止**：新增30行（reviewer14／回填回应1／backfill-diff9／三包3／批材料3）；manifest705／主TSV v32 609条 `edcc4b54979e635f95a70324d5b501a03a03bc865441acab120878c2ad26274f`（83,890字节），原675/579行保留。只送三新包、回填/C02与直接交界统一外审后停止；不启动WP58或第四包。

**第五十八轮（WP55／WP56／WP57首审REQUEST_CHANGES修订、C01记法与继承C02剩余；2026-09-29）**：

- **授权／预检**：独立首审报告 `1e3d4314e0d4d2d6b6d8b3a83cd3b4d2ed80540b0bc5072268a6a7a5a5ad4531`（20,977字节）与修订提示 `e5f787e4944979843d860259e15b9988d7739f283a055be2ec33df04abcc9244`（11,926字节）：REQUEST_CHANGES共13项（WP55×5、WP56×5、WP57×3）；WP52-B限定Reviewed回填接受、旧R01／N01／C01不重开；9项固定对象逐字节匹配，707项输入与旧677／644／613／589／548／521快照、reviewer16件原件保护。
- **WP55**：R01～R05修订（会话决定／单场返回分层与保存门；空报名与未开始结束；保存返回假与未捕获异常分层；data查询先失败；零长度抽样与短名单）；`d5ee5ba7`/21,873→`0bcff15b`/27,698（34场景）；另按WP57-R01同步§2.5属主概括；继续ReviewPending。
- **WP56**：R01～R05修订（实际抽样门A与2A＋D并重算61/129、22/64、90/185；压半生命周期；AI换人早返标记；技分覆盖与时点；评判2／0与三具名心分）；`fde119ea`/16,917→`8ed7940b`/21,274（27场景）；WP55引用重固定为批内修订稿。
- **WP57**：R01～R03修订（Factory默认拥有者id0/空名/gender2/language2；取消仍提交队伍与首屏退出确认；含端点越界在创建处失败）；`e510f840`/11,933→`7e69ccdc`/14,776（17场景）。
- **矩阵／C01／C02**：F13-04/F13-05 → “首审REQUEST_CHANGES，按原编号修订后再送”（`0a726a5f`/51,444→`b97ed883`/51,500）；C01三处记法（WP55 W19“抽到”、WP56压半阈值方向、回填回应14件）；继承C02剩余闭合（旧self v4 `b776328d`/1,070,038、旧摘要v4 `4ba4ed58`/9,587、批boundary v2 `8c2033a7`/8,670、批self v2 `36704503`/20,320、批摘要v2 `0fcab05d`/6,514、回填回应维护版 `835459a7`/6,661）。
- **材料／登记**：`review/wp55-wp57-review-2026-09-28/revision-response.md` `0da546c0a7451250bbe08963f937b95e4d405a0ebcac783ea764e142c97d7f93`（21,627字节）；revision-diffs 10份相对本轮input-snapshot（重建10/10）；reviewer16件补登。新增27行；manifest §1共732条／主TSV v33 636条 `0f8113065947f4b94c3ed8cf8d0ea9db8ef53160b7d1728fce7abe56028c2333`（87,544字节），原705/609行保留，manifest不自哈希/TSV不收自身。
- **登记后校验／停止**：全量身份/字节/短标签/集合/缺失重复、链接/JSON/绑定、diff重建、快照原件/reference实测由交付报告；只送原13编号、C01／继承C02及直接传播作有限复审后停止，不启动WP58或其它包、不重做首审、不创建任务/Agent、不发reviewer消息、不提交推送。
