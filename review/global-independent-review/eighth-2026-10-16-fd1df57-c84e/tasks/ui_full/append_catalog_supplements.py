"""Hand-authored B04/B16 UI/B17 claims, exact original rows retained."""
from pathlib import Path
import json,datetime
B=Path(__file__).parent;p=B/'catalog-mapping.json';d=json.loads(p.read_text());path=Path(d['identity']['path']);rows={}
for n,line in enumerate(path.read_text().splitlines(),1):
 if line.startswith('| '):rows.setdefault(line.split('|')[1].strip(),[]).append((n,line))
entries=[]
def a(id,units,text):entries.append((id,units.split(',') if units else [],text.split(' / ')))
for id,units,text in [
('B04-M01','UI17-U019','禁符号负12→0文本00 / 有符号负12幅12 / 正12两者12 / 负123禁0允-99'),
('B04-M02','UI17-U032','禁负负范围变0..0初0确认0 / 允负原范围-6 / 显式取消-1不夹'),
('B04-M03','UI17-U042','ACTION只定位OK不音不返 / 后USE确认X / 已OK USE同轮返'),
('B04-M04','UI17-U042','A UP→UPPER / 再UP末行0 / UPPER DOWN首A'),
('B04-M05','UI17-U042','J RIGHT跳全空列10到逗号 / 末9右c11空格 / A LEFT句点 / 当前空不等全列空'),
('B04-M06','UI17-U042','UPPER LEFT OK / OK RIGHT UPPER / OK上下末首行列11非12'),
('B04-M07','UI17-U042','repeat方向先只移B不插 / 单USE XA'),
('B04-M08','UI17-U042','ACTION+USE只定位 / SPECIAL+ACTION只切组 / BACK+USE只删除 / 不同轮插返'),
('B04-M09','UI17-U042','LEFT胜RIGHT到末句点 / RIGHT单到B'),
('B04-M10','UI17-U040','键盘min0max0RETURN空正常关文字输入 / 插A拒 / 光标另失败'),
('B04-M11','UI17-U041','光标max0首淡回调clamp0,-1失败 / 部分UI位图已初始化 / 主输入结束未到 / max1可空返'),
('B04-M12','UI17-U040','min1max0RETURN不返 / ESC不返 / 插入拒 / min0独立空返不顶层退出'),
('B04-M13','UI17-U040,UI17-U041','光标max-1首clamp0,-2失败 / 键盘负max守卫不启可A / max0拒A / 文字事件给定非观察'),
('B04-M14','UI17-U018','两行逐字第三行前自动暂停 / 确认后名义.1滚一行再C / 三行或非逐字不该门'),
('B04-M15','UI17-U018,UI17-U021','暂停刚显示先0 / .35更新帧2 / 四帧.15 / 导航八帧.1此时3 / stop隐藏不重相位'),
('B04-M16','UI17-U034','男两替色男/女 / 女反 / 未知无玩家移两项 / 不等绘pg动作'),
('B04-M17','UI17-U047','行走四帧.5在.2为1 / 箱四帧.4为2 / 各32方 / 不证Load其它预览'),
('B04-M18','UI17-U036','可见0返回 / 事件映射原B / 403取消独立 / 变换一次清 / 未隐藏0原A'),
('B04-I01','UI17-U045,UI17-U046,UI17-U051','HP100/50/25/0时.375帧1/1/0/0 / 物种1 / 高48物品0 / 盒首0 / 媒体未证'),
('B04-I02','UI17-U046','选中frame0偏4,6 / frame1偏4,-2 / 未选0,0 / 不重相位'),
('B04-I03','UI17-U045','96x48两48帧1秒 / 非48高整单帧 / 普通空back / 摘要空独立隐'),
('B04-I04','UI17-U045','持物有→空→新逐更新对应 / 普通空back不套持物'),
('B04-D01','UI17-U028,UI17-U052','img默认源0,4,16,16 / 显式0,0 / icon同Y4 / 尾标DT07 / 不证裁剪像素'),
('B04-D02','UI17-U026,UI17-U027,UI17-U028','快速无格式A&lt;B字面 / pg强一般A<B / 去格式A<B / 消息色标一般 / amp lt只一层不重复解'),
('B04-D03','UI17-U048','8位红alpha128 / 6位红 / 001F红248 / 02色255128128 / 三位默认 / 不套c2两半'),
('B04-D04','UI17-U028','有A才消费missing回Arial / 仅标签无项目不证回退'),
('B16-006','UI17-U018,UI17-U021','绝对0/.15/.31/.60暂停帧0/1/2/0 / 导航0/1/3/6 / .31刚显示先0后2 / 不重局部相位'),
('B16-A015','UI65-U022,UI65-U023','debug非包skip读空直接new / 非空直接continue / 两者无菜单 / skipfalse菜单 / 旧文件迁移空不推继续'),
('B16-A058','UI17-U047,UI65-U002','命名双模式和Load行走0/1/3/0(.5周期) / 箱0/2/0/1(.4) / 全局相位 / 缺Load行走另T35'),
('B16-C058','UI65-U009','BGS记忆共享80→SE50当前记忆均50 / 恢复二次百分比25 / 信息副本改不影响 / 无BGS不改 / SE同值不重播 / 非BGM恢复'),
('B16-C114','UI65-U001,UI65-U020','两splash名义5.6 / 停留USE缩2非淡段 / 标题40/20=2闪 / USE叫等1淡.4 BGMfade1不保全叫 / 帮助双fade各.5阻再确认 / 末退.4'),
('B16-C115','UI65-U011','内部尺寸首应用同会话不重 / 0..3关闭全屏倍.5/1/1.5/2居中 / 4和-1全屏 / 7读min请求4存7 / 选项退出存4 / 负不钳0 / hostDPI未证'),
('B16-C118','UI17-U045,UI17-U046,UI17-U051','个体HP四档帧1/1/0/0 / 物种1物品0 / 选中两半4,6和4,-2 / 空成员隐 / 非48物品单 / 盒首方格 / 普通空返回图摘要空隐Party刷新 / 素材host未证')]:a(id,units,text)
for id,units,text in [
('B17-P003-equivalent','','独立表示同输入排序取消共享失败仍唯一结果 / 不要求参考继承参数槽容器'),
('B17-P003-identity','','必要外部身份/哨兵/共享Sketch影响不能净化删 / 源组织可迁移 / 仅行为范围贡献不授全源'),
('B17-P003-partial','UILC-U018,UILC-U020','净化室跨级失败保Shadow缎带成长 / 遗迹透传收尾 / 未证底层值不猜常量'),
('B17-P005-far','UI67-U009','3v3远4初选文本nil / 框精灵4高亮按钮无 / USE登记4离窗 / 布局维持执行排4无活近 / 非成功HelpingHand'),
('B17-P005-near','UI67-U009','活近2首选 / 文本按钮可选 / USE登记2'),
('B17-P005-none','UI67-U009','双盟友倒初己0 / 非倒2/4 / 可登记0不等执行合格'),
('B17-PA050-silhouette','UILC-U006','2.6秒目标白大轮廓 / 未正常色 / 未物种提交 / 不以准备隐藏概整段'),
('B17-PA050-prelude','UILC-U005,UILC-U006','准备目标隐藏 / 首更可见满白零缩放无非零影像'),
('B17-PA050-cancel','UILC-U006,UILC-U007','轮廓后取消回旧不提交 / 之前轮廓请求保 / 无BACK成功白闪新正常色 / 消息早于物种'),
('B17-PA059-trainer','UI67-U020','后B覆A / 后nil保A / 全nil地图M / M空全局G / G空两固定分别'),
('B17-PA059-presets','UI67-U020','五入口各对应三个预置 / X不套全部 / getter不清 / 正常外层清理另合同'),
('B17-PA059-empty','UI67-U020','普通后空覆A落M / FromType空保请求 / nil才M / 非普通入口非实际声'),
('B17-PA059-wild','UI67-U020,UI67-U015','野三地图WVC优先 / 再各全局 / 再各默认 / 野捕ME3.5 / 训练家不套'),
('B17-PA059-intro-queued','UI67-U020','无记忆有Q计时先清计时记Q位置0 / 再I / 无计时记当前位 / 位置查询错0'),
('B17-PA059-intro-memory','UI67-U020','已有R保 / 待播Q计时保 / 再I / 空引子不写不播'),
('B17-PB031-encore','UI67-U006,UI67-U009','自动Encore目标BACK回主 / 从未手选招 / 候选清Mega撤 / PP计时不变'),
('B17-PB031-manual','UI67-U006,UI67-U009','仅清Encore手选目标BACK招式 / PP不变 / 再BACK主'),
('B17-PB031-item','UI67-U008','未登记类型4目标BACK物品表 / 袋重显 / 不套Encore / 既登记退款合同保'),
('B17-PB032-move','UI67-U006','MegaMove无物可按钮 / ACTION登记再撤留菜单 / 攻击阶段形态'),
('B17-PB032-unreachable','UI67-U006','去指定招无石无可达 / 无按钮'),
('B17-PB032-debug','UI67-U006','CTRL不能绕禁止/不可达/野生前三门 / 只前三过绕环额度SkyDrop / 非CTRL仍后门'),
('B17-PB033-self','UI67-U009','2v2盟友倒初0文本nil / 自框精灵高亮 / 非初2 / 登0后执行排己无活盟'),
('B17-PB033-alive','UI67-U009','只恢复2则初2可登'),
('B17-PB033-far','UI67-U009','3v3远4活初4 / 不是无近就回己'),
('B17-PB034-direct','UI67-U019','首候选前缺读取失败 / 消费者无下标 / 无随机合法 / 不保全局退出回滚'),
('B17-PB034-main','UI67-U019','AI控制正常命令旁路该辅助 / 不由局错判主失败或整模拟成功'),
('B17-PB034-other','UI67-U019','Bag1/15 / 非BagCall1/10总体7/75 / 目标只敌活不类别 / 空-1 / 换人caller验空无返'),
('B17-PC003-labels','UILC-U003','a直接前序提交 / b仅演出自身写 / c直接不归零 / abc唯一'),
('B17-PC003-duplicate','','历史C第三标b预期c不唯一 / 不能以行数统计通 / 不是当前L09新错误'),
('B17-PC003-original','UILC-U003','原L09abc已对 / 恒true与回退不可达 / 只正式标号修订不改变入口行为'),
('B17-PC119-last','UILC-U006','最后更新同轮BACK先取消 / 旧种取消+1 / 不成功统计/后置/物种 / 已caller写不撤'),
('B17-PC119-forbidden','UILC-U006','入口显式false非默认Caterpie石 / 末轮BACK不取消 / 双轨完成功'),
('B17-PC119-flash','UILC-U007','进入成功白闪后BACK不取消 / 原成功链继续'),
('B17-PD018-both','UI67-U013','阶段23已到原布局收双计划 / 0↔2及1↔3均依序执行 / 活2/3 / 不因首新近邻撤次'),
('B17-PD018-asym','UI67-U013','3v2多计划剔双席1↔3 / 三席0↔2执行 / 活2/1'),
('B17-PD018-unreached','UI67-U013','未到阶段不保反馈 / 原有近邻无新计划 / 手动Shift不改'),
('B17-PD018-owner','UI67-U013','玩家0/2异主不收 / 敌1/3同主执行 / 活0/3 / 单侧多主不等双禁')]:a(id,units,text)
for id,units,atoms in entries:
 matches=rows[id];assert len(matches)==1; n,row=matches[0];family='B04' if id.startswith('B04') else 'B16' if id.startswith('B16') else 'B17';key=family+':'+id;assert not any(v['id']==key for v in d['vectors'])
 d['vectors'].append({'id':key,'original_id':id,'family':family,'formal':{'path':str(path),'line':n,'complete_row':row},'source_units':units,'assertions':[{'id':key+f'.{j:02d}','claim':s,'evidence':'DERIVED_VECTOR','execution':'NOT_EXECUTED'} for j,s in enumerate(atoms,1)],'premises':'Complete original input/expected/control fields retained, plus full section shared premises. Fixed defaultR and stated ordinary dependencies/no interference. Domain only bounded peer reception; historical accepted-baseline wording is not independent acceptance credit.','status':'MANUAL_STATIC_ATOM_RECONCILIATION; HISTORY_APPROVAL_SEPARATE','business':'NOT_EXECUTED'})
d['vector_count']=len(d['vectors']);d['atomic_assertions']=sum(len(x['assertions']) for x in d['vectors']);d['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'added':len(entries),'vectors':d['vector_count'],'atoms':d['atomic_assertions']}))
