import pathlib,json,sys
O=pathlib.Path(__file__).parent
R=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
for p,a,b in json.loads((O/'dependency-read-plan.json').read_text())['batches'][int(sys.argv[1])]:
 print(p,a,b)
 lines=(R/p).read_text().splitlines()
 for i in range(a-1,min(b,len(lines))):print(str(i+1)+': '+lines[i])
