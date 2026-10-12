import pathlib,json,datetime
r=pathlib.Path(__file__).resolve().parent.parent
p=json.loads((r/'progress.json').read_text())
p['updated_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
lines=['# 第四轮独立审查进度','',f"更新时间（UTC）：{p['updated_at']}",'','固定B `1f36475d22120a0d1175967d5b17d71fe8311d88`；主会话唯一汇总者。readiness PARTIAL_READY。M01–M12均由新独立CLI审者负责；主会话承担身份、限定历史账、汇总与明确列出的整合检查。','', '所有任务请求 gpt-6-astra / ultra / default，禁Fast；实际回显UNVERIFIED。CLI的请求/日志和真实ID见下表链接，不读取私有会话文件。','', '|模块/角色|状态|真实任务ID / PID|产物与日志入口|','|---|---|---|---|']
summary=[]
for m, task in p['task_plan'].items():
 q=r/'tasks'/(m+'-launch.json')
 if q.exists():
  launch=json.loads(q.read_text());task.update({'task_id':launch['thread_id'],'pid':launch['pid'],'status':launch['status'],'log':launch['log'],'launch_receipt':f'tasks/{m}-launch.json','output_directory':f'modules/{m}','requested':launch['requested'],'actual_echo':'UNVERIFIED'})
  lines.append(f"|{m} {task['name']}|{task['status']}|{task['task_id']} / {task['pid']}|[启动回执](tasks/{m}-launch.json)；[目录](modules/{m}/)|")
  f=r/'modules'/m/'findings.json'
  if f.exists():
   try:
    data=json.loads(f.read_text());fs=data['findings'] if isinstance(data,dict) else data
    task['submitted_finding_ids']=[x['id'] for x in fs]
    summary.extend([f"- {x['id']} ({x.get('disposition','待确认')})：{x['title']}" for x in fs])
   except (ValueError,KeyError):pass
 else:lines.append(f"|{m} {task['name']}|PLANNED|尚未派发|独立审查待启动|")
lines+=['','## 当前候选问题','', '以下仅为模块提交，最终必修需独立反证与汇总裁决；不提前授权整改。','']+ (summary or ['尚未提交成稿。'])
lines+=['','## 已完成的共享工作','','- 131正式文件完整bytes/SHA256/blob验证通过，全部分配主责及共享契约审者。','- R 432 tracked字节验证通过；62原未跟踪文件逐项保护；仅本轮隔离目录可写。','- 229原问题与341 scoped contributions逐项保留限定身份，不冒新语义PASS或执行。','- 54既有交界+8旧链+18新增链固定导航可读；新语义投影另记。','', '## 下一步','','完成各域范围/反证/实际执行与限制；随后新独立审者做交界原证据审查与必修针对性质疑。最终报告和完整中文handoff在去重裁决后生成。未启动下一轮update。','']
p['completed_semantic_modules']=[m for m,t in p['task_plan'].items() if m.startswith('M') and t['status']=='PROCESS_COMPLETED']
p['active_tasks']=[m for m,t in p['task_plan'].items() if t['status'] in ['RUNNING_REQUEST_ACCEPTED','REQUEST_SUBMITTED']]
p['remaining_semantic_modules']=[m for m in [f'M{i:02d}' for i in range(1,13)] if m not in p['completed_semantic_modules']]
p['status']='SEMANTIC_REVIEW_IN_PROGRESS' if p['remaining_semantic_modules'] else 'INDEPENDENT_CHALLENGE_AND_INTEGRATION'
p['blockers']=[]
p['current_issues']=[{'module':m,'candidate_ids':t.get('submitted_finding_ids',[]),'acceptance':'PENDING_INDEPENDENT_COUNTERREVIEW_AND_ROOT_ADJUDICATION'} for m,t in p['task_plan'].items() if t.get('submitted_finding_ids')]
p['next']='Complete remaining source domains '+','.join(p['remaining_semantic_modules'])+'; then independent challenge/junction and final scoped integration. No update has started.'
(r/'progress.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
(r/'progress.md').write_text('\n'.join(lines))
print(json.dumps({m:x['status'] for m,x in p['task_plan'].items()},ensure_ascii=False))
