from mysql.connector import connect

conexao = connect(
    passwd='root',
    port=3306,
    user='root',
    host='localhost',
    database='mundo_pokemon'
)

# Query
sql = f'''select * from base_pokemons
where P_LETRA = '{letra}' and
TYPE_1 = '{tipo}' and
GERACAO = '{geracao}' and
EST_EVOL = '{evo}' and
LENDARIO = '{lend}';
'''

cursor = conexao.cursor()
cursor.execute(sql)

# Resultado da query
pokemon = cursor.fetchall()[0]

conexao.close()

print(pokemon)

