#!/usr/bin/env python3
"""Independent negative probes of real Git descendants and actual apply path."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('source_audit_helpers',Path(__file__).with_name('source-audit.py'))
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

def main():
    results={'candidate':a.CAND,'current':a.FINAL,'independent_static_only':True,'started_utc':a.now(),'checks':[]}
    with tempfile.TemporaryDirectory(prefix='r3-independent-source-') as temporary:
        root=Path(temporary);inv=root/a.REL;shutil.copytree(a.INV,inv)
        a.git('init','--quiet',str(root));common=a.git('rev-parse','--path-format=absolute','--git-common-dir').decode().strip();(root/'.git/objects/info/alternates').write_text(str(Path(common)/'objects')+'\n')
        env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','GIT_AUTHOR_NAME':'Independent static review fixture','GIT_AUTHOR_EMAIL':'review@example.invalid','GIT_COMMITTER_NAME':'Independent static review fixture','GIT_COMMITTER_EMAIL':'review@example.invalid','GIT_AUTHOR_DATE':'2026-10-17T00:00:00Z','GIT_COMMITTER_DATE':'2026-10-17T00:00:00Z'}
        r=a.module('source_r3_fixture',inv/'routing.py');oldpath=inv/'r2-independent-fixture.py';oldpath.write_bytes(a.blob(a.R2,str(a.REL/'routing.py')));old=a.module('source_r2_fixture',oldpath)
        m=a.read(inv/'routing-manifest.json');c=a.read(inv/'section-coverage.json');registry=a.read(inv/'accepted-source-updates.json');baseline=r.errors(m,c,registry)
        assert not baseline,baseline
        def descendant(path,content):
            b=a.git('hash-object','-w','--stdin',cwd=root,data=content,env=env).decode().strip();a.git('read-tree',a.FINAL,cwd=root,env=env);a.git('update-index','--cacheinfo','100644,'+b+','+path,cwd=root,env=env);tree=a.git('write-tree',cwd=root,env=env).decode().strip();commit=a.git('commit-tree',tree,'-p',a.FINAL,cwd=root,data=b'Independent static negative fixture\n',env=env).decode().strip();return commit,b
        def currentize(commit,changed_path,changed_bytes,stale_document=None):
            mm=copy.deepcopy(m);mm['current_snapshot']['commit']=commit;mm['current_snapshot']['formal_tree']=a.git('rev-parse',commit+':'+a.FORMAL.rstrip('/'),cwd=root).decode().strip();lines=changed_bytes.decode().splitlines(keepends=True)
            for d in mm['documents']:
                if d['document_id']==stale_document:continue
                cur=d['current_applicability'];cur['snapshot_commit']=commit;cur['identity']=r.identity(commit,cur['path'])
            for f in mm['features']:
                cur=f['current_applicability'];cur['snapshot_commit']=commit;ident=r.identity(commit,cur['document']);cur['locator']['file_sha256']=ident['sha256'];cur['locator']['file_git_blob']=ident['git_blob']
                if cur['document']==changed_path:cur['locator']['unit_sha256']=r.digest(''.join(''.join(lines[x-1:y]) for x,y in cur['locator']['line_ranges']).encode())
            return mm
        path=a.FORMAL+'generic-kernel/wp04-pbs-lifecycle.md';content=r.blob(a.FINAL,path);lines=content.decode().splitlines(keepends=True);lines[195]=lines[195].rstrip('\n')+' [INDEPENDENT UNRECEIPTED CONTENT]\n';changed=''.join(lines).encode();commit,b=descendant(path,changed);mm=currentize(commit,path,changed);oe=old.errors(mm,c,registry);ne=r.errors(mm,c,registry)
        results['checks'].append({'finding':'SOURCE-R2-001','case':'real descendant same accepted path receives unaccepted bytes; all actual identities and locators recomputed','descendant':commit,'path':path,'old_errors':oe,'new_errors':ne,'passed':not oe and any('lack matching ACCEPTED target identity' in e for e in ne)})
        active={f['document_id'] for f in m['features']};meta=next(d for d in m['documents'] if d['document_id'] not in active and d['upstream']['accepted_events']);path=meta['current_applicability']['path'];lines=r.blob(a.FINAL,path).decode().splitlines(keepends=True);ix=next(i for i,x in enumerate(lines) if x.strip() and not x.startswith('#'));lines[ix]=lines[ix].rstrip('\n')+' [INDEPENDENT METADATA CONTENT]\n';changed=''.join(lines).encode();commit,b=descendant(path,changed)
        for name,stale in [('metadata-only stale document snapshot',meta['document_id']),('metadata-only synchronized identity still requires exact accepted bytes',None)]:
            mm=currentize(commit,path,changed,stale);oe=old.errors(mm,c,registry);ne=r.errors(mm,c,registry);token='current applicability snapshot mismatch' if stale else 'lack matching ACCEPTED target identity';results['checks'].append({'finding':'SOURCE-R2-001','case':name,'descendant':commit,'path':path,'active_features':0,'old_errors':oe,'new_errors':ne,'passed':any(token in e for e in ne) and (any(token in e for e in oe) if stale else not oe)})
        tools=inv/'revisions/r3/tools';backfill=a.module('source_actual_apply_fixture',tools/'backfill-accepted-sources.py');build=backfill.build_current_coverage
        def invalid(snapshot,sections):
            value=build(snapshot,sections);value['sections'][-1]['metadata_reason']=None;return value
        backfill.build_current_coverage=invalid
        names=['routing-manifest.json','accepted-source-updates.json','current-section-coverage.json','section-coverage.json']
        before={n:a.sha((inv/n).read_bytes()) for n in names};archives_before={p.name:a.sha(p.read_bytes()) for p in tools.glob('source-backfill-input-*.json.gz')};previous=sys.argv;sys.argv=[str(tools/'backfill-accepted-sources.py'),'apply','--snapshot',a.FINAL,'--new-mapping',str(inv/'revisions/r3/new-heading-mappings.json')];caught=None;stdout=io.StringIO();stderr=io.StringIO();started=a.now()
        try:
            with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):backfill.main()
        except AssertionError as e:caught=str(e)
        finally:sys.argv=previous
        after={n:a.sha((inv/n).read_bytes()) for n in names};archives_after={p.name:a.sha(p.read_bytes()) for p in tools.glob('source-backfill-input-*.json.gz')}
        results['checks'].append({'finding':'SOURCE-R2-002','case':'actual apply, invalid final section null; core/archive refuse before write','started_utc':started,'ended_utc':a.now(),'actual_argv':[str(tools/'backfill-accepted-sources.py'),'apply','--snapshot',a.FINAL,'--new-mapping',str(inv/'revisions/r3/new-heading-mappings.json')],'injected_pointer':'/sections/2703/metadata_reason','exception':caught,'stdout':stdout.getvalue(),'stderr':stderr.getvalue(),'core_before':before,'core_after':after,'archives_before':archives_before,'archives_after':archives_after,'passed':bool(caught and 'invalid prospective current coverage' in caught) and before==after and archives_before==archives_after})
        check=a.module('source_governance_fixture',tools/'current-coverage-check.py');data=a.read(inv/'current-section-coverage.json');schema=a.read(inv/'current-section-coverage.schema.json');positive=check.check(data,m,schema)
        allowed=check.governance_headings();paths={x[1] for x in allowed};actual_global=[s for s in data['sections'] if s['coverage_scope']=='ALL_FORMAL_FEATURES'];results['checks'].append({'finding':'SOURCE-R2-003','case':'all2704 current rows valid; exact46 exemptions within3 governance files','errors':positive,'allowlist_headings':len(allowed),'allowlist_paths':sorted(paths),'actual_global_headings':len(actual_global),'passed':not positive and len(allowed)==46 and len(paths)==3 and len(actual_global)==46 and all(check.allowed_governance(s,a.FINAL) for s in actual_global)})
        ordinary=copy.deepcopy(data);s=next(x for x in ordinary['sections'] if x['path']==a.FORMAL+'combat-requirements/wp39-battle-context-and-participants.md' and x['anchor']=='4-战斗初始化与布局');s.update(feature_refs=[],metadata_refs=[],coverage_scope='ALL_FORMAL_FEATURES');errors=check.check(ordinary,m,schema);results['checks'].append({'finding':'SOURCE-R2-003','case':'ordinary behavior heading cannot use global exemption to erase both consumers','errors':errors,'passed':any('requires fixed governance' in x for x in errors) and any('unmapped current heading' in x for x in errors)})
        # Even an existing governance heading loses its exemption when document bytes change.
        path=a.FORMAL+'README.md';lines=r.blob(a.FINAL,path).decode().splitlines(keepends=True);ix=next(i for i,x in enumerate(lines) if x.strip() and not x.startswith('#'));lines[ix]=lines[ix].rstrip('\n')+' [INDEPENDENT GOVERNANCE CONTENT]\n';changed=''.join(lines).encode();commit,b=descendant(path,changed);mm=currentize(commit,path,changed);dd=copy.deepcopy(data);dd['snapshot']=mm['current_snapshot'];errors=check.check(dd,mm,schema);results['checks'].append({'finding':'SOURCE-R2-003','case':'fixed governance title cannot exempt changed governance file bytes','descendant':commit,'path':path,'errors':errors,'passed':any('requires fixed governance' in x for x in errors)})
        results['baseline_errors']=baseline;results['ended_utc']=a.now();results['all_passed']=all(x['passed'] for x in results['checks'])
    a.save('source-independent-probes.json',results);a.save('source-independent-probe-command-io.json',a.LOG)
    print(json.dumps({'all_passed':results['all_passed'],'checks':[{'finding':x['finding'],'case':x['case'],'passed':x['passed']} for x in results['checks']]},ensure_ascii=False,indent=2))
    return int(not results['all_passed'])

if __name__=='__main__':sys.exit(main())
