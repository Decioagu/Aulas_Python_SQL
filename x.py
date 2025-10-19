import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='decio',
    password='decio123',
    database='banco_docker',  # ou outro banco que você criou
    port=3306                 # ou 3307 se estiver usando Docker com porta mapeada
)

cursor = conexao.cursor()
cursor.execute("SELECT DATABASE();")
print(cursor.fetchone())

conexao.close()
