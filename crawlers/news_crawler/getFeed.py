import feedparser
from bs4 import BeautifulSoup

urls=[
'http://tecnologia.uol.com.br/ultnot/index.xml'
,'http://www.portalconscienciapolitica.com.br/rss/all.xml'
,'https://www.reddit.com/r/saopaulo/.rss'
,'http://pox.globo.com/rss/g1/sao-paulo/'
]
fhand=open('feeds.txt','w')
for url in urls:
	feed=feedparser.parse(url,'charset=utf8')
	print(feed['feed']['title'])

	for item in feed.entries:
		texto = item.title+' --> '+item.link
		textoUtf8=texto+'\n'
		fhand.write(textoUtf8)
