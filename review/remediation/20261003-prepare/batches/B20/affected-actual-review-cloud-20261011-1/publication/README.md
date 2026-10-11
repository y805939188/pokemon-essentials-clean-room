# B20 affected actual：普通发布与独立远端读回

首份实质报告 commit `248039a6b84e5326a3516db07924030295b79a49`，tree `da6abeb9119a4de712f3dece201da2754b3c206c`。

普通推送分支 `review/b20-affected-actual-cloud-20261011-1` 后，使用无共享对象库/alternates的全新 bare `/tmp/b20-act-report-readback-20261011-1.git` 从 GitHub 网络 fetch 该分支，并用独立 ls-remote 确认同一SHA。18个输出全部从远端对象读取，逐文件核完整字节、Git blob、SHA256、大小、mode、JSON解析及清单；全部通过，包含根 output-manifest.json 本身。

详情见 [report-readback.json](report-readback.json)。这是网络读取的报告产物元数据核验，不是游戏或案例运行。固定被审 ACT 为 `6babcf657aef559dbf101aeb093a1beb730ab507` / tree `7f511347be10a55ed1341f4132e198ac6bdedede`；报告0 affected阻塞，未签FULL、正式C或canonical关闭。

本次三份publication输出只追加到本人新报告目录。该目录最终共21个输出；[publication清单](output-manifest.json) 列出除本清单之外20个输出的Git blob/SHA256/大小，避免自hash递归。根清单记录首份报告17个其它输出；本回执绑定首份实质报告18个输出。

最后普通快进推送后，从另一全新独立 bare `/tmp/b20-act-final-readback-20261011-1.git` 读取最终21个输出，并确认首份18文件未变。最终包精确commit/tree与全21输出读回结果由完成响应外部返回，不将包含自身的最终commit递归写入自身。正文、公共记录、参考和旧证据仍不修改。
