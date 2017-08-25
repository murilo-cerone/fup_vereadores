from bs4 import BeautifulSoup
import urllib.request

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
	
def getStrings(root):
	tag=root.html
	print(tag.attrs)
	#return 
	for s in tag.descendants:
		if s.name=='script':
			continue
		else:
			print(s.string)

#		print ("valor de S: ",dir(s),type(s),s.name)
		#if hasattr(s, 'name'):    # then it's a tag
		#	if s.name == 'script':  # skip it!
				#continue
			#for x in getStrings(s): 
				#yield x
			#else:                     # it's a string!
				#yield s


				