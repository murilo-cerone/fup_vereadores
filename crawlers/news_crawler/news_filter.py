import os
import urllib.request
from bs4 import BeautifulSoup
from Documento import Documento
import sys

def whiteList():
    termos=list()
    fhand=open('whitelist','r')
    for line in fhand:
        termos.append(line.strip())
    return termos

def getFeeds(whitelist):
    feeds=open('feeds.txt','r')
    interessante_feeds=dict()
    for feed in feeds:
        quebra=feed.split('-->')
        headline=quebra[0].strip()
        link=quebra[1].strip()
        #print (headline,link)
        for termo in whitelist:
            if termo in headline and headline not in interessante_feeds:
          #      print(headline+"  interessante!! por causa do termo: "+termo)
                interessante_feeds[headline]=link
          #      x = input("hammer time")
    return interessante_feeds

def getFromG1(sopa):
    cabecalho=sopa.find('div',{'class':'row content-head'})
    titulo=cabecalho.find('h1').text
    subtitulo=cabecalho.find('h2').text
    metadados=sopa.find('div',{'class':'content-meta-info'})
    escritor=metadados.find('span',{'itemprop':'creator'}).text
    dataPublicacao=metadados.find('time',{'itemprop':'datePublished'})['datetime']
    dataAtualizacao=metadados.find('time',{'itemprop':'dateModified'})['datetime']
    paragrafoPrincipal=sopa.find('div',{'class':'mc-column content-text active-extra-styles active-capital-letter'})
    paragrafos=sopa.findAll('div',{'class':'mc-column content-text active-extra-styles '})
    texto=paragrafoPrincipal.text+' '
    fonte='G1 / Globo'
    for item in paragrafos:
        texto=texto+item.text+' '
#    print("Titulo: ",titulo)
#    print("Subtitulo: ",subtitulo)
#    print(escritor)
#    print("Publicado: ",dataPublicacao)
#    print("Atualizado: ",dataAtualizacao)
#    print(texto.strip().lower())
    return[titulo,subtitulo,escritor,dataPublicacao,dataAtualizacao,texto]

def getContent(links):
    for link in links:
        url=links[link]
        html=urllib.request.urlopen(url)
        soup=BeautifulSoup(html,"html.parser")
        doc=getFromG1(soup)
        #print(doc)
        docx=Documento(doc[0],doc[1],doc[2],link,doc[3],doc[4],doc[5])
        dic_new=docx.resumoDocumento()
        print(dic_new)




def test():
    teste=dict()
    url='http://g1.globo.com/sao-paulo/sorocaba-jundiai/noticia/policia-civil-apreende-cerca-de-2-toneladas-de-maconha-em-mairinque.ghtml'
    teste['A']=url
    getContent(teste)

#test()
#sys.exit(0)
links = getFeeds(whiteList())
getContent(links)

