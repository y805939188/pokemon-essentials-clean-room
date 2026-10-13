- 行显示：按 [WP27 §2.2](../creature-rpg/wp27-bag-and-item-storage.md) 的数量判定，普通物品的 ShowQuantity 省略/false/true 都通过，重要物品仅 true 通过。重要物品已登记实心图标优先，其次未登记且可登记的空心图标；二者都遮数量。无图标且判定通过时画当前槽份数，不画跨槽总量；普通物品直接登记也无登记图标。CLOSE BAG 行无图标、说明文本换为「Close bag.」。

PC 物品列表沿 WP27 §2.2 的普通/重要 × ShowQuantity 三态判定画当前槽数，没有背包的登记图标遮数分支。重要物品在成功存取消息中按 1 显示不改变列表判定；普通 ShowQuantity=false 仍可显示每槽 2/3，而非总量 5。

### 5.1 数量窗口的同轮输入竞争

