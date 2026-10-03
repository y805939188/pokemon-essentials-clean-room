# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-27 WP59／WP36／WP60 v2 复审收尾（v3）后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md`（WP59／WP36／WP60 v2 复审收尾（v3）后；六行状态同步） | `1de3852f` | `1de3852f489b25b9649492e4ea2e54b5ecda967cdb8b5fb40392fb3de5c82d1e` | 44,896 |
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
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv`（v19 重测，WP59／WP36／WP60 v2 复审收尾（v3）材料后；266 行） | `d2e72991` | `d2e72991a07d41b8637a47e064291e30398ceafdc79c29dfedbb1017bb18e8ac` | 36,452 |
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
| `specs/pokemon-rules/wp34-inheritance-and-offspring.md`（WP34 闭合复审回填 Reviewed（限定静态范围，管理性）；被审 v3 `d0113d76` 保留历史） | `8e3511d3` | `8e3511d338fc0952bb618f37d514fc093691131e9ed0587b2996e2a2df541136` | 30,758 |
| `specs/creature-rpg/wp35-eggs-and-hatching.md`（WP35 v2 复审回填 Reviewed（限定静态范围，管理性）；被审 v2 `0abe2622` 保留历史；引用 WP34 回填后哈希；WP59 轮 BATCH-C02 头部引用同步） | `1fbfd98e` | `1fbfd98e7a1da4d6bb71c026a6a8740e62dae163501db1df7cfed5d2fc42ad45` | 24,610 |
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
| `specs/overworld/wp59-world-time-weather-field-moves.md`（WP59 v2 复审收尾稿（v3）；被审 v2 `440a67b1` 保留历史；尚未外审） | `9a41d185` | `9a41d185fd77de187ceb3ca81be2425ba7a2cbc79407fbcdb99ec8b611733e59` | 42,041 |
| `specs/creature-rpg/wp36-wild-encounters-and-modifiers.md`（WP36 v2 复审收尾稿（v3）；被审 v2 `3120d1e1` 保留历史；引用 WP59 v3 哈希；尚未外审） | `d21edcc7` | `d21edcc7d94091758279c8bbdbee4b1a5b2abfbd158b984ae90c134a33e649ae` | 33,424 |
| `specs/pokemon-rules/wp60-berry-plants.md`（WP60 树果 v2 复审收尾稿（v3）；被审 v2 `e468c3bf` 保留历史；引用 WP59/WP36 v3 哈希；尚未外审） | `114c432b` | `114c432b51682763a38228bda930c1109e4f4ff2c34b2a87a797a887bc3180e1` | 24,912 |
| `specs/overworld/wp60-fishing.md`（WP60 钓鱼 v2 复审收尾稿（v3）；被审 v2 `f280e9a7` 保留历史；引用 WP59/WP36 v3 哈希；含 WP36-R02 传播；尚未外审） | `5f274a2c` | `5f274a2cd767cf5f057d5ac05bcd178faf2d9e80634bf30278e51619d4847040` | 20,759 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/backfill-response.md` | `8ab43cb9` | `8ab43cb90b0ea042e5d62b0d2dd89a0758d132ec39b507cb61299c3fe6ebe1d5` | 3,778 |
| `review/wp59-wp36-wp60-delivery-2026-09-27/delivery-summary.md`（本批交付摘要 v3；v2 复审收尾轮） | `809e0fa0` | `809e0fa0a01590dd22f83e2400e82a304f0ce8225055f52a04bf1f75a349d209` | 12,097 |
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

### 2.2 历史版本关系（据本地记录重建，证据受限）

- 2026-09-19 14:18:53 四份总控文档定稿；约 14:38 首次计算哈希并写入清单（历史条目见第 3 节）。
- 2026-09-19 14:39:03，overview 与 module-map 在本地被进一步修订（内容增大、行数不变），送审附件为 14:39 版，清单未同步，造成联合 review 实测值与清单记录不一致（联合 review R01）。
- **证据限制**：14:39 的修改时刻来自本地文件 mtime；变更范围（补核 E04 训练家引用、E11 HTTP 工具、E21 参战/布局，细化总览 §3 与 module-map D01/D11 行）是本地模型比对当前版本与此前阅读记录后重建的说明。**没有该次修改的操作日志或旧版全文**；14:39 之前的两版内容（`0421575b` / `0e22b7f2`）在本地已被覆盖、无留存副本，无法提供逐行 diff。不补造旧版本或历史日志。

## 3. 历史条目（已被替代，仅供追溯）

| 文件 | 旧 SHA-256（前 8 位） | 记录时点 | 替代关系 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `0421575b` | 2026-09-19 约 14:38 | 被 14:39 修订版 `1ca34f44` 替代 |
| `planning/module-map.md` | `0e22b7f2` | 2026-09-19 约 14:38 | 被 14:39 修订版 `32eab70d` 替代 |
| `planning/feature-matrix.md` | `2f4e3e31` → … → `6b49c40b` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联、WP03 回填+WP04–WP07 追踪、批次复审关联、三包回填、WP06 回填+WP08–WP10 追踪、批次复审关联、WP09 回填修订、WP08/WP10 回填与 WP11–WP13 追踪修订、WP11–WP13 复审修订（v2 状态与移动路线附表登记）、v2 复审修订（v3 状态与关闭项登记）、WP11/WP12 Reviewed 回填与 WP13 v4 状态同步、WP13 Reviewed 回填、WP14–WP16 批次追踪修订、WP14–WP16 首轮复审修订（v2 状态登记）、WP14–WP16 回归复审修订（v3 状态与 WP16-R02 关闭登记）、WP14–WP16 Reviewed 回填、WP17 批次追踪修订、WP17 首轮复审修订（v2 状态与绘制附表登记）、WP17 回归复审修订（v3 状态与 R02～R05/C01 关闭登记）、WP17 Reviewed 回填（F05-05/F05-06）、WP18–WP20 批次追踪增量（八个 Feature）、WP18–WP20 首轮复审修订（八行状态措辞与还原记录措辞同步）、WP18–WP20 定点复审回填（F06-05/F06-06/F08-05 → Reviewed；WP18/WP19 行更新）、WP18/WP19 回填（F06-01/F06-02/F07-01、F06-03/F06-04 → Reviewed）、WP21–WP25 批次追踪增量（五个 Feature）、WP21–WP25 首轮复审修订（五行状态措辞）；2026-09-26 经定点复审回填（F07-02～F07-05 → Reviewed＋前向 Inventoried；F06-07 措辞更新）被 `e0762970` 替代；2026-09-26 再经闭合回填（F06-07 → Reviewed（WP21 子范围）＋前向 Inventoried）被 `8b83d668` 替代；2026-09-26 再经批次增量（六个 Feature → ReviewPending＋各自范围）被 `af8328ee` 替代；2026-09-26 再经首审修订（六行版本说明）被 `c4505715` 替代；2026-09-26 再经 v2 复审收尾（六行"仅剩具名项"）被 `6b49c40b` 替代；2026-09-26 再经 WP26–WP30 闭合回填（六行 → Reviewed（对应子范围））与 WP31→WP28→WP29 批次增量（F09-03、F08-03/F08-04、F08-06 → ReviewPending（批内固定、尚未外审））被 `cbf671a8` 替代；2026-09-27 再经首审修订（四行 → "首审已送审：REQUEST_CHANGES，修订后再送"）被 `a05c39f4` 替代；2026-09-27 再经有限复审回填与余量行同步（F09-03 → Reviewed（WP31 子范围）＋前向 Inventoried；余量行"仅剩三点已修订"）被 `909080cb` 替代；2026-09-27 再经 WP28／WP29 回填（F08-03/F08-04、F08-06 → Reviewed（对应子范围）＋前向 Inventoried）与 WP33→WP34→WP35 批次增量（F09-05/F09-06/F09-07 → ReviewPending（批内固定、尚未外审）＋前向 Inventoried）被 `77c3bff0` 替代；2026-09-27 再经 WP33／WP34／WP35 首审修订（F09-05/F09-06/F09-07 → "首审已送审：REQUEST_CHANGES（已修订（v2），待复审）"）被 `243df4e4` 替代；2026-09-27 再经 WP33／WP35 回填与 WP34-R03 收尾（F09-05/F09-07 → Reviewed（对应子范围）＋前向 Inventoried；F09-06 → "v2 复审仅剩 WP34-R03 末次缓存（v3 已修订、待短复审）"）被 `17fa287c` 替代；2026-09-27 再经 WP34 回填（F09-06 → Reviewed（对应子范围））与 WP59→WP36→WP60 批次增量（F10-01/F10-02、F14-01～F14-04 → ReviewPending（各自范围，批内固定、尚未外审）＋前向 Inventoried）被 `64d297de` 替代；2026-09-27 再经首审修订（WP59／WP36／WP60 六行 → "首审 REQUEST_CHANGES，已修订为 v2、待复审"）被 `b580eb92` 替代；2026-09-27 再经 v2 复审收尾（六行 → "9/13 关闭＋四项已收尾修订为 v3、待复审"）被 `1de3852f` 替代（当前有效） |
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
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` | `57025ecc` | 2026-09-26 首次送审 | 经 v2 重测被 `cdb89a96` 替代（v2）；经 v3 重测被 `ef231e80` 替代（v3）；经 v4 初测被 `1c515390` 替代；同轮二次重测（WP24/WP25 修正后）被 `a5a2ded7` 替代（v4）；经 v5 重测（WP21–WP25 修订材料后）被 `7db3b12b` 替代（v5）；经 v6 重测（定点复审修订与回填材料后）被 `4c66bcb4` 替代（v6）；经 v7 重测（闭合回填材料后）被 `679338ea` 替代（v7）；经 v8 重测（WP26–WP30 批次材料后）被 `08ced51b` 替代（v8）；经 v9 重测（首审修订（v2）材料后）被 `ec86e13d` 替代（v9）；经 v10 重测（v2 复审收尾（v3）材料后）被 `35cd3605` 替代（v10）；经 v11 重测（闭合回填与 WP31→WP28→WP29 批次材料后）被 `a7149e31` 替代（v11）；经 v12 重测（WP31／WP28／WP29 首审修订（v2）材料后）被 `0c811f2d` 替代（v12）；经 v13 重测（WP31 回填与 WP28／WP29 三点收尾材料后）被 `ef046028` 替代（v13）；经 v14 重测（WP28／WP29 回填与 WP33→WP34→WP35 批次材料后）被 `7368bba6` 替代（v14）；经 v15 重测（WP33／WP34／WP35 首审修订（v2）材料后）被 `44da94e7` 替代（v15）；经 v16 重测（WP33／WP35 回填与 WP34-R03 收尾（v3）材料后）被 `a756e2ee` 替代（v16）；经 v17 重测（WP34 回填与 WP59→WP36→WP60 批次材料后）被 `aec34bd2` 替代（v17）；经 v18 重测（WP59／WP36／WP60 首审修订（v2）材料后）被 `a8eb500f` 替代（v18）；经 v19 重测（WP59／WP36／WP60 v2 复审收尾（v3）材料后）被 `d2e72991` 替代（当前有效，v19） |
| `review/wp21-wp25-delivery-2026-09-26/delivery-summary.md` | `a046f5f5` | 2026-09-26 首版 | 同轮随 WP24/WP25 修正重测被 `d29d177a` 替代（v1 定稿）；经首轮复审 v2 同步被 `c88e1e5b` 替代（v2）；经定点复审 v3 同步（回填＋R03）被 `62d8a2c8` 替代（v3）；经闭合回填 v4 同步被 `8d8b7e5d` 替代（当前有效，v4） |
| `review/wp26-wp27-wp30-delivery-2026-09-26/delivery-summary.md` | `9c713161` | 2026-09-26 首版 | WP26–WP30 批次首发固定（v1 首版，被审）；经首审 v2 同步被 `dd06a4bd` 替代（v2，被审）；经 v2 复审 v3 收尾同步被 `df4926ae` 替代（v3）；经闭合回填 v4 注记被 `bdd353fd` 替代（当前有效，v4） |
| `specs/pokemon-rules/wp31-basic-evolution.md` | 无中间版本 | 2026-09-26 首版 | WP31→WP28→WP29 批次首发固定为 `e5658f31`（35,631 字节）；批末交界核对修正对 WP18 的引用（§4.1→§3.4）后重固定为 `b5966bbf`（35,629 字节，被审首版）；经首审 REQUEST_CHANGES（WP31-R01/R02＋BATCH-C01）修订被 `e541c650` 替代（v2，被审版）；经 2026-09-27 有限复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `ee47f124` 替代（管理性回填；被审 v2 `e541c650` 保留历史）；经 WP28/WP29 回填后引用同步（管理性）被 `0b40917c` 替代（当前有效） |
| `specs/creature-rpg/wp28-item-use-and-training.md` | 无中间版本 | 2026-09-26 首版 | 批次内自检修正后固定为 `4abaf6f9`（32,848 字节）；批末交界级联重固定为 `f9cd5fe3`（32,848 字节，被审首版）；经首审 REQUEST_CHANGES（WP28-R01～R06＋BATCH-C02）修订与 WP31 引用级联被 `f2f7618c` 替代（v2，被审版）；经有限复审（7 项关闭、剩 R03/R06）收尾修订与 WP31 回填后引用同步被 `7e10cb25` 替代（v3；被审 v2 `f2f7618c` 保留历史）；经 2026-09-27 闭合复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `a4ccb383` 替代（当前有效，管理性回填；被审 v3 `7e10cb25` 保留历史） |
| `specs/creature-rpg/wp29-shops-and-exchanges.md` | 无中间版本 | 2026-09-26 首版 | 批次首发固定为 `3705047f`（21,918 字节，被审首版；含自检修正后的当前值）；经首审 REQUEST_CHANGES（WP29-R01/R02＋BATCH-C02）修订被 `d5c847f1` 替代（v2，被审版）；经有限复审（7 项关闭、剩 R02）收尾修订被 `1ed4b957` 替代（v3；被审 v2 `d5c847f1` 保留历史）；经 2026-09-27 闭合复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `f7788c7d` 替代（当前有效，管理性回填；被审 v3 `1ed4b957` 保留历史） |
| `review/wp31-wp28-wp29-delivery-2026-09-26/delivery-summary.md` | `3f832427` | 2026-09-26 首版 | 批次首发固定为 `3f832427`（8,403 字节）；经首审修订注记（v2）被 `023c090e` 替代（v2）；经有限复审注记（v3）被 `6b22ac03` 替代（v3）；经闭合回填 v4 注记被 `990f30b4` 替代（当前有效，v4） |
| `specs/creature-rpg/wp33-daycare-and-breeding-session.md` | 无中间版本 | 2026-09-27 首版 | WP33→WP34→WP35 批次首发固定为 `4e17c679`（21,180 字节，被审首版、保留历史）；经 2026-09-27 首审 REQUEST_CHANGES（WP33-R01/R02＋BATCH-C01/C02）修订被 `6cb65468` 替代（v2 修订稿，被审版）；经 2026-09-27 v2 复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `8c678e33` 替代（当前有效，管理性回填；被审 v2 `6cb65468` 保留历史） |
| `specs/pokemon-rules/wp34-inheritance-and-offspring.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `bb950920`（24,359 字节，被审首版、保留历史）；经首审 REQUEST_CHANGES（WP34-R01～R03）修订被 `7ba35a9d` 替代（v2 修订稿，被审版）；经 2026-09-27 v2 复审 R03 收尾（末次普通异色缓存时点）修订被 `d0113d76` 替代（v3；引用 WP33 回填后哈希 `8c678e33`）；经 2026-09-27 闭合复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `8e3511d3` 替代（当前有效，管理性回填；被审 v3 `d0113d76` 保留历史） |
| `specs/creature-rpg/wp35-eggs-and-hatching.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `61a6bdb9`（19,715 字节，被审首版、保留历史）；经首审 REQUEST_CHANGES（WP35-R01～R03）修订被 `0abe2622` 替代（v2 修订稿，被审版）；经 2026-09-27 v2 复审 PASS_SCOPED 后回填 **Reviewed（限定静态范围）** 被 `315e74f6` 替代（管理性回填；被审 v2 `0abe2622` 保留历史）；经 WP34 回填后引用同步（管理性）被 `34e83236` 替代；经 WP59 轮 BATCH-C02 头部引用同步（管理性）被 `1fbfd98e` 替代（当前有效） |
| `review/wp33-wp35-delivery-2026-09-27/delivery-summary.md` | `8c420fa7` | 2026-09-27 首版 | 批次首发固定为 `8c420fa7`（7,573 字节）；经首审修订注记（v2）被 `462ee890` 替代（v2）；经 v2 复审收尾注记（v3）被 `28cbc965` 替代（v3）；经闭合复审收尾注记（v4）被 `6b1d9a1a` 替代（当前有效，v4） |
| `specs/overworld/wp59-world-time-weather-field-moves.md` | 无中间版本 | 2026-09-27 首版 | WP59→WP36→WP60 批次首发固定为 `971b0807`（34,153 字节，批内固定、尚未外审；被审 v1）；经首审 REQUEST_CHANGES（WP59-R01～R04）修订被 `440a67b1` 替代（v2 修订稿，被审版）；经 v2 复审收尾（R02/R04＋C03）修订被 `9a41d185` 替代（42,041 字节，v3 收尾稿，被审版；当前有效） |
| `specs/creature-rpg/wp36-wild-encounters-and-modifiers.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `b8a5bc26`（27,307 字节；引用 WP59 批内哈希 `971b0807`、尚未外审；被审 v1）；经首审 REQUEST_CHANGES（WP36-R01～R04）修订与 WP59 v2 级联被 `3120d1e1` 替代（32,592 字节，v2 修订稿，被审版）；经 v2 复审收尾（R02＋C01 剩余一条）与 WP59 v3 级联被 `d21edcc7` 替代（33,424 字节，v3 收尾稿，被审版；当前有效） |
| `specs/pokemon-rules/wp60-berry-plants.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `227bb696`（20,545 字节；引用 WP59/WP36 批内哈希、尚未外审；被审 v1）；经首审 REQUEST_CHANGES（WP60-R01～R03）修订与上游级联被 `e468c3bf` 替代（24,593 字节，v2 修订稿，被审版）；经 v2 复审收尾（R01＋C03.4）与上游 v3 级联被 `114c432b` 替代（24,912 字节，v3 收尾稿，被审版；当前有效） |
| `specs/overworld/wp60-fishing.md` | 无中间版本 | 2026-09-27 首版 | 批次首发固定为 `b7de3ff4`（16,866 字节；引用 WP59/WP36 批内哈希、尚未外审；被审 v1）；经首审 REQUEST_CHANGES（WP60-R04/R05）修订、上游级联与 C02 引用同步（§1 WP27→WP28）被 `f280e9a7` 替代（20,304 字节，v2 修订稿，被审版）；经 v2 复审收尾（WP36-R02 传播＋C03.3）与上游 v3 级联被 `5f274a2c` 替代（20,759 字节，v3 收尾稿，被审版；当前有效） |
| `review/wp59-wp36-wp60-delivery-2026-09-27/delivery-summary.md` | `407c61a5` | 2026-09-27 首版 | 批次首发固定为 `407c61a5`（7,191 字节，被审 v1）；经首审修订注记（v2，首批哈希与修订材料入表）被 `835334ef` 替代（10,390 字节，v2 注记；短标签笔误于第四十四轮更正）；经 v2 复审收尾注记（v3）被 `809e0fa0` 替代（12,097 字节，当前有效，v3） |
| `review/wp59-wp36-wp60-delivery-2026-09-27/self-checks.json` | `86348342` | 2026-09-27 首版 | 批次首发固定为 `86348342`（6,866 字节，被审 v1）；经首审修订同步（受影响结论更正、旧结论留史）被 `4f9c02d8` 替代（11,965 字节，v2）；经 v2 复审收尾同步（入口分列、向量分列）被 `3bad9fd6` 替代（12,955 字节，当前有效，v3） |
| `review/wp59-wp36-wp60-delivery-2026-09-27/boundary-checks.json` | `cef81335` | 2026-09-27 首版 | 批次首发固定为 `cef81335`（4,074 字节，被审 v1）；经首审修订同步（组 2/3/4/5 更正）被 `b12ebefd` 替代（6,271 字节，v2）；经 v2 复审收尾同步（组 2/4/5）被 `db51d641` 替代（6,903 字节，当前有效，v3） |

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
