<!-- U06-E025; target/location and exact B5 anchor in fragment-manifest.json -->
有限ASCII 1–9字符都占位、0/x为空（WP62 §5.3.1）；正常作者指导仍为01，任意Unicode/nil/损坏输入不扩张本合同

<!-- U06-E026; target/location and exact B5 anchor in fragment-manifest.json -->
#### 6.2.1 普通参数页的候选和焦点邻接

候选索引从0开始，列数仅说明逻辑邻接，不要求物理布局。排序6项依次数值、字母、最高、最矮、最重、最轻，2列且无空白；名字默认A–Z共26、7列；类型按定义顺序纳入已登记非伪类型，默认18、4列；颜色按定义顺序排除None，默认10、3列；形状按定义顺序排除None，默认14、5列。内容扩展时用实际候选序列及数量N，不能将默认18当所有类型上限。A–Z向量以每标签仍为对应单字符为前提。

非排序页另有空白、OK、Cancel；打开聚焦已选项，无选聚焦空白。普通方向trigger只改焦点；USE在具体候选/空白才写本地选值，OK才提交子页，Cancel/BACK弃稿。焦点、本地选值、写回外层草稿三个量分开；大小端点和类型双槽沿§6.2原合同。

令普通候选为0..N−1、列数c、末行首项L=c×floor((N−1)/c)。以下单键转移中未列成立条件则原位：

| 焦点/输入 | 转移 |
| --- | --- |
| 候选i，UP | i≥c时到i−c，否则原位 |
| 空白/OK/Cancel，UP | 分别到L−1、L、空白；排序Cancel例外到N−1 |
| 候选i，DOWN且i+c<N | 到i+c |
| 候选i，DOWN且下格不存在、i在倒数第二行 | 列号i mod c<c/2则到N−1，否则到空白；不是统一夹到同列末项 |
| 候选i，DOWN且i在最后一行 | 列号<c/2到OK，否则Cancel |
| 空白，DOWN | Cancel；OK/Cancel DOWN保持 |
| 候选i，LEFT | i>0且列号非0到i−1；空白LEFT到N−1，Cancel LEFT到OK |
| 候选i，RIGHT | 非排序末项到空白；其它非最右列到i+1；OK RIGHT到Cancel |

默认名字未选只给方向：空白→UP→U(20)→DOWN→空白→LEFT→Z(25)→RIGHT→空白→DOWN→Cancel→UP→空白；参数始终未选。独立四轮UP；USE；ACTION；USE才提交U；前三轮后BACK则弃本地U、保留进入前未选。排序焦点0经三次DOWN为2、4、OK，RIGHT到Cancel、UP到5，方向不改变已选排序0。颜色7 DOWN到9而8 DOWN到空白；类型14/15 DOWN到空白；形状9 DOWN到空白。空白/OK向上对照分别为名字20/21、颜色8/9、类型15/16、形状9/10。

### 6.3 搜索结果态的退出

<!-- U06-E027; target/location and exact B5 anchor in fragment-manifest.json -->
#### 6.2.2 本轮输入阶段

参数子页先按UP>DOWN>LEFT>RIGHT处理一个方向，再独立按ACTION>BACK>USE处理一个按钮。普通页方向均trigger；大小页UP/DOWN trigger、LEFT/RIGHT repeat，按钮trigger。大小方向可先写本地端点，BACK仍弃稿；ACTION+USE只聚焦OK，不提交。名字未选时UP+USE先焦点U再本地选U，尚未写回外层。

搜索主画面全部trigger，UP>DOWN>LEFT>RIGHT>ACTION>BACK>USE是一条互斥链，不能套子页两阶段；Start上UP+USE只移到体重，不搜索；ACTION+USE只聚焦Start。以上为输入服务条件快照，不证明实体键可达，也不把本顺序推广其它UI。

### 6.3 搜索结果态的退出
