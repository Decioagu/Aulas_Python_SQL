from connection import DBConnectionHandler

# conectar ao banco de dados
teste_de_conexao = DBConnectionHandler()
teste_de_conexao.connect_to_db()

# ============ CRUD ============
# dados para inserir
dados1 = {
            "title": "Post Title 9",
            "body": "Body of post.",
            "category": "Technology",
            "likes": 9,
            "tags": ["novo", "velho"]
        }

# ========== inserir documento (Create) =========   
teste_de_conexao.set_data(dados1)

# filtro de pesquisa 
filtro1 = {"title":"Post Title 12"}

# ========== buscar documento (Read) ==========
teste_de_conexao.get_data(filtro1)

# filtro de pesquisa 
filtro2 = {"title":"Post Title 30"}

# dados de atualização
dados2 = {
            "title": "Post Title 1",
            "body": "Body of post.",
            "category": "Technology",
            "likes": 1,
            "tags": ["novo", "velho"]
        }

# ========== atualizar documento (Update) ==========
teste_de_conexao.update_data(filtro2, dados2)

# ========== deletar documento (Delete) =========
teste_de_conexao.del_data(filtro1)


