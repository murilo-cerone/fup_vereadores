import urllib.request
import re
from bs4 import BeautifulSoup
import json
import datetime
import sys
from Documento import Documento

url="http://www.camara.sp.gov.br/sala-de-imprensa/noticias/"

def getPage(url):
    resposta = urllib.request.urlopen(url).read()
    sopinha=BeautifulSoup(resposta,"html.parser")

    return sopinha

def getNews(sopa):
    news=dict()
    tagsList=list()
    tagsIn=sopa.findAll('div',{'class':"two-column-main cf"})
    tags=tagsIn[0].findAll('article')
    for noticia in tags:
        header=noticia.find('header')
        section=noticia.find('section')
        print(noticia["id"])
        atualizacao=header.find('time').text
        for marcador in header.findAll('a'):
            tagsList.append(marcador.text)
        resumo=header.find('h1').text
        titulo=header.find('h1').find('a')['title']
        link=header.find('h1').find('a')["href"]
        print(atualizacao,'\n',tagsList,'\n',titulo,'\n',link,'\n',resumo)
        tagsList=[]
        print(section.text)

#fazer um metodo que vai ler a noticia no site da camara e salvar o texto. A pagina da noticia tem um "article" que usa o id da noticia como id!!
#Montar o Documento correspondente
#fazer um metodo que escreve todos os documentos em arquivos (talvez soh imprimir dicionarios num mesmo arquivo seja suficiente)

getNews(getPage(url))
sys.exit(0)

