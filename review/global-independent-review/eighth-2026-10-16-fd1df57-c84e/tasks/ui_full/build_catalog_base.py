"""Explicit manual vector assertions. Row indexing preserves already full-read original fields only."""
import json,datetime,hashlib,re
from pathlib import Path
B=Path(__file__).parent;project=B.parents[4]
catalog=Path('deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md')
lines=catalog.read_text().splitlines()
rows={};family=None
for n,line in enumerate(lines,1):
 if line.startswith('## '):family=line[3:].split('：')[0]
 if line.startswith('| '):
  name=line.split('|')[1].strip()
  if name and name!='ID' and not name.startswith('-'):rows[(family,name)]=(n,line)
# Every assertion below is authored after full row + source/consumer reads.
data=[]
def a(family,id,atoms):data.append((family,id,atoms.split(' / ')))
a('MG','MG01','A后暂停 / 确认后续B')
a('MG','MG02','忙非暂停USE只恢复 / 不推进字符 / 不变速度 / 计时继续')
a('MG','MG03','显式暂停USE解除 / 请求决定音 / 继续显示')
a('MG','MG04','全显且出现动画完USE结束')
a('MG','MG05','空w置空皮肤 / 不恢复默认')
a('MG','MG06','f直接Pictures / ff先头像后图片 / 四列96x96')
a('MG','MG07','控制转c2 / 前4位15RGB正文 / 后4位阴影')
a('MG','MG08','负取消字段有效 / BACK-1 / 写变量3')
a('MG','MG09','变量号0通过数字检查 / 实际变量0写义另分层')
a('MG','MG10','x.to_i为0 / cancel0 BACK无效')
a('MG','MG11','初索引1 / USE返当前索引')
a('MG','MG12','cancel2 BACK返1 / cancel-1返-1 / cancel0无效待USE')
a('MG','MG13','commands nil立即0')
a('MG','MG14','空数组仍建窗循环 / 无条目不移动 / USE返0 / BACK按策略')
a('MG','MG15','整除列数首UP trigger回绕末 / 后纯repeat不回绕')
a('MG','MG16','固定范围确认3 / BACK-1不夹限')
a('MG','MG17','后设默认清取消值 / BACK返夹限初5')
a('MG','MG18','当前6超1..5 / USE蜂鸣 / 不返回继续')
a('MG','MG19','键盘7满插H拒')
a('MG','MG20','光标满删末插H / 得ABCDEFH / 自动OK')
a('MG','MG21','超长初值不截断 / 两模式可直接返8字')
a('MG','MG22','第一组插入后pos1切小写 / 不按字符类')
a('MG','MG23','交互已开且max>=1 / 空低于min1 OK先确认音 / 不退出 / 无蜂鸣 / max0首绘另例')
a('MG','MG24','键盘min0 Esc空 / min正Esc无效')
a('MG','MG25','自由编辑Esc原文 / 编辑作废')
a('MG','MG26','B自身无等可更新合法命令 / A消息不全局阻塞B / B新消息被守卫拒')
a('MG','MG27','块异常无本地ensure关文字输入 / 组件释放未保 / 淡出ensure不管此开关')
a('MG','MG28','无块无内建地图更新 / 显式地图块独立对照 / 异常块边界保留')
for id,text in [
('DT01','前4正文15RGB / 后4阴影'),('DT02','A外层双颜色 / B红无阴影 / C恢复外组合 / D调用默认'),('DT03','A保证标签消费字体回退Arial / 仅标签无项目不证消费'),('DT04','先换行 / 再右对齐'),('DT05','后续X使循环到标记 / 直接图标目录绘item'),('DT06','后续A使标记消费 / 源矩形16x16'),('DT07','仅图像空项目 / A文尾图像只A / 尾图不生成'),('DT08','pg识别无动作')]:a('DT',id,text)
for id,text in [
('P01','有Gear优先 / 暂停不TownMap'),('P02','无Gear且无图两项无'),('P03','三项上下回绕 / BACK关闭无该场景写'),('P04','地图BACK nil / 无飞行目的 / 回Gear循环'),('P05','访问治疗点确认写目的 / Gear结束 / 后飞行链'),('P06','wallmap不写目的 / 带开关点隐藏'),('P07','无定位退0左上 / 无玩家图标'),('P08','有资格ACTION切飞行 / 图标提示 / 再ACTION普通'),('P09','未访问非debug无选择'),('P10','地图取消nil无目的 / 队伍重建选0 / 本次BoxLink许可丢'),('P11','有改两确认后存PBS并退 / 无改直接退无问'),('P12','三可见项数3 / 待再战1图标 / 信号依地图'),('P13','无联系人只消息 / 不开画面'),('P14','无机预检false / 不经预检直接注册新增可见'),('P15','隐藏旧不恢复 / 新建可见 / 相同版本3起0重复直接新增'),('P16','删除隐藏 / 清倒时旗标 / A=true刷新 / 可见优先重排 / 删光消息关闭'),('P17','NPC正常UI无删除'),('P18','三排序各键 / 可见稳定优先 / 隐藏沉底组序保'),('P19','移动实时 / BACK还原位置 / USE或ACTION落定'),('P20','倒时至0置旗1 / Afalse Btrue刷新 / 后每秒旗>0跳过不随机'),('P21','旗1取request写2 / 下通remind缺退request'),('P22','两body齐75%拼 / 无body恒拼 / end非空追加'),('P23','当前节缺退起始 / 再缺Default'),('P24','06晨专intro / 22夜仍通用intro'),('P25','同图当面 / 跨区拒 / 无信号更早拒'),('P26','同区异图异地图名可见训练家 / 无候选不呼'),('P27','胜后下一版本 / 旗0倒时0 / 下次重随机'),('P28','版本数1上限0恒起始'),('P29','March请求 / lowerfalse highertrue / 无覆盖写 / 新图完成两旗false / 实际曲目host未知'),('P30','Custom写A / March旗更但实际覆盖A / Stop清覆盖请求地图曲'),('P31','身份呼出缺类get先失败 / 早于距离信号 / UI对象正常门'),('P32','公开查询恒0 / increment无动作 / 对象级正确独立'),('P33','最终缺ID99或0严格错早提示 / 有效实际1成功不查缺0/99 / 图标定位另门'),('P34','无效请求退当前0定位图标 / 有效异区1左上无标 / 无定位优先0无标'),('P35','ceil5/3=2 / 偏移2,1 / 游标标15,13 / 形状0不阻'),('P36','同长全1偏移相同 / 宽1长1无偏移 / 缺尺寸宽0无偏移 / 非法实际尺寸不保'),('P37','首点关门阻整组 / 后点不补 / CTRL不越开关 / 交换顺序首完整生效'),('P38','首A无详情治疗后B不补 / 首完整访问三项有效 / wallmap开关首仍藏'),('P39','文本普通新增排序后反馈失败保可见 / 文本静默true / 规范普通静默true / 未知类型false无新增'),('P40','NPC事件0注册保留但拨打消息类型错 / 正缺事件助手false后提示 / 正有事件请求未执行 / 无信号更早'),('P41','一通TP一次TE一次跨段一致 / TE只前四均1/4无权重 / 第五E0 / 队伍等概率含重复'),('P42','AABC→A半BC各1/4 / Land空Cave均X/Y / 再WaterZ / 三表空文字空 / 普通遭遇权重不变'),('P43','Custom目录缺失败前A旗未清 / 空USE清覆盖两旗false / 空BACK保覆盖旗 / host恢复未知'),('P44','CustomA两旗false / March保A highertrue / 换图保A清两旗 / 最终声未证'),('P45','旧RegisterBattle版本参数3成为起当前3版本数1 / 预检拒或确认拒无新增false / 文本反馈错前新增'),('P46','旧Reset未定义参数求值先失败 / 不查不写旗倒时A / 正确胜重置另路'),('P47','独立领域表示可同等 / 保旧ASCII入口参数排序共享与真异常 / 概念未执行')]:a('PG',id,text)
for id,text in [
('PL01','规范成功count1/start3/current3 true / 确认取消false无新 / 文本先写后错'),('PL02','文本静默注册true不用机 / 未知false无新'),('PL03','NPC事件0两visible参数均true可见 / 0拨打失败 / 正事件按P40'),('PL04','直接删除训练家返false但隐藏并附写 / NPC可直接隐藏无附写 / 越界失败 / UI NPC无删除'),('PL05','旧查缺公开get失败 / 正确记录查询可取'),('PL06','真假比较前失败 / 正确可见查询真假'),('PL07','取旗前失败 / 记录旗1就绪0不'),('PL08','参数求值先失败无重置 / 正确重置另路'),('PL09','旧0含无联系人 / 记录相对1'),('PL10','旧忽参数无动空返 / 记录级可推进1'),('PL11','AfalseBtrue刷新 / 不改旗0倒10 / NPC无动作空'),('PL12','无信号也均抽可见候选 / 无定位nil / 真呼入信号另门'),('PL13','缺get早于同图信号 / 对象呼出无信号先拒'),('PL14','生成文字不播放 / 不抽TPTE / 旗1写2旗0不写 / NPC空类型可错'),('PL15','直接播放无信号也可进 / 每通固定占位抽样 / 返回末消息结果 / 呼出包装无信号先拒'),('PL16','AABC前四A半BC1/4 / 非训练家无记录空表空文字 / 每次直接可重抽'),('PL17','队AA恒A / AB均半 / 无训练家数据空 / 空队伍不冒保护'),('PL18','只地图命名服务值 / 不查同图或信号 / 未知数据依服务未知host')]:a('PG',id,text)
for id,text in [
('T01','两splash各.4+2+.4总5.6名义 / 停留USE提前淡入出不检测 / 标题USE叫声等1 / 标题淡出.4 BGMfade1 / 三菜单'),('T02','继续大面板及三菜单 / 地图名查询先存档名展开 / 早于选择共享材料保留'),('T03','debug非打包skip且读后空直接新 / 文件存在不等非空'),('T04','debug skip默认false直接Load / 跳splash标题'),('T05','无语言无装配选择无命令 / 两语言首次空装配问 / Load语言命令'),('T06','有继续选语言关闭再选载消息直写 / 不经正常保存 / 无继续不写'),('T06b','选项60离开不落盘仍80 / 后语言直写整体系统60 / 仅回菜单或无继续无此写'),('T07','二次拒中止删保档 / 回标题'),('T08','无档提示 / 回标题'),('T09','无效无bak拒绝直接进程退出 / 同意删并重置系统 / 无档Load'),('T10','无效有bak提示递归读 / 有效备份继续面板'),('T11','保存No返回false / 选择音 / 暂停重显'),('T12','覆盖No档不动false / 菜单重显'),('T13','保存真成功消息关闭 / 假失败消息重显'),('T14','退出同意后保存No仍结束进程 / 不查保存返回'),('T15','紧急先置scene nil与重启消息 / 有玩家旧档先备份 / 成功保存备份消息后恢复旧scene / 无玩家消息后返不恢复scene'),('T16','速度字段即时写 / BACK不还原 / 关闭不保存'),('T17','TextSpeed首末夹限'),('T18','SpeechFrame编号回绕21→1'),('T19','音量100夹限'),('T20','Load选项音量字段写无BGM预览 / SE仍查BGS'),('T21','无跑鞋隐移动项 / 有鞋可见'),('T22','配置假隐送盒 / 默认世代8可见'),('T23','游戏选项无语言'),('T24','缺图鉴队伍GearMap均隐 / 保存未禁则现 / 选项卡退出可见'),('T25','Safari隐保存现Quit / 确认可关闭会话决定回起点 / 拒返菜单'),('T25b','合法同地图两会话启动可并存 / 保存隐 / 两Quit均现 / 仅静态条件非Demo'),('T26','隐藏招式成功菜单关闭in_menufalse后执行 / 取消返菜单'),('T27','满队withdraw提示不开屏 / 留四项子菜单保下标 / 一BACK才主PC'),('T28','最后可战斗拒存 / 留四项子菜单保下标 / BACK才主PC'),('T29','信箱移袋满提示 / 邮件信箱不改'),('T30','无候选不开菜单 / 只登记提示'),('T31','招空转道具侧 / 下标夹2 / LEFT空侧不切'),('T32','已登记未持有不候选 / 不等执行成功'),('T33','FLY取消重显保游标 / 确认目的in_menufalse后执行关闭'),('T34','使用前拒直接重显in_menu不变 / 包装假恢复标记重显 / 成功与扣量分开'),('T34b','CoinCase真使用关菜单 / 数量不变独立'),('T35','缺walking charset具名错 / 不静默fallback'),('T36','快捷游标写bag持久 / 暂停游标临时不存')]:a('NV',id,text)
for id,text in [('CH01','四页依次内容fade / 其余opacity0'),('CH02','末页确认快照冻结置黑 / 过渡8/20=.4目标 / 正常释放'),('CH03','文字键名不证明绑定'),('CH04','缺图按资源合同 / 不猜运行'),('CH05','ACTION方向无分支 / 仅USE页进末退')]:a('CH',id,text)
for id,text in [('TC01','默认bg/card / 六行 / 三徽章按真位0/3/7 / x72/216/408不紧排'),('TC02','背景card女性候选独立 / bg_f有card_f缺只背景女'),('TC03','缺开始时间展示即写当前 / 以后固定'),('TC04','ACTION方向无响应 / BACK关闭音淡出清理回暂停'),('TC05','3661秒1h1m / 公开号42为00042 / Money千分位'),('TC06','地区1只全局8..10真 / 图集行1槽0..2 / x72/120/168 / 不画其它假槽'),('TC07','128x256位置336,-16 / 128x128位置336,112 / 底均240 / 横128区对齐'),('TC08','outfit2有变体用2 / 缺退基础 / outfit0仍先_0再基础')]:a('TC',id,text)
assert len(data)==153
families={
'MG':['UI17-U018','UI17-U020','UI17-U031','UI17-U032','UI17-U034','UI17-U035','UI17-U036','UI17-U040','UI17-U042'],
'DT':['UI17-U026','UI17-U027','UI17-U028','UI17-U029','UI17-U030','UI17-U052'],
'PG':['UI63-U001','UI63-U002','UI63-U003','UI63-U004','UI63-U005','UI63-U006','UI63-U007','UI63-U008','UI63-U009','UI63-U010','UI63-U011','UI63-U012','UI63-U013','UI63-U014','UI63-U015','UI63-U016','UI63-U017','UI63-U018','UI63-U019','UI63-U020','UI63-U021','UI63-U022','UI63-U023','UI63-U024'],
'NV':['UI65-U001','UI65-U002','UI65-U003','UI65-U004','UI65-U005','UI65-U006','UI65-U007','UI65-U008','UI65-U009','UI65-U010','UI65-U011','UI65-U012','UI65-U013','UI65-U014','UI65-U015','UI65-U016','UI65-U017','UI65-U018','UI65-U019','UI65-U022','UI65-U023','UI65-U024','UI65-U025'],
'CH':['UI65-U020'],'TC':['UI65-U021','UI67-U021']}
vectors=[]
for family,id,atoms in data:
 n,line=rows[(family,id)]
 vectors.append({'id':family+':'+id,'original_id':id,'family':family,'formal':{'path':str(catalog),'line':n,'complete_row':line},'assertions':[{'id':family+':'+id+f'.{i:02d}','claim':s,'evidence':'DERIVED_VECTOR','execution':'NOT_EXECUTED'} for i,s in enumerate(atoms,1)],'source_units':families[family],'source_binding_scope':'Family source set names complete actually read semantic payloads; per-clause manual source links in reverse-mapping.json resolve specific branch. Does not claim every family source supports every atom.','premises':'Every original row field and section public premise preserved. FixedB8/R, stated legal objects/configuration, ordinary dependencies normal. WI/CRE/kernel interfaces only their exact received finite scope; actual media/host/Demo and history approval remain separate.','status':'MANUALLY_DECOMPOSED_STATIC_ROW_RECONCILED_WITH_EXACT_PREMISES','business':'NOT_EXECUTED'})
out={'schema':'gr8-ui-catalog-atomic/v1','reader':'/root/ui_full','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Original rows indexed only after actual full reading. Manual authored individual claims define semantic atoms; no delimiter/method/line counts used as completeness proof.','identity':{'path':str(catalog),'bytes':len(catalog.read_bytes()),'sha256':hashlib.sha256(catalog.read_bytes()).hexdigest()},'vectors':vectors,'vector_count':len(vectors),'atomic_assertions':sum(len(x['assertions']) for x in vectors),'all_catalog_denominator':'NOT_FINAL','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
(B/'catalog-mapping.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'vectors':len(vectors),'atoms':out['atomic_assertions']}))
