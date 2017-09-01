import urllib.request
import json
import datetime
import re
import pprint
import fileuploader as fup


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

def getGastos(ano, mes):
	url="https://app-sisgvconsulta-prd.azurewebsites.net/ws/ws2.asmx/ObterDebitoVereadorJSON?ano=<ano>&mes=<mes>"
	if ano.isdigit() and mes.isdigit():
		if int(ano)>datetime.datetime.today().year:
			print("ano invalido! (",ano,")")
		elif int(mes) not in range(1,13) or int(mes)>datetime.datetime.today().month:
			print("mes invalido! (",mes,")")
		else:
			url=url.replace("<ano>",ano)
			url=url.replace("<mes>",mes)
			print(url)
			resposta=urllib.request.urlopen(url).read()
			jData=json.loads(resposta)
			return jData
	else:
		print("Ano ou mes invalidos!\nano: ",ano,"\tmes: ",mes)
			
			

def gastosToFile(gastosList):
	fhand=open("gastos.json","w")
	for item in gastosList:
		fhand.write(str(item)+"\n")
	fhand.close()
	
def testeGetGastos():
	gastosList=list()
	for i in range(1,datetime.datetime.today().month):
		d = getGastos(str(datetime.datetime.today().year),str(i))
		for item in d:
			gastosList.append(item)
		print(i," - ",len(gastosList))
	
	#gastosToFile(gastosList)
	fup.insertGastos(gastosList)
		

testeGetGastos()
			
# funcoes de testes!
def testeOcupacaoGabinete():
	jData=getOcupacaoGabinete()
	queryjData(jData)
