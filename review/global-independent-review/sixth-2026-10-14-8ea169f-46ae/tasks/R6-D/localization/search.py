"""Run an explicit read-only repository search and preserve stdout for audit."""
import audit,subprocess,sys,json
label=sys.argv[1];args=sys.argv[2:]
assert args[0]=='rg'
r=subprocess.run(args,cwd=audit.ROOT,text=True,capture_output=True)
(audit.OUT/(label+'.stdout')).write_text(r.stdout)
(audit.OUT/(label+'.stderr')).write_text(r.stderr)
audit.event('search',argv=args,returncode=r.returncode,stdout_file=label+'.stdout',stdout_sha256=audit.sha(r.stdout.encode()),extent='inventory_only; displayed hits not whole-file semantics')
print(r.stdout,end='');print(r.stderr,end='',file=sys.stderr)
