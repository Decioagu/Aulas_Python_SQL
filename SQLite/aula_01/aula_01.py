# video aula 388
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent / 'BD'
DB_NAME = 'db.sqlite3' # pode ser usar "nome.db" ou "nome.sqlite3" ou "nome.sqlite"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'cliente'

# Cria o diretório se não existir
ROOT_DIR.mkdir(parents=True, exist_ok=True)

# https://www.sqlite.org/doclist.html
# https://www.techonthenet.com/sqlite/index.php
connection = sqlite3.connect(DB_FILE) # conectar o arquivo (criar)

cursor = connection.cursor() # variável de controle (abrir conexão)

# Criar tabela e colunas SQLite
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
    ')'
)
# cursor.executemany() # executa varias tarefa na tabela 

connection.commit() # adicionar comando na tabela
cursor.close() # Fechar variável de controle
connection.close() # Fechar conexão com arquivo

# https://dbeaver.io/download/ (instalar banco de dados)

# CRUD - Create  Read    Update  Delete
# SQL  - INSERT  SELECT  UPDATE  DELETE