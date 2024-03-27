from pymongo import MongoClient
import dotenv
import os

# chama arquivo .env (configurações confidenciais)
dotenv.load_dotenv()

class DBConnectionHandler:
    def __init__(self) -> None:
        # arquivo .env (configurações confidenciais)
        self.host=os.environ['HOST'],
        self.port=os.environ['PORT'],
        self.user_name=os.environ['USER_NAME'],
        self.password=os.environ['PASSWORD'],
        self.db_name=os.environ['DB_NAME'],
        self.collecton=os.environ["COLLECTION"]

        # endereço do banco
        self.__connection_string = f'mongodb://{str(*self.host)}:{str(*self.port)}/'

        self.__client = None
        self.__db_connection = None

    # conectar ao banco
    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[str(*self.db_name)]
        print()
        print(f'Lista de collecton => {self.__client.list_database_names()}')
        print()
        print(f'Coleção => {self.__db_connection}')
        print()

    # def get_db_connection(self):
    #     return self.__db_connection

    # def get_db_client(self):
    #     return self.__client
    
    # get da coleção (auxiliar)
    def my_collection(self):
        self.__conexao = self.__db_connection.get_collection(self.collecton)
        return self.__conexao
    
    # ============ CRUD ============

    # inserir documento (Create)
    def set_data(self, dados: dict):
        conexao = self.my_collection()
        registro = conexao.insert_one(dados)
        print(f'Novo registro inserido com sucesso, ID: "{registro.inserted_id}"')
    
    # buscar documento (Read)
    def get_data(self, procurar: dict | None):
        conexao = self.my_collection()

        # inserir filtro se houver
        if procurar == None:
            filtro = {}
        else:
            filtro = procurar

        # buscar documento por filtro se houver
        registros = conexao.find(filtro)
        
        # variável auxiliar de retorno de informação (dados)
        vazio = True

        # ler registro (dados)
        for reg in registros:
            print(reg)
            vazio = False
        
        # se não haver retorno de informação (dados)
        if vazio:
            print('Informação não encontrada!')
            print()

    # atualizar documento (Update)
    def update_data(self, procurar: dict | None, dados: dict):
        conexao = self.my_collection()

        # inserir filtro se houver
        if procurar == None:
            filtro = {}
        else:
            filtro = procurar

        novos_valor = {"$set": dados}

        # buscar documento por filtro se houver
        registro = conexao.update_one(filtro, novos_valor)
        
        # Imprimindo o número de documentos atualizados
        print(f"{registro.modified_count} documento atualizado.")

    # deletar documento (Delete)
    def del_data(self, procurar: dict | None):
        conexao = self.my_collection()

        # inserir filtro se houver
        if procurar == None:
            filtro = {}
        else:
            filtro = procurar

        # buscar documento por filtro se houver
        registro = conexao.delete_one(filtro)
        
        # informa se registro foi deletado
        if registro.deleted_count == 1:
            print("Documento excluído com sucesso!")
        else:
            print("Nenhum documento encontrado para exclusão.")
