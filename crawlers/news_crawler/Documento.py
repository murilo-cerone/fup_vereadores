class Documento:

	def __init__(self,titulo,subtitulo,autor,url,dataP,dataA,conteudo,src_id=None,tags=None):
		self.titulo = titulo
		self.subtitulo = subtitulo
		self.autor = autor
		self.url = url
		self.dataPublicacao = dataP
		self.dataAtualizacao = dataA
		self.conteudo = conteudo
		self.src_id=src_id
		self.tags=tags

	def __str__(self):
		return self.titulo+" publicado em "+self.dataPublicacao+" por "+self.autor

	def resumoDocumento(self):
		resumo=dict()
		resumo['titulo']=self.titulo
		resumo['subtitulo']=self.subtitulo
		resumo['autor']=self.autor
		resumo['url']=self.url
		resumo['data publicacao']=self.dataPublicacao
		resumo['data atualizacao']=self.dataAtualizacao
		resumo['conteudo']=self.conteudo
		resumo['src_id']=self.src_id
		resumo['tags']=self.tags
		return resumo

