# X-C-STORAGE 独立首判

保存：2026-10-03 18:12:32 UTC。本文件先于任何ROOT存储结论对照保存，后续比较另存文件。

只读中性brief、固定WP66-B原/净化正文与BX39条、参考局部链。保存前未读ROOT或其他组的存储结论。之前授权ROOT002范围比较已存在，未涉及本场景。

WP66-B原稿/净化§3.2第71行“交换后暂持清空”错误，与各自§4.2第101行冲突。成功交换会继续持有原目标成员；BACK禁止退出。

| 步骤 | P | Q | 手中 | BACK |
|---|---|---|---|---|
| 初始 | X | Y | 空 | 无暂持时可进入继续操作确认，不是无条件立即退出 |
| 拿起X成功 | 空 | Y | X | 提示仍持有成员，留整理循环 |
| 对Q成功交换 | 空 | X | Y | 仍有暂持，提示仍持有成员；不出现退出确认、不回滚P/Q/手中状态 |
| 交换后BACK | 空 | X | Y | 禁止退出 |

空格对照：从P=X、Q空开始，拿起后P空、手中X；成功放到Q后P空、Q=X、手中空。BACK此时进入“是否继续盒子操作”确认：Yes继续、No或BACK退出；移动不回滚。

交换后再成功把Y放回P，才形成P=Y、Q=X、手中空，并恢复上述退出确认权限。

BX B03、B04分别正确覆盖手中非空/空的BACK，B07只写“交换”，没有断言交换后的手中成员；三者不组成逐步交换→BACK向量。应新增上述两个连续场景，不改其原有正确断言。

普通菜单Shift和quickswap的已占用目标都调用同一交换操作；视觉手中图也换成原目标图。

来源：

- `specs/ui/wp66-b-storage-and-pokedex-ui.md`：69-71;95-118;226-232
- `deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md`：69-71;95-118
- `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`：201-243
- `Data/Scripts/016_UI/017_UI_PokemonStorage.rb`：837-940;1117-1175;1490-1690;1690-1895
- `Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb`：150-185;252-264

纯静态阅读，未运行UI、参考代码或模拟器；以守卫通过、依赖正常为前提；C-07整体主来源尚在继续全文阅读，本局部首判不代表全批完成。
