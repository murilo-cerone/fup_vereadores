class Noticia:

	def __init__(self,site_origem,id_new,ultima_atualizacao,url,tags,chamada,resumo):
		self.url_base=site_origem
		self.id_noticia=id_new
		self.data_atualizacao=ultima_atualizacao
		self.url_noticia=url
		self.tags=tags
		self.headline=chamada
		self.resumo=resumo

	def __str__(self):
		return self.id_noticia+": "+self.chamada

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
