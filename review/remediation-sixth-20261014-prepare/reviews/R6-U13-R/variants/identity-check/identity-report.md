# R6-U13 V001–V004 独立输入身份核验

核验基准为 `00b45de642f07cee9953e42f04cce9c35d77346f` / tree `6708f580d5a02f874a1a24a95d7c0649b10c393b`。已全文读根 AGENTS.md；未切分支、提交、运行作者脚本／参考程序／CLI探针；写入仅在本目录。

- `contracts/R6-U13.json` 与 `prompts/R6-U13-R.md` 第一完整 JSON 结构相等；当前工作树的 prompt、合同、索引、manifest、历史报告字节均与冻结对象相同。
- V001–V004 所有嵌套 payload_identity 共113次引用、18个唯一 commit/path，逐项核 bytes、SHA256、Git blob、mode、type、行数及声明 tree，全部匹配。R commit/tree和必要blob可在项目对象库读取。两个声明参考工作区路径均不存在；未把缺工作树误记为源修改，也未声称参考独立对象库存在。
- candidate-manifest 八份 baseline 均匹配固定 main；八份 candidate 均匹配冻结提交和当前镜像。镜像差集恰为合同八个正式路径，无额外或缺失路径；全部八份确有变化。固定 main 与当前冻结正式 tree相同。四ID对应的写路径联合为WP40、WP56、WP58及combat WP54/55/56/58测试目录；其余四镜像属于同批其他ID，不能在本辅助核验中当作四ID独立语义PASS。
- prompt末共同恢复证据完整 JSON 含115条，每条九个原元数据字段全部解析并与inputs/evidence/index.json相等；每份冻结缓存、当前缓存和声明Git blob的bytes/SHA256/blob均115/115匹配。7个四ID引用的反证EV均包含其中。原core `5210b009db5191f307301115845e31475cd798ef` 本地对象缺失，所以115条原commit/path及report-directory tree绑定无法独立复验；原variants/findings.json与normative-records.json也不能从该core恢复。缓存／声明blob身份通过不扩大成原发布绑定或语义通过。
- 历史导航缓存 `review/remediation-fifth-20261013-prepare/integration/R5-U08/candidate-01/historical-regression-input.json` 的3283387 bytes、SHA256 `789fe2806041016c31fb1d7907eff663dc803bc4c21bebb018ad0f1c3eccf406`、blob `534ed3e48528156bccc7a5ecf3422062fda83521`可独立核验。作者历史报告所引30个绑定分组（含该缓存）中：20组原commit/path可读；2组仅声明blob可读、commit/path未核；7组不可恢复。可读绑定及可解析pointer未发现身份不匹配。
- 缺失历史绑定为c0ff330…的regression-fourth-17.json、regression-third-23.json、regression-legacy-scope.json和modules/REG/reading-coverage.json（7组记录、4个唯一路径）。R5三条scope所指两个blob `bbdee0813200953d50abf647b73341466d5559c9`、`7b21312f9f3512bfdd57e21a17cfb83096074050`也缺失。75900f…的B12 review及d984a0…的B13 control-coverage仅原声明blob可验证。因上述缺口，完整历史资格原件身份与精确scope不能在当前环境全部独立复验。

未发现当前可核载荷的mismatch。结果只证明身份、范围和可恢复性；哈希、JSON解析及旧作者记录不构成新的语义审读、行为PASS、历史回归PASS、整合接受或CLOSED。

要求的model/effort/tier/speed/UUID实际有效回显均未提供，保持 `UNVERIFIED`。未执行CLI探针，也未冒称实际配置符合请求。

完整逐载荷与错误证据见 `identity-check.json`；固定main到候选的完整差异见 `fixed-main-to-candidate.diff`；本次安全核验的真实argv/cwd/UTC/stdout/stderr/exit见 `execution-receipt.json`、`check.stdout.txt`和`check.stderr.txt`。
