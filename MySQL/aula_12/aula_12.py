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
    cursorclass=pymysql.cursors.SSDictCursor # cursor dicionário
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
cursor.execute(sql) 


print('for 1:')
for linha in cursor.fetchall_unbuffered():
    print(linha)
    if linha['id'] >= 5:
        break

'''
cursor.fetchall_unbuffered(): é um método utilizado em algumas bibliotecas Python para 
interagir com bancos de dados, como MySQL Connector/Python. Ele serve para recuperar 
todas as linhas de um resultado de consulta sem armazená-las na memória de uma só vez.
'''

print()
# cursor.scroll(0, 'absolute') # não é possível executar utilizando "cursor.fetchall_unbuffered()"

print('for 2:')
for linha in cursor.fetchall_unbuffered():
    print(linha)
    
cursor.close() # Fechar variável de controle
conexao.close() # Fechar conexão com arquivo
