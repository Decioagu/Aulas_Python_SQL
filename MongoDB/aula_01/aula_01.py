from pymongo import MongoClient
client = MongoClient("localhost", 27017)

# ver lista de bancos existentes
print(client.list_database_names())

# Aponta para um banco de dados (independente da sua existência)
db = client["Novo_Banco"]

# Cria coleção dentro do banco de dado apontado
db.create_collection("nova_colecao")

# ver lista de bancos existentes
print(client.list_database_names())

