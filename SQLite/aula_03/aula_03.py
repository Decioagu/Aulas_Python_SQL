# video aula 389
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent / 'BD'
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
print(DB_FILE)
TABLE_NAME = 'cliente'

# https://www.sqlite.org/doclist.html
# https://www.techonthenet.com/sqlite/index.php
connection = sqlite3.connect(DB_FILE) # conectar o arquivo (criar)
cursor = connection.cursor() # variável de controle


# Limpar TODOS os valores na tabela SQLite
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Reiniciar "id" da tabela SQLite
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)


connection.commit() # adicionar comando na tabela
cursor.close() # Fechar variável de controle
connection.close() # Fechar conexão com arquivo

# https://dbeaver.io/download/ (instalar banco de dados)