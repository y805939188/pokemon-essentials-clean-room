# NEW2 affected 报告发布与独立读回

固定审查 NEW2 `3f521e6dea0b442e4bb174a9715c458416386b37` / tree `49f406a6de8ca2786e5dda27abada19780fdfa05`。报告提交为 `cecc826263aab5e11cb51d1653bfb191306332c8` / tree `29093931f5080263dd7087227445cd409b11bdde`，父提交为作者最终读回包 `dbfa219547690f06eac9180f3ecd9dd1091eb49f`。

该报告已普通 push 至 `refs/heads/review/b20-affected-cloud-20261011-2`。随后新建独立 bare Git 仓库，以明确远端 URL/ref 网络 fetch；无本地对象共享、alternates或环境对象目录。全部17个报告文件，包括根输出清单本身，均从远端读取并逐字节、blob、SHA256、bytes核验一致，JSON解析通过。

[report-readback.json](report-readback.json) 绑定报告固定commit/tree及上述全部17个输出身份。本后继提交只增加本README、读回JSON和[output-manifest.json](output-manifest.json)。后继提交将普通推送，再用第二个新建独立bare仓库远端读回全部20个文件；最终准确publication commit/tree与全部输出核验由最终回复绑定，避免把自身提交哈希写入自身文件或无限递归复制凭据。

原[报告](../report.md)、[问题处置与验收](../findings.json)及其它17个报告输出在后继包保持相同字节。结论为 `PASS_SCOPED_AFFECTED_CANDIDATE`，本门剩余阻塞0；未签FULL、actual或正式接受，不改canonical状态。旧独立报告仍固定在既有 `680e3988c4144db269e063971991134b8e0bd678` 及 `be3363e8711bdf17b0f08e22517ec3bb00f9ef55`，没有改写。
