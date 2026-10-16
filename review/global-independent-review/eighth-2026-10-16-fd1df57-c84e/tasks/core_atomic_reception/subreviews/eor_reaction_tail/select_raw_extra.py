from pathlib import Path
import re,json,sys
r=Path("/workspace/pokemon-essentials")
sets={"PBS/items.txt":{"AGUAVBERRY","APICOTBERRY","BERRYJUICE","FIGYBERRY","GANLONBERRY","IAPAPABERRY","LANSATBERRY","LIECHIBERRY","MAGOBERRY","MICLEBERRY","ORANBERRY","PETAYABERRY","SALACBERRY","SITRUSBERRY","STARFBERRY","WIKIBERRY","ASPEARBERRY","CHERIBERRY","CHESTOBERRY","LUMBERRY","MENTALHERB","PECHABERRY","PERSIMBERRY","RAWSTBERRY","LEPPABERRY"},"PBS/moves.txt":{"TRICKROOM","GRAVITY","WATERSPORT","MUDSPORT","WONDERROOM","MAGICROOM","ELECTRICTERRAIN","GRASSYTERRAIN","MISTYTERRAIN","PSYCHICTERRAIN","UPROAR"}}
for path,names in sets.items():
 lines=(r/path).read_text(encoding="utf-8-sig").splitlines()
 starts=[i for i,x in enumerate(lines) if re.match(r"^\[.+\]$",x)]+[len(lines)]
 for i,j in zip(starts,starts[1:]):
  name=lines[i][1:-1].split(",")[0]
  if name in names:
   print(json.dumps({"path":path,"range":[i+1,j],"key":lines[i]},ensure_ascii=False))
   print("\n".join(lines[i:j]))
