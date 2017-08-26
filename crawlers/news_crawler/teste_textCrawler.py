from bs4 import BeautifulSoup
import urllib.request
import re

fhand=open('feeds.txt','r')

def getUrls():
	urls=list()
	for line in fhand:
		x=line.split('-->')
		urls.append(x[1].strip())
	return urls 
	
def getText(url):
	try:
		html=urllib.request.urlopen(url)
	except:
		print("Erro ao abrir a url",url)
		return None
	try:
		soup=BeautifulSoup(html,"html.parser")
		return soup
		#textos = soup.findAll(recursive=False,text=True)
	except:
		print("erro ao fazer parsing ")
		return None
	
def visible(element):
	if element.parent.name in ['style','script','[document]','head','title']:
		return False
	elif re.match('<!--.*-->',str(element.encode('utf-8'))):
		return False
	else:
		return True
		
	
def getStrings(root):
	conteudos=list()
	if root:
		tag=root.body
		data=tag.findAll(text=True)
		resultado=filter(visible,data)
		l = list(resultado)
		for text in l:
			if len(text.strip())>100:
				print(text)
				print('\n------------------------------------------------------------------\n')
		
		return
		tags=tag.descendants
		for t in tags:
			x = input('')
			print(t)
	return 


				
urls=getUrls()
i=0
for url in urls:
	getStrings(getText(url))
	i=i+1
	if i>2:
		break