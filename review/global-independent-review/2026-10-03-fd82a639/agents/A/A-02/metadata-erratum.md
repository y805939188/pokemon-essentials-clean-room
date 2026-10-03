# A-01 配置元数据补充勘误

本补充只修正 A-01 的配置证据表述，不改写 A-01 原件或审查结论。

Root 首次派发 A 时明确提交 `fork_turns=none`、`model=gpt-6-astra`、`reasoning_effort=ultra`，工具接受请求后返回 `/root/review_a`。A-01 将配置描述为继承父任务不准确。父任务有自身 turn_context 核验；本子任务没有独立运行时模型/推理强度回显。请求配置是 Astra / Ultra；不能把请求获接受再升级为本子任务独立运行时证据。速度仍为 UNVERIFIED；没有更改速度设置。

证据来源：Root 在 A-02 派发消息中说明首次调用实参及工具返回；本子任务未另行读取 Root 的运行时上下文。
