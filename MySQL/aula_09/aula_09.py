# PyMySQL - um cliente MySQL feito em Python Puro
# pip install pymysql
# pip install types-pymysql (opcional)
'''
PyMySQL é uma biblioteca leve e pura de Python que facilita a interação com bancos de dados MySQL.
OBS: para execução do programa é necessário esta conectado no banco de dados já criado no SGBD de sua escolha
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

# chama arquivo .env (configurações confidenciais)
dotenv.load_dotenv()

# Conectar ao banco de dados
conexao = pymysql.connect(
    host=os.environ['HOST'],
    user=os.environ['USER'],
    password=os.environ['PASSWORD'],
    database=os.environ['DATABASE'],
)
TABLE_NAME = 'cadastro'

'''
# .fetchone(): Recupera apenas uma linha do conjunto de resultados.
# .fetchmany(n): Recupera linhas do conjunto de resultados "n"
# .fetchall(): Recuperar todas as linhas de banco de dados em uma lista de tuplas.
# iter(cursor): Permite iterar sobre o conjunto de resultados linha por linha.
'''
# -----------------------------------------------------------------
# variável de controle (abrir conexão)
cursor = conexao.cursor() 

# Lendo os valores com SELECT nados MySQL
sql_01 = (
    f'SELECT * FROM {TABLE_NAME} '
)
cursor.execute(sql_01) 

data = cursor.fetchall() # variável "data"

# Lendo os valores com SELECT nados MySQL
# consulta a variável 
print('for 1:')
for linha in data:
    print(*linha)

print()

# consulta a variável
print('for 2:')
for linha in data:
    print(*linha)

'''
Cursor de banco de dados: Em sistemas de banco de dados, existem cursores roláveis. 
Eles permitem a navegação pelos dados, uma vez solicitado os dados o cursor permanece
na posição conforme a busca solicitada como iterável, não permitindo nova consulta dos 
dados já exibidos.
'''
# -----------------------------------------------------------------
print()

sql_02 = (
    f'SELECT * FROM {TABLE_NAME} '
)
cursor.execute(sql_02) 

# Lendo os valores com SELECT nados MySQL
# consulta diretamente ao cursor
print('for 3:')
for linha in iter(cursor):
    print(*linha)

print()

# consulta diretamente ao cursor
print('for 4:')
for linha in iter(cursor):
    print(*linha)
# -----------------------------------------------------------------
conexao.commit() # Adicionar comando na tabela
cursor.close() # Fechar variável de controle
conexao.close() # Fechar conexão com arquivo
