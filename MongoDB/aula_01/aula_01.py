from pymongo import MongoClient
client = MongoClient("localhost", 27017)

# ver lista de bancos existentes
print(f"\nLista de banco de dados: {client.list_database_names()}")

# Aponta para um banco de dados (independente da sua existência)
db = client["Novo_Banco"]
print(f'\nBanco de dados atual: {db}\n')

# Cria coleção dentro do banco de dado apontado
try: 
    db.create_collection("nova_colecao") # ocorre erro caso banco já exista
except Exception as erro:
    print(f"Banco já existe: {erro.__class__}") # <class 'pymongo.errors.CollectionInvalid'>
    print()

# ============== acessar coleção do banco ==============
collection = db.get_collection("nova_colecao")
print(f"Coleção: {collection}")

# ========== buscar documento (Read) ==========
print("\nregistro1")
registro1 = collection.find()

for reg in registro1:
        print(reg)
        
# ============== dados para inserir ==============
dados1 = {
            "_id" : "Meu_id_03",
            "nome": "Décio Santana",
            "idade": 43
        }
# "_id" <= personaliza ID inserido | caso já exista ocorrerá um erro
# ========== inserir documento (Create) =========   
collection.insert_one(dados1)

# ========== buscar documento (Read) ==========
print("\nregistro2")
registro2 = collection.find()

for reg in registro2:
        print(reg)

# ========== atualizar documento (Update) ==========
dados2 = {
            "nome": "Luana"
        }
novos_valor = {"$set": dados2} 
collection.update_one(dados1, novos_valor)

# ========== buscar documento (Read) ==========
print("\nregistro3")
registro3 = collection.find()

for reg in registro3:
        print(reg)

# ========== atualizar documento (Update) ==========
dados3 = {
            "idade": 15
        }
novos_valor = {"$set": dados3} 
collection.update_one(dados2, novos_valor)

# ========== buscar documento (Read) ==========
print("\nregistro4")
registro4 = collection.find()

for reg in registro4:
        print(reg)

# ============== dados para inserir ==============
dados4 = {
            "atualizado": True
        }
collection.replace_one(dados3, dados4)
# .replace_one() altera TODO o documento exceto _id gerado 

# ========== buscar documento (Read) ==========
print("\nregistro5")
registro5 = collection.find()

for reg in registro5:
        print(reg)

# ========== deletar documento (Delete) =========
# collection.delete_many({})

# ========== buscar documento (Read) ==========
print("\nregistro6\n")
registro6 = collection.find()

for reg in registro6:
        print(reg)
