from mysql.connector import connect

conexao = connect(
    passwd='root',
    port=3306,
    user='root',
    host='localhost',
    database='mundo_pokemon'
)

# query
sql = f'''select * from base_pokemons
'''

cursor = conexao.cursor()
cursor.execute(sql)

# resultado da query
achei = cursor.fetchall()

conexao.close()

print(achei)