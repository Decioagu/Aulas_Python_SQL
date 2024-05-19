# video aula 393
import sqlite3

from caminho import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE) # conectar o arquivo (criar)
cursor = connection.cursor() # variável de controle

# Consultar toda da tabela SQLite
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}' # "*" todos os dados (_id, nome, peso)
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
sql = (f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = ?'
)
dados = ("3")
cursor.execute(sql, dados)

linha = cursor.fetchone()
# linha = cursor.fetchmany(5)
# linha = cursor.fetchall()
print(*linha)
# ---------------------------------------------------------

cursor.close() # Fechar variável de controle
connection.close() # Fechar conexão com arquivo

