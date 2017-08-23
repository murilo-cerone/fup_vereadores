#import urllib3
#testando
#testando2
import urllib.request
from Vereador import Vereador
import re
from bs4 import BeautifulSoup
import json
import datetime

def dicionarioUrls(src_file="urls.txt"):
	urls=dict()
	try:
		fhand=open(src_file)
		for line in fhand:
			print(line)
			kv = line.split('|')
			urls[kv[0]]=kv[1].rstrip()
		#print(urls.keys())
		return urls

	except:
		print('Erro ao ler o arquivo ',src_file)
		return None

def getVereadores():
	hora_coleta=datetime.datetime.now()
	vereadoresL=list()
	urlD=dicionarioUrls()
	url=urlD['camara_vereadores']
	print(url)
	#http=urllib3.connectionpool.HTTPConnectionPool(url,maxsize=1)
	print(hora_coleta,' Atualizando dados dos Vereadores. Utilizando a seguinte url: ',url+'/vereadores/')
	resposta = urllib.request.urlopen('http://'+url+'/vereadores/').read()
	pagina_vereadores=BeautifulSoup(resposta,"html.parser")
	lista_vereadores=pagina_vereadores.findAll('div',{'class':'vereadores-group'})
	articles=lista_vereadores[0].findAll('article')
	for vereador_data in articles:
		vereador_foto_url=vereador_data.find('h2',{'class':'vereador-picture'}).find('img')
#		#print(vereador_foto_url["src"])
		partido_vereador=vereador_data.find('h3').find('img')
		sigla_partido=partido_vereador["title"]
		icone_partido=partido_vereador["src"]
#		#print(sigla_partido,'\t',icone_partido)
		vereador=vereador_data.find('p').find('a')
		nome_vereador=str(vereador.text).strip()
		pagina_vereador=vereador["href"]
		pagina_url=("/"+pagina_vereador.split('/')[3]+"/"+pagina_vereador.split('/')[4])
	#	#print(nome_vereador,' ',pagina_vereador)
		v=Vereador(nome_vereador,sigla_partido,pagina_vereador)
		vereadoresL.append(v)
	return vereadoresL


def getVereadorDetail():
#ToDo - Tratar os contatos ?
	hora_coleta=datetime.datetime.now()
	vereadores=getVereadores()
	urlD=dicionarioUrls()
	url=urlD['camara_vereadores']
	fhand=open('out.json','w')
	for vereador in vereadores:
		#coleta dos dados da pagina do vereador na camara - informacoes de contato e Biografia
		#http=urllib3.connectionpool.HTTPConnectionPool(url,maxsize=1)
		x = vereador.url_camara
		print(x)
#		print(vereador.url_camara)
		resposta=urllib.request.urlopen(x).read()
		pagina_vereador=BeautifulSoup(resposta,"html.parser")
		#print(pagina_vereador.prettify())
		main=pagina_vereador.findAll('div',{'class':'cf','id':'main','role':'main'})

		#Pegar os contatos disponivies
		contatos=main[0].find('div',{'class':'vereador-data'}).findAll('li')
		for contato in contatos:
			tipo=contato.text.split(':',1)[0].lower()
			conteudo=contato.text.split(':',1)[1]
			vereador.contatos[tipo]=conteudo

		#Pegar a biografia
		biografia=main[0].find('span').text
		vereador.biografia=biografia
		json.dump(vereador.resumoVereador(),fhand,ensure_ascii=False)
		fhand.write('\n')

	return vereadores


# Metodos para testes
def testadorParte1():
	lista=getVereadores()
	for x in lista:
		x.apelidos.append('Ze do caixao')
		x.termos.append('Lava Jato')
		#print(x,x.url_camara,x.partido,x.apelidos,x.termos)



def testadorParte2():
	start=datetime.datetime.now()
	print('Teste ',start)
	getVereadorDetail()
	end=datetime.datetime.now()
	print('\n\nFinished! ',end-start)

#Fim dos metodos de teste

#testadorParte1()
vereadoresAtualizados=testadorParte2()
#fhand=open('teste.json','w')
#for vereador in vereadores:
#	json.dump(vereador,fhand)
