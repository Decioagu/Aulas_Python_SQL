# video aula 393
import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE) # conectar o arquivo (criar)
cursor = connection.cursor() # variável de controle

# Consultar toda da tabela SQLite
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

'''
# .fetchone(): Recupera apenas uma linha do conjunto de resultados.
# .fetchmany(n): Recupera linhas do conjunto de resultados "n"
# .fetchall(): Recuperar todas as linhas de banco de dados em uma lista de tuplas.
# iter(cursor): Permite iterar sobre o conjunto de resultados linha por linha.

'''
# print(cursor.fetchone())

# print(cursor.fetchmany(3))

# print(cursor.fetchall())

# Consultar toda da tabela SQLite
for linha in iter(cursor):
    _id, nome, peso = linha
    print(_id, nome, peso)
print()

# ---------------------------------------------------------
# Consultar (id = 3) na tabela SQLite
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)
linha = cursor.fetchone()
print(*linha)
# ---------------------------------------------------------

cursor.close() # Fechar variável de controle
connection.close() # Fechar conexão com arquivo