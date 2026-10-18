from pathlib import Path
import importlib.util,json
p=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("inert_sf2",p/"audit_resources.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
b=Path("/workspace/pokemon-essentials/soundfont.sf2").read_bytes()
r=m.soundfont(b)
r["current_identity"]={"B8":"fd1df570cad987dc3852a3b958f03916e317f7fe","R":"8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b","helper_origin":"historical data-only standard-library parser, inspected in full; its old PIN is not current acceptance"}
(p/"soundfont-full-audit.json").write_text(json.dumps(r,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(r["summary"],ensure_ascii=False))
