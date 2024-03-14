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
import pymysql.cursors

# chama arquivo .env (configurações confidenciais)
dotenv.load_dotenv()

# Conectar ao banco de dados
conexao = pymysql.connect(
    host=os.environ['HOST'],
    user=os.environ['USER'],
    password=os.environ['PASSWORD'],
    database=os.environ['DATABASE'],
    cursorclass=pymysql.cursors.DictCursor # cursor dicionário
)
TABLE_NAME = 'cadastro'

'''
# .fetchone(): Recupera apenas uma linha do conjunto de resultados.
# .fetchmany(n): Recupera linhas do conjunto de resultados "n"
# .fetchall(): Recuperar todas as linhas de banco de dados em uma lista de tuplas.
# iter(cursor): Permite iterar sobre o conjunto de resultados linha por linha.
'''

# variável de controle (abrir conexão)
cursor = conexao.cursor() 

# Lendo os valores com SELECT nados MySQL
sql = (
    f'SELECT * FROM {TABLE_NAME} '
)
quantidade_de_linhas  = cursor.execute(sql) 

print('for 1:')
for linha in iter(cursor):
    print(linha)

print(f'1º: São {quantidade_de_linhas} linhas.')

print(f'2º: São {cursor.rowcount} linhas.')
'''
Rastreia a contagem de linhas: "cursor.rowcount" monitora o número de linhas impactadas 
pela última operação de banco de dados executada no cursor específico.
'''

cursor.scroll(0, 'absolute') # retorna cursor para posição desejada
data = cursor.fetchall()
print(f'3º: São {len(data)} linhas.')

cursor.close() # Fechar variável de controle
conexao.close() # Fechar conexão com arquivo
