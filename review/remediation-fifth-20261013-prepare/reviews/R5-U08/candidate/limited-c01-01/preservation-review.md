# C01 三行限定机械保留复核

裁决：`PASS_LIMITED_MECHANICAL_PRESERVATION`；失败数 0。固定候选 `40d4f08f4c3a3325e3f53c2de7dd7597224101e4`，定位 `59390e301bac9df82083e9b792d7b04d0fe25884`；原独审 `7533e516bd6e2a34ebeb68af28617c854ac17d50` 的整体 FAIL 保留。

仅 UIcatalog 第206/207/242行变化，+3/-3、净增169 bytes；其它所有行精确未变。三行 source/mapping、独立生成 patch、私有正向及逆向 apply 均逐 bytes/SHA/blob对齐。三项纠正单列，未并入原262贡献。

原 U02-F066 和 U06-E039载荷各在旧/新全文精确出现一次。U02-F065在两全文中均因已接U06-E039组合不再字面出现；用该原操作的准确after→before逆向一次，均恢复原F065载荷一次且身份完全一致。三个旧作者记录与已接载荷均核冻结身份，未授予新整篇签名。

原8步×131重放、85sole-writer及262原贡献不重跑；准确原报告 SHA/bytes/blob与结果仍匹配本子任务原交付。旧总体候选失败不转PASS。

六行政镜像、20其它共享全文、WP66-A全文、A07含LF行及18原矩阵/合同/packet输入在oldcore/newcore/locator/外部oldreview提交中身份均相同；410原native pointer记录hash逐项吻合，568原schema矩阵字节不变（410 native＋158 additional）。原评审载荷按外部7533提交引用，不声称复制进新core/locator。

七目标仅以当前正式主体 `e4ea8d03b0e2c7c20fc41fce92f0b2b7b7f02514` 为基底，在/tmp私有Git index/alternate objects投影；workspace tree `e72b606c5f35fe1bf11693724755b1c90471672b`、formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5` 与固定输入一致；旧六目标workspace `332fe1800236fd64ecaa45da691dad255b87147b`也吻合，相对旧六目标投影只有UIcatalog一条规范路径变化。newcore/locator含新增行政载荷，不是此可选workspace投影基底；本结果不签未来actualworkspace。live formal/support及其131formal tree均未改。

本结果仅提供机械保留裁决；G03/G09新语义裁决由父审及原共享审者另行完成。未接live、未正式接受、未CLOSED，参考/model/host执行均0。任务UUID及模型参数实际回显仍UNVERIFIED。
