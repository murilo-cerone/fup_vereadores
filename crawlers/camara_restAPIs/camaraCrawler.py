import urllib.request
import json
import datetime
import re
import pprint


def getOcupacaoGabinete():
    ocupacaoGabinete="http://splegisws.camara.sp.gov.br/ws/ws2.asmx/OcupacaoGabineteJSON"
    resposta=urllib.request.urlopen(ocupacaoGabinete).read()
    fhand=open("gabinetes","w")

    jData=json.loads(resposta)
    fhand.write(str(jData))
    fhand.close()
    return jData

def getVereadorFile():
    url='http://www.camara.sp.gov.br/wp-content/uploads/dados_abertos/vereador/vereador.txt'
    arquivo=urllib.request.urlopen(url).read()
    texto=str(arquivo).split('\\r\\n')
    for i in texto:
        print (i)

def convertTimestampToDate(data):
        digitos = re.findall('[0-9]+',data)
        if len(digitos)==1:
            tstmp=int(digitos[0])
            dia=datetime.datetime.utcfromtimestamp(tstmp/1000)
            return dia
            #print(datetime.datetime.fromtimestamp(tstmp).strftime('%Y-%m-%d %H:%M:%S'))

def geraGabineteVereadorFile(lista_dict):
    for dicionario in lista_dict:
        return

def queryjData(jData):
    for d in jData:
        #if d['gabinete']==53 and d['legislatura']==17:
        #    pprint.pprint(d)
        if d['vereador']=='CAIO MIRANDA CARNEIRO':
            pprint.pprint(d)

jData=getOcupacaoGabinete()
queryjData(jData)
