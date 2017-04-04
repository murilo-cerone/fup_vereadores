class Vereador:

	def __init__(self,n,p,url):
		self.nome=n
		self.partido=p
		self.url_camara=url
		self.apelidos=list()
		self.termos=list()
		self.contatos=dict()
		self.biografia=None

	def __str__(self):
		return self.nome

	def resumoVereador(self):
		resumo=dict()
		resumo['nome']=self.nome
		resumo['partido']=self.partido
		resumo['pagina camara']=self.url_camara
		resumo['apelidos']=self.apelidos
		resumo['termos relacionados']=self.termos
		resumo['dados de contato']=self.contatos
		resumo['biografia']=self.biografia
		return resumo
