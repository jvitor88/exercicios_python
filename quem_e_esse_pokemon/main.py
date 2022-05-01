from mysql.connector import connect
from classes_e_funcoes import *
import random

cabeca()
alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ltipo = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']
ltipo2 = ['None', 'Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']
lgen = [1, 2, 3, 4, 5, 6]
levo = ['Bebe', 'Basico', 'Estagio 1', 'Estagio 2']
# Variáveis de testes lógicos
okteste = False
okteste1 = False
okteste2 = False
okteste3 = False
okteste4 = False
okteste5 = False
# Condição principal
while True:
    if okteste3 == False:
        test3 = random.choice(lgen)
        perg3 = input(f'Seu pokemon é da {test3}ª geração? [S/N]: ').strip().lower()[0]
        if perg3 == 's':
            gen = test3
            okteste3 = True
        if perg3 == 'n':
            lgen.remove(test3)
    if okteste == False:
        test = random.choice(alfa)
        perg = input(f'Seu pokemon começa com a letra {test}? [S/N]:  ').strip().lower()[0]
        if perg == 's':
            pletra = test
            okteste = True
        if perg == 'n':
            alfa.remove(test)
    if okteste1 == False:
        test1 = random.choice(ltipo)
        perg1 = input(f'O tipo principal do seu pokemon é {test1}? [S/N]: ').strip().lower()[0]
        if perg1 == 's':
            type1 = test1
            okteste1 = True
        if perg1 == 'n':
            ltipo.remove(test1)
    if okteste4 == False:
        perg4 = input(f'Seu Pokemon é Lendário? [S/N]: ').strip().lower()[0]
        if perg4 == 's':
            lend = 1
            okteste4 = True
        else:
            lend = 0
            okteste4 = True
    if okteste5 == False:
        test5 = random.choice(levo)
        perg5 = input(f'A evolução seu Pokemon está no {test5}? [S/N]: ').strip().lower()[0]
        if perg5 == 's':
            evo = test5
            okteste5 = True
        if perg5 == 'n':
            levo.remove(test5)
    if okteste == True and okteste1 == True and okteste5 == True and okteste3 == True and okteste4 == True:
        break
# Concxão ao banco
conexao = connect(
    passwd='root',
    port=3306,
    user='root',
    host='localhost',
    database='mundo_pokemon'
)

# Query
sql = f'''select * from base_pokemons
where P_LETRA = '{pletra}' and
TYPE_1 = '{type1}' and
GERACAO = '{gen}' and
EST_EVOL = '{evo}' and
LENDARIO = '{lend}';
'''

cursor = conexao.cursor()
cursor.execute(sql)

# Resultado da query
achei = cursor.fetchall()

conexao.close()

linha()
# Selecionando a informação a ser mostrada na tela
copia = achei[0]
resp = copia[1]

print(f'{achei}')
# Resultado
'''
print(f'Você está pensando no {achei}?')
# Finalização
final = input('SIM OU NÃO? ').strip().lower()[0]
if final == 's':
    print('OBRIGADO VOLTE SEMPRE!')
else:
    print('DESCULPE, TENTE NOVAMENTE...')
'''