# R5-U03 actual-02：WING一行机械接入

按原作者 `6ced99e1279bc947bfbc63d33ceaeb240b8f9f02` / tree `bb27f8dfee659ea77738c29cd989accabccee469` 与原独审 `c22c9c5e8f0a18f930222a8d2055f14c1e3191d0` / tree `da0847af181d912c2076b22715e2f981ed65d604` 的限定候选PASS，R5-I仅复制正式测试目录第294行的输入前提。补丁与9fab提案完整3597bytes逐字节相同；最终目录与受审作者镜像完全相同。

新前提为“六FEATHER逐身份独立；另对应WING须有合法作者记录，且为非重要物品、有效消费为真（Consumable省略或true）。”其余premises/expected不变。行387→461bytes（+74），UTF8零基字节偏移48464；新行SHA256 `11c61cf1eaaa3cf78adbf47fb06dfbfc67afa46372cbeacf8178f0dffacc9c08`，完整文件56918→56992bytes，SHA256 `4ac5462303f6bb5ae8aa3a7e891a53aed6fcd7f992a7a48167e876981b9371ba`。

[精确映射](candidate-to-actual.json)、[一行增量](current-to-actual.patch)、[机械身份核验](mechanical-validation.json)、[正式131身份](formal-tree.json)和[依赖门](upstream-impact-and-gates.json)。其余130正式Git blob、15个U03投影、U02已接受16文件以及WP27/28/U01-O025的实际正文不变；68向量/51操作和原59静态记录/11finding记录身份已核。旧8b actual与1eda FAIL、两处冻结MISMATCH和所有旧候选/实际/公共账原样保留。

候选PASS仅允许本次机械接入，不授actual-02 PASS、U03正式接受或CLOSED。实际commit/tree由下一独立定位提交绑定；交[原审者入口](reviewer-entry.md)定向核实际字节与必要消费消费者，精确未变签名按原限定资格复用。禁止全11项/global重审及自签语义PASS。U04/U06恢复等待域未触碰；main、Mac、optional/政策未动。本update新增参考/模型/宿主/Demo行为执行0；所有身份/patch检查仅TOOL_VALIDATION。
