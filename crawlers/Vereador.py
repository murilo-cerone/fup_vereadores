class Vereador:

	nome=None
	partido=None
	url_camara=None

	def __init__(self,n,p,url):
		self.nome=n
		self.partido=p
		self.url_camara=url

	def __str__(self):
		return self.nome

	def getNome(self):
		return self.nome

	def getPartido(self):
		return self.partido
	
	def getUrl(self):
		return self.url_camara


