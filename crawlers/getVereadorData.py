import urllib3
from Vereador import Vereador
import re
from bs4 import BeautifulSoup
import datetime

def dicionarioUrls(src_file="/home/oracle/TCC/crawlers/urls.txt"):
	urls=dict()
	try:
		fhand=open(src_file)
		for line in fhand:
			print(line)
			kv = line.split('|')
			urls[kv[0]]=kv[1].rstrip()
		print(urls.keys())
		return urls
			
	except:
		print('Erro ao ler o arquivo ',src_file)
		return None

def getVereadores():
	hora_coleta=datetime.datetime.now()
	vereadoresL=list()
	urlD=dicionarioUrls()
	url=urlD['camara_vereadores']
	http=urllib3.connectionpool.HTTPConnectionPool(url,maxsize=1)
	print(hora_coleta,' Atualizando dados dos Vereadores. Utilizando a seguinte url: ',url+'/vereadores/')
	resposta = http.request('GET','http://'+url+'/vereadores/')
	pagina_vereadores=BeautifulSoup(resposta.data,"html.parser")
	lista_vereadores=pagina_vereadores.findAll('div',{'class':'vereadores-group'})
#	print(pagina_vereadores.prettify())
#	print(lista_vereadores)
	articles=lista_vereadores[0].findAll('article')
	for vereador_data in articles:
		vereador_foto_url=vereador_data.find('h2',{'class':'vereador-picture'}).find('img')
#		print(vereador_foto_url["src"])
		partido_vereador=vereador_data.find('h3').find('img')
		sigla_partido=partido_vereador["title"]
		icone_partido=partido_vereador["src"]
#		print(sigla_partido,'\t',icone_partido)
		vereador=vereador_data.find('p').find('a')
		nome_vereador=str(vereador.text).strip()
		pagina_vereador=vereador["href"]
	#	print(nome_vereador,' ',pagina_vereador)
		v=Vereador(nome_vereador,sigla_partido,pagina_vereador)
		vereadoresL.append(v)
	return vereadoresL
		

lista=getVereadores()
print(len(lista))
for x in lista:
	print(x)
	
