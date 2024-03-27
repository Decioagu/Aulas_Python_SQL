from bson.objectid import ObjectId
from pymongo import MongoClient
from datetime import timedelta, datetime

connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
print("<===============================================================>")
# ver lista de bancos existentes
print(client.list_database_names())
print("<===============================================================>")
# acessar o banco de dados
db = client["decio"]
print(db)
print("<===============================================================>")
# acessar coleção do banco
collection = db.get_collection("teste")
print(collection)
print("<===============================================================>")

# ================================================================================
# =================================== CRUD =======================================
# ================================================================================

# ===================================(Create)=====================================
# Inserir documento no banco de dados
inserir = collection.insert_one({
    "title": "Post Title 8",
    "body": "Body of post.",
    "category": "Technology",
    "likes": 8,
    "tags": ["ovo", "zero"]
})
print(inserir)
# ====================================(Read)======================================

# buscar documento
registros = collection.find({})
# ler documento
for reg in registros: 
    print(reg)

print("<===============================================================>")
# eliminar "_id" da busca
registro1 = collection.find_one({}, {"_id": 0}) 
print("registro1 =",registro1)

print("<===============================================================>")
# somente "_id" da busca
registro2 = collection.find_one({}, {"_id": 1}) 
print("registro2 =",registro2)

print("<===============================================================>")
# verifica no banco se existe chave "likes" no documento
registro3 = collection.find_one({"likes": {"$exists": True}}) 
print("registro3 =",registro3)

print("<===============================================================>")
# verifica no banco se existe chave "cpf" no documento
registro4 = collection.find_one({"cpf": {"$exists": True}})
print("registro4 =",registro4) 

print("<===============================================================>")
# ordenar dados pelo "title" crescente
registro5 = collection.find({}).sort(["likes"])
for reg in registro5: 
    print(reg)

print("<===============================================================>")
# ordenar dados pelo "title" decrescente
registro6 = collection.find({}, {"_id": 0, "likes": 1, "title": 1}).sort([("likes",-1)])
for reg in registro6: 
    print(reg)

print("<===============================================================>")
# buscar dados "AND", e "OR"
registro7 = collection.find({"category": "Technology",  "$or": [{"likes": {"$lt": 10}}, {"likes": {"$gt": 20}}]}, {"_id": 0, "likes": 1, "title": 1, "category": 1} ).sort([("likes")])
for reg in registro7: 
    print(reg)

print("<===============================================================>")
# buscar dados pelo "_id" (necessário biblioteca)
registro8 = collection.find_one({ '_id': ObjectId('65fe513bad9b68d89d22c505')})
print("registro8 =",registro8) 

print("<===============================================================>")

# ====================================(Update)======================================
# atualizar um documento
meu_filtro9 = {'title': 'Post Title 45'}
atualizar9 = {'title': 'Post Title 50'}
novos_valor9 = {"$set": atualizar9}                               
registro9 = collection.update_one(meu_filtro9, novos_valor9)
# Imprimindo o número de documentos atualizados
print(f"{registro9.modified_count} documento atualizado.")

print("<===============================================================>")
# atualizar vários documento
meu_filtro10 = {'title': 'Post Title 31'}
atualizar10 = {'title': 'Post Title 35'}
novos_valor10 = {"$set": atualizar10}
 # collection.update_one(FILTRO, {"$set": UPDATE})                               
registro10 = collection.update_many(meu_filtro10, novos_valor10)
# Imprimindo o número de documentos atualizados
print(f"{registro10.modified_count} documento atualizado.")

print("<===============================================================>")
# inserir "novos dados" em documento
meu_filtro11 = {'title': 'Post Title 45'}
atualizar11 = {'likes': 'campo'}
novos_valor11 = {"$set": atualizar10}
 # collection.update_one(FILTRO, {"$set": UPDATE})                               
registro11 = collection.update_many(meu_filtro11, novos_valor11)
# Imprimindo o número de documentos atualizados
print(f"{registro11.modified_count} documento atualizado.")

print("<===============================================================>")
# atualizar vários documento (faz uma soma no campo numérico na chave "likes")
valor12 = 5
meu_filtro12 = {'title': 'Post Title 45'}
atualizar12 = {'likes': valor12}
novos_valor12 = {"$inc": atualizar12}
 # collection.update_one(FILTRO, {"$set": UPDATE})                               
registro12 = collection.update_many(meu_filtro12, novos_valor12)
# Imprimindo o número de documentos atualizados
print(f"{registro12.modified_count} documento atualizado.")

# ====================================(Delete)======================================
# deletar um documento
meu_filtro13 = {'title': 'Post Title 22'}
registro13 = collection.delete_one(meu_filtro13)

# informa se registro foi deletado
if registro13.deleted_count == 1:
    print("Documento excluído com sucesso!")
else:
    print("Nenhum documento encontrado para exclusão.")
    
# ====================================(índice TTL)======================================
'''
Um índice TTL (Time-to-Live) é um tipo especial de índice de campo único que o MongoDB 
usa para remover automaticamente documentos de uma coleção após um período de tempo 
especificado. Esse é um recurso valioso para gerenciar coleções que contêm dados com 
uma vida útil limitada, como:

# Logs
# Dados da sessão
# Conteúdo do carrinho de compras
# Dados temporários# 
'''
# tempo de duração do registro de 10s
tempo_de_vida = timedelta(seconds=10)
collection.create_index("data_de_criacao", expireAfterSeconds=tempo_de_vida.seconds)
documento = { "nome": "Arnaldo", "idade": 30, "data_de_criacao": datetime.utcnow() -timedelta(hours=3)}
registro15 = collection.insert_one(documento)
print(registro15.inserted_id)
