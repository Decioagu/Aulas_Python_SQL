# video aula 390 até 392
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent / 'BD'
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
print(DB_FILE)
TABLE_NAME = 'cliente'

# https://www.sqlite.org/doclist.html
# https://www.techonthenet.com/sqlite/index.php
connection = sqlite3.connect(DB_FILE) # conectar o arquivo (criar)
cursor = connection.cursor() # variável de controle

# Inserir valores nas colunas da tabela tabela SQLite
sql_01 = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, peso) '
    'VALUES '
    '(?,?)' # lista ou tupla
)
# multiplos elementos
cursor.executemany(sql_01, [('Décio', 81.3), ('Luana', 61.7), ('Ana Rosa', 21.53)]) 

# Inserir valores nas colunas da tabela tabela SQLite
sql_02 = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, peso) '
    'VALUES '
    '(:_nome, :_peso)' # dicionario
)
# multiplos elementos
cursor.executemany(sql_02, [{'_nome': 'Mara', '_peso' : 75.1}, {'_nome': 'Fabio', '_peso' : 45.3}])

connection.commit() # adicionar comando na tabela
cursor.close() # Fechar variável de controle
connection.close() # Fechar conexão com arquivo

# https://dbeaver.io/download/ (instalar banco de dados)