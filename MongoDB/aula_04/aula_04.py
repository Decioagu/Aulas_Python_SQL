'''
No MongoDB, Write Concern (Preocupação de Gravação) define o nível de confirmação 
que você deseja para operações de gravação. Isso significa que você pode especificar 
o quão certo você precisa estar de que seus dados foram gravados com sucesso antes 
que a operação seja considerada concluída.

Existem diferentes níveis de Write Concern disponíveis, cada um com suas próprias 
implicações de desempenho e confiabilidade:

    # w: "0" (Sem confirmação): Este é o nível de Write Concern mais rápido, mas também o 
    menos confiável. Com w: "0", o MongoDB não retorna nenhum erro se a gravação falhar. 
    Isso significa que seus dados podem ser perdidos sem que você saiba.

    # w: "1" (Local): Este nível de Write Concern garante que a gravação seja bem-sucedida 
    em pelo menos um nó do replica set. Isso significa que seus dados não serão perdidos 
    se um único nó falhar. No entanto, se a maioria dos nós do replica set falhar antes 
    que a replicação seja concluída, seus dados poderão ser perdidos.

    # w: "majority" (Maioria): Este é o nível de Write Concern padrão no MongoDB. 
    Com w: "majority", o MongoDB garante que a gravação seja bem-sucedida na maioria dos 
    nós do replica set antes de retornar um sucesso. Isso significa que seus dados serão 
    protegidos contra falhas na maioria dos nós.  O "wtimeout" evita esse cenário interrompendo 
    a operação e retornando um erro após o tempo limite especificado. Não garante falha: 
    Mesmo que o "wtimeout" seja atingido, isso não significa necessariamente que a gravação 
    falhou. É possível que a gravação tenha sido bem-sucedida em alguns nós antes do tempo 
    limite, mas não na maioria exigida pelo Write Concern.

    # w: "tags" (Etiquetas): Este nível de Write Concern permite que você especifique um 
    conjunto de tags e garanta que a gravação seja bem-sucedida em pelo menos um nó com 
    as tags correspondentes. Isso é útil para ambientes em que você deseja direcionar 
    suas gravações para nós específicos.

    # w: "replicações" (Replicação): Este nível de Write Concern garante que a gravação 
    seja replicada para um número especificado de membros do replica set antes de 
    retornar um sucesso. Isso é útil para ambientes em que você precisa garantir que 
    seus dados sejam replicados para um número mínimo de nós antes de considerá-los seguros
'''

from pymongo import MongoClient, WriteConcern
from pymongo.collection import Collection

# Conectar ao servidor MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Acessar um banco de dados específico
db = client['meu_banco_de_dados']

# Configurar a coleção com write concern
# Exemplo de write concern com w=1 (confirmação da escrita por um nó)
collection = Collection(db, 'minha_colecao', write_concern=WriteConcern(w=1))

# Inserir um documento com o write concern configurado
resultado = collection.insert_one({'nome': 'João', 'idade': 30})
print(f'Documento inserido com o ID: {resultado.inserted_id}')

# Exemplo de write concern com w=majority (confirmação da escrita pela maioria dos nós)
collection_majority = Collection(db, 'minha_colecao', write_concern=WriteConcern(w='majority'))

# Inserir outro documento com o write concern configurado para majority
resultado_majority = collection_majority.insert_one({'nome': 'Maria', 'idade': 25})
print(f'Documento inserido com o ID: {resultado_majority.inserted_id}')

# ------------------------------------------------------------------------------------------------

from pymongo import MongoClient, WriteConcern
from pymongo.errors import WriteConcernError

# Conectar ao servidor MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Selecionar o banco de dados e a coleção
db = client['meu_banco_de_dados']
collection = db['minha_colecao']

# Definir o WriteConcern com wtimeout
write_concern = WriteConcern(w=1, wtimeout=1000)  # Espera confirmação de escrita de 1 nó, com timeout de 1000 ms

# Aplicar o WriteConcern à coleção
collection_with_wc = collection.with_options(write_concern=write_concern)

# Inserir um documento com o WriteConcern especificado
try:
    result = collection_with_wc.insert_one({"nome": "Teste", "valor": 123})
    print("Documento inserido com ID:", result.inserted_id)
except WriteConcernError as e:
    print("Erro de WriteConcern:", e)

# Fechar a conexão com o MongoDB
client.close()
