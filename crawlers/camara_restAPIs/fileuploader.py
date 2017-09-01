import pymongo

def connect():
	connection_string="mongodb://mcerone:murilo123#@cluster0-shard-00-00-kywrh.mongodb.net:27017,cluster0-shard-00-01-kywrh.mongodb.net:27017,cluster0-shard-00-02-kywrh.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"

	try:
		client = pymongo.MongoClient(connection_string)
		return client
	except:
		print("connection to mongo failed")


def connGastosDB(client):
	try:
		db = client['gastos']
		collection=db['expenses']
		return collection
	except:
		print("failed to connect/create gastos db")
		return None
	
def insertGastos(gastos):
		try:
			c = connect()
			col=connGastosDB(c)
			result = col.insert_many(gastos)
			print(len(result.inserted_ids),' registros inseridos')
		except Exception as e:
			print(str(e))
			print("Falha ao inserir os gastos")
			

