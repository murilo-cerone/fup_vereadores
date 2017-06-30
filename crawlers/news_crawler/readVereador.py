import json

fhand=open('vereadores.json','r')
partidos=list()
for line in fhand:
    vereador=json.loads(line)
#    print(vereador["nome"].lower())
    if vereador["partido"] in partidos:
        continue
    else:
        partidos.append(vereador["partido"])

for partido in partidos:
    print(partido)
