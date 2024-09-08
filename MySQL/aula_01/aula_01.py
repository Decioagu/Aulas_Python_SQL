# PyMySQL - um cliente MySQL feito em Python Puro
# pip install pymysql
# pip install types-pymysql (opcional)
'''
PyMySQL é uma biblioteca leve e pura de Python que facilita a interação com bancos de dados MySQL.
OBS: para execução do programa é necessário esta conectado no banco de dados já criado no SGBD 
de sua escolha
'''

# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

# pip install python-dotenv
'''
O Python-dotenv é uma biblioteca Python que facilita o gerenciamento de variáveis de ambiente 
em seus projetos. Ele permite que você armazene suas variáveis em um arquivo .env separado, 
o que pode ser útil para manter suas configurações confidenciais e organizadas.
'''
import pymysql
import dotenv
import os

# chama arquivo .env (configurações confidenciais)z
dotenv.load_dotenv()

# Conectar ao banco de dados
conexao = pymysql.connect(
    host=os.environ['HOST'],
    user=os.environ['USER'],
    password=os.environ['PASSWORD'],
    database=os.environ['DATABASE'],
)
TABLE_NAME = 'cadastro'

# variável de controle (abrir conexão)
cursor = conexao.cursor() 

# Inserir valores nas colunas da tabela MySQL
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
    'id INT NOT NULL AUTO_INCREMENT, '
    'nome VARCHAR(50) NOT NULL, '
    'idade INT NOT NULL, '
    'PRIMARY KEY (id)'
    ') '
)

conexao.commit() # Adicionar comando na tabela
cursor.close() # Fechar variável de controle
conexao.close() # Fechar conexão com arquivo


