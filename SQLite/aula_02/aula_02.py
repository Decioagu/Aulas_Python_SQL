# video aula 389
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent / 'BD'
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
print(DB_FILE)
TABLE_NAME = 'cliente'

# Cria o diretório se não existir
ROOT_DIR.mkdir(parents=True, exist_ok=True)

# https://www.sqlite.org/doclist.html
# https://www.techonthenet.com/sqlite/index.php
connection = sqlite3.connect(DB_FILE) # conectar o arquivo (criar)
cursor = connection.cursor() # variável de controle

# Inserir valores nas colunas da tabela tabela SQLite (UTILIZAR MÉTODO CONFORME aula_04)
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(id, nome, peso) '
    'VALUES '
    '(NULL, "Helena", 4), '
    '(NULL, "Eduardo", 10)'
)

connection.commit() # adicionar comando na tabela
cursor.close() # Fechar variável de controle
connection.close() # Fechar conexão com arquivo

# https://dbeaver.io/download/ (instalar banco de dados)