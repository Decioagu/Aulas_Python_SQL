# video aula 395
import sqlite3
from pathlib import Path


# Caminho
ROOT_DIR = Path(__file__).parent / 'BD'
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'cliente'

connection = sqlite3.connect(DB_FILE) # conectar o arquivo (criar)
cursor = connection.cursor() # variável de controle

# ---------------------------------------------------------
# Consultar toda da tabela SQLite
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

# Consultar toda da tabela SQLite
for linha in iter(cursor):
    _id, nome, peso = linha
    print(_id, nome, peso)
print()
# ---------------------------------------------------------

# Deletar "id = 7" da tabela SQLite
sql = (
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = ?'
)
dados = ("7")
cursor.execute(sql, dados)
print('========================================================================')
# ---------------------------------------------------------
# Consultar toda da tabela SQLite
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

# Consultar toda da tabela SQLite
for linha in iter(cursor):
    _id, nome, peso = linha
    print(_id, nome, peso)
# ---------------------------------------------------------
connection.commit() # adicionar comando na tabela
cursor.close() # Fechar variável de controle
connection.close() # Fechar conexão com arquivo

